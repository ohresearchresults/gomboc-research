# material-a91415f30d7b

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# J85 exact one-sided continuation and angular-loss control

## Identity, evidence and dependencies
This is coordinator-executed work on literal J82_S1_ROBUST_G6, not a new alias for RA40_LATTICE220 or B7. It supplies the complete exact inputs and runnable replay for three new homogeneous bodies. REQUIRED existing source dependency: [internal-source-reference], J84_EXACT_CENTRE_TRAP_AND_FINITE_CAPS.md, SHA14ccbeb81ba1242436e8ab1dfd5bb8c73026d86317e781533de57e696ed0d01c. Extract its unchanged exact84.py (6333B/SHA144a8b82a1e62ad42368a02597a79958a38bab3e320e3caa499a941588105835) and J82_S1_ROBUST_G6_INPUT.json (1153B/SHA753b899123a05588f7a566b8f08d08cc6e72636fdbd59bca5c7f465f32bea3ab). No other old optimizer, FULL76, Library file or originating sandbox is needed for exact replay. Numerical producing methods are preserved separately, not prerequisites for these exact rational objects.

All three new bodies have V45/E129/F86,C258. J85_CLASS_FIRST_G8 has own strict121,weak000, exactly one positive P depth .45742260439156845 and no Q. Its material-row labels are S16,U0/40,H21--30. Its own volume is1375960275293920889903831/750000000000000000000000. The exact centroid and all positive bar fractions are regenerated in the report. There is no claim of primitivezero000, independent-verifier status, own110, or canonical-record improvement. The accepted own110 remains C622, outside the target.

J85_CLASS_FIRST_G6 is a distinct rounding control: own strict132,weak000. Its two positive P depths are .4574223753609665 and2.2380811701356266e-12, no Q. The small positive bar is real. J85_ANGULAR_FLATTEN_G8 is own strict176,weak000, six P bars and no Q. Its largest P depth .617918930448228 is worse than the original robust body's .5678697406886946, despite substantial improvement of the worst normalized local angular witness in the numerical producer. Keeping S1 and improving angular loss alone did not cancel U and fragmented its landscape.

## Exact sufficient S1 centre-cube proof
For outward support n_i.x<=h_i and own centroid g, put a_i=h_i-n_i.g>0. For every nonroot facet choose an index j with N_ij=(n_i.n_j)a_i-|n_i|^2 a_j>0. Under reference-centre displacement d its numerator changes by B_ij.d, where B_ij=|n_i|^2 n_j-(n_i.n_j)n_i. Thus all selected guards and all support distances stay positive for ||d||inf<rho, where rho is the minimum of a_i/||n_i||1 and chosen N_ij/||B_ij||1. Positive polar arrows strictly increase squared radius; they terminate only at the one omitted root. That root must be strict: a zero root guard would imply a strictly larger-radius point, whose positive path back is impossible. Hence S1 with no weak S holds throughout this OPEN cube on the unchanged surface. This is not the largest S1 region and not a bound for changed material/facets.

freeze85.py selects the best exact witness bound separately over adjacent and all polar vertices; both give the same rho on J85_CLASS_FIRST_G8:
125689065155545167768675127001963803636369467222607/40662186112407871214889537193264285956587104807296000000 = approximately3.091055281879981e-6.
The original RA40_LATTICE220 chosen-policy rho from fully read coordinate material [internal-source-reference] is1810977069903098449612643416623101/14995203158974813283127175262943440000000, with own volume829896755263307921/500000000000000000 from fully read immutable RA40 result figure-0569,SHA0937e84dd6fe6aa357b3b5b71468fdfb93a439ff616b1f8c902fe093f94ac1a2. New rho is25.594472010566438 times that sufficient certificate; after normalizing radius by volume^(1/3), the factor is24.75422409421686. New P is about.0966587408 percent below that author's reported .4578651711005153. This compares specified certificates/endpoints, not full S1 regions, global Pareto optimality or a successful110 construction. Relative to robust J82_G6, the bar improves but the sufficient cube shrinks.

## Recovery and observed execution
Save each fenced file verbatim with its final LF in the same directory as the two required J84 source files. Run CPython3.13.5 standard library:
python replay85.py
Expected final marker: J85_THREE_RATIONAL_BODIES_AND_CENTRE_CERTIFICATES_PASS_NO_110.
The replay regenerates all true supporting faces/edges, oriented closed connected topology, positive-tetrahedron filled mass, global primal/polar root census, direct edge saddle/weak census and all positive radial bars using exact84.py. It checks the expected full output hashes. This is a source-only replay through the same exact implementation, not a second independent physics engine.
freeze85.py is included unchanged as the actual rational-freeze/cube producer. Importing it for replay needs no floating checkpoint. Running its main function instead requires the complete BAR_GUARD85_B.json point/face checkpoint supplied with the separately preserved producing methods.

## Source manifest
J85_CLASS_FIRST_G8_INPUT.json: 1435 bytes, SHA256 df634ed4bf827d133c8a5ba9b4ae656f18e3e8a59181c7a8bc67c5fdf7ecb165
J85_CLASS_FIRST_G6_INPUT.json: 1163 bytes, SHA256 7e05574bcc2f0f80f6e01018aa96a17233f2fa39e6e05f16ec64dc3cb774daf7
J85_ANGULAR_FLATTEN_G8_INPUT.json: 1429 bytes, SHA256 6df8ed78c857998e418c9e90c9a8edb722da192c88ea612d36ed45f78ff7b06c
freeze85.py: 3438 bytes, SHA256 e9822b370fc1a5292a24e9867dc7521370d968e99cc5871e63de4097fff8abf9
replay85.py: 1575 bytes, SHA256 f51c69864eced0ae2eeb28ad996dff23bc554f498581cca9c59e801f0b529877

## Reproduced output manifest
J85_CLASS_FIRST_G8_EXACT.json4943B/dba5a60bfd7f64121364dfd4f3c7899083c3ee2f90b44fc5aab6d65f680a816a
J85_CLASS_FIRST_G8_CUBE.json102402B/7f943d139235730b336b1582050fdf15143605fd0eee0ef9d8efb6ebc9159d99
J85_CLASS_FIRST_G6_EXACT.json4639B/602ddb80aa2eea5f03defd3701eaf713e52b3e8051df3d9eb7a5682632b0baaa
J85_CLASS_FIRST_G6_CUBE.json78672B/60c36846f0913b529768fc61331d3ae973a5c0e9aaf37be3889fac9103a79570
J85_ANGULAR_FLATTEN_G8_EXACT.json7576B/471cd34c8a61ab98046a14c9b8be537fda9122e2609a010e88860e0245d123b1

## J85_CLASS_FIRST_G8_INPUT.json
```json
{"denominator":100000000,"name":"J85_CLASS_FIRST_G8","points":[[-177249800,-122247600,44660000],[-110275348,-35168087,-75512362],[-96770955,-18033675,10907897],[-84635423,682344,1413670],[-81600221,9040112,-24716845],[-80625664,-23683685,-96581266],[-81103749,9031401,-35335676],[-64587787,-20890361,-103801664],[-65396693,23086766,-17159662],[-57453696,26269151,-46185744],[-48443746,-20783798,-107834809],[-38104533,-20801615,-109152253],[-42052667,25062360,13149316],[-34721827,48421131,-37601369],[-34635728,51376140,-23280438],[-27715799,-20368888,-109204797],[-23905124,44572436,-47144870],[-23226687,52701069,-6704482],[-17740389,-23018189,-108208773],[-17036004,-59318383,-69354778],[-14487538,32752145,-58081690],[-10741801,-26928922,-106797374],[-8546739,51300394,12965951],[-7810435,23207501,-65575461],[-1946405,47547996,18145529],[2118383,19670416,29956897],[7093128,45218693,22236252],[17280315,42953689,25456879],[39295179,36947571,29264732],[45690011,29587335,30020111],[50440077,-46678740,-88911555],[52743909,22023895,29572585],[60308552,14474315,27796578],[64363295,21734354,688517],[66043898,5807037,24763694],[71463171,-11537840,-66653136],[72328463,-2894751,19971546],[77871454,-1229084,-41276558],[77319260,-12229978,13300277],[81313400,-21067976,4965425],[84284778,-45276626,-50013098],[84483076,-42529612,-31030773],[84252006,-29288536,-5276602],[85910638,-36516662,-17580686],[86800156,-35521227,-36430411]]}
```

## J85_CLASS_FIRST_G6_INPUT.json
```json
{"denominator":1000000,"name":"J85_CLASS_FIRST_G6","points":[[-1772498,-1222476,446600],[-1102753,-351681,-755124],[-967710,-180337,109079],[-846354,6823,14137],[-816002,90401,-247168],[-806257,-236837,-965813],[-811037,90314,-353357],[-645878,-208904,-1038017],[-653967,230868,-171597],[-574537,262692,-461857],[-484437,-207838,-1078348],[-381045,-208016,-1091523],[-420527,250624,131493],[-347218,484211,-376014],[-346357,513761,-232804],[-277158,-203689,-1092048],[-239051,445724,-471449],[-232267,527011,-67045],[-177404,-230182,-1082088],[-170360,-593184,-693548],[-144875,327521,-580817],[-107418,-269289,-1067974],[-85467,513004,129660],[-78104,232075,-655755],[-19464,475480,181455],[21184,196704,299569],[70931,452187,222363],[172803,429537,254569],[392952,369476,292647],[456900,295873,300201],[504401,-466787,-889116],[527439,220239,295726],[603086,144743,277966],[643633,217344,6885],[660439,58070,247637],[714632,-115378,-666531],[723285,-28948,199715],[778715,-12291,-412766],[773193,-122300,133003],[813134,-210680,49654],[842848,-452766,-500131],[844831,-425296,-310308],[842520,-292885,-52766],[859106,-365167,-175807],[868002,-355212,-364304]]}
```

## J85_ANGULAR_FLATTEN_G8_INPUT.json
```json
{"denominator":100000000,"name":"J85_ANGULAR_FLATTEN_G8","points":[[-177249800,-122247600,44660000],[-105146685,-28553433,-71216111],[-101543243,-24522528,15221017],[-82162343,1897443,2324417],[-80240991,9668117,-23975225],[-78695685,-23831170,-90870086],[-81014885,8564316,-36243360],[-61006449,-20875766,-96963170],[-62161043,23904322,-17108822],[-51466899,26634804,-49541099],[-48834866,-19352933,-97988566],[-37961385,-18671094,-98498921],[-37579117,25895810,11845772],[-32273794,43978247,-42744254],[-30308619,49963013,-21970337],[-28777343,-17964297,-97986055],[-24206385,40342159,-48999276],[-19980548,50172586,-6866162],[-20766443,-21111227,-97356157],[-20006685,-55930956,-78437581],[-14627043,29323357,-57516246],[-13829143,-23776032,-96090769],[-4763219,48001477,12604543],[-4776543,17868380,-64566613],[-703161,44998742,15977903],[2999813,20351640,26269134],[5894619,42578433,19173759],[16551818,40511651,22123150],[38810515,34566715,24666541],[44797696,27276079,25057304],[47725757,-44300034,-84164557],[52521272,21400557,24217195],[60755715,15013164,22087399],[65053315,20699415,2863085],[66358144,7232053,18860391],[71598957,-10886643,-57596557],[72793915,79737,14290463],[78585754,-1078985,-33808407],[78648296,-7662995,7915082],[82729073,-15712954,-81176],[90145420,-36030115,-48499715],[82054777,-36229710,-34027631],[86264202,-23033146,-9931620],[89272332,-29116940,-21588729],[91861388,-32929185,-40571585]]}
```

## freeze85.py
```python
"""Exact rational endpoints and fixed-surface S1 centre-cube certificates.
Requires unchanged exact84.py and the selected full JSON checkpoints. This script
is an endpoint audit, not a proof of any floating optimization trajectory.
"""
import json,hashlib
from fractions import Fraction as R
from exact84 import ROOT,load,audit,topology,mass,dot,sub

def cube(P,F):
    edges,planes=topology(P,F);V,g=mass(P,F);adj=[set() for _ in F]
    for ee in edges.values():a,b=ee[0][0],ee[1][0];adj[a].add(b);adj[b].add(a)
    a=[h-dot(n,g) for n,h in planes];ns=[n for n,h in planes]
    qs=[tuple(t/aa for t in n) for n,aa in zip(ns,a)]
    roots=[i for i,q in enumerate(qs) if max(dot(q,sub(r,q)) for j,r in enumerate(qs) if j!=i)<0]
    if len(roots)!=1:return None
    root=roots[0];interior=min(aa/sum(abs(t) for t in n) for n,aa in zip(ns,a));out={}
    for kind in ['adjacent','global']:
        bounds=[interior];policy=[]
        for i,n in enumerate(ns):
            if i==root:continue
            choices=[]
            for j in (adj[i] if kind=='adjacent' else range(len(ns))):
                if i==j:continue
                nn=dot(n,n);nm=dot(n,ns[j]);N=nm*a[i]-nn*a[j]
                if N<=0:continue
                B=tuple(nn*ns[j][k]-nm*n[k] for k in range(3));L=sum(abs(t) for t in B)
                assert L>0;choices.append((N/L,j,N,B))
            assert choices
            b,j,N,B=max(choices,key=lambda t:(t[0],-t[1]));bounds.append(b)
            policy.append({'from':i,'to':j,'bound':str(b),'N':str(N),'B':[str(t) for t in B]})
        rho=min(bounds)
        out[kind]={'rho':str(rho),'rho_float':float(rho),'rho_cubed_over_volume':str(rho**3/V),'policy':policy}
    return {'root':root,'volume':str(V),'centroid':[str(x) for x in g],'interior_bound':str(interior),'certificates':out,
            'scope':'Every reference centre in the OPEN infinity cube on THIS unchanged surface; not finite changed-surface capacity.'}

def dump(name,obj):
    raw=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode();(ROOT/name).write_bytes(raw)
    print(name,len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
    return {'name':name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

def main():
    j=json.loads((ROOT/'BAR_GUARD85_B.json').read_text());mf=[]
    for k in [6,8]:
        D=10**k;name='J85_CLASS_FIRST_G'+str(k);rows=[[round(t*D) for t in p] for p in j['points']]
        inp={'name':name,'denominator':D,'points':rows};mf.append(dump(name+'_INPUT.json',inp))
        P=[tuple(R(t,D) for t in row) for row in rows]
        try:
            rep=audit(P,j['faces']);rep['name']=name;mf.append(dump(name+'_EXACT.json',rep))
            print('EXACT',name,rep['V'],rep['E'],rep['F'],rep['strict'],rep['weak'],'P',[float(R(x['depth'])) for x in rep['P']],flush=True)
            cc=cube(P,j['faces'])
            if cc is not None:
                mf.append(dump(name+'_CUBE.json',cc));print('CUBE',name,[(s,d['rho_float']) for s,d in cc['certificates'].items()],flush=True)
        except AssertionError as ex:
            print('EXACT_REJECTED',name,type(ex).__name__,flush=True)
    P,F=load();cc=cube(P,F);mf.append(dump('J85_PARENT_CUBE.json',cc))
    print('PARENT_CUBE',[(s,d['rho_float']) for s,d in cc['certificates'].items()],flush=True)
    dump('J85_FREEZE_MANIFEST.json',mf)
    print('J85_CLASS_FIRST_FREEZE_COMPLETE_NO_110_CLAIM',flush=True)
if __name__=='__main__':main()
```

## replay85.py
```python
"""Cold replay of the three literal J85 rational bodies and S1 centre certificates.
Dependencies: this capsule's freeze85.py and three INPUT files; existing complete
J84 capsule supplies exact84.py and J82_S1_ROBUST_G6_INPUT.json. No optimizer.
"""
from fractions import Fraction as R
import hashlib,json
from exact84 import ROOT,load,audit
from freeze85 import cube,dump
CASES={
 'J85_CLASS_FIRST_G8':([1,2,1],'dba5a60bfd7f64121364dfd4f3c7899083c3ee2f90b44fc5aab6d65f680a816a'),
 'J85_CLASS_FIRST_G6':([1,3,2],'602ddb80aa2eea5f03defd3701eaf713e52b3e8051df3d9eb7a5682632b0baaa'),
 'J85_ANGULAR_FLATTEN_G8':([1,7,6],'471cd34c8a61ab98046a14c9b8be537fda9122e2609a010e88860e0245d123b1'),
}
CUBES={'J85_CLASS_FIRST_G8':'7f943d139235730b336b1582050fdf15143605fd0eee0ef9d8efb6ebc9159d99',
       'J85_CLASS_FIRST_G6':'60c36846f0913b529768fc61331d3ae973a5c0e9aaf37be3889fac9103a79570'}
_,F=load()
for name,(strict,sha) in CASES.items():
    data=json.loads((ROOT/(name+'_INPUT.json')).read_text())
    P=[tuple(R(x,data['denominator']) for x in row) for row in data['points']]
    rep=audit(P,F);rep['name']=name
    assert (rep['V'],rep['E'],rep['F'],rep['C'])==(45,129,86,258)
    assert rep['strict']==strict and rep['weak']==[0,0,0] and rep['is_own']
    m=dump(name+'_EXACT.json',rep);assert m['sha256']==sha
    if name in CUBES:
        m=dump(name+'_CUBE.json',cube(P,F));assert m['sha256']==CUBES[name]
    print(name,strict,'weak000','P',[float(R(b['depth'])) for b in rep['P']],flush=True)
print('J85_THREE_RATIONAL_BODIES_AND_CENTRE_CERTIFICATES_PASS_NO_110',flush=True)
```
