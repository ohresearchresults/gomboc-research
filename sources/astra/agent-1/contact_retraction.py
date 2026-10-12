"""Orthogonal numerical retraction of a physical tangent step onto incidences.

Newton corrections act on all primal/polar coordinates. Only after convergence
are chart free coordinates extracted and all contacts rebuilt from the literal
chart. This is a search parametrization; exact acceptance still uses the rational
free-control construction and a complete own-mass audit.
"""
import numpy as np
from scipy.linalg import lstsq

def retract(model,e,dz,alpha=1.,iterations=8):
    F=model.F;n=model.n
    dA=np.einsum('ikp,p->ik',e['DA'],dz)*alpha
    A=e['A']+dA
    fi,vi=np.where(model.inc);vi=vi+F;rows=np.arange(len(fi))
    scale=np.r_[np.full(F,np.sqrt(np.mean(e['Y']**2))),np.full(n-F,np.sqrt(np.mean(e['P']**2)))]
    initial_error=float(np.max(abs(np.einsum('ij,ij->i',A[fi],A[vi])-1)))
    history=[]
    for k in range(iterations):
        residual=np.einsum('ij,ij->i',A[fi],A[vi])-1
        err=float(np.max(abs(residual)));history.append(err)
        if err<3e-15:break
        J=np.zeros((len(fi),3*n))
        for c in range(3):
            J[rows,3*fi+c]=A[vi,c]*scale[fi]
            J[rows,3*vi+c]=A[fi,c]*scale[vi]
        dx,res,rank,s=lstsq(J,-residual,cond=1e-12,lapack_driver='gelsy',check_finite=False)
        if rank<len(fi):raise ValueError('contact projection derivative lacks full row rank')
        step=dx.reshape(n,3)*scale[:,None]
        accepted=False
        for level in range(10):
            B=A+step*2**-level
            rr=np.einsum('ij,ij->i',B[fi],B[vi])-1
            if np.linalg.norm(rr)<np.linalg.norm(residual):
                A=B;accepted=True;break
        if not accepted:break
    residual=np.einsum('ij,ij->i',A[fi],A[vi])-1
    if np.max(abs(residual))>1e-12:raise ValueError('full-coordinate contact projection did not close')
    z=model.encode(A)
    final=model.evaluate(z,False)
    displacement=float(np.linalg.norm((final['A']-e['A'])/scale[:,None]))
    correction=float(np.linalg.norm((final['A']-(e['A']+dA))/scale[:,None]))
    return z,final,dict(initial_contact_error=initial_error,newton_errors=history,physical_step=displacement,physical_correction=correction)
