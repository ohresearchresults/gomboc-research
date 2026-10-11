"""Round only free controls, solve every chart contact rationally, audit the body.
This preserves true non-simple hull incidence; rounding support normals directly
would define a different combinatorial body and is not used here.
"""
import pathlib,json,sys,math,hashlib,subprocess,numpy as np,gmpy2
from audit_integer import run as audit
from audit_persistence import run as bars
sys.set_int_max_str_digits(0);R=gmpy2.mpq

def solve(A,b):
    n=len(b);M=[list(row)+[v] for row,v in zip(A,b)]
    for k in range(n):
        j=next((j for j in range(k,n) if M[j][k]),None)
        if j is None:raise ValueError('singular rational contact reconstruction')
        M[k],M[j]=M[j],M[k];s=M[k][k];M[k]=[v/s for v in M[k]]
        for j in range(n):
            if j!=k:
                s=M[j][k];M[j]=[v-s*w for v,w in zip(M[j],M[k])]
    return [row[-1] for row in M]

def run(source,input,out,D=10**15):
    source=pathlib.Path(source);input=pathlib.Path(input);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);meta=json.loads((source/'chart.json').read_text())
    if input.suffix=='.json':
        controls=json.loads(input.read_text());D=int(controls['grid']);ints=[int(v) for v in controls['integers']]
    else:
        dat=np.load(input);z=dat['z'] if 'z' in dat else dat['q'];ints=[int(round(float(v)*D)) for v in z]
    assert D>0 and len(ints)==meta['free_coordinates']
    q=[R(v,D) for v in ints];A=[None]*meta['nodes'];done=set()
    for p in meta['plan']:
        i=p['node'];deps=p['deps'];axes=p['axes'];v=[R(0)]*3
        for axis,j in zip(p['free_axes'],p['free_indices']):v[axis]=q[j]
        assert set(deps)<=done
        if deps:
            mat=[[A[j][k] for k in axes] for j in deps];rhs=[1-sum(A[j][k]*v[k] for k in range(3)) for j in deps]
            for k,x in zip(axes,solve(mat,rhs)):v[k]=x
        A[i]=tuple(v);done.add(i)
        assert all(sum(a*b for a,b in zip(A[i],A[j]))==1 for j in deps)
    F=meta['F'];H=[]
    for row in A[:F]:
        d=math.lcm(*(int(x.denominator) for x in row));H.append([int(x*d) for x in row]+[d])
    for f,cy in enumerate(meta['faces']):
        contact=set(cy)
        for i,v in enumerate(A[F:]):
            value=sum(a*b for a,b in zip(A[f],v))
            assert (value==1) if i in contact else (value<1)
    (out/'H.json').write_text(json.dumps({'H':H},separators=(',',':')));(out/'free_controls.json').write_text(json.dumps(dict(grid=D,integers=ints),separators=(',',':')));(out/'chart.json').write_bytes((source/'chart.json').read_bytes());(out/'source.json').write_text(json.dumps(dict(chart_source=str(source.resolve()),numerical_input=str(input.resolve()),numerical_sha256=hashlib.sha256(input.read_bytes()).hexdigest()),indent=2));a=audit(H)
    assert (a['V'],a['E'],a['F'])==(meta['V'],meta['E'],meta['F'])
    expected=set(A[F:]);actual={tuple(R(x) for x in v) for v in a['raw_vertices']};assert expected==actual
    (out/'audit.json').write_text(json.dumps(a,separators=(',',':')));print('EXACT_CONTACT_ATLAS_BODY',{k:a[k] for k in ['V','E','F','C','counts','weak','primitive_zero']},flush=True);subprocess.run([sys.executable,'certify_boundedness.py',str(out/'H.json'),str(out/'boundedness.json')],check=True);bars(out/'audit.json',out/'bars.json');manifest={p.name:dict(bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in out.iterdir() if p.is_file()};(out/'manifest.json').write_text(json.dumps(manifest,indent=2))

if __name__=='__main__':run(sys.argv[1],sys.argv[2],sys.argv[3],int(sys.argv[4]) if len(sys.argv)>4 else 10**15)
