"""Event-driven spring removal preserving true own-centred escape inequalities.
Numerical discovery. Endpoints must be reconstructed and checked exactly elsewhere.
"""
from pathlib import Path
from fractions import Fraction as F
import json,itertools,collections,time,sys
import numpy as np
from scipy.optimize import linprog
from tutte_physical import TutteBody
from tutte_opt import PhysicalTutte
from fit_restoration import embedded_faces
from numeric import topology,mechanics

def ref_exact(root,name):
    src=root/name;aa=json.loads((src/'A.json').read_text());raw=json.loads((src/'RAW.json').read_text());q=np.array([[int(t)/int(h[3]) for t in h[:3]] for h in raw['H']]);P=np.array([[float(F(t)) for t in p] for p in aa['raw_vertices']]);owners,ef=topology(aa['faces']);edges=sorted(tuple(sorted(v)) for v in ef.values());rot={}
    for i,cy in enumerate(aa['faces']):
        rot[i]=[]
        for a,b in zip(cy,cy[1:]+cy[:1]):
            pp=ef[tuple(sorted((a,b)))];rot[i].append(pp[0] if pp[1]==i else pp[1])
    cy=[0,52,133];outer=next(i for i,c in enumerate(owners) if set(c)==set(cy));B=q[cy].mean(0);ez=-P[outer]/np.linalg.norm(P[outer]);slack=1-P@B;den=P@(-ez);ii=[j for j in range(len(P)) if j!=outer and den[j]>1e-10];limit=min(slack[ii]/den[ii]);assert limit>0;d=limit*.5
    e1=q[cy[1]]-q[cy[0]];e1/=np.linalg.norm(e1);e2=np.cross(ez,e1);O=np.array([e1,e2,ez]);r=(q-B)@O.T
    cap=np.column_stack([d*r[:,:2]/(r[:,2,None]+d),r[:,2]/(r[:,2]+d)])
    s0=d-ez@B;C=np.array([d*e1,d*e2,ez]);a=np.array([-d*e1@B,-d*e2@B,-ez@B]);o0=a/s0;linear=(C-o0[:,None]*ez[None,:])/s0;beta=ez/s0
    eq=np.zeros((4,len(q)+1));eq[:3,:len(q)]=q.T;eq[3,:len(q)]=1;lp=linprog(np.r_[np.zeros(len(q)),-1.],A_ub=np.column_stack([-np.eye(len(q)),np.ones(len(q))]),b_ub=np.zeros(len(q)),A_eq=eq,b_eq=[0,0,0,1],bounds=[(0,None)]*(len(q)+1),method='highs');assert lp.success and lp.x[-1]>0;gamma=lp.x[:-1];lam=gamma*(r[:,2]+d)/s0;lam/=lam.sum();assert np.linalg.norm(lam@cap-o0)<1e-12
    gf,grot,df=embedded_faces(edges,rot);planes=[];xy1=np.column_stack([cap[:,:2],np.ones(len(q))])
    for fac in gf:
        triples=np.array(list(itertools.combinations(fac,3)));tr=triples[np.argmax(abs(np.linalg.det(xy1[triples])))];planes.append(np.linalg.solve(xy1[tr],cap[tr,2]))
    planes=np.array(planes);omega={}
    for u,v in edges:
        f,g=df[u,v],df[v,u];delta=cap[v,:2]-cap[u,:2];rd=np.array([-delta[1],delta[0]]);omega[u,v]=float((planes[g,:2]-planes[f,:2])@rd/(delta@delta))
    boundary={tuple(sorted((cy[k],cy[(k+1)%3]))) for k in range(3)};sgn=1 if np.median([w for e,w in omega.items() if e not in boundary])>0 else -1;omega={e:w*sgn for e,w in omega.items()};assert min(w for e,w in omega.items() if e not in boundary)>0
    return dict(G=edges,rotation=rot,outer_nodes=cy,outer_primal_id=outer,boundary=sorted(boundary),omega=[[u,v,w] for (u,v),w in sorted(omega.items())],xy_boundary=cap[cy,:2].tolist(),lam=lam.tolist(),linear=linear.tolist(),beta=beta.tolist(),height_sign=sgn,original_q=q.tolist(),original_P=P.tolist(),original_cap=cap.tolist(),schlegel_d=d,origin_weights_gamma=gamma.tolist(),exact_parent=name)

def dynamicstate(body,theta,jac=True):
    st=body.fullstate(theta,jac=False,roots=False);body.sparent=st['cs'].argmax(1);body.uparent=st['cu'].argmax(1)
    return body.fullstate(theta,jac=jac)

def close_edge(body,edge,steps=300,keep=8e-6,maxtrust=.08):
    theta=np.zeros(body.K);k=body.free_edges.index(edge);trust=.005;t0=time.time();best=theta.copy();st=dynamicstate(body,theta);assert st['vals'].min()>0
    for it in range(steps):
        st=dynamicstate(body,theta);vals=st['vals'];J=st['J'];objective=theta[k]
        if it%10==0:print('REMOVE',edge,it,'sec',round(time.time()-t0,2),'logw',objective,'cos',vals.min(),'gap',st['gaps'][~body.inc].min(),'trust',trust,flush=True)
        if objective<-15:return theta,'weight_small'
        # All nonroot vertices must retain a strictly positive physical escape.
        obj=np.zeros(body.K);obj[k]=1.;A=-J;b=vals-keep;sc=np.maximum(np.linalg.norm(A,axis=1),1e-3)
        lp=linprog(obj,A_ub=A/sc[:,None],b_ub=b/sc,bounds=[(-trust,trust)]*body.K,method='highs',options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
        if not lp.success:
            trust*=.4
            if trust<1e-8:return theta,'lp_stall'
            continue
        direction=lp.x;prediction=-direction[k]
        if prediction<1e-10:return theta,'blocked'
        accept=False
        for ls in range(24):
            alpha=2.**(-ls);nt=theta+alpha*direction
            try:ns=body.fullstate(nt,jac=False);newcos=ns['vals'].min()
            except Exception:continue
            if newcos>keep*.75 and ns['gaps'][~body.inc].min()>-1e-8 and ns['det'].min()>-1e-10 and ns['V']>0:
                theta=nt;accept=True
                trust=min(maxtrust,trust*(1.4 if ls==0 else 1.1 if ls<3 else .6))
                break
        if not accept:
            trust*=.4
            if trust<1e-8:return theta,'line_stall'
    return theta,'budget'

def reduced(body,theta,edge):
    st=body.fullstate(theta,jac=False);ref=json.loads(json.dumps(body.ref));ref['omega']=[[u,v,float(w)] for (u,v),w in zip(body.free_edges,body.w0*np.exp(theta[:body.W]))]+[[u,v,0.] for u,v in body.bedges]
    ref['lam']=st['lam'].tolist()
    mt=theta[body.W+3:];T=np.array([[np.exp(mt[0]),0,0],[mt[3],np.exp(mt[1]),0],[mt[4],mt[5],np.exp(mt[2])]])
    ref['linear']=(body.linear@T).tolist()
    ee=[e for e in body.edges if e!=edge];new=TutteBody(ref,ee);s=new.state(new.log0)
    return ref,new,s

if __name__=='__main__':
    R=Path(__file__).parent;name=sys.argv[1] if len(sys.argv)>1 else 'C642_CONTACT26_82';ref=ref_exact(R,name);(R/(name+'_TUTTE_REFERENCE.json')).write_text(json.dumps(ref,separators=(',',':')))
    body=PhysicalTutte(ref,ref['G']);body.setup(stable=3,unstable=2);zero=np.zeros(body.K);st=dynamicstate(body,zero);rr=body.census(zero);print('BEGIN',name,rr,'root',body.uroot,'mincos',st['vals'].min(),flush=True)
    # Correct the root deterministically using the actual apex owner cycle.
    apex=[i for i,c in enumerate(body.faces) if len(c)==44];assert len(apex)==1;body.uroot=apex[0];body.ui=np.array([i for i in range(len(body.faces)) if i!=body.uroot]);st=dynamicstate(body,zero);assert body.census(zero)['counts']==[1,1,0] and st['vals'].min()>0
    H=set(tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines());candidate=[]
    for e in body.free_edges:
        if e in H:continue
        try:
            fs,rt,df=embedded_faces([t for t in body.edges if t!=e],{int(k):v for k,v in ref['rotation'].items()})
            if min(map(len,rt.values()))<3 or len(fs)!=len(body.faces)-1:continue
            f,g=body.df[e],body.df[e[::-1]];length=np.linalg.norm(st['P'][f]-st['P'][g]);candidate.append((length,e))
        except Exception:continue
    candidate.sort();print('CANDIDATES',candidate[:20],flush=True)
    ledger=[]
    for rank,(length,edge) in enumerate(candidate[:12]):
        theta,status=close_edge(body,edge,steps=260)
        nf,new,nst=reduced(body,theta,edge);rr=nst['audit'];prefix=name+f'_SPRING_{edge[0]}_{edge[1]}'
        np.savez(R/(prefix+'.npz'),theta=theta,q=nst['q'],P=nst['P']);(R/(prefix+'_REFERENCE.json')).write_text(json.dumps(nf,separators=(',',':')));(R/(prefix+'_faces.json')).write_text(json.dumps(new.primal_faces,separators=(',',':')));(R/(prefix+'_numeric.json')).write_text(json.dumps(rr,indent=2))
        ledger.append(dict(edge=edge,status=status,logweight=float(theta[body.free_edges.index(edge)]),audit=rr));(R/(name+'_SPRING_LEDGER.json')).write_text(json.dumps(ledger,indent=2))
        print('REMOVAL_END',edge,status,rr,flush=True)
        if rr['counts']==[1,1,0] and rr['min_gap']>1e-8 and rr['max_incidence_error']<1e-7:
            print('SPRING_COARSEN_WINNER',prefix,flush=True);break
