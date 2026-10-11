# minimum-0104

Historical AI scientific report · saved 2026-09-19 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# BEVEL_FOUR_SHAPE_AND_NONPARALLEL_ALL_SPD_U2_V1

## 1. Итог: два полных непрерывных запрета, без ограничения метрики

**Завершён собственно-центроидный all-SPD запрет четырёхпараметрического класса.** Для каждого

`0<t≤1/2, 1/2≤r≤2, 1<a≤3, 1<b≤5`

настоящий однородный многогранник `P(rt,t,a,b)` буквальной bevel-решётки имеет **не менее двух строгих неустойчивых вершин при каждой M>0**, с единственной сопряжённой метрикой `N=M⁻¹`. Условия S1, H0 или отсутствия дополнительных слабых равновесий не нужны. Все совместные аффинные образы включены.

**Дополнительно получен новый all-SPD запрет настоящей непараллельной геометрии.** Пусть `B=P(1/4,1/4,2,3)` в исходных координатах, а

`T_h(x,y,z)=(x,y,z)/(1+h y)`.

Для **всего** `−1/4≤h≤1/2` равномерно заполненный образ `T_h(B)`, оценённый относительно своего заново проинтегрированного объёмного COM, также имеет U≥2 при **каждой** SPD M. При h≠0 его две пятиугольные грани непараллельны: это не аффинный образ уже закрытого квадратного каркаса. Сохранены семь точных контролей этого класса, включая действительные **222weak000** при h=1/64 и h=1/8.

Важная исправленная граница данных: **реально приложенный полный compact.json содержит396 строк, а не548**. Его396 строк без изменения коэффициентов закрывают весь четырёхпараметрический прямоугольник. Совпавшие старые числа13 клеток,2973 применения и761088 блоков сами по себе не использовались как доказательство. В этой передаче находятся обе полные таблицы —396 и395 строк — вместе со всеми списками применения, исходниками и выполненной source-only recovery.

Это не полный запрет11-мерного пространства реализаций и не новый аттейнер110. **34≤C_min≤622 и все FULL/LOCAL/root registry-счётчики неизменны.**

## 2. Входная граница и исправления

Новый journal `research-journal(20260919-095440).md` прочитан целиком:320445 bytes, SHA-256 `5565dc8fd207bf5a6f5517d582f16101459718031be41375cbf697725d636363`,2329 отображаемых строк. Прочитаны весь буквальный parent и все пять приложенных рабочих файлов. Неизменённые ранее прочитанные источники сохранены в прежнем статусе.

Parent — `minimum-0100`, runtime SHA-256 `f8fa18403331d55fd0be6a1b09df47815dc790c642fd8f077670ddb75d67e468`, **BEVEL_REALIZATION_CHART_AND_FOUR_SHAPE_S2_CONE_V1**. Его11-параметрический chart и аналитический S2-конус — унаследованные результаты, не новые теоремы этой передачи. Его четырёхпараметрическое all-SPD вычисление прямо оставалось неподтверждённым. :contentReference[oaicite:0]{index=0}

До редактирования побайтно сохранены все пять входных файлов. Полный `compact.json` имеет23691 bytes и SHA-256 `223b1decdb52bb8a42e8986f3419007df3f8468d17ba6539a3198c8e47492fb0`. В нём396 строк; встроенная копия CERT в пришедшем builder совпадает с ним по всем коэффициентам, клеткам и назначениям. Однако builder содержит ошибочный `assert len(rows)==548`. Никаких дополнительных152 строк в пакете не обнаружено; они не угадывались и для доказательства не требуются. Это конфликт прежнего рабочего счётчика с буквальными данными, а не конфликт уже принятой геометрической теоремы. :contentReference[oaicite:1]{index=1}

Был обнаружен и второй исполнимый дефект: отрицательный контроль, названный «parent row6», содержал не ту строку и ложный `K[0]==−81`. Исправленный контроль использует действительно шестую строку буквального старого all-SPD source; точная отрицательная форма приведена в разделе6. Ни396 строк основного сертификата, ни13 клеток, ни2973 назначения не изменялись.

В окончательном builder устранено дублирование таблицы: он читает **тот же буквальный compact.json**, полностью встроенный в recovery. Независимый checker дополнительно проверяет истинный граф, порядок стрелок, число строк, степени полиномов и проектный контроль. Старый locator освобождён от абсолютного импорта: его150 исходных seed-строк встроены буквально, равенство генерируемого поля стрелок проверено. Утилита `recover_incoming.py` восстанавливает **все пять исходных рабочих файлов побайтно**, включая их ошибочные asserts; это выполнено и проверено по исходным хешам. Исполнение этих ошибочных восстановленных файлов не является частью доказательства.

## 3. Настоящая геометрия всего четырёхпараметрического класса

### 3.1. Вершины, грани и направления нормалей

Положим s=rt. Сохраняются постоянные метки:

```
0=(-1,-1,-1+t)   1=(-1,-1,1)   2=(-1,-1+rt,-1)
3=(-1,1,-1)      4=(-1,1,1)
5=(1,-1,-1+t)    6=(1,-1,1)    7=(1,-1+rt,-1)
8=(1,1,-1)      9=(1,a,b).
```

Полные наружные максимальные циклы:

```
F0=(0,1,4,3,2)  F1=(1,9,4)  F2=(3,4,9)
F3=(0,5,6,1)    F4=(1,6,9)  F5=(2,3,8,7)
F6=(3,9,8)      F7=(5,7,8,9,6)  F8=(0,2,7,5).
```

Все истинные рёбра, в лексикографическом порядке:

```
(0,1),(0,2),(0,5),(1,4),(1,6),(1,9),(2,3),(2,7),(3,4),
(3,8),(3,9),(4,9),(5,6),(5,7),(6,9),(7,8),(8,9).
```

Поддержки `A_i·x≤H_i`, в порядке0…8:

```
A0=(-1,0,0),             H0=1
A1=(1-b,0,2),            H1=b+1
A2=(1-a,2,0),            H2=a+1
A3=(0,-1,0),             H3=1
A4=(0,1-b,a+1),          H4=a+b
A5=(0,0,-1),             H5=1
A6=(0,b+1,1-a),          H6=a+b
A7=(1,0,0),              H7=1
A8=(0,-1,-r),            H8=1+r-rt.
```

Это реальные максимальные грани на всём заявленном диапазоне. Пять направлений нормалей меняются с r,a,b. При t>0, a,b>1 все56 неинцидентных vertex/facet-slacks строго положительны; все34 положительных множителя истинных рёбер и16 настоящих ориентированных конусных детерминантов положительны. Код доказывает эти знаки на всём параметрическом прямоугольнике: выносит только положительные физические факторы t,a−1,b−1, затем проверяет полные строго положительные коэффициенты Бернштейна остатка. Это не проверка конечного набора образцов.

Каждая перечисленная сторона есть пересечение двух настоящих поддержек, с ровно двумя общими вершинами. Циклы образуют замкнутую связную поверхность; каждое ребро принадлежит ровно двум граням. Следовательно дополнительные грани отсутствуют. Имеются настоящие V10/E17/F9 с размерами граней5,3,3,4,3,4,3,5,4. Интеграционные диагонали в рёберный список не включаются.

Границы t=1/2,r=1/2,r=2,a=3,b=5 включены. Значения t=0 или a=1 или b=1 используются только как алгебраические границы Bernstein-box: там меняется решётка, и они не объявляются дополнительными weak-пакетами E17.

### 3.2. Собственная равномерная масса

Пусть `D=3Vol`. Точные интегралы дают

```
D=4a+4b+16−3rt²,
m=(a+b−2,
   a²+ab+a−r²t³+3rt²−3,
   ab+b²+b−rt³+3rt²−3),
g=m/D.
```

Геометрическое доказательство: к кубу добавлены две настоящие пирамиды над видимыми квадратами y=1,z=1, объёмами4(a−1)/3,4(b−1)/3 и центроидами(1,a+3,b)/4,(1,a,b+3)/4. Затем удалена настоящая призма объёма rt² со средним(0,−1+rt/3,−1+t/3). Это вычитание равномерных объёмных интегралов, не свободная completion.

Независимо проверены полиномиальные тождества на16 треугольниках истинной границы:

`Σ det(v_i,v_j,v_k)=2D`,

`Σ det(v_i,v_j,v_k)(v_i+v_j+v_k)=8m`.

Первый builder раскрывает их в целочисленном полиномиальном кольце. Второй checker проверяет их на5⁴ рациональных узлах при доказанной мультистепени≤(4,4,4,4). Это полная проверка тождеств; узлы вне физической области не используются как примеры тел. Положительность самих физических конусов доказана отдельно внутри нужной области.

## 4. Полное устранение каждой SPD-метрики и каждого U1-корня

### 4.1. Настоящие слабые деревья

В координатах относительно вычисленного g положим `x_i=v_i−g` и `d_ij=x_iᵀM(x_j−x_i)`. Если вершина не строго неустойчива, существует настоящий сосед с d_ij≥0. При любом таком выходе

`|x_j|_M²−|x_i|_M²=2d_ij+|x_j−x_i|_M²>0`.

Поэтому выбранные слабые выходы не цикличны, включая стены d=0. Глобальный максимум нормы всегда даёт строгую U-вершину, в том числе при нескольких равных максимумах. Значит U1 породило бы одно из настоящих корневых деревьев графа.

Полное перечисление всех `C(17,9)=24310` подмножеств даёт5440 остовных деревьев; лапласов кофактор совпадает с5440. Каждый из10 корней даёт единственную ориентацию: всего54400 наборов слабых выходов. Независимое перечисление530712 функций выбора соседей после отбрасывания циклов даёт буквально те же54400 наборов.

### 4.2. Одно полиномиальное поле, одна настоящая масса, одна M

Порядок34 стрелок — по исходной вершине, затем по конечной. Запишем `v_j−v_i=l_ij e_ij`, l_ij>0. Используется ровно такое нормирование: у рёбер с вершиной9 берётся полный вектор разности; у(0,2),(5,7) снимается множитель t, оставляя направление(0,r,−1) или противоположное; у остальных снимается положительная длина, оставляя знаковую координатную единицу.

Положим

`W_i=Dv_i−m=D x_i`,

`B_ij=W_i e_ijᵀ+e_ij W_iᵀ`.

Каждая запись B имеет степень≤3 по каждому из t,r,a,b. Точное механическое равенство:

`tr(MB_ij)=2D d_ij/l_ij`.

Для каждой переданной строки R с положительными целыми λ определено

`K_R=−Σ_(ij∈R) λ_ij B_ij`.

Если все её стрелки слабые, tr(MK_R)≤0. Но K_R≻0 несовместимо с этим при **любой** M≻0. Таким образом, не оптимизируются разные метрики у разных строк или граней; весь SPD-конус устраняется одним точным трассовым противоречием.

### 4.3. Все13 замкнутых клеток и все396 строк

Исходный закрытый box равен `[0,1/2]×[1/2,2]×[1,3]×[1,5]`. Каждая пара цифр в ключе обозначает ось0…3 и левую/правую половину её текущего интервала. Полный набор листьев:

```
001020, 00102130, 00102131,
001120, 00112130, 00112131,
011020, 01102130, 01102131,
01112030, 01112031, 01112130, 01112131.
```

Он проверен как полное бинарное разбиение, с обеими закрытыми половинами на каждом шаге. Поэтому все внутренние стенки, рёбра клеток и вершины включены. Числа назначенных строк в этом порядке:

`(256,186,231,256,183,235,275,193,235,207,260,196,260)`.

Каждая строка имеет полный тензорный Bernstein-набор256 симметричных3×3 матриц. Для степени3 преобразование монома xʲ на[u,v] имеет коэффициенты

`T_ij=Σ_(k=0…min(i,j)) C(j,k)u^(j−k)(v−u)^k C(i,k)/C(3,k)`.

Четыре таких преобразования применяются тензорно к одному и тому же K_R. После положительной очистки знаменателей **все761088 матриц PD**, все2283264 ведущих минора положительны. Положительность K_R на всей клетке следует из неотрицательности Bernstein-базиса и суммы его весов1. Минимальный ведущий минор после примитивной целочисленной нормировки равен1; это не заявляется метрическим запасом в произвольных единицах.

В каждой клетке **каждое** из54400 корневых деревьев содержит хотя бы одну её сертифицированную строку. Выполнены все707200 проверок «клетка × дерево». Значит U1 невозможно на всём физическом прямоугольнике. Получено U≥2.

Полные396 строк имеют1607 членов, λ от1до56; распределение длин:138×3,140×4,85×5,25×6,6×7,2×8. Ни одна строка, клетка или список применения не сокращены в recovery.

Независимый checker восстанавливает полиномиальные стрелки по4⁴ значениям при доказанной степени≤3; строит клеточные Bernstein-матрицы **de Casteljau-подразбиением**, а не сдвигом степеней builder; проверяет их рациональными дополнениями Шура и сравнивает полные канонические потоки коэффициентов. Деревья он перечисляет через функции родителей, а не рёберные подмножества.

**Симметричное следствие.** Перестановка координат y↔z и явная перестановка меток `(2,3,0,1,4,7,8,5,6,9)` дают также полный all-SPD запрет области `0<s≤1/2,1/2≤t/s≤2,1<a≤5,1<b≤3`. Это перенос той же теоремы, не дополнительный registry-count.

## 5. Новый непараллельный сектор, с заново вычисленным COM

### 5.1. Физическая область и аффинная несводимость

Для фиксированного B=P(1/4,1/4,2,3) все вершины буквально получаются из списка раздела3. T_h действует в этих исходных, ещё не центрированных координатах. Полная область положительных знаменателей — `−1/2<h<1`; новый сертификат покрывает **закрытый** сектор `−1/4≤h≤1/2`.

Здесь `1+h y≥1/2` на всём B. Поэтому T_h — невырожденное проективное отображение ограниченного выпуклого тела, сохраняющее всю решётку и метки. Если исходная поддержка A_i·x≤H_i, новая равна

`(A_i+H_i h e_y)·x≤H_i`.

В частности, нормали F0,F7 равны(-1,h,0),(1,h,0); их векторное произведение(0,0,−2h). При h≠0 никакой аффинный образ параллельного четырёхпараметрического каркаса не даёт это тело.

Разные h также дают разные помеченные аффинные формы. Единственная нормировка четырёх parent-реперных вершин имеет линейную часть

```
L_h=((1-h, -h(1-h), 0),
     (0, 1-h², 0),
     (0, h(1+h), 1+h))
```

и сдвиг(-h,h,−h). В ней `x8=(1−3h)/(1+h)`, строго монотонный по h. Таким образом, это реальное направление вне параллельного слоя11-мерного chart, не перенумерованная старая форма.

### 5.2. Настоящая масса и полиномиальная очистка

Обозначим исходные вершины через v_i, `l_i(h)=1+h(v_i)_y`, `Y_i=v_i/l_i`. Для16 настоящих ориентированных треугольников τ=(i,j,k) положим `d_τ=det(v_i,v_j,v_k)>0` и

```
S(h)=Στ dτ/(li lj lk),
A(h)=Στ [dτ/(li lj lk)](vi/li+vj/lj+vk/lk).
```

Тогда **истинные** `Vol(T_hB)=S(h)/6`, `g(h)=A(h)/(4S(h))`. Это интегрирование равномерно заполненного нового тела, а не T_h(g(0)).

Положительный очиститель

`C(h)=(1−h)^4(1−3h/4)^3(1+h)^3(1+2h)^2`

даёт полиномиальные векторы

`W_i(h)=C(h)[4S(h)Y_i(h)−A(h)]`.

Если `v_j−v_i=s_ij e_ij(0)` с положительным фиксированным s_ij, используем истинное проектное направление

`e_ij(h)=[l_i v_j−l_j v_i]/s_ij`.

Положительный множитель нового ребра равен `s_ij/(l_i l_j)`. Матрицы `B_ij=W_i e_ijᵀ+e_ij W_iᵀ` после точного сокращения имеют степень≤8, и

`tr(MB_ij)=8 C(h) S(h) l_i l_j d_ij/s_ij`.

Все множители справа, кроме механического d_ij, положительны. Таким образом, применяется тот же настоящий слабый-tree аргумент с **новой собственной массой**, а не со старым reference core.

### 5.3. Полное двухклеточное покрытие

Новая literal-таблица содержит395 строк,1490 положительных целых членов, λ от1до150.238 строк применяются на `[-1/4,1/8]`,199 на `[1/8,1/2]`;437 применений в сумме. Полные9 Bernstein-матриц степени8 каждого применения дают **3933 PD-блока,11799 положительных миноров**. Все54400 корневых деревьев покрыты на каждом интервале:108800 проверок.

Удостоверена вся объединённая закрытая область, включая h=1/8 и оба внешних конца. h=0 безвреден: там пятиугольники становятся параллельными, но решётка и положительные массы не вырождаются. Следовательно U≥2 для каждой формы и каждой SPD M в этом секторе.

Новый независимый checker не импортирует ни один builder. До сокращения общий знаменатель `L=Π_(c∈{-1,-3/4,1,2})(1+ch)^4` имеет степень16; после очистки четыре линейных знаменателя каждого момента оставляют числитель стрелки степени≤13. Удалённый положительный фактор равен `(1−3h/4)(1+h)(1+2h)^2`.14 различных точных значений доказывают соответствующие **полиномиальные тождества**, а не положительность по выборке. Затем checker восстанавливает Bernstein-матрицы прямой интерполяцией настоящих физических формул, проверяет Schur-положительность и независимо перечисляет все функции родителей. Объёмы, центры и ковариации семи контролей дополнительно проверены отдельным положительным веером из вершины9.

## 6. Действительные контроли и сохранённые отрицательные результаты

Во всех следующих контролях интегрируются реальные площадные C_i,T_i, объёмная Σ и34 положительных детерминантных контактных веса. Проверены `T_iq_i=C_i`, `Σd_iC_i=0`, `Σd_iT_i=5Σ`, контактные балансы, все17 настоящих векторных равенств для рёберных подошв и MN=I. Обязательная поправка `Σμvvᵀ−d_iT_i=3Στd_iτ Sτ` вычислена, не отброшена. Все указанные контроли имеют68 ненулевых примитивов и weak000.

Общая рациональная метрика

`G=((3,1,0),(1,2,1),(0,1,2))`

имеет ведущие миноры3,5,7. Второй точный выбор, обозначенный H, задаётся

```
u=(1,2,-1), v=(7,-4,-1), w=(1,1,3), L=128,
H=uuᵀ/(36L²)+vvᵀ/(4356L)+wwᵀ/121,
H⁻¹=L²uuᵀ+Lvvᵀ+wwᵀ.
```

Это один M=G или H и его настоящий N, не две независимо заданные механики.

**Четырёхпараметрические контроли**, параметры в порядке(t,r,a,b):

| Параметры | M | Vol | Собственный COM | strictSUH |
|---|---|---|---|---|
|(1/2,2,3,5)|G|31/2|(4/31,50/93,173/186)|446|
|(1/3,3/2,5/2,4)|H|83/6|(9/83,97/249,494/747)|222|
|(1/8,1/2,3/2,5/4)|G|1151/128|(32/1151,5423/55248,1751/27624)|6/7/11|
|та же геометрия|H|1151/128|тот же настоящий COM|222|

Они не отождествляются с FinchVol35, H0Vol4/3 или проективным H0-контролем6/6/10. Две222 конструкции показывают достигаемость U2 на конкретных новых формах, не на всех параметрах автоматически.

**Непараллельные контроли:** при M=G значения h=−1/4,1/8,1/2 дают соответственно345,8/6/12,569; при M=H значения h=−1/4,1/2 дают334,334. Дополнительно h=1/64 и h=1/8 при H дают222. Все их полные рациональные геометрии, метрики, моменты и feature-lists реконструируются.

Особенно простой новый собственный222-контроль имеет h=1/8, M=H:

```
Vol=188254208/16689645,
g=(649252/12409335, -20452856/839698335, 3181865287/10076380020),
S={F3,F6}, U={2,9}, Hedges={(3,4),(5,6)}, weak000.
```

Его координаты — буквально `v_i/(1+(v_i)_y/8)` для десяти исходных v_i из B; N=H⁻¹ задан выше. Это конечный рациональный аффинный chart настоящего тела. Евклидова реализация получается одним линейным B с BᵀB=H после вычитания указанного g.

**Неверный перенос COM действительно опровергается геометрией.** У этого h=1/8 образ старого центра равен `(1536,4696,7768)/18923`, тогда как настоящая y-компонента нового COM отрицательна. Не только точное значение, но и знак компоненты не сохраняется при таком переносе. Прежний отдельный контроль h=1/10, M=G имеет Vol4087415000/362274363, собственный8/6/12weak000; теперь он также лежит внутри доказанного непараллельного сектора.

**Старая строка не продолжается автоматически.** Для настоящего углового параметра(t,r,a,b)=(1/2,2,3,5) буквальная строка6 старого all-SPD source, `[(0,3),(22,1),(26,2)]` в объявленном новом нормировании стрелок, даёт

```
K=((162,-119,-184),
   (-119,572,975/2),
   (-184,975/2,373)),
(0,-1,1)ᵀK(0,-1,1)=−30.
```

Это граница именно переноса данных коэффициентов, не контрпример U≥2: новую настоящую форму закрывает новая полная396-строчная таблица.

**Закрыта прежняя исполнимая граница аналитического S2-parent.** Его буквально приведённый, ранее не исполнявшийся `bevel_chart_sector.py` теперь извлечён без изменения и выполнен. Два контрольных случая дали435weak000 и424weak000. Они относятся к более широкому аналитическому наклонному конусу; их s=t=1 или s/t=64 лежат вне нового all-SPD box. Эти исполнения не распространяют all-SPD теорему на их остальные метрики.

Ни усечённый T_y, ни независимые129 веса в доказательство не подставлялись: запрет получен непосредственно из U1. Новые129-весовые аудиты здесь не заявляются.

## 7. Что осталось в11-параметрическом пространстве

Унаследованный chart фиксирует `v1=(-1,-1,1),v3=(-1,1,-1),v4=(-1,1,1),v6=(1,-1,1)`, свободно выбирает v0,v2 в x=−1, v8,v9 в R³ и η; затем

```
Π3=plane(v0,v1,v6), Π5=plane(v2,v3,v8), Π7=plane(v6,v8,v9),
R:r·x=d=plane(v0,v2,v6), Π8:r·x-d+η(x+1)=0,
v5=Π3∩Π7∩Π8, v7=Π5∩Π7∩Π8.
```

Полные строгие опорные условия девяти циклов задают настоящую область. Этот chart остаётся11-мерным; доказанные сейчас четыре параметра и отдельное непараллельное направление не исчерпывают его. :contentReference[oaicite:2]{index=2}

Открыты остальные формы квадратного каркаса вне двух симметричных all-SPD областей, большинство других параллельных реализаций и общие непараллельные пятиугольники. Для отдельного T_h(B) не закрыты `−1/2<h<−1/4` и `1/2<h<1`; это действительные геометрические остатки, не остаток больших κ внутри уже доказанного сектора. Метрического остатка у форм внутри обоих новых сертификатов нет.

Геометрически две грани, вместе содержащие все вершины, можно сделать параллельными проективно: сумма их положительных поддерживающих slack-функций нигде не обращается в0 на теле. Но такое спрямление не переносит собственную равномерную массу или постоянную физическую метрику. Вычисленный отрицательный знак COM после T_h показывает, почему заменить этот остаток прежней параллельной теоремой нельзя. Полезное продолжение — реальные determinant-моменты и совместные метрические поля в остальных направлениях chart, а не новый формальный спектр Lambda.

**34≤C_min≤622 неизменно.** Ни нового proper110, ни V≥11/F≥10/E≥18, ни полного запрета данной решётки не получено.54400,707200 и108800 — собственные объекты этих сертификатов, не вычеты из FULL/LOCAL. :contentReference[oaicite:3]{index=3}

## 8. Полная recovery, фактическое исполнение и численные локаторы

Ниже source-only капсула из **14 полных payloads:10 Python-файлов и4 JSON-файлов**. Она содержит обе полные таблицы, все клетки/списки применения, оба builders, оба независимых checkers, исходный аналитический аудитор, локаторы, minimizers и весь замороженный проектный поисковый checkpoint861 строк. Исторические входные пять файлов восстанавливаются побайтно отдельной включённой утилитой. Нет отсутствующего coefficient-файла, archive-ID, seed или абсолютного импорта в точной recovery.

Проверенная exact-среда: **CPython3.13.5, только стандартная библиотека**, assertions enabled. В новом пустом каталоге находилась только нижеследующая капсула; её `build` и `check` исполнены полностью, все три JSON и весь stdout совпали побайтно. Одна первоначальная объединённая длинная команда была остановлена лимитом исполнения после завершённого build; это не было зачтено как check. Затем отдельный полный check успешно выполнен. Окончательная14-файловая капсула прошла собственные отдельные cold build/check. Proof-assistant или внешнее рецензирование не заявляются.

Сохранить как `recover_bevel_shapes_v2.py`, UTF-8/LF с конечным LF:

```
python -S recover_bevel_shapes_v2.py sources
python -S recover_bevel_shapes_v2.py build
python -S recover_bevel_shapes_v2.py check
```

Последний маркер:

`BEVEL_FOUR_SHAPE_AND_NONPARALLEL_ALL_SPD_DURABLE_RECOVERY_PASS`.

Существенные промежуточные маркеры:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


Все individual source-pins находятся в исполняемом FILES-manifest самой капсулы. Главные pins:

| Объект | Bytes | SHA-256 |
|---|---:|---|
|recover_bevel_shapes_v2.py|39488|7304ea9a7b5753c790d959aa4d70e151b2a06549d80ec83feb4ce98d305bb540|
|полный decoded payload|159583|500bf3b2efa31f3e4a3910e36344879a08c8eb97fb4219f6caacebf100ed1a2d|
|compact.json, неизменённые396 строк|23691|223b1decdb52bb8a42e8986f3419007df3f8468d17ba6539a3198c8e47492fb0|
|projective_compact.json,395 строк|12712|5a2c714980ea8176daf8fc337bb20789e314b3321b8c1ef5b71a6e470921d8b0|
|bevel_shapes.json|144340|8839126439eca33d25e1441ee673726759bdcfee7efab55b2b7607b62569a70a|
|projective_pencil.json|154203|f98b10fcd389c804176b45630ccce71f5a9fc3ece286aa9a9c2f5fc42618cbf1|
|bevel_chart_sector.json|18825|e4963d4ec0f7e9bfd9166e7edf5789c20b3b62483dd27764a4cb9e1685709bc1|
|полный cold stdout build=check|2707|d64eb6bc7d9a4d96dfacf19c59800d82bb5be9f5047ebabf1adf1c13a671d686|

Матрицы не оставлены за хешами: их полные источники, полиномы и множители восстанавливают каждый коэффициент. Для буквального экспорта **всех** матриц выполнены и доступны команды

```
python -S bevel_shapes.py dump
python -S projective_certificate.py dump
```

Они дают `all_matrix_coefficients.txt`,34707053 bytes,SHA-256 `b679adeb90452fe47cd489ce3aa8c204f1175f1f3e1d2c0b69ebff140091bcf8`, и `projective_matrix_coefficients.txt`,336605 bytes,SHA-256 `37d9f4816eefecea8bbf26a05b024784bbfb48123fecccc1d1448f86a7438413`. Каждая строка:cell,row,coefficient-index и шесть симметричных примитивных целых записей. Полные потоки покрытия деревьев также вычисляются обоими checkers; их per-cell pins находятся в отчётах, а не заменяют сами циклы проверки.

**Локаторы — отдельный evidence-tier.** Необязательная numerical-среда NumPy2.3.5,SciPy1.17.0,SymPy1.14.0, по одному BLAS/OMP потоку, без RNG. `discover.py` и `minimize.py` сохраняют полный старый eigenvector-cut/HiGHS метод; весь старый поиск не переисполнялся, и396 строк не создавались заново из548-счётчика. Его символическое поле проверено на точное совпадение с builder.

Новый поиск действительно исполнен и затем повторён из cold recovery:

```
python projective_probe.py -1/4 1/2 4
python prune_projective.py
```

Полученный checkpoint861 строк совпал побайтно с полным `projective_progress_frozen.json`:51705 bytes,SHA-256 `76191b4710842962daa5848d16271bd2353245d07c3ca14fb84dea529d0df256`. Детерминированное сокращение вновь дало395 строк и437 применений с указанным pin. Все maxiter, границы, rounding-scales и входные seeds находятся в исходниках. Неудача поиска одной общей строки или клетки не считалась доказательством геометрической осуществимости; принятие каждого используемого блока производится только exact-checkers.

Удобные дополнительные копии: [recovery](sandbox:/mnt/data/bevel_shapes_completed/recover_bevel_shapes_v2.py), [буквальная396-строчная таблица](sandbox:/mnt/data/bevel_shapes_completed/compact.json), [395-строчная непараллельная таблица](sandbox:/mnt/data/bevel_shapes_completed/projective_compact.json), [четырёхпараметрический отчёт](sandbox:/mnt/data/bevel_shapes_completed/bevel_shapes.json), [непараллельный отчёт](sandbox:/mnt/data/bevel_shapes_completed/projective_pencil.json). Следующий полный источник не зависит от этих ссылок.

```python
"""Complete four-shape and nonparallel-pencil ALL_SPD_U2 recovery.
CPython3.13.5 standard library; optional locator requires numpy2.3.5,
scipy1.17.0,sympy1.14.0 and is not needed for exact build/check.
python -S recover_bevel_shapes_v2.py sources|build|check
"""
from pathlib import Path
import base64,hashlib,json,lzma,subprocess,sys
assert __debug__, 'Assertions must be enabled'
if sys.argv[1:] not in (['sources'],['build'],['check']):raise SystemExit('Use sources|build|check')
DATA=r'''
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;%{DWKwSVmh=@j%c0~2!8f<CmPAlMXl$^2buuGS5S^G!k#c<*?pW>pt_s2PJzn_Mp>
3xpul9eHek(wAMl>)cWUf-
+RO!TXe=Ksv(47wDGiXLJPX1db1Gz&CcIx5sz6A2=aCJ^QY=lxoK3A7p`l95Q8EP!G(d#bYOmENfIet;m8JX}D@4ucycUMz7
2Uz~JcWKfU?!g)%O;M5yQO;*B(8obE`FL%T;{gE~V2EBmW<xr9ja=c>zm3E>g@$1A5th8ji*adVrGPNAM_jycs1l|6)A7k@y
&b;2L!lca={D2|#QzpFPrzG-!$E7aO4niS-n@mVIhH0^@G#f?7M6c@;1&HlwFx4I5x^<#0L=VVLB23}(#L_t<-
Gzhd$#`9elZHuw2$72`bKw^g$A&bVI+l6&3`?HSx_VyfC^zmKEn#LAj_#Y|fIH&9vTsqroybu6`iIW!3E=YTbFt$4WNKzmkV
p@p1M-6RIN{Faeq5nvK?COb4|jOywqk0vuRZ5`;_5h}P2-}#Yil#8ppuhwfzUoU&Ij>~^B6zg5?at|!dlr(bZ1|&HMIW-
<KamGKF6cg)w7>{e;vZqVE}Zy;=qRwcOPe>3S3{z2R9H5Ibm~o`@wfO#pcAP@-t$rwd>p-
{g&qh_vA<<gSaZ>K6SUy$+uo$3`>sYt@yx%y%uP6N*dJsdkhl%T`^Ds3R4cMyCl#Wi2RSr@mG6J6tV)=xa*|MS<7B{J%BX0{
)`y9p4JE~kXwd`Yj`Mel;fqh!yxNM?}N;bDqo%qCzHf$JOv)$JKQS>-
AdM!TDC`go<Hz4(7&l65um{Px#ui3qw6q;V5uwOy)eOjy~;A65)p+o<N`o)9+MHc>f~}q=q_PlsXzZ8Su(8T?V^BdktQ`Q&I
}G%h$L^4M#+ZF-
H6b<T*!}JdI1loJS5PyV0H^VdrU_=z)QzcGGjv}AaKsWRmR2$1P)1BU4RtqcIGmwm}fpA?eTzTy)C3})2Ot9ti!l&J>SFyU|
eDf%Gf;@wG!ulTa<GQqRa|SSXQ!cS(!UvZ~R=qA-%Arhs@Gr;*7h8HZ<40d%Jgx8kR=QPM>+`_(u-
f1Y+$F<0ZmHh1p&muNW}*wFxVcF02Pp3D#E{FLir$fZxkgmaZD?beH}qX>4D`w?ir`xXHm{G%b2^q;Ph0g6D1e(|zB=kI!jj
=z>d-
Kgi0f#&^jD<<|YJ%nEV1sNkG29O@MiT`j?_Xazko9xM8JirJZk=#7sy?H~1zZ|Z0Dl`JiGb1i*iNsH8ys;Djb3dE#66ZBG9i
gQ$k;PSv`?1G|AU~MIyg;rA{_i~&{IDS1;+u(s8BXihJer#$b4U~aeg9ZBOrFYm>rB~Cbze{d--nDTWCN<a4nZNTLDCTo|Q}
lnQk4M_MEG={A$}=W(8z}X+*jmQlb>yqBCxlnn`<bwa5jwG&Y8<p~E-
@NQl83yKcUhH|{1Yn#lNO7Q>+_Riu0a(q*C(8vzc?405|qWzoKjZ_bev{u#87^J+L;`<tmwhNRRjKv;r6X(tL2p+99_CP?=P
nS)n8liake;vjhEM>(PwTxYdRX<Uf|#cpG>e5<xnIVAq;e&<POH~ISZnfvD?6~H!PQQ&eiEcvKW(1ku!SZENl%r4BH*3a|B#
}^*0#M1uPk`f`5+Cg<8&I8Td;>iRa-waYsSc-+$qc7NSp-
NN2f;OY_*49CC{v7}XT?isHmiF|;7Pbzrrr1vVL57|Fa$ZcO=xB-sm|W)EJ4Mg*3-
BB|9fTx9XZ<V=&%a#D10*|N*#Uzl?f?1j|ETQaXhzFy~|(ZJ&9Gx4bG*X%)HTj^0p2XPv!T%h8DK%6m0{uwP)`A1oPE3iEY6
H9B+5Q*8ZnZ93DM&;s-
(AKoH;V2}&v|L<YXtsdA0*?{xYp^Zj2h0$$F8InQgM~Smy7O#Mhin3u><TF#`EYMA<EVvD@sI1B&G5@Df<epNNunvcp&ic|4
n5ym4$x4xwvEkd8))C38q`!Rt~=KGj~8$G!S;iHyVli}nMs<txZN;W2kr%FL8JQldY92SzNhv<y9BBrUJfoJLMOR1t}7dgVa
~@xLZU6dBg*)X(tvT$fuYHN;u3DMEXP%hQj5^;vMAr4^$JL%bpr3@6x7&H_AM$H`i<9M#di?<NBMp#DVRR%5L8$l+^&p|jB<
>kjCQJ|?|@U8%2PL4R^HRyTtw+HA7FY;Zf?Gj&xKA)(bcu|ZBCY#Uk=#L9DP*77>x-U#z!*YJ+663#X#%Suf{z-
HVygWVIST#z(MNefZ~-qx{aK0-
UlRQ5!WWv@_6_#lbw@f53h+9A!<IZhnVB9m43<Wwqv?Dhc}Z17f}4x#G)DY&j~$<xtc4qhAic8)40m13tdB4RUzIW-
0#r~688ELPequTOi|%GHgI<+jnanF=xZGl39T#=W&131s7d#t%)^#6%KNo1`IUWLkgb;R|LH-lH4+DCW%KK%(;u(##d)W4^v
WVgf!ah#RN*95a$3g^e=uS=@{{)g#PRzmx13*0p3jk0p7^&~sR1Xc@9-rb%n-
XOaxk?4Z`G=74SXFF1M#biu}Te7txjyZcpjpd;3w=P?`A(|Aj)h9aw$4MJT=<lP|J}rIO7k83|WJbNQ-
94g7^RtsGj|V?=f^Y|Fx9?GC@x=Ab?FT_*YU&^h0?~5RI?llL3nc&`=D5@)$zyB$)W(!fXRT*3fgdl89_zj6Q=68cH=xAf{h
@(olUlTRxO(m+_nxqR%9OukoD??%NAx;-
5}FkE@n|Y_&oFItyt}^!ZLGA@`HAF&ESfX0#E!33?@`cvp(Ptc>iSevAHwn@`I)uq<HH(G2rbvG){aw_LphWjOuJ5UfZH)dG
>J%L4bA9n<+aS$w}N8qwChY}g}$xbySMJoO^j&ld=B=39E@@>z;lCmAR;W3NXc@!~J;R^jZb$*eCE%HN5KUUk{X9jNBc#fXy
~iz{jaM8cLw*L4$c>|DOWjfXPv`qb*#6dD2feFa0+G<1GpqPAf4piko5Zc#`*BNwN5fC{J$oD-
V)nE?dH(R)x8{fM0s>b;pZ$$y2^u-
nlU!uNgUpb7uc2lq=269_X51!ojKtdM0ltzqyO%)A288n>@<Zk*={ggj?BMJ}iHj3MYjOMXxlWpY?zb(^yxUxz@0e}OzT_=`
Y-{sk#e+ckvQe`*bLNm%Od`E-2DFJH&(?G{Dz9>74eSUG8Exn5jU;c>8&PhD@R66_IVzvvadJcpk2mMnvCft-
7?O;&7i(4;g=*NL%20UOZ;9``!xx|~MKP|mKY>kIrb31YLZ%@>}DhYtY}G1-
n|Wce@keS)sKnnfiG(#Mu2vE0dlV$04sC)JE`7_Z*KnU}-
&VQWeetTCEImX&YN76eeN#QxWhTM)K!1xYMTE=w{d#mqJ<VkSMg^P~@!<z7I*%m)NuK#f@b9J{DprCP4msy@}bYS{B^h)uYb
t5?Ms`LS|ghoPEc%EbCZ#7s45e8aVwE&187;*fjSc?R(E6oQc8Sdr9ID5<F<w%^;J>eV0UqXDd+Vq=MKs{4+z2<$^!+X)RED
{Pg@t+BLd>~X^RdErac95uTKl)t4DOoEO2rmhx_7$Lp<6{(iGM)cA(&IzkI0!cvATxqx&zczNoR>v&M!b#1xr40+^tKj1}4X
$`N>lZNWDa`WraeSpr41o5LTL$C>!xEtEqbBA8N5|sBoTE|j_SkBRzuk3)rfwDn8SMA)03G)fK2ptj<UPFx3-
@?Bq<3deH2b@rm<Mf~xjr)e6#%5JNy$X#T<InoaSf-C(Z<{L@~C~7h9=Or#pV|7dKPa3S5QV@u{}xDli1?+0{bQ-
_=m$2a30O8I+W~87Z44OF`*FV1}&SK1i6*R26#OIZON8N%Zyobu98tNkb_oFqEHXpxbuYiLme4bh$4{5h2c&KV<eNP5B7f}W
O$8*Y|z#EOXcF{qwn_g>GJ|*px;A_3(;zxq8|k0+2ywlOJbjQ1dG3Kh`NWDlz7<-
ZGJ)Smmi=HlTzOujyS;X5i$q`Ws%*APKEMQFSOY{o@Q1UZ?lJH#3r?tBL86oYLQkz3~-
1eYY6Cga`g~5o8jMDuYqys(CY13OY`O4$&p4#{}wEFq(^0AD6tK4dZq*wWYY`D(MLb;6yEL0ii}6Xx<8y?8-
JIpmil0v2ORp77WpFKp9MRx)IS>$yHSv702U+YRsU|iB8S<+o#S*pG2vk8d!~;hjVuoABDk<3I2W)Ef$YxtLUPuc=Pj)U5W=
_u8K?aHTr~$Oz*(tsTU+-d)(n}yTBU`_oW5)Gc9S*MO_zy!(<zP>L`kBKql-wl_1w)F9Bf^_nnKLpFF%~U))}_`)X-
2Gp%<gL?{@DwLY3kpD(v}wFGa+{Iu_LB$MvK+eqW^>YK@pf5!iITOX>i_B3*d2FUZ88hcb@Ir_$a=+Seu#^C4HE)}^<%<Q$J
EE}fX@a#T{Tmeq)zb)!mV)3jsY-EFb`)^e!Ljf|zyT}j!P>D<H3-
W(z4b@T2<MJDb@oISv0c=%uCy(L#?R?j!Dm*6qig!sisjQm4`t;#18VL%bnC)Y#7W{!jlryH3?#d%@A6&Wz-VE1Fu$YZT_#)
&gaiJ|ZZ!sX}*1`Z`c7afU@$Ld;BC8?M5Sc<6k2E7XxExU#CoR~ZMY!M4&rbPZsdg4m$MklZt3OzCT23YlP<72tYuf5_}U|D
&c@IUTD$^0L&U`|2$D%(1cQ_<>(w=V;b`y9umWP7POjGXHI)ffKkNhpvXF}3)*EUa2jc*)a@LhG@C0rsa+I@@QZr^MNKoKvw
^zePR?V)z3!QAQ9=#QN!hDlIjG50A2J1*ZsalsoBLGV1K%72(dkUfc3LcF;|E%VY}+F5O5$o#fv5$ulwXQev!2(?QQlPI1gr
kR2rA`b1d1BFl<uaXHqe6&Fi?KbF0tX%Ha&><?eaU#J{`WzY!JW`AN)DhwK6XL^r=WRgjN77&F47E+L@T$1V*5(w<wjq|`qf
czQg+9&}d`+n|YuMXzx)ViR^?>k<Ers?{3DeU)O68;jFCV6?BhaUN@B^}3AV7dv#3EJz(gD`7aeC#}?aHq=osyO?J9oCk8Td
%(0d}vdur`NtjI^${o0H&hpKYgLp6nX7(I8L$ye7x3mIJ;CU!C$Fo`lRlBSW29-
L+dzo5DKiz0Gz&&b)C0K43pFBg~0D2tG8p{I*kdOwn38w(0+DArs;YDEY5-
Jba^EyR~nIbu)UTLY{ip~6FHriR2&zNCZCYpA2#IJWYGq9t*e&Xuko}NLBR7mSu7QZVE#(RHc#>u;!%>`%|!~(R(#y7<D2Nq
17n;mRl8dAjtb`0l3}H&eaC8y3VH#rlkel?G;KShAA7RYdylRgv0ykATk?-
x{Jczc{~@VBHfnm)ZJH7Gfk&n60MA}Ha(AdPL(@)SlL~h3Ut@4ouT7Reg+m9_KEkQ(OFXz0=zc|h<#<qMt!E)uZ+6SrPdz5f
of+}dV!I~ru_>tOX69L7E8dWIegG)KxIs;E*k8Pl01!0X`>ri{#k!T@()kPwSbZ&&{$gw$p4Uao*HwjF03zObSXI>knRvaIy
E-IVHN>VWf*FzmQ_h)*6k`)}QZ$iX(%t(_qlB>>+(Vcw=;Gzm1qDm2S<&p334mNl+_ht-
Z~dj+g^>6Zn@}E()^qcGs1fU_=;W5-
1AH#R$*(t6$tIo|26C^)74RI2<Uv%=<Vr;Ta>_cX{MGpxKM^=xGl7(&;QT{X>ukbY$iHNaa6xgvRm44Gv(rhT5nWm4g22LVX
i~luGy#Op7De6FaDTgb1QX+(veU4k`)~OvROBE%=`ii6Gk9)r64*#{xb2!q5Kq4ow^nu9^8S~~2ysJ(`${eTZ^%Y@xvd*!It
YY`f^bdd!Xci4C<G&9ii*gfxtPeL;0x#C<9`a6%;sW6@AON~df%w0AgJc+%w>U@$PX;bUsW9D)Sc-
*@k3=ru2%9q9KRqK@#<Lzo|ml~2Odizp@tQZsc7isA@^P7ge_Q*n}?ptf%tFbE@SG^Y}vE3H#M_<-
yVbfZ}m6+J%6Y`U#0Wlgt{szz>Up!-s305nE6VbFxFBhM6q;0Qp-yxAIS7p)r0<uy3i(*#-
znj_QvG~mT_|nOSOrSjCSV!vJ~K*QtxVs5_OBD-*$!>j`S8SL1Pf2*G`K%k5S1x?R-
nCyyY$r;1|09aj_Nqd7InfS|`D!PwUx%j=TsN|Gem+*_fAhOB-sAQQ^3G6d|Ig8d<4;FNM)&GP`QFOOW=M(kK7j`SLm^=kj6
MWp{TeQb{mohYU|pcirdx+9LZnkyZ5|TwO_SE^>ad?eB|&Y5S)Sd!s2N#KCP`B3C@Nk_Ay-
O?oSAeyWgMir=ZSfY&rx_&f%&?^78EPZjIL==SP5`lRS&)bK{$Rv033BolTGmV^Bd8BYuv`rD^A`kYV9VJXTilLCq0PY051j
8iKWMs$7%7h=_NcNf`m3s;#hDpvC4#5*?U<~^|9rC1d4!(FJTZc<YTuTi`q_xdK2P08{eyS;Es(DZ>Q*{K;)v+yB`*MApdAq
rcAgyCJ5B8i{}mDnd`%WC#s>j!=f?x&FxeJpkH@;EEd1Hb1ZJ@f&*aqGAhWA%IJwu(QTx<HJK#NE+;M5R+Td&Vs2k^J`j;R5
>%br2wodW*(kYtvHyBH6#n2#5cu)2RCdq3wH}-
fwIREW`1j#MSZLUtATI>m~}`vtT+7Q@i;gW>|mC5|>U*l*716kl7dTZo(I;BvfN)maj+i6MzCjMkL|L&EW=i=AwYCx(ZYW_p
*xlJEOUf!U)3?KuY_80mSF(SeBaQhmuCFl9R8{V0)@Lw)^Vrq9>qzkIFd5iojl3`rq$Hf!Ek|m#FWH;t2;wUP8wr>5n5y5pa
Gl4=fLBD*Kil9+Zg@!U}XtqEnyqo*Rdx{u)AEy=f;GTkelR{W|2m9kJ>*WY)-R-
gKv~C+8EY)r~WGeR(g&m+*po=zRv21F;g>s(uSF6$lRve2nN#4YlovSptYogUTa_V~OqPCr#;+1R*l{Ws1*@j*uO{D(OQ~$W
J8jETb?^9-
|g^MVz^6EwpyFe*AmX0#mj2hs=Nzv+MLb+4ZxW_Y9m!gqH`(dR^jG07y$7B(wew%w*6MeJ|Wzz=b3zA)m=e3%(;7`nDWop+w
Kk!BQrBL3=anwdR>7K#Ax;TRs8ua*5>$az^MA%@899qfO4atzYc=|KPOBSTH|b{kooS18SmXy6^M_0MA(b^Uyh@fghM)mT4N
KN?NEtJV$>l(|;RI@_f_#08x^|+2EoBlqN+^db^bfjHf>hm!mlB?>Ut(oq7*3jD4cK_i-
R%B7uxnFQdhKYEkwZt<G<7t5|3|GXC=H3lf}I_chv45$S^4HXbutA>m0#=E)Kb@7(xa_tQ7*`v6pziO)orQz@jP|B1FnSG>4
)sRR)nq_$R#_ykRB3@QV2&%nTeLabE>Ar#s<EF%N>O6dHfD0oMA>u&$yv@?s`<+9$l_x=-
HCdw*p^kc6{G6yp{tG(%*r*DP8?t0%4x9c<_;aWHsDSJ1>-
O5xX7fkD3CxgcYHYtuhJ92?DEvH6U8;dmQ?#yBBq4z3C)UdBPS0e1%pG=yXrFwVAMx)mpat$hkLmE%<jQ&)<lgP3;QG}3g`O
iH{KmVxkn1zY>CnH^k@jGjYf%qjRvjQ^8;5{YnwfChoR}DDq;?G5vuz<+$J}5M!o{B*ggP_xB9#Wgx1v-
a@X8P}krB3OTAeWafJFhq<#J$}6x{}(Ks6*~{s%mDaWS}OE@KR;jnD%Aa*bSP4se>h!s<B$IM%!lUvEls_c_P)W34X(<qM{J
56<VMBRc<s7u7&CE11C_<=B;>xZdmQ`L`-$Q+f>)8RXbV@v+$X??h&n=EjWv)YXKS^b$0^ej-Z1~iTMW!)P-
6|Ak#0JPQJ;q#sx2xSH6zYs=Gg>APSs^!BQ%;7Z<Xn$ToFMmJ;|OZatKD(JWpVBTyotb|-
oqf)KGn3Xo0Hispmgupv>Xkg=3jwaq+YGj6E-o?qeuLmfW#s6-G4>z%dsBg&TavS0o-
^5IPM8S*9g9Z+FjFLt*rLG#_`zVR9e_uju2V3g%Gb4c)!wM(d?=!AS^OU}<-UUn6mL-
;Z++l{u_9nQ;S{AHk07L<$B@%eOKvIaF-tU38VK-sI0W$4ELb@vGSjKcl(JQk8-
&Xmhc4q@c!8x15SwS7_V?^uSo2XTl<9tpyW=I6Ry(T_s|-
h)I0S?2kWBNZXHU%(iEmec=>!5kGO38aV{H#A>XPD(X`x^jprJdctWKB|&7C*tAeXV;5u-
KRs90?E|B?yMA)G+6^aorxU`)B}(u1ZW=#8j3J#JMToN5|x){VdKQcIdvwz@1T5X_wT;hp*`IHNh?FA*dmV48R;5*QK^z`xf
0XVHsDa9h^82(#N{B{bv!JJvSUFglxw(hXH{F9o6TB;2F6m0gb=kwiSGWQD)#FQn1~Oz{b`59#TWQx((;8NN#CL$f{Z3<wm-
KC=W(=NeU!B!bDD~ir^YR<5u0QVi3(xX=!+-V{sy3(emsA*`ZF4go}BUZPw+Ze&DM#&hm<g}6n?~ZMA-
$!F?iS>aD@#LkZ?TH!nHweZOHgXl8KEtoEOOY7V2nm{o;Ka+FaU5NeLdgyLEfB5Tx~0ST;`4z?F13{)vCm9nGU|7R^2(JQ?|
c6Wyg`bu1EVqB67C7%T#2?AcfF+27S78hHEf^PUv#Z(@-7vxJumE;IE{K)hzhU-
%#Q24z*hh>Wv@QTS4K9SFyQ!TSkD)e(~>i4-
BKGV}hriV4qeLVo2g?u5B#s*5x$Q(Brtk*O)m$Ewafe+M_ZzrhBiro(?WSzw>9+~0cacaYvP<~m%Mm@dCOIm<g_kaR0G%Aae
R_r)3v9MD2LG?sN6YiAgQ4b32$-
gTVIKCWHc5XLuvbjL_?YWjh>Yfa!d(5OVPqY4a*9QB5!cwD9{NHdsV(o`e*P*;b0^}aJhuvI(Iye@Se(T#(uZG07P+q`RJm)
bml5!zCOd@B!ns@Esgv|rm08W2kBK;g5N0cH%(Q4bpk<JeI5oI?O|Z0~$*MQx@9jm@B?1SLrt;sI!@Y6bVr7}xJKMXl7pGhI
bPu^wJ*?~N#*GL`pfQ#L7aQ$Ot0^+idgq3es6Wwnarqi+)=<C{HmviS{i)}7E}s}80O>V-a0CDJS-
#B}g$M(W|%8RN#d=BA+zy=D{gM^SRt3Tc)<e>6j0Ejqily3q#b#d8%KRewUaUk+43Q|#x#OJV7`Vpe~Db{BmG11?|fnb}y7p
i(W_gNWMA@5#5x40DjVi;iEFtg^XLaB9~ueJASEiLYbJHlY7gY4X2bcig`Hzs*W6+te8!0dasU4nH=4x(@ELD&yyj9ALccI4
491LuPR*gyZ^<|5ea-
s~CMRbd?`l%^zsqtE9b%avYb1Q`KGDtDW|wUZk9J43k@9wSrUPv8C*XlkU+v(Im&mkQ+AnXm!i;)zLJ^qxPjAWNk8PpYmmXi
gmRuua^&G46=nWMua}yM5C)yG#eIYts4Z&JgZnVvT4+?fAxskUH-MyKGCMDm>=up2J;FCSxIKV&>(?UCKN0~2}u{u9AoIrjz
e^rqFLc@<WITRU=NpuR4#84<@x`4R3;egr}0P;2xu^>fa3uO5=zJPf6gOABm1Iw{F1mh%_e>Iy)N(C(FDr-Dpj(GoOZ=EBH!
HWT?ogBL52xruysizdMP*@k8sqpbep1&pT(($i;cE9?o(*l``&15Z<difd@xsnm{%IZOM2Z%EDLD2%G5ln8?`K9yW_NUO6OH
qw-60B<xdD^s25L<`kniIQ9%WA^KC%7X^D@jHmJz<ek`5l^a<K})Z0qXnH6`A(}hAY&b_0V3-
$g%5DEItEAG(*L|_vksiDd1iM_ycV{;S(H6I~=6me+AV360%D|bYSiR-
^pR^3=Bs~MWO&irL8fdXDp=hQWadQ=mQa}Mj6x0Ucyl2%`qaxGXXWNE7CgLF8N%9!pL;=Rsq53ftmJIGHh;jV-HQU>~2BmmK
yyWcgXeS+~`Y#JBmV*I-y@jFzo$v%=h?E=LNUFOEfH1Br8WPYFdooiy8B>Zxh$!O$BvAV>-hGS^wiW=#%*V9IW763^@^*-
L8o4^JUlI~;$yf~2v-)X-zUDQzd7Z;Q60gSoAv+O|V?=h%FU4&L0R^AW3<Fc_T6ThS|hj#@-
uhRye$4u)%$;}l?V94b};V4~kTL~aG?4GU~d0GelOYZl+TinR3GI@oamK92Kw2VM7>%RWV@FqOW_xPL1+~;e_|FhE+4aaCRJ
pfigDLI9QSAoe?^T|^F@6OT`Y0-
U0B+FS79#4`C{tp1&9=vK&p;DThy@>dvilzbD8ejx8=!5~h(jhg${yiXQlEK>inhZ%4klbVgkrr8Bo=CWzzN!}#-g_2o43-
aYrMz_<6mam%HG{9(Q>vO7$ErY44eO*EV`(DH8g?b+Xr3SjG_LWR4oijaPJLWyCS<~*`*>J!=>j>;#i$Im7kaaa@(Jvaki8R
aSsyF%Lp^66q#j=1F7^ew$NP(78S2cX$;t2&|5cTWs8zm+2e2o;f6||`tds6Y&|1_EKW-
JS<J5)i9k8lmZKN>iaK3e$>PgFQ#?GxRrrBtoUBd-hieln!%lxwdC?O*1>P4@9?3GhjhXl_!cwAml-
34_^o3ThFg=#96bkI5rv3m<3*qLxB7+%mk6h&Zc<TKQ|hg(kDJfzsx5Y{=!_;fJ0JP!}ur@X7$miEm2_l#*$eH{iro+K#M%K
`sn@O$$q1WqT4RJ{r6O@G3Im<uH}QmXL$L`_p%m4kc|ac!o_G6lExSic=udJE4U9WYrayO4Q?iW~3@1x*}aa+ZxJrJXfNHL6
55z(qw|Ta^A@L*#CdEBIHc2a#-->Cepj(Q_NXb)o!1PQ+A1y9l@ranBEN@-
JRC3Z@i`YCv)FC`Rqg_H3aIlXDB~bbO4vdc6HR{Ia(i6{(Fo83ymzDS)g2JYT5WQpOu(lU>5y>3y8T>RbV~+{;CHlEEHGKMF
eX-
K4UHeg%mkAhtW)e3@arFtOaWFbgCAB<a25qDsH!TKiImi1)UDb$C@J1MUhlB}fvbc#Q%((q}CjUZ1Vz*%O3TJ19Dg&HQqjo8
U*oeQ@JCN!tfn1y<krQq$@PE~1E{bX@^YD5`q@W^SNq{#i31Tt(Jz6xbARzv@L+tMN9g_VTEy&{at&x4LM0wySCfg16LIzp#
f)#OEZ?M28-HB2BsCK@O<6G<F^lso;Xw2nJX6>xD<y0I)d(^^y?5i30bY#xR<!S|9>4l6N^-
wc=G~M?5MwWrp#Dk&SBUcrawHlC21NOYWw8eFO+90)&;goH-Btm-
<P+P8XO2AZA55tC3QQN4!aWq4jSMj|=}I_a!nH<xBAv7wUwy=aQWKX0S}Bdy=T~NZBjdS2*aKrezP;v-Vs}?O2-Zw4O-
O#;6pOTRQ)XCMS1fJt8c2LW&qzlv4g779VaoQ&;MMxOSd(^)lb@(h|T`9r(#LgE=5%3|>(a7a%7n0nZtz#tazUl|Tf#lHS=s
rRR;{8qK~|j|0(r1Az`H&~cFsMe$R}^oeI&pkAq67pPL(6VSV;q3FbY&_X+KBM<C$R<HV)YB?I9Nf5@*8<jYW<B;=k3EjO;5
7t28Wh!AqhhKTfLFHLPv?*%#t>O_vj?{kf9+5?2Z^aWh7D0TD2}KG3Id>b^_OXa|_=I6=h38q^s-
S=~9U!viP)2meVPC)p{ctuFs1DoDbThrx2zI+g?8nUF9SF1Bi@Q9}51zCvX0V%@Q$&AF4W0RU(!MCqTSXW<@3hoSN46FW%sn
$oIKhL`MBtLaThoY0h>4h$u!kMWh@Fz_U{aj-MOPgf^k9<l{x0on{-
(xW)3t*E_#S)|QmC(xlafXhSXmVuM~1C*+6)ib>sIB61Vdg&$PL+2!WCCLa9(b>Bd>s}6@@G3*s@kJnlue4EW<hT*AN`$Ig#
1h?dS0%ZH8FpC%Un|>q)ZL&+%(m7ME~JnJT>~`-nU}lO8CL+ra0Yr%$-@`c*Y5NSO#mi-
2&zB(q{6q2y^Y3LB%~p!0EoESIT$7fixDDYa})(8(qA?vzv3tEWd32+9rRGH1^(b5#)wBu>{AQb<SXJ}1JSMl$apOjU#^1$s
jbL+834nkKv1diaZwUWIv(JzH0Im8+%0Fn3!1iK(C}Pq%;N+ujjG?k{sZ63R10+wxb*BT_LBu$qSR6~BR~WN3V?_7&3h@%<l
c<tsqA6_IY2`JC!{@_deShgIJF_G!%dY$c}TJz|!XtL2c^r|{gk`8{Q?d0Pw>+n=<q$tSBm51BlxhgoVVNq(FuftR79h+yv_
^3RqNcd-
d9LJeg#9m>=v|8N{Be7qOUXF@z~2gg*(P_375H@4Cb%XZ;}hfi`ikO>wa$aMEl3So*Yw=WA^WqOq{>)H0xI_(`dH=Y7bL@~E
I!w^$#2PF}J1e@Ksg0K`D5=}Y(y5bK}`T}RZ2Z;9`UhFlvhXCssaGQm6X4@5C6Dv}QJu@U{=%u4UK%Fx^sgff%*Xb!;cv-
ki`{wO)CO1=#MLc}))O*KXP{}B=Ms&eUxK!LxK;z+zTX~=!kRYH-Qd^P%Ay?uN?N63uhau0Ao*(Jzc$tHP>{CPmmgI~6Ik2V
cxNQIK*TFvXKmAw#YU%GzGdIm<u5EwK^|G&!&a#-wcJm7|QRK(8-4l-
NKSltQS~Q?%)qU$#ULwTC6QizsZ$8r4a?Xg4NK}by;Sa%k_hYH&LOF2Awt#8wGhgTOmWB#ukJQXS)WNXI!zFzF{=QlT)_BAk
sp#{|KkLFJgjRFo84qkMpw14mIa6p5N5GnfD?wj;&bC)SDV2R>&^bS57NNrl6M7&#&2?=OT8#_5`0=Ojl^mp|W`-
8uf6b>+Je?Ub<Xh+Q_|ZB_3rcoG9vM@<_;-+#+)yCY^!+b|b)y|q-
7p_@@?qooJM6P4v_)BkR5rNV46a^n7}&x%pPw9pz}h!R#353Cq7=RTnjjoZkrkCx^n&48HIgN&fcra!`*wbmDp~qb2wd#NW8
*86SDiCHXVFpwn;Rbr35I>BgR13=dv=|p>)tmH6{R#Fwwq#vxz$w8X%)u|=Zl(U8>2{}Jch7B{)2-
VJ&J!RJ442K5bKVY0KtSU9?+HJD>4VJ{$%*{$f20Tz(n^a3;Ax|99hLH7j`kRmse*p21?0CS;>X2Wu?&B!Qpu0wowYW$-
z4A`{fP}zsq^+ADv;#i8i&&GxrZT<&6JJzfQYk4X9+L+(PpZR_ID?rG9m=u!(e{|J8@~B6+?ygdulW63cp%<*&V(wdm}LRy$
6{CJDobBRk^F&3ckBYnwJ`Oyqw;bh2f(7*rzoJy;&vp35Geu_11(5Hyf;cgAtQOg=DQP~&WiIh%z}dJjk(UuDI?Pt(K6h?#O
lqqidz!Igj`eEpj(x^7kxmAQ~bJN%Sph^`SXzc1jds%v8{&HM@irJMi1B?3oy@qcYgxCt@2$=+sN<?$h{LX}t0xMkr^v;+T;
`E)!y)W%2phm6QY;+D&zrA?EB)#(6dg`>jFi)HMo3eKcTshu@FGGYKvOU$o(K2cfviB3@C$aszz2;zp98?hr0e=m`-
kqficT}{8r{xa9V_x}lbE`!4aXPnT#qE(A>b4<XnC2KTfhKCa1dr7r#_!nyKR?h(zHW}wtbAmb@E1Dj%SpL5I)Wqb~p3`Yoo
s-bN)8A)!%ICQ0)yULd#CJJ>OFd7i!~_j|xB4g@H5m1z@a*XM<{^Rror<kD{W49f!7WGh#_@*Ufn%Djk)EN%okslBWh?yI0h
Am8&4y;<CEbjA8yHShdR{AZB^wR!yXUa$$3DgH*ww}Mj6)Ur{p>{<@viU?ISIsTR|z6{W?mb8r|)<%vNMgGj~fBg@k+5exi`
tJsgQQA1G_ISw^9FFoXrcJ+9NjZl1(mN2gz85_o_5>!PPprGBWdH6|GvlpRj8dDJHQI$37Hp_N#%LJ{K>u{~l6*gN;6R1)R*
Y{U0EoM|ALw)?mFrnxNKT!brXb*W|8qCrt}2?J_wA%MgR6SE=V48AvVSoD(?(vFo0pU$_ntFt9IW(}tTCManVMNUBY5&N?V5
%Y{2v7%I#sSS<`2=Dj6Ir_>iJ%^SUSuYzjot<H`@)eVArfl?fXEu(^%%eFh?&jHzXjUm<oGIMX>Pr-
S!hrdOeSH~=>93z45Ru-
61`?%arbC9SXLfRBy5Npwj(CjXr<dAAxp>7VWxH$)T@T~vTi^z$PgoH*1Nvg<Z&&`p=lZO`<@u_iBa1r`iu0(HlWK&C+wguA
#HRI)TcKvn^zl0oB;LrmSwLr{wlh@5_<x-I_oU^!iXY$<OaAxp;|F~rOxT&0t@lFm%-
gDERe~#J#9vV6on`DR*Ij}9{g|vX7Gd*ZqeR0x-YmGvGyZEPHNhW#iUGtvW1_Jeyx!F5$i&!W4{v$;+gkMb4l$ok*z3-
$fZ~&~r0Vr}gz*Koez8}x?Uj`Uxdh0Ox=r+BbeU@D_iq*O4@-
^I0<#f?r#9iMI?CS0TiklKX>;r0=YY5#qaW4BeawVrT`kdw9@QEXK5mE;fDD&KeYy!sn@WiuU63Lrlj595njG#}hj=kK_Zxe
1BX6_ty;);ogl7oQvb!0=`Bs>1GNE-
c(1_g5z6Na@VLXlq_`fXM(R4)2O*1iFD0eR;g5OPFRjmK<qb*GLaZ1*G)DA*DBW4>3Xm?quk5w$^Q;sM;Z9QmPTe%d5OrwEy
};1vXF$2vB4f7XnNQFS(H`S(Y3dNSokN%o57*=BjI)DNe0neXdyOkGQdM5B3}d))n1k)cjek|hp(s0=cNRrUY9n>7!<n7oat
kLK;kkh5V<HE$blz0zGL<{%(AS&c(vgVw78^AGwlo{?LfkjWF*)IPgzYb(xuBBS-CC!?Xo8$MUJ(KsKjY3iqw;Ppk%BY7|yi
yWLtsU*R=ru}}?dHPYk1D%f@i5adN3>Qs`iq!IiJ3phU;|-
EV;QYXS*scvgFwMjXl!p@7(cSTIwW?^;lO9{QS5l;tB0S1uQ>|}0pV^gl287jIwTo`3*z~~$FX93si$r|03*(ZjlTMT^XLwy
sRo+`pP|K~bJjtcf+VDMik8pjl2SRFMNP+r4%i~9QeV$mGu%AkkoH5L!qf47Q*A4ALgmTC3!;u*JvmeCZHlxv}1d1fFi^bYZ
m1~0!=m<Hh4WR4Q)0e7r5bSaIp<<wifL7<bYj?&E#fUo-
@rV8GWDnCcqlDpA2xX+x91Ky6>7|>eJ+UzdcSYaqcJKq|b=e!KQ*qzL!h#yp`g+{9|0$pjdfqyYiyNZkB-
(9gXBviMV`HDenTsV)h1xC&tOM{vlBz2Z<_=Izm_siR59<=EE(C!Uv$-
UTD>Jq{0Xbta1DjGwp*Nb~LwmKju+bNOjk1S6=rk0)MG<n?&9Ur4xsV3ZWW1MUxtko#VpZOAGO>Zwl%YnHb}EXT%fi-
7m~<WKD~GZWn(-rv_9^1MJDIU>JAzX&fhgoKq=G+mlwKdtbqqV<_-
qy%8a`FyOkjx|@kQTN=w%{H{`HR3cX|;fASBzhVWSz`nyna4uXcTdK`^M!nU6n7B_vWEM7d~^O;$cv4bvh8iqDh!OW&+YD+K
p^rQ%H$O6*tZ-cNRs-3-
3Rd&m0sM0PD2W6?WMfzO2dM9jd72<5bvUcTxL|IRxY|DsQc+o6A)AULlfSlu0cRzN=l7f65=u<%_eC)2~k-
g_2^DyAH4TXMOwKlwbOq_9XW(>qt@g%u>+|FLvg9Ru;{NiKXIbET05BAwK@7hEffhnQElYr#(TM)TSKq(xT;k$AK=(&AL4{I
IT-dV{z=`Va%Z?XErb+0Fb@K2e+jXq(m6kRFEPzGjgSc6qwZm-9ZWio(-
n%>rlk`~z06=B3YoYsJglDB)_E4#r#I(P2N;tI$L$jMhAANQ$&vXrhImHV@eIIHsehJxLfXW`0rprFG8DW4PuKye$O;!bg?^
O+1v%UrCc|-fYSqgp|cFar)?GIwQ%xC6_E_YVBm;_MCD8s_D#M9sSRpvBXbekC(F~1829U0&LKZtzXRCk{I|Rdwuir)dJK-
v4**`Z}!A2|3szP#nt=t^_d^ZDPPsxF%Z%qbb1!hxMftpu#VUxD@5vdNpw8fmpK-
x%;i%vXa&s3WvR<MA+WNt=)PYC2O{qAx0ty#IWyvv&jm1s29W|iS4QmnFx=9q(jk7Ywe{~2VKN@cK2AnfG0{uTT^N91ee(ZH
{_?)WU7?q08{m}S=T-
VD2PV|CzgYL@;Mkk=AR@xU!s{zt9#$uiUsj$Z8W$pUlMnbDxq%Xu*TMqjat$pJ_I3?q0`q<$XDBP&5xz2J+d!82h|zVBA}rv
Q-Uhr2N2h*0SoqP&@hdF2w|3eguse5iAk284fv^ekiVfFTr`&z3ccXTtIXOCzH<T$(;pvF<42A8k><ft39Ns9+TLpfMtUdj}
aPb7_PjhwOlk(yl%19kblvBwqUJIXmj$X-?&%DNCqMkbmSeI~-^Pc<t-
*dTl95zYkXaPQMteww%)7B;tM87mj`6y@&_+kY60S<$GwwIo`or_(w9FL0nmp^^kFvMgP6g-
*(gc}t{T!&xaq@NsSZ{H4#ot;)dN3_d~bkQnXHg=|v5F(1!;cIM+5OBL=a!iLCog+f;7_B;&7Qxu>Gsp4ao-rI&`Dg)SR|yb
bNN0ex>TL=me*ZQrX>WS1Klm*2JW0H{$g%^><WVFxY}FN52WOA1Ac*&%hiPmY?vxf8%aPi|^CugZ4&v6XqoyOk;VogIW_}P3
$iq+pq!-
YsS!gCAQanPdBBHpFv1+9Zs9hBv87kh@Oowb7K~}8o>=jY|gaCI5dG}H2kdAfJMZ9q5AUEqbPU%e^YqLQqlAmc08Bi^mRH9?
Ct)W8e5u7&5^Kbc!46!uaauhv$#vVByTM&(j#nfOIDZcw$HV<L-
GQaxTeM(Sf?dKXi&c#sder()W*j6L@SV+otFb0EZad7&{K+^p61n7@<xv=w?{6f;Vpqyiv3YoeX46F^y|2_E=EdZn4?8pR^i
E!^V1yFJ3Y?uvtYRSrYV8=sUKT~WRfT3QU$;=>_T_-
@OaLyf3Km9@NQCY#asx6OZsM8!!&!BJME0Am~^`EYM3Vb10BFr*9TIW<NkK6w6H8|1%G(D9_+$-
qM*lIRuOG~UOq{K)di`#Pu%>*uf@|Jmhwbp>zT+$8`s10}Ud<m^8hmW@#M)R|y$Ixh|gq>y)pe$GxH!anAA8E!>kM@g^qoAq
BP&zGRa$@+>!I>W5LwTfoe&}q`r81LRiJ-0LX;iS485P<;WFu)FeK!CWF>5=xwlC>^ii`3+lqfo>Z%cvjHgM+Q+|3{1u_@-
!>}3=(b(YFc(4H%ni+)zyLcOsBe-bC)I3EbjrtIr27Flwx_go|BpkO+<sJ0nyn7008-6>JXP=rQ}^saupSBe#2b-
V%#Dq&~3REh?Xnv^Q)P<;en`9X0EeXS0??XIT!ef%t`%8}kQR1OlfQNJ!qX+sa^s>I7<hAf#s3~eVvE6qdVD?VEpD7ftiS+D
w-qrwIRRc7_+7t?<AnMmvf;N}M<VUie^2SXF@RPH+WVwzqj0Z8Hu*o($IDicsLgiZuRT<!>rN#&dG3IYzfYf6t?1;8te=?Jr
P{)3?5C*1kFd-+Y3qNV6vzdqYUP-
8&gd@YZy>t1D0Cc#H*hi8|I4eSYS;^g3Az|mNR;D6bX!``5y^)o`hx+}9t)pQEu3c7xka`AKP-aLu-qs_C&S0?FbYCsTk2F`
P*QprA+<t9MO)n#V*?#q;kQo{Rw%Hxv<HeQedf#AT%VgUu&&WaAK#=-
PzAQ#SDfo?A5Yk+}`KtV)X;NIlrz)l2Yq>SYQxB*P}p-
{TmQu9QcY4mX~Z3{1GtE}Y>qoSJX8CaQm{P}JN^*s>0?a@4xhqgDILsL#39<ic{1r@zz{H+5kHSA4H8@@=hi7ir}oaN1TBBM
95OJhf37+fv|=nlPdVa@%G^S~xWnm^>=Xm2f?2hPkKjvPNSvk?U#%tmXpggiq$5_GLQDwR6Vrz4*jG0xf;ppQ=hltNBSu#=x
In+dW`))(Y#+NRcoQDlwb!CyIjML(id)2%y`S?G9$YS_tKH3*q?8fN=|t!;?vLEV&?g92BbREpDnIZd|p!%*bjAr*Warq1Ec
#d;()Q@sj{ffNJ4*ysHRTH?(bi(03Dd3&J^7zk(gXrC>1zwl03VuHv@N1ZCvnwdNscg+GkAW}K8B!FVCo@S$xjZdvnkIc)7$
A^8TMphMfJ<mi3NDBoX7VvG9V(8yA)D6lHcs9&;Y`7ml@dmISiq&`O08gilII<`l7`2hb_`U{Tn|7=Abbf(g?Ov_ejx(g>Qx
P0>1?<hixllb58YOD<KY?|BQmnmN?1_fM*QKLW^6JgcK%ADo>!QJyYcD*dG~5d<bsK?&1M8jpBsedviasCfKrf}F|A+L<R;4
$&dpVY3F`jYv5b0C{9VrBmr#^M!Tjx(5da)p>NyqK>)60Du9~m*h_+IyxEtoN9x;FW5(=K)rS*PSnnBpUI<ZV}vTrsHw)h^z
^`arfRamiFh0`062>|8^;e<0XfOrU;j3@sTl@^fLwuv&u|^Wq^fwnze8i`LECr48wxZl%e9MnVI!G6n5m4@q0@qg$J$Frrug
6%I1m-
LQUtd@by{GTMIa3StETbVMlghRdT%5svzvnaVi<&BOKh$_=Ts@;C;iip>!Q7vi|J8e5b{v;pPEp48jr=0|uOFu*_Ns{C@PI$
PM-Eq;6IU%6nW;T1TDMVc|TO)C-
vnf`DCJ0U`9SUE%qZ;zfwR8N}Yg3TTuxnAkcNOPkbF<v3@M9mUkvj3&>(0Q!eZr8EI+lhB54f!CzVD3~z-
V8w6%<Iwj#bbvRn56dqD>H*#%!+^1)MCS)n(sB$?s4P1uvzh3Vx2N=MrCJy*YCLMV>NOl+uB^^`sw)%2fyl1*`-
Gf7N=HAi=e>YkOEA@Jz~eq5eRmuh-LA}y(Bn5FOv$b>F4MiEMpiAhrK+6V13rnQ8u4vS&Xpv!^FvioGGj|yZR70JRR`YR9AO
W2(=kj)z-g{6aAGSY_tXW0LES*NZjN+dHc9U6LXISM-3j_*oEtfJ7d^otA6+^|9_HHC02`Ezc0yuk-
l!)XX3oNiX^J#R*c`F=@BTgbF$td(1w+hc(jL+`Ap%Uu_P3da`Bcrl9yd)8=LOWOO18Ju@0?MG=}AhBkL0lIuJGOf_T>D$&w
thh3^YB7#8>XNZZIw8rB&LlTE&`#C4tQQs05`xi<Q=|8<7F@;G2e_>?CCs0Z(!5JG}bO@`r|%uTh@C4dnzcoNs^65@VgcT_f
G^PI)0B15BzYnSJ5M*haGZfo^UfPlB`AHDb}Y23$uw6B!T5Tb^Dmn(#AdvQ|7^YihQdWZIOn$-
HDKp;Hsu*6OzgDlD@dex*NJJA%0rSmrSR@hSkGZS?LsYYQc5eW)=5OC}iZpod+uU^8HD3=O$rQnfzI<HBFLBUOvXD61fq^M!
_$%fQ($X8)M_#I5pX&ZfRY`Asf!4DPbc{L?(^6kk7GUL4^gPb9s+7APN!5`S}8ngMo%!M_rI?avka66otE%#dxm8DPbySJdw
)--
~pbqQROZI}uwCliVE><GR6GSCs@P;n?UPqJ@CAdqci7>}6%cr)a&^01yTPO+wE`j7h?vU{k8b<FL*U?O6$n~S3Pm0)_|lUVo
KGSeEmSb4tI2A#XbfU=!hJM<<P_TX~Fn+QfMu4`{IOs>P5mi-
X)37nEuOQpwtsvb6D&j$_)@s(ZUTQW?tg$JJ{ofT=h_>XomM#aRu<xb4mxiTKvh_X4wh=#Qvp!J%%IF_Ax85})09Ch__&lCW
~ujAl@X%R&TM1Nc8hZ+nnNpnGMZ=ZgZ5ieU5f^=*g$eC8o-
1$MFz`RHD>Uh{ibOH!_906*yHue8R`+Cb^qsoN5!2$T?Fca5_8JGWnXG@dzByUq|na2dED^-
yf(=RiR==1*M>U6eapQ<7IW@(IHDifc@9ArwL3AXWS+#V@M!k!r+;c5O>^c^zPYltm}zv5Glk?S2mz*0u*P_Wl~-
%n=IWLpAoH+kMst1jh^K&Q}1=nfbfgAA#X=~3_iP+;HN{iR;3YL{Vl!zoc!fmB=Tz`rIjRV}XH<~-|myr-
C^FK$)bj6~tcM9@Q$I`)yb3sfy={jeIG;_aiXq*)=!YtOn(j0x{P=Df2cHy#$zOTi!!X2nctG^S%gtqBk^!}+*IJh$;E=Olg
K%JvF^uUg~JmgCbG9cIcOthzMO;FS6^Yj4>7IM^^On6hFaRAOM}n8+NtpA5k|%J}ShTW(y?C|9p?P}v;NZ9H<ixXVTJfW6}Y
;FZC+U&IfcV6F&(yhrZZZVW*h7<Hl_1r3zsS^7U=7`(Kry5vx?(Fq5>J4>71^CpQ-p>nYwx8Pw-
9OEqWb`xS|ot6BrGnQQ!u+6siz6-
rz6Yk<k1LEc34F2#UkT<WPJNh4LKhUR`iQ5prXK>G<KO<O1n#U$P*Cce0#!zai{b7XNlP(!<w!?a+RW+%WxFpFtC7VpRoZ-
b5JwE;6)rZ;&LvMns4`OvBrgAhH6*9Vn+&3wDEi@9EYoDJjDufi)^X0-
O0K4M2ud{lN_rRZ2Z&(n>8_oDf%gbLQ(5QrWM%2zSQS;KhPh<<SwK2d>rlKW$zc_)Rg64Xza5M1xYmb7!FbYv(s#kW^ya_!X
R@6t&kl<Ah-z)uRcly|$H|*;^WTRYDA8Gm|;7KO{cVsgY%BppOy}$`-=?@-
4GCbkShg4|`qH<glz8e;G1Tv@#G3Em{;I!XvEJ4rFdQuW|EX5T9Viy*i8mlY1(aEJ-L}+`j(40mo5JQ}*qZ{9+h9par6-
SUwQ+ieg8dF-SlvIhQ!xMFi4f5|x2O8>DYn4kjIHlqz+P_@uNsv7V)0Qrme0%dlH${H%qU<4MzhKgL$!f(vAIpMQaXb7;Q;+
)DkMi2X1vLYTb0M+-T6acz6+$$uy&pdJ@`?-}U)@28+1=;FlU*U8=Q^#chTc3*Sr+bHOni-ef?Sr|fe*axa8!f8wPPULT2zT
3jswtd#RW&E*F)(jaE?Mt(Gh?VW5c9qYN%8?|9PhwPJ6i8N_LQ~;Y56X+8Dsq1AO)jmP?c9-
U4itK&Jo^#0Wb93~B96LIW`F?>aBd60v}X!3;dksolcro>RVa2bHoCuJcZzCLqmh7*JdXe}K|Gr%Pl=pq82vX@@VvgLQEc$?
7EpBn>0f#>RG?rg5<59xdP;v~tCs9|Of>%ij~701&bJ6IXy@9q2YgJ=h8Ma~0VH9S8RgNz#?_EQ`Ex{nBe}P^KaD^h6(5-
ny2sn#hD@am0cq?a$Kw70~>EkVDw3AR7%U{3E0pc|yAH%2Vk@!4;DsZ|Kvk<x0lbJObp*0^^w1hxhQUp+RiZHnyE1l(1m)QP
#y_>DSfH3wVmsVfQQMOV-&DSj8|YqzLizW9>q3&Ae+;`YzC#R`p>z=M$4EG3s$8$c!7va`HWY-
%_=Ixz^>u`Vv?56+5yhn#Xek0^!M4*_Q?;;b&cV8^=h-
Vg`M(#k|gwW>MGB+`xL>eL4(`W<+xHx!QPi+fFQTGvS*}b7p`p#`R|0uZqQ(ppVc@{+_!s8_msRD$;;|g1D96<cz|zfcM$CG
+3%4pvDy&^P5||O;WF}8I?yOKN1Vm`iP$-
$Wo#fFh+(Zm5oRiycOq&4E+SHEY{O#S(>8LkSqruX1Hy9kHfZbo)D_i<oVt9Pv>AOnw^)+rX_eEZ?qg)=d;5&ouVTnb1w*SN
vfW`@jwNF-`UC^dVgpMYp#9DMHP&FiCYmvW@bdBbcf;{DN_U)D^@=W>7Kgo_L$i0d^rAXg;DqzQ1dI$j>0BoujV3tt-
|h;2(5Pwo30yIbH8PG2f+tYd~Y@?$~pswmGu&Ia-?}{tUsq8s1nGUB<F{GLFu>DJ^e#TYEhr&y@XIREJP9e%qa-
!|GBn`{`ur-bD=8}lGx&UgO({}V3qV@^qSH_2HoGoV!>N@O&ihrDp2l`45{nirZ`a5<+J$lnK6;}jOXyv1Q&axKB!>0ZRW7{
rdR=}5tL0s!UtBNk(G0|Z;o7X5=AS4wE<u!Ar|R$c%veKK;6&BC8h18NeJ8Z;pkVzJ8(5h_&|__!uuMhTS@1@(Kn@yD$0HIl
(IvV!6Urr+n~~CP%VVAfY^Sv>yGw`gCCW#x*MhSiN}5HVHC?bAQd??L4Q@7D(e`Fx-XIos=qN&1I3W=LmLo9ENW8i&nnV3Hy
7gJTxCdXY&v<E(rM*fIfYVmbS^Te*TiR+;d^7foj|Wb1|pOMmfaPmE}o{slJ?<CUt^o));0Eyk;3XsHkfx?XB!=?wm%O<@t@
es<UXc#+M+uI?@_!@DO}z{Y3(U<_tq9KH4)|2lozoV-Hyka*n6t;nKz78DCQ!=FfET8lTscU71AfHe8@5vz7YY+M!JdMPsuX
@BPjYQyL2hU8O}sS%Vp4pHom`|E(Xd?07?f8`<ib@gCZcwHp7+GivpWriQFlJsl}?;kk4*qed$Tj$*B-
cGxKXnZ9+qKQ;vGeB%FZu6G(u=WAE*uvOy}^hFQJ7`%TU!p6X3SuyeJPJ>Rk-MuI$rAi6z7bXP=^&DR^}u{lstX=k`#cPt(}
+%nvuSnz?l9)+Rdwfw0>T6YHZ+)aEsCR|P~)YKDCS#o}4Mwq&Qq9^KHtHO|2I%?MW^SfC}D}NUVtAdKliBb^ar7rG;2@pqAL
>=l1#jUt|FaT`O|BvUgLpUR>X*92_w3FT9k&wM*$ng)BpB!EIm+V)l(NBdBH8L*3z@_@^VR^<lBB`tndl@aYaHw6ZKU!5flI
CTH+3}^SMx+ZcAE9KD3h~lJtl9r!mA(Onl7$0tU@z$bpU?=29HLQYFBug<uo`oSR`#L%m?1vzhM$`pezsnYyZgVu7X?<fo}V
QD)hmCBn|ANDFFTSve|8|0YrS_w<C%7Lu10~O8LTzvt9Hck#w~iw_s(GcyzOV)K&IJZq^}$uSISl_W*O(&x1N?OTsuDs43cv
!2EW&;$bX7j#$gx<`f+3=B`6C3TK@URTyUY5sCOdMH}4i4JD`U0X?3ooe!}&(6Nk=U(x9g^Ka|=(Q?70GTj4-o{MF8D#-
}nC3#&pOOM&rIZrxBa#zINju$jr_61tj%5!xPz7Ax~kemRj+QTGV&Chrt84L{qRn}?X6KVc~!Kf*@;2_Bh`x~(a@oZA0vr}X
RcY^md5!399=Cp&>$bUfN`qn+be{^}xMV)`7`xiC_XK(PZe^v|*~65PI>SbL;9anXua>kjJF+Zox2E0C3Qr)YgXOnVQXk8MT
>rK@R3maL#WHgKGiX~<s(B=+gH5T0zJ1mT{cZRHzlRh^6;#}+cie2oTj_jef$K=ino8`J#?ux921-
jo&_8FaNW3hdlzU2^PW8=2~SfOwZ-70<K2VJm+-v9VI+FH-AGb*=y$>tUTPOpUSuod@7*Z)%{(DR2&H7;TwGyOT$ZI7Di?Lg
eNM@;+^@Z^p3kb=aK31uVd)<t=j8_+KWwQ$Wy9M9e+J%jugwe0N8l_VI&oEsyLbqBlL&wnQFMnYmVk`kKw9#TVf7Z-
)OdXG~lrURIWngQsfz33VmM-hbE`TBL7wlLu@VmtJ^Ff~U8LQ=AbNKAp?m03_%Af4i^vNZ6}%9_ve9DI&ZzLn3vwW!k(tX<r
$c4xx()1EXp;KA{m+v6?6Bj<>I+W{eDS#{~}N{21_fZx;RU6V~M<>v)P?^|%lD@L{C8@><yT*K_A8M-
;j_@5N9d1!FEHEc2}e;D$u#<A{y=_hK9cYphHeQY@;S!{q2{koVV@Y_@#G@h2<zC9U@X1S=J|D4c@gb9ojL-
V#rYxC>~1VO9;FkD|X!+a_}h>3NJ_gcdxo4|5lR;PNw#d~p4(!oBL4o8$f1KbDsD+(^gsxSWxD%k$GjdOlJX@1WrNS$Y;e4V
ja#@w4FyK*5k4f5wEr4g&6(z?K;hb8{|lBn}%(4TfMLM{d%wU92tG=5D!}$}msjZLRL(SBw0nG6g@!CwpRo0>}_?TFPIUa<p
218NPQJj~jTIJ}S#zQEHum4c7Bv&b(4G;%riGYs@MzBNwwj9+vv?2Fi%nYGJ|2K~@$m=r)}r4(#N<^}Z4VP57hD7k+e7APA^
d)UXvqK^oUw`%uL~zCzjZ_+Z4Kl9u=S`@3qzZ&}Kz!2fc`j!veQzMR$5{^=eSAi&=!n(wgF%&Z&r7!Byl-
(gl2%u$gPS@5R;58too^GP6J5Kn|_!p@}Y6Z=a(ePtq~QuyMQmrZ>>OS6T}S}}WgHUV+0EhAmt!UMf?nNI1#4eoKIo@Cd~hG
Y=1_^}$8)p{yd6;)Nq26{4D2$36Vec7vES~H>ac^XqXCsVi<g4w>-W#Jz|YZEnw-Fqq%qAO7gM|d+cWvDp~FqQt~P%}%g6rA
BJw{ALq_tJ9WJ!SQ^a|T!$$Phf^_Gyavi=(n!U?rjO;<{7KQ{Ostej7TNW>vU?*T1Q$?G2e^ASCbipzDDu5jKNI-
$T4FOiHBt>t!F6h3Yq#V}o0doR9LNlx#O))+O)ABvYPD@CGLr_f?|5oq9DCcd>sb8V@GxAQk>_rdXO}(1MF>9tWoBM3ip(-
J^9c-`~?!P%4PB!~c~xiZ$fd|H~8KmjLFI;-
S=Uh$G`Bdwaq!BJ3?w><2lvvJ8@OkZUqA{`VEaUzr%i^qk@Yk{?ZRy#Y}lh2)Zke`r88Ta_AdUl*M%k&iWJ3&!Wv>n!m#Ox(
rrVd#D@xl{Ts4VCMTCm^L&?oZ6toBm8Ph%caPge`>2Ar=BFhq=)e=r)r{P-E<n>M&*zrA*zc+417Bj7Hp0DkFt{#t~f-
(_AOigVv$z0hHQ8go+Mg{9@p4gjl=)N#UjR8!gEtD(GMnqoO~jJzq@Td1ao>9k#)qQ`H12QBYJs0ID4ssQ*Q;)Cs*56(uf3@
lk@cR~DOsf=9UaTzPrEx`e)@?`7B>b$dWfF}?WSYQ*h>bi9()Jz6FCoP3D9Dq^P^JQ3d!HR(W{%m_Xd&Jy}uO@BvCuBOE(Vo
=FKes)BKbSPe{Y`M$?L$mMbFQD-
z76oIcgsKQ4f?s!V8;N*aoXmRVV!LpN%u$$56lQeM%OK=m56>JaLvVY#_%A5k_*wTkdA?)_J>BaZD(-
8x^%D&a<8eOb^{*SgkCnnL(##KXjW4nO_a$)ls8-O`rF&Y~;H!+aJ!7%(?n3hViRM#A-
@?S2*OC}G?RLS~ZZ8a2Z@pKjq$h9I9y|<z<Y1O#v3S@eJiuu{oH2tY4n`vHBwscWaGRuOH~9!@Jt%sc7Kx7-
4Qh<B>aEV$(NweU7v#1DbzsC7s=#L1s4jmK&E`eN$Zi>fJ)`NBaq2_BfadY*uxkpiNs0O~_QE#viByD5;ZKg?$)*+O(?@<>)
ZoIs(9)!Lh%UgwM6;nfG%3xkX;UmwSUPUZa=smER#V6EQHj;&k7#sYvDZ@$Dd3Jbl1D}ZLTU;$%=xGBMR~*yHMJXDg{j4xup
f_t><R5n>CVV=R>~kcn*j0W`c`~%Ht0r{F%I_SwI{Of8i{;wagzKFDh-
Ut#_##YD7*JLlrXYV8d@Inn@R@fBnQmbXiT6=PnhB?^o#C)h?L%$&@}=Lsp=4&Rkz3<9OM8?um5qT-
WeKM2GH&v5%RoA>(GoLBOBktai&^=cUj*orm$rv2GLnAk2;PL=zq14!^gMe>FfhYfF<9Om-sUUep^He>*CjuP!=rxV1q8dvL
nQ{XV%*iAyj8)4+*N|xH_aYWK@w-Q{fD2;N-
xmOqn!jMo(8YMDbPu94K%)3Ay)UCmdGa7>!5x1_TR_LNXN?=~O(5(Y8LD9KG~COCN_$I3d%P^B=B=Fn(7+NG45HE<CI2e|I(
lH-dZw53DDkEuN1RQjih2d&f3y_DY73ORPd_rR|9shAwctIGc*{*%i^^Ai7<SssZI(elLT3(dRB&=r0C3EDfkK(3$j?qy^*<
LEC}^8EajJZP5?Mz{X|(s1;|x)i<TsXcbHKHPTViLXv04DWgz!LaG&}7SEMx;r2lE_4eGs+98t<8fioumShkIqUv%t6d>m*0
Iv$(-
$B!WuueAL%>#RKPBSG5%iub}`#I+ukM%9J@0bDO!?WueWsE{EjF>cHCA!NG^WI+Pt<P<h&o=^BA*Sn;^ybsr_eUhG(SNe62V
{Dp%5ok~l5^FURv~G$OBN~{b8$CSqB5B|Y@F$EMP|tze?i)(jU1xcf(h0FV`D<@A#~L};R;9E>i<+?^%((mCoc7YezDm}v{x
IGKliOzB>Hrgt1-
R<vRB!X&^gU+o{i%a{G==GwGoTqE!14#pgL7q2a`$GugAfs*yMDCK|P@Co7(_zjWEw9i|#od!hkiHnDIr3&6q%K3R5F)VHh5
I^?IEryU--BIn*^M(KQ_{RBlNrm}^A%vEnjBqWUXC;Jw(qNPqN|CcG(&jMst!XW`|oONYCv8tONL7Y#5VHi2ko$OS|1g?)Bp
cO!Ny2}qY!&}8bzi0&T!%wDfNoIz<*$ouoIY^$VQ1G-
$?EZ0&#?qp~k4>>ahhq5Yfre4vzzM(hI&9`Vrq%L{5n>7ro9Cfl$QZ3C7uprB8DMc!tz|}_p*AJaKP*9#?k-
9~obTnS%$ADop1N`2w9_m1Swsjh&<@}$G5Vt@ue@Q~!HeL;7ALh^q#sx4r8^a<~8o8lWY~y(4r6y2iHSUHs{JWeMi`9Z^`<H
%g12KJu*4t#>Zwo^8R>3WKMktd*9V|K8w)*2Cu5jgM_n;0<f!D1Rx6buQbGtVpl%)&U4AtEv9BP^PQ-qI%^8m-
zmkd8?p$bI7Z#3K=oGdA`272Drr`}Dw-
0?aq!VkLD{ujv1Z2ug?{IwpI<Y3p?^N$Z|$y%v7cKl)O(ljh_zQko?l@;m)Xsldzf>dLy=wjJaRB9y9vS?p99XgB9j1oiFew
Q6}C!wwOnI(y-w`Kd6Re#QzArx|DHF_5{Wn20sZT*}GGJryBp<A}90|Sg*=d_qs@Ob=>rxfwGYX8=Ka5}C-
5<@JOn5zPLRMLaI)CswQWX-U4Wavann3T@cJ4qJxt-
=y)Y)7*@#D9e9QmGZp*r$je0M!%QuTQD>lrdU0*e|{zPx>>#j*~Y?*!~Vb{2zweprQ7iKr%*8U`|^AWU8C{qjP|+5@gITMP~
tzjFSvN&G2C<)*mYS6WqaXbIUJZ&|Jxe9;B7AzFt$L#+B_f^!vgFj#k<`@9*HjOFp`!u@F5QFrk84L62TUsdS0ttZ4((`-
vmJiV#hqh$IuI^*Z*pf)obGs(JI-pNb?3JjfisQ;m)>(~M(my~!v>(fy2b-
x#fMknWbXaJ#<WP#{FCRP3+DtN+{WYw=_U!386><m7wgV6XU9-a)25A`9Zg`fbEfI+X|-
2(W!WT==JncJ@e>Oi{UUbPF1C{3CCN7mjPp(V@-8Ez`nF9#0!Hd^aVL9sy?k&)W_<)-
KNrkUv@LZubxjp_tu6Xtn+8Rtot0iTDN~uoR0>V~lE}K!ElJ0Qtf@K59>eIy4<dlbr^HYyNZE+Cj+$@_s!;{}o3=;M-
65pz##%3Bc=Qkup~6W?mRMKHhQ*GOIF57pjn}*vgB21va0|Pr~NtS(v-
?GQ0SX{ssg)LP8)xJe(BZ<YNbUuD;z^fitgodLX~ePE)WE>Ycnyef%Nv)upV14CyB=kkGO<0=|;tf!=jqm#`N?39<pS_)`Gq
b{;$x=~9JY)Aq<xKq&CMnhNN_^g#RvBj>qMVErAnhbQzQhUM2m&}7CIf>XjZzypRy=U8|<9h{4boL-
KP8Ynoj9_7;bUY&yDzl{85Ez5S?9}2x$_fRE^5nC*U6B{uClWpWctRTb^I=j--Mo)D1Lsgvk$d$-w)uYCnG<-
GZsTcw2GF?`2!1$Y9RXTyTEPp~2=Rg@17W~!!A2I^ed9|;__hL6g(@H6}Fm*yl+`nFYz$Laf(uLZ_xscmxY|3?l&93zi1P%_
v!)!hgky>>J_(ty{fJyyLW#UJkOnU{3wbZRwtwaq=DF}<=3A2>ULgoSC3h!fN@_p!9JUCS<W#4B*0#4}(3mTlyt4^g5wd8QE
(#m<wi2_ig?evU<bKNUP1G0c3?_^SLjT4MQVr9n0qag_}SfBSK$2}iq7#@=sfGK7Igq;x(T{WA#I`51aHAQ9Q?uPEr1fktPY
HcFdoh&<^+poWNl+L)!^jdZV@ki;SfrdoAvAOnACB{@BONtvx%c?S2zk@T~w`~4dh>d(c383d#RZrgwECUanNvs^$JVz8@_=
2eYYEO%m%~@k!V4$?IuqbChy?#g8nBMpDmE1mYD{C^A(4yfN%xsj69l%kpcQTmYE*9$b8h?Uh3{J)!;!;uFL82#4kKvM#m`d
~tL@}f#p5nvyzAar`_%r=B9y^di<E9&G5knfy1w<a-
9F(BQ5Ht0!zzO5z8{ZYD_poXPt+1g6n5n&gEp<EhG6V~x_<~(MPmPlQOR*(FDqgb+iBS>96+r?w9zeY1!gk0qAS-
C3;GxEee5f}EMxS#|%ix}82EX#6%@T*LPF&mulz!4DJ9qLUI0|^$&%!dNv_Rv$(IE6H+q>`PY=eK(3jUj}8UYl)W*`btbRA7
SC&>QXwsW$!@^4dBIdrTGWN^IvYh6K`oJ3e%4{R1MuGgKuju|tM6O`WVL%4lZP!xvyFC$j+?~;|D+ldk(#Uz(Z=snjkwW15)
%>~tTLZwY!@gIB6H)4APqPbeoDIfim!Qo4>5O^JXRC5C$qxS!@AR&?)Oi%wdGyPLJ==;Nbap>t*?af1!U!&y-
)a3h!j3Qleu2K9V3r0#X1Op8!-PL3-SE_T)QN+p_!uc=b6j1n*47sX-ymoVy&~H~NOq!)v0y3Oiq9ETI48#73288D5yehwlJ
@CKLOH(^k32JBJVI(x#gzY@Y@ok%D8j<i(Rn=m@Ft}kLG8^u8_qytR?Gd))@;lozB*d?oakMh7HZ$gKcrsJZhq9tp#)4Dh6F
Vp%@0UGg5__3&iDgF3hj}m6{gGRCuOWT?_c=mU+<X@5q$yvC5#Z!y3;pTaIZyRUqSee}5hMC{9Bie=vaK_+X~_+C^brVkO8(
P5Kq}+7zRyp*_*IFEQ*$ui*FTWTm6yrb&^A%Ig}F_^k1T%8YgSgLE3Gz8RMm$`dE#Y^=QFc6G8u<Ga$lXPuX*$BbWy))n8Ss
lSw*v@GmUxfKeM<3A#!ZX&!W}B)hg+kreQ$OLx)9(C#<ImWdaz|<PllB%{E3LU~~_Q8DxQ=)GSuxp7BF!rYQrBXO;ONObd@l
s#?-
xa#9eN<sChevF3C!%+hPqbs$@tgrCNbFxXt~(v7JhMpbw$!>;GN7uQ9K)x*<BRiC?rA;of+b<Xo9FXMO~UICP+aFWVPDfG)G
i0ht5cYES)l{Vo-RNO}Gqj&eLy`=_SooD7vFayc_-C}&<z$RbjD1qNmNJ|Af-nAT_0m6hrYy0U~EDKCP;y!M@Q9YdW`J&wop
)DQNz{XuKZ4?wu)$4q!D|}?(UD@z;&IeSnp1#|D3J{Yjm}{bgq!Fn&Q$ykofSkCWx|KqrrGO_!D)c`RAjF7E^?E}{v(Amv?p
dQ1BCOhnaveKVC{>~w+G(keS@%9m05th8?bQ$gdsPCC7M?c3^rhvex~^q7KYMXLZW&jNt;6~p5VTt;xaIzrPYsZulthyL_Dg
~vVY<1(V6xJSe32*(Yp^SirC7>4B0Y0Rve<O!XuSYap~8{?7`+AR<r&^qR_eMUZyafu<~kUa1a{dGOo}H&HP1hY210m8Pe-
dHFY|8ixX(y?80}eLgA1cxyR^~wGLClv8I4HOscTCOt}Z*IIVav6(yp-jJHxVws=#_O4*kx~)uTTd2oS))VRY*3m4?gndC>x
Nkkh^~^53;KfV8n!#YoO#^Kl?7o<J>N;30g$P?G*p+&eW$A@Uwacg(v<vOJk9IAz6*5-2R8Wt^d^WR+LQF1792O*oQs``m-
$7Duwm&f?x42MyMt7>Cs9<Xr<iC`8`M!5qBZZ?eCCBcZ!-
Ezlhk28taRBSxEc4A*3mI`#)<!$`8s%sJ0;=$%(%7YS^_R|)8Qwak+{e~lN=i?8@XQ)>p^NVNn!2*B4GO4WnLt%=1p6lxxU2
X)7%MJo^g001W82v=nW`xAUjBfR=fF75T_goY;#;~TN#of`HK3Lr1NOC>krK66$`Y(Mlg`lrV-lcujcMa-
2^`R{j;Z$7qqqMj8Yu{&^43SOB{a(2G1Qke^l$9rRVVW6)1gmMsyS*|!k+<o5XFRc6G4Q7ACi2@1vr}hbhXCw=|jDD$9C^$p
&Yq!ujJ-
9i&;@af?oZ%+K;?BC9Er5T%yf)wQef~i_V+86QI(`~nfBUI{Mt>6EqoqqsYHusTg8ca232NSxM;iVb9fyU?|5k?gy#edx#pu
QViWUye*n#w{PF_h(UoU{1e+C3wpa`)mUx4MO2~Nb%<X*w@knyhn63zQ?h%p{y?IItR9fh6lYtPp(5^oW#_8pZ;Einzw#tn$
F9)v`x!yHMOYb~V7h9j6@Lr3wNyGn{sD<FDV`tdeeeG&SZ5lX6_-C_F8`Fz^cW7H10KW}-D-
7b+UgK~vKC(_b8)x1ezaxd!FJQ8)1u15OVJdi-w_QSDH!A+z5L5q|*NcL<uRa9cQIwM}$KAq(ulcS@*4${pIQImoLK{<thI2
wnOgfooWP;Wt}^2z{m)_M6>yM?;Ce8XT!=4#Y0d@+l4sV*ub#Ba2ig)BUfBA8(~Pk^@Y&iq{+iL}0}j4ol#J@{Gsk+{s-
Ru6ar1OptE-
M1+UC9#+nZd0ny@$?~M4jpVr29*O&Z0NyOR@h}2FDPgHh*k&GQUjku4vIK|r2yX+KKMby@e3c=KUx8>B_b2V$;}fF2IssV-
`?LoDgFze#b^n9O`<x-
P5u>kxg5Z~%l<QAq4YmD)|?>R`^As$K@<yOwSDjNRGI3&W=#q!==B}s^vz;$7XzV9SLznUG4CE5NJ(!ByZjD24pr^(0dq|?)
8Jo-M!}t*^0EH-GOw9Af00_(u|bLE<^L}7>{F0g4)_NQ*(s(9+*{n|n1&E$l$ER=9N?al7OOmxwkiy!^~;7gqUD*(WfJJk&Q
!-Wio2~H-
V7?oK>?Mi?9szul+8dpt?AK;DsqPy{X9&LuC1#h2{Ot95Q9C7Z=uuCt>F}vT~iWU)BCjbia>(66%PzOv&>_J>P(80yWrm;ft
ExqfEwuGyjV85SCC=UVfdy5$gDho+u%bexv;ttiB{++j;Bg9{1HzP42LZdzP~m%gFfmXz>f`hZ8PsI<{S9))6h1F$kA7*ntu
y$`FNQZit4>h+v8BaR<K6!7^fZxEb8abzaQdSRR_g}j;aO^1X~8{t6?u3*?<xkNlbk(35O#)nP8`A9Q|how}XU!el0qDV*dh
$;JR8KVgC!y2CzT;e!$LS!zk&&d84S(Pc%|PaYSV-v()>o{RLDDdM0A!ks~=bPB_REV%dwx8l0ZIB|muj(CKM=y@Pi=I2dc-
g&o3@(7ak#NCOW>I0JAYQak2$ltet4lp+)p^jV9wab&<!l!rfi6+-
7Cxlp;gg)D48{APm8!2LEO=rK#@RXIc&jTdybjgE`xKnWOTH4&E6#uSwzqywN%blU#z0mtOnQDs9R$1D*Bn7_Pjjrp<Bm1zc
gLJG3xcG7j}|8`n>{QHOzUN=KIryGpsH?^c%q8-
QXLsh+Lh;%4K;@p*=N%dFJh_9vZ&^)izOR=AD7^~lZ1kc053n8V=UzXmsqI1i_VS%F;9C6p`)y1Sez@+SbYkhr0Fj-
X4`U3wDEH?Sa>2J^%*gmxSnMuWxwVfKI(>eNzR#jk}r1q;%)4?&-
LcU#lOavv46qLsgXJfj6L0>8`{FxugQNhs$F1XEW57SMP!fSuyy&2W@VMU?M{zxQYbU^@=vI9s@sWm`LQck|#aBiPGico;Tq
Tgp|Gsta(q#maf5jsS)K0u!nQwS~zvu5Yf*79RL%%8K7{@{}G`T;8OCAdjX>lth9P=Z8`XfxNWA1=`hza7K8Hz5C@ErKaEWw
#gjIsSVWXFmr&3z}~H_PYOq7j^NX?z@bzaYwkOQBdjA_jRwRz$Y?E;SJ9=WSvuNY|!7&m*I}aD9Iv^FziGEn`39a@u#m1Vc7
jUt>?|j;i8axOQ+^qb#Ut};<=P_zKxceHu}%Y6=O832Z<mx!OZ`Tl(RJt|3+t)J8}wE8A=0kj8q0T01xeNRNsdL8AhmMe2B4
#hj{QWoFd6gi<Q+lAy~T1iM$06r5^&VC|5nHuUVul4A^v-PzuGx*lhj^-z#X*jFo_g>2Y}Dm6C!d0HB<;chH>9-
{U|?oB;ltPr~~EKrbZ3eS$HNrl`WJK(#5LX23K+4?kt(9~9yy{gxRJ4iA$*(Z{*eF3u#*T$t=%qchWYxkM}$mWN4r9l=lgRZ
-EUVc<HIQ>7DW!tpMJ;U&G>P#UvqV78aO-
V4oMl5A+fvV0@iEWbQ|ZarzPy9!RCZ$H4|x}iE+t0aW?*j;c8^t$PDxUkY|EP>}dB%A7>b0-
0YnK**3=~dGPAPp<R>O^71Q7U;R2^N80E~D~EB6~xh(U7le?6YuMVArqWm2m=A8T<Cr@4yZx&W&;UNbw9Z3K7qKX&D7|#mAm
Ar`Vw&Wr%UBvDgMAm)9BV&yVHp^CUA;)b-|q)j6}~*x!$Tf|$1-
`ncQcnrZY%ysp4S<ZC%D(?zDSDc{7|UB@Bk#nAdcmzu+l`?`dROEyIL{S&VW<!Fi-c6AAK$l4t89a91vo>0-
h9j44V7fI(jCGvLQ0Gu-ej30Ab#H<%2_IkBmuiPvS39!v;tcT(iTJ+Qwe}0?jfqkR}7VKT%vMgrhpBVwe-if3Dy6Ev-Uk6E1
bF;2k3|V<ZLCIK?`-CFciAp%Df?r=uW++DRGHvl*(n%esQj^A}pjt9B!*I{>>($gh5}U`hzjSira0NL=;{!7Fui+zpEJJmw-
r%#8X*{+|-S5F$)IasiqqjamX<9N#?t_SkyjYCqRcY;y;-Yf~a-
lTU<Nd1s(@TzLgblc)e0RlO`X1qGYb9azo5_?1X|~GCCQuYmEG>@>yyTyzVv}{vHiwHw@|QH)XuNJ2+;JD0N)FUVl~30^h;S
Fl^GtJ+j4EGY+{<bj02Ou1dxVxjuf4`lE0e9dEnkG24blRp4~L|*7o4;Hdy45Xs-CU4a8e?4f79YD=L|@i@b8L6wjZpa!2g-
Fo()}gRN)$AjrG|?ypfsm3^kyPPE|3u_;<&B?L9$>@sMQpYSy;MD_z1~uLYfECz!?aVUXCZ$rHWW#z(vJo}ztpq^2BY#b5~X
<}LMHs1ScmwR-
O&fHW$Z515Y_nb5lnU65nBfj<WfkRk9N`55n?ppoX7g)RGRgvBXL2j4ddn^W0y>DJ+wS5q)S4yI9*K}l?(@E)Zx7!ZPP1iXL
W=zkm=8mh9C&vy`u-
LBt~oPZ!|$$WGMR7^+X(|?}j%^C2;(#G}?b%8p9Y(sgHaoH4@ULZEJYgfg#w+ShhG#lBE^};ZjFE=E1mp8A4E_@87qMO9>=Z
Uv$R=)$fAq55e24#fA;nhF?dzY!;l^pyZLXX&{LOR;_%y9UP2x3Dn0~es}L`gt~4&Vpmm$qu{5iRSiGtIDdlUhRQSMS6aTj!
Rd#V)}&;65Z-+%2tAs`GPvIeQ)VvSD6gqMab3h<OChiXf>aZh(#@ZM3fVLeTH9^8`Fh1xbcaw6{2;nuE2^WNFD|JY=Xc0-
DC6#OfHIN<7SeLFRlvQ~Z~(KO(|OI9Bv$GM=PcCsL<~*7(j)0VEakDTj*2@_ctQ_K-v5dZ4Ctl(-^k<DuT23d;(1L_-
ojY1io$V6%9CP`2abACcPL^_-0FPJs5~-ImVKn(kU)b~1HOp2W~JglR%mKC^lQw-
gO&fQlbg8<B&i{Ih`VEbu4-$vB9>7MimUmDm1-DZ-vc02HdxQ<66o`xNrSSSUTn;K2?!GBRpe5h(CTk`ki>E|Gr=e@^+h-
okfC02&tY+oV7X8?7fTS67IeU#YB~*)b-|&6VxbIc=~W{yzK5HYNx*P^*WIiDl+(WeRo^hun5F#M-
4o%*8t!bC3|0HF8Q$1btMgN}EERbE8{&;QIYJy+EOxRt@$5ah;FOgE3ycn^iN<ZgK9cK^&MaxYk}(GT;?y>m@Qg^*4daOt`!
IvV1{Fe05_I;}p|ITcjUrg=Y_0v7;&ouY<3_*Z-jOhP-0F#@;Pl`A;;DrfF9<DNUK0M-GqurN47=crT8{EdwJQL^;i0-
1lgwadYpEz<CLdtjpY96^7%jJ^7V#TiZ#AN2JNiV;Xa-NoT>x=h6?O4H%kewzCGFqM^MZP=`Vb+qKJnGr#Mwc4Smns<20@w%
#SB_&idt-
7xmZu>u;BZp8J>b(X1M5~5Uvhcg!bCQd}aS2h10WSxj(YvvrUNZff5bddNhf*+!t#M%xIyP@+5YPg@c222kN3n5NoIJ4UL!%
|~y+P5}cW;9T?C(i@$9)j2U#?s!v@>}_>`E>s`9V@%E3wljVvt^NGZGbLdFGSPiM&>E!mqd(7$~2OfmpZg!B(Vn)<lQhM(#P
3(vYXPEcslNI6I8>0{~sfB5$L%`=xXyO#DG}9{9RWxr9tM{#$g4*Un8V|3zvD-
?kQP4CEH!a96_NTbFlO9Ei}3px%S?iq$>m5=1uj&Xr@)|aW0hcv5>#49%2h5B?kOHOLL0fivLL0m^SZWY8~Nmw;|(oQs=`u?
YmBTmUKQdM;m7In~%}Ts8H>tR)I__wfVk1M43WS|Gie^>LQYb*vSNLTXLcQ)c5SV8$nzVZDeG|s+BY_|D((Y4!ya3>#G`@nl
Gd{2ZvuGSc<PX{mk|5Dr#k3Bvs?0sx2@R18j!UhIWeU97)ZUB-
j$;a*b^~h4vBzZ~al{!Em;Ln#Hrx7y{Df)kHHtLycS*i#%%;zB=0I+L<a;MX<M>Ez#f`HbLZ9Pq@cBD}vbD=1+gMB28{N$pY
`7+ikq19oM$lbry^P#rw-PKwN+6*q1nKZTRQkV<_Z31A##cg%-ZO+M0&-m&23k({}#-
dqc~RN94+^OcMjHGGFkg6j3Z7UYLw07c^B0lzu9;Q6;0vFT^JoG;eMt9~neynRFfHU8|iyw8ZMaj?bEbPMOpbYd0`T^neNPG
ir^FPnaSGR!Ur|p19d0MS6QadkRtL-wz#15sipXh>=c+Gx6XOd!UuYG<uOmteBHmr9TD*&%a<XKwBy}PmN~l;EMbMXtXT)TP
l!R5-B*a6$4z7I%wzjb0?jNE6VPJwF3Rc-@N2r(iO(K^5=1Ml~A+8{CGFU+~l-
@&qCTqB9LAf8rc;jd*%@{ff!N~UYGwn8Dl5R3`hdHAZCA_S93n@P2q~mf17$WTn7)%L)(WPbjsj5@*X#EPqLg&sCelBvaM!r
YOuAV=`zvz=1T>!dEbpo`_emh{fNZRm&>ylctPGaXv6yJ0eB#EC8Td?kW{M}Mb3H<GS!1bA9ucRV+flAcDPru4)c|Ru54Qz?
S{(0cf{O!9$iK8id|J27@O+rSLT-
8(SAeswpXs;RiH^9SN%kHImsV|pS%earwM_+f@2cv1W>%t02+mTkCp%Jyd;3M0UuT4<Ch5shGw@^*XR<^w(Yb-iV204p8~*o
?N$%+?T|`|Y)C*iOBu$e7i_&f@&@Y)L#47fY0V$wgXDYhz1yH?vq*BL5hYr!E6jYJS{=w$aJ&MxLOHss-
*|k$kQFQ729#srMYQ2&>#(e@r&IX$YUxBYp7Ks9hssHOw=5IoF`v-pnNmA<h>14-U&W(UZlC-
g!edF}KQ5loTZHm>BMHR((^%9pTV>5Pz8tj_;gd$>i7;W&aV!-fKhC~_0PVr`&w&+;R<x3upJF({-
iCiKhsON|@C^n}_Cpr&>c@$zT87*Yn3Py#YoutWgBnJg2=kXqB4NI7{yavBZAKNcV=@ypPv%X!f;M>oSM!vvF&qHzKVd#K6D
cKwzpJe@q_Ue9iDUA|qKofDzWaZ}14-
O}IEq%!HJIOfvd@ZZ{ogeU>pFD8^5h~DI_MeltSDYpae{>0Oc&acdRu3=#`?cvYe?cBdu|X#Run>cfM`vmjZ`X!fbA_U`wHf
o;MARS*ge0yqSnhiT~x`m?9QG;8YcPJJKJ|Iv8rysP0o-fV+e1Wl9o?Q`RI@p-
rer*BmmFEZQ~8qML@J)naANU{2pgy%~JV0{|VzU86Zt#?qY09uXZaI^2;5O?IpvJy}A9o@BL8|Dx^1HyY-
3e;}c;bnLwDO(W{L|w9fgMcCW<`c+DErjEW>Zp;Uk4?D+pCFibNZd=;-
a+BXTLAgd&$GT%2pAYVl;J1p3sTFe>Z^cU}+HxaMQcWILC&DkA1f-X*Rr=uNe+iBySlh#V603=aF<;bABq>kW-
b9>3#;TQ6Dyz7Ug7=Il@kuK*BD=|Hn(ZKW%u+g>y_Idv9C^<sVZgq_9Dm0tV6BWIy_sF5B<>7NKXU0rQFV7o5=>JPg%N?D6Q
BE(w)^TfJQGciyjQhG<+o+uLU_p#1%Ak5p4ct-
g@*9iala*|XXGy`K@tjhgBrz@kVke^^52@$i00G?I0pH#U?2KZ_vBYQl0ssI200dcD
'''
raw=lzma.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==159583 and hashlib.sha256(raw).hexdigest()=='500bf3b2efa31f3e4a3910e36344879a08c8eb97fb4219f6caacebf100ed1a2d'
FILES={'bevel_shapes.py': [19751, '163cd4725da72966a701f066c872fd1eeb9d00cd419cc73219674a41973227d8'], 'verify_shapes.py': [7686, '3ae81936a0cedec66880f53607deeb4eed0ed6a25fa873589915cfa34ef8364d'], 'compact.json': [23691, '223b1decdb52bb8a42e8986f3419007df3f8468d17ba6539a3198c8e47492fb0'], 'discover.py': [10371, '50bf3efed836f095a9b4128ca91700481dfe8624b8309393d367b0fe7102e907'], 'minimize.py': [1407, 'dabaaf31e03f6065c9c5b01ce3c6116efac9a7c262e4f86977ed4ceccb111a51'], 'bevel_chart_sector.py': [6487, 'b72ac5c2b86c32f598bbb442b707fc8a159d0dbe99608f5e9b7442964f4e0b08'], 'incoming_manifest.json': [454, '43b589ef11a81466e125153c9d644ce376b0afbf7e354969e65e26a230091c56'], 'recover_incoming.py': [2471, 'fc6c5ce487719780dd3a75ee511c86eaa4a42dd52130f1f5a732e4f8a4a066a2'], 'projective_probe.py': [5315, 'b75b6bdd2f4997016e6ec6b0c159582b24a158017f13011541e2046d24931ebd'], 'prune_projective.py': [1835, 'd7f85310e26e2d1cfcea1eaf13b1c38b80530e68255ebc966b0891472c5811df'], 'projective_certificate.py': [7266, 'a993cbc0a50200a5a2bbaba06d151a9f07ac13698f348b7fea00a89bb2794f46'], 'verify_projective.py': [6360, '8aad7b5742bbc3b16067374ef1a7aab0ddf0f8f6bb51459d522e3533c2945c6a'], 'projective_compact.json': [12712, '5a2c714980ea8176daf8fc337bb20789e314b3321b8c1ef5b71a6e470921d8b0'], 'projective_progress_frozen.json': [51705, '76191b4710842962daa5848d16271bd2353245d07c3ca14fb84dea529d0df256']}
OUTPUTS={'bevel_shapes.json': [144340, '8839126439eca33d25e1441ee673726759bdcfee7efab55b2b7607b62569a70a'], 'bevel_chart_sector.json': [18825, 'e4963d4ec0f7e9bfd9166e7edf5789c20b3b62483dd27764a4cb9e1685709bc1'], 'projective_pencil.json': [154203, 'f98b10fcd389c804176b45630ccce71f5a9fc3ece286aa9a9c2f5fc42618cbf1']}
root=Path(__file__).resolve().parent
files=json.loads(raw);assert set(files)==set(FILES)
for name,text in files.items():
    b=text.encode();size,sha=FILES[name]
    assert len(b)==size and hashlib.sha256(b).hexdigest()==sha
    p=root/name
    if p.exists():assert p.read_bytes()==b, 'Refuse to overwrite different source: '+name
    p.write_bytes(b)
if sys.argv[1]=='sources':
    print('COMPLETE_396_AND_395_ROW_TABLES_AND_FOURTEEN_PAYLOADS_RESTORED')
else:
    for name,args in [('recover_incoming.py',[]),('bevel_shapes.py',[sys.argv[1]]),('verify_shapes.py',[]),('bevel_chart_sector.py',[]),('projective_certificate.py',[sys.argv[1]]),('verify_projective.py',[])]:
        subprocess.run([sys.executable,'-S',name]+args,cwd=root,check=True)
    for name,(size,sha) in OUTPUTS.items():
        b=(root/name).read_bytes();assert len(b)==size and hashlib.sha256(b).hexdigest()==sha
    print('BEVEL_FOUR_SHAPE_AND_NONPARALLEL_ALL_SPD_DURABLE_RECOVERY_PASS')
```
