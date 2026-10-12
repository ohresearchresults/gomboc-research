"""Exact source patch of the supplied numerical Atlas: keep a specified
reference point for mechanical discovery, but retain actual filled V and M.
This is not homogeneous certification; actual mass closure is separate.
"""
from pathlib import Path
import sys
import numpy as np
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'parent/mechanism/parent_sources'))
s=(R/'parent/mechanism/parent_sources/atlas_opt.py').read_text()
if '\ndef optimize(' in s:s=s[:s.index('\ndef optimize(')]
assert s.count('cent=M/V')==1 and s.count('dcent=(dM-cent[:,None]*dV[None,:])/V')==1
s=s.replace('class Atlas:', 'class ReferenceAtlas:').replace('cent=M/V', 'cent=self.reference').replace('dcent=(dM-cent[:,None]*dV[None,:])/V','dcent=np.zeros((3,self.np))')
exec(compile(s,'<REFERENCE_ATLAS_PATCH>','exec'))
from atlas_opt import Atlas
Old=ReferenceAtlas.__init__
def init(self,data,faces,stable=3,unstable=None):
 Old(self,data,faces,stable,unstable)
 origin=Atlas(data,faces,stable,unstable);self.reference=origin.state(origin.u0,False)['c'].copy()
ReferenceAtlas.__init__=init
