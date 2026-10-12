"""Export the verified rational C1374 body for viewing; keep exact source separate."""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import csv,gzip,json,sys,hashlib,re,math,zipfile
sys.set_int_max_str_digits(0)
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d import proj3d
import trimesh
PTH=Path(__file__).resolve().parent
report=json.loads((PTH/'REPLAY_REPORT.json').read_text())
assert report['status']=='FRESH_STANDARD_LIBRARY_COMPLETE_REPLAY_PASS'
assert report['VEF']==[258,687,431] and report['SUH']==[1,1,0] and report['C']==1374
assert not report['degeneracies']
r=json.loads((PTH/'verified/exact_report.json').read_text())
def rows(name):
 with gzip.open(PTH/'verified'/name,'rt') as f:return [tuple(map(int,row)) for row in csv.reader(f)]
ints=rows('vertices.csv.gz');T=rows('triangles.csv.gz');Q=int(r['centred_denominator'])
p=np.array([[float(Fraction(x,Q)) for x in row] for row in ints])
assert len(p)==258 and len(T)==512 and len(np.unique(p,axis=0))==258
cycles=r['maximal_cycles'];assert len(cycles)==431
stable=r['stable'][0];ui=r['unstable'][0]
assert set(stable)=={158,163,161} and ui==138
tri=p[np.array(T)];norm=np.cross(tri[:,1]-tri[:,0],tri[:,2]-tri[:,0]);area=np.linalg.norm(norm,axis=1)
assert np.all(area>0)
norm/=area[:,None]
stl=PTH/'gomboc_C1374_V258_view.stl'
lines=['solid gomboc_C1374_V258_view']
for idx,t in enumerate(T):
 lines.append('  facet normal '+' '.join(format(x,'.17g') for x in norm[idx]));lines.append('    outer loop')
 for v in t:lines.append('      vertex '+' '.join(format(x,'.17g') for x in p[v]))
 lines+=['    endloop','  endfacet']
lines+=['endsolid gomboc_C1374_V258_view']
stl.write_text('\n'.join(lines)+'\n',encoding='ascii')
# Parse serialized decimals explicitly; bound error against exact rationals.
tokens=re.findall(r'^\s*vertex\s+(\S+)\s+(\S+)\s+(\S+)\s*$',stl.read_text(),re.M)
assert len(tokens)==1536
largest=Fraction(0)
for tok,v in zip(tokens,[v for t in T for v in t]):
 for a in range(3):largest=max(largest,abs(Fraction(tok[a])-Fraction(ints[v][a],Q)))
assert largest<Fraction(1,10**15)
# Independent standard STL loader and exact binary64 readback.
mesh=trimesh.load_mesh(stl,file_type='stl',process=False)
assert np.array_equal(mesh.triangles,tri)
verts,inverse=np.unique(mesh.vertices,axis=0,return_inverse=True)
clean=trimesh.Trimesh(vertices=verts,faces=inverse[mesh.faces],process=False)
assert len(clean.vertices)==258 and len(clean.faces)==512
assert clean.is_watertight and clean.is_winding_consistent and clean.euler_number==2
assert clean.volume>0 and np.all(clean.area_faces>0)
exactvol=float(Fraction(int(r['W']),6*int(r['raw_denominator'])**3))
assert abs(clean.volume/exactvol-1)<1e-12
polys=[p[cy] for cy in cycles]
normals=np.array([np.cross(x[1]-x[0],x[2]-x[0]) for x in polys]);normals/=np.linalg.norm(normals,axis=1)[:,None]
sf=next(i for i,cy in enumerate(cycles) if set(cy)==set(stable))
S=normals[sf]*np.dot(normals[sf],p[stable[0]]);U=p[ui]
light=np.array([-.3,-.4,1.]);light/=np.linalg.norm(light)
shade=.70+.19*np.maximum(normals@light,0);colors=np.repeat(shade[:,None],3,axis=1);colors[sf]=to_rgb('#346a9b')
centre=(p.max(axis=0)+p.min(axis=0))/2;radius=np.ptp(p,axis=0).max()*.56
sdir=normals[sf];udir=U/np.linalg.norm(U);side=np.cross(sdir,udir)
if np.linalg.norm(side)<1e-5:side=np.cross(sdir,np.array([0.,0.,1.]))
side/=np.linalg.norm(side)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12})
fig=plt.figure(figsize=(18,7.5),dpi=160,facecolor='white')
fig.text(.04,.94,'Polyhedral Gömböc — C = 1374',fontsize=23,color='#20242a')
fig.text(.04,.895,'258-vertex construction · Orthographic views at equal scale · Equilibria checked on exact rational coordinates',fontsize=12,color='#555b61')
for index,(direction,title) in enumerate([(sdir,'(a) Stable-face view'),(udir,'(b) Unstable-vertex view'),(side,'(c) Side view')]):
 azim=math.degrees(math.atan2(direction[1],direction[0]));elev=math.degrees(math.asin(direction[2]))
 ax=fig.add_axes([.01+index/3,.16,.313,.69],projection='3d',computed_zorder=False);ax.set_proj_type('ortho')
 ax.add_collection3d(Poly3DCollection(polys,facecolors=colors,edgecolors=(.16,.16,.16,.45),linewidths=.35,zorder=1))
 for setter,c in zip((ax.set_xlim,ax.set_ylim,ax.set_zlim),centre):setter(c-radius,c+radius)
 ax.set_box_aspect((1,1,1),zoom=1.3);ax.view_init(elev=elev,azim=azim);ax.set_axis_off()
 for point,label,color,visible in [(S,'S','#235582',np.dot(normals[sf],direction)>1e-8),(U,'U','#ad3638',max(np.dot(normals[i],direction) for i,cy in enumerate(cycles) if ui in cy)>1e-8)]:
  if visible:
   ax.plot(*point[:,None],marker='o',markersize=4,color=color,zorder=10)
   x,y,_=proj3d.proj_transform(*point,ax.get_proj())
   ax.annotate(label,(x,y),xytext=(-22,22) if label=='S' else (22,22),textcoords='offset points',fontsize=17,color=color,arrowprops={'arrowstyle':'-','color':color,'lw':.8},zorder=12)
 fig.text((index+.5)/3,.17,title,ha='center',fontsize=13)
fig.text(.5,.105,'V = 258 · E = 687 · F = 431     |     S = 1 · U = 1 · H = 0',ha='center',fontsize=15)
fig.text(.5,.061,'S: stable face (blue) · U: unstable vertex (red) · Uniform volume density',ha='center',fontsize=11,color='#515961')
fig.text(.5,.025,'Unexaggerated proportions. Display mesh: 512 triangles; 81 coplanar diagonals are not true edges. Exact source supplied separately.',ha='center',fontsize=10,color='#666d75')
png=PTH/'gomboc_C1374_views.png';fig.savefig(png,facecolor='white');plt.close(fig)
delivery={'exact_source_sha256':report['capsule_sha256'],'exact_VEF':report['VEF'],'exact_SUH':report['SUH'],'exact_C':report['C'],'exact_checks':report['status'],'stl_role':'Rounded viewing copy, not an exact rational certificate; coplanarity and equilibrium class are certified for the rational source only.','max_absolute_coordinate_error':float(largest),'trimesh':{'vertices':len(clean.vertices),'triangles':len(clean.faces),'watertight':bool(clean.is_watertight),'winding_consistent':bool(clean.is_winding_consistent),'euler':int(clean.euler_number),'volume':float(clean.volume)},'unchanged_binary64_triangle_coordinates':True}
(PTH/'DELIVERY_CHECKS.json').write_text(json.dumps(delivery,indent=2)+'\n')
print(json.dumps(delivery,indent=2))
