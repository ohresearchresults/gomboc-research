# material-4a4c26be2775

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced.

---

"""TREE253_K2_PRIMAL_PATH_TRANSPORT_V1: complete exact recovery and proof.

Reconstruct/verify: save this complete immutable text as
primal_path_transport_recovery.txt and run, with assertions enabled,
  python -S primal_path_transport_recovery.txt
  python -S primal_path_transport_recovery.txt --verify
Standard library only, CPython 3.13.5 observed. No numerical locator is used.
The first command writes transport_37_classes.json; --verify only compares.
Expected terminal marker: TREE253_K2_PRIMAL_PATH_TRANSPORT_EXACT_PASS 55 37 18 52.
The exact output bytes and SHA-256 are enforced by EXPECTED_OUTPUT_PIN below.
The exact literal input is embedded below and enforced by NATIVE55_PIN.

SOURCE AND DOMAIN. The 55 incidence rows are copied literally from section 6
of immutable result minimum-0078, SHA-256
2a0d3544bfb7f0c3b6366bdda3555bc650eede67a1444d51a2d7207a0079eecd,
read from cursor 0 through eof. This is its native parent55_index numbering,
not the global polyhedral-type numbering. The input pin also equals the
incidences.txt pin in accepted checkpoint38 proof
[internal-source-reference]. Facet labels remain 0,...,8 and native vertex
labels remain the order of the ten tokens in each row. A token is the actual
incident maximal-facet set of that vertex, not pairwise shadow information.
The full nonnegative unequal pole-arrow graph in each application separately
is p=(0,0,1,2,3,4,5,0,7). Its eight true dual edges have primal complements
which are actual Hamilton paths. The path orientation convention starts at
the endpoint with the smaller native vertex number. No path-position label
is substituted for a native label without the explicit maps in the output.

TRANSPORT THEOREM. Consider two of the literal incidence rows A,B, with their
complementary paths PA,PB. Suppose a permutation pi of native vertices maps
all actual maximal-facet vertex sets of A bijectively onto those of B and
maps PA[j] to PB[9-j] for every j. Any theorem excluding ALL uniform-volume
centred convex realizations of A in ALL common SPD metrics under weak path
arrows toward position r also excludes all such realizations of B under
weak path arrows toward position 9-r.

PROOF. If a realization of B existed, relabel its physical vertices by
x_A[v]=x_B[pi(v)] without moving any point. By the bijection of maximal facets
this is a realization of the literal incidence row A. Volume, density,
actual volume centroid and the single SPD metric M are unchanged. The path
edges are carried exactly to reversed path edges, so every necessary
inequality x_i^T M (x_parent-x_i)>=0 is identical after this permutation.
The putative B realization would violate the universal A exclusion theorem.
The inverse permutation proves the converse. This includes weak walls and
non-simplicial facets. No assumption about an off-path arrow is introduced.

For the mono-monostatic TREE253/K2 application, theorem A of the cited native
parent establishes the weak complementary-path hypotheses separately for A
and B. It is NOT asserted that the facet permutation carries the full
oriented pole-arrow graph to itself, that the native labels are aliases, or
that these are the same pole-labelled domain. Those stronger statements
are unnecessary and may be false. Only a path-based universal exclusion is
transported. Arbitrary extra pole inequalities or a shape-specific witness
would need their own compatibility check and cannot automatically transfer.

WHY FACET MATCHING IS STRONGER THAN A CANONICAL-FAN MATCH TEST. In each genuine
convex facet every polygon triangulation gives a legitimate tetrahedral fan.
A fan used in an A certificate can be transported by pi to B, even when it
differs from the artificial cycle-start convention used by B's default
verifier. Thus canonical-fan equality is sufficient but not necessary for
transport. It yields 52 classes, with only three nontrivial pairs; exact
maximal-facet/path matching yields 37 classes, with eighteen nontrivial pairs.
The output records both inventories and all explicit native vertex and
facet permutations for the stronger result. Edges, facets, paths, inverses
and the reflection relation are checked using only exact finite data.

COVERAGE BOUNDARY. This capsule proves the transport theorem and exact
37-class inventory. It contains no new integer matrix coefficients and by
itself does not assert exclusion of a new root or of a whole row. In
particular, exclusions for native 5 can transfer to 12, for 6 to 18, and for
7 to 16 after their literal source root exclusions are established. Native
8 and 9 are another equivalent pair; proving both independently is redundant
for this path-only purpose but does not identify their original pole labels.
The global 632/52585 inventory, the accepted universal C>=34 lower bound,
existence on C=34, and the unauthenticated Figure C=650 claim are untouched.
All eighteen pairs are explicit in the generated output, not inferred from
names or a failed numerical search.
"""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import hashlib,json,sys
assert __debug__
N=10
DUAL=((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(0,7),(7,8))
NATIVE55='0: 012 016 0237 067 1245 156 234 3478 458 5678\n1: 012 016 0237 067 1256 234 245 3478 458 5678\n2: 012 016 0237 067 1256 235 345 3478 458 5678\n3: 012 016 0237 067 126 2356 345 3478 458 5678\n4: 013 018 0237 078 1245 1278 134 2356 346 456\n5: 0134 017 0237 1245 128 178 2356 278 346 456\n6: 0134 017 037 1245 1278 2356 238 346 378 456\n7: 0134 017 037 1245 128 178 2356 2378 346 456\n8: 0134 018 023 027 078 1245 1278 2356 346 456\n9: 0134 018 0237 078 124 1278 2356 245 346 456\n10: 0134 018 0237 078 1245 127 178 2356 346 456\n11: 0134 018 0237 078 1245 1278 235 346 356 456\n12: 0134 018 0237 078 1245 1278 236 256 345 356\n13: 0134 018 0237 078 1245 1278 236 256 346 456\n14: 0134 018 0237 078 1245 128 2356 278 346 456\n15: 0134 018 0237 078 125 1278 145 2356 346 456\n16: 0134 018 0237 078 1256 1278 145 236 345 356\n17: 0134 018 0237 078 1256 1278 145 236 346 456\n18: 0134 018 0237 078 126 1278 145 156 2356 345\n19: 0134 018 037 078 1245 1278 2356 237 346 456\n20: 0134 018 037 078 1245 128 2356 2378 346 456\n21: 014 017 0347 1245 1278 2356 238 346 378 456\n22: 014 017 0347 1245 128 178 2356 2378 346 456\n23: 014 017 047 1245 1278 2356 238 346 3478 456\n24: 014 018 0237 034 078 1245 1278 2356 346 456\n25: 014 018 0347 078 1245 1278 2356 237 346 456\n26: 014 018 0347 078 1245 128 2356 2378 346 456\n27: 0145 017 0347 125 1278 2356 238 346 378 456\n28: 0145 017 0347 125 128 178 2356 2378 346 456\n29: 0145 017 0347 1256 1278 236 238 345 356 378\n30: 0145 017 0347 1256 1278 236 238 346 378 456\n31: 0145 017 0347 1256 128 178 236 2378 345 356\n32: 0145 017 0347 1256 128 178 236 2378 346 456\n33: 0145 017 0347 126 1278 156 2356 238 345 378\n34: 0145 017 0347 126 128 156 178 2356 2378 345\n35: 0145 017 047 125 1278 2356 238 346 3478 456\n36: 0145 017 047 1256 1278 236 238 345 3478 356\n37: 0145 017 047 1256 1278 236 238 346 3478 456\n38: 0145 017 047 126 1278 156 2356 238 345 3478\n39: 0145 018 0237 034 078 125 1278 2356 346 456\n40: 0145 018 0237 034 078 1256 1278 236 345 356\n41: 0145 018 0237 034 078 1256 1278 236 346 456\n42: 0145 018 0237 034 078 126 1278 156 2356 345\n43: 0145 018 0347 078 125 1278 2356 237 346 456\n44: 0145 018 0347 078 125 128 2356 2378 346 456\n45: 0145 018 0347 078 1256 1278 236 237 345 356\n46: 0145 018 0347 078 1256 1278 236 237 346 456\n47: 0145 018 0347 078 1256 128 236 2378 345 356\n48: 0145 018 0347 078 1256 128 236 2378 346 456\n49: 0145 018 0347 078 126 1278 156 2356 237 345\n50: 0145 018 0347 078 126 128 156 2356 2378 345\n51: 015 017 0457 125 1278 2356 238 346 3478 456\n52: 015 017 0457 1256 1278 236 238 345 3478 356\n53: 015 017 0457 1256 1278 236 238 346 3478 456\n54: 015 017 0457 126 1278 156 2356 238 345 3478\n'
NATIVE55_PIN=[2630,'58126aee072933749b18eca00ac4d32842e56e6ac8d662d06713bacef28bf96e']
EXPECTED_OUTPUT_PIN=[5872, '403b00acabd759d695eb748568b0cd17b1fae94b5bedcaea40cb7a6f6df1adb8']
def enc(o):return (json.dumps(o,sort_keys=True,separators=(",",":"))+"\n").encode()
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def geometry(incidence):
    inc=[set(map(int,s)) for s in incidence]
    edges=[(i,j) for i,j in combinations(range(N),2) if len(inc[i]&inc[j])==2]
    assert len(edges)==17
    pedges=[(i,j) for i,j in edges if tuple(sorted(inc[i]&inc[j])) not in DUAL]
    adj={i:[] for i in range(N)}
    for i,j in pedges: adj[i].append(j);adj[j].append(i)
    ends=sorted(i for i in adj if len(adj[i])==1)
    assert len(pedges)==9 and len(ends)==2
    assert all(len(adj[i])==2 for i in adj if i not in ends)
    path=[ends[0]]
    while len(path)<N:
        choices=[i for i in adj[path[-1]] if i not in path]
        assert len(choices)==1
        path.append(choices[0])
    assert path[-1]==ends[1] and sorted(path)==list(range(N))
    inv={v:i for i,v in enumerate(path)}
    faces=[]
    for f in range(9):
        vs=[i for i in range(N) if f in inc[i]]
        a={i:sorted(j for j in vs if tuple(sorted((i,j))) in edges) for i in vs}
        assert all(len(a[i])==2 for i in vs)
        cy=[min(vs)]
        while len(cy)<len(vs):
            choices=[j for j in a[cy[-1]] if j not in cy]
            assert choices
            cy.append(choices[0])
        assert cy[0] in a[cy[-1]] and set(cy)==set(vs)
        faces.append(cy)
    faceedges={}
    for f,cy in enumerate(faces):
        for i in range(len(cy)):
            edge=tuple(sorted((cy[i],cy[(i+1)%len(cy)])))
            faceedges.setdefault(edge,[]).append(f)
    assert sorted(faceedges)==edges
    assert all(tuple(sorted(fs))==tuple(sorted(inc[i]&inc[j])) for (i,j),fs in faceedges.items())
    assert N-len(edges)+len(faces)==2
    fans=[]
    for ap in path:
        ts=[]
        for f in faces:
            if ap in f:continue
            for j in range(1,len(f)-1):
                t=tuple(sorted(inv[v] for v in (ap,f[0],f[j],f[j+1])))
                assert len(t)==len(set(t))==4
                ts.append(t)
        assert len(ts)==len(set(ts))
        fans.append(sorted(ts))
    return path,edges,faces,fans

def reconstruct():
    assert pin(NATIVE55.encode())==NATIVE55_PIN
    table={}
    for line in NATIVE55.splitlines():
        label,tokens=line.split(':');i=int(label)
        assert i not in table;table[i]=tokens.split()
        assert len(table[i])==10 and len(set(table[i]))==10
    assert sorted(table)==list(range(55))
    data={};classes=defaultdict(list);fanclasses=defaultdict(list)
    for i in range(55):
        p,e,f,fans=geometry(table[i]);inv={v:j for j,v in enumerate(p)}
        key=tuple(sorted(tuple(sorted(inv[v] for v in facet)) for facet in f))
        rev=tuple(sorted(tuple(sorted(9-j for j in facet)) for facet in key))
        canonical=min(key,rev);classes[canonical].append([i,int(key!=canonical)])
        ff=tuple(tuple(t for t in fan) for fan in fans)
        rf=tuple(tuple(sorted(tuple(sorted(9-j for j in t)) for t in fan)) for fan in reversed(fans))
        fanclasses[min(ff,rf)].append([i,int(ff!=min(ff,rf))])
        data[i]=(p,e,f)
    result={'identity':'TREE253_K2_PRIMAL_PATH_TRANSPORT_V1','native_input_pin':NATIVE55_PIN,
        'classes':sorted(classes.values()),'canonical_fan_classes':sorted(fanclasses.values()),'transports':[]}
    for group in result['classes']:
        assert len(group) in (1,2)
        if len(group)==1:continue
        (a,ra),(b,rb)=group
        assert a<b and ra!=rb
        pa,ea,fa=data[a];pb,eb,fb=data[b]
        pi=[None]*N
        for j,v in enumerate(pa):pi[v]=pb[9-j]
        assert sorted(pi)==list(range(N))
        phi=[]
        for facet in fa:
            mapped=set(pi[v] for v in facet)
            matches=[j for j,f in enumerate(fb) if set(f)==mapped]
            assert len(matches)==1;phi.append(matches[0])
        assert sorted(phi)==list(range(9))
        assert sorted(tuple(sorted((pi[u],pi[v]))) for u,v in ea)==eb
        for v in range(N):
            assert set(int(k) for k in table[b][pi[v]])==set(phi[int(k)] for k in table[a][v])
        result['transports'].append({'source_native_index':a,'target_native_index':b,
            'source_path':pa,'target_path':pb,'native_vertex_permutation':pi,
            'facet_permutation':phi,'path_position_permutation':list(reversed(range(N)))})
    expected=[(5,12),(6,18),(7,16),(8,9),(10,11),(13,14),(15,19),(17,20),(21,42),(22,40),(25,39),(26,41),(27,49),(28,45),(29,34),(30,50),(32,47),(44,46)]
    assert [(t['source_native_index'],t['target_native_index']) for t in result['transports']]==expected
    assert len(result['classes'])==37 and len(result['transports'])==18 and len(result['canonical_fan_classes'])==52
    return enc(result)
if __name__=='__main__':
    assert sys.argv[1:] in ([],['--verify'])
    b=reconstruct()
    if EXPECTED_OUTPUT_PIN is not None:assert pin(b)==EXPECTED_OUTPUT_PIN
    path=Path(__file__).resolve().with_name('transport_37_classes.json')
    if sys.argv[1:]:assert path.read_bytes()==b
    else:
        if path.exists():assert path.read_bytes()==b
        path.write_bytes(b)
    print('TREE253_K2_PRIMAL_PATH_TRANSPORT_EXACT_PASS 55 37 18 52')
    print('OUTPUT',*pin(b))
