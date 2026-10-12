"""Strict-mechanics-preserving contact events. Floating discovery, exact replay separate."""
import sys,json,time,itertools
from pathlib import Path
import numpy as np
from numeric import *
from atlas_opt import Atlas,optimize
from contact_chart import make_chart

def merge_rechart(data,faces,a,b,controls=None):
    # This is not a definition of the old object; it constructs a distinct exact atlas.
    q=recover(data,controls)[:data['n_supports']];owners,ef=topology(faces);P=vertices(q,owners)
    nf=merge_faces(faces,a,b);no,ne=topology(nf)
    keep=[i for i in range(len(P)) if i!=b];ref=P[keep]
    # The raw apex is an unmodified fixed reference point, not the center of mass.
    special=[i for i,cy in enumerate(no) if len(cy)>3]
    apex=int(np.linalg.norm(ref-[0,0,1],axis=1).argmin());assert apex in special
    order=[apex]+[i for i in special if i!=apex]
    pp=ref[order];pp[0]=[0,0,1];groups=[no[i] for i in order]
    gen,depth=make_chart(q,pp,groups,grid=data['grid'],prefer='supports')
    return gen,nf,max(depth.values())

def run(genfile,facefile,outdir,epochs=30,steps=400):
    R=Path(__file__).parent;out=Path(outdir);out.mkdir(parents=True,exist_ok=True)
    H=set(tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines())
    data=json.loads(Path(genfile).read_text());faces=json.loads(Path(facefile).read_text());ledger=[];start=time.time()
    for epoch in range(epochs):
        m=Atlas(data,faces);base=m.state(m.u0);E=len(m.ef)
        print('EVENT_EPOCH',epoch,'E',E,'initial_min',base['vals'].min(),'elapsed',time.time()-start,flush=True)
        assert {tuple(sorted(p)) for p in m.ef.values()}>=H
        if E<=249:print('TARGET_NUMERIC_E249',flush=True);return
        floors=np.full(base['gaps'].shape,1e-9)
        for (a,b),pol in m.ef.items():
            if tuple(sorted(pol)) in H:
                for v,w in ((a,b),(b,a)):
                    for j in set(m.owners[w])-set(m.owners[v]):floors[v,j]=max(1e-9,base['gaps'][v,j]*0.05)
        u,st,status=optimize(m,steps=steps,trust=0.0005,keep=1e-5,goal=max(0.003,base['vals'].min()*10),geofloors=floors,stopgap=1e-7)
        tag=f'E{E}_condition_epoch{epoch}';z=m.save(u,out/(tag+'_GENERATOR.json'))
        (out/(tag+'_faces.json')).write_text(json.dumps(faces,separators=(',',':')))
        rr=mechanics(recover(z)[:z['n_supports']],faces,tol=1e-12)
        print('CONDITION_DONE',status,rr,flush=True)
        candidates=sorted((np.linalg.norm(st['P'][a]-st['P'][b]),a,b) for a,b in m.ef if tuple(sorted(m.ef[a,b])) not in H)
        print('CLOSEST',candidates[:8],flush=True);success=False
        for dist,a,b in candidates[:12]:
            if dist>1e-4:break
            try:
                zz,ff,depth=merge_rechart(z,faces,a,b)
                audit=mechanics(recover(zz)[:zz['n_supports']],ff,tol=1e-10)
                print('EVENT_TRY',a,b,dist,'depth',depth,audit,flush=True)
                if audit['counts']!=[1,1,0] or audit['min_gap']<1e-8 or audit['max_incidence_error']>1e-8 or min(audit['polar_escape_min'],audit['primal_escape_min'])<1e-6:continue
                name=f'C{2*audit["E"]}_EVENT_{epoch}_{a}_{b}'
                (out/(name+'_GENERATOR.json')).write_text(json.dumps(zz,sort_keys=True,separators=(',',':')))
                (out/(name+'_faces.json')).write_text(json.dumps(ff,separators=(',',':')))
                rec=dict(tag=name,oldE=E,edge=[a,b],polar_edge=m.ef[a,b],depth=depth,**audit)
                ledger.append(rec);(out/'LEDGER.json').write_text(json.dumps(ledger,indent=2));data=zz;faces=ff;success=True
                (out/'LATEST_GENERATOR.json').write_text(json.dumps(data,sort_keys=True,separators=(',',':')))
                (out/'LATEST_faces.json').write_text(json.dumps(faces,separators=(',',':')))
                print('EVENT_NUMERIC_ACCEPT',rec,flush=True);break
            except (AssertionError,ValueError,np.linalg.LinAlgError) as exc:print('EVENT_ERROR',a,b,str(exc),flush=True)
        if not success:print('NO_EVENT_ACCEPTED',flush=True);return
    print('EVENT_BUDGET',flush=True)

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('generator');p.add_argument('faces');p.add_argument('outdir');p.add_argument('--epochs',type=int,default=30);p.add_argument('--steps',type=int,default=400);a=p.parse_args();run(a.generator,a.faces,a.outdir,a.epochs,a.steps)
