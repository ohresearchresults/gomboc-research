# material-8c3a515214c4

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Recovery capsule part 1b of 3: rational polyhedron geometry

This is the second consecutive segment of the exact convex-polyhedron auditor, not a standalone executable. Part1a is material [internal-source-reference]. Concatenate its entire text with the literal code block below, retaining the block's final newline. The result is exact_poly.py,7469 bytes,SHA256 7e2bd2e8b675510fee3cf1c33588f770a5fada10d4b7bea1767a363510ff8438. The suffix alone has3996 bytes,SHA256 c5308938e4d9fff2187afab3554be244abe12c545357d5d7f21cbf2a70fe7254. This arithmetic computes uniform-volume centroids and equilibrium inequalities. It uses only the Python standard library. Part2 contains the complete input point coordinates. The checks constitute one full mechanical auditor with two mass identities, not independent duplicate mechanical audits.

```python
    V=[tuple(F(z,den) for z in a) for a in verts]
    D=F(0);W=(F(0),)*3;tris=[]
    for cyc in cycles:
        for j in range(1,len(cyc)-1):
            a,b,c=[V[k] for k in [cyc[0],cyc[j],cyc[j+1]]]
            d=det(a,b,c);D+=d;W=add(W,mul(add(add(a,b),c),d));tris.append((cyc[0],cyc[j],cyc[j+1]))
    assert D>0;volume=D/6;centroid=mul(W,1/(4*D));P=[sub(v,centroid) for v in V]
    # Independent positive tetrahedra about the computed interior point, both mass identities.
    D2=F(0);W2=(F(0),)*3
    for ia,ib,ic in tris:
        a,b,c=P[ia],P[ib],P[ic];d=det(a,b,c);assert d>0
        D2+=d;W2=add(W2,mul(add(add(a,b),c),d))
    assert D2==D and W2==(0,0,0)
    Ns=[k[:3] for k in plane_keys];hs=[F(k[3],den)-dot(k[:3],centroid) for k in plane_keys]
    assert all(h>0 for h in hs)
    for n,h in zip(Ns,hs):assert all(dot(n,p)<=h for p in P)
    U=[];WU=[];S=[];WS=[];H=[];WH=[];zeros=[0,0,0]
    for i,p in enumerate(P):
        signs=[-dot(p,sub(P[j],p)) for j in adj[i]];zeros[1]+=sum(s==0 for s in signs)
        state=classify(signs)
        if state=='strict':U.append(i)
        elif state=='weak':WU.append(i)
    for fi,cyc in enumerate(cycles):
        n=Ns[fi];foot=mul(n,hs[fi]/dot(n,n))
        signs=[dot(cross(sub(P[b],P[a]),sub(foot,P[a])),n) for a,b in zip(cyc,cyc[1:]+cyc[:1])]
        zeros[0]+=sum(s==0 for s in signs);state=classify(signs)
        if state=='strict':S.append(fi)
        elif state=='weak':WS.append(fi)
    for a,b in edges:
        d=sub(P[b],P[a]);dd=dot(d,d);t=-dot(P[a],d)/dd;foot=add(P[a],mul(d,t));fi,fj=edge_faces[(a,b)];n,m=Ns[fi],Ns[fj]
        nn,mm,nm=dot(n,n),dot(m,m),dot(n,m);g=nn*mm-nm*nm;assert g>0
        l1=(dot(foot,n)*mm-dot(foot,m)*nm)/g;l2=(dot(foot,m)*nn-dot(foot,n)*nm)/g
        assert add(mul(n,l1),mul(m,l2))==foot
        signs=[t,1-t,l1,l2];zeros[2]+=sum(s==0 for s in signs);state=classify(signs)
        if state=='strict':H.append([a,b])
        elif state=='weak':WH.append([a,b])
    Q=[mul(n,1/h) for n,h in zip(Ns,hs)]
    def bars(X):
        births=[dot(x,x) for x in X];links=[]
        for i,j in itertools.combinations(range(len(X)),2):
            A=dot(X[i],X[i]);B=dot(X[i],X[j]);C=dot(X[j],X[j]);delta=A+C-2*B
            assert delta>0
            w=A if B>=A else C if B>=C else (A*C-B*B)/delta
            links.append((w,i,j))
        par=list(range(len(X)));peaks=list(par);out=[]
        def root(i):
            while par[i]!=i:par[i]=par[par[i]];i=par[i]
            return i
        for w,i,j in sorted(links,key=lambda z:(-z[0],z[1],z[2])):
            a,b=root(i),root(j)
            if a==b:continue
            if (births[peaks[a]],-peaks[a])<(births[peaks[b]],-peaks[b]):a,b=b,a
            born=births[peaks[b]];assert born>=w
            if born>w:out.append(dict(peak=peaks[b],elder=peaks[a],edge=[i,j],birth=qstr(born),death=qstr(w),gap=qstr(born-w)))
            par[b]=a
        return out
    pb,qb=bars(P),bars(Q)
    if not any(zeros):assert len(S)+len(U)-len(H)==2 and len(pb)==len(U)-1 and len(qb)==len(S)-1
    common=math.lcm(*(x.denominator for p in P for x in p))
    return dict(name=data.get('name'),input_count=len(A),V=N,E=M,F=K,C=2*M,strict=[len(S),len(U),len(H)],weak=[len(WS),len(WU),len(WH)],primitive_zero= zeros,volume=qstr(volume),centroid=list(map(qstr,centroid)),common_centered_denominator_bits=common.bit_length(),vertices=[list(a) for a in verts],denominator=den,facets=cycles,planes=[list(k) for k in plane_keys],edges=[list(e) for e in edges],stable=S,unstable=U,saddles=H,weak_stable=WS,weak_unstable=WU,weak_saddles=WH,Pbars=pb,Qbars=qb,positive_centered_tetrahedra=len(tris),marker='EXACT_HULL_TRUE_FEATURES_OWN_MASS_FULL_MECHANICS_PASS')
if __name__=='__main__':
    data=json.load(open(sys.argv[1]));r=audit(data)
    if len(sys.argv)>2:json.dump(r,open(sys.argv[2],'w'),separators=(',',':'),sort_keys=True)
    print(json.dumps({k:r[k] for k in ['name','V','E','F','C','strict','weak','primitive_zero','common_centered_denominator_bits','marker']}))
```
