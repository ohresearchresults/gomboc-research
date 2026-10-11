#!/usr/bin/env python3
"""Deterministically regenerate the exact M42 three-nonsimplicial-cell endpoint.

Coordinates are rational on one 10^-36 lattice. The three ordinary first
moments are solved by the exact dependent translation tau=-M/V. The full hull
and mechanics are reconstructed independently by verify_exact_cleanroom.py.
"""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
import argparse,csv,json,hashlib,subprocess,sys
R=Path(__file__).resolve().parent;S=10**36;K=10**24
ABSORB={134,180,181,199,218,219}|set(range(143,153))
CSTAR=(-22638817877*K,9862693840*K,-7081176048*K)
NEW={220:(2498667797393*K,-2884051905141*K,-865392654376*K),221:(2866953149070*K,-6660906984580*K,-1535167851984*K),222:(3712882082663*K,-5945040770195*K,-825500569466*K)}
def dot(a,b):return sum(a[k]*b[k] for k in range(3))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def qs(x):return f'{x.numerator}/{x.denominator}'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default='regenerated');ap.add_argument('--skip-independent-verify',action='store_true');args=ap.parse_args();out=(R/args.output_dir).resolve();out.mkdir(parents=True,exist_ok=True)
 rows={}
 with open(R/'predecessor_two_cell_coordinates.csv') as f:
  for r in csv.DictReader(f):
   i=int(r['source_id']);assert int(r['denominator'])==S;rows[i]=(int(r['x_num']),int(r['y_num']),int(r['z_num']))
 assert len(rows)==131
 for i in ABSORB:rows[i]=CSTAR
 rows.update(NEW)
 cert=json.load(open(R/'certificate.json'));active=set(cert['active_rows']);cycles=json.load(open(R/'face_cycles.json'))
 with open(out/'coordinates_all_exact.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['source_id','x_num','y_num','z_num','denominator','x_exact','y_exact','z_exact','active','lineage'])
  for i in sorted(rows):
   p=rows[i];lin=('third_cell_absorbed_packet' if i in ABSORB else ('third_cell_apex_'+str(i) if i in NEW else 'two_cell_predecessor_input'));w.writerow([i,*p,S,*[qs(Q(z,S)) for z in p],int(i in active),lin])
 D6=0;M=[0,0,0]
 for c in cycles:
  for j in range(1,len(c)-1):
   a,b,z=(rows[i] for i in (c[0],c[j],c[j+1]));d=det(a,b,z);D6+=d
   for k in range(3):M[k]+=d*(a[k]+b[k]+z[k])
 assert D6>0;V=Q(D6,6*S**3);C=tuple(Q(M[k],4*D6*S) for k in range(3));Mom=tuple(Q(M[k],24*S**4) for k in range(3));assert all(Mom[k]-V*C[k]==0 for k in range(3));assert qs(V)==cert['volume_exact'];assert [qs(z) for z in C]==cert['centroid_unshifted_exact']
 with open(out/'coordinates_active_centered.csv','w',newline='') as f:
  w=csv.writer(f);w.writerow(['source_id','x_exact','y_exact','z_exact','x_decimal','y_decimal','z_decimal','radius_squared_exact','radius_squared_decimal'])
  for i in sorted(active):
   p=tuple(Q(rows[i][k],S)-C[k] for k in range(3));r2=sum(z*z for z in p);w.writerow([i,*map(qs,p),*[format(float(z),'.18g') for z in p],qs(r2),format(float(r2),'.18g')])
 assert sha(out/'coordinates_all_exact.csv')==sha(R/'coordinates_all_exact.csv');assert sha(out/'coordinates_active_centered.csv')==sha(R/'coordinates_active_centered.csv')
 if not args.skip_independent_verify:subprocess.run([sys.executable,str(R/'verify_exact_cleanroom.py')],check=True)
 print('PASS deterministic exact M42 three-cell coordinate generator');print('inputs',len(rows),'active',len(active),'volume',qs(V));print('centroid',*[qs(z) for z in C]);print('centered moments 0/1 0/1 0/1')
if __name__=='__main__':main()
