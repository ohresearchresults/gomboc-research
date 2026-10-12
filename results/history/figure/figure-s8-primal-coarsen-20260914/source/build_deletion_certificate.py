"""Propose all S8 one-/two-vertex deletion hulls; proof is verify_deletions.py.
Usage: python build_deletion_certificate.py S8_RAW_COMPLEX CERT.json
SciPy/Qhull is only used to propose facets, never as the verifier.
"""
from pathlib import Path
from itertools import combinations
import json,sys,hashlib,time
import numpy as np
from deletion import Model,canon
rawbytes=Path(sys.argv[1]).read_bytes();raw=json.loads(rawbytes);m=Model(raw);orig=set(m.originalplanes.values());catalog={};cases=[];beg=time.monotonic()
for deleted in [(i,)for i in range(len(m.X))]+list(combinations(range(len(m.X)),2)):
 keep,faces,H,ef=m.hull(set(deleted));extra=[]
 for h,cy in zip(H,faces):
  if h not in orig:
   extra.append(h)
   if h not in catalog:
    zeros=[i for i,p in enumerate(m.hom)if sum(h[j]*p[j]for j in range(3))==h[3]*p[3]]
    triple=next(t for t in combinations(zeros,3)if m.plane(t)==h);catalog[h]=list(triple)
 C=2*len(ef);witness=[]
 if C<624:
  P=m.X[keep];tri=np.array([(cy[0],cy[j],cy[j+1])for cy in faces for j in range(1,len(cy)-1)]);a,b,c=[P[tri[:,k]]for k in range(3)];d=np.einsum('ij,ij->i',a,np.cross(b,c));V=d.sum()/6;g=np.einsum('t,tc->c',d,a+b+c)/(24*V);z=P-g
  ua=z@z.T-(z*z).sum(1)[:,None];np.fill_diagonal(ua,-np.inf);mx=ua.max(1);order=np.argsort(mx,kind='stable');assert mx[order[1]]<0
  witness=[int(keep[j])for j in order[:2]]
 cases.append([list(deleted),extra,witness])
 if len(cases)%1000==0:print('PROPOSED',len(cases),'catalog',len(catalog),'seconds',round(time.monotonic()-beg,2),flush=True)
keys=sorted(catalog);index={h:i for i,h in enumerate(keys)}
cert=dict(version=1,object='S8_FIXED_COORDINATE_ALL_ONE_TWO_VERTEX_DELETIONS',parent_sha256=hashlib.sha256(rawbytes).hexdigest(),precision_bits=128,new_planes=[catalog[h]for h in keys],cases=[[ds,sorted(index[h]for h in hs),w]for ds,hs,w in cases])
b=canon(cert).encode();Path(sys.argv[2]).write_bytes(b);print('ALL_DELETION_CERTIFICATE_PROPOSED',len(cases),len(keys),len(b),hashlib.sha256(b).hexdigest(),flush=True)
