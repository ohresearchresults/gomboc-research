# material-94f0925c2e22

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

# BASE_CLOSING_EXIT_GRAM_EXPLORATION_V1 — полная численная история, НЕ ДОКАЗАТЕЛЬСТВО

## Смысл и диспозиция

Эта единица сохраняет все15 фактически выполненных Gram-dual locator запусков: три общие релаксации base closing, каждая при slope=0,8,16,24,32, в указанном порядке с warm start между соседними slope. Она участвовала в обнаружении структуры точного TWO_APEX_BASE_ESCAPE_SUPPORT_497_V1, но численные значения, статусы success, матрицы и собственные значения не принимаются как непрерывные сертификаты, тела или границы C_min.

Модели plain, apex, base различаются допущением о выходе второго апекса: без дополнительного выхода, z->x, z->w∈B соответственно. Максимальная базовая b, замыкающая базовая y и z сохраняются раздельными. В base добавляется отдельная w, не подменяющая b. Целевая функция — |q|²-slope*|y|². В исходнике буквально заданы все равенства/неравенства, начальные multipliers, условия и nondefault параметры. SLSQP ограничивает численные eigenvalues, поэтому даже success не означает PSD; малые отрицательные eigenvalues остаются в контрольных записях.

Наблюдённые цели при перечисленных slope:
plain: около9,1,-7,-15,-23;
apex: около14.8017388251,11.4426783151,7.46156481484,2.73807425190,-2.71648893785;
base: около32.1728068291,28.0311702336,22.9527178609,17.1425700566,10.8154743769.

Это наблюдения оптимизатора, не доказанные оптимумы. Ни один набор не назван ownCOM110-конструкцией. Именно обнуление y-множителей при base/slope0 подсказало endpoint-free двухквадратную лемму; её окончательные рациональные коэффициенты получены аналитически и сохранены отдельно.

## Фактическая среда и команды

CPython3.13.5, NumPy2.3.5, SciPy1.17.0, переменная окружения OPENBLAS_NUM_THREADS=1. Случайных чисел или seed нет. Из каталога с неизменным исходником выполнены:

OPENBLAS_NUM_THREADS=1 python base5_locator.py plain 0 8 16 24 32
OPENBLAS_NUM_THREADS=1 python base5_locator.py apex 0 8 16 24 32
OPENBLAS_NUM_THREADS=1 python base5_locator.py base 0 8 16 24 32

Повторный solver-run в другой библиотечной/BLAS среде не обещает побайтной идентичности. Поэтому part2 хранит все literal наблюдённые checkpoints, включая каждую матрицу S, весь вектор множителей, все eigenvalues, итерации и сообщения. Стандартнобиблиотечное восстановление этих исторических JSON задано ниже и не вызывает solver.

## Полный исходник base5_locator.py

Сохранить следующий блок UTF-8/LF с последнимLF. Размер2516bytes,SHA256 **027bf68534f034d7f493ce0e06d16cba5efd6e9302c28255a6657e0b027a0bd3**.

```python
"""Exploratory Gram dual bounds for two-apex base closing; NOT exact proofs.
Run: python base5_locator.py [plain|apex|base] [slope ...]
SciPy SLSQP; full parameters and selected checkpoints emitted as JSON.
"""
import json, sys, platform
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import minimize

def problem(kind, slope):
 n=7 if kind=='base' else 6
 # x, max-base b, second apex z, closing-base y, L0 q, base pole B[, escape target w]
 def D(i,j):
  a=np.zeros((n,n)); a[i,j]+=0.5; a[j,i]+=0.5; return a
 E=[D(0,0), D(0,4),D(3,4),D(1,5),D(3,5)]
 e=[1]*5
 I=[D(0,5)+D(2,5), D(5,5)-D(4,5),D(1,4),D(2,4),
    D(1,1)-D(0,1),D(3,3)-D(0,3),D(2,2)-D(1,1),
    D(3,3)-D(1,1),D(1,1)]
 d=[-2,0,1,1,0,0,0,0,1]
 if kind=='apex':I.append(D(2,2)-D(0,2));d.append(0)
 elif kind=='base':
  E.append(D(5,6));e.append(1)
  I += [D(2,2)-D(2,6),D(6,6)-D(1,1),D(4,6)]
  d += [0,0,1]
 C=D(4,4)-slope*D(3,3)
 return np.array(E),np.array(e,dtype=float),np.array(I),np.array(d,dtype=float),C

def solve(kind,slope,initial=None):
 E,e,I,d,C=problem(kind,slope);k=len(E);m=len(I)
 mats=np.concatenate((-E,I)); cost=np.concatenate((-e,d))
 def S(v):return C+np.einsum('i,ijk->jk',v,mats)
 def eig(v):return np.linalg.eigvalsh(S(v))
 def jac(v):
  _,Q=np.linalg.eigh(S(v));return np.einsum('ik,aij,jk->ka',Q,mats,Q)
 v=np.zeros(k+m);v[0]=-2000;v[k:]=.01
 v[k+1]=1;v[k+4]=80;v[k+5]=slope+20;v[k+6]=20;v[k+7]=10
 if kind=='base':v[k+10]=10
 if initial is not None:v=initial
 sol=minimize(lambda z:float(cost@z),v,jac=lambda z:cost,method='SLSQP',
  bounds=[(None,None)]*k+[(0,None)]*m,
  constraints=[{'type':'ineq','fun':eig,'jac':jac}],
  options={'maxiter':3000,'ftol':1e-10,'disp':False})
 return {'kind':kind,'slope':slope,'objective_q2_minus_slope_y2':-float(sol.fun),
 'success':bool(sol.success),'message':sol.message,'nit':int(sol.nit),
 'v':sol.x.tolist(),'eig':eig(sol.x).tolist(),'S':S(sol.x).tolist()}

if __name__=='__main__':
 kind=sys.argv[1] if len(sys.argv)>1 else 'plain'
 slopes=list(map(float,sys.argv[2:])) or [0,8,16,24,32,48]
 rows=[];last=None
 for slope in slopes:
  row=solve(kind,slope,last);rows.append(row);last=np.array(row['v'])
  print(kind,slope,row['objective_q2_minus_slope_y2'],row['success'],row['eig'][0],flush=True)
 out={'scope':'NUMERIC_LOCATOR_NOT_PROOF_NOT_BODY','python':platform.python_version(),
 'numpy':np.__version__,'scipy':scipy.__version__,'rows':rows}
 path=Path('base5_'+kind+'_locator.json');path.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
```

## Восстановление наблюдённых файлов из полного literal part2

Part2 сохранить как locator_checkpoints_compact.json, без Markdown-fences. Он является обычным незакодированным JSON-object с именами трёх исходных файлов в качестве ключей. Необходима вся literal запись, не только значения целей.

Следующий полный стандартнобиблиотечный скрипт сохранить как recover_base5_checkpoints.py и выполнить `python -S recover_base5_checkpoints.py`. Он восстанавливает первоначальные JSON побайтно и проверяет каждый pin. Форматирование sort_keys=True,indent=2 и последнийLF является частью определения исторических байтов.

```python
from pathlib import Path
import hashlib,json
assert __debug__
pins={
 'base5_plain_locator.json':(9738,'8f4407a765c5cb7354624e18b7b9cb85c4fd921888d0cc8d4c7e56ab440436f7'),
 'base5_apex_locator.json':(9959,'345d1f4480075e797dda0c34c9d993d5bb6e81f3439267e30d4246c54d77d6e1'),
 'base5_base_locator.json':(11798,'0b0b078ba4fc39d7e8aa145d651808c50209150dd5f8931122b172dfb3cecfc1')}
objects=json.loads(Path('locator_checkpoints_compact.json').read_text(encoding='utf-8'))
assert set(objects)==set(pins)
for name,obj in sorted(objects.items()):
 assert obj['scope']=='NUMERIC_LOCATOR_NOT_PROOF_NOT_BODY'
 assert [r['slope'] for r in obj['rows']]==[0,8,16,24,32]
 b=(json.dumps(obj,sort_keys=True,indent=2)+'\n').encode('utf-8')
 assert (len(b),hashlib.sha256(b).hexdigest())==pins[name]
 p=Path(name)
 if p.exists():assert p.read_bytes()==b
 p.write_bytes(b)
 print(name,len(b),hashlib.sha256(b).hexdigest())
print('BASE5_ALL_15_NUMERIC_CHECKPOINTS_EXACT_RECOVERY_PASS')
```

Критерий приёмки истории — все три pins и последняя строка BASE5_ALL_15_NUMERIC_CHECKPOINTS_EXACT_RECOVERY_PASS. Это восстановление точных записей поиска, не научная верификация численного оптимума. Значительные выводы принимаются только из отдельно сохранённых рациональных тождеств и непрерывных доказательств.
