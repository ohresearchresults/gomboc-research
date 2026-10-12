# material-8da989165096

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Exact free two/three-link endpoint audit on both C616 deletions

## Established result and scope
For the exact homogeneous filled CONDITION25 DELETE99 and DELETE117 bodies, at their OWN volume centroids, the unwanted unstable vertex has NO positive one-link, two-link, or three-link path to ANY existing vertex, even when all intermediate points are completely free in R^3. This is a fixed-endpoint, fixed-center geometric exclusion, not a global deformation exclusion and not an edge-complexity lower bound. Moving either endpoint or the body's own centroid, using a longer path, or changing the body remains possible.

DELETE99 is V174/E308/F136,C616,strict121/weak000, bad raw-lex144, desired apex94. DELETE117 has the same V/E/F,C and equilibrium class, bad79, desired apex92. Exact tests enumerated all174 endpoint labels separately on each body. Both produced one/two/three-link target counts0/0/0. In particular all three tests are false for DELETE99 endpoints128,145,94 and DELETE117 endpoints76,82,92. Thus the previously proposed two-link paths144->128->145 and79->76->82 cannot succeed merely by moving their intermediate point with the current endpoints and center fixed. This strengthens, but does not replace, the mutual-arrow cycle correction.

## Mathematical criterion
For centered nonzero endpoints u,z write A=u.u,B=z.z,C=u.z. A positive escape link x->y means x.(y-x)>0. For a path of n links, every successive radius increases and every successive angular separation is less than pi/2. If R=|z|/|u| and phi=angle(u,z), summing spherical angular distances and applying convexity of log(sec(theta)) gives the sharp free-path criterion phi/n<pi/2 and R*cos(phi/n)^n>1. Sufficiency follows from equally spaced directions along a shortest great-circle arc and a common radial ratio R^(1/n). This statement permits arbitrary free intermediate points; it imposes no polyhedral incidence constraints.

For two links, completing a square gives |y-z/2|^2<B/4 and u.y>A, so existence is equivalent to C+sqrt(AB)>2A. In common integer centered coordinates P_i/D, set alpha=P_bad.P_bad,beta=P_j.P_j,gamma=P_bad.P_j and K=max(0,2alpha-gamma). The exact test is alpha*beta>K^2.

For three links, necessarily B>A. Set R=sqrt(B/A),s=R^(1/3)*cos(phi/3). When R>8, s>1 for every phi<=pi. Otherwise cos(phi/3)>=1/2 places s on the increasing branch of 4s^3-3R^(2/3)s=C/A, and comparison with s=1 yields (4A-C)^3<27A^2B. The exact integer test is beta>alpha and [beta>64alpha or (4alpha-gamma)^3<27alpha^2beta]. All acceptance comparisons in the audit are integer comparisons; displayed relative discriminants are supplementary binary64 summaries.

## Complete recovery closure and commands
All exact coordinate inputs are already preserved by the standalone CONDITION25 ALL THREE source materials [internal-source-reference],[internal-source-reference],[internal-source-reference], with respective SHA25620469536cc4461b597cd92b9c7420b89ad4f1efd82ef72aa4f934b9bb772067a,a527d91c2ba70ee5220ca4b6ba30964e804fd4fa52a8619d3ae6567608cc8087,ecb59180686fbea53343e4b78e64b70478df5ede3679acd200c163185c1e29d4. Decode their24-file dictionary into source/. The complete MAKE_DELETION_INPUTS.py in [internal-source-reference] (material SHA c3e7fc3cef5a2c1fc3d3d7d20930add743d579643fc221381905ae6834960581) reconstructs the two exact reports. No originating sandbox or additional worker result is required.

Run python -B -S MAKE_DELETION_INPUTS.py. Expected terminal BOTH_EXACT_DELETION_INPUTS_RESTORED and inputs del99_exact/A.json310157bytes SHAaf5e1884bf301785a618928bf9ccbd44e965391ee964fd24f7e4cdf0cdaac85d; del117_exact/A.json309887bytes SHA3832d35b39b5e70cef5c21cfdd3cc5bb91985ba376324574200ddd287eb48446. Both were reconstructed with the expected bytes and hashes in the producing coordinator turn.

Save the complete code below with its final newline as FREE_PATH_ENDPOINT_AUDIT.py,3380bytes SHA7b10c3c26832b9dd74cb5a8d5abf0dd665b2b12abd1f9c26dec5b73be60df326. Run python -B -S FREE_PATH_ENDPOINT_AUDIT.py --out FREE_PATH_ENDPOINT_REPORT.json. CPython3.13.5,standard library only,assertions enabled. Expected terminal TWO_DELETIONS_EXACT_FREE_PATH_ENDPOINT_AUDIT_PASS. The report69770bytes SHA0d319ed3707597cffd08fbf3233b4f9e7e320473595c47ec44e6c67c887f4793 includes all exact-predicate booleans, target lists, pinned source hashes, and supplementary floating relative discriminants. This command completed and terminal/bytes/hash were observed. No new polyhedron is promoted by this audit.

### FREE_PATH_ENDPOINT_AUDIT.py
```python
"""Exact two/three-link free-path feasibility at the OWN filled centroid.
Input hashes pin two exact CONDITION25 C616 nonwinner bodies. A common integer
centered realization avoids square roots and contains no rounded geometry.
Free path feasibility does not establish incidence or convexity compatibility.
"""
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
assert __debug__
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
H=lambda b:hashlib.sha256(b).hexdigest()
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def rational_bridge(u,z):
 A=dot(u,u);BB=dot(z,z);C=dot(u,z);L=max(F(0),2-C/A);m=0
 while True:
  t=L+F(1,2**m)
  if A*t*t<BB:break
  m+=1
 y=[(b+t*a)/2 for a,b in zip(u,z)];m1=dot(u,[b-a for a,b in zip(u,y)]);m2=dot(y,[b-a for a,b in zip(y,z)]);assert m1>0 and m2>0
 return dict(t=str(t),dyadic_offset_exponent=m,centered_middle=list(map(str,y)),escape_margins=[str(m1),str(m2)])
def main():
 p=argparse.ArgumentParser();p.add_argument('--workspace',type=Path,default=Path('.'));p.add_argument('--out',type=Path,required=True);a=p.parse_args();out={}
 for name,bad,selected,sha in [('del99_exact',144,[128,145,94],'af5e1884bf301785a618928bf9ccbd44e965391ee964fd24f7e4cdf0cdaac85d'),('del117_exact',79,[76,82,92],'3832d35b39b5e70cef5c21cfdd3cc5bb91985ba376324574200ddd287eb48446')]:
  rb=(a.workspace/name/'A.json').read_bytes();assert H(rb)==sha;r=json.loads(rb);assert r['counts']==[1,2,1] and r['weak']==[0,0,0];X=[list(map(F,row)) for row in r['raw_vertices']];g=list(map(F,r['raw_centroid']));D=math.lcm(*(v.denominator for row in X+[g] for v in row));P=[[int((v-c)*D) for v,c in zip(row,g)] for row in X];assert all(F(p,D)==v-c for pp,row in zip(P,X) for p,v,c in zip(pp,row,g));u=P[bad];A=dot(u,u);assert A>0;rows=[]
  for j,z in enumerate(P):
   BB=dot(z,z);C=dot(u,z);K=max(0,2*A-C);q2=A*BB-K*K;two=q2>0;three=BB>A and (BB>64*A or (4*A-C)**3<27*A*A*BB);direct=C>A
   row=dict(target=j,direct=direct,two_links=two,three_links=three,relative_B_minus_A=(BB-A)/A,relative_two_link_discriminant=q2/(A*A),relative_C=C/A)
   if j in selected and two:
    # Use the same exact common denominator; keep a literal rational bridge.
    row['free_bridge']=rational_bridge([F(v,D) for v in u],[F(v,D) for v in z])
   rows.append(row)
  ans=dict(input_report_sha256=sha,VEF=[r[k] for k in ['V','E','F']],own_counts=r['counts'],bad=bad,selected_targets=selected,common_centered_denominator_bits=D.bit_length(),one_link_targets=[x['target'] for x in rows if x['direct']],two_link_targets=[x['target'] for x in rows if x['two_links']],three_link_targets=[x['target'] for x in rows if x['three_links']],selected=[x for x in rows if x['target'] in selected],all_endpoint_tests=rows,scope='Exact free intermediate-point feasibility with endpoints and own center fixed, not a polyhedral construction or deformation exclusion.')
  out[name]=ans;print('EXACT_FREE_PATH_ENDPOINT_COUNTS',name,len(ans['one_link_targets']),len(ans['two_link_targets']),len(ans['three_link_targets']),[(x['target'],x['two_links'],x['three_links']) for x in ans['selected']],flush=True)
 receipt=dict(marker='TWO_DELETIONS_EXACT_FREE_PATH_ENDPOINT_AUDIT_PASS',bodies=out);a.out.write_bytes(B(receipt));print(receipt['marker'],len(B(receipt)),H(B(receipt)),flush=True)
if __name__=='__main__':main()
```
