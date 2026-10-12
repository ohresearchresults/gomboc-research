# figure-0428

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Bright Harbor 81 — площадь центрального сечения усиливает массовое препятствие

Ветка: `[internal-source-reference]`.

**Новый собственный110 здесь не заявляется. Получен самостоятельный математический результат: нижняя оценка радиуса противоположной части тела через действительную однородную массу, высоту положительного полюса и площадь центрального сечения.** Она усиливает прежнее необходимое условие `rho≥R/3` и даёт положительную нижнюю оценку полного радиального барьера даже в некоторых случаях, когда это прежнее условие уже выполнено.

## 1. Масса заставляет противоположную часть тела достигать определённого радиуса

Пусть K — полноразмерное выпуклое тело с **собственным центром однородного объёма в 0**. Выберем единичное направление e и обозначим:

`h = max{x·e : x∈K}`;

`A = area(K ∩ {x·e=0})`;

`B_minus = max{|x|² : x∈K, x·e≤0}`.

Тогда

**`B_minus ≥ h²(πh²+9A) / [9(πh²+A)]`.**

Это оценка для действительного заполненного тела. В ней не используются среднее вершин, свободный проверочный центр, сохранение старого графа свидетелей или неизменность гранной структуры.

При A→0 правая часть стремится к `h²/9`, то есть возвращает прежнюю массовую оценку высот. При положительной площади она строго больше `h²/9`.

### Доказательство

Положим `q=sqrt(B_minus)`. Отрицательная половина K лежит в шаре радиуса q. Обозначим через C(z) площадь сечения тела плоскостью `x·e=z`.

Пирамида с основанием центрального сечения и вершиной на высоте h содержится в K. Поэтому

`C(z) ≥ A(1−z/h)²`, для `0≤z≤h`,

и положительный первый момент удовлетворяет

`M_plus ≥ A h²/12`.

С другой стороны, соединение любого отрицательного сечения на высоте −u с той же верхней вершиной даёт в центральной плоскости уменьшенную копию этого сечения. Отсюда

`C(−u) ≤ A(1+u/h)²`.

Принадлежность отрицательной половины шару даёт ещё одну независимую оценку:

`C(−u) ≤ π(q²−u²)`, для `0≤u≤q`.

Собственное массовое центрирование требует `M_plus=M_minus`. После подстановки `t=h/q`, `alpha=A/(πq²)` получаем

`alpha t²/12 ≤ ∫_0^1 s min{alpha(1+s/t)², 1−s²} ds`.  (1)

Здесь `0<alpha≤1`.

Для `sqrt(3)<t<3` разделим интеграл в точке

`b=(t²−3)/(2t)`.

На `[0,b]` используем конусную оценку, на `[b,1]` — шаровую. Тогда

`alpha t²/12 ≤ alpha[b²/2+2b³/(3t)+b⁴/(4t²)] + (1−b²)²/4`.

Прямая алгебраическая подстановка b даёт

`alpha ≤ t²(9−t²)/[9(t²−1)]`.

Это равносильно заявленной оценке B_minus.

При `1<t≤sqrt(3)` та же конечная оценка следует уже из `alpha≤1`. При `t≤1` она очевидна, поскольку её правая часть меньше h². Значения `t≥3` исключаются непосредственно из (1): при t=3 полная конусная оценка дала бы равенство, но шаровая оценка строго уменьшает отрицательный момент на ненулевом интервале возле s=1; при t>3 противоречие ещё сильнее.

Таким образом, оценка действует во всех случаях, а не только в выбранном гладком или комбинаторном участке семейства.

## 2. Следствие для полного дополнительного радиального бассейна

Теперь выберем e в направлении глобально дальней вершины v. Тогда `R=|v|=h`. Пусть

`rho=max{|x| : x∈K, x·v=0}`.

Определим

`L(R,A)=R²(πR²+9A)/[9(πR²+A)]`.

Если

**`L(R,A)>rho²`,**

то в отрицательной половине есть вершина радиуса строго больше rho. Максимум радиуса этой половины достигается вне разделяющей плоскости и является строгой неустойчивой вершиной всего многогранника. Дальняя вершина v даёт другую строгую U.

Кроме того, каждый путь по настоящим рёбрам между двумя половинами пересекает центральное сечение. Поэтому имеется конечный радиальный бар с

**`bar ≥ L(R,A)−rho²`.**

Нормировка, используемая здесь и в исходном журнале, — деление на **глобальное R²**, а не на квадрат радиуса умирающего пика:

`bar/R² ≥ max(0, L(R,A)/R²−rho²/R²)`.

Это нижняя оценка полного бассейна. Малый локальный dot-дефект, исчезновение старой метки вершины или отбрасывание микроскопических положительных баров её не заменяют.

### Необходимое условие для собственного U1

Пусть `alpha=A/(πrho²)` и `t=R/rho`. Для собственного U1 необходимо

` t⁴−9(1−alpha)t²−9alpha ≤ 0`,

то есть

**`t² ≤ [9(1−alpha)+sqrt(81(1−alpha)²+36alpha)]/2`.**

Два полезных точных частных случая:

* При площади сечения, близкой к площади описанного диска, допустимое отношение R/rho приближается к `sqrt(3)`, а не к 3.
* Если `A/(πrho²)>20/27`, то необходимо **`R<2rho`**. Таким образом, даже `rho=R/2` может быть недостаточно.

Новая оценка не сильнее прямого измерения уже известного полного отрицательного колпака во всех случаях. Её преимущество другое: она заставляет противоположный колпак иметь большой радиус **без фиксации его геометрии**, используя только массу, верхнюю высоту и центральное сечение. Поэтому она ограничивает целые семейства конечных замен этого колпака.

## 3. Полностью заданный рациональный контроль

Для проверки нового различия возьмём вершину

`p0=(0,0,3)`

и шесть вершин основания в плоскости z=−1:

`p1=(2,0,−1)`,
`p2=(1,5/3,−1)`,
`p3=(−1,5/3,−1)`,
`p4=(−2,0,−1)`,
`p5=(−1,−5/3,−1)`,
`p6=(1,−5/3,−1)`.

Это **контроль теоремы, не кандидат на110 и не переименование LOW121**.

Его максимальный комплекс имеет

`V=7, E=12, F=7, C=24`.

Основание — один шестиугольник; остальные шесть граней — треугольники. Площадь основания равна 10, объём равен `40/3`. Центр основания имеет координату z=−1, вершина — z=3, поэтому собственный объёмный центр пирамиды точно равен 0.

Полный собственный census:

**`strict(S,U,H)=(7,7,12)`, `weak=(0,0,0)`.**

Все семь граней устойчивы, все семь вершин неустойчивы, все двенадцать рёбер седловые; нулевых примитивов нет. Например, перпендикулярная проекция на наклонную грань `[0,1,2]` имеет положительные барицентрические коэффициенты `(59,48,54)/161`, а на грань `[0,2,3]` — `(61,54,54)/169`. Остальные случаи следуют из симметрий; полный проверяющий исходник ниже не использует эту симметрийную сокращённую проверку.

Для дальней вершины p0:

`R²=9`, `rho²=9/4`, `A=45/8`.

Следовательно, старое необходимое условие `rho≥R/3` выполнено с запасом: `rho/R=1/2`. Условие прежнего thin-box также не выполнено.

Но новая оценка требует при R/rho=2 отношения площади не больше20/27. Здесь оно равно `5/(2π)>20/27`. Используя рациональную верхнюю оценку `π<355/113`, получаем без вычислений с плавающей точкой:

`B_minus ≥ 1585/681`,

`bar ≥ 211/2724`,

**`bar/R² ≥ 211/24516 > 0`.**

Таким образом, контроль действительно проходит старый радиусный тест, но новая массовая оценка всё равно доказывает существование второго строгого U.

Полные положительные бары контроля, нормированные на соответствующий глобальный квадрат радиуса:

**Физическое тело:** `16/45`, `11/81`, четыре раза `128/1377`.

**Полярное тело относительно того же центра0:** `3721/7650`, `44/225`, четыре раза `512/3825`.

Это полные списки, не только наибольшие бары. Полярное тело здесь также имеет собственный центр0, но для вычисления полярных баров повторное массовое центрирование вообще не применяется.

## 4. Что это меняет в конструктивном поиске

Просто увеличивать rho или объём при сохранении длинного полюса недостаточно. При фиксированных R и rho увеличение площади A усиливает вынужденный противоположный радиус. Поэтому конечное расширение сечения необходимо согласовывать с положением полюса и массовым распределением по обе стороны сечения.

Практический новый остаток для поиска:

`G_area = L(R,A)/R²−rho²/R²`.

Положительное значение запрещает U1. Неположительное значение — только выход из этого ограничения, а не сертификат U1. После него по-прежнему нужны полный истинный рёберный барьер, собственный S/U/H-census и все слабые случаи.

Для нелинейных изменений LOW121 были подготовлены и вызваны отдельные процедуры полиномиального изменения физических вершин, свободного изменения действительных опорных нормалей, увеличения центрального сечения, отслеживания контакта центральной плоскости с вершиной и восстановления положительных механических запасов. Во всех этих постановках масса вычисляется по новой действительной оболочке. В частности, контакт центрального сечения нельзя проходить, продолжая производную по уже исчезнувшему пересечению ребра: это отдельная смена геометрического участка, даже без изменения числа граней.

**Из этого численного маршрута здесь не объявляется новый подтверждённый собственный класс.** Читаемый итоговый протокол выполнения инструментов в текущей передаче недоступен, поэтому отправленные команды не трактуются как наблюдённые успешные сертификаты. Замороженные входы, полные исходники, предусмотренные независимые проверки и сохранённые протоколы собраны отдельно:

[Исходники и буквальная восстановительная капсула](sandbox:/mnt/data/BH81_SECTION_AREA_HANDOFF.md)

[Полный вычислительный снимок](sandbox:/mnt/data/BH81_SECTION_AREA_FULL.zip)

В этом JSON вычислительные endpoints не повышаются до долговечных преемников LOW121/CUT121. Приведённые выше новая теорема и рациональный контроль от этого снимка не зависят.

## 5. Самодостаточный точный проверяющий исходник

Ниже приведены все данные контроля и весь исходник: максимальные грани и настоящие рёбра, собственный центр, два различных объёмных интегрирования, строгие и слабые механические случаи, оба полных списка баров и рациональная проверка новой оценки. Внешних помощников или численных библиотек нет.

Сохранить как `AREA_RADIUS.py` и выполнить:

`python AREA_RADIUS.py`

Ожидаемый контрольный маркер:

`BH81_AREA_RADIUS_CONTROL_PASS 7 12 7 7 7 12 0 0 0`

Это ожидаемый маркер проверяющего исходника, не заявленный наблюдённый вывод. Аналитические значения контроля выше установлены независимо от запуска. При записи полного отчёта программа печатает его фактические число байтов и SHA-256; ненаблюдённые числовые хеши здесь не подставляются.

Тот же исходник принимает точный JSON с полями `points`, `faces` и необязательным `centroid`. Например, после восстановления доставленной первичной пары:

`python AREA_RADIUS.py LOW121_EXACT.json --out LOW121_AREA_RADIUS.json`

Центр из входного файла не используется как свободный параметр: программа самостоятельно интегрирует заполненное тело и проверяет совпадение.

```python
from fractions import Fraction as F
from collections import defaultdict, Counter
from pathlib import Path
import argparse, hashlib, json, math, sys
sys.set_int_max_str_digits(0)
PI_UPPER = F(355,113)
CONTROL = {
 'points': [[0,0,3],[2,0,-1],[1,'5/3',-1],[-1,'5/3',-1],
            [-2,0,-1],[-1,'-5/3',-1],[1,'-5/3',-1]],
 'faces': [[1,6,5,4,3,2]] + [[0,i,1+i%6] for i in range(1,7)]
}

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def mul(t,a): return tuple(t*x for x in a)
def cross(a,b):
 return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],
         a[0]*b[1]-a[1]*b[0])
def encode(x):
 return json.dumps(x,sort_keys=True,separators=(',',':'),default=str).encode()

def pi_certificate():
 def bounds(x):
  lo=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(40)),F(0))
  return lo,lo+x**81/F(81)
 a,b=bounds(F(1,5));c,d=bounds(F(1,239))
 lo,hi=16*a-4*d,16*b-4*c
 assert lo>3 and hi<PI_UPPER
 return {'lower':lo,'upper':hi,'rational_majorant':PI_UPPER}

def cycle(points,n):
 points=sorted(set(points))
 k=max(range(3),key=lambda j:abs(n[j]))
 axes=[j for j in range(3) if j!=k]
 def xy(p): return (p[axes[0]],p[axes[1]])
 def turn(a,b,c):
  a,b,c=xy(a),xy(b),xy(c)
  return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 seq=sorted(points,key=xy);lo=[];hi=[]
 for p in seq:
  while len(lo)>1 and turn(lo[-2],lo[-1],p)<=0: lo.pop()
  lo.append(p)
 for p in reversed(seq):
  while len(hi)>1 and turn(hi[-2],hi[-1],p)<=0: hi.pop()
  hi.append(p)
 out=lo[:-1]+hi[:-1]
 assert len(out)>=3
 if dot(cross(sub(out[1],out[0]),sub(out[2],out[0])),n)<0:
  out.reverse()
 return out

def audit(data):
 P=[tuple(F(x) for x in p) for p in data['points']]
 faces=[list(map(int,f)) for f in data['faces']]
 assert len(set(P))==len(P)
 anchor=tuple(sum(p[k] for p in P)/len(P) for k in range(3))
 edges=defaultdict(list);nbr=defaultdict(set)
 links=defaultdict(lambda:defaultdict(set))
 planes=[];used=set();face_keys=set()
 V=F(0);M=[F(0)]*3;Vp=F(0);Mp=[F(0)]*3;tets=0
 for fi,row in enumerate(faces):
  assert len(row)>=3 and len(set(row))==len(row)
  assert all(0<=i<len(P) for i in row)
  assert frozenset(row) not in face_keys
  face_keys.add(frozenset(row));used.update(row)
  a,b,c=(P[i] for i in row[:3])
  n=cross(sub(b,a),sub(c,a));h=dot(n,a)
  assert dot(n,n)>0 and dot(n,anchor)<h
  assert all(dot(n,p)<=h for p in P)
  assert set(row)=={i for i,p in enumerate(P) if dot(n,p)==h}
  planes.append((n,h))
  for pos,i in enumerate(row):
   j=row[(pos+1)%len(row)];before=row[pos-1];e=sub(P[j],P[i])
   assert all(dot(n,cross(e,sub(P[t],P[i])))>0
              for t in row if t not in (i,j))
   edges[tuple(sorted((i,j)))].append((fi,i,j))
   nbr[i].add(j);nbr[j].add(i)
   links[i][before].add(j);links[i][j].add(before)
  for k in range(1,len(row)-1):
   a,b,c=(P[i] for i in (row[0],row[k],row[k+1]))
   w=dot(sub(a,anchor),cross(sub(b,anchor),sub(c,anchor)))/6
   assert w>0
   V+=w;tets+=1
   for j in range(3):
    M[j]+=w*(anchor[j]+a[j]+b[j]+c[j])/4
  # Separate projected-polygon divergence integration.
  k=max(range(3),key=lambda j:abs(n[j]));u=(k+1)%3;v=(k+2)%3
  A=F(0);mu=F(0);mv=F(0)
  for i,j in zip(row,row[1:]+row[:1]):
   a,b=P[i],P[j];d=a[u]*b[v]-b[u]*a[v]
   A+=d/2;mu+=(a[u]+b[u])*d/6;mv+=(a[v]+b[v])*d/6
  ints=[F(0)]*3;ints[u]=mu;ints[v]=mv
  ints[k]=(h*A-n[u]*mu-n[v]*mv)/n[k]
  Vp+=h*A/n[k]/3
  for j in range(3): Mp[j]+=h*ints[j]/n[k]/4
 assert V>0 and V==Vp and tuple(M)==tuple(Mp)
 assert used==set(range(len(P)))
 assert len(P)-len(edges)+len(faces)==2
 for inc in edges.values():
  assert len(inc)==2 and inc[0][1:]==tuple(reversed(inc[1][1:]))
 for i in range(len(P)):
  link=links[i]
  assert set(link)==nbr[i] and all(len(ns)==2 for ns in link.values())
  reached={next(iter(link))};todo=list(reached)
  while todo:
   a=todo.pop()
   for b in link[a]-reached: reached.add(b);todo.append(b)
  assert reached==set(link)
 reached={0};todo=[0]
 while todo:
  i=todo.pop()
  for j in nbr[i]-reached: reached.add(j);todo.append(j)
 assert reached==set(range(len(P)))
 c=tuple(x/V for x in M)
 if 'centroid' in data:
  assert c==tuple(F(x) for x in data['centroid'])
 X=[sub(p,c) for p in P]
 strict=[[],[],[]];weak=[[],[],[]];zeros=[0,0,0]
 def record(k,label,values):
  zeros[k]+=sum(x==0 for x in values)
  if min(values)>0: strict[k].append(label)
  elif min(values)>=0: weak[k].append(label)
 for fi,(f,(n,h)) in enumerate(zip(faces,planes)):
  record(0,fi,[-dot(n,cross(sub(X[j],X[i]),X[i]))
               for i,j in zip(f,f[1:]+f[:1])])
 for i in range(len(P)):
  record(1,i,[-dot(X[i],sub(X[j],X[i])) for j in sorted(nbr[i])])
 for (i,j),inc in sorted(edges.items()):
  e=sub(X[j],X[i]);ee=dot(e,e);t=-dot(X[i],e)
  z=add(mul(ee,X[i]),mul(t,e))
  n,m=planes[inc[0][0]][0],planes[inc[1][0]][0]
  aa,bb,ab=dot(n,n),dot(m,m),dot(n,m)
  zn,zm=dot(z,n),dot(z,m)
  record(2,[i,j],[t,ee-t,zn*bb-zm*ab,zm*aa-zn*ab])
 allU=[i for i in range(len(P))
       if all(dot(X[i],sub(X[j],X[i]))<0
              for j in range(len(P)) if j!=i)]
 assert allU==strict[1]
 if not any(weak):
  assert len(strict[0])+len(strict[1])-len(strict[2])==2
 out={'VEF':[len(P),len(edges),len(faces)],'C':2*len(edges),
      'volume':V,'centroid':c,'strict':list(map(len,strict)),
      'weak':list(map(len,weak)),'primitive_zeros':zeros,
      'strict_features':strict,'weak_features':weak,
      'positive_tetrahedra':tets,'projected_polygon_mass_equal':True}
 return out,X,planes,edges

def persistence(P,edges):
 B=[dot(p,p) for p in P];R=max(B)
 parent=list(range(len(P)));events=[]
 def root(i):
  while parent[i]!=i:
   parent[i]=parent[parent[i]];i=parent[i]
  return i
 weighted=[]
 for i,j in edges:
  d=sub(P[j],P[i]);dd=dot(d,d);t=-dot(P[i],d)
  if t<=0: h=B[i]
  elif t>=dd: h=B[j]
  else: h=B[i]-t*t/dd
  weighted.append((h,i,j))
 for h,i,j in sorted(weighted,reverse=True):
  a,b=root(i),root(j)
  if a==b: continue
  if (B[a],-a)<(B[b],-b): a,b=b,a
  depth=(B[b]-h)/R
  assert depth>=0
  if depth:
   events.append({'peak':b,'older_peak':a,'merge_edge':[i,j],
                  'relative_bar':depth})
  parent[b]=a
 return sorted(events,key=lambda e:e['relative_bar'],reverse=True)

def area_gate(X,edges):
 B=[dot(p,p) for p in X]
 i=max(range(len(X)),key=lambda k:(B[k],-k))
 R2=B[i];n=X[i];s=[dot(n,x) for x in X]
 section=[x for x,z in zip(X,s) if z==0]
 for a,b in edges:
  if s[a]*s[b]<0:
   t=s[a]/(s[a]-s[b])
   section.append(add(X[a],mul(t,sub(X[b],X[a]))))
 polygon=cycle(section,n)
 rho2=max(dot(p,p) for p in polygon)
 area_vector=tuple(
  sum(cross(a,b)[k] for a,b in zip(polygon,polygon[1:]+polygon[:1]))/2
  for k in range(3))
 kappa=dot(area_vector,n)/R2
 assert kappa>0
 # A = kappa*sqrt(R2); use a rational lower bound on A.
 G=10**24
 Rlo=F(math.isqrt(R2.numerator*G*G//R2.denominator),G)
 Alo=kappa*Rlo
 lower=R2*(PI_UPPER*R2+9*Alo)/(9*(PI_UPPER*R2+Alo))
 neg=max((k for k in range(len(X)) if s[k]<0),key=lambda k:B[k])
 assert B[neg]>=lower
 relative=(lower-rho2)/R2
 if relative>0:
  assert all(dot(X[neg],sub(X[j],X[neg]))<0
             for j in range(len(X)) if j!=neg)
 return {'farthest_vertex':i,'R2':R2,'rho2':rho2,
         'section_vertices':polygon,'area_over_R':kappa,
         'area_lower':Alo,'opposite_radius2_lower':lower,
         'relative_bar_lower':max(F(0),relative),
         'radius_only_gate_passed':9*rho2>=R2,
         'area_gate_proves_two_U':relative>0,
         'opposite_strict_U_witness':neg if relative>0 else None}

def main():
 p=argparse.ArgumentParser()
 p.add_argument('input',nargs='?')
 p.add_argument('--out',default='AREA_RADIUS_REPORT.json')
 a=p.parse_args()
 data=CONTROL if a.input is None else json.loads(Path(a.input).read_text())
 out,X,planes,edges=audit(data)
 out['pi']=pi_certificate()
 out['section_mass_gate']=area_gate(X,edges)
 out['physical_bars']=persistence(X,edges)
 Q=[mul(1/(h-dot(n,out['centroid'])),n) for n,h in planes]
 dual_edges={tuple(sorted((inc[0][0],inc[1][0])))
             for inc in edges.values()}
 out['polar_bars']=persistence(Q,dual_edges)
 if a.input is None:
  assert out['VEF']==[7,12,7] and out['strict']==[7,7,12]
  assert out['weak']==out['primitive_zeros']==[0,0,0]
  assert out['centroid']==(F(0),)*3 and out['volume']==F(40,3)
  g=out['section_mass_gate']
  assert g['R2']==9 and g['rho2']==F(9,4)
  assert g['area_lower']==F(45,8)
  assert g['opposite_radius2_lower']==F(1585,681)
  assert g['relative_bar_lower']==F(211,24516)
  assert Counter(e['relative_bar'] for e in out['physical_bars'])==Counter(
   [F(16,45),F(11,81)]+[F(128,1377)]*4)
  assert Counter(e['relative_bar'] for e in out['polar_bars'])==Counter(
   [F(3721,7650),F(44,225)]+[F(512,3825)]*4)
  print('BH81_AREA_RADIUS_CONTROL_PASS 7 12 7 7 7 12 0 0 0')
 out['literal_input']=data
 b=encode(out);Path(a.out).write_bytes(b)
 print(json.dumps({'output':a.out,'bytes':len(b),
                   'sha256':hashlib.sha256(b).hexdigest()},sort_keys=True))

if __name__=='__main__': main()
```

## 6. Следующее содержательное геометрическое решение

Для продолжения LOW121/CUT121 следует изменять весь центральный участок и сопряжённый отрицательный колпак так, чтобы одновременно выйти из `G_area>0`, сохранить или восстановить единственный собственный S и уменьшить полный положительный физический бар. При смене дальней вершины R, плоскость сечения, rho и A должны вычисляться заново. Ни прежний thin-box, ни новая площадь-зависимая оценка не исключают такой конечной смены геометрии.

Новая оценка ограничивает семейства с соответствующими геометрическими инвариантами; она не является исключением всех малых многогранников, всех многосрезовых тел или всей ветви. Принятый собственный110-рекорд этой передачей не изменяется.
