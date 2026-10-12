# material-c3e7fc3cef5a

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Exact mutual escape obstruction on two CONDITION25 deletion bodies

## Scope and proof
For centered points x,y, let e(x,y)=x·(y-x). Then e(x,y)+e(y,x)=-|x-y|²<0 whenever x!=y. More generally, along a closed directed cycle, the sum of these escape numerators is minus one half the sum of squared edge lengths. Therefore a directed cycle cannot have every escape positive. This is an exact algebraic identity, independent of the chosen center. It excludes the simultaneous chosen arrows, NOT every deformation of either body; changing a neighbor's escape target can break the obstruction.

The exact initial CONDITION25 DELETE99 body has bad vertex144, child128, true root94. At its OWN volume centroid vertex144 has173negative and zero positive escape numerators to other vertices; child128 has exactly ONE positive target,144, and172negative targets. No off-diagonal zero occurs. DELETE117 has bad79, child76, root92, with the analogous exact sign counts and child's sole positive target79. Thus forcing144→128 or79→76 while retaining the initial child's witness creates a two-cycle. A max-arrow numerical method could switch that child's witness, so this observation does not prove global failure of that method. The observed local trajectories instead shortened the mutual edge, motivating explicit acyclic rerouting.

Both exact inputs are separate own-centroid strict121/weak000 nonwinners, V174/E308/F136,C616, NOT own110 records. Their independent complete A/B and centered-mass certificates are in [internal-source-reference]. This new audit uses exact Fraction arithmetic and all other vertices, not just adjacent ones.

## Complete input closure
Decode ALL THREE original CONDITION25 source materials into a directory named source beside these two scripts:
[internal-source-reference] SHA20469536cc4461b597cd92b9c7420b89ad4f1efd82ef72aa4f934b9bb772067a;
[internal-source-reference] SHAa527d91c2ba70ee5220ca4b6ba30964e804fd4fa52a8619d3ae6567608cc8087;
[internal-source-reference] SHAecb59180686fbea53343e4b78e64b70478df5ede3679acd200c163185c1e29d4.
They contain the complete24-file source dictionary, exact generator and exhaustive auditor. No originating sandbox is required. The mathematical deletion recipe is literal removal of support99 or117 separately from that parent's reconstructed H representation, never both. This material plus those THREE original materials is sufficient for the present audit; the earlier deletion material is additional evidence of B/mass, not a missing byte dependency.

Source environment CPython3.13.5, standard library only. Save each complete code block verbatim, including its final newline. MAKE_DELETION_INPUTS.py1098bytes SHA7db53651afb6573083e7ddf4dc24b8447d4a7412e969ecd5c477969300b38922. CYCLE_AUDIT.py2162bytes SHA3e05efa4cfe8b96550284d16b85c6d21909f885348c258a43627c1d3d6ed072a.
Run in a fresh workspace:
`python -B -S MAKE_DELETION_INPUTS.py`
`python -B -S CYCLE_AUDIT.py . CYCLE_REPORT.json`
Expected first terminal BOTH_EXACT_DELETION_INPUTS_RESTORED. Expected exact input reports del99_exact/A.json310157bytes SHAaf5e1884bf301785a618928bf9ccbd44e965391ee964fd24f7e4cdf0cdaac85d and del117_exact/A.json309887bytes SHA3832d35b39b5e70cef5c21cfdd3cc5bb91985ba376324574200ddd287eb48446. The second terminal is TWO_FORCED_BRANCHES_EXACT_MUTUAL_CYCLE_AUDIT_PASS; CYCLE_REPORT.json1307bytes SHA7f9eca55aa767771bedebcff70d0b60015e230daed529c89d5eac2bf61785779. Both commands and these byte/hash checks completed in the producing coordinator turn.

### MAKE_DELETION_INPUTS.py
```python
"""Restore exact deletion reports for nonlinear experiments; no numerical geometry."""
import sys,json,subprocess,concurrent.futures,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'source';sys.path.insert(0,str(SRC/'methods/parent'))
import RECONSTRUCT
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
raw=RECONSTRUCT.recover(json.loads((SRC/'GENERATOR.json').read_text()))
expected={99:'af5e1884bf301785a618928bf9ccbd44e965391ee964fd24f7e4cdf0cdaac85d',117:'3832d35b39b5e70cef5c21cfdd3cc5bb91985ba376324574200ddd287eb48446'}
def one(f):
 d=ROOT/f'del{f}_exact';d.mkdir();(d/'RAW.json').write_bytes(B({'H':[r for i,r in enumerate(raw['H']) if i!=f]}))
 subprocess.run([sys.executable,'-B','-S',str(SRC/'methods/parent/check_A.py'),str(d/'RAW.json'),str(d/'A.json')],check=True)
 assert hashlib.sha256((d/'A.json').read_bytes()).hexdigest()==expected[f]
 print('EXACT_DELETION_INPUT_RESTORED',f,flush=True)
with concurrent.futures.ThreadPoolExecutor(2) as pool:list(pool.map(one,[99,117]))
print('BOTH_EXACT_DELETION_INPUTS_RESTORED',flush=True)
```

### CYCLE_AUDIT.py
```python
"""Exact signed escape audit of the two attempted forced-arrow branches.
Inputs are the canonical CONDITION25 exact deletion reports; hashes enforced.
No global infeasibility of the bodies or of deforming them is claimed.
"""
import sys,json,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
assert __debug__
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
dot=lambda a,b:sum(x*y for x,y in zip(a,b))
sub=lambda a,b:[x-y for x,y in zip(a,b)]
def main():
 p=argparse.ArgumentParser();p.add_argument('workspace',type=Path);p.add_argument('output',type=Path);a=p.parse_args();result={}
 for deletion,bad,child,root,sha in [(99,144,128,94,'af5e1884bf301785a618928bf9ccbd44e965391ee964fd24f7e4cdf0cdaac85d'),(117,79,76,92,'3832d35b39b5e70cef5c21cfdd3cc5bb91985ba376324574200ddd287eb48446')]:
  b=(a.workspace/f'del{deletion}_exact/A.json').read_bytes();assert hashlib.sha256(b).hexdigest()==sha;r=json.loads(b);X=[list(map(F,row)) for row in r['raw_vertices']];g=list(map(F,r['raw_centroid']));rows={}
  for i in [bad,child]:
   vals=[dot(sub(X[i],g),sub(x,X[i])) for x in X]
   rows[str(i)]=dict(positive=[j for j,v in enumerate(vals) if v>0],zero_excluding_self=[j for j,v in enumerate(vals) if v==0 and j!=i],negative_count=sum(v<0 for v in vals))
  u=sub(X[bad],g);v=sub(X[child],g);d=sub(v,u);uv=dot(u,d);vu=-dot(v,d);d2=dot(d,d);assert d2>0 and uv+vu==-d2 and uv<0 and vu>0
  assert not rows[str(bad)]['positive'] and rows[str(child)]['positive']==[bad]
  result[str(deletion)]=dict(VEF=[r[k] for k in ['V','E','F']],own_counts=r['counts'],weak=r['weak'],input_report_sha256=sha,bad_vertex=bad,child=child,root=root,escape_signs=rows,mutual_sum_is_negative_squared_edge_length=True,scope='At the exact initial body, the selected child has only the bad vertex as a positive escape. Two opposite arrows cannot both be positive at any distinct pair. Rerouting remains possible; no global body exclusion.')
 out=dict(marker='TWO_FORCED_BRANCHES_EXACT_MUTUAL_CYCLE_AUDIT_PASS',bodies=result);a.output.write_bytes(B(out));print(B(out).decode(),flush=True)
if __name__=='__main__':main()
```
