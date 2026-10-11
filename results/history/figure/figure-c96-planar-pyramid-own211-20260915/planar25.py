"""Exact orthogonal planar-base coalescence of the C138 integer25 body."""
import hashlib,json,sys
from pathlib import Path
from exact_points import encoded,make
sys.set_int_max_str_digits(0)
def main():
 b=Path(sys.argv[1]).read_bytes();assert hashlib.sha256(b).hexdigest()=='1be5293390fbabf8b86b02805771d0fed82fddd2c61678b58d36c7bab9f93cd8';P=json.loads(b)['points'];n=(4,11,0);nn=sum(t*t for t in n);Y=[]
 for i,p in enumerate(P):
  d=sum(p[j]*n[j] for j in range(3));Y.append([nn*p[j]-(d*n[j] if i!=15 else 0) for j in range(3)])
 shift=[sum(p[j] for p in Y)//len(Y) for j in range(3)];Y=[[p[j]-shift[j] for j in range(3)] for p in Y];raw=make(Y);sys.path.insert(0,str(Path(sys.argv[2]).resolve()));import check_A,check_B,centred_mass
 A=check_A.run(raw);B=check_B.run(raw);assert A==B;M=centred_mass.run(A);out=Path(sys.argv[3]);out.mkdir(exist_ok=False)
 for f,o in [('POINTS.json',{'object':'COORD_C96_PLANAR24_PYRAMID_OWN211','points':sorted(Y)}),('raw.json',raw),('A.json',A),('B.json',B),('MASS.json',M)]:
  b=encoded(o);(out/f).write_bytes(b);print(f,len(b),hashlib.sha256(b).hexdigest(),flush=True)
 print('C138_PLANAR_BASE_AB_MASS_PASS',A['V'],A['E'],A['F'],A['counts'],A['weak'],flush=True);print('SHIFT',shift,'FACES',sorted(map(len,A['faces'])),'ROOTS',A['stable_face_ids'],A['unstable_vertices'],A['saddle_edges'],'BITS',M,flush=True)
if __name__=='__main__':main()
