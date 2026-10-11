import json
import numpy as np
from rational56 import points
from atlas_opt import Atlas
def enc(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def model(d,fs):
 z=json.loads(json.dumps(d));X=np.array(points(d),float);z['controls']=X.tolist();z['grid']=1;return Atlas(z,fs)
def freeze(m,u,grid=10**12):
 z=json.loads(json.dumps(m.data));X=m.chart(u,False);z.pop('denominators',None);z['grid']=grid;z['controls']=np.rint(X*grid).astype(np.int64).tolist();return z
