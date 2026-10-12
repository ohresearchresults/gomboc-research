# material-2c9323397ca8

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J88 exact finite-event checkpoints and actual-hull wall method

## Meaning, evidence and dependencies
This complete capsule preserves three new raw rational bodies and their three exact volume-restored, centred companions. All six have V46/E132/F88,C264, additional weak000 and no Q bars. They are NOT own110.
- J88_FULL_C_G8 is own121, soleP .4472721825931315, S1 open-cube radius .0000031149465967151487. Its MASS companion has soleP .44727218265729163 and S1 radius .000003114849356229082.
- J88_BUNDLE_G10 is own(S,U,H)=(1,25,24), mainP .35884268027698113 and24 positiveP bars. MASS mainP .35884268034764477. This improved main bar does not constitute an own121 improvement; it is an exact multiroot continuation checkpoint.
- J88_WALL_C_G10 is own(1,10,9), mainP .44688667873035565 and9 positiveP bars. MASS mainP .446886678817842. Its actual fan differs from original J88_FULL_B_G8 by removing {11,18,19},{16,17,28},{17,22,28},{18,19,30} and adding {11,18,30},{11,19,30},{16,17,22},{16,22,28}. The two diagonal changes are real endpoint incidence changes, not a certified full path with fixed equilibrium counts.
All MASS companions in THIS final capsule target the original J85_DETACHED_CONTINUED_B_G12 volume V0=3791834665223904409031391864938220273/2000000000000000000000000000000000000, with centroid exactly0. Earlier ephemeral BUNDLE/WALL MASS reports used the slightly different G8 raw volume; those are superseded and are NOT the identities below. These are useful nonwinners; canonical own110 is still C622.

Save each complete fenced source/input below with its indicated filename, beside the complete J88_REPLAY.py recovered from immutable [internal-source-reference] (12483B/SHA8bfbc4d8f8e18c4e85c9f69a834b5974b285da8bcb698830a6fedf2f3e507a75). Run `python event_replay88.py`. It uses only standard-library Fraction and the complete imported exact core, enumerates actual supporting triples, checks actual homogeneous mass, strict/weak S/U/H and EVERY positive primal/polar bar, and verifies all nine input/report hashes. Observed marker: J88_EVENT_ENDPOINTS_EXACT_PASS_NO_110. The `reconstruct(name)` function returns raw points, exact mass-restored centred points, true faces and correction; no numerical optimizer is needed to reproduce any of these bodies. The full census core is the reused existing implementation, not a claimed independent second verifier.

For the new numerical wall algorithms, additionally supply complete numerical-method parts1 and2: [internal-source-reference] and [internal-source-reference], and their complete parallel.py dependency from [internal-source-reference]. The wall sources are supplementary to the completed three-part J88_NUMERICAL_METHODS capsule, not a missing fourth part of it. Their actual environment is the same CPython3.13.5/NumPy2.3.5/SciPy1.17.0/PyTorch2.10.0+cpu, float64, one thread, J88_WITNESS_FLOOR=1e-5. Numerical bars still have the old1e-14 floor; exact acceptance uses the replay without that floor.

## Wall mechanism and actual experiment
The fixed-fan rational chart supplies a derivative only. For each trial, let K be the actual convex hull with the chosen pivot removed. Its outward triangular facets have normals n_f=(b-a)cross(c-a), supports h_f=n_f dot a. The actual volume after reinserting p0+t e_k is V(K)+sum max(0,n_f dot p0-h_f+t n_f,k)/6. This is piecewise affine in t, including fan changes. Enumerate its intervals, solve target volume on each, choose a nearest eligible root, rebuild the actual hull and subtract its actual centroid. Target volume can be below V(K), in which case that pivot cannot repair it. The code checks the actual-volume residual and rejects vertex loss; its numerical tolerances do not constitute the exact theorem, whose formula and hypotheses are in [internal-source-reference].


From BUNDLE_A the trial `python wall88.py --input J88_BUNDLE_A.json --steps 3 --trust .02 --out J88_WALL_B.json` made no accepted change; all three iterations repeated the same fixed-radius LP. Actual changed-fan trials at alpha .015625,.0078125,.00390625,.000244140625 had respectively S8,S9,S5,S3, even though P-loss improved. Thus the actual S1 condition, not an old invalid volume formula, rejected them. This is a scoped negative sample, not a fan-changing impossibility theorem.

`python strictwall88.py --input J88_FULL_C.json --steps 3 --trust .01 --out J88_STRICT_WALL_A.json` stopped after one unsuccessful search, preserving own-nominated121. The model retains all old nonroot primal witnesses but removes retired diagonal convexity constraints; the final actual-mass check still requires S1 and U<=2. It did not produce a new endpoint. The underlying exact FULL_C input and the producing fullchart command are preserved in the prior capsule. The complete strictwall patch below is deterministic and imports the literal complete wall function; it is not an omitted helper.

## J88_FULL_C_G8_INPUT.json —1430B/SHA2460fe721517acd3564b2b80709de47d4adac4f53f77c3323c6c023c7889b718
```json
{"denominator":100000000,"name":"J88_FULL_C_G8","points":[[-150604932,-96540423,67441653],[-85283974,-10769301,-53633535],[-66896463,10440997,33896392],[-58177345,26507080,24287123],[-56161233,34237446,-2264123],[-54615858,1152174,-75601477],[-55615371,34325903,-12894710],[-37587176,4263643,-83140263],[-38617951,49519084,5494780],[-30613085,52812896,-24077729],[-21712702,4158264,-87101657],[-10994091,4088623,-88436951],[-15255550,51401298,35888395],[-7844566,75133223,-15437521],[-7596860,78213846,-579936],[-908671,4391220,-88524940],[3544482,70873298,-25633083],[3574151,79421415,15789759],[9179437,1889945,-87518445],[6644599,-36103107,-43424585],[12415650,59703852,-35827871],[18562523,474174,-85488765],[18492532,78037080,35645898],[18860647,50361527,-43167755],[24090429,73458692,40942314],[28806222,45310306,53013369],[33694472,71381314,45128426],[44444247,69577455,48342179],[67790145,63407842,52289026],[76572376,57055041,52862818],[77852657,-21843520,-65607076],[83051714,48846928,52364377],[89499225,39950428,50445216],[91076613,49726445,27669611],[95505252,30851878,47049574],[99521171,14019594,-43579804],[100859283,21749414,42155830],[105594137,25655157,-16197540],[105703315,12472222,35354051],[109365328,4040612,27380073],[112501068,-20285983,-25010949],[113847404,-16778412,-8037284],[112213762,-4118157,17207796],[113766335,-11184540,5394655],[114753942,-10181541,-13334280],[83886242,-28735538,-27558190]]}
```

## J88_BUNDLE_G10_INPUT.json —1710B/SHA97fd236ac547eda139868185f0c47a32940180d32d669c7107a199dd4a1dfce1
```json
{"denominator":10000000000,"name":"J88_BUNDLE_G10","points":[[-15461280434,-9654064496,6605084204],[-8143790394,-524403081,-4825974188],[-6894501772,1085150027,3169588907],[-5611661002,2882414651,2316170352],[-5655115770,3346641921,-135992187],[-5325739154,515632287,-7313052686],[-5536627100,3423024893,-1121107345],[-3688629795,761124942,-8236628265],[-3925714385,4894427377,503625964],[-3252156729,5206953268,-2186314964],[-2192821946,633797133,-8747139326],[-1125258900,582866673,-8930213097],[-1658835758,5127438726,3487332252],[-1197573021,7273643580,-1348366878],[-1200732263,7475566181,-204729794],[173746628,527498466,-9036481798],[353805853,7166293889,-2330335677],[-21555795,7652632890,1500364138],[875772186,282490309,-9031994884],[-10078565,-3792212847,-4030643049],[1175510718,6153337162,-3301791614],[1795247687,85518429,-8890270843],[1436460175,7519255388,3517741517],[1836612709,5154827221,-4158457399],[2116963569,7221179192,4037445202],[2423087344,4615073493,5249650291],[3133789435,7108378864,4462671663],[4195504262,6957967354,4804952420],[6503182030,6508086591,5248332311],[7715836729,6099327777,5338331615],[7900857997,-2134275712,-6850877145],[8389963362,5255552376,5334423140],[8977034115,4325871107,5196116824],[8966091869,5258047810,3317274056],[9540739079,3372577143,4907016196],[9176499789,1555378448,-4707913015],[10040477786,2378720065,4447752377],[10357400872,2762006925,-1333232901],[10480608869,1418174388,3824542513],[10820356760,487936840,3027754274],[10787703268,-2176459212,-2302793572],[11083213024,-1762934821,-441377647],[11040826030,-336199235,2115547641],[11149119152,-1100377446,985319633],[11151410226,-917855494,-1136013515],[8704304722,-2786392062,-2758491697]]}
```

## J88_WALL_C_G10_INPUT.json —1710B/SHAf63dacd9f75f4ec6c0fcdb60e00a56b468a769c9c0d4828d3f006cdc752ff7d5
```json
{"denominator":10000000000,"name":"J88_WALL_C_G10","points":[[-15071224857,-9656466511,6741353859],[-8520382314,-1063829004,-5361451298],[-6701968376,1032818622,3387708715],[-5833477876,2641524407,2420943215],[-5611447261,3426880811,-224241222],[-5455203314,125739572,-7554617398],[-5557029974,3435710346,-1293279295],[-3770755214,431570779,-8303559362],[-3870107373,4942287637,553632878],[-3052099576,5288618152,-2407831398],[-2177020114,422555585,-8702567298],[-1112237514,415068566,-8836857598],[-1542681085,5132792908,3583129409],[-787328122,7510607005,-1540423735],[-765386276,7816176242,-59186914],[-105476338,445016506,-8847308498],[352561186,7087860741,-2560035022],[351342000,7937448817,1581146978],[893386121,196238708,-8750479344],[674219279,-3599981125,-4364900798],[1238828104,5965522134,-3586609960],[1831907562,49724746,-8554480161],[1835971776,7803402802,3557546638],[1879604559,5038759221,-4315306886],[2403293963,7341138844,4093764510],[2852447024,4546080708,5296245424],[3353733310,7140689608,4507643008],[4438637086,6960486208,4832364574],[6748651462,6357671808,5227761643],[7632699462,5719828708,5288638778],[7766977562,-2186205005,-6577950061],[8300326662,4880926489,5237450978],[8935238962,4002793126,5050267478],[9087259440,4989472308,2774894965],[9543255162,3087276930,4708770178],[9936724642,1395485107,-4383321244],[10083951562,2171096756,4215283178],[10554767962,2569073486,-1626161498],[10565575104,1247587730,3538957159],[10940651304,389335247,2721757320],[11241757842,-2027957333,-2517564440],[11379642821,-1678868761,-801170980],[11217605204,-412859849,1723276720],[11373982904,-1121509557,535706520],[11471206985,-1014290220,-1336765440],[8353750100,-2877498668,-2759472398]]}
```

## event_replay88.py —2427B/SHAf6ed4ef4d1299a765000d5e8f5cdf829dacd4d1517959f7fb3fc38c755436b0e
```python
"""Exact event checkpoints. Requires complete J88_REPLAY.py and three literal inputs.
No numerical optimizer or NumPy is needed. All MASS bodies target the original
J85_DETACHED_CONTINUED_B_G12 volume, not the slightly different G8 raw volume.
"""
from J88_REPLAY import R,V0,exact_hull,audit,cube,correct,dump,ROOT
import json,hashlib
EXPECTED={'J88_FULL_C_G8_INPUT.json':(1430,'2460fe721517acd3564b2b80709de47d4adac4f53f77c3323c6c023c7889b718'),'J88_FULL_C_G8_EXACT.json':(23260,'7ebcdbe7b00ecb12006a9336ffeec6db565804320f926c8b4dadada88964d39b'),'J88_FULL_C_G8_MASS_EXACT.json':(41085,'087604e991a3f102d8c7cbd7caa5aaa0ef8ab5ce7d77bd8fd07380b8a0918619'),'J88_BUNDLE_G10_INPUT.json':(1710,'97fd236ac547eda139868185f0c47a32940180d32d669c7107a199dd4a1dfce1'),'J88_BUNDLE_G10_EXACT.json':(43228,'7e855431f251238c979ac9db9e204cd21f268d3f20b8febd534ae51a388208db'),'J88_BUNDLE_G10_MASS_EXACT.json':(67341,'a4802e580c676b5f7a7763fadd799d5a5b106fcf048c1b387f09c8507f2e9346'),'J88_WALL_C_G10_INPUT.json':(1710,'f63dacd9f75f4ec6c0fcdb60e00a56b468a769c9c0d4828d3f006cdc752ff7d5'),'J88_WALL_C_G10_EXACT.json':(33511,'140a5eab36d2eeb8951ad6d3dd9694a91536790284ec1610bbf2a0bd7c0d746e'),'J88_WALL_C_G10_MASS_EXACT.json':(51804,'b55e44999f25471c0329e082df0d7a242219f4c1f5b019517517016c0e7f1f69')}

def reconstruct(name):
    d=json.loads((ROOT/(name+'_INPUT.json')).read_text())
    p=[tuple(R(z,d['denominator']) for z in row) for row in d['points']];f=exact_hull(p)
    q,co=correct(p,f,V0)
    return p,q,f,co

def main():
    for name,counts in [('J88_FULL_C_G8',[1,2,1]),('J88_BUNDLE_G10',[1,25,24]),('J88_WALL_C_G10',[1,10,9])]:
        p,q,f,co=reconstruct(name)
        for points,suffix in [(p,''),(q,'_MASS')]:
            r=audit(points,f);r['name']=name+suffix
            if suffix:r.update(correction=co,faces=f)
            r['S1_cube']=cube(points,f)
            assert r['strict']==counts and r['weak']==[0,0,0] and not r['Q']
            assert (r['V'],r['E'],r['F'])==(46,132,88)
            if suffix:assert R(r['volume'])==V0 and r['centroid']==['0','0','0']
            dump(name+suffix+'_EXACT.json',r)
            print(name+suffix,r['strict'],r['weak'],len(r['P']),float(R(r['P'][0]['depth'])))
    for name,(n,h) in EXPECTED.items():
        raw=(ROOT/name).read_bytes();assert (len(raw),hashlib.sha256(raw).hexdigest())==(n,h),name
    print('J88_EVENT_ENDPOINTS_EXACT_PASS_NO_110')
if __name__=='__main__':main()
```

## wall88.py —4508B/SHAeeeeb9df1465ec595adea7206b18be8eeb42ac5c5bd18fba278e5905f7364f2d
```python
"""Fan-changing S1 flow with actual-hull piecewise-affine volume retraction.
The fixed-fan chart supplies only a local search derivative. Trial points are
retracted using the actual hull of all other vertices, then recentered using
actual homogeneous mass. This is numerical nomination, not exact certification.
"""
from s1flow88 import *
from scipy.spatial import ConvexHull,QhullError

class WallModel(S1Model):
    def rawguards(self,z):
        allg=super().rawguards(z)
        # Retired diagonal convexity conditions must not be continued as guards.
        return torch.cat([allg[:len(self.iq)+2],allg[-len(self.f):]])

def actual_retract(raw,pivot,V0):
    a,k=pivot;others=np.delete(raw,a,axis=0);f=hull(others);VK,_=mass(others,f)
    if VK>V0+1e-12:return None,dict(error='target below pivot-removed hull')
    tri=others[f];n=np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]);h=np.einsum('ij,ij->i',n,tri[:,0])
    A=n@raw[a]-h;B=n[:,k];breaks=np.unique(-A[abs(B)>1e-14]/B[abs(B)>1e-14]);bounds=np.r_[-np.inf,breaks,np.inf];roots=[]
    for lo,hi in zip(bounds[:-1],bounds[1:]):
        sample=(lo+hi)/2 if np.isfinite(lo+hi) else (hi-max(1,abs(hi)) if not np.isfinite(lo) else lo+max(1,abs(lo)))
        active=A+B*sample>0;c=VK+A[active].sum()/6;b=B[active].sum()/6
        if abs(b)<1e-16:
            if abs(c-V0)<1e-13:roots.append(float(np.clip(0,lo,hi)))
        else:
            t=(V0-c)/b
            if lo-1e-12<=t<=hi+1e-12:roots.append(float(t))
    if not roots:return None,dict(error='no target-volume root')
    for t in sorted(roots,key=abs):
        pp=raw.copy();pp[a,k]+=t;ff=hull(pp)
        if len(np.unique(ff))!=len(pp):continue
        v,g=mass(pp,ff)
        if abs(v-V0)>1e-10:continue
        return pp-g,dict(pivot=list(pivot),correction=t,relative_volume_error=float((v-V0)/V0),candidates=len(roots))
    return None,dict(error='volume roots lose vertices')

def wallstep(p,trust=.01,power=2):
    f=hull(p);v0,g=mass(p,f);e,_=edges(f);bs,_=bars(p-g,e);bs.sort(reverse=True)
    if not bs:return p,{'target':True}
    m=WallModel(p,bs,power);z0=np.zeros(len(m.free));v,J=m.vg(z0);z=torch.tensor(z0,requires_grad=True);old=m.objective(z);old.backward();gg=z.grad.numpy()
    r=linprog(gg,A_ub=-J,b_ub=v*.95,bounds=[(-trust,trust)]*len(z0),method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    out=dict(initial=float(old),power=power,pivot=m.pivot,lp_success=bool(r.success),predicted=None if r.fun is None else float(r.fun))
    if not r.success:return p,out
    trials=[]
    for k in range(16):
        alpha=2.**-k;zz,ok,ns=restore(m,alpha*r.x,trust*alpha*.5)
        if not ok:continue
        raw=m.points(torch.tensor(zz)).numpy()
        try:
            pp,repair=actual_retract(raw,m.pivot,v0)
            if pp is None:trials.append(dict(alpha=alpha,repair=repair));continue
            rr=report(pp);loss=sum(b[0]**power for b in rr['P'])
            newfan={tuple(sorted(map(int,t))) for t in hull(pp)};oldfan={tuple(sorted(map(int,t))) for t in f}
            trials.append(dict(alpha=alpha,S=len(rr['S']),U=len(rr['U']),loss=loss,changed=len(newfan-oldfan)))
            if len(rr['S'])==1 and not rr['Q'] and loss<float(old)-1e-11:
                out.update(alpha=alpha,restore=ns,loss=loss,params=zz.tolist(),actual=rr,repair=repair,removed=sorted(oldfan-newfan),added=sorted(newfan-oldfan),trials=trials)
                return pp,out
        except (QhullError,FloatingPointError,ValueError):continue
    return p,dict(out,alpha=0,loss=float(old),trials=trials)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='J88_FULL_B_G8_INPUT.json');ap.add_argument('--out',default='J88_WALL.json');ap.add_argument('--steps',type=int,default=3);ap.add_argument('--trust',type=float,default=.01);ap.add_argument('--power',type=int,default=2);a=ap.parse_args();d=json.load(open(ROOT/a.input));p=np.array(d['points'],float)/d.get('denominator',1);hist=[];start=time.monotonic()
    for k in range(a.steps):
        p,r=wallstep(p,a.trust,a.power);hist.append(r);rr=report(p)
        (ROOT/a.out).write_text(json.dumps(dict(points=p.tolist(),parameters=vars(a),history=hist,final=rr),sort_keys=True,indent=2)+'\n')
        print(k,{k:v for k,v in r.items() if k not in ['params','actual','trials','removed','added']},'flips',len(r.get('added',[])),'U',len(rr['U']),'P',rr['P'][:3],'seconds',time.monotonic()-start,flush=True)
        if r.get('target'):break
if __name__=='__main__':main()
```

## strictwall88.py —1993B/SHA69b38d0b87821b08163cb71816d8bfbc9ca0ca934b57e47850226d93a559b28c
```python
"""Same actual-hull wall retraction, retaining numerical own121 or better.
A trial must retain S1 and at most two primal roots after actual mass repair.
Neither this quota nor floating signs constitute the exact endpoint census.
"""
from wall88 import *
class StrictWallModel(Model):
    def __init__(self,p,bs,power=2):
        self.power=power
        super().__init__(p,[bs[0][0],bs[0][1],*bs[0][2]])
    def rawguards(self,z):
        allg=super().rawguards(z);count=len(self.ip)+len(self.iq)+2
        return torch.cat([allg[:count],allg[-len(self.f):]])
    def objective(self,z):return super().objective(z)**self.power

# Explicit version of the wallstep algorithm, changing the model and own quota.
import inspect
src=inspect.getsource(wallstep).replace('def wallstep(', 'def strictstep(').replace('m=WallModel(p,bs,power)', 'm=StrictWallModel(p,bs,power)').replace("if len(rr['S'])==1 and not rr['Q'] and loss<float(old)-1e-11:","if len(rr['S'])==1 and len(rr['U'])<=2 and not rr['Q'] and loss<float(old)-1e-11:")
exec(compile(src,'strictwall88:strictstep','exec'))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='J88_FULL_B_G8_INPUT.json');ap.add_argument('--out',default='J88_STRICT_WALL.json');ap.add_argument('--steps',type=int,default=3);ap.add_argument('--trust',type=float,default=.01);a=ap.parse_args();d=json.load(open(ROOT/a.input));p=np.array(d['points'],float)/d.get('denominator',1);hist=[];start=time.monotonic()
    for k in range(a.steps):
        p,r=strictstep(p,a.trust,2);hist.append(r);rr=report(p)
        (ROOT/a.out).write_text(json.dumps(dict(points=p.tolist(),parameters=vars(a),history=hist,final=rr),sort_keys=True,indent=2)+'\n')
        print(k,{k:v for k,v in r.items() if k not in ['params','actual','trials','removed','added']},'flips',len(r.get('added',[])),'U',len(rr['U']),'P',rr['P'],'seconds',time.monotonic()-start,flush=True)
        if r.get('target') or r.get('alpha')==0:break
if __name__=='__main__':main()
```
