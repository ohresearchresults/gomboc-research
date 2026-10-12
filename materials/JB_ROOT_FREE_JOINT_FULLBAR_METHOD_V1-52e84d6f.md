# material-52e84d6f4b5c

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Root-free joint P/Q full-bar method and exact floating checkpoints, complete recovery unit

Scientific scope: physical free point-cloud optimization using the actual homogeneous centroid, rebuilding the convex hull, primal and polar edge graphs, all finite radial merge-tree bars, roots and witnesses at every step. No original U-root, stable facet, or witness map is fixed. This extends the earlier fixed-U full-Q-bar live-hull methods; it is not a claim that automatic differentiation or full-Q bars are new. The exact-control capsule [internal-source-reference] contains the literal resulting G6/G8 bodies and a self-contained exact auditor. Both211 controls are non-target; their sole Q18/cut20 depth remains .69616.

## Dependencies and reconstruction
The exact starting source HARD_U1_B_G8.json is preserved literally in [internal-source-reference], 978 bytes, SHA f5ee0fa9fd5f39860ff0e85add8c695c4476c8601ea0a623a13de9ada9f41d97. That material must be selected when starting from the original body. No archive retrieval by a worker is implied. The continuation checkpoint and both selected final floating point clouds are included literally below, so continuation can also be started without the original material.

Write all labelled files verbatim with LF final newline. Observed environment: Python3.13.5, numpy2.3.5, scipy1.17.0, torch2.10.0+cpu, torch threads1 and float64. Float searches are deterministic in the observed environment but no cross-platform bitwise claim is made. Literal checkpoints guarantee recovery of the selected exact rational objects independently of floating search replay.

Observed current joint_fullbar.py: 7315 bytes, SHA921d814c8ff17af335b9133d24646d20acc1733aeb0690794469c6a3a1fa9eec. rationalize_control.py:743 bytes, SHA0c300579206ed4c9747fa36d73a0dfaaff5517e34fbc55a6e1424eea6b8e8d3e.

Executed positive-control search commands:
```sh
python joint_fullbar.py HARD_U1_B_G8.json JB_ROOT_P3 --steps 1000 --lr .0006 --power .5 --pweight 3 --record-every 50
python joint_fullbar.py HARD_U1_B_G8.json JB_ROOT_P30 --steps 1000 --lr .0006 --power .5 --pweight 30 --record-every 50
python joint_fullbar.py JB_ROOT_P3_BEST_FLOAT.json JB_ROOT_P3_CONT --steps 3500 --lr .0005 --power .5 --pweight 3 --record-every 100
python rationalize_control.py JB_ROOT_P3_CONT_S2U1_FLOAT.json JB_CONT211_G8.json --digits 8
python rationalize_control.py JB_ROOT_P3_CONT_S2U1_FLOAT.json JB_CONT211_G6.json --digits 6
python rationalize_control.py JB_ROOT_P3_CONT_BEST_FLOAT.json JB_CONT_BEST_G8.json --digits 8
```
Other default parameters in these runs: qweight1,epsilon1e-16,noise0,seed0,grad_clip10,verbosefalse. Every run normalizes by its actual starting volume centroid and RMS radius, an inert similarity. Every subsequent centroid is recomputed from oriented live-hull tetrahedra. No centroid translation is counted as physical repair.

Observed terminal marker is JOINT_FULLBAR_FLOAT_DONE. First P3 best loss=.8637634258997225, V30/E84/F56, floatingS2U1, Psum0,Qsum.7460872644709746,Qmax.7460872644709745. Its BEST_FLOAT input to continuation is1851 bytes SHAd55edb5aea415580f767efb1231246aeece86fc5ada11de47ae9eb233ce59078.
P30 best loss=.8781343755559163,V30/E84/F56,S2U1,Qdepth.7711199990956668. A large P penalty is not automatically better.
Continuation best loss=.8326566602468131, floatingS2U2,Pdepth1.2104550540604776e-10,Qdepth.6932622158576318; selected BEST_FLOAT1858 bytes SHAfee6de528d67b56d7758493cee133d554806b1927683bb7fae68dd37426f38ee. Exact rational replay finds genuine222 rather than suppressing tiny positive P1.
Continuation saved S2U1_FLOAT at iteration3500:1862 bytes SHAc41d3639d5fdc59d420df7951335c1556c3f9a5cad0b20b52ef7c762db47b907, Qdepth.6961615574442367. Its G6/G8 rationalizations genuinely pass own211/weak000 in the exact-control capsule. Earlier recorded211 Qdepths: iteration0 .7460872644709746;100 .7394708220597889;1400 .7087087423677353;2500 .7010112700891923. Intermediate unrecorded bestloss checkpoints may have2U.
Expected rationalization and audit hashes are given in [internal-source-reference]; inputreproduction commands above yield JB_CONT211_G8.json974 bytes SHA7735223d4eaceea6a2fc71b76e464e10ddffc860c5040bcdb71114aa462bf9e6, G6json792 bytes SHA27c6bcafff1d74ae7d9a3c0a67854aa8dcadfeccf583f6d398d6a5096efee12f, BESTG8json976 bytes SHA62212062036562c396ff9402c4bbe39e5264703ef7a2179eca22d6e77d4cf395.

## Objective limits and earlier complete variant
Before epsilon stabilization, the loss line was exactly the mathematical expression pweight*sum(pd**power)+qweight*sum(qd**power). A complete runnable equivalent of that prior variant is the code below with --epsilon 0 for powers1 or2; the original edited file's byte identity is not asserted. All other default parameters agree. The three earlier observed finite experiments, not exact-class controls, were:
* power2,pweight=qweight1,steps300,lr.004,record25,seed0,noise0:bestloss.009784905164305826,V27/E75/F50,floatingS22U19,Pmax.027549094192653716,Qmax.03855303423126255,P18/Q21 positive bars. Small quadratic loss fragmented the basin rather than cancelling equilibria.
* power1,pweight1,steps800,lr.002,record50:bestloss.42023138817841044,V30/E84/F56,S19U27,Psum.051033935319378776,Qsum.3691974528590316,P26/Q18.
* power1,pweight30,steps800,lr.001,record50:bestloss.588941955156398,V30/E84/F56,S10U29,Psum.0007655813789874505,Qsum.5659745137867745,P28/Q9.
All used original HARD_U1_B_G8. These are local finite search outcomes, not impossibility results. Summary notes from a compacted context contained different floating numbers and old software versions; the values in this material are read directly from actual saved TRACE.json records and exact terminal outputs.

Reason for square-root penalty: near a radial maximum/saddle birth the normalized squared-radius depth can be second order in the violated first-order equilibrium sign. Squaring depth suppresses this defect further. A square-root penalty more directly penalizes weakly born extrema, while root/witness refresh still allows different landscapes. This is a local mathematical explanation, not a global convergence theorem. Next useful extension is root-free dynamic-witness feasible projection or finite physical facet/carrier additions, rather than interpreting a1e-10bar as zero.

## joint_fullbar.py
```python
#!/usr/bin/env python3
"""Root-free P+Q radial merge-tree descent, with own homogeneous centroid.
Float search, NOT an exact certificate. Changes the live convex hull every step.
Input: literal rational point-cloud JSON. Python 3, numpy, scipy, torch.
"""
from __future__ import annotations
import argparse, hashlib, json, platform
from pathlib import Path
import numpy as np
import scipy
from scipy.spatial import ConvexHull
import torch

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)

def live_geometry(x: torch.Tensor):
    raw=x.detach().cpu().numpy()
    hull=ConvexHull(raw)
    f=hull.simplices.copy()
    cross=np.cross(raw[f[:,1]]-raw[f[:,0]],raw[f[:,2]]-raw[f[:,0]])
    flip=(cross*hull.equations[:,:3]).sum(1)<0
    f[flip]=f[flip][:,[0,2,1]]
    a,b,c=(x[f[:,i]] for i in range(3))
    d=(a*torch.linalg.cross(b,c)).sum(1)
    sixvol=d.sum()
    center=(d[:,None]*(a+b+c)).sum(0)/(4*sixvol)
    z=x-center
    normal=torch.linalg.cross(b-a,c-a)
    height=(normal*z[f[:,0]]).sum(1)
    q=normal/height[:,None]
    edge_faces={}
    for fi,face in enumerate(f.tolist()):
        for i,j in zip(face,face[1:]+face[:1]):
            edge_faces.setdefault(tuple(sorted((i,j))),[]).append(fi)
    pe=np.array(sorted(edge_faces),dtype=int)
    qe=np.array([edge_faces[tuple(e)] for e in pe],dtype=int)
    assert qe.ndim==2 and qe.shape[1]==2
    return z,q,pe,qe,center,sixvol/6,f,np.asarray(hull.vertices)

def segment_height(x:torch.Tensor,edges:np.ndarray):
    a,b=x[edges[:,0]],x[edges[:,1]]
    d=b-a
    denominator=(d*d).sum(1)
    t=torch.clamp(-(a*d).sum(1)/torch.clamp(denominator,min=1e-280),0.,1.)
    closest=a+t[:,None]*d
    return (closest*closest).sum(1)

def merge_selection(x:torch.Tensor,edges:np.ndarray):
    radii=(x*x).sum(1)
    height=segment_height(x,edges)
    R=radii.detach().numpy();H=height.detach().numpy()
    parent=np.arange(len(x));peak=np.arange(len(x))
    def find(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]];v=parent[v]
        return v
    roots=[];death_edges=[];elders=[]
    # Birth order/edge order are selected afresh; no fixed U or S witnesses.
    order=sorted(range(len(edges)),key=lambda k:(-H[k],int(edges[k,0]),int(edges[k,1])))
    for k in order:
        a,b=map(int,edges[k]);u,v=find(a),find(b)
        if u==v:continue
        if (R[peak[u]],peak[u])<(R[peak[v]],peak[v]):u,v=v,u
        roots.append(peak[v]);elders.append(peak[u]);death_edges.append(k)
        parent[v]=u
    birth=radii[roots];death=height[death_edges]
    depth=torch.relu((birth-death)/birth)
    return depth,dict(roots=roots,elders=elders,death_edges=death_edges)

def diagnostics(x:torch.Tensor,geom=None):
    if geom is None:geom=live_geometry(x)
    z,q,pe,qe,center,vol,faces,verts=geom
    pp,_=merge_selection(z,pe);qq,_=merge_selection(q,qe)
    zn=z.detach().numpy();qn=q.detach().numpy();strictU=[];strictS=[]
    for i in verts:
        neighbors=[int(b if a==i else a) for a,b in pe if a==i or b==i]
        if all(zn[i]@(zn[j]-zn[i])<0 for j in neighbors):strictU.append(int(i))
    for i in range(len(qn)):
        neighbors=[int(b if a==i else a) for a,b in qe if a==i or b==i]
        if all(qn[i]@(qn[j]-qn[i])<0 for j in neighbors):strictS.append(i)
    p=pp.detach().numpy();qv=qq.detach().numpy()
    return dict(V=len(verts),E=len(pe),F=len(faces),S=len(strictS),U=len(strictU),Psum=float(p.sum()),Qsum=float(qv.sum()),Pmax=float(p.max(initial=0)),Qmax=float(qv.max(initial=0)),Pbars=int((p>1e-12).sum()),Qbars=int((qv>1e-12).sum()),center=center.detach().tolist(),volume=float(vol.detach()),U_ids=strictU,S_ids=strictS)

def input_points(path):
    raw=json.loads(Path(path).read_text())
    if isinstance(raw,dict):return np.asarray(raw['points'],dtype=float)/raw['denominator']
    return np.asarray(raw,dtype=float)

def run(args):
    np.random.seed(args.seed);torch.manual_seed(args.seed)
    source=Path(args.input);raw=input_points(source)
    x=torch.tensor(raw)
    g=live_geometry(x);center=g[4].detach().numpy()
    scale=np.sqrt(((raw-center)**2).sum(1).mean())
    raw=(raw-center)/scale
    if args.noise:raw+=np.random.normal(0,args.noise,raw.shape)
    x=torch.tensor(raw,requires_grad=True)
    optimizer=torch.optim.Adam([x],lr=args.lr)
    best=float('inf');records=[];prefix=Path(args.output)
    prefix.parent.mkdir(parents=True,exist_ok=True)
    meta=dict(arguments=vars(args),versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,torch=torch.__version__),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),initial_center=center.tolist(),initial_scale=scale)
    best_classes={}
    for it in range(args.steps+1):
        optimizer.zero_grad()
        geom=live_geometry(x)
        z,q,pe,qe,c,v,f,verts=geom
        pd,_=merge_selection(z,pe);qd,_=merge_selection(q,qe)
        penalty=lambda t: ((t+args.epsilon)**args.power-args.epsilon**args.power).sum()
        loss=args.pweight*penalty(pd)+args.qweight*penalty(qd)
        # Similarity gauge only; no shape stiffness or fixed-root condition.
        gauge=1e-4*((x.mean(0)**2).sum()+(((z*z).sum(1).mean()-1)**2))
        objective=loss+gauge
        value=float(loss.detach())
        if value<best:
            best=value
            best_x=x.detach().numpy().copy()
            Path(str(prefix)+'_BEST_FLOAT.json').write_text(json.dumps(best_x.tolist(),separators=(',',':'))+'\n')
        if it%args.record_every==0 or it==args.steps:
            record=dict(iteration=it,objective=value,**diagnostics(x,geom));records.append(record)
            key=(record['S'],record['U'])
            if value<best_classes.get(key,float('inf')):
                best_classes[key]=value
                Path(str(prefix)+f'_S{key[0]}U{key[1]}_FLOAT.json').write_text(json.dumps(x.detach().tolist(),separators=(',',':'))+'\n')
            if args.verbose:print(json.dumps(record,separators=(',',':')),flush=True)
        if it==args.steps:break
        objective.backward()
        if not torch.isfinite(x.grad).all():raise RuntimeError('Nonfinite gradient')
        torch.nn.utils.clip_grad_norm_([x],args.grad_clip)
        optimizer.step()
    final=diagnostics(torch.tensor(best_x))
    meta.update(best_loss=best,best_diagnostics=final,records=records)
    Path(str(prefix)+'_TRACE.json').write_text(json.dumps(meta,sort_keys=True,separators=(',',':'))+'\n')
    print('JOINT_FULLBAR_FLOAT_DONE',prefix.name,'best',best,json.dumps(final,separators=(',',':')),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input');parser.add_argument('output')
    parser.add_argument('--steps',type=int,default=500)
    parser.add_argument('--lr',type=float,default=.003)
    parser.add_argument('--pweight',type=float,default=1.)
    parser.add_argument('--qweight',type=float,default=1.)
    parser.add_argument('--power',type=float,default=2.)
    parser.add_argument('--epsilon',type=float,default=1e-16)
    parser.add_argument('--noise',type=float,default=0.)
    parser.add_argument('--seed',type=int,default=0)
    parser.add_argument('--grad-clip',type=float,default=10.)
    parser.add_argument('--record-every',type=int,default=25)
    parser.add_argument('--verbose',action='store_true')
    run(parser.parse_args())
```

## rationalize_control.py
```python
#!/usr/bin/env python3
"""Deterministically round a float cloud to a specified rational grid."""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('output');p.add_argument('--digits',type=int,required=True);a=p.parse_args()
x=np.array(json.loads(Path(a.input).read_text()),dtype=np.float64)
assert x.ndim==2 and x.shape[1]==3 and np.isfinite(x).all()
d=10**a.digits
v=np.rint(x*d).astype(np.int64)
raw=dict(name=Path(a.output).stem,denominator=d,points=v.tolist())
b=(json.dumps(raw,sort_keys=True,separators=(',',':'))+'\n').encode();Path(a.output).write_bytes(b)
print('RATIONAL_GRID_WRITTEN',Path(a.output).name,len(b),hashlib.sha256(b).hexdigest())
```

## JB_ROOT_P3_BEST_FLOAT.json
```json
[[-0.9623067509515136,-0.07255288628190858,0.03283636440440581],[-0.9503819991688165,-0.10424013946520205,0.2565070191552671],[-0.9204456406738851,-0.035667603249016175,-0.18594509245701457],[-0.9130088301156142,-0.018681806150058017,0.426111193995523],[-0.9228656687896358,-0.26437361055526365,0.12448497817208665],[-0.875030321686221,-0.3718389786475601,-0.025863169851531465],[-0.8391546659827297,0.08012762601034892,0.5872957388881683],[-0.8011519645994406,-0.06944554881329083,-0.4180948024247989],[-0.7953307656387455,-0.45300937325094076,-0.18374438103768592],[-0.5583989691759734,0.04137395250809975,-0.633167533689559],[-0.734277120640228,0.16759924391105968,0.7256473967450111],[-0.6793983284524369,-0.51606378359211,-0.32557585929849636],[-0.5359420179777625,-0.13438841016110112,-0.6367467320802143],[-0.5854347990821082,0.2476798859295628,0.8615969027572203],[-0.5360579323300934,-0.5777780430035165,-0.42993181506075495],[-0.3998777774646714,0.3234679319296534,0.9684336471824638],[-0.28783964256237193,0.05018789159167674,-0.7446440769761011],[-0.1290212326065422,-0.717634064929247,-0.247918154129722],[-0.36839257589306806,-0.5525521290980802,-0.5704192966085776],[-0.18094966355794873,0.3951028864463256,1.0400804607858127],[-0.22773873288814228,-0.4904195165481917,-0.6691989816863299],[0.03809761677221249,-0.5389324510748906,-0.5911606494739878],[0.1275396357198515,-0.5678588503637709,-0.45321015452740027],[0.05174101333139184,0.4517824765130012,1.06338106743391],[0.06878745312904071,-0.3012007970272297,-0.7096426047176664],[0.39368159556799204,0.5217412414844941,1.0233375021684734],[0.6830468631347744,0.17034836965818462,-0.44667211306555193],[0.7379849963153243,0.5747769399474338,0.8733289457490325],[0.9360766445322237,0.5916001858306901,0.7060615968394781],[1.5325977613675372,0.5980847069775704,-0.06132372472645434]]
```

## JB_ROOT_P3_CONT_S2U1_FLOAT.json
```json
[[-0.9678418830217256,-0.05465233011352433,0.034731775448720845],[-0.9588868045010175,-0.08644824583032668,0.2596936838931042],[-0.9231707876346567,-0.02238270449408084,-0.18997666483906733],[-0.9227155185642493,0.00761054899071324,0.42877205413324304],[-0.9364249671556741,-0.2419497656535508,0.12199321748861072],[-0.883260213050726,-0.366063125864016,-0.014054464903939919],[-0.8501685065757649,0.10875539016799222,0.5834103178332696],[-0.8062941319913548,-0.03708122958807192,-0.41463022729013765],[-0.8038985110559508,-0.45473911996294536,-0.16065236205645272],[-0.6023830897744993,0.06016184121276966,-0.6094249471764376],[-0.7413748144503269,0.1978979344657797,0.7263402741380107],[-0.6900249182102018,-0.5256867839815831,-0.30057532593801356],[-0.6116459546083126,-0.13140692504765716,-0.5958115364904921],[-0.5960412645610391,0.2688762135791167,0.8568559119035166],[-0.5313539426978918,-0.5911862352423687,-0.4115079552862067],[-0.414136449396838,0.32533046456468556,0.9673175398509404],[-0.3301152043725962,0.10458323175108554,-0.7281653498514788],[-0.06964651154230636,-0.7003736524954378,-0.19009460504861928],[-0.38574782704436245,-0.5601531296089969,-0.5472297131292727],[-0.19721608693213846,0.3846378112096883,1.0418100339003624],[-0.22415662180789184,-0.47066819096894535,-0.6660059167019259],[0.010413202482668391,-0.5303777124930005,-0.6115337455929379],[0.10922040983902671,-0.6085432608894914,-0.4005885560785859],[0.061873812233680076,0.44584240439249734,1.0701396899642213],[0.015434335497952532,-0.29254518257038525,-0.7334666732342987],[0.37020007823696927,0.5089091385085783,1.0282955509188043],[0.6152076702789182,0.18076131472305665,-0.4507925654210912],[0.679503356324832,0.5590100158138225,0.8956360301642518],[0.9290525437110491,0.5852183264425858,0.6932726605990998],[1.4670036462155274,0.6025390183027395,-0.030419793668914747]]
```

## JB_ROOT_P3_CONT_BEST_FLOAT.json
```json
[[-0.9683367136123077,-0.05623789064644286,0.0351901183740714],[-0.9584464545601935,-0.08777708489697592,0.2604526030158436],[-0.9236730330178058,-0.02147049144585141,-0.18909517540158155],[-0.9222827850725026,0.0073253435644685975,0.4288322014708955],[-0.9361989356944379,-0.2431650474281798,0.12146650388976891],[-0.8833188028763583,-0.366222187979268,-0.014426073500962403],[-0.8501282813686959,0.10926816298432607,0.5836863648077597],[-0.807380911335468,-0.038671096866867864,-0.4152820599396823],[-0.8042545552700232,-0.4543606020476654,-0.16144216849851636],[-0.6017181305246692,0.062047688473972046,-0.6104824135530078],[-0.7413551764567767,0.19820565903298878,0.7263280145967436],[-0.6905516234178576,-0.5248921611587248,-0.3015425521294153],[-0.6091659376275078,-0.13104440223229735,-0.5965922240972845],[-0.5958895337269342,0.2691730658106069,0.8567851592734458],[-0.5317181920445779,-0.5914276625247397,-0.41164998616407356],[-0.4142645808358219,0.3257880380519972,0.9674230781826428],[-0.3295491302639659,0.10228192218153226,-0.7274916336316988],[-0.06844907651501332,-0.6997660858923344,-0.18492733134193812],[-0.3867882903606983,-0.5601545261757204,-0.5479429592946587],[-0.19755040480236769,0.38445601112748606,1.041816261237821],[-0.22306087587843743,-0.4725961308798204,-0.6660397145561257],[0.010249937070571069,-0.5287624142198094,-0.6082680849119805],[0.1092082145834292,-0.6054073486937435,-0.40016922013400485],[0.061219332765317026,0.44588724965566556,1.0700568197114366],[0.015071921001648926,-0.29136833369876436,-0.7319249595290377],[0.37337268453900213,0.508832915770441,1.0282297197359556],[0.617856878990019,0.18152339372281712,-0.4486914589283915],[0.6824222728699411,0.5587990828654162,0.8944585163498665],[0.9279035396671333,0.585280316582504,0.6944737754194161],[1.4660112332308466,0.6023281630018146,-0.031228189257814537]]
```
