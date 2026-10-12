"""Exact whole-complex quotient comparison to the literal BQ13 C626 parent.
The endpoint complex and moments come exclusively from independent exact audits.
"""
import sys,json,itertools
from pathlib import Path
from fractions import Fraction as F
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R/'parent/parent'));import RECONSTRUCT
sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def owners(fs,N):
 o=[set()for _ in range(N)]
 for j,cy in enumerate(fs):
  for i in cy:o[i].add(j)
 return o

def run(record,raw,spec):
 fs=json.loads((R/'parent/BASIN69_96/faces.json').read_text());H=RECONSTRUCT.recover(json.loads((R/'parent/BASIN69_96/GENERATOR.json').read_text()))['H'];oo=owners(fs,178);nn=owners(record['faces'],record['V']);ids=spec['original_support_ids'];old2new={x:j for j,x in enumerate(ids)};lost=set(range(137))-set(ids);byowner={tuple(sorted(g)):j for j,g in enumerate(nn)};P=[]
 for o in oo:
  for i,j,k in itertools.combinations(sorted(o),3):
   a,b,c=[H[v][:3]for v in (i,j,k)];D=det(a,b,c)
   if not D:continue
   aa,bb,cc=cross(b,c),cross(c,a),cross(a,b);p=tuple(F(H[i][3]*aa[t]+H[j][3]*bb[t]+H[k][3]*cc[t],D)for t in range(3));break
  else:raise AssertionError('missing parent independent triple')
  assert all(dot(r[:3],p)<=r[3]for r in H);P.append(p)
 assert len(set(P))==178
 rawlex={p:i for i,p in enumerate(sorted(P))};c2lex=[rawlex[p]for p in P]
 classes=spec['parent_vertex_classes'];assert sorted(i for cl in classes for i in cl)==list(range(178));assert len(classes)==record['V']
 mapping=[None]*178;mergers=[]
 for cl in classes:
  o=set().union(*(oo[i]for i in cl))-lost;sig=tuple(sorted(old2new[j]for j in o));v=byowner[sig]
  for i in cl:mapping[i]=v
  if len(cl)>1:mergers.append(dict(parent_construction=cl,parent_rawlex=sorted(c2lex[i]for i in cl),new_rawlex=v,new_owners=list(sig),original_owners=sorted(o)))
 assert len(set(mapping))==record['V']
 def canon(cy):
  k=cy.index(min(cy));return cy[k:]+cy[:k]
 rebuilt=[];OE=set();discarded=[]
 for fi,cy in enumerate(fs):
  OE.update(tuple(sorted((a,b)))for a,b in zip(cy,cy[1:]+cy[:1]));cc=[]
  for i in cy:
   if not cc or cc[-1]!=mapping[i]:cc.append(mapping[i])
  if len(cc)>1 and cc[-1]==cc[0]:cc.pop()
  if fi in lost:discarded.append(dict(original_support=fi,image=cc));continue
  assert len(cc)>=3 and len(set(cc))==len(cc);rebuilt.append(canon(cc))
 assert rebuilt==record['faces'];EE=set(map(tuple,record['edges']));mapped={};collapsed=[]
 for a,b in OE:
  if mapping[a]==mapping[b]:collapsed.append([a,b]);continue
  im=tuple(sorted((mapping[a],mapping[b])));mapped.setdefault(im,[]).append([a,b])
 assert set(mapped)==EE
 W=F(0);M=[F(0)]*3
 for fi,cy in enumerate(fs):
  assert all(dot(H[fi][:3],P[j])==H[fi][3]for j in cy)
  for j in range(1,len(cy)-1):
   tri=[P[k]for k in (cy[0],cy[j],cy[j+1])];v=det(*tri);assert v>0;W+=v/6
   for k in range(3):M[k]+=v*sum(p[k]for p in tri)/24
 newp=[tuple(map(F,p))for p in record['raw_vertices']];changed=[old for j,old in enumerate(ids)if any(F(H[old][k],H[old][3])!=F(raw['H'][j][k],raw['H'][j][3])for k in range(3))];same=[c2lex[i]for i,p in enumerate(P)if p==newp[mapping[i]]]
 keepers=[]
 for name,o in [('nine',[3,17,49,57,73,88,134,135,136]),('six',[71,94,109,116,119,126])]:
  sig=tuple(sorted(old2new[j]for j in o));v=byowner[sig];keepers.append(dict(identity=name,rawlex=v,original_owners=o,current_owners=list(sig),degree=len(sig)))
 assert not any({16,18,71,94}.issubset({ids[j]for j in o})for o in nn)
 dw=F(record['ordinary_volume'])-W
 return dict(parent_id='asg_RCec_cSHP9QT7MDzi-ldZ6Dy',original_support_ids=ids,deleted_original_supports=sorted(lost),old_VEF=[178,313,137],new_VEF=[record[k]for k in ['V','E','F']],parent_construction_to_rawlex=c2lex,parent_construction_to_new_rawlex=mapping,identified_classes=mergers,collapsed_parent_edges=sorted(collapsed),collapsed_parent_rawlex_edges=sorted(sorted([c2lex[a],c2lex[b]])for a,b in collapsed),coalesced_edge_images=[dict(new_edge=list(e),parent_edges=v)for e,v in sorted(mapped.items())if len(v)>1],discarded_facet_images=discarded,whole_maximal_complex_matches=True,true_edges_match=True,changed_retained_original_supports=changed,unchanged_parent_raw_vertices=sorted(same),protected_vertices=keepers,no_RL_owner=True,volume_change_sign=(dw>0)-(dw<0),volume_change_decimal=float(dw),centroid_change_decimal=[float(F(v)-m/W)for v,m in zip(record['raw_centroid'],M)])
if __name__=='__main__':
 p=Path(sys.argv[1]);spec=json.loads(Path(sys.argv[2]).read_text());out=run(json.loads((p/'A.json').read_text()),json.loads((p/'raw.json').read_text()),spec);(p/'COMPARISON.json').write_text(json.dumps(out,sort_keys=True,separators=(',',':')));print('BQ13_WHOLE_PARENT_QUOTIENT_COMPLEX_PASS')
