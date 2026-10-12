# material-660c289e362c

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# Reroute before contact — complete producer patch and exact input helper

## Scientific objective and evidence status
This changes the order of operations: start with exact CONDITION25 own110 C622, remove both directions of a prospective collapsing edge from the auxiliary escape objective, and improve the remaining negative alternative escape BEFORE imposing a four-support contact. The actual unblocked escape from the affected vertex remains an additional strictly positive guard, so accepted numerical stages retain actual physical and polar escape conditions even while the alternative route is incomplete. The topology remains C622. This method does NOT itself contract an edge; successful rerouting would permit a later contact homotopy without depending on the vanishing edge. No new record or completed rerouting is claimed by this source material.

Two finite trials started from the same exact parent, edges128–133 and76–79, each with35stages,30inner iterations and fraction.05,gamma1e-8,trust.1,qbound.01. Both first rejected the attempted lambda.05 stage and subsequently accepted lambda.025, retaining actual bad escape respectively2.774607516869945e-8 and1.6198569622248902e-8. These are observed numerical partial stages, not exact endpoint audits or durable object promotions. Exact frozen checkpoints and eventual outcomes must be preserved separately before reuse.

## Complete dependencies
The patch consumes the complete CONTACT_HOMOTOPY.py in [internal-source-reference] (C620_CONTACT_HOMOTOPY_COMPLETE_SOURCE.md, SHA cf6089cfa6afc8ff626428353bd8c6cd9ca29e786e54d63ea52306ce2f8cbd36). It needs no contact-chart or deletion object: the geometric input is the distinct same-C CONDITION25 parent. Its complete24-file source closure is ALL THREE [internal-source-reference],[internal-source-reference],[internal-source-reference], with hashes20469536cc4461b597cd92b9c7420b89ad4f1efd82ef72aa4f934b9bb772067a,a527d91c2ba70ee5220ca4b6ba30964e804fd4fa52a8619d3ae6567608cc8087,ecb59180686fbea53343e4b78e64b70478df5ede3679acd200c163185c1e29d4. Decode those into source/.

Save each code block with its terminal newline. MAKE_PARENT_INPUTS.py1122bytes SHA77d3de011f75468b449bac126c4230be10d071f37acc2ed33618b567d00578e8. MAKE_PREROUTE_SOURCE.py4152bytes SHA780c1f14150a1d7e344c5610b80a52f065be3c974ee21cde68ca6da72558acd6. Run:
`python -B -S MAKE_PARENT_INPUTS.py source parent_exact`
`python -B -S MAKE_PREROUTE_SOURCE.py CONTACT_HOMOTOPY.py PREROUTE_BEFORE_CONTACT.py`
Expected markers PARENT_CONDITION25_INPUTS_EXACT_READY and PREROUTE_SOURCE_RECOVERED6477d5c1d30706fad0f4eca76d8516181f88eb45914959fd3d51ce7e896365638ecc (spaces separate the printed marker/size/hash). Both commands completed with these exact identities in the producing turn. The helper pins the complete exact parent generator11841bytes SHA8b8c74c7995098ff531e5d7652da20c1afa9cbaefaeea42cd78ea54e3e7e86f5, RAW15551 SHA99b773cbcf09fe227a1c19850e778dfca7f1124820b72b77c53883219e1cb697, and A313272 SHA41b440d3a557a88f0abfc4b2e1bde8b99c8793b173d433c7dfad162fefd4878d.

Numerical commands:
`python -u -B PREROUTE_BEFORE_CONTACT.py --source source --body parent_exact --edge 128,133 --out preroute_128_133 --stages 35 --inner 30`
`python -u -B PREROUTE_BEFORE_CONTACT.py --source source --body parent_exact --edge 76,79 --out preroute_76_79 --stages 35 --inner 30`
CPython3.13.5,NumPy2.3.5,SciPy1.17.0,BLAS/OMP1thread; no random seed. Reconstructed source includes all default parameters. Initial alternative angle deficits are-.017413861990724 and-.021686588225725 respectively. Full configurations, actual input hashes, rounded grid1e12 generators, binary64hex coordinates, stage histories and actual/blocked escape measurements are written. Expected finite-run terminal PREROUTE_BEFORE_CONTACT_FINITE_DONE. A numerical rerouting flag only describes all alternative inequalities becoming positive; a later exact contact and independent all-feature A/B/mass audit remain necessary.

### MAKE_PARENT_INPUTS.py
```python
"""Recover exact CONDITION25 parent input and its exhaustive A report."""
from pathlib import Path
import hashlib,json,sys
assert __debug__
assert len(sys.argv)==3,'Give source_directory output_directory'
src,out=map(Path,sys.argv[1:]);out.mkdir(parents=True,exist_ok=True);sys.path.insert(0,str(src/'methods/parent'));import RECONSTRUCT,check_A
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
G=(src/'GENERATOR.json').read_bytes();raw=B(RECONSTRUCT.recover(json.loads(G)))
expected={'GENERATOR.json':(11841,'8b8c74c7995098ff531e5d7652da20c1afa9cbaefaeea42cd78ea54e3e7e86f5'),'RAW.json':(15551,'99b773cbcf09fe227a1c19850e778dfca7f1124820b72b77c53883219e1cb697'),'A.json':(313272,'41b440d3a557a88f0abfc4b2e1bde8b99c8793b173d433c7dfad162fefd4878d')}
for name,b in [('GENERATOR.json',G),('RAW.json',raw)]:assert (len(b),hashlib.sha256(b).hexdigest())==expected[name];(out/name).write_bytes(b)
p=out/'A.json'
if not p.exists():p.write_bytes(B(check_A.run(json.loads(raw))))
b=p.read_bytes();assert (len(b),hashlib.sha256(b).hexdigest())==expected['A.json'];print('PARENT_CONDITION25_INPUTS_EXACT_READY')
```

### MAKE_PREROUTE_SOURCE.py
```python
"""Exact source patch: reroute before imposing the C620 edge contact."""
import hashlib,sys
from pathlib import Path
assert len(sys.argv)==3,'Give original CONTACT_HOMOTOPY.py output PREROUTE_BEFORE_CONTACT.py'
s=Path(sys.argv[1]).read_text();assert hashlib.sha256(s.encode()).hexdigest()=='6a8430bcf7004652dbfd159735c03d70e953c6cc9306ab81c720f5ac5fa96b08'
s=s.replace('"""Finite own-centroid contact-chart escape homotopy; numerical discovery only.\nInput is an exact GENERATOR.json and exhaustive maximal-complex A.json.\nThe physical witness graph is made acyclic before continuation. In fixed mode\nits arrows are retained. In dag mode each vertex may switch to any later vertex\nin a topological ordering, including its original chosen successor. Polar\nescapes can switch in both modes. No numerical output is an exact certificate.\n"""','"""Reroute physical escapes BEFORE imposing a smaller contact architecture.\nThe input is the exact own110 CONDITION25 C622 parent. Block both directions\nof the chosen future collapsed edge in the continuation mechanics, but also\nretain the true unblocked bad-vertex escape as a positive guard. Thus the one\ninitially negative blocked escape can improve while the actual body stays\nnumerically own11. All other guards use its actual filled volume centroid.\nNo edge is contracted here; a positive rerouting permits a later contact.\n"""')
s=s.replace("p.add_argument('--mode',choices=['fixed','dag','switch'],default='fixed');","p.add_argument('--edge',required=True);")
a=s.index("Q=np.array(");b=s.index("s.floor[:s.mechlen-2]",a)
s=s[:a]+'''Q=np.array([[float(F(x,r[-1])) for x in r[:3]] for r in raw['H']]);s=FlexibleAtlas(G,rep,Q);z=np.zeros(s.n);edge=tuple(map(int,a.edge.split(',')));assert len(edge)==2 and sorted(edge) in rep['edges'] and s.U not in edge
 assert rep['counts']==[1,1,0] and rep['weak']==[0,0,0]
 s.blockedp=[edge,edge[::-1]];s.last=None;v,J,g=s.evaluate(z);bads=s.keptp[v[:s.nv-1]<0];assert len(bads)==1,bads;bad=int(bads[0]);slot=int(np.where(s.keptp==bad)[0][0]);initial=float(v[slot]);assert initial<0
 def evaluate(zz):
  vv,JJ,gg=s.evaluate(zz);ee,DE=s.escape(gg['X']-gg['g'],gg['DX']-gg['Dg']);return np.r_[vv,ee[bad]],np.vstack((JJ,DE[bad])),gg
 '''+s[b:]
a=s.index('cfg={');b=s.index("(a.out/'CONFIG.json')",a)
s=s[:a]+'''floor=np.r_[s.floor,a.gamma];rescale=np.r_[s.rescale,1e-3]
 def residual(zz):return np.maximum(floor-evaluate(zz)[0],0)/rescale
 cfg={k:str(v) if isinstance(v,Path) else v for k,v in vars(a).items()};cfg.update(generator_sha256=H(B(G)),raw_sha256=H(B(raw)),report_sha256=H((a.body/'A.json').read_bytes()),versions=[platform.python_version(),np.__version__,scipy.__version__],root=s.U,bad=bad,edge=list(edge),slot=slot,initial_blocked_bad_angle=initial,variables=s.n)
 '''+s[b:]
s=s.replace('vv,JJ,gg=s.evaluate(zz)','vv,JJ,gg=evaluate(zz)')
# Restore the wrapper's base call, avoiding accidental recursive evaluation.
s=s.replace("def evaluate(zz):\n  vv,JJ,gg=evaluate(zz)","def evaluate(zz):\n  vv,JJ,gg=s.evaluate(zz)")
s=s.replace("centroid=gg['g'].tolist())","centroid=gg['g'].tolist(),actual_bad_escape=float(vv[-1]))")
s=s.replace('s.floor[slot]=initial+(a.gamma-initial)*target','floor[slot]=initial+(a.gamma-initial)*target')
s=s.replace('desired=s.floor+np.maximum(abs(s.floor)*.01,1e-13)','desired=floor+np.maximum(abs(floor)*.01,1e-13)')
s=s.replace('desired[slot]=s.floor[slot]','desired[slot]=floor[slot]')
s=s.replace('s.residual(zz','residual(zz').replace('vv-s.floor','vv-floor').replace('JJ/s.rescale[:,None]','JJ/rescale[:,None]').replace('(desired-vv)/s.rescale','(desired-vv)/rescale')
s=s.replace("status['numerical_own11_candidate']=status['mechanical_minimum']>0 and status['slack']>0 and status['v6minimum']>0;","status['numerical_rerouting_complete']=status['mechanical_minimum']>0 and status['actual_bad_escape']>0 and status['slack']>0 and status['v6minimum']>0;")
s=s.replace('CONTACT_HOMOTOPY_STAGE','PREROUTE_STAGE').replace('CONTACT_HOMOTOPY_FINITE_DONE','PREROUTE_BEFORE_CONTACT_FINITE_DONE')
Path(sys.argv[2]).write_text(s);print('PREROUTE_SOURCE_RECOVERED',len(s.encode()),hashlib.sha256(s.encode()).hexdigest())
```
