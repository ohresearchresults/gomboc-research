# material-00c8fba78bc8

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J124 common-apex exact bodies — Recovery capsule part 1/2

Use BOTH J124_COMMON_APEX_RECOVERY_PART1OF2.md and J124_COMMON_APEX_RECOVERY_PART2OF2.md, plus the complete already immutable exact auditor [internal-source-reference], J115_EXACT_AUDITOR_SOURCE.md, material SHA ac3226f5ae6212be2bedfa4f5797dbd7fa9f4d0f1e3969c3753825a98b9ba4fc. Its complete C++ block is UTF-16 [1442,12480), 11038 bytes, SHA d7fd1244c086a0c5354844cca3453c42b26ed31a55b89720aa9e3987f0a06736. This dependency is preserved, not a missing sandbox. Supply the complete material to a computational successor.

Part 1 gives all reconstruction and extra certificate sources. Part 2 gives every raw integer input, exact nested recipe and the complete input/output/source manifest. Save each named fenced unit with its terminal newline; save the dependency's complete C++ block as exact115.cpp. Run `python replay_j124.py`. Expected terminal marker: J124_SIX_EXACT_NONWINNERS_PASS 6 P6 Q0 weak000 primitive000. Individual six audits and every certificate have actually run. The replay wrapper itself is supplied, not counted as a separate mathematical engine. The reused engine's marker is J115_EXACT_PASS.

Python 3.13.5 and C++17/GMP are used; reconstruction itself is Python stdlib only. No optimizer, old source sandbox or encoded archive is needed for these exact bodies. G6/G8 are ties-to-even raw-parameter grids 10^6/10^8 BEFORE exact incidence projection, not claims about the final normal or centroid denominators. Every input defines a distinct rational body.

All six bodies are own strict121, additionalweak000, primitive000, one positive P and Q[]. None is own110; canonical own110 remains C622.
APEX1_G6: V165/E248/F85, P~.1632721004844304, one degree-four common apex.
APEX2_MATCH_G6: V164/E247/F85, P~.1601784921212976, two degree-four common apices.
APEX2_MATCH_G8: same counts, P~.16017782064342567, distinct finer rational body.
APEX_RELAY_MATCH_G6: V165/E249/F86, P~.1600709699908561, apex degrees five and four.
APEX_RELAY_MATCH_G8: same counts, P~.16007094985607956, distinct finer rational body.
APEX_NESTED_RELAY_G6: V165/E249/F86, P~.16017849212117824. It preserves all85 parent APEX2_MATCH_G6 H rows byte-for-byte and adds just one row; precisely old vertex38 is removed, two vertices added. Exact removed volume is positive, approximately2.4071520913658904e-13; actual centroid displacement is nonzero. At the NEW actual centroid, polar arrows81->85->24 are strictly positive, squared angular guards exceeding655/10^12 and542095357/10^12. The P difference is negative but tiny, not a substantial cancellation. In all five frozen bodies S is input17, a20-gon; both U avoid it. Raw vertex indices vary between bodies.

## freeze_apex.py
```python
"""Deterministic rational freezing of all raw parameters, then exact incidences.
Python stdlib only. The result is a new rational body, not the floating input.
No optimum, path, or class is inferred: run exact115 on the resulting H file.
"""
from fractions import Fraction as F
from pathlib import Path
import json,sys,math,hashlib
sys.set_int_max_str_digits(0)

def solve(A,b):
 n=len(b);r=[list(a)+[v]for a,v in zip(A,b)]
 for j in range(n):
  k=next(i for i in range(j,n)if r[i][j]);r[j],r[k]=r[k],r[j];z=r[j][j];r[j]=[a/z for a in r[j]]
  for i in range(n):
   if i!=j:
    z=r[i][j];r[i]=[a-z*c for a,c in zip(r[i],r[j])]
 return [a[-1]for a in r]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def build(obj):
 D=obj['denominator'];a=[F(v,D)for v in obj['raw_integers']];m=obj['config']['m'];N=[a[3*i:3*i+3]for i in range(m)];A=[a[i:i+3]for i in range(3*m,len(a),3)]
 for ii,ids in obj['config']['row_apices'].items():
  i=int(ii);B=[A[j]for j in ids];w=solve([[dot(v,u)for u in B]for v in B],[1-dot(v,N[i])for v in B]);N[i]=[v+sum(w[j]*B[j][k]for j in range(len(B)))for k,v in enumerate(N[i])]
 for i,ids in obj['config']['row_apices'].items():
  assert all(dot(N[int(i)],A[j])==1 for j in ids)
 rows=[]
 for n in N:
  den=math.lcm(*(v.denominator for v in n));row=[int(v*den)for v in n]+[den];g=math.gcd(*row);rows.append([x//g for x in row])
 return (str(m)+' 0\n'+'\n'.join(' '.join(map(str,r))for r in rows)+'\n').encode(),A

def run(source,prefix,power=8):
 source=Path(source);x=json.loads(source.read_text())
 if 'raw_integers'in x:obj=x
 else:
  D=10**power;obj=dict(denominator=D,raw_integers=[round(F(v)*D)for v in x['raw']],config=x['config'])
 b=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode();Path(prefix+'_INPUT.json').write_bytes(b);h,A=build(obj);Path(prefix+'.txt').write_bytes(h)
 print('EXACT_APEX_INPUT',prefix,len(h),hashlib.sha256(h).hexdigest())
if __name__=='__main__':run(sys.argv[1],sys.argv[2],int(sys.argv[3])if len(sys.argv)>3 else 8)
```

## apex_certificate.py
```python
"""Exact incidence, budget and equilibrium report for a frozen common-apex body.
The complete uniform-mass audit is produced by the supplied exact115 engine.
This wrapper does not turn one engine into independent implementations.
"""
import json,sys,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from freeze_apex import build
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det(a,b,c):return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def run(prefix):
 obj=json.loads(Path(prefix+'_INPUT.json').read_text());h,apices=build(obj);assert h==Path(prefix+'.txt').read_bytes()
 a=json.loads(Path(prefix+'_AUDIT.json').read_text());v=[tuple(map(F,p))for p in a['vertices']];index={p:i for i,p in enumerate(v)}
 rows=[tuple(map(int,l.split()))for l in h.decode().splitlines()[1:]];assert len(rows)==len(set(rows))
 N=[tuple(F(x,r[3])for x in r[:3])for r in rows];active=a['active_input_planes'];edges=[tuple(e)for e in a['edges']];out=[]
 for k,p in enumerate(apices):
  p=tuple(p);assert p in index;i=index[p];ids=obj['config']['apex_rows'][k];assert all(dot(N[j],p)==1 for j in ids)
  assert any(det(N[i0],N[i1],N[i2]) for ii,i0 in enumerate(ids)for jj,i1 in enumerate(ids[ii+1:],ii+1)for i2 in ids[jj+1:])
  degree=sum(i in e for e in edges);incident=[active[j]for j,f in enumerate(a['faces'])if i in f]
  assert degree==len(incident);out.append(dict(apex=k,vertex=i,degree=degree,assigned_inputs=ids,active_incident_inputs=incident,coordinates=[str(t)for t in p]))
 assert len({r['vertex']for r in out})==len(out)
 multiplicities={int(i):len(ids)for i,ids in obj['config']['row_apices'].items()};assert max(multiplicities.values(),default=0)<=3
 m=obj['config']['m'];bound=3*m-6-sum(len(ids)-3 for ids in obj['config']['apex_rows']);assert a['E']<=bound<=249
 assert a['strict']==[1,2,1]and a['weak']==[0,0,0]and a['primitive_zeros']==[0,0,0]and len(a['P'])==1 and not a['Q']
 result=dict(name=prefix,VEF=[a[t]for t in ['V','E','F']],C=2*a['E'],raw_H_count=m,raw_apex_bound=bound,strict=a['strict'],weak=a['weak'],primitive_zeros=a['primitive_zeros'],apices=out,S_input=[active[i]for i in a['S']],U=a['U'],H=a['H'],S_vertex_cycles=[a['faces'][i]for i in a['S']],U_avoids_S=all(u not in a['faces'][i]for u in a['U']for i in a['S']),P_depth_display=[float(F(b['depth']))for b in a['P']],Q=[],volume_display=float(F(a['volume'])),centroid_display=[float(F(x))for x in a['centroid']],exact_audit_sha256=hashlib.sha256(Path(prefix+'_AUDIT.json').read_bytes()).hexdigest(),scope='Exact common-apex incidences and true-edge budget; one reused exact own-mass engine; not own110.')
 b=(json.dumps(result,sort_keys=True,separators=(',',':'))+'\n').encode();Path(prefix+'_CERTIFICATE.json').write_bytes(b)
 print('EXACT_COMMON_APEX_CERTIFICATE_PASS',prefix,result['VEF'],bound,result['P_depth_display'],flush=True)
 return result
if __name__=='__main__':run(sys.argv[1])
```

## nested_relay.py
```python
"""Exact nested coplanar relay through a specified existing physical apex.
Requires only the base raw integer generator, not a floating optimizer.
Normal rows are inherited byte-for-byte; only the final row is new.
"""
from pathlib import Path
from fractions import Fraction as F
import json,sys,math,hashlib
from freeze_apex import build
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def generate(recipe):
 obj=json.loads(Path(recipe['base_input']).read_text());h,A=build(obj);ls=h.decode().splitlines();rows=[list(map(int,s.split()))for s in ls[1:]];N=[tuple(F(v,row[3])for v in row[:3])for row in rows];a=A[recipe['apex']];i,j=recipe['source'],recipe['target'];lam=F(recipe['lambda']);eps=F(recipe['epsilon']);sgn=recipe['orientation'];d=sub(N[j],N[i]);t=cross(a,d);n=tuple((1-lam)*N[i][k]+lam*N[j][k]+sgn*eps*t[k]for k in range(3));assert dot(n,a)==1
 den=math.lcm(*(v.denominator for v in n));row=[int(v*den)for v in n]+[den];g=math.gcd(*row);row=[v//g for v in row];out=(str(len(rows)+1)+' 0\n'+'\n'.join(ls[1:]+[' '.join(map(str,row))])+'\n').encode();return out
if __name__=='__main__':
 recipe=json.loads(Path(sys.argv[1]).read_text());out=generate(recipe);Path(recipe['name']+'.txt').write_bytes(out);print('EXACT_NESTED_RELAY_INPUT',len(out),hashlib.sha256(out).hexdigest())
```

## nested_certificate.py
```python
"""Exact matched-host incidence, nesting, mass and positive-arrow certificate."""
import json,sys,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from nested_relay import generate,dot,sub
sys.set_int_max_str_digits(0)
def run(recipe_path):
 r=json.loads(Path(recipe_path).read_text());name=r['name'];base=r['base_input'].removesuffix('_INPUT.json');h=generate(r);assert h==Path(name+'.txt').read_bytes();oldh=Path(base+'.txt').read_bytes();assert h.decode().splitlines()[1:-1]==oldh.decode().splitlines()[1:]
 old=json.loads(Path(base+'_AUDIT.json').read_text());new=json.loads(Path(name+'_AUDIT.json').read_text());ov=[tuple(map(F,x))for x in old['vertices']];nv=[tuple(map(F,x))for x in new['vertices']];rows=[tuple(map(int,l.split()))for l in h.decode().splitlines()[1:]];N=[tuple(F(x,s[3])for x in s[:3])for s in rows];cut=[i for i,v in enumerate(ov)if dot(N[-1],v)>1];assert len(cut)==1
 vanished=[i for i,v in enumerate(ov)if v not in set(nv)];added=[i for i,v in enumerate(nv)if v not in set(ov)];assert vanished==cut and len(added)==2
 assert [new[t]-old[t]for t in ['V','E','F']]==[1,2,1];assert new['active_input_planes']==list(range(len(rows)))
 assert new['strict']==[1,2,1]and new['weak']==[0,0,0]and new['primitive_zeros']==[0,0,0]and len(new['P'])==1 and not new['Q']
 V0,V1=F(old['volume']),F(new['volume']);g0,g1=[list(map(F,z['centroid']))for z in [old,new]];dm=V0-V1;assert dm>0;dg=sub(g1,g0);assert any(dg);q=[tuple(x/(1-dot(n,g1))for x in n)for n in N];arrows=[]
 for i,j in [(r['source'],len(rows)-1),(len(rows)-1,r['target'])]:
  d=sub(q[j],q[i]);z=dot(q[i],d);assert z>0;square=z*z/(dot(q[i],q[i])*dot(d,d));floor=(square.numerator*10**12)//square.denominator;arrows.append(dict(source=i,target=j,positive=True,squared_angular_floor_1e12=floor))
 out=dict(name=name,parent=base,VEF=[new[t]for t in ['V','E','F']],strict=new['strict'],weak=new['weak'],primitive_zeros=new['primitive_zeros'],nested=True,unchanged_old_H_rows=len(rows)-1,retired_old_vertices=vanished,added_vertex_indices=added,delta_VEF=[1,2,1],removed_volume_display=float(dm),centroid_shift_display=list(map(float,dg)),removed_mass_centroid_display=[float((V0*g0[k]-V1*g1[k])/dm)for k in range(3)],actual_positive_arrows=arrows,P_old_display=float(F(old['P'][0]['depth'])),P_new_display=float(F(new['P'][0]['depth'])),P_difference_sign=(F(new['P'][0]['depth'])>F(old['P'][0]['depth']))-(F(new['P'][0]['depth'])<F(old['P'][0]['depth'])),Q=[],audit_sha256=hashlib.sha256(Path(name+'_AUDIT.json').read_bytes()).hexdigest(),scope='One exact nested two-edge relay with nonzero removed homogeneous mass; not own110 or evidence of a substantial P reduction.')
 Path(name+'_CERTIFICATE.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n');print('EXACT_NESTED_RELAY_CERTIFICATE_PASS',json.dumps(out),flush=True)
if __name__=='__main__':run(sys.argv[1])
```

## replay_j124.py
```python
"""Reconstruct and audit six exact J124 nonwinners from complete inputs.
Place the complete exact115.cpp from [internal-source-reference] here.
No optimizer or originating sandbox is used.
"""
from pathlib import Path
import hashlib,json,subprocess
from freeze_apex import run as freeze
from apex_certificate import run as certify
from nested_relay import generate
from nested_certificate import run as certify_nested

def identity(p):
 b=Path(p).read_bytes();return [len(b),hashlib.sha256(b).hexdigest()]
def main():
 manifest=json.loads(Path('J124_MANIFEST.json').read_text())
 assert identity('exact115.cpp')==[11038,'d7fd1244c086a0c5354844cca3453c42b26ed31a55b89720aa9e3987f0a06736']
 for p in manifest:
  if p.endswith('_INPUT.json')or p.endswith('.py')or p.endswith('_RECIPE.json'):assert identity(p)==manifest[p],p
 subprocess.run(['g++','-O2','-std=c++17','exact115.cpp','-lgmpxx','-lgmp','-o','exact115'],check=True)
 def audit(name):
  with open(name+'.txt','rb')as inp,open(name+'_AUDIT.json','wb')as out,open(name+'_AUDIT.log','wb')as err:subprocess.run(['./exact115'],stdin=inp,stdout=out,stderr=err,check=True)
 names=['APEX1_G6','APEX2_MATCH_G6','APEX2_MATCH_G8','APEX_RELAY_MATCH_G6','APEX_RELAY_MATCH_G8']
 for name in names:freeze(name+'_INPUT.json',name);audit(name);certify(name)
 r=json.loads(Path('NESTED_RELAY_RECIPE.json').read_text());Path(r['name']+'.txt').write_bytes(generate(r));audit(r['name']);certify_nested('NESTED_RELAY_RECIPE.json')
 for p,want in manifest.items():assert identity(p)==want,p
 print('J124_SIX_EXACT_NONWINNERS_PASS 6 P6 Q0 weak000 primitive000')
if __name__=='__main__':main()
```
