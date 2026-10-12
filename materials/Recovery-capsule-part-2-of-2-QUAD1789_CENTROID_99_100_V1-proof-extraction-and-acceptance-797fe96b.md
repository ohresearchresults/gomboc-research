# material-797fe96b2000

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 2/2 — QUAD1789_CENTROID_99_100_V1

## Identity, dependencies and evidence disposition

Part1 is the complete immutable source container [internal-source-reference],38964 UTF-8 bytes,SHA256724cda78b7af85ae69a322d8fc93f6eafe944eab3f2f55ff061085928d0137fd. Its complete UTF16 interval[0,30608) was submitted to research_store_material as part1 in this continuation; storage deduplicated the exact bytes to that same material ID. This part2 and part1 together are sufficient for recovery without any sandbox. The container is a JSON object with a handoff_markdown string, including ONE complete fenced Python decoder. Historical status and counts inside its prose are not current instructions and do not override later C+D results.

ACCEPTED HERE: the conditional genuine quadrilateral centroid theorem QUAD1789_CENTROID_99_100_V1 and its complete exact certificate. The 147-position/125-class K3 application is retained as a separately reproducible archived result, but its intersection with already accepted C+D deletions has NOT yet been computed in this continuation. Do not add147/125 blindly to current counts. Current accepted C+D K3 remains5702positions/4164classes pending that integration. No stronger universal C bound is claimed.

## Complete mathematical theorem and proof

Let x1,...,x9 be formal vectors in any finite-dimensional real inner-product space with ONE positive-definite metric. Let u=x3 and let
p1=2,p2=3,p4=3,p5=4,p6=5,p7=6,p8=7,p9=8.
Assume gi=<xi,xi>-<xi,xpi><=0 for i=1,2,4,5,6,7,8,9. Formal vectors may coincide. Suppose the distinct points a=x1,b=x7,c=x8,d=x9 form a nondegenerate planar convex quadrilateral in the indicated cyclic order. If cQ is its actual uniform area centroid, then

< u,3cQ > >= -(99/100)<u,u>.

Consequently the actual uniform volume centroid of the nondegenerate pyramid with apex u and base Q has projection on u at least <u,u>/400. The theorem does not assume freely chosen triangle masses.

The diagonals meet at unique s,t in(0,1), with sa+(1-s)c=tb+(1-t)d. The actual areas abc:acd=(1-t):t. Indeed the two heights from b,d to ac are in this ratio, since their common diagonal point divides bd with distances(1-t)|bd| and t|bd|. Taking the area-weighted triangle centroids gives 3cQ=a+c+(1-t)b+td.

On s<=1/2, solve for c with denominator w=1-s; on s>=1/2 solve for a with denominator w=s. Multiplying
(99/100)<u,u>+<u,a+c+(1-t)b+td>+sum_i lambda_i gi
by w² yields a symmetric matrix polynomial Q(s,t) of order8 and bidegree at most(2,2), acting on the eight remaining formal vectors coordinate by coordinate. Here the lambda_i are nonnegative rational constants within each of13 dyadic cells; their104 exact numerators with common denominator10^6 are the TABLE in quad1789_exact.py, fully preserved in part1.

The dyadic code set is000,0010,0011,010,0110,0111,1000,1001,101,1100,1101,1110,1111. Bits alternate subdivision of s,t, starting with s,0lower and1upper. The recursive prefix-tree checker proves coverage of all[0,1]², not just test points. For each cell, the exact checker expresses Q in the degree(2,2) tensor Bernstein basis and proves all9 coefficient matrices positive definite by rational Schur/LDL pivots. There are117 matrices and936 positive pivots. Bernstein weights are nonnegative and sum1 throughout the closed cell, so Q(s,t) is positive definite there. Since lambda>=0 and gi<=0, the desired nonnegative form follows. Multiplication by w² is harmless since w>=1/2. Weak arrow equalities and cell boundaries are included. The actual centroid under any nonsingular linear change transforms affinely, since the area Jacobian is constant on the facet plane. Thus the proof is valid for the stated common arbitrary SPD metric.

The root may be repeated to pad a shorter abstract branch. This is substitution of equal formal vectors in a universal quadratic inequality, NOT merging actual incidence labels. A valid application has a of depth1 or2 and b,c,d successive vertices on another actual parent path whose terminal depth is3..6. The source checks the complete formal-to-actual role map. A quad can be a cell in a larger true facet. To infer an entire body exclusion, all nonincident true facets must admit a dissection into good cells with the SAME root projection, and actual positive cone volumes must be used. A negative or unproved embedded triangle is not automatically a bad maximal facet.

## Exact recovery and pins

Save part1's complete text as quad1789_source_container.json, UTF8 with the exact original bytes (the material already contains its full JSON). Save the following complete source as recover_container.py,UTF8/LF with final LF. Its pin is1005bytes,SHA256c9c0eb5824e0821592565226ebee97ab2e8e03a9ddbc8d14b4900dca199a5938.

```python
"""Recover the exact QUAD1789 source capsule from its immutable JSON container.
python -S recover_container.py ARCHIVED_CONTAINER OUTPUT_DIRECTORY
The archived prose is historical, not the current K3 endpoint.
"""
from pathlib import Path
import hashlib,json,subprocess,sys
assert __debug__ and len(sys.argv)==3
source=Path(sys.argv[1]).read_bytes()
assert [len(source),hashlib.sha256(source).hexdigest()]==[38964,'724cda78b7af85ae69a322d8fc93f6eafe944eab3f2f55ff061085928d0137fd']
text=json.loads(source)['handoff_markdown']
assert text.count('```python\n')==1
code=text.split('```python\n',1)[1].split('```',1)[0].encode()
assert [len(code),hashlib.sha256(code).hexdigest()]==[17275,'339495220abcec51219649c1aa36b5783ca93001de709d71435133d082968670']
root=Path(sys.argv[2]);root.mkdir(parents=True,exist_ok=True)
target=root/'minimum_quad1789_recovery.py';target.write_bytes(code)
subprocess.run([sys.executable,'-S',str(target),str(root)],check=True)
print('QUAD1789_ARCHIVED_CONTAINER_RECOVERY_PASS')
```

Run `python -S recover_container.py quad1789_source_container.json recovered`; then in recovered run `python -S quad1789_exact.py build`, `python -S quad1789_exact.py check`, `python -S triangle_bounds_exact.py build`, `python -S triangle_bounds_exact.py check`. Assertions must be enabled. Proof checking needs only CPython standard library, actually replayed under3.13.5. The container extractor itself was written and its pin computed; its full-container command was not run locally because the immutable JSON wrapper was not copied to sandbox. Instead its exact decoder was reconstructed independently from the complete retrieved fence, byte-pin checked, and run. This distinction does not change the full literal recovery data.

The recovered decoder17275bytes,SHA339495220abcec51219649c1aa36b5783ca93001de709d71435133d082968670 contains the complete whitespace-free base6415824bytes,SHAff3e13708f78da5aff1874afb0c1132ef4ccc9ee86e87ae5deb5075fbb51f621. Decoded lzma JSON44918bytes,SHA4d4ad1f66f6efd5f4d98d1768703cc2b8815cad87e165c11cd6ec3bdf4643583. These three exact pins and all seven recovered source pins were verified in this continuation. Numerical locators are not proof dependencies.

Source pins: quad1789_exact.py5801/fae2a51174c73a0a27ad6aafa549a54ed645f64fa13c04549f6774bed3f8ff17; triangle_bounds_exact.py3661/fa629a519fa4541239f3b41e8ad54089c62fbef46ef8cb21cf886629c02f758d; quad1789_delta.py15916/29437de31c79ae02f0682b93efec4d9beb43d2a2343f594174799750cb21f516. Four complete archived optional exploratory sources also remain in part1 and its full manifest, with no omissions.

Fresh actually observed terminal markers, build and check:
QUAD1789_RECOVERY_SOURCES_PASS 7 44918 4d4ad1f66f6efd5f4d98d1768703cc2b8815cad87e165c11cd6ec3bdf4643583
QUAD1789_EXACT_BERNSTEIN_COVER_PASS 13 117 936 1204 4553e91aea9b21c0bc98f4ca2c3333910090885d4db2b52953dc685ead8f56eb 54131 6a7e3ace687d67cbacc58cc04d3a27fbdfdba282baf5f3673ad92409466f23fb
INHERITED_TRIANGLE_BOUNDS_EXACT_REPLAY_PASS 11 76 3 5522 80452b9502ec7649e0cd61a5aaade3c859b3f937e69c55d21378c81e78adec36

Output filenames respectively quad1789_table.json1204bytes and quad1789_report.json54131bytes with the pins above; triangle_bounds_report.json5522bytes with the pin above. A second clean subdirectory recovered the identical seven sources and independently ran quad build/check with identical output pins. This accepts a conditional continuum theorem, not a new complexity threshold or unconditional K3 count.
