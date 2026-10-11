"""Piecewise quadratic horizontal sections and their exact-form integrals.
Coefficients are floating point search data. Final hull moments are computed
independently; this module is not an exact rational certificate.
"""
import numpy as np


class SlabMass:
    def __init__(self,mesh):
        X=mesh['X'];edges=mesh['edges'];raw=np.sort(X[:,2]);scale=max(float(np.ptp(raw)),1.)
        groups=[]
        for z in raw:
            if not groups or z-groups[-1][-1]>1e-12*scale:groups.append([z])
            else:groups[-1].append(z)
        self.knots=np.array([np.mean(g) for g in groups]);self.rows=[]
        aa=X[edges[:,0]];bb=X[edges[:,1]];lo=np.minimum(aa[:,2],bb[:,2]);hi=np.maximum(aa[:,2],bb[:,2])
        for low,high in zip(self.knots[:-1],self.knots[1:]):
            mid=(low+high)/2;active=(lo<mid)&(hi>mid);a=aa[active];b=bb[active]
            if len(a)<3:raise ValueError('Horizontal section lacks three crossing edges')
            slope=(b[:,:2]-a[:,:2])/(b[:,2]-a[:,2])[:,None]
            p=a[:,:2]+(mid-a[:,2])[:,None]*slope;centre=p.mean(0)
            order=np.argsort(np.arctan2(p[:,1]-centre[1],p[:,0]-centre[0]));p=p[order];slope=slope[order]
            nxt=np.roll(p,-1,axis=0);dn=np.roll(slope,-1,axis=0)
            cross=lambda a,b:a[:,0]*b[:,1]-a[:,1]*b[:,0]
            c0=float(cross(p,nxt).sum()/2);c1=float((cross(p,dn)+cross(slope,nxt)).sum()/2);c2=float(cross(slope,dn).sum()/2)
            if c0<=0:raise ValueError('Horizontal section has nonpositive orientation')
            width=high-low;volume=c0*width+c2*width**3/12;moment=mid*volume+c1*width**3/12
            self.rows.append((mid,c0,c1,c2,volume,moment))
        self.rows=np.array(self.rows);self.Vsuffix=np.r_[np.cumsum(self.rows[::-1,4])[::-1],0.]
        self.Msuffix=np.r_[np.cumsum(self.rows[::-1,5])[::-1],0.]
        if abs(self.Vsuffix[0]-mesh['volume'])>1e-8*mesh['volume']:raise ValueError('Slab volume disagrees with oriented boundary integration')
        if abs(self.Msuffix[0]/self.Vsuffix[0]-mesh['g'][2])>1e-8*scale:raise ValueError('Slab first moment disagrees with boundary integration')

    def above(self,z):
        if z<=self.knots[0]:return float(self.Vsuffix[0]),float(self.Msuffix[0])
        if z>=self.knots[-1]:raise ValueError('Empty upper slice')
        k=int(np.searchsorted(self.knots,z,side='right')-1);low=z;high=self.knots[k+1]
        mid,c0,c1,c2,_,_=self.rows[k];newmid=(low+high)/2;d=newmid-mid
        a0=c0+c1*d+c2*d*d;a1=c1+2*c2*d;width=high-low
        v=a0*width+c2*width**3/12;moment=newmid*v+a1*width**3/12
        return float(v+self.Vsuffix[k+1]),float(moment+self.Msuffix[k+1])

    def centroid(self,height):
        v,m=self.above(-height);return m/v
