"""Regenerate population CSVs and disposable projects; never edit common PCB geometry."""
from pathlib import Path
import argparse,copy,csv,json,shutil
from sexpr import *
ROOT=Path(__file__).resolve().parents[1]
SCHEMAS={'200w':ROOT/'hardware/common/RayCouplers.kicad_sch','2kw':ROOT/'hardware/variants/2kw/RayCouplers.kicad_sch'}
FIELDS=['Variant','Category','References','Quantity','Value','Description','Footprint','Manufacturer','MPN','Supplier','Supplier_PN','Datasheet','Ratings','Population_notes','Sourcing_status']
def population(path):
 s=parse(path.read_text(encoding='utf8'))
 return s,{str(props(i)['Reference']):i for i in items(s,'symbol') if not str(props(i)['Reference']).startswith('#')}
def make_boms():
 for variant,path in SCHEMAS.items():
  s,inst=population(path);rows=[]
  for ref,i in sorted(inst.items()):
   p=props(i)
   if ref.startswith('H'):continue
   assert get(i,'in_bom')=='yes',ref+' excluded from BOM'
   notes='Populate according to selected schematic; sourcing fields are candidates, not stock guarantees'
   if ref in ['T1','T2']:notes=f"Custom assembly: {p['Winding_Turns']} turns, {p['Cores_per_transformer']} Fair-Rite 5943001401 #43 core(s), 21 AWG high-temperature enameled copper wire; cores procured ONLY in Material rows; see construction document for unresolved lead mapping"
   if ref in ['JP1','JP2']:notes='Header plus separate shunt; configure BOTH jumpers: 1-2 for SWR, 2-3 for power interrupt'
   if ref in ['TP1','TP2']:notes='PCB test-point feature; no separately purchased component required'
   if ref in ['D1','D2']:notes='Panjit SOD-123 candidate; pad 1 cathode, pad 2 anode; tested manufacturer unknown'
   rating=str(p.get('Description','')) if ref.startswith(('R','C')) else ('30 V, 200 mA candidate datasheet rating' if ref in ['D1','D2'] else 'See cited datasheet; historical operating rating not independently verified')
   rows.append(dict(zip(FIELDS,[variant,'PCB feature' if ref.startswith('TP') else ('Transformer assembly' if ref in ['T1','T2'] else 'Electrical'),ref,1,p['Value'],p.get('Description',''),p.get('Footprint',''),p.get('MANUFACTURER',''),p.get('MPN',''),p.get('Supplier',''),p.get('Supplier_PN',''),p.get('Datasheet',''),rating,notes,p.get('Sourcing_Status','Unresolved') ])))
  # Group only components with equivalent value/package/sourcing/population information.
  groups={}
  for row in rows:
   key=tuple(str(row[k]) for k in FIELDS if k not in ['References','Quantity'])
   if key in groups:groups[key]['References']+=','+row['References'];groups[key]['Quantity']+=1
   else:groups[key]=row.copy()
  rows=list(groups.values())
  for category,refs,qty,value,desc,notes in [('Mechanical','H1,H2,H3,H4',4,'3.2 mm grounded mounting holes','Plated board features; retained copper pads','Do not purchase as separate electrical components'),('Accessory','ASSY-SHUNTS',2,'2.54 mm removable shunt','One shunt for each JP1/JP2 header','Historical STC02SYAN is a sourcing lead only; verify fit'),('Accessory','ASSY-FASTENERS',4,'M3 mounting fastener positions','Fasteners matched to enclosure/stack height; exact hardware unresolved','Select fasteners/standoffs as needed for four holes; do not infer length/material')]:
   row={k:'' for k in FIELDS};row.update(Variant=variant,Category=category,References=refs,Quantity=qty,Value=value,Description=desc,Population_notes=notes,Sourcing_status='Mechanical fit and sourcing require verification' if category=='Accessory' else 'Existing PCB geometry verified');rows.append(row)
  cores=2 if variant=='200w' else 4
  for refs,qty,value,desc,mfr,mpn,supplier,spn,notes in [
   ('MAT-CORES',cores,'43 toroid','Individual core; 25.4 mm OD x 15.5 mm ID x 8.15 mm height','Fair-Rite','5943001401','DigiKey / Mouser (historical)','Mouser 623-5943001401','Procure this quantity once for BOTH transformer assemblies; do not multiply by T1/T2 assembly quantities'),
   ('MAT-WIRE','','21 AWG high-temperature enameled copper wire','For both T1/T2 windings; length, enamel class, temperature rating and supplier unspecified','','','','','Quantity as needed; established wire gauge and type only'),
   ('MAT-TAPE','','Insulating construction tape','For taped double-core preparation' if variant=='2kw' else 'Optional retention; exact historical material unspecified','','','','','Quantity as needed; manufacturer, thickness, adhesive and rating unspecified')]:
   row={k:'' for k in FIELDS};row.update(Variant=variant,Category='Material',References=refs,Quantity=qty,Value=value,Description=desc,Manufacturer=mfr,MPN=mpn,Supplier=supplier,Supplier_PN=spn,Datasheet='https://fair-rite.com/product/toroids-5943001401/' if refs=='MAT-CORES' else '',Population_notes=notes,Sourcing_status='Established core identity' if refs=='MAT-CORES' else 'Established wire gauge and type' if refs=='MAT-WIRE' else 'Construction consumable specification unresolved');rows.append(row)
  dest=ROOT/'bom'/variant;dest.mkdir(parents=True,exist_ok=True)
  with (dest/('RayCoupler-'+variant+'-population.csv')).open('w',newline='',encoding='utf-8-sig') as f:w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows)
  print(variant,'electrical/test-point references',sum(int(r['Quantity']) for r in rows if r['Category'] in ['Electrical','PCB feature','Transformer assembly']),'grouped rows',len(rows))
def make_projects():
 common=parse((ROOT/'hardware/common/RayCouplers.kicad_pcb').read_text(encoding='utf8'))
 for variant,path in SCHEMAS.items():
  s,inst=population(path);board=copy.deepcopy(common)
  for f in items(board,'footprint'):
   ref=str(props(f)['Reference']);i=inst[ref]
   assert f[1]==props(i)['Footprint'],ref+' footprint mismatch'
   for key,value in props(i).items():
    if key not in ['Reference','Footprint'] and any(p[1]==key for p in items(f,'property')):setprop(f,key,value)
   node(f,'path')[1]=Quoted('/'+str(get(s,'uuid'))+'/'+str(get(i,'uuid')))
  dest=ROOT/'generated'/variant;dest.mkdir(parents=True,exist_ok=True)
  (dest/'RayCouplers.kicad_pcb').write_text(dump(board)+'\n',encoding='utf8')
  shutil.copy2(path,dest/'RayCouplers.kicad_sch');shutil.copy2(path.with_suffix('.kicad_pro'),dest/'RayCouplers.kicad_pro')
  for kind,typ,uri in [('fp','KiCad','RayCouplers.pretty'),('sym','KiCad','RayCouplers.kicad_sym')]:
   (dest/(kind+'-lib-table')).write_text(f'({kind}_lib_table (version 7) (lib (name "RayCouplers")(type "{typ}")(uri "${{KIPRJMOD}}/../../hardware/libraries/{uri}")(options "")(descr "Generated project; edit hardware/common instead")))\n')
 print('Generated disposable variant projects; common PCB unchanged')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--boms',action='store_true');p.add_argument('--projects',action='store_true');a=p.parse_args()
 if a.boms:make_boms()
 if a.projects:make_projects()
 if not a.boms and not a.projects:p.error('Choose --boms and/or --projects')
