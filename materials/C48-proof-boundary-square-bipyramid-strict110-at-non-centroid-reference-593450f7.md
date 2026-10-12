# material-593450f71892

AI research material

---

# Exact proof-boundary countercontrol: a square bipyramid can be strict110 at an arbitrary interior reference point

This object is not centred at its uniform-volume centroid. Its role is only to refute the proposed center-free statement that every ordinary bipyramid has S+U at least 3.

Equatorial square:
B0=(-1,-1,0), B1=(1,-1,0), B2=(1,1,0), B3=(-1,1,0).
Apices:
T=(-296352,252052,4358196)/10^6,
D=(369820,54247,-864080)/10^6.
The apex segment meets z=0 at
q=(16945952607/65278450000,113553037643/1305569000000), strictly inside the square, so the hull is the ordinary square bipyramid with facets
F0=(T,B0,B1), F1=(T,B1,B2), F2=(T,B2,B3), F3=(T,B3,B0),
F4=(D,B1,B0), F5=(D,B2,B1), F6=(D,B3,B2), F7=(D,B0,B3).

Reference point g is the positive convex combination of (B0,B1,B2,B3,T,D) with weights
(161176,132956,16829,15693,16097,657249)/10^6.
Thus g is strict interior, and explicitly
g=(52802361759/250000000000,-221898932453/1000000000000,-124440458727/250000000000).

The actual filled-volume centroid is
c=(-15187594303/326392250000,17896340093/326392250000,873529/1000000), so g!=c.

Stable-facet certificate: orthogonally project g to each facet plane and take the minimum barycentric coordinate. In F0..F7 order the exact minima are
-298780160006087381/5140376646280000000,
-14334917836658983/258430011029000000,
-34872965975509709/543147182920000000,
-16463481660758983/243612411029000000,
33604202425495235556909/232258872926125000000000,
-136752224466854575003/3574253371250000000000,
-11528538556941294943091/205135372926125000000000,
-252483092744663362503/8197003371250000000000.
Exactly F4 is strict stable.

Unstable-vertex certificate: the maximum outgoing dot (v-g)·(w-v) over true neighbours, in vertex order (B0,B1,B2,B3,T,D), is
85713883759090549/250000000000000000,
43142607277090549/250000000000000000,
58219141050590549/250000000000000000,
100790417532590549/250000000000000000,
-5112895190788590549/250000000000000000,
44590842229380269/1000000000000000000.
Exactly T is strict unstable.

Edge certificate. For e=a--b let t=((g-a)·(b-a))/|b-a|^2 and p=a+t(b-a). An edge equilibrium needs 0<t<1 and (g-p)·(v-p)>0 for every other vertex v.
Equator edges have interior t but a negative witness:
B0-B1: T gives -298780160006087381/250000000000000000;
B1-B2: T gives -14334917836658983/12500000000000000;
B2-B3: T gives -313856693779587381/250000000000000000;
B0-B3: T gives -16463481660758983/12500000000000000.
All four T edges have t<0:
B0-T -85713883759090549/5264156773256000000;
B1-T -43142607277090549/5560508773256000000;
B2-T -58219141050590549/5308456773256000000;
B3-T -100790417532590549/5012104773256000000.
For D edges:
B0-D has t=969851895734793423/1244825938603000000 and negative witness B3=-84161030914887787501/972520264533593750000;
B1-D has t=1747496793132380269/2255197815809000000 and negative witness B2=-136752224466854575003/1761873293600781250000;
B2-D has t=2082800658038380269/2038209815809000000>1;
B3-D has t=3244859552110380269/3517489815809000000 and negative witness B2=-11528538556941294943091/109921556744031250000000.
All signs are strict, so H=0 and there are no weak edge events.

Therefore the ordinary square bipyramid is exactly strict (S,U,H)=(1,1,0) at g, but not at its own centroid. It is a proof-boundary countercontrol only and does not solve or exclude the homogeneous own-centroid C48 problem.
