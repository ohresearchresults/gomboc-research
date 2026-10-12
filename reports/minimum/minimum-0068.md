# minimum-0068

AI research report · 2026-09-16 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# ROOF_E17_ACTUAL_AFFINE_FLUX_RANK8_V1

## Итог

**Утверждение `rank Φ=9` для всякого настоящего тела `(V,E,F)=(10,17,9)` ложно.** Построен точный рациональный контрпример с `rank Φ=8`, настоящими центрами площадей, собственным объёмным центром, всеми девятью максимальными гранями и семнадцатью истинными рёбрами. Это не предел вырождающихся тел. Его рациональный аффинный образ имеет строгий класс **(S,U,H)=(2,2,2)**; все 162 тени между различными вершинами или полюсами ненулевые. Сохранён также отдельный точный метрический контроль класса `(3,4,5)`.

Получена **полная классификация ранга на непрерывном семействе симметричных восьмиугольных roof-тел**, без ограничений на обусловленность метрики. Исключительный слой — явная гладкая гиперповерхность; на ней ранг всегда ровно 8, вне неё ровно 9. При этом **добавление настоящего конусного уравнения объёмного центра восстанавливает единственность масс на всей семье**. Независимо, её восстанавливают настоящие вторые моменты граней с общей фактической объёмной ковариацией. Обе невырожденности доказаны на всём исключительном слое.

Новых полных механических root/type-исключений нет. Принятая граница `C≥34` и текущий реестр `632 типа / 52585 совместных корневых орбит` не изменяются. Здесь не используется старый неподтверждённый вычислительный фронт из прежней передачи. Текущий статус и отличие семейной полноранговости от универсального результата явно зафиксированы в синтезе.

## Источники и путь к результату

Полностью прочитан буквальный родитель `minimum-0061`, **SHA-256 `5bd7dc9ed75e5dcbd403d23bf0c22fdaaf06d0d60f54066507505173dc3ee910`**, включая три его полных исходника. Его компактная UTF-8 JSON-сериализация `{version:2,result_markdown:...}` с одним конечным LF в Markdown восстановлена как **49087 байт с тем же SHA**. Конфликтов с буквальным объектом нет. Его epsilon-геометрия и TREE253 не переименованы и не объявляются исключёнными. Родитель требует одну настоящую геометрию и различает необходимые моментные тождества и достаточность реализации.

Непосредственным геометрическим отправным контролем стала полностью прочитанная капсула `AFFINE_FLUX_EXACT_CONTROLS_ROOF_EDGE_CUT_OCTAHEDRON_V1`. Её исходник `affine_flux_rank_controls.py`, **6129 байт / `fde0629286fb1b117825a76d0212f87676e70451040d962b050d4a90488ad4e5`**, исполнен; воспроизведены исходные два rank9-контроля и rank7 неотсечённого октаэдра, JSON **3259 байт / `5dba75e5bb9080297697371af717684a6c151b7f1b68567e40d4671953ad99f0`**. Их идентичности сохранены. Новый roof — другая точка расширенного семейства, не исправление старого rank9-контроля.

Текущий входной журнал: `research-journal(20260916-130715).md`, **4699968 байт / `b397606b2487733993c846f87703d6720c1b238616538d3038444374fa567023`**. Для новых результатов не требуются отсутствующие material-файлы или epsilon-capsule. Первым вычислительным шагом было разложение настоящего аффинного потока по двум отражениям; оно выделило один исчезающий 2×2 определитель. Рациональная точка этого слоя затем проверена полным H/V-аудитом. Результат не выводится из отрицательного численного поиска.

## 1. Вся непрерывная область roof-семейства

Пусть `0<a<c`, `0<d<b`, `r>0`. Нижний восьмиугольник, в циклическом порядке, имеет вершины

`(-a,-b,0),(a,-b,0),(c,-d,0),(c,d,0),(a,b,0),(-a,b,0),(-c,d,0),(-c,-d,0)`;

верхние вершины — `(-r,0,1),(r,0,1)`. Их выпуклая оболочка обозначается `P(a,b,c,d,r)`. Высота 1 не ограничивает аффинные образы. Область **не** ограничивается `r<a` или малостью r.

Обозначим `D=bc-ad`, `L=D-r(b-d)`. Девять настоящих поддерживающих неравенств имеют нормали и правые части, в порядке граней полного verifier:

~~~text
n0=(0,0,-1),          h0=0
n1=(0,-1,b),          h1=b
n2=(-(b-d),-(c-a),L), h2=D
n3=((b-d),-(c-a),L),  h3=D
n4=(1,0,c-r),         h4=c
n5=((b-d),(c-a),L),   h5=D
n6=(0,1,b),           h6=b
n7=(-(b-d),(c-a),L),  h7=D
n8=(-1,0,c-r),        h8=c
~~~

Это всегда ровно `(10,17,9)`. Действительно, `0≤z≤1`, `|y|≤b(1-z)` и `|x|≤c(1-z)+rz` дают ограниченность. Сечение на высоте z равно сумме Минковского `(1-z)B+z[-r,r]e_x`, где B — указанный восьмиугольник. Перечисленные плоскости поддерживают соответственно восьмиугольник, две настоящие четырёхугольные грани и шесть треугольников. Все неинцидентности строги при данных открытых неравенствах на параметры. Никакая грань не заменяется триангуляционным куском.

Площадь основания и собственный объёмный центр вычисляются без предположений о массах вершин:

~~~text
A_B=2[b(a+c)+d(c-a)],
Vol(P)=(A_B+2br)/3,
o=(0,0,z0),  z0=(A_B+4br)/(4(A_B+2br)).
~~~

Это следует интегрированием настоящей площади сечения `A_B(1-z)^2+4br z(1-z)`.

Пусть `g_i` — центры площадей до переноса, `c_i=g_i-o`, `hhat_i=h_i-n_i·o>0`, `q_i=n_i/hhat_i`. Для треугольников g_i равны средним их трёх вершин; для двух четырёхугольников **настоящие** значения:

`g_1=(0,-b(2a+r)/(3(a+r)),(a+2r)/(3(a+r)))`,
`g_6=(0,+b(2a+r)/(3(a+r)),(a+2r)/(3(a+r)))`.

Остальные центры: `g_0=0`; на диагональных треугольниках `g=(±(a+c+r)/3,±(b+d)/3,1/3)` с соответствующими знаками; на двух x-торцах `g=(±(2c+r)/3,0,1/3)`.

### Теорема ранга

Для столбцов `Φ_i=(q_i,vec_row(q_i c_iᵀ))`:

~~~text
rank Φ = 8  ⇔  r=c-d(a+2c)/b>0;
rank Φ = 9  во всех остальных точках указанной области.
~~~

Иных понижений ранга внутри этой семьи нет. После нормировки `α=a/c`, `δ=d/b`, `ρ=r/c` исключительный слой задаётся

`0<α<1, 0<δ<1/(α+2), ρ=1-δ(α+2)`.

Это двумерный слой внутри трёхмерного пространства нормированных форм, не вырожденная граница `r=0`.

**Доказательство.** Ранг можно вычислять по столбцам `B_i=(n_i,vec_row(n_i g_iᵀ))`: переход к Φ — обратимое вычитание `n_i oᵀ` из нижнего блока и ненулевые положительные масштабы столбцов `1/hhat_i`. Отражения x и y разбивают пространство столбцов на четыре характера с размерностями `4,2,2,1`.

В чётно-чётном блоке основание выделяет строку n_z. Остальной 3×3 блок, с колонками «y-четырёхугольник, диагональный треугольник, x-треугольник», равен

~~~text
E=(1/3)*[[0,                     (b-d)(a+c+r), (2c+r)],
         [b(2a+r)/(a+r),         (c-a)(b+d),    0],
         [b(a+2r)/(a+r),         L,             c-r]].
det E=br(a-c)[a(b-d)+c(b+d)+br]/[9(a+r)] ≠ 0.
~~~

Нечётно-чётный блок имеет потенциальный ранг 2, определяемый строками `n_x,n_z g_x`:

~~~text
OX=[[b-d,             1],
    [L(a+c+r)/3,     (c-r)(2c+r)/3]],
det OX=(a-c)(ad-bc+br+2cd)/3.
~~~

Третья его строка `n_x g_z=n_x/3` избыточна. Первая строка ненулевая, поэтому на нулевом определителе ранг ровно 1. В чётно-нечётном блоке строки `n_y,n_y g_z` имеют определитель `r(a-c)/(3(a+r))≠0`; его ранг 2. Нечётно-нечётный блок имеет одну колонку с положительной компонентой `(b-d)(b+d)/3`, поэтому ранг 1. Сложение рангов даёт точное утверждение. Все факторизации дополнительно проверяются полным символическим исходником ниже.

Любой невырожденный аффинный образ сохраняет результат: настоящие центры площадей переходят в их аффинные образы, поскольку якобиан площади постоянен на каждой плоскости; после собственного центрирования `q→A⁻ᵀq`, `c→Ac`. Преобразование обоих блоков Φ обратимо. Полярный объёмный центр нигде не используется.

## 2. Буквальный рациональный rank8-контроль

Выбрано `(a,b,c,d,r)=(1,4,2,1,3/4)`. Это отличается от исходного roof-контроля `(1,2,2,1,1/2)`, у которого по доказанной формуле ранг 9.

Полные V/H, максимальные циклы F и все 17 E являются буквальными константами `V,NORM,RHS,FC,E` автономного исходника ниже. Все номера здесь **локальные**; канонический C34 ID этому объекту не присваивался. Его степени вершин: восемь значений 3 и два значения 5; это не epsilon-контроль с четырьмя вершинами степени 4.

Для нового тела:

~~~text
Vol=32/3,
o=(0,0,19/64),
Σ=diag(443/640,389/160,1011/20480),
ω=(247/1024,315/2048,1431/16384,1431/16384,417/8192,
   1431/16384,315/2048,1431/16384,417/8192).
~~~

Здесь `ω_i=Area(F_i)/(3 Vol ||q_i||)` — настоящие нормированные конусные объёмы. Настоящие площади: `26` на F0, `7√17/4` на F1,F6, `√521/8` на F2,F3,F5,F7 и `√41/4` на F4,F8.

Центры площадей после **того же** переноса:

~~~text
c0=(0,0,-19/64)
c1=(0,-44/21,241/1344)
c2=(-5/4,-5/3,7/192)
c3=(5/4,-5/3,7/192)
c4=(19/12,0,7/192)
c5=(5/4,5/3,7/192)
c6=(0,44/21,241/1344)
c7=(-5/4,5/3,7/192)
c8=(-19/12,0,7/192)
~~~

Например, сырой центр F1 — `(0,-44/21,10/21)`, а среднее её четырёх вершин — `(0,-2,1/2)`. В доказательстве и verifier используется первое.

### Полная Φ и точный сертификат

Порядок строк: `q_x,q_y,q_z,q_xc_x,q_xc_y,q_xc_z,q_yc_x,q_yc_y,q_yc_z,q_zc_x,q_zc_y,q_zc_z`. Введём положительную диагональ

`Dcol=diag(19,3780,4293,4293,1251,4293,3780,4293,1251)`.

**Полная матрица — `Φ=Z Dcol⁻¹`, где буквально**

~~~text
Z=[
[  0,     0,-2304, 2304,  768, 2304,    0,-2304, -768],
[  0, -1344, -768, -768,    0,  768, 1344,  768,    0],
[-64,  5376, 3648, 3648,  960, 3648, 5376, 3648,  960],
[  0,     0, 2880, 2880, 1216, 2880,    0, 2880, 1216],
[  0,     0, 3840,-3840,    0, 3840,    0,-3840,    0],
[  0,     0,  -84,   84,   28,   84,    0,  -84,  -28],
[  0,     0,  960, -960,    0,  960,    0, -960,    0],
[  0,  2816, 1280, 1280,    0, 1280, 2816, 1280,    0],
[  0,  -241,  -28,  -28,    0,   28,  241,   28,    0],
[  0,     0,-4560, 4560, 1520, 4560,    0,-4560,-1520],
[  0,-11264,-6080,-6080,    0, 6080,11264, 6080,    0],
[ 19,   964,  133,  133,   35,  133,  964,  133,   35]]
ν=(0,0,-159,159,-278,159,0,-159,278).
~~~

Имеем `Φν=0`. Минор по строкам `(0,1,2,3,4,7,8,11)` и колонкам `(0,1,2,3,4,5,6,7)` равен

`36893488147419103232 / 659324621620108719135 > 0`.

Следовательно, ранг ровно 8, а ядро ровно `span{ν}`. Это точный верхний и нижний сертификат ранга, не оценка малой сингулярной величины.

## 3. Геометрическое ядро и точная граница массовой жёсткости

На всём исключительном слое сырое ядро B порождается

`κ=(0,0,-1,1,-2(b-d),1,0,-1,2(b-d))`.

Соответствующее ядро Φ — `ν_i=hhat_i κ_i`. Оно перераспределяет веса между левыми и правыми треугольными скатами; основание и оба четырёхугольника не меняют веса. Все настоящие площади остаются положительными. Более точно, для сырого нормирования `ν_i=hhat_iκ_i` все положительные решения первых потоков образуют ровно интервал

`ω+tν,  |t|<d/[6 Vol(P)(b-d)]`.

Действительно, настоящие `Area(F_i)/||n_i||` равны `A_B,a+r,1/2,1/2,d,1/2,a+r,1/2,d`; масштабы hhat_i сокращаются в проверке положительности. На rank8-слое `d<b/2`, поэтому раньше диагональных скатов обнуляется один из двух x-треугольников. Это точная граница положительности ложных масс на всём слое, а не только у контрольной точки.

Дополнительная геометрическая зависимость имеет вид `q_iz c_ix=k q_ix` на всех девяти гранях, где `k=(c-r)(2c+r)/3>0`. Поэтому аффинное поле `v(x,y,z)=(-k,0,x)` имеет нулевой **интегральный** нормальный поток через каждую настоящую грань: `∫_Fi n_i·v=Area(F_i)n_i·v(c_i)=0`. Это не утверждение поточечной касательности или неподвижности грани. Оно описывает дополнительную зависимость в первом аффинном потоке.

### Восстановление по настоящему объёмному центру — вся семья

Настоящие веса удовлетворяют

`Σω_i q_i=0`, `Σω_i q_i c_iᵀ=I/3`, `Σω_i=1`, **`Σω_i c_i=0`**.

Последнее — интегрирование настоящих пирамид с вершиной в собственном объёмном центре. Нормировка уже следует из следа второго уравнения, поскольку `q_i·c_i=1`.

На исключительном слое точное вычисление даёт

`Σν_i c_i=(4/3)r(b-d)(a-c)e_x ≠ 0`

для нормирования `ν_i=hhat_iκ_i`. Члены с z0 сокращаются ровно по `det OX=0`. Поэтому

**`rank [Φ; c_0 … c_8]=9` на всей непрерывной roof-семье и всех её невырожденных аффинных образах.**

Любые веса, удовлетворяющие первым потокам, отличаются от настоящих только на tν. Настоящее уравнение объёмного центра вынуждает t=0. Это единственность при заданной фактической геометрии, не существование иной геометрии и не исключение 110.

### Независимое восстановление по общей настоящей ковариации — тоже вся семья

Положим `T_i=E_Fi[(x-o)(x-o)ᵀ]`, без свободных PSD-блоков. Настоящее конусное тождество — `Σ=(3/5)Σω_i T_i`. На исключительном слое

~~~text
Σν_i (T_i)_xz = r(c-a)[-b+2d+z0(4b-5d)]/3
              = br(c-a) N(α,δ)/(12 D(α,δ)) > 0,
D(α,δ)=α+2-(2α+1)δ,
N(α,δ)=4-(7+α)δ+(7-α)δ².
~~~

Здесь `0<δ<1/(α+2)<1/2`; поэтому D>0, а полное положительное удостоверение:

`N=3/2+2(1/2-δ)+6(1/2-δ)²+(1-α)δ(1+δ)>3/2`.

Для вывода достаточно настоящего треугольного момента `E(xz)=g_x/4+x_roof/12` на шести гранях с ненулевым κ. После переноса вычитается `z0 g_x`; остальные три грани имеют нулевой коэффициент ядра. Следовательно, даже один действительный xz-компонент общей ковариации устраняет ядро. В аффинном образе используется соответствующая билинейная форма, либо весь блок настоящих вторых моментов. Получена ещё одна полная семейная теорема массовой жёсткости, независимая от механических знаков.

### Точная положительная линия ложных масс у рационального контроля

Для целого ν из раздела 2:

~~~text
Σν_i c_i=(-256/3,0,0),
Σν_i T_i=[[0,0,9],[0,0,0],[9,0,0]].
~~~

Все решения только первого аффинного потока с положительными весами — **ровно**

`ω(t)=ω+tν,  -3/16384<t<3/16384`.

При `t=1/16384` все веса ещё положительны и все 12 уравнений Φ неизменны, но формальный центр конусного разложения равен `(-1/256,0,0)`, а ошибка xz-компоненты объёмного второго момента — `27/81920`. Настоящее тело при этом, конечно, не приобрело другие массы: неправильны предлагаемые веса.

Это также показывает точную связь с уже используемой общей Λ. При `Λ(w)[:,i]=3w_i(1-Qc_i)`:

`Λ(ω+tν)1-3·1=256t Qe_x`.

Следовательно, этот ложный массовый параметр **не проходит** полную родительскую систему с `Λ1=3·1`. Нельзя выдавать контрпример к `rank Φ=9` за контрпример ко всем совместным настоящим моментным условиям.

## 4. Ранг 8 вне механических нулевых стенок

Возьмём рациональную матрицу

~~~text
A=[[3,1,0],[0,4,1],[1,0,3]],  det A=37,
M=AᵀA=[[10,3,3],[3,17,4],[3,4,10]],
N=M⁻¹=(1/1369)*[[154,-18,-39],[-18,91,-31],[-39,-31,161]].
~~~

Матрица M имеет положительные ведущие миноры `10,161,1369`. **Настоящее рациональное евклидово тело** `P*=A(P-o)` задаётся вершинами `A(V_j-o)` и неравенствами `(A⁻ᵀq_i)·x≤1`. Его центры площадей — `Ac_i`, объём `1184/3`, собственный центр ровно 0, ковариация `AΣAᵀ`. Полные данные, включая его собственную Φ, восстанавливаются verifier. Использование M,N в исходной аффинной карте в точности равно евклидовой механике P*; независимая полярная метрика не вводится.

Полный аудит даёт:

~~~text
S=[F0,F1], U=[v0,v4], H=[(v2,v3),(v6,v7)], класс (2,2,2).
min_{i≠j}|D_ij|=57/64,
min_{a≠b}|A_ab|=32768/311487201.
~~~

Проверены все 90 вершинных и 72 полюсных тени, не только 68 направлений настоящих рёбер. Сохраняется полный строгий класс на **замкнутом шестимерном боксе** симметричных M′ с `|M′_ij-M_ij|≤2^-20`. Для доказательства verifier проверяет для каждой пары точные оценки ошибок `ε||x_i||_1||x_j-x_i||_1` и `(68ε+2ε²)||q_i||_1||q_j-q_i||_1` для линейного и adjugate-квадратичного числителя соответственно. Гершгорин даёт положительность M′. Все проверки рациональные.

Таким образом, недостаток ранга не вызван ни геометрическим слиянием граней, ни равенством механического свидетеля. По непрерывности существует также относительно открытая область класса222 на найденном геометрическом rank8-слое. Утверждения о110 из этого не следует.

Сохранён и отдельный метрический контроль `M2=[[10,1,2],[1,15,3],[2,3,12]]`, `det M2=1650`. Его фактический обратный N2 полностью записан в JSON и детерминированно вычисляется в исходнике. На той же координатной геометрии он даёт `S=[0,1,6]`, `U=[0,1,4,5]`, `H=[(0,1),(2,3),(4,5),(6,7),(8,9)]`, класс345, также без нулей во всех162тенях. Этот невыигрывающий контроль не потерян и не смешивается с парой M,N основного контроля.

## 5. Граница результата и продолжение

Полный вопрос из назначения разрешён отрицательно: универсальный ранг9 опровергнут **на том же f-vector** настоящим точным телом. Полный исключительный слой описан только внутри указанной roof-семьи и её аффинных образов; классификация всех rank-deficient реализаций всех632типов не заявляется. Не доказаны отсутствие более глубокого ранга на других типах, невозможность110 на всей найденной семье или глобальная полноранговость дополненной матрицы `[Φ;c]` на E17.

Наиболее полезное продолжение — исследовать **полный ранг именно `[Φ;c]` на действительном E17**, а не повторять уже ложную гипотезу для Φ. Этот новый пример не препятствует массовой жёсткости полной системы: настоящее конусное центрирование уже устраняет его единственный параметр. При поиске более серьёзного исключительного слоя следует требовать одновременно `Φν=0`, `Σν_i c_i=0`, а при использовании общей Σ ещё `Σν_i T_i=0`, с настоящими центрами и моментами всех граней. Альтернативно, в задачах на эту roof-геометрию свободные массы можно исключать сразу по доказанной дополненной ранговой теореме.

## 6. Полная recovery и фактическая проверка

Оба исходника ниже включены полностью, без внешних геометрических входов и без сокращённых архивов. Первый использует только стандартную библиотеку; второй — SymPy1.14.0 для буквальных полиномиальных тождеств. Наблюдаемая среда: **CPython3.13.5, SymPy1.14.0**. У всех запусков assert включены. Нет случайности, допусков, оптимизации или неуказанных численных параметров.

Сохранить блоки как `roof_rank8.py` и `roof_stratum_symbolic.py`, UTF-8/LF с конечным LF. Команды:

~~~sh
python -S roof_rank8.py > roof_rank8.log
python roof_stratum_symbolic.py > roof_stratum_symbolic.log
# Не требуется для нового тела; дополнительная аутентификация родителя:
python -S roof_rank8.py 'research-journal(20260916-130715).md'
~~~

При отсутствии SymPy установить ровно `sympy==1.14.0`; основной точный геометрический сертификат от этой зависимости свободен. Повторный запуск в отдельном чистом каталоге дал побайтно те же JSON и оба журнала. Дополнительно оба исходника извлечены из полного подготовленного `result_markdown` в новый каталог и исполнены: восстановленные источники, журналы и JSON совпали побайтно.

| Объект | Байты | SHA-256 |
|---|---:|---|
|roof_rank8.py|12576|299aaa364c9a67ddec95f8eb728bbafc9e83d132c823657b5f30f12db2e9b0f7|
|roof_rank8.json|12984|be81a321d272e8a8267d8701f3aaa799ef6cc43d6d8a3bbe0d3e662a8f766621|
|roof_rank8.log|475|e766c33f59bbf4b3fc3fda8bf6239f2ae91b2515278ed90fe07eb69581ebb016|
|roof_stratum_symbolic.py|2807|c90efe3ba2646bafa1c6eac19873617b88ada71e9da7717fd3a2fc77b6ab5ef5|
|roof_stratum_symbolic.log|300|d66e84c5b21552ca3f8712593c6ac3e1ac20d491c9d142b0bf7dbaa99b406e3f|

Ожидаемые и наблюдённые маркеры:

~~~text
ACTUAL_H_V_F_E_10_17_9_RANK8_NULL_PASS
ACTUAL_CENTROID_AND_SECOND_MOMENT_EACH_RESTORE_RANK9_PASS
POSITIVE_AFFINE_FLUX_WEIGHT_LINE 3/16384 FALSE_CENTROID -1/256 0 0
RATIONAL_EUCLIDEAN_E17_RANK8_CLASS_2_2_2_ALL162_NONZERO_PASS
CLOSED_METRIC_BOX_CLASS_2_2_2_PASS 1/1048576

[Encoded source block omitted; the code in this passage is incomplete.]


Дополнительные копии: геометрический исходник (`roof_rank8.py`), символический исходник (`roof_stratum_symbolic.py`), полный точный JSON (`roof_rank8.json`). Они не заменяют полные блоки ниже.

### Полный исходник roof_rank8.py

```python
"""ROOF_E17_ACTUAL_AFFINE_FLUX_RANK8_V1; CPython 3.13.5, stdlib only.
Run: python -S roof_rank8.py
Optional provenance: python -S roof_rank8.py JOURNAL.md
Parent minimum-0061
SHA256 5bd7dc9ed75e5dcbd403d23bf0c22fdaaf06d0d60f54066507505173dc3ee910
No solver, tolerances, random choices, or external geometric inputs.
"""
from fractions import Fraction as F
from itertools import combinations
from math import lcm
from pathlib import Path
import hashlib,json,sys
assert __debug__
PARENT='minimum-0061'
PINSHA='5bd7dc9ed75e5dcbd403d23bf0c22fdaaf06d0d60f54066507505173dc3ee910'
CONTROL=['AFFINE_FLUX_EXACT_CONTROLS_ROOF_EDGE_CUT_OCTAHEDRON_V1',6129,
'fde0629286fb1b117825a76d0212f87676e70451040d962b050d4a90488ad4e5']
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def transpose(a):return list(map(list,zip(*a)))
def outer(a,b):return [[x*y for y in b]for x in a]
def mm(a,b):return [[dot(r,c)for c in zip(*b)]for r in a]
def det(a):
 b=[list(map(F,r))for r in a];v=F(1)
 for k in range(len(b)):
  j=next((j for j in range(k,len(b))if b[j][k]),None)
  if j is None:return F(0)
  if j!=k:b[k],b[j]=b[j],b[k];v=-v
  p=b[k][k];v*=p
  for i in range(k+1,len(b)):
   z=b[i][k]/p
   for j in range(k+1,len(b)):b[i][j]-=z*b[k][j]
 return v
def solve(a,b):
 d=det(a);assert d
 return tuple(det([[b[i]if j==k else a[i][j]for j in range(len(b))]for i in range(len(b))])/d for k in range(len(b)))
def rref(a):
 a=[list(map(F,r))for r in a];k=0;piv=[]
 for j in range(len(a[0])):
  p=next((i for i in range(k,len(a))if a[i][j]),None)
  if p is None:continue
  a[k],a[p]=a[p],a[k];v=a[k][j];a[k]=[x/v for x in a[k]]
  for i in range(len(a)):
   if i!=k:
    v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[k])]
  piv.append(j);k+=1
  if k==len(a):break
 return a,piv
def serial(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return {k:serial(x)for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [serial(x)for x in v]
 return v
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
V=[tuple(map(F,p))for p in [(-1,-4,0),(1,-4,0),(2,-1,0),(2,1,0),(1,4,0),(-1,4,0),(-2,1,0),(-2,-1,0),(-F(3,4),0,1),(F(3,4),0,1)]]
NORM=[tuple(map(F,n))for n in [(0,0,-1),(0,-1,4),(-3,-1,F(19,4)),(3,-1,F(19,4)),(1,0,F(5,4)),(3,1,F(19,4)),(0,1,4),(-3,1,F(19,4)),(-1,0,F(5,4))]]
RHS=list(map(F,[0,4,7,7,2,7,4,7,2]))
FC=[[6,5,4,3,2,1,0,7],[0,1,9,8],[8,7,0],[1,2,9],[2,3,9],[9,3,4],[8,9,4,5],[5,6,8],[8,6,7]]
E=[[0,1],[0,7],[0,8],[1,2],[1,9],[2,3],[2,9],[3,4],[3,9],[4,5],[4,9],[5,6],[5,8],[6,7],[6,8],[7,8],[8,9]]
# Exhaust all H-vertices, not merely selected incidences.
found=set();nonsingular=0
for ids in combinations(range(9),3):
 a=[NORM[i]for i in ids]
 if not det(a):continue
 nonsingular+=1;v=solve(a,[RHS[i]for i in ids])
 if all(dot(n,v)<=h for n,h in zip(NORM,RHS)):found.add(v)
assert found==set(V)
area_factor=[];centers=[];raw_second=[];edge_faces={};minimum_slack=None
for i,(cyc,n,h)in enumerate(zip(FC,NORM,RHS)):
 ss=[h-dot(n,v)for v in V]
 assert {j for j,s in enumerate(ss)if s==0}==set(cyc)
 assert all(s>=0 for s in ss)
 z=min(s for s in ss if s>0);minimum_slack=z if minimum_slack is None else min(z,minimum_slack)
 for j in range(len(cyc)):
  a,b,c=[V[cyc[(j+t)%len(cyc)]]for t in range(3)]
  assert dot(n,cross(sub(b,a),sub(c,b)))>0
 for u,v in zip(cyc,cyc[1:]+cyc[:1]):edge_faces.setdefault(tuple(sorted((u,v))),[]).append(i)
 weights=[];triangles=[]
 for j in range(1,len(cyc)-1):
  pts=[V[k]for k in (cyc[0],cyc[j],cyc[j+1])]
  w=dot(n,cross(sub(pts[1],pts[0]),sub(pts[2],pts[0])))/dot(n,n)
  assert w>0;weights.append(w);triangles.append(pts)
 total=sum(weights);area_factor.append(total/2)
 centers.append(tuple(sum(w*sum(v[k]for v in pts)/3 for w,pts in zip(weights,triangles))/total for k in range(3)))
 raw_second.append([[sum(w*(sum(v[k]for v in pts)*sum(v[l]for v in pts)+sum(v[k]*v[l]for v in pts))/12 for w,pts in zip(weights,triangles))/total for l in range(3)]for k in range(3)])
assert sorted(edge_faces)==list(map(tuple,E)) and all(len(fs)==2 for fs in edge_faces.values())
assert len(V)-len(E)+len(FC)==2 and len(rref(NORM)[1])==3
# Positive spanning proves boundedness of the full H-intersection.
assert all(a>0 for a in area_factor)
assert all(sum(a*n[k]for a,n in zip(area_factor,NORM))==0 for k in range(3))
volume=sum(a*h for a,h in zip(area_factor,RHS))/3
COM=tuple(sum(a*h*c[k]for a,h,c in zip(area_factor,RHS,centers))/(4*volume)for k in range(3))
Sigma=[[sum(a*h*T[k][l]for a,h,T in zip(area_factor,RHS,raw_second))/(5*volume)-COM[k]*COM[l]for l in range(3)]for k in range(3)]
assert volume==F(32,3) and COM==(0,0,F(19,64))
# Independent oriented tetrahedron volume and first-moment evaluation.
tv=F(0);tm=[F(0)]*3
for cyc in FC:
 for j in range(1,len(cyc)-1):
  a,b,c=[V[k]for k in (cyc[0],cyc[j],cyc[j+1])];w=dot(a,cross(b,c))/6;tv+=w
  for k in range(3):tm[k]+=w*(a[k]+b[k]+c[k])/4
assert tv==volume and tuple(x/tv for x in tm)==COM
support=[h-dot(n,COM)for n,h in zip(NORM,RHS)];assert min(support)>0
Q=[tuple(x/h for x in n)for n,h in zip(NORM,support)]
C=[sub(c,COM)for c in centers];X=[sub(v,COM)for v in V]
T=[[[R[k][l]-c[k]*COM[l]-COM[k]*c[l]+COM[k]*COM[l]for l in range(3)]for k in range(3)]for c,R in zip(centers,raw_second)]
omega=[a*h/(3*volume)for a,h in zip(area_factor,support)]
assert omega==list(map(F,['247/1024','315/2048','1431/16384','1431/16384','417/8192','1431/16384','315/2048','1431/16384','417/8192']))
assert centers[1]!=(tuple(sum(V[j][k]for j in FC[1])/4 for k in range(3)))
assert sum(omega)==1 and min(omega)>0
assert all(sum(w*q[k]for w,q in zip(omega,Q))==0 for k in range(3))
assert all(sum(w*c[k]for w,c in zip(omega,C))==0 for k in range(3))
assert all(sum(w*q[k]*c[l]for w,q,c in zip(omega,Q,C))==F(k==l,3)for k in range(3)for l in range(3))
assert all(sum(w*A[k][l]for w,A in zip(omega,T))==5*Sigma[k][l]/3 for k in range(3)for l in range(3))
Phi=transpose([list(q)+[q[k]*c[l]for k in range(3)for l in range(3)]for q,c in zip(Q,C)])
nu=[0,0,-159,159,-278,159,0,-159,278]
assert all(dot(row,nu)==0 for row in Phi) and sum(nu)==0
rr,piv=rref(Phi);assert len(piv)==8
rows=rref(transpose(Phi))[1];minor=det([[Phi[i][j]for j in piv]for i in rows])
assert rows==[0,1,2,3,4,7,8,11] and piv==list(range(8))
assert minor==F(36893488147419103232,659324621620108719135)
Psi=Phi+transpose(C);assert len(rref(Psi)[1])==9
aug_rows=rows+[12];aug_minor=det([Psi[i]for i in aug_rows]);assert aug_minor
lever=tuple(sum(n*c[k]for n,c in zip(nu,C))for k in range(3))
second_lever=[[sum(n*A[k][l]for n,A in zip(nu,T))for l in range(3)]for k in range(3)]
assert lever==(-F(256,3),0,0)
assert second_lever==[[0,0,9],[0,0,0],[9,0,0]]
bound=min(w/abs(n)for w,n in zip(omega,nu)if n);assert bound==F(3,16384)
s=F(1,16384);fake=[w+s*n for w,n in zip(omega,nu)]
assert min(fake)>0 and sum(fake)==1
assert [dot(row,fake)for row in Phi]==[dot(row,omega)for row in Phi]
fake_center=tuple(3*sum(w*c[k]for w,c in zip(fake,C))/4 for k in range(3))
assert fake_center==(-F(1,256),0,0)
# Two separate physical metric controls; no equations mix their metric pairs.
def mechanics(M):
 M=[list(map(F,row))for row in M]
 minors=[det([row[:k]for row in M[:k]])for k in (1,2,3)];assert min(minors)>0
 N=transpose([solve(M,[F(i==j)for i in range(3)])for j in range(3)])
 assert mm(M,N)==[[F(i==j)for j in range(3)]for i in range(3)]
 GX=mm(mm(X,M),transpose(X));GQ=mm(mm(Q,N),transpose(Q))
 D=[[GX[i][j]-GX[i][i]for j in range(10)]for i in range(10)]
 A=[[GQ[i][j]-GQ[i][i]for j in range(9)]for i in range(9)]
 assert all(D[i][j]!=0 for i in range(10)for j in range(10)if i!=j)
 assert all(A[i][j]!=0 for i in range(9)for j in range(9)if i!=j)
 U=[i for i in range(10)if all(D[i][v if i==u else u]<0 for u,v in E if i in (u,v))]
 S=[i for i in range(9)if all(A[i][j]<0 for j in range(9)if len(set(FC[i])&set(FC[j]))==2)]
 saddles=[]
 for (u,v),(i,j)in sorted(edge_faces.items()):
  if D[u][v]<0 and D[v][u]<0 and A[i][j]<0 and A[j][i]<0:saddles.append([u,v])
 assert len(S)+len(U)-len(saddles)==2
 return dict(M=M,N=N,leading_minors=minors,primal_shadow=D,pole_shadow=A,
 stable_facets=S,unstable_vertices=U,saddle_edges=saddles,
 mechanical_class=[len(S),len(U),len(saddles)],
 minimum_absolute_primal_shadow=min(abs(D[i][j])for i in range(10)for j in range(10)if i!=j),
 minimum_absolute_pole_shadow=min(abs(A[i][j])for i in range(9)for j in range(9)if i!=j))
linear_image=[list(map(F,row))for row in [(3,1,0),(0,4,1),(1,0,3)]]
primary=mechanics(mm(transpose(linear_image),linear_image))
assert det(linear_image)==37 and primary['leading_minors']==[10,161,1369]
assert primary['stable_facets']==[0,1] and primary['unstable_vertices']==[0,4]
assert primary['saddle_edges']==[[2,3],[6,7]]
secondary=mechanics([(10,1,2),(1,15,3),(2,3,12)])
assert secondary['stable_facets']==[0,1,6] and secondary['unstable_vertices']==[0,1,4,5]
assert secondary['saddle_edges']==[[0,1],[2,3],[4,5],[6,7],[8,9]]
# Exact closed metric box, including every unused shadow sign.
eps=F(1,2**20);M=primary['M'];K=max(abs(v)for row in M for v in row)
assert min(M[i][i]-sum(abs(M[i][j])for j in range(3)if i!=j)for i in range(3))>3*eps
norm1=lambda x:sum(abs(v)for v in x)
for i in range(10):
 for j in range(10):
  if i!=j:assert abs(primary['primal_shadow'][i][j])>eps*norm1(X[i])*norm1(sub(X[j],X[i]))
for i in range(9):
 for j in range(9):
  if i!=j:assert det(M)*abs(primary['pole_shadow'][i][j])>(4*K*eps+2*eps*eps)*norm1(Q[i])*norm1(sub(Q[j],Q[i]))
primary['closed_six_entry_metric_box_radius']=eps
# The primary Euclidean body is a rational affine image at its own centroid.
image_vertices=mm(X,transpose(linear_image))
inverse=transpose([solve(linear_image,[F(i==j)for i in range(3)])for j in range(3)])
image_poles=mm(Q,inverse);image_centers=mm(C,transpose(linear_image))
assert mm(image_vertices,transpose(image_poles))==mm(X,transpose(Q))
image_Phi=transpose([list(q)+[q[k]*c[l]for k in range(3)for l in range(3)]for q,c in zip(image_poles,image_centers)])
assert all(dot(row,nu)==0 for row in image_Phi) and len(rref(image_Phi)[1])==8
# Full Phi is exactly integer_Phi * diag(1/column_denominators).
L=[lcm(*(Phi[i][j].denominator for i in range(12)))for j in range(9)]
IP=[[int(Phi[i][j]*L[j])for j in range(9)]for i in range(12)]
result=dict(identity='ROOF_E17_ACTUAL_AFFINE_FLUX_RANK8_V1',parent=[PARENT,PINSHA],direct_control=CONTROL,
vertices=V,H_normals=NORM,H_rhs=RHS,facets=FC,edges=E,edge_facets=[edge_faces[tuple(e)]for e in E],
nonsingular_H_triples=nonsingular,minimum_raw_nonincidence_slack=minimum_slack,
area_over_normal=area_factor,area_squared=[a*a*dot(n,n)for a,n in zip(area_factor,NORM)],
volume=volume,centroid=COM,actual_covariance=Sigma,actual_poles=Q,centered_area_centroids=C,
centered_facet_second_moments=T,actual_cone_weights=omega,Phi_integer=IP,Phi_column_denominators=L,
rank=8,minor_rows=rows,minor_columns=piv,minor=minor,null_vector=nu,augmented_rank=9,
augmented_minor_rows=aug_rows,augmented_minor=aug_minor,centroid_kernel_image=lever,
second_moment_kernel_image=second_lever,positive_weight_parameter_bound=bound,fake_parameter=s,
fake_weights=fake,fake_coned_centroid=fake_center,primary_metric_control=primary,
secondary_metric_control=secondary,primary_affine_map=linear_image,
primary_Euclidean_body=dict(vertices=image_vertices,poles=image_poles,area_centroids=image_centers,
volume=37*volume,centroid=[0,0,0],Phi=image_Phi,covariance=mm(mm(linear_image,Sigma),transpose(linear_image))),
scope='Actual rank-deficient E17 bodies, not 110; fake weights are only affine-flux solutions, not a second mass realization.')
blob=(json.dumps(serial(result),sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
Path('roof_rank8.json').write_bytes(blob)
print('ACTUAL_H_V_F_E_10_17_9_RANK8_NULL_PASS')
print('ACTUAL_CENTROID_AND_SECOND_MOMENT_EACH_RESTORE_RANK9_PASS')
print('POSITIVE_AFFINE_FLUX_WEIGHT_LINE',bound,'FALSE_CENTROID',*fake_center)
print('RATIONAL_EUCLIDEAN_E17_RANK8_CLASS_2_2_2_ALL162_NONZERO_PASS')
print('CLOSED_METRIC_BOX_CLASS_2_2_2_PASS',eps)
print('SECONDARY_METRIC_CLASS_3_4_5_ALL162_NONZERO_PASS')
print('REPORT',*pin(blob));print('SOURCE',*pin(Path(__file__).read_bytes()))
if len(sys.argv)>1:
 text=Path(sys.argv[1]).read_text();p=text[text.index('## Parent '+PARENT):];p=p[p.index('Получены три'):].rstrip()+'\n'
 parent=json.dumps(dict(version=2,result_markdown=p),ensure_ascii=False,separators=(',',':')).encode()
 assert pin(parent)==[49087,PINSHA]
 print('LITERAL_PARENT_ENVELOPE_SHA256_PASS',*pin(parent))
```

### Полный исходник roof_stratum_symbolic.py

```python
"""Exact roof rank-stratum algebra. CPython 3.13.5; SymPy 1.14.0.
Run: python roof_stratum_symbolic.py
No numeric sampling or external input. Physical domain: 0<a<c, 0<d<b, r>0.
"""
import sympy as s
from pathlib import Path
import hashlib
assert __debug__ and s.__version__=='1.14.0'
a,b,c,d,r=s.symbols('a b c d r',positive=True)
D=b*c-a*d;L=D-r*(b-d)
E=s.Matrix([[0,(b-d)*(a+c+r),2*c+r],
 [b*(2*a+r)/(a+r),(c-a)*(b+d),0],
 [b*(a+2*r)/(a+r),L,c-r]])/3
OX=s.Matrix([[b-d,1],[L*(a+c+r)/3,(c-r)*(2*c+r)/3]])
OY=s.Matrix([[1,c-a],[(a+2*r)/(3*(a+r)),(c-a)/3]])
assert s.factor(E.det()-b*r*(a-c)*(a*b-a*d+b*c+b*r+c*d)/(9*(a+r)))==0
assert s.factor(OX.det()-(a-c)*(a*d-b*c+b*r+2*c*d)/3)==0
assert s.factor(OY.det()-r*(a-c)/(3*(a+r)))==0
n=[(0,0,-1),(0,-1,b),(-(b-d),-(c-a),L),(b-d,-(c-a),L),
   (1,0,c-r),(b-d,c-a,L),(0,1,b),(-(b-d),c-a,L),(-1,0,c-r)]
one=s.Integer(1)
gq=(a+2*r)/(3*(a+r));yq=b*(2*a+r)/(3*(a+r))
g=[(0,0,0),(0,-yq,gq),(-(a+c+r)/3,-(b+d)/3,one/3),
   ((a+c+r)/3,-(b+d)/3,one/3),((2*c+r)/3,0,one/3),
   ((a+c+r)/3,(b+d)/3,one/3),(0,yq,gq),
   (-(a+c+r)/3,(b+d)/3,one/3),(-(2*c+r)/3,0,one/3)]
B=s.Matrix.hstack(*[s.Matrix(list(u)+[u[i]*v[j]for i in range(3)for j in range(3)])for u,v in zip(n,g)])
pressure=s.Matrix([0,0,-1,1,-2*(b-d),1,0,-1,2*(b-d)])
star=c-d*(a+2*c)/b
assert all(s.factor(z.subs(r,star))==0 for z in B*pressure)
base_area=2*(b*(a+c)+d*(c-a))
zcom=(base_area+4*b*r)/(4*(base_area+2*b*r))
h=[0,b,D,D,c,D,b,D,c]
nu=s.Matrix([(h[i]-n[i][2]*zcom)*pressure[i]for i in range(9)])
C=s.Matrix([[g[i][k]-(zcom if k==2 else 0)for i in range(9)]for k in range(3)])
target=s.Matrix([4*r*(b-d)*(a-c)/3,0,0])
assert all(s.factor(z.subs(r,star))==0 for z in C*nu-target)
assert all(s.factor(z.subs({a:1,b:4,c:2,d:1,r:s.Rational(3,4)})*s.Rational(256,9)-v)==0 for z,v in zip(nu,[0,0,-159,159,-278,159,0,-159,278]))
# Only the six triangular facets have nonzero pressure.
roof_x=[0,0,-r,r,r,r,0,-r,-r]
Txz=s.Matrix([[g[i][0]/4+roof_x[i]/12-zcom*g[i][0] for i in range(9)]])
second=r*(c-a)*(-b+2*d+zcom*(4*b-5*d))/3
assert s.factor(((Txz*nu)[0]-second).subs(r,star))==0
alpha,delta=s.symbols('alpha delta',positive=True)
num=4-(7+alpha)*delta+(7-alpha)*delta**2
den=alpha+2-(2*alpha+1)*delta
expr=s.factor((-b+2*d+zcom*(4*b-5*d)).subs(r,star).subs({a:alpha*c,d:delta*b}))
assert s.factor(expr-b*num/(4*den))==0
positive=s.Rational(3,2)+2*(s.Rational(1,2)-delta)+6*(s.Rational(1,2)-delta)**2+(1-alpha)*delta*(1+delta)
assert s.expand(num-positive)==0
print('ROOF_ALL_PARAMETERS_FOUR_CHARACTER_BLOCK_IDENTITIES_PASS')
print('ROOF_RANK8_IFF_r_EQUALS_c_MINUS_d_TIMES_a_PLUS_2c_OVER_b')
print('ROOF_STRATUM_CENTROID_KERNEL_IMAGE_NONZERO_PASS')
print('ROOF_STRATUM_ACTUAL_SECOND_MOMENT_KERNEL_IMAGE_POSITIVE_PASS')
raw=Path(__file__).read_bytes();print('SOURCE',len(raw),hashlib.sha256(raw).hexdigest())
```
