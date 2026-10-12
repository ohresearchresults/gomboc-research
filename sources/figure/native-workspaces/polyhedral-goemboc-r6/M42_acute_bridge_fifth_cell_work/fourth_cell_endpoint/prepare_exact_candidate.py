#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as Q
import csv,json,math,sys
import numpy as np
ROOT=Path('/mnt/data/m42_fourth_cell_exact')
SRC=Path('/mnt/data/m42_fourth_work')
PAR=SRC/'parent'
sys.path.insert(0,str(PAR))
from numeric_hull_proposer import evaluate,score_target

x=np.array(json.load(open(SRC/'lobe911_robust_x.json'))['x'],float)
D=10**12
qrat=lambda z: Q(int(round(float(z)*D)),D)
# exact parent unshifted rows and exact parent centroid
pcert=json.load(open(PAR/'certificate.json'))
C=tuple(Q(z) for z in pcert['centroid_unshifted_exact'])
raw={}
with open(PAR/'coordinates_all_exact.csv') as f:
    for r in csv.DictReader(f):
        raw[int(r['source_id'])]=tuple(Q(r[k])-C[j] for j,k in enumerate(('x_exact','y_exact','z_exact')))
# Float frame exactly matching search family closely.
ALLf={i:np.array([float(z) for z in p]) for i,p in raw.items()}
axis=ALLf[153]/np.linalg.norm(ALLf[153])
tmp=np.array([0.,0.,1.])
if abs(axis@tmp)>.9:tmp=np.array([1.,0.,0.])
e1=np.cross(axis,tmp);e1/=np.linalg.norm(e1);e2=np.cross(axis,e1);e2/=np.linalg.norm(e2)
base=evaluate(ALLf,plane_tol=1e-8,strict_tol=1e-12)
bf=next(f for f in base.faces if set(f['cycle'])==set(range(17)))
BN,BOFF=bf['n'],bf['off']
ABSORB={130,153,154,176,182,201,220,221,222}
# Rational global controls.
gfac=[qrat(math.exp(x[j])) for j in (9,10,11)]
u=tuple(qrat(x[j]) for j in (12,13,14))
L=((qrat(math.exp(x[15])),qrat(x[17]),qrat(x[18])),
   (Q(0),qrat(math.exp(x[16])),qrat(x[19])),
   (Q(0),Q(0),qrat(math.exp(-x[15]-x[16]))))

def dot(a,b):return sum(a[i]*b[i] for i in range(3))
def mat(A,p):return tuple(sum(A[i][j]*p[j] for j in range(3)) for i in range(3))
def transform(p):
    den=Q(1)-dot(u,p)
    assert den>Q(8,100),(float(den),p)
    return mat(L,tuple(z/den for z in p))

pre={i:p for i,p in raw.items()}
for i in ABSORB:pre[i]=(Q(0),Q(0),Q(0))
# exact new pre-transform rows from rounded floating geometric construction
k=0
a1,delta,r1,r2,twist=x[k:k+5];k+=5
t1,t2,as1,as2=x[k:k+4];k+=4
c1=a1*axis+t1*e1+t2*e2;c2=(a1+delta)*axis+t1*e1+t2*e2
newf={}
for j in range(3):
    th=2*math.pi*j/3
    rr=r1*(1+as1*math.cos(th)+as2*math.sin(th))
    newf[223+j]=c1+rr*(math.cos(th)*e1+math.sin(th)*e2)
for j in range(3):
    th=2*math.pi*j/3+twist
    rr=r2*(1-as1*math.cos(th)+as2*math.sin(th))
    newf[226+j]=c2+rr*(math.cos(th)*e1+math.sin(th)*e2)
for i in range(223,229):
    slack=float(newf[i]@BN+BOFF)
    if slack>-0.03:newf[i]=newf[i]-(slack+0.03)*BN
    pre[i]=tuple(qrat(z) for z in newf[i])
# per-group exact radial scaling
for fac,g in zip(gfac,(range(155,176),range(183,199),range(202,218))):
    for i in g:
        if i in pre:pre[i]=tuple(fac*z for z in pre[i])
# global exact projective + linear transformation; this preserves protected base coplanarity exactly
rows={i:transform(p) for i,p in pre.items()}
# numeric audit
rf=evaluate({i:np.array([float(z) for z in p]) for i,p in rows.items()},plane_tol=1e-8,strict_tol=1e-10)
assert rf.valid,rf.error
print('EXACT-TRANSFORM NUMERIC',len(rows),len(rf.active),len(rf.edges),len(rf.faces),(len(rf.stable),len(rf.unstable),len(rf.saddles)),rf.centroid,rf.volume)
print('stable',[(rf.faces[i]['cycle'],d) for i,d in rf.stable])
print('unstable',rf.unstable);print('saddles',rf.saddles);print('score',score_target(rf))
# exact input output
with open(ROOT/'input_rows_exact.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['source_id','x_exact','y_exact','z_exact','lineage'])
    for i in sorted(rows):
        lin='parent_exact_global_transform'
        if i in ABSORB:lin='absorbed_parent_packet'
        elif 223<=i<=225:lin='prism_near_section'
        elif 226<=i<=228:lin='prism_far_section'
        w.writerow([i,*[str(z) for z in rows[i]],lin])
con={
 'version':2,'source':'exact rationalization of robust macroscopic triangular-prismatic lobe; common rational projective/linear map preserves protected 17-gon exactly',
 'parent':'../m42_three_cell_exact/coordinates_all_exact.csv','absorbed_rows':sorted(ABSORB),'new_rows':list(range(223,229)),
 'search_parameters_binary64':[float(z).hex() for z in x],
 'rational_group_scales':[str(z) for z in gfac],
 'rational_projective_u':[str(z) for z in u],
 'rational_linear_map':[[str(z) for z in row] for row in L],
 'new_pretransform_rows':{str(i):[str(z) for z in pre[i]] for i in range(223,229)},
 'exact_rule':'center every parent input by its exact parent ordinary-volume centroid; absorb listed rows at 0; scale three listed groups; apply q->q/(1-u.q); apply L. New pretransform rows are literal rationals.'
}
json.dump(con,open(ROOT/'construction.json','w'),indent=2)
