"""Focused integrity, connectivity, geometry, population and CAD validation."""
from pathlib import Path
import argparse,json,subprocess,csv,hashlib,os,collections,xml.etree.ElementTree as ET
from sexpr import *
from prepare import ROOT,SCHEMAS,population
CLI=os.environ.get('KICAD_CLI',r'C:\Program Files\KiCad\9.0\bin\kicad-cli.exe')
OUT=ROOT/'validation';OUT.mkdir(exist_ok=True)
def run(args,name):
 r=subprocess.run([CLI,*args],capture_output=True,text=True)
 (OUT/(name+'.log')).write_text(r.stdout+r.stderr,encoding='utf8')
 if r.returncode!=0:raise RuntimeError(name+': '+r.stdout+r.stderr)
def netlist(sch,name):
 p=OUT/(name+'-netlist.xml');run(['sch','export','netlist','--format','kicadxml','-o',str(p),str(sch)],name+'-netlist')
 x=ET.parse(p);return {n.attrib['name']:sorted((a.attrib['ref'],a.attrib['pin']) for a in n.findall('node') if not a.attrib['ref'].startswith('H')) for n in x.findall('./nets/net')}
def geom(board,kind):return collections.Counter(json.dumps(canonical(n),sort_keys=True) for n in items(board,kind))
def verify(portable=False):
 baseline=json.loads((ROOT/'hardware/common/validation-baseline.json').read_text(encoding='utf8'));b=parse((ROOT/'hardware/common/RayCouplers.kicad_pcb').read_text(encoding='utf8'))
 a=['kicad_pcb',*[n for k in ['segment','via','gr_rect'] for n in baseline['geometry'][k]]]
 for k in ['segment','via','gr_rect']:assert geom(a,k)==geom(b,k),k+' geometry changed'
 bf=items(b,'footprint');assert len(bf)==54
 old={uid:['footprint',*[n for nodes in fields.values() for n in nodes]] for uid,fields in baseline['footprints'].items()}
 for f in bf:
  orig=old[str(get(f,'uuid'))]
  for key in ['at','pad','fp_line','fp_arc','fp_poly','fp_circle','fp_rect']:
   assert geom(orig,key)==geom(f,key),str(props(f)['Reference'])+' changed '+key
 holes=[f for f in bf if props(f)['Reference'].startswith('H')];assert sorted(tuple(map(float,node(f,'at')[1:3])) for f in holes)==[(72,91),(72,185),(128,91),(128,185)]
 for f in bf:
  ref=props(f)['Reference']
  if ref in ['D1','D2']:
   assert 'SOD-123' in f[1]
   assert {get(p,'pinfunction') for p in items(f,'pad')}=={'K','A'}
   assert all(node(p,'size')[1:]==['1.2','1.2'] for p in items(f,'pad'))
 originals={v:netlist(ROOT/'archive/original-projects'/v/'RayCoupler.kicad_sch','original-'+v) if (ROOT/'archive/original-projects'/v/'RayCoupler.kicad_sch').exists() else {n:[tuple(z) for z in nodes] for n,nodes in baseline['nets'].items()} for v in SCHEMAS}
 curated={v:netlist(p,'curated-'+v) for v,p in SCHEMAS.items()}
 assert originals['200w']==originals['2kw']==curated['200w']==curated['2kw'],'Electrical connectivity changed'
 values={}
 for v,p in SCHEMAS.items():
  s,inst=population(p);values[v]={r:str(props(i)['Value']) for r,i in inst.items() if not r.startswith('H')}
  rows=list(csv.DictReader((ROOT/'bom'/v/('RayCoupler-'+v+'-population.csv')).open(encoding='utf-8-sig')));seen={}
  for row in rows:
   if row['Category'] not in ['Electrical','PCB feature','Transformer assembly']:continue
   refs=row['References'].split(',');assert len(refs)==int(row['Quantity'])
   for ref in refs:assert ref not in seen;seen[ref]=row['Value'];assert row['Footprint']==props(inst[ref])['Footprint']
  assert seen==values[v] and len(seen)==50
  materials={r['References']:r for r in rows if r['Category']=='Material'}
  assert int(materials['MAT-CORES']['Quantity'])==(2 if v=='200w' else 4)
  assert materials['MAT-CORES']['Manufacturer']=='Fair-Rite' and materials['MAT-CORES']['MPN']=='5943001401'
  assert materials['MAT-WIRE']['Value']=='21 AWG high-temperature enameled copper wire'
  for ref in ['T1','T2']:
   pr=props(inst[ref]);assert pr['Core_MPN']=='5943001401' and pr['Cores_per_transformer']==('1' if v=='200w' else '2') and pr['Winding_Turns']==('16' if v=='200w' else '24')

  run(['sch','erc','--format','json','--units','mm','-o',str(OUT/('erc-'+v+'.json')),str(p)],'erc-'+v)
  run(['pcb','drc','--format','json','--units','mm','--schematic-parity','-o',str(OUT/('drc-'+v+'.json')),str(ROOT/'generated'/v/'RayCouplers.kicad_pcb')],'drc-'+v)
 changes={r:[values['200w'][r],values['2kw'][r]] for r in values['200w'] if values['200w'][r]!=values['2kw'][r]}
 assert set(changes)=={'R1','R2','R3','R4','R5','R6','R7','R8','R11','R12','T1','T2'}
 assert values['2kw']['R23']=='2.7K' and values['2kw']['C1']=='.01 µF' and values['2kw']['C2']=='.01 µF'
 summary={'geometry':'200 tracks, 214 vias, all 54 placements/pads and openings preserved','electrical_connectivity':'30 nets and original 50 electrical references unchanged; H1-H4 added on existing GND','bom_references_per_variant':50,'variant_value_differences':changes,'cad':{}}
 for v in SCHEMAS:
  e=json.loads((OUT/('erc-'+v+'.json')).read_text());vs=[x for sh in e['sheets'] for x in sh['violations']];d=json.loads((OUT/('drc-'+v+'.json')).read_text())
  summary['cad'][v]={'erc':dict(collections.Counter(x['severity'] for x in vs)),'erc_types':dict(collections.Counter(x['type'] for x in vs)),'drc':dict(collections.Counter(x['severity'] for x in d['violations'])),'drc_types':dict(collections.Counter(x['type'] for x in d['violations'])),'unconnected':len(d['unconnected_items']),'parity':len(d['schematic_parity']),'parity_types':dict(collections.Counter(x['type'] for x in d['schematic_parity']))}
  assert not any(x['severity']=='error' for x in d['violations']) and not d['unconnected_items'],'Significant PCB regression'
  assert not d['schematic_parity'],'Schematic/PCB parity regression'
  assert collections.Counter(x['type'] for x in vs if x['severity']=='error')=={'power_pin_not_driven':2,'pin_not_connected':2},'Unexpected ERC error'
 if not portable:
  for root,entry in json.loads((OUT/'source-baseline.json').read_text()).items():
   actual={}
   for base,dirs,names in os.walk(root):
    dirs[:]=[d for d in dirs if d not in ['.git','.pio','build','.qtcreator']]
    for n in names:
     p=Path(base)/n;actual[str(p.relative_to(root))]=hashlib.sha256(p.read_bytes()).hexdigest()
   assert actual==entry['hashes'],'Original source changed: '+root
   if entry['status'] is not None:
    assert subprocess.run(['git','-C',root,'status','--porcelain=v1'],capture_output=True,text=True).stdout==entry['status']
    assert subprocess.run(['git','-C',root,'rev-parse','HEAD'],capture_output=True,text=True).stdout.strip()==entry['head']
 inventory=ROOT/'archive/source-inventory.csv'
 if inventory.exists():
  for row in csv.DictReader(inventory.open(encoding='utf8')):
   if row['preserved_path']:assert hashlib.sha256((ROOT/row['preserved_path']).read_bytes()).hexdigest()==row['sha256']
 elif not portable:raise RuntimeError('Local archive absent; use --portable for a curated repository checkout')
 summary['source_integrity']='PASS: geometry/connectivity baseline checked; available preserved copies checked; external originals/Git not checked in portable mode' if portable else 'PASS: originals, Git status/HEAD, preserved copies unchanged'
 (OUT/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf8');print(json.dumps(summary,indent=2))
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--portable',action='store_true');a=p.parse_args();verify(a.portable)
