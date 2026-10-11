"""Complete finite initial local-contraction screen without unused Jacobian work."""
from LOCAL_UNION import *
from contact import contact

def values(s,Y):
 coords=np.array([Y[i,a] for i,a in s.free]);YY,_=contact(s.G,coords,s.free,False);Q=YY[:s.nq];X=np.empty((s.nv,3));ix=s.direct>=0;X[ix]=YY[s.direct[ix]];X[s.simple]=np.linalg.solve(Q[s.trip],np.ones((len(s.simple),3,1)))[:,:,0];tr=X[s.tris];v6=np.einsum('ic,ic->i',tr[:,0],np.cross(tr[:,1],tr[:,2]));V=v6.sum()/6;g=(v6[:,None]*tr.sum(1)).sum(0)/(24*V);sl=np.where(s.mask,1-Q@X.T,np.inf);az=arrows(X-g);h=1-Q@g;aq=arrows(Q/h[:,None]);ep=az.max(1);eq=aq.max(1);dynamic=min(ep[s.keptp].min(),eq[s.keptq].min());fp=min(az[i,j] for i,j in s.forcedp.items());return dict(dynamic_mech=float(dynamic),inherited_primal=float(min(fp,eq[s.keptq].min())),slack=float(sl.min()),det=float(v6.min()),minimum_centred_offset=float(h.min()))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--chart',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();c=Chart(a.chart);rep=json.load(open(a.chart/'baseline/A.json'));rows=[];oldX=c.X
 for k,pair in enumerate(c.edges.tolist()):
  if c.w[k]<=0 or min(len(rep['faces'][q]) for q in pair)<=3:continue
  try:
   s,nr,patch,Y0=make_local(c,rep,pair,F(1,2));s.forcedp,mp,ch=inherited(rep,s.owners);node=s.G['n_supports']+s.G['groups'].index(patch['child_group']);u,v=patch['parent_vertex_indices']
   for lam in [F(t,10) for t in range(11)]:
    Y=Y0.copy();Y[node]=(1-float(lam))*oldX[u]+float(lam)*oldX[v];row=values(s,Y);row.update(pair=pair,lam=str(lam),union=patch['child_group']);rows.append(row)
  except (AssertionError,ValueError,np.linalg.LinAlgError,ZeroDivisionError) as e:rows.append(dict(pair=pair,error=str(e)))
  a.out.write_bytes(B(rows));good=[t for t in rows[-11:] if t.get('slack',-1)>1e-9 and t.get('det',-1)>0];print('FAST_LOCAL_SCREEN',k,sorted(good,key=lambda t:t['dynamic_mech'],reverse=True)[:1],flush=True)
 good=[t for t in rows if t.get('slack',-1)>1e-9 and t.get('det',-1)>0];print('FAST_FINAL_RANK',json.dumps(sorted(good,key=lambda t:t['dynamic_mech'],reverse=True)[:30],indent=2),flush=True)
if __name__=='__main__':main()
