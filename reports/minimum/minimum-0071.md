# minimum-0071

AI research report · 2026-09-16 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# E17_AUGMENTED_AFFINE_FLUX_RANK8_BELT_V1

## Результат и область принятия

**Универсальная полноранговость дополненного потока тоже ложна:** существует настоящее рациональное выпуклое однородное тело с `(V,E,F)=(10,17,9)`, для которого `rank Φ=rank[Φ;c]=8`. Полный ненулевой вектор ν удовлетворяет всем пятнадцати строкам, включая `Σν_i c_i=0`. Более того, рациональный евклидов аффинный образ этого тела имеет строгий класс **222**; все 162 тени между различными вершинами или полюсами ненулевые. Ранговый дефект не является ни геометрическим вырождением, ни механической нулевой стенкой.

Результат усилен полной непрерывной теоремой на новой двухпараметрической семье: указаны весь геометрический домен, точная кривая ранга8, единственное ядро и его физический смысл. **На всей этой кривой один настоящий компонент гранного второго момента устраняет ядро**, с явным положительным запасом в установленной нормировке. Поэтому `[Φ;c;T_yy]` имеет ранг9 на всей семье и её невырожденных аффинных образах с соответствующим переносом линейной функции y. Глобальная полноранговость дополнения вторыми моментами для остальных E17-геометрий здесь не утверждается.

Получен также независимый от каталога конечный достаточный критерий: **35 настоящих скалярных гранных моментов степеней≤4 однозначно определяют веса любой девятигранной геометрии**, включая все E17 и все ранговые границы. Достаточность относится к массам при заданной действительной геометрии, а не к существованию геометрии или невозможности110.

Новых полных root/type-исключений: **0**. Принятые `V≥10,F≥9,C≥34` и реестр `632/52585` не меняются. Родитель уже отделял свой rank8-контроль от этих глобальных вопросов.

## 1. Буквальная власть источников и выполненная работа

Полностью прочитан приложенный immutable родитель **minimum-0068**, SHA-256 **80f95b882a35ae8de063c134068898e89bf129db83c0f48a9116d03d101c03ff**. Его компактный JSON-envelope восстановлен как **45852 байта с этим SHA**. Оба его исходника прочитаны целиком и повторно исполнены; источники и три родительских результата совпали с опубликованными pins. Семейство roof, его ядро и механические метрики не изменены. Новый объект ниже не переименовывает roof или epsilon-контроль и не получает выдуманного канонического ID.

Текущий вход: `research-journal(20260916-142136).md`, **4764851 байт / 684fab34115bb239d1fd4e6012786e66ab4f9aeb89d3a70cac322eb7888987df**. Сначала прочитан актуальный синтез, затем релевантная запись о ранге и полный буквальный родитель. Нерелевантные архивные материалы не используются; обязательного отсутствующего входа для настоящего результата нет. Родительский roof остаётся примером, где центроидное дополнение устраняет дефект, а не универсальным доказательством.

Основной новый ход — разложить фактическую матрицу по двум отражениям и построить тело с четырьмя парами граней и одной торцевой гранью. Настоящие прямоугольные сечения дают точные центры площадей. Чётный блок первого потока имеет пять столбцов и четыре строки. Добавленное центроидное уравнение становится зависимым на явной кривой. Это привело к точному рациональному объекту; затем проверены настоящий второй момент, полная механика и непрерывное продолжение. Никакой отрицательный численный поиск не используется как исключение.

## 2. Полная геометрическая семья

Параметры: **`−1<k<s<1`**. Определим

`P(k,s)={ (x,y,z): |y|≤min(1+x,1+kx), |z|≤min(1+sx,1+kx), x≤1 }`.

Все девять правых частей H-представления равны1. Нормали, в неизменном порядке:

~~~text
n0=(-1,-1,0), n1=(-1,1,0),
n2=(-k,-1,0), n3=(-k,1,0),
n4=(-s,0,-1), n5=(-s,0,1),
n6=(-k,0,-1), n7=(-k,0,1), n8=(1,0,0).
~~~

Полные вершины и максимальные циклы:

~~~text
v0=(-1,0,-(1-s)); v1=(-1,0,1-s);
v2=(0,-1,-1); v3=(0,-1,1); v4=(0,1,-1); v5=(0,1,1);
v6=(1,-(1+k),-(1+k)); v7=(1,-(1+k),1+k);
v8=(1,1+k,-(1+k)); v9=(1,1+k,1+k).

F=[[3,1,0,2],[1,5,4,0],[2,6,7,3],[8,4,5,9],
   [0,4,2],[5,1,3],[2,4,8,6],[3,7,9,5],[6,8,9,7]].

E=[[0,1],[0,2],[0,4],[1,3],[1,5],[2,3],[2,4],[2,6],
   [3,5],[3,7],[4,5],[4,8],[5,9],[6,7],[6,8],[7,9],[8,9]].
~~~

Для `−1≤x≤0` сечение — прямоугольник с полуширинами `1+x` и `1+sx`; для `0≤x≤1` — квадрат полуширины `1+kx`. При x=−1 прямоугольник сжимается только в настоящий отрезок. Все остальные размеры положительны. Поэтому перечисление является полным для всей открытой области, без дополнительного предположения общего положения: имеются десять различных вершин, семнадцать истинных рёбер, две треугольные и семь четырёхугольных максимальных граней. Переход наклонов строгий, поскольку `k<1` и `k<s`; новые неинцидентные контакты невозможны. Начало координат строго внутри P.

Пусть `V=Vol(P)`, `o=(m,0,0)` — **собственный объёмный центр**. Прямое интегрирование сечений даёт

`V=4(3/2−s/6+k+k²/3)`,
`m=(4+s+8k+3k²)/(18−2s+12k+4k²)`.

Положим

`a=(2s−3)/(3(2−s))`, `b=(3+2k)/(3(2+k))`, `d=−1/3`.

Сырые настоящие центры площадей в указанном порядке:

~~~text
g0=(a,-1-a,0); g1=(a,1+a,0);
g2=(b,-1-kb,0); g3=(b,1+kb,0);
g4=(d,0,-1-sd); g5=(d,0,1+sd);
g6=(b,0,-1-kb); g7=(b,0,1+kb); g8=(1,0,0).
~~~

Например, на F0 среднее x вычисляется с фактической линейной шириной `1+sx`: это отношение интегралов `∫x(1+sx)dx/∫(1+sx)dx` на `[−1,0]`, а не среднее четырёх вершин. Соответствующие настоящие `Area(F_i)/||n_i||` равны

`(2−s,2−s,2+k,2+k,1,1,2+k,2+k,4(1+k)²)`.

Используем `h_i=1−n_i·o>0`, `q_i=n_i/h_i`, `c_i=g_i−o`, `ω_i=Area(F_i)h_i/(3V||n_i||)`, `T_i=E_Fi[(x−o)(x−o)ᵀ]`. Все эти величины принадлежат одной постоянной плотности и одной геометрии.

## 3. Полная теорема ранга на семье

Обозначим `Ψ=[Φ;c]`, где `Φ_i=(q_i,vec_row(q_i c_iᵀ))`. Тогда

**`rank Φ=8` во всей области `−1<k<s<1`.**

**`rank Ψ=8` тогда и только тогда, когда**

`s=s₀(k)=(29k²+78k+45)/(15k²+42k+31)`,
`−1<k<κ*=(-9+4√2)/7`.

Во всех остальных точках этой области `rank Ψ=9`. Более глубокого дефекта здесь нет. Это полная стратификация данной непрерывной семьи, не generic-утверждение и не классификация остальных E17-типов.

### Доказательство

Для вычисления Ψ можно пользоваться сырыми столбцами `(n_i,vec(n_i g_iᵀ),g_i)`. Вообще полная тензорная колонка `(h_i,n_i)⊗(1,g_i)` при переносе центра меняется обратимыми четырёхмерными преобразованиями обоих множителей и ненулевым масштабом столбца. Строка h_i уже равна следу `n_i g_iᵀ`. Это доказывает инвариантность ранга и перевод ядра `ν_i=h_i κ_i` из сырой карты. Ни центр полярного тела, ни средние вершин вместо площадей не требуются.

Отражения y и z разбивают девять колонок на чётный блок размерности5 и два нечётных блока размерности2. Последние имеют ранг2: строки `n_y,n_y g_x` различают `a<0<b`, а строки `n_z,n_z g_x` различают `d<0<b`.

Чётный блок Φ, с представителями пар `F0/F1,F2/F3,F4/F5,F6/F7` и отдельной F8, равен

~~~text
B4=[[-1, -k,  -s,  -k, 1],
    [-a,-kb, -sd, -kb, 1],
    [1+a,1+kb,0,    0, 0],
    [0,   0,1+sd,1+kb, 0]].
~~~

Положим `H=k²+3k+3`,
`A0=s(3k²+9k+8)−k(k+3)`,
`A2=s(3k²+9k+10)−5k(k+3)−18`.

Два 4×4 минора, после удаления соответственно колонок0 и2, равны

`2H A0/[9(k+2)²]`, `−2H A2/[9(k+2)²(s−2)]`.

Одновременно они нулевыми быть не могут: `A2−A0=2[s−2k(k+3)−9]<−8`, поскольку `k>−1,s<1`. Поэтому `rank B4=4` и `rank Φ=4+2+2=8`.

Единственная новая чётная строка Ψ — `(a,b,d,b,1)`. Определитель B5 после её добавления:

`det B5=−2(s−1)H[(15k²+42k+31)s−(29k²+78k+45)]/[27(s−2)(k+2)²]`.

Все множители, кроме последней квадратной скобки, ненулевые в физической области. Кроме того,

`R=15k²+42k+31=15(k+7/5)²+8/5>0`,
`R(s₀−k)=(k+1)(3k+5)(9−5k)>0`,
`R(s₀−1)=2(7k²+18k+7)`.

Следовательно, условие `k<s₀<1` эквивалентно точному интервалу, приведённому в теореме. Все факторизации воспроизводятся символически полным исходником ниже.

## 4. Ядро всей исключительной кривой и устранение вторым моментом

Пусть `G=k²+6k+17`, `J=7k²+18k+7`, `R=15k²+42k+31`. Зададим пять полных рациональных функций

~~~text
θ0=1,
θ1=−8(k+2)/G,
θ2=(k−1)(k+3)R/[2(k+1)(3k+5)G],
θ3=−4(k−1)(k+2)(k+3)/[(k+1)(3k+5)G],
θ4=−(k−1)J/[2(k+1)G].
~~~

Тогда сырое ядро задаётся

`κ=(θ0/2,θ0/2,θ1/2,θ1/2,θ2/2,θ2/2,θ3/2,θ3/2,θ4)`;

фактическое ядро — `ν_i=(1−n_i·o)κ_i`. Все его девять компонент ненулевые внутри кривой; знаки в этой нормировке — `(+,+,−,−,−,−,+,+,−)`. Отражения скрывают перераспределение между четырьмя парами граней от нечётных строк. Ранговое равенство показывает, что это **всё** ядро.

На кривой

`V=4(k²+3k+3)(5k²+14k+13)/R`,
`m=(9k²+24k+13)/(12(k²+3k+3))`.

Настоящие сырые yy-моменты пяти представителей равны

`((4−s)/(6(2−s)), (k²+2k+2)/2, 1/6, (k²+2k+2)/6, (1+k)²/3)`.

Это непосредственно интегралы квадратов по полосам соответствующих граней. Например, первый — `∫(1+x)²(1+sx)dx/∫(1+sx)dx`; четвёртый имеет дополнительный множитель1/3 от равномерного отрезка по y. Перенос объёмного центра по x не меняет yy.

Подстановка настоящего ν даёт **на всей кривой**

`Σν_i(T_i)_yy=−P8(k)/[144(k+1)(3k+5)(k²+3k+3)(k²+6k+17)]`,

где полный полином

~~~text
P8=1494k^8+15708k^7+68621k^6+161252k^5+216907k^4
   +159588k^3+49779k^2−3636k−4113.
~~~

Полное положительное удостоверение без выборки: в базисе Бернштейна степени8 после `k=−1+(4/7)v`, `0≤v≤1`, коэффициенты **−P8** равны

~~~text
[224,1328/7,48448/343,203312/2401,2862304/84035,
 270192/16807,8712576/117649,215811216/823543,
 3474015840/5764801].
~~~

Все они больше16. Поскольку `κ*<−3/7`, этот замкнутый интервал покрывает всю физическую кривую. Знаменатель положителен и меньше `144·1·5·3·17=36720`. Итак,

**`Σν_i(T_i)_yy>1/2295`**

в ровно указанной нормировке `θ0=1`. Эта численная константа относится к установленной координатной карте; ранговое следствие аффинно инвариантно.

Настоящее конусное тождество `Σ=(3/5)Σω_iT_i` теперь устраняет единственный массовый параметр. Вне кривой уже достаточно Ψ. Поэтому **`rank[Φ;c;T_yy]=9` на всей двухпараметрической области**, включая её внутреннюю ранговую границу. Это независимая от механической метрики теорема. Для аффинного образа нужно переносить линейную функцию y или использовать полный тензор T, а не выбирать новую несогласованную метрику.

## 5. Полный рациональный контроль того же f-vector

Выбрано **`k=−3/4,s=45/127`**. В списках раздела2 это означает `1−s=82/127`, `1+k=1/4`; все десять вершин, девять H-строк, циклы и семнадцать рёбер заданы буквально. Точные интегралы:

~~~text
Vol=1785/508,  o=(1/252,0,0),
Σ=diag(4191847/26989200,11581/61200,180156947/767740400).

ω=(52877/337365,52877/337365,42545/359856,42545/359856,
   1187/12495,1187/12495,42545/359856,42545/359856,
   31877/1349460).
~~~

Настоящие `Area/||n||` — `(209/127,209/127,5/4,5/4,1,1,5/4,5/4,1/4)`. Вместе с буквальными нормалями это задаёт все настоящие площади, в том числе их радикалы, без квадратнокорневого округления.

### Полная фактическая матрица и ядро

Порядок строк Ψ: `q_x,q_y,q_z,q_xc_x,q_xc_y,q_xc_z,q_yc_x,q_yc_y,q_yc_z,q_zc_x,q_zc_y,q_zc_z,c_x,c_y,c_z`.

`Ψ=Z diag(D)⁻¹`, со всеми данными:

~~~text
D=[13325004,13325004,422100,422100,113966244,113966244,
   422100,422100,63252]
Z=[
[-13272336,-13272336,317520,317520,-40325040,-40325040,317520,317520,63504],
[-13272336,13272336,-423360,423360,0,0,0,0,0],
[0,0,0,0,-113806224,113806224,-423360,423360,0],
[6212556,6212556,125748,125748,13601700,13601700,125748,125748,63252],
[7112448,-7112448,-222264,222264,0,0,0,0,0],
[0,0,0,0,35562240,-35562240,-222264,222264,0],
[6212556,-6212556,-167664,167664,0,0,0,0,0],
[7112448,7112448,296352,296352,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,38387020,-38387020,-167664,167664,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,100364544,100364544,296352,296352,0],
[-6237209,-6237209,167165,167165,-38440995,-38440995,167165,167165,63001],
[-7140672,7140672,-295470,295470,0,0,0,0,0],
[0,0,0,0,-100505664,100505664,-295470,295470,0]]

ν=(-1163294,-1163294,884400,884400,2019087,2019087,
   -2532600,-2532600,1584814)
~~~

Первые три и последние три строки этой полной матрицы также буквально задают все q_i и все **настоящие** c_i. Проверены `Ψν=0`, `Σν_i=0` и ненулевой минор по строкам `(0,1,2,3,4,5,7,11)`, колонкам `(0,1,2,3,4,5,6,7)`:

`161981404497794379669917663232 / 32547126255098083369971484375 >0`.

Таким образом, ранг точно8. Целый ν равен `−2317392` умножить на нормированное семейное ядро предыдущего раздела.

### Все настоящие гранные вторые моменты

В следующей полной таблице строка i задаёт шесть компонент симметричного `T_i` в порядке `(xx,yy,zz,xy,xz,yz)`:

~~~text
0: (3996929/13272336,463/1254,22853/96774,635/3762,0,0)
1: (3996929/13272336,463/1254,22853/96774,-635/3762,0,0)
2: (14617/63504,17/32,17/96,-2/9,0,0)
3: (14617/63504,17/32,17/96,2/9,0,0)
4: (10753/63504,1/6,25313/32258,0,5/18,0)
5: (10753/63504,1/6,25313/32258,0,-5/18,0)
6: (14617/63504,17/96,17/32,0,-2/9,0)
7: (14617/63504,17/96,17/32,0,2/9,0)
8: (63001/63504,1/48,1/48,0,0,0).
~~~

Получено

`Σν_i T_i=diag(2389931/3,−882087/8,35446202897/129032) ≠0`.

После добавления строки yy ненулевой 9×9 минор по строкам `(0,1,2,3,4,5,7,11,15)` равен

`−31115350860027428349281067466752 / 89862615590325808184491268359375`.

### Что действительно не определяют первые потоки

Все положительные решения первого потока **с добавленным настоящим центроидным уравнением** — ровно

`w(τ)=ω+τν`,
`−127/8520490440 < τ < 127/2720511360`.

На нижней границе обнуляется вес F8; на верхней — веса F6,F7. Внутри все веса положительны. Однако только τ=0 даёт настоящие однородные конусные массы этой геометрии.

Для всей линии определим `Λ(w)[:,i]=3w_i(1−Qc_i)`. Тогда **точно сохраняются** `Λ1=3·1`, `ΛQ=−Q`, `Λ²+Λ=12·1wᵀ`, `rank Λ=4`, `d_i=(Λ²)_ii/4=3w_i`. Последнее следует из первых трёх балансов, не из независимого подбора строк. При буквальном `τ=1/100000000` дополнительно проверены положительность всех весов и строгий cap `0<Λ_ij<10/9` при i≠j.

В отличие от ложной линии родительского roof, эта линия **не отсеивается Λ1=3**. Но она не проходит настоящую общую Σ: при указанном τ ошибка предполагаемой объёмной ковариации равна

`diag(2389931/500000000,−2646261/4000000000,106338608691/64516000000000)`.

Это барьер выводу «дополненные первые потоки уже определили реальные массы», а не две различные однородные плотности на одном теле. Площади и настоящие массы геометрически фиксированы; меняются лишь не удовлетворяющие полной физике предложения весов.

### Строгая механика и ненулевая камера

Возьмём рациональное линейное преобразование

~~~text
A=[[10,1,1],[0,3,1],[0,1,1]], det A=20,
M=AᵀA=[[100,10,10],[10,11,5],[10,5,3]],
N=M⁻¹=[[1/50,1/20,-3/20],[1/20,1/2,-1],[-3/20,-1,5/2]].
~~~

У **одного настоящего евклидова тела** `A(P−o)` вершины равны `A(v_i−o)`, полюса `A⁻ᵀq_i`, центры площадей `Ac_i`, моменты `AT_iAᵀ`, объём `8925/127`, собственный центр0 и ковариация `AΣAᵀ`. Все эти полные рациональные массивы дополнительно записывает исходник.

Полный точный аудит даёт `S={5,6}`, `U={0,9}`, `H={(1,5),(2,6)}`, то есть222. Минимальные абсолютные значения по всем различным парам: вершинные тени **1/2**, полюсные **3921372/398481325**. Проверены все17 настоящих рёбер и все162 тени, а не выборка.

На замкнутом шестимерном боксе `|M′_ij−M_ij|≤2^-24` сохраняются положительность M′ и каждый из162знаков при `N′=(M′)⁻¹`. Доказательство использует `λ_min(M)>det(M)/Σ principal2minors=50/151`, норму возмущения≤3ε и буквальные оценки ошибок линейных и adjugate-квадратичных числителей, проверенные Fraction. Поэтому ранговая кривая не является механической стенкой. По непрерывности есть и относительно открытая геометрическая окрестность этой точки внутри кривой с тем же классом. Область110 этим не закрыта: контроль имеет две неустойчивые вершины.

## 6. Универсальная конечная достаточная система масс

**Теорема.** Пусть P — любой настоящий полноразмерный выпуклый политоп с m максимальными гранями. Матрица нормированных настоящих скалярных гранных моментов всех мономов степени≤`floor(m/2)` имеет полный столбцовый ранг m.

**Полное доказательство.** Предположим, что ν — ненулевой вектор её ядра. Константная строка даёт `Σν_i=0`, значит присутствуют оба знака. Сменив общий знак, можно добиться, чтобы отрицательных компонент было не более `floor(m/2)`. Пусть I — их индексы. Для одного общего внутреннего центра запишем положительные внутри P слэки `Y_j=1−q_j·x`. Полином `f=Π_{j∈I}Y_j` имеет разрешённую степень. На каждой грани из I он тождественно нулевой, а в относительной внутренности любой другой максимальной грани строго положителен: различные настоящие максимальные грани не содержат относительные внутренности друг друга. Поэтому `Σν_i E_Fi f>0`, что противоречит принадлежности ν ядру. Доказательство покрывает все формы граней, все нулевые внутренние определители и любые размерности пространства; выборки и общий вид не используются.

Для m=9 имеются **35** мономов `x^α`, `|α|≤4`. У своего объёмного центра настоящие массы удовлетворяют конечной линейной системе

`Σ_i w_i E_Fi x^α = (|α|+3) E_P x^α /3`, для всех `|α|≤4`.

Радиальное интегрирование каждой настоящей пирамиды доказывает необходимость; теорема ранга доказывает **единственность** её решения `w=ω`. Любые девять независимых строк полного35-строчного массива после точного исключения Гаусса достаточны при фиксированной геометрии. Это глобальный достаточный критерий массовой жёсткости, действующий и на всём E17, но он использует именно настоящие гранные и объёмные моменты. Подстановка свободных моментных блоков не сохраняет доказательство. Он не является сам по себе достаточным критерием реализации полюсов, заданных моментов или механики110.

## 7. Точное оставшееся содержание задачи

Основная развилка назначения разрешена: `[Φ;c]` не всегда имеет ранг9 даже в действительном E17, вне механических стенок. Новый пример проходит всю первую Λ-алгебру, но вся его непрерывная ранговая кривая отсеивает ложные массы одним настоящим вторым моментом. **Не доказано**, что `[Φ;c;T]` полнорангова для всех остальных E17-тел; такой глобальный вывод нельзя получить из нашей кривой или её аффинной орбиты. Не заявляются другие канонические ранговые страты или новая полная110-невозможность.

Самое полезное продолжение теперь — искать или исключать одновременно `Φν=0`, `Σν_i c_i=0`, **`Σν_i T_i=0`** на других настоящих E17-геометриях. Для полного устранения свободных масс уже доступна доказанная система степени4; остаётся выяснить, можно ли на всём насыщенном срезе снизить её до вторых моментов с аффинным потоком, и только затем использовать это в механическом исключении. Это отличается от повторного generic-rank теста или независимых PSD-матриц.

## 8. Полная recovery-капсула

Два следующих исходника полностью автономны. Первый содержит все точные геометрические входы, восстанавливает все H-тройные пересечения, проверяет максимальные грани и17рёбер, вычисляет настоящие моменты; объём, центр и ковариация дополнительно проверяются независимым интегрированием прямоугольных сечений. Он проверяет оба ранга, ядро, ненулевые миноры, ложную линию, Λ-алгебру и полную механическую камеру. Второй восстанавливает все символические факторизации, всю ранговую кривую и положительный Bernstein-сертификат настоящего второго момента.

Среда фактических запусков: **CPython3.13.5, SymPy1.14.0** только для второго файла. Первый запускается с `-S` и требует лишь стандартную библиотеку. Все параметры и точные входы буквальны; assert включены, случайности и численного оптимизатора нет. Сохранить UTF-8/LF с конечным LF:

~~~sh
python -S augmented_belt.py > augmented_belt.log
python belt_stratum.py > belt_stratum.log
# Необязательная аутентификация буквального родителя:
python -S augmented_belt.py 'research-journal(20260916-142136).md'
~~~

Наблюдён холодный повтор в отдельном каталоге: оба JSON и оба лога совпали побайтно. Затем оба исходника извлечены из полного result_markdown и исполнены в ещё одном каталоге с тем же результатом; все буквальные строки Ψ и таблицы T также сопоставлены с точным JSON. Основной маркер первого источника: `ACTUAL_E17_PHI_AND_CENTROID_AUGMENTATION_RANK8_PASS`; второго: `ACTUAL_YY_MOMENT_RESTORES_RANK9_ON_ENTIRE_STRATUM_PASS`. Дополнительные маркеры и pins:

~~~text
EXACT_ALL15_ROWS_NULL_AND_NONZERO_8_MINOR_PASS
POSITIVE_FAKE_MASSES_PASS_FULL_LAMBDA_ALGEBRA_BUT_FAIL_ACTUAL_COVARIANCE
RATIONAL_EUCLIDEAN_CLASS_2_2_2_ALL162_SHADOWS_NONZERO_PASS
CLOSED_SIX_ENTRY_METRIC_BOX_PASS 1/16777216
FULL_TWO_PARAMETER_E17_GEOMETRIC_RANK_STRATA_IDENTITIES_PASS
BARE_PHI_RANK8_EVERYWHERE_AUGMENTED_RANK8_EXACTLY_ON_STATED_CURVE
POSITIVE_NINE_BERNSTEIN_COEFFICIENTS_AND_UNIFORM_1_OVER_2295_PASS
~~~

| Объект | Байты | SHA-256 |
|---|---:|---|
|augmented_belt.py|11814|3b477b4d3a6b27aef52930b0b949e71d944bbd6f19f2efd86222f9ec9e757927|
|augmented_belt.json|14982|88b7be74fdcdbdf4fa096218fe214aa7ac7c15966b0ed776f4533a6853f864ad|
|augmented_belt.log|481|09bdbffea8bf311343a5a4864ba492656cbb1117c6be69d3bf80d2d91f241ca3|
|belt_stratum.py|4771|868e8ce5e73546b7c9749f151c8c7c86b3f426476d2b86e96a9c7ae6a954c316|
|belt_stratum.json|1336|8ad0e4309fb205b6e477731c04a24720a58517967961a05df303b16a9cb061f2|
|belt_stratum.log|402|f8c804d631e86fb8e77980f6d2be1a885826b17607ce515ac1183ea002230ce4|

Дополнительные копии: геометрический verifier (`augmented_belt.py`), символический verifier (`belt_stratum.py`), полный точный объект (`augmented_belt.json`). Основой восстановления являются следующие полные исходники, а не эти ссылки.

### Полный исходник augmented_belt.py

```python
"""E17_AUGMENTED_AFFINE_FLUX_RANK8_BELT_V1.
CPython 3.13.5, standard library; run python -S augmented_belt.py.
Optional argument: the exact research-journal(20260916-142136).md attachment.
Parent minimum-0068,
80f95b882a35ae8de063c134068898e89bf129db83c0f48a9116d03d101c03ff.
No external geometry, optimizer, random seed, or floating-point predicate.
"""
from fractions import Fraction as F
from itertools import combinations,product
from pathlib import Path
from math import lcm
import hashlib,json,sys
assert __debug__
PARENT='minimum-0068'
PINSHA='80f95b882a35ae8de063c134068898e89bf129db83c0f48a9116d03d101c03ff'
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[dot(r,c)for c in zip(*b)]for r in a]
def det(a):
 b=[list(map(F,row))for row in a];v=F(1)
 for k in range(len(b)):
  j=next((j for j in range(k,len(b))if b[j][k]),None)
  if j is None:return F(0)
  if j!=k:b[k],b[j]=b[j],b[k];v=-v
  z=b[k][k];v*=z
  for i in range(k+1,len(b)):
   r=b[i][k]/z
   for j in range(k+1,len(b)):b[i][j]-=r*b[k][j]
 return v
def solve(a,b):
 d=det(a);assert d
 return tuple(det([[b[i]if j==k else a[i][j]for j in range(len(b))]for i in range(len(b))])/d for k in range(len(b)))
def inv(a):return tr([solve(a,[F(i==j)for i in range(len(a))])for j in range(len(a))])
def pivots(a):
 b=[list(map(F,row))for row in a];k=0;out=[]
 for j in range(len(b[0])):
  p=next((i for i in range(k,len(b))if b[i][j]),None)
  if p is None:continue
  b[k],b[p]=b[p],b[k];z=b[k][j];b[k]=[v/z for v in b[k]]
  for i in range(k+1,len(b)):
   z=b[i][j];b[i]=[v-z*w for v,w in zip(b[i],b[k])]
  out.append(j);k+=1
  if k==len(b):break
 return out
def serial(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {k:serial(v)for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [serial(v)for v in x]
 return x
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
k=-F(3,4);s=F(45,127)
assert -1<k<s<1 and s==(29*k*k+78*k+45)/(15*k*k+42*k+31)
V=[(-F(1),F(0),z*(1-s))for z in(-1,1)]
V += [(F(0),F(y),F(z))for y,z in product((-1,1),repeat=2)]
V += [(F(1),y*(1+k),z*(1+k))for y,z in product((-1,1),repeat=2)]
NORM=[(-F(1),F(y),F(0))for y in(-1,1)]+[(-k,F(y),F(0))for y in(-1,1)]
NORM += [(-s,F(0),F(z))for z in(-1,1)]+[(-k,F(0),F(z))for z in(-1,1)]+[(F(1),F(0),F(0))]
FC=[[3,1,0,2],[1,5,4,0],[2,6,7,3],[8,4,5,9],[0,4,2],[5,1,3],[2,4,8,6],[3,7,9,5],[6,8,9,7]]
EDGES=[[0,1],[0,2],[0,4],[1,3],[1,5],[2,3],[2,4],[2,6],[3,5],[3,7],[4,5],[4,8],[5,9],[6,7],[6,8],[7,9],[8,9]]
found=set()
for ids in combinations(range(9),3):
 n=[NORM[i]for i in ids]
 if det(n):
  v=solve(n,[F(1)]*3)
  if all(dot(a,v)<=1 for a in NORM):found.add(v)
assert found==set(V)
area=[];g=[];rawT=[];ef={}
for i,(cyc,n)in enumerate(zip(FC,NORM)):
 slack=[1-dot(n,v)for v in V]
 assert all(x>=0 for x in slack) and {j for j,x in enumerate(slack)if x==0}==set(cyc)
 for j in range(len(cyc)):
  a,b,c=[V[cyc[(j+d)%len(cyc)]]for d in range(3)]
  assert dot(n,cross(sub(b,a),sub(c,b)))>0
 for a,b in zip(cyc,cyc[1:]+cyc[:1]):ef.setdefault(tuple(sorted((a,b))),[]).append(i)
 triangles=[[V[a]for a in(cyc[0],cyc[j],cyc[j+1])]for j in range(1,len(cyc)-1)]
 w=[dot(n,cross(sub(v[1],v[0]),sub(v[2],v[0])))/dot(n,n)for v in triangles]
 assert min(w)>0
 total=sum(w);area.append(total/2)
 g.append(tuple(sum(z*sum(v[a]for v in tri)/3 for z,tri in zip(w,triangles))/total for a in range(3)))
 rawT.append([[sum(z*(sum(v[a]for v in tri)*sum(v[b]for v in tri)+sum(v[a]*v[b]for v in tri))/12 for z,tri in zip(w,triangles))/total for b in range(3)]for a in range(3)])
assert sorted(ef)==list(map(tuple,EDGES)) and all(len(v)==2 for v in ef.values())
assert len(V)-len(EDGES)+len(FC)==2 and len(pivots(NORM))==3
# Positive spanning plus an interior point certifies boundedness.
assert all(sum(a*n[j]for a,n in zip(area,NORM))==0 for j in range(3))
volume=sum(area)/3
COM=tuple(sum(a*c[j]for a,c in zip(area,g))/(4*volume)for j in range(3))
Sigma=[[sum(a*T[i][j]for a,T in zip(area,rawT))/(5*volume)-COM[i]*COM[j]for j in range(3)]for i in range(3)]
assert volume==F(1785,508) and COM==(F(1,252),0,0)
# Independent one-dimensional integration of the rectangular sections.
def polymul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out
def integral(a,l,r):return sum(z*(r**(i+1)-l**(i+1))/F(i+1)for i,z in enumerate(a))
sections=[(-F(1),F(0),[F(1),F(1)],[F(1),s]),(F(0),F(1),[F(1),k],[F(1),k])]
vol2=F(0);first2=F(0);second2=[F(0)]*3
for l,r,f,g0 in sections:
 fg=polymul(f,g0);vol2+=4*integral(fg,l,r);first2+=4*integral([F(0)]+fg,l,r)
 second2[0]+=4*integral([F(0),F(0)]+fg,l,r)
 second2[1]+=F(4,3)*integral(polymul(polymul(fg,f),f),l,r)
 second2[2]+=F(4,3)*integral(polymul(polymul(fg,g0),g0),l,r)
assert vol2==volume and first2/vol2==COM[0]
assert all(second2[i]/vol2-COM[i]**2==Sigma[i][i]for i in range(3))
assert Sigma==[[F(4191847,26989200),0,0],[0,F(11581,61200),0],[0,0,F(180156947,767740400)]]
# Independent oriented tetrahedron volume/first moment.
vv=F(0);mom=[F(0)]*3
for cyc in FC:
 for j in range(1,len(cyc)-1):
  a,b,c=[V[v]for v in(cyc[0],cyc[j],cyc[j+1])];d=dot(a,cross(b,c))/6;vv+=d
  for u in range(3):mom[u]+=d*(a[u]+b[u]+c[u])/4
assert vv==volume and tuple(x/vv for x in mom)==COM
hh=[1-dot(n,COM)for n in NORM];assert min(hh)>0
Q=[tuple(a/h for a in n)for n,h in zip(NORM,hh)]
C=[sub(c,COM)for c in g];X=[sub(v,COM)for v in V]
T=[[[R[a][b]-c[a]*COM[b]-c[b]*COM[a]+COM[a]*COM[b]for b in range(3)]for a in range(3)]for c,R in zip(g,rawT)]
omega=[a*h/(3*volume)for a,h in zip(area,hh)]
Phi=tr([list(q)+[q[a]*c[b]for a in range(3)for b in range(3)]for q,c in zip(Q,C)])
Psi=Phi+tr(C)
nu=[-1163294,-1163294,884400,884400,2019087,2019087,-2532600,-2532600,1584814]
assert sum(nu)==0 and all(dot(row,nu)==0 for row in Psi)
assert len(pivots(Phi))==len(pivots(Psi))==8
rows=pivots(tr(Psi));cols=pivots(Psi);minor=det([[Psi[i][j]for j in cols]for i in rows])
assert rows==[0,1,2,3,4,5,7,11] and cols==list(range(8))
assert minor==F(161981404497794379669917663232,32547126255098083369971484375)
lever=[[sum(n*A[a][b]for n,A in zip(nu,T))for b in range(3)]for a in range(3)]
assert lever==[[F(2389931,3),0,0],[0,-F(882087,8),0],[0,0,F(35446202897,129032)]]
Psi2=Psi+[[a[1][1]for a in T]];rows2=pivots(tr(Psi2));minor2=det([Psi2[i]for i in rows2])
assert len(pivots(Psi2))==9 and rows2==rows+[15]
assert minor2==-F(31115350860027428349281067466752,89862615590325808184491268359375)
lo=-min(w/n for w,n in zip(omega,nu)if n>0);hi=min(w/-n for w,n in zip(omega,nu)if n<0)
assert lo==-F(127,8520490440) and hi==F(127,2720511360)
tau=F(1,10**8);fake=[w+tau*n for w,n in zip(omega,nu)]
assert lo<tau<hi and min(fake)>0
slacks=[[1-dot(q,c)for c in C]for q in Q]
lambdas=[]
for weights in(omega,fake):
 assert sum(weights)==1 and all(dot(weights,[q[j]for q in Q])==0 for j in range(3))
 assert all(dot(weights,[c[j]for c in C])==0 for j in range(3))
 assert all(dot(weights,[q[a]*c[b]for q,c in zip(Q,C)])==F(a==b,3)for a in range(3)for b in range(3))
 L=[[3*weights[j]*slacks[i][j]for j in range(9)]for i in range(9)];LL=mm(L,L)
 assert all(sum(r)==3 for r in L)
 assert mm(L,Q)==[[-x for x in q]for q in Q]
 assert all(LL[i][j]+L[i][j]==12*weights[j]for i in range(9)for j in range(9))
 assert len(pivots(L))==4
 assert all(L[i][j]==0 if i==j else 0<L[i][j]<F(10,9)for i in range(9)for j in range(9))
 lambdas.append(L)
assert all(sum(w*A[a][b]for w,A in zip(omega,T))==5*Sigma[a][b]/3 for a in range(3)for b in range(3))
fake_error=[[3*tau*lever[a][b]/5 for b in range(3)]for a in range(3)]
# One reciprocal metric pair and its rational Euclidean image.
A=[list(map(F,row))for row in[(10,1,1),(0,3,1),(0,1,1)]]
M=mm(tr(A),A);N=inv(M);minors=[det([r[:j]for r in M[:j]])for j in(1,2,3)]
assert det(A)==20 and minors==[100,1000,400]
GX=mm(mm(X,M),tr(X));GQ=mm(mm(Q,N),tr(Q))
PD=[[GX[i][j]-GX[i][i]for j in range(10)]for i in range(10)]
AD=[[GQ[i][j]-GQ[i][i]for j in range(9)]for i in range(9)]
assert all(PD[i][j]for i in range(10)for j in range(10)if i!=j)
assert all(AD[i][j]for i in range(9)for j in range(9)if i!=j)
U=[i for i in range(10)if all(PD[i][j]<0 for j in range(10)if i!=j)]
S=[i for i in range(9)if all(AD[i][j]<0 for j in range(9)if i!=j)]
H=[list(e)for e,(i,j)in sorted(ef.items())if PD[e[0]][e[1]]<0 and PD[e[1]][e[0]]<0 and AD[i][j]<0 and AD[j][i]<0]
assert S==[5,6] and U==[0,9] and H==[[1,5],[2,6]]
eps=F(1,2**24);norm1=lambda v:sum(abs(x)for x in v)
# lambda_min(M)>det(M)/sum of its principal 2-minors = 50/151.
assert 3*eps<F(50,151)
K=max(abs(v)for row in M for v in row)
for i in range(10):
 for j in range(10):
  if i!=j:assert abs(PD[i][j])>eps*norm1(X[i])*norm1(sub(X[j],X[i]))
for i in range(9):
 for j in range(9):
  if i!=j:assert 400*abs(AD[i][j])>(4*K*eps+2*eps*eps)*norm1(Q[i])*norm1(sub(Q[j],Q[i]))
Y=mm(X,tr(A));Qc=mm(Q,inv(A));Cc=mm(C,tr(A))
assert mm(Y,tr(Qc))==mm(X,tr(Q))
imagePsi=tr([list(q)+[q[a]*c[b]for a in range(3)for b in range(3)]+list(c)for q,c in zip(Qc,Cc)])
assert len(pivots(imagePsi))==8 and all(dot(r,nu)==0 for r in imagePsi)
den=[lcm(*(Psi[i][j].denominator for i in range(15)))for j in range(9)]
integer=[[int(Psi[i][j]*den[j])for j in range(9)]for i in range(15)]
out=dict(identity='E17_AUGMENTED_AFFINE_FLUX_RANK8_BELT_V1',parent=[PARENT,PINSHA],
parameters=dict(k=k,s=s),vertices=V,H_normals=NORM,H_rhs=[1]*9,facets=FC,edges=EDGES,
edge_facets=[ef[tuple(e)]for e in EDGES],area_over_normal=area,
area_squared=[a*a*dot(n,n)for a,n in zip(area,NORM)],volume=volume,centroid=COM,
actual_volume_covariance=Sigma,actual_poles=Q,actual_area_centroids=C,
actual_facet_second_moments=T,actual_cone_weights=omega,
Psi_integer=integer,Psi_column_denominators=den,rank_Phi=8,rank_Psi=8,null_vector=nu,
minor_rows=rows,minor_columns=cols,nonzero_minor=minor,second_moment_kernel_image=lever,
second_augmented_rank=9,second_minor_rows=rows2,second_nonzero_minor=minor2,
positive_weight_interval=[lo,hi],fake_parameter=tau,fake_weights=fake,
actual_Lambda=lambdas[0],fake_Lambda=lambdas[1],fake_covariance_error=fake_error,
M=M,N=N,metric_leading_minors=minors,primal_shadows=PD,pole_shadows=AD,
stable_facets=S,unstable_vertices=U,saddle_edges=H,metric_box_radius=eps,
minimum_absolute_primal_shadow=min(abs(PD[i][j])for i in range(10)for j in range(10)if i!=j),
minimum_absolute_pole_shadow=min(abs(AD[i][j])for i in range(9)for j in range(9)if i!=j),
Euclidean_image=dict(A=A,vertices=Y,poles=Qc,area_centroids=Cc,Psi=imagePsi,
facet_second_moments=[mm(mm(A,t),tr(A))for t in T],volume=20*volume,centroid=[0,0,0],
covariance=mm(mm(A,Sigma),tr(A))),
scope='Actual E17 rank8 augmented-flow counterexample. Class222, not110. Fake weights are not a second homogeneous realization.')
blob=(json.dumps(serial(out),sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
Path('augmented_belt.json').write_bytes(blob)
print('ACTUAL_E17_PHI_AND_CENTROID_AUGMENTATION_RANK8_PASS')
print('EXACT_ALL15_ROWS_NULL_AND_NONZERO_8_MINOR_PASS')
print('ACTUAL_FACET_YY_SECOND_MOMENT_RESTORES_RANK9_PASS')
print('POSITIVE_FAKE_MASSES_PASS_FULL_LAMBDA_ALGEBRA_BUT_FAIL_ACTUAL_COVARIANCE')
print('RATIONAL_EUCLIDEAN_CLASS_2_2_2_ALL162_SHADOWS_NONZERO_PASS')
print('CLOSED_SIX_ENTRY_METRIC_BOX_PASS',eps)
print('REPORT',*pin(blob));print('SOURCE',*pin(Path(__file__).read_bytes()))
if len(sys.argv)>1:
 txt=Path(sys.argv[1]).read_text();txt=txt[txt.index('## Parent '+PARENT):]
 txt=txt[txt.index('# ROOF_E17_ACTUAL_AFFINE_FLUX_RANK8_V1'):].rstrip()+'\n'
 b=json.dumps(dict(version=2,result_markdown=txt),ensure_ascii=False,separators=(',',':')).encode()
 assert pin(b)==[45852,PINSHA]
 print('LITERAL_PARENT_ENVELOPE_45852_BYTES_AUTHENTICATED')
```

### Полный исходник belt_stratum.py

```python
"""All-parameter E17 augmented affine flux rank and actual YY moment.
CPython 3.13.5; SymPy 1.14.0. Run python belt_stratum.py.
Parent minimum-0068:
80f95b882a35ae8de063c134068898e89bf129db83c0f48a9116d03d101c03ff.
Exact physical domain: -1<k<s<1. No numerical sample proves a stratum.
"""
from pathlib import Path
from math import comb
import hashlib,json
import sympy as S
assert __debug__ and S.__version__=='1.14.0'
k,s,x,v=S.symbols('k s x v',real=True)
R=15*k*k+42*k+31;B=29*k*k+78*k+45
H=k*k+3*k+3;G=k*k+6*k+17;F0=7*k*k+18*k+7
alpha=(2*s-3)/(3*(2-s));beta=(3+2*k)/(3*(2+k));gamma=-S.Rational(1,3)
E=S.Matrix([[-1,-k,-s,-k,1],[-alpha,-k*beta,-s*gamma,-k*beta,1],
 [1+alpha,1+k*beta,0,0,0],[0,0,1+s*gamma,1+k*beta,0]])
A0=s*(3*k*k+9*k+8)-k*(k+3)
A2=s*(3*k*k+9*k+10)-5*k*(k+3)-18
assert S.factor(E[:,[1,2,3,4]].det(method='domain-ge')-2*H*A0/(9*(k+2)**2))==0
assert S.factor(E[:,[0,1,3,4]].det(method='domain-ge')+2*H*A2/(9*(k+2)**2*(s-2)))==0
assert S.expand(A2-A0-2*(s-2*k*(k+3)-9))==0
aug=E.col_join(S.Matrix([[alpha,beta,gamma,beta,1]]))
assert S.factor(aug.det(method='domain-ge')+2*(s-1)*H*(R*s-B)/(27*(s-2)*(k+2)**2))==0
assert S.expand(R-15*(k+S.Rational(7,5))**2-S.Rational(8,5))==0
assert S.expand(B-k*R-(k+1)*(3*k+5)*(9-5*k))==0
assert S.expand(B-R-2*F0)==0
star=B/R
th=[S.Integer(1),-8*(k+2)/G,(k-1)*(k+3)*R/(2*(k+1)*(3*k+5)*G),
 -4*(k-1)*(k+2)*(k+3)/((k+1)*(3*k+5)*G),-(k-1)*F0/(2*(k+1)*G)]
assert all(S.factor(z.subs(s,star))==0 for z in aug*S.Matrix(th))
volume=4*(S.Rational(3,2)-s/6+k+k*k/3)
m=(4+s+8*k+3*k*k)/(18-2*s+12*k+4*k*k)
ms=(9*k*k+24*k+13)/(12*H)
assert S.factor(volume.subs(s,star)-4*H*(5*k*k+14*k+13)/R)==0
assert S.factor(m.subs(s,star)-ms)==0
n=[(-1,-1,0),(-1,1,0),(-k,-1,0),(-k,1,0),(-s,0,-1),(-s,0,1),(-k,0,-1),(-k,0,1),(1,0,0)]
g=[(alpha,-1-alpha,0),(alpha,1+alpha,0),(beta,-1-k*beta,0),(beta,1+k*beta,0),
 (gamma,0,-1-s*gamma),(gamma,0,1+s*gamma),(beta,0,-1-k*beta),(beta,0,1+k*beta),(1,0,0)]
kap=[th[j]/2 for j in range(4)for _ in range(2)]+[th[4]]
raw=S.Matrix.hstack(*[S.Matrix(list(a)+[a[i]*b[j]for i in range(3)for j in range(3)]+list(b))for a,b in zip(n,g)])
assert all(S.factor(z.subs(s,star))==0 for z in raw*S.Matrix(kap))
nu=[S.factor(((1-n[i][0]*m)*kap[i]).subs(s,star))for i in range(9)]
expected=[-1163294,-1163294,884400,884400,2019087,2019087,-2532600,-2532600,1584814]
assert [-2317392*z.subs(k,-S.Rational(3,4)) for z in nu]==expected
# Genuine uniform-area integration, not four-vertex means or PSD blocks.
def integ(p,a,b):return S.integrate(p,(x,a,b))
rawyy=[integ((1+x)**2*(1+s*x),-1,0)/integ(1+s*x,-1,0),
 integ((1+k*x)**3,0,1)/integ(1+k*x,0,1),
 integ((1+x)**3,-1,0)/(3*integ(1+x,-1,0)),
 integ((1+k*x)**3,0,1)/(3*integ(1+k*x,0,1)),(1+k)**2/3]
yy=[(4-s)/(6*(2-s)),(k*k+2*k+2)/2,S.Rational(1,6),(k*k+2*k+2)/6,(1+k)**2/3]
assert all(S.factor(a-b)==0 for a,b in zip(rawyy,yy))
xxnorm=[-1,-k,-s,-k,1]
lever=S.factor(sum(th[i]*(1-xxnorm[i]*m)*yy[i]for i in range(5)).subs(s,star))
P=1494*k**8+15708*k**7+68621*k**6+161252*k**5+216907*k**4+159588*k**3+49779*k**2-3636*k-4113
Den=144*(k+1)*(3*k+5)*H*G
assert S.factor(lever+P/Den)==0
# All coefficients in the Bernstein basis on -1 <= k <= -3/7 are positive.
bc=list(map(S.Rational,['224','1328/7','48448/343','203312/2401','2862304/84035','270192/16807','8712576/117649','215811216/823543','3474015840/5764801']))
assert min(bc)>16
assert S.expand(-P.subs(k,-1+S.Rational(4,7)*v)-sum(bc[j]*comb(8,j)*v**j*(1-v)**(8-j)for j in range(9)))==0
assert S.Rational(16,144*5*3*17)==S.Rational(1,2295)
report=dict(identity='E17_BELT_COMPLETE_AUGMENTED_RANK_STRATA_V1',domain='-1<k<s<1',
 rank_Phi=8,rank_Psi_on_stratum=8,rank_Psi_elsewhere=9,
 stratum='s=(29*k^2+78*k+45)/(15*k^2+42*k+31); -1<k<(-9+4*sqrt(2))/7',
 even_augmented_determinant=str(S.factor(aug.det(method='domain-ge'))),
 theta=[str(S.factor(z))for z in th],stratum_volume=str(S.factor(volume.subs(s,star))),
 stratum_centroid_x=str(ms),actual_YY_kernel_image=str(lever),
 YY_numerator_descending=[int(z)for z in S.Poly(P,k).all_coeffs()],
 negative_numerator_Bernstein_interval=['-1','-3/7'],
 negative_numerator_Bernstein_coefficients=[str(z)for z in bc],
 positive_YY_kernel_lower_bound='1/2295',second_augmented_rank_on_entire_domain=9)
blob=(json.dumps(report,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
Path('belt_stratum.json').write_bytes(blob)
print('FULL_TWO_PARAMETER_E17_GEOMETRIC_RANK_STRATA_IDENTITIES_PASS')
print('BARE_PHI_RANK8_EVERYWHERE_AUGMENTED_RANK8_EXACTLY_ON_STATED_CURVE')
print('ACTUAL_YY_MOMENT_RESTORES_RANK9_ON_ENTIRE_STRATUM_PASS')
print('POSITIVE_NINE_BERNSTEIN_COEFFICIENTS_AND_UNIFORM_1_OVER_2295_PASS')
print('REPORT',len(blob),hashlib.sha256(blob).hexdigest())
b=Path(__file__).read_bytes();print('SOURCE',len(b),hashlib.sha256(b).hexdigest())
```
