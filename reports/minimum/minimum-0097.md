# minimum-0097

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# RAVEN_MERIDIONAL_U7_V2

## 1. Результат

**Нового достигающего собственного однородного 110 и нового weak110-кандидата не получено. Получен полный геометрический запрет, существенно усиливающий и расширяющий прежний fixed-section барьер: U≥7 независимо от числа и адаптации углов.**

Для точно определённого ниже семейства это верно одновременно при любом числе меридиональных подразделений n≥1, любом допустимом вписанном многоугольнике B, любом 0<δ≤1/1000 и любой одной механической метрике с ||M−I||op≤1/16. Многоугольник B не обязан быть правильным; его соседние хорды могут быть сколь угодно короткими. В частности, все правильные m-угольники при **любом m≥3** включены.

Следовательно, исходное семейство parent не содержит 110 ни при каком C в прежнем метрическом боксе. Прежнее утверждение «для 110 необходимо C≥880» остаётся верным, но теперь усиливается до полного исключения этой архитектуры. Это не глобальный запрет и не изменение принятой верхней границы C622.

Дополнительно сохранены три новых точных физических не-рекордных тела:

| Тело | Настоящие V,E,F | C=2E | Собственные строгие S,U,H | Дополнительные weak packets |
|---|---|---:|---|---|
| ADAPTIVE_SHEAR_N1 | 62,132,72 | 264 | 50,42,90 | 0 |
| ADAPTIVE_SHEAR_N2 | 134,276,144 | 552 | 48,42,88 | 0 |
| H61_GRID1E9 | 118,177,61 | 354 | 14,12,24 | 0 |

У всех трёх нет даже безвредных нулевых примитивов: соответственно проверены 528,1104,708 ненулевых VE/EF-примитивов. H61 — отдельная конструкция пересечением полупространств после свободной оптимизации геометрии, а не ещё один член секционного семейства. Ни одно из этих тел не называется near110 или улучшением верхней границы.

## 2. Источники и точное родительство

Прочитан весь update `research-journal(20260919-065515).md`, включая буквальный parent и окончание EOF. Файл: 225440 байт, 2248 текстовых строки, SHA-256 `a67c1c730d4543abb2c89b35a8fe5b0bc07b8c632a489dc868f547c8af6e2cf5`. Неизменённый общий блок до строки1361 совпадает с ранее прочитанным журналом, кроме строки, объявляющей continuation; новые блоки и parent восстановлены полностью.

Parent `minimum-0091` проверен по буквальному содержимому: его compact-JSON оболочка версии2 с завершающим LF в result_markdown имеет 41063 байта и SHA-256 `b52fe5ba38f1159ae673805843d6f6840b15e683579b7a2e301cd4b2daadc94a`. Встроенный исходник совпадает с приложенным `raven_section_certificate.py`: 10153 байта, SHA-256 `847b3dfd4c9cf5d22dfc903e6a5ac652960c22e1b9449511fb0f035dbe00b40b`. Parent действительно утверждал только U≥2 при m≤39 и сохранял собственные не-110 контроли и отдельное гладкое семейство.

Конфликта буквального parent с использованными данными нет. Новая теорема закрывает предложенную в нём возможность исправления **одной лишь общей угловой сетки**, но не опровергает его прежний запрет. Исходники C622 не использованы; ни одно новое тело не является его потомком. Старые потерянные оптимизационные параметры не используются. Новая капсула не требует parent-файла, research-плагина или внешней библиотеки доказательств.

## 3. Новый механизм: максимум по слою, а не по столбцу

Пусть в настоящем выпуклом многограннике выбран слой вершин. Предположим, что у каждой его вершины все истинные рёбра, выходящие из слоя, имеют строго отрицательный радиальный примитив относительно настоящего центра и одной SPD-метрики M.

Выберем в слое вершину x максимальной M-нормы. Для любой другой вершины y того же слоя

    2 xᵀM(y−x) = yᵀMy−xᵀMx−(y−x)ᵀM(y−x) < 0.

Таким образом, все исходящие рёбра у x отрицательны, и x — строгая U-вершина. Равенство максимальных норм не мешает строгому знаку. Размеры угловых хорд вообще не участвуют.

В рассматриваемом семиузловом профиле **все пять сохранённых внутренних слоёв** обладают этим свойством, а обе концевые вершины имеют отрицательные примитивы по всем спицам. Это даёт пять различных послойных максимумов и два апекса: U≥7. Прежний выбор двух столбцовых максимумов скрывал гораздо более сильное меридиональное препятствие.

## 4. Полное новое семейство

### Геометрические параметры

Используются следующие семь строк (z,r,cx,cy), без каких-либо неуказанных параметров:

    (-1,   0,   -2/45,     0)
    (-4/5, 3/5, -1/25,    -1/125)
    (-3/5, 4/5, -4/125,   -3/125)
    (0,    1,    88/1965,  0)
    (3/5,  4/5, -4/125,    3/125)
    (4/5,  3/5, -1/25,     1/125)
    (1,    0,   -2/45,     0).

B — любой выпуклый многоугольник с различными вершинами на единичной окружности, центром площади0 и содержащий диск радиуса2/5 с центром0. Обозначим число его вершин m. Никакой нижней границы соседних хорд нет.

На каждом исходном интервале выбираются n равных подразделений. При t=j/n высота и центр интерполируются линейно, а радиус нового узла равен

    r(t)=(1−t)r_left+t r_right+δt(1−t),    0<δ≤1/1000.

Между новыми узлами снова применяется линейная интерполяция. Сечения тела имеют вид c(z)+r(z)B. Истинная комбинаторика:

    V=m(6n−1)+2,    E=m(12n−1),    F=6nm.

Боковые максимальные грани — четырёхугольники между соответствующими рёбрами B; у концов — треугольники. Диагонали их интеграционной триангуляции не входят в E.

### Настоящая однородность и метрика

Для интервала высоты d с радиусами a,b настоящие объёмный и узловые моментные веса равны

    I=d(a²+ab+b²)/3,
    w_left=d(3a²+2ab+b²)/12,
    w_right=d(a²+2ab+3b²)/12.

Это интегралы реальных сечений, не свободные массы. Сам секционный способ интегрирования унаследован из parent.

Для точного восстановления при любом n положим t=n² и

    q0=(t−1)/(6t),
    q2=(t−1)(9t−1)/(180t²),
    b2=(t−1)(3t−2)/(90t²).

Тогда

    I_n=458/375+(74/25)δq0+2δ²b2,
    J_n=−(32612/1228125)δq0+(49456/1228125)δq2−(17404/736875)δ²b2,
    Vol(K)=Area(B) I_n,
    g=(J_n/I_n,0,0).

Разрешена вся замкнутая операторная область ||M−I||op≤1/16. Она автоматически SPD; простой достаточный покоординатный бокс — max|Mij−Iij|≤1/48. Физическое евклидово тело есть M^(1/2)K, его центр равен M^(1/2)g, объём умножается на sqrt(det M). Полярная механическая метрика только M^−1. Никакого независимого полярного центрирования или изменения плотности нет.

## 5. Доказательство на всём семействе

### Выпуклость и центр для всех n,δ,B

У исходных узлов −Δr′≥2/3 и ||Δc′||<13/50. Подразделение увеличивает исходный скачок r′ не более чем на10δ. Поэтому

    (2/3−10δ)(2/5) > 13/50    при δ≤1/1000.

Внутри исходного интервала скачок c′ равен0, а скачок r′ равен −2δ/(nd)<0. Следовательно, для каждой внешней нормали ребра B профиль h_B(u)r+u·c строго вогнут. Это доказывает выпуклость, истинность всех перечисленных вершин и максимальных граней, а не только локальную выпуклость выбранной сетки.

Исходные точки (r,z) лежат на единичной окружности, а минимальный квадрат хорды между ними равен2/25. Оценка

    2/25 > 2δ+δ²/4

даёт r_n²+z²≤1 на всём профиле. Также 0≤r_n−r_0≤δ/4, откуда

    0≤I_n−I_0≤δ+δ²/8,    I_0=458/375.

Исходный первый момент равен0. Центры c(z) при подразделении не меняются и имеют норму не больше88/1965. Поэтому интегрирование приращения r², а не назначение начала, даёт

    |gx|<δ/20,    gy=gz=0,
    ||c(z)−(gx,0)||<9/200,
    ||x−g||<21/20

для всех рассматриваемых вершин. Все эти оценки равномерны по n и по допустимому B.

### Все выходы из семи сохранённых слоёв отрицательны

Для соседних исходных строк i,j обозначим

    D_ij(u)=(c_j−c_i+(r_j−r_i)u, z_j−z_i),    ||u||=1,
    x_i(u)=(c_i+r_i u,z_i).

В евклидовой метрике при исходном начале

    x_i·D_ij = a_ij+b_ij·u,
    a_ij=c_i·(c_j−c_i)+r_i(r_j−r_i)+z_i(z_j−z_i),
    b_ij=r_i(c_j−c_i)+(r_j−r_i)c_i.

Полная двенадцатистрочная рациональная таблица восстанавливается кодом. Из неё непосредственно следуют две равномерные группы оценок:

    между уровнями |z|=3/5 и4/5:
        x_i·D_ij≤−352/15625,  ||D_ij||<3/10;
    для остальных восьми направленных соседств:
        x_i·D_ij<−9/100,     ||D_ij||<7/10.

Каждая оценка на u получена через a+|b_x|+|b_y|, а оценка длины — через точный квадрат; это не выборка углов.

Настоящее ребро от сохранённой строки к ближайшей новой строке имеет вектор

    (1/n)[D_ij(u)+δ(1−1/n)(u,0)].

Положим η=1/16, K=21/20, γ=δ/20 и возьмём соответствующую границу L на ||D_ij||. После **собственного** переноса и изменения метрики получаем верхнюю границу для n-кратного примитива:

    a+|b_x|+|b_y|+γL+Kδ+ηK(L+δ).

Правая часть монотонна по δ; достаточно её точного значения при δ=1/1000. Максимум по всем двенадцати направлениям равен

    −13679/8000000 < −1/600.

Итак, каждый выход из сохранённого слоя вдоль настоящего меридионального ребра имеет примитив строго меньше −1/(600n). Для концевых вершин та же формула действует при r_i=0 и покрывает все спицы.

Послойная максимизация из раздела3 теперь даёт **семь строгих U при всех допустимых параметрах**, включая границу метрического шара и δ=1/1000. Дополнительные слабые контакты в других местах не могут отменить эти семь строгих равновесий. Ни ограниченность числа углов, ни положительная минимальная хорда, ни общий максимум на фиксированном столбце не нужны.

## 6. Три точно проверенных физических тела

### Адаптивные сечения, действительно пересекающие прежний chord-test

В двух секционных контролях δ=1/1000, n=1 или2. Полный B задан в коде; он получается из прежнего рационального восьмиугольника добавлением четырёх точек с координатами ±(999999/1000001,2000/1000001) в указанном циклическом порядке. Его площадь равна14007998/5000005, центр площади0.

Обе хорды у прежнего опасного направления (−1,0) имеют квадрат4/1000001, существенно меньше (201/1250)². Тем самым прежняя достаточная оценка на длинные хорды здесь намеренно разрушена.

Затем к **самой геометрии** применяется рациональное преобразование

    A=((1,1/100,0),(0,1,1/100),(0,0,1)),    det A=1.

Оно также выходит за прежний крошечный entrymetricbox. В исходных координатах его согласованная метрика равна AᵀA, обратная проверяется кодом. В сохранённых физических координатах уже применён A, поэтому механическая пара равна I,I. Объём не меняется.

Точные собственные объёмы и центры:

    ADAPTIVE_N1:
      Vol=6415663084/1875001875,  g=(0,0,0).
    ADAPTIVE_N2:
      Vol=68454473734373/20000020000000,
      g=(−32745902/21605824186875,0,0).

Фактические классы и V/E/F указаны в первой таблице. Это разные тела, не копии старых C176/368/560. Разбиение создаёт настоящие новые грани и рёбра.

### H61_GRID1E9: сохранённый результат другой архитектуры

Полное определение — 61 строка HNUM в исходнике и полупространства

    (HNUM_i/10^9)·x≤1.

Все 61 строки являются настоящими максимальными гранями; полный точный перебор троек восстанавливает118 вершин и177 истинных рёбер. Никакое объявленное заранее простое комбинаторное число не подменяет проверку hull.

Собственный объём и центр вычислены двумя независимыми тетраэдральными разложениями того же однородного тела. Для ориентации, но не как сертификат:

    Vol ≈4.276113118161479,
    g ≈(0.015405181947644305,0.015456788904237934,0.0281951909159769).

Полные рациональные V,g определены точными суммами в автономном коде и полностью выводятся в отчёт. Механика использует x−g и q/(1−q·g), а не исходное начало полупространств. Принятый точный класс именно14/12/24, weak000, C354.

### Что именно проверено

Выполнены строгие глобальные опорные неравенства, полнота максимальных граней, выпуклость каждой грани, две противоположные ориентации каждого истинного ребра, ссылки вершин, связность и Эйлер. Объём и COM сверены двумя настоящими положительными тетраэдральными разложениями; секционные тела дополнительно сверены с прямыми интегралами сечений и закрытыми формулами I_n,J_n.

На каждом истинном ребре вычислены знаки всех четырёх primal/dual примитивов. Проверены все VE/EF/VF-пакеты с правильным склеиванием VF; локальные списки U/S независимо сверены с глобальными тестами по всем вершинам/полюсам. У всех трёх контролей все примитивы ненулевые.

Для H61 прямое повторение дробных операций после центрирования оказалось неудачной вычислительной реализацией: знаменатель COM содержит5571 десятичных цифр. Сохранённый целочисленный аудитор устраняет эту проблему без изменения математики. При x_i=a_i/d_i, g=G/D знак i→j равен знаку

    (D a_i−d_iG)·(d_i a_j−d_j a_i).

Если исходный полюс q_f=b_f/e_f, положим B_f=e_fD−b_f·G>0. Знак полярного выхода f→h равен знаку

    b_f·(B_f b_h−B_h b_f).

Знаменатели во всех случаях положительны. Это точный способ полного собственного census, не приближение гигантских дробей.

## 7. Численная работа и её честная граница

Свободно оптимизировались строки H-представления, начиная с80 касательных полупространств к гладкому parent-семейству k=1, ε=2/45. При каждом вычислении заново строился hull, восстанавливались вершины, интегрировались настоящий объём и первый момент, и только затем одновременно оценивались primal и polar escape-функции. Метрика этой численной ветви — I с обеих сторон.

Пробовались нормированные по длине направления и ненормированные скалярные escape-loss. Полный использованный исходник ниже. Малый loss сам по себе оказался плохим диагностическим критерием: один численный checkpoint имел loss≈5.52·10^−7, но S/U=25/12. После увеличения целевого запаса сохранён другой checkpoint, округлён к сетке10^−9, очищен от неактивных строк и **заново точно проверен** как H61_GRID1E9.

Остановка L-BFGS-B не является запретом для этого H-класса. Ни один численный checkpoint не принят как110. Точный H61 из полного HNUM — воспроизводимый не-рекордный старт для дальнейшей свободной оптимизации; его восстановление не требует повторять плавающий поиск.

## 8. Автономная точная recovery-капсула

Сохранить следующий исходник с LF и конечным LF как `raven_meridional_barrier.py`. Нужен только **CPython3.13.5, стандартная библиотека**, assertions включены. В нём присутствуют все координатные данные, генераторы, настоящий hull, два объёмных разложения, полный строгий/слабый census и точная таблица семейного запрета. Внешних входных файлов нет.

```python
"""RAVEN_MERIDIONAL_U7_V2. CPython3.13.5, standard library, assertions enabled.
Exact family obstruction plus three fully physical NON-110 controls.
"""
from fractions import Fraction as R
from collections import defaultdict
from itertools import combinations
from math import lcm
from pathlib import Path
import json, hashlib, sys
assert __debug__
sys.set_int_max_str_digits(0)
def dot(a,b): return sum(x*y for x,y in zip(a,b))

def sub(a,b): return tuple(x-y for x,y in zip(a,b))

def scale(t,a): return tuple(t*x for x in a)

def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def det(a,b,c): return dot(a,cross(b,c))

def serial(a):
    if isinstance(a,R): return str(a)
    if isinstance(a,dict): return {str(k):serial(v) for k,v in a.items()}
    if isinstance(a,(tuple,list)): return [serial(v) for v in a]
    return a

def certify(X,F):
    Q=[];uses=defaultdict(list)
    for f,C in enumerate(F):
        a,b,c=(X[i] for i in C[:3]);n=cross(sub(b,a),sub(c,a));h=dot(n,a)
        assert h>0
        q=scale(1/h,n);Q.append(q)
        for i,x in enumerate(X): assert dot(q,x)==1 if i in C else dot(q,x)<1
        for a,b in zip(C,C[1:]+C[:1]):
            assert all(dot(cross(sub(X[b],X[a]),sub(X[v],X[a])),q)>0 for v in C if v not in (a,b))
            uses[tuple(sorted((a,b)))].append((f,a,b))
    assert len(set(Q))==len(Q)
    E=[]
    for (a,b),L in sorted(uses.items()):
        assert len(L)==2 and L[0][1:]==L[1][1:][::-1]
        E.append((a,b,L[0][0],L[1][0]))
    assert len(X)-len(E)+len(F)==2
    for v in range(len(X)):
        ff=[f for f,C in enumerate(F) if v in C]
        assert any(det(*(Q[f] for f in t)) for t in combinations(ff,3))
        link=defaultdict(set)
        for f in ff:
            C=F[f];j=C.index(v);a,b=C[j-1],C[(j+1)%len(C)]
            link[a].add(b);link[b].add(a)
        assert all(len(s)==2 for s in link.values())
        seen={next(iter(link))};todo=list(seen)
        for a in todo:
            for b in link[a]:
                if b not in seen: seen.add(b);todo.append(b)
        assert seen==set(link)
    seen={0};todo=[0]
    for a in todo:
        for u,v,_,_ in E:
            if a in (u,v):
                b=v if u==a else u
                if b not in seen: seen.add(b);todo.append(b)
    assert len(seen)==len(X)
    W=R(0);moment=[R(0)]*3
    for C in F:
        for j in range(1,len(C)-1):
            a,b,c=(X[i] for i in (C[0],C[j],C[j+1]));d=det(a,b,c);assert d>0
            W+=d
            for k in range(3): moment[k]+=d*(a[k]+b[k]+c[k])
    volume=W/6;g=tuple(v/(4*W) for v in moment)
    return Q,E,volume,g

def homogeneous(v):
 d=lcm(*(x.denominator for x in v));return tuple(x.numerator*(d//x.denominator) for x in v),d

def audit(X,Q,E,g):
 G,D=homogeneous(g);VX=[homogeneous(x) for x in X];QQ=[homogeneous(q) for q in Q]
 C=[tuple(D*a-d*b for a,b in zip(v,G)) for v,d in VX]
 B=[d*D-dot(q,G) for q,d in QQ];assert min(B)>0
 ps=[[] for x in X];qs=[[] for q in Q];sgn=[];packets=defaultdict(list);harmless=[]
 for k,(i,j,f,h) in enumerate(E):
  ai,di=VX[i];aj,dj=VX[j];e=tuple(di*v-dj*u for u,v in zip(ai,aj))
  af,_=QQ[f];ah,_=QQ[h];d=tuple(B[f]*v-B[h]*u for u,v in zip(af,ah))
  z=(dot(C[i],e),-dot(C[j],e),dot(af,d),-dot(ah,d))
  s=tuple(int(t>0)-int(t<0) for t in z);sgn.append(s)
  ps[i].append(s[0]);ps[j].append(s[1]);qs[f].append(s[2]);qs[h].append(s[3])
  assert not(s[0]>=0 and s[1]>=0) and not(s[2]>=0 and s[3]>=0)
  if max(s)>0:harmless.extend((k,j) for j,v in enumerate(s) if v==0)
  elif max(s)==0:
   pr=[j for j in (0,1) if s[j]==0];du=[j for j in (2,3) if s[j]==0]
   assert len(pr)<=1 and len(du)<=1
   if pr and du:key=('VF',(i,j)[pr[0]],(f,h)[du[0]-2])
   elif pr:key=('VE',(i,j)[pr[0]],k)
   else:key=('EF',k,(f,h)[du[0]-2])
   packets[key].append(k)
 U=[i for i,s in enumerate(ps) if max(s)<0];U0=[i for i,s in enumerate(ps) if max(s)==0]
 S=[i for i,s in enumerate(qs) if max(s)<0];S0=[i for i,s in enumerate(qs) if max(s)==0]
 H=[i for i,s in enumerate(sgn) if max(s)<0];zero=[i for i,s in enumerate(sgn) if max(s)==0]
 vu=set();fq=set()
 for (kind,a,b),ee in packets.items():
  assert len(ee)==(2 if kind=='VF' else 1)
  if kind in ('VE','VF'):vu.add(a)
  if kind in ('EF','VF'):fq.add(b)
 assert vu==set(U0) and fq==set(S0) and len(zero)==len(U0)+len(S0)
 assert len(S)+len(U)-len(H)==2
 def all_roots(A,D,C):
  a=[];b=[]
  for i,(v,d,c) in enumerate(zip(A,D,C)):
   scores=[dot(c,tuple(d*w-e*x for x,w in zip(v,u))) for j,(u,e) in enumerate(zip(A,D)) if j!=i]
   t=max(scores)
   if t<0:a.append(i)
   if t==0:b.append(i)
  return a,b
 assert all_roots([a for a,d in VX],[d for a,d in VX],C)==(U,U0)
 assert all_roots([a for a,d in QQ],B,[a for a,d in QQ])==(S,S0)
 return dict(SUH=[len(S),len(U),len(H)],S=S,U=U,H=H,S0=S0,U0=U0,weak_packets=[dict(kind=k[0],a=k[1],b=k[2],edges=v) for k,v in sorted(packets.items())],degenerate_edges=zero,harmless_zero_incidences=harmless,edge_signs=sgn)

P=[(R(-1),R(0),R(-2,45),R(0)),(R(-4,5),R(3,5),R(-1,25),R(-1,125)),
   (R(-3,5),R(4,5),R(-4,125),R(-3,125)),(R(0),R(1),R(88,1965),R(0)),
   (R(3,5),R(4,5),R(-4,125),R(3,125)),(R(4,5),R(3,5),R(-1,25),R(1,125)),
   (R(1),R(0),R(-2,45),R(0))]
DELTA=R(1,1000)
r=R(999999,1000001);s=R(2000,1000001)
B=[(R(1),R(0)),(r,s),(R(3,5),R(4,5)),(R(0),R(1)),(R(-3,5),R(4,5)),(-r,s),
   (R(-1),R(0)),(-r,-s),(R(-3,5),R(-4,5)),(R(0),R(-1)),(R(3,5),R(-4,5)),(r,-s)]
A=((R(1),R(1,100),R(0)),(R(0),R(1),R(1,100)),(R(0),R(0),R(1)))
HNUM=[[-1200461104,85946661,-13292305],[-1193676744,-17936867,-55724624],[-1106431536,337850396,-98774941],[-961051515,347342804,289290786],[-928916299,-499698106,229330172],[-928521664,-500074368,229953763],[-780634737,355901919,465662369],[-769485540,-264365347,-537670636],[-687113413,431496697,452271143],[-648373454,-132496374,-618823625],[-607307101,-906913602,191261878],[-606700498,-907175732,191649108],[-604326866,357921751,-553596840],[-423018044,245975246,774340844],[-224371689,-395447751,-950973333],[-224056060,-563365382,-714556732],[-223950796,-396013003,-950840871],[-217473371,440503752,-794275037],[-207842617,-959395802,53975177],[-144729261,280210294,923698741],[-102718382,890484802,-619614962],[-93193890,723272882,549295727],[-60167296,1115968778,-327032438],[-59978376,-886437404,-335769810],[-59364455,1115560033,-328479740],[-23441984,-383266053,813267478],[2852378,728325136,-744973025],[12800785,-873861781,490867323],[48761889,-898856291,-371589357],[89209572,-973893283,364605425],[125461337,429107159,973488368],[126692130,428111466,973741117],[126959401,940808100,43646997],[184922305,192053467,-984600741],[185231189,192058209,-984505829],[222600835,-741625091,675300525],[310382861,-984044428,501613119],[310768573,-983153882,502943159],[356015221,-776913414,-706844904],[357757040,-931863652,58241235],[358876493,-775858572,-706228146],[371385062,-577258660,-800836731],[430270996,868340080,-51709104],[477052640,-900171286,288530069],[487821251,778322409,-482476958],[488076124,778269192,-482397136],[542012328,412984946,691996135],[612265195,-497208459,-387564639],[630119800,-166097740,-878729354],[631126901,-165834926,-877922787],[651646518,213052872,741028920],[651712893,212985270,741024935],[761733194,-218055005,-456068452],[776439002,-410242418,634024467],[776729429,-410688565,633440806],[777069154,521517030,-427023442],[777096920,521233441,-427323568],[846745991,-187302078,584406220],[851657862,334256438,-419822895],[944672624,-86500813,318695083],[953979532,60837583,94302183]]

def second_fan(X,F,V,g):
 a=X[0];W=R(0);G=[R(0)]*3
 for C in F:
  if 0 in C:continue
  for j in range(1,len(C)-1):
   b,c,d=(X[i] for i in (C[0],C[j],C[j+1]))
   w=det(sub(b,a),sub(c,a),sub(d,a));assert w>0;W+=w
   for k in range(3):G[k]+=w*(a[k]+b[k]+c[k]+d[k])
 assert W/6==V and tuple(x/(4*W) for x in G)==g

def profile(N,delta=DELTA):
 assert isinstance(N,int) and N>=1 and 0<delta<=DELTA
 out=[]
 for a,b in zip(P,P[1:]):
  for j in range(N):
   t=R(j,N);v=tuple((1-t)*x+t*y for x,y in zip(a,b))
   out.append((v[0],v[1]+delta*t*(1-t),v[2],v[3]))
 out.append(P[-1]);return out

def section_body(N):
 rows=profile(N);m=len(B);X=[(rows[0][2],rows[0][3],rows[0][0])]
 for z,r,cx,cy in rows[1:-1]:X.extend((cx+r*u,cy+r*v,z) for u,v in B)
 top=len(X);X.append((rows[-1][2],rows[-1][3],rows[-1][0]));F=[]
 for j in range(m):F.append((0,1+(j+1)%m,1+j))
 for k in range(len(rows)-3):
  off=1+k*m
  for j in range(m):
   a=off+j;b=off+(j+1)%m;F.append((a,b,b+m,a+m))
 off=1+(len(rows)-3)*m
 for j in range(m):F.append((off+j,off+(j+1)%m,top))
 return [tuple(dot(row,x) for row in A) for x in X],F,rows

def h_body():
 Q=[tuple(R(a,10**9) for a in row) for row in HNUM];T=[];X=[]
 for t in combinations(range(len(Q)),3):
  a,b,c=(HNUM[i] for i in t);d=det(a,b,c)
  if not d:continue
  u=tuple(x+y+z for x,y,z in zip(cross(b,c),cross(c,a),cross(a,b)))
  if d<0:d=-d;u=scale(-1,u)
  if any(dot(row,u)>d for row in HNUM):continue
  assert tuple(i for i,row in enumerate(HNUM) if dot(row,u)==d)==t
  T.append(t);X.append(scale(R(10**9,d),u))
 assert len(set(X))==len(X);F=[]
 for i in range(len(Q)):
  ids=[j for j,t in enumerate(T) if i in t]
  adj={a:sorted(b for b in ids if b!=a and len(set(T[a])&set(T[b]))==2) for a in ids}
  assert all(len(v)==2 for v in adj.values());C=[min(ids)]
  while True:
   opts=[v for v in adj[C[-1]] if len(C)<2 or v!=C[-2]];nxt=opts[0]
   if nxt==C[0]:break
   assert nxt not in C;C.append(nxt)
  assert len(C)==len(ids)
  if dot(cross(sub(X[C[1]],X[C[0]]),sub(X[C[2]],X[C[0]])),Q[i])<0:C=C[:1]+C[:0:-1]
  F.append(tuple(C))
 return X,F,Q,T

def section_moments(rows,N):
 area2=R(0);J=[R(0),R(0)]
 assert all(dot(b,b)==1 for b in B)
 for u,v in zip(B,B[1:]+B[:1]):
  d=u[0]*v[1]-u[1]*v[0];area2+=d
  for k in range(2):J[k]+=d*(u[k]+v[k])
  assert d>0 and d*d>R(4,25)*dot(sub(v,u),sub(v,u))
 assert J==[0,0]
 weights=[R(0)]*len(rows);I=R(0)
 for i in range(len(rows)-1):
  d=rows[i+1][0]-rows[i][0];a=rows[i][1];b=rows[i+1][1]
  I+=d*(a*a+a*b+b*b)/3
  weights[i]+=d*(3*a*a+2*a*b+b*b)/12
  weights[i+1]+=d*(a*a+2*a*b+3*b*b)/12
 g=tuple(sum(w*p[k] for w,p in zip(weights,rows))/I for k in (2,3,0))
 n=R(N*N);q0=(n-1)/(6*n);q2=(n-1)*(9*n-1)/(180*n*n);b2=(n-1)*(3*n-2)/(90*n*n)
 closedI=R(458,375)+DELTA*R(74,25)*q0+2*DELTA**2*b2
 closedJ=DELTA*R(-32612,1228125)*q0+2*DELTA*R(24728,1228125)*q2+DELTA**2*R(-17404,736875)*b2
 assert I==closedI and g==(closedJ/I,0,0)
 return area2*I/2,tuple(dot(row,g) for row in A),area2/2

def uniform_certificate():
 delta=DELTA;eta=R(1,16);K=R(21,20);gamma=delta/20
 assert (R(2,3)-10*delta)*R(2,5)>R(13,50)
 assert R(2,25)>2*delta+delta*delta/4
 assert (delta+delta*delta/8)/R(458,375)<delta
 assert R(88,1965)+delta/20<R(9,200)<R(1,20)
 for z,r,cx,cy in P:assert r*r+z*z==1 and cx*cx+cy*cy<=R(88,1965)**2
 for i in range(1,6):
  z,r,cx,cy=P[i];zl,rl,xl,yl=P[i-1];zr,rr,xr,yr=P[i+1]
  dr=(rr-r)/(zr-z)-(r-rl)/(z-zl)
  dc=((xr-cx)/(zr-z)-(cx-xl)/(z-zl),(yr-cy)/(zr-z)-(cy-yl)/(z-zl))
  assert -dr>=R(2,3) and dot(dc,dc)<R(13,50)**2
 table=[]
 for i in range(7):
  for j in (i-1,i+1):
   if not 0<=j<7:continue
   z,r,cx,cy=P[i];zz,rr,x,y=P[j];dz=zz-z;dr=rr-r;c=(cx,cy);dc=(x-cx,y-cy)
   a=dot(c,dc)+r*dr+z*dz;b=tuple(r*u+dr*v for u,v in zip(dc,c))
   L=R(3,10) if {i,j} in ({1,2},{4,5}) else R(7,10)
   assert dot(dc,dc)+dr*dr+dz*dz+2*abs(dr)*sum(map(abs,dc))<L*L
   bound=a+sum(map(abs,b))+gamma*L+K*delta+eta*K*(L+delta)
   assert bound<-R(1,600)
   table.append(dict(i=i,j=j,constant=a,linear=b,direction_norm_bound=L,upper_bound=bound))
 assert max(row['upper_bound'] for row in table)==-R(13679,8000000)
 M=tuple(tuple(sum(A[k][i]*A[k][j] for k in range(3)) for j in range(3)) for i in range(3))
 assert det(*A)==1 and sum((M[i][j]-int(i==j))**2 for i in range(3) for j in range(3))<eta*eta
 N=tuple(tuple(cross(M[(j+1)%3],M[(j+2)%3])[i]/det(*M) for j in range(3)) for i in range(3))
 assert all(sum(M[i][k]*N[k][j] for k in range(3))==int(i==j) for i in range(3) for j in range(3))
 assert min(dot(sub(u,v),sub(u,v)) for u,v in zip(B,B[1:]+B[:1]))==R(4,1000001)<R(201,1250)**2
 return dict(delta_upper=delta,metric_operator_bound=eta,metric_entry_sufficient_bound=R(1,48),base_inradius_lower=R(2,5),U_lower=7,meridional_margin_coefficient=R(1,600),table=table,physical_shear=A,chart_metric=M,chart_inverse_metric=N)

def save(name,record):
 data=(json.dumps(serial(record),sort_keys=True,indent=2)+'\n').encode()
 Path(name+'.json').write_bytes(data)
 print('REPORT',name,len(data),hashlib.sha256(data).hexdigest())

def main():
 cert=uniform_certificate();save('raven_u7_uniform',cert)
 for n in (1,2):
  X,F,rows=section_body(n);Q,E,V,g=certify(X,F);second_fan(X,F,V,g);a=audit(X,Q,E,g)
  sv,sg,area=section_moments(rows,n);assert (sv,sg)==(V,g)
  assert [len(X),len(E),len(F)]==[12*(6*n-1)+2,12*(12*n-1),72*n]
  assert a['SUH']==([50,42,90] if n==1 else [48,42,88])
  assert not a['weak_packets'] and not a['harmless_zero_incidences']
  save('raven_adaptive_N%d'%n,dict(name='RAVEN_ADAPTIVE_SHEAR_N%d'%n,delta=DELTA,base=B,base_area=area,profile=rows,vertices=X,maximal_facets=F,true_edges=E,poles=Q,volume=V,centroid=g,physical_metric=((1,0,0),(0,1,0),(0,0,1)),physical_pole_metric=((1,0,0),(0,1,0),(0,0,1)),audit=a))
  print('ADAPTIVE',n,'VEF',len(X),len(E),len(F),'C',2*len(E),'SUH',*a['SUH'],'WEAK000')
 X,F,Q,T=h_body();Q2,E,V,g=certify(X,F);assert Q2==Q;second_fan(X,F,V,g);a=audit(X,Q,E,g)
 assert [len(X),len(E),len(F)]==[118,177,61] and a['SUH']==[14,12,24]
 assert not a['weak_packets'] and not a['harmless_zero_incidences']
 save('raven_h61_exact',dict(name='RAVEN_H61_GRID1E9',denominator=10**9,pole_numerators=HNUM,active_triples=T,vertices=X,maximal_facets=F,true_edges=E,poles=Q,volume=V,centroid=g,physical_metric=((1,0,0),(0,1,0),(0,0,1)),physical_pole_metric=((1,0,0),(0,1,0),(0,0,1)),audit=a))
 print('H61 VEF 118 177 61 C 354 SUH 14 12 24 WEAK000')
 print('ALL_N_ALL_ADMISSIBLE_B_U7_METRIC_BALL_DELTA_INTERVAL_PASS')
 print('THREE_OWN_VOLUME_CONTROLS_TWO_FANS_FULL_WEAK_CENSUS_PASS')
if __name__=='__main__':main()
```

### Команда точного восстановления

```sh
mkdir clean && cd clean
python -S ../raven_meridional_barrier.py
sha256sum *.json ../raven_meridional_barrier.py
```

В новой пустой директории фактически выполнен source-only cold replay; все четыре JSON совпали побайтно. Ожидаемые конечные маркеры:

```text
ADAPTIVE 1 VEF 62 132 72 C 264 SUH 50 42 90 WEAK000
ADAPTIVE 2 VEF 134 276 144 C 552 SUH 48 42 88 WEAK000
H61 VEF 118 177 61 C 354 SUH 14 12 24 WEAK000
ALL_N_ALL_ADMISSIBLE_B_U7_METRIC_BALL_DELTA_INTERVAL_PASS
THREE_OWN_VOLUME_CONTROLS_TWO_FANS_FULL_WEAK_CENSUS_PASS
```

| Объект | Байты | SHA-256 |
|---|---:|---|
| raven_meridional_barrier.py | 13978 | 4c86997ed4fd9d8f267660a519f4b51e9422bb52392936773a63889dfec902b9 |
| raven_u7_uniform.json | 3425 | 285eca24bada507e4617a27318601019022c1b979b93611d34bb669dc219b627 |
| raven_adaptive_N1.json | 32472 | e3b8717e666dbb78e5634c94b332e6f1235c4051689f7b8ccae235c4e6290925 |
| raven_adaptive_N2.json | 65478 | 27ccaf753a884809aada55248f1b39f327a7987e5b065373f3f31d69b8c56f24 |
| raven_h61_exact.json | 103115 | 379de0625d767e25ec6727198fcac81fd71f3830088ae6757ed51a0d09016df3 |
| Полный stdout cold replay | 648 | 1812eeb30b91b50161da3a4db3ee1719a5c421568477d21ae585f46a10993901 |
| h_checkpoint.json: полный HNUM, compact JSON+LF | 2026 | 2218d86cc3124496e878e9d961c29a7dae6e192e6911b1b197d18baa46d2304a |

JSON-отчёты содержат полные массивы вершин, максимальных граней, истинных рёбер, полюсов, собственные рациональные моменты, все знаки и все строгие/слабые списки. Семейный вывод не выводится из трёх контролей: его доказательство — раздел5 и двенадцать равномерных направленных оценок.

## 9. Полный численный search source

Это необязательная discovery-ветвь, а не зависимость точного сертификата. Наблюдённые версии: **CPython3.13.5, NumPy2.3.5, SciPy1.17.0, PyTorch2.10.0+cpu**; код фиксирует один поток. Сохранить как `search_hull.py`, LF и конечный LF. Исходник:3882 байта, SHA-256 `b0e8e1e25e8555417e6bb1c4e091b0033417ce735924ed136541d4fbaa7a54ea`.

```python
"""Numerical discovery only. Python3.13.5 numpy2.3.5 scipy1.17.0 torch2.10.0+cpu."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np, torch, sys, json
from pathlib import Path
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
OUT=Path(__file__).resolve().parent
MODE=os.environ.get('RAVEN_SCORE','unit')
assert MODE in ('unit','raw')
MARGIN=float(os.environ.get('RAVEN_MARGIN','0.0001'))

def seedq(m,seed):
 r=np.random.default_rng(seed);a=1.5*np.pi;e=2/45
 u=r.normal(size=(m-1,3));u/=np.linalg.norm(u,axis=1)[:,None];z=u[:,2];f=a*(z-z*z*z/3)
 c=e*np.column_stack((np.cos(f),np.sin(f)));dc=e*a*(1-z*z)[:,None]*np.column_stack((-np.sin(f),np.cos(f)))
 X=np.column_stack((c+u[:,:2],z));n=np.column_stack((u[:,:2],z-np.sum(u[:,:2]*dc,axis=1)))
 return np.concatenate((n/np.sum(n*X,axis=1)[:,None],[[-1/(1-e),0,0]]))

def combinatorics(q):
 h=ConvexHull(q)
 if max(h.equations[:,3])>=-1e-7:raise ValueError('unbounded')
 t=h.simplices.copy();X=np.linalg.solve(q[t],np.ones((len(t),3,1))).squeeze(-1);T=[]
 for k in h.vertices:
  ids=np.flatnonzero(np.any(t==k,axis=1));p=X[ids];c=p.mean(axis=0);n=q[k]/np.linalg.norm(q[k]);e=p[0]-c;e/=np.linalg.norm(e);f=np.cross(n,e)
  ids=ids[np.argsort(np.arctan2((p-c)@f,(p-c)@e))]
  T.extend((ids[0],ids[j],ids[j+1]) for j in range(1,len(ids)-1))
 return t,np.array(T),h.vertices

def evaluate(q,grad=False):
 t,tri,active=combinatorics(q);Q=torch.tensor(q,requires_grad=grad)
 p=torch.linalg.solve(Q[t],torch.ones((len(t),3,1))).squeeze(-1);v=p[tri]
 d=(v[:,0]*torch.linalg.cross(v[:,1],v[:,2])).sum(dim=1);g=(d[:,None]*v.sum(dim=1)).sum(dim=0)/(4*d.sum())
 p=p-g;r=Q[active];r=r/(1-(r*g).sum(dim=1))[:,None]
 def score(y):
  dd=y[None,:,:]-y[:,None,:];L=torch.linalg.norm(dd,dim=2);unit=dd/(L+torch.eye(len(y)))[:,:,None]
  a=(y[:,None,:]*unit).sum(dim=2)/torch.linalg.norm(y,dim=1)[:,None]-3*torch.eye(len(y))
  if MODE=='raw':a=(y[:,None,:]*dd).sum(dim=2)/(y*y).sum(dim=1)[:,None]-3*torch.eye(len(y))
  mx=a.max(dim=1).values;root=torch.argmax((y*y).sum(dim=1));mask=torch.ones(len(y));mask[root]=0
  return (torch.relu(MARGIN-mx)**2*mask).sum(),int((mx.detach()<0).sum())
 cp,U=score(p);cq,S=score(r);cost=cp+cq+1e-6*((Q*Q).sum(dim=1).mean()-1)**2
 if grad:
  cost.backward();return float(cost.detach()),Q.grad.detach().numpy().ravel()
 return float(cost.detach()),S,U,len(p),len(active),g.detach().numpy().tolist()

def run(m,seed,iterations=350,start=None):
 q=seedq(m,seed) if start is None else np.load(start)['q'];m=len(q);initial=q.copy();best=float('inf');count=0;log=[]
 def fun(x):
  nonlocal best,count
  z=x.reshape(m,3);count+=1
  try:
   f,g=evaluate(z,True)
   if not np.isfinite(f) or not np.isfinite(g).all():raise ValueError('nan')
  except Exception:return 1e3+np.sum((z-initial)**2),2*(z-initial).ravel()
  if f<best:
   best=f;np.savez(OUT/('h_best_%d_%d.npz'%(m,seed)),q=z)
   if not log or f<.85*log[-1][1]:
    row=[count,*evaluate(z)];log.append(row);print(seed,*row,flush=True)
    (OUT/('h_log_%d_%d.json'%(m,seed))).write_text(json.dumps(log))
  return f,g
 R=minimize(fun,q.ravel(),jac=True,method='L-BFGS-B',options=dict(maxiter=iterations,maxls=25,ftol=1e-14,gtol=1e-10,maxcor=20))
 np.savez(OUT/('h_end_%d_%d.npz'%(m,seed)),q=R.x.reshape(m,3))
 print('END',seed,R.message,evaluate(R.x.reshape(m,3)),flush=True)
if __name__=='__main__':
 if sys.argv[1]=='freeze':
  q=np.load(sys.argv[2])['q'];a=np.round(q*10**9).astype(np.int64)
  a=a[ConvexHull(a.astype(float)).vertices]
  rows=sorted(set(tuple(map(int,r)) for r in a))
  data=(json.dumps(rows,separators=(',',':'))+'\n').encode()
  Path(sys.argv[3]).write_bytes(data)
 else:run(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]) if len(sys.argv)>3 else 350,sys.argv[4] if len(sys.argv)>4 else None)
```

Точные использованные запусковые параметры и последовательность:

```sh
RAVEN_SCORE=unit RAVEN_MARGIN=0.0001 python search_hull.py 80 731 350
RAVEN_SCORE=raw RAVEN_MARGIN=0.0001 python search_hull.py 80 732 1200 h_best_80_731.npz
RAVEN_SCORE=raw RAVEN_MARGIN=0.003 python search_hull.py 80 733 2000 h_best_80_732.npz
python search_hull.py freeze h_best_80_733.npz h_checkpoint.json
```

Численная траектория чувствительна к floating-point реализации; математическая принятность не зависит от её побайтного повторения. Замороженные61 целочисленная строка уже полностью встроены в точную капсулу. Полный stdout и плавающие файлы текущих запусков дополнительно сохранены в архиве, но не являются единственным носителем нового геометрического checkpoint.

## 10. Наиболее полезное продолжение

Общая угловая адаптация при сохранении этого меридионального профиля теперь исключена, в том числе когда обе соседние хорды прежнего опасного столбца очень коротки. Необходимо менять **сами межслойные направления и радиальные наклоны**, а не только n или углы: например, заменять сохранённые сферические узлы новым профилем, менять центры в настоящем секционном моментном ядре либо менять межслойную комбинаторику через разные B_i. Теорема не исключает такие изменения и не исключает произвольные SPD-метрики вне указанного шара.

Послойную лемму стоит использовать как предварительный геометрический тест: пока два или более слоя имеют отрицательными все истинные выходы наружу, оптимизация углов не может дать U=1. Для произвольного M выход x(u)ᵀMD(u) является явной квадратичной формой на единичной окружности; это позволяет проверять и целенаправленно разрушать препятствие до дорогого полного поиска S/U/H.

Для другой архитектуры точный H61_GRID1E9 можно продолжать непосредственно с HNUM/10^9. Его настоящие собственные14/12/24 и отсутствие слабых контактов известны; более низкий loss не следует принимать за уменьшение числа равновесий. Новая110-конструкция и соответствующая верхняя граница остаются задачей продолжения.

Дополнительные файлы: точный автономный исходник (`raven_meridional_barrier.py`), полный пакет с отчётами и численной ветвью (`raven_u7_recovery.zip`). Полная recovery-информация уже находится в этом handoff.
