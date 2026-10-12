"""Lead continuation from exact C820. Numerical discovery, never exact acceptance.
Every finite trial rebuilds both dual hull and ordinary volume centroid.
The exact selected output must be independently audited from rational input.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import argparse,itertools,json,time,sys
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix,eye,hstack,vstack
from geometry import geom,brief,escape_grad
from forest_search import widest

ERR=(ValueError,AssertionError,np.linalg.LinAlgError)

def data(G,root=3,der=True):
    vr=G['source'].index(('root',))
    ui=np.array([i for i in range(G['V']) if i!=vr])
    si=G['active'][G['active']!=root]
    if root not in G['faces']:raise ValueError('stable root disappeared')
    pu,cu=widest(G['A_U'],vr)
    ps,cs=widest(G['A_S'],root,G['active'])
    v=np.r_[G['A_U'][ui,pu[ui]],G['A_S'][si,ps[si]]]
    J=np.vstack([escape_grad(G['Y'],G['JY'],pu,ui),escape_grad(G['Z'],G['JZ'],ps,si)]) if der else None
    return v,J

def checkpoint(q,labels,path,**kw):
    G=geom(q);b=brief(G)
    b.update(q_hex=[[float(x).hex() for x in row] for row in q],original_rows=list(map(int,labels)),minimum=float(data(G,labels.index(3),False)[0].min()),**kw)
    Path(path).write_text(json.dumps(b,separators=(',',':'),default=lambda x:x.item() if hasattr(x,'item') else list(x)))
    return b

def load(path):
    p=json.loads(Path(path).read_text())
    if 'I' in p:return np.array(p['I'],dtype=float)/p['D'],list(range(len(p['I'])))
    return np.array([[float.fromhex(x) for x in a] for a in p['q_hex']]),p['original_rows']

