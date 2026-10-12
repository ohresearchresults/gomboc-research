# minimum-0101

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# OVERHANG_SHARED_AFFINE_FAN_BUDGET_V1

## 1. Доказательное определение

**Универсальный наклонный запрет T<51/25 для произвольной проекции в этом продолжении не доказан; действительный контрпример также не получен.** Получен новый достаточный геометрический критерий для свободной внешней части x+y>1. Он сохраняет действительный запас призматической части и оценивает внешний вклад через одну совместную аффинную функцию, а не через независимо назначенные массы или координатные моменты.

Критерий действует при произвольном числе вершин и граней, произвольной форме проекции и без ограничения величины rho. Его полностью доказанная область и непрерывное дополнение приведены ниже. Это не новый fixed-L результат и не предположение о монотонности отсечения.

Новый автономный точный расчёт применён к неизменённым 16 телам parent: пяти призматическим и одиннадцати с настоящим выступом. Все одиннадцать внешних тел проходят критерий с действительным призматическим запасом; девять проходят даже его версию, использующую только универсальный cap 203/100. Для двух более крупных тел замена действительного запаса округлённым cap действительно теряет сертификат. Все девять прежних случаев уменьшения T при призматическом отсечении сохранены.

**Ни доказанная нижняя граница 34, ни верхняя граница 622, ни FULL/LOCAL или другие реестры не изменены.** Первый открытый слой остаётся (10,17,9). Это унаследованный статус научной линии, а не новый пересчёт её доказательств. :contentReference[oaicite:0]{index=0}

## 2. Прочитанные источники и зависимость

Новая версия `research-journal(20260919-062818).md` прочитана полностью до EOF, включая общий notebook, память ветви и полный буквальный parent с обоими исходниками. Файл имеет 222422 байта, SHA-256 `2360cd7ec54fe68362c2420be35e6c3a2432d7ecf104c4240273e57631dfc340`.

Математический parent:

`minimum-0089`, SHA-256 `891b41773841961163f155590af8f226a198ce4a68017e870a8a492b3c7c1f52`, **FREE_FIBRE_PRISM_TRACE_203_AND_SEGMENT_CORE_V1**.

Его идентификатор и SHA относятся к поставленному immutable payload. Я не выдаю хеширование извлечённого Markdown за повторную аутентификацию исходного JSON-envelope. Конфликта математических утверждений или идентичности использованных тел между буквальным parent и новой памятью не обнаружено.

Единственная специальная математическая посылка нового критерия — доказанная в parent теорема: при настоящих ABC,ABD,AB и проекции Delta всякое допустимое тело имеет T<203/100. Нулевая плоскость ell для этой аналитической теоремы не обязана быть гранью. :contentReference[oaicite:1]{index=1}

Побайтно проверены доступные неизменённые файлы parent:

- `free_fibre_prism_exact.py`: 18642 байта, SHA-256 `0e5727d6a4d02105ce1a225f0a8ac8fb990650e9477dc81bcd3dc0f7f3c38d71`;
- `free_fibre_prism_exact.json`: 604422 байта, SHA-256 `7c7957213edd8f6923d58b95fc1b70b189192cb53625f5a81850575a293543b0`;
- `search_free.py`: 1295 байт, SHA-256 `10d924fe2b362ab21dd1a7cbcfd4b8d942daeb22ef122615f251aeeaba14fb59`.

Это проверка целостности, не новый запуск 393-cell prism certificate. Новые исполнения относятся только к приведённому ниже source. Старые численные поиски не перезапускались. Более сильные endpoint-gap материалы, названные в notebook, не являются посылками нового доказательства; их отсутствие как отдельных приложений не восполняется предположениями об их содержимом.

## 3. Теорема о действительном внешнем вкладе

### 3.1. Одна геометрия и обозначения

Пусть P — компактное полноразмерное однородное выпуклое тело. В канонических координатах

```text
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0)
```

треугольники ABC и ABD являются настоящими максимальными гранями, AB — их настоящим общим ребром. Пусть

```text
ell=a+(d-a)x+(c-a)y+(b-a)z >= 0 on P,
ell is not identically zero,
n=(a+b+c)x+(a+b+d)y,
tau=51/25, sigma=203/100.
```

Для любого измеримого R обозначим

```text
V(R)=integral_R 1,
B(R)=integral_R ell,
N(R)=integral_R n.
```

Тогда исследуемый след равен

`T(P)=N(P)/(6 V(P) B(P))`.

Никакого изменения плотности или центра отсчёта в этих интегралах нет.

Положим

```text
Pc=P intersect {x+y<=1},
Po=P intersect {x+y>=1},
S=P intersect {x+y=1},
v=V(Pc), W=V(Po), Bc=B(Pc), Bo=B(Po), Nc=N(Pc), No=N(Po).
```

При rho=max_P(x+y)=1 тело уже призматическое и закрыто parent. Далее rho>1. Тогда Po полноразмерно, W>0, S — двумерное сечение, одновременно настоящий новый фасет Pc и Po. Pc сохраняет исходные ABC,ABD,AB и имеет проекцию Delta. Его корневая плоскость может перестать быть гранью; это не мешает применению prism theorem.

Введём **одну совместную аффинную функцию**

`g_tau(p)=n(p)-6 tau v ell(p)`

и её действительные экстремумы

```text
A_tau=min_{p in S} g_tau(p),
H_tau=max_{p in Po} g_tau(p),
m=max_{p in S} ell(p).
```

Функция g_tau может иметь оба знака. В частности, отрицательное A_tau не заменяется нулём.

Имеем m>0. Действительно, при rho>1 сечение S пересекает внутренность P, а ненулевая аффинная ell>=0 строго положительна во внутренности полноразмерного P. Следовательно ниже не возникает скрытого случая деления на нулевой m.

Определим

```text
Dc=6 tau v Bc-Nc,
d0=6(tau-sigma)v Bc=(3/50)v Bc,
J=(A_tau+3 H_tau)/4-6 tau Bc,
q=(3 tau/2)m=(153/50)m,
Phi=Dc-J W+q W^2,
Phi0=d0-J W+q W^2.
```

Здесь q — скалярный коэффициент, не полярный вектор.

### 3.2. Утверждение

Для каждого указанного действительного тела

`6 tau V(P) B(P)-N(P) >= Phi > Phi0`.

В частности:

**(A)** вся область `Phi>0` имеет `T(P)<51/25`;

**(B)** более простой достаточный тест `Phi0>=0` также даёт строгое `T(P)<51/25`, включая равенство в тесте.

Тест B не требует вычисления Nc: достаточно универсального prism cap, действительных v,Bc,W и трёх действительных экстремумов на S и Po. Тест A сохраняет настоящий запас Pc и потому сильнее.

Это критерий для произвольной свободной формы внешней части. L, верхний и нижний графики, проекция и внешние вершины не фиксируются. Экстремумы и интегралы не объявляются независимыми параметрами, которые можно произвольно реализовать.

## 4. Полное доказательство

### 4.1. Элементарная веерная лемма

Пусть K — полноразмерное однородное выпуклое трёхмерное тело, f — аффинная функция и p принадлежит K. Тогда

`integral_K f <= V(K)[f(p)+3 max_K f]/4`.

Если ell>=0 на K и p' принадлежит K, то

`integral_K ell >= V(K) ell(p')/4`.

Для многогранника триангулируем настоящую границу и используем положительный веер из p. В каждой тетраэдральной ячейке среднее f равно четверти суммы четырёх вершинных значений. Одно значение есть f(p), три остальных не превосходят max_K f. После суммирования с настоящими объёмами получается первое неравенство. Для второго используем веер из p' и неотрицательность трёх остальных значений ell. Точка веера может лежать на границе; нулевые ячейки разрешены.

Для общего компактного выпуклого K берём возрастающие внутренние многогранные приближения, содержащие выбранные точки. Объёмы и интегралы аффинных функций сходятся; приведённые нестрогие оценки переходят к пределу. Строгость итогового trace-утверждения ниже возникает не из предела строгих знаков, а из отдельного строгого prism gap.

Два веера могут иметь разные апексы, но оба интегрируют одно и то же K. Никаких независимо подбираемых масс не вводится.

### 4.2. Применение к настоящему Po

Выбирая на S точку минимума g_tau, получаем

`No-6 tau v Bo <= W(A_tau+3 H_tau)/4`.

Выбирая на S точку максимума ell, получаем

`Bo >= m W/4`.

Обе оценки относятся к одному действительному Po с одним объёмом W и одной ell-массой Bo.

### 4.3. Точный смешанный знаменатель

Так как Pc и Po пересекаются лишь по двумерному S,

```text
V(P)=v+W,
B(P)=Bc+Bo,
N(P)=Nc+No.
```

Поэтому имеется точное тождество

```text
6 tau V(P)B(P)-N(P)
 =Dc+6 tau(v Bo+W Bc+W Bo)-No
 =Dc+6 tau W Bc+6 tau W Bo-integral_Po g_tau.
```

Подставляя две веерные оценки, получаем

```text
6 tau V(P)B(P)-N(P)
 >=Dc+W[6 tau Bc-(A_tau+3 H_tau)/4]+(3 tau/2)m W^2
 =Phi.
```

Из настоящей призматической теоремы `Nc<6 sigma v Bc` следует

`Dc>6(tau-sigma)v Bc=d0>0`.

Следовательно `Phi>Phi0`, что завершает доказательство, в том числе при Phi0=0.

Важно, что здесь **не** доказывается `T(P)<=T(Pc)`. Отрицательный внешний линейный вклад допускается и оплачивается действительным Dc и положительным смешанным членом qW².

## 5. Полные непрерывные секторы и точное дополнение

### 5.1. Два сектора без ограничения W или rho

Если `J<=0`, то Phi>0 автоматически. Геометрически это условие записывается как

`H_tau <= 8 tau Bc-A_tau/3`.

То есть вся внешняя часть находится в соответствующем полупространстве для одной g_tau. Это не ограничение типа rho<=1+epsilon; оно допускает произвольную внешнюю форму и не требует заранее малого выступа.

Также весь замкнутый сектор

`J^2 <= (459/625) m v Bc`

закрыт независимо от W. Действительно,

`4 q d0=(459/625)m v Bc`,

и дискриминант квадратного многочлена Phi0 по W неположителен. Поэтому Phi0>=0 при всех W, включая равенство дискриминанта и двойной корень. Сектор J<=0 остаётся закрытым и вне этого дискриминантного условия.

### 5.2. Что действительно остаётся после нового теста

Для тела с T>=tau необходимо Phi<=0. Поскольку Dc>0 и q>0, это требует одновременно

```text
J>0,
J^2-4q Dc>=0,
[J-sqrt(J^2-4q Dc)]/(2q)
 <=W<=
[J+sqrt(J^2-4q Dc)]/(2q).
```

Это точное дополнение к достаточному тесту Phi>0. Равенство дискриминанта и обе конечные стенки W оставлены в непокрытой области; они не удаляются численно. Здесь J,Dc,q,W всё ещё должны происходить от одного настоящего P и его настоящего сечения. Приведённые условия не являются утверждением реализуемости произвольного скалярного набора.

С учётом parent вся оставшаяся область возможного высокого следа дополнительно удовлетворяет

```text
rho>(204/203)^(1/4),
Psi>204/203,
a!=b,
1<t<45/7,
```

и прежним принятым tilt/endpoint-gap условиям. Parent определяет

```text
lambda=1/rho,
HN=integral_projection(P) n dxdy,
Psi=[(v/V(P))(Bc/B(P))]
     /[lambda^4+lambda^3(1-lambda)HN/N(P)].
```

Его segment-core theorem и прежние ограничения сохраняются без изменения. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

**Не доказано**, что действительное тело не может попасть в это совместное дополнение. Никакой конечный набор вычисленных тел не используется для такого вывода.

## 6. Точные контроли и полезные отрицательные результаты

### 6.1. Полные входные данные

Все тела здесь — неизменённые контроли parent, а не новые конструкции. Пусть

```text
nd=(a,b,c,d)=(1,1/4,c,d),
ell=1-(1-d)x-(1-c)y-(3/4)z,
Root(x,y)=(x,y,(4/3)[1-(1-d)x-(1-c)y]),
e=1/10000, r=5/6.
```

К T0=conv(A,B,C,D) добавляются четыре точки Root с парами

```text
(r-e,e), (e,r-e), (e,1-2e), (1-2e,e).
```

При указанном rho дополнительно добавляется `Root(rho/2,rho/2)`. При `rho=None` дополнительной точки нет.

Точный порядок 16 входов:

```text
(c,d)=(1/10000,1/20000): rho=None,101/100,3/2,2;
(c,d)=(3/1000,1/500):   rho=None,101/100,51/50;
(c,d)=(1/200,1/400):    rho=None,101/100,51/50;
(c,d)=(1/100,1/200):    rho=None,101/100,51/50;
(c,d)=(1/500,1/500):    rho=None,101/100,51/50.
```

Новый source заново строит максимальные грани, настоящие рёбра, Pc,Po и их собственные объёмы и первые моменты двумя различными положительными веерами. Проверяются точные аддитивные равенства V,B,N и всех трёх первых моментов. Проверяется настоящая корневая грань исходного P, а также настоящие ABC,ABD,AB у P и Pc. Нулевая плоскость у каждой части записывается как грань только после действительной проверки.

### 6.2. Прежний cut-drop контроль теперь проходит новый достаточный тест

Для `P*=P(1/100,1/200;101/100)`, индекс 11 в source, сохранены

```text
f(P*)=(9,19,12),
T(P*)=2155518603728164661400000/1065579991917354553894843,
T(Pc*)=317136889441260199286440200000
       /156805732128382273017653918249,
2<T(Pc*)<T(P*)<51/25.
```

Именно это тело сохраняет настоящие ABC,ABD,AB и root при отсечении и опровергает прямую монотонность призматического cut. Это не прежний оператор продления C,D. Унаследованные механические счётчики равны strict(S,U,H)=(5,5,8); новый source не выдаёт себя за повторный полный механический аудит всех примитивов. :contentReference[oaicite:4]{index=4}

Новые действительные данные:

```text
v=15339916548677/81810000000000,
Bc=71554504316605459/1322049600000000000,
W=69991/1818000000,
m=1/100,
A_tau=13999158918672491/11362500000000000,
H_tau=50803/40000,
q=153/5000,
-J=-5491020910285379167/9180900000000000000.
```

При этом

```text
Phi0=1056133425845492151438047751743
     /1802614629600000000000000000000000
     >1/2000,
Phi=1552191560556569809419245531
    /1487305800000000000000000000000
    >0.
```

Следовательно новый тест закрывает этот действительный внешний объект, несмотря на `Psi>204/203` и несмотря на уменьшение T при cut. Это не контрпример к общему порогу, а контроль того, что новый механизм не предполагает ложной монотонности.

Все девять индексов прежнего cut-drop выше 2,

`1,5,6,8,9,11,12,14,15`,

заново точно подтверждены и проходят Phi0>0.

### 6.3. Зачем сохранять действительный запас, а не только 2.03

Для неизменённых более крупных тел с `(c,d)=(1/10000,1/20000)` получены:

```text
rho=3/2: Phi0<-3/200, но Phi>1/25;
rho=2:   Phi0<-1/25,  но Phi>7/100.
```

Таким образом слабая версия теста здесь действительно не сертифицирует знак, тогда как сохранение реального Dc даёт положительный сертификат. Эти отрицательные результаты слабого теста не объявляются телами с высоким T или запретом геометрии.

Точные следы этих невыигрышных тел остаются

```text
rho=3/2:
4205391046965498077770140000000/2504277028012898070119717005243;
rho=2:
6939555600406104319945140000000/4631974902407559318308619610243.
```

Унаследованный высокий призматический контроль `P(1/10000,1/20000;None)` с f=(8,17,11) и T около 2.028670 также сохранён. Он не становится телом (10,17,9) и не объявляется 110 или аттейнером C34. :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6}

## 7. Физический Lambda и реестры

Когда ell=0 — настоящая корневая грань r исходного P, с mu=ell(g_P), t=6V(P), i=ABC, j=ABD имеем

```text
Lambda_ri=gx(a+b+c)/(t mu),
Lambda_rj=gy(a+b+d)/(t mu),
T=Lambda_ri+Lambda_rj.
```

Это следует из настоящих площадей 1/2 двух канонических треугольников, их настоящих площадных центроидов и собственного g_P. В новом расчёте вычислены именно эти физические коэффициенты от восстановленного P. Полные старые Lambda-аудиты и механические знаки остаются доказательствами parent, а не вновь исполненной частью настоящей капсулы. :contentReference[oaicite:7]{index=7}

Новое утверждение относится только к настоящей паре 3,3. Оно не переносится на 5,3. Не выполнено буквальное сопоставление нового непрерывного сектора с labelled incidence domains FULL253, LOCAL или другими реестрами; никакого изменения счётчиков не заявляется.

**Нижняя граница 34 не повышена:** совместное дополнение из §5 не исключено, весь слой (10,17,9) не закрыт и новый строгий 110-аттейнер не построен. Верхняя граница 622 также не изменена.

## 8. Recovery capsule и фактическое исполнение

Доказательство общей области — §§3–5. Код ниже не заменяет его конечной выборкой: он восстанавливает все точные входы и проверяет новое применение к действительным телам, включая отрицательные тесты.

Среда: CPython 3.13.5, только стандартная библиотека, assertions включены. Сохранить полный source ниже как `overhang_fan_budget.py`, UTF-8/LF с одним завершающим LF. Дополнительные файлы, оптимизатор, seed, сеть и parent-code не требуются.

```bash
python -S overhang_fan_budget.py build
python -S overhang_fan_budget.py check
sha256sum overhang_fan_budget.py overhang_fan_budget.json
```

Окончательный source отдельно перенесён в другой каталог; там build и check выполнены, результат совпал с сохранённым отчётом. Пины:

```text
overhang_fan_budget.py
8195 bytes
8a641f0e89cbe9dd76088811287ffc212eca092fc8ac8083552e1d4fafd6767a

overhang_fan_budget.json
66699 bytes
82adee6b6c554983dcda6799c402c067ff3bbd02db38c2abe45354394f93a6ea
```

Полный ожидаемый stdout каждого запуска:

```text
FREE_OVERHANG_BUDGET_CONTROLS_PASS 5_PRISM 11_OVERHANG 9_UNIFORM 11_ACTUAL
ACTUAL_COMMON_MASS_FACETS_TWO_FANS_PASS 16
PRESERVED_TRUE_ROOT_CUT_DROP_ABOVE_TWO_PASS 9
OVERHANG_SHARED_AFFINE_FAN_BUDGET_PASS 66699 82adee6b6c554983dcda6799c402c067ff3bbd02db38c2abe45354394f93a6ea
```

### Полный минимальный автономный source

```python
"""OVERHANG_SHARED_AFFINE_FAN_BUDGET_V1.
CPython 3.13.5; standard library; assertions enabled.
Mathematical parent (not imported): minimum-0089,
SHA256 891b41773841961163f155590af8f226a198ce4a68017e870a8a492b3c7c1f52.
The parent supplies the free-prism theorem T<203/100.
Run: python -S overhang_fan_budget.py build; then check.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import hashlib, json, sys
assert __debug__
TAU=F(51,25)
SIGMA=F(203,100)
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def av(P): return tuple(sum(p[j] for p in P)/len(P) for j in range(3))
def h2(P):
    P=sorted(set(P))
    def turn(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    rows=[]
    for seq in (P,P[::-1]):
        row=[]
        for p in seq:
            while len(row)>1 and turn(row[-2],row[-1],p)<=0: row.pop()
            row.append(p)
        rows.append(row[:-1])
    return rows[0]+rows[1]
def audit(points):
    P=list(dict.fromkeys(tuple(map(F,p)) for p in points)); planes={}
    for i,j,k in combinations(range(len(P)),3):
        n=cross(sub(P[j],P[i]),sub(P[k],P[i])); d=dot(n,P[i])
        if not any(n): continue
        slack=[dot(n,p)-d for p in P]
        if min(slack)<0<max(slack) or min(slack)==max(slack)==0: continue
        if min(slack)>=0: n=tuple(-x for x in n); d=-d
        den=lcm(*(x.denominator for x in (*n,d)))
        ints=[int(x*den) for x in (*n,d)]; div=gcd(*ints)
        H=tuple(F(x//div) for x in ints)
        planes[H]=[i for i,p in enumerate(P) if dot(H[:3],p)==H[3]]
    faces=[]
    for H,ids in planes.items():
        drop=next(j for j in range(3) if H[j]); axes=[j for j in range(3) if j!=drop]
        mp={tuple(P[i][j] for j in axes):i for i in ids}
        face=[mp[p] for p in h2(list(mp))]
        if dot(cross(sub(P[face[1]],P[face[0]]),sub(P[face[2]],P[face[0]])),H[:3])<0: face.reverse()
        start=face.index(min(face)); face=face[start:]+face[:start]
        faces.append((tuple(face),H))
    faces.sort(); vertices=sorted({i for face,H in faces for i in face})
    edges=sorted({tuple(sorted((i,j))) for face,H in faces for i,j in zip(face,face[1:]+face[:1])})
    assert len(vertices)-len(edges)+len(faces)==2
    for i in vertices:
        normals=[H[:3] for face,H in faces if i in face]
        assert any(det(*tr) for tr in combinations(normals,3))
    interior=av([P[i] for i in vertices])
    answers=[]
    for ref in (P[vertices[0]],interior):
        V=F(0); moment=[F(0)]*3
        for face,H in faces:
            for j in range(1,len(face)-1):
                tr=[P[i] for i in (face[0],face[j],face[j+1])]
                w=det(*(sub(p,ref) for p in tr))/6
                assert w>=0
                V+=w
                for k in range(3): moment[k]+=w*(ref[k]+sum(p[k] for p in tr))/4
        answers.append((V,tuple(moment)))
    assert answers[0]==answers[1] and answers[0][0]>0
    V,moment=answers[0]
    return dict(points=P,vertices=vertices,faces=faces,edges=edges,
                f=(len(vertices),len(edges),len(faces)),V=V,M=moment,
                g=tuple(x/V for x in moment))
def clip(R,side):
    P=R['points']; vals=[p[0]+p[1]-1 for p in P]
    out=[p for p,v in zip(P,vals) if side*v>=0]
    for i,j in R['edges']:
        if vals[i]*vals[j]<0:
            t=vals[i]/(vals[i]-vals[j])
            out.append(tuple(P[i][k]+t*(P[j][k]-P[i][k]) for k in range(3)))
    return out
def ell(p,nd):
    a,b,c,d=nd
    return a+(d-a)*p[0]+(c-a)*p[1]+(b-a)*p[2]
def nfun(p,nd):
    a,b,c,d=nd
    return (a+b+c)*p[0]+(a+b+d)*p[1]
def rootpoint(x,y,nd):
    a,b,c,d=nd
    return (x,y,(a+(d-a)*x+(c-a)*y)/(a-b))
def body(c,d,rho):
    nd=(F(1),F(1,4),c,d); e=F(1,10000); r=F(5,6)
    P=[(0,0,0),(0,0,1),(0,1,0),(1,0,0)]
    P += [rootpoint(x,y,nd) for x,y in ((r-e,e),(e,r-e),(e,1-2*e),(1-2*e,e))]
    if rho is not None: P.append(rootpoint(rho/2,rho/2,nd))
    return P,nd
def enrich(R,nd,pair=False):
    V=R['V']; g=R['g']; R['B']=V*ell(g,nd); R['N']=V*nfun(g,nd)
    assert min(ell(p,nd) for p in R['points'])>=0 and R['B']>0
    R['T']=R['N']/(6*V*R['B'])
    sets=[frozenset(face) for face,H in R['faces']]
    zeros=frozenset(i for i in R['vertices'] if ell(R['points'][i],nd)==0)
    R['root_is_facet']=zeros in sets
    if pair:
        assert frozenset((0,1,2)) in sets and frozenset((0,1,3)) in sets and (0,1) in R['edges']
        a,b,c,d=nd; mu=ell(g,nd); t=6*V
        pair_values=(g[0]*(a+b+c)/(t*mu),g[1]*(a+b+d)/(t*mu))
        assert sum(pair_values)==R['T']
        R['physical_Lambda_pair']=pair_values
    return R

def one(c,d,rho):
    points,nd=body(c,d,rho); P=enrich(audit(points),nd,True)
    C=enrich(audit(clip(P,-1)),nd,True)
    assert P['root_is_facet'] and C['T']<SIGMA
    if rho is None:
        assert P['V']==C['V'] and P['M']==C['M']
        return dict(nodes=nd,rho=F(1),P=P,C=C,uniform_pass=True,actual_pass=True)
    O=enrich(audit(clip(P,1)),nd)
    assert P['V']==C['V']+O['V'] and P['B']==C['B']+O['B'] and P['N']==C['N']+O['N']
    assert all(P['M'][j]==C['M'][j]+O['M'][j] for j in range(3))
    section=[p for p in C['points'] if p[0]+p[1]==1]
    assert len(section)>=3
    v=C['V']; B=C['B']; W=O['V']
    def h(p): return nfun(p,nd)-6*TAU*v*ell(p,nd)
    A=min(map(h,section)); H=max(h(O['points'][i]) for i in O['vertices'])
    m=max(ell(p,nd) for p in section)
    assert m>0
    assert O['N']-6*TAU*v*O['B']<=W*(A+3*H)/4
    assert O['B']>=m*W/4
    dc=6*TAU*v*B-C['N']; dp=6*TAU*P['V']*P['B']-P['N']
    linear=6*TAU*B-(A+3*H)/4; quadratic=F(3,2)*TAU*m
    uniform=6*(TAU-SIGMA)*v*B+linear*W+quadratic*W*W
    actual=dc+linear*W+quadratic*W*W
    assert dp>=actual>uniform and dc>6*(TAU-SIGMA)*v*B
    assert dp==dc+6*TAU*(v*O['B']+W*B+W*O['B'])-O['N']
    if uniform>=0 or actual>0: assert P['T']<TAU
    return dict(nodes=nd,rho=rho,P=P,C=C,O=O,A=A,H=H,m=m,W=W,
                linear=linear,quadratic=quadratic,uniform=uniform,actual=actual,
                true_deficit=dp,core_deficit=dc,uniform_pass=uniform>=0,actual_pass=actual>0)

def enc(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {k:enc(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [enc(v) for v in x]
    return x

def main():
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    cases=[(F(1,10000),F(1,20000),rho) for rho in (None,F(101,100),F(3,2),F(2))]
    for c,d in ((F(3,1000),F(1,500)),(F(1,200),F(1,400)),(F(1,100),F(1,200)),(F(1,500),F(1,500))):
        cases += [(c,d,rho) for rho in (None,F(101,100),F(51,50))]
    data=[one(*case) for case in cases]
    assert data[11]['P']['T']==F(2155518603728164661400000,1065579991917354553894843)
    assert data[11]['C']['T']==F(317136889441260199286440200000,156805732128382273017653918249)
    drops=[i for i,R in enumerate(data) if R['C']['T']>2 and R['P']['T']>R['C']['T']]
    assert drops==[1,5,6,8,9,11,12,14,15]
    assert all(R['actual_pass'] for R in data)
    assert [i for i,R in enumerate(data) if not R['uniform_pass']]==[2,3]
    assert data[11]['uniform']>F(1,2000)
    assert data[2]['actual']>F(1,25) and data[3]['actual']>F(7,100)
    assert data[2]['uniform']<-F(3,200) and data[3]['uniform']<-F(1,25)
    raw=(json.dumps(enc(dict(identity='OVERHANG_SHARED_AFFINE_FAN_BUDGET_V1',data=data)),sort_keys=True,separators=(',',':'))+'\n').encode()
    assert len(raw)==66699
    assert hashlib.sha256(raw).hexdigest()=='82adee6b6c554983dcda6799c402c067ff3bbd02db38c2abe45354394f93a6ea'
    target=Path('overhang_fan_budget.json')
    if sys.argv[1]=='build': target.write_bytes(raw)
    else: assert target.read_bytes()==raw
    print('FREE_OVERHANG_BUDGET_CONTROLS_PASS 5_PRISM 11_OVERHANG 9_UNIFORM 11_ACTUAL')
    print('ACTUAL_COMMON_MASS_FACETS_TWO_FANS_PASS',len(data))
    print('PRESERVED_TRUE_ROOT_CUT_DROP_ABOVE_TWO_PASS',len(drops))
    print('OVERHANG_SHARED_AFFINE_FAN_BUDGET_PASS',len(raw),hashlib.sha256(raw).hexdigest())
if __name__=='__main__': main()
```

## 9. Наиболее полезное продолжение

Оставшийся вопрос теперь можно ставить через совместную геометрию S и Po: исключить весь действительный сектор `J>0, J²>=4qDc` с W в указанном замкнутом интервале либо построить в нём действительное высокоследовое тело. Самая явная потеря нового доказательства — замена распределения g_tau на внешней части единственным максимумом H_tau. Следующее усиление должно удерживать площадь, аффинные моменты всего сечения S и настоящие вынужденные внешние пирамиды при том же Pc, вместо независимого усиления скалярных границ. Реальные запасы Dc следует сохранять: два точных крупных контроля уже показывают, что округление их до prism cap может уничтожить полезный сертификат.

Копии для удобства: [полный source](sandbox:/mnt/data/overhang_fan_budget/overhang_fan_budget.py), [полный точный отчёт](sandbox:/mnt/data/overhang_fan_budget/overhang_fan_budget.json). Все новые объекты восстанавливаются из приведённого source; ссылки не являются единственным носителем recovery data.
