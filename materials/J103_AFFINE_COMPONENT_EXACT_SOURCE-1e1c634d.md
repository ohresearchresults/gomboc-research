# material-1e1c634dba92

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

#!/usr/bin/env python3
"""Exact finite affine witness-cone obstruction for KF27D_QCANCEL_ROBUST_G4.
No floating inequality determines a certified sign. LP data nominate five rows
for each dual certificate; their rational equations and signs are checked here.
"""
import sys,json,hashlib,itertools,math,time
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
sys.set_int_max_str_digits(0)

EXPECTED='52a71e8f9dbfe781d3a0aeafe053045e7cedb2fa588661f822d05990c5a86421'
INPUT=Path(__file__).with_name('KF27D_QCANCEL_ROBUST_G4.txt')
INPUT_TEXT='49 10000\n-5079 13732 9267\n-14396 11026 -3218\n-12466 13017 -2373\n-10223 14660 -1659\n-12371 13207 485\n-5511 15313 6055\n-8438 14243 6102\n-6944 14003 7847\n-2416 17109 -242\n-5135 16720 -706\n-3100 13245 10467\n-7743 15902 -1141\n5950 3897 -9129\n7859 14371 112\n7631 1392 -8083\n-7105 -20060 -8288\n3029 16527 756\n10270 12338 -490\n5553 15635 147\n13447 -12400 4798\n10989 9339 -4734\n8969 11100 5188\n-1080 12497 11470\n5972 13236 -6394\n3314 -20677 -1248\n2405 11856 11399\n2827 16105 -3395\n-1372 -21226 -4632\n337 17042 309\n6856 -18977 2259\n8235 -11672 11211\n-1912 9348 13526\n3963 10154 12299\n6264 11222 9621\n-48 16910 -1981\n9667 -16286 5360\n13499 -8728 8488\n-9829 14213 4254\n-11155 13859 2378\n-13471 12248 -1382\n-15456 9243 -4601\n-16262 7227 -5952\n-16803 4959 -7230\n-17054 2425 -8392\n-16933 -367 -9448\n-16470 -4196 -10134\n-15277 -8346 -10358\n-12715 -13423 -10051\n2909 -2 -9206\n'
if not INPUT.exists():
    INPUT.write_text(INPUT_TEXT,encoding='utf-8')
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def coeff(a,b):return (a[0]*b[0],a[1]*b[1],a[2]*b[2],a[0]*b[1]+a[1]*b[0],a[0]*b[2]+a[2]*b[0],a[1]*b[2]+a[2]*b[1])
def solve(A,b):
    n=len(b);M=[[F(x) for x in row]+[F(y)] for row,y in zip(A,b)]
    for k in range(n):
        i=next(i for i in range(k,n) if M[i][k]);M[k],M[i]=M[i],M[k]
        p=M[k][k];M[k]=[x/p for x in M[k]]
        for i in range(n):
            if i!=k:
                p=M[i][k]
                if p:M[i]=[x-p*y for x,y in zip(M[i],M[k])]
    return [M[i][-1] for i in range(n)]
def fraction_record(q):return [str(q.numerator),str(q.denominator)]
def interval(q,D):return [str(q.numerator*D//q.denominator),str(q.numerator*D//q.denominator+1),str(D)]

def reconstruct():
    raw=INPUT.read_bytes();assert hashlib.sha256(raw).hexdigest()==EXPECTED
    lines=raw.decode().splitlines();n,D=map(int,lines[0].split());A=[tuple(map(int,l.split())) for l in lines[1:]];assert len(A)==n==49
    V=[];triples=[]
    for t in itertools.combinations(range(n),3):
        a,b,c=[A[i] for i in t];d=dot(a,cross(b,c))
        if not d:continue
        u,v,w=cross(b,c),cross(c,a),cross(a,b);N=tuple(D*(u[k]+v[k]+w[k]) for k in range(3))
        if d<0:d=-d;N=tuple(-x for x in N)
        if all(dot(row,N)<=D*d for row in A):
            x=tuple(F(z,d) for z in N)
            assert [i for i,row in enumerate(A) if dot(row,x)==D]==list(t)
            V.append(x);triples.append(t)
    assert len(V)==94 and len(set(V))==94
    # A fixed tetrahedron of input normals certifies boundedness; found below
    # by exact enumeration stopping at the first strictly positive dependence.
    bound=None
    for t in itertools.combinations(range(n),4):
        try:w=solve([[A[t[j]][k] for j in range(4)] for k in range(3)]+[[1]*4],[0,0,0,1])
        except StopIteration:continue
        if all(x>0 for x in w):bound=(t,w);break
    assert bound is not None
    faces=[];edge_count=Counter();vol=F(0);mom=[F(0)]*3
    for k,a in enumerate(A):
        ids=[i for i,t in enumerate(triples) if k in t]
        # Cyclic order follows the exactly reconstructed trivalent edge graph.
        nei={i:[j for j in ids if i!=j and len(set(triples[i])&set(triples[j]))==2] for i in ids}
        assert all(len(x)==2 for x in nei.values())
        cyc=[min(ids)];prev=None
        while True:
            nxt=next(j for j in sorted(nei[cyc[-1]]) if j!=prev)
            if nxt==cyc[0]:break
            assert nxt not in cyc;prev,cur=cyc[-1],nxt;cyc.append(cur)
        assert set(cyc)==set(ids)
        if dot(cross(sub(V[cyc[1]],V[cyc[0]]),sub(V[cyc[2]],V[cyc[0]])),a)<0:cyc=cyc[:1]+cyc[:0:-1]
        for i in range(len(cyc)):edge_count[tuple(sorted((cyc[i],cyc[(i+1)%len(cyc)])))]+=1
        faces.append(cyc)
        for j in range(1,len(cyc)-1):
            x,y,z=[V[i] for i in [cyc[0],cyc[j],cyc[j+1]]];vv=dot(x,cross(y,z))/6;assert vv>0
            vol+=vv
            for k in range(3):mom[k]+=vv*(x[k]+y[k]+z[k])/4
    assert len(edge_count)==141 and set(edge_count.values())=={2}
    g=tuple(m/vol for m in mom);den=math.lcm(*(x.denominator for x in g));gn=tuple(x.numerator*(den//x.denominator) for x in g)
    h=[D*den-dot(a,gn) for a in A];assert min(h)>0
    return A,D,V,triples,faces,sorted(edge_count),vol,g,den,h,bound

def main():
    A,D,V,tr,faces,edges,vol,g,den,h,bound=reconstruct();print('EXACT_BODY',len(V),len(edges),len(faces),'MASS_INTEGRATED',flush=True)
    # Only these finite nomination data are needed; never trust their values.
    nom={'root': 15, 'policy': [7, 40, 39, 2, 39, 6, 37, 6, 9, 11, 0, 3, 20, 18, 20, 27, 28, 13, 16, 35, 17, 33, 10, 26, 27, 22, 34, 15, 8, 24, 35, 22, 25, 25, 8, 29, 19, 38, 4, 1, 41, 42, 43, 44, 45, 46, 47, 15, 12], 'bounds': [{'k': 0, 'sign': 1, 'active': [3, 5, 35, 36, 40]}, {'k': 0, 'sign': -1, 'active': [5, 18, 32, 38, 40]}, {'k': 1, 'sign': 1, 'active': [18, 19, 36, 40, 46]}, {'k': 1, 'sign': -1, 'active': [5, 18, 24, 40, 44]}, {'k': 2, 'sign': 1, 'active': [5, 10, 18, 34, 40]}, {'k': 2, 'sign': -1, 'active': [9, 15, 17, 24, 33]}, {'k': 3, 'sign': 1, 'active': [15, 18, 22, 38, 40]}, {'k': 3, 'sign': -1, 'active': [5, 10, 18, 34, 40]}, {'k': 4, 'sign': 1, 'active': [23, 24, 26, 33, 35]}, {'k': 4, 'sign': -1, 'active': [5, 10, 18, 34, 40]}]}
    root=nom['root'];W=nom['policy'];assert root==15 and len(W)==49
    C=[];b=[];labels=[]
    for i,j in enumerate(W):
        if i==root:continue
        a=tuple(h[i]*x-h[j]*y for x,y in zip(coeff(A[i],A[j]),coeff(A[i],A[i])))
        gg=math.gcd(*a);a=tuple(x//gg for x in a)
        assert sum(a[:3])>0 # Exact feasibility at J=I/3.
        C.append((a[0]-a[2],a[1]-a[2],a[3],a[4],a[5]));b.append(a[2]);labels.append([i,j])
    boxes=[(F(3328,10000),F(3339,10000)),(F(3331,10000),F(3341,10000)),(F(-14,10000),F(2,10000)),(F(-4,10000),F(22,10000)),(F(-4,10000),F(19,10000))]
    polar_edges={tuple(sorted(t)) for triple in tr for t in itertools.combinations(triple,2)}
    adj={i:sorted({b if a==i else a for a,b in polar_edges if i in (a,b)}) for i in range(49)}
    positive={i:[j for j in adj[i] if dot(A[i],tuple(h[i]*A[j][k]-h[j]*A[i][k] for k in range(3)))>0] for i in range(49)}
    forced={i for i in range(49) if len(positive[i])==1};assert len(forced)==45
    assert not positive[root] and all(positive[i] for i in range(49) if i!=root)
    forced_labels=[[i,positive[i][0]] for i in sorted(forced)]
    assert all(labels[i][0] in forced for r in nom['bounds'] for i in r['active'])
    reports=[];proof=[]
    for r in nom['bounds']:
        k,s=r['k'],r['sign'];act=r['active'];assert len(act)==5 and max(act)<48
        lam=solve([[C[i][j] for i in act] for j in range(5)],[s if j==k else 0 for j in range(5)])
        assert min(lam)>=0
        assert all(sum(lam[z]*C[i][j] for z,i in enumerate(act))==(s if j==k else 0) for j in range(5))
        lower=-sum(lam[z]*b[i] for z,i in enumerate(act));target=boxes[k][0] if s==1 else -boxes[k][1]
        assert lower>target
        rec=dict(k=k,sign=s,active=act,witnesses=[labels[i] for i in act],bound=interval(s*lower,10**12),slack=interval(lower-target,10**15))
        reports.append(rec);proof.append(dict(k=k,sign=s,active=act,lambda_values=[fraction_record(x) for x in lam],bound=fraction_record(lower)))
        print('EXACT_CONE_BOUND',k,s,float(s*lower),flush=True)
    a=[max(abs(lo-F(1,3)),abs(hi-F(1,3))) if i<2 else max(abs(lo),abs(hi)) for i,(lo,hi) in enumerate(boxes)]
    # J22=1-J00-J11; this safe interval loses correlations deliberately.
    a22=max(abs(1-boxes[0][0]-boxes[1][0]-F(1,3)),abs(1-boxes[0][1]-boxes[1][1]-F(1,3)))
    E=[[a[0],a[2],a[3]],[a[2],a[1],a[4]],[a[3],a[4],a22]]
    delta=max(map(sum,E));assert delta<F(3,500)
    uroots=[tr.index((12,46,47)),tr.index((15,31,47))];rootchecks=[]
    for i in uroots:
        v=sub(V[i],g)
        for j in sorted({b if a==i else a for a,b in edges if i in (a,b)}):
            d=sub(V[j],V[i]);vd=dot(v,d);vv=dot(v,v);dd=dot(d,d)
            assert vd<0 and 400*vd*vd>vv*dd
            rootchecks.append(dict(vertex=i,neighbor=j,score=interval(vd,10**15),angular_square_gap=interval(400*vd*vd-vv*dd,10**15)))
    # ||J-I/3||_op < .006 implies ||J^-1-3I||_op < 27/491.
    # v.G.d/(|v||d|) < -3/20+27/491 < 0 for both old roots.
    assert -F(3,20)+F(27,491)<0
    # Entire S1 affine component: no forced arrow can be replaced at its wall.
    fids=[labels.index(x) for x in forced_labels]
    FC=[C[i] for i in fids];FB=[b[i] for i in fids]
    angular_arcs=[];special_reports=[]
    required={(i,j) for a,b in polar_edges for i,j in ((a,b),(b,a)) if i==root or (i in forced and [i,j] not in forced_labels)}
    for i,j in sorted(required):
        assert i in forced or i==root
        d=tuple(h[i]*A[j][k]-h[j]*A[i][k] for k in range(3))
        vd=dot(A[i],d);vv=dot(A[i],A[i]);dd=dot(d,d)
        if vd<0 and 250000*vd*vd>81*vv*dd:
            angular_arcs.append([i,j]);continue
        assert [i,j]==[33,32]
        raw=tuple(h[i]*x-h[j]*y for x,y in zip(coeff(A[i],A[j]),coeff(A[i],A[i])))
        gg=math.gcd(*raw);raw=tuple(x//gg for x in raw)
        tc=(raw[0]-raw[2],raw[1]-raw[2],raw[3],raw[4],raw[5]);tb=raw[2]
        act=[9,16,31,33,37]
        lam=solve([[FC[z][k] for z in act] for k in range(5)],[-x for x in tc])
        assert min(lam)>=0
        assert all(sum(lam[z]*FC[i][k] for z,i in enumerate(act))==-tc[k] for k in range(5))
        upper=sum(lam[z]*FB[i] for z,i in enumerate(act))+tb
        assert upper<0
        physical_upper=F(den*den*gg,h[33]*h[33]*h[32])*upper
        special_reports.append(dict(arc=[33,32],active=act,physical_upper=interval(physical_upper,10**15)))
        proof.append(dict(arc=[33,32],active=act,lambda_values=[fraction_record(x) for x in lam],upper=fraction_record(upper)))
    assert len(angular_arcs)==218 and len(special_reports)==1
    # Verify that every nonselected true edge from a forced vertex, and every
    # outgoing true edge from root15, was checked. No skipped alternative.
    polar_edges={tuple(sorted(t)) for triple in tr for t in itertools.combinations(triple,2)}
    required={(i,j) for a,b in polar_edges for i,j in ((a,b),(b,a)) if i==root or (i in forced and [i,j] not in forced_labels)}
    assert required==set(map(tuple,angular_arcs))|{(33,32)}
    proof_raw=json.dumps(proof,sort_keys=True,separators=(',',':')).encode();Path('policy_duals_exact.json').write_bytes(proof_raw)
    out=dict(theorem='The entire connected weak-stable-free S1 affine-metric component containing the original body has at least two strict U; no own110 occurs in that component.',scope='Other disconnected S1 affine components and physical boundary changes are not excluded. The whole closed45-arrow cone also has both strict U.',input_sha256=EXPECTED,V=len(V),E=len(edges),F=len(faces),volume=interval(vol,10**15),centroid=[interval(x,10**15) for x in g],boundedness_tetra=list(bound[0]),polar_root=root,polar_witnesses=labels,forced_polar_arcs=forced_labels,angular_negative_alternatives=angular_arcs,special_negative_alternatives=special_reports,box=[[fraction_record(x) for x in pair] for pair in boxes],dual_bounds=reports,delta=fraction_record(delta),unstable_vertices=uroots,unstable_triples=[tr[i] for i in uroots],root_checks=rootchecks,proof_bytes=len(proof_raw),proof_sha256=hashlib.sha256(proof_raw).hexdigest(),marker='J103_CONNECTED_S1_AFFINE_COMPONENT_NO_110_EXACT_PASS')
    raw=json.dumps(out,sort_keys=True,indent=2).encode()+b'\n';Path('policy_cone_exact_report.json').write_bytes(raw)
    print(out['marker'],len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
if __name__=='__main__':main()
