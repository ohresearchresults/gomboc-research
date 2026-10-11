# material-4b193195588c

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Exact checkpoint replay: no LP or floating optimizer is needed.
Run input, minimum_displacement, mechanical_factor4, wide_capacity16, counter
as separate --phase values, or use --phase all. See capsule manifest.
"""
import argparse,json,itertools,hashlib
from pathlib import Path
import core as c
from capacity import modes_for
RECIPE=json.loads(r'''
{"controller_material":[10,12,17,20,29,32,46,49,57,64,66,69,70,72],"controller_indices":[10,12,17,20,28,31,45,48,56,63,65,68,69,71],"recipes":[{"name":"minimum_displacement","factor":1,"pivot":[8,14,23],"fixed_coefficients":{"0":"-33031319671/1000000000000000","1":"33031319671/1000000000000000","2":"-33031319671/1000000000000000","3":"-790177823/200000000000000","4":"-15198835511/250000000000000","5":"27764022373/1000000000000000","6":"-20409551643/500000000000000","7":"-33031319671/1000000000000000","9":"-6990369749/125000000000000","10":"-13568113233/125000000000000","11":"75513586193/1000000000000000","12":"-936829494841/1000000000000000","13":"90379817517/100000000000000","15":"-3702957601/125000000000000","16":"-33031319671/1000000000000000","17":"14861614371/250000000000000","18":"825298949/31250000000000","19":"-33031319671/1000000000000000","20":"-33031319671/1000000000000000","21":"8558907161/250000000000000","22":"-33031319671/1000000000000000","24":"28787073741/1000000000000000","25":"-33031319671/1000000000000000","26":"20836086383/1000000000000000","27":"-33031319671/1000000000000000"}},{"name":"mechanical_factor4","factor":4,"pivot":[8,14,23],"fixed_coefficients":{"0":"-31908813837/200000000000000","1":"31908813837/200000000000000","2":"-31908813837/200000000000000","3":"-4770782189/250000000000000","4":"-146823323347/500000000000000","5":"134102577509/1000000000000000","6":"-7503477649/250000000000000","7":"-31908813837/200000000000000","9":"-67528154853/250000000000000","10":"-104856216121/200000000000000","11":"18236850571/50000000000000","12":"-2262482868221/500000000000000","13":"4365421667257/1000000000000000","15":"-94174906869/1000000000000000","16":"-31908813837/200000000000000","17":"1689219647/20000000000000","18":"-1967310603/250000000000000","19":"-31908813837/200000000000000","20":"65682092479/1000000000000000","21":"157149325827/1000000000000000","22":"-31908813837/200000000000000","24":"13897322913/1000000000000000","25":"-31908813837/200000000000000","26":"-9628453781/200000000000000","27":"-31908813837/200000000000000"},"float_rho":0.00015954406918523454},{"name":"wide_capacity16","factor":16,"pivot":[8,14,23],"fixed_coefficients":{"0":"-1792090718533/1000000000000000","1":"1792090718533/1000000000000000","2":"-294619055509/250000000000000","3":"-189760243571/200000000000000","4":"-3298407974399/1000000000000000","5":"31997024743/10000000000000","6":"68892517787/500000000000000","7":"-197635196021/500000000000000","9":"-9626891579/15625000000000","10":"-1292824523789/250000000000000","11":"5295186894273/1000000000000000","12":"-2585621163161/1000000000000000","13":"198382611157/250000000000000","15":"-50175611267/15625000000000","16":"-1792090718533/1000000000000000","17":"-30216202111/125000000000000","18":"-592646369753/500000000000000","19":"-1792090718533/1000000000000000","20":"-975047411819/1000000000000000","21":"-306786773461/500000000000000","22":"-140027421903/100000000000000","24":"-478046420947/500000000000000","25":"-1792090718533/1000000000000000","26":"-815268912761/500000000000000","27":"-1744406829027/1000000000000000"},"float_rho":0.0017920907185326857}]}
''')

def input_body():
 K0=c.hull(c.parent_points());R0=c.mechanics(K0);assert R0['VEF']==[75,204,131] and R0['strict']==[2,2,2]
 x,ch=c.original_chart(K0);Y=c.construct(x,K0['faces'],ch,c.F(1,32));K=c.hull(Y);R=c.mechanics(K)
 assert K['material']==[i for i in range(75) if i!=27] and R['VEF']==[74,201,129] and R['strict']==[5,2,5]
 c.dump('postcontact_input.json',K);c.dump('postcontact_report.json',R);c.dump('original_chart.json',ch)
 print('J74_EXACT_INPUT_PASS',flush=True)
 return K

def endpoint(K,rec):
 X=K['points'];faces=K['faces'];V,M=c.mass(X,faces);verts=RECIPE['controller_indices'];assert [K['material'][i] for i in verts]==RECIPE['controller_material']
 assert all(sum(i in f for i in verts)<=1 for f in faces)
 modes,images=modes_for(X,faces,verts);pivot=rec['pivot'];coef=[c.F(0)]*len(modes);target=c.mul(M,-rec['factor'])
 assert set(map(int,rec['fixed_coefficients']))==set(range(len(modes)))-set(pivot)
 for k,v in rec['fixed_coefficients'].items():
  i=int(k);coef[i]=c.F(v);target=c.sub(target,c.mul(images[i],coef[i]))
 for i,a in zip(pivot,c.solve_columns([images[i] for i in pivot],target)):coef[i]=a
 Y=list(X)
 for a,(i,b) in zip(coef,modes):Y[i]=c.add(Y[i],c.mul(b,a))
 assert c.mass(Y,faces)==(V,c.mul(M,1-rec['factor'])) and c.valid_complex(Y,faces)
 H=c.hull(Y);R=c.mechanics(H);assert R['VEF']==[74,201,129] and R['strict']==[5,2,5] and R['weak']==R['zeros']==[0,0,0]
 out=Path('capacity_output');out.mkdir(exist_ok=True)
 c.dump(out/(rec['name']+'_body.json'),dict(points=Y,density=1))
 if rec['factor']==1:
  assert R['centroid']==c.ZERO
  disp=max(abs(float(y-x)) for p,q in zip(X,Y) for x,y in zip(p,q))
  receipt=dict(controller_material=RECIPE['controller_material'],controller_indices=verts,modes=modes,images=images,coefficients=coef,pivot=pivot,input_mass=c.mechanics(K),output_report=R,max_coordinate_displacement=disp,LP_status='floating nomination; full rational endpoint certified',original_material=K['material'])
  c.dump(out/'distributed_body.json',dict(points=Y,density=1));c.dump(out/'distributed_receipt.json',receipt)
 else:
  receipt=dict(factor=rec['factor'],report=R,modes=modes,images=images,coefficients=coef,pivot=pivot,original_material=K['material'],float_rho=rec['float_rho'])
  c.dump(out/('mechanical_factor'+str(rec['factor'])+'.json'),receipt)
  c.dump(out/('mechanical_factor'+str(rec['factor'])+'_candidate.json'),dict(points=Y,coefficients=coef,pivot=pivot,factor=rec['factor'],float_rho=rec['float_rho']))
 print('J74_FIXED_CHECKPOINT_PASS',rec['name'],R['VEF'],R['strict'],flush=True)
 return Y

def counter(K):
 X=K['points'];Y=c.convert(json.loads(Path('capacity_output/distributed_body.json').read_text()))['points'];Z=[c.add(x,c.mul(c.sub(y,x),4)) for x,y in zip(X,Y)];assert c.valid_complex(Z,K['faces']);V,M=c.mass(X,K['faces']);assert c.mass(Z,K['faces'])==(V,c.mul(M,-3));R=c.mechanics(c.hull(Z));assert R['VEF']==[74,201,129] and R['strict']==[6,7,11] and R['weak']==R['zeros']==[0,0,0]
 c.dump('capacity_output/minimum_ray_factor4_body.json',dict(points=Z,density=1));c.dump('capacity_output/factor4_report.json',dict(factor=4,report=R))
 print('J74_COUNTERCONTROL_6711_WEAK000_PASS',flush=True)

def main(phase):
 if phase in ['input','all']:K=input_body()
 else:K=c.convert(json.loads(Path('postcontact_input.json').read_text()))
 for rec in RECIPE['recipes']:
  if phase in [rec['name'],'all']:endpoint(K,rec)
 if phase in ['counter','all']:counter(K)
 print('J74_REPLAY_PHASE_PASS_NOT_110',phase,flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--phase',choices=['input','minimum_displacement','mechanical_factor4','wide_capacity16','counter','all'],default='all');main(p.parse_args().phase)
