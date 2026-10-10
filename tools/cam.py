"""Parse the KiCad-generated Gerber subset used here; reject unknown drawing commands.
Geometry counters include aperture definitions, regions, linear/arc interpolation and polarity.
This is a focused export check, not a general CAM engine or fabrication acceptance tool.
"""
import re,collections

def gerber(text):
 assert '%MOMM*%' in text and '%FSLAX46Y46*%' in text and text.rstrip().endswith('M02*')
 apertures={};macros={};macro=None;buf=[];ap=None;pos=(0,0);region=None;pol='D';mode='G01';shapes=[];flashes=[];attrs={}
 for raw in text.splitlines():
  l=raw.strip()
  if macro:
   buf.append(l)
   if l.endswith('%'):macros[macro]='\n'.join(buf);macro=None
   continue
  m=re.match(r'%AM([^*]+)\*',l)
  if m:macro=m[1];buf=[l];continue
  m=re.fullmatch(r'%ADD(\d+)([^,]+)(?:,(.*))?\*%',l)
  if m:
   typ=m[2];assert typ in ['C','R','O','P'] or typ in macros,typ
   apertures[m[1]]=(typ,m[3] or '',macros.get(typ,''));continue
  m=re.fullmatch(r'%TO\.([^,]+),(.*)\*%',l)
  if m:attrs[m[1]]=m[2];continue
  if l=='%TD*%':attrs={};continue
  m=re.fullmatch(r'D(\d+)\*',l)
  if m:ap=apertures[m[1]];continue
  if l in ['G01*','G02*','G03*']:mode=l[:-1];continue
  if l=='G36*':assert region is None;region=[];continue
  if l=='G37*':assert region is not None;shapes.append(('region',pol,tuple(region)));region=None;continue
  if l in ['%LPC*%','%LPD*%']:pol=l[3];continue
  m=re.fullmatch(r'(?:X(-?\d+))?(?:Y(-?\d+))?(?:I(-?\d+))?(?:J(-?\d+))?D0([123])\*',l)
  if m:
   new=tuple(int(v) if v is not None else pos[i] for i,v in enumerate(m.group(1,2)));op=m[5];ij=tuple(int(v or 0) for v in m.group(3,4))
   if region is not None:region.append((mode,op,new,ij))
   elif op=='3':assert ap is not None;shapes.append(('flash',pol,ap,new));flashes.append((ap,new,dict(attrs)))
   elif op=='1':assert ap is not None;shapes.append(('line' if mode=='G01' else mode,pol,ap,pos,new,ij))
   pos=new;continue
  if not l or l.startswith('G04') or l.startswith('%TF.') or l.startswith('%TA.') or l.startswith('%TD.') or l in ['%MOMM*%','%FSLAX46Y46*%','G75*','M02*']:continue
  raise ValueError('Unsupported Gerber command: '+l)
 assert macro is None and region is None
 return {'shapes':collections.Counter(shapes),'flashes':flashes,'apertures':apertures}

def drill(text):
 tools={};tool=None;hits=[];metric='METRIC' in text;assert 'M48' in text and 'M30' in text and metric
 for l in text.splitlines():
  m=re.fullmatch(r'T(\d+)C([\d.]+)',l)
  if m:tools[m[1]]=float(m[2]);continue
  m=re.fullmatch(r'T(\d+)',l)
  if m:tool=m[1];continue
  m=re.fullmatch(r'X(-?[\d.]+)Y(-?[\d.]+)',l)
  if m:assert tool in tools;hits.append((float(m[1]),-float(m[2]),tools[tool]));continue
  if l.startswith(('X','Y','G85','G00','G01')):raise ValueError('Unsupported drilling command '+l)
 return hits
