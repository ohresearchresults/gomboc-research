# material-0b2838e30401

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Exact necessary normal-root filter: 34 of58 W51 directions excluded

## Claim and scope
For polyhedra retaining the Euclidean facet-normal directions of the literal W51_ROBUST_G3 seed, 34 of58 directions cannot host the sole stable facet of a strict own-uniform-volume-centroid S1 body without weak equilibria, regardless of positive support heights or redundant input planes. The two baseline stable directions, original rows[4,30,31] and[10,29,30], are lexicographic facet indices16,31; neither is excluded. This is not whole-family impossibility, not a 110 body, and not invariant under changes of normal directions or physical metric.
Exact parent figure-0537 was fully read, SHA256 05577e4a0b36b334bf63e1fd41ffdbb8b9c663892f7da776c851bf47acf7af21. It supplies the literal 32 rows/1000 below (one interior), exact own211 seed V31/E87/F58 C174. Normals here are reconstructed by exhaustive rational support-plane enumeration, not numerical hull data.

## Proof
For a 3-polytope K with uniform-volume centroid0, decompose K into tetrahedra sharing any vertex v. Their centroids are (v+a+b+c)/4. Volume-weighted averaging gives 0=(v+3z)/4 with z in K, hence -v/3 in K. Convexification gives -K/3 subset K. Polarity yields -Q/3 subset Q for Q=K polar.
Write q_i=y_i N_i for polar vertices, N_i nonzero rational outward normal representatives and y_i=1/h_i>0. Scale so the unique radial-maximum root r has y_r=1. Absence of any other strict or weak radial maximum gives every nonroot actual polar vertex a chord to a vertex j with q_i dot(q_j-q_i)>0. Squared radius strictly increases; iteration terminates at r. Such an arc implies Ni dot Nj>0 and y_i<a_ij*y_j for a_ij=(Ni dot Nj)/(Ni dot Ni).
Let z_r=1 and z_i be the maximum product of a along positive-angle paths i to r. Nontrivial cycle products are <1, because norm factors telescope and the remaining product consists of cosines of distinct directions. A maximum-product Dijkstra algorithm is rational when priorities are z_i^2*(Ni dot Ni). The verifier additionally checks all exact Bellman inequalities z_i>=a_ij*z_j and selected-parent equalities; thus all paths are dominated independently of algorithm trust. Every actual q_i lies in [0,z_i Ni], so Q subset L_r=conv(0,{z_i Ni}). Any rational separator w with w dot(-Nr/3)>max(0,max_i z_i*w dot Ni) contradicts -Nr/3 in Q. All34 integer separators below pass strictly. Redundant planes enlarge the outer envelope and do not invalidate the necessity.
The centroid-asymmetry lemma is classical; see Lemma6,p4 of Naszodi,Pach,Swanepoel, Arrangements of homothets of a convex body, arXiv1608.04639v3. The proof here is self-contained. The new method combines it with the full rooted-chord path envelope.

## Recovery
Save the Python block verbatim with LF and final newline as exact_normal_root_filter.py. Python3.11.8 stdlib only. No floating calculation, seed, tolerance or numerical solver enters verification.
Run: python exact_normal_root_filter.py > normal_root_filter_report.json
Then: sha256sum exact_normal_root_filter.py normal_root_filter_report.json
Source5521bytes SHA256 77e750a210e936bafdd137a5e616daad5ce49540e5f909375e824dcb2a7e1492.
Output45584bytes SHA256 8c647cc8e56a446acebae437ae6d3b75939af0f3a526c6d1ee2b5886ff3bdfb3.
Markers EXACT_NORMAL_ROOT_FILTER_PASS=true,excluded=34,total=58,normal_sha256=fed749fd4ac7693e044900c19fcab2a014ecd2c1a16061081efdbdf4f887de26. Max envelope fraction bits856. Root order is lexicographic original material-row maximal-facet tuples, not the canonical auditor numbering.

```python
"""Exact necessary root exclusion for W51 fixed facet-normal directions.
Complete verifier uses only Python stdlib. All inequalities are rational.
Separators were proposed numerically, but no floating-point operation enters this verifier.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations
from math import gcd
import json,argparse,hashlib
from pathlib import Path

POINTS=[[-2678,-1136,975],[-2745,-769,406],[-2212,-627,45],[96,-637,-245],[465,1184,-402],[80,119,-1160],[294,781,-935],[157,537,-1075],[311,1098,-580],[681,814,-815],[565,-379,-1032],[883,11,-962],[947,461,-856],[1007,793,-634],[840,1037,-473],[1206,848,-369],[1174,1065,103],[1389,818,-95],[1535,736,189],[1603,668,465],[1571,172,-108],[1639,563,721],[1644,425,972],[1609,244,1244],[1506,4,1547],[1301,-295,1859],[970,-604,2131],[548,-896,2304],[78,-1126,2365],[-418,-1288,2323],[-968,-1386,2170],[-1604,-1391,1853]]

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def exact_normals(points=POINTS):
    facets={}
    for ids in combinations(range(len(points)),3):
        a,b,c=(points[i] for i in ids);n=cross(sub(b,a),sub(c,a))
        if not any(n):continue
        d=[dot(n,sub(p,a)) for p in points]
        if min(d)<0<max(d):continue
        if min(d)==max(d)==0:raise ValueError('not three dimensional')
        if min(d)>=0:n=tuple(-x for x in n)
        gg=gcd(gcd(abs(n[0]),abs(n[1])),abs(n[2]));n=tuple(x//gg for x in n)
        face=tuple(i for i,p in enumerate(points) if dot(n,sub(p,a))==0)
        facets[face]=n
    labels=sorted(facets);return labels,[facets[k] for k in labels]

def envelope(normals,root):
    """Exact maximum path products a_ij=(Ni.Nj)/(Ni.Ni), including root's empty path."""
    n=len(normals);n2=[dot(a,a) for a in normals]
    z=[F(0)]*n;z[root]=F(1);par=[-1]*n;seen=set()
    for _ in range(n):
        k=max((i for i in range(n) if i not in seen),key=lambda i:z[i]*z[i]*n2[i])
        if z[k]==0:break
        seen.add(k)
        for i in range(n):
            if i in seen:continue
            a=dot(normals[i],normals[k])
            if a<=0:continue
            cand=z[k]*F(a,n2[i])
            if cand>z[i]:z[i]=cand;par[i]=k
    if len(seen)!=n:raise ValueError('positive-angle graph disconnected')
    # Bellman inequalities prove domination of EVERY path, not only the selected ones.
    for i in range(n):
        for j in range(n):
            a=dot(normals[i],normals[j])
            if a>0:assert z[i]>=F(a,n2[i])*z[j]
    for i in range(n):
        if i!=root:assert par[i]>=0 and z[i]==F(dot(normals[i],normals[par[i]]),n2[i])*z[par[i]]
    return z,par

def certify(root,w,normals):
    z,par=envelope(normals,root)
    target=-F(dot(w,normals[root]),3)
    dots=[z[i]*dot(w,ni) for i,ni in enumerate(normals)]
    bound=max([F(0)]+dots);gap=target-bound
    return gap, {'root':root,'separator':list(w),'contact':dots.index(bound) if bound in dots else -1,'gap':str(gap),'tree':par,'max_fraction_bits':max(max(a.numerator.bit_length(),a.denominator.bit_length()) for a in z)}

SEPARATORS=[(5, [5627221, -46789130, 100622019]), (7, [5627221, -46789130, 100622019]), (8, [8441777, -70184892, 150932419]), (9, [72490659, -399644247, 913799530]), (10, [38926423, -345399790, 937647972]), (11, [-375446698, -484622968, 790050857]), (12, [-556042031, -483258991, 676223342]), (17, [-250105864, -462677074, 850515715]), (18, [-215447367, -457967337, 862466434]), (19, [-294028843, -468175161, 833282100]), (20, [-375446698, -484622968, 790050857]), (21, [-294028843, -468175161, 833282100]), (22, [-250105864, -462677074, 850515715]), (23, [-375446698, -484622968, 790050857]), (24, [-558824205, -467996817, 684612655]), (25, [-111461285, -95291749, 135999502]), (26, [-954519403, -212503627, 209128951]), (33, [-814457314, -373206079, 444270757]), (34, [-271435769, -124681089, 147947154]), (35, [-814457314, -373206079, 444270757]), (36, [-556892246, -478710174, 678754445]), (37, [-566511561, -481390190, 668825938]), (38, [-404393761, -201104930, 214528537]), (39, [-209644502, -90076055, 102154232]), (40, [-836711563, -388279954, 386202586]), (41, [-836506726, -390595738, 384306475]), (42, [-835854649, -397446161, 378660210]), (50, [-209644502, -90076055, 102154232]), (51, [-838763612, -356096241, 411911483]), (52, [-949783145, -232119675, 209839067]), (53, [-950477161, -229348493, 209743738]), (54, [-951354733, -225796344, 209619136]), (55, [-476338037, -110170884, 104711273]), (56, [-318074103, -71261959, 69725958])]

def main():
    labels,normals=exact_normals()
    assert len(normals)==58
    rows=[]
    for root,w in SEPARATORS:
        gap,row=certify(root,w,normals)
        assert gap>0
        row['labels']=list(labels[root]);rows.append(row)
    roots=[r['root'] for r in rows]
    assert len(roots)==len(set(roots))==34
    report={'EXACT_NORMAL_ROOT_FILTER_PASS':True,'excluded':34,'total':58,
      'scope':'fixed W51 ROBUST_G3 Euclidean facet-normal directions; own strict S1 and no weak equilibria',
      'root_order':'lexicographic original material-row maximal-facet tuples',
      'remaining_roots_not_excluded':[i for i in range(58) if i not in roots],
      'normal_sha256':hashlib.sha256(json.dumps(normals,separators=(',',':')).encode()).hexdigest(),
      'certificates':rows}
    print(json.dumps(report,sort_keys=True,indent=2))

if __name__=='__main__':main()
```
