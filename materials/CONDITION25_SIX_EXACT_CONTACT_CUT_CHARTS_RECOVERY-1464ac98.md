# material-1464ac98592b

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Six exact one-neighbor truncation contact charts

## Geometry and objective
Start with the exact CONDITION25 C622 parent; independently delete its unused free triangular support99 or117, obtaining exact C616 own121. At the extra unstable degree-three vertex u, the original parent's deleted support meets each incident edge at a rational cut point. Reintroduce that support through ONE existing neighbor n of u, retaining the original two other edge-cut parameters for the ideal normal. The actual restored support is constrained to pass exactly through n by an alternating contact DAG, not by tolerating approximate coplanarity.

For each of the six choices, a new point node180 is solved from the neighbor's three original supports, then the restored support99/117 is solved in one coordinate from contact with that point. Its other two coordinates are the ideal normal rounded ties-to-even on grid1e12. All other controls and contact equations remain literal CONDITION25 data. This creates a four-support vertex and313free coordinates. Every generator and reconstructed H is exact. The expected true complex is V175/E310/F137,C620; independent maximal-incidence A determines rather than assumes this count. These are new contact architectures for further full-body deformation, not yet own110 constructions.

Completed A observations at preservation time: delete99_neighbor128 V175/E310/F137,strict121,weak000,S3,U94/128,H128–144,A316462bytes SHA290524e82efd07897aab77d1fd71537654b91f99bce3741717481a08c07ebfb0; delete99_neighbor145 sameVEF/strict/weak,S3,U94/145,H145–146,A313970 SHA bb3f50d4924f333086656c483a9264b71e10fd7bb3a5746985fce4d08798d264. delete99_neighbor111 sameVEF,strict25/37/60,weak000,A315821 SHA9bea4317d2a6404d8c63873a9d63a1c9bd4537d2fe2f4acd7e29aac97bd0fef4. delete117_neighbor75 sameVEF,strict35/47/80,weak000,A315064 SHA3aa8b23fd9405081825ac92b07d94058c9eb08ceb47a46d431fdd633207446e2. The remaining two A outcomes and any B/mass results must be recorded separately, not inferred here. The parent C622 own110 record is unchanged.

## Durable source/input closure
Use complete CONDITION25 source ALL THREE [internal-source-reference],[internal-source-reference],[internal-source-reference], decoded into source/. Generate the exact del99_exact/A.json and del117_exact/A.json inputs using MAKE_DELETION_INPUTS.py from [internal-source-reference]. Their expected SHA values are af5e1884bf301785a618928bf9ccbd44e965391ee964fd24f7e4cdf0cdaac85d and3832d35b39b5e70cef5c21cfdd3cc5bb91985ba376324574200ddd287eb48446. This material and those FOUR dependencies are sufficient without an originating sandbox or optimization. Generator labels in each output report are that body's own raw-lex labels; filename neighbor labels refer expressly to the starting deletion body.

Save complete CONTACT_CUT_CHARTS.py below with final newline,4084bytes SHA693002f3716b1d27ca2295baaadd599a5f22c2ede9a0a40a07456069cc30de33. CPython3.13.5, standard library only. Command:
`python -B -S CONTACT_CUT_CHARTS.py --source source --workspace . --out contact_charts --workers 2`
Terminal expected SIX_EXACT_CONTACT_CUT_CHARTS_AUDITED; each body directory contains GENERATOR.json,RAW.json,RECIPE.json,A.json,SUMMARY.json. RECIPE includes exact original cut fractions, rational ideal normal, new solved contact/axis and hashes. Exact recovery of the six bodies does not depend on completing the audits: the code writes all six complete generators and H representations before auditing any of them. Their twelve exact byte/hash expectations are below. For B verification run source/methods/parent/check_B.py on each RAW.json; then centred_mass.run(A_report) supplies the third check. Do not call these B/mass checks completed without their receipts.

### CONTACT_CUT_CHARTS.py
```python
"""Exact one-neighbor truncation charts derived from CONDITION25 support deletions.
A previously free triangular support is reintroduced through one existing
neighbor. Its two other cuts initially follow the original parent's cuts.
The added four-support contact is enforced exactly by a topologically ordered
point/support atlas, not by rounding a coplanarity residual to zero.
"""
import argparse,copy,hashlib,json,sys,subprocess,concurrent.futures
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
assert __debug__
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
H=lambda b:hashlib.sha256(b).hexdigest()
dot=lambda x,y:sum(a*b for a,b in zip(x,y))
sub=lambda x,y:[a-b for a,b in zip(x,y)]
def main():
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--workspace',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--workers',type=int,default=2);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 sys.path.insert(0,str(a.source/'methods/parent'));import RECONSTRUCT
 G0=json.loads((a.source/'GENERATOR.json').read_text());raw=RECONSTRUCT.recover(G0);Q=[[F(x,row[-1]) for x in row[:3]] for row in raw['H']];jobs=[];inputs={}
 for f,bad in [(99,144),(117,79)]:
  rp=a.workspace/f'del{f}_exact/A.json';r=json.loads(rp.read_text());X=[list(map(F,v)) for v in r['raw_vertices']];u=X[bad];nb=[b if c==bad else c for c,b in r['edges'] if bad in (c,b)];assert len(nb)==3
  assert [row for row in G0['plan'] if row[0]==f]==[[f,[],[]]] and not any(f in deps for _,deps,_ in G0['plan'])
  ts={n:(1-dot(Q[f],u))/dot(Q[f],sub(X[n],u)) for n in nb};assert all(0<t<1 for t in ts.values())
  for n in nb:
   own=[k+(k>=f) for k,cy in enumerate(r['faces']) if n in cy];assert len(own)==3
   pts=[X[n]]+[[u[k]+ts[j]*(X[j][k]-u[k]) for k in range(3)] for j in nb if j!=n];q=RECONSTRUCT.solve(pts,[F(1)]*3);assert dot(q,u)>1 and all(dot(q,v)<=1 for i,v in enumerate(X) if i!=bad)
   G=copy.deepcopy(G0);idx=len(G['controls']);ax=max(range(3),key=lambda k:abs(X[n][k]));G['groups'].append(sorted(own+[f]));G['controls'].append([round(x*G['grid']) for x in X[n]]);G['controls'][f]=[round(x*G['grid']) for x in q]
   G['plan']=[row for row in G['plan'] if row[0]!=f]+[[idx,own,[0,1,2]],[f,[idx],[ax]]]
   rr=RECONSTRUCT.recover(G);name=f'delete{f}_neighbor{n}';d=a.out/name;d.mkdir();(d/'GENERATOR.json').write_bytes(B(G));(d/'RAW.json').write_bytes(B(rr));info=dict(deleted_support=f,bad_parent_delete_label=bad,retained_neighbor_parent_delete_label=n,neighbor_supports_original=own,new_contact_point=idx,solved_support_axis=ax,initial_other_cut_parameters={str(j):str(ts[j]) for j in nb if j!=n},exact_parent_report_sha256=H(rp.read_bytes()),ideal_cut_normal=list(map(str,q)),generator_sha256=H(B(G)),raw_sha256=H(B(rr)))
   (d/'RECIPE.json').write_bytes(B(info));inputs[name]=info;jobs.append(name)
 def audit(name):
  d=a.out/name;rr=subprocess.run([sys.executable,'-B','-S',str(a.source/'methods/parent/check_A.py'),str(d/'RAW.json'),str(d/'A.json')],capture_output=True,text=True);assert rr.returncode==0,(name,rr.stderr[-3000:]);r=json.loads((d/'A.json').read_text());s=dict(VEF=[r[k] for k in ['V','E','F']],C=2*r['E'],strict=r['counts'],weak=r['weak'],S=r['stable_face_ids'],U=r['unstable_vertices'],H=r['saddle_edges'],report_bytes=(d/'A.json').stat().st_size,report_sha256=H((d/'A.json').read_bytes()),all_supports_active=r['active_input_indices']==list(range(G0['n_supports'])));(d/'SUMMARY.json').write_bytes(B(s));print('EXACT_CONTACT_CUT_CHART',name,B(s).decode(),flush=True);return name,s
 with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:res=dict(pool.map(audit,jobs))
 receipt=dict(marker='SIX_EXACT_CONTACT_CUT_CHARTS_AUDITED',bodies=res,scope='Exact C620 contact charts when audited as such; no own110 improvement unless full independent checks and recovery are subsequently completed.');(a.out/'RECEIPT.json').write_bytes(B(receipt));print(B(receipt).decode(),flush=True)
if __name__=='__main__':main()
```

### EXPECTED_BODIES.json
```json
{"delete117_neighbor75/GENERATOR.json":{"bytes":11931,"sha256":"40b38731435b657d2aa57d18183943d5dc2c2019dc10448edd079aa7bcfc0da3"},"delete117_neighbor75/RAW.json":{"bytes":15685,"sha256":"435b0b4a5bdd03fe5275749418b1e2c8b88329fbe2b12214bb33bb9a263e668e"},"delete117_neighbor76/GENERATOR.json":{"bytes":11932,"sha256":"ac979930ee01117c87f6527f75cfa486031a32656d157f577f005a839c98c2b5"},"delete117_neighbor76/RAW.json":{"bytes":15859,"sha256":"24d12220bb566bad2a85996840817b2ae107a83ba53fdca31ea402d642be5b89"},"delete117_neighbor82/GENERATOR.json":{"bytes":11927,"sha256":"c1ff50ff519d5a4f1d2d9bdbdeadceef0264e7b1375e9ab83263d3bc898a21d2"},"delete117_neighbor82/RAW.json":{"bytes":15776,"sha256":"586047a8d60339bf8e6992de3a78472d5a1ea54268cb47d4f06a5908f60a4a38"},"delete99_neighbor111/GENERATOR.json":{"bytes":11927,"sha256":"8bbbeb2629643fe633784da25bd236be51be30071358cee84a79cfb57be61578"},"delete99_neighbor111/RAW.json":{"bytes":15816,"sha256":"a8080b654c26c4941343ab6cafe6a00d00342e10034d54646dc2345868bbcb64"},"delete99_neighbor128/GENERATOR.json":{"bytes":11926,"sha256":"e18ee94968df19e3894266a9bfa5c640bd6b99bf022ebe67098ada5a138d4b4e"},"delete99_neighbor128/RAW.json":{"bytes":15823,"sha256":"2ae5eadc2c73422a2f7a323383a672411430dbd44de276d78acacd56c5946aef"},"delete99_neighbor145/GENERATOR.json":{"bytes":11928,"sha256":"e5e72e93628e88c37b6d1f2e7c6e19d043c0460180ddfb2be1de0234bd38a954"},"delete99_neighbor145/RAW.json":{"bytes":15680,"sha256":"da1ef72b9a5b6c9ce29040722e8d8670633d464a60aa8d6d9de810255825b92c"}}
```

To check the exact recovered coordinate files after the command, save the JSON block as EXPECTED_BODIES.json and run:
```python
import hashlib,json
from pathlib import Path
for name,w in json.loads(Path('EXPECTED_BODIES.json').read_text()).items():
 b=(Path('contact_charts')/name).read_bytes()
 assert len(b)==w['bytes'] and hashlib.sha256(b).hexdigest()==w['sha256'],name
print('SIX_CONTACT_CHART_EXACT_COORDINATE_HASHES_PASS')
```
