# minimum-0096

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# BEVEL_OWN_COM_ALL_SPD_U2_V1
## Вся bevel-семья исключена: при любой положительно определённой метрике U≥2

**Получен полный запрет для оставшегося класса, без ограничения обусловленности.** Для каждого `0<ε≤1/2`, каждой SPD-матрицы `M` и `N=M⁻¹` настоящий равномерный многогранник

`Pε=conv(({±1}³\{(1,1,1)})∪{(1,2,3)})∩{y+z≥−2+ε}`

при **собственном объёмном COM** имеет как минимум две **строгие неустойчивые вершины**. Это сильнее запрета совместного S1/U1: гипотезы S1, H0 и weak000 не нужны, дополнительные слабые равновесия разрешены. Все собственные аффинные образы этой семьи включены. Остаток `κ>8/3` для поставленной задачи110 **закрыт полностью**, а не немного сокращён.

Граница U≥2 достигается на каждом члене семьи. Сохранено новое **двухпараметрическое настоящее семейство222weak000**: все `0<ε≤1/2`, все вещественные `L≥128`, одна явно заданная взаимно обратная пара метрик с неограниченно растущей обусловленностью. Следовательно `min_{M>0} U(Pε,M)=2` для каждого ε. Это не аттейнер110; существование S1 **отдельно от U1** здесь не решалось.

**Глобальная скобка остаётся34≤C_min≤622.** Закрыта данная кривая настоящих геометрий вместе со всеми её аффинно-метрическими образами, не вся область реализаций её комбинаторного типа и не весь E17. Никакого FULL/LOCAL/root registrydelta не заявляется.

## 1. Источники, прочтение и смена механизма

Полностью прочитан новый `research-journal(20260919-073838).md`,2448строк, включая весь буквальный parent и recovery-капсулу. Точные байты:274444; SHA-256 `7a203afda7dbd4853bdf00b53f2cc958f5fe12f27d0bf16bb5a8e0379957135a`. Усечённый первоначальный вывод расширен последовательными диапазонами до EOF. Прочитаны полные три используемые parent-sourceunits. Неизменённые материалы предыдущих продолжений остаются прежними; отсутствующих дополнительных зависимостей для нового доказательства нет.

Буквальный parent — **minimum-0093**, runtime SHA-256 `7d6294560524b0a9265a56603e131bdcc2153edc2c1caa92c3ec106f16d531fa`, **ACTUAL_FACET_ESCAPE_BUDGET_AND_BEVEL_FULL_CLASS_V1**. Его прежняя область — две устойчивые x-грани при κ≤8/3 — не была запретом произвольной метрики. Здесь используется буквально та же Pε, без изменения геометрического рецепта. Конфликта с parent не обнаружено. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

Результат не получен попыткой вновь сделать малым суммарный гранный функционал: настоящий тонкогранный контрконтроль parent остаётся действующим. Вместо совместной оптимизации S1/U1 оказалось достаточно исключить **все настоящие слабые вершинные деревья одним и тем же объёмным центром**. Метрика устраняется положительно определёнными матричными тождествами, а весь параметр ε — кубическими матричными коэффициентами Бернштейна. :contentReference[oaicite:2]{index=2}

Это не новая универсальная теорема о completion и не повторная проверка её рангов. Спектр Lambda, свободные гранные средние и независимо выбранные массы вообще не участвуют в исключении. Внешняя историческая первизна и proof-assistant формализация не установлены.

## 2. Полная настоящая геометрия и собственный COM

### 2.1. Постоянные метки

Положим t=ε. Все10 исходных вершин в порядке0,…,9:

```
(-1,-1,-1+t), (-1,-1,1), (-1,-1+t,-1), (-1,1,-1), (-1,1,1),
( 1,-1,-1+t), ( 1,-1,1), ( 1,-1+t,-1), ( 1,1,-1), ( 1,2,3).
```

Настоящие поддержки `a_i·x≤b_i(t)`:

```
i    a_i          b_i
0   (-1, 0, 0)      1
1   (-1, 0, 1)      2
2   (-1, 2, 0)      3
3   ( 0,-1, 0)      1
4   ( 0,-2, 3)      5
5   ( 0, 0,-1)      1
6   ( 0, 4,-1)      5
7   ( 1, 0, 0)      1
8   ( 0,-1,-1)    2−t
```

Полные наружные максимальные гранные циклы:

```
F0=(0,1,4,3,2)   F1=(1,9,4)     F2=(3,4,9)
F3=(0,5,6,1)     F4=(1,6,9)     F5=(2,3,8,7)
F6=(3,9,8)       F7=(5,7,8,9,6)  F8=(0,2,7,5).
```

Все17 истинных рёбер в лексикографическом порядке:

```
(0,1),(0,2),(0,5),(1,4),(1,6),(1,9),(2,3),(2,7),(3,4),
(3,8),(3,9),(4,9),(5,6),(5,7),(6,9),(7,8),(8,9).
```

Итак, `(V,E,F)=(10,17,9)`, размеры граней `(5,3,3,4,3,4,3,5,4)`. Нет восьмиугольной базы. Фиксированная настоящая вершинная триангуляция каждой грани — веер из первого элемента указанного цикла; суммарно16треугольников. Интеграционные диагонали не входят в17рёбер.

### 2.2. Непрерывная полнота геометрии

Все независимые тройные пересечения H-плоскостей аффинны по t. Exact-аудитор перебирает все84тройки:21зависима;38независимых кандидатов, не являющихся указанными вершинами, имеют одну явно выписанную линейную поддержку, строго нарушенную на всём `0<t≤1/2`; остальные дают ровно10перечисленных вершин. Все56неинцидентных vertex/facet-slacks строго положительны на этом интервале. Совпадения и ненулевые определители проверены полиномиально, не по нескольким t.

Тело ограничено: `−1≤x≤1`, `−1≤y≤2`, `−1≤z≤3`;0 — его внутренняя точка. Все девять поддержек настоящие. Каждый указанный цикл составлен из настоящих пересечений соседних граней. Положительность всех16ориентированных конусных детерминантов проверена на всём интервале, при необходимости с вынесением положительного множителя t. Значение t=0 используется только для полиномиальной границы, не объявляется10-вершинным телом.

### 2.3. Истинное объёмное центрирование

Обозначим объём через `v(t)`, чтобы не путать его с числом вершин:

```
v(t)=12−t²,
g(t)=(1, 3+t²−t³/3, 5+t²−t³/3)/(12−t²),
m(t)=(3, 9+3t²−t³, 15+3t²−t³)=3v(t)g(t).
```

Это настоящие интегралы. Из P0 удаляется ровно призма `[-1,1]×{u,v≥0,u+v<t}`, где `y=−1+u,z=−1+v`: её объём t², среднее `(0,−1+t/3,−1+t/3)`. Кроме того, новый код независимо от этого вычитания проверяет символически по16настоящим конусам

`Στ det(v_a,v_b,v_c)=6v(t)`,

`Στ det(v_a,v_b,v_c)(v_a+v_b+v_c)=8m(t)`.

Деление второго равенства на четыре первых детерминантных суммы даёт именно g(t). Все дальнейшие механические точки — `x_i(t)=v_i(t)−g(t)`, не вершины относительно старого g0 и не свободного contact-reference.

## 3. Почему U1 даёт один из54400 настоящих деревьев

Пусть M — произвольная SPD-матрица. Введём

`D_ij=x_iᵀM(x_j−x_i)`

только для настоящих направленных рёбер. Строгая неустойчивость вершины эквивалентна отрицательности всех её исходящих истинных D. Если вершина не строго неустойчива, касательный конус, порождённый настоящими рёбрами, даёт хотя бы один слабый выход `D_ij≥0`.

Для такого выхода

`|x_j|_M²−|x_i|_M²=2D_ij+|x_j−x_i|_M²>0`.

Поэтому выбранные слабые выходы не образуют ориентированный цикл, включая нулевые D. Если строгая U-вершина ровно одна, выбор одного выхода у каждой другой вершины образует настоящее остовное дерево, направленное к этой вершине. Любая вершина максимальной M-нормы строго неустойчива, включая случай нескольких равных максимумов, поэтому U≥1 без дополнительных гипотез.

Таким образом, исключение всех корневых деревьев приведённого истинного графа доказывает U≥2. Не нужно знать стабильную грань, выбирать сопряжённое дерево или устранять weak-пакеты возмущением.

## 4. Полные непрерывные матричные сертификаты

### 4.1. Механические знаки как кубические матрицы

Перечислим34направленных ребра по возрастанию исходной вершины, затем конечной. Для каждого `(i,j)` положим

`v_j(t)−v_i(t)=s_ij(t)e_ij`,

где `e_ij` — постоянное примитивное целочисленное направление, а `s_ij(t)>0` на всём целевом интервале. Точный рецепт: вычислить разность при t=1 и разделить на положительный НОД её трёх целых компонент; затем восстановить s по любой ненулевой компоненте. Этот t=1 — только выбор направления, не новая область исключения.

Определим

```
W_i(t)=3v(t)v_i(t)−m(t)=3v(t)x_i(t),
B_ij(t)=W_i(t)e_ijᵀ+e_ij W_i(t)ᵀ.
```

Все B — симметричные матричные полиномы степени≤3 с целыми коэффициентами. В одной и той же механической метрике

`tr(M B_ij(t))=6v(t)D_ij/s_ij(t)`.

Знак сохранён строго положительным множителем. Никаких отдельно подобранных масс или метрик у разных стрелок нет.

### 4.2. Сертификат для частичного набора выходов

Полная таблица содержит150строк; каждая — список индексов стрелок с положительными целыми весами λ. В каждой строке исходные вершины различны. Имеются118строк по3стрелки,31по4 и одна по5: всего483члена, все веса от1до6. Все данные буквально включены в source-only капсулу раздела9.

Для строки R строится

`K_R(t)=−Σ_{a∈R}λ_a B_a(t)=K₀+tK₁+t²K₂+t³K₃`.

У каждой строки **все четыре** следующие целочисленные матрицы положительно определены:

```
24K₀,
24K₀+4K₁,
24K₀+8K₁+2K₂,
24K₀+12K₁+6K₂+3K₃.
```

Это24кратные кубические матричные коэффициенты Бернштейна на `[0,1/2]`. При `u=2t` матрица K_R равна сумме этих четырёх матриц с неотрицательными весами `C(3,k)u^k(1−u)^(3−k)/24`. Следовательно `K_R(t)≻0` на **всём закрытом интервале**, включая оба конца.

Всего проверено600PD-матриц и1800положительных ведущих миноров; минимальный из этих целых миноров1548. Каждый блок отдельно проверен рациональными дополнениями Шура. Это точный конечный сертификат полиномиальной положительности, а не выборка форм или метрик.

Если все стрелки строки были бы слабыми выходами, то

`tr(MK_R)=−Σλ_a·6vD_a/s_a≤0`.

Но M≻0 и K_R≻0 дают `tr(MK_R)>0`. Противоречие. Одна строка исключает свой частичный набор выходов одновременно при **каждом t и каждой SPD M**, без верхней границы её собственных значений или отношения собственных значений.

Для непосредственного контроля первая строка — `(0→1),(1→4),(5→0)`, все λ=1. Её четыре коэффициента в степенном базисе:

```
K₀=((66,-6,-12),(-6,90,24),(-12,24,102))
K₁=((0,0,36),(0,0,0),(36,0,-72))
K₂=((-6,-3,-3),(-3,0,6),(-3,6,0))
K₃=((0,1,-2),(1,-2,-2),(-2,-2,4)).
```

Остальные149строк не сокращены и не оставлены за внешним файлом: вся таблица и все помощники восстановления находятся в капсуле.

### 4.3. Полнота комбинаторного покрытия

Первый точный checker перебирает **все** `C(17,9)=24310` подмножеств истинных рёбер. Ровно5440соединяют все10вершин; при9рёбрах это ровно все остовные деревья. Для каждого из10корней дерево единственным образом ориентируется к корню. Каждый из **54400** полученных наборов слабых выходов содержит хотя бы одну из150запрещённых строк. Число5440 дополнительно совпало с точным лапласовым кофактором, вычисленным Bareiss.

Второй, независимый standard-library checker **не импортирует генератор**. Он перебирает все530712функций выбора настоящего соседа у каждой некорневой вершины, отбрасывает ориентированные циклы и получает те же54400корневых дерева, по5440на каждый корень. Их первые покрывающие строки совпали побайтно с первым перечислением.

Для независимой проверки матричной части второй checker вычисляет K непосредственно из настоящих W,e в четырёх рациональных параметрах и восстанавливает кубические коэффициенты Бернштейна решением интерполяционной системы. Доказанная степень≤3 делает это проверкой тождеств, не sampling positivity. После этого все600восстановленных блоков проверяются Schur и сравниваются с отчётом.

**Теорема доказана:** U1 обязала бы выбрать одно из54400деревьев; оно содержит запрещённую строку; её единая SPD-трасса невозможна. В сочетании с U≥1 получаем U≥2.

## 5. Реальное неограниченно обусловленное семейство, достигающее U2

Чтобы не превратить исключение в потерю полезных физических конструкций, сохранена полная непрерывная семья с точным SUH222weak000.

Пусть

```
u=(1,2,-1), v=(7,-4,-1), w=(1,1,3),
N_L=L²uuᵀ+Lvvᵀ+wwᵀ,
M_L=uuᵀ/(36L²)+vvᵀ/(4356L)+wwᵀ/121,       L≥128.
```

Векторы взаимно ортогональны, их квадраты норм6,66,11. Поэтому M_L=N_L⁻¹ точно; собственные значения N_L равны6L²,66L,11. Для **каждых** `0<t≤1/2,L≥128` при действительном g(t):

```
строго устойчивые грани: F4,F6;
строго неустойчивые вершины: 2,9;
строгие седловые рёбра: (3,4),(5,6);
дополнительные weakVE/EF/VF: отсутствуют.
```

Все68настоящих направленных рёберных примитивов ненулевые. В частности, x-грани F0,F7 здесь **не** устойчивы: переносить на большие κ прежнее доказательство через неизменные две x-подошвы было бы неверно. Глобальный запрет110 сохраняется по другой причине — две U-вершины.

### Непрерывное доказательство механики222

Положим β=1/L. Компактный прямоугольник доказательства — `0≤t≤1/2,0≤β≤1/128`; физическая семья имеет t,β>0. Обозначим

`h_i(t)=3v(t)b_i(t)−a_i·m(t)>0`,

так что настоящие собственно-центрированные полюса равны `q_i(t)=3v(t)a_i/h_i(t)`.

Знак каждого примального примитива совпадает со знаком

`W_iᵀ[121β²uuᵀ+βvvᵀ+36wwᵀ]e_ij`.

Знак каждого дуального примитива совпадает со знаком

`h_i a_iᵀ[uuᵀ+βvvᵀ+β²wwᵀ]a_j − h_j a_iᵀ[uuᵀ+βvvᵀ+β²wwᵀ]a_i`.

Каждое выражение имеет бистепень≤(3,2). Для всех68выражений после умножения на заявленный знак получены **12строго положительных тензорных коэффициентов Бернштейна на всём прямоугольнике**. Всего816положительных коэффициентов; наименьший24075/4096. Все они восстановлены независимо прямой тензорной интерполяцией физических формул. Отдельно проверены положительные собственно-центроидные знаменатели h_i.

Знаки дают в точности перечисленные S/U/H. Любой слабый VE/EF/VF-пакет потребовал бы нулевого соответствующего истинного рёберного примитива, которых нет. Значения t=0 или β=0 используются только для полиномиального сертификата; вырожденные метрики и потеря двух вершин при t=0 не включаются в физический класс.

Относительно настоящей объёмной ковариации Σ_t обусловленность тоже неограниченна. Два обобщённых отношения Рэлея дают

`cond(Σ_t⁻¹/²N_LΣ_t⁻¹/²) ≥ (36/121)L²·(wᵀΣ_t w)/(uᵀΣ_t u)`.

Для каждого t множитель положителен; при L→∞ правая часть растёт квадратично. Здесь Σ_t не заменяет механическую N_L.

## 6. Два полностью проинтегрированных точных контроля

Первый — `t=1/2,L=128`:

```
Vol=47/4,
g=(4/47,77/282,125/282),
N=((22657,29185,-17277),
   (29185,67585,-32253),
   (-17277,-32253,16521)).
```

Второй — `t=1/128,L=4096`:

```
Vol=196607/16384,
g=(16384/196607,18874751/75497088,31457663/75497088),
N=((16977921,33439745,-16805885),
   (33439745,67174401,-33538045),
   (-16805885,-33538045,16781321)).
```

Для обоих M определяется полной точной формулой раздела5; прямое матричное умножение проверяет MN=I. Рациональные нижние оценки относительной κ соответственно

`374166061056/18540313`,

`313795931069566817805533184/14521547987986714763`.

Оба тела имеют настоящий собственный222weak000, не110. Их одинаковая комбинаторика не отождествляется ни с FinchVol35, ни с H0Vol4/3, ни с проективным H0-контролем6/6/10.

Для каждого восстановлены настоящие площадные C_i,T_i, объёмная Σ_t и все34положительных детерминантных контактных веса. По настоящему треугольнику с суммой вершин s и `Bτ=ssᵀ+Σv∈τ vvᵀ` используются точные средние s/3,Bτ/12 для площади и s/4,Bτ/20 для конусного объёма. Поэтому вторые моменты **не** подменены вершинной суммой `Σμvvᵀ`; обязательная внутритреугольная поправка parent не отброшена.

Проверены `T_iq_i=C_i`, `Σd_iC_i=0`, `Σd_iT_i=5Σ_t`, все гранные суммы μ, а также общие `Σμq=0`, `Σμqxᵀ=I`, `Σμx=0`. Проверена настоящая взаимная векторная формула для каждой из17рёберных подошв и её конусных компонент.

Дополнительно для каждой геометрии/метрики вычислены **все129весов**, двумя точными способами: simplex-KKT и reciprocal exterior-KKT. Итого258согласованных весов. Сохраняются все независимые допустимые носители и их нулевые коэффициенты; сингулярные Gram не отвергаются как невозможные геометрии. В каждом контроле13нулевых весов,676независимых кандидатных exterior-support описаний и63проверки полного rank3носителя с математическим Hessian **2M**.

Эти проверки нерва — контроль двух реальных точек, не самостоятельное конечное покрытие произвольного N. Полное исключение всей семьи доказано в разделах3–4 без cycle–cocycle аргумента; сертификат с обрезанным T_y не используется и не заявляется.

## 7. Область, отрицательные результаты и переносимость

Полностью исключены **все** ε из задания, **все** SPD N и их общая обратная M, все корни и все слабые стены. Нет оставшейся высокообусловленной части этой семьи для110. Совместная аффинная замена `P↦AP+b`, `M↦A⁻ᵀMA⁻¹`, `N↦ANAᵀ` сохраняет доказательство, поскольку настоящий объёмный COM переходит в Ag+b.

Не исключены другие реализации того же графа, произвольные9-гранники, весь E17 или S1 с несколькими U. Не обнаружен110аттейнер. Сохранён не просто отдельный нерекордный пример, а полная достигающая U2 семья222 с произвольной большой κ. Она одновременно показывает, почему две конкретные прежние устойчивые грани не могут служить глобальным механизмом.

Переносимый метод: на настоящем параметрическом семействе вычислить его **истинный** центр, снять положительные знаменатели механических выходов, затем найти конечные частичные наборы выходов, чьи отрицательные положительно-взвешенные матричные суммы PD на всём геометрическом параметре и которые покрывают все настоящие корневые деревья. Полнота по метрике получается из двойственности PSD-трассы, а не из сетки или условной компактности SPD-конуса. Общая техника положительных квадратичных сертификатов уже присутствовала в родительской научной линии; новым результатом здесь является её полное физическое покрытие этой не-roof8семьи с явной малой таблицей.

**34≤C_min≤622 неизменно.**54400 — число корневых деревьев одного истинного графа в данном доказательстве, не число новых FULL/LOCAL/incidence-domains. Ни один исторический счётчик не пересчитан и не уменьшен. Следующее геометрическое продолжение — другие истинные E17реализации, где аналогичный центр-зависимый PD-cover не существует или требует новых поверхностных ограничений; повторное увеличение κ для уже закрытой Pε не требуется. :contentReference[oaicite:3]{index=3}

## 8. Фактическая проверка и pins

Все вычисления, принимающие результат, выполнены **точно**, без float-допусков. Полный source-only build/check выполнен; затем обе sourceunits перенесены в чистый каталог и повторены. Наконец, одна нижеследующая recovery-капсула перенесена в третий чистый каталог и восстановила всё с нуля. JSON, оба исходника и terminal outputs совпали побайтно. Независимый checker не импортирует builder и использует другое перечисление деревьев и другую реконструкцию коэффициентов.

Исполненная среда **CPython3.13.5, только стандартная библиотека**, assertions enabled. Нет SymPy, NumPy, SciPy, численного solver, seed, сети или внешнего checkpoint в recovery. Полная целочисленная таблица150строк — точный вход verifier, а не инструкция вновь найти отсутствующие множители. Предварительные поисковые пробы не используются как доказательство невозможности.

| Объект | Bytes | SHA-256 |
|---|---:|---|
|recover_bevel_all.py|13845|91971815a4ee6e1efb01ee4774d5e005687e92fb39dfeba8ff3118ea2a654ce1|
|decoded two-source payload|26966|8272a48b24d0a4734399ccb698862fc186db579f2b29ccd3cbd2c28b2a50d0fa|
|bevel_all_spd.py|20799|0ea6d3d1dc1a0cba8d9ffe27204448ecfd35e1ef90e09f488026ab622874ca33|
|verify_bevel_independent.py|5598|4b20769bb5d12b8eb58a60e5063b221cb5fcc579bf81f7b650f0c0d09f9502b2|
|bevel_all_spd.json|220670|f4dd53a7634854909822623e71545910a4001f4e0bc3a9faf5ec29cb035e70a2|
|main check stdout|512|e7cac0f7d040188de6c5dce9306abb6d798a9a4571761df8d88384fcfab6552d|
|independent stdout|246|6432ed20f640b2197a8715d419ce10e783af0bf06457d6465127501f1e625bfd|
|whole capsule check stdout|810|f730957d1d8690809734bbb43985c4ad9a94625dac319207c5e0516c2434fcfc|

Полный поток покрытия54400деревьев детерминированно восстанавливается обоими checker:272000bytes, SHA-256 `32d602d1ee3d8909b20e82aad72935fe6edbc6498461af27c5307a3e3ce586d5`. Каждая запись —3байта big-endian17-битной маски истинных рёбер, затем байт корня и байт первой покрывающей строки. Порядок — лексикографический по9-элементному кортежу индексов рёбер, затем по корню. Код строит **весь поток**, не принимает его хеш вместо покрытия.

## 9. Полная самодостаточная recovery-капсула

Сохранить следующий полный текст как `recover_bevel_all.py`, UTF-8/LF с конечным LF; выполнить в чистом каталоге:

```
python -S recover_bevel_all.py build
python -S recover_bevel_all.py check
```

Ожидаемый полный вывод check:


[Encoded source block omitted; the code in this passage is incomplete.]


Дополнительные удобные копии: [читаемый полный генератор и TABLE](sandbox:/mnt/data/bevel_full/bevel_all_spd.py), [независимый checker](sandbox:/mnt/data/bevel_full/verify_bevel_independent.py), [точный полный отчёт](sandbox:/mnt/data/bevel_full/bevel_all_spd.json), [source-only капсула](sandbox:/mnt/data/bevel_full/recover_bevel_all.py). Ни одна ссылка не является необходимой зависимостью: ниже находятся все байты двух исходников с полными точными входами.

```python
"""BEVEL_OWN_COM_ALL_SPD_U2_V1: complete two-source recovery.
CPython3.13.5, standard library, assertions enabled, no external inputs.
python -S recover_bevel_all.py build|check
"""
from pathlib import Path
import base64,hashlib,json,subprocess,sys,zlib
assert __debug__
if sys.argv[1:] not in (['build'],['check']):raise SystemExit('Use build|check')
DATA=r'''
c-p;v3v=7H(&%5|Y3Dm4W!M&}haU<u<5v>5j-A?ak~4}9hZ1R-wnQnS9=3b?-|s#E5~Sob{pQY16PsKD3t+L>7Z&KBzx1PJH
1dPd$WN!?&h+`0!(YD9f5&H^&o2C{FPHww)kpv6;=;fAbn4%F{%3c`I{EZGzn>&leaEfuG=-JUgCq=Qp*4#8vtagYO_I^`&b
MUB#kOy(aywRk5s$+EGq{fikKdA`(a4IPg2CL1lj&lf3Tu8JS$7Kn4<^YxP8O3z3XjWZW<g69lw1V-Z8jODRxpdK`)C$HlSg
S9&F1kWNv&D*eG$*1aL2lw0Qz|}OQ6zSJc^)!WHF9r@c;nnWCVC&5K$DS)?{XdlT|XB1Yrv3m>A!ZyV+!H-OZq3LLHB%liA#
QrvO%vTJKb$7}}Xnuve<kU^4E<NkA2aHJweu#bB-qkAwNWSx#8PL8!h>;TzCXfBpoo-xBrmkWLa|-3KX_fUZBM-;#hvZux!~
^%q0m|CXGe%E}MsvGOhXbaZ`o*^%8!kPiJcaNqs$?()<3dHv(ye7QVH$BTo{56=}**$Z3VL8IBKHN8f^794o3X3%W4YW2viy
Zvx5@Z4rS3J2c69R%=sP>%*~t##+N!e-sQ3o5;D$=90fcDG$Ye|thb=1&@EKEcDc#DYKFyhv8f1Z5ANsQ0ij7aFUH8WqIfHT
vzU-!=2MYT@Tf1MbVK>yJklH#{2tMh~jjo+`bqt8ZhUR4Z22)Hb)(&>gSk)c^v`T)lgDbJoFTuz&~u>R1r|HA}xeRpaD8Cl_
ZoG;kLX*M&!z4@3hi1LS~OXo{AiUkf35#{f}X?2A1reIWL+39$!|1JR<I9=tWNrL)ub*pLkkIRbuq^s@;+p<(*jqMrxw6Ohu
+JtuF<u2V5+jecUW2K{VO#U>WETLjsoGSCMH+C4h`O?FdQ0a0i_Sn-_|OS!b7Q5spXbq8xV7648x>K}ez;+qXn$D!}^J`0jz
WV<!Oczu2K1&4xV7)7B7fe0tG-HmbZ?=OMGI2Q*nX>~P!P5s=neziLHvnaCW@i<CJk|}w07thkUwVaGV_5j9tG@Jz^5Hg>yE
@apBm?^#`x03i6p4-+JNz7e`$IoXcvb!g?8(ivF>ns@DTeHc^in$dKAk$Gak3b4TGj<5FZvcea4rWv+38N>FKa(_`$4k{d$k
SC65AWv=bfa^0d~pUt>oO}hm`V2F7yMR0mw$P!B6N?T#j;+#3`Kry=^98u4+gsS&D+m_RL0XyYACX^+oF#yvu0LBNd}i$U$?
BF_2P&Wv?-d#5P);(BR8sQG*k@}=rs#KMHqK8biWAQ-$);iI=!chczW#lH)zx2(K3_~FgDlQ0Q71F;6ZUXCNLY0>Xd3w&B#I
a(IecRLC%IEy%IMbPZ|%SUMo~|8=KG(1}N(mp&Of4%uvEhonJ58EaR;+NeG&gt6_9oV`vmOrm2S5$miIgt%9}~Zwb0zE}PFW
&3_Km2#V11fE#O!Q0TS#SkFIZ!*B3{$<~;LHjN>9`RX>%HZ_CQH?-Nzd5V^g3H96}Z*i~lrQ#K<cpFxXg1RP&jJAKka?Jvlt
_{iHJa4}YC47w{^q@$%rk<X{q%rCDii?+lZmq~-3aS>`UU_6n^wrHF@gVk0LS=kxe)H;zVOv@Xd0M6zP?tN<fCXScJw0=E#$
KpW*H!8!v{B^z3|coSlR=wI+XCLE7Ur(06ta&EUP6U_wl<NbJV`CR`aE+&TP5c7*85prb}dsX8fDc?wDNwIK5B8Jp?jJP4PI
zW$bCH{1-Y<aP_AwP>aCUa3~t&lLhD7{RDgPQy?VS2A6tbgnvgmAMqzOlpvJ;O=)p!cd9YDU7N8l29~9PXqX5;COY_yiMt!N
<Y2}L7m}56HW(o>Iubz@Nacdhzu&d0Irlwzg!&d+oSVe>Pb%#6+ZW^Vte!2yb+bV%uX20@LxSI!ONa!LiQwO)!aGBD$JVuuX
<K+|}uvbu?nGxn~?k-EdHNns*eQlU>Hs|w($<c1zT<Dn{>DD)zI61gTsQTu9);B6eQ?a}X&L^}8&N!^4S4Clgx~+{8TF=H_Q
QoKt*W%(}4V*0|b5whIlV*o9aHE8)k%P^an+$Fi25VSECLin<*70766y>jl4tSfFViBAT&fCoLniTcoyys08beslfO?n%^S@
&~m+WP@m6E2s?^+M?k+$@Z;zLEL>ZW`dM-_3On1ZVOaIEQyuIGNjl=sSnAXug;wR=OD5_EYtleBdYXj9&0dJf$*@cxTrfhbz
u!c97LV@6#R!QyU)ymahhmE;$|-TIhDM&6yampFO}909oJZ(fbVFgPy9ogsRKDD%V^(>m`FQEVlBrwQ&rpc)IA9if{k0_#hZ
X_M^y0+<mM*aRsv%lf^uml}4+HNqGCc^-9rmWG6<2cXll0gAs+`z(k@56c<2@;w73*QoDeo=Jcv{s^I4p>bk->DE1P`HxsEM
tVlP|V4M~SplLGOFdJbsuOoYWgNC`d9dv6w_*;bsw+DZ#LD%cS-)(yL)VterjG);zRdRKu+AEc6g-Tmg$tzcKRV6pCr1>*WC
bQJw=C10i(0x`Fv+h(qp+>02I}O!nRX{e7lGX=Bt^vQDwc)(2L9t)0BP)%j!7P|ZDhfWMXmK#IZU*;@nKh4KAz8@;a3xk052
Iumj24kKpNt}y%K^r{t-kDLEAJglL}@0h)qOmQtUh+kdXaq|O<VQxg?fTGy8Uk4>pt|h={Jm*N<Q><U&=h_icyrnQe9`o{7X
LP*`U=T!k{~|9h6BVRtTK-ygZ04;NGQ{24Y!aMFKyXYk-Cq%OrZ5+jd;;*rP}sj0(<iY>z!hTuzdR_yt3W7)L{Zo_c)7Z*wR
ru!_VV0$<xN5`W<n{+8XPq7U^DLD;+XB}(0+#{MNA`NevXsyl6Jqr2RGsje8ASm^<0Et@p$&br&KAt~pI1LI_=Sa2}Fa4C~I
VvfMbABh<zxrq-4jGYUTXM3QjkqhPlNNEbS0z1Pqx7813QJkil<t6m#upqqKlTj$$^||8aw_QhZWT5D&IdTL29=DjYpw~>h5
=X9mx0dn+7A!M#z*MeMLl0R)%m2X+%352Mlgr&*fM9+6@RE}!Kx%g>_^Q=jJkADg@NIz7L@hY(&s&%Gt*|z<br|eSCsW%oa4
Xpn7;9o2JSi&a_0(3Sso}1TJtk&)!^L=ZYR;D3FMR1|Up6QWHILJxM5h*VO{WWuv+e<7v0hPK+~S5{KGjsmf)ras8*L!k6rp
&|Sh42c0Oz0^Z$0$3B&f)oEYuCnYE$ImIbm5!Y+SWO?aZQOG)p6ry-T^Q&bOX&G)skGnprsT?L~rQ(<q9X{_sV@OuPsfFMM%
~d3s??gDJ>-5KJ`nqAvz=nU{g8_;*ZdPVi$NH);l;Ya9WT-gX7SJcNOogFoi}5dF!Dp~A_q)Lz3<BP?Y+RNX68cZ=0sqq<tt
(F~?kBof!ZxQ~I@U>x(J0;WnbL8;~TwwtRvhP;u<mTO2VG9?38Ue)`!T79U#vvIo<c<aFt^ps><G{%BPZD}lOZFH`Q{Vg|Bz
G{2JpG>I^uT8a3+tbM^n#o$WIB|k-IU>yp-GA%01CU7WVUO!<kp$~Yri`Oy2llVeT3ih@j0bZ&nx^q+lK6L^%O^8Q7z9>L=T
V%<z9RF})U?uIIR!XAZTkXSX_iD|tXH<izShLoY}mZl12zL~W8rv0+5K7rdV{dr`s(t-Hb7#2aQUH3NwNv8p&SlEyBcQW9GX
J}UAH^Tm0hU1u$oRr&vu-T2zf5G>&RrEuP(&Y(OfrFGdLAPJs2bfYPk28dPKBo<s(kCWubL2r)9U72^Zdyqs=>|Ky(M%kt~t
}KMy9+-JR?z+qi5BH=ImeE3&I?dRvo4%%W)&%%!I^%T)64qHez@Ub+D<sR$n6tq+T-ZSd0+mO~>`SdVPR<ic+X!VkNLdMW5Z
Z4xFp;GJL!Y#iG3*^ol;N$a3tG#N+0-vd7mqhub>pP5`=CDODFUw~@uFhyb4rVU8kAI9BW`qyixqhRounxrKWSnMLsk=phaY
F}FESm5!9D=W!flKNj2!Ins{zLq;Ah`ZfoFXtnm+!IM4HjtJQdwhuKH5GU!NtGRPul1KMOtV;u;^JRA><XxfNI_sDHb+W)<h
^p>IcAS%nE~`r9?J&p;5jo_tQaXecqW1RjP@b^+yZC19ZFUX-LJ6da)AaFdLV#ilgXVd_A}&R0Yacqm<shy%xJDmWzwWn4*q
`a0#2MlWIBFv>BUiR9=~xlntFJ}%K90XW+>8BQ5|?i6O_alO>Hcem`^i^QW<0CB5-O!>;=hOhMM5Obdp9!h!nkHJQ8NRC1CL
zU}iztg-`n+322xk2HsyH<)d&IQBsgpyZnF77gI1o)EkE$RIq?lHcwkwVh)~hLO^_P!LLJ5cz+pP$lH*VCt$d0qmhl8iYz3+
k2c$bdM-B!eB`aA96039o#>7D58FUfc(kaw9SifE27ojUVQFyMQgC+{Cv20m)<9nl+`Bj=Hbs-~fwu8!8Amufu*^w^VdKA1?
~Dv1C9w`1p*ZG9cGb!)@Z)bi<@S*CdgP!Q%+Q0nYpcYoh^6N!)sDoG=qd@oN(FH|l9`!<wY_OJXJ~Co8|kss?vievDvhAxKi
D1@cvP<3qY|BK(gmA;ksHuFmE5~Wv|7-ICd-8=yn~UBN2f4U&^l5(e*X(`Xf5Ljt<TL8?nUdselF?2tc6OV=Dd|P;y49RM%U
Y#TKI-SfzO~)yf$_gWFNft+WlD+JR0&&C5Gq`3;Q={okpk_DifZ+2`Jk$76`K+@n4n)<GiYQ%j&kR=In9ZxWM5?=)@|`LDo@
f<46fCNURZCDLQ>so;s7OC^#8`DdTbdzK(+A5w;^#&GimCB}<NTbtKv^bIj@SNqqSX_H_zRD&JoUU_d}J0yzm!Wotf}Bylnz
4ecw1%fCdn=KK#n3yV}{Frnwl_^3gSwg3hwpYP%UFlKH8d{XhY!DJR1%AFH|EXwpbED<hF;{+2q2N6so42=U;wKp<;Q*Y3-Q
DT*sSiP+&&LG^-gj2Go|733AfKsXKUob6LMpq+??`I6P97P@rcr;5M5-N<&jA1>hXE6qzScy-XC#a|Bz==>&83Y{5E)??`;P
?utn?I*^gF@d3EW-C04iGWOov`(Cu9qP|-8dj%9dteiV$h?2(N9Br%wr$ph>ndxKm3e!s%YQ!8r5Ykf5>_1YD#dlW1Vb0P#o
YCb;m{lqZf*$3Wfrj1i+Y+m7s`0=nocsFi4NJ$K#I!v`~S0kHL@%!Z;cF91oN@UejtIR^TRpG2A9gMAXUj#RzH=4?~&8em!5
bs%o}0Fk_hQ;c<|nm5Z3%H*ews3zf0rK=0#pK7qwOCUd!pt#gZImc%qdFtZ~VU9F9gT2R%sb_x)v+kc)%;K>Bfw(~a%+ud`-
0Z$(zK^+`~572yXQ<DWN^*3ddiU+o6D2^6BzzpWLGXWklK&*5@0H#SO|E&Gh{=SG7k&21raUz12qHT;?sU;BU52R%%2t()&)
o;?T&@$mDTJcber<w{n|B`O)&{V@jQ1-f&;8HDU0w^~um`RMORoz+}p1WAAC-J8q4neZ+mxuJqm`E)Hx`*DI+95y4c+)V5t)
yZqmU26kXla8C#fsoxY|JX<5HNO*@s#bHanax)?xkAz^zX5hW5c@9i|4Vd@N@hbJ2OErD!|00Y}Gi;lSj3M4;A78ub^NUS<K
LAy@DKpi5^A?buF~|&(<6<+$|C^0(J;3m*2s(d!UxBNc3P>gpRW_pZK^!Py$x^@v!1-@hf#wDET}Jro0B-+A9m8Y=s{}6_j2
v4zi6e4=Bp?3x|XAFEPI4B1lKHF_K*fuVZn9^c>vL!38gyjYci6saC)A8g-Wimv$&-4wuc5WfM|1InX=t(?uVwFEAwtqgW(J
5D=`~Ed3PgAfQm$@L+p|X3@`@1fu&`TV@c!)5Wtv`j`Q0VM$dky$`%*OR571JN&Ba?A%9BVLXJc+fHt!@L3JAnPy;MvQ%D-C
2y17id(0>)Nh~9P6YgO+A9tDBEFcuCD_)tR6<IA{-U0+CO#XpLL0?Py-~~w;Zzw4qM~bwR!g`T)we#Lkmj$q#0rMK9J9uD#b
OLH{t`Ye#t2=FvG5034srFf5Z5c_|NBeryc)i0*^%fK{ZWcBqUOE_#q20s>mDnAaI&yiJB^2lVdtrxBVG+9<G}`EtQ-L*+)_
I&YbN|^m4(w-&azd;!&<FGw;S~G2*r45k45D443p*K2@72#h(+A}2+~njrr@jvql$<ns;mb=5z-XdvLDR@HpJLAyAwm%)k1M
l+BHy)c$Vj{JoXho_twS@$Y9(<ai_<vhegwfL(`se42I&;PDJiG!_<C2X<l9sINv|28FS4Ctp^h9%H<EK6E1#=HikV9cn)*p
8GzkNv0A0qp4KEdmTdjidgNU;9ETW3x}@-Gz+B|FZ@W5rIjtGNQx4)|g({;V*;!>jwOWno$@TUf4De@UQjz{Z#46HXhbKpG0
Q9pB01r0+vRb8$fc}=drbcmL1Zs0Y_ouW+&@V)`%ON%8Oc=5Jms~#6nCbO}ZA9K7C)y$jDm{t6+KSl9FU?F|_)HjhVd_c77a
Zdac<trk91tJlil6Bg-Wd7<rWn7&H)Ik(ulR&G9-uLTVj9uy?FRJ9==dl2)hgZ4LJEc*`l8)6A0NzEwo;yGuxYnZeLRGJTaB
Lcre=sX`$pW}3WW#+w%u*;Ne()sv=4mLE4c;GLnznUFX>B6oEW3c;`b*{vRkRWQGv8K(%tncq5>TGMqa#$lRGeK=Fe?fM(*x
KrB`0dmp%x=cpAyd#eY3(vG{Li>%v+t;n!;Q-%dq*%)aBdUC<Ly&e_5eyLO}AY+X21au;+)rHp(bZ^crg+F8jjd8m32p<awb
A3XO723F_j7JU%IMSz|=47!ZyMgr+15buLj<P)nXc$E5}TDH;TFQWlrYwa8DAy>wO7@AGxzT3(av<hZ`SbZYtcuHHWddooN5
Vccqus}vB_q-iaSaKW%q<q@r$(ZnFddLizl7tFlMmvaeoby=Y`>D|T67WA2Vwv`aK)i#Ic#3T<(`+*)<VB3x2ACoS|CS^Smn
m(EE-_~Aw2zg|@uC7|xe8yVhsPLAI2K$2tqLx3x+OzJD@03A><!!DZUYcGnsiW|pU}7ncfFc8Rye{KkpN{7!ywM8*Qq*C398
OxuI75WS{UXk#NnyP#0?>Ecf(i=K<4V{(Vx+{!Ef`}jC-B#wuG*DDrg`axqvtBxFfpt>T>tg*aHkf>tV}6HKCabe1v6We;0`
u)9k&M<FO5Y0pf`H%>Ir!4U-iy4<7dg&v|ek%z%Y-fIE#}C^~M_(at=D;QaN#H&#)+avzg*1YU^RqgrP#EWM?9>lGLMTs-Om
7#!-pH)10yyp4%Uz@kPj6v6-qFc5#t>^+4eos1+$(~pH(22{j#vh1~(a-<3|Yb^&xV6U&RK6xVoA1Eos(iKsaL7^<5ti2G`?
P{R5>H=+o{wA<ElwalDKX(p+dPb0#n$7z6yTmM`jifM1U<~K?EN#Ga^x+TBIC^I!n!$YfU1-7?^&h3IXEf-KCWA-COu$Fo@1
;IC;&))vHK?wxbw0-H2o-1+dKo*!huS&L$ca7sC-kK9P{Az_R5yQ3Ap<I-Mbq`$8nUTDZ~QE-dj$_4W`ue`QPuk_`|F-P$~g
v8x#KJF?dF)dho?wY<(2M#e=-@_&={1a$5o*X9NnsV&#6jojvp&fIb5&>v-Mn_14FI^9q*4Zj_?E?>=aL`r`QkrKnL*S$t?e
Z2+N^AK#gPY4zjo(SRO01JPcb!m#XKLmDG@}y%yCZVIo`glCc0C0o-UIrvl?NI`*#m<SR7%OMr-Yto!#-n#Mumdmnw;#!Dq4
&-5mr?e&#^Ye(XOL+`;#a!$uqRPFz>j1F}~SPaFr@bN#HD`&uK?$q%91X}j!fJPjVAL9Nh*!u7eMoN_n8Czq#)%t|d&_3v}V
c}@>N_9XCQ7Ma?csLG3C{9F2nkGV_4^pZ_&D1*9liD015FwGMzpg0&?<)N{#9R<W^<8$g&at8Aedzf%=W0O#5&UDHd1(XF0g
DW%B0P(MuG$gb#fiyx$Ydduty5RY$qCV~IWbaX3U>O2eWPABUL)?1qw27r_-Slq_lFt)!Zmq19F-oZHWx0c7b1_Mkh0bQ9Y_
Ia9!J6I<Geb0ZS__ausCHj<RpS!n}0G8s_$Uy7LX(MX=o=-n|3j>RH?CzMu3!<dRk{bMGcam<mD}IvH~dlwYG0ni0*M*;Qpu
L0vmSnd%P=-?DeGF^|8Q}fJUWwB99%7KrZl5C=g?T2fZD6;!>gS-8<#<W1;We`<_4$VmZ|%?h7UEu*AJa1A=cjzn9xb+sEzG
Xap*-h?S95i-@@XcDW=1t5vVK0SDOMvg9Z9Yy{7t!Cn5ydbhiM3N{`V5Zfo}NyShmY}L~Ed7aMJC}z6SNHDAgbBp!33O0hqH
VsD@FjrFpQBY<(%>0o!7ALMa&D9q!Z2qbXg3Z8y0@oB&6Mn!g@(0@VMZ~~4J%O$*`9rC~fH8<E*e2w?%!Ru>?`^RT$6PuP^B
6Bp?f-z)oh7*GO{7vf*MBlcn*)zPjbow~1>79vbU$!}u3YWmU)sf<iN#EEt7I+n;}cpa_kZJgBWYfDya}_o|AEtux(w7>D*v
=&JaK~-sv7HSOD$6%gXh1pHTz28!=KKu+UVG|$1oCh?Z6K-BdnBTwQILf<CQ!&_;jd;g&7mQEs1D~)`u>D%Ak=Q*U-=%<`i2
U+bE?Bu?=WH0KM1_%&NunXpCFgIJ+1?krH*n21T#|X%z>k)do$*X5@~xkJhpo)-ZlI)Y|_;j9>=;d|$zkuz?njD&bc={&-WH
c7Z5$_Z`OOQRASxB8m6~*B2WppnP_DHy{Ju77R>8@z$-?Udh*$V7ti+u=-a1R|!9bvaXahc5?Mm4#ijbB>s@!SrJQaMdjzPA
&6pT?jv(yCWk0ODNu4!1hP||%1#lFBAd_mv%rc+wiUtOlD8)=Wg<Sxu|hYCMuCd_Bw>vHtWSjS`;$cyN_rMI5~RYd1iA1*-k
0J@C_=$lHzcgWOwPSDUHr@_j*`J7)R81q!+GY&lX#aOFa+0)Ov!Q)oR+NApO1$MpW4Gw8MIG&$bW6Xz^4x>dC<v4b`cL_F%G
~yslBQI^L0Q$;Q;iRHN0|bCtQp%he(f3U|OR87(K)6%@&bR$G9-&W>*CKcUW<pt;)A=NyXVwwRDa>-halMV4q|m*}07=y>e4
tZyQs6<SY3;ZM{`1Rn|jWxg>IZ>#fB98jCzX#Z7C>FXW5CKub?B+=<tQ72~SeO=2GpZ{JF<eR<`(ZcPV0lgVt1_MA4;CwF(W
ovF-q@wFz&*^yse5bFaBC9`f2b0DM797o2ULa6UD@`+NZ<gIq0i1bX<5;+wyk_t;GOFQ|b&={mkiH@R3G<Xn;gcb(0<#`?~(
Q!O_)+AhCp)<;iEct-EBSKptV#6nbH);nhiuM5G`hF6OBj1;@;zOt7#P=&|;iS)C&&-BP%w^SC7IwEn+*1LaT_KmW(gQvX;x
w{uo>N#8XHW6muH3@Aam`+ZOql>Iy_~-l7lN%W@qRhGQoN@RdA{P5dxCod+<`-t$}!!Eo?y9QroP@d+L=W`sCM^J<w3i&L$$
M-!Kzgs5Q^w2rTfP<!D0iYQR!UYp80&I-Iotn7ia$YW#{br^U;O>;TAaZ=<<~Ax&vqU_Tw2{dH3n)=7z?gFu2VcReFDR?VsJ
89DRafXV;zccjqTZowFOiRjc{H*T-kqmp7fW^GpBu;_Br08{gfB4<FBgrEk`7;$ompe;=9Fzqvg|HurJI-|t+Xo$+JMzrMQa
oSiDr$<^nxYk1p)?9<iFdFTA|nSXlr?)>t+bLM|M>s+6o-1xWtQOCbHJG$xkoiA5wm2WSPuWm0-0WDV`CVqGH@%-XHerw-<e
|vO&dgJfAt-OhotFw17_;XnA>m$Q9j!rtaK;V<B%g*)H#f?vM@bT&+Rq&eo{+F}!_aET-`t0QV)AiK}6xQ7>;hXLtr<1Kmb1
zC61OzPQ59qGEdXphEi=_Nd*4QuN7g)^k9qxT1I~$Q6^NP#!91NN$#Jd*3<QN6d*5r<_Z5xfYp$$`PkW~mYHSeY5t(u*0iMk
e(Z^hiPu7QtJx(d@WvSrp5SlbFG5r=uz?T+z0<%Ju~3YTd9U{L?$rpiD5f8JE7@2JF)Zn~rLRFYz)`!?;@We^L6Ip#<qPaOT
j%NKv{#>JC=dUfK@Uzn%{e%h@l-H0L0BlgKbh?5RP(8;&tOdowHoP5A!?7;aq{_2;KND5mOC!l$Bc3rWK1WP*W2!6)wNq3Lq
$%Q)`&ag0aD_6#Ne`kL4VxJsbFylF0ATT>~mPK9otj30YXu5UrXKq|n_buu!7y5W~tvXpU4X~$+`~t;geq~~NrSDRF{kDtOF
1ye<Okn-mbMq>L{6^EQ`TCuvTk{{^YHFERn-YS;<)*s&`t_!CzXTgqc5W#1cPQLc|GaH|B%Jo~%%Z@rTlMO^I^UjGt5BzDys
0|i_ZT%?KvtcrFVO&I&%{>c!qt~;=7yJiGelDjgGag>g>#GMnZ^Eguy&S*>i=Q84xun#A8?yjomR9_N$5y1ZAzNEn%zI(n>w
}_n8y}JaS{bH`&bO93mp&ve-zN**@!KGz371bWF=m7->_P5^V#-}N-~;qX6J^x2vjLtFddbT-tJ(eqtl)CB>oWi%I9P{>Uey
It{Vu{bpzDH&MVgqn7vrLb3nD&?$DhB!S>7gCIx<?9{lLeflhww#j!!b7stq*F^V7aSw!5N$0^L6^Ny4oE{^Fq#!>o?qGzXg
cg6H=tsPe7v~7g`DEfmvQIYrUj=IgFqi(a9ZobW;^XhFDox)8Cm}1ViAEa?=C+1R6r<r31mQyvZ+U_<ii>jS$$Lpu>`P?$}^
AA`9^|kK};O=8s6Vyl@8sXgxP4-{G!r(ixDc|18l8-Fy_*kT#_08I#?!h@CJ;Aq$P>z^oW`uyb!O8qE%@um87?X#Z%J85ny`
Fi>m5OuHKG+3nrEtU`yTt;Fh&42Y+fs@rQG&urlwiY2lzv{Kud*W*533_3#e*n#!nW2c6)PP=(J^SfvYFz<eZLcT*PIPIH09
Z=8)sF*C&6)?!jTnB@Pi(~*IxTcDxtdTWha=k)5|}3GWmBtKD;fxMwOeZ+D`zh;wj}VJe*v8!o$gVoLw)N-w{R|;TUN82P52
Yenb)N=MGZ8$V>otRrjg(@04ysee7*Y3u-ur+}-@p^b5;M4iM4D(j602-Z76oaTdY4$TxVN8Ms^do0Bb-o)*GdDuuRAEXd^A
A3|d*o`R|9vq;L*IR^*s(;57@?D(hW;NEoD&HZ$Banw1#y3{`E$?Y+Cc*;N3&d;ybX?%AVVH77DJgoRbTv--Jcd}G{^iHe<I
i(NXXlL+Xv^|^!(|d~yQ_5=x$p9|T-6+O=0ey@nC@(iNDU}vGkc8Gc3w_$dketh(ot06-V(oNCGNG*Z*K-;10EM1$9$0E}T-
E-q5NB8Tobn-?siYtn$|qGs1;J8`i*#o_IcxKYNR07mUIghgn;U3(MW<1esB^oIl8SIP2I;Ry=r75sM;*z*;)nP{pG19>Q>F
1K;{_`4Nmcm{T!tt=<B7L$Ow>WmLORVjKa64=L@6CZ(UjP9z;;kvG})XJ#RquuWS~x-v^SkPp#z~=C(cwKif6cWhhFQFKBhh
1>Bo3>VF7CbmeB#FA~Q2-xn)OVF%yrJMFy+|lSP?3*%4S|H`&GD3$h$8j$`(#Em(%pEVUMi_8<7j5uRolMNjcyLJI)2D*8X$
Gz^P|kqR|?e0@5e$Jxo4d<Vy9KSs}T6pZ^}V7(lw!LKth@7LKcupHjLjh%nHj(DNVV7?{#^jM{`^Dx01!+vm529L>b-aS%+{
6X$Z(b-dHGstDqu}+XX74zT+I-uU3M;jzM;plHqc)W&@YoI%}L8@_h*?)I?d4dA%rXtiymx>u8tMI0v8jh&sBJMLqLP(_b<1
iY+)B$C{^W|6!ok@z46e(_+Js8;G`L?F_&nf-yKY(=O#VA12=U7={p0h#IwU0AX%qy5;$7qWUQzXNt*fElXdsQizOT$!UGaD
jvn4%aN&f+jPJ|e^Vn9B(4gZBNs%ssBYN|ec5tFjq?ByvxYO%hbO#+@B~H4GMElnc<G@4DW88x0gnaE~iJK@Sg=OghnfIayr
!7nwD)!IlA?UvJUg9T-KN))2u1ZMQ4%QiGSymg~7y`c(DQ*M<JNFfIg9`viC+$}A{eGRgE&wfgXoHx=ln`q-4&OrZPL7ptt_
_xG61Lk%3Eb996r=r%wficoc{2oYL~D&yopmGg>mp7mEONj4aC!B^)kv}JT$xK<Hsu_ux)MssD3Zn)ktx5OUSZV?$wMuy!r(
^--;J|(PskQ-hFpX88RR=1@AD!wyC%Utf(k8P^g&P<fjxPrH4(jOr<5dP3!IzIn=bbWr*Ir~RZ??R+mN0@O>ArGtL!ZzDm4?
h3(e*xHc98d
'''
raw=zlib.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==26966 and hashlib.sha256(raw).hexdigest()=='8272a48b24d0a4734399ccb698862fc186db579f2b29ccd3cbd2c28b2a50d0fa'
SOURCES={'bevel_all_spd.py': [20799, '0ea6d3d1dc1a0cba8d9ffe27204448ecfd35e1ef90e09f488026ab622874ca33'], 'verify_bevel_independent.py': [5598, '4b20769bb5d12b8eb58a60e5063b221cb5fcc579bf81f7b650f0c0d09f9502b2']}
root=Path(__file__).resolve().parent
sources=json.loads(raw);assert set(sources)==set(SOURCES)
for name,text in sources.items():
    data=text.encode();size,sha=SOURCES[name]
    assert len(data)==size and hashlib.sha256(data).hexdigest()==sha
    p=root/name
    if p.exists():assert p.read_bytes()==data
    p.write_bytes(data)
subprocess.run([sys.executable,'-S','bevel_all_spd.py',sys.argv[1]],cwd=root,check=True)
subprocess.run([sys.executable,'-S','verify_bevel_independent.py'],cwd=root,check=True)
data=(root/'bevel_all_spd.json').read_bytes()
assert len(data)==220670
assert hashlib.sha256(data).hexdigest()=='f4dd53a7634854909822623e71545910a4001f4e0bc3a9faf5ec29cb035e70a2'
print('BEVEL_ALL_METRICS_SELF_CONTAINED_COLD_RECOVERY_PASS')
```
