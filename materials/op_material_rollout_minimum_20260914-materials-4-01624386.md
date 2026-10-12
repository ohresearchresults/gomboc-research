# material-016243864e08

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---



# Preserved span 351 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 352 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 353 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 354 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 355 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 356 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 357 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 358 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 359 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 360 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 361 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 362 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 363 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 364 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 365 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 366 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 367 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 368 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 369 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 370 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 371 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 372 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 373 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 374 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 375 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 376 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 377 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 378 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 379 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 380 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 381 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 382 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 383 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 384 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 385 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 386 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 387 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 388 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 389 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 390 (literal-source)

```python
"""Exact constants for the centroid/signed-shadow certificate tradeoff.
The proof is the actual-fan identity in the research journal. Standard library.
These constants concern the full frozen necessary signed-shadow list.
"""
from pathlib import Path
from math import isqrt
import json
import c34_joint48_filter as h
import c34_701_exact_check as ck
assert __debug__
INPUTS={
 'c34_joint48_filter.py':[6928,'058a5573ffe5a35256c252ea7778f3d0828660cdd74666be3381848134c9a7aa'],
 'c34_701_exact_check.py':[6347,'6664fddb3ca52621df15d298a16099543d5e596b525617a56507da157bfcd81b'],
 'c34_701_certificates.json':[4860172,'b29f6bf010a7b9f3f3046895e0ac2363604860cfb3dd6d80488915c0393f028c'],
 'c34_701_exact_report.json':[499531,'d2a4063449eef6e0dc0bb24b710f97f2f2f089342060ec02e75f4baeab1a097d'],
 'c34_701_frontier.json':[2246318,'bf3512f2fdbe7fd0e378499fb83a978afbe89183f2db3df06833984e1c68014c'],
 'c34_catalogue.json':[1111066,'1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77']}
for name,want in INPUTS.items():assert h.pin(Path(name).read_bytes())==want,name
certs=json.loads(Path('c34_701_certificates.json').read_bytes())['records']
report=json.loads(Path('c34_701_exact_report.json').read_bytes())
assert report['uncovered_domains']==[] and len(report['coverage'])==1917
assert len(certs)==1265
rows=[]
for r in certs:
 pats,arcs,order=ck.model(ck.domains[r['index']],r['fan_apices'],r['fan_mode'])
 A=len(r['fan_apices']);m=len(arcs);z=r['z'];end=10*A+m*len(pats)
 assert len(z)==end+56*(A-1) and all(type(t)==int for t in z)
 assert min(z[10*A:end])>=0
 gamma=[sum(z[10*a+i] for a in range(A)) for i in range(10)]
 q=sum(v*v for v in gamma);assert q>0
 k=max(sum(z[10*A+m*t:10*A+m*(t+1)]) for t in range(len(pats)))
 assert k>0
 b=isqrt(q);b+=int(b*b<q)
 assert (b-1)**2<q<=b*b
 rows.append(dict(index=r['index'],gamma_sum=gamma,gamma_norm_squared=q,
  gamma_norm_integer_upper=b,maximum_shadow_multiplier_sum=k,
  centroid_ratio_strict_lower_if_all_signed_shadows_hold_squared=[1,64*q],
  centroid_ratio_rational_strict_lower_if_all_signed_shadows_hold=[1,8*b]))
by_id={r['index']:r for r in rows}
assert len(by_id)==1265 and all(c['certificate_index'] in by_id for c in report['coverage'])
qmax=max(r['gamma_norm_squared'] for r in rows)
kmax=max(r['maximum_shadow_multiplier_sum'] for r in rows)
bmax=isqrt(qmax);bmax+=int(bmax*bmax<qmax)
assert qmax==103824771015 and kmax==4015976 and bmax==322219
out=h.serial(dict(identity='C34_701_CENTROID_SIGNED_SHADOW_TRADEOFF_V1',
 inputs=INPUTS,records=rows,coverage=report['coverage'],
 maximum_gamma_norm_squared=qmax,maximum_gamma_norm_integer_upper=bmax,
 maximum_shadow_multiplier_sum=kmax,
 uniform_rational_tradeoff=dict(centroid_coefficient=8*bmax,shadow_coefficient=2*kmax,strict_lower=1),
 normalization='eta=norm_M(g)/sqrt(sum_i norm_M(x_i)^2); epsilon=max(0,max_e(-s_e D_e))/sum_i norm_M(x_i)^2',
 scope='Full frozen signed-shadow systems; additional redirected negative signs are not automatic for arbitrary reference-centre 110 bodies.',
 number_of_certificates=len(rows),number_of_domains=len(report['coverage'])))
Path('c34_701_centroid_shadow_tradeoff.json').write_bytes(out)
print('C34_701_ALL1917_DOMAINS_CENTROID_SHADOW_TRADEOFF_EXACT_PASS')
print('UNIFORM_STRICT_TRADEOFF',8*bmax,'eta +',2*kmax,'epsilon > 1')
print('OUTPUT',*h.pin(out));print('SOURCE',*h.pin(Path(__file__).read_bytes()))
```


# Preserved span 391 (literal-source)

```python
"""Exact current joint41 landscape and full prepared TREE669 frontier."""
from pathlib import Path
from collections import defaultdict
import json
import c34_joint48_filter as h
assert __debug__
pins={
 'c34_joint41_filter.json':[4073330,'fca1a568719778e732a8437d7d6f14265abde9090adc4e465acebf1d2452ff20'],
 'c34_669_frontier.json':[3227401,'45bda17ac507da9111deddcf9c7d66e94deb201560674c67fabdb927704bcc35'],
 'c34_669_groups.json':[31333,'53d29cb58c2bb5e4eb6046ba161d574f990e40903fddf57ed60ca453f12a45f7']}
for name,pin in pins.items():assert h.pin(Path(name).read_bytes())==pin
x=json.loads(Path('c34_joint41_filter.json').read_bytes())
assert set(x['remaining_vertex_trees'])==set(h.REMAIN)-{671,672,673,674,675,701,709}
parents={h.INDEX[c]:h.parent_tuple(c) for c in h.INDEX}
leaves=defaultdict(list);kmin=defaultdict(list)
for t in x['remaining_vertex_trees']:
 p=parents[t];degree=[0]*10
 for i in range(1,10):degree[i]+=1;degree[p[i]]+=1
 ell=sum(d==1 for d in degree)
 leaves[ell].append(t);kmin[ell+int(degree[0]==1)].append(t)
assert {k:len(v) for k,v in leaves.items()}=={2:5,3:21,4:15}
assert {k:len(v) for k,v in kmin.items()}=={2:4,3:13,4:14,5:10}
hits=x['shape_hits'];nexts=[]
for t in sorted(x['remaining_vertex_trees'],key=lambda t:(sum(v.get(str(t),0) for v in hits.values()),t))[:12]:
 counts=[hits[str(k)].get(str(t),0) for k in h.TREES]
 nexts.append(dict(tree=t,parent=parents[t],counts_by_facet_tree=counts,total=sum(counts)))
f=json.loads(Path('c34_669_frontier.json').read_bytes());g=json.loads(Path('c34_669_groups.json').read_bytes())
assert len(f['domains'])==2971 and len(g['groups'])==1762
assert sorted(i for group in g['groups'] for i in group)==list(range(2971))
out=h.serial(dict(identity='C34_JOINT41_LANDSCAPE_V1',inputs=pins,totals=x['totals'],leaves=dict(leaves),minimum_leaf_window_requirement=dict(kmin),next_shapes=nexts,tree669_state_counts=f['counts'],tree669_retained_domains=len(f['retained_domains']),tree669_representatives=1762,feasibility_claimed=False))
Path('joint41_landscape.json').write_bytes(out)
print(out.decode(),end='');print('C34_JOINT41_LANDSCAPE_EXACT_PASS')
print('OUTPUT',*h.pin(out));print('SOURCE',*h.pin(Path(__file__).read_bytes()))
```


# Preserved span 392 (literal-source)

```python
"""TREE669 complete physical moment campaign from pinned TREE701 source units.
python replay_c34_669.py prepare|stage1|stage2|freeze|all
Six independent single-thread numerical processes. UNKNOWN is no exclusion.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
os.environ['OPENBLAS_CORETYPE']='SkylakeX'
from pathlib import Path
import sys,json,subprocess,concurrent.futures,hashlib
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
INPUTS={
 'c34_701_probe.py':[3898,'bbbfa5a4594e13f72afb9868c2b8acd56bd8dc45787e39620eebfa7a043b8773'],
 'c34_701_exact_check.py':[6347,'6664fddb3ca52621df15d298a16099543d5e596b525617a56507da157bfcd81b'],
 'c34_701_freeze_compact.py':[3093,'428aaeb4a0fc5b2f5231dda299d82edba88b70f58878ddc97d8051ca0b15ce0f'],
 'c34_669_frontier.py':[4971,'21c5671140c6fe8f2bef9c8c23855569795ee1e6a830748dc707e03cfb5768de'],
 'c34_669_frontier.json':[3227401,'45bda17ac507da9111deddcf9c7d66e94deb201560674c67fabdb927704bcc35'],
 'c34_joint48_filter.py':[6928,'058a5573ffe5a35256c252ea7778f3d0828660cdd74666be3381848134c9a7aa'],
 'c34_catalogue.json':[1111066,'1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77'],
 'ten_successor/work/continue10_cells/coupled.py':[5991,'f5973659810ea240367024f7a46c48f18b82e8866df86a7eba34a809157cf7f1'],
 'ten_successor/work/universal10_engine/engine.py':[5104,'a254810e332f31e5cdae6e88dc05a84c6c9718f2903ef84f6a900668d1b8f226'],
 'ten_successor/work/universal10_engine/fast.py':[2737,'3a54df86eca10711bcddd96099ec8eab9b71a7d4aa0f1a1aadeed6db1fe36f5c']}
for name,want in INPUTS.items():assert pin(Path(name).read_bytes())==want,name
def once(s,a,b):
 assert s.count(a)==1,(a,s.count(a));return s.replace(a,b)
for name in ('c34_701_probe.py','c34_701_exact_check.py','c34_701_freeze_compact.py'):
 s=Path(name).read_text()
 if not name.endswith('compact.py'):
  s=once(s,"[2246318,'bf3512f2fdbe7fd0e378499fb83a978afbe89183f2db3df06833984e1c68014c']","[3227401,'45bda17ac507da9111deddcf9c7d66e94deb201560674c67fabdb927704bcc35']")
 if name.endswith('probe.py'):s=once(s,'len(gs)==1265 and sum(map(len,gs))==1917','len(gs)==1762 and sum(map(len,gs))==2971')
 elif name.endswith('exact_check.py'):
  s=once(s,'P=(0,0,1,2,3,4,5,6,5,5)','P=(0,0,1,2,3,4,5,5,4,8)')
  s=once(s,'len(domains)==1917','len(domains)==2971').replace('range(1917)','range(2971)')
 else:
  s=once(s,'((0,5,7),(0,1,3,5,7))','((0,4,6,9),(0,1,3,4,6,9))')
  s=once(s,'[0,0,1,2,3,4,5,6,5,5]','[0,0,1,2,3,4,5,5,4,8]')
  s=once(s,'len(records)==1265 and 1265<=len(attempts)<=2530','len(records)==1762 and 1762<=len(attempts)<=3524').replace('ALL_1265_CERTIFICATES','ALL_1762_CERTIFICATES')
 s=s.replace('c34_701','c34_669').replace('C34_701','C34_669').replace('TREE701','TREE669').replace('coupled701','coupled669')
 Path(name.replace('701','669')).write_text(s)
mode=sys.argv[1];assert mode in ('prepare','stage1','stage2','freeze','all')
if mode=='prepare':
 for n in ('c34_669_probe.py','c34_669_exact_check.py','c34_669_freeze_compact.py'):print(n,*pin(Path(n).read_bytes()))
 print('C34_669_SOURCES_PREPARED_PASS');raise SystemExit
if mode!='freeze':
 assert sys.version_info[:3]==(3,12,14)
 import numpy,scipy,scipy.linalg,threadpoolctl
 assert (numpy.__version__,scipy.__version__,threadpoolctl.__version__)==('2.3.5','1.17.0','3.6.0')
 pools=[p for p in threadpoolctl.threadpool_info() if p['internal_api']=='openblas']
 assert pools and all(p['version']=='0.3.30' and p['architecture']=='SkylakeX' and p['num_threads']==1 for p in pools)
from c34_669_probe import groups
reps=[g[0] for g in groups()];assert len(reps)==1762 and sum(map(len,groups()))==2971
def result(i,apices):
 r=json.loads(Path('c34_669_d'+str(i)+'_a'+''.join(map(str,apices))+'_m0.json').read_bytes())
 assert r['index']==i and r['actual_apices']==list(apices) and r['fan_mode']==0 and r['maxouter']==12
 assert r['status'] in ('EXACT_CERTIFICATE','UNKNOWN');return r
def stage(indices,apices,label):
 def run(j):
  ids=indices[j::6]
  if not ids:return
  with open('c34_669_'+label+'_'+str(j)+'.log','w') as f:
   subprocess.run([sys.executable,'c34_669_probe.py',','.join(map(str,apices)),','.join(map(str,ids)),'0','12'],stdout=f,stderr=subprocess.STDOUT,check=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:list(ex.map(run,range(6)))
 print('C34_669_STAGE_FINISHED',label,len(indices),flush=True)
if mode in ('stage1','all'):stage(reps,(0,4,6,9),'stage1')
if mode in ('stage2','all'):
 unknown=[i for i in reps if result(i,(0,4,6,9))['status']=='UNKNOWN']
 stage(unknown,(0,1,3,4,6,9),'stage2')
 left=[i for i in unknown if result(i,(0,1,3,4,6,9))['status']=='UNKNOWN']
 print('C34_669_REMAINING_UNKNOWN',left,flush=True)
 if left:raise SystemExit('NO_WHOLE_TREE_EXCLUSION')
if mode in ('freeze','all'):subprocess.run([sys.executable,'c34_669_freeze_compact.py'],check=True)
```


# Preserved span 393 (literal-source)

```python
"""Recover exact equal-fan-volume TREE701 quantitative certificates.
Needs the complete pinned TREE701 proof inputs, already in the journal.
CPython 3.12.14 stdlib, assertions enabled. No numerical solver on replay.
"""
from pathlib import Path
import base64,lzma,json,hashlib,subprocess,sys
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
PACK_PIN=[143103, 'c0fd7b52381e31463c6a911b87485eaba121a7ac0a79189a3e5ec4b31efe90e5']
MANIFEST={'c34_701_balanced_tradeoff.py': [3809, '7fb3d7229eaab18e46cb91d60f76183dbc7ce6179137f77e8592cdbf31985528'], 'c34_701_balance_witnesses.json': [131563, 'aa2d06100054d9858f04ece6fe1cafdc0cb6e9cb943e611a00369ca82dab2892']}
DATA="""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;x7JL%v}IIh=^ll$&q7xzdU}L7s%vVj;*=pd&DkHdRo7%-D>pjUCK8|ZG#%>iPk<d(MGKX
eH7$IWUTJxBJsXlXOvcOw>L2VrS%e7P^PbC|Gd{MeRDS_K&o!jb|y#YCl<zHTuxml&g4+`7{7U%h@zxu`22rdzBCCrhVIG7nDJp<
3`N0rXW9gaNf!XA94W0h!td{~==Of>1?--Oq$}ZYF5xge(*Vf8(^ZaWf;3~%1lVB(cFj9bfUfojLvS{Y2-zVfM@*VSHm;n~y*!5@
BoVL+rbRN6XF+2Xl6(2NHmbGj-VIsoAh?fNrcg+xCI@(VWOVVMRezzGTh;y_Tb2_#Db9$GYS0=OjKFQQuN1ZS;t-%k9OxtuPUFd!
9*_`7*XUWNNu1ATbo4o*i3Rp{uyVlh$!4w&6Ymzk&kG-@#2rXx>}1ce5vL4=)yQ<L!|mAPvXDlpe0XuU+9BG8>9yL!!?@-niQ1{s
!eW-Cjj$M&D+p^ZXxq?5GSQQE`LFcK|E>5NnnrURdM+xdFjgASq0VEs$rv3~50j_17nSy8++;>gCEWKD8XYOLbhIPgRrxKg^J0Cc
u%k1=rsgE$&7^y8cWBRaSkKoPXUEXdL(OO<=Lg3T4n7QYCw(P_%(K7xQ&eMzKMIj>jb?LVJ*lt*D~T>5u$+0d2p4)cMO`jjmh$Xf
a|L_Hbqn3grSSo!5*CQ41jEx~<-VD1Gi9m|A-G_3nTj&D)kd8CWS`QOVkF@&!Ywdq1`YTZA^XtpnMl-AOfvu&6Yx@RvI$R#3*ld}
d_8Kp*jT2~HqfJ2Y|+~#g53X}vByppN_pi*)-F)j40?ku0c;(yPo4H3J7{aUb^z?vR!V8zjOAGcOyK7&gbPAEod|Dk-bL1y&?h;7
c2JwgqIPvY#cm891$dKl|1D|n5iF<3L-L;p1H`RFnw@i}LC3gToO}j^@P*-vW#rnI2=NSxqcpeI=a8m|^WTvRmZ39vUL32%^tUz{
13tnB0&3%btXE_DTH4m3nT-|WlT3GV(&+Z;$ry$Zw%cK6a7>)sf}Ly3D7*W0P3%~OncullMexE?fQPhl%<_-b(A7F0SE)}BK5G{*
+uuv>q`9?S9)Q)v6&gX|S$JXNS^3tEyIgewS>vh=L7-Q6n$etJiz^*HG)^L>-aYl2<0@`m&#i9sb$F#m<#Q;io4DiVOfGevoAQiG
avTMl_20)1C`$f0O_*8Z0w;M8mCVif23dJ|<^O!w9weOsxc1&u@57}DY=?dw498c^*ZRilE9mMK*J*$8R8)G&HCW?(hQ#UYdY)5y
+6v>eu~>K4`r;tV{0<*^Mf}(-7<-?f8p3lPj-ZKUW$o{4eJOKX@oZZIt`hWy)8jtVYiw|ESex;v2W0mOFTK}mKrooM-BESPP9BWq
+rY;*qnH;r8NXKJ``KEkOz+<$mTKNQ*Pe|v{TSlir=-T;vjT~Iu)2FLcQNrf_?!BlrMO@P<GjsFln>l!%wm5|_3@YsE4hzKO9==J
PQ$Iwe%3IZ4)BvU#$+MS68acCbwP>0U5^zVsZ-91IhjR2rUurdis5q-VLT-6yVb&6_}V*Z0w!X1iIQ`2=8)yhp#aW#hkqDKW4<+i
#`RGw=^{(Rz#BCFL1VUVGpKL&6h+)0KeF$~P5a*`NG{>weu%O!YgW0DKuskZvM;<er%BZCb1gFn)0B?OQgItL-?jJkjyExWWiN*2
euP<GYj{+D+QY)w@yTs;k{eQyx1=sc{6{!Vo2x?BmwN#4u7s%cjnz9lv@PrVR9=B=r@30ipO1~|5Dk8hvjfND>>OUV)Fix1A@Ijc
xRC^G9}Qac%6|e{2ST_c=Jd})-Tx9cbk=@um1OMLv-x?jl8)P2u|A?a%KgClG8s{63d104ZG!q!-JShXEGa%J=9yK)p0h`)*FEi7
E?NX@8c8UhvB1KiBl#r`O13!~fqn1Cw6pq<p>D(!eyb;VwMeZ^-d#7Fted^6XxWK-=8lQJGrrOh-61sj>7l@HsgdW8rXzIO+BT9*
U0AP{>Y2yCXcqf;D5`4@kI00*;1$Bw*q|@^FB;V*o?UM{)tlWRN0A-|)NaBvCCd%s&kjsCd$I=dTFYPFe5<~PG>-V`6S-np>;&Ki
z;_CN4`yi24Vao?>2K2q4QBy_h+Y?@Uqjp0h&JJhC?7F}C4p0>3IFK?16HZ!>uP9@Tli}^xN1{rVw?>==Zz47)h#^dJwz%wtmA;#
ew<T43LKulq|=8$lRn{7b20H=UcR&!FqfsFuK0sO!T@kRZqIlE0bOoU$Wb-!yli0EV0Yg7q1I;+nUYB-tZ{B!ILW_$xENnU0aQO)
4XOmIMC-HVVSd-7Gb#XI)L=a~@zI+#ia4)Mn%~!{4o-UuB79x_AR2KmIf^baNIFV*?{eM(rr9i>FeJ^UAthqvDRcv~(wri);6+}{
bH1^qBK1`t)*H(xEG1<v&8IycB$u#)YWsdmbK1UX!CTbZC}jVWibV$!3IJn|N=rXO3yEq<7=+)&mXm}y2I?IEWfx-w=jEQNedpPq
Ej3BDX4L=PSTv)EB8f?<oTeKy&)=E;&HCt)WT{1VbGZuwgaL8zd_-IUaQ94$9n>Vo9WKF!x2nW@Uv4n6xJ7pSFT;Z-!SfM`&hl)a
HzKjRSVxRJvZ%12lv){Pgq~-8Du!wtd=fs{B=2dd2ETFFpne1nK?H3tsxhE=1N)b?l%)<()c7khvPQho*=JG<KMlI*_0SdxXb0>3
7GQpV9pNMnZ9V+~XoB{Xt#fRxv_n1tEyJP+>b8^?h-87CtR_c1B1Ulg0i<O|*`5yhlAd{oGRW3X@!Cu$0%ZG0TTT-_wW39afd!OI
<&S~VpVYEC>CtW&SQ#UxKrDR4F66E(()Mj_zj5T{Aw#ZLh^PVM|2x&BE8~xR>3;6!UhLMkMkbLeEn-O!NTFJrZ1<r&AXq!D@}vI*
OE(8@Bvcewk01nShD{-RDn}<-$8o{yZv-t?n5O22nwIV^dLfTRME<c_8<2Ya4aXZq7Z$A^`;6r?X6OOrrvXJ%btxh3zrX?vkvX04
PDC{o<%@b==N@t~a&M|sYoa-TO_Q4ZHWE4yA7cY-BaCPUJl7Knrs=JiyTA)E_F(L};w$w|m!4(v-!PZU;NMD`blM3Q6LkILChO;@
bX+=FsVAcznQ)s+9WWLBdRHn_)EWgr)y~9>Be?9<-E}Tz7tf#-Q}2Si%7{UOa8_v@WX2;mLL<TkwuX+fl2DiLyr4CDrjAU&`I^;Y
Wlxi=LLH5vs)f`5Xl{;pI>w4Z?6->f752d+bt{3%s7dwaP`xP4rI1jBB`bAXKSm0WCdO%m-~3gMl2XWyM~8#@5{ii0ap^+JWazJ_
$B@1S8BuzQe{NSUUN*M_ui1X)7_gUBBLZ{4B4v#QAV$#>7h`a{VcGYWSSEW?#Ep6Ay;F8vwT*`v0h^#rRp0EHHJp-CxrWw~Gw1s%
6B9T%@b4cjhCtF7_dZle(LCbN&_=)?_gHpt-5s`&8idgyTXsobPvaKE(i6Cx1vi%`ztFOiu<g~frkw;*mK=U^ZpO4J&(AZ`bRE+B
&}otW{Mey@FmHL*0}MJQhjepEO_6DAycTPUPM6UIZFnU$Pq}w-WW};6OTh1b!O^=zN5n}m9<)y1W3-_oqg&WQc)wEnq1OT!w1MHb
CzsI<RxfhlvEKl~bg8~<t`W&8%-`(VcDI;iQ#Ll-+slh<6Nv4+V$lc8Vwj6{xj7@wW4(9_O)!a*E{IN3f;NZ!`EJjrMMYd1<_$6_
O)lf6Ey73E-0@q`GD(VuXCH)vyWBcb-M<l-@OBZwo}xm$98{2ov%qnIQJZMj&0A)D^U?pB&m;BKdu@6rF;a=k^L6k}uD)HmC%n3=
PPSk77{-!RdKqZKT+cTXwb`aosY@sV1+xSD&XNAcMtT*o@)tlfuo~+T%AW2f6u3&byz!0d4G~1ZxJu3b4mM$fmj8}g;E9ZQkv35%
MIA^Un%9Ikry#<hwp$kfn@%>7dL*RbbLor(y0%ZqBT2eMzdCofOV@%A$@;CXMU?)IE1L#$KV~XA<=7@yy`e|$T;@|hzx%8qkR-1t
wf5d0qCb)A4xe;dbQG<V!cvxb%_|85Oi(5p)I+$^sQth$n)9#?XQ*2^A0(JBxdrM8idL&B>iyhzUN1YlGZ<{>Ptw1Qh#?6<Mgf~s
dAWy=xL=oT_PqUE94k^f;MX40OdPES`_xfGY`<3;#7#+ZpOw{vu^t<f{9&!3PTf-LAK(MUhHVo*wgX8X*UHD~)d*1u6h3yM5&-SY
;~>Wr7{Gsdn3F}?rP-aKn#$IQMVY}#4tEw;N*6>^Zg2hC0NvtsWF*f&wlDtXk+5U63JB6;djV~EN+|4lG3f)VK&DX5iih2O{%ZzK
EQ|I<enD?Zn0#4F&0guz%f{AluA=h1j{CYRR2IUFP`Eu*C^UMuG^@TGVA@?cr4;J}2!*lDfwxI11Qr|Im<Yk(V`OM^DE?ioFai92
4P8<8`kOt>tNWQ7_$~LZf9vbgWV(N%?Vog?^7`ly^Q8l6n2OxxCzMao$?y6ag6oDQekmjnQp1DDq)DcCs%W>t@d`^ErBG3{@%eC8
V<7&!xcDDT()pv0K!QFfUM9Ris9Z9n>79Zb@MPR-|JaTMhXJ7?rl?u3i?uO=z5?W|g1crr*umH+(;6cF$vmQ}mR^g$PEqTHX|6nK
N#o&IAl=w&n>Z$ctAmxaD*G_Vd3;>muLHV1!CYqX*v5)r#{==~lpdeQSMr_`{L5@luX8SQ))*YNvrXv2G6w3+ziu+|%gSFgT3obs
2i{2UAZ-DL3bw#7Bej9;&)iL7@1qkwdvOIqld`jA#l69JXD+&qx<SM!{~%m!Y|njvpJ{+trBXc)K&#YIg%fImz?#83K-hZK{jPfh
V(a467mGcb*?`H0S2PJX>{j~k*4fqUyw(?(aGp4UT=<c*KP+_gC~DHX03ZQF1%cI%`xU{aUWFSyP_E2nPDQ;gJJ(gSk$aVJh1~dp
Ty0$j@a)^5J|na(^c<xa%5tWw<FXbC(9XDr#)BEB>)!B&OpVUwXiy>rcdSiI!`RS7d(!94`+#lZ5CS9N?v%QHLmZnFXc=AH<hTT5
O53%Ss1tEo_I%E{QDS3<EV2RV5?;}jT^yhzokO!Q{<z1U0;En-#iyffs%0X-G12y&EmNMH-lUYDSXVwq2G~2o+jo12ed?VE5x{y|
tnsn9l@q5XQ+ydXP{WgDy0Ja#mDS{Pv_pU7$1g#Wa)4Vu1Ar}ICt+Udzk6oFrL8kRQXwSMIEkyq3Kh?=y$IZGuvmT-Dv4K)l4&Cy
Kv65uS>G<l!(NG&ho3>d&t>ZvW>zSWh#5Kyi!W%MLC>9-1$A9!I!6S~l@uax)@B1m?GJA)Ewl(jk5jA7!|Y^!U(xlHcyG-#LgKP<
^z~l-FFK<T_HW`%dP8hRCa+9q6)fLSZjE6oeuW>E9#0SAN=lh(MmZ3xu>7KG(&nsY$+gTv^52+{8OQH+nwd0lB7Y;AZ;;7j_Na<G
PNUq5Hrqj9tnTKcWj`b8G!r_@Y$=*%=tbK$XA6C+x3IY}qw3<XPWjqTKJUJ*3>Od?<(ks2_#aF!rxdZ_9HLepA9DlgLUIHnqylzF
3)K)ci}SG?W8BgM;-mc{XPReXZxtruS;HI^?zTWFC*QG4p13we{pc>hjwoYWV`;%#!n5QdeoqugZf}S7pYfYq%!*ccVTqbm9Y2~k
vs5JxZeIO~uok7vvQ*6YNc%7NW#L?2_?S^ZQm*lAI#R9Txq~om*x#~_G$db)S%^LY6&`kDF}-F-=p{;4Zt4H@OkUO1j$D(38<@lD
v(%=vnYo&}sye#>L4Def-ZpZC>oX4E3e;(<pzS~x)ebOL{jph#3q%*?!7$|$L^>%`;uTK!yr8#s*z82(ncpJA$)6GV1%-bNerof9
7sa0l6FNwdth<^$&EazE6io43rceE{Qu=7r?{^3OTL#s*wpN6w@6@h8=EOHSzrC$MUDE9n{|${R8n<U93Pn@n^wQ4=unNeB_b$M+
zga}171qdTi%EVZrJXK^$ea$<>vZH(TH)UBTXjYS0^x1kyrP3Nf6zK=@pdsB<$(O57vA`vyJ^3FVAvZzbxvv778mBL%dP$>PdI`a
IcE9%hbWW=Qi6xpdSYkvd|$w8S8B_t7#Eq6Tl#R9su)ZY(Sz@4Gr{EJZSyyY?~YJ+y_`)EUy#7&q2xot9jFzkqP@IWqEYE_Gr)po
+!+al`5OjmzEjTywr{P%2QFyTB%XP28WL1y)F_3PHl;`&dV6r$EKsZF7b?l7pOqPlkOiV2SU@Q(!H(}?f}6Hsl)CJugEv0?RXLe&
xE@i&ajxVNasW18jECcc(RJlE32-!(sVOd()8<LjZC!(5_Y{}IMC%s`La0*;NajH4=TZVYy<GYMxzTfmNJEr*><SGuHrZCL)ME<O
zLS}zAB7SNKFEF=xdxHFN`7(atdA}afJV$F8_8u4uM)!UmQ7u4r-YmIaNhsVpM@HYxVIIvte%qCmj$F_Te~`|^zs;iCvu;_4o40}
B?q$f>3f*DoTb<%TU_Gb5DU8*#cduX{1;psLzUY@5x;hMSGT8Y>ne`LV=^`3<km=l=>rBmPS--H+t*86L?KHw6Kc7*3oLk4Mt2H8
E#D&dwbhnQo3PB=I1}fjJL@UQ`UT?t-PC;u(8c5I)re$z1eNduIMk`xLD(O$xUn~CJEE$)C!8TUhKTc2618P?`eQ&lWN~OM)-5;^
M$f`IkJh1YEcJ?9CSc@EYra;>|Hv7>pO=EXE{LGZ6Zf>Q!$P>XQ;vLnzIpwCm)8u>_l?|>%Aa}r)Ge|D-(~{Sj>RAVd<w*h3ftIx
hAq`P#MM8UR8zMdu!k+WS6!&$6hrT{I)vV-_wdAnV$)CvhQmVnUM>$P9rBwB)o<`VZ!cxV`J_c<#f<S3OY62IbSOOVqRUc=PaGCL
jY&Yf9gLPeAE@(QpZX)A^Bl36x?k9yKn!kc=AeZSik8?}F#cRCNwOL&{I+ohHqUmMC~!Y5=!}Mt2+%nJ+i4WABg(F*G@WL+%|3+Q
_}p4<p(XHxt=-{j@B%vv11Oj960o+5{4i<D77Yb{9x@hRa@;kvCFurccOzWM9_NHt#|EKJoNZ_S67F+|#RL>dey^C(80hmc=TfSR
=)T6O$ktjlA4{ArhBX-)(={laC*+!dkig!y=X+u7a)aH#fDkm7o@st;>2;)^`W_=Cb>Ks4Dld^)aHnGgH17mbYCmD(ACe!z;PptI
NB6E!Qb4FfnAoIeHy#v;{Bt8v^jTT*F0*j<11=n<YA3R<g1=*J;4);a_coW58(0i8A`i-D+6r{oH$&nl(V3U|FWg+{WK?6hYqW@A
R@IVmB-Txc+6wt~Z}>h^cl7}JPb3Q2#ca1ULO3sC{(W)GbirRqE~wqa^Elr`zKb8$TijIv`#88i-u3B3mSVQVb9aoISQ}vpvDxh5
j+-Zq*vxju*sEQh@W?uMaXXqe>rwfR<!cx`hsrpBz~LkQ4A!a-Ry-OdMKVqPisfW$RFFTATi%K6h&p%iE;CC<akid6)Nqw-d%?yz
V3c()mUvYXjpbW+QJq`QH3%ggY6X=(zOyCv((R(vO2@B-pJO>t4FfjmuhZ}DgI6AM85Jz8FenPx0km@Lq0WdfFEqUkGdS}y_0P%A
t+4H>9_AXXtZga*5XA#^peOh4?ok`??H4Ue9!9{LR+UHe-!@+jU8~Ir-jFsrTpy+)ITq!%K9>-s2T~?^S1Ox4+bjVvR3^^<x#k#p
YGsY4DT2%EP!^znih9G1Uk(OxOqD~12qW@qu+!xSKXi~b*m?k!x0s~F?S_Ve=K9UfYeOZrpBVq39LOw@dE+FSXKt~2ppns3+#cRU
56^wyj&~a&qD5+w`?f-m`=RRm$p!W3nxks+d_LX~s*MJ5K5R<XhyJ~zo)>>J3g=2|-Mf-tqkMnqTRdMHr{sD#otSp{QoAT0?=;s&
%Z&wTVTqjYVRu=T?Q(Z=7=o2P>J9?$wL>k|%bg8PINXt=60$Tvd&jGhdwY<VRVCaakV3GA<dHUWh+KBASQ&1Cp9kQE#_ZP@&U3ey
5+07_MKx(i6L|oE!YOdW4nB<*2GUaT;6*uihewuScFJgqQ&nx7OqL;a3hT$D*38=B8-IpYQtTl)_;_k|tVxHCC;(~fLdnWp4c&=h
^yfNms}AB;Nh0mP4zcWQ<g|qU(qx0pO*(y|dKmWp8y6ClsQHxTpnc;slPS#$0z~i#c8xF{a!lCOxJcc*i!ubA1qshb38EC)ri^ze
@*z{2b<kU~+7pkvUI&wB=>z1EQOY(GFagICYnk_+eH3cAy;(5aG663Z&$Qro$WZ3zpkalSLKs!=qT_NU)?klDrmLeP^7QNSg~4WS
yc~dCo<E$>C%gghwbenf2n^rcgH4EI;5eJL?R`|GOyFdFSr2X%Xp8W(d~PVzUf5*T(+;r@iWCz_h{$O{7Ygr2Yy=O#<S~N=mWN$0
HoV!WINAm55$3_eS#^CyHTwwBCl6z?qHsb^X9gS)rXumdofiy>rdGa!#ZQIah6uj9&BW$mxu(8OyO!zlH4D`35D)OY<?lF!U8#a2
aeNMeB>RQ=P6FtiJ*~!<G_oR$?|6slG6?&~?IIc`U73`lV|rm7tF~UZei4Ru-(`}`T8bZ{aT@Um+`%KHBZb})d!mkO-#6MuazSPr
MUhNz3T#!tLrwtq^*X~8LC3t{k9@Qk;9r_V*&I><29+`w99byP0eBMUzgFGD<%^gZ-Sra{OJC3B^P3Br>Qpz`_tjkwBy01a;=60H
ZI9CP@t>DPCR~N-)O7ULwUMm&koDFN-!#(Bq`XXdC=*CntA`y<e*yjr%xgr;=2gMe9%6T1kWifjsSj3%CM)u4$<{a$d91ZCD}|kq
+56%0&|9%M%3<=t^)_8w29g<NU6A!eW3UD<B<UbbA>n7NQhWTmS;&*yUpcX4;Khs5MbQ)_p4^AOxU;$%_VpHpm<ivfAezEwhDxV`
^=C?D^&!SZiTI<dIK&gggtQfN`s&Q*-o&Qd%njsj>F)$p1U(G`Fk1{cmFPN1asC5<bVwYazfX_uC$ve9`jy}4#_9=CaJwRBDcN{T
6H&40Q<POF`hIywe;D1%<^I@K4_1eSlgzj85rs|#lw}w2iwbR>N}F;=0GoKu1#>C9?H<if6;L-frTCi=mRz<7VB&3*Y5)iG<N^yG
v{{{{<d~tQ=1Eb`B+XznOfiK+iA+`SEZMa8nfZNv@t8m}ezsO;sfT#=7cBr1J$?$v{M|OKF41bw6y5UYSE&O9o9E*WVCz12MoB)T
OXkx(KY!E&rpviNQs5c>z<q{_BIoHK1kHI9#G>SEt~~ZIT7?{MS|I=_iuvyk#+GH6z%+VP91^Pmwz~J9h@N^Lf@7`>OXETvA+@}a
*-Jpq3k+7x4%~)DXeVSE@MsP`r}w$n;H@X<C+kBnQ_&!;S7iMo=dLa;rQ`vY$qJ?r-(j63zS61rb%Y{r3*RAr<dlC@!?5aWJ#3Wo
-F>;36lT!27((w2&|{`(W=Yv}En9lKWf1^J)+f@OTGP|7Zog3^g1X=cG^%{<^X#O0eUr(<OlBFy0uAiqK3{Mr3w)|Tb@Ytnv`}Ba
ukYJ9$S)1Hb5K6I0?$j_ew1u+UfywdZ1#VSQkQg8$5-K-I+9ZJ5GMJXNvvoHL;@~$%~dK=f6xR<_}}Ib8#=k}z7eG22L{m4>!_K?
f?U#)f05^^-`tN&MJca&-(H7@ZjMq;(yCfLvdd>a33Q9WnE8?j_0N8LVPtV6i)ih|ygvwyNXvjoZf#Kf2OO}~!>V{DYa!P##a8Rc
6WuBzvhCMfs9u-^Dg%lw#f^n%04cqJ-!_1zdfr{<og<md`YI@lB^A^|!TANn-&G<YX8M!E;wDG@oX)4QA|Ie(3>SU-qhYo_so082
45!LgYk;}QxXQH+79Rv>!E|PTlaV766h;c4oc*L=MsS&X|6wL>?(X!tqtWV&u(qAru=HZ9f0XOGwGxjry3#H8t6c@_YB7%|TXRu7
=_;kDGe74v?L*#raCjJJJ@;l2mJiRF&DMKy^<wB>KB1X!P8`Cvl)DS+-5GM#U3{52VA>D2h;GKb53w<G1>64Mzh4oq^_b4bKgU{$
SvVKxu&(>^TVWI|MMh0bdNnvZ+pqRgv{m;;9o1X75IEA_rCqFY8P0~_M=w+e$*vp7Z@<z}{An%^*T&xN-$n5{;;EmD3_ITVk(tws
?Gv@GWp9XTt+=?m#FuVH;+DNbLSdZfL{_zAf~ZL&tA)CR<qZ6}oP9qHoJmfkO-mQ{SdqOA1j(z2?U98MXb?1PO0119?|Fw$bemRA
L>I45XQ?b}f@Uc|#@VGNgO95%bFlq>xXl%r*9dnWA#c2!hdN<6Il#-y2PHrxf<YhMbMalDBWfuMrzD9!?SJ4cAnmCNG+7}CBWNV7
c~{^@HC6=KP5D|(c=xgoS{hfHc)={}@;GZSELPK_W|ue%77jKB&$FsXdOVU)Z~<(!?8r0CNtg6*FU%&Beb~gfA9Ur6BrMxZWKldj
+2mQ6Iv@&QDsH<q|D(>ILP%J$MV{}(Jnrrh_pGc`bNA#S^*7#n36vfiL!&n%hWYrU-6Z-lKVD1APq#&X3wo_b?UC@uyVos|=45V&
7&@1bminM0=)y@Y+KkIN<HRrg5Zm(!Htjs!sM%OCsHlH&a!Fq@E7eZpjH+bs&qx-d^En=-rHt$y%JkD6)I$d)>Jo}2Z$5Ijbv%C*
_qNC`ui{wm9IR}NGq8$&M^h=wRPg#24uu-R4uI!M3-wV<wc`mpOZ%nU`xf3njb3j1Xz)854rB>oR|64DGNFFG%deI86<0VrdUi#v
c{xpmb$VVQ9bB5RVlt~<bJWoWG#$hqH)v)g>?DvEmtked7ZsEU5rpdsuC4pmg@S9(TWkOa@pa|Tp=?W=!@m|U+$`z3SjuwsmNRbN
xB28Z0|rjqZzHo+L%(nQ;rkvHYD<g>q3VOvrrZ7Ec|4~x(I;)2iF}ypc9piSmVUnndWyy~T(6$Xazz3GLUpY&9pN3Z@QJQ)4iisD
5`(^JSenUK-^Ac@g#NkoA8jH7J~C^O7$F6;VC)pS1=oV;P=<a)&(bmXHlY<@!MtQgxb>wBKLXgrZ3hoytSjYzOqt?$qQR^9i!ti_
>=KgA+I4m$k;9ir(c<E044Q@hb2o;BPwxoNSluR9K~AzD`spB$E`GBx-QGpgG<jnbotDLa(6o|cRTD(mF?eG59mUgaC+K}q&Xq^h
CF9ZRfBk#s42W^MfLi?Re%DhEpxHDIF1vpqw3_f}Q7qGFjho?k_*I~f`pXrl3Kcoe#P31=vcT_ygHxTmQnvoC^LFBldmQ4U@%Gop
$AiT|{xA9o0NM+(k*g0U=Sb*FLSaP|gQTeE#N<bq(7B%(5aM`}6JUBhw+;%Fe7ik6;B<pc-IF=;XptY6+<8I(8iQm_DZ0F<WOvbb
?8~<tb^1im6pk9$=(V0a(XHddshR)VZ*eR8S&MCxXeod7-m;=S-9(HQ&jE?t(T;vtiYRfro`f_3^JAWtl1_7z0+e`mh7_UiXS_LD
UE2K{c0;*EG)WMA{2Q~jhoXS}y!lft4_o<TBU@qkH-VSzl=&2E{xd2C*>Y&~_;an#f=hrYslcc3wU`s}Bt4j{9Qs7()vJw)Ts*=$
iW2uyxuqR<(R5_k1=KXk-gABE>Z*_ogOA|tumJ%7iFoubCATvgVM0Qryv7eN@|I<JZ0E5xAc71|MLV7eKA{eXeV*y1Fk5J~s+`Wh
Y?-8RfUwo;rLFqA>w8-tmX_;@>GoycH|PZytbfzKwgnUY!Hfri@7mo&h0<(hbk6U=)V?T4Kn>E#)Ym5ga-S8T5>ny|dWufl>I`^|
wi!|7v)!{w@5I5k+`W1!t;w58JzUE97dlv5tJT$EPV8sBz`$Y`@rgiFk}6NNP;#0v+r~p5s&G(3IKXDaNrSpWt;i$l^UvB;q4}cp
d}u5TB>tvd<g)Fj6B61%Sn=MLK}IX_Z3GBEMO8$MU#Ej1g3;J-x%}V3DEE^59#%PpJQTLia|lHf2<?Y=^S1;6*yagPNB*1Jr+vvF
4wHNRy#FRFbvQ7vzdT>Z6uz%T5}J@ZG-Jv4-&d2AeYv`!;`DOpmZSqDmj@4F0I_wN(b?Q_YP1;hC0a(-j<{?)gpuGIurFV&FB%b1
_P)Yw(A8|Z%`k<Cm^a(~@ilUze!&r3p_O>^Q>zT5_YZRpu?G8Pv$^Q9AP(>7crjkprO;xoQ@84-L9>Hv?_tp?yS1L3WCYZkUR+P{
#oE<S&j>C+Rb9(8cW5qdPCy7$O6KYP&*^OT+9XiD=GXaO$Ioug_*I*?^o}~P2%mw>s|K7G3aSuz(TRtw82%&ji}Sxs3WNm*S*jxu
B`l8kU5zVYNSK?&4N1bV7A*<GDAz7u9V6Z-*z|!#v>0HH3zX#m+3R<%6JQB;o*LVOqNiJ*W_6BQedq$*ow$>4pZ^}7DrZtr$s9s!
5%XKBb>elPBDRK0%$2x&hv3~9An-q+4ef#LylRo1SuNz;yptgr$<FnI?`}q<m)C^ji1$5yy|RMMcHJe;g4bbz<K%WuF~;~a+c&HP
^fvn`+5l3<<3JrIrad-z5xEjf&s+V_PsFq@(<6#q(%nlWVkdTI5w`0j4NQ_^j#DfFlm$DvMbyz^9X>nYeurUC1UtV%ukL(mq={^r
SbMvl5vDOpR<?2bM;BjhWXUJYqemW0(f`Gm*(FbShi3oemtok*MSp0COzyyqg{2j|*v_=uJ)rHfk3<hjF>A`mkVkgE1HAc33*ll>
`>y<e!-GdWaBEbt1^$_T?zc`tZ<->hVsV^C`?dv;lUJ<ly1yV-D^h)%&Zx8vLzGSuCOTRo_V#XW`SB9%iXu5R{T=V(!frM0O#G)0
a|kiHBz(W~HePA6IfOA6U)x7E1t*pCCFx5#j^{dDA<;WMq6VJ>0wciMvqE<uoe^Z25FQNn_<9tUA8yzSi>@Of&cFJkaWw$_e9`B1
m@@DlF;#UN9IxT(wfn}mNh|8==x_JKZ#da9?7J?bNKgXd5fMVNp7m<jIYjsqF9_x#Bc}D{mfWcrRq%RQ|0!Wdkv;w`<OM`MxgLll
7{!I!pL4VlCxv_iiiv}woSzkXsHkQ3M~>ZfgzSlmq-$Hmb&<jYua!A2H$tx7U*MK04WnQWpN9o4|KII6j{3=6a(p1olbj@fHgjea
uiJPAUyKBTIkKVv&1MPSb3JIH40etSdgR0DF;tGO;<C^LN8Zm*`{?74T7cl9o#sWz0EwW2CW*E-EkTQp4e4RIx`C)Ii7$!}99VbH
fwA?r82!sPu=#};fE`G;>2*Y$>vc%-vzbxbjNDG%DLq$$uci}m@5KF!3VBNMjYW<82+|l@;%M`1Vwx?GbL-)dlMLy><@GAR2`<{3
yuzV?4qIZnBx{=6*o;VGR9MDm|I8sz<=J?Qu-Q7|V4Ak-=fpNnQxW0EcoRW8V8*d1<vDMuOVh*`^glk-{Z4IES}t&=pA>m~Lxgtg
s{%ifoNsGmTT||UrLiJno<N3%Ewn~=<&-u9H-=d-BLdQ`_8Y&-4CV56`pbp8dGJ%t_`KU+{J@4)vD2u{spmo3?ENia{mlatrk7vS
uBFraRg6&uX1a9&s}7-BKUOL0$?3<Yi0c$myGjE<G>~y0GQ-l|+1y|P1WUg3xs54J@TO=HQ9hzNSEsTZSHR%Z6-QvWXA*xoz_yV$
%jCG*Ne!2T0?7DPkU(i|nIY5?vQC$8Aes`zKU()!300uyHb?j!9nBLN`r@VcjbM^XbdqZyR1-=<h-}+L=>OEX9bYrIP<eG#Q_t7~
y9Rd#F@nP?#FvnN7B(yuI+p+}E(0G(9*eb6-6^a|5ZOnEMix4)h2JPtrTA^=A60nEl#dVD!!}2?4inqZOZrXZ`sK(@*8J;7n*gVC
5cib_IfqP6n57Ovs@nQp?jt5Sqt^sU2q=eJFX&bgQ*Sgd=eLPlVjEgfWEU8`t<2_RP#ZHEHHHmBVdxj-k;}}+_3dhB8*Hz;J+~!)
SVZu@y59KR{iZRg)KjkN%<_({V5R)>x-KFTT2RPUj3H55wK)0WvgX6fD@CvE<)J3V-A`~O6c*_ZxIEH=Y$Iya$(4$kj1s*`tGXJ0
-!5tKb{3zk)L~`x!%@`@kDqg!<wNaI;xq6M*1U;r*<mn}>5#r-U0~6WV|Rw_kpD7bg~C^y;D`<tBZ!>g-tok$zk83+pg^B-O59r&
2;x9|i}of5ucIJH|0zz8R>s87+Eu_8epjh*&YT)N9Zc+(J`(Q#ev=gfV3+nDj{}&fv_yIF)z8=q<Tm9LY37#^k5@D-H&%6`!_m*0
0C?WcJBb6Vm_>E~Zez+w%}jY$c_K9H3|(>6O_xX+6~f-`=2@-jnIJ;21gx20r+5py3pun=JE!LU%>MF3z6-b9+G9@L5OoE8eTB+h
pQ+@`EbtapYwJxfi`WBXOv8mNW;Eay>L~YE#}yf3Aajf>c3t&lBJRQdvT|GCoJFr}01MvZK4)Xe8wK*k%oF99rL|-X8MmS%9XV?}
V1AmpHX6Kq@c4-jeS*?CG5_vdwa*|^TvwV;pv6N{&Z^@EcY<j-U*0A;-E!m5dIXRhfa{R@c>g}!@xXH4eQkBP{grgx3chRo(Jo6A
a2+OxT4&on!7Ny1V)AK7=zfQl*D7jAn~PqASuLzLiL&<~y12cK`?J2EO;IHuIo6120wd}Ljv+W;pcbf``xC~gZT`D`FYM}6X>!rU
EfQVLYkdu64j;mExk$Fb4H&H~w34(VEzSGH#Xo77+=L&+gSxr}*-o#v@)lML9c|K{=TPET>_=wWp%-uvNIFApPG=NPO3+c%B9q2E
T-RZGH<mn$9j3^DM4tH2{ALreLugG1`~s=@s%>V}9!)jN$*D!UcfPHQzh$T*=mxG=xiRICPgbZo%qJ-8RV*udzD(S}dF;%p{1n~m
I+*Y{dAZ-V0*m3o*ZV7dBBU-VVkKh9C>{>%__|Z(Qt-P?a5|P(?&jW+Yp!sxZW}U+D3UB`boxw$5c8w^R0Oj=;@wf6KDo7zn2ml1
)^sL`hkgUifQxGH%=x=qau1H>3w{~XT%m_Je!dP;lISHDfsyCEs2G4zzbnImvAMA&wB0nWu?4jRMdgc>So(O)1k&Yti_}fE24s^-
@v#?@4Dn%bf`FcLhS7#73Z{C;OHpG6DoF)Jk?GoYE=gc{pWYL1pFq26O!N#56ECg5m9Exe1^UWPkW+%0kov)718D&6jnf@?==q1s
dfjZRUc0#7{rfRKU;TU}69kC0x1hhFz4H4S>AVE7o*lIM5)y7;QAbi$OEI^8wG2*gysoc!S0f9c=u_wpBATUB!NA2j6CxJ4f-Y;n
U>EPG)vO)Vu8e!A38cPZ|0#ofvTus44aG6_QaW>xELJtG!43Hz-FoaG51e(EX=xcp4+DjpmJ44&hm>Z+j@$fG@G~JA*lSGeC{9`y
sqv6&BX9^ND3M&|ZW_WokHLZgLC%mKvtxM$Z_Uvpw_|JizPwx+-C`_!zWSS}YhveH>d7YiSHg&{K1qC%h@??76>Y-9Qwed+Z_Agb
65zy=C(iSTbd^G(bR@376QakI-voXu9e00-c|}RX>Rg@|L;pv^u~U^PM%n6gV|63aF6Wu*C+`~1Fb%w2HTpR1VWE;d4^W~fbs3!x
qHO1&swDZ3G>oN~23e^&q^2oYWCFR;=o04GBcYX)lMJX?&(i9kqFV6kqKt0Tbf$aGaK0#DD)+ttX<fsh^cs7G)_0jUB<+7nQNH4r
^!-#s2@VG7+vaiYv|FpzU4aAs5XKT{ELUhvHCC|*l5Mg-=cLo@t@x<OnDI=p)EZo<JuNI(ae-AXs6zIgkeufZ@l@G=&fowiyUYUD
{STdJGyNY@DPsVu8z)wQob42q4Da*0x(E`uK|>r7Ig;v!r=f&}rS6=Am7YF=D2PWR8L#?M@^PzeXW$lDPzP<1R~z}6<dY}Kn(6HT
R%>gp^$?g<=Oh+Q!dQ^NRR}E<8zre}l);Rf&8C+$ZKy{9pz;PJRb}p*p;3ebVRk4PR2o2%R;5FS_7PIr!->t?(d}HYla>?)VjQiQ
-ls1hcwHwsmZFHfNoVz>?wL)>1-&#r^v3ei+Poe`O@7$i{GCyLq($feqM@R9EEte*hIgmP`K?}^T9fhk+X<>>uU*Pg)e|f5a-o5F
^ise295GRAZk8@|8e4frhO=)$Xv0jo0w3}n<o~=^z4#3x-te|82W>%O#3)PUE;4!orv~qq%KTj8dD$J4WgD{mg=?Y5N0rk0X$kzP
`bnWhg(O^6f;+^K6>IjkJiuvltaAW`(WQV|bi$KOrGTq8%3<Kk>to`(DQfN=$%Q@1(&C*T-<3Q`&a*wZ_*2wn%ndd?yp#m+0r<-F
H_3e}^?zI-M0skR0r#V|gD-0d(g44WtiD{+;GgJ<p^Z0g?K}}OxNc0yG-%^Wk^CUEVn6wDYmXH|zS3c-bSgS(K@+7p4}u^7cmS<b
h~C11oCUn~rga}`2s{K4=1&&2fMcK1;L=5WV#JT@3wZ-?z#2pEL=cq0`D#8`ul?;RKj>K~_!*T&3J75&%#l;*O)x&J7V-f`Q(D+q
jivh9qe6T1@bs7s09jQD2CijN4b`m$=tOHa+z<bL0Qnvl4M%?lrIbc#M&lpuBMuMuQ@MPpNQn#}a3GXaVs*3;SYivqN&z|^iT+!7
+(uG_HoU~XNKM&ZWnwl)*lE(S3?<5eI3vJ3RlkeD7}4<eXJ`3$YG~h7UUrI}Z$o|T#uIvRsg-30yq2Y!8?$6RH0ev7B@{l?tiT`Q
zDM{n&zbsFN^MMZ8;)EKcSSOEGlRimYJhlJk_1zD@=vH12Fxx@<4Z+Z@pLVKHDBJ?KX|lk(i9>+;?%tQ{+0JmecxSVbHOTK;=73Z
5;JXigU9QJyBQ~KZuS{Z>pqr=rox-E5W&Gf(OcI*LSC2)Q*z%P0KS8TR%P7>AMHtBIUy!B<pR@mvYHo8Ws%l0P-5OX?Do?L$W?2w
y#1og_>(Tj2MjdIStQd9#0_!C!WiZf+N<>SE4|u$C!+ch?SBc6)-x;mozGx2W)P6wM&Q@2Qg15$!yHs)?4KM1dW={5<_fUO<(eJo
-6-ra@2M3otUgI&ww5c#doZTnAvsimSb}_1jkl}=#KR*TO(q|u^DLcNq+0JF+>q}gx9p{3wK~#is>NMn1=*wGa6SHSe_D)3#b4`t
8j%h~3(aB0taol}zcwnE%V@A!u5omu;dGfw>vVTpS#4YWMVACdla^h&l%(omt0I;DXwno4Xm)o%s*uGuw%3lhaW0zX|G6XlV>8Kt
banr+tw!`$nn2ij2g+!@LGue8ywT3Uk`h`d723Jy3VWJ(wP%I&J&9?KgUhHf<%Q}$^Nnh&`IX!-zJUA3ENnr{$Lv;u<A2+p`6cJ6
5FBZSQ+`ZjX%@hJMHW;(>`0_9Hdd9rdl+v?7~>zbsFS$79*L=-_a0L;q+X|Y9Cm{c5o*ZXPGVO#Ejn8}@P6IKmnx>OQsTy4pXu?L
cW!1o@Xa-Prt<D&BH(aT8X;6v=1>F{cL*5VdWU*FK$GA+BYJ5y?S_J<LnyA|gL9isH{<t<D|6_N_g^8Xjy^2IXo@z><4J!2->{RT
nGVRpxNH&{8wvnVB1hrxzOk11cjqou;hLKxxbw~$@Z#C_?B#-db9I%`NQO^=eAa2!N_9K5fx44XIDPjn4>R_J6y`P9)qpSOgg!Sl
I(n1It~@B|I$!Jm99jfgr_rJ~V<%gIh4+cF$+)IxlXOd=%v45C%$;{-=v-$j@Hb_R%@)-o_(vwriBA}pqJjkfke$7~5C?|q;FX=0
0e9$_;0$^&yCsrXn;Z?k+VUUj8CaJj0S{2N2!jq{y-rK8^hSuC>u5>+K!t!!_|!Ro#SQ$er5k}g042$-Hx+G--0VK-DPrr{4U2b<
^*>ky!F#tZy-WEGf>m2sxqwo^Z`?n(#FHz1m*{u3@%8jN{UEvBcIWQVR__bYKAMvu8Ttxry=><Zvf74z(XR0<Q}BVrOG*_|izsh%
P~tGnfFvw&yFdkw?l+fCm`?>*pIOCg`RSY{$Wl>^Pbh^@LaU=3ik^ZiOlU)4+qxCi(IN&a#~b_kBy1qJe0xMr)^xlbu78;~#Yh0Z
C7~OtnxNpj9zZqmz5PQRMbSyvI3+F|Z@6L$O+FQA2#s0YKh!<BWl^FKh(FSa&Mfrulxv^&598ujQ5HRlPqe5v8rBSnr$}kSZNd&?
JkV_%|6keQ8x;NZDqNMa3u9f9Nj@|mvcC0>ala{%>fIGZC^lmE17jJcijYXE*MP=#l!(}N&8Z1FB-D9qfEuEO>AX~F%)ogpTn=;@
?nGK~NXQ<u<BPH0sEe0tqnw(SxJ+V+0(C&ZbRvNHC;BqCDknlxeDvm*tNeqVM+zraLJr$n(%0-Z|AV?bG$?f{4$_+HlI1ypEJ}=X
g7svtS4`OwvNn`_%a-A#25t@*ra0dc7#9as2MvKp9ooF9KD3l^9tma56Zmm2SCo^?WA#1d6Q)6-Myjlz%($U|s}+5~`AuIgy<UYu
(i2s-JR_Yg!vVwnG$zDt!=>Qn`hl283B)ZN>RME@L%Iuww1=IwA-r8>P8q_rR%k#`(w9F5x`WbgRnZb9B;3OR7<a>o_c9n&$&nZz
xtDAwDdh%lqf*dTC$X+F*2vE~SfG-I1eM`hoEX*V`HjiIggTN<=mj%=jI7q+h9mDJZkCo~mArg4z#@&hI2Tp!E?cc5$e6}WFz#FF
vMWE-B87JML5C`YBf%}=r>r^pVVt2^81+@0%S&{9`fz5v^$8YxIHLdiMpDstf+h2a(=q2;m0=9>S7P%d1NL<QL8Wshk^45HKC-JX
JZ8fz$G(=Rfv&K{o?wHRdiM3k1*wfRi;$@j2xtPn4hL^T@!vPU3%wFXDUB=X20i$w<RAq=B9Wwdl4+~ktBdzoVobx>AJ37bs}6<b
yZ{c2VLT`BB2aq!>U@Myy~WVg2b=8#vr7iqQ4dB?jR&Ixi6VHz`A&9m{t3iIo+qf}cyV8+cB^+}BI5T;0`xm@+{eNwcOB`K4Hd(_
w-gN5DE&y|#5w3EKF)=}@t;sewdrAj-EN;ojpP>vzvz`6&VK)zpl-W6q2DPZFF|V?*Qnf0`f@hlSG)BTq2FGeWUlWaSmVKYUG<LU
aiPiTA(Nm16;S+%6D^P)8*9?&S~LE5<1S133wZ2OCvw40pd<J4j-{GdYFR})dQ2z5pzhjFc3vtN>Ix(?0(i`nyBRDFWRgGtnc8qE
=6IiY!Q~@o34mA{#3}--)L1loH??%P-*Np(9#t!E_X(48SN%c8oWhK@E5IyC^e>uSS<biu5ttWgCY_86QDRwQb<iYVL%m_*Q-ow`
u-QS5t~SPvuSD5=nW{A$bu#N%m9v_y=pr@`bG#e$SO9$6YnEq78+23f6S{|AWm~WIn|?Xs4C8MAGIxd4nAzlte_iRr7s;9{6T2EW
3th!V?|8)q`q?2xBuT(VAZ`n?q?K<j5RbGD6il57U?j0}(Pq-j3k4$y!Led00lG|z<iS1t#8JMM)!wf6J}V~)7WaO+QI->B;dtaS
#~RV*6C<uL8sz*n65;vyde$ihZMMsx!4mZz`?y&I41%D8kJNgLGIq<e*5nn73+>$fJ+h1yD6=}CXX!H_AQaSKzVU{xl~F@JjuUfO
9czIIs7O}G)@3sgu+#2_^10&ZK*W8HTkbX?t*m;<w$y5HwPcud6nr|^vQ4=0*W1oNvVRYYzVuMMYIx;>kC%KhNI=H9+c&700D(GI
93h1*RiQRNP%}!27`ls*5hc7$`#)Y*l%5|KrbvdlfMeso)aAIHu_z1&9!*woSqkGIKtxMZ7gO1SnGeFg^R?pvwYKEV9gFd!jsCII
F~4yr5>M~t7L6r}-D&6$z^U}U^1lPAXM82BePX$mTx|X{I7~D(`DiF?@@_LTKTmf?oSW($kJrA}7WI7wrT6~vN&1(|BwO0_8E01n
{s;$lr(C5gLOk;o2U=LFkE;3Jlpknet3mI3CV%x*<Zv#nfq#j<&SgzYiGYx&C@B1CQgJY%3g!{RTHc){$z!Y>hS(WZC>Q{Io;>ip
gk2&WW<<fHWE6Dn;eL%6;#_yLSy@{5-?~Mo78@;?Vb_oI9}xWoQeV@?O;A2KoaZZ@X<v`rF;gzvM#42iL~OxWWZpuCS>DrO&6rQM
kWP^LC=im|!-|^23Hry_F&)pa5}Ro>ZD|d4*@zKQ0M$Njk6BSYN(KaePo!X~nUJ-Rg!+ouiJ0W^c#B)Q-e#M+#;*sY3T~B24;&$8
g$^F$l4e{x)M6}Z2#d_^>c@6I4(x!QMxS%Q)hf!|pd?%0%$Hoo&JTGgbnm!W&z#pR)kUNy@bsE2l1o#m_q2&@J=x`otY!$;Y7aF~
IY-heCnL8JK7ZDXc;LFF3KURiCa-CVvvYWf&~Wy5;aRn4^4b;{A-(!@t>l+I!YXUH2Id&?WL!O2G67ElfUwVxpYetJl{W<?-i#{V
W|;>0|Kv9R{yuLM`UD7Sm;v1)`v2<;gS`6IZ65(_$THf_!FGpX6d88(=3r5$RV7_2y2A++?mf#?)1>g`L$KUpjZVI;;};uX=kFP;
7jJKl@Aw>P536apT|=zD(N;EWS0LiQ>fQ;3OW?8W*TN^`%4Z^gmDg9{Cw1E8+3G|vc$h?2WW8`1)3@fi^zNl@y~&Y<sUiM@_8T@c
X;c*0+O#pw9d9coCt;dSvF)1M%pv}K^AmpJ+*gr0poVx^R@H($yR?CuB3>fZV&A@!wer#4C3&Qc)S|pwx4+BEvj2gt=8wzO9r~&7
?MN{qw0$~C5r1I6`+zR|@I<B2D>DmAo0%Oi+JEt=$y;EiOn?~)x}4E(6~4*Cz~LD@tZqb-0|H)mhM(1^!KL9u;a`@f8bxm||Awk;
DM1<yX}%cc$BikW1DKq)qmLmlRBlBTN;m2AoOrD`g+RcM3UqE!K?TFqVldvd8)4#A$3!e&k9S^nw#>NoO$3nI*zOb`|5z#?X+TNM
{L@?dC#MYL-EK?-EZt(|h2SyHBQ}WhZ*laQQzz7}{%)MnWM?6BhV{fxi_!&`tgOLSD>unQ?K*SklcHIh-11eJU>00BLUmR~RWj`z
qpnw)!p#5LeePyIpw=##2URalEjE0arCR*%y7WE2^BQvIZO1T_U%f_6_UzMi!3bY5D^aY2t1Na7*MLh%hdGu&fqKz%ykT<Ox8Vpo
4>BbQ8;z}EDMVe5{N?))v3w?x*<YTL^p!1(mL^2!+c50&F~jqS`_BSq54u!D8#nxAklb--UP<wD*>0Zm2fnF;#C-g&ZuDgB+I?Nk
j7-;))5z+HIg{7)CA9d=x#fg&JJuBe$fG4u5}yBc;E_bh+bu7x;d<*&l=fe2`xgA<|AlnzfVsJ9sMx|P(hl}pGta=cjVYth<X%~<
50O^Y?;KLsjbUBJjm_Mm6RrAks&qrhdF91x%VHQg`=9u{@S5#)#ewW`{y`*o(9VmI(V-7+E0(XK>-V9+hTEhLnkwC?vAsx<<x!Hv
PxUSO)UuD4>QWrG&3QT}Qrf5^MnGsMYSEJ|GtkkAq$watIE<gtG_YHI<Le+3K|F-0tH1{-Pf&M>xp|}x39$HvK(*VZ3SL51c^0?T
I2t^D5WAPcqBeu$Ym$_bnG(T~jl^uEhKjzJzl$Q*q0A$9oIRMf%qOEv8Vj8crWYS>7B<KJtqF#~O#uESaJ(pcm%oiYYAKs>7C+|%
%ENX&IqROgGMkAIDgpNj%YsW5FVQ<>5(p6nrm^u|n7Z)Ee)WSBDzS(FxKmW~IyYL((eM?&`MSUR)f+&ASVRElOv}h@{>Z^_IZ>Zo
-0o}}Nck#f0Y9+@G3IOZM!t1V@x;$^hyoo*#kOeXibCl6epe;Y*S^d(pcPOsjFOWM`rS+qIqQWTmIJK(rfe3pxtTsMv8&35=%hTH
p*DQ%8~XD$)H$)1JLY8xKIAgt4Q%1aCt!@e-WB;h1QD>%w*;(1!G+iwGz_`;TPF-sy$<1Z$^k%EZ=Q(Js;O3!p|1TjI?BX$$Zi-R
oQgmOz1JD6(lr~0n~yawhf!TOt8x7!(O9l05Sd}K20QjOjR#z<I07sdcLb1d__xBFmIwwJ!ZmsWte@ozgqoBKO%$$Q9n}HjUS?Wa
f%59>fyNeRawq<$^URF}9$ab|=*l9vVDGmxdz~~fu4sS7c7V9Q0;znluoUx36ZQXUJUDWriFsD7YL%y#g6(rMVKumvH3-o2>K^cv
aAKQR8tUKw_|41UtIC8&@m@9Y4Z6x<5*vp}iFpspMG5@-@mQb9PC}2%ac{AJ)!>D%b~osGQ(|PwqE+y1^54f1+_@Yle1!8)DQM;(
<a{08^si4RnQq(?oC4ccpb=%wqY3t+6VZwd#T_6whRuerZRsFMXOkE0*$tNd73w;1jOPdBFTY;Q2a=M3I2(fdq}Ve;8Q5DShS|AZ
)?9~&6p71HH(N+5nsb!x)Z%ReS+U#(FQwymlwL4lfA=o_`?i|AgQPiGZwsdDBc=|GBTotEN}@t0X%n?uh+an=!`^91`@fUUcnYh0
OOygPCJ6BL{|B*4W-G~y6r3DK?in(-HaK`b88+1FcqI<ON;`be?8vMdqT=8`2CsK$1bmf0%72!%C3oZ6seEV1DcYt5K3&GnS^<Vg
=+#LAZcw$k#gj_zyQL+PzXpbo=us%BA#rOPdoq;e2my68rddgNgpBI)6z>bvu>=r9J%l{NAJN0XC?0M6Oj0h`j*lQoSyYwgIfY@X
p*I3-Lk#iGauc(tnrI6=pn1WEXgVF(XS3Bj9hq<0q)2IO7uIZU9~HN2Nwm2i`Nn*rsD)t0LrFGFTtPDQ-{K)ni^@a-(YQ9q!GX;7
my&N{dOFh1`cBd&NMGG#{E?u1EK!%d1nEq*uiaZbRq!60KUH(OcKdOL&@qPNl%^7-_l49>3?X#)Gzk|T@P4!v4QLEMh{@}1vG5=C
b>*^^grPB6El%!E1F|qoS!*g7nMDWMv=1ul5Y8uZgwDA^ON-D!alL9Y2@gW?5;`&S8PpRsX6zvi=ttd*=Z!O5MFV3(FZ2=X^In)c
*oqK|ArBg4z6mK`IdfFLu>^(wuhErkQl#ucab>?x{>b?`K4=b!WH4|ot`5Al?E$FJy!hu8_+4T#y?tht5`&NN3y#1#II|0R@Zz7}
uq%x5@1pw%yRwycKRvfN#JtAPlBLHC%CQS8q4Gb}zj34yQ^M|TT@V$bUvQ)UgmYF6$mtCjG=#lsHFFR}cY0l*iCMjd^kro9`#8O<
?_1rwZXxxjEkMnaO=zqbQi;BXtAN!rE~{GtGqqz_1iSA47rZ2cJ2LqS<L56xZ?U{F)_qZp7tH71&3~PssHR?XP8@Z?x`xaNfMvS;
8<fe1rQ{)r`iq7((VZ!EOKx>{{NTf`tqt$S@2bKSE6?d{q_7#62#{|>)qq5}?5ccCoG5jN_hwp50-#<&INM8s{900!4>qP}6t^u|
APF+Scnwa}4n#-)fy@oruPXRrA))pjo4<;X+m|Z9O+Kmyszt?lCku7|<NQW~bLzvXBhs9zk8_jSxuT>!t>UN5bX3QNizA@S!0lWk
rfMbs%72B@5A0uc7CI$gS|!vT`OK56)y=Q;o$jSYH@l;MrZ$n9;v`(xDdF1CK`ya%_PF)f=^IA`;sxi5>e^AqcN5G|qoRFuy=74^
VB^Gx?uCH0Sh2*0n6c0E8RZ>=J568jN%cUsP5~XKmcE?DXaaAH)jr1}I{_<Mh9QnhRg;4i$mJ9wIt$`|cpD{knrbHJiH(uiZ7n34
e!})}OT1C%2s_4If0I~+<nI9jGZbA9&Er3fjwUx(hRXD*u8ap2QC+mf7sq%VPo{++lR5C*IJoerv2(QsacQiLf|g%V&f4ti49&9A
*U!0Qm_Y{4h$CV8*wHvR+LtK9D1&1aY%@DU{k0%g+EQW?9lCq^kd{)9RbK_nF{{62qUSJLs$_|Dm+!tFL0V`^V!}LZFpj@ys)#Az
;lrWEIa&1nfL$7?$nSkZDuML9fb(B3uI>zwjn)HIOvHFtQ|b#&$5(?oAh>?w_MBPkaG!~RD5z6Bgu)UuN(XbOReUB@LP~?oTR!9W
dI57f(ZHlpyN<9Nu?MsHiM?luHBz}OR+e*x#<`AI*wwAgih`zq9yPp-hTJzb%)IVBMfQDOat!|P)~ppn)>ih+73bUiN8@GB?rP(R
{X9z=poT8TT#q$ov^#*_w~w%FCB~JtA8s?WfVL(^l>u%KqkO8VBeTV-fQ;nafCIdRQejA)$att$G}yA64xTaP8bHy=x(cn42c^}#
HDGqt>Z!IV_Q+1+;{up{ul>9drmF(Q@D0zOQb0=MEFD_Hf?5PL#dLZVd_CTG24;Dlh7W=>wnuL94|<Nj&N`QQ_R?&0fRM(~#uUtQ
2b5uP$dHbT(nQ6&<D$3@wk}5mTIkB`0{nrIc!^<6sKNNw^bsdiiQ%j0P`FJ|N1Vnm*kH@EsOG%)?Nc6Q@#&sp@PjiBq`9IWW}xA;
Cva4iciyBpDl$^AJ<J;6+qj?BN8H(qg}vUID)koTtwfMYE9kn6z87!O+<Qab)2?nZ#$-|+%rR^>Vz@bgJ+o^iFz)KlKn8#{!n#eD
tK!!U44(uu4|BK}skU|<W*w+Z{NU@6lFGLu+-=oD&vxaKiy|(!!tCpSSEa?z$5kV^p>#X$$GH#XQMDDr#efB6?>W#<df0{r$@@wA
J4}yfHO78+S!G^Tr(nZT4jYQbUF@lZmrsdkA}~Y|G7qNrWP7z2B$u^T-PKmUWp?3&{C(^5jaaQ0Qto8SQMqUTmR-9tSk46IzSlE5
Qn?W$_4V`MXvLORhOsLze7q;X0MXySM8fHn+RsyW&Ya6vSi>x<eyyCrlXH}l_%pIA25^?+?ll3ml&)a8Q?zANBj4rTqm{UT>k6`F
taM{L@&*ZqFZb5b4h63CtKxG(ZXjvFV@xVYm~BwHfC@k3z`j#XaWi?Asi(emkvaYm1B^yB);CCY?0Hewb)ex7_`3sB4xWod=PD5_
QLy_%G&<yY5I}1SC+3Ewq-P-5p%@$Ii}JZ|8BwmIK=&qZ_#5FGftn5BOSZ8?W0L#pcS|FM`yDQ`@gw_V4K>PRI#9?mQ#%Mi^ScoF
J)3}+iMOT9E@6jS)|eyGE3OXEjlfyTB21Ms%3m$6W&nC+I_^Atf;B;jFOO?P$)wn%RNBI36&!z6%LkGo;=F|O+4b?kx*84NLQoH`
qIgDCnuM@y*I@n`Ua_@lc}F5goFFAo2tSEsUS2@1u=`y=g;n4T<vA-L3RF`Y+cy6!;@SPYm&sm-Xq@{_mFf0-0|@OH+f6?OaS;w&
xOQ-qO|39e!L~pHwKQ!<5w2A%n0H(NMCz<e8Wo|?3Y|2N!I~7c_{Yzpc7lc98{hw0w`8;5a#qP8el)4<WkN}sg2h-mhQ5c^H>?D^
3+VG}2$4L69MiA`Yd^gtlq390)yTeGDM*yH0pdIn+redfga!6L^mXSN!&YG82asXp@^@2VgdRn*ay4z;uzJyNrU#`DX-WnUt0?2E
fx9PwdJrUn^ljV-0#Gr>>ELrssZAD;Psj#sh3eNt@y)4VcuhRZs0Nz)ZHq{Dd8bp+j@wfUcPZoNr&aMniTu}1Bn3mI^1&_E{&1kx
b~h$VV;m{5q0Pypj3ox)AztxtK59u|KWI1l0PE8@r&iRU35-PQdon-*C-HkytkaqOe1d?WvRm{F-|EG5iIm^nLB9w<Xs$Z;ke3WZ
@Ua$Hp!Zr0@zK6&rEsTFn%=AhRijlhSxcRyXHeYWs0BP)>#U^v%YlpKbKo008U`_%1knh0#fd2m8orggZuAuOz6_d<>oSMaj`!xS
mtW6_h5xz<gtlk@mM{m}FC{ni!aZH@cq^U#mO@3D?I9fYVEbwQHu2j_3B+b^LlFM!WAHe>vZGcLjLxtbYIGT{tYv(J6H7>w{-@+C
)_Cz2w?U6@^FpABDm9z@iLkYQq3}5!4LIbZ*Fjnv)?^dd_hd1E6Si%}$4W)SdGW2%t91xP-59$d;>F&xzp>VfL0f8Px3)4DUcvs2
7)l%vU8t;m4I;SSi|9mfubg==2tqt+?CxMj3nXOS@7rdQjK&N^R5+5WfDj#ti_gO~7$2MZr?@SG4+btN_}uc;dz|@~=wt0H!f=~A
&j<%qnu)SVTfPM3rL&zM{LKACw#7Lo3wnAKCEpC+x`gJko|%?<T*~f!$0K{eJ;nwFLC{_K$)?6&MGde$x!uNwv~&jjh%>e@s4{N6
Ni2?uZEMl8fgjz$4AS>VV|Qyd^fhkX69d$~{(p`EvY~dU669E@Ab(-gi+*%UJf+$fe(I1X8*_Rx>@RVPdfLv}3GT72Ri-8nK?Vf2
AnVq4%Cx1*3HsTRugtm+VU`CZ4=xv$(-2|Xa9=Xt3iZS+fWwg^;$zj~0nvfV+%qE0o4W)cQo3p^O*dF^&$wT(w=IqK$^^?*HbUDh
e$^}q>qLis;RRnRJQuGn=-uShYGTUHG==oPQ0+bgg?bTOn2QKljA)2Uj)o$@ASfE~4>*Tj%jNKh7O+x1aB_9@se;wQE?B%3m{W$u
{v|}^u40B12Tj4AQNf;81!|~21M*6c;{3we=@Mg*kj~RoKX#W<3eK>O^-p9)GW(OLE^PgiqZEW#bf9v!W&N>I%~>W@XEddD2{4!b
ce-A49Ulav3QGzETXAxUpe!tUW7u!Z!Q{jX_!42i2C|oi{kM8X#S7n^xT}bv0qhuupA+NtMTp|_SxR3JV1QJCoPoz<ct=OW`krgT
u$Olk^iGszF<RcjE0B7fPc8Z`KF3D18WDYq$$R8A*Sd(odn(7{)T*HwhdfYIZUim@GtlC@Oxn-qNU|e-o7SpJK<(YLQO*5+1Gr@K
PRtTW>#lnt8pqc+K_JT=Dli$daxK`kE&G9W642IJ-0y0PN&S@;iAqFgHXRa9?{0f98#fpnpSwLJG(Vk(L|&LllJR>}320;TZ?aYt
0h(X)zwxNEV9l^!8>kcq6bwj+(hi@PYA5_DKW7n^99iiDk)xYJ-QlD%nT5C1VTq9q<}SvM+rcogvWC+wm#YZ%79l(>x6W2;zqSwm
*~&j-)#N}wL9WjazY1LbZ@6@oK{QPI?}2&cn^Sa)4u?i4+ow93!d`Paq|T>RHnFgvn~9~AMd8+8Q?sK?ba1ZBCa&D-QQB&Tgb|Ko
l|if1Xjk3nfX$151q5tm>k21RnquMUO1LD!kC1e;c*)h4CM?xDZ_325{e+x59mTE$3r`nwNmG)(VaDtK@Z`ByBn%W8W+r~w6V?ev
Yo{<+&sEKKxdN~l@6(8Lgq5ZHiEal*iGt;Ji?`c@W#lcYZ8J2bQPD)9;_RrWD`oc}47omRV%Q?)kkq*1hNj`I%i|omptAqj@TNC*
l-;Q`tjJiU<QTopz9!pWL76lB&S)LP5>c&|)DkeJk8;P0&5(Khbjd)m4Q=B_!(^c>saFhZZyemVAzbF{ty9xOy0G^@sJKQ<t3YSE
+x>l5&1M3DUU-)~bX*S7WI~T^vlTn#Xzzg9c`e)^V?5-VS+N*nbQUK)G-Y~kj>ZV{upJTaBL*;o3PM<w90iFZoGBH)f<wA+ct{ef
sC(y#Y15-JUh4#cwU4RUZj?%-jN3@23J(WkY+|C5849?c|F*gxf(8*XP=)(mi$iLW+8x{f^;_8M$3MebXa@hU5<)Xl9;vsG0_1!9
oHQ9c*o3J>hR7FhhY$^@9TO1xnfrqMPFynNSf3{XuoWAFysCVIcuB+&=04cZ9Q_(d`zl7xjrwJ`@s#m9msiwyCt{MoQ@gbUw$YbI
Ok&%=TT`hb&m)@$bHAj`pMO(CYinK{y^U=%CnMRTeSrLw+);cq)phbgS|t0XtcJxtHer}}GfH0m3lNY5qG){&8}j@t6-<c2y>J25
oN8~|h4IGbu-?n072=*7Z;wVVtsG!j{5c<xGAdq&0NEdVPc3}P-y=&0??Pl;!zTFCE5c)=gy)j-*8FY)3MbSM2e=aDCE7>|`}bgk
o9smNgGb9<b*gt#C!i7hnw)|~AQ#z8lbMJ>ol9)TGmxcDy!C|>yKyQgpP4VKgl<=#tkQ?U0A_)xs1_q4kV4d~$epu8XAAiwB4tcO
)15i8l1EqT<B#`fa|&HhuT=?B_Kq3XLi&xKGKz5ViRtKxd0~4W>eP?2JgqT2^?eX-P9>$dgM7uEC!d1c?>iUAPVth~{U1QkOJM#W
?Wk4-cchgOW_1<gI+gn=PC8zzE73_Js5q#KN*vUuI}seEt+q~0T2Nc5rfA`%u*E&}OR#Yp!z`zmBP1dcV(C?<WUwN=489E@yRKoi
9p2D%08=MR9_OD+Yz0$b&bSp6e|8v*&XHp|hURcI=6Jc{3-J6Bfu<y~MQ46>4YLV$OWjlW7dy_|raUM@hZ*PA4K}Owm~0&PVKFjP
W#Zl2GZ+d5Py~gvepFb7_zcX}=8lLC&r#pT;X0Qt8oot*cCn2sjf8E;*`xuV-UNuCFN%*jtjM}2tXJWVO1XUX>D4R{J()dc&98=k
W<Efsb+R@OXe_t3PG>@W*Ho-t`P?^h=_BcnUb+!(=q3PJ4OhM4UGSMy8iB}zk|96b!=e=!7vb(?xIz_j{4Yr@E$F}fElDrUi5-7)
SEuoq9{OuawaRqMa;AP#6*R-d8d6^Y&J}2IRzB+za2yXo_nN%$Fjy>DRgcv#^A7hXAfKqVN=YBp&5*7xTMJ$Snymj_9d;BGaAUj)
{g5qV$IPESj383q`AB-x%YPE_?P%E6l7(Ai5Ju>;yzQDFCVuPzJ)9(O=gAAVPNK^umwypDw6cMUU6=Pf?p59eSV*Bm(#Vm=@ItdZ
gL{K%IRP3#NwqDjjZ;DI@j>&?KE<ZG5U^xsJ$3yiR-q?HH|)_DJG9o<WqwnjKl<FZ$2rA)Ne(SVIa4(JgRrd+damOi3-(Sm112Mx
+kK8VN|T=CJA1<)lIM=?{n=qocC?gz?1|*__LDG^y9W*>Wx$8-fH<cM=vic`ZJ-o|5RnXS3UnrgCWsQNkfihRN-1b>x?)8rNL<rT
P5dKeSrL&vlzDjshT{k{xe6%>LN?Pwv7scfbBk0ZIm^5Eh<2?Ecd^|3?2<SS;6s3kjM?#oG;hK}PD{OMkRa_Sm`wat;|OI!ww|;R
Ag>u-<^7-fblbI~s$7d$1l?FmN)6#f&&SR>KowmJr8G1G^?=**%z`#iw|b&b6BK!ZP#cUILq&O38a_Q`w1?HaLJ&C(#YRKq&JLuM
K#?KNTWOw(xBe)&jg-*z<zU!`^vKqtMmPJQoN}u($tjAG(q!`BiQ`0bOdstufUkj5$x~G?7dXh4p4zDwHZ)QfDfdZtVE40O*CF#(
YG-BDdoeNDqfj%*&U48F#>%FEckCVJPSH4zRu4eo12KSY7BIafLMHukI#k4TT8Rj7|MYJOR#@gk;xU=yPWmzB(r0U#ZZg`Ml=q!C
<4Gc%u`Ac{o`7{-D#R+Po^f|s$LMb;edZF=Q5XZJIr6M*g7x2&5YcAWW3q8?97Lso6y9P^#WB)2MRB?f-E1xI1n1KMWAnqxYa^G(
<k}u2kcvYCSuqk8%=v%L7${YCyIQ1^-yFjg;OL3O)w<`S_g8(t<Z#k9(#(j^^J&l#te+4LyCi5ejuG#tq$7m`?1*n)N^m&rp>%8t
w%TyJk0<F~q@Itfscf>=b@a#1g-5Nk3hngG<2yWHG!D5iiYXVN)q0z~($+EVfl^)k<R*z_!pH_&l3g$H$fBQ0n<K!mlN`gztiF=)
8*F_Uyo#aYva%Z1Pk2V81A3733b6aFJJ66Sp<ewq1f|@rKCu!$22U8270iHGc>9lQf5w7q+q<FF`rnvr`?a$Qpt%r)?EnA(r>PRs
)~n(C00HQ=0sq|yzN!q}vBYQl0ssI200dcD
"""
raw=lzma.decompress(base64.b85decode(''.join(DATA.split())))
assert pin(raw)==PACK_PIN
pack=json.loads(raw);assert set(pack)==set(MANIFEST)
for n,v in pack.items():
 assert Path(n).name==n
 b=v.encode();assert pin(b)==MANIFEST[n]
 if Path(n).exists():assert Path(n).read_bytes()==b
 Path(n).write_bytes(b)
subprocess.run([sys.executable,'-S','c34_701_balanced_tradeoff.py','check'],check=True)
assert pin(Path('c34_701_balanced_tradeoff.json').read_bytes())==[270245, '5653c0002b4c11e1f08c9c48215c0933a382408ce0de94472556e73695f84820']
print('C34_701_BALANCED_TRADEOFF_COMPLETE_RECOVERY_PASS')
```


# Preserved span 394 (literal-source)

```python
"""Recover exact equal-fan-volume TREE709 quantitative certificates.
Needs the complete pinned TREE709 proof inputs, already in the journal.
CPython 3.12.14 stdlib, assertions enabled. No numerical solver on replay.
"""
from pathlib import Path
import base64,lzma,json,hashlib,subprocess,sys
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
PACK_PIN=[59761, '1d8e53dd8b5b556883ac6288a3296f325b7a541f77bea0da4ae55abde9380860']
MANIFEST={'c34_709_balanced_tradeoff.py': [3805, '53fa623670e7c791c3e487f4b689db4646fef5fbf1d25594f42bebc66a176316'], 'c34_709_balance_witnesses.json': [52509, '9a2528f78e59b4e7677b2f3459c8794a0509a1e0f1fe8ec983a9b631b2cbfcc9']}
DATA="""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;OTHGKV1Mlh=^ll$&q7x#_EKf&3%^+If2zKNdN|+M~`Uuni<SUjg}eFnq-+^$pES^=u7AX
#oYqibA&jzuNv-Jo$UocRpG;v?5R2GHr1UZ4_4>;`wkD6BGmJ2RSI=|FRz1S5WI$VJJhPNQ(ChE3UAxqQm5iL<)4nVF{m1V;VI%V
YG11*^I|r+IS3T;L~2SLC&F`#!mQ+75>aEQ2lWgL!s7JIz9DRJU5d7VK<z86KzFAwk#C)>t$4e}GD2k&4oRc@)fDH6IA1zv)gFFd
I0@fEXM=y^5)n~E;oTOP(o&OKOdAg^5o@x5y(BW_mg%&VSDtk(rkG!D46{aBP@ic>7+bSp?!h_2m(~(-(0&Xyo`CI4cU$wmf;oAB
p|k+-+CZE`a60roqNMM9fa|fzo%fglpb%<jG_Yb;P)|>VIAhw$X)JAHY+gbOb>L1{yu#s1AisRM0V{?Ezou;zC^?OnrG#(4)J%>k
>}_b$xj}1sH6Ep|#<Vs28=@&RB?$?0;3e`j+XBP8d56m~`5Y)c!fksa%d*thFlE<oWkt&#QKk$X{gjL)x#1EpacI9@$Bf>(O=ObK
hIbXuKQGletml<4Xx<S?Q1@x$WEldZLY-G^4sE$VfKS;RVx3%Q%L#HGcXNO@TVJ)rIo-=&D5MJ@HF@oE(d{kI#+;mdo&dH?Zo~&K
W?9l9G>_-@@|G<h8dq(7twVHFlHD$gk5fG0NZN<h6Vfgu>mN1A0b?4lb}5nh*b58yqwlC1Qu_rH+3;VxU2e@_K7TX7NO(8Xb1)|-
Du_V3;l-q?f?S}qH2`x2KHN*gUY*_Luj6JtKUCyrZ~-8_wze2{esheB2^<$$H0r!v)5pdY+73pXGcqFY<|SEe&Ka3UQaG-?b^0DL
Hv!VY_QuB&X)zum_`2-ulsiy-or_-ccWG6r@?qP{Y7<7MRsrd*<@tda3BWXI%Ro*Aqnd{Ze`RlFM^_39VkR=$Q=8*7IrX^r^XOew
z0h|Kf(Q4+{5k)%95Sc5TCmoH!tp@nV#PUD1bzWD_e7yQv{%v;0vU(eiM>E~dwWwbLdA|Pzt|r_#?(R;^@|~_RKXVTV-KqxDPaq6
(%1`gDnFHju>Pp@F_N$qtZd-qR3#$3K?GupIskXes1y=_9Cj=Fkf$MhW<U{se_2#~MyJF;l3s$r(EfGVSR_#XO@d7ttKa>gBxBuC
8vpG|nnYmyxVuGzq9+ET6*=*ClPC7)LWQF^sCMzbgkB4soiAKy<A=Fd6$uxk;m_)d*CoT?`R>9GLkCCmkS=SC(=SIr_LKuk7W8D(
XZx$TO0ohLgeVWIN*X!Zc4r(?pXVgN*T^aZfLqM^6&TH)+SPn}I_gTmY$7$A5mvVSg0T6zQD@I-dKx6HFo$e~S8*7u5vhAhLx<j(
-AR<Sh_^@`xuH11SB0NIMYb4)0h>47=3&7X8*L9Fjk9+MZEx=h4SDnoSB3SwkCUQ7vEk6t*mi7o5NaSwjRsP5<az);acILa(cVRD
Q_+3Vfl|YbO#c12Lu7*hiK&?hwinXRKO@={k$+cf8lLFsu?_LNlyy0-YzXCudL&E#V=)TNWUjI|5^qezhV?gS%fJcWr5lr!^qqaj
0^Z~T_<7m{;{%o|0M6Tl;0*w$7fBR%bSxX<OFWETiNr-M3N`vDSo~SSN%CNeH(u(p5=`Um6LRzj@O%&EiCNClOtKJP*?Te$`&lh_
Mv00Lv&fz=lqiHtNg(mHsZ{h)=HQdoQj@$<#=k?L)BjMhDSRQ8MEm?V6=2lBdgN0`^@C?*W(aCY1AbaWv>s8Q<--xE;Gs;Rpq@{<
#_vGj%^%|FSa8^VCUCj)Ft2mgr+>h1na(Y%6T$K^Q=I#F_s;QS82X@8-591)XCrXX;&lsQ7)L(f06S0>f9BPoAd{kHHCh{0m^r`X
B<@OCbuRpa>&m+?ha<-V$i@?Radq*p<Wc>rQP>>WWebG@aLa0PAXCJuA=4!L5F)lmC-xm2z35#P3(l%De(O{O7@ASoYI)<VnaS5?
(doX!3pU3COwT%t?TsU#F)~wBH>gPk@^Qm?S?7w^GHKT%s1Vq0HF(Yswj?wq<y^0Q%@7fq1rXANt=Z&vF*BLG#MMjYQf&!A3=#Z(
Y53}r9JuxW^EbtgOSPyv?A?O}5v^5sUb`>Pa3w}mPPe47U2HmTW;Iy~uNlQeawi3l)xR0=&!WY*Pw>}7+RODE|LoZdyE=^ou2fpV
SBf}vSN{@ueXZ^W04m{=j9T^3o33TV#c2!w{=9>N)Bq}}1?F$(FW!ipQ0$y>d;~?j^IG;(U_#=mnZfZO1JF+e1l=i~;mC_DG6a^t
P<u&JDo*DobnELzLPlA&;{RNo^+(`s-Y<-6blOh0eh_fPCG-mdA>t`Vrfj7{u6XfCKjC|{Y^T9yh+%{!BvKV`tl)-69wS@|ZVke`
)b5TFkLyiq)laH!o7BP8v=(IdTd9wE1#*;TklX0<7acBVnmfXo-U-Wxf5)3Tl8aE63-D&4xYF&txz!r{iclCf!S)KijW%Becl^G3
^d<UaB5+F7uD@>|T*iH|Q{Q4l-h`-E_YyP8qky<sCO0(_lFL+781zsSR-*Da8vqfvA+Hkb7pAnobofsBX6SD);J-kham@84nTR*<
paZA7Nn0D&&RD1isvq{^)i<dKRhs`hW6VA|;rCrT?KMK@1AgHaNNLVNySms5zx~Ggw8pJxu_fpY{h>T<nNPVW-vCae?X)xZ-JJxo
Ht;VjhZ>)%;In$qI%aIgq*ucE4eH8nSsR1ANn$anL3s-y(<9NO=!M1Nrxue25V4YNJk4A)hRy6ALn|LJWFz!l#PS_;KNV`lGe{j4
sx6EA8P+9baB84kwXWC;Zg$nW=Xpm(gbkazmra{*lgtNOSrGs9+Nh}&s&@RbLNY2sZU%DYw=~aCaia*2HQdIWSOyBj8WA&-bhI+^
JAt=`jARZyj^zDj9{~1DUQ@Za77YU*<V&AV+86bLX=h3(bL7_V<tk*{)oS3|$-VRjnm!Xxa5ZtJlNM=>iaet_o4en$Cr{oJce(>(
Q}zzczPtKgW^4Ei<iS^!O*d(_Uo9&naJ8R4`co=pJTpc#cTxd4payRG>opSp`<_}q0Ddsl8{F)C53n(AN&O%vt)C;q+Q6foS14AE
EBJ9F99Fz^hzDjrgqyzSulHAr`i-+H$$Of2qQoaHnP9GH0rWIAiM?&F9j1to-v_<E_5{h3$mhPe7N-1jK3EF+BivqO*c;0?0ivqB
XIcFLldDxEzAA>heLt;IuI0>LlHa?)UidF79PfaPge~w{{ntj7Y>R$se*AvcVewWQ(uV<cqcX=#NoA;W7!H$&Wsh87jvR1D3zeM9
VS{XuJHxK=*MJ0<)hd8^CC&57F>Le$&)&eej0ls_i~qs3jpkiadLOZh@`tcFY?Q{iz{K<l;^DH#LBOsRr&voAw1zNe9vkKt7nwvU
#5N`7#630W&j9igpXY$53RWf(3^enp?%A%ARL#CX?(r66FRfsv{-&<~4kYa()iP9PMzSe4a_0?SE9A+$8|V^)fXmfpWT{+Ql4Qde
2~7$k9F&ai!QYYql)(1onZ<lP?$iM}YRa5YJ<GrMhk$jzp96qfrteI7Pjb|oc|>4di25&1pm@UsQtocouFS`1eg<)FLS^j!UXPLt
s+U`@e>S@U4Qlea?~8a4dDFt-Tu0XkDVB$DBj*&V*28YfFjNq5DWvwHKekP(A!Yx<YfZ4$99>K!&e+LI0$!$23jpD~AAbEnm0IE6
B>#YAZIZIhrtzSl5nB6uB~!{$*#lDh4}pkVCVXYdK@6T3sFPSSMl>F{76y_Gd{@z9rZwC)nF2J)I4HT39&)3M1WRRr_{8dI@Jq&s
hM+}dl^TI0H=#A;4qwszwtJ%LN_>Drs~_%{<&yYA>jGfFH#4c9Vs8{qAUWUiLLa5YvVlG+lCipfLe-<N#+0%ebSyzkKtXti)J!6a
bX6i~^i5L6;%&ka*37z+EKnvx;KG!L)We^IbqlSP{!_{lhh3c5krC~~A0}tu+CE9T07%R1DFPf$MR=H{o3OTKU1u9s7Q&c*{xTU)
ry(V7Rf!59hvvCHQf}OZ7B?F-xq5l2==_shz-d8eTMjCDCz?H?1o{HG6QLE=UBlnFV?hB$LE@$maVSjwBR<8AGRCFK1_t0Om@_D^
&ynpD=h0?MPIzw$AS2S#StY)NrEf6M+b9HO;Nu{Q(%Y+hbB}7wnRu5K`gRJ%F#5sbEv;h%MRW7wv>OYIKC6WWgxAHhAw$|NP%)Hg
Mt?QRe^wVrxr#=A$@Zdbb)9gFIky!T+B>I3Vvs0xedTxhSTVyV^bYdgZl|=M!2P?f$SDKf3|XxW3xEt_&CmWQggag{VS@=cK&*ic
GSs<hE<roleQKCQXd^DlW!`sSi#W%vLBNMN2>nL;E9WaSBhT<jNFE5SjqP6>7_K49$8Re)LVP3z^#VHetoPkO*ZKeL9sC$5K-+Te
N3p1ugiB3&I0ifoP+kg~gBw<9NLn7rw0M=dg&(=-gTt+F%;mYB23Q*7A$$;jMht+C%|BcR&Ydtl>j_|-SQhfyM2U#R=t@w>javL#
n(qup7FO#XDn1VT52o&Q_BdrX4(=aK8LNW|@nOtwZ~@qpB|B*L?zV}49AHJ9OGJC|XONu&SWG*01QfSO#mmjE@?XYU2k{G^4B%sT
rhxRF8`1`-of(DMjFrRQ2&!ww6+?@r@z-2b@^gOW`&IU+mZ8nRb&E){4)<)}Vbw3h<3sUBgze-k(et4+e>%bgE$sk^nbYa8>Y@JL
{UoJMW`q^XgDzeq&y0ujPRezo9`Z!DV4Ax9lLMyDgJ=P+l-FV$&K`<VZ8sCqNEK=|BL1gNI^SD~#}H|+UN9&tV3kPQUac}a(|I+n
bhEDa)wGT|0U-~VtPe5q=*0%zF=|RzoxRoPs`eBkI9-FWKU0X->zRt#F`5ZQ8fzc-YUjX9wu{bw3Gq;aJEkpV^g+JU8F&!m`c}u%
gzGq#5&F5g1(FdWjM_~H^F<16n!pgJN;eN&=HAZMQz{XRwVA$?@RkWJG<rlPqG?BG0vW39cShUQSQt3%(dR{1BKG@eq1Nd#MosDs
!RZxavBXm*iP&~=Jy+S(c4A~$XC!OYF;Ba`bJi!SBG3T2R;P#Q9dJ^_BN_LM8?p-opH<Jqgx(C+JxoiUrx1`kQ!#y#y*v=3^p78%
E!v@lFpG^(^3Y6EFiILJZVbwa?SE~-w{ZzEudQl`q&4P{V|57=7k$XcipyH0T!C4qIu;esYdmd&NDP*E5Qki>aJ3F}KKLj$h<v+m
tEMs$I4Z&rh83vC3l1mqtQMy9b-&qMxR3K1R$WNGv9Z2&I1s<NFvG5hReBI7YmGZ-5^tD}N@b5^cZZ^3si#N40pORK#}C!3pQged
i!d=TN7bB?t$$i%7+yH^Y8&YjQP8nsd0g6SGA6#kUnRAK6p&kl9jRhRsbY}demAyRHnwY!&+p%1+jHwfm=@1}qv3JFZV)}#ge$oW
y$G4`i-A?4j{fySpxFie1PGAAw?e`@ve9YIMt9PQryd|Q%hh<z#iI@f&r<PyW<_&GZP`K|*Au^D4S0yMV&62X(%w-GZFlt}rQ_LE
xey6MrGVZ<LAM@7N%VQFGr<nx8`HGFe=&<8kS>s+b`2mH8BQk}laqWm4Z0+OOX|~UV(scN$<~ikY!ze@xNffvI6?_RZk49q$h~yb
7>Zt61#Aa8Mf2vY(OX*|$CUshMynhS*)*w@U9`@d+|cregv*TeeZR1gUe)Wl&05!n-~<-#5{GEi!All5P0mN|o@bm~?85jauQ;OW
L6AR&nU8|-j6{2#0b0x-mRtQ*)RGw#+UZtyFcje0Yq*&vRty@c*<k%FttYomtP04vTA84MJ_{l97j+$e$>8<DB6dpY_}z3t*m5O>
2C;ZO<*}++8(X9x4ZNA*J9f!_-uITNOHwJm_Rp_lTbHkWh`36pviKv8@OF!B&lgz1$MRL{zRzb>U#35phuF96%-pzzZmYpeONQnT
>6K0<q*~7CT+QeCD7fqe3s-O&yTJdEL9lJ<=@%C&4|sKPAJm4qt8z^#=po|!JkF?ZkfL`WV)&j^D}9hIl!pOW7V_Bg41cS0y7Wp3
I{9k)g%3+Kj^A`~rR}DqM-5aoCLgO)cz6>r!Vemb+DQ;aJ)sqhkWnJVWrOwCZ>_Lk8u*@{z+tg1K7?sPe|2r8Gx)EwAW2@;Nj5W!
bL!MERF~$1qwRY$IFnxKY$TS33sIWm@HXNB-$?Nyy^O@d8km-KCO*V17XB3+z*<S?O@$^`5_&_pq2nF3K`xwrWC-otf6YbSo1-n;
m65izF6@z#4g;uh%uhX|sSQ!BQ~Lj(FaIEUnz*-t<_q#h43wmJ);!Tw$n#>i3RI`j;g9Scnu}d-pT)~Ak>qz7_2og24$!R0ItI&<
iM+^=m^Az*dYt-_3p{0ujSUB82zkpK!_wMOrU=+7#j!Z0f*7kaBE8Gq`)`FipWU6QKlxJEzole%Ip2@4iX4tSmLf6{)my(%LP-XJ
Z(e?Cmr?+wR0e?%v`EhrQPaeFnL&|&S^xlhC@uEmi1d~F*0Q-7(AX1uyK&pm&$JG$1fH|(>ad7#Hj(8|(|vo;0jWKG?}bYBbV4dK
e_<nes5u$HP-gPrRFF)dI7aCOi5#N)qMCWWt+M;?$rr`B4G54%9~~jaEK_{CZ3IgrQp&G-WSEJ=g{Dvg@fQVpCdD$D#0D7vt&4j$
$S$lsQ&bn1cH5>h)i!Wn(_jQL)d)J43d3pC<0QWs(fZD&tD`16*>~$}T@vkDZ2j(4Q3C0=?%82;?(%Z0%0Y1MapJ$*<8!MYEkS52
NVqNOj%hRZ(Kfi=keDQ%YH(u+;L>nEwqf#to<6sf+AKt5&%Mv181bE8`^U_gUo4A4t7~Jj+5-?uhZ06jEbrTK5pLwRTo-pm2e8ix
x+<~D$fg+NafTjY|9BsO(nm&RnSBs9ELP88E``<ln7KkDBd6%}>)fpex7#@7I-}EATRgj67$6A%3K<%XupL7WpPDp%u|wuS1CGci
G?CAD{84E6cX-O)IU_}|6kL!&+K<%Rp^!p;{Gai)EwDPRBnTlIZ!L{U&+e^)b^_=<mc74({@2)BjiC<~5O8M<RiQuQ)@|#uEvO5v
ihluRI!s2+w)YHY&MO_2`}5eHHmzc|=+^=f2;9VcmL}AyYCE5!Ty)J}S1cc_oJcMFk+t1Kfz$C+^=zqAtxD=7$Kj?9I69#Y{aa5d
BY$R=3q<K8y_*4&uW+=PWnJYmlhsc>!OdbMlXxcOeDiYHsr5$3914b~Z{7!(q;DL;od#mJaEmq}%`fB@qtcPoqt`slq-+bDwqg+O
pY%|IBOMFZW-zL&Hp8Qy{3T`14j@C;1*U&SDd2U4s=`fVl{1>#HY;O`s?Ca_7W8xdxnz^z8VI?_X_VPGGfma2qx<+wmo|^lo;_(H
2=TtcXVt+0-gzVx^F%%=gL8?|<fe^;^RMu~6|=!|4D|hOH!yQHvhe|Fo>?%vvT`}AMrXQsdEc<SNR1Iax0iBTYu24B)eL629t%?o
xARGGh_y9(cb-zlXf5ZPOXbc$qqoZr%csfrmCEA*Z6diuS)lZBgOA?XZ})YIi(vbCOS7D%Q<LQhnDscesCubbyDgc!Fr8EXR$_0;
WFE-3n_a3(tVs=&ygnI`b*lN51H3&ZU&B=hoH)9;R0n}76cvj0P=$M*y%Nb2q=AHqzGp>_OAM-aG(u}7=+nlXf(fH*OA;5Ue8*gv
O4hs#z%rru^|s6b^y(oKY5Ig0rRK&?Ysd7Gjj?v>TT3`*JaJ%TrUW@a=FiKuLeGVuT40})Py1AdcJCQYRu5O$G8LN9r=RB?FDn4Q
0n!*VnKXEwPaOfaa9<?kj)@LY$Q+O(D1^T9+FQ3j0W)O41xRt-oGIo%@0uB~wEw{HL+|O9PRG>@T;S_W(7LwJ@7_fAqc!|E;|TG!
4Y1O;nJDvPcYtiNrC~uTQ);oEz9D(xk7K%*P+xy#ni5kLV}*OLnhG4l?9gYtYWRti$-hp*C*m{xU*j@D1Bg&XVX;)&f)X-&H%W1>
$H9V-rD;SxdkGDr<xog(is{%_{U^#~UqY*#R!<ZAk8kEhucWc+hz+u%sDUXAZK-1h{^)G1s*_OV#OtlDgeOt_9dtvWGQD|AFlhpE
6auK5SJm~)T(f@u1cYny7*E8|HVmdyC}*7B2Sl*Qou6Y&*4gxC!Y3^j4v~6x-I12jIqWEdCd#QvCjfqxVp8g94k68W5#BTYnV)AF
Z@`kEv%7Jm<+EqK&Jur#Y0cz5=TuxvZTURE=>~R1h81iVQw`q2ZTH<G=S9{mwcA@lHkUwD7FCPJ3vOM=`mz&N?j%?A3bkf{+<Zi{
s4Q5qs$vTv`X}(H^+)Yx(&LS{apJm~2(sywgOi?BxZqhHe$Q)G4(58Rq$sDb>gH>jbtSH5yKP#k^_m&dB|ne!X*_-WFTZXa3z?%c
Di_<N^>sf>I4p=&dJ1>o?NU}qv{**?HNe|myhtiQu53M^Mb{E_)3X*6ipx^+II>V9uFqJ1j+y3i6Y|U4AKqF?Tp=$et|OaxQ;HPY
k87UGtY33eTof4-n#MP7MSU5ncL|xEKIE23x0mP`{_%9#W7FvBgJoLHZz{73W1X4=y>sbW3t`4hs0MJfjH<}NdASIt1BhDfq+Fl?
_}}Zy*iJxBj(vxEqo)S<2){H-;Zty~9&@BL)LwGD|8W0p*_GMv8N7gc@D49k_e0q1uYtHRx<6_PCV}U2h1Eh4O;{8_&Im!)sSU#-
T7d6>p@7cMQ3=i}Vhz$JMYx6*D&sINE?=S@IXXsh-}a#*mx&ZjTx=$MtB_<pEr_SC%;cKK{jl5%fmCq~XRa$@_jzpDms2Jg!V56_
VoPmvbc%F=HAG+;yKFBsZ*{l_<$;2_NKV?wxrR+&9JBp*<;mt;=kIG#9Pu&^SXB(s4DanI8$8|Mb#k{e!PJwTGi)i@rSm{R!fO>G
191sHYuUKH1q92S$opj>aI^M>p#&YWnCE%}+&Ciuxh^YvCIZ4dF4FD)@}kFtq@EdqK<9XS$YE8?Ewz1fk6~GA6$0X$=0>p0VF%zB
?OU9>u74~qYvvGEMGi3Ub=6R9olB+mS@LYTI<yS^Cz0`5xS&zAIX>MiYe<klR6Z-92rBLG@-P@`c6<87@mT$+8SEKA(qf8|{&amN
KW4oAIo+`%=9fUO<wZtz8Q|PW3|PC>v98#oGltqtaVZwh&VJ$qj}gle@gRJ=L~mv|*LoKVbN+4h;jU5$v-BntMEmI1{p93{S$fG?
J$yE{Rg>$3YWdb<>CVtV6~23J8+9|`bj*!@pejS<OjJjz(K0m=9K))i+LNyCgwM-Z02O8c-7Y?RElhdjAmpuiv87lf?CuF-ZsYq)
aCwnU!;a3oWJRDsGjZSFEnc9>H3b`}9B!TGe(wy61DhvwXD(pM7MqwiI@w#F`;h>AVIXE?@A?a3{7F_Z)l%VOVl@}4KV+9a{bCEk
HA=6gV%Jx0{L!dbr?{_2awXJ<Xtf7^HeDHP%R~|ZXj-?;4W`W-UNQ2&rNI_725hW8<T5qm&<DF2%<YEX@QESkrYqn;;e<)2Eg&XP
R?iSxI188mYGg?NQ_Hj^RdiR=DQ|SzVJ`>$dOl4B6Ks-{T|y<`A?#rYlB<tcDRMG7phM+knMaMnGuk43RbWsKC<DWbTLb+x3hgVl
gaKYtD*^93R>l%U@2gPU_?qr9JVfOK4J3&k9^v!N;JlmvSJ?}sa+6wp-REN1_4Ak2wmuK3eomDe-<MBgF!fiY=mTlFvUsX+`Q|mN
DrxWn_rostBiE%*GevJVUd~iiz>yYWJ{H-=!~}Lc4;Z3uZxp)7tS?KR3fhiElV?)TYAGOqsCZqdeVVV|O(eq)iEj*<XJ3F;{YI(t
pD`0T_;S^B0Nq%JFmFKqU@HRDH4gN1fl$HDX3qRVsXE{eLDyuG(^1^ktcDC(?G`NjGbaav^}lteYqzptFi<I}Zu{+};8<~eRDO*(
c+28xg`9`iv46=p+W&^xH5h7rlreIgT^mK=0JPb?TVRYHbMf+jQko}_CbB#B>+^0wUO1*$jP5U;N(L3``?2IabHL9Bkr{tGk7_5P
_oe{t9GqR)J(ndUvUd29S?n8G`&<h=_Z~eN%S6w9Y6WQ(E8GI(UvY~YHB25a^Zh%ge|bO#w627s%UIw7?DtKCc&_*n6~ICYx-17+
AE9NY?$Q)?EJivt`;b0}xF4#<<AlzSBDtqv<!cMb7mI%dRNy%4CDY_5`x(u+Mr2fNo5XQn%$Ik0fMd6UWGAwUJ(`kyMGcvPyuIuy
P0iDAY}J_6?_Mj1GiB6hbj5Ww;m3kYHYFBa>=GkI2l2|f#8eR+-)e{i!(O#FOZ2e*6@=w6pcb7r-0pCrjIT|u@!EqXxjWflAQz8N
kNibiR}tPf!S~4`p|p7)sl_sZTKy!QUi~)$Adsc7<66K$K*3R@tPqcP`{!GFTID<<t6{~NhJOHgg*0Cr2~WE7&A`0YGr4|bh{gJI
ZINwhI2rIZ-fl18H#}WZDnkS7>Uz?O^S#Tn@o-H88|1HKFFm*#x-7g~D!c&N%`6yUk3Ifqj5mOL;+8z?cZwqTnLJ1%zDdw6i{NbR
ZQQ;5u#!@-FNOoRTEaF8mK0I&uJ=|Poh<hXz0~-V`c(tjVW&GVawle9gi%Q!SJYsipNVlk?5r4p=pAE&wLPr%8Tf*>c>7sPHeClY
-lWO~!8ymH9^*`y?lUvlXY-8k*UuVVvH|Vz$Wp-3`lkUaJbMP66OcAa59Kj+>hv?EISeTSm6|oIJyD&R*qRMYKRx{wOj-;zF3krD
cTwy2C)J9ZS-TZ9QGB7)>ZV?;)RG{Tt|B2tBScQ!>KWXkO%Xiu&Lf4EtCPf`CU6NMJbKGChAc6Tu1u^xA`?|5U0Ni!JAIim(X*V{
QE{1p{8V{_=jqat`v?G)Kevt>$PF9mEEn3yI*{GOZM~prDVs`jp!+irAl!jY4i>L0NAR)?+;x<Tqhb7jiO@o^6Qg?y*jJ=l4Y;w-
8bo6%>;9&UVlTzTMf^3W^v)@B!vO{nw0*i`!+HUAgAd(&8*M_Si3kyP8{oqPq{FphgNM-62QD#U31Pz)htf;`-)}l8*#<ofBK|H;
GwUYDR)DL6#DKfoSuQHuQIUTiEK(veuoGbSSgEM_{>szc`4CJk_{iY??~eKS_mb-qI7R-?h#{4KVx$O-o<iuFj0V$51zdrHNZ-xs
A3QRax&?v|W&KIuy8pidjUO&iw{^!~^CuO_4=KFtQ<G}+*JiELcE7&DnrjtXzF39uP9BY{->he+yw<Q@F2i`NSRI~P)k}uqvozmS
1a$>)Ph4^>sW3^yeN0pVhQZv(KkZS3`Hh?a@`)dLsC_=IXga#Flq~lXosZDZYI<0i$P#5V0dahTxl1+Hrf{iBDCG5%oNyZ03g;cf
Q=y^7J<GB1lfTCPwCPe9*M(xCx$*Aaw)<lsTzBNSmxgzD;b!mP0690>5%`<bQd#$vtC$u+C%5)KUE5J;PhG&<l)T2(U4oLsgYhR9
Oi~jKHNr%ph$5%(yz26-3Q@SP<$lf6`5xslc?Ruod7A+PL5g`xyNGUSZh<khZJa^ddtlXkFaEYpT77z>drl}$eQC+%HeHQdiEN&e
@-1+={qNg^H>d;Cn%{wh-9nb2oR`yQPBu!0T{6hVQ`&9$j|GF>g=1;XGC;M8znETA^|-zfO=x=9E*ZseeBGcgOZ<Qr?C0KSdCbqH
7rb7X?N$yp(rHXQLLA2nI|__`qAzCsEnnGb#m!Z%^F1vkyGfil?FTn72|xk52E|8iKJa-v3b6^npQt;*{*%`O?8N2m7qRx7m`V{}
r50B-HJk451x5!~%Y1s=P0Uo-T}<G~G22P5#9XnW^xaF_kuWIYm#%@TuH$jiO8AEK(g+BsR{FCsn00#KAt-xo9$<Nsl*~<eIBJ^Z
AlNN92TRe@!LnA!X{3A~yUOh(X2jnR3eqiatP3Pu9~|GL?a^Re!olMQhu_}tB!H)#UEr$hB#`&&$ts9GZhkaDXp`<3OfU)BrQPnx
CHP~}!RP6yWK=qw0S$X!bgh&Ul@Chj()&y9^b&MOm`a&z0rw;_*ZID#rHpU{4zc38JQ#FVieI%~SaXuM3COh-ITA2JpAVByLGxbi
5rrvi^c0#bq>H{c$?U_BMMEhn53qCR)NAVd{Q_XsG2(yOuJMcx@2cMv2-*6Y+$#3Rr7Z|geVbgYf|f~RSI}9r`R49W%_oYR|4u=V
V)^`h*Yox)kL|ITxFsq?sl$7)D?&t`5}tf{__gwqVu$}|5En7Z%|xU!SvRd2oRf@9{-&B$ZHD~Dy@wH8z~5<@8LCCqYmzDqx!q>a
COGM?lLUbw(!6=r1({d_{*RkCJfg>I-|U(>f3tJQc<~V+OP+tJ88%HI*h&Y@NT4dLVYKr6;bI!*TG4}NIX<N%4hB_!t<q&in^CX&
f7yc?wa3m9F-T7}X#c~zue#5c@%T-Z!Jd!|_Tu(0y!VyG=CQd8Uy3ZET<x-wI)|HuOM80Ek-5$!nZY#~F$9ReZy!*x^??<;*oZp}
2{aEVq$=bIZBmIH2xf?9?C(b4J;^KoM#U=%2j}W#j;z(nko5UAqCZa{Zi4}cL#UJi8=YL5OOht)0&sSyLJ4<0k;SEtGX~NuT6@*?
KL_1BKX`RjbqZUf0+A6Dj7wSngl)7c+ZE3VZS@%*p>~F447%WEy7jEkD$0$YigK-LXMNBIyR>@ov1yU_);asm*dm{cA&}1y#&W~e
>`^lH@cWMYuN8`uG%{S5pWC7~^EAbW`Tl_(F~BcgcSoN<nunWwldK^v3LI@i|4$ZoJu7o13BBH*)s}8OqoHnbt}e>3(=ogN)TLER
$qxrQMAuQ69W;RP7f_#Lk(BnkoCmF|QZglMV&35)MhZa6vz{9-2)TdAc|gk~RZXpbxzX^P;Gh6lLy)0E<k&<OTHkkO$st<QqQJTN
HTN2&;oLJqoQoU}A|Dt<imIj8*C(!#IsMh#TcI!I4Fx=Hr-q_k`wZq!7m?1Pq5R&B^d38<qN@uXKu1P}UB38S$_b6<m;>)OJ*+R=
T@w`wNr(lg+^G^|)Qxz!-C=8PCm`>R4Nd-!IugIAc`+yo{?y4e_xlK_JD;1RU%`Omfgv_P6`FL9g?P+JRB{B407f#nP#x{(`BJ4~
h2X6CuvYa0zvSXjiL-opn>K6zO(N1#OVI~Sgbk#wlK`MeQ1>+#!%D{K+fU#;=gv;1%>~<mjzUESO8EIPyv|&bMx*NcDNZhmF?xdP
>^Mf7CQFvkUplj6(A-}#SIv)|iZnsfp)<z|x()c7aI&^5Yc^{M)v>QYe+CE?^CIdAJ*D9626n7nndsoto-Rzwpd#T_-I+PPNAd7C
RB`-XsHB-hQQ<~<_#}N@5{(pFzYYj*_oi4NYQbbO<o1=SxRhgXo@IaV$#G^Xv)Fv$GHIzJIjt4xfm_nL0LK!9wUZCJ&fhSYmq70)
)R@E3zlgUor?TQtvU&$-&NU3G7D*t8<^yysD#q2R&S~Z7nC}v588Up|ZMm!I-f+_No@?;+UB~gKDC7*p!#2ak7(EpS_9?ds8OTiF
2A`rToBW}f)K+>zu-yyOTrrJS@5%0CKNfsR4gSbb5o$b;5z^qQ({l}TgZ3FayQi+{`^nW=xw==SL87tak53lXQ>xL{_7bYuHDMrp
bC2$Fx5{vhoIz^{2(w^DKG5G_AE*xRi~apD^vB&}v4(HyP8@tq+Q6p<c)Bv_YdY6L6!es>NHTDm!7tS_X79OUJTY5}t(E9jyG1pI
4sHpMv`{2bHPAG^!@6-8=T^0GlqZ2xJ(MxfHRhr`!QF7M+k$hT-b<U!^Z)<=jemQ}g>UWT00G-n@zMhTWs=41vBYQl0ssI200dcD
"""
raw=lzma.decompress(base64.b85decode(''.join(DATA.split())))
assert pin(raw)==PACK_PIN
pack=json.loads(raw);assert set(pack)==set(MANIFEST)
for n,v in pack.items():
 assert Path(n).name==n
 b=v.encode();assert pin(b)==MANIFEST[n]
 if Path(n).exists():assert Path(n).read_bytes()==b
 Path(n).write_bytes(b)
subprocess.run([sys.executable,'-S','c34_709_balanced_tradeoff.py','check'],check=True)
assert pin(Path('c34_709_balanced_tradeoff.json').read_bytes())==[118508, '5d1b48f2a08e6470a1102a8298bfdf905412eec135249d6f62d576c7489d8ab4']
print('C34_709_BALANCED_TRADEOFF_COMPLETE_RECOVERY_PASS')
```


# Preserved span 395 (literal-source)

```python
"""All surviving direct-tree choices at every joint root of the C34 catalogue.
Combinatorial necessary cover only. No geometric realizability assertion.
python -S c34_joint41_support_sets.py
"""
from pathlib import Path
from collections import Counter
import json
import c34_joint48_filter as h
assert __debug__
PINS={'c34_joint48_filter.py':[6928,'058a5573ffe5a35256c252ea7778f3d0828660cdd74666be3381848134c9a7aa'],'c34_catalogue.json':[1111066,'1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77']}
for n,w in PINS.items():assert h.pin(Path(n).read_bytes())==w,n
allowed=tuple(t for t in h.REMAIN if t not in (671,672,673,674,675,701,709));assert len(allowed)==41
bits={t:1<<i for i,t in enumerate(allowed)}
maps=json.loads(Path('c34_catalogue.json').read_bytes())['slices'][1]['maps'];assert len(maps)==633
rows=[];hist=Counter();signatures=Counter()
for r in maps:
 fs=r['facets'];edges=r['edges'];sets=list(map(set,fs));owners={}
 for f,cyc in enumerate(fs):
  for u,v in zip(cyc,cyc[1:]+cyc[:1]):owners.setdefault(tuple(sorted((u,v))),[]).append(f)
 dual=[tuple(sorted(owners[tuple(e)])) for e in edges];ix={e:k for k,e in enumerate(dual)};adj=[[] for _ in range(9)]
 assert len(set(dual))==17
 for u,v in dual:adj[u].append(v);adj[v].append(u)
 for a in adj:a.sort()
 incident=[tuple(f for f,s in enumerate(sets) if u in s) for u in range(10)]
 cache={};support={}
 for f in range(9):
  for t,p in h.TREES.items():
   seen=set()
   for order,mask in h.placements(adj,p,f,ix):
    if mask in seen:continue
    seen.add(mask)
    if mask not in cache:cache[mask]=h.complement(edges,mask)
    tadj,codes=cache[mask]
    if any(all(w==v or w in tadj[v] for w in fs[f]) for v in fs[f]):continue
    chosen={e for k,e in enumerate(dual) if mask>>k&1}
    for u,code in enumerate(codes):
     if code not in bits:continue
     if any(all(b==a or tuple(sorted((a,b))) in chosen for b in incident[u]) for a in incident[u]):continue
     support[u,f]=support.get((u,f),0)|bits[code]
 reps=[tuple(x) for x in r['joint_root_representatives']]
 for u,f in reps:
  mask=support.get((u,f),0);assert mask>0
  rows.append([r['id'],u,f,mask]);hist[mask.bit_count()]+=1;signatures[mask]+=1
 if r['id']%100==0:print('SUPPORT_MAP',r['id'],len(rows),flush=True)
assert len(rows)==52635
smallest=min(hist)
minimal=[]
for mask in sorted(signatures,key=lambda x:(x.bit_count(),x)):
 if not any(m&mask==m for m in minimal):minimal.append(mask)
def labels(mask):return [t for t in allowed if mask&bits[t]]
minrows=[dict(map=m,U=u,S=f,trees=labels(mask)) for m,u,f,mask in rows if mask.bit_count()==smallest]
out=h.serial(dict(identity='C34_JOINT41_ALL_DIRECT_TREE_SUPPORT_SETS_V1',inputs=PINS,allowed=allowed,rows=rows,cardinality_histogram=dict(sorted(hist.items())),distinct_support_sets=len(signatures),minimum_support_size=smallest,smallest_support_roots=minrows,inclusion_minimal_support_sets=[dict(trees=labels(m),exact_frequency=signatures[m]) for m in minimal],feasibility_claimed=False))
Path('c34_joint41_support_sets.json').write_bytes(out)
print('C34_JOINT41_ALL52635_SUPPORT_SETS_EXACT_PASS',dict(sorted(hist.items())),flush=True)
print('DISTINCT',len(signatures),'MINIMAL',len(minimal),'MINIMUM',smallest)
print('MINIMAL_SETS',[labels(m) for m in minimal])
print('SOURCE',*h.pin(Path(__file__).read_bytes()));print('OUTPUT',*h.pin(out))
```


# Preserved span 396 (literal-source)

```python
"""Build full pole-shadow frames in the three two-choice joint root domains.
The support-set theorem and catalogue fix the exact root identities.
"""
from pathlib import Path
import json,subprocess,sys
import c34_joint48_filter as h
assert __debug__
raw=Path('c34_674_frontier.py').read_bytes()
assert h.pin(raw)==[5046,'0dd9880d4588c5fcf276c181cd29df2616b7ee03d639e26fe7c70e6ff1f6d04c']
support=Path('c34_joint41_support_sets.json').read_bytes()
assert h.pin(support)==[1145761,'6445ee3eaa496d47c87cfb745f07e101d3e0dba25b1f80360ecf1a452846abe5']
scopes={410:{542:(9,7)},585:{542:(9,7)},608:{379:(1,0),391:(5,5)},677:{379:(1,0),391:(5,5)}}
summary=[]
for tid,scope in scopes.items():
 code=next(c for c,i in h.INDEX.items() if i==tid);p=h.parent_tuple(code)
 s=raw.decode()
 def replace(a,b):
  global s
  assert s.count(a)==1,(a,s.count(a));s=s.replace(a,b)
 replace('P=(0,0,1,2,3,4,5,5,5,4)','P='+repr(p))
 replace('==674','=='+str(tid))
 replace('  M=Map(10,r[\'facets\']);Q=Map(9,M.dual)','  if r[\'id\'] not in '+repr(scope)+':continue\n  expected_root,expected_stable='+repr(scope)+'[r[\'id\']]\n  M=Map(10,r[\'facets\']);Q=Map(9,M.dual)')
 replace('  for pi in embeddings(M.adj,P):','  for pi in embeddings(M.adj,P):\n   if pi[0]!=expected_root:continue')
 replace('   for stable in range(9):','   for stable in (expected_stable,):')
 replace(" assert len(domains)==167 and Counter(d['facet_tree'] for d in domains)=={253:14,266:77,272:62,278:14}"," assert domains and all((d['root'],d['stable'])=="+repr(scope)+"[d['map']] for d in domains)")
 s=s.replace('TREE674','THIN_ROOT_TREE'+str(tid)).replace('c34_674_frontier.json','c34_thin_'+str(tid)+'_frontier.json').replace('ALL_167_DOMAINS','ALL_SCOPED_DOMAINS')
 name='c34_thin_'+str(tid)+'_frontier.py';Path(name).write_text(s)
 subprocess.run([sys.executable,'-S',name],check=True)
 f=Path(name.replace('.py','.json'));d=json.loads(f.read_bytes())
 summary.append(dict(tree=tid,parent=p,scope=scope,domains=len(d['domains']),retained=len(d['retained_domains']),counts=d['counts'],source_pin=h.pin(Path(name).read_bytes()),frontier_pin=h.pin(f.read_bytes())))
out=h.serial(dict(identity='C34_THREE_THIN_JOINT_ROOT_FRONTIERS_V1',records=summary,physical_exclusion_claimed=False))
Path('c34_thin_root_frontiers.json').write_bytes(out)
print('C34_THREE_THIN_JOINT_ROOT_FULL_FRONTIERS_PASS',out.decode())
```


# Preserved span 397 (literal-source)

```python
"""Frozen-incidence moment probes for exactly three two-choice joint roots.
python probe_c34_thin_roots.py prepare|run
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
os.environ['OPENBLAS_CORETYPE']='SkylakeX'
from pathlib import Path
import sys,json,importlib.util,subprocess,concurrent.futures
import c34_joint48_filter as h
assert __debug__
assert h.pin(Path('c34_701_probe.py').read_bytes())==[3898,'bbbfa5a4594e13f72afb9868c2b8acd56bd8dc45787e39620eebfa7a043b8773']
assert h.pin(Path('c34_701_exact_check.py').read_bytes())==[6347,'6664fddb3ca52621df15d298a16099543d5e596b525617a56507da157bfcd81b']
front=json.loads(Path('c34_thin_root_frontiers.json').read_bytes());jobs=[]
for r in front['records']:
 tid=r['tree'];prefix='c34_thin_'+str(tid);F=prefix+'_frontier.json';assert h.pin(Path(F).read_bytes())==r['frontier_pin']
 oldpin="[2246318,'bf3512f2fdbe7fd0e378499fb83a978afbe89183f2db3df06833984e1c68014c']"
 for kind in ('probe','exact_check'):
  s=Path('c34_701_'+kind+'.py').read_text();assert s.count(oldpin)==1;s=s.replace(oldpin,repr(r['frontier_pin']))
  if kind=='probe':
   a='gs=groups();assert len(gs)==1265 and sum(map(len,gs))==1917';assert s.count(a)==1
   s=s.replace(a,'gs=groups();assert sum(map(len,gs))=='+str(r['domains']))
  else:
   s=s.replace('P=(0,0,1,2,3,4,5,6,5,5)','P='+repr(tuple(r['parent'])))
   s=s.replace('len(domains)==1917','len(domains)=='+str(r['domains'])).replace('range(1917)','range('+str(r['domains'])+')')
  s=s.replace('c34_701',prefix).replace('C34_701','C34_THIN_'+str(tid)).replace('TREE701','THIN_TREE'+str(tid)).replace('coupled701','coupled_thin_'+str(tid))
  Path(prefix+'_'+kind+'.py').write_text(s)
 spec=importlib.util.spec_from_file_location(prefix+'_probe',prefix+'_probe.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 gs=mod.groups();reps=[g[0] for g in gs];jobs.extend((tid,i) for i in reps)
 print('THIN_GROUPS',tid,len(gs),r['domains'],flush=True)
assert sys.argv[1] in ('prepare','run')
if sys.argv[1]=='run':
 assert sys.version_info[:3]==(3,12,14)
 import numpy,scipy,scipy.linalg,threadpoolctl
 assert (numpy.__version__,scipy.__version__,threadpoolctl.__version__)==('2.3.5','1.17.0','3.6.0')
 pools=[p for p in threadpoolctl.threadpool_info() if p['internal_api']=='openblas']
 assert pools and all(p['version']=='0.3.30' and p['architecture']=='SkylakeX' and p['num_threads']==1 for p in pools)
 def run(job):
  tid,i=job;tag='c34_thin_'+str(tid)
  with open(tag+'_probe_'+str(i)+'.log','w') as f:subprocess.run([sys.executable,tag+'_probe.py','0,1,3,5,7,9',str(i),'0','12'],stdout=f,stderr=subprocess.STDOUT,check=True)
  r=json.loads(Path(tag+'_d'+str(i)+'_a013579_m0.json').read_bytes());print('THIN_DONE',tid,i,r['status'],flush=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:list(ex.map(run,jobs))
 print('C34_THIN_ROOT_COMPLETE_PROBES_FINISHED',len(jobs),flush=True)
```


# Preserved span 398 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 399 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 400 (literal-source)

```python
"""Complete immutable recovery; CPython3.12.14 standard library, assertions enabled."""
from pathlib import Path
import json,hashlib,lzma,base64,subprocess,sys
assert __debug__
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
INPUTS={'c34_joint48_filter.py': [6928, '058a5573ffe5a35256c252ea7778f3d0828660cdd74666be3381848134c9a7aa'], 'c34_catalogue.json': [1111066, '1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77'], 'c34_joint41_support_sets.json': [1145761, '6445ee3eaa496d47c87cfb745f07e101d3e0dba25b1f80360ecf1a452846abe5'], 'c34_thin_root_exclusions.json': [1141280, 'd7630fbb533bebffc4a73a3d7911f36218f5dcac7c3a911398f82efd446e18ae']}
MANIFEST={'c34_674_frontier.py': [5046, '0dd9880d4588c5fcf276c181cd29df2616b7ee03d639e26fe7c70e6ff1f6d04c'], 'c34_675_fullframes.py': [7371, '4a37af5114c03b3394ad0698049223c07d2baa6b63a19d046151d3a9916538dd'], 'c34_701_exact_check.py': [6347, '6664fddb3ca52621df15d298a16099543d5e596b525617a56507da157bfcd81b'], 'c34_701_probe.py': [3898, 'bbbfa5a4594e13f72afb9868c2b8acd56bd8dc45787e39620eebfa7a043b8773'], 'c34_root592_608_certificates.json': [10459, '91e278965b938d3c16f0208646dd226d50c6866f3a87f1d978cedb9fd8177d3e'], 'c34_root592_608_exact_check.py': [6409, '3b656af313b8ef2a6b0ad41b2f07f15e64c7e4905c32c9a72df4376d128fa2ba'], 'c34_root592_608_exact_report.json': [938, '20e19144a0a2727bd7e5f434a052c5f91f4841680e4d78bcf4257b9ec914ed64'], 'c34_root592_608_frontier.json': [1105, '41c99c2becf8b5edfd162d30778b788b57c597a93e575b8b5d7cc1cda89c1f54'], 'c34_root592_608_frontier.py': [5228, '6d5ecc74a1f6031016d2221d605bf95e890cb97d00a4e03a08d52399caaf7a47'], 'c34_root592_608_probe.py': [3926, '176f39f2b0b05b968816bdf0c8e43239d7c1864111f51592c6502cdcb6bc61ef'], 'c34_root592_627_certificates.json': [5593, 'bcb813b6e72ed04ad755a22add52477a2e3c116c3de88d2c4a12aa57015f8d71'], 'c34_root592_627_exact_check.py': [6409, 'dd58cea8123316ea9139de3ae9016581d8384f73e7dd5d5c3654795601a1c1a6'], 'c34_root592_627_exact_report.json': [599, '22b773c2860de9a6061f01ae11a6d8693bdcf440e694af513be4a6b6b30c50e1'], 'c34_root592_627_frontier.json': [1707, '7cb3e4c47bb6cf096f80596a400e996672abfe22953f9fc3985d696f55c6a29b'], 'c34_root592_627_frontier.py': [5228, 'fd175ef2009e8c5331736d2967ff7498b99cbdc0b34b02313b256115c0b40f81'], 'c34_root592_627_probe.py': [3926, '161aec772390857b106e24f9bf6aced492563f3644202d6f3a3b22e7b72ee843'], 'c34_root592_651_certificates.json': [5954, 'af666a2faf6e9a45f7af980a23feadc31492d284e0ac6fe748c5b75e737736bf'], 'c34_root592_651_exact_check.py': [6409, '14b8b05059e4abfe08611c8162a4934c25421891190a72cbf5b7b6cde6c125ce'], 'c34_root592_651_exact_report.json': [600, 'df7e381e33f79163f428b617788aa82bbcc9529c426ac689498eb076138431fe'], 'c34_root592_651_frontier.json': [1870, 'c0689eb52332346f34b1006828c663a4fcd7a1532f30ee5bfc81efaaed44b109'], 'c34_root592_651_frontier.py': [5228, 'b4da2331d69aa654b432cef8961626c6d324ccfa3cdf3312921c635a1e49c122'], 'c34_root592_651_probe.py': [3926, '34d9c0230ca5534ca0aa54aa34a93b15f8d31eaaa4b111469d318157cf88d044'], 'c34_root592_finalize.py': [2162, '777275b16dd3544c5c1bda9f87666dc4133e41267c2ed43ee956606a6edf8a99'], 'c34_root592_root_discovery.json': [1176, '94d2a26fb99a58ad78b21e58239213cdb86493994c7a570922847a1d3368bb72'], 'c34_root592_root_frontiers.json': [998, '28a79e26723fbed71204c0ea3eecba95aef3012aaba71edd67dff7610ae911d5'], 'freeze_c34_root592.py': [573, '6d365c691db629ac7b015f6890a9d9b13928914999df3bd8f7843ec4b6c3c649'], 'freeze_c34_thin_roots.py': [2630, '4ca7d9473baa11627a06dafa3f3010da23b69053b0a8a4066626eaa0af08cc3c'], 'prepare_c34_root592.py': [972, 'bf24e3aff2f46afeb528b5b05677feee1e0056e73b545365d998e485ce9d14ef'], 'prepare_c34_thin_roots.py': [2360, 'bdece045b95615584a6a0e3023cc1604bfecfa17088b3ceae29254efd28f51ee'], 'probe_c34_root592.py': [515, 'fba5d00a7ffa0e6dd297c815be2fd76adc4a84b876793f994d830a767119a8d8'], 'probe_c34_thin_roots.py': [2958, '4f801eba17623ea18c4ae436122174c21b5f817c592e0bd2f5eb5d904eccbc14'], 'ten_successor/work/continue10_cells/coupled.py': [5991, 'f5973659810ea240367024f7a46c48f18b82e8866df86a7eba34a809157cf7f1'], 'ten_successor/work/universal10_engine/engine.py': [5104, 'a254810e332f31e5cdae6e88dc05a84c6c9718f2903ef84f6a900668d1b8f226'], 'ten_successor/work/universal10_engine/fast.py': [2737, '3a54df86eca10711bcddd96099ec8eab9b71a7d4aa0f1a1aadeed6db1fe36f5c']}
PACK_PIN=[130263, 'be0457f37ea4b0cad04976745d511e59fb877396e418bac810ecdb203addc1c9']
OUTPUTS={'c34_three_root_exclusions.json': [1141359, 'ab735ac6bde52778b3c8f01047720086b181accc1cc0f462e9286b89b0c82111']}
COMMANDS=[['prepare_c34_root592.py'], ['c34_root592_608_exact_check.py'], ['c34_root592_627_exact_check.py'], ['c34_root592_651_exact_check.py'], ['c34_root592_finalize.py']]
for n,w in INPUTS.items():assert pin(Path(n).read_bytes())==w,n
DATA="""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;r!NNRb2o*h=^ll$&q0rE;w#?-Ap!&Ow$i&;XTv**rm3=)sJ1AMPMmhN$yhcWW)3VJaoAc
!u}MUQ>JW$(``Mwd45m^bIK7FfsA=^A3a&pJC*hU!>lVQ^LU+w&H>gA{*$7LE6tfkrM%J+gNTiE#4ACmFjtyR--_C%x;v7kjS3UX
53e3@Ilk0m83!FNF4cvG<GuE@Hk#_ldzyqjQOC9{-yO-#p3ROFv>w?#piAimYbPW_-Z)PN?aXz06{?;9ARRcl@+fh`bhkz9E72B{
Unt7rb!nt}wrJyEW))=2KVr^h&#yg&{UfkrsI9}_E{<bEKouDV^(}+PE_r01t-abyLnf&+fitrw^rJ8I#rD{Ht^yA2+UIR0<lE{N
Eh$?tE#}|j6qu|A56n|Vm`Gq@h*;#P#F|5WcOf-BK7P@^AGG5iI8+Xk2O(J7D~x|+&lxIH;FRFc^kTTIi(gV95pfHlccxra-BgV(
d~pxp4aADc;QJMhUFB{-nudpK+_aOgzPEAGIbo^;Vy48fvg>QvR8#}j!;Ml3H%#O&nvG}~{}=9^PS4Kn80H#z#Bf<?uRU~2{t5!*
?=B3M6L_t?C{qfd?)fIjH1q=Bn#r!zv>=ag*ZbL;;Eq4sTaRH<J);12^i@$AX*Xz5g5|jb`lSjUKt*$RQ<OKj)&!09elgzKrKbwi
N=|X!MYV``StvGp&N`u8br8%nhJbqjiBn@5*8ic~2xXFIIv^E9+|sv<STRzSeVHu`6MV7p8I8B162}rSZMXPJ-(?Shb8?;$5*A}9
$-mrX&AYgK`bHmOciIMJS-qaXSMo2H;XcQEV5BpULpcx_nww^BX5j@ife?*5vX_c@(P2D$Dd$-uj2Nw6Y7L$CH+<U9m}at>@rTYe
>$ay3u~u=eZbcG`=((p`5HSY?yW_KWzUtsgO%m048=P`I1yM%ypWf`K&L;jG)b3m+F*ziYX6uh-KMg(bvTd?(vkh5y52Cs7$yS1%
S=F)$7?$SVoPAfp6^A0YRcsfBI0z^Rx|Y&paqbdJ>-W7r8vw1qMEAGx9e_-4Ag-UIvK{#kE<Q?WDQ;DE6roq3eb{YmA=q;!p;2@W
_mP+5)N>(+v|;pFx32f%v>PRaj{BPmB?h2?bgiwY+?k1!iDqLAn_Ic%<&c_p(fF#;?=Fl<+YkxjE4|EU$8|<H7uMxj0IPKu5X7~S
%Xlc^q~*Vd96Q5FQ|@JdHwY$6O%_==md(t*H<+Qu+5H<Qj=nfD#J-b4-+pvDOt)jbA4T%Rq}_+t4!j<YLYX;z;%^+o8Abk&HG|WV
wQ1B&B?%0MibfA=3%{<Elrt+Q3SP%1juMrAi8QI1ovD#FQ+x92qkc!~*lZ=17zreUH-O)YtkyKx^^^)at^CHdI=s0lz7(97x9tKl
&;s(n`|dU`sB)Of`{x%h_nRY=l?bP~f4tF_P%hs*($+|29W(WE&{D@mdZtCa3O~i|D0=Tlq;dWcIWEP}E?AhCJS`<>-}P2cUs;CO
GUxnF#dS!IlJ@l?kwrQ<nW175-&V;9808%X?QEb>!5|WL<;CQ!&!Drnoc-C!M<ZPa4W3FXsMcNrEdAk3Bhd2?(T6S-p$5R$MV7#9
rKabT^-;#7kAF;*tS2hYTax^FlQN+N*8`5RbHyP#R|zF^iU2e|&`?)Oa*!U9*xgHbB9_W?t)iomT8E7GD-~-_M%RRaY-UjzhqCM5
4R;GgGny;TXE1XoSCvKyX+Cx=At~tXO5wIKX^Zvdt8;nQr)tv>hO|q=23|T)aVcag79MWn);0c6MGw(2p|8vWKB-q5So2Q(S(*q{
EM%|7gnINO!fF&zRhI8k`tSxDR+R1_OQJ{WgWx19wN#@3Q=;FXc>iehK!9WjB$&^8J5My4&>fkZyWWz$ODW|mqb0agU^glG=w&{r
7}t{GFm~%3RV$HC{|Ib9jUqh;Lh3*Gmhtpm+6b%4##!*j!qynu0A)FAZDDo0O~>=R1b1~)coB&G+FvnDiZP?A(0cRbEWM#Yu?z~(
jH&$;8;6;NW7eQ;&lf6Q+5Pb|o8n(BAR!LWQ80({tMsg?M_C7QCpoqaX8^GRHq3&87jo7HXK5jp(w(0~`ZO)xnDT3>3D^!!5WQSQ
R3GnxVjr2qWz?qsh8SUYOjhiUBBOu;jBCKKl*JH?lX(<`j)bQ4wuAQ^9#?kEOGUOAgp{#6qtop#^_q(kRfgDeyamDc(F+URP&?R)
<gbCQRT8XjyUnoH7jJrGK~qvzNuNY$D9*5tQ>ONRpmzdP+jef2aqdBm8YsGkS#)tIp~sAqoULS)nc=?-q)jm{3YWABX9H81Y$0ax
cu)}ILe=$?lktGFb-+WXl?wf*BtiySGrfH7h%`->qk_ANld#^L0X&v0ps3ztY?iu(E8S0UkYf&Ax1@aZ)CxZA3a<{|CmmRtyQir)
{3h^1^a#=XKkG79UsaK}GUq3Gl(wub{(4gbM9FDxt321nbn3}m$1s<&9|&_RxctXXd@v?O;}c^>kpg1BB7CTyIo(l@m^d+fIaLg5
Q%Kjz2=;QXpy+J`Vu4)x1zv;~%M;)Kj90vuo6!O@2sPLUkTI@Si3Z|M%YIWHhyI&#A?`A+k5%I<Mz1fArez*0$TZg6KminOJ?R!@
cO_1?gnArkCKVu7FUKgeLJMrwMyUY)<cQ-nzG<f%Cm)$3v!D|l2oG2+;ib)C-}}F27C0(&6WfOB*Dhsd^w&Uqi7f9JZpuj3NWyY3
mZj&HN%C%-I?rP5IOAU)VqKh7v+eu&W`wv#fWi9HR{E}kU%Qd~ZQUCd6O?TXl+A~Op#GDxuAIzMH&t?Z*LnaTGXlh#3-F?}k3S~R
)Td@Tev5`5xCa&Z8Y;OtF!j=BBMIlkRuf!96wB;1Og)y_`TgFr*Iqmpkgt#8hI!<R1ME{mG+grFDYhJvwKXW5+!?GSrqM2-tLSHG
mUHoybLROX4ugv}X1DxPHIzO>?Hmp%QG7>Fyyt&VG*fL+5h%^u?fgcZPYCwuOC*{2P^<&e9Ab5$l5@KdweVa=5C^W&Dgp8HA)C+z
U1-@2R|r|dN+R7M>MLAwVn}<nF$OBjREOHYC@hmH1+bCU+6dSdD>^t1NcO(W5?C&ecq*=JTul|bz}7wso=1wc?)c1()|mwC7^iO5
OP7Ncju6oYK}JwI$w@1t$Eufw8Z7p$M6R%ReWIE=<U;C&$6D17ApfcoxadB4)<w8C4{NPfXUM>meGzZ?5Gd2v4%n2qY__gW-a(B^
1N+2s`*od51+6lwlDS>vnMX8^tyL*>#y1z+hr8R2{5_zZW#gC{V|g-9)*-^@ZUycB3=R?pW98QWzN`Y&@`H1Dc0>EZqDR^>f2Ch%
+KjQuLz2;Bd+5Oi@Pk4qW><C-6N`CT$hJSweZmOEM7i&bZxG{c>`BFY92KMVuv9$T)b`0@izA5d%ggl4tXMy*yeV_p`@VZ5paeXk
7fFyhueXNr2{{U(a|*zW_!IrFXX!8E0pgYoHxkFc5NiSGq#Ad7NyoivVUn3?Jd^Ro1O3w~8duYp%AK2Qx1%a*00&JPANc|g|9iFX
k4=)o2u_g(0Cf?zEJ=))c=@0~IMSs-$-|6A5-LO}`1p+%Nod3&mVrIZL!Cqe!>1TY$$an}3EG>E?J5+L4~MQ@xCb&Yv2n;`V&W)k
rg6lm6a=J7r}2Ef8gi{Fl+0`o5Q#Ur-B23LVt=`T)MQ8tQ66m8b=nmx+)A2-Zjl>0b$-WBs#5_h2^)NqInByzr9pAQ!7OY<`QTr^
hZ39A5ZqQ!P4_0WUTv><IKEGha?Za$af$QZOaA5&-EdG(cI2>6P(j;+o-&6M`8S1_%z8zWN@StOxncMUu!)!p=Z18BR~0HEMgJVP
|EWlcUI|&=x2eX!O~YwOqr*6tSPTfKZg^R@nxH3KsvkTI5szXc2T`o}vrp}{C&5B!$*LU-(p<8R>dbJvrT8^+O*mJqMZLaHe>jVR
LM`~c96;sf?o&%8U<yrQ$}$D{j7P@W8Io$R2MNqW4whzU%_cIFq#>TEZmxbj#YcOdLWdrD&??n?oa>CD%=*DX*mh`deMTcHN8a2w
ROWGlXVF%_nG8W`c_AzZl9Of6p<Oci-ed3=C?xmvT4#E2f`@o3%R|>ZF+uiQEFMVhZUC~{M0!YC>kcc}<iHuysZFPAw$WSL0uj^l
MS9H8OQ&Ukpqolch);9bEIQ=fY+fI$+Uj1IRlF|W7KW1jky2(xsskU(9!}s@{Y@MisFGZjQ!?%|9n#C~>Tr?YF~T$sdxuC5j{&4Y
q+!onIT-rINjCdV17j##w!*XZkq6Sy=TnlM%+J-S3Hly(7~V{pdKd*quoI7+sDHx@gVR}47A;&wO(tgvyIb&S4pm2!_qvR7Gjjij
D}1K=AMq1*$*`TfIy!>Zfb66WYB2|9*UBgbUr3x^hXH$tu>`V;ymfjwV>{<UZPLaVgVS{9#!7>|Tbh`P5pBqi2B1c2kX9E3I|*uY
uP$1De*ls7F%{I9vm>ZjbXn{VH;5>9UaB?USf$bO0o|rlOjpDrdeo&R_!G(Ess4-5%kQ@MzMx)R)ORajrN9qGw>HNaKXiD??=tEv
r{r{*GRSw6$<QO35vlsDd!mJs>=F)l>`wKAjs){H-@mKkP)2eN=Y<BJ5SYVei~E{{l0^v>DWP+JFd2fu>@UVD6tl&rMKCu*Z0&OZ
&I2v?%*8$EGP9pSzD~H@C}d$(z$eX)dU+EFfzaqgb8c!u;KV0`yE7cF!hc=%jb(j_L<Z$797@hrw~D>M*Bxn{BU*U6X97BfOzGdj
dr{Z+ZQqO*gkdmWhmr{iCZGp}yqO7}73f9;NyL96t&~E1qa!|~t@%q!W{_I@MPGSby5{Hy_25nlylY<-riK7}S;%Q(UG7tL{99B|
mUubw#F>QHH|Bm*%C<h{BjbD|vr;RQNQu94--y`FDAz6~eOvSe+tC~IC9FMi_inP~$7l>jE_cCfvIItoi=n<_EQ&hqH1219ln(;A
F%H30Jd-W~D)K)>dAmxJV-E33F^(Lea`o<?;TJ#7CQq-|;cs{ha1!SI&cv@cl_sz<;r`VhG%nqz)<T@b3~G?|-(xaa_i^W2t0eM2
WtKxM(N?;w`oMt`D#>m?&(F}FQ=W)lTwcexgfnS6WZFdf8ZB&|ct|4^F;qRiK!rsJK;?C3?(q%;Kvmx8yF|`oSP{$F+QxMcAceMW
bqn0NpSkcWR*VQ%7N|shum(Z&g+5rEIvFXPO7T9U-4wJ~5%2BaP^4i9@CRDm;;E(EN5|R@zsys*%0PY<arj-z*pm(xbG2j6NM@XR
$`t);x&<aj;lZRyb%Z3@OyUDh8wf^?hqbc18L3hk_QBCi1EnKU1LKBCq3Ci|yCajYcz+Z9Pa;8<{^!2$1-^~zA>MT={kQ1@C8Zrz
H8;sX1<k{*RqKcWUyJGNj`tT80*L?ZRQ1=TD7mS<k!wJ=(0r)lx`_m<uuBIg?@k_>MtoFU?b(a;P&58cY6;7h8TvXQdDcrXM&Jj+
^|!Drzo7BNA8rcRuLt3bR^%mrFEVmBf+)?Pa}B?BI(Mw7PS?u_D2zL`^Myx(uW6g(%<c)Gk&H-Lv{|Qgcd_d9&O?dL5}i>_)pHyb
i~1S_15+IK{z>j)9v=HHJuhFIu@YVKIATrHm&Xw+jAs*^N5UfJXaKlb{D!~xhi6Y2GrrTBr62NiCSG_fbh9KFh{c;iGKaA&O68R>
a~Yyxghve8(@YpYw~oJfZ_%E#Q&0mBrJDqyehkINXzK`5)AKf}{BTrG0J9Mpp&D8#*Jfp8OLE-eGDjvU{<+|pO8waFcRczo$Tjz&
%g+b8s}hb8&wt5`I)xZah;mDcz2uzsT>T1mnM3zmQN_l`ZY#Y=ty})_c$Gw3lt)?j5f;5D>fDK5%ZHa)A3y0Qj!;8gL*As4EZ{ih
(mef?LQXIdi(IOO4x5Gd|6B8t>+w*xIcm8gb*BCnJkF<+ei)!wBk;m+j&qEx&{BKuVcoGy3Qp3t^Sd1JG*)Z27iJ&gPyyjH(t$o#
G2*Gw`j59dj1wMva9{T7X=6Q4g5>mu;*S-J&sKzkxSE#`55Og4k-xGaeLI?S{SV~3U5KVx3Qr;z-=3ARi0hLieUW6;xuCc!On&Lc
LS?QlNn=XDQ<+WD`NF1sFJ2B)b|e`#f7onWW_)#1d?_=n$U*y4uLr7`>im3uJxbWWu#Yt6IHyYDxSw36k^Ujv(cW;qJ2p#Ba=G?q
tNt#cQpFy!9;*~?T#a(9*38+N$7L9Mp^{<Tudnr84X|3RNkM+WKbh`RQ0UAVct3V8o8-^UUISJfDbRzJrw|ze9*{&>Iw=%e%aC5|
NFl$ca2`|5cd7%1?gaFvib5%$xz_{kC`t339@GO-UyXmpF*MKRW2pt!MLCn3559U{DFYe#_(J6`>84}}bp=X|gDPC^cR%Klwzbh4
^||G+wCvp#dWHfDrASnp)6{N&<a{1w#ySF)3}5`|gM^2*3PaYk0DWLkB#deKNme+@bpk6weo`%!Y;sa<;a>Ol&y3Qejb6=xOA%T=
m3iO3U#4;;JEz+N^d?p}_4X!(U&y0<SH6WZfZ&RwAh2i|P<3?leyw1^xv)Z$3KLU5viPXJxb^vfdrnDS_qeZQlIl}*TOeI6XhRL{
oP?_S{^28Z+zKGznM883o9!v(wwmj5VVu=?X5Vq>Nn70oLm+u3mXZRfWe90$2fb6W!iOjxA~qQa2qy-(@@M}@a3rH0XM&k{XHpMM
B>B!wB?Cdnv-(!0;_-QDDp2)eQh)^Zsu?3@cLe1ijtTkK(=$A~%HTW)x0~LGhbDxhSLOyMJ@K#7<P;&{D~aS_1TznJlNFRnBBZe?
#!8NGErEXp&{lDfgm(KvB!~+tJ617UbmX9Lj1eze&=>N@oXHRa`r~%fRb7l3g#(6BrnxP|I``IthhIDj+d6}z=VhhC(}_;+u{EYa
@cL9vEbE-Uv#L@~b*)NDa|=QWZh65nv_ErF(qCSn+7_?JuZ=r{rjTtn!KZyAWiJvKdTbfvQ{*Xmw4fFaHT6HzFc<wgB2-G0536-$
NB`vt7z{ZGZzUnIl8inz@saUp^u84&dn!pmr;<Q!PLXZq^Y;eXho{D-R%AGBR}F9hi26N)cz-EaQro$@dBiLmL1rFEBJyVVH9noc
wMmcexzv~;$FCY+kU@Ib$QhdY2cD}*BolQL<t;aA^T!nw116i{r?feSLd#~x>$qF=Y*?_~gZgJ-1dk@WfNLr{g1{2p|9rvoHW6~U
;%yu%?-8BcBxl5pLbTIdHltYMhOcH8q4QpDS}fC)BXby_xW<Q97&K!q)X`Vr)Mq<B+1fjyEs?_cFY8-d&~A9xX$Atg4Gz|R0bDS+
R{W*@UT$nuZ*m^U#f2V)wUuNPou^G@-8Z=hoF(<23>-=DOG}Xu%Y2hs2jd{+7#>hH;RTATElx5XMo=dv!sbod+n=phcPCm|En6d8
kAOX91Ioat`U`~>;uwPT-N99ag%t3+W8~)O={&=4-tA6+*uX_N7s!ewk<)oA3L#`A`T^#@^IaB608Tc#l~>lnwc*mr6_=mU{cQ&0
FRozGSU{U`fk#kY%G!o~<+hQpmas2oZ~DLl^Du%?A7VDY<Qt0I&|34NVGa-eO+TG>Y~pgYn0QU;n(llp0e|{DRdP!+O?pf%9)Gi>
WY`@)ru$~RnaalZy<n<7Dar09hqrzn2vKtH`8amjB)$KKD#DXsX{H8*HU}pgtrWBOq5hk^DJUg?e5Y!kfBWj)tMpFmtajLX>SC>;
@e`W`<)AcDqN~o#OHY&Lc~s$kd*mZe*b5M)c-h6ZzmllW0*8<lr*W|<p}r$KQ*uQqaIrvgG`Nd7k}K^umB>LZaf9-$g04><jS^<0
wa3ve4dbd0p1?id$mBfw#_R`**+!xp#Er0j7e28vo<>5FeG0TJhp*^Q<<TlL)Ka3*-$HGgS|d=!=wT?@4-XxOZ?lKp?tdn;b4{6i
bWXM6MYgQ3tygmD!g`?Z3QaMcu*PPc+e+YJJ?luRUH@j0_hJpL8ez;i(GX`iG0yKgB+ZPTsQOO9<DPEA*WeZTBbx4{+!n8)?nAUK
Gp!xW6TIMr);NAm9)y*Re+2`b#B^&@vo4X!nJ90%(-X!2!{=aY{Y)*sYYq4q@KQn*qD}X38Mi9_VVfKHY*%p*Vrk+Ty%P5yIySnO
iS$*TUiY;1KuqQBBDRM$<rx#Z#!FXzY*dJfl#0@}4LXLDmVaLJT^<8O@b;vx_gq|J&4jQC0Yf%{^hjy3P!5T|qR>_dYqJ<&6mV45
<-cR7@D5N=E-c84$i`5Q*)$4&XcD4a+>}-Wuxn+|3aN8aO9?sSNjVMN(mQesUpK??%tlrnRPRla*sishzdFXavyiBu6G8#GRd=|k
R}A2`R}*~c*IZ_up90)%u8rTBp#isS*gX-!Mnxb1V&wf*l*7bQHz`tzr;CfL-WknA7R4r7^PKYdxfC^R%p&1EH)xGwMkj@4ltJ$!
-)dhx@_rTGg;fWn&`7F6KSLpc_$fkRo2%&l&pM6Fug^n$c1873N*_sUm2#Q^bzYp0PbO72ZpBd&0bQ)rg9?QjR_G6|xw|V>uhdAR
5Paf%>0n~{$BeREl>FoYaonX8Tu$h!^E@AAkWTq;Q~-;x;k`m8wr=5Tx{JlyM2;n*C10aMaWJU1@Px6@3c_J5C26}ycv%y|uNPR{
Pbz(<5R(L*QTnKLwFiCmLr(sQ@o$n!0srl(_NcQBTjEhPgDeG~SHQK+nnYaXOWw`wR5+2yMkMBJ%aiMWB#nh;D1y64`**vkqYbY|
%NT~hd!cv?*MFY|T^)&8AR5NI;*6rZ%ofjEZB5NcJlmB54IV3oC_|l!m~OF=ZyiCzNNgc95tNh2G;X2^?%;{jMFF+#zpVq~!@Vjn
?}3eKCfva5CYAQeu7r<?8H5A5^1`ZNsCD7F3_4ten7vGO+s7qvNIfgN^-J(K=L1Y)|Ap8+H#J~z_4IdEd7DgG`-m3Z-A)SLo4(VV
O~9|GYx+A(&|AKJSN5jRw8gt=2F7|}=X;3{bjc`{Sn^#C`x2N(Fe9Q#t%Agkk^?0Uf(404wHyyJO%cirVVHV3y0dA3;Y<o)xJyoC
8>9_jp1=F5;60XV89#yEE!cFjYcKeZ<3%TZy2M9jKZ9MWD7J!-8fldYJYGYw4tQE!jq{(z)@QXK5Ap|j=lO=veQ9@149cr>kE$OI
8F{l8+4n8B+Mi+a8(f^uHHShunFTFswx;bZ12AXq`N@5u{!<o5AwUL}j(<;UtDB#XEWB*Un%lmH4l%mwQhu_HKS3<Sbu{7OnWrDh
;Ro^1!};3`{83aFnK~?o`_}FS=I$*s`y-I5LhUATN6Mt;{_tVrNO(4;X2{8qW~K68i6F|(hO8hiqgJ?wqyy)PH6{Oz5rT2A5q#bl
brJ3e12l8$qgj+JZDzS#`oS>Xx~^$5Bhl8<yw2glw=q}Y6aQw>y;n4c<-&pUn^dZCvJ%<4C6Kgfi>g&7k>M`Tvk++7j)g$S*GOcK
J}GL^NXSet6g1gI^SYv^0w|SCtU2;0j_Y80chp;v%`2wp#hHYek>+W1pf-HPSb)OSc!ATZ@mbz*Pu%62{LPMC1Wg`_8}i_2$vi(!
3ak({orwWSUx@*YbJ6|8aNXhb&IM(=asOt}En)f2GMEQhflXbeuq@8^mX!((aKCc-GA2;_^{wr2@E$DVK8$LKT4lvDVon-CNR!Gl
f~Nr<)i5osHV?Nm;bfiVJc|)&+kvsq-AdOlLkc2oC!!TuLgp(jA7y6l*pnhXxx5YqD>j+n^g7CU>_-?fU&ER=*#%c3C9|X}T`zh{
k)E}e13n!bJI*%}(zpukBy-$?);;^hJm;|xeUG(WWf{M8`@9lb);#V1<7!aUO-@vLFl&tERzc1a`M^}y&{!#s!}gul1cNmn6!oF4
mVMNNQWy9@@!~7fNq?FNW~9Gx^f86d#Be^N{8@+TCL_9kM<OwbNxP)Sh>?*#V_)mHhXn=qzUWrz%*W$xg_k}Ga}9l8-}#v>F(Mhq
_tm{@FG1T3vEEDgQGMaVevBFRUE-U;HdjGqZOk>~zq1=o^V+jVEMatLf{8Cuv0KG3D3UXDXd-coBnV`fJoFen;1VhhG^@4xJB|P1
uE)~CMK}wWu%@8CH}9!1a^KrJ6hHJ`d?CsDjTp9&T{QX$-Q|7r(!p_mCm8~mIz3(%q96K#%7Y_b@D{`wJDS`+vdIGYX-iRf$+rQz
>uP@crRYQ_Qi5kynhblf4E=f@#h!@v-i#?Jqp1d1pjN?j1RfD%bgUlPk0<CEyT)TH@nj!Wes)f_SFiMw<(FDHwQ4$~N@AgcQrnxC
Ps#jToEB--j~f^2xP=5kJRFW^wDDx%1)wiZ_$-bxbVmU*<A4ADuAx!aiUYQEkG&nSMFk>E(W=ljCJt|YUbJnMqY#FYt}@sdL_g)g
*hrHKTYD)g^WW#Gm?|0cYgD{=1L`N1!OukV*e6YmA2UP|aC&B$Er@gCfSQ60c{_y9-AZ^}@qjzoc+h%K2&=AvM5>=?C&a!AdTPUJ
bCzKp@qW)dO6Qu4>R$@u0ZI$Pt_p0ghrsdd-Lc#u&u(-Z;8OGyS@Z{Fn;3@9ejwj3`4@LZjfyh-MP0T1F)T0y8yu-05R17;8m1~b
PDa_VWmBfzx#1`q2d>Clb%XFw!(dDX2fyydbFW_OVeiuR6ddrIcb+-3BT{Y2fXt#}2Dr`2mMoXj_kBf`uea9-OsTS2!HmN|e&tN>
t8isZ^aM8E$Nkte6e+v-wRg_Way?n2ZAS9TRL%l?xMRYN;p?7<92eUfxsx>H8PC0!(1J#l$bdZ}=HfS$<Q?xCs{94SwC;94?GBDS
SlRLmmPofap*%O($oPdt^JCLn6I9|&YQFGrX)dxX4Vb<aewaMu<{+4uIUxBOleu3QH@keezM~z`Ztb@-(!JnEB0arL;uk!Sy->15
*D2fLSbUQ#GQIm|d6Opmv1Sxd)JjO9K?yXNdcL~Ej^?Fx|MwR1>t)(95zCnD`@RLLnD`BkQVRG^;c@aq14=7xP?zok?j<ouW;<5j
*!_}f1w=LxTzcIE7W4p^(Wkg1M{W~*6EJDK!CQc=&7mPrf;y7Z3gde~;#?+zDu6{7lm!&S&P2_$=AGWw1p^$QI@#}+{2N9=(^79K
TmeUfkfqYON}?~qa7lcGGM_F;WEmI(<|GAq5Km1w?<_Auhxc+n2>`^s#ct`{ZdLe9J*c*V8nnh}a|M^gMy<ZY>B~o@SgB}DlGs;y
r1fU&6zXF??l|QPVHnQxYMu+5`SVM0!|25#cm*Y~?gUm;qnj{}rPfdfhtt@ng?*;WX{v*`-OHC^`K@JhcfMoH^YkLm7D_ILLa%LA
PhC5y_)vQ<5QO#Ce=%O$*9w(@Wl~sAGuwyl4Ar<+9l;+G*beCN?(Zwf-ZO2zw5soIx{GbFWBf3!cd&7A2c2mcsdG9(;<FWBvkytC
)5M9igar$T50%2lY)m(XjjagLt&r??yTmOgZnsN@Fn_@o((t+kX@IZzevVCgd{*evTv}~iO3ELYA;UExLiS0X4m#;JkiVQ{_FA=L
0FAZEL@Phf$P(WRjc1_y`Gvi?vl5G~^kTlWqp(gu>_ga)8T1yN-CJ>W1ng?6Y5Xhc(IxM6#+b5{WnPd4(n_(ltLODfiF9(#wbO>f
XgIa@f(&yvVL0$Om8$4v55H<-ZyTv>_2B86a0d!a?m`&kulm@dr~8dxG1rb#OnQ<xtH5bVgXcCYE`c%vj^$<~g(N6^k<=DLiWhbx
`z*j~6JbCH_ZpT*R)kR)5M?SBH01Nj=)yYeQ+gn279NW6Pw3`va>7c^9s|k^$vt0rX1-928JRRA#TCZCAH_aGfuaB%K~E|C>dp#K
fV7(E`5*Q?x($ZCxx%FIoqEL=UsLOSOzy~Pnhs<ss%o?Z?$}A-usU3biVAFN><%^OO*?2xH`%c3CQ(SjrXh!`dT_)@B3Z{eHz1_9
+s;}LK)4&7#enXZM_;pZ8|84uA?O$(zilbU%6_(uT|5UZsOE0ST(f<C0&;>N-8#9)q&8{iFDI4Ps#4ysgYjnQs;rIRjWEy5It;m%
;vrl8^<k?vu9Q&lT{3!c9v5?)Wu2Orfy{-?_oia*q{%$tYz1>JXP!T4MN9YtD~>>8Q*j##aC4T8^nhr-PV~}qnUBc`0Dc5+?Viq*
36gi1*6A-vK(_+o%W*>(1@;5PUwr*(LfaF(^zb9RVJtd&uP)&TR!<SGwEk`~@J8bItX8n!ozPWKLufgnj3*>rc>)mrJwnIsQ4`5E
!S`+nHGMaD2MgaUfo%BhXQQ3dd}|g0Mz36x77!jo%en+gTz`fp6STs-71UUAsaL0bfncx<Jgw2-y3~I3V0OiQ3A)=6lBZkiQ#ex`
;n$!}+F+SLGsvERPf!Z2J%oD4$ros+xBOp{dEB68Cl2sCC%O`ekRE8}iFy8E>Np&yVd*E}`Jv|<nfKTh5B4u#eZ$EsP{42e#lrn|
?1cnuoo1xm(iM{eMEL|qkUm~LjP#1#!XL1t$ow<D<{NEIzg7V`H9!xaR8Nwv0n}VkBc~a*`ZM0gP<yo_6YHjB7rMCLz0W^-_i0Wl
GxGi@M+SDFU>mC>0#GKmuVpNck4(w2ZwKsoIlVabIP(Jql%X&!ULaayJ*Kj`!1UCyB6sJIDM~$#Oa?Cx&^a*MfUT!%Kky)N6zRnM
<!m}g%&sUgf%^&nvwo7zyv<&MeQ!LYzC6mv-N^bwjMdcbh)pBL`f3^{b29mh0i=8f`GhCwbDt1UZi^B%!R6=!gc7Wmmu_Dse=p^N
1@zbOz$1(GghXJf!blTcgpcB1LZR_=uX@pL3H10i2x5QPFOSY!waBxW)NIIZS9Hadp(>x*zhIQ<0$Wqq@Gin8;$k1a=S8XvLMS%*
nrdDaxiA$5G#=eJgOcsa%O;W%fla5b1@sVm=IpnxO0ecY%y-$w9JD2`ICcLu9)x?T3lA6sjm?J=J-hjf_d~MdWh2N>LpR+(Lf8Yy
@`&yX3XJ%AiKk7<{_Z&3&WUhcVk2`g|M12A&3U&ETK3Rlez>?*8haCDMNV6d*tg#~&Cxt5Y)Z`H{hO~Id&Mb7hGmskv7Bk{VSDAz
YdCDbn(Ouj`Yq?R1qnu#%9S6XO;eX>)|fl#&Gq9!vYOd}^DZu0QAMuxJC1rA8U&(ZFrVO<xSG}N_68!zNep9pSQbn;OtibS)m`D*
&WO!cwhE`dEms*bo-Bh`Ob~<Ae5X4idPvKnJTo4`WjmIEWP`m>vDd4#fN;<Cc!Y>%1#dEz;L=a6)q^!WCgGa&aOzX@O3Z4(4B>Cw
lY_^#8|dCOF9Ur{n#h-D;>dC6F@8;KLs}7a(zfyq&5?g#kw!{&vpb;)JeWm&(2!END(=|OQ-n?(@$lsr)DyW2#PL9^MwrMc9ij@k
>}ql_?v>R7QA!fO`XK}cxQyw7cS#a9=F!@83#m5o4;R-zsVmk5)X$;gB^48;2q*&Wex{GDIv8hsQmjT&A4(^*e3bKoSX|ZCnumu8
ayp4gE${>&8KQ@bHBE|z(WE3o35f%mmH(I<xq%%sl;7axdH3A!srUP=w#|WwTWLn`Y+R8pw>|pY$9;s}!m`#dXRQk;Ehyji)U@Ex
^Z=Lh5lP)qdT@1?u<={!Wfgt`KlXXv=8)i>X?MX_X3E!x-xBr>CQJS<@fQc85F&F^IUBXmWjm6R3`V|klF4h@*CXy(e$igV8u?g)
7S1Q_G-U*E@&rQpmr5^oSlRd{Pf?%y40!VDR@VM;j;lsl_646QR}Q2_;o7sLOW*ZHHG`xM8t5$><f5!!5L1dr(}Z$&lVg1Iki*dc
dT}-?@-{&5P@m-`nj=fA39{@#<lE;osUCcHCr1@4Q@a8w3na%Q4lp430cx2#O=cUs=OhNP^$qs3(A$+nu`Nyc%4@>_nJ6-nzS@jR
o$9$yN`G&Lg{3R0ovTj&Fo-(pO#4GCbvbMz|5tzm7Hq}a<I*lm2K<|^_C5Vcq3eS^(Lb%;*Er~OI&i-RMM0A=EA+3ErgEW#h9yGF
Q+YZob8D9nXgvLP6q(=b*VX}b%Z8)xzv?N7;d0`vVep1F;6-10uzf`*O}#v(m8T=NBpp;3qqGC7x9d2<6}Yh=*K<*eO=S<~C1lwD
&KnCV?ww|C{NdZ!34a>qsfZFpwMw>1uUDIL2O^ONqaV=pB}0R;Vk6(TU?Al>o`o9gt-;<cSk-7H%S;q+kIah~b-WW!kYTh(2Nj(y
<{W^LZn`2^Z2!>qWs8r72xZT=W29ilRfjLUx8u4Q%4)|djNVL@`sj!Lur^B~u+7RVXvoDRPuT5IqIqC7tcbEECWMNH&9_(wLtxjh
&EW_4#KWK47~Eg<H_h@Di72dyVR$5hDmYNIoDk?-Vtax`n<VQ5_riH`Bt-f2`oBqnwK+JNRHQ^v$N+iI;w!J0-h~>KaER#y1NK!r
mPq5a_)kLHs){^3WBkeH1$v-Mkm!5i)<_A1pZ9Oyd&AsziIqq%7IIijeS5p$(g^Jcp$BBwdI<O!c``4U;B!5Jd8Wex+e;U{VBq4|
oc$>$ExZ*vZV|L`1aAfjq`kE$U1()P7Dv>e6MYCf4MC1fGw%g)A$x<WKiFnr&@XlA8IH{~#$Xf1(<64$=iWTP(cSr8W{5q&ug`t9
lpNkK5YPfGoE>~)l*j)%u_?28Pyd0umiu0oE?E};DGF`w_2O+OPBU9p2U)h>hRcn3T=^wie1F1ro*$yEe}%g1)v7F%CW#9vfr?xl
FwtRasl~1Xyv-(PFzK{nrW>8g+it#w7}lDU>cYvWvD&Q^a~0s#Xw}&x7c=F|%b9-PguLTBSEd1$`<v%RJJ3CeSs9p@abKz5<8<au
tzKFC3Q@VsaQ5tC;xd{JUE89#h8#_WRRG+g{MXuzBEKu4D#>&+D0XlApYN*wN>e00wtU3r_(YbpNKz(FZYsm~Kt&Mz0nV!+MvWck
sc)uA^Wu`W$qQE8#qp*}vc#^DmHB}0&7hcZ<FSI5^^cGkej}U8$2Mg$0OastW+$0p(v$8?5tOZ{W(7Gb5BO4wqt3y*1DF7O(mcNG
?~O{3xZ)f^O5rToCTn1MF%-Q{+F_KViY)Lf?_cQvvPOdTaB<0%1>F7Dc6<vnoC=MJRcG#BVkHCzVrz9?Wcg&>t#BS$-ci3|H7-ww
{9ae0gbx}RVHLs%y;p|ILGA?ym~o;~(VxfByd7J(iLO-=h<W_!uVq+vjUd5A3u5j>FOznf%jgCr;>lzDJQ%CxkX5)jmpJy#s8@e&
JQZ}-dk*Dn+44~7_I(30mT`OQ%u<;`mY=4VH8@<u^VJ{G(%~o|`ejZBet5}S8JTlPH=z9|s=vWN*-NdI8MAi)oLCdD9<T2N^-rFq
WcHVVZ)BJxF2o+uZi>ogu_c~KwKSpf5Y;m9`-$8$9ys6QN<%H3?&P=y1~6?{e0vM=+l9(ZM+XiPcPVIuw~d81j$h1r-vyJsEs;Jm
dctpFnQts)*^k>&YE%0V%lM;d<=;*_kCR1ZxTKoLZMsc%du2`xCPs8_v<+tHoKMp~2x^*?suS~N_XHY(&&&IzrCa}TP>=BluV>4q
pY>V`{>MO(z{<N`0--foWuKJl-D)@45(fV?E&xI3_!UI+6655l+4C!mAnAhPOt^iBxLC7PJVzvIMx@!PwB^gd3WtuaZ6_|lFQev+
;c^?yMPgoVnTfk7JcAn}_-EzlwaRVBnl3AWUH&&08W(!j`A6S4hQu#1@sX{57~dVRdLBGIZ2Za6%dmAdC<&c?a{?b@G=&jp(c00+
1n`&*6;<CP8o4btkf)#6TnqKZFedIHALYlA&fdV*hJhn6f`63!+g#}A4LRhc#~rZH_0$Tv2ZAtKYe<~5gbk2V$hGqmciRa5h#SSa
wqjH=>#qCp-3wIh#_gl^%|j-tLy~`#lw?Fde;op=D2xeMp7D9M-=H^WQ&JfAm>sW5DRW9#$;F52@RaFL$d=`JHs0v~8#1+pM(}!M
3%mFrXLBD~eJk=+-D>hgHK|3UyPS0=dWIU)L^M1JXc(yuOq|~%Q#JANg+ybSBUmTiP>^i!519Ul>&^>loBc+^y~ZNCcm<GFx<L>m
A|-Q_hi=V;)?>v!=keZf%0@a+ZbryW1^D60XRuiJj^~Qhy*wKi%6aYJsEr5zhG57;m6V%yZD9teD=tnh%s0U-d%NTAtLDXmzSC+1
J6@67+ePl9+-mk=IHT}I911%BIn{^rM-|)j6JCDlWfiLXTVE(6Bw7D<I~Z>0$1q`3HDBs6Z_P5iCAR3;wj|Y`kau4P!S@?D1KM7G
0T}1Rumd*cPQZxVBp|!;Fv;r_pHiz!!ejy)iY!_odam1uKD4|$U2tAxA@;>97L)1-(#WZ`MfPVHoEOqQ7ZnZfmR|+nFR%BwQ867L
M#$jpJ6EgO6RVHUOMN5^lwxnVa{&3`eO&RLc#uj!rjv6sz&+8>oC8{DiBxEnT%5AZAt`cBdvQ1vSiEb2%)caL$7Tw}(#~%Zz5EwG
H(q@%lyo=0UE-i0{!sMczuB9)szxG!nT19ZA!|E9>&vgIB_^8SeX;ukfQ4TIWGWsH4*V4DG~~Hy(4Yv})C}+kx>CZm(<BAv*Q!=X
c|O?Kl50Qas$5Y&q})<MN`Wg(IB}&4l^Ch=@1{1pkEPW&wy=~M<i;G*xUxM$>v7lKge@(6s*!5}9TXUZc<EjOc!&MXok>u8MwEPv
ysYHQCbO*}L41%DsP^2kqXuV~TTQiy#gQEg&;8bQj~v=%8xVK3gr!ksIy7|W>_<ReYeK`2n(#JG@L6TX999L&^eciDyLDj~13JyJ
1wfMnY4?QdIr4RrH<W1^pt1T2p8C~XBz^MS%TEPATTySZWS`~S-6@NZPrkP&vTIfQz|+ULsS2SEV!Ry2<uCxsagl~Tnd9B@oeo~<
h2|kc8X%Y=jci^jp`e8FKA->?77=_S$5tal-?roS3#)-Fvid1a)LqKRDuhGmY7%CHq?=|TqveCK>LsI{G6d<?r7}gFPH4sVd_*+{
wec*vn6HjS3FnQctyGvV`&81QeO#tSPqq(Trlav{;}Bdkn`aZdD;691`*k#Ey<v>IXhs9t^wgfs|1Fq~39MH;T3lpQ(GWopZN|~R
UL@=T8+VHi8mzr@xa?Zp74BD>OD21eI9J_%h=E($I7}`))Al4y5*U`WC$(vShUlPPGOvBX%k)>+F?{Q%cOekO$@~>6#LTQ8+&yv<
xxI}Pn|nZ4ZCL`tC+fA!6~*><j?xc&Ga$(W@j?g>Ijy4d^xrz1rak74s6NW4WHlq-nNXG%U>t3H|6+4bcW@sIjKzn-=bhSqNw4%z
Q0Bv6afVM3tcW=PU6nSj04KQmbqU9!#Fw08!e*eTOm>HwfX5hMeDEv1kHX-)PS!;qhD;228FjjmhCln6@`4zKF4X}IwC+UtqTw%s
{#O<YdwP;2WN_rRTQBK|y8cVvlOGgOHVw?k;^ldX#OUzt_EK?Cs!8S+!vh}EkCIi4%EGp;f{k-xw_J{5Ts&E&9NEWb;>*j<fGXHZ
7%iP1wj<b8RTVX>EyomqMZ**C6duMmo>wovm6Fx_(K%h6{-TTBgw$y#Sb}bSQTB^VOP|k9rU|sZKfGLb*Y7xqTmC!B1|w=-g8CZ&
)S-o-zl~T`PUX{x_9HJG>--PbDT^pWLjs-?vH-3_rsSrObzcH^h3qzESgk!OT0g0fp4p56O7ms;;3+I}rCKeuS1D}7us9jAv1;vt
hgAZf3^-;;7UQVsuAm6;Q)<0l{ta<Dz9LjOL|X{b?w479d6bu}_Rp6-NpQ#etBPub40dns6W2+PcEgMqw`7<XMc`#nJw-I8Fb?eK
x~*J5>Q-?`qi>Hba-du5I9WnXT5L{&Ydw$4&ks?*q2aRE^$n!WTR!M{F5`oIlf*wrsKkUlrSdP$x#Dna8Hc&fQoXS<M<7;LK==H+
H@OYin__M)ocqp9mB1LWlm}}ro25Vk-U6u{Y)jpg9;z4)<2qb3eU2TIQ%{&4sT1%Zolpkv-Z}(6RN|<EXLL=<q;2J!cxIPtE&H1~
Y5d=n5%)KD-EnlkyO`-8=Z)4YXB}B}Koico+NwEurffhTSrid!Q@F;;mLFfKX&l^ARRW>KO4-mbj}!$;*PZ<m-RtYNKv{`D>cJOD
7}qm<T3r`DHrWoWrzOSPx)Sr(s&XsI>?}Mo)R3k1eR7wwS4wW7irvq|K6nF4%C)O`pu0P)&0#34EQnEqfdrXqSa1lWL4CO}W!`50
O>PZzn)Hs$arLIKh{uX0^@lkJ;!hfrAwFc+;t>jrS9x&Av+r5?9;E8SUlAnu$^((Ulc&VOYF!!l<6ug-WV%fi5&64i9&4=R5Xb(g
F7|L)fEL@vYz=8yXfp!;fF%gpiN9ZC|BTM<yRBJKQoNo_e4PNYH>kmEguzW*NX}n^qi+3u=9p?fMRl~R9Eh&fW(cple#aT4B(?eg
vc&Gv*pK`kCp^eyNlVFZA0Bt#pGy3hooN>WqGGuc>oX+khWzbR7oRIi*a7#M5W9V=TJ^bd%>w3I`z!r-gbGu__4);A%V07-t}^j5
Pvt5BLSUcvQ-$wc%m6Bubxr&*5|h9O_4-6z^hTv<uDex!IQwkxxz)O%4_*pzU`>ay%2`OJTQl|>^`ASp07^2bfh&J^YPpJJQ8+h(
`)H@}G~USpG|fI%@)Sdr7JNEkEC<Hh3c|_WDg`{yq9#qzJ{K%+KDyF+X1b1E?OO|W?7lXc2m6KB`B-4cH$7|`d*uvGPqPqDcb!3=
MUC8X=rRj9icnbXh5MufQ*f`TvuTRvjgKr}aZkV~l<DJ1|D60=!E6bB=~B<ILK30JX<Wc1D*seYEmO<+PSdEKRijq}DI|I71Rhr6
#t=nlmZt5JU{XYb$UNd%R1m93k!0WJzGZj|jl$;-R%ER3@Al62t%b~a*Ow_3<|vmU3Jih{KPGM`uD8RPLd5T>E61)h<zM}e(%&7c
rCS(^*Exr;ZruWsrXjS*8xNl0Cf;@b>6+6b7zSyPhZC1Yeb=iyH5g58#X$Tw-%pFqw)a}X+Bw$@Z64OomYZ4ZaFcajvAV&5w5-!a
Qq)Z=CxelXaBF^|kfGu;7gthDJ4F8ue_ubnl(*XhdFdIDD0m`T7nQl07Go%7pm=m3>GH(|9o<q@)drWIA*--t64u8ghFwLZu6U18
M;eeXiZ>kFzWr1jdv0>7e*w#-UKrn2gB!Y<k@+Q(d5L8(OcUBWRb#iTF*8ZT=rzuy^B8Lfh<wL47UR7MA7JyQ)V#C=uF)syGCjEG
<0BjUJ;V6F&Xbg`Oj{0l)jU|U+&)sFcpt^pTQOhZe9B#jrpseLSmyQTYM@rSwP4UpbKU<s&t1zim6_G?)Oa!M4pC~1Bh~kLYDJ^C
I|im&tcA^D9j`y8F~J4a?{)Z{LvNTh_wg>%Y9gUVdHrD6#2RDF%l4|VB>b7Yer0FcIdDKvwv-8=09$$94$az`sEopI<f8bZ47Q8G
4Q|yC<?KRbymj?=_^_aG46z@W*D6ZmRIh9stCB^M?B@@W7Jmbe&O~ZXJOz{VgBM^TL}%>OATtmn2P0dM03pT^?I`~y?bq)Px_3BE
?6npiv%tMF>+Y*MP5(M*I|oeXXRGjY&X9P5O4s+7>zABXpx71=0Hgm4dL2Fj!@Zj|6U%`*1nTOlMG|n_eT38Xc0Q<68%ii3oKmhC
S;VlA4GkwRfykp}%E}aCoV)mL^91btA(>m?B?z6x)MiUtS;3|F^3<&U;PIJjpxXx*#{?;at50~Z;qOYnfWqG+G_Jdi$@PE$!rYxV
BR6MS2=wPx43n^&mH8>~g1S*1Z2#+K^)Z0RrCT=YEQp^TnwW2q<9_U87{u5S9$eeRgeV3q8vy=EMs{(8zVEv9cw&H_)$8RXp9k_-
iOH+N_$|KRP{DOJVeDIE4weobsfiY|?m&yN?juKVCoC?Odn=76-e8px+d8%XUJNG22W09MxKAx}IFSSI<rR-Sk1=d|?*q*f(zx9y
XellffetyPd3z*Urt}3vDU;S<ZJh_Up%s42Z~R#Vk;d&mb9iD&!$qJ%Epz8o-?G+%HcS$aGB+(+l7sN?Ev=u6UYW0VWNmzm4bN_H
8WQNa1`k-4Rm2YNj_7JRAz0KJ2<oi|NUtyfESYloLcrC-kHy=3Uyqa+s4cw4_J93JKwS*8r2i)ImstU!Uw(ngBe#gii~=3wig+9f
gr3mvnLOz);?0&JGilL#4NzzE1F*-V0P;)E3tU%E;IGS9>D%L1U|tjri?C@O0FCKlrlS!uck&zNilkp0?Lfy<{a|EA_I(n<gim8L
mlEc=O05td&v{f6hJ8`0-IBbS8^d*1$!lWVrhD5G5#|sFto#>B<F`e&MYiB?BbvJl{ql#9QN)w2u6Qqs%z+(1PhA>eZyg+18AT>3
!8ItmUZZOoE#`hWp=^`MHD<o7&`@4@gm%<QJCSg=kh4UF<5(eZq1_0&dOnjET$@$?N%XZLN|L;Nl^fyhlPdL1imPT7G_VqAHS)2v
U&-M7z7Y=djqusm<{wAM8T&QR=+P1yO8OLcg{Q~4gAg&`lGck%<I>FJ35;nJoS~>IUJqS2JAy&-LGpyq7W(*{mg-2j-2$DZUX0s~
ululv5*}vSzt=P0liIrG_k9B0`gHFn&xOqleIV8<6;sI*g5$Kdh&zHuX=f2CUDbL}++s%lu|gt@(&Xw|*h_uHp#ZTY^V@}oJo;yQ
P3EwH6O_znyKo#&&pdKC?*(S^?h$X4m+Knw7-LnNcq0j13vMp)b3AFkZn6<TD9s1-0LJaz&;p$hbpzrQneI%>XaK-jT3cx=u^z8-
wr%Fv!*n(D_JF~Hf(p5dGRuBCpV)tv<D`9Fhk<;Vt6qb`Rg#?}aTTSU!&Y{3U0Joiv<}hf`4vMr9wzIk`*~UQdtp89L4eZW%-kBu
v4N@_!+7a;##A<WF2=KfD7oxrXUh7h<QZN-nVQuFB@Y(AH+xxH+xlR#>T`rRT!mMGs&|-Nt)$^Mi}9|1M|p;Q4<n-v=(a>k^{7pE
A_rEy)3{LjLfa|bjzzNqB3zgP!~rE72uY-!c4E26pz?rHviFtlLa$J#nd=+&m0OQM-j!m`TuOFfC{%5coC>x8qmhb4hXCXB8XjhI
(#SnZ4Td#tl3RTeW=iN2#0aU7*zgzpLw?xF2caeuNlPNshH+N5+`;or*-A#zdn=yEM8Nn;yg7G!mqO(!8s~O#9T>u`3<><XcI}e@
)6e=tWV$(Xm%#AJY3Z@7kI#LxUpXyq&oL#att45ybn2~bpBM|x`RY7RjUc<^Vaj5M1;VcTHgg0FdE^S64vU%g8ChxVtRyyQgoJ)c
9C!|eNkb=4wzyIR#2|}RY14PrqGi@4*Q>I>o!?q;eYia3q~dnGUYeNYU>mAcLtlmY%!Jf6Dj=exiUsOXzj@Nwl<Pz7;6MZPJA62S
zGaHPxEIg0EjCl>iH^ly32}-xtUcjPDhb~eNI-*3elP*{fKDO#0Byy5qj#bXjDyA$BTqK@3>^r6!xlh>IHSF3h~5p_iS%3XdjU(&
4|CK|7+|ogB}i+}CWZ(f?_QzSRis>0N`Es|^bj{eCm>rD7ag1-e)=|J${^j3&CC%Mp#lWH)VXP!!Q)$%uzQI)yU;O3rVbcp)$sGH
c_n*y#U%0_USa&X=X7DZ3BKjtWAfd9kEg?}n5L$Y3yg%5Y8{djL9)7$8E>5~8WQ6LEGN<=_Y~Ay{+6N&DG9#(e7I@&!gDQ4emW~&
2szB@Elm#9B{Rs@m=Jh|#XN%nu+*33fuMjX{%*6jJEsW=gZeWk`h}5%Oxv&yK1p0hgk$56{u;#O=tfJ#*{`;QXtCQ%5lfE5u>k<o
f{Z!H=4Z=q;cJ_W-66Qj62bcHiZ<t(I2<3bQ0Hv~^a`Qiu^mf&3A6XpxJOBlk4SB?ey+-ESqdk&)w;8N`SZO3=1g-Y7yg@YMRCYj
wRNJVvXM^i0!IbNuz~q&K{l1<`~8gB8mf$1NV$7g@r&d;=W`onugX-cPBqK3C?w_9X-*uAJV!)u9*k<Q>FDhkE`ya?jhsJIsBEvH
pbV2;k*Jm!U^!3>>ZGn(K6()j0P8TdY8oaorT}q6M9vO0)pDZKCId~aNl)s3q=9Zbiwcump7wbf=<0^}+W)jY4fdJl)Lze7(raIg
Pf}yvyX}F9x+WKoEc!K=1!AIj4GQ`#4GaD=Rv@6T`V=;mPWyBZc<SGiZKvZcx5>JyJEGW;*v>XQq_EL3ukK^_nnz?aAqh_|_uUMD
OG_!eJ?V3-BY%kL1_;bbc8-46jM>d1%5^KYa^e3>T}jnvk6dFYf)7FNr%<D$J<F@N)@d-NqBx;H534lB&)3)5gYF~nxNbnxthnJk
KPl&OYK9#dR`pS8e?fecO{PX5olgme1$!4L`)+K^f!akZl$V5VcdB>3U9^1kvnCx+gf);$`NfX?0Ib+Y1jgDx63fak^1%FumiOM&
AQP%dq~pdVe$V>4>&ksqvP9WZ%7T?Z`IgBG9KP&lPPfDGHpRYZE?U@3P<Dsv6`enw_pl=B-AzqJZ-a&w>}!IkT-<0htRt+>+w9_P
w2?XK#ovo)3R1Ah|3v`mrYV_&v6ogD*Wu^gp}A1!`Bwa-Y(#@wkb2=9xXxjG(-R5vF5euTUTPzhKCd0+S}0`nU^~X|6LN?q2;O*f
#3VWxW5dp~1);EYqK@F%>V2_EXhh~(!^K~Qmg?}9LZteFC6*;sM+$qRZ}pjIyN8(Zuh_1=g>Zz`@_Bj9^Ky81ATzEnR4Y+6Rsat6
`#Y758ck{bHDu@e+D?X2({6K=5|;T64*y3l{}lPnEn`*XER!wrt?UW_J)8xi?H_Y&d>>-HN3g;2)y3SzC20ZhYR<~Q#jnh#smM=B
t4?FK%LPp7^+ci4iZ~=^shtFSF3+d}IKg$(YcI$PYFNS3RR}7dmB7n-x>}UR>IUKb)l^GwivNTUh8eZhT9pVz;X`@+{|2Byrx2_B
)0eP*pfrZN&YI^*hx@J}CFSv3U_OIaXD1rh{J5xAX2(v}#vE$kBd%xVIz?-vblSdBhHT!Knv4w6zM%Ja2VgApBB~O3!U}7r6NcJ5
abPS6<h%{a7`j>`3EtmL%Sui%LtUUGdbvkQJ&LZIAQmfVEUN;c&eaj`q%U9kAMbpxV3aDei=VFbxzYoPfHwr2SIAcq5mrOR?8fGq
rfaEVZj8)9yJ`q!X4{M-DAzbKSguM*CoN(jkQGGTtAs*~6bP&w32z!}e)Se3+vRgnPfR;04IXm>a?!I=F`=iJg*Q*hu{Kn5g+K7W
SqzjuCol5fbazwWvn}~a#m{&8eO~O8JR$9!vE!aP8y*0>Orj7=J6!Ly!xAMwGp2NZEZa3OiWPbJMALNqY*K##oFAyKXdMQKAc^@X
`NJ|Jg+_<0_<*?VT$*K|4g+E@hzkZN44W7bm>sA<^19FtccbJ7vu*ykG2(xd(h6D49O~+5O}6=N-C?E3oH)U^jM98U5tz!dD1BR2
NHU)S6EP#W!G1J%$?~W#>ONkRioiKRj9aPjO}oC%tXU*h#2wyUmbF8Hrg6~$nXl%Px~+_rJSM>kR)N=)SpVv}b!icB;5xRZUlO#g
XA~q;M4~v|8M6bz)rV%|h-mi?Vq%J<2iODRB}YrA(CN@vRAyj}z=5Y-=<~-Vp3?^f?}+s&GIeKe?NwqWf#`paPN*=3Bpw9ApPnND
Kn;Ukw++cg2kt&4q3mQ^(_cz6d{GZhx2N2e+aA_!Gs*Nw!{y1vrZkuqD4p~0+0R_qbm9^=zFnlAFD`u{FNLCalVJA0X&F72{uZQ8
KxHqnju@zx>}mgY5ci3q*08H{Jh&62yal+4v=T9_==PHWTX@J#aQ>?xlBb9dh+q=8|M*J3Y&Pdd11<|mO6zb`2wjF9B+I%Uyg=)G
_SUy?!7NSjCC3xs;=L4|i0G`A^{=_BN8XI(5gVS+#~nk3#yWsF#aI(0B)4T;?iOU?<K__5Zk(A55ocoj7&F7_dB1KzAPJ#Em&_d(
^EKXt%W{@aYC9@B86^m0ZB9c643C_0$?MG4T5@#Sx6mMQjlW`Z>ykM0>*?{QxLay2!?aAk!Lc@F?NlCH9ck!EwVlV-FWZ?IEX`PG
u1KGd4=BdLarj^CvqXn39u^*^Bku|6d|X%1;{xk|vG+f4B?dX3MJwF?J~Olbp>qBalz&Z138VS`EPFC($xy-q{<v5I0PA?i4Y#=x
LPe#eVQ*Up1`qs4NHKKwv_0b^2#X}JGQhkFO@7>ubj`?vxi?4)Pw|ucmi!(=bq_`(0{QNv|Ir{{G}TK`OaCfHFM~Owif1+kZO(;p
+#RM2N3B=vatU|VU9;UAX?Vr6Ri6wqR%9V3e}Wmm+QN6P0Y?)BR~4J59prK^iEhpwJeuSFB(-OGsCS#CWT-%08oQFvG$z%{itpe(
D}G`Co6XTG4MBIV2pMcO?^rKhG=a@!u?!K~pHM7>v8eVWum=m|q`m~MyU^;616R>poT3$*Tp@D$GUdM7*9e2ew&*Yy3B<>NPX;7Z
LyK8L%&o_L79yG305~F#orQw%U^EB}tc5wi@;M#My!w6Ccm;zGF}&l2eN@O*wR0_|<);nitb@kTvEHHf7Nv!DDeq()x;y)ACyjv@
>1ov3$L0+Ms~sP?d}XE~^nqC7xcVjy>u?7Cs4r|HG=Ei~#CnNfgC9WPPtz(jt4KC^BYF)=>*D<`hH@*XW_7tVboheG;_Kf?rltdL
mFMsk^psGTX4z!pglYwxuz!D+j?K-;VlTC_6^ZFvB9DnvREqI8n2Wnw&865^oRSWQZ_<}egMKy`8@@b3B+tBLaJ=ZxQGU9BzIH|s
kQ8@>l=g?kRL86{yPvTQ5PR|{LiScF>PVAtZrPY0nn%0mSI5NQ0KAeQz&mSK)+l^hmKV4%ygA0%eVn9+q4_sOJ8di|ZBS~AJN}iS
!wo4_OeGX8S(PlNF8(b^Ir3o!8fRq49BS`t9Ybra*zRZ;-2IH80)cl^8e?Q;C8hd;sg~KwMtc65I|)mGRiR647T8`ZiO+gHm7m8_
5{izL9*a2KLnncr3W=M9Nr}=i?3atB1QA-nAKvtfS2IrNrp3q(G1uRq51t}CK#mAdT8ZGg#EA3-6DO3bxUZKcyJy?T-inh0kXPLH
6waXP=nwn1A@GW$Eq~gJGi<>`EjJnu+_CLv5jL@N63aNs9wtkL+vRhr*aUGpF}6{P@+!p`5K}(l%Eb7fV@fPZ{KGWwwx~4_$jH%%
rPpX(<){W@iTcEJHomrKa=b$@a-uYx_%pr_<T)pkbP5%>ZWx?l14YmUOs5m3hscQkA=qnTdm(**Avh`<rSix`t6*95_i8IulpvG8
SknPQ#!X&?=|_Yp;g>-;mGv@?UV-~kM{l>U@cIO9@*%!X{rcT_-90-#F%2)lze9{4SkskoHuzIBVx{d9=f#RfORTQATUjm{NY^mm
i`1>~7l14L2`$CzQJL-hX++rxme(L+!nP}e>!TAaoyf*%!E8%=l%GK&Ty?|uMJC(o)Xo~ah)oRJ!vez@k9G*Vt*vXKDWo-L#_9L1
kTO6y=59JA0f!75I*`=Jd5$t9Ak%&_lav3VEawq|r?g03goCpWtfg1j0}qfqcpe+0tqILMY0IM>YmoC@?ce!|p>vl+d#N4V7mIUC
QM@wl5fEC)dUo3l*qd>wpOtr64nn^xVX6}smM5(}Bl(QW_c7*RIje~})AHGn9XWn?X!)D06;eVtg5f7Z+F1G!p)s2aom^)sDni$$
Sv3I5Zwd0?n{OTW{?7%tbH%*Q;}-$$p?kDCmss&kDTK|4>?;po@1~7}B9@sbO8E8-vc7*W*sswa*$~E*u!~^szccJjwjRYHAgC?R
i_b<4&(-}su&iQDb`jscmp;Hk?4Ck7#r+!M(GoyN_q)nim;uXq{m7_z=oaYql7YW~sCnD8AkznyOm_d=KN_{R^Aw<8a?i?&&1vYQ
NemqbFD)j&@9Em?c_jxqJi7T|up?fIf~_hrY3R~IVo|g>-nq~b<9{T&!pC9sMolTT$)J~vbRPP$v1OOY1})~kLrOjr{)Bq2xrtA%
th(B7WBXZMAMi5y^P${7^$3ySG#+UIJCaE3Dp;IMao}HjQ?D{2#g1nU7m?G3oLA)WXsS){rE77Y(*JeC66;ygixRN9{>pqEj;)d`
Rk^VZy!eHcBHb`=n$&Um#30d5Ygu@sQ`~;SwUKD~4(wbyHrS$jx9I#5&SB>ret3Rk9-mJ4fcQ`Ylvm1^7S_=rzfkTo?5LQCZOE=Q
mlaFrm%FqybZK2N#GL=ns+`b$mp_Nf&v-A*X~_c7CZ6=)&N7LB<PX~X_9>yJ3J7+oAyFjTbgNSJWT3o#khx`QNtoWnB&_ekIYJc*
loW>MB|azRa%4g$5IjC|u*|RYO_&KpEf6*6f^gtF3@0z$2(t3N92@3GBlAT}HD6P=qB}g}Tb%P$0nIkDneru#!o^<W0xpkEzh@9)
)|oKZ5mDZDNX}+Q`=ou{i?C|;_hDG}|J6~!d8p2S(wpFqwaiRBxdRK|q`)UjJYoXuAU>)6d>;CTSsqKPE`=+72u-l=xXD!S@4-ed
d>ulv7WLRtg7c4w$1~B+3$r7wLHaRJ{!d{#NQYBs_twU7J0wSo*TWy`j_!&e*2)Di_2%McS&fmPF-qow<tA+)@nWZfo!(I_4ZK%D
sJF$Hr{mqY&<zE6p@ZhRmr^nJYa1szmdJPu6S%#}#<l<ZLg}Hz{pXQ=U9csoK@!k$KOC4d#CS(!sp!2J$KJLih^d4$^(OFR)5O4W
nYO6a|2dBKS0nP&BoYTFXb-XlFv{&^yp51^iFVCXruvqNE>>mHH%ogQ9F8uWnlkP4gp|)hHSwwOMARPQ@Z}i+8twPV0YaFyDOncu
u3$Dp!}|ncRMsU8dZ4+fG^Vp)Y7B>Ald<H)r@@%J4Hc{BRSnw9vhUGxFhwcH$&xZD)I5v1w+VztnmK1TM?=aAYs5LhTXld2=O`kC
+fm@W|ExhMCBeuj!`8on*N}Pn(?a(EZo;=S3UQUj?mFpYIiuxYFr&W08J%z6t#WdLa#y<$yFI@s>mSBJ*hK0<bf|R9u&gr)&nz^K
MowK0TVM<6*MzaAyFId8O-T=u?Hx_}+OEj+v=xh^QMO)l0j*FMssV|2(_wGXuXzNQXTluuwHE>_9WDa9_qOxTjg|COa~Lu?gfei3
lWWzOMD!c>qPtVQrd#dN-P!&QGZV5jbDHAtqpth^a7`MoMyg(3t$UN-n0Lv4r9@1{?v8H_6^$PL7;FJ+h|DahlF!W95?;@eglc6;
+xqtF1R)Z75UZMfx*{JL)&~@M*}=(WAgZd?S+jAMQ_PYAN_tQw9{mBBJ5a)ZR^c>8?FrXQ`&y)I>;vps;1m!NeCAaq5eZmn&c4zg
;Z)Dr-mvD1iC^HMzigkRD*rLmX?4PZ=%kBon01-M=~@!{X7uWC+VM_OScj2V9Z8obj5UKi#1b0wJ~D_f!M6H|4Q8TouIl5U4LUkb
HLGt|9h*mv;d~fwS-vs$lkzO=3c_&X)UqLzfbv=kEv7o=#*qIVWd*8hvRo+nji}0|nl(U0v$h|-6pL}aYkr1qAu}n2@*AU*Ti8BY
b<~IM8`NdvY&4uaRF?6Oz%AKdC5lNPG3%~2XJmj@Xlhm0`k=G^vBay?PN-y9vbfbT_NpH&z^nt0<)Ll*{$Ii$h;Od<9$Upk@7nph
7Q(p5W5g8yuX?opVuu8S*MeEQauJQ3_>D~EZYUXj!mcEP^1-r6^T{u?I_4V~v8f#)*G1c=)isdFiS(&tqMD2QE-dSG&kiBzY6P>6
IN}<M&t*F3NMee`IQ6Z#Sc(*_(qW%hH9@18|6V!L2EzpzLw8fl%!@Bw44iJYT;(gh5FX`l-lU9>qYi^79mTNY0b{*mz_BwXV?hoE
;@<$fHksVqxjL8xt{YnLnv)Lkn<mF&j7S}>f&hU1gWwfs2xkG)fc);Z0r*L+?3p^_(o;BAv>pFWh5JwgCUebeyLy+x$#SUF_=3uy
pJ31%zVuZdW<q!RXl`2$2ViL)HjaS;ZVFcv>ckd7bn^K>=3igXI_g6s*xa%)F|?H)Pnnv@@H$OdYNb;}<1P#`Ogrj%1WSz^%UMvQ
ctl@nJi?}R_I$9#X+}{3Wx(FW?$Foa@OpaL*YHO-#s0T4>lRF3BF+}NM=L12+3F~HWFZ^LPYO9rBmAn|<~5Hl=i{#LOlG+TZgj8{
wBe1o{I6_3^;FlmuJC3f(U|y|LYI-LXmXQoLLr$-NPnT!@VX_epe#uR6{>wNCg>-rzPXN={5d8gR77wc-_@w<&^4cNwn_CLe@<1E
w`-Amuxwieb5cVLmchQ2><O&-)38WiG8Y+J3~oR~N=_UY&%JdhEMR1^Vnlf}EhV4d@Y&wt8p2loO`gy1S(R5DfR*eHiazum`L<-|
tTF3mVVFOFl^eN92O!6D>RKg#iA%;7BES*`!H`(@p8V|xUc+m>BR9nK(~ma{grsAACIzHyi7g2WX!&ID8lD|qs|T>mm!XyXROxju
e#mH)QQlEmiq@O$)=z(7i<5oX)q4RvrKxC1q#O@BL)J&FVC;w#G6=4I{clyVZewKt4z!-4uI4%N)&8L${w5wuFdvgyLo$>B#f=Kv
xB0GdqK-U_fS<jImTDMP)<$G;o*^L%CtQ;L+2cnxnrW&AE9@DJ(8amWB1cUrY5i_ZKsu+b9zwBwXnoyl)oW_9Hm!**ixfmK^dH=9
<MW{mQgsz%@6uuP`Ix+a2O{8*L$MPJ8Ui!Wb?)%_FZm$d1NH>w;Dj%&r7GI;4EfY7mir-|<1!}ki`L$*MRm3I9qlgd#deruf9k;w
F^KG<(EG?2f74;SEhyaJb4qFH|E-asJ*`y5(A!3sV?;3PalbjzOI?Bbewz4f{>Cp^Ey>9K!H7W0EdlZsZVEjW7vM&6D?+7Q_JpWR
;8*tIzB)!b8grb|xK-2Q?rw63d2&G>qP9CRyrxgT&zxQ_g_Q)Q4?P=9Wi_tbgqc`eiafq8e}@!YP!@k|q*dQ#FMma?j6RavG1SMY
>Wk?%>#%Ddfsfq5^;!kRhcY3DXP!kuQKb#~OEnokgdrl&uJh)Nbvk<VwNQS)D_hic76(+z$PgXbLd<YgnG69`H+}B*?t_S`zXyb+
2Q&0B+~oq&6DNEplBxNi_+*$2iW+d{iG&;%w!5Xi*YYFso7|d<mCEFi_ozV{Z8e{`0_ZA&OOZ#ux|Uzw)o^&Nb;^{Q2_dxC(cLrc
3&?Kqvv78j%Kdu<+LMeB-yO5=@%|Hn#>Z_|jqsOyrcCwfyxdq&+;sUsAq+ik^gV+~cT)Ot(t^)fryRPU2z2rDku|Wq{6=q6C`|P`
p1s$zAAM4tD3~_7I(0y!WznCoE!UmTBhO4<{FY>7=^M6vEtovw$Gwr|-Azls-T3>lr13Zt_x)z`fH?;&*vfQH13niJGS>;3HW)H0
TMZygkuPogobe{@6A2zTO>tc>n3Nj(1FWt{Dv-HK4M4o_l0|&FZrX=(TR#HoQp&8emwVmbb%%G}1&=|Kz!fb=VDvTbkN*$eyAAZh
#TiPpD8@S?qt#Vi6$6np!&@%I8PQ^X-@68P#%s01c>GP)?|j2<@h0(SS6}&3{6+}J|84XD$QerdKwpi43`Aj=hc+Oa1$Ei`U+UYj
$^AXj5-5&E2#wbAlB+;6si86XI>5k+Z<@WI)I48%uN^YLl3e;8H%z^A7UO4vo%N<PManWU^p*4uh^lMhMxPH8nV1zETfxV&Bw3Az
Y`<&J+6FA5Ss2usc?9gRc`FAN_BA<)_n8msK~z+geHY$Bhsn4Ws1N;bf3UA9*j?#Iri3CuIAoEqGt;%1o9!fuwHpXXO;?bsejMWd
NTWp%(=yDox^zr11+5+|&4`Sb+l_@pSe9bOn9VoIyUQ4DJ?IYNMZFiM`4NmO{3lBX0@4ahs4r!EAT?5!pOR&w-n^NxF3M+v`Wlz&
l3mNAny|dmOrYN|oCN>U8}H41tti*f%K+4cG`n@>?9L#2w}dV5XiG)q=Y^nQNwSvIDPx+N(5^Uuf!B1ZVVYC6#JsHR%7ZT?7R~P6
&&ZeVVQ<aw08SiE_B)?>BtbQG<AEVIxbI0lJDGoMI77;Le5qb9Aa|bacG5m@bCnWuRWEb5y)t;Zxw@6y81~ByQffpcdP4QDJsvQS
Izrho3cT9TB?-c!s&m3p8_ABP4<1_Ye|;)suL%MOg%CJWD5G(WEj?nM|B;jyAK+x*=pKdk5bg_pJY9B%1Pw5vU}&pc(ngS8$Yitp
!DFBECXK*pvkj)dv2bNHy5!+8)<T)_SgoWrlM95Vi30Ow<g*QtO-HE_FdSt!`6{JWN{+#Kc`T5pqWrG&X{zNjC{I-L>`v4*&7k+I
;nbtFQW>|^<$ujQ<LIuI@1E&u%eMg|M&-SDrdNA!e^NpxG8%r}gV*`OzFwbfX6aU^0Gz7UpzN`y46{-Ae5E(v8{>5{&ThiZa=4to
Jent>wsEe$9B>*F{6yhHpXtt0J2E?iJy(zkY+_=Lr@8MGI_cdb7Vnw;n*{8L`Nff3bH#eMXPDzM4b|tY&;qo4<rl7E1t*#Ob~)vB
bR0N4vwiD|%rIhtL1jm{RaR^iqc|Rh%nlauPAAl0S_s2q3h!9UR@tcNo1U$!LW~Zi);w7WDpBvpc9=jx;c={q{45ma8Xr!yILZqc
L&H@BjPtpVq>RYv-s7PR9>+fdqv#`ANI5NZ4UYj+IRGUuDdbi6G6{@;p29!SG~u|J92D0JYX99^hE0<U12oFj+BDigdju><Xx+{7
I?x!50WVzWRL}u$I`9)@v$VFheP66etfGaLqkoJhdA${*dyGxEYgms<BolO{NMZj_*c;VzZa}TZw=HX1_3jIxFsQF%R~+ql@|0Ml
^}4Gk!V$z-y!uZVDd0;ecKNXVn(acaSx*dfY|VUm^mWr^6CUEHw!VXPI}K<e$|55U3moFRpt<}9@}E*xl2E{PA=5SMX=r((-Ul$L
4h7{RR~(xF$S|}pI}wvxn)^R|V28U?2)YVDmN}LoL#qL$g;PFpI{?lYL)n<tN<smZcYPhLOs}%ZY}Pyi2hk?$NHuroFJ!=F&b-ap
Y?W$N^MM5!cEOYf108Ibb;``e<@LUJp+zX!qmq$roz;}O+pQdD&|ZzUMq)yr0o~Rkj>@y)@^ACn%)p++=b-EPgUa>X=LwuV0^{P=
j`8mxTjurg0GI;VWlYnzT9Gu6;5e+9w|;Tiq!ibLf`Ph4&&IBiT50oy?w6#$Cj}L+)O_w|ikkbzaR>G4k*{*<AA9^2DHuXLr*x|o
308lij%~d-XA$hsPc$XG^kp4ewC#Y#tnB|WiAjFqkRwIt^1vw=END^gAp_)5^|wro`C4#7n~C3QVvY98oC5OG>2Ymr@L{(Hj(I!?
{9SL(V*C}Vh4)~=_5(2eoxYcpJ1pdvxtrp);5}9x1(;AN29OsbfcQy#)@<W$r-n<q5taN(Y&ki{R})R`O|4%sR(b~<QBuXWew0%j
lVOHnalA8*{s#NK6%TMMmd@>o^aWa4)A6`eET&o5X(*4`e;k$0w0Cl=6UpCR`6^~usz!s;tMgpmZ^3B@zQC3Lde)pGOkWVJKs}C6
GMJ(T`e(#mkRFKkDBaU};FrxOYk&(J@&QEHq=rZ-si6@{T(cc#P)2{TMWZ-mZ((&gNu;86y=vxEThU7D@iT`Z?2=NsVJ_kzmYD^<
SmD1xJGrakFejPpAb<5)+trBHbwrD-4>3@`_=~X~V&eFBnQ%Cf4*bnqEaszX>3y$P230vxowP?3@K5fA3qo8b{_~ATV50Cz0oI9Q
*EAxi0ZB9Dcx@e87vY2OR$&;hSok*-{j{5Y&$e$48*Uh3`O<s}m)?xo7<y$tj@=;jSGkL7B6h3HH&LGru^Shs?`FMRUGuD*Q|#v&
yBm%435WdJJ}X0@F~R}z%Hcy~+^G(#?hF9oOLSpdV5>0UM!gasyECPoykIsG?6Z^z<jp$G`)MVn1F=F>sc2jP000009f>rp&k}3W
00HsB0oVBlT`n%=vBYQl0ssI200dcD
"""
raw=lzma.decompress(base64.b85decode(''.join(DATA.split())))
assert pin(raw)==PACK_PIN
pack=json.loads(raw);assert set(pack)==set(MANIFEST)
for n,v in pack.items():
 p=Path(n);assert not p.is_absolute() and '..' not in p.parts
 b=v.encode();assert pin(b)==MANIFEST[n]
 p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():assert p.read_bytes()==b,n
 p.write_bytes(b)
for cmd in COMMANDS:subprocess.run([sys.executable,'-S']+cmd,check=True)
for n,w in MANIFEST.items():assert pin(Path(n).read_bytes())==w,n
for n,w in OUTPUTS.items():assert pin(Path(n).read_bytes())==w,n
print('C34_ROOT592_FULL_COEFFICIENT_RECOVERY_AND_THREE_ROOT_COVERAGE_PASS')
```


# Preserved span 401 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 402 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 403 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 404 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 405 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 406 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 407 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 408 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 409 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 410 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 411 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 412 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 413 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 414 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 415 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 416 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 417 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 418 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 419 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 420 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 421 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 422 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 423 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]



# Preserved span 424 (literal-source)


[Encoded source block omitted; the code in this passage is incomplete.]
