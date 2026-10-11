# material-2d59b409e57a

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

# J121: exact separation of angular-root improvement from persistence improvement

These are two new rational homogeneous own222/weak000/primitive000 nonwinners, not own110. Both have exactly one positive P and one positive Q. A complete exact comparison also proves that both unwanted-root angular guards can strictly improve while both persistence depths strictly worsen. Thus this scalar improvement is not a certificate of progress toward whole-basin cancellation. It does not prove that a continuation allowing temporary persistence growth cannot eventually succeed.

## Executed method and actual finite limits
The complete rootguard121.py below protects every positive nonelder angular outgoing guard and increases the deficient root's outgoing guard on both primal and actual-centred polar landscapes. It does NOT demand decreasing persistence depths. Full current hull and homogeneous mass are rebuilt at every finite admission. The complete source dependencies geometry121.py and coforest121.py are in [internal-source-reference], J121_NUMERICAL_METHODS_PART1OF2.md. Environment: Python3.13.5,NumPy2.3.5,SciPy1.17.0,torch2.10.0+cpu; OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1.

Executed commands:
- python rootguard121.py J121_PAIRED_RELAYQ_G8.txt rootguard_relayQ 48 .03 .0000001
- python rootguard121.py J119_FREEH_P_G6.txt rootguard_P 48 .03 .000001

Both completed all48 accepted steps and terminated at iteration_limit. Every recorded accepted floating endpoint had numerical S2/U2 and sole P/Q, with VEF90/135/47 and92/138/48 respectively. Minimum admitted protected guards were5.000000510461573e-8 and5.000008303716591e-7. Final trust bounds had shrunk substantially; this is a bounded finite trial, not convergence or nonexistence.

RELAYQ numerical unwanted-root angular guards improved from(-.123242901177233,-.21323130392785564) to(-.12232225595229752,-.21163842502863392), while P grew to .24593534097977143 and Q to .20515600599788353. P-input guards improved from(-.14430425461879542,-.2417462377738528) to(-.13792540193550365,-.23106739317063424), while P grew to .18966350734049708 and Q to .24623232671268003. Floating vertex-label changes are not proof of actual geometric root turnover.

The exact consumed RELAYQ starting H input is literal in [internal-source-reference]; the P starting H input is literal in [internal-source-reference]. No other checkpoint or hidden parameter was used. New exact endpoints are defined by rounding each final H normal with np.rint(n*10**10), not by rounding physical vertices. Their literal inputs below suffice without rerunning the numerical search.

## Complete source rootguard121.py
4762 bytes; SHA9b008684a780321e83e517332acd006c85f2230df1e9c34bde7ce3854eba431c. Save with its final newline.
```python
"""J121 guarded root-outgoing continuation, numerical only.
Unlike paired121, neither persistence depth is constrained to decrease. Every
positive nonelder guard is individually protected; at most one deficient root
per landscape may move toward zero. All finite hulls and own mass are rebuilt.
Dependencies: complete geometry121.py/coforest121.py in J121 methods part1.
Python3.13.5 NumPy2.3.5 SciPy1.17.0 torch2.10.0+cpu, one thread.
"""
import json,sys,time
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.spatial import QhullError
from geometry121 import geometry,arrows,read_h,normalize,describe
from coforest121 import model

def frontier(G,tau):
    mins=[];safes=[];roots=[]
    for key in ('p','q'):
        x=G[key];a,w,_=arrows(x)
        elder=int(np.argmax((x*x).sum(1)))
        idx=np.array([i for i in range(len(a)) if i!=elder])
        order=idx[np.argsort(a[idx])]
        mins.append(float(a[order[0]]))
        safes.append(float(a[order[1:]].min()))
        roots.append(dict(elder=elder,deficient=int(order[0]),witness=int(w[order[0]]),negative_count=int(sum(a[idx]<0))))
    return np.array(mins),np.array(safes),roots

def run(inp,prefix,maxiter=48,trust=.03,tau=1e-7):
    n=read_h(inp);n=normalize(n[geometry(n)['active']])
    initial=n.copy();hist=[];accepted=0;delta=trust;reason='iteration_limit';start=time.time()
    for it in range(maxiter):
        G,a,J,gauge,policy=model(n,True)
        old,safe,roots=frontier(G,tau)
        if min(safe)<tau*.49:reason='initial_multiple_deficits_or_margin_failure';break
        if min(old)>tau:reason='NUMERICAL_SINGLE_ROOT_EACH_REQUIRES_EXACT_AUDIT';break
        # Every present positive nonroot gets its own fixed lower margin.
        # Current deficient roots instead receive a fractional gain to +tau.
        deficient=a<tau
        coeff=np.where(deficient,tau-a,0.)
        floor=np.where(deficient,a,tau)
        scale=np.repeat(np.linalg.norm(n,axis=1),3);dim=n.size
        A=np.column_stack([-J*scale,coeff]);b=a-floor
        eq=np.column_stack([gauge*scale,np.zeros(4)])
        lp=linprog(np.r_[np.zeros(dim),-1.],A_ub=A,b_ub=b,A_eq=eq,b_eq=np.zeros(4),bounds=[(-delta,delta)]*dim+[(0.,1.2)],method='highs',options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
        if not lp.success:
            reason='linear_solver_failure';hist.append(dict(iteration=it,status=int(lp.status),message=lp.message));break
        gain=float(lp.x[-1])
        if gain<1e-10:reason='linear_guard_pareto_stall';break
        step=(lp.x[:-1]*scale).reshape(n.shape);trials=[];good=False
        for k in range(18):
            alpha=2.**(-k)
            try:
                nn=n+alpha*step;gg=geometry(nn)
                if not gg['simple']:raise ValueError('nonsimple free-H wall')
                now,ss,rr=frontier(gg,tau)
                required=np.where(old<tau,old+.05*alpha*gain*(tau-old),tau*.5)
                ok=min(ss)>=tau*.5 and all(now>=required) and float(sum(now-old))>1e-12
                trials.append(dict(alpha=alpha,mins=now.tolist(),safe=ss.tolist(),roots=rr,accepted=bool(ok)))
                if ok:good=True;break
            except (ValueError,AssertionError,QhullError,np.linalg.LinAlgError) as ex:
                trials.append(dict(alpha=alpha,error=str(ex)))
        rec=dict(iteration=it,mins=old.tolist(),safe=safe.tolist(),roots=roots,predicted_fraction=gain,trust=delta,accepted=good,trials=trials,policy=policy,duals=(-lp.ineqlin.marginals).tolist())
        if good:
            n=normalize(nn);accepted+=1;delta=min(.1,delta*(1.25 if k<2 else .85));rec['stats']=describe(n)
            Path(prefix+'.last.json').write_text(json.dumps(dict(n=n.tolist(),stats=rec['stats'],iteration=it,accepted=accepted),indent=2)+'\n')
        else:
            delta*=.2
            if delta<1e-9:reason='finite_no_birth_guard_stall';hist.append(rec);break
        hist.append(rec)
        if it%10==0 or not good:print('ROOTGUARD121',it,accepted,'guards',old.tolist(),'to',trials[-1].get('mins'),'trust',delta,flush=True)
    out=dict(input=inp,n=n.tolist(),initial=initial.tolist(),stats=describe(n),reason=reason,accepted=accepted,maxiter=maxiter,trust=trust,tau=tau,seconds=time.time()-start,history=hist)
    Path(prefix+'.json').write_text(json.dumps(out,indent=2)+'\n')
    print('ROOTGUARD121_DONE',reason,accepted,out['stats']['VEF'],len(out['stats']['S']),len(out['stats']['U']),[b['depth'] for b in out['stats']['P']],[b['depth'] for b in out['stats']['Q']],flush=True)
    return out
if __name__=='__main__':
    run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 48,float(sys.argv[4]) if len(sys.argv)>4 else .03,float(sys.argv[5]) if len(sys.argv)>5 else 1e-7)
```

## Complete endpoint J121_ROOTGUARD_RELAYQ_G10.txt
1700 bytes; SHA7f4e652a9abe6903e613a71b72bfd9c6b5a554f312e6d9e5751447e35de5e488. V90/E135/F47,C270,strict222,weak000,primitive000,one P and one Q. Exact S=[0,31],U=[2,56],H=[[88,89],[4,50]]. Depth intervals (a,a+1)/10^15: P a=245935340967404; Q a=205156006001196.
```text
47 10000000000
-20692787311 5742697880 -7154633555
3543341078 -11729771485 4030684061
-6856590902 -10694467968 -15731287236
-10103971963 -9887567604 -14864443639
-517205820 11278517078 -4873422933
-4801578088 12092810636 -2410579200
-17597707981 -2022988878 -12233731376
-4735784241 4434994898 -12840633238
788972321 9603697541 -8975483021
-12968514588 -7717354160 -14360887695
-15481905448 -5111063096 -13491775695
15755661152 -1911077607 12429027722
7377462928 -11667307910 -13026942613
17415328221 1718537172 8739562858
9328605756 -9469626054 -2113075129
3146490453 -13553727867 -12821978217
2904917575 -10417057368 -16096598778
6199224935 3439286090 -13091381407
-195869177 -11207118167 -16144897212
6104813017 -7079251015 -16344948936
5468968281 -10948181080 -14751843112
12138245660 1825585635 -5545030446
12517361342 -2295314884 16476801901
17678356042 4676683107 3837119990
-3495041402 -11100254989 -16179051989
4981961114 6926653367 -11473531663
5455589398 9580155794 -5556983464
10632632695 9393248831 685292727
2641334910 12939641812 1065083198
3009227866 12326772648 7633464462
7529321908 -9359347328 16155948320
8403043098 -2854971280 19525451723
5327457141 399388917 20269680167
2095822005 3500676594 20063599896
-991983861 6131695825 19046799707
-3851132087 8115242520 17496553991
-6416602701 9473022278 15616352700
-11303154130 11280582754 11187560191
-13920176821 11699146418 8124243060
-16524223877 11413534283 4087928641
-18907992251 9999387884 -1596640412
-6843453081 -14573842471 -10418513601
-8837554130 -12351417250 -10777861183
-9990785663 -10933895838 -10790446771
-11180616366 -9670456436 -11199270079
-19350085228 1499729235 -10295539556
16713698625 -115720246 10614678090
```

## Complete endpoint J121_ROOTGUARD_P_G10.txt
1736 bytes; SHAd1bdba5d0a07140dbbb989fe9ed394eb930f3a12b2d311838e9306028297a949. V92/E138/F48,C276,strict222,weak000,primitive000,one P and one Q. Exact S=[0,34],U=[0,48],H=[[79,90],[27,40]]. Depth intervals (a,a+1)/10^15: P a=189663507385460; Q a=246232326682983.
```text
48 10000000000
-20642513511 5058004795 -7229680256
3632850572 -11591157673 4049713953
-6975831074 -10201059646 -16008574025
-10145440453 -9179624997 -15279562010
-3557143730 9835182098 -8523692602
213008358 12088984291 -5225219715
-3850722013 13061429355 -3162818633
-17856021446 -2107158836 -11817835102
-3509451762 5709544993 -12227899314
1468739927 8008045111 -10220901043
-1773834740 13216726630 1814775031
-13153383392 -7653281044 -14200061343
-15696700516 -5145985209 -13196916750
16061212326 -1503791448 12141424651
6979940922 -11857728196 -12687416167
17631980239 1662764208 8042009208
9170212582 -9486179757 -2325301088
3427640067 -13564829152 -12744787233
2610899619 -10821162498 -15924322976
6507660158 3429819788 -12623700835
-489140522 -10879070082 -16394043422
5890741862 -5759667456 -16221808434
6288291295 -9653216120 -15140442800
11960430152 1916921787 -5878249932
12716949137 -2273645841 16470626161
17821042018 4408934449 3460897460
-3638761868 -10835581331 -16329470297
5872303248 6100169073 -11331346149
5989276518 8421775560 -7669067141
6830342219 11089594699 -1622602014
12001708473 8830631538 575195510
3385242253 12986925014 1097572813
3640136208 12391403814 7598841242
7807121349 -8931309449 16414124567
8460519993 -2285714303 19756160484
4919260810 1174216883 20410605327
1721278757 4431776524 19915403605
-1597034299 7308553318 18485749036
-4922111443 9017384678 16518036876
-7678365371 10177766831 14168499481
-13083116897 11105246813 8753005827
-15954736907 10971247600 4663775544
-18365618963 9553564010 -187574293
-7473255720 -14746179769 -10868282843
-9404638339 -13355500227 -11490128159
-11076276601 -11708710067 -12128889761
-11959023549 -10389007104 -11747338766
-19543027147 1423648021 -9899064106
```

## Exact reconstruction and observed audit identities
The exact source dependency is [internal-source-reference], exact115.cpp11038 bytes,SHA d7fd1244c086a0c5354844cca3453c42b26ed31a55b89720aa9e3987f0a06736. Compile g++ -std=c++17 -O2 exact115.cpp -lgmpxx -lgmp -o exact115 without NDEBUG, then ./exact115 < STEM.txt > STEM.audit.json 2> STEM.audit.log. Both commands were executed successfully before preservation. This is the existing exact hull/mass/census engine, not an independent second physics verification.

J121_ROOTGUARD_RELAYQ_G10.audit.json:173987 bytes,SHA a5e591fc23197c8ffd03470b2ba58814d811a72babf472134b095f851e58ac3f. Its log138 bytes,SHA38d4e0f6a3fda00e7d8a2396b40189d9e10283ddb816502f1d301f87f981ba76, final marker J115_EXACT_PASS VEF=90/135/47 SUH=2/2/2 weak=000 P=1 Q=1.
J121_ROOTGUARD_P_G10.audit.json:179576 bytes,SHA dccedcc561a339c9c8391729029cf9075b2ac4219b5b1a7bbf9d794fe166f9c1. Its log138 bytes,SHA5668e61ab7e2f23b14408f1a498355bad03bf24b3c6a1ba1e0858cec49f781ab, final marker J115_EXACT_PASS VEF=92/138/48 SUH=2/2/2 weak=000 P=1 Q=1.
The previous RELAYQ_G8 parent input and audit identities are fully specified in [internal-source-reference]. All centroids, true facets/edges and complete positive bars reconstruct from the literal inputs and exact115, without the numerical producers.

To reproduce the numerical freeze after the two complete runs, save/run this complete Python unit:
```python
import json
import numpy as np
from pathlib import Path
for name in ['rootguard_relayQ','rootguard_P']:
 d=json.loads(Path(name+'.json').read_text())
 n=np.array(d['n']);s=np.rint(n*10**10).astype(np.int64)
 out=Path('J121_'+name.upper()+'_G10.txt')
 out.write_text(str(len(s))+' 10000000000\n'+'\n'.join(' '.join(map(str,r)) for r in s)+'\n')
print('J121_TWO_ROOTGUARD_G10_INPUTS_FROZEN')
```
The actual rounding operations were executed in the endpoint capture; the standalone unit is the identical operation, not a separate replay claim. Floating optimizer histories contain wall-clock seconds and are not expected byte-deterministic output objects.

## Exact proxy-separation proof and comparison
At a strictly unstable point u all numerators u dot(x-u) are negative. Its maximal angular outgoing score is therefore -sqrt(R), where R is the minimum over all other actual vertices of (u dot(x-u))^2/(|u|^2|x-u|^2). Improving this negative score is equivalent to strictly decreasing R. For each landscape choose the junior of its exactly two U points by its smaller exact squared radius. On the polar side these are the physical S facets. This selection does not assert that label numbers represent persistent material points across bodies.

Exact R intervals are strict open (a,a+1)/10^15:
- Parent J121_PAIRED_RELAYQ_G8: P junior62,witness53,a=15188812690581; Q junior31,witness32,a=45467588974773.
- New J121_ROOTGUARD_RELAYQ_G10: P junior56,witness52,a=14962734295693; Q junior31,witness32,a=44790822963501.
Thus both negative angular guards strictly improve. The exact P depth increases from its parent interval a=245357468575877 to245935340967404, and exact Q increases from204368769327801 to205156006001196. This is an exact two-sided counterexample to using monotone angular-guard improvement as a monotone persistence surrogate, with strict222/weak000 and true C270 at both ends. It is not a proof that a guard-driven path cannot eventually reach110, and no exact classification of every intervening floating point is claimed.

## Complete source proxyseparation121.py
3296 bytes; SHA0756e8f5711e52eb814c2bad9c7580f95c39c98be281c9b7da7ad3a8ebaef95b. Standard library only. The integer denominator cancellations avoid any floating square-root test. This is a new exact scalar comparison on exact115 outputs, not independent recovery of the hull or mass.
```python
"""Exact squared-angular-guard separation from exact115 outputs.
This is a new integer comparison, not an independent hull/mass physics engine.
For a strictly unstable point all outgoing angular scores are negative. Thus
max_j score(i,j)=-sqrt(min_j R_ij), R_ij=(u.d)^2/(|u|^2|d|^2).
A smaller R is a strictly better angular guard. Denominators cancel as below.
Python3.13.5 standard library only; needs two complete H inputs and their audits.
"""
import json,sys,math
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def vector(row):
    f=list(map(F,row));d=math.lcm(*(a.denominator for a in f))
    return [int(a*d) for a in f],d

def less(a,b):return a[0]*b[1]<b[0]*a[1]

def score(stem):
    data=json.loads(Path(stem+'.audit.json').read_text())
    assert data['strict']==[2,2,2] and data['weak']==[0,0,0]
    assert data['primitive_zeros']==[0,0,0]
    gn,gd=vector(data['centroid'])
    raw=[vector(v) for v in data['vertices']]
    pn=[[n[k]*gd-gn[k]*d for k in range(3)] for n,d in raw]
    pd=[d for n,d in raw]
    lines=Path(stem+'.txt').read_text().splitlines()
    count,D=map(int,lines[0].split());assert D>0
    nn=[list(map(int,s.split())) for s in lines[1:] if s.strip()]
    assert len(nn)==count and all(len(n)==3 for n in nn)
    qn=[nn[i] for i in data['active_input_planes']]
    qd=[D*gd-dot(n,gn) for n in qn];assert min(qd)>0
    result={}
    for side,points,den,roots in [('P',pn,pd,data['U']),('Q',qn,qd,data['S'])]:
        assert len(roots)==2
        i=roots[0]
        if less((dot(points[roots[1]],points[roots[1]]),den[roots[1]]**2),(dot(points[i],points[i]),den[i]**2)):i=roots[1]
        u=points[i];uu=dot(u,u);best=None;witness=None
        for j in range(len(points)):
            if j==i:continue
            if side=='P':
                ni,di=raw[i];nj,dj=raw[j]
                d=[nj[k]*di-ni[k]*dj for k in range(3)]
            else:d=[den[i]*points[j][k]-den[j]*points[i][k] for k in range(3)]
            num=dot(u,d);assert num<0
            candidate=(num*num,uu*dot(d,d));assert candidate[1]>0
            if best is None or less(candidate,best):best=candidate;witness=j
        assert best is not None
        a=best[0]*10**15//best[1]
        assert a*best[1]<best[0]*10**15<(a+1)*best[1]
        result[side]=dict(root=i,witness=witness,squared_angular_open_interval=[a,a+1],denominator_scale=10**15,pair=best)
    result['bars']={s:F(data[s][0]['depth']) for s in ['P','Q']}
    assert len(data['P'])==len(data['Q'])==1
    return result

def main(parent,child,out):
    a,b=score(parent),score(child);summary={'parent':parent,'child':child,'sides':{}}
    for side in ('P','Q'):
        assert less(b[side]['pair'],a[side]['pair'])
        assert b['bars'][side]>a['bars'][side]
        summary['sides'][side]={'parent':{k:v for k,v in a[side].items() if k!='pair'},'child':{k:v for k,v in b[side].items() if k!='pair'},'angular_guard_strictly_improved':True,'persistence_depth_strictly_worsened':True}
    summary['marker']='J121_EXACT_TWO_GUARDS_IMPROVE_BOTH_BARS_WORSEN_NO_110'
    Path(out).write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main(sys.argv[1],sys.argv[2],sys.argv[3])
```
Executed command: python proxyseparation121.py J121_PAIRED_RELAYQ_G8 J121_ROOTGUARD_RELAYQ_G10 proxyseparation121.json. All assertions passed. Output1278 bytes,SHA0acf57c2d6c27d4400a8c0adcc67e514bb183555fbdb30a7fb41aadce620064c; terminal marker J121_EXACT_TWO_GUARDS_IMPROVE_BOTH_BARS_WORSEN_NO_110. The output intervals above are the actual produced intervals. No own110 and no improved canonical record result from this experiment.
