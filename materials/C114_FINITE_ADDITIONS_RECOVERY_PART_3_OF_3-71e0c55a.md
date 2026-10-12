# material-71e0c55a013b

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# C114_FINITE_ADDITIONS — Recovery capsule part 3/3

All three parts together are self-contained. Part1 [internal-source-reference], part2 [internal-source-reference], then this part. No previous sandbox is required. All four new rational solids have V22/E60/F40,C120, all22 points extreme, all40 maximal faces triangular, weak000/primitivezero000. ADDED_G4/G5/G6 are distinct own233 bodies with common centered denominators59/65/69bits. CENTERED_G6 is distinct own222,85bits; its rational centroid is small NONZERO, unlike the numerically centered precursor. Parent remains VL12_DUAL_CANCEL21_G4 own211/C114, and accepted own110 remains C622.

Exact full-basin results, intervals [L,L+1)/10^12: parent TP=0 exactly,TQ L33906510555318; ADDED_G4 TP L1736009301780 (two positive bars),TQ L22588379983226 (one); CENTERED_G6 TP L9151794 (one),TQ L33890384006146 (one). TQ ratios to parent: ADDED_G4 L666195949193, CENTERED_G6 L999524381928. Exact root-exempt all-point cosine-hinge ratios: ADDED_G4 L109065652762, CENTERED_G6 L166266284. Thus the centered addition reduces that surrogate by more than6000-fold while decreasing the true whole polar barrier by less than0.048%, and introduces a positive physical bar. This is an exact surrogate countercontrol, not near110 or a claimed main-objective improvement. No family exclusion follows from either finite campaign.

Observed full exact replay markers: ADDITION_TETRA446_PRISM446_WEAK123_CONTROLS_PASS; C114_ADDITION_FOUR_PINNED_FREEZES_PASS; C114_FINITE_ADDITION_SOURCE_ONLY_EXACT_FIVE_BODIES_PASS 14. One mechanical implementation, distinct coordinate-boundary mass, exact primal/polar paths and complete cuts; not two independent whole-mechanics auditors. The larger original numerical ledgers are supplementary; CAMPAIGN preserves both literal terminal checkpoints, source versions, every finite nondefault/seed through source plus settings, counts and solver stops. Its old output-directory string is historical metadata, not a recovery dependency. A best visited evaluation is not necessarily the final differential-evolution x.

Reconstruction: save the three exact material texts as part1.md,part2.md,part3.md; save the following complete decoder as RECOVER.py in a clean directory. Run `python -B -S RECOVER.py part1.md part2.md part3.md`, then `cd recovered && python -B -S REPLAY.py`. Source-only replay uses Python3.13.5 standard library, no SciPy. Numerical producers require the versions in part1 and should run in a separate directory to avoid modifying the frozen inputs. The byte/hash manifest below identifies every recovery source and all14 reproduced outputs.

```python
from pathlib import Path
import sys,re,hashlib
out=Path('recovered');out.mkdir(exist_ok=True)
seen=set()
for arg in sys.argv[1:]:
 b=Path(arg).read_bytes()
 for m in re.finditer(rb'^@@FILE ([A-Za-z0-9_.-]+) ([0-9]+) ([a-f0-9]{64})\n',b,re.M):
  name=m[1].decode();n=int(m[2]);data=b[m.end():m.end()+n]
  assert len(data)==n and hashlib.sha256(data).hexdigest()==m[3].decode(),name
  assert name not in seen;seen.add(name);(out/name).write_bytes(data)
assert seen=={'cap_search.py','centered_caps.py','exact_addition.py','exact_landscape.py','INPUTS.json','CAMPAIGN.json','REPLAY.py','MANIFEST.json'},seen
print('C114_ADDITION_EIGHT_SOURCE_UNITS_RECOVERED')
```

@@FILE INPUTS.json 2578 119620735d0812e215fc7007a06ad96f96a3a63f06db3db15ac6998b20c14603
{"ADDED_G4.json":{"grid":10000,"points":[[-13513,10001,-9032],[7585,971,-5336],[9215,2535,-2766],[9859,3065,-261],[10414,1455,1511],[10533,-561,2627],[10245,-2747,3309],[9489,-4870,3884],[8292,-6612,4622],[6777,-7643,5870],[4984,-8225,7187],[2841,-8790,8032],[556,-8903,8725],[-1868,-8784,9006],[-4342,-8346,8933],[-6808,-7570,8472],[-9197,-6461,7561],[-11427,-4979,6139],[-13362,-2964,4209],[-14798,-281,1613],[-15515,3415,-2186],[-14708,23414,-34121]]},"ADDED_G5.json":{"grid":100000,"points":[[-135130,100010,-90320],[75850,9710,-53360],[92150,25350,-27660],[98590,30650,-2610],[104140,14550,15110],[105330,-5610,26270],[102450,-27470,33090],[94890,-48700,38840],[82920,-66120,46220],[67770,-76430,58700],[49840,-82250,71870],[28410,-87900,80320],[5560,-89030,87250],[-18680,-87840,90060],[-43420,-83460,89330],[-68080,-75700,84720],[-91970,-64610,75610],[-114270,-49790,61390],[-133620,-29640,42090],[-147980,-2810,16130],[-155150,34150,-21860],[-147084,234136,-341209]]},"ADDED_G6.json":{"grid":1000000,"points":[[-1351300,1000100,-903200],[758500,97100,-533600],[921500,253500,-276600],[985900,306500,-26100],[1041400,145500,151100],[1053300,-56100,262700],[1024500,-274700,330900],[948900,-487000,388400],[829200,-661200,462200],[677700,-764300,587000],[498400,-822500,718700],[284100,-879000,803200],[55600,-890300,872500],[-186800,-878400,900600],[-434200,-834600,893300],[-680800,-757000,847200],[-919700,-646100,756100],[-1142700,-497900,613900],[-1336200,-296400,420900],[-1479800,-28100,161300],[-1551500,341500,-218600],[-1470844,2341363,-3412090]]},"CENTERED_G6.json":{"grid":1000000,"points":[[-1351126,994582,-904180],[758561,92733,-536367],[920470,249022,-278533],[983832,301709,-27962],[1039308,140858,149082],[1051621,-60591,260689],[1023462,-279258,329059],[948436,-491892,386806],[828980,-666493,460847],[677264,-769667,585758],[497635,-827714,717414],[283123,-884161,801895],[54444,-895255,871037],[-188038,-883182,898980],[-435428,-839208,891507],[-681925,-761455,845242],[-920656,-650459,754027],[-1143455,-502232,611784],[-1336677,-300760,418792],[-1479942,-32596,159301],[-1551375,336697,-220302],[95234,140228,92831]]},"parent.json":{"grid":10000,"points":[[-13513,10001,-9032],[7585,971,-5336],[9215,2535,-2766],[9859,3065,-261],[10414,1455,1511],[10533,-561,2627],[10245,-2747,3309],[9489,-4870,3884],[8292,-6612,4622],[6777,-7643,5870],[4984,-8225,7187],[2841,-8790,8032],[556,-8903,8725],[-1868,-8784,9006],[-4342,-8346,8933],[-6808,-7570,8472],[-9197,-6461,7561],[-11427,-4979,6139],[-13362,-2964,4209],[-14798,-281,1613],[-15515,3415,-2186]]}}

@@END

@@FILE CAMPAIGN.json 8325 a09c8c5bc712da530bae1f7b602975321c127f26a8f44dcc7cc0c2e3314edd15
{"projectively_centered_addition":{"best_visited_not_final_de_endpoint":{"center_iterations":2,"cost":0.002010412353038298,"geometry":{"E":60,"F":40,"Pbars":[{"birth":0.87170332395376,"death":0.8716950824682582,"depth":8.241485501825352e-06,"edge":[1,2],"elder":0,"peak":1}],"Qbars":[{"birth":39.44158540062686,"death":1.820539242546352,"depth":37.62104615808051,"edge":[0,1],"elder":37,"peak":25}],"S":2,"TP":9.148692607709242e-06,"TQ":33.89044968174504,"U":2,"V":22,"active_inputs":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],"centroid":[3.08511686592633e-13,-8.484553878988464e-14,-1.284354326916572e-13],"loss":1.041235303829765e-05,"min_edge_relative":0.11646126525366918,"physical_nonroot_min":-0.0030748108045972034,"polar_nonroot_min":-0.000978719343954102,"relative_P":2.2689600833420645e-06,"relative_Q":0.9538421232992752,"stable_triangles":[[18,4,21],[17,18,1]],"unstable_inputs":[0,1],"volume":0.8550070482761176},"physical_points":[[-1.3511255445790646,0.9945820881915584,-0.9041795055157387],[0.7585610080128473,0.09273282971615925,-0.5363666128402447],[0.9204695642047938,0.24902192634180476,-0.2785334324383955],[0.9838318893388728,0.30170919300170407,-0.027962294784674387],[1.0393077329702227,0.1408575097720654,0.149082004525789],[1.0516211281764647,-0.060590556774136335,0.26068943957750895],[1.0234618046420296,-0.2792584930836617,0.32905887006192214],[0.9484362080995643,-0.4918918228525081,0.3868055733001234],[0.8289796715801857,-0.666492604265852,0.46084732476100526],[0.6772640728928443,-0.7696674013161291,0.5857580821736341],[0.49763512816374755,-0.827713515934787,0.7174143522047342],[0.2831233395939989,-0.884161437710873,0.8018950415533923],[0.054444201919486436,-0.895255389120113,0.87103695214513],[-0.18803833085469068,-0.8831822076625365,0.8989802765962024],[-0.43542831569915624,-0.8392078013438884,0.8915066887782083],[-0.681925093651453,-0.7614552580614399,0.845241589727096],[-0.9206558204337579,-0.6504591353756939,0.7540270186095901],[-1.143455121395279,-0.5022315276225292,0.6117839615669071],[-1.3366768622884286,-0.3007604321175343,0.4187915020253964],[-1.4799424375182733,-0.032596261959261914,0.15930059624192686],[-1.5513751232533002,0.33669712991956735,-0.2203018419617305],[0.09523428359871959,0.1402282406763397,0.09283053222649379]],"point":[0.0953156121232853,0.14034799330622988,0.0929098079866018],"projective":[-0.0001867734574511242,0.003912384054456554,0.0034731625066217143],"tag":"de_2026092041"},"counts":{"10,11":2,"10,4":1,"12,4":1,"13,11":1,"14,11":1,"14,4":1,"2,1":559,"2,10":202,"2,11":251,"2,12":120,"2,13":73,"2,14":96,"2,15":15,"2,2":684,"2,3":177,"2,4":125,"2,5":65,"2,6":176,"2,7":136,"2,8":888,"2,9":362,"3,1":6,"3,10":82,"3,11":83,"3,12":64,"3,13":44,"3,14":70,"3,15":41,"3,16":3,"3,2":64,"3,3":38,"3,4":103,"3,5":66,"3,6":71,"3,7":65,"3,8":570,"3,9":180,"4,10":27,"4,11":49,"4,12":36,"4,13":29,"4,14":20,"4,15":11,"4,2":7,"4,3":8,"4,4":44,"4,5":32,"4,6":13,"4,7":17,"4,8":42,"4,9":69,"5,10":7,"5,11":18,"5,12":10,"5,13":14,"5,14":5,"5,15":1,"5,3":1,"5,4":8,"5,5":5,"5,6":1,"5,7":1,"5,8":4,"5,9":44,"6,11":10,"6,12":1,"6,13":3,"6,14":1,"6,15":1,"6,4":9,"6,5":1,"7,11":3,"7,12":1,"7,4":5,"7,5":1,"8,11":1,"8,4":5,"9,11":1,"9,4":2},"de":[{"fun":0.002013698527394243,"message":"Maximum number of iterations has been exceeded.","nfev":2818,"nit":80,"seed":2026092041,"success":false,"x":[0.09529264084268974,0.14045009495827365,0.09294284467960591]},{"fun":0.056228261696731556,"message":"Maximum number of iterations has been exceeded.","nfev":2514,"nit":80,"seed":2026092042,"success":false,"x":[-3.594553264399089,2.9456795592830676,-3.8125593309009194]}],"fail":78,"number_improving_checkpoints":70,"original_report":{"bytes":336276,"sha256":"dfba667fa682e8de9e4460b951c55d5fb5b8d023fed61cb44b8c3bc343b46016","status":"large full chronological ledger supplementary; exact final checkpoint and producing code preserved here"},"settings":{"centroid_tol":1e-11,"maxiter":80,"newton_iterations":40,"popsize":10,"random_count":800,"random_seed":2026092044},"valid":6054,"versions":{"numpy":"2.3.5","python":"3.13.5","scipy":"1.17.0"}},"single_addition":{"best_visited_not_final_de_endpoint":{"cost":0.009826205018287265,"geometry":{"E":60,"F":40,"Pbars":[{"birth":4.295103631246922,"death":4.282323500178067,"depth":0.01278013106885556,"edge":[11,12],"elder":11,"peak":12},{"birth":4.298198388031773,"death":1.4292116857801234,"depth":2.8689867022516498,"edge":[20,21],"elder":21,"peak":11}],"Qbars":[{"birth":14.988681714697375,"death":1.3816153113422913,"depth":13.607066403355084,"edge":[1,5],"elder":17,"peak":21}],"S":2,"TP":1.7360000157879725,"TQ":22.587783584886587,"U":3,"V":22,"active_inputs":[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],"centroid":[-0.35331569190105394,0.4600118253970959,-0.6455742940833848],"loss":0.006826205018287265,"min_edge_relative":0.06285615912220689,"physical_nonroot_min":-0.060773199981235995,"polar_nonroot_min":-0.012542387783930237,"relative_P":0.23161678596580368,"relative_Q":0.46330428647416355,"stable_triangles":[[13,21,11],[4,3,0]],"unstable_inputs":[11,12,21],"volume":2.1387679667089614},"point":[-1.4708440031311503,2.341363322472921,-3.412089651169719],"tag":"de_2026092002"},"counts":{"10,10":10,"10,11":12,"10,12":7,"10,13":6,"10,14":11,"10,15":4,"10,16":3,"10,17":5,"10,4":6,"10,5":6,"10,6":11,"10,7":13,"10,8":12,"10,9":15,"11,10":6,"11,11":9,"11,12":8,"11,13":5,"11,14":6,"11,15":1,"11,16":5,"11,17":3,"11,3":1,"11,4":3,"11,5":4,"11,6":7,"11,7":12,"11,8":7,"11,9":14,"12,10":7,"12,11":4,"12,12":7,"12,13":2,"12,14":1,"12,16":3,"12,4":4,"12,5":7,"12,6":14,"12,7":12,"12,8":20,"12,9":14,"13,10":9,"13,11":6,"13,12":6,"13,13":2,"13,15":1,"13,16":2,"13,17":2,"13,5":9,"13,6":16,"13,7":13,"13,8":17,"13,9":12,"14,10":7,"14,11":1,"14,12":1,"14,13":2,"14,15":1,"14,4":1,"14,5":12,"14,6":16,"14,7":16,"14,8":11,"14,9":13,"15,10":5,"15,11":1,"15,17":2,"15,3":1,"15,4":1,"15,5":2,"15,6":8,"15,7":13,"15,8":13,"15,9":5,"16,10":5,"16,12":3,"16,14":1,"16,15":1,"16,6":3,"16,7":17,"16,8":5,"16,9":6,"17,10":2,"17,12":1,"17,7":7,"17,8":5,"17,9":7,"18,10":2,"18,11":2,"18,7":4,"18,9":1,"19,10":1,"19,8":1,"2,1":24,"2,10":12,"2,11":10,"2,12":23,"2,13":30,"2,14":16,"2,15":12,"2,16":11,"2,17":15,"2,18":11,"2,19":6,"2,2":3,"2,3":1409,"2,4":96,"2,5":61,"2,6":24,"2,7":35,"2,8":12,"2,9":13,"20,7":1,"20,8":1,"21,8":1,"3,10":19,"3,11":23,"3,12":22,"3,13":31,"3,14":30,"3,15":53,"3,16":40,"3,17":6,"3,18":5,"3,2":16,"3,3":1860,"3,4":384,"3,5":91,"3,6":44,"3,7":38,"3,8":28,"3,9":19,"4,10":15,"4,11":16,"4,12":15,"4,13":13,"4,14":13,"4,15":17,"4,16":46,"4,17":19,"4,18":3,"4,2":13,"4,20":1,"4,3":550,"4,4":196,"4,5":46,"4,6":29,"4,7":30,"4,8":23,"4,9":10,"5,10":17,"5,11":7,"5,12":6,"5,13":9,"5,14":13,"5,15":21,"5,16":40,"5,17":21,"5,18":3,"5,2":1,"5,3":41,"5,4":33,"5,5":26,"5,6":17,"5,7":13,"5,8":14,"5,9":13,"6,10":12,"6,11":7,"6,12":10,"6,13":16,"6,14":14,"6,15":9,"6,16":31,"6,17":29,"6,18":2,"6,19":1,"6,2":2,"6,3":15,"6,4":16,"6,5":17,"6,6":11,"6,7":14,"6,8":14,"6,9":9,"7,10":15,"7,11":21,"7,12":16,"7,13":23,"7,14":20,"7,15":22,"7,16":29,"7,17":39,"7,18":7,"7,19":1,"7,2":1,"7,3":7,"7,4":7,"7,5":9,"7,6":8,"7,7":13,"7,8":22,"7,9":18,"8,10":18,"8,11":19,"8,12":23,"8,13":27,"8,14":33,"8,15":18,"8,16":14,"8,17":13,"8,18":3,"8,3":3,"8,4":14,"8,5":11,"8,6":7,"8,7":11,"8,8":18,"8,9":20,"9,10":9,"9,11":21,"9,12":15,"9,13":13,"9,14":16,"9,15":9,"9,16":12,"9,17":3,"9,3":3,"9,4":11,"9,5":12,"9,6":7,"9,7":16,"9,8":17,"9,9":12},"de":[{"fun":0.00982645419774816,"message":"Maximum number of iterations has been exceeded.","nfev":2514,"nit":80,"seed":2026092001,"success":false,"x":[-1.4704250884998018,2.3416422905320995,-3.4115036971748216]},{"fun":0.009826231601484303,"message":"Maximum number of iterations has been exceeded.","nfev":2514,"nit":80,"seed":2026092002,"success":false,"x":[-1.470843424925143,2.3413642019304173,-3.412090466168925]}],"fail":0,"number_improving_checkpoints":56,"original_report":{"bytes":159949,"sha256":"95ef00b930eb3492db8052a1f5d325e8ddb64547e20edf86cad82530e6ff3e91","status":"large full chronological ledger supplementary; exact final checkpoint and producing code preserved here"},"settings":{"generations":80,"out":"/mnt/data/c114_finite_caps/results","random_count":2400},"valid":7428,"versions":{"numpy":"2.3.5","python":"3.13.5","scipy":"1.17.0"}}}

@@END

@@FILE REPLAY.py 2547 05613c8b7866b112bd3eef437f9cfdc2ab3e798eca11809d809df89d1e791009
"""Source-only exact recovery of parent and four C120 nonwinners. No optimizer required."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
from exact_addition import audit,encode,controls
from exact_landscape import run,cube_bracket,SCALE

def dump(x):return (json.dumps(encode(x),sort_keys=True,indent=2)+'\n').encode()
def receipt(p):
    b=Path(p).read_bytes();return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def replay():
    manifest=json.loads(Path('MANIFEST.json').read_text())
    for n,h in manifest['sources'].items():assert receipt(n)==h,n
    inputs=json.loads(Path('INPUTS.json').read_text());campaign=json.loads(Path('CAMPAIGN.json').read_text())
    a=campaign['single_addition']['best_visited_not_final_de_endpoint']['point']
    y=campaign['projectively_centered_addition']['best_visited_not_final_de_endpoint']['physical_points']
    p=inputs['parent.json']
    for k in [4,5,6]:
        frozen=dict(grid=10**k,points=[[z*10**(k-4) for z in row] for row in p['points']]+[[round(F(z)*10**k) for z in a]])
        assert frozen==inputs['ADDED_G'+str(k)+'.json']
    assert dict(grid=10**6,points=[[round(F(z)*10**6) for z in row] for row in y])==inputs['CENTERED_G6.json']
    controls();print('C114_ADDITION_FOUR_PINNED_FREEZES_PASS')
    for n,d in inputs.items():
        Path(n).write_bytes(json.dumps(d,separators=(',',':')).encode())
        target='PARENT_AUDIT.json' if n=='parent.json' else n[:-5]+'_AUDIT.json'
        Path(target).write_bytes(dump(audit(d['points'],d['grid'])))
    results={}
    for n in ['parent.json','ADDED_G4.json','CENTERED_G6.json']:
        r=run(inputs[n]);results[n]=r
        target='PARENT_LANDSCAPE.json' if n=='parent.json' else n[:-5]+'_LANDSCAPE.json'
        Path(target).write_bytes(dump(r))
    baseline=results['parent.json'];comp={}
    for n in ['ADDED_G4.json','CENTERED_G6.json']:
        r=results[n];loss=sum(r[k]['root_exempt_allpoint_cosine_hinge_sum'] for k in ['P','Q'])
        oldloss=sum(baseline[k]['root_exempt_allpoint_cosine_hinge_sum'] for k in ['P','Q'])
        ratio=loss/oldloss
        comp[n]=dict(TQ_ratio_bracket_1e12=cube_bracket(r['TQ_cube']/baseline['TQ_cube']),
            hinge_ratio_bracket_1e12=[int(ratio*SCALE),int(ratio*SCALE)+1],hinge_ratio=ratio)
    Path('COMPARISONS.json').write_bytes(dump(comp))
    for n,h in manifest['outputs'].items():assert receipt(n)==h,n
    print('C114_FINITE_ADDITION_SOURCE_ONLY_EXACT_FIVE_BODIES_PASS',len(manifest['outputs']))
if __name__=='__main__':replay()

@@END

@@FILE MANIFEST.json 3498 1527c44f1c60317d9680b54a153eb190871e7be3db69d0eb8106b5b4f8079be8
{
  "outputs": {
    "ADDED_G4.json": {
      "bytes": 437,
      "sha256": "1cc74f8ca565d3673bee6e175b152c9ecee5aa7ab2a9a448a54bd28c51801293"
    },
    "ADDED_G4_AUDIT.json": {
      "bytes": 9627,
      "sha256": "dcf3a823c811c0f139ddf59d3cca94e7db296c5df6e313be7bb886e15c3902d2"
    },
    "ADDED_G4_LANDSCAPE.json": {
      "bytes": 6847,
      "sha256": "9f77d04137f7bdc4b20cac3a48e0a9bc79960c0099953c7e4d321da7923ebeb5"
    },
    "ADDED_G5.json": {
      "bytes": 504,
      "sha256": "38ece413853ee03882d40bc22eab3d0af0cc75f72a658ea76df456cfa3a50c84"
    },
    "ADDED_G5_AUDIT.json": {
      "bytes": 9734,
      "sha256": "81b83264d5920520495e3fe10946cebff2a5dc2a0411c81bd0788b8a26a5affd"
    },
    "ADDED_G6.json": {
      "bytes": 571,
      "sha256": "95b76e88983589cdef9db404f47ad742739da6099b26801f96fdb0a2bd06be37"
    },
    "ADDED_G6_AUDIT.json": {
      "bytes": 9838,
      "sha256": "55118b7a3927e5ae9c05058b3805f65116a9684019be0485527dcda348838048"
    },
    "CENTERED_G6.json": {
      "bytes": 563,
      "sha256": "6bf9e4db61aa3496df7193c7f422213cef7da4a3d8910ce2fe01ee7938d6004a"
    },
    "CENTERED_G6_AUDIT.json": {
      "bytes": 10299,
      "sha256": "7d579b8fefed3af10004ba793e734c281d984cf3841db65c730fc9f4332aaa31"
    },
    "CENTERED_G6_LANDSCAPE.json": {
      "bytes": 6461,
      "sha256": "16dcfa57949b43c851e6661e081fe1d34e680678102cd56e8a51cc08dda17678"
    },
    "COMPARISONS.json": {
      "bytes": 1169,
      "sha256": "b229c2b1e40ad485deb31b4dc6005ec55bf9534a85bb6a92440dcdf0f4c0963f"
    },
    "PARENT_AUDIT.json": {
      "bytes": 9042,
      "sha256": "cca54dbd12221a955743cdb178057610539a10e0ca7fb4e775f1353ac1299735"
    },
    "PARENT_LANDSCAPE.json": {
      "bytes": 3464,
      "sha256": "1164f1dafaecd8a1e6a23739a2657c646bfad778791df6dfb3c3ee476232f60e"
    },
    "parent.json": {
      "bytes": 415,
      "sha256": "df0a606ee746a5546f046a4800f1eed5c833bf27e0fbe31d28da4984a482a6f2"
    }
  },
  "sources": {
    "CAMPAIGN.json": {
      "bytes": 8325,
      "sha256": "a09c8c5bc712da530bae1f7b602975321c127f26a8f44dcc7cc0c2e3314edd15"
    },
    "INPUTS.json": {
      "bytes": 2578,
      "sha256": "119620735d0812e215fc7007a06ad96f96a3a63f06db3db15ac6998b20c14603"
    },
    "REPLAY.py": {
      "bytes": 2547,
      "sha256": "05613c8b7866b112bd3eef437f9cfdc2ab3e798eca11809d809df89d1e791009"
    },
    "cap_search.py": {
      "bytes": 7453,
      "sha256": "9aca9b719fed5537438430f00cf62ff7cc800eb845177350219e5deb1caa48ac"
    },
    "centered_caps.py": {
      "bytes": 3842,
      "sha256": "5e9ba19596f09e0ad0825d721d7aed8c0a56cb0b4fea639ecdff5f21fc3566ce"
    },
    "exact_addition.py": {
      "bytes": 6947,
      "sha256": "130800bb8fd045a0399a04663cb193d728fbc7ed4379a6d5328ea5d4972cc079"
    },
    "exact_landscape.py": {
      "bytes": 4720,
      "sha256": "e65997173e5eb13d05d15f5a6989b4337be15aec6cc733c1a04468545ae1a964"
    }
  }
}

@@END
