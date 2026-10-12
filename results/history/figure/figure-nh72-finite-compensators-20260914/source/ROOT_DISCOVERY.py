"""High-precision proposal of cap parameters; exact acceptance is ROOT_VERIFY.py."""
import sys,json
from pathlib import Path
from fractions import Fraction as Q
import mpmath as mp
import BUILD
mp.mp.dps=80
sys.set_int_max_str_digits(0)
def to_mp(x):x=Q(x);return mp.mpf(x.numerator)/x.denominator
out={}
for case,guess in [('PAIR99',[-.2508314428454454,.024242076847475633,.008575325279432193]),('TRIPLE117',[-.030567244989715078,.0351207386308224,.01682259889680614])]:
 j=BUILD.CASES[case]['deleted_support'];base=json.loads(Path(sys.argv[1],f'DEL{j}','B.json').read_text());P,keep,faces,labels,beta=BUILD.setup(base,case);c=[to_mp(x) for x in base['raw_centroid']];X=[tuple(map(to_mp,p)) for p in P];B={key:tuple(map(to_mp,row)) for key,row in beta.items()};tri=[(cy[0],cy[k],cy[k+1]) for cy in faces for k in range(1,len(cy)-1)]
 def fun(*eta):
  Y=X.copy()
  for ci,cap in enumerate(BUILD.CASES[case]['caps']):
   for i in cap['vertices']:
    d=mp.mpf(1);num=list(X[i])
    for k,(cc,l) in enumerate(BUILD.SELECT):
     if cc==ci:
      z=eta[k]*B[ci,i][l];d+=z
      for axis in range(3):num[axis]+=z*X[cap['boundary'][l]][axis]
    Y[i]=tuple(x/d for x in num)
  V=mp.mpf(0);M=[mp.mpf(0)]*3
  for i,j,k in tri:
   a,b,z=Y[i],Y[j],Y[k];v=BUILD.det(a,b,z)/6;V+=v
   for axis in range(3):M[axis]+=v*(a[axis]+b[axis]+z[axis])/4
  return tuple(M[i]-c[i]*V for i in range(3))
 rr=mp.findroot(fun,tuple(guess),tol=mp.mpf('1e-70'),maxsteps=30)
 nums=[int(mp.nint(z*(1<<120))) for z in rr]
 residual=max(abs(x) for x in fun(*(mp.mpf(v)/(1<<120) for v in nums)))
 record=dict(centre_bits=120,eta_numerators=nums,radius_bits=100)
 out[case]=record;print(case,list(map(str,rr)),'residual',residual,flush=True)
Path(sys.argv[2]).write_text(json.dumps(out,sort_keys=True,separators=(',',':')))
