"""Exact literal support additions with separate reference and own mass checks."""
import sys,json,hashlib
from pathlib import Path
from math import gcd,lcm
from gmpy2 import mpq as Q
from support_persistence import ROOT
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(ROOT/'sources/full76/decoded/methods/parent'))
import check_B
check_B.Q=Q
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def blob(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()

def run(folder,sample,out,grid=10**14):
    folder=Path(folder);out=Path(out);out.mkdir(parents=True,exist_ok=False)
    meta=json.loads((folder/'source.json').read_text());src=Path(meta['source']);raw=src.read_bytes();assert hashlib.sha256(raw).hexdigest()==meta['sha256'];old=json.loads(raw)
    screen=(folder/'screen.json').read_bytes();row=next(r for r in json.loads(screen)['rows'] if r['sample']==sample)
    rational=lambda x:Q(int(round(float(x)*grid)),grid)
    c=tuple(map(rational,meta['reference_center']));new=[tuple(map(rational,p)) for p in row['new_normals']]
    H=[[*n,h] for n,h in zip(old['normals'],old['offsets'])]
    for y in new:
        h=1+dot(y,c);den=lcm(*(int(v.denominator) for v in (*y,h)));ints=[int(v*den) for v in (*y,h)];d=gcd(*ints);H.append([v//d for v in ints])
    body={'H':H};(out/'H.json').write_bytes(blob(body));(out/'construction.json').write_bytes(blob(dict(source=str(src),source_sha256=hashlib.sha256(raw).hexdigest(),screen=str(folder/'screen.json'),screen_sha256=hashlib.sha256(screen).hexdigest(),sample=sample,grid=grid,reference_point=list(map(str,c)),new_support_normals_at_reference=[[str(x) for x in p] for p in new],old_halfspaces_preserved=True)))
    YY=[tuple(Q(x,Q(h)-dot(n,c)) for x in n) for n,h in zip(old['normals'],old['offsets'])]+new
    signs=[];witness=[]
    for i,y in enumerate(YY):
        vals=[(dot(y,sub(w,y)),j) for j,w in enumerate(YY) if j!=i];v,j=max(vals);signs.append((v>0)-(v<0));witness.append([i,j,str(v)])
    if signs.count(-1)!=1 or 0 in signs:raise ValueError('rounded bridge did not retain reference S1')
    (out/'reference_S1_certificate.json').write_bytes(blob(dict(reference_point=list(map(str,c)),normal_count=len(YY),unique_reference_stable_polar_index=signs.index(-1),positive_escape_witnesses=witness,scope='all normals tested exactly, including inactive supports; this is a reference S1 certificate, not the own-centroid census')))
    r=check_B.run(body);(out/'audit.json').write_bytes(blob(r));summary={k:r[k] for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};summary.update(C2E=2*r['E'],VplusEplusF=r['V']+r['E']+r['F'],audit_sha256=hashlib.sha256(blob(r)).hexdigest(),goal_candidate=(r['counts']==[1,1,0] and r['weak']==[0,0,0] and 17<=r['E']<=248));(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print('EXACT_THALES_BRIDGE',sample,summary,flush=True);return r

if __name__=='__main__':run(ROOT/sys.argv[1],int(sys.argv[2]),ROOT/sys.argv[3])
