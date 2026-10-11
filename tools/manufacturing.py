"""Export/check one common preliminary fabrication package. Python standard library only."""
from pathlib import Path
import argparse,collections,hashlib,json,os,subprocess,shutil,zipfile,math
from sexpr import *
from cam import gerber,drill
ROOT=Path(__file__).resolve().parents[1]
ID='P3-prep-01';PACKAGE=ROOT/'manufacturing/release'/ID
PCB=ROOT/'hardware/common/RayCouplers.kicad_pcb'
CLI=os.environ.get('KICAD_CLI',r'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe')
LAYERS=['F_Cu','B_Cu','F_Mask','B_Mask','F_Silkscreen','B_Silkscreen','F_Paste','B_Paste','Edge_Cuts']
ZIP=PACKAGE/('RayCouplers-CommonPCB-'+ID+'-manufacturing.zip')
CHECKDIR=ROOT/'validation/phase3';CHECKDIR.mkdir(parents=True,exist_ok=True)
SOURCE_HASH_POLICY='sha256-utf8-lf-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def source_sha(p):
 # Canonical source bytes only: validate UTF-8, replace CRLF with LF, retain all other bytes.
 data=p.read_bytes();data.decode('utf8');data=data.replace(b'\r\n',b'\n')
 if b'\r' in data:raise ValueError('Unsupported bare CR in source')
 return hashlib.sha256(data).hexdigest()
def run(args,name):
 r=subprocess.run([CLI,*args],capture_output=True,text=True);(CHECKDIR/(name+'.log')).write_text(r.stdout+r.stderr,encoding='utf8');assert r.returncode==0,name+r.stderr

def expected_drills(board):
 result=[(*map(float,node(v,'at')[1:3]),float(get(v,'drill'))) for v in items(board,'via')]
 for f in items(board,'footprint'):
  at=node(f,'at');x,y=map(float,at[1:3]);angle=math.radians(float(at[3]) if len(at)>3 else 0)
  for p in items(f,'pad'):
   if not items(p,'drill'):continue
   assert p[2]=='thru_hole','Unexpected NPTH introduced'
   px,py=map(float,node(p,'at')[1:3]);result.append((x+px*math.cos(angle)+py*math.sin(angle),y-px*math.sin(angle)+py*math.cos(angle),float(get(p,'drill'))))
 return result

def compare(a,b):return {'shared':sum((a&b).values()),'reference_only':sum((a-b).values()),'release_only':sum((b-a).values())}

def check_geometry():
 b=parse(PCB.read_text(encoding='utf8'));parsed={l:gerber((PACKAGE/('RayCouplers-'+l+'.gbr')).read_text(encoding='utf8')) for l in LAYERS}
 edges=parsed['Edge_Cuts']['shapes'];assert sum(edges.values())==12
 edgepoints={xy for s in edges for xy in [s[3],s[4]]}
 assert edgepoints=={(int(x*1e6),int(-y*1e6)) for x,y in [(65,87),(135,87),(135,189),(65,189),(90,92),(110,92),(110,122),(90,122),(90,132),(110,132),(110,162),(90,162)]}
 hits=drill((PACKAGE/'RayCouplers-PTH.drl').read_text());np=drill((PACKAGE/'RayCouplers-NPTH.drl').read_text());native=expected_drills(b)
 assert len(hits)==len(native)==244 and not np
 remaining=hits.copy()
 for n in native:
  ix=next((i for i,h in enumerate(remaining) if max(abs(a-c) for a,c in zip(n,h))<.002),None);assert ix is not None,n;remaining.pop(ix)
 assert not remaining
 assert sorted((x,y) for x,y,d in hits if d==3.2)==[(72,91),(72,185),(128,91),(128,185)]
 for f in items(b,'footprint'):
  if props(f)['Reference'] not in ['D1','D2']:continue
  ref=str(props(f)['Reference']);at=node(f,'at');x,y=map(float,at[1:3]);angle=math.radians(float(at[3]) if len(at)>3 else 0)
  for p in items(f,'pad'):
   number=str(p[1]);assert get(p,'pinfunction')==('K' if number=='1' else 'A');assert node(p,'size')[1:]==['1.2','1.2'];px,py=map(float,node(p,'at')[1:3]);point=(round((x+px*math.cos(angle)+py*math.sin(angle))*1e6),round(-(y-px*math.sin(angle)+py*math.cos(angle))*1e6))
   for layer in ['F_Cu','F_Mask','F_Paste']:
    flashes=[a for a,xy,attrs in parsed[layer]['flashes'] if xy==point and (attrs.get('C')==ref or attrs.get('P','').split(',')[0]==ref)];assert len(flashes)==1,(ref,layer,point)
    ap=flashes[0];assert ap[0]=='RoundRect';v=list(map(float,ap[1].split('X')));assert abs((max(v[1:9:2])-min(v[1:9:2])+2*v[0])-1.2)<.00001;assert abs((max(v[2:9:2])-min(v[2:9:2])+2*v[0])-1.2)<.00001
 assert sum(parsed['B_Paste']['shapes'].values())==2
 assert all(a[:2]==('R','6.000000X6.000000') and attrs.get('C') in ['T1','T2'] for a,xy,attrs in parsed['B_Paste']['flashes'])
 summary={'package':ID,'source':'hardware/common/RayCouplers.kicad_pcb','source_sha256':source_sha(PCB),'source_hash_policy':SOURCE_HASH_POLICY,'gerbers':{l:sum(d['shapes'].values()) for l,d in parsed.items()},'outline_mm':[70,102],'internal_openings_mm':[[20,30],[20,30]],'plated_hits':244,'nonplated_hits':0,'drill_diameters_mm':dict(collections.Counter(d for x,y,d in hits)),'mounting_holes':4,'diode_pads':'SOD-123, 1.2 x 1.2 mm on copper/mask/paste, pin 1 K / pin 2 A','physical_fabrication_test':'NOT PERFORMED','clearance_acceptance':'0.2 mm retained geometry; not strictly 8 mil; fabricator CAM acceptance required'}
 # Historical comparison retains macro and arc structure; no claim of bitmap equivalence.
 history=list((ROOT/'manufacturing/historical/2kw').rglob('W764321ASZ24_RayCoupler.kicad_pcb_gerber.zip'))
 if history:
  with zipfile.ZipFile(history[0]) as z:
   summary['historical_primitive_comparison']={}
   for l in LAYERS:
    suffix=l.replace('Silkscreen','SilkS');name='RayCoupler-'+suffix+'.gbr'
    if name in z.namelist():summary['historical_primitive_comparison'][l]=compare(gerber(z.read(name).decode())['shapes'],parsed[l]['shapes'])
 # Re-exported accepted PCB diagnostics allow comparison against the owner-accepted native geometry.
 accepted=CHECKDIR/'accepted-gerbers'
 if accepted.exists():
  summary['phase2_geometry_comparison']={l:compare(gerber((accepted/('accepted-200w-'+l+'.gbr')).read_text())['shapes'],parsed[l]['shapes']) for l in LAYERS}
  assert all(d['reference_only']==d['release_only']==0 for d in summary['phase2_geometry_comparison'].values())
 return summary

def export():
 PACKAGE.mkdir(parents=True,exist_ok=True)
 run(['pcb','export','gerbers','--layers',','.join(l.replace('_','.') if l not in ['Edge_Cuts','F_Silkscreen','B_Silkscreen'] else {'Edge_Cuts':'Edge.Cuts','F_Silkscreen':'F.Silkscreen','B_Silkscreen':'B.Silkscreen'}[l] for l in LAYERS),'--no-protel-ext','--subtract-soldermask','-o',str(PACKAGE)+os.sep,str(PCB)],'gerber-export')
 run(['pcb','export','drill','--format','excellon','--excellon-units','mm','--excellon-separate-th','--generate-map','--map-format','svg','-o',str(PACKAGE)+os.sep,str(PCB)],'drill-export')
 job=PACKAGE/'RayCouplers-job.gbrjob';j=json.loads(job.read_text());j['GeneralSpecs']['Size']={'X':70,'Y':102};j['GeneralSpecs']['ProjectId']['Revision']=ID;job.write_text(json.dumps(j,indent=2)+'\n',encoding='utf8')
 for src,dest in [(ROOT/'docs/fabrication.md',PACKAGE/('RayCouplers-CommonPCB-'+ID+'-fabrication.md')),(ROOT/'LICENSE',PACKAGE/'LICENSE'),(ROOT/'NOTICE',PACKAGE/'NOTICE')]:shutil.copy2(src,dest)
 summary=check_geometry();(CHECKDIR/'manufacturing-check.json').write_text(json.dumps(summary,indent=2),encoding='utf8')
 (PACKAGE/'RayCouplers-drill-report.txt').write_text('RayCouplers common PCB '+ID+'\nPlated holes: 244; non-plated drilled holes: 0. Internal openings are routed Edge.Cuts, not drill hits.\n'+''.join(f'{d:.3f} mm: {n} plated hits\n' for d,n in sorted(summary['drill_diameters_mm'].items()))+'Four 3.2 mm grounded plated mounting holes retained. No slots.\n',encoding='utf8')
 payload={p.name:sha(p) for p in PACKAGE.iterdir() if p.is_file() and p.name not in [ZIP.name,'manifest.json','SHA256SUMS.txt']}
 manifest={'identifier':ID,'preparation_date':'2026-10-10','kicad':subprocess.check_output([CLI,'version'],text=True).strip(),'source':'hardware/common/RayCouplers.kicad_pcb','source_sha256':source_sha(PCB),'source_hash_policy':SOURCE_HASH_POLICY,'export_settings':'X2 Gerber, mm 4.6 absolute; legend minus mask; separate PTH/NPTH metric decimal absolute Excellon; SVG maps','job_metadata_adjustments':'Nominal outline 70 x 102 mm from centerlines; revision P3-prep-01','status':'Engineering preparation; retained clearance rule requires CAM acceptance; not physically fabricated/tested','files':payload}
 (PACKAGE/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf8')
 with zipfile.ZipFile(ZIP,'w',zipfile.ZIP_DEFLATED) as z:
  for name in sorted([*payload,'manifest.json']):z.write(PACKAGE/name,name)
 (PACKAGE/'SHA256SUMS.txt').write_text(''.join(sha(p)+'  '+p.name+'\n' for p in sorted(PACKAGE.iterdir()) if p.is_file() and p.name!='SHA256SUMS.txt'),encoding='utf8')
 check()

def check():
 summary=check_geometry();m=json.loads((PACKAGE/'manifest.json').read_text());assert m.get('source_hash_policy')==SOURCE_HASH_POLICY,'Unsupported source fingerprint policy'
 assert m['source_sha256']==source_sha(PCB),'Stale export: canonical source hash changed'
 for name,h in m['files'].items():assert sha(PACKAGE/name)==h,name
 expected=set(m['files'])|{'manifest.json'}
 with zipfile.ZipFile(ZIP) as z:
  assert set(z.namelist())==expected and len(z.namelist())==len(expected) and z.testzip() is None
  for name in expected:assert z.read(name)==(PACKAGE/name).read_bytes(),name
 assert {p.name for p in PACKAGE.iterdir() if p.is_file()}==expected|{ZIP.name,'SHA256SUMS.txt'},'Unexpected/stale package file'
 for line in (PACKAGE/'SHA256SUMS.txt').read_text().splitlines():
  h,name=line.split('  ',1);assert sha(PACKAGE/name)==h,name
 summary['zip_sha256']=sha(ZIP);summary['zip_members']=len(expected);summary['manifest_archive_integrity']='PASS';(CHECKDIR/'manufacturing-check.json').write_text(json.dumps(summary,indent=2),encoding='utf8');print(json.dumps(summary,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--export',action='store_true');p.add_argument('--check',action='store_true');a=p.parse_args()
 if a.export:export()
 elif a.check:check()
 else:p.error('Choose --export or --check')
