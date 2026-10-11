"""Deterministically generate a complete VF auditor from exact90.cpp.
The new frontend certifies a closed convex maximal-facet complex instead of
exhaustive H triples. The exact mass/census/bar engine is unchanged.
"""
from pathlib import Path
import hashlib
src=Path('exact90.cpp').read_text()
assert hashlib.sha256(src.encode()).hexdigest()=='ace049716ec9ca6a016a0001bacbf2ef3196b406bf58ee03656725a77b16fa64'
front=r'''int main(){
 int V,F;assert(std::cin>>V>>F);assert(V>=4&&F>=4);std::vector<VQ>x(V);for(auto&p:x)for(auto&a:p){assert(std::cin>>a);a.canonicalize();}
 std::set<Point>unique;for(auto&p:x)unique.insert(hom(p));assert(int(unique.size())==V);
 int m=F;std::vector<std::vector<int>>faces(F);std::vector<IZ>n(F);std::vector<Z>hh(F);std::vector<int>active(F);std::iota(active.begin(),active.end(),0);
 std::vector<std::array<int,2>>edges,dual,ef;std::map<std::array<int,2>,int>emap;
 for(int fi=0;fi<F;fi++){
  int k;assert(std::cin>>k);assert(k>=3);auto&cy=faces[fi];cy.resize(k);for(int&i:cy){assert(std::cin>>i);assert(i>=0&&i<V);}std::set<int>on(cy.begin(),cy.end());assert(int(on.size())==k);
  VQ nn=cross(sub(x[cy[1]],x[cy[0]]),sub(x[cy[2]],x[cy[0]]));Q h=dot(nn,x[cy[0]]);assert(h>0);
  Z den=h.get_den();for(auto&a:nn)mpz_lcm(den.get_mpz_t(),den.get_mpz_t(),a.get_den().get_mpz_t());Z gg=h.get_num()*(den/h.get_den());hh[fi]=gg;
  for(int j=0;j<3;j++){n[fi][j]=nn[j].get_num()*(den/nn[j].get_den());mpz_gcd(gg.get_mpz_t(),gg.get_mpz_t(),n[fi][j].get_mpz_t());}assert(gg>0);hh[fi]/=gg;for(auto&a:n[fi])a/=gg;
  for(int j=0;j<V;j++){Q s=h-dot(nn,x[j]);if(on.count(j))assert(s==0);else assert(s>0);}
  for(int j=0;j<k;j++){auto a=x[cy[j]],b=x[cy[(j+1)%k]],c=x[cy[(j+2)%k]];assert(dot(nn,cross(sub(b,a),sub(c,b)))>0);for(int v:cy)if(v!=cy[j]&&v!=cy[(j+1)%k])assert(dot(nn,cross(sub(b,a),sub(x[v],a)))>0);
   std::array<int,2>e={cy[j],cy[(j+1)%k]};if(e[0]>e[1])std::swap(e[0],e[1]);
   if(emap.count(e)){int ei=emap[e];assert(ef[ei][1]==-1);ef[ei][1]=fi;dual[ei][1]=fi;}else{emap[e]=edges.size();edges.push_back(e);ef.push_back({fi,-1});dual.push_back({fi,-1});}
  }
 }
 int E=edges.size();assert(V-E+F==2);std::vector<std::vector<int>>incident(V),fadj(F);for(int i=0;i<F;i++)for(int v:faces[i])incident[v].push_back(i);
 for(auto&e:ef){assert(e[1]>=0);fadj[e[0]].push_back(e[1]);fadj[e[1]].push_back(e[0]);}
 for(int vi=0;vi<V;vi++){auto&a=incident[vi];bool rank=false;for(size_t i=0;i<a.size();i++)for(size_t j=i+1;j<a.size();j++)for(size_t k=j+1;k<a.size();k++)if(dot(n[a[i]],cross(n[a[j]],n[a[k]]))!=0)rank=true;assert(rank);}
 std::set<int>seen={0};std::vector<int>todo={0};for(size_t i=0;i<todo.size();i++)for(int j:fadj[todo[i]])if(seen.insert(j).second)todo.push_back(j);assert(int(seen.size())==F);
 // Every listed polygon is a genuine convex-hull facet, with its entire vertex
 // set checked exactly. The list is closed under true-edge adjacency, and is
 // connected, hence it is the complete boundary of the bounded convex hull.
 Q W=0;VQ M={0,0,0};for(auto&cy:faces)for(size_t j=1;j+1<cy.size();j++){auto a=x[cy[0]],b=x[cy[j]],c=x[cy[j+1]];Q w=dot(a,cross(b,c));assert(w>0);W+=w;M=add(M,mul(add(add(a,b),c),w));}
 assert(W>0);Q volume=W/6;VQ g=mul(M,Q(1/(4*W)));std::vector<VQ>p,q;for(auto&a:x)p.push_back(sub(a,g));for(int f:active){VQ nn=qvec(n[f]);Q h=hh[f]-dot(nn,g);assert(h>0);q.push_back(mul(nn,Q(1/h)));}
 std::cerr<<"EXACT_VF_HULL_DONE "<<V<<" "<<E<<" "<<F<<"\n";
'''
start=src.index(' // Second exact mass sum')
tail=src[start:]
# The finite convex hull is bounded without H-conic certificates.
lo=tail.index('std::cout<<",\\\"boundedness')
hi=tail.index(' std::cerr<<"J90_EXACT_PASS',lo)
tail=tail[:lo]+'std::cout<<",\\\"checks\\\":\\\"EXACT_VF_HULL_MASS_DIRECT_GLOBAL_CENSUS_FULL_BARS_PASS\\\"}\\n";\n'+tail[hi:]
out=src[:src.index('int main(){')]+front+tail
out=out.replace('J90_EXACT_PASS','J90_VF_EXACT_PASS')
Path('vfaudit90.cpp').write_text(out)
print('J90_VF_AUDITOR_GENERATED',len(out.encode()),hashlib.sha256(out.encode()).hexdigest())
