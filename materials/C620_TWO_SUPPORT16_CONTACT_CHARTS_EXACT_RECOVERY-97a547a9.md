# material-97a547a9e033

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# Two distinct C620 support16 contact charts — complete exact recovery

## Established construction and scope
Two contact charts obtained by merging different simple edges of COORD_C622_CONDITION25_G12 each have V175/E310/F137,C620,strict(S,U,H)=(1,3,2),weak000,all137 supports active. Both completed exhaustive independent exact A and B with byte-identical output, then third own-centered integration with346positive tetrahedra and exactly zero first moments. They are distinct NONWINNERS, not own110 and not aliases of the support99/117 contact charts. They preserve the unique stable face3 but create two extra unstable equilibria.

COORD_C620_F16_EDGE82_84_KEEP82: S3,U[82,87,93],H[[82,85],[87,92]],common centered denominator57285bits. GENERATOR11932bytes SHA14d0681119a85ac420a887505a234fa84ed25c2b868b16f8bc404c06ecee0dc8;RAW15727SHAf8ef7e1d3e5562fccf03e403ed624dd7df7943a9385720df843307a8fde857f2;A=B314431SHA3b77c243a631f646035c4c34b61692edde52ab4416cdcd237044e17e3086c343;MASS223SHAe4725eab3e0b8a45867577ad15d7d5d83ce6ca248fc0f118b3b29df2d417a1b3.

COORD_C620_F16_EDGE90_93_KEEP93: S3,U[84,86,93],H[[84,86],[86,92]],common centered denominator57576bits. GENERATOR11927bytes SHA980bc662f735e4a3c39ceb43056b291bb6ebee678531f414e601f6ee4771c45c;RAW15818SHA8d08186a8af81574d6cfc22d51cc16b5e34ce040665c07e0fa770f180b3f4000;A=B315947SHAe08d0048e9f8e15e9083ffc5dc0823c98bd1d2c8ae4737f941c286530707458a;MASS223SHA685e3ebeb66e5cb2535cc5b7957198e16f8fcf1b060cee86a871937d2e0d29b5.

Edge labels in object names are from the original CONDITION25 parent; equilibrium labels above belong to each child's independently reconstructed raw-lex ordering. The new point180 is solved by three existing support equations. Support16 is then solved on axes[2,0] using point152 and point180. Its y coordinate remains free. All original contact equations and exact DAG dependencies remain in the recovered generator. This is exact contact, not approximate coplanarity.

## Complete input closure and verification command
Decode the standalone CONDITION25 ALL THREE materials [internal-source-reference],[internal-source-reference],[internal-source-reference] into source/. Their materialSHA values are20469536cc4461b597cd92b9c7420b89ad4f1efd82ef72aa4f934b9bb772067a,a527d91c2ba70ee5220ca4b6ba30964e804fd4fa52a8619d3ae6567608cc8087,ecb59180686fbea53343e4b78e64b70478df5ede3679acd200c163185c1e29d4. These contain the exact parent GENERATOR11841bytes SHA8b8c74c7995098ff531e5d7652da20c1afa9cbaefaeea42cd78ea54e3e7e86f5 and all independent reconstruction/audit source. No other source material, numerical screen, original sandbox or worker result is needed to reconstruct the exact two bodies.

Save RECOVER_TWO_F16_CHARTS.py below with its final newline:3066bytes SHA1576855d1c44fe3c6bb69dc59e7cb5d9c42982af2047295adb82f3145033d184. Save the complete TWO_F16_INPUTS.json literal WITHOUT a final newline:690bytes SHAfe26f35e349645d11b5c0f24af0e45e25f11b6f38182994f3b4374aa9bf82cbf.
Run python -B -S RECOVER_TWO_F16_CHARTS.py --source source --inputs TWO_F16_INPUTS.json --out fresh_output --workers 2. CPython3.13.5,standard library only,assertions enabled. Expected terminal TWO_SUPPORT16_CONTACT_CHARTS_EXACT_AB_MASS_PASS and fresh_output/RECEIPT.json1427bytes SHA347cf972e730b899d40de4bc9e80caca87f86d74b42201d2ccaca5a4c61053f0. This exact command completed with its terminal, output bytes and hashes in the producing coordinator turn. Each body directory contains G,RAW,A,B,MASS,RECEIPT. The full numerical factory that selected these contact control values is separate evidence; the complete frozen input deltas below define the exact constructions.

### RECOVER_TWO_F16_CHARTS.py
```python
"""Deterministic exact regeneration of two different support16 contact charts.
Complete frozen control deltas are supplied in INPUTS.json; no numeric search
or original sandbox is needed. Charts remain nonwinners unless exhaustive
independent own-centroid A/B and mass checks say otherwise.
"""
import argparse,copy,hashlib,json,sys,subprocess,concurrent.futures
from pathlib import Path
sys.set_int_max_str_digits(0)
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
H=lambda b:hashlib.sha256(b).hexdigest()
def sort_plan(rows,root):
 todo={i:[i,d,ax] for i,d,ax in rows};done={root};out=[]
 while todo:
  ready=sorted(i for i,(_,d,_) in todo.items() if set(d)<=done);assert ready,'contact DAG cycle'
  for i in ready:out.append(todo.pop(i));done.add(i)
 return out
def main():
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);p.add_argument('--inputs',type=Path,required=True);p.add_argument('--out',type=Path,required=True);p.add_argument('--workers',type=int,default=2);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False);sys.path.insert(0,str(a.source/'methods/parent'));import RECONSTRUCT,centred_mass
 gb=(a.source/'GENERATOR.json').read_bytes();assert H(gb)=='8b8c74c7995098ff531e5d7652da20c1afa9cbaefaeea42cd78ea54e3e7e86f5';G0=json.loads(gb);spec=json.loads(a.inputs.read_text())
 def one(name,x):
  G=copy.deepcopy(G0);f=x['support'];k=len(G['controls']);assert k==180;G['controls'][f]=x['support_controls'];G['controls'].append(x['point_controls']);G['groups'].append(x['new_group']);G['plan']=sort_plan([row if row[0]!=f else x['new_support_plan'] for row in G['plan']]+[[k,x['point_owners'],[0,1,2]]],G['n_supports']);b=B(G);assert H(b)==x['generator_sha256'];d=a.out/name;d.mkdir();(d/'GENERATOR.json').write_bytes(b);raw=B(RECONSTRUCT.recover(G));(d/'RAW.json').write_bytes(raw)
  for which in ['A','B']:
   z=subprocess.run([sys.executable,'-B','-S',str(a.source/'methods/parent'/('check_'+which+'.py')),str(d/'RAW.json'),str(d/(which+'.json'))],capture_output=True,text=True);assert z.returncode==0,(name,which,z.stderr[-2000:])
  ab=(d/'A.json').read_bytes();assert ab==(d/'B.json').read_bytes();r=json.loads(ab);mass=centred_mass.run(r);mb=B(mass);(d/'MASS.json').write_bytes(mb);res=dict(VEF=[r[k] for k in ['V','E','F']],C=2*r['E'],strict=r['counts'],weak=r['weak'],S=r['stable_face_ids'],U=r['unstable_vertices'],H=r['saddle_edges'],all_supports_active=r['active_input_indices']==list(range(G['n_supports'])),report_bytes=len(ab),report_sha256=H(ab),raw_bytes=len(raw),raw_sha256=H(raw),mass=mass,mass_sha256=H(mb));(d/'RECEIPT.json').write_bytes(B(res));print('F16_CONTACT_EXACT_AB_MASS',name,B(res).decode(),flush=True);return name,res
 with concurrent.futures.ThreadPoolExecutor(a.workers) as pool:results=dict(pool.map(lambda p:one(*p),spec.items()))
 receipt=dict(marker='TWO_SUPPORT16_CONTACT_CHARTS_EXACT_AB_MASS_PASS',bodies=results);(a.out/'RECEIPT.json').write_bytes(B(receipt));print(receipt['marker'],len(B(receipt)),H(B(receipt)),flush=True)
if __name__=='__main__':main()
```

### TWO_F16_INPUTS.json (no final newline)
```json
{"edge82_84_keep82_support16":{"generator_sha256":"14d0681119a85ac420a887505a234fa84ed25c2b868b16f8bc404c06ecee0dc8","new_group":[16,55,94,117],"new_support_plan":[16,[152,180],[2,0]],"point_controls":[-115942395890,368757391448,-487917660397],"point_owners":[55,94,117],"support":16,"support_controls":[-132316683913,815807995773,-1401514463836]},"edge90_93_keep93_support16":{"generator_sha256":"980bc662f735e4a3c39ceb43056b291bb6ebee678531f414e601f6ee4771c45c","new_group":[16,18,56,57],"new_support_plan":[16,[152,180],[2,0]],"point_controls":[-8066404932,410714183010,-468435709701],"point_owners":[18,56,57],"support":16,"support_controls":[-18930005014,855130708237,-1384678792161]}}
```
