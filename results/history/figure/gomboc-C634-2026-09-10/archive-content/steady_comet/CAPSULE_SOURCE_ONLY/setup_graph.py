from pathlib import Path
import json,collections,hashlib
R=Path(__file__).parent
A=json.loads((R/'parent650/C650/A.json').read_text());faces=A['faces'];ef=collections.defaultdict(list)
for fi,cy in enumerate(faces):
 for a,b in zip(cy,cy[1:]+cy[:1]):ef[tuple(sorted((a,b)))].append(fi)
G=sorted(tuple(sorted(x)) for x in ef.values());blob=''.join(f'{u} {v}\n' for u,v in G)
assert hashlib.sha256(blob.encode()).hexdigest()=='3039216e06fa3dd0d5790c6cb53cdc79eeb1bed17c98357cbea64c866a6d88fe'
(R/'C650_polar_edges.txt').write_text(blob)
H=[tuple(map(int,l.split())) for l in (R/'H213_edges.txt').read_text().splitlines()];HS=set(H)
rot={}
for fi,cyc in enumerate(faces):
 rr=[]
 for a,b in zip(cyc,cyc[1:]+cyc[:1]):
  pair=ef[tuple(sorted((a,b)))];rr.append(pair[0] if pair[1]==fi else pair[1])
 rot[fi]=rr
(R/'C650_rotation.json').write_text(json.dumps(rot))
rot={i:[j for j in rr if tuple(sorted((i,j))) in HS] for i,rr in rot.items()}
text=''.join(f'{i}: '+','.join(map(str,rot[i]))+'\n' for i in range(137))
(R/'H213_rotation.txt').write_text(text)
assert hashlib.sha256(text.encode()).hexdigest()=='84a66b01a7ca3211da3e4bef6c0a616e07c75fa821630b493ed9465ad9dddf0e'
seen=set();fs=[]
for u,v in sorted((u,v) for a,b in H for u,v in ((a,b),(b,a))):
 if (u,v) in seen:continue
 cy=[];a,b=u,v
 while (a,b) not in seen:
  seen.add((a,b));cy.append(a);rr=rot[b];a,b=b,rr[(rr.index(a)-1)%len(rr)]
 fs.append(cy)
(R/'H213_faces.json').write_text(json.dumps(fs))
print('GRAPH_READY',len(G),len(H),len(fs))
