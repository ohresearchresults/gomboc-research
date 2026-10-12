# material-e993c696939a

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

# MASS_VOLUME_EXPLORATION_V1

Полная recovery-капсула ограниченного численного поиска, который помог найти точное семейство равенства для новой совместной массы. Это НЕ доказательство невозможности, не сертификат110 и не верхняя/нижняя граница сложности. Основной принятый результат уже имеет независимое непрерывное доказательство [internal-source-reference] и точный source [internal-source-reference].

Два реально выполненных поиска максимизировали g_x+g_y-3V/2-1/4 на оболочке стандартного ABCD и дополнительных точек. Число дополнительных точек3и5; начальные seed271828и314159. Каждый x,y ограничен[0.0001,5], z[-5,5]. Полные параметры и буквальные выходы ниже. Оба запуска завершились по maxiter150, success=false;16308и27180вычислений. Минимумы отрицательного запаса -1.1102230246251565e-15 и -1.5543122344752192e-15 имеют масштаб округления и НЕ являются контрпримерами. В первом лучшем hull только дополнительная точка6 стала вершиной, во втором только точка5; остальные дополнительные точки внутренние. Это подсказало настоящее пятивершинное семейство равенства, затем доказанное аналитически и проверенное рационально отдельно.

Среда выполненных запусков: CPython3.13.5,GCC14.2.0,NumPy2.3.5,SciPy1.17.0,OpenBLAS0.3.30 Haswell DYNAMIC_ARCH USE64BITINT. OPENBLAS_NUM_THREADS=1,OMP_NUM_THREADS=1. Все недефолтные параметры буквальны в source; для остальных используются дефолты указанной версии SciPy. Битовое совпадение при повторной плавающей оптимизации на иной платформе не обещается. Буквальные входные checkpoints и весь метод сохранены точно, поэтому математический след не зависит от будущей воспроизводимости оптимизатора.

Реально использованные команды поиска:
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python joint_mass_explore.py 271828 3
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python joint_mass_explore.py 314159 5

Для побайтового восстановления трёх файлов сохраните полный декодер ниже как recover_mass_exploration.py. Затем:
python -S recover_mass_exploration.py CAPSULE.md recovered
python -S recover_mass_exploration.py CAPSULE.md recovered --check
Ожидаемый маркер обоих шагов: MASS_VOLUME_EXPLORATION_LITERAL_RECOVERY_PASS 3 4023.
Побайтовое восстановление и check выполнены на этой капсуле в новом каталоге; SHA всех трёх совпали с исходными. Никаких внешних библиотек для recovery не требуется.

## Complete recovery source
```python
from pathlib import Path
import hashlib
import re
import sys
assert __debug__
PINS={
'joint_mass_explore.py':(1321,'e6791ac6a527623b3c11d408fb6b95f9b7a822ebef10525ab602acc6b66cfa96'),
'mass_search_271828_3.json':(1177,'3dba5c860286d1c07bde8f5fb1c3fb60090daae4e91e04ed83d6762575d4446a'),
'mass_search_314159_5.json':(1525,'7d1886a7217b39a26a13a6973a72bc5c1dd8526f4bc22232eb9250250b2dccea')}
if __name__=='__main__':
    assert len(sys.argv) in (3,4)
    check=len(sys.argv)==4
    if check: assert sys.argv[3]=='--check'
    text=Path(sys.argv[1]).read_text(encoding='utf-8')
    files=re.findall(r'^## File: ([^\n]+)\n```[^\n]*\n(.*?)^```\n',text,re.M|re.S)
    assert len(files)==len(PINS) and {n for n,_ in files}==set(PINS)
    out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
    for name,source in files:
        raw=source.encode('utf-8');count,digest=PINS[name]
        assert len(raw)==count and hashlib.sha256(raw).hexdigest()==digest
        if check: assert (out/name).read_bytes()==raw
        else: (out/name).write_bytes(raw)
    print('MASS_VOLUME_EXPLORATION_LITERAL_RECOVERY_PASS',len(files),sum(n for n,_ in PINS.values()))
```

## File: joint_mass_explore.py
```python
import json
import sys
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import differential_evolution
BASE=np.array([[0.,0.,0.],[0.,0.,1.],[0.,1.,0.],[1.,0.,0.]])
def vals(points):
    h=ConvexHull(points)
    interior=points.mean(0)
    triangles=points[h.simplices]
    weights=np.abs(np.linalg.det(triangles-interior))/6
    V=weights.sum()
    g=(weights[:,None]*(triangles.sum(1)+interior)/4).sum(0)/V
    return V,g,h

def objective(params):
    a=np.asarray(params).reshape(-1,3)
    pts=np.vstack([BASE, a])
    V,g,_=vals(pts)
    return -(g[0]+g[1] - 1.5*V-0.25)

if __name__=='__main__':
    seed=int(sys.argv[1]) if len(sys.argv)>1 else 271828
    n=int(sys.argv[2]) if len(sys.argv)>2 else 3
    bound=[(0.0001,5),(0.0001,5),(-5,5)]*n
    res=differential_evolution(objective,bound,popsize=12,maxiter=150,seed=seed,tol=1e-9,polish=False,workers=1)
    V,g,h=vals(np.vstack([BASE,res.x.reshape(-1,3)]))
    out=dict(seed=seed,n=n,bounds=bound,popsize=12,maxiter=150,tol=1e-9,polish=False,workers=1,nfev=res.nfev,success=res.success,message=res.message,x=res.x.tolist(),objective=float(res.fun),V=V,g=g.tolist(),simplices=h.simplices.tolist())
    path=f'mass_search_{seed}_{n}.json'
    open(path,'w').write(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(path,res.fun,V,g)
```

## File: mass_search_271828_3.json
```json
{
  "V": 1.010007234041224,
  "bounds": [
    [
      0.0001,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      -5,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      -5,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      -5,
      5
    ]
  ],
  "g": [
    1.2554133957482907,
    0.5095974553135464,
    -0.8465526727851407
  ],
  "maxiter": 150,
  "message": "Maximum number of iterations has been exceeded.",
  "n": 3,
  "nfev": 16308,
  "objective": -1.1102230246251565e-15,
  "polish": false,
  "popsize": 12,
  "seed": 271828,
  "simplices": [
    [
      2,
      6,
      0
    ],
    [
      1,
      2,
      0
    ],
    [
      1,
      2,
      6
    ],
    [
      3,
      6,
      0
    ],
    [
      3,
      1,
      0
    ],
    [
      3,
      1,
      6
    ]
  ],
  "success": false,
  "tol": 1e-09,
  "workers": 1,
  "x": [
    0.08857106894195343,
    0.6607913678153103,
    0.2541566351148916,
    0.5348944270361495,
    0.7738871442814672,
    -0.24648519283521741,
    4.816439963603539,
    1.2436034406438081,
    -4.386210691140562
  ]
}
```

## File: mass_search_314159_5.json
```json
{
  "V": 1.2322905436529044,
  "bounds": [
    [
      0.0001,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      -5,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      -5,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      -5,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      -5,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      0.0001,
      5
    ],
    [
      -5,
      5
    ]
  ],
  "g": [
    1.2224734543751508,
    0.8759623611042072,
    -0.45377514745864905
  ],
  "maxiter": 150,
  "message": "Maximum number of iterations has been exceeded.",
  "n": 5,
  "nfev": 27180,
  "objective": -1.5543122344752192e-15,
  "polish": false,
  "popsize": 12,
  "seed": 314159,
  "simplices": [
    [
      2,
      5,
      0
    ],
    [
      1,
      2,
      0
    ],
    [
      1,
      2,
      5
    ],
    [
      3,
      5,
      0
    ],
    [
      3,
      1,
      0
    ],
    [
      3,
      1,
      5
    ]
  ],
  "success": false,
  "tol": 1e-09,
  "workers": 1,
  "x": [
    1.2761919279643825,
    0.7173817379389664,
    -0.5048901247339321,
    4.498284498538685,
    2.8954587633787443,
    -2.8151005898345955,
    1.8926911501622723,
    1.072354043587568,
    -0.9647780237136622,
    0.8276556834581461,
    0.6250205705084251,
    -0.257694566215505,
    2.4607574424219676,
    1.5651712027630893,
    -1.4356249685851818
  ]
}
```

Все три SHA и byte counts проверяются полным декодером; хеши не заменяют приведённые буквальные данные. Дополнительный ранее испробованный локальный анзац на каждую противоположную грань отдельно опровергнут точным семиточечным телом в [internal-source-reference]; численная неудача поиска такого тела не была принята как теорема.
