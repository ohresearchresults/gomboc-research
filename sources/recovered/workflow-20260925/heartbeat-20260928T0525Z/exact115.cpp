// J115 exact rational H-polyhedron audit. C++17 and GMP/GMPXX.
// Based on the fully read J90 exact90.cpp mass/census/bar methodology.
// This is a new source unit, not byte-identical exact90.cpp.
#include <gmpxx.h>
#include <array>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cassert>
#include <numeric>
#include <tuple>
using Z=mpz_class; using Q=mpq_class;
template<class T> using Vec=std::array<T,3>;
using IZ=Vec<Z>; using VQ=Vec<Q>;
template<class T> T dot(const Vec<T>&a,const Vec<T>&b){T z=0;for(int k=0;k<3;k++)z+=a[k]*b[k];return z;}
template<class T> Vec<T> sub(const Vec<T>&a,const Vec<T>&b){return {T(a[0]-b[0]),T(a[1]-b[1]),T(a[2]-b[2])};}
template<class T> Vec<T> add(const Vec<T>&a,const Vec<T>&b){return {T(a[0]+b[0]),T(a[1]+b[1]),T(a[2]+b[2])};}
template<class T> Vec<T> mul(const Vec<T>&a,const T&s){return {T(a[0]*s),T(a[1]*s),T(a[2]*s)};}
template<class T> Vec<T> cross(const Vec<T>&a,const Vec<T>&b){return {T(a[1]*b[2]-a[2]*b[1]),T(a[2]*b[0]-a[0]*b[2]),T(a[0]*b[1]-a[1]*b[0])};}
Q rat(const Z&a,const Z&b){assert(b!=0);Q r(a,b);r.canonicalize();return r;}
VQ qvec(const IZ&v){return {Q(v[0]),Q(v[1]),Q(v[2])};}
struct Point{IZ n;Z d;bool operator<(const Point&o)const{return std::tie(n,d)<std::tie(o.n,o.d);}};
Point reduce(IZ a,Z d){assert(d!=0);if(d<0){d=-d;for(auto&x:a)x=-x;}Z gg=d;for(auto&x:a)mpz_gcd(gg.get_mpz_t(),gg.get_mpz_t(),x.get_mpz_t());d/=gg;for(auto&x:a)x/=gg;return {a,d};}
VQ toq(const Point&p){return {rat(p.n[0],p.d),rat(p.n[1],p.d),rat(p.n[2],p.d)};}
Point hom(const VQ&x){Z d=1;for(auto&a:x)mpz_lcm(d.get_mpz_t(),d.get_mpz_t(),a.get_den().get_mpz_t());IZ n;for(int i=0;i<3;i++)n[i]=x[i].get_num()*(d/x[i].get_den());return reduce(n,d);}
void vprint(const VQ&v){std::cout<<"[\""<<v[0]<<"\",\""<<v[1]<<"\",\""<<v[2]<<"\"]";}
void ilist(const std::vector<int>&v){std::cout<<"[";for(size_t i=0;i<v.size();i++){if(i)std::cout<<",";std::cout<<v[i];}std::cout<<"]";}
void pairs(const std::vector<std::array<int,2>>&v){std::cout<<"[";for(size_t i=0;i<v.size();i++){if(i)std::cout<<",";std::cout<<"["<<v[i][0]<<","<<v[i][1]<<"]";}std::cout<<"]";}
struct Bar{int root,a,b;Q birth,death,depth;};
std::vector<Bar> bars(const std::vector<VQ>&v,const std::vector<std::array<int,2>>&edges){
 std::vector<Point>x;std::vector<Z>A;std::vector<Q>r;for(auto&a:v){auto p=hom(a);x.push_back(p);A.push_back(dot(p.n,p.n));r.push_back(rat(A.back(),Z(p.d*p.d)));}
 struct Event{Q level;int a,b;};std::vector<Event>ev;
 for(auto&e:edges){int a=e[0],b=e[1];Z C=dot(x[a].n,x[b].n),d=x[a].d,f=x[b].d;Q lev;
  if(C*d>=A[a]*f)lev=r[a];else if(C*f>=A[b]*d)lev=r[b];else{IZ z=cross(x[a].n,x[b].n);Z den=A[a]*f*f+A[b]*d*d-2*C*d*f;assert(den>0);lev=rat(dot(z,z),den);}ev.push_back({lev,a,b});}
 std::sort(ev.begin(),ev.end(),[](const Event&a,const Event&b){if(a.level!=b.level)return a.level>b.level;return std::tie(a.a,a.b)<std::tie(b.a,b.b);});
 std::vector<int>par(v.size());std::iota(par.begin(),par.end(),0);
 auto root=[&](int i){while(par[i]!=i){par[i]=par[par[i]];i=par[i];}return i;};
 std::vector<Bar>out;for(auto&e:ev){int a=root(e.a),b=root(e.b);if(a==b)continue;if(r[a]<r[b]||(r[a]==r[b]&&a>b))std::swap(a,b);assert(r[b]>=e.level);if(r[b]>e.level)out.push_back({b,e.a,e.b,r[b],e.level,Q(1-e.level/r[b])});par[b]=a;}
 for(size_t i=1;i<v.size();i++)assert(root(i)==root(0));
 std::sort(out.begin(),out.end(),[](const Bar&a,const Bar&b){if(a.depth!=b.depth)return a.depth>b.depth;return std::tie(a.root,a.a,a.b)<std::tie(b.root,b.a,b.b);});return out;
}
void barprint(const std::vector<Bar>&b){std::cout<<"[";for(size_t i=0;i<b.size();i++){if(i)std::cout<<",";auto&a=b[i];std::cout<<"{\"root\":"<<a.root<<",\"edge\":["<<a.a<<","<<a.b<<"],\"birth\":\""<<a.birth<<"\",\"death\":\""<<a.death<<"\",\"depth\":\""<<a.depth<<"\"}";}std::cout<<"]";}
int main(){
 int m;Z D;assert(std::cin>>m>>D);assert(m>=4&&D>=0);std::vector<IZ>n(m);std::vector<Z>hh(m,D);for(int i=0;i<m;i++){for(auto&x:n[i])assert(std::cin>>x);if(D==0)assert(std::cin>>hh[i]);assert(hh[i]>0);}
 std::set<Point>all;std::array<bool,6>bound{};std::array<std::array<int,3>,6>bt{};std::array<IZ,6>bc{};std::array<Z,6>bd{};
 for(int i=0;i<m;i++)for(int j=i+1;j<m;j++)for(int k=j+1;k<m;k++){
  IZ u=cross(n[j],n[k]),v=cross(n[k],n[i]),w=cross(n[i],n[j]);Z det=dot(n[i],u);if(det==0)continue;
  for(int l=0;l<3;l++)for(int s=0;s<2;s++)if(!bound[2*l+s]){int sign=s?-1:1;IZ c={Z(sign*u[l]),Z(sign*v[l]),Z(sign*w[l])};Z dd=det;if(dd<0){dd=-dd;for(auto&t:c)t=-t;}if(*std::min_element(c.begin(),c.end())>=0){bound[2*l+s]=true;bt[2*l+s]={i,j,k};bc[2*l+s]=c;bd[2*l+s]=dd;}}
  Point p=reduce(add(add(mul(u,hh[i]),mul(v,hh[j])),mul(w,hh[k])),det);bool ok=true;for(int l=0;l<m;l++)if(dot(n[l],p.n)>hh[l]*p.d){ok=false;break;}if(ok)all.insert(p);
 }
 for(bool b:bound)assert(b);std::cerr<<"EXACT_H_TRIPLES_DONE "<<all.size()<<"\n";std::vector<Point>hp(all.begin(),all.end());int V=hp.size();assert(V>=4);std::vector<VQ>x;for(auto&p:hp)x.push_back(toq(p));
 std::vector<std::vector<int>>fv(m);for(int f=0;f<m;f++)for(int i=0;i<V;i++)if(dot(n[f],hp[i].n)==hh[f]*hp[i].d)fv[f].push_back(i);
 std::vector<int>active;for(int f=0;f<m;f++)if(fv[f].size()>=3){bool noncol=false;for(size_t j=2;j<fv[f].size();j++)if(dot(cross(sub(x[fv[f][1]],x[fv[f][0]]),sub(x[fv[f][j]],x[fv[f][0]])),qvec(n[f]))!=0)noncol=true;if(noncol)active.push_back(f);}
 int F=active.size();std::vector<std::array<int,2>>edges,dual,ef;std::map<std::array<int,2>,int>edgeindex;
 for(int a=0;a<F;a++)for(int b=a+1;b<F;b++){
  std::vector<int>is;std::set_intersection(fv[active[a]].begin(),fv[active[a]].end(),fv[active[b]].begin(),fv[active[b]].end(),std::back_inserter(is));if(is.size()<2)continue;assert(is.size()==2);std::array<int,2>e={is[0],is[1]};assert(!edgeindex.count(e));edgeindex[e]=edges.size();edges.push_back(e);dual.push_back({a,b});ef.push_back({active[a],active[b]});
 }
 int E=edges.size();assert(V-E+F==2);std::vector<std::vector<int>>faces;std::vector<int>used(V,0),edgeuse(E,0);Q W=0;VQ M={0,0,0};
 for(int fi=0;fi<F;fi++){
  int f=active[fi];std::map<int,std::vector<int>>adj;for(int ei=0;ei<E;ei++)if(ef[ei][0]==f||ef[ei][1]==f){auto e=edges[ei];adj[e[0]].push_back(e[1]);adj[e[1]].push_back(e[0]);edgeuse[ei]++;}assert(adj.size()==fv[f].size());for(auto&a:adj)assert(a.second.size()==2);
  std::vector<int>cy;int start=adj.begin()->first,prev=-1,cur=start;do{cy.push_back(cur);auto ns=adj[cur];int next=(ns[0]==prev)?ns[1]:ns[0];prev=cur;cur=next;assert(cy.size()<=adj.size());}while(cur!=start);assert(cy.size()==adj.size());
  if(dot(cross(sub(x[cy[1]],x[cy[0]]),sub(x[cy[2]],x[cy[0]])),qvec(n[f]))<0)std::reverse(cy.begin()+1,cy.end());
  // Verify all polygon vertices, its orientation and each maximal facet exactly.
  for(size_t j=0;j<cy.size();j++){int a=cy[j],b=cy[(j+1)%cy.size()];for(int t:cy)if(t!=a&&t!=b)assert(dot(qvec(n[f]),cross(sub(x[b],x[a]),sub(x[t],x[a])))>0);}
  for(auto i:cy)used[i]++;
  for(size_t j=1;j+1<cy.size();j++){auto a=x[cy[0]],b=x[cy[j]],c=x[cy[j+1]];Q w=dot(a,cross(b,c));assert(w>0);W+=w;M=add(M,mul(add(add(a,b),c),w));}faces.push_back(cy);
 }
 for(int k:edgeuse)assert(k==2);for(int k:used)assert(k>=3);assert(W>0);Q volume=W/6;VQ g=mul(M,Q(1/(4*W)));std::vector<VQ>p,q;for(auto&a:x)p.push_back(sub(a,g));for(int f:active){VQ nn=qvec(n[f]);Q h=hh[f]-dot(nn,g);assert(h>0);q.push_back(mul(nn,Q(1/h)));}
 VQ c={0,0,0};for(auto&a:x)c=add(c,a);c=mul(c,Q(1,V));Q vol2=0;VQ mom2={0,0,0};
 for(auto&cy:faces)for(size_t j=1;j+1<cy.size();j++){auto a=x[cy[0]],b=x[cy[j]],d=x[cy[j+1]];Q v=dot(sub(a,c),cross(sub(b,c),sub(d,c)))/6;assert(v>0);vol2+=v;mom2=add(mom2,mul(add(add(a,b),add(c,d)),Q(v/4)));}assert(vol2==volume&&mul(mom2,Q(1/vol2))==g);
 std::cerr<<"EXACT_MASS_DONE\n";std::vector<int>S,U,WS,WU;std::vector<std::array<int,2>>H,WH;std::array<int,3>zero={0,0,0};std::vector<std::vector<int>>vadj(V);for(auto&e:edges){vadj[e[0]].push_back(e[1]);vadj[e[1]].push_back(e[0]);}
 for(int i=0;i<V;i++){bool neg=true,nonpos=true;for(int j:vadj[i]){Q z=dot(p[i],sub(p[j],p[i]));if(z==0)zero[1]++;if(z>=0)neg=false;if(z>0)nonpos=false;}if(neg)U.push_back(i);else if(nonpos)WU.push_back(i);}
 for(int fi=0;fi<F;fi++){int f=active[fi];VQ nn=qvec(n[f]);Q h=hh[f]-dot(nn,g);VQ foot=add(g,mul(nn,Q(h/dot(nn,nn))));bool pos=true,nonneg=true;auto cy=faces[fi];for(size_t j=0;j<cy.size();j++){int a=cy[j],b=cy[(j+1)%cy.size()];Q z=dot(nn,cross(sub(x[b],x[a]),sub(foot,x[a])));if(z==0)zero[0]++;if(z<=0)pos=false;if(z<0)nonneg=false;}if(pos)S.push_back(fi);else if(nonneg)WS.push_back(fi);}
 for(int ei=0;ei<E;ei++){int a=edges[ei][0],b=edges[ei][1];VQ d=sub(p[b],p[a]),n1=qvec(n[ef[ei][0]]),n2=qvec(n[ef[ei][1]]);Q dd=dot(d,d),T=-dot(p[a],d);VQ rr=add(mul(p[a],dd),mul(d,T));Q aa=dot(n1,n1),bb=dot(n2,n2),ab=dot(n1,n2);assert(aa*bb-ab*ab>0);Q X=dot(rr,n1)*bb-dot(rr,n2)*ab,Y=dot(rr,n2)*aa-dot(rr,n1)*ab;std::array<Q,4>guards={T,Q(dd-T),X,Y};bool pos=true,nonneg=true;for(auto&z:guards){if(z==0)zero[2]++;if(z<=0)pos=false;if(z<0)nonneg=false;}if(pos)H.push_back(edges[ei]);else if(nonneg)WH.push_back(edges[ei]);}
 std::cerr<<"EXACT_DIRECT_CENSUS_DONE\n";auto P=bars(p,edges),B=bars(q,dual);std::cerr<<"EXACT_BARS_DONE\n";if(WS.empty()&&WU.empty()&&WH.empty()){assert(S.size()+U.size()==H.size()+2);assert(P.size()+1==U.size());assert(B.size()+1==S.size());}
 auto global=[&](const std::vector<VQ>&v){std::vector<Point>h;std::vector<Z>A;for(auto&x:v){h.push_back(hom(x));A.push_back(dot(h.back().n,h.back().n));}std::vector<int>s,w;for(size_t i=0;i<v.size();i++){bool neg=true,np=true;for(size_t j=0;j<v.size();j++)if(i!=j){Z z=dot(h[i].n,h[j].n)*h[i].d-A[i]*h[j].d;if(z>=0)neg=false;if(z>0)np=false;}if(neg)s.push_back(i);else if(np)w.push_back(i);}return std::make_pair(s,w);};assert(global(p)==std::make_pair(U,WU));assert(global(q)==std::make_pair(S,WS));
 std::cout<<"{\"V\":"<<V<<",\"E\":"<<E<<",\"F\":"<<F<<",\"C\":"<<2*E<<",\"volume\":\""<<volume<<"\",\"centroid\":";vprint(g);std::cout<<",\"active_input_planes\":";ilist(active);std::cout<<",\"strict\":["<<S.size()<<","<<U.size()<<","<<H.size()<<"],\"weak\":["<<WS.size()<<","<<WU.size()<<","<<WH.size()<<"],\"primitive_zeros\":["<<zero[0]<<","<<zero[1]<<","<<zero[2]<<"],\"S\":";ilist(S);std::cout<<",\"U\":";ilist(U);std::cout<<",\"H\":";pairs(H);
 std::cout<<",\"vertices\":[";for(int i=0;i<V;i++){if(i)std::cout<<",";vprint(x[i]);}std::cout<<"],\"faces\":[";for(int i=0;i<F;i++){if(i)std::cout<<",";ilist(faces[i]);}std::cout<<"],\"edges\":";pairs(edges);std::cout<<",\"P\":";barprint(P);std::cout<<",\"Q\":";barprint(B);std::cout<<",\"boundedness\":[";for(int i=0;i<6;i++){if(i)std::cout<<",";std::cout<<"{\"indices\":["<<bt[i][0]<<","<<bt[i][1]<<","<<bt[i][2]<<"],\"numerators\":[\""<<bc[i][0]<<"\",\""<<bc[i][1]<<"\",\""<<bc[i][2]<<"\"],\"denominator\":\""<<bd[i]<<"\"}";}std::cout<<"],\"checks\":\"EXACT_HULL_MASS_DIRECT_GLOBAL_CENSUS_FULL_BARS_PASS\"}\n";
 std::cerr<<"J115_EXACT_PASS VEF="<<V<<"/"<<E<<"/"<<F<<" SUH="<<S.size()<<"/"<<U.size()<<"/"<<H.size()<<" weak="<<WS.size()<<WU.size()<<WH.size()<<" P="<<P.size()<<" Q="<<B.size()<<"\n";
}
