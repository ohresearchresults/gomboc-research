# figure-0352

Historical AI scientific report · saved 2026-09-09 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# Sharp Raven 79 — global coarse reconstruction handoff

## Acceptance boundary

**No new strict own-volume-centred (1,1,0) successor is promoted by this handoff.** The accepted incumbent remains the lead-owned **COORD_FIVE_CONTACTS_H132_C688**, with actual (V,E,F)=(214,344,132), strict (S,U,H)=(1,1,0), and weak counts (0,0,0). Its two completed independent exact audits and source-only replay are inherited journal evidence, not new executions credited to this slot. The exceptional two-dimensional replacement of row 67 is retained exactly.  

There are three distinct deliverables below:

1. Recovered, fully defining C688 parent data.
2. A **new completely specified rational coarse reconstruction with a proved complexity bound E≤247, hence C≤494**, but **without an established equilibrium census in this capture**. It must not be called a Gömböc or an accepted C494 endpoint.
3. A coupled physical/polar reconstruction objective that addresses two concrete defects of the initial searches: short-edge false convergence and a discontinuous unweighted per-vertex loss at contact splitting.

The supplied program contains the complete construction and two independently derived exact reconstruction/census routes, including weak cases and both cone coefficients on every true edge. **Successful execution of that new program, agreement of its two reports, and its cold replay are required next gates; they are not reported as observed accomplishments here.** Later submitted search commands did not provide an inspectable terminal acceptance report in the available capture, so they are not converted into results.

## What was actually explored

### Global support quantization

The first reconstruction replaced groups of polar support vectors by their arithmetic means. Groups were selected globally by Ward clustering of normalized support directions, separately on the 44-row apex plane and off that plane. The stable support was retained separately. This is a replacement of the supporting geometry, not a count reduction obtained by deleting triangulation diagonals.

Every numerical screen rebuilt the physical solid and its filled-volume centroid. The centred polar vectors were always computed as

    z_i = q_i / (1 - q_i·g),

using the centroid g of the rebuilt physical solid—not the old origin and not a vertex-cloud average.

The earlier completed numerical screens recorded these representative outcomes:

| Requested apex / other clusters | Numerical (V,E,F) | Numerical (S,U,H) | Minimum normalized escape |
|---|---:|---:|---:|
| 40 / 78 | (194,311,119) | (61,78,137) | −0.03279527910099268 |
| 32 / 68 | (166,264,100) | (43,46,87) | −0.05402918097819555 |
| 28 / 60 | (147,233,88) | (55,49,102) | −0.07421522074257386 |
| 44 / 54 | (151,247,98) | (52,53,103) | −0.07614370177426436 |

These are **numerical observations, not exact maximal-facet or true-edge certificates**. In particular, the apparent C494 in the last row is not an accepted body. Contact coincidences in a floating reconstruction cannot be promoted by its merging tolerance.

The last case changed numerical volume from approximately 0.5046713338009572 to 0.5074603290968331—about 0.55%—while introducing many equilibria. Small volume error plainly was not an adequate surrogate for preserving the two escape systems.

### Whole-coordinate repair and its failure mode

I explored live-centroid full-coordinate repair, using both relative radial gain and normalized directional escape, rather than holding an unrelated reference point fixed.

A relative-gain branch reached a nominal low-count screen (145,236,93), class (6,12,16), with minimum relative gain about −4.7348×10⁻⁸. This was **not near certification**: numerous physical vertices were almost coincident, and several support vectors were also almost coincident. The small objective was partly purchased by making edges short. Capturing those coincidences as genuine contacts exposed substantially negative reserves again.

That branch's complete selected coordinate array did not survive the environment boundary in inspectable form. It is therefore **excluded as a continuation parent**. Its scalar objective and counts must not be used to reconstruct or name a new exact object.

The later searches also opened a genuinely different chart: Ward reconstruction of the physical vertex cloud, retaining a planar stable polygon but not the inherited apex degree or the five contacts. Its geometry and mass were parameterized directly by physical coordinates. No successful endpoint from that chart is credited here.

## New finite construction: protected rational Ward-98

This is a fully specified new reconstruction, not an optimization-dependent endpoint.

Start from the exact C688 support vectors q_i. Let A be all indices with q_i,z=1; there are 44. Keep every row in A, and additionally keep rows 3, 6, and 46. Thus 47 rows are protected. The other 85 rows are agglomerated into **51 groups**, using exact rational Ward cost in the original three support coordinates:

    Δ(B,C) = |B||C|/(|B|+|C|) · ||mean(B)-mean(C)||².

At every merge, choose the smallest exact cost, breaking ties lexicographically by the sorted original-index tuples. Replace the two groups by their union. After exactly 34 merges, replace each group by its exact rational mean. Order the final rows as the sorted protected original indices, followed by groups in lexicographic order.

Call the resulting 98-row halfspace body P98⁰. Define its requested homogeneous own-centred version by

    P98 = P98⁰ - M(P98⁰)/Vol(P98⁰).

The program below computes this centroid from the filled solid. There is no unclosed moment target.

### What is proved about this reconstruction without relying on a floating hull

**Boundedness and full dimension.** The retained rows 0, 1, 6, and 46 have rank three and the strictly positive dependence coefficients

    [1276568005786033446132145760,
     508987154124181646352880198,
     1705025649102230389304185757,
     2606755976314515537297069808].

Their weighted sum is zero. Hence their convex hull contains the origin in its interior. These retained inequalities already bound the physical body. The origin strictly satisfies every normalized halfspace.

**A true degree-44 apex remains.** All 44 original apex-plane rows remain unchanged and are vertices of their exact planar convex polygon. Every other retained or averaged row has z<1. Thus the polar has a maximal 44-gon on z=1, and the physical body has the vertex (0,0,1) of degree 44. This is a genuine incidence fact, not epsilon merging.

**The complexity bound is genuine.** Let F be the number of actual maximal facets and let Δ be the total excess of physical vertex degrees above three. Then

    E = 3F - 6 - Δ.

Here F≤98 and Δ≥44−3=41. Therefore

    E ≤ 3·98 - 6 - 41 = 247,
    C = 2E ≤ 494.

This does **not** assert exact counts (V,E,F), and it does **not** assert monostaticity. The missing equilibrium census is decisive. The construction is useful because it places an exact, globally reconstructed, homogeneous body inside the requested complexity budget while retaining a complete recovery route. It does not erase the distinction between a low-complexity body and a Gömböc.

This Ward-98 construction is different from the earlier floating 44/54 directional-clustering screen. Do not transfer that screen's class or counts to it.

## A better joint reconstruction objective

### Why a local best-arrow loss was inadequate

For a centred point p and candidate witness w, use

    a(p,w) = p·(w-p) / (||p|| ||w-p||).

Replacing this by an unnormalized or relative raw dot allows a failed search to make its negative values arbitrarily small by shortening edges. Positive normalized arrows avoid that particular false progress.

There is another issue. An unweighted sum over current physical vertices is not invariant under contact splitting. At fixed noncoalescing witness choices, one defective vertex splitting into two nearby vertices can duplicate a nonzero loss contribution even though the bodies approach the same limiting geometry. This can obstruct a line search independently of whether a useful geometric direction exists. It is a possible mechanism, not a claim that it explains every failed run.

### Root-reaching, area-weighted shortest-path deficit

Use the actual centred physical vertices p_i and the vertices z_j of the actual centred polar. Select a maximum-radius vertex as the respective root. For a positive target δ define directed edge cost

    c(i,j) = max(δ-a(i,j),0)²,  i≠j.

Let d_i be the minimum total directed cost of a path from i to the designated root. These costs are nonnegative, so reverse Dijkstra gives both the distances and an acyclic root-reaching predecessor structure. Unlike independent best outgoing arrows, it cannot quietly accept a rootless cycle of mutually bad witnesses.

Weight each physical vertex by the area of its dual polygon in the centred polar; weight each polar vertex by the area of its corresponding physical facet. Normalize each set of weights by its total area. The proposed objective is

    Φ(P) = Σ_i A_i d_i / Σ_i A_i
         + Σ_j B_j d_j / Σ_j B_j.

The primal and polar geometries must be rebuilt from the same filled-solid centroid on every evaluation. In a support chart, z_j=q_j/(1-q_j·g). In a physical-vertex chart, obtain the maximal support planes from the physical hull before constructing z_j.

The area weights address contact multiplicity: when a polar polygon is split into nearby polygons, their areas partition the limiting area. Locally, with roots fixed and a nondegenerate limiting body, this removes the artificial duplication of a per-vertex contribution. A numerical short-distance cutoff is an additional regularization and can itself introduce discontinuities; it is not part of an exact certificate.

For a fixed shortest-path forest, the objective is differentiable away from the usual active-set boundaries. Each selected edge receives the sum of the source weights routed through it. For e=w-p and a=p·e/(||p||||e||), the endpoint derivatives are

    ∂a/∂p = (w-2p)/(||p||||e||)
             - a p/||p||² + a e/||e||²,
    ∂a/∂w = p/(||p||||e||) - a e/||e||².

The derivatives of the area weights and of the actual volume centroid also belong in the gradient. Holding g fixed would change the problem.

At a finite body with positive feature areas, Φ=0 for δ>0 supplies strict root-reaching escape witnesses for every nonroot point in both systems. **It still does not replace the requested explicit all-edge and weak-boundary audit.** The supplied exact checks remain the acceptance gate.

## Complete source-only reconstruction and exact audit program

Save the following as `raven79_replay.py`. It requires only the Python standard library. The exact Ward rule therefore has no NumPy, SciPy, optimizer-state, or floating tie-breaking dependency.

Commands:

    python3 -S raven79_replay.py parent
    python3 -S raven79_replay.py ward98
    python3 -S raven79_replay.py ward98 --cold

The first command reconstructs C688. The second constructs the new protected Ward-98 body and runs both complete exact routes. The third repeats construction and both routes in a fresh directory containing only this source text, then compares the generated bytes.

Known parent input hashes:

- Canonical free-control JSON: 4686 bytes, SHA-256 `f48217f5cf20f4ac52e62eb36b8c035731d0cc7acedb86e4e887af185a81bee5`.
- Canonical replaced C688 RAW: 70592 bytes, SHA-256 `b0d7fa06f6fb4f0ad8f51c537fbfd609b927238dc8439e7eede4f3891252c703`.

The new Ward-98 output hashes are generated by the program. No unobserved digest is invented here. The program's completion marker is conditional on actually finishing; it is not an observed receipt in this handoff.

```python
import sys, json, math, hashlib, itertools, tempfile, subprocess
from pathlib import Path
from fractions import Fraction as Q

if not __debug__:
    raise RuntimeError('Run without -O')
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

I = [[-1516204246,1849139645,1000000000],[-2254924317,68907591,1000000000],[-1942427409,1275056998,1000000000],[310798034,3032067097,902486097],[-2178849796,-527243316,1000000000],[-2124703951,-706928961,1000000000],[-1537100858,-87128866,-625180704],[-1579823983,-445960594,-406895294],[-2058090579,-877927565,1000000000],[-2219595020,-338289167,1000000000],[-2245639848,-139027255,1000000000],[884558971,-2090964379,1000000000],[2087806465,-1144815612,518723504],[209330176,-720489314,-1866927874],[688862775,-709906220,-1838375761],[-62612748,790890337,-1385412424],[406612636,586683927,-1558474227],[139281975,2134968990,-102406846],[-23804467,1899852210,-372204663],[116991928,713797159,-1467785422],[274185559,638051107,-1531332766],[-1888521007,-1197048594,1000000000],[-1978525655,-1042545496,1000000000],[-1437926816,337690618,-664983338],[-1327989677,-1805432807,1000000000],[-1198139652,-1896466038,1000000000],[-1063513980,-1977581537,1000000000],[-485567378,-2202038395,1000000000],[983670716,-2047543685,-347589365],[585948077,-2191735047,1000000000],[280140289,-2248370060,1000000000],[-1789396905,-1340944360,1000000000],[-1684109369,-1472130436,1000000000],[-2245434226,287388136,1000000000],[-334499147,-2232410312,1000000000],[-1452343962,-1704654541,1000000000],[-1571549285,-1593345676,1000000000],[1843159840,-1309055022,1000000000],[2038681648,-1189197047,644590496],[1161841131,-1951003090,1000000000],[1025376858,-2026069123,1000000000],[1750481977,-1435176027,1000000000],[1649203747,-1553915661,1000000000],[1540841583,-1663827367,1000000000],[1723278566,-363126913,-1383386628],[913700383,10654172,-1908017780],[2188184004,-862017257,-276054234],[2196517912,-909618317,-136064235],[1938336206,-530460479,-1076834759],[2128721354,-1097904084,388828271],[-937968537,1104233874,-740305648],[-1165790227,667384105,-890929313],[-1330893741,670611223,-681089333],[-1159878719,-903637714,-855451015],[-352958574,1200333625,-996053728],[-246706031,1393761227,-848041412],[-152550627,1664856588,-606957844],[-924301588,-2048873069,1000000000],[-634848144,-2161203260,1000000000],[-781231522,-2110118500,1000000000],[457252626,-2300648797,652544373],[-626352666,-1465617488,-825322365],[126994444,-2260314531,1000000000],[-2068952206,1010573740,1000000000],[1915979790,-1271458033,885771707],[1981060447,-1231648432,767565689],[1294086110,-1865304483,1000000000],[1420442443,-1769716274,1000000000],[1532650395,-252711375,-1572900600],[1628826931,-302611405,-1484278251],[631573852,84201340,-1988747033],[783676509,51133793,-1950680935],[241208978,2447913440,253249402],[1328780001,-466540690,-1662206183],[1028713364,-562748353,-1784215919],[990352865,-1853081411,-749258436],[734232496,-2225863918,-55636281],[601291857,-2294764764,302842349],[385245101,-2081787071,-607259194],[1390575069,-193848845,-1681150253],[1237315471,-130786692,-1777640003],[2171564882,-804102470,-420173712],[1231653923,1147277750,306602010],[1810598466,-422770780,-1275434754],[1866342077,-505837050,-1183483283],[2147452521,-739907438,-558430785],[-1044070189,663721785,-1016232685],[-788434343,1047513369,-927165354],[-1189906740,-673338658,-964606097],[-1067002858,-1055988580,-831384521],[-923358253,-1226846215,-813366043],[-638608894,-774898590,-1360060448],[-1121497916,314635557,-1081813236],[-180707722,639952347,-1483162472],[-181120851,-2252363821,1000000000],[-27779144,-2261673473,1000000000],[-2214009880,517930834,1000000000],[-2156812428,759053667,1000000000],[793514475,1215807964,-694571670],[622069942,1987987827,6850346],[691837861,2220481935,429012425],[2115080288,-680451632,-686239937],[2193569360,-957073951,-3576549],[759411866,2124946839,622851416],[2160072747,-1050405059,259458124],[2182503733,-1001688014,129341556],[-937582411,563125258,-1145143207],[-663630702,391804351,-1383496257],[-1145114066,-482582973,-1087898340],[-1395893772,71473293,-836007225],[-1264084986,178655253,-981474514],[-1008542007,368103841,-1162439930],[-960653070,118742489,-1260780554],[-719945426,213800264,-1413449880],[-350764336,895988642,-1236557935],[-612521522,1022346157,-1053256685],[-423375990,654558836,-1380149608],[1034188318,1493525804,52573735],[2006819781,-587465676,-947883986],[2065086600,-636867364,-818416439],[-733066415,916662503,-1070344122],[-896706378,-288884357,-1316342302],[-1073101972,-336399702,-1189563534],[-965685379,-96677917,-1282880900],[-498010321,-25540582,-1565846660],[-813659639,712454898,-1147005450],[-662448069,532250060,-1325188070],[-591195729,644931348,-1305588431],[-1122069797,2191853239,1000000000],[-1765647664,1553048346,1000000000],[430849318,-2226134311,1000000000],[737538529,-2146515367,1000000000]]

Z = (Q(0), Q(0), Q(0))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def packed(x): return json.dumps(x,separators=(',',':')).encode('ascii')
def sha(b): return hashlib.sha256(b).hexdigest()
def raw(q):
    D=math.lcm(*(x.denominator for a in q for x in a))
    return {'D':D,'I':[[int(D*x) for x in a] for a in q],'scale':1}
def write(name,obj):
    b=packed(obj); Path(name).write_bytes(b)
    print(name,len(b),sha(b),flush=True)
    return sha(b)

def parent():
    free={'D':10**9,'I':I,'scale':1}
    assert len(I)==132
    assert len(packed(free))==4686
    assert sha(packed(free))=='f48217f5cf20f4ac52e62eb36b8c035731d0cc7acedb86e4e887af185a81bee5'
    q=[tuple(Q(x,10**9) for x in a) for a in I]
    contacts=[(23,[52,109,110]),(101,[75,85,119]),
              (60,[11,77,131]),(89,[21,31,53]),(67,[12,28,43])]
    for j,ids in contacts:
        a,b,c=[q[i] for i in ids]
        D=det(a,b,c); assert D
        p=mul(1/D,add(add(cross(b,c),cross(c,a)),cross(a,b)))
        e=p if j!=67 else (p[0],p[1],Q(0))
        den=dot(p,e); assert den>0
        q[j]=add(q[j],mul((1-dot(q[j],p))/den,e))
        assert all(dot(q[i],p)==1 for i in ids+[j])
    assert q[67][2]==1
    rb=packed(raw(q))
    assert len(rb)==70592
    assert sha(rb)=='b0d7fa06f6fb4f0ad8f51c537fbfd609b927238dc8439e7eede4f3891252c703'
    ids=[0,1,6,46]
    weights=[1276568005786033446132145760,
             508987154124181646352880198,
             1705025649102230389304185757,
             2606755976314515537297069808]
    assert all(sum(w*q[i][k] for w,i in zip(weights,ids))==0 for k in range(3))
    assert any(det(q[a],q[b],q[c]) for a,b,c in itertools.combinations(ids,3))
    return q

def ward98(q):
    apex=[i for i,a in enumerate(q) if a[2]==1]
    assert len(apex)==44
    fixed=sorted(set(apex+[3,6,46])); assert len(fixed)==47
    groups=[(i,) for i in range(len(q)) if i not in fixed]
    assert len(groups)==85
    means={g:q[g[0]] for g in groups}
    while len(groups)>51:
        best=None
        for ia in range(len(groups)):
            A=groups[ia]
            for ib in range(ia+1,len(groups)):
                B=groups[ib]; e=sub(means[A],means[B])
                cost=Q(len(A)*len(B),len(A)+len(B))*dot(e,e)
                key=(cost,A,B)
                if best is None or key<best: best=key
        _,A,B=best; G=tuple(sorted(A+B))
        means[G]=mul(Q(1,len(G)),add(mul(len(A),means[A]),mul(len(B),means[B])))
        groups.remove(A); groups.remove(B); groups.append(G); groups.sort()
    definition=[(i,) for i in fixed]+groups
    result=[q[i] for i in fixed]+[means[g] for g in groups]
    assert len(result)==98
    assert sum(a[2]==1 for a in result)==44
    assert all(a[2]<=1 for a in result)
    return result,[list(g) for g in definition]

def integer_rows(q):
    rows=[]
    for a in q:
        h=math.lcm(*(x.denominator for x in a))
        n=tuple(int(h*x) for x in a)
        g=math.gcd(h,math.gcd(*n)); n=tuple(x//g for x in n); h//=g
        if n==(0,0,0): raise ValueError('zero normal')
        if (n,h) in rows: raise ValueError('duplicate support; deduplicate explicitly')
        rows.append((n,h))
    return rows

def rotate_min(c):
    j=c.index(min(c)); return c[j:]+c[:j]

def polygon_hull(ids,V,n):
    if len(ids)<3: return []
    drop=max(range(3),key=lambda k:abs(n[k])); ax=[k for k in range(3) if k!=drop]
    ids=sorted(ids,key=lambda i:(V[i][ax[0]],V[i][ax[1]],i))
    def turn(i,j,k):
        a,b,c=V[i],V[j],V[k]
        return ((b[ax[0]]-a[ax[0]])*(c[ax[1]]-a[ax[1]])
               -(b[ax[1]]-a[ax[1]])*(c[ax[0]]-a[ax[0]]))
    lo=[]; hi=[]
    for i in ids:
        while len(lo)>1 and turn(lo[-2],lo[-1],i)<=0: lo.pop()
        lo.append(i)
    for i in reversed(ids):
        while len(hi)>1 and turn(hi[-2],hi[-1],i)<=0: hi.pop()
        hi.append(i)
    c=lo[:-1]+hi[:-1]
    if len(c)<3: return []
    if dot(n,cross(sub(V[c[1]],V[c[0]]),sub(V[c[2]],V[c[0]])))<0: c.reverse()
    return rotate_min(c)

def edges_from_faces(faces):
    E={}
    for f,c in faces.items():
        for a,b in zip(c,c[1:]+c[:1]): E.setdefault(tuple(sorted((a,b))),[]).append(f)
    assert all(len(fs)==2 for fs in E.values())
    return {e:sorted(fs) for e,fs in E.items()}

def topology_check(V,faces,E):
    assert len(V)>=4 and len(faces)>=4
    assert len(V)-len(E)+len(faces)==2
    used=set(); adj=[set() for _ in V]
    for a,b in E:
        assert a!=b; used.update((a,b)); adj[a].add(b); adj[b].add(a)
    assert used==set(range(len(V)))
    seen={0}; todo=[0]
    while todo:
        for j in adj[todo.pop()]:
            if j not in seen: seen.add(j); todo.append(j)
    assert len(seen)==len(V)
    return adj

def complete_report(V,faces,E,volume,M,rows,route):
    adj=topology_check(V,faces,E)
    assert volume>0
    g=mul(1/volume,M)
    assert sub(M,mul(volume,g))==Z
    assert all(h-dot(n,g)>0 for n,h in rows)
    S=[]; U=[]; H=[]; wS=[]; wU=[]; wH=[]; primitives=[]
    for f,c in sorted(faces.items()):
        n,h=rows[f]
        foot=add(g,mul(Q(h-dot(n,g),dot(n,n)),n))
        if route=='A':
            vals=[hh-dot(nn,foot) for j,(nn,hh) in enumerate(rows) if j!=f]
        else:
            vals=[dot(n,cross(sub(V[b],V[a]),sub(foot,V[a])))
                  for a,b in zip(c,c[1:]+c[:1])]
        if all(x>0 for x in vals): S.append(f)
        elif all(x>=0 for x in vals): wS.append(f)
    for i,v in enumerate(V):
        others=range(len(V)) if route=='A' else sorted(adj[i])
        vals=[dot(sub(v,g),sub(v,V[j])) for j in others if j!=i]
        if all(x>0 for x in vals): U.append(i)
        elif all(x>=0 for x in vals): wU.append(i)
    for (ia,ib),fs in sorted(E.items()):
        a,b=V[ia],V[ib]; e=sub(b,a); L=dot(e,e); assert L>0
        n,m=rows[fs[0]][0],rows[fs[1]][0]
        if route=='A':
            T=dot(sub(g,a),e); other=L-T
        else:
            T=dot(sub(a,g),sub(a,b)); other=dot(sub(b,g),sub(b,a))
        r=add(sub(a,g),mul(T/L,e)); nn=dot(n,n); mm=dot(m,m); nm=dot(n,m)
        G=nn*mm-nm*nm; assert G>0
        if route=='A':
            alpha=(dot(r,n)*mm-dot(r,m)*nm)/G
            beta=(dot(r,m)*nn-dot(r,n)*nm)/G
        else:
            direction=cross(n,m)
            alpha=dot(cross(r,m),direction)/dot(direction,direction)
            beta=dot(cross(n,r),direction)/dot(direction,direction)
        vals=[T,other,alpha,beta]
        primitives.append([ia,ib,[str(x) for x in vals]])
        if all(x>0 for x in vals): H.append([ia,ib])
        elif all(x>=0 for x in vals): wH.append([ia,ib])
    return {'counts':[len(V),len(E),len(faces)],'C':2*len(E),
            'vertices':[[str(x) for x in v] for v in V],
            'facets':[[f,c] for f,c in sorted(faces.items())],
            'edges':[[a,b]+fs for (a,b),fs in sorted(E.items())],
            'volume':str(volume),'moments':[str(x) for x in M],
            'centroid':[str(x) for x in g],
            'S':S,'U':U,'H':H,'weakS':wS,'weakU':wU,'weakH':wH,
            'edge_primitives':primitives}

def audit_A(q):
    rows=integer_rows(q); N=len(rows)
    assert any(det(rows[i][0],rows[j][0],rows[k][0])
               for i,j,k in itertools.combinations(range(N),3))
    # Independent recession-cone test: rank three and no feasible extreme ray.
    for i,j in itertools.combinations(range(N),2):
        t=cross(rows[i][0],rows[j][0])
        if t==(0,0,0): continue
        for direction in (t,mul(-1,t)):
            if all(dot(n,direction)<=0 for n,h in rows):
                raise ValueError('unbounded halfspace body')
    vertices=set()
    for i,j,k in itertools.combinations(range(N),3):
        a,ha=rows[i]; b,hb=rows[j]; c,hc=rows[k]
        bc=cross(b,c); D=dot(a,bc)
        if not D: continue
        numerator=add(add(mul(ha,bc),mul(hb,cross(c,a))),mul(hc,cross(a,b)))
        if D<0: D=-D; numerator=mul(-1,numerator)
        if all(dot(n,numerator)<=h*D for n,h in rows):
            vertices.add(tuple(Q(x,D) for x in numerator))
    V=sorted(vertices); faces={}
    for f,(n,h) in enumerate(rows):
        ids=[i for i,v in enumerate(V) if dot(n,v)==h]
        c=polygon_hull(ids,V,n)
        if c: faces[f]=c
    E=edges_from_faces(faces); volume=Q(0); M=Z
    for c in faces.values():
        a=V[c[0]]
        for j in range(1,len(c)-1):
            b,d=V[c[j]],V[c[j+1]]; dt=det(a,b,d); assert dt>0
            volume+=dt/6; M=add(M,mul(dt/24,add(add(a,b),d)))
    return complete_report(V,faces,E,volume,M,rows,'A')

def audit_B(q):
    rows=integer_rows(q); records=[]; vertices=set()
    # Independently clip every pair-intersection line by every halfspace.
    for i,j in itertools.combinations(range(len(rows)),2):
        n,hn=rows[i]; m,hm=rows[j]; t=cross(n,m); G=dot(t,t)
        if not G: continue
        nn=dot(n,n); mm=dot(m,m); nm=dot(n,m)
        x0=add(mul(Q(hn*mm-hm*nm,G),n),mul(Q(hm*nn-hn*nm,G),m))
        lo=None; hi=None; feasible=True
        for a,h in rows:
            c=dot(a,t); rhs=h-dot(a,x0)
            if not c:
                if rhs<0: feasible=False; break
            elif c>0:
                v=rhs/c; hi=v if hi is None else min(hi,v)
            else:
                v=rhs/c; lo=v if lo is None else max(lo,v)
            if lo is not None and hi is not None and lo>hi:
                feasible=False; break
        if not feasible: continue
        if lo is None or hi is None: raise ValueError('unbounded pair line')
        if lo==hi: continue
        a=add(x0,mul(lo,t)); b=add(x0,mul(hi,t))
        vertices.update((a,b)); records.append((a,b,i,j))
    V=sorted(vertices); index={v:i for i,v in enumerate(V)}
    active=[]
    for f,(n,h) in enumerate(rows):
        ids=[i for i,v in enumerate(V) if dot(n,v)==h]
        if len(ids)>=3:
            a,b=V[ids[0]],V[ids[1]]
            if any(cross(sub(b,a),sub(V[k],a))!=Z for k in ids[2:]): active.append(f)
    active=set(active); E={}
    for a,b,i,j in records:
        if i in active and j in active:
            e=tuple(sorted((index[a],index[b]))); owners=sorted((i,j))
            if e in E: assert E[e]==owners
            E[e]=owners
    faces={}
    for f in sorted(active):
        adj={}
        for (a,b),owners in E.items():
            if f in owners:
                adj.setdefault(a,[]).append(b); adj.setdefault(b,[]).append(a)
        assert adj and all(len(v)==2 for v in adj.values())
        start=min(adj); c=[start]; previous=None; current=start
        while True:
            choices=sorted(v for v in adj[current] if v!=previous)
            nxt=choices[0]
            if nxt==start: break
            assert nxt not in c
            c.append(nxt); previous,current=current,nxt
        assert set(c)==set(adj)
        n=rows[f][0]
        if dot(n,cross(sub(V[c[1]],V[c[0]]),sub(V[c[2]],V[c[0]])))<0: c.reverse()
        faces[f]=rotate_min(c)
    # Independent planar-flux mass, using last-vertex rather than first-vertex fans.
    volume=Q(0); M=Z; flux=Z
    for f,c in faces.items():
        n,h=rows[f]; r=V[c[-1]]; nn=dot(n,n)
        for j in range(len(c)-2):
            a,b=V[c[j]],V[c[j+1]]
            area_over_norm=dot(n,cross(sub(a,r),sub(b,r)))/(2*nn)
            assert area_over_norm>0
            flux=add(flux,mul(area_over_norm,n))
            volume+=h*area_over_norm/3
            M=add(M,mul(h*area_over_norm/12,add(add(r,a),b)))
    assert flux==Z
    assert any(det(rows[i][0],rows[j][0],rows[k][0])
               for i,j,k in itertools.combinations(sorted(faces),3))
    return complete_report(V,faces,E,volume,M,rows,'B')

def class_counts(a): return [len(a[k]) for k in ('S','U','H')]
def weak_counts(a): return [len(a[k]) for k in ('weakS','weakU','weakH')]

def controls():
    cube=[(Q(s),Q(0),Q(0)) for s in (-1,1)]
    cube += [(Q(0),Q(s),Q(0)) for s in (-1,1)]
    cube += [(Q(0),Q(0),Q(s)) for s in (-1,1)]
    tetra=[tuple(map(Q,a)) for a in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
    octa=[tuple(map(Q,a)) for a in itertools.product((-1,1),repeat=3)]
    for q,counts,cl in [(cube,[8,12,6],[6,8,12]),
                         (tetra,[4,6,4],[4,4,6]),
                         (octa,[6,12,8],[8,6,12])]:
        A=audit_A(q); B=audit_B(q)
        assert A==B and A['counts']==counts and class_counts(A)==cl
        assert weak_counts(A)==[0,0,0]
    sheared=[tuple(map(Q,a)) for a in [(1,-1,0),(-1,1,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
    A=audit_A(sheared); B=audit_B(sheared)
    assert A==B and sum(weak_counts(A))>0


def main():
    mode=sys.argv[1] if len(sys.argv)>1 else 'ward98'
    if mode not in ('parent','ward98'): raise ValueError('mode must be parent or ward98')
    controls()
    q=parent()
    if mode=='ward98': q,groups=ward98(q)
    else: groups=[[i] for i in range(len(q))]
    hashes={}
    hashes['GROUPS.json']=write('GROUPS.json',groups)
    hashes['RAW.json']=write('RAW.json',raw(q))
    A=audit_A(q); B=audit_B(q)
    assert A==B
    if mode=='parent':
        assert A['counts']==[214,344,132]
        assert class_counts(A)==[1,1,0] and weak_counts(A)==[0,0,0]
        assert A['S']==[3]
    else:
        assert A['counts'][2]<=98 and A['counts'][1]<=247
        apex=A['vertices'].index(['0','0','1'])
        assert sum(apex in e[:2] for e in A['edges'])==44
    hashes['A.json']=write('A.json',A)
    hashes['B.json']=write('B.json',B)
    print('COUNTS',A['counts'],'CLASS',class_counts(A),'WEAK',weak_counts(A),flush=True)
    if '--cold' in sys.argv:
        source=Path(__file__).read_bytes()
        with tempfile.TemporaryDirectory(prefix='raven79-cold-') as td:
            p=Path(td); script=p/'raven79_replay.py'; script.write_bytes(source)
            subprocess.run([sys.executable,'-S',str(script),mode],cwd=p,check=True)
            for name,digest in hashes.items(): assert sha((p/name).read_bytes())==digest
        print('COLD_SOURCE_ONLY_BYTEWISE_REPLAY_COMPLETE',flush=True)
    print('REPLAY_COMPLETE',mode,flush=True)

if __name__=='__main__': main()
```

### Audit scope and independence

Route A enumerates every support triple, tests every candidate against every halfspace, and builds maximal polygons by exact planar convex hulls. Its mass uses outward tetrahedra. Its face census uses all other supporting inequalities; its vertex census uses all other vertices; its edge census uses Gram coefficients.

Route B enumerates every support-pair line and clips it by every halfspace. It obtains true edges from nonzero clipped segments, reconstructs facet cycles from those edges, and computes mass by planar flux with a different polygon fan. Its face census uses oriented polygon-edge tests, its vertex census uses true neighbours, and its cone coefficients use cross products. It does not import A's vertices, facets, edges, mass, centroid, or census.

Both routes record all four exact edge primitives, not just the saddle count. Strict and weak cases are classified separately. Shared rational vector arithmetic, serialization, and report formatting are not separate geometric evidence.

Again: this is a complete **proposed replay unit**. It is not a claim that these newly supplied implementations have already completed the Ward-98 audit or that their controls have been observed to pass in this capture.

## Most useful continuation

Run `ward98 --cold` first and retain its complete output, regardless of class. That supplies the currently missing actual maximal incidence, exact filled mass, full equilibrium census, output hashes, and executed replay receipt for the complexity-bounded reconstruction. A successful census would require strict (1,1,0), weak (0,0,0), and all the stated audit comparisons; a low edge count alone is insufficient.

If it is defective, the useful repair target is the **root-reaching, area-weighted joint deficit**, with the centroid and centred polar differentiated through the actual rebuilt solid. Allow temporary equilibrium-pair births and active-facet changes during repair. In parallel, the physical-vertex reconstruction chart remains the genuine escape from the inherited degree-44 architecture; it must not be judged using the support chart's incidence budget.

Do not resume from the lost near-zero relative-gain array, do not transfer the floating 44/54 census to exact Ward-98, and do not promote any later run merely because a command was submitted. The accepted strict endpoint at this boundary is still C688.
