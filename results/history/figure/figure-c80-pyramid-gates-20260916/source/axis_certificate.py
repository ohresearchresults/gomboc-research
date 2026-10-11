"""Exact complete diagonal one-axis affine-orbit S/U classification.
For t>0 the linear map scales coordinate axis by sqrt(t). The centre is the
actual filled-volume centroid, transformed with the body. No H count is inferred.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
def enc(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def regions(X,axis,polar):
 result=[]
 for i,p in enumerate(X):
  lo=F(0);hi=None;empty=False;constraints=[]
  for j,q in enumerate(X):
   if i==j:continue
   ab=p[axis]*(q[axis]-p[axis]);rest=sum(p[k]*(q[k]-p[k]) for k in range(3) if k!=axis)
   a,b=(rest,ab) if polar else (ab,rest);constraints.append([str(a),str(b),j])
   if a==0:
    if b>=0:empty=True
   else:
    c=-b/a
    if a>0:hi=c if hi is None else min(hi,c)
    else:lo=max(lo,c)
  if hi is not None and hi<=lo:empty=True
  result.append({'index':i,'lower':str(lo),'upper':None if hi is None else str(hi),'strict_empty':empty,'linear_tests':constraints})
 return result
def census(regions,t):
 strict=[];weak=[]
 for r in regions:
  v=[F(a)*t+F(b) for a,b,j in r['linear_tests']]
  if max(v)<0:strict.append(r['index'])
  elif max(v)==0:weak.append(r['index'])
 return strict,weak
def main():
 p=argparse.ArgumentParser();p.add_argument('audit');p.add_argument('out');p.add_argument('--axis',type=int,default=1,choices=[0,1,2]);a=p.parse_args();b=Path(a.audit).read_bytes();A=json.loads(b);g=list(map(F,A['raw_centroid']));X=[[F(v)-c for v,c in zip(p,g)] for p in A['raw_vertices']];Q=[]
 for n,h in zip(A['normals'],A['offsets']):
  nn=list(map(F,n));hh=F(h)-dot(nn,g);assert hh>0;Q.append([v/hh for v in nn])
 R={'S':regions(Q,a.axis,True),'U':regions(X,a.axis,False)}
 knots={F(0)}
 # Include every potential sign event, also for empty strict regions: isolated
 # weak equilibria must not be missed just because their open interval is empty.
 for rs in R.values():
  for r in rs:
   for c,d,j in r['linear_tests']:
    c,d=F(c),F(d)
    if c and -d/c>0:knots.add(-d/c)
 knots=sorted(knots);cells=[]
 def test(t,kind,left,right):
  ss,sw=census(R['S'],t);uu,uw=census(R['U'],t)
  row={'kind':kind,'lower':str(left),'upper':None if right is None else str(right),'sample':str(t),'S':ss,'U':uu,'S_weak_only':sw,'U_weak_only':uw}
  row['excluded_own110_weak000']=len(ss)!=1 or len(uu)!=1 or bool(sw) or bool(uw)
  cells.append(row)
 for i,t in enumerate(knots):
  if t>0:test(t,'boundary',t,t)
  end=knots[i+1] if i+1<len(knots) else None;test((t+end)/2 if end is not None else t+1,'open',t,end)
 assert all(c['excluded_own110_weak000'] for c in cells)
 # Compress adjoining ordinary sign cells with identical equilibrium lists.
 summary=[]
 for row in cells:
  key={k:row[k] for k in ['S','U','S_weak_only','U_weak_only']}
  if summary and summary[-1]['census']==key:summary[-1]['last']=row['upper'];summary[-1]['last_kind']=row['kind'];summary[-1]['cells']+=1
  else:summary.append({'first':row['lower'],'last':row['upper'],'first_kind':row['kind'],'last_kind':row['kind'],'census':key,'cells':1})
 out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
 (out/'CERTIFICATE.json').write_bytes(enc({'input_sha256':hashlib.sha256(b).hexdigest(),'axis':a.axis,'regions':R,'cells':cells,'summary':summary,'claim':'NO_OWN110_WEAK000_IN_COMPLETE_POSITIVE_AXIS_STRETCH_ORBIT'}))
 print('EXACT_COMPLETE_AXIS_ORBIT_EXCLUSION_PASS',a.axis,'positive_knots',len(knots)-1,'cells',len(cells),'summary_pieces',len(summary))
 for x in summary:
  z=x.copy();z['first_approx']=float(F(x['first']));z['last_approx']=None if x['last'] is None else float(F(x['last']));print(json.dumps(z),flush=True)
 for f in out.iterdir():b=f.read_bytes();print(f.name,len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':main()
