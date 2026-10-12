"""Literal ray-envelope bodies, followed by constrained uniform-centroid closure.

For fixed unit rays u_i and radial upper caps R_i, propagate the largest
root-reachable radii satisfying r_child <= (1-margin)*cos(theta)*r_parent.
This creates strict positive escape chords at reference zero.  The actual
homogeneous centroid and own equilibrium census are separate calculations.
"""
import argparse,json,time,heapq,hashlib
from pathlib import Path
import numpy as np
from gmpy2 import mpq
from vertex_geometry import geometry
from support_geometry import escape
from persistence_birth import evaluate
from primal_log_thales import Chart
from constrained_mass_projection import project
from exact_audit_vertices import audit
from exact_barcode_report import report

def envelope(X,root,growth,margin):
    r=np.linalg.norm(X,axis=1);u=X/r[:,None];cos=u@u.T
    caps=r*(1+growth);caps[root]=r[root];best=np.zeros(len(r));best[root]=r[root];parent=np.full(len(r),-1,int);done=np.zeros(len(r),bool);queue=[(-best[root],root)]
    while queue:
        neg,j=heapq.heappop(queue)
        if done[j]:continue
        assert -neg==best[j];done[j]=True
        for i in np.flatnonzero((~done)&(cos[:,j]>0)):
            value=min(caps[i],(1-margin)*best[j]*cos[i,j])
            if value>best[i]:best[i]=value;parent[i]=j;heapq.heappush(queue,(-value,int(i)))
    assert min(best)>0 and np.all(done)
    Y=u*best[:,None];v=escape(Y)[0];assert np.sum(v<0)==1
    return Y,dict(root=int(root),parent=parent.tolist(),growth=growth,margin=margin,radial_ratio=(best/r).tolist(),max_contraction=float(max(1-best/r)),reference_U=int(np.sum(v<0)),strict_reference_min_escape=float(min(np.delete(v,root))))

def run(source,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);a=json.loads(Path(source).read_text());cen=[mpq(v)for v in a['raw_centroid']];X=np.array([[float(mpq(v)-cen[j])for j,v in enumerate(row)]for row in a['raw_vertices']]);X/=np.max(np.linalg.norm(X,axis=1));np.save(out/'source_points.npy',X)
    assert len(X)<=84;roots=sorted(a['unstable_vertices'],key=lambda k:-np.linalg.norm(X[k]));hist=[];start=time.time()
    (out/'source.json').write_text(json.dumps(dict(source=str(Path(source).resolve()),sha256=hashlib.sha256(Path(source).read_bytes()).hexdigest()),indent=2))
    for root in roots:
        for growth in [0.,.01,.03,.1,.3]:
            d=out/f'root{root}_growth{growth:g}';d.mkdir();Y,meta=envelope(X,root,growth,1e-6);np.save(d/'reference.npy',Y);g=geometry(Y,False);inf=evaluate(Y)[2];meta.update(own_mass=g['g'].tolist(),own_mass_norm=float(np.linalg.norm(g['g'])),own_initial_S=int(np.sum(escape(g['H'])[0]<0)),own_initial_U=int(np.sum(escape(g['Z'])[0]<0)),own_initial_P=inf['Pmax'],own_initial_Q=inf['Qmax']);(d/'envelope.json').write_text(json.dumps(meta,indent=2));row=dict(root=int(root),growth=growth,reference=meta)
            try:
                c=Chart(Y);q,e=project(c,c.z0.copy(),.03);np.save(d/'closed.npy',e['X']);np.save(d/'closed_params.npy',q)
                np.savez(d/'chart.npz',X0=c.X0,u0=c.u0,B=c.B,parent=c.parent,order=c.order,root=c.root,tetra=c.tetra,z0=c.z0)
                v,G,ii=evaluate(e['X']);row.update(result='uniform centroid closure numerical',S=e['S'],U=e['U'],P=ii['Pmax'],Q=ii['Qmax'],mass_norm=float(np.linalg.norm(e['g'])),V=len(e['vertices']))
                if e['S']==e['U']==1:
                    aa=audit(d/'closed.npy',d/'exact_nomination_g12',10**12);report(d/'exact_nomination_g12');row['exact_counts']=aa['counts'];row['exact_weak']=aa['weak']
            except (ValueError,AssertionError,np.linalg.LinAlgError)as err:row.update(result='finite centroid closure failed',error=repr(err))
            row['seconds']=time.time()-start;hist.append(row);(out/'trials.json').write_text(json.dumps(hist,indent=2));print('RADIAL_ENVELOPE_CLOSURE',row,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');a=p.parse_args();run(a.source,a.out)
