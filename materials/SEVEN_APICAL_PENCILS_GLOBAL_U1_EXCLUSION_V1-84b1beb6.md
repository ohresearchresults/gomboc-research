# material-84b1beb6b412

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# SEVEN_APICAL_PENCILS_GLOBAL_U1_EXCLUSION_V1

Exact coordinator application of the complete analytical theorem APICAL_U1_NORMAL_PARAMETER_COMPACTNESS_V1, [internal-source-reference]. It simplifies the four earlier degree-five exclusions and gives a NEW global exclusion for all three degree-six apical proper-subsystem pencils. No whole-H/f, whole-completion, whole-incidence or proper110 claim follows. Global bounds remain34<=Cmin<=622.

## Exact dependencies — all three source units are required
This recovery capsule uses two ALREADY preserved autonomous sources, without duplicating their bytes:

1. Material [internal-source-reference], SCHUR_PENCIL_GLOBAL_U1_TUBES_V1.md, SHA cdfafb30c57898d24345c62b407652dd54a01de90df481bc6be9a06b7b5043b4. Save its complete Python fence as schur_pencil.py:12232B SHA2f4fcfd1c2cd73fd47c7f95565cc373c5435ba88ab562f674773a824e3cab37c. This supplies the EXACT Bright Willow18 moderate-cut own-centred degree-five body and its chart. It is NOT the separate corner-cut apex4 family.
2. Material [internal-source-reference], HEXAGON_MINIMAL_FIVE_ARROWS_ACTUAL_E17_V1.md, SHA aa2caacb28bfde019a10dc36e909fd20d7273be44edfd98b4db1ffec944c25ef. Save its complete Python fence as hexagon_five.py:11755B SHA4c113fb5c4f9307f2219df999b02ac6ec5320040db51365de8f649323a931380. This supplies the DISTINCT actual degree-six body, actual moment recentering, full true primal/polar lattice and three apical H/f controls.
3. Save the entire Python fence below as apical_bounds.py. No parent payload, external solver, random search or omitted array is needed beyond these two explicitly named complete dependencies. A computational successor must receive all three materials. The general analytical theorem is useful additional reading, not a runtime file dependency.

The two source bodies are never relabeled into each other. The dependency hashes identify the exact already-preserved bytes; the hash alone is not substituted for either material.

## Findings
Write the apex-normalized quantities as in the analytical theorem: tau_i=z_i+f.y_i, r_i=y_i^T H^-1 y_i, delta D_ij=a_ij delta+b_ij. A is strictU for every delta>0 and the required proper local subsystem remains strict throughout every pencil below.

For the four degree-five stronger controls (omissions0,1,2,3):

* Omit0: vertices2,7,8,9 have tau_i^2>=1. Thus this fixed FOOTPOINT excludes apicalU1 for EVERY H positive definite and EVERY delta>0, independently of the local arrow constraints.
* Omit1: vertex3 violates the same radial condition. Also the negative-support vertex3 has L=+infinity.
* Omit2: every |tau_i|<1, but the negative-support vertex1 gives an exact positive lower bound L strictly larger than the exact radial upper bound R. For interpretation only, L~0.1646534412,R~0.0448962329; the proof uses the full exact fractions in the generated report and asserts L>R>0, not these rounded values.
* Omit3: vertices7,8,9 violate the H-independent radial condition; negative-support vertex9 also has L=+infinity.

This is a shorter alternative proof of the four already-known positive-pencil exclusions, not a new count subtraction or a replacement of their stronger radius1/10000 tube theorem.

For the DISTINCT degree-six hexagon's apical proper-subsystem controls (omissions0,2,3), the SAME nonapical true vertex9 is STRICT unstable for EVERY delta>0 in ALL THREE pencils. It is the negative-support vertex in each control. Every one of its THREE outgoing primitives has BOTH affine coefficients STRICTLY NEGATIVE: six exact negative rational coefficients per control, eighteen total. Thus no finite positive normal-parameter wall or unbounded-conditioning tail escapes the obstruction. The apex remains strictU and all four retained local polar arrows remain strict.

For omissions0 and3, vertices3,8,9 additionally violate |tau_i|<1, so those two fixed FOOTPOINTS exclude apicalU1 for every tangential H. Omission2 lies inside the radial footpoint domain, but vertex9 is still a permanent extraU for its reported H. Hence even the radial-footpoint filter being satisfied does not rescue this control.

Across the seven controls, the exact lists failing the H-independent footpoint filter are respectively
[[2,7,8,9],[3],[],[7,8,9],[3,8,9],[],[3,8,9]].
The equality/non-strict filter is checked exactly, and all original retained local arrows and strict apex inequalities are recomputed with the actual poles/vertices. No new stable/unstable/saddle census over the entire H/f cone is claimed.

Scientific consequence: the degree-six branch must vary H/f or actual completion geometry, rather than changing only delta in its three existing apical witnesses. The open questions for omitted1/4 and for completeU1 outside these pencils remain. A locally minimal-five-arrow chamber and a strict apical-U proper subsystem are still not a globalU1 witness.

## Execution and pins
CPython3.13.5, standard library, assertions enabled. Put the three complete pinned source files in one directory and run:

python -B -S apical_bounds.py build > build.stdout
python -B -S apical_bounds.py check > check.stdout
cmp build.stdout check.stdout

Coordinator executed these commands normally and in a fresh directory containing ONLY the three source inputs. Output report and stdout matched. This is exact regeneration, not an independently written verifier or proof-assistant formalization.

apical_bounds.py:4026B SHA e969832858a0f8bf2aaf24250ffe2043c58338d77a404edc7cc0cff98dd9ba29
apical_bounds.json:54715B SHA708321c92870b61968715e3b0119591b6fd81281789cb61cedac3922f3e68be4
build.stdout=check.stdout:477B SHAe5d0645960fed5e663a69b9bdd782877195542b61a4a529ecc6584c20a8d09a7

Expected terminal markers include ALL_SEVEN_ACTUAL_APICAL_PROPER_SUBSYSTEM_PENCILS_U1_EMPTY_PASS, FIVE_CONTROLS_FAIL_H_INDEPENDENT_RADIAL_FOOTPOINT_FILTER_PASS, PENTAGON_OMIT2_EXACT_LOWER_BOUND_EXCEEDS_RADIAL_UPPER_BOUND_PASS, ALL_THREE_HEXAGON_CONTROLS_VERTEX9_PERMANENT_STRICT_U_ALL_DELTA_POSITIVE_PASS and NO_ALL_H_F_EXCLUSION_NO_FULL_INCIDENCE_CLAIM_NO_BOUND_CHANGE.

## Complete new source
```python
#!/usr/bin/env python3
"""Exact application of APICAL_U1_NORMAL_PARAMETER_COMPACTNESS_V1.
Required exact sources: schur_pencil.py and hexagon_five.py, as pinned below.
CPython3.13.5 standard library. python -B -S apical_bounds.py build|check
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib,importlib.util,json,sys
PINS={'schur_pencil.py':(12232,'2f4fcfd1c2cd73fd47c7f95565cc373c5435ba88ab562f674773a824e3cab37c'),
      'hexagon_five.py':(11755,'4c113fb5c4f9307f2219df999b02ac6ec5320040db51365de8f649323a931380')}
def load(filename,name):
 b=Path(filename).read_bytes();n,sha=PINS[filename]
 assert len(b)==n and hashlib.sha256(b).hexdigest()==sha
 s=importlib.util.spec_from_file_location(name,filename);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def analyze(h,name,om,H,f,X,Q,edges):
 assert X[0]==h.v((0,0,1))
 G=h.inv(H);assert min(h.minors(H))>0
 tau=[x[2]+h.dot(f,x[:2]) for x in X]
 r=[h.form(G,x[:2],x[:2]) for x in X]
 assert all(t<1 for t in tau[1:]) # strict apical normal-cone interior, independent of H/delta
 w=min(range(len(X)),key=lambda i:(tau[i],-r[i]));assert tau[w]<0
 coeff=[];bounds=[]
 for i,j in edges:
  for a,b in ((i,j),(j,i)):
   if a!=w:continue
   aa=h.form(G,X[a][:2],h.sub(X[b][:2],X[a][:2]));bb=tau[a]*(tau[b]-tau[a])
   assert bb<=0 and (bb<0 or aa<0)
   if aa>0:bounds.append(-bb/aa)
   coeff.append((a,b,aa,bb))
 L=min(bounds) if bounds else None
 bad=[i for i in range(1,len(X)) if tau[i]**2>=1]
 R=None if bad else min((1-tau[i]**2)/r[i] for i in range(1,len(X)) if r[i]>0)
 closed=bool(bad) or L is None or L>=R
 assert closed
 if name=='HEXAGON':
  assert w==9 and L is None
  assert all(a<0 and b<0 for _,_,a,b in coeff)
 # The locally retained arrow inequalities remain strict for the entire Schur pencil.
 k=h.mul(-1,h.mv(H,f));N,M=h.metric(H,k)
 nlocal=4 if name=='PENTAGON' else 5
 local=[h.form(N,Q[i],h.sub(Q[i+1],Q[i])) for i in range(nlocal)]
 assert all(d>0 for i,d in enumerate(local) if i!=om) and local[om]<0
 return dict(body=name,omitted=om,H=H,f=f,tau=tau,r=r,negative_support_vertex=w,
             outgoing_affine_coefficients=coeff,L=L,L_infinite=L is None,R=R,
             radial_bad_vertices=bad,local_arrows=local,whole_positive_pencil_excluded=closed)

def main():
 assert __debug__
 p=load('schur_pencil.py','pentagon_source');h=load('hexagon_five.py','hexagon_source')
 _,_,_,edges,_,_,X,Q=p.body()
 controls=[((p.vec(1,'1/100'),p.vec('1/100','1/10')),p.vec('35/18','1/600')),
           ((p.vec(1,'-1/2'),p.vec('-1/2','17/64')),p.vec('31/25','149/60')),
           ((p.vec(1,'1/4'),p.vec('1/4','5/64')),p.vec(-1,'8/3')),
           ((p.vec(1,'1/4'),p.vec('1/4','65/16')),p.vec('-1/20','2/25'))]
 rows=[analyze(h,'PENTAGON',om,H,f,X,Q,edges) for om,(H,f) in enumerate(controls)]
 a=h.actual()
 rows += [analyze(h,'HEXAGON',om,tuple(h.v(r) for r in H),h.v(f),a['chart_vertices'],a['chart_poles'],a['edges']) for om,H,f in h.APEX_DATA]
 assert [r['radial_bad_vertices'] for r in rows]==[[2,7,8,9],[3],[],[7,8,9],[3,8,9],[],[3,8,9]]
 assert rows[2]['L']>rows[2]['R']>0
 out=(json.dumps(h.serial(dict(identity='SEVEN_APICAL_PENCILS_GLOBAL_U1_EXCLUSION_V1',records=rows)),sort_keys=True,indent=2)+'\n').encode()
 target=Path('apical_bounds.json')
 if sys.argv[1]=='build':target.write_bytes(out)
 else:assert target.read_bytes()==out
 print('ALL_SEVEN_ACTUAL_APICAL_PROPER_SUBSYSTEM_PENCILS_U1_EMPTY_PASS')
 print('FIVE_CONTROLS_FAIL_H_INDEPENDENT_RADIAL_FOOTPOINT_FILTER_PASS')
 print('PENTAGON_OMIT2_EXACT_LOWER_BOUND_EXCEEDS_RADIAL_UPPER_BOUND_PASS')
 print('ALL_THREE_HEXAGON_CONTROLS_VERTEX9_PERMANENT_STRICT_U_ALL_DELTA_POSITIVE_PASS')
 print('SIX_NEGATIVE_AFFINE_COEFFICIENTS_PER_HEXAGON_CONTROL_PASS')
 print('NO_ALL_H_F_EXCLUSION_NO_FULL_INCIDENCE_CLAIM_NO_BOUND_CHANGE')
 print(target.name,len(out),hashlib.sha256(out).hexdigest())
if __name__=='__main__':
 if len(sys.argv)!=2 or sys.argv[1] not in ('build','check'):raise SystemExit('Usage: python -B -S apical_bounds.py build|check')
 main()
```
