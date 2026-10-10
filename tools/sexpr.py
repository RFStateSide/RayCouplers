import re,json
class Quoted(str): pass
def parse(text):
 stack=[];root=None
 for t in re.findall(r'\(|\)|"(?:\\.|[^"\\])*"|[^\s()]+',text):
  if t=='(':
   n=[]
   if stack:stack[-1].append(n)
   stack.append(n)
  elif t==')':root=stack.pop()
  else:stack[-1].append(Quoted(json.loads(t)) if t.startswith('"') else t)
 return root
def items(x,k):return [n for n in x if isinstance(n,list) and n and n[0]==k]
def node(x,k):return next(n for n in x if isinstance(n,list) and n and n[0]==k)
def get(x,k,default=None):
 ns=items(x,k);return ns[0][1] if ns else default
def props(x):return {n[1]:n[2] for n in items(x,'property')}
def setprop(x,k,v):
 ns=[n for n in items(x,'property') if n[1]==k]
 if ns:ns[0][2]=Quoted(str(v))
 else:
  p=props(x);base=items(x,'at');at=base[0][1:3] if base else ['0','0']
  x.append(['property',Quoted(k),Quoted(str(v)),['at',*at,'0'],['effects',['font',['size','1.27','1.27']],['hide','yes']]])
def dump(x,depth=0):
 if not isinstance(x,list):return json.dumps(str(x),ensure_ascii=False) if isinstance(x,Quoted) else str(x)
 atoms=[];children=[]
 for n in x:
  (children if isinstance(n,list) else atoms).append(n)
 head='('+' '.join(dump(n) for n in atoms)
 if not children:return head+')'
 return head+'\n'+'\n'.join('\t'*(depth+1)+dump(n,depth+1) for n in children)+'\n'+'\t'*depth+')'
def walk(x):
 if isinstance(x,list):
  yield x
  for n in x:yield from walk(n)
def canonical(x):
 if not isinstance(x,list):return str(x)
 if x and x[0] in ['uuid','tstamp']:return None
 return [v for n in x if (v:=canonical(n)) is not None]
