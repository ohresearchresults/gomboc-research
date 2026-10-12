# material-397d627f8074

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Exact six-arrow affine-metric obstruction on delete99_neighbor128

## Mathematical statement and scope
Let x_i be vertices of the exact C620 delete99_neighbor128 body, g its OWN filled-volume centroid, and R_ij = ((x_i-g)(x_j-x_i)^T + (x_j-x_i)(x_i-g)^T)/2. Under any nonsingular affine map y=A x+b the own centroid is A g+b, and the physical escape numerator from i to j becomes trace(G R_ij), where G=A^T A is positive definite.

The following six positive integer weights give a NEGATIVE DEFINITE matrix Q=sum w R_ij:
(1,6,1145658), (12,19,26105312), (56,59,20123166), (114,102,1000000), (128,144,37788589), (171,170,24394371).
Exact rational arithmetic gives signs of its three leading principal minors (-,+,-), so Sylvester's criterion makes Q negative definite. Consequently trace(GQ)<0 for every positive definite G. It is impossible for all six listed transformed escapes to be nonnegative. At the untransformed exact body the six numerator signs are(+,+,+,+,-,+): the fifth arrow is the desired escape from the unwanted unstable vertex128 toward144. Thus no affine transformation can activate this particular arrow while retaining the other five listed witnesses as nonnegative.

This is an exact retained-witness obstruction, NOT a proof that no affine transformation can produce an own110 body after changing other witnesses; NOT a projective obstruction; NOT a general geometric-deformation exclusion; and NOT a C620 lower bound. Full contact-atlas homotopies remain scientifically useful. The exact input is independently verified strict121/weak000, V175/E310/F137,C620, S3,U94/128,H128–144, not an own110 record.

## Complete recovery and verification inputs
The exact body is recovered from the complete chart construction [internal-source-reference], deletion-input helper [internal-source-reference], and CONDITION25 ALL THREE [internal-source-reference],[internal-source-reference],[internal-source-reference]. Their complete literal sources, not any originating sandbox, are sufficient. Decode into source/, run MAKE_DELETION_INPUTS.py, then CONTACT_CUT_CHARTS.py. The exact proof input contact_charts/delete99_neighbor128/A.json is316462bytes SHA290524e82efd07897aab77d1fd71537654b91f99bce3741717481a08c07ebfb0. Its GENERATOR11926bytes SHAe18ee94968df19e3894266a9bfa5c640bd6b99bf022ebe67098ada5a138d4b4e and RAW15823bytes SHA2ae5eadc2c73422a2f7a323383a672411430dbd44de276d78acacd56c5946aef are already fixed by that complete source. Independent A/B/centered-mass acceptance of the body is preserved in [internal-source-reference]; it is additional evidence, not a missing input byte dependency of this proof.

Save the full CHECK_AFFINE_TREE_CERT.py block including final newline:1821bytes SHA3ddcf66666edfb0f053c75271bc8522c98ac2eb6afad55bd0cf418e4c6cd4fcf. Run `python -B -S CHECK_AFFINE_TREE_CERT.py contact_charts/delete99_neighbor128/A.json CHECKED_AFFINE_CERT.json`. CPython3.13.5,standard library only, assertions enabled. Expected terminal EXACT_SIX_ARROW_AFFINE_OBSTRUCTION_PASS. CHECKED_AFFINE_CERT.json512bytes SHA979c4b291dada0299e06a28f08198eca398019d115a7f8f41deb5616820e9ec5. This separate standard-library check completed with the expected marker, bytes and hash in the producing coordinator turn. Its frozen six integer weights, not a numerical LP output identity, define the proof.

### CHECK_AFFINE_TREE_CERT.py
```python
"""Standard-library exact check of a six-arrow affine-metric obstruction."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
sys.set_int_max_str_digits(0)
assert __debug__
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
EXPECTED='290524e82efd07897aab77d1fd71537654b91f99bce3741717481a08c07ebfb0'
TERMS=[[1,6,1145658],[12,19,26105312],[56,59,20123166],[114,102,1000000],[128,144,37788589],[171,170,24394371]]
def main():
 assert len(sys.argv)==3,'Give delete99_neighbor128/A.json output.json'
 b=Path(sys.argv[1]).read_bytes();assert len(b)==316462 and hashlib.sha256(b).hexdigest()==EXPECTED
 r=json.loads(b);assert [r[k] for k in ['V','E','F']]==[175,310,137] and r['counts']==[1,2,1] and r['weak']==[0,0,0]
 X=[list(map(F,row)) for row in r['raw_vertices']];g=list(map(F,r['raw_centroid']));Q=[[F(0) for j in range(3)] for i in range(3)];sg=[]
 for i,j,w in TERMS:
  assert w>0 and i!=j;x=[u-v for u,v in zip(X[i],g)];d=[v-u for u,v in zip(X[i],X[j])];c=sum(a*b for a,b in zip(x,d));sg.append((c>0)-(c<0))
  for a in range(3):
   for b in range(3):Q[a][b]+=F(w,2)*(x[a]*d[b]+x[b]*d[a])
 det1=Q[0][0];det2=Q[0][0]*Q[1][1]-Q[0][1]**2;det3=Q[0][0]*(Q[1][1]*Q[2][2]-Q[1][2]**2)-Q[0][1]*(Q[0][1]*Q[2][2]-Q[1][2]*Q[0][2])+Q[0][2]*(Q[0][1]*Q[1][2]-Q[1][1]*Q[0][2]);assert det1<0 and det2>0 and det3<0 and sg==[1,1,1,1,-1,1]
 res=dict(marker='EXACT_SIX_ARROW_AFFINE_OBSTRUCTION_PASS',input_report_sha256=EXPECTED,terms=TERMS,initial_escape_signs=sg,leading_principal_minor_signs=[-1,1,-1],scope='For this exact body, no nonsingular affine transformation can keep all six listed escapes nonnegative. Witness switching and non-affine deformations are not excluded.');Path(sys.argv[2]).write_bytes(B(res));print(B(res).decode(),flush=True)
if __name__=='__main__':main()
```

## Complete numerical producer and exact frozen output
The producer searches a positive combination of the initial rooted physical witnesses whose normalized matrix sum is -I, then rounds its weights and accepts them ONLY after exact negative-definiteness checks. It is supplied for reproducibility of the method; the proof above does not rely on LP tolerances. Save AFFINE_TREE_CERTIFICATE.py3585bytes SHA239422028aff4613775cb243dd8a93de2fd8cac03d866d4c0648d7bd96166ca5. Numerical environment CPython3.13.5,NumPy2.3.5,SciPy1.17.0, BLAS/OMP1thread. Save the complete CONFIG.json literal below with no added newline,2824bytes SHA57e1cafc79c6981138ec88978a716a5b0e3e3cb7cd68372fe0e1332ee717b544. Paths in that historical config are provenance strings; the producer reads only its complete tree, and takes the real report path from --body.
Command: `python -u -B AFFINE_TREE_CERTIFICATE.py --body contact_charts/delete99_neighbor128 --config CONFIG.json --out AFFINE_TREE_CERT_99N128.json`. Expected exact frozen output below597bytes SHA41f49c36e1171f7717c89fc33022a3a46cfb9aef2922644f6f27179265412282. A different LP basis on another numerical platform may find a different valid certificate; use the frozen standard-library proof for identical acceptance.

### AFFINE_TREE_CERTIFICATE.py
```python
"""Search and EXACTLY certify retained-witness affine-metric obstructions.
A positive combination of escape matrices that is negative definite cannot
have nonnegative trace product with any positive definite affine metric G.
This excludes only the listed simultaneous witness inequalities, not arbitrary
witness switching, projective transformations, or full geometric deformation.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import linprog
sys.set_int_max_str_digits(0)
B=lambda x:json.dumps(x,sort_keys=True,separators=(',',':')).encode()
H=lambda b:hashlib.sha256(b).hexdigest()
def coef(x,d):return np.array([x[0]*d[0],x[1]*d[1],x[2]*d[2],(x[0]*d[1]+x[1]*d[0])/2,(x[0]*d[2]+x[2]*d[0])/2,(x[1]*d[2]+x[2]*d[1])/2])
def certify(r,terms):
 X=[list(map(F,row)) for row in r['raw_vertices']];g=list(map(F,r['raw_centroid']));Q=[[F(0) for j in range(3)] for i in range(3)];signs=[]
 for i,j,w in terms:
  assert isinstance(w,int) and w>0 and i!=j
  x=[u-v for u,v in zip(X[i],g)];d=[v-u for u,v in zip(X[i],X[j])];dot=sum(a*b for a,b in zip(x,d));signs.append((dot>0)-(dot<0))
  for a in range(3):
   for b in range(3):Q[a][b]+=F(w,2)*(x[a]*d[b]+x[b]*d[a])
 det1=Q[0][0];det2=Q[0][0]*Q[1][1]-Q[0][1]**2;det3=Q[0][0]*(Q[1][1]*Q[2][2]-Q[1][2]**2)-Q[0][1]*(Q[0][1]*Q[2][2]-Q[1][2]*Q[0][2])+Q[0][2]*(Q[0][1]*Q[1][2]-Q[1][1]*Q[0][2]);assert det1<0 and det2>0 and det3<0
 return dict(marker='EXACT_AFFINE_RETAINED_WITNESS_NEGATIVE_DEFINITE_PASS',leading_principal_minor_signs=[-1,1,-1],initial_escape_signs=signs,terms=terms,scope='No positive definite affine metric can make all listed escapes nonnegative. Does not exclude switching witnesses or full deformation.')
def main():
 p=argparse.ArgumentParser();p.add_argument('--body',type=Path,required=True);p.add_argument('--config',type=Path);p.add_argument('--certificate',type=Path);p.add_argument('--out',type=Path,required=True);a=p.parse_args();rb=(a.body/'A.json').read_bytes();r=json.loads(rb)
 if a.certificate:
  c=json.loads(a.certificate.read_text());assert c['input_report_sha256']==H(rb);res=certify(r,c['terms']);res['input_report_sha256']=H(rb);a.out.write_bytes(B(res));print(B(res).decode(),flush=True);return
 assert a.config;cfg=json.loads(a.config.read_text());X=np.array([[float(F(x)) for x in row] for row in r['raw_vertices']]);g=np.array([float(F(x)) for x in r['raw_centroid']]);arrows=[(int(i),j) for i,j in cfg['tree'].items()];C=np.array([coef(X[i]-g,X[j]-X[i]) for i,j in arrows]);norm=np.linalg.norm(C,axis=1);U=C/norm[:,None];fit=linprog(np.ones(len(arrows)),A_eq=U.T,b_eq=np.array([-1.,-1.,-1.,0,0,0]),bounds=(0,None),method='highs')
 if not fit.success:
  res=dict(marker='NO_NEGATIVE_IDENTITY_COMBINATION_FOUND',message=fit.message,input_report_sha256=H(rb),scope='Finite LP failed; no exclusion certificate.');a.out.write_bytes(B(res));print(B(res).decode(),flush=True);return
 ix=np.where(fit.x>1e-8)[0];w=fit.x[ix]/norm[ix];w=w/w.min();last=None
 for grid in [10**6,10**9,10**12,10**15]:
  terms=[[int(arrows[k][0]),int(arrows[k][1]),round(float(v)*grid)] for k,v in zip(ix,w)]
  try:res=certify(r,terms)
  except AssertionError:continue
  res.update(input_report_sha256=H(rb),config_sha256=H(a.config.read_bytes()),search_grid=grid);a.out.write_bytes(B(res));print(B(res).decode(),flush=True);return
 raise AssertionError('Floating candidate not converted to exact negative-definite certificate')
if __name__=='__main__':main()
```

### CONFIG.json (no trailing newline)
```json
{"bad":128,"body":"/mnt/data/condition25_research/contact_charts/delete99_neighbor128","fraction":0.05,"gamma":1e-08,"generator_sha256":"e18ee94968df19e3894266a9bfa5c640bd6b99bf022ebe67098ada5a138d4b4e","initial_bad_angle":-0.017413860507080187,"inner":30,"mode":"fixed","order":[2,0,1,3,5,6,7,8,4,9,10,12,15,19,22,24,26,28,31,34,37,38,40,42,45,50,62,66,68,65,74,75,87,88,91,95,92,89,85,83,81,77,71,64,60,51,41,36,30,27,21,17,11,13,16,14,18,20,23,25,29,32,33,35,97,101,104,107,109,112,115,118,121,122,117,111,108,105,98,70,125,126,127,129,141,139,138,135,132,131,134,137,142,143,140,136,133,130,124,120,114,102,78,72,58,49,44,43,48,54,57,61,55,53,46,39,47,52,56,59,63,67,69,73,76,79,80,82,84,86,90,93,96,99,103,106,110,113,116,119,123,128,144,145,146,147,148,149,150,151,152,154,156,157,159,160,162,164,165,167,169,172,174,173,171,170,168,166,163,161,158,155,153,100,94],"out":"/mnt/data/condition25_research/homo_delete99_neighbor128","qbound":0.01,"raw_sha256":"2ae5eadc2c73422a2f7a323383a672411430dbd44de276d78acacd56c5946aef","report_sha256":"290524e82efd07897aab77d1fd71537654b91f99bce3741717481a08c07ebfb0","restart":null,"root":94,"slot":127,"source":"/mnt/data/condition25_research/source","stages":35,"target":144,"tree":{"0":1,"1":6,"2":0,"3":10,"4":9,"5":10,"6":9,"7":11,"8":4,"9":12,"10":14,"11":13,"12":19,"13":16,"14":18,"15":22,"16":14,"17":11,"18":20,"19":24,"20":23,"21":17,"22":26,"23":25,"24":28,"25":29,"26":38,"27":21,"28":34,"29":32,"30":27,"31":38,"32":33,"33":35,"34":37,"35":39,"36":30,"37":47,"38":40,"39":47,"40":50,"41":36,"42":62,"43":48,"44":43,"45":55,"46":39,"47":52,"48":54,"49":44,"50":59,"51":41,"52":56,"53":46,"54":57,"55":53,"56":59,"57":61,"58":49,"59":63,"60":51,"61":55,"62":66,"63":67,"64":60,"65":63,"66":74,"67":69,"68":65,"69":73,"70":55,"71":64,"72":58,"73":76,"74":75,"75":80,"76":79,"77":71,"78":72,"79":80,"80":82,"81":77,"82":84,"83":81,"84":86,"85":83,"86":90,"87":86,"88":77,"89":85,"90":93,"91":96,"92":89,"93":96,"95":92,"96":99,"97":101,"98":70,"99":103,"100":94,"101":104,"102":78,"103":106,"104":109,"105":98,"106":110,"107":102,"108":105,"109":112,"110":113,"111":108,"112":115,"113":116,"114":102,"115":118,"116":119,"117":111,"118":121,"119":123,"120":114,"121":126,"122":117,"123":128,"124":120,"125":127,"126":131,"127":129,"128":144,"129":124,"130":124,"131":134,"132":131,"133":130,"134":137,"135":132,"136":133,"137":142,"138":135,"139":138,"140":136,"141":139,"142":143,"143":140,"144":145,"145":146,"146":148,"147":157,"148":149,"149":150,"150":151,"151":152,"152":154,"153":100,"154":156,"155":153,"156":157,"157":159,"158":155,"159":160,"160":162,"161":158,"162":164,"163":161,"164":165,"165":167,"166":163,"167":169,"168":166,"169":172,"170":168,"171":170,"172":174,"173":171,"174":173},"trust":0.1,"variables":313,"versions":["3.13.5","2.3.5","1.17.0"]}
```

### AFFINE_TREE_CERT_99N128.json (no trailing newline)
```json
{"config_sha256":"57e1cafc79c6981138ec88978a716a5b0e3e3cb7cd68372fe0e1332ee717b544","initial_escape_signs":[1,1,1,1,-1,1],"input_report_sha256":"290524e82efd07897aab77d1fd71537654b91f99bce3741717481a08c07ebfb0","leading_principal_minor_signs":[-1,1,-1],"marker":"EXACT_AFFINE_RETAINED_WITNESS_NEGATIVE_DEFINITE_PASS","scope":"No positive definite affine metric can make all listed escapes nonnegative. Does not exclude switching witnesses or full deformation.","search_grid":1000000,"terms":[[1,6,1145658],[12,19,26105312],[56,59,20123166],[114,102,1000000],[128,144,37788589],[171,170,24394371]]}
```
