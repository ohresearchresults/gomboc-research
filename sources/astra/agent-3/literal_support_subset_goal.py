"""Literal rational facet deletions from an owned exact monostable body.

All support coefficients are unchanged exact rationals. Known nonsimple source
vertices are preserved through exact incidence; new intersections are grouped
by exact rational coordinates, never tolerance. Numerical full mass and census
screen the new bodies. Every under-bound own110 is audited by the native exact
half-space checker, including the true maximal-facet incidence and weak contacts.
"""
import argparse,json,hashlib,time,itertools
from pathlib import Path
from math import gcd,lcm
import numpy as np
from gmpy2 import mpq
from scipy.spatial import ConvexHull
from exact_projective_audit import inverse,apply
from exact_audit_vertices import check_B,dot
from support_geometry import escape
from persistence_birth import bars_loss
from goal_nomination import ExactGoalCandidateFound

class Source:
    def __init__(self,path):
        self.path=Path(path);self.a=json.loads(self.path.read_text());a=self.a;self.n=a['F'];self.Q=[];self.rows=[];self.cache={}
        for n,h in zip(a['normals'],a['offsets']):
            nn=tuple(map(mpq,n));hh=mpq(h);assert hh>0
            self.Q.append(tuple(v/hh for v in nn));rr=(*nn,hh);D=lcm(*(int(x.denominator)for x in rr));ii=tuple(int(x*D)for x in rr);gg=gcd(*ii);self.rows.append(tuple(x//gg for x in ii))
        self.Qf=np.array(self.Q,float);inc=[[]for _ in range(a['V'])]
        for f,cy in enumerate(a['faces']):
            for v in cy:inc[v].append(f)
        for v,faces in enumerate(inc):
            p=tuple(map(mpq,a['raw_vertices'][v]))
            for tri in itertools.combinations(sorted(faces),3):self.cache[tri]=(p,frozenset())

    def point(self,tri):
        tri=tuple(sorted(tri))
        if tri not in self.cache:
            p=tuple(apply(inverse([self.Q[i]for i in tri]),[mpq(1)]*3));bad=frozenset(i for i,q in enumerate(self.Q)if dot(q,p)>1);self.cache[tri]=(p,bad)
        return self.cache[tri]

    def geometry(self,ids):
        ids=list(ids);kept=frozenset(ids);hull=ConvexHull(self.Qf[ids])
        if max(hull.equations[:,3])>=0:raise ValueError('subset normal hull excludes origin; unbounded body')
        if len(hull.vertices)!=len(ids):raise ValueError('numerical normal hull dropped a retained exact extreme point')
        T=hull.simplices;pts=[];lookup={};tri2=[]
        for tri in T:
            p,bad=self.point([ids[int(i)]for i in tri])
            if bad&kept:raise ValueError('nominated new intersection violates a retained exact plane')
            if p not in lookup:lookup[p]=len(pts);pts.append(p)
            tri2.append(lookup[p])
        X=np.array(pts,float);faces=[];Q=self.Qf[ids];pe={}
        for f in range(len(ids)):
            incident=np.flatnonzero(np.any(T==f,axis=1));start=int(incident[0]);prev=-1;cur=start;cycle=[]
            while True:
                v=tri2[cur]
                if not cycle or v!=cycle[-1]:cycle.append(v)
                loc=np.flatnonzero(T[cur]==f)[0];links=[int(hull.neighbors[cur,k])for k in range(3)if k!=loc];nxt=links[0]if links[0]!=prev else links[1]
                if nxt==start:break
                prev,cur=cur,nxt
            if len(cycle)>1 and cycle[0]==cycle[-1]:cycle.pop()
            if len(cycle)<3 or len(set(cycle))!=len(cycle):raise ValueError('exactly grouped facet boundary is invalid')
            p=X[cycle];area=np.sum(np.cross(p,np.roll(p,-1,axis=0)),axis=0)
            if area@Q[f]<0:cycle.reverse()
            faces.append(cycle)
            for a,b in zip(cycle,cycle[1:]+cycle[:1]):pe.setdefault(tuple(sorted((a,b))),[]).append(f)
        if not all(len(fs)==2 for fs in pe.values())or len(X)-len(pe)+len(faces)!=2:raise ValueError('grouped exact-incidence hull failed manifold/Euler check')
        TT=np.array([(cy[0],cy[k],cy[k+1])for cy in faces for k in range(1,len(cy)-1)]);a,b,c=X[TT[:,0]],X[TT[:,1]],X[TT[:,2]];v6=np.einsum('ic,ic->i',a,np.cross(b,c));volume=v6.sum()/6;g=np.sum(v6[:,None]*(a+b+c),axis=0)/(4*v6.sum());Z=X-g;H=Q/(1-Q@g)[:,None]
        vp,_=escape(Z);vf,_=escape(H);_,_,P=bars_loss(Z,np.array(list(pe)),.01);_,_,Qbars=bars_loss(H,np.array(list(pe.values())),.01)
        return dict(X=X,Z=Z,H=H,g=g,volume=volume,V=len(X),E=len(pe),F=len(ids),S=int(sum(vf<0)),U=int(sum(vp<0)),Pmax=max(P,default=0.),Qmax=max(Qbars,default=0.),P=P,Qbars=Qbars,faces=faces,edges=list(pe),exact_points=pts)

    def freeze(self,ids,out,reason):
        out=Path(out);out.mkdir(parents=True,exist_ok=False);raw=dict(H=[self.rows[i]for i in ids]);enc=lambda x:json.dumps(x,default=str,sort_keys=True,separators=(',',':')).encode();(out/'raw.json').write_bytes(enc(raw));(out/'definition.json').write_bytes(enc(dict(source_audit=str(self.path.resolve()),source_sha256=hashlib.sha256(self.path.read_bytes()).hexdigest(),retained_source_face_ids=list(ids),density=1,reason=reason,scope='literal unchanged exact halfspace subset; uniform mass of this same intersection')));a=check_B.run(raw);(out/'audit.json').write_bytes(enc(a));s={k:a[k]for k in ['V','E','F','counts','weak','face_primitive_zero_count','vertex_max_zero_count','edge_primitive_zero_count']};s.update(C_2E=2*a['E'],VplusEplusF=a['V']+a['E']+a['F'],audit_sha256=hashlib.sha256((out/'audit.json').read_bytes()).hexdigest());s['goal_met']=a['counts']==[1,1,0]and a['weak']==[0,0,0]and 34<=2*a['E']<500 and s['VplusEplusF']<500;(out/'summary.json').write_text(json.dumps(s,indent=2));print('LITERAL_SUPPORT_EXACT',s,flush=True)
        if s['goal_met']:raise ExactGoalCandidateFound('Exact literal-support subset Figure '+str(out))

def run(source,out,depth,width):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);F=Source(source);ids=tuple(range(F.n));g=F.geometry(ids);a=F.a;assert(g['V'],g['E'],g['F'],g['S'],g['U'])==(a['V'],a['E'],a['F'],a['counts'][0],a['counts'][1]),'source full-incidence numeric replay failed';(out/'source_check.json').write_text(json.dumps({k:g[k]for k in ['V','E','F','S','U','Pmax','Qmax','volume']},indent=2));beam=[(ids,g)];history=[];seen={ids};start=time.time();serial=0
    for level in range(depth):
        pool=[]
        for parent,(ids,g)in enumerate(beam):
            for i in ids:
                ss=tuple(j for j in ids if j!=i)
                if ss in seen:continue
                seen.add(ss);serial+=1
                try:gg=F.geometry(ss)
                except(ValueError,np.linalg.LinAlgError,ZeroDivisionError):continue
                row=dict(serial=serial,parent=parent,removed=i,retained=list(ss),**{k:gg[k]for k in ['V','E','F','S','U','Pmax','Qmax','volume']})
                if gg['S']==gg['U']==1 and 17<=gg['E']<=248 and gg['V']+gg['E']+gg['F']<500:F.freeze(ss,out/f'exact_goal_{serial:07d}','actual uniform-centroid numerical110 after literal support deletion')
                score=gg['Pmax']+gg['Qmax']+1e-7*(gg['S']+gg['U']);pool.append((score,ss,gg,row))
        if not pool:print('LITERAL_SUPPORT_NO_NEXT_BODY',level,serial,flush=True);break
        pool.sort(key=lambda r:r[0]);beam=[]
        for _,ss,gg,row in pool[:width]:
            beam.append((ss,gg));d=out/f'level{level:03d}_beam{len(beam)-1:02d}';d.mkdir();(d/'subset.json').write_text(json.dumps(row,indent=2));np.save(d/'physical_vertices.npy',gg['X']);np.save(d/'supports.npy',F.Qf[list(ss)])
        row=dict(level=level,trials=serial,best=pool[0][3],cache_size=len(F.cache),seconds=time.time()-start);history.append(row);(out/'history.json').write_text(json.dumps(history,indent=2));print('LITERAL_SUPPORT_GOAL',row,flush=True)
    print('LITERAL_SUPPORT_FINITE_STOP',serial,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--depth',type=int,default=84);p.add_argument('--width',type=int,default=3);a=p.parse_args();run(a.source,a.out,a.depth,a.width)
