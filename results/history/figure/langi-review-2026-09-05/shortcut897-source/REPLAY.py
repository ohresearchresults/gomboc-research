"""Fresh reconstruction, two complete implementations, and mutation fixtures."""
import csv,gzip,json,hashlib,math,os,shutil,subprocess,sys,tempfile,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def manifest():
 rows=json.loads((ROOT/'MANIFEST.json').read_text())
 for name,sha in rows.items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==sha,name
 return len(rows)

def run(args,base=None,expect=True):
 env=dict(os.environ,OPENBLAS_NUM_THREADS='1')
 if base is not None:env['GOMBOC_AUDIT_DIR']=str(base)
 p=subprocess.run([sys.executable,*map(str,args)],env=env,capture_output=True,text=True)
 if expect and p.returncode:raise RuntimeError(p.stdout+p.stderr)
 if not expect:assert p.returncode!=0,'invalid fixture unexpectedly accepted'
 return p

def rows(b,n):
 with gzip.open(b/n,'rt')as f:return [tuple(map(int,r))for r in csv.reader(f)]
def write(b,n,r):
 (b/n).write_bytes(gzip.compress(''.join(','.join(map(str,x))+'\n'for x in r).encode(),mtime=0))
def recenter(b,I,F,D):
 W=0;M=[0,0,0]
 for i,j,k in F:
  a,c,d=I[i],I[j],I[k];t=a[0]*(c[1]*d[2]-c[2]*d[1])+a[1]*(c[2]*d[0]-c[0]*d[2])+a[2]*(c[0]*d[1]-c[1]*d[0]);W+=t
  for q in range(3):M[q]+=t*(a[q]+c[q]+d[q])
 g=math.gcd(4*W,*M);C=4*W//g;B=[x//g for x in M];Q=D*C
 P=[tuple(C*p[j]-B[j]for j in range(3))for p in I]
 write(b,'raw_vertices.csv.gz',I);write(b,'vertices.csv.gz',P);write(b,'triangles.csv.gz',F)
 definition=dict(raw_denominator=D,centred_denominator=str(Q),centroid_multiplier=str(C),centroid_subtract=list(map(str,B)),volume_numerator=str(W),moment_numerators=list(map(str,M)))
 (b/'definition.json').write_text(json.dumps(definition,indent=2))
 return P

def main():
 start=time.time();count=manifest();out={'manifest_entries':count}
 with tempfile.TemporaryDirectory(prefix='gomboc897_exact_')as td:
  td=Path(td);b=td/'literal';run(['-S',ROOT/'EXACT_BODY.py',b]);run(['-S',ROOT/'verify_rational.py',b,'--allpairs']);run([ROOT/'verify_second.py'],b);run(['-S',ROOT/'exact_ascent.py',b])
  r=json.loads((b/'verification_rational.json').read_text());s=json.loads((b/'verification_second.json').read_text());g=json.loads((b/'exact_ascent_graph.json').read_text())
  assert[r[k]for k in ['vertices','true_edges','maximal_faces','C']]==[897,2684,1789,5368]
  assert r['class_SUH']==s['independently_recomputed_exact_equilibrium_class']==[1,1,0]
  assert r['degenerate_equilibria']==r['zero_true_edge_primitives']==0 and g['base_ranks']==[188]*4
  for name in ['raw_vertices.csv.gz','vertices.csv.gz','triangles.csv.gz']:assert rows(b,name)==rows(ROOT,name)
  out.update(first=r,second=s,exact_ascent=g)
  I,F=rows(b,'raw_vertices.csv.gz'),rows(b,'triangles.csv.gz');D=10**14
  t=td/'translation';shutil.copytree(b,t);shift=[17*D,-9*D,5*D];II=[tuple(p[j]+shift[j]for j in range(3))for p in I]
  translated=recenter(t,II,F,D);assert translated==rows(b,'vertices.csv.gz');run(['-S',ROOT/'verify_rational.py',t,'--allpairs']);run([ROOT/'verify_second.py'],t)
  out['exact_translation_invariance']=True;reject=[]
  for kind in ['reversed_triangle','open_surface','corrupt_centred_vertex','corrupt_raw_vertex','false_centroid_multiplier']:
   q=td/kind;shutil.copytree(b,q)
   if kind=='reversed_triangle':FF=list(F);i,j,k=FF[0];FF[0]=(i,k,j);write(q,'triangles.csv.gz',FF)
   elif kind=='open_surface':write(q,'triangles.csv.gz',F[:-1])
   elif kind=='corrupt_centred_vertex':PP=rows(q,'vertices.csv.gz');PP[17]=(PP[17][0]+1,PP[17][1],PP[17][2]);write(q,'vertices.csv.gz',PP)
   elif kind=='corrupt_raw_vertex':II=list(I);II[17]=(II[17][0]+1,II[17][1],II[17][2]);write(q,'raw_vertices.csv.gz',II)
   else:
    dd=json.loads((q/'definition.json').read_text());dd['centroid_multiplier']=str(int(dd['centroid_multiplier'])+1);(q/'definition.json').write_text(json.dumps(dd))
   run(['-S',ROOT/'verify_rational.py',q,'--allpairs'],expect=False);reject.append(kind)
  out['rejected_fixtures']=reject
 assert manifest()==count
 out.update(status='EXACT_SHORTCUT897_PACKAGE_FRESH_REPLAY_PASS',elapsed=time.time()-start)
 dest=Path(sys.argv[1])if len(sys.argv)>1 else ROOT.parent/'SHORTCUT897_FRESH_REPLAY.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(dest);print('elapsed',out['elapsed'])
if __name__=='__main__':main()
