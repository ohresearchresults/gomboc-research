"""A full C598 radial atlas ordered by the literal ancestor's sparse dependencies.
Priority is only an algebraic-complexity choice, not a new contact constraint.
"""
import json,itertools,time,argparse,os
from pathlib import Path
from model import Model,HERE
from rechart import atlas
import radial,numpy as np

def prepare(tag,start):
 M=Model();z=M.z0 if start is None else np.load(start)[:M.D];R=M.evaluate(z);G0=json.load(open(HERE/'core/BQ13_C602.json'));P0=np.array([[float(__import__('fractions').Fraction(x)) for x in row] for row in json.load(open(HERE/'seed/PARENT_A.json'))['raw_vertices']]);X=atlas(G0);owner={int(np.argmin(np.linalg.norm(P0-p,axis=1))):136+k for k,p in enumerate(X[136:])};ranks={i:k for k,(i,ds,ax) in enumerate(G0['plan'])};ranks[136]=-1
 perm=[M.root]+[i for i in range(len(M.labels)) if i!=M.root];pri=[]
 for k,sel in enumerate(M.meta['selectors']):pri.append(ranks[sel['old']] if 'old' in sel else 3000+k)
 for i in perm:
  label=int(M.labels[i]);pri.append(ranks[owner[label]] if label in owner else (1000+label if label<167 else 2000+label))
 G=radial.make(R['P'],R['q'],M.F,M.root,10**12,pri);G['priority']=pri;G['parent_labels']=[int(M.labels[i]) for i in perm]
 (HERE/(tag+'.json')).write_text(json.dumps(G,sort_keys=True,separators=(',',':')));t=time.time();raw,P=radial.reconstruct(G);(HERE/(tag+'_raw.json')).write_text(json.dumps(raw,sort_keys=True,separators=(',',':')))
 print('RADIAL_SPARSE',time.time()-t,'nodes',len(G['controls']),'free',sum(3-len(x[1]) for x in G['plan']),'Hbits',max(abs(x).bit_length() for r in raw['H'] for x in r),'Pbits',max(max(x.numerator.bit_length(),x.denominator.bit_length()) for p in P for x in p),flush=True)
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('tag');a.add_argument('--start');v=a.parse_args();prepare(v.tag,v.start)
