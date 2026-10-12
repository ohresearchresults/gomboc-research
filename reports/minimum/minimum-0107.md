# minimum-0107

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# BEVEL_COMPLETE_POSITIVE_PROJECTIVE_PENCIL_ALL_SPD_U2_V1

## 1. Главный результат и его точная граница

**Весь положительный проективный pencil закрыт, включая оба ранее открытых конца.** Пусть B — буквальное тело P(1/4,1/4,2,3) из parent, а

`T_h(x,y,z)=(x,y,z)/(1+h y)`.

Для **каждого −1/2<h<1**, после равномерного заполнения T_h(B) и вычисления его **настоящего нового объёмного центра масс**, при **каждой** положительно определённой метрике M, с одной сопряжённой N=M⁻¹, имеются **как минимум две строгие неустойчивые вершины**. Никаких ограничений на обусловленность, S1, H0 или дополнительные слабые равновесия не требуется. Все совместные невырожденные аффинные образы включены.

Это не продолжение прежнего ограниченного метрического конуса. Закрыта вся геометрическая полуоткрытая у обоих концов область, на которой знаменатель проективного отображения положителен. В частности, включены формы сколь угодно близкие к h=−1/2 и h=1.

**Граница U2 точна для каждой формы pencil.** Ниже дан общий конечный алгоритм выбора двух ортогональных направлений, который для каждого рационального h строит рациональное евклидово тело с собственным COM0 и strict(S,U,H)=(2,2,2), weak000. Аналитическое доказательство работает и для каждого вещественного h. Следовательно

`min_{M>0} U_strict(T_h(B),M)=2` для каждого `−1/2<h<1`.

Дополнительно точными непрерывными знаковыми сертификатами сохранены две простые **222weak000-семьи на целых концевых интервалах**, с фиксированными списками строгих элементов и явно взаимно обратными метриками.

Не получены полный запрет11-мерного пространства реализаций, запрет всех трёхпараметрических положительных проективных образов B или новый110-аттейнер. **34≤C_min≤622 и все глобальные E17/FULL/LOCAL/root-счётчики остаются неизменными.**

## 2. Прочтение, буквальный parent и сохранённые зависимости

Новый `research-journal(20260919-112719).md` прочитан последовательно целиком, все1996 строк, включая весь буквальный parent и его полную recovery. Файл имеет333443 bytes, SHA-256 `5f913de1571df8bbcd56023f0831339308e9881b79341f99ca7c599858ccdcc2`. Неизменённые ранее прочитанные источники не заменялись предположениями. Нужные исходники parent восстановлены и прочитаны полностью; отсутствующей вычислительной зависимости нет.

Авторитетный parent — `minimum-0104`, SHA-256 `4ff810064e672e253e9b78e0d59fcc525651da2a11f45e228cca436de13bad41`, **BEVEL_FOUR_SHAPE_AND_NONPARALLEL_ALL_SPD_U2_V1**. :contentReference[oaicite:0]{index=0}

Его полный четырёхпараметрический all-SPD запрет и непараллельный сектор −1/4≤h≤1/2 приняты как прежние результаты. Открытыми у отдельного pencil были именно −1/2<h<−1/4 и1/2<h<1; нового метрического остатка внутри прежнего сектора не было. Эти два геометрических остатка теперь устранены. :contentReference[oaicite:1]{index=1}

Нового конфликта меток, решётки, массы или source authority не найдено. Уже исправленная parent-граница396vs548 не переоткрывалась. Новый конечный сертификат вычислен с пустым набором начальных строк и **не требует старых396 или395 строк** для восстановления либо проверки.

## 3. Полная настоящая геометрия и собственная масса

### 3.1. Буквальные вершины, максимальные грани и рёбра

Исходные вершины v_i тела B:

```
0=(-1,-1,-3/4)  1=(-1,-1,1)  2=(-1,-3/4,-1)
3=(-1,1,-1)     4=(-1,1,1)
5=(1,-1,-3/4)   6=(1,-1,1)   7=(1,-3/4,-1)
8=(1,1,-1)      9=(1,2,3).
```

Максимальные наружные циклы, с сохранением номеров parent:

```
F0=(0,1,4,3,2)  F1=(1,9,4)  F2=(3,4,9)
F3=(0,5,6,1)    F4=(1,6,9)  F5=(2,3,8,7)
F6=(3,9,8)      F7=(5,7,8,9,6)  F8=(0,2,7,5).
```

Все истинные рёбра в постоянном лексикографическом порядке:

```
(0,1),(0,2),(0,5),(1,4),(1,6),(1,9),(2,3),(2,7),(3,4),
(3,8),(3,9),(4,9),(5,6),(5,7),(6,9),(7,8),(8,9).
```

Исходные поддержки A_i·x≤H_i:

```
A0=(-1,0,0), H0=1
A1=(-2,0,2), H1=4
A2=(-1,2,0), H2=3
A3=(0,-1,0), H3=1
A4=(0,-2,3), H4=5
A5=(0,0,-1), H5=1
A6=(0,4,-1), H6=5
A7=(1,0,0), H7=1
A8=(0,-1,-1), H8=7/4.
```

Пусть `l_i(h)=1+h(v_i)_y`, `Y_i(h)=v_i/l_i(h)`. Возможны ровно четыре линейных знаменателя:

`1−h, 1−3h/4, 1+h, 1+2h`.

Все они положительны **в точности при −1/2<h<1**. На этой области T_h невырождено и сохраняет ограниченность, выпуклость, все метки и полную решётку. Новые настоящие поддержки имеют вид

`n_i(h)·Y≤H_i`, где `n_i(h)=A_i+H_i h e_y`.

Их неинцидентные slacks равны исходным положительным slacks, делённым на l_i. Поэтому вся физическая область имеет настоящие V10/E17/F9, размеры граней5,3,3,4,3,4,3,5,4. Триангуляционные диагонали используются только для интегрирования.

Полнота исходной решётки дополнительно проверена точными поддержками и строгими внутренними сторонами всех полигональных рёбер. Каждый перечисленный отрезок является пересечением двух настоящих поддержек; замкнутый связный комплекс исчерпывает границу. Для32 конечных контролей независимо восстановлены все допустимые пересечения84 троек H-плоскостей.

При h≠0 пятиугольники F0,F7 непараллельны: их нормали (−1,h,0),(1,h,0) имеют векторное произведение (0,0,−2h). h=0 — настоящая форма с параллельными гранями, **не** переход решётки.

### 3.2. Объём и COM всего pencil в замкнутой рациональной форме

Определим

```
Q(h)=226h^4−563h^3+1022h²−1747h+1146,
D_V(h)=(1−h)^3(1+h)^2(1+2h)(4−3h)^2,
d(h)=32(1−h)(1+h)(1+2h)(4−3h)Q(h),

m_x(h)=64(1−h)^2(4−3h)^3(h²+3),
m_y(h)=8(5424h^7−17116h^6+39492h^5−82269h^4
          +65409h^3+28077h²−45225h+4696),
m_z(h)=3716h^7+3232h^6−25527h^5+58535h^4
        −145021h^3+228077h²−183644h+62144.
```

Тогда настоящие равномерные интегралы дают

`Vol(T_h(B))=Q(h)/(6D_V(h))`,

`g(h)=(m_x(h),m_y(h),m_z(h))/d(h)`.

Все знаменатели положительны на физической области. Полные коэффициенты Бернштейна Q на замкнутом [−1/2,1] равны

`(4719/2,35853/32,5667/8,267,84)`

и строго положительны.

Это не перенос T_h(g(0)). Для каждого из16 ориентированных треугольников τ=(i,j,k) настоящей границы, полученных веером из первой вершины соответствующей грани, положим d_τ=det(v_i,v_j,v_k)>0. Тогда непосредственно

```
S(h)=Στ dτ/(li lj lk),
J(h)=Στ [dτ/(li lj lk)](vi/li+vj/lj+vk/lk),
Vol=S/6,  g=J/(4S).
```

Источник раскрывает эти рациональные тождества в точном полиномиальном кольце. Независимая проверка подтверждает их с явными верхними границами степеней. При h=0 возвращаются Vol=191/16 и g=(16/191,587/2292,971/2292).

## 4. Новый механизм: нормировка геометрии у обоих открытых концов

Прямое продолжение старого полиномиального поля до вырождающихся концов плохо обусловлено не из-за оставшегося большого κ, а из-за ухода настоящих координат в бесконечность. Использованы две **аффинные нормировки самих форм**, зависящие от h, с точным снятием положительных факторов настоящих стрелок.

### 4.1. Одно исходное поле настоящих механических стрелок

Порядок34 стрелок — по исходной вершине, затем по конечной. Для каждого базового ребра запишем `v_j−v_i=s_ij e_ij(0)` с s_ij>0. Если ребро инцидентно9, s_ij=1; для02 и57 берётся s_ij=1/4; для остальных s_ij=max абсолютных координат базовой разности.

Положим

```
C(h)=(1−h)^4(1−3h/4)^3(1+h)^3(1+2h)^2,
W_i=C(h)(4S(h)Y_i−J(h)),
e_ij(h)=(li vj−lj vi)/s_ij,
B_ij=W_i e_ij^T+e_ij W_i^T.
```

Все W_i и B_ij полиномиальны; степень B_ij не превышает8. Настоящая разность Y_j−Y_i равна `s_ij e_ij/(li lj)`. При x_i=Y_i−g и D_ij=x_iᵀM(x_j−x_i) имеем точное равенство

`tr(MB_ij)=8C S li lj D_ij/s_ij`.

Все очищающие множители положительны. Здесь всегда используются одна настоящая масса и одна M.

### 4.2. Левая нормировка

```
A_-(h)=((1,-1/2,0),(0,-3/2,1),(0,1+2h,0)),
ell_-(h)=1+2h,  det A_-=-ell_-.
```

На физической области A_- обратима. Матрицы

`Bhat^-_ij=A_- B_ij A_-^T / ell_-^(1+1_{9∈{i,j}})`

после **точного деления** являются полиномами степени≤7. Никакое приближённое усечение ряда не применяется. Проверяется каждая из34 степеней снятого фактора.

### 4.3. Правая нормировка

```
A_+(h)=(1−h)I,  ell_+(h)=1−h.
```

Матрицы

`Bhat^+_ij=A_+ B_ij A_+^T / ell_+^(2+1_{{i,j}⊂{0,1,5,6}})`

полиномиальны степени≤8. Эквивалентно, Bhat^+=B на остальных рёбрах и Bhat^+=B/(1−h) на четырёх рёбрах настоящей F3.

Для любой исходной M>0 соответствующая метрика нормированного тела есть `Mhat=A^-T M A^-1>0`; преобразование является биекцией всего SPD-конуса для каждого физического h. В частности, зависимость A от h **не** ограничивает метрику и не подменяет её двумя независимыми выборами. Объёмный COM при этой последующей аффинной нормировке переходит именно в Ag(h).

## 5. Полное конечное доказательство U≥2

### 5.1. Все настоящие корневые деревья, включая нулевые выходы

Если вершина не строго неустойчива, её касательный конус даёт настоящий соседний слабый выход D_ij≥0. При нём

`|x_j|_M²−|x_i|_M²=2D_ij+|x_j−x_i|_M²>0`,

включая равенство D_ij=0. Поэтому U1 породило бы корневое остовное дерево истинного графа. Максимум нормы всегда является строгой U-вершиной, даже при нескольких совпадающих максимальных нормах.

Из всех C(17,9)=24310 рёберных подмножеств ровно5440 — остовные деревья. Для каждого из10 корней получается одна ориентация: всего54400 наборов слабых истинных стрелок. Независимое перечисление530712 функций выбора соседей даёт тот же полный набор после удаления циклов.

### 5.2. Все коэффициенты и всё непрерывное покрытие

Каждая буквальная строка R задаёт положительные целые λ и полином

`K_R(h)=−Σ_(ij∈R) λ_ij Bhat_ij(h)`.

Если все её настоящие стрелки слабые, `tr(Mhat K_R)≤0`. Если K_R>0, это противоречит Mhat>0. Достаточно поэтому покрыть каждое настоящее корневое дерево хотя бы одной такой строкой.

Полные данные нового сертификата:

| Поле и закрытая алгебраическая клетка | Назначенные строки | Степень | PD-блоки | Корневые деревья |
|---|---:|---:|---:|---:|
|left, [−1/2,0]|277|7|2216|54400|
|right, [0,1/2]|256|8|2304|54400|
|right, [1/2,1]|260|8|2340|54400|

Всего **725 буквальных строк,2946 положительных членов,793 применения,6860 PD-матриц3×3,20580 положительных ведущих миноров и163200 проверок «клетка × настоящее корневое дерево»**.

Левая таблица:277 строк,1066 членов, λ1…51; длины114×3,106×4,43×5,13×6,1×7. Правая таблица:448 строк,1880 членов, λ1…442; длины114×3,169×4,130×5,33×6,2×7. Правая строка может применяться в обеих клетках; это учтено отдельно, не сложено как разные геометрии.

Каждая запись K_R представляется в **полном** базисе Бернштейна соответствующей степени на своей клетке. Все её коэффициентные матрицы положительно определены. Поэтому K_R(h)>0 на всей клетке, поскольку веса базиса неотрицательны и суммируются в1. Все списки строк, клеток и применений буквально находятся в нижеследующей recovery; положительность не выводится из конечной выборки h.

Каждое из54400 деревьев покрыто в каждой из трёх клеток. Их объединение содержит всю физическую область −1/2<h<1. Внутренние стыки h=0 и h=1/2 включены. Алгебраические внешние концы использованы для доказательства знаков полиномов, но не объявляются физическими членами pencil.

**Следовательно U1 невозможно при любой M>0 на всём положительном pencil.**

### 5.3. Независимая проверка

`verify_pencil.py` не импортирует builder. Он восстанавливает исходные механические выражения через настоящий объёмный интеграл и обе нормировки, проверяет полиномиальные тождества на22 точных рациональных узлах при доказанных границах степеней, затем строит Bernstein-матрицы независимой интерполяцией. Это проверка **тождеств**, не sampling-положительность.

Положительность6860 матриц проверяется рациональными дополнениями Шура, отдельно от формул ведущих миноров builder. Совпадают полные канонические матричные потоки. Деревья независимо перечисляются через функции родителей. Для32 конечных контролей истинные объём, COM и ковариация дополнительно проверены положительным веером из вершины9, независимо от конусов из начала.

Минимальные ведущие миноры после примитивной целочисленной нормировки в трёх клетках равны321,4200,32. Это арифметическая характеристика данного сертификата, не физически инвариантный запас по метрике.

## 6. Что действительно происходит у исключённых концов

### 6.1. Левая предельная форма

При h→−1/2+ нормированные вершины A_-(h)Y_i(h) имеют следующие **полные десять помеченных пределов**:

```
0=(-1/3,1/2,0)  1=(-1/3,5/3,0)  2=(-5/11,1/11,0)
3=(-3,-5,0)     4=(-3,-1,0)
5=(1,1/2,0)     6=(1,5/3,0)     7=(1,1/11,0)
8=(1,-5,0)      9=(0,0,2).
```

Настоящая предельная оболочка — пятиугольная пирамида с основанием (3,4,1,6,8) и вершиной9: V6/E10/F6. Её истинные

`Vol=416/27`, `COM=(−97/156,−239/156,1/2)`.

Метки0,2 оказываются внутри основания,5,7 — внутри его стороны. Они не считаются шестью дополнительными вершинами.

### 6.2. Правая предельная форма

При h→1− нормированные вершины (1−h)Y_i сохраняют исходные координаты0,1,5,6; остальные шесть меток2,3,4,7,8,9 сливаются в(0,0,0). Предельная оболочка — четырёхугольная пирамида с основанием(0,5,6,1), V5/E8/F5,

`Vol=7/6`, `COM=(0,−3/4,3/32)`.

Оба предела проверены двумя способами: точным сокращением рациональных функций и независимыми Taylor-коэффициентами, затем настоящим интегрированием предельных пирамид.

**Ни один предел не является E17-телом при h=−1/2 или h=1.** Исходные T_h(B) там не определены как ограниченные положительные проективные образы. Запрет на всём открытом pencil доказан полиномиальными строками, а не предположением о переносе пирамидального запрета на некоторую неопределённую окрестность.

## 7. Непрерывные222-семьи и точная достигаемость U2

### 7.1. Две простые концевые семьи

Пусть

```
u=(1,2,-1), v=(7,-4,-1), w=(1,1,3), L=128,
H=uuᵀ/(36L²)+vvᵀ/(4356L)+wwᵀ/121,
H⁻¹=L²uuᵀ+Lvvᵀ+wwᵀ.
```

Векторы ортогональны, нормы в квадрате6,66,11; обратность точна.

Для **каждого −1/2<h≤−31/64** берём

`M(h)=A_-ᵀ H A_-`, `N(h)=A_-⁻¹H⁻¹A_-⁻ᵀ`.

Во всём этом интервале строго устойчивы F5,F6, строго неустойчивы3,9, строгие седловые рёбра(1,4),(8,9). Других строгих и слабых равновесий нет: **222weak000**.

Для **каждого63/64≤h<1** берём M=H,N=H⁻¹. Во всём интервале S={F3,F7}, U={0,6}, Hedges={(0,1),(5,6)}, также **222weak000**.

В этих утверждениях все68 настоящих примитивов не равны нулю. Для их точной очистки используются li, d(h), `c_f=H_f d−n_f·m>0`. Прямой очищенный полином равен

`(d vi−li m)ᵀ M(h)(li vj−lj vi)=d li² lj D_ij`.

Если N=J_N/δ, где δ=(1+2h)² слева иδ=1 справа, двойственный очищенный полином равен

`n_fᵀJ_N(c_f n_k−c_k n_f)=(δ c_f² c_k/d²) D^polar_fk`.

Все множители положительны. Сняты только положительные концевые факторы. Полные Bernstein-векторы остатка дают слева68 guards/570 положительных коэффициентов, справа68/647: **136 guards,1217 строгих положительных коэффициентов**. Максимальные степени остатков8 и9. Независимый checker проверяет исходные физические формулы и непрерывные знаки отдельно.

### 7.2. Общий рациональный алгоритм222 для каждой формы

Следующее элементарное построение полезно за пределами pencil; внешняя первизна не заявляется. Пусть произвольный полный выпуклый политоп имеет заданную внутреннюю точку, здесь — свой настоящий COM. Выберем ортогональные ненулевые a,b,c так, чтобы a имел ненулевые проекции всех центрированных вершин и всех их разностей, а c — всех настоящих полюсов и их разностей. Положим

```
M_K=K^4 aaᵀ+K²bbᵀ+ccᵀ,
N_K=aaᵀ/(K^4|a|^4)+bbᵀ/(K²|b|^4)+ccᵀ/|c|^4.
```

Они взаимно обратны. При достаточно большом K знак каждого прямого примитива равен знаку `(a·x_i)(a·(x_j−x_i))`. Поэтому строгими U являются ровно единственные максимум и минимум линейной функции a·x. Каждая другая вершина с положительной проекцией имеет настоящий соседний подъём этой линейной функции; с отрицательной — спуск. У неё есть положительный механический выход. Двойственный аргумент с c и N_K даёт ровно две строгие S. Все примитивы ненулевые, weak000; тогда H=2, что также непосредственно проверяется аудитом.

Для рационального тела выбор производится конечным точным перебором. Берём первый n≥0, для которого `a=(1,n,n²)` избегает всех прямых нулей и не параллелен ни одному полюсу или разности полюсов. Затем первый k≥0, для которого

`c=(nk−n²,−k,1)`, `b=c×a`

избегает всех двойственных нулей. Конечность следует из конечного числа ненулевых полиномиальных, затем линейных запретов. Ни численный допуск, ни RNG не используются.

Для каждого прямого ребра обозначим произведения на a,b,c через A,B,C. В список T включаем `(abs(B)+abs(C))/abs(A)`. Для двойственных рёбер делим соответствующие произведения на |a|⁴,|b|⁴,|c|⁴ и включаем `(abs(A_d)+abs(B_d))/abs(C_d)`. Берём максимум с1 и

`K=isqrt(ceil(T))+1`, так что `K²>T`.

Этого достаточно для всех строгих доминирований одновременно. Матрица с рядами K²a,Kb,c имеет положительный определитель и целые записи. Она переводит центрированное рациональное тело в **рациональную евклидову** реализацию собственного222weak000.

Четыре полностью восстановленных контроля:

| h | n,k,K | Целочисленная аффинная матрица B, BᵀB=M | S; U; истинные H-рёбра |
|---|---|---|---|
|−499/1000|2,1,3|((9,18,36),(−18,27,−9),(−2,−1,1))|{1,6};{3,9};{(3,9),(6,9)}|
|0|2,3,18|((324,648,1296),(−252,−126,126),(2,−3,1))|{2,3};{2,9};{(1,9),(8,9)}|
|1/8|2,1,19|((361,722,1444),(−114,171,−57),(−2,−1,1))|{0,7};{2,9};{(3,4),(5,6)}|
|999/1000|2,1,43|((1849,3698,7396),(−258,387,−129),(−2,−1,1))|{3,7};{0,6};{(0,2),(5,6)}|

Во всех случаях полный физический список координат — `B(Y_i(h)−g(h))`, с буквальными Y_i,g из раздела3. Физические M=N=I, COM0, volume=det(B)Vol(T_h(B)). Полный код восстанавливает координаты, полюса и все проверки без внешних данных. Эти тела имеют C34, но222, **не110**, и не дают C_min≤34.

Для каждой вещественной формы то же конечное избегание нулей и строгое доминирование доказывают существование222. Вместе с all-SPD запретом получена точная достигаемость минимального числа U=2 **во всём pencil**, не только на четырёх рациональных примерах.

## 8. Значимые отрицательные результаты и фактические аудиты

**Грубая клетка правого конца не закрылась тем же поисковым шагом.** При пустых начальных данных поиск на[0,1] остановился после163 используемых строк, оставив35927 деревьев; выбранный mask77793546 получил результат `notPD`, итерация6, значение `−4.6494198314260635e−05`. Это лишь неуспех данного локатора на данной клетке, не свидетельство U1 или его невозможности. Разбиение в1/2 привело к полному доказанному покрытию. Левая половина[−1/2,0] закрылась одной клеткой.

**Нельзя считать каждый нулевой примитив слабым равновесием.** Попытка сохранить68 ненулевых знаков фиксированной H на большем правом интервале встретила реальный ноль. При h=97/100 и49/50 оба тела имеют222weak000, но прямой примитив2→0 на настоящем ребре(0,2) меняет знак с положительного на отрицательный. Его точный очищенный полином сохранён целиком. На всём закрытом[97/100,49/50] один двойственный примитив **того же настоящего ребра** строго положителен, что удостоверено полным Bernstein-вектором. Следовательно между концами действительно есть нулевой примитив, но полный пакет исключён положительной компонентой: этот ноль **безвредный, не физическая weak-точка**. Здесь не заявляется непрерывное отсутствие всех прочих нулей на большем интервале; две простые концевые семьи доказаны отдельно.

Сохранены все26 конечных контрольных parameter/metric случаев, использованных при изучении концов, плюс2 точных внутренних контроля непрерывных хвостов и4 рациональных евклидовых flag-конструкции: **32 полных аудита**, не32 новых комбинаторных типа. Помимо222 сохранены нерекордные многорaвновесные варианты; ни один не переименован в110.

В каждом контроле восстановлены настоящие максимальные грани и рёбра, собственные объёмные COM и Σ, площадные C_i,T_i, одна пара MN=I,17 векторных тождеств рёберных подошв, строгие S/U/H, полные VE/EF/VF-пакеты с объединением совпадающих физических точек и безвредные нули. Проверены

`T_iq_i=C_i`, `Σd_iC_i=0`, `Σd_iT_i=5Σ`

и34 положительных контактных детерминантных веса с обязательной внутритреугольной ковариационной поправкой. Все32 конечных контроля имеют68 ненулевых примитивов иweak000. Непрерывные теоремы не выводятся из этих конечных примеров.

## 9. Общая положительная проективная свобода: точная масса вместо ложного переноса центра

Сохранён также следующий общий аналитический механизм, не являющийся запретом остальных форм.

Для фиксированного B с0 внутри положим

`D_B={p∈R³:1+p·v_i>0 для всех десяти i}`.

Это вся область положительных нормированных знаменателей. Любое невырожденное проективное отображение с положительным знаменателем на B, с точностью до последующего аффинного преобразования, имеет представителя

`T_p(x)=x/(1+p·x)`.

Действительно, `(Ax+b)/(1+p·x)=b+(A−bpᵀ)T_p(x)`, где последняя линейная матрица обратима. Разные p задают разные помеченные аффинные формы: если аффинный перенос связывал бы T_p(B) и T_q(B), соответствующая проективность фиксировала бы все вершины B. Четыре точки общего положения в каждой из F0,F7 заставляют её фиксировать обе плоскости поточечно; тогда проективность тождественна. T_{q−p} аффинна только при p=q. Имеются три настоящих проективных параметра, но не всё11-мерное пространство решётки.

Пусть V(p),g(p),Σ_p — настоящие объём, COM и ковариация **равномерно заполненного** T_p(B). По якобиану

`V(p)=∫_B(1+p·x)^−4 dx`,

`g(p)=−(1/4)∇log V(p)`,

`Dg(p)=−5Σ_p−g(p)g(p)ᵀ≺0`.

Последнее следует прямым дифференцированием интегралов: `Dg=−5E[YYᵀ]+4ggᵀ`. Поэтому

`∇²log V=20Σ_p+4ggᵀ≻0`.

Более того, **g:D_B→R³ — аналитический диффеоморфизм**. Область D_B ограничена, поскольку B содержит шар с центром0. При приближении к любой её границе некоторая опорная функция1+p·x обращается в0 на настоящей грани B. В полном конусе у одной из её вершин интеграл предельной функции четвёртой обратной степени расходится; Fatou даёт V(p)→∞. Поэтому для каждого c∈R³ строго выпуклая функция `log V(p)+4c·p` достигает единственного внутреннего минимума. Его уравнение — g(p)=c. Положительно определённый гессиан обеспечивает локальную аналитическую обратимость; строгая выпуклость — глобальную единственность.

Это **не свобода reference-point при фиксированном теле**: выбор c однозначно выбирает другую связанную геометрию и её настоящую равномерную массу. В частности, вдоль изученного pencil g_y'(h)=−5(Σ_h)_yy−g_y(h)²<0. Такая массовая параметризация может быть полезна для оставшегося трёхпараметрического класса, но здесь не объявлена его механическая разрешимость или невозможность.

Открыты D_B вне линии p=(0,h,0) и остальные направления11-мерного chart, включая общие непараллельные пятиугольники, не проективно эквивалентные B. Внутри **всего теперь закрытого pencil метрического остатка нет**. Следующее содержательное направление — совместная геометрия этих дополнительных параметров с истинным g(p), а не ещё одно увеличение κ или проверка уже закрытых метрик.

## 10. Полная исполнимая recovery и фактические pins

Ниже находится **полный** source-only payload: семь законченных Python-units и один буквальный JSON со всеми725 строками, тремя клетками и всеми списками применения. Компрессия не заменяет данные хешами: декодируются именно полные буквальные таблицы и исходники. Старый parent-код, sandbox-файл или внешний coefficient-пакет не нужен.

Проверенная exact-среда: **CPython3.13.5, только стандартная библиотека, assertions enabled**. В новый пустой каталог была скопирована только нижеследующая recovery. Полные `build`, `check` и `dump` исполнены; отчёт и stdout совпали побайтно. Независимая проверка выполнена полностью. Это не proof-assistant-формализация и не заявление внешнего рецензирования.

```
python -S recover_pencil_full.py sources
python -S recover_pencil_full.py build
python -S recover_pencil_full.py check
python -S recover_pencil_full.py dump
python -S recover_pencil_full.py flag -499/1000
```

Последняя команда строит отдельное рациональное евклидово222weak000-тело, а `dump` буквально выводит все6860 коэффициентных матриц в канонический файл.

Необязательный численный локатор также включён полностью. Проверенная среда NumPy2.3.5/SciPy1.17.0/OpenBLAS0.3.30, без RNG и без parent-seeds. Для однозначного ограничения потоков переменные задаются **до запуска Python**:

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python recover_pencil_full.py locate
```

Эта команда заново исполнена в cold-каталоге; фактически подтверждены по одному потоку NumPy/SciPy OpenBLAS. Получены те же498 левых и939 правых промежуточных строк, затем те же277 и448 конечных строк и байтовое совпадение всей таблицы. Максимальная глубина6, eigenvector-cut/HiGHS, лимиты итераций, округления и порядок дерева целиком в source. Плавающая арифметика только находит кандидатов; принятие теоремы использует лишь exact-код и буквальные коэффициенты.

| Объект | Bytes | SHA-256 |
|---|---:|---|
|recover_pencil_full.py|30788|63eae3c470aa9dbc2c103dbc8c6047520691193b5ef09763db5f3073a7d8aa7b|
|полный decoded payload|75737|3212a7a390ca5f9f9dc7a035021f43a8e09d9935e2415ea787fac7bc0eb0d117|
|pencil_coefficients.json|24814|b8274c3577940c41be83c9211b313c3f1a6ec1e57bdccfc0663d816eb51e86b7|
|pencil_full.json|1144002|0946e156dee3942d5c68a26b1219873beae9e34af902227a8c98cc65425dde76|
|pencil_matrix_stream.txt|498550|4e2047398397dca1c420e6a2bf4b7696a4460402304ca450e47b62c89b77c432|
|pencil_left_progress.json|29956|c6163cb97963ca1b4a8d97b8b305fc28cc445cc93124ce3627100a443c8a2453|
|pencil_right_progress.json|75043|90510a1414c3b809b1f6456ce7b3b45bfac48ea6aa9de6b6db1fb853c4954eed|
|cold stdout build=check=dump|1119|2a06ca21be5c79db846f4a5b81e75648687b85c196dd6da8a49dfa9538b86bf7|

Главные реально полученные маркеры:


[Encoded source block omitted; the code in this passage is incomplete.]


Удобные дополнительные копии: [recovery](sandbox:/mnt/data/bevel_projective_full/recover_pencil_full.py), [вся буквальная таблица](sandbox:/mnt/data/bevel_pencil_cold/pencil_coefficients.json), [полный exact-отчёт](sandbox:/mnt/data/bevel_pencil_cold/pencil_full.json), [все коэффициентные матрицы](sandbox:/mnt/data/bevel_pencil_cold/pencil_matrix_stream.txt). Продолжение не зависит от этих ссылок: полный источник следует ниже.

```python
"""Complete self-contained BEVEL full positive projective pencil recovery.
Tested CPython3.13.5; exact modes use only the standard library, assertions enabled.
Optional locate: NumPy2.3.5/SciPy1.17.0, one OpenBLAS/OMP thread, no RNG or parent seeds.
python -S recover_pencil_full.py sources|build|check|dump
python recover_pencil_full.py locate
python -S recover_pencil_full.py flag -499/1000
"""
from pathlib import Path
import base64,hashlib,json,lzma,subprocess,sys
assert __debug__
args=sys.argv[1:]
if not args or args[0] not in ('sources','build','check','dump','locate','flag') or (args[0]=='flag' and len(args)!=2) or (args[0]!='flag' and len(args)!=1):
 raise SystemExit('Use sources|build|check|dump|locate OR flag RATIONAL_H')
DATA=r'''
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;V0Nrg<SwWh>3?YpURM(Ku(jb=D0j;%x_A0RFs9@m)LC*RuvBr=Rpr%b0!H7
ZeNzQo;FW7s&98;Epy}M)it0$mdkqVKyDLpuv9StRs3Sx_uO)rY^%&L9;mp}J=4_?F+APDG-3b*7~zPIfXbA_;0!RS
92n<Xzh)2|Vw=uw(e25M@2kGFc7d^dxdRYq_WdngF_<=m;TvyeYj?OrX}oKODz@duXnh55ckJUU&B-Ff`ALu=EI|x_
3ZJbYQsfcR3+nd!A=a0HmE`KbeCAc}T-$+}K8Wo%&Pag>`!d{N(r_bAO8asus$Nw3!oi5*z?+r+xg`_bcBWdAcERHK
U>T9}o7fe}fJba|#gnIB)aKDc9TEE<0uJ2ntFB`5ub7O5p)EJBfXabnml2;mz@_;3D?ZNW$=V`VM7}A7Wpl!@zW1Og
{-mIj(y>L^U7RfDjv&s&8Bl<T*!hG*#jZp9Aq{(ygeF}!Bfs=T-#Sc=ewx0z4jcfh|HTjD5WuGp&G9#wU4nA5YvObd
J$22C0FJ$fnB)!@hBW?uH658z(<F1ha>M0_N^KVyrG<?ZR=$(kKY&!Cy8hC-0IhJIj3*-O`3l%9v`L-zuCj#*K<4gw
Pj+;3xD2~+=byrO?fi6ho<|-O+$ObvcoO~=r|m-4zK4p!pUc(#>Fv`bO+K=T{@VzS34&Bh?nhRd&wv)$HoU<r(I_Fr
D%7R*!M87(Rg56zx7huM?cmA8`*<>&ThmYlSx%etT`==`xK>v9aUY7f-U`qyl89Nh#~IJtMku%~Hw|8AclCPijs<tg
*4Mc|+;#wfi_XTNxI}iDldn4|1IveCua%)9xEqsgd<X$`t(f=yT2;CZyKNNkBZVm4a3r5h9Z}rvYknAuN@vYH^0D;k
r9@=TC$368C=s3)fJIml#yKnOtM(t#z*RwS#)2!PwFA|z9I1qQbF}vf{s)LR1|WVB!$X?;yu!Am-vWV|L?r({P>cu3
tn1-JUSZAR)a>fhrj2Y^n~xS>RIYO2g2^9z%yWZuZO2Dt+L+i`#d>JwbLF63wL`y~QF}J=_gRt81Hq5!Ke6K?D{w{;
2d2L%l1WcncHlA<?u3JGzjUT&hxb^sWO5h_r007DOHw*U;oxkGDZG=aoF&_z`@XD-KHRHoYFi=--0ESp6ft~ZM(xZk
WzfoONQB#}8L*4<4~#H$uv74y>%<E8Mp0N9(~<w+A&is-QQ3<H*vDxrBYSIRHUp~d_6E7qKc}x+*CRStl_g3L(AWEB
cU%mS^o3pu263#8Mi%GN*AOd-p5A6=<Lt~RSGv!i4SEnv{S_-I9#z=DufGLF1`iS2|3TrLBRyz(;_1GQUp#x@-BAXC
#*vYOrnd}M4y{J9!}8NQHIG{A1|RjRI7yB5PA@WhKu2LI${Wb$YRz42=dC~+rGJanuxqJ<m>|IvBF6)drLzycGnPpQ
QG~qM07tS;QtV)VNf|!6iLEeEuMYK6>A6u>Bv;-Ek$d+iJ5hC1!OUeyVAbq^naT-;!cX5fYC1TY;>3q>8Qo<~z*Sw4
t;V%hM(NSMHQD?D5{Szu+(kT+*lUa<U;2uyQYS2BsQL{atOX5lgH~K-P&a;6d&a}V@N=U+ICT{<9yRi1zeZ^;U6_f5
q%Rb&OPk-(&FH#bQEQI$SXZOBlPeI%{h~bHOZCaZfBRM8C2B;tflXRXF>^_Vi-d}nM6^!lmR|Je0zvQ*1iz(obZFl>
dH9hq@(Q%w>{0*yeXMOvBiSo?vDFEWF@pS%@Q+KRQ#HLU%&D&YJFRXeo0B!=tSQ=~F*g0><$@Z^J($__hW0sAv*h|}
)<s757gDU3*F>o0Us?II)WT<)9}V@V1AOSNvdW!_a%CS@pT<)+&i(*bl<XNX<d{dF)sQ@u-=eDX${AsN`&+9_gYar)
G;n@vKEp!!xpqu>FuwGc`@NDF9^}-fG4!TkP^GCGm(zu^J2xU3Yi~^6O2-niCAII3HkV%O$O-xcd1aRe`aW#f7ltre
T-38}os<v9B1ca!3gHyA;s|#t)Lj{pPltq+00hI+eCE9tNUzkeXqVcDS##N;>vM)kO5xn_mI%!@R$Bw<w~vypsyDuo
;9>6sb`NAz=yvjjCaWssZ|U5Au0l)QRhy4^M;&Cv)v0?`M2#Kz5&ir638eWp#L40cu)EU~X^v^c)A-<@>s~?}Rf@aW
(EF(EveQSaqn&2Y#46wO;efr|h>v?e!08{)ev`QLLO;|I2~pnCND_(*k)PY@g<MATXvR22vK?~?huS(~cr(4(MgtHs
#|V2{3eKoGm+Nsft=_3tzj93%=_%<ZlK<|3-@L}N7}Se6KpB+(JKxFVmEgbJlf_V14V!kY;|=Zx^Qd1q4*g4yE$<Vr
+o|%5x)z#L{K*0p#7+4U2!`SpJu`qJAn9h#Q8tA=H>CH$aPMD9iy>Jm>|kRTuz78{^UStt<N52;kz+E=Y|rBLX^``t
+f~M&brBcCC0rckIz6t#QDx62N`@tg)r)8X7*L(>y^Yh}%)4p>QWC@zV1vA0W6VOinyC#51!+|(w9b*%7POa6H86Oc
*Pi|TNT1a8fc7aeLY+VBG|Wcs7nf;VS;iXeZ=M|lWQ2JtW~WsOXI9`r`6ymxAv-CoN~2(G0A7WJ1R=9mN!0+kd6`~1
*s5ff>Kk4mkIM^spg>+K)BVQ2Gmn8<VC?s%2l=(IA){p95OL9<M~ClY+25;Luekxy|8n=6)LHyZ4JCNG(`?0E1S_}E
L;l^Gvy#KUx|_xc5k5hx-MLDIBTdB}r@SdBmG4Pv&T~}sBDTm_q`<8S1x4$in@qQ;+ZUZJfC3xfLkb(=s}!Lp$KN4j
I->maQyuF$CFYJih9z_SYIp6CJ{}Q}eq5q7DJ3cRrcxY-w+;EbND1W7G(8viDpHO@sEAj*tHO@cG*Nu~%X9L`pDALV
W*y(4M^o?uBMT%%WKz_rC1e>Vmqei&45*%o(s<-Wjn*h!cWJC5%!_(GCz8E?%_z10YjQh{eQ8|tw7E}!djKWe^<Z$v
h8A-V3?pdt&!Py)(OPuqmbd{R07$?va`l`px;f+w2r90wwH)%NX+G8Ygpm&c`yE#S^uCvo)8sM1_K}YY^S)&JMNT-P
+h`SHU7BnV#|zuP*rg&aE{n<$fEI^PZWx9gT9pC$CrzA;ZgPWkA3m~=)UCb;-aP!rv}Zd15ua_sVGRA-*`A*OI~0hw
F&f65Q~FM`9%%f(e;l1j>Qdb84uxu?Qdyt2MJGX7t3lNhIiW3X3xeSbo8}lc{r6NTNbtY(qmNh(JJfujiBXCgC-9t)
d9Reszsq7r#G!yyS$}MUVO!XFEGL=?O7$M5Gcb3Egv)EB#T?YWyzTIhAM*Y!e=5MuwOzjzm7RA~OrB>r1VQ2Lo49l`
S#%Psy>2uWL_~~TVh;?6QO$Mz-rh?0F@b^y9vtw<R3JzFNNsbfm-@M3sh``+!R!Fc7uR_Cb;WrgAMZeQV+Mr4_CJEI
bptg6&}MO>itrCP7?s|u!?;8m+$%%i2Ts-=U3j!Gl~b2EZ4akMKp46K-<Wk3aRfrgXO0p{)RnWC^ca1oIDvHRvUq8f
v6$tQeIXpfpK?i)!`=JN42wnw;iT}`sgQCTT9i5o4*~h*#~LCR^sfa!cx_no8k}}lMruFS<kDk0=9l=f+)(aC1N10|
O+K_F`)6v6;=ME$qT`~wylzb$s1lZbRlTY`fHqc(>_Yr1-otUwaVMq?J<)PM!U--S*;qvNTEav)$a3vX%Ov_gh)VF$
V#`IhBGw@|f|P5EXL2)aann2K6$N#s{Er$Hh6NSw9;o}8Q(7dIUR5B=gx$6bbD_Mg^V{K}<#7jGYc%9VkLtV3;E<Ms
^mKL^kIy)>83xiV2>Bz&Hb_TB8aJx#gi{$#a2!XbxH#5pB2?j|tP@(l+Wq-1T?MOt(5m_eNY|;2Zn~Tv(SY8`ftUo<
Q?leszz|JhK%g!vpky|*T?Y+_j++w8boda@<qGA;th}&f@Zutuer`t-YU}vREB&eRNp>~{NeOfJ5yt4Pe-~)aG$vt@
l~JX%8B!n4)#~{w7wl(^8A!SjvlvhT*J_GM<-3z!nzv49^1(`}XR0m8_FFKd?rB;dmt!?mIt-^B2*a^P`7eTzu3YI_
xP<N~v24`<qVCP!EmALq8vfB)$WZ#PJb|P5(?k-E)-D|n+{R?O&;Qy~eXiNB&85C!4w&}C#XZp}>lcsGKqq0*3ck?Y
@SBChQisgMtaSs{Bhd*U$FGMs7}cR~X>JQEO3=opHC#GX4_DR!+)9w4?54icqf-SM<CTdBeO=XbdW%mAl-J@1Jz{zL
d(wgDPg?cE_7$eHd>vl>hPedVd>wU=)gDoBSVDtdxU;}1$|8M~27T|v3Fo~Oxy*lNxVE1}5_`FUZyt@mrSp9<YaZTq
`-iN0(>e{MpRE*Ud=QWK`SD<aGo?_zmRV1TI1D}Le!C|nL2zS4>v%zy*8wErvc&>$f_P}ptnvr9bB?0`(Ndxu8RH&o
*ahR8f0QD1Ux>X*MM;uGE9*_{je32I->vV1DSkdWIJ<G{<-!0c+siu;tz#g6h65Cn2%B7Dcq0Y-nT(T(YjB6eF~?M2
wqoaS+k3+^>*SPDAq1*)S3xxT8dZq%qy=5DBGss^<IuZ4N%0J%-vt;G9tiP{y-?B%v}uNRK`(1(mzg!TcT`FeaWKz*
<x(*>xwXUOfp-W(cst?%Sp2TZ`hS2}Q^&AZuXJFrVNPC9;l4|^kRmdkRa_!0SL>t2n}lIw3~M%jU_$sXq-RHuiYcVb
2LfL;7-nT|1#xt}U|TQyz;E&k9}q~)41j@K+s>Iey?oh`EoV{z5|yH^9S54x$zx0KOoVq&4`E_in5Z4w<#6-sq(~2E
!5EEAcsS=YkZNcvjqWU?0Vub$){kinnT*ZgXac$JR@_Cl-Zb`fFS>DZ>ZiPazodU^m)+39B)lyUMvzLj)QPp&jM?ck
67pUNr3D;8v+EyM(VDFLX)gWqoSCMJM-J04GH=}Up|NIa3bA8F`34u=K}=qU*u>yMG%HqS7rMkPR3S5<&|3*q;J@gN
Y&skUSe16rF`Pj?RB;(^&jGJbw@S<q{3*PER!|HgWuhlu><m<tZwt=)@jv#N<=0d-p>4qvwv<7615;`FsqB>otcfAf
mA_c$Q*FK9f;+&iKr6Z$#H)z^BVfn;O-F-|__a=vkEh-y-eAyh>t1t={nALZM2MXpmcVB*5WIlwLo(`_M;^(_3F9qL
`z-LTau;*)VjKxtt6sjwUCqLp?Gc>q5HS699<5|;<J*q=GX7yxN#KI6z;8w}fu8BixVEaRYrvua#k||q0{WkBD|)c|
9J9}}5<_3>w$2xS$#OW{yk%>kdP?aAE@et$?&sOf8t}+=3!Rhe58#^{{h^xMLm7RYK#8c}1x^D8L*p+_s2SmT@XYl#
g)~`V-#6SYQ|E|NNjXxWiGO{2P#_LPX4l2(hXOdsf>^KmNFq@+ve`|4aWBO+8(rGP0nv6f3%pPGt2;(%v}y=A{HY(0
zz-E&lb{WHzvO)MYKFXgrqAei^poy9>3Q+g_Ft<c+E+l=JaY${Wpp%F2WdBqo`CX50tza9f<d7RukAD<NEVyNS06%_
+(f-T9W9erCiG_F>AK0Zp(^5KRUXNiZKC4d^b6P3R91UMa(}b8%*V%hkrld24sbM|m_xMf@ford!;Jq}<d%3m*f#8D
#zs_H`n0TeXt8@*H3OR7<o|6RFh&t^uU*;%3|W2uZpgnc<F^=-(nxWnUn_9$#(U#FuRKfnBZNX^WsWW@J3fU=1G7~v
V<ZCU<+%_B7AroBn}Y)7E{VW<?_OH7!D%TDXsoJ6ub<ZSB@f-2JA_pz3hce7qmb*Ub<7*6Fl)xj%#cgw?_jRQs3eRW
YZ<A^5gper6YB|fU$?Ke@}m{fhghn`U>W<YPu0#Sg-5E{f~?lP8V_HyPkHHv@4?)-pQ|88F)A>F0+b!3t?UXu?j_06
vf^?sVmT!liJ>GRp5YLse<@|21T24;bRXE0+@l2OUcTSUaVh*F^<<D^3nsTnN#;mHQ^MCvXO)1kKmyk^d)DAi;0M<l
0R_t#PZ=dP&(7Z8CNt5&gp1M*Q!K)+r}0OnxaYYxptSY^bfR>?bR}(hFVX3CurAXndM+YKI|f*L#D<<x-=7~->2=IC
^0rXw@7ZM+=*di5xi<9Vy5-3MognPiygEQ;6`4SUS9*~2-{#XV@d}|Svi!%}neOfz;M7r<aSE#tuMMv$l_ff=N55$I
qIV(wR~@pi>Ok^}A<r|(dAjnntT(~|G2FWkb{*G^=xGorH#8D<^*VV*i4G#j%-5N5H8n)c)vMsd=v&kaRM&9Nlb5nZ
Ux?V=H#F4JEijJ(ZKD`Jq))kUJA5I3jilj2Cw&Mv)7Q`tHu<^IhVQT03fw=Wu^;;4rdMVBkR+Glv!FRb?!(2ZIj&ej
#FB1v3m~lL(HIz&DtevxjE&KG-5L;YeZh)}!Mh@?02S|R?=LQxs~duN%dd_CR$@ifF~f%6>v^FSV;as6?w^GXuCGnl
2a$-Mx$L$`t`(3|O00+PM~*k{Lc$eaq}Y6zTwNnW;#oTqD!ijp)}G#U|5mo*S+hp8+cczHuUFC<cDF4=op2<?bbULB
QI>6Gv`=0+=$yNtJMOGG4ehmweZux@CZ`bA(kn0qUtxD{j#S|N*9S%rWyAr_aD#Es5?4VeebWD{j%1&ko5<N^!BEgd
P#$P)@c^jWynfaYwKuF5td#KrjRxeM4y-yb3OGDDz))t;-FDs6PYJ)V`)}NTPnw&wMeS>ahEmdDfHE8A5YIj+J&PxR
z_54!q#aXXnUG$Pmo4GfsEwnSO0|)#)=FyS4vw-BiApK5T81gE)F@`ORAMc~!vKaJLRbN~RIc}Bzi}e?fVJpb3&z$b
gL@|){D#Z;cCGaTgjtpRnc+XTL`W`6{mk9u6?2ESmqRHMU1cKbm1>O=mMyAUIF`{$^)g}anPe#a54^?wbTxNL!X8AG
Kv!=wun`PuyB}4l#ZpxHoA0R6&TlTUp2+@IdwbsQ@1jLxw@iFXIj-Ph;Y@=e7>wXzD$#$kC`LP1o=f4rgq%YLREV*L
*3=bi@tS3P+UU*P&GTi7t@msl=C^x-3!be~+R_^vGG-BY29AoqMHEa7LzIJ1(2S+c2429}`J6__Y3uv{$z$6)$r0m7
jNw}_azq92i#D6Lc0A>m@#^gUdh(<Yy{V<391PEVN$;HnC>DDg+ocu<c3b^oB#lf%;Vfv#eTjo9$tO%Mm*0uIv<&%y
S^(&Nr*-;_Fnk@w!wKM{m4dGrDsKE|=u_v1*LnpUR5=SSsXjeMiW!qJ`RfPN%iQ<pv0mC%KcnvOK2gcnJPLsSl-mns
h^9lM{4gyyoLaC6Zc=*6iVVVVyA-Bfv%EsswmwmXPTEMOzz*KqKUl(TtFy=vs(LVDlDuHdW5G8Lm5w%)uK<)%pD@->
GU+QGx(b$PmLd_Hr(E4t{7gc!!D4x1WwrQe^i3GFeHp<Ovb3MbXJ=RLesru<s?uDbh|uF1+kZG8tp&cc^phX~FZYK=
nFBF2dc6`T_(B~@9^xWezP&oOmiE+9S4e4RDG-GWWVV_;g%l(i9quHq-?Ezu{9AdNa7(D$5Rk<mq4m2(Z5On>ZnDFv
_|IMGr&d<gd^l=fI>bQm!k5t3xVaQq>=Txh0`EW#6d?PsJQKo*{Ubh>g=8;?m**6PJ4`Qj`#FWR-Np2-z%u2cwqSKW
E(=!AHBWIa^=z#VGWX_d`x^2+J{9Ez2k5{E*f3aqX@uF%@N+~<qO7#IjUR57mHWD9AIHL~Iv-Fqe+C`5Pb!=vhsU|w
O4f)Lxy!waI7wp-0yiPXeh_lTswgr2&AuLA-F?ia`M=3cIy8VoE5<$i5nTl`^NTwqa5qVtDMhuKYg$0-yo0q6DAE@3
ITd)7N_!Iesc9)?XN_@P4H?5K4|aR?8<o{U%Zo{~K~0Q!WI`P#_bv9<2#-T774o-IzfK%CEUAR@3X>Ub+biy<r7{S~
sImUYPaGI>%Zh)3_#!S5M_hl@33j=TCb%@D`Q&|uYFy5&?7C>y6dkcZ(DctoF)?Z~8Ggy}asB!dvhb$G6W@eScUnNi
E*~&9Yt4p($QqHYI09W5@RwMB+29{2Muw|m`9VHA>qq;2I%4-Opj?O@FjKfO3v+Q<Y#TKZ*%XGS5fXj@m@=Y}qC2ag
*6{2}P>O<~q7Ex#r2{315MMFiH%H18az*F0BF{2lg~=9-H1>or_~#-pV69(DFLb}6plbKqESMIj#NN}XpIv*xQb65q
!!0ww-&TnM<K4ua494ijXDu!#jzWE9GA=$c8!A6~!mDok!S#540=Ypt|G_EyI^QRDFb`7iLA{x;j{2XlmU)-a0-2Rp
$<woJ4+>P=$uv!Dd>U7lXFYAu)r+2z@ROX$v_F7AQg-PWM9(E>_iHDc8eD%9)NJ11AU&I+cO_FxgDfP}@Y<qzf=G8a
xIFgm;%7G{oMo-Q%@ja2QR(E!|G*q<{aC|WhyGR5-WBZYdWW2+rLT^X89WRU@OeC*gKP(6%Fb5{Tz5e4rlel@W1{&~
Sya>_#GDCBO-)`)q@7$VHtLb-=PPmd3ca3K`Ar&I;tSnbCuE{B<g%T?Ery||JWKK!Jh%dcR0*_C->TWh;|($E#0YDy
{s^gE0}eQlXW)#$1DzS@gP>rbgk~1QAHD5^5zkzdV0OF;&Z?_67=<J(u%58TSuv77QGKIugJ!n*4ZL@a^%felTxbb?
K5UqwD$MEK<Pw}dt<6r63^=p>yN4;Cse}>O_iySO<Zgxe$q!0~3a5e-^F-g!GO-*UVm=Y=NtK;6uJ;F1LZ#EqIa^`!
`CEa~U7Do5oiLABAqkKTdoJJwZ34H`%@c(T*v#?xQA0Lc?pvkbs45TSF_O87$Z`!|X$yiZGms^&u980PLSd6U`zTPC
lzE&}S4V>{()4b}le7E$F5zZ?G5k$+cK{yl|H@E{pTP+qj-l$mBJ30}H<hs|BT?ve#*au2XylEUCE%42t-{~!96L@9
7Nd=Y<mdxxouBQ^;)Aw<QZT{>t|vx6d<kE58U(V4;Yyo*EM$_kUf7}?FqbXrVrE#^3CKTc^Z_aE81b{{?+s=+<waAa
3i`;iAvev#7t$N`L}pdr67Jg6V}VY+sr|ItV(~Miie9+>>R@v-VkepIy3#SU?(*}jH}?1T4sm-_X_*sgrp-AMEjof<
1@HwZDTyg^-Dh?#&^C3hVkKV{?#NA0^BO*>eC){_2H{UK_^~OLd{ld7{U^Iv^JxuoXjZMqOC|ttv>}+D|I|Sw^`4wT
<aPLhNmWwd+-?eJ?r(5O;JPH@FqWLBGgOix#3aX${2L#5IZFWs8~TM@Q}e8U6eQEzo32%+oQ*Jd4F78=p78uFX*&|Q
TB>fq8$aqaSY+_{HYJ^8OxlZ${lHJAb;$*QNTRvIfAbuJ)6_prUX-~XQ6m-(%Gscs#Y@WjG_GrxjR<SEtxL5#+aF9B
S`beBjq*sz6j5&FNwPYiPyg!+Zi}BB8-9Xd<9!6V1|P{)3}mFNVH_S%^)Us8l?!JgQ>sW^=B|1vL);Wd)<$8JIb~Th
CkRg(jEoaz+$zaW(0#JkD}&s7rEfK(BLI=Ew{6pKihu7ug)N6Mh#;`y;;IiOKM&_ZA?+FWi5n9seHfd(3wEqJW6QlM
@FsY3lr*oE>qgS2MJ)6kQkr^cAHPK;eA|?+S_QBD<R{I5XfAJ}2f*E;RtsFi#i`kypE8xm^(Zxs-lGIe8rahdtQWRM
`g!}nl`(ZWTkQ*)4DITkv0Cs`I5`Z+Kx4>IAQ715yDs7?&6TL!(J^0op*_dQ0AZ4qT;wEl^PQL?Us`Gg`ZPc$<^nn~
W?=&k-VF#yz--%Ib;IAl-=7Y69x=wUI#%!q>rncd>~Z?N2ln4EZ5xR9%MEfqlGm#orDDI4aZQ|_ZlpDt54_ri$SM|X
$Slz;AO`JLJGy1~I;zg0Q;C-Y8r(H^=y3-bwwMi2UgOhDh3u)M>8I263L@nD!>m;LXhha*gUD4e0fE3W*hS}{#4*(Y
K+!u5pk`G8n3rEiIa+ooKV&CC^mJebaHi;Yfoj8y^KYx+T?LytVIEV#9Z1uCN&bp;I-hQbfQ@{j1+xSA)q-5^jC|@9
Yy8`&bVc7C&i$uM9(7uB*?@H(sopIVeGzzPc-6q{f;&|IUX*j2!p5ycK3}8C0VezByEn4#OMZCXvF)@nGmn2gRIXD-
p!4+UIq{{fQd(jung7lC0jAfs+U;L5mmi6e#8JQ}l4o5x+oc)I#0}_+ZA}re&g_B`VQ0%fvC~Qy8YL-A#>Qg1OM~iZ
iGW_*y`J3z+0>d&<WVOiS!?k3Yr5?)pO1t)2D_W4h-AYyA(3P15Grwd;-n_KlK}HK`Qe3tE(2OqWOgTR4!Pn#=`T4|
xUm$t_fTUte;iBLS9QG|2dM`3NSeJ6N{aB(CNHV<Xr1>Im(H=ddSbxgEvB@gs8xHw``y7IKo~H^Pq%gy8QKvytJ<%m
Y~P{DHqa1I_AGs$mwJCcYS0QYi)8liu8YJy5j=;1clW$a@Q}(9mx@TI1X@B6wM}c}T`QL1Fyf_E*@nEQ1D>@GL~I%a
(>JFt#Nq(>bQRs!<ku^PQwQ{!YPk=MvLJQDxWic;j=zW+492Y*+jw`D(fs9arEb;XQ#{^OH@>6#UT%vhWB^}3)o?Ml
YyWXwQ<e?<Cc<)o{Q`ep^%ooDqfU55yK9%hdM$=7WwO!P`t#Y_scmgPegbyMA%mnBLD~CjPmWM>y*A9lk*RU|R>rLH
lsCV%$WFktfEPzD0X=aOo%85w1seC|v>U8+|D`>HuBFPOZccnh892~zQ$_7YCyrV&Jyz-!BqZu=)2~wT&$;y$TZ71P
q#hPFLl7rYJ#wqo<H}Fe30#nAND8MSU-oqV6iWK;8qE^pnQnr0mN61Znc}g<W^9UVRF2XyybJU$tGf^WuUXi<Ip@q*
4DK5xgE%@$V{NQ@nditA25t`&%RiacST7r!!~y+eZU9(U|36|fjq{Efi5P9W>JzJBLmd|^GGfl&Eok*7HD7rW2+7W+
zq?$FY+UK;JTgu`^JK^G+ngIZwtEP|^`9FLGhRvBj8=8^$2UhRnJu=pKm6d<{5gyd&(zSa+^aNgVJCXS?b#7-@9gvw
C{NS+jBRNct~sPu0O7I&_wNb5JHSx2#(Md7A(#rxbt#XTsU|weSoA`Wtmyz$SP_I=peQ!Jcd7+bYFZ{<l)8qfQmXQZ
K|kpZ<cKH<&y-)2Q-9k~4`{uv1pW;ce1uXlPW(p*e&siHHxE<nOPX{uR#Ug8BAh)KS4Ft|2~D~NWYBTs6*#4<%vGJ~
iL`5DZ4G|u&X3$$lrP-Ed@0+JLWlzS9;|1j5WR8~bS%7RiQf~<5YC~X>b_7in4D0Dkor=x9Ygj@A8s?SiiS7R>-jB5
ZsVPiKj>e2D9a~HnJuLYAF$4FbYTv_YWn&QvES5~G{h$uJ2Z@%CKr|Z-EAGgdAi_e$zDX1B+KTozOvGHK2t04Q5_l|
4b)o1&{b~=ll2g4$jcIlokQ;#ty~y1mAMqS#t6Ys1zUHBucqF)J<;T2lKkZxHw-s{j*o>)_i0+@zkla4-M$H*B8Z76
wtmxnI;%Wu4+(r!TlDPs?-bMSm!Vmf0_xLC1A-RgVl&qm&k;Jw6I9HCYe^kdWCPbQKsyRGFv4uAFZ%v&btirF;of~3
6M9|+98Mw-2EQgQtftDG(+v6_h&`+d&%hx7qe*J5!}-W&9tjG{vzKB_f)X6H$7$PDikVpw+rZ7rr?*olx!T@31*>7V
nvAkzAl;`k$yLoRiSc@oPI-mUz<9Hk!Gt&e58H5hdXXN6W}PsmuM{|7;<9C&2RUE-j_0U3*Q=!+Aw7b$gqf1xS{f^R
PLBj54OEb{BH2yvuI(%XQNxB5YF|F7tLUIn=@}=B-iwOS<SUD~AOR}Spf8H=hwM-7uBbOtuMU+pYuh&4L*m7{hV1Tj
b|i_0GhIU*^BHFRHcYI_R?$romQWoKNS6;xol!Gb6Ye1mU?_Cm5HV9l0M@5fL9)onn3qj4b!$V4X;`^R4+}9OwckBh
-*``lGNFax?hXs68B{Y+-LW|E8k4}Bn<I3{Xhzn7nC~JLSDN><#zhQ@I%D^JGJ%%4?g8QiE~MDF4wCO=fn9-g;>xY~
$LPG)d%4OGX?YV+%+>8<#6UKAzD21h>smKl3Ev9a@|7AV%}4<GP78x|lW$p)xXwM4XB@`Q#+#|QO>3!_2pvO}!0muV
JVXjqjFqkF6j2=2(hbW5kwuTd1Xe@zlLPLZd2`~ODiSOqj<ABewWOW5VQIhU;!`@O4hbS2qC*|z!MKP1rbvCRm;1kg
!z{=KXE}74NFTY}W;$RQyizjiKn6H;vQS5ZIY?wu-Qla%T(RVrhD@G(C0{@xnc2J#RHa2b;dYKqYRB}(wa?KQaC4ET
*=Q2dPI=ngSKo|s&|;kgnaSS2{c}y)f|)R_v(>d7T0bY<vip0YgN|eLV=4Imy3@6P`Njp4Xa;f?WHeo)PTXfQFYUOt
Ib4;!C_$X-HRYG*+@UWoferwTb-?a)N9LxLEN9T|5=~T)M1e1>eScz_UYrZ}%IPVt7W=)2^F<FhmQ7;C-c$kYJ?~=~
E424UTk-Tr*ez(oX-Q%gWI8g-Ts5!V^=vCGLl#oSad$%jbDg#EN$38*>&XlsQ)*)<11@9%=B2>P&zv(hQ=f&^$s>@C
3S@v0aN71!XnN`0*}7o2-u@{YN-=|xad!7b&Rm_^mP8KOn_=0Mc|Xg_jb27%;Xwvg73@X4y&D)J9nv8L>cA#Y-y(~L
wZma3TO#gLswMwZH1Xg=uYuqyN94D(X*H+w8YOpNq}UTS>B`By|1p`uj0D&385)o*!{;J!YX)A$rL{ncr;TIFhILOQ
oY92HwDk+^{o`}gd%RT*SERKbZ6-LQ5RbwpY6e$#1k34Q|8I*KPs`L?p%gZfN{Ws61Bg*PqoMu?K9dZ95anaAIJ`H7
PUg6m^cU>ioP6=s6r-w(Jz=0X29D`8O!(T0yn-Z6b=FK?{oaw4QslcUS`Oxiq>sFDmR3S+xSchsAW!@<U@qPPrOjBv
bHsz4yroGIR>R6Rv9bY78$UeKl0=_Z23k9`IlYXq<gatL(@hjv$DVz}fLbL1;Nc+Q8WWopVcF}(&5_j*S1JyzKB1qV
VRhuc4Yehqu&p>9jON7qW<M->q*tKQ$LS;X<Q()8HvSv2#(*p0Pf5yN6@d>bi<ndq7ntgU%f86w9RYKqn0P(cAEc@f
FJHMJ5`Nm--}tFzLtaL5vw^F%o3=|$SN<%9tXxmx$}81BiW~NN@+!p?Urku3O1HY6qIJHY;Z!~XkbyZF(t>w^pVzUU
#I|)35=ipLDj`<wYvuC;DRN?yYL}GP8>UTan5kQ$7W^eU;*dG-0wKcT--4dI4W<6Av&?}xJFw#BLq}CBw!7k<KE;4p
vG7AJTQ*$DH?}{CNN%fiWxuK<T<X_K%NI}zg2wL_DF10Ht3plf?S9d+q`D0|r0`F=*w+uQ8<t0pFrj3gkS+nTdJgDV
wTe7*nyyc3*;`(mt@9j?(s;QI1)akB$d8get%~8<bZ*{O_wjpZZ9?{!Eq}0yZw-5<&DqCA7S``EeMM~tU;v|EhfjU(
T{N1_5bs^OQS8zyHWx{Z|3+Q^3o{#2dEEaz*%xg8*3?^jQ#(Nd$R_*0Iof`7Tz=|a8^rdTSdivir&$q!WRM__wh$y?
6R(ZZmv1Sby_z>oE<0xRSk!gU&HrL<g1)iv!xPg%Rat2N%(a(YVFeUss{>!jEb^p*00(@&gB>sy*idd#S*`3>&G*Ml
j)V4Oo_@wvmlIe37{u<R?FsvtTE@S&T3|Q|!%0@^9tP9+a=E}*x*%MM+-&2fF(@@I2^9^QH}UDRQRo#>Q>qK>^bvhN
&x*vXI$|QpKP<`YepVjU%$DYi1<?|vuy;`(S$DB1E#HbH_|?*z%&gsNS~yC0iI1{U5jcs{>MRI~2JlWhrfXXxD+{rp
I;YmyB8R~|VKI*T@PgfBYGMh6^qpWR0@rLTl$+aOsFN$^b~Y6%4dH}qD;YDW54!B8Prl>)3H@wQQhjgG21TBwvf9R{
iI4b%Wy1b-smeR-(1gUlM&*8u=EBh#e8C|7R8Qr(xU<iU!9<Khb9<c&Qz^xK@e~p3!HkSJ@9qY>Wjy`a$Y5GE6$HI&
Zv8fn1u{1yZe9y|2N_#pY3Lj@5@k5s)`N2uTARB@ysV|!=Aeiz-JsvLU#sKbK9JNVmt@v+TS&5Z-lz2@OWy>qZ7{Us
ytO&4>Ww%jz`7&7T+oj0emk^P_@e}X!U*tv11JnXS4#*~uisX0WvZ+I^r(f6<kdeJCztFPYE_yv8l#El?0pfHRRV%x
+uZEO+s!ORd*maS9l}~2Z$XuuJ!xBO;3@TM7^MQ1X8`QJCm|~-!pv-6`$Snmi_JYb&M|+@f#C!iiI_B^y)Ci7NLf1q
ACQ<1&qUhYX9l6eo?YM_%`A_=N!D(uRYX>@4u(8~tzamu4@VC>{dO$vKH&)^0TB12fTKE4N^8?ahCC>6f3O;1Bodd7
@dt32s?Aoj$H`(0>SlR8f9TsueLHrDwpZwJ@D9?=CNp0}WHROa%S^ImIqmQZ&X|<*6@>Wxtc(MF4ZHO?)YgqUi+c?y
>0C9p`$4VL|0}+{!=+$wH>#*Pe8hD7z-W&G4@#ztF0an=DCnDr%PrlAkFAhiAbZ2_QOot;?P`3=k&zE~DT)Cc2YT?B
B4=yag;HPG1rh%R(tX~~Ul$(`v+G*n$_cCSIrOgow8brb5CbDPC8UoaSvy=qg<~iU__ev<-*u5-5L<kX_uVxp@4M-P
Jr3ZV@(A}X;*Z`ZPzX4P>z}d#xT0|ET3-0bc`J{{>^l@9cjW+ITaAx#2r_OMdM+$$Jq|ArmroL!a-^HJCK5p5sPO>|
XBuw%bxh=@BL$`<=~{%Uc&yHx;I&shJ7^bYVs1)DQI5o0<A8O!96lyExgb<T3{>&P0w>f%N0N$QhPRv?NaJ`C6w0b;
IP86#cc#MdY3U&!H`p=(&`8*ljj_ap&&Kf#eM_cn#?!?RS24lSF=)dkv-xOw*>&_6jPDJExrRp|_mjhLro7LLP+6KI
(OjuQJ_81LT9QxYqdf9>{4AwDCy=yJR$g^!zkXDMMMrZFi_e393x%^pAg42ie2=x7XKOUDc!ZrE3u5eEgOmTqYCPLj
?^3$NRYS!89HoAHteg?O3izPa1<qGA>`1WMs4E8=bMtP^#!AonLjRDSG!|QI7#soo(i3<sL*@kyM}0bS7&X%k&W=(t
8FJ+Bt5mO=qx6`G*kdP0w(WiV!I25mijwW)vd()8F}@!d4K^I}A_J46EafaJxSy6B2bti`V{|*9bnw-lB6R1Y4u62J
FtW#9!#SR3l8;HA)E~Nv1pK~4+>eg0HjSVsG+~ku@QEn4X7K-@QzvUtHeB0#6eBL<u(pcuw-^M8y!$rJ$C)#6oyOM*
M&u=sM`0dmpwY~7s#EAsCQGl7&_fvi4Cf^WA3btBV9i1ym;5|j8)x8Wks11?@thNFP}3Gz{)$O_lH2_|Ie3q(hOFNA
e^>N$nB+KIMk3D4WcAj(Q6+_~<38?H(xCdUXPt)@cY!he#N$pN!=ygX<_OB-b}c2VJB#-NAU@n=ttl)}Euu$in6yAe
7*j@`5Fn+)u!(*1w<>OWc8)z@Jn?R~e|D7|QfM#|%D!ume=WDxS|y#qQIGGl(IM;&zF^MYd*a_{BG9<Q-7;^s$q-v?
@Vy^{1&7G$VnA@rnFAM_jp2e6Wa?mv4!JG&(WP4aT(Xr12%20)&h3|L^$)-t@uP!dT^y<Cc8?<#P_zi;wY4Cvbb9gS
yIg4nEcVM907izmOE$?vvdI2s<;b_vR2=@z2Skz>5HK6>dSt&9O%Qvy`RYL<?;<6NV_N;zOytCyND*W5STQ0!b{N*Y
mtSQQyMvt&(;thU_Yx6yK4uz-9M6y{+DR>r8^~{~aPayypa~30j*!kK$bA)r0;IB_7%F4D$}FR6)CU)V!`$dk7f4tG
$w?r{Bi}FDgb2OU98fWr!}~oeIODD65L)?@al;v2N6wZ&A-<I`3ZHy&BcWYV%IOdOW($o-FfZs)xk_<LS`Z@)zkI6e
n7->8=*O3WV24T~JiSnraqKRIK~pHfTH7mJ*<?NQ+0x#_Y#6urV_3`(${+)Z%DV9mJ0SA|>q~SnQaM%0Y+(Kwsm<L+
#Bjv)*_-oP(d3J8f8NmUj!cPSz4e(#mj&p85ytq=<Tor#ZRXstsID5_<f^X**a0sGiJDK^*=~l$+&kN~Sa0{;L?fc^
06tz$9cB3I0cGxhKzZ#Z12@$^pzn0@bOL_&B@_mJMOE|GUkGx8byxJ1co@_#e&SOYtvi5xO%R^ewD(CEz9V)=JBV|7
j>x!RM_rD_uOu#n{(mf``?d<%>t;Iq18+o11p`AC3wwTV6qDR7!H8K1MlO~Vg3nPZ(N52D)s?hyGUL0P&)~^%oCoL{
LSRywX7kS{8rC_BI@9QH5f#x-i|usZ?sqj!KyNJb{i<z&rYkN%T<b!*Le?o-ZI_oLb5?sr%&mSB-#d{ZM)OXr&%T{b
?JB6-h|2ZQg?9vQ^Mwl0yfT)oIA_Zh+sQI7{&-;H_6pwA>%~s{>M+u*EY5^zzmWdto1QD%GL&M9JQ{?n{?JbH?vXr7
EXLR9*^DMGnNJG_q6m!QAK>F1!wWl08lYbgz-2gqLC#x7xe4(e6xw?iW2)XN`-y}`5%31NWrwQ;kV2n|gfW;>K;8K5
j=(LIQ6wNcSS0%3(E;G<c}Ipf7Azr6IjPH?2HNTGzsok1@+kYiu4<Vi6J{~+!xrdRx$If7bDb%cc-5Dsa#43ju`S6I
deI2>z{hFm?SYBVB=XcFuK?t^{CqMR@1n>Tc#KCYxwzt`@Rfm`UIQmTY6E2=$kG(Vfc#l~D9wHUC63=`wycn!;*-Gw
@Ye4f!_ypGEXERrrW{9^x~LvV(|uX-4{^$u;`M~&a{@YmfCw*h(a0K=*{O<a?E@N)us;#*2H?cPKrAL#>y}J{v&&c%
B&mS!ef~=avbgfWUzjj}&qS&<E6V|u^_EmqSo0_y2`x{>hgffHGf55L+G)3`{Wp<~rl4jLJtm?yT0P<;%*3wS`J`DD
SCYkxN7K$!PFGb3jhnN$)U0eYj%e_uyGBwdJu(aoUEnb<^UN$<*0r>eQ0zU6phcab;GwKz*&jS}%Om*Wrg~(j*h<80
4lpR{1f!<!GSEllK;!G)%oKTDmYoFF`$%L$-y(=o!2ZC!z!((Xg_VdL%1!q}1;<@!nWp#lVTSH<@aVuRpR^+pScTj{
RkB5St%*UDqCfFJN}-mG5b~6IVU;K5&qJA)?A^TM6>$3gcbSNgTCc@x4%2xSZYp!4%~IR?iM23LkcZMBRy>UCU@EP$
*D5WbYyfOa;Gh)lV4%&#29%fNeyu&sx@_z3&!PnmIWzF{WBmdE3@LBdC8U%uBQMQWN4AoRrd;}!Fu&#jOx!s5>%`f}
x7;g0x_j@y@4AH;6<%pAABNMOiD}4P9x0GB9^O6%h>rR+(f!P3ksx3-H(2fGWYe?pSQ4*a$<04MUBF`4Q(H{t<oe@>
JU$ZC-vPKa1SAPn>k9T3_ofS@LPMtdyLHJn^nW4fiC=3CokTgRl$~ehRev~t#M8L3$hW^jW!x96Wn?$}w1FGUWad<U
y6bjgDk7d^1g2p@6e=8})hswfU*zNqZ7isH%w`4YjoC<rkE>sMKt%JfsiSdj+gV<%pA3i95h>Q*qy&vmt-sBIeAGu$
p!$S2zwt)ir&_!x?OVMa--57^`3=d!{$TjYN33)x*S5k)WoxoMJyb(rdTlIOqS9Ww6gHY^n%xZE)lW<yO0h<NBr7&J
R{Zuj%X>@h_yuX~zrcEDoREB|uISG!qhpA%n~jmQ;pw9l$bT`OzFL~`A+DlX(KG#tm}URE{K_S7QP&_<4y07z48=33
B5u_!1@TR&izUwt?_1pd2H%FM7={UB@`JM{aj5!@LsD1R@h+)@6>7cEr|?4^&C*G9pV3QMP)bPp!SCh$r5>GwaAzJZ
lHGTS#JM3+v04%{^)!t$s_1z++bS5wPk~^#;lVAp%N}gg`AvzAiWN{h1a4Bz1x36bkj2U~Z7IDdPkq&i=8OdfV0YaM
<~mWWB(_fl$uvTD(P}4`w7gdT0%m2T6sfC($;TB=vW<&Cc;STK*mV=~Mn=JZt|~G>@c@BGCBVU%TNas4EC>|`C1%L-
g21q6klKaUnhx#&F^aSCddK*zX^vuVG|E_Va}&ph;7Mz3y`Bhw6Kn>gH{C+TwC7C#8E9Q-JbkvA09=F_u}GTW5fP8J
=hcal)=5F7#vfqbbc1ua2YxNU?y>=e_Wcw7ZSy5hX|?5lC4X^HaR}HO8e2@RY>KAG-)A)c3^sM6ABm5pr#<N94$UkP
;yd~<JI-lpk9&Qjd5p7M#I&)Nb$L!0b?c8|kZ~4?Ylp@Ywh%82Zk=8R!D5n22A5EoPcgG)S3^fjCQBlty=jdOipsMn
wiK)xUT|}>4Ro=?Kk7Zs-L^-rG>L9@PpW-^`!B3sRUrpFoTJAVdP_i&Zy%=;8tVVpZ6+z^R?nHNzQPrh{>uwsXXjzQ
MDFFliy5C{hhOVI1OMq7s81gMer~Z_P_Q^muF89=%JL0vb>j>9V!3^=XFiTp(;sdz%<*<#+df!}J+*6PYOoe#pfM$}
vRIA#A(U|e^)5%RT6tgVA6#bl4Crm%oR|{W`NkvbiS9d$w^V_LEqo_-OTr+yOfK66O)9As4Mff+V)6%f4&!#YXbfhI
m?x|WTSTQ3mce#lMYhLOK-UoY4E%Tg6V9pNk%#n?{d=-q>}HH*>WA%4)(F}R9-k=D(VUqm4pL{P3C;^D0)O&v-c3E3
e9FY~VNZV!c7rD+Ko^sK%`WO>M;`ocXk|W0yOy_;OMq!~H(GF*+h5&uqkJ=Xd!}>^IR3@GA=E_#Y0#*d!&y~F;<#Yl
TNisyDwu&hmYEU{mKWk4BH2=f&+*?9Tw_;h?=*XR*t5^y!;WV5%H!VFk#?717c%HBO&6Oqf)H|a6|Kr(7Y8cK7~H}L
Tj;yHiYL9bT?If&lUmdC=S&=G0Pa@J;Dq6#z1%Bi0G|~5Xjf26z<og+oI+9cqR#N0eM`r>v&v`FOJDu&&n?G_2O0Hd
Y0Q-SNQ(PrKvFTrSW-wqE!YD@0vcxjCJLtACi8*P$r4B1$0DcWJuOwN{<w$vnd-t<L{5WkWRe%Wi>xh#(ukt+GR=HS
5^UN!4x1dZ#=IV@>fiV59C)lFaM>41`qWdqEk(n5@3X`mm-nDQtTb>6ugy~Mr|L1$9;!aZ)pF#>^u=p{F+1>$fcmC_
*{(q$hwnQA80qQft#Qpk^!%lN0Pee$(l?W%5&sMo0<yRYTXPVq)=`0;00_J;v?F}W&ph0>;Iy#8=5>74jSMF27!jpP
0oMnTov6)6ZZO<4JQCHz@`FM>-u^p5%p){*1AXDrEciZ_t*mez*@aHTvfzMY=^~K(0K-Ci(A*2g;SalO%6?j<1<n5i
b_Qtvh7e5;*{894`v~6v@<2U{v=z}AqFRb8b>V|ILJXp-E^@Q2J)#XU_W#a}S#4DSS3(O=yICf0Rj@LRj-h95l`qLd
JFjvFJ`lE7$)!ryj7)ShT~Z*CKOrCW|D6xTIh7L*3y{wpO~8wkVEGFP1$K!_^Tgw(`44FM1FSbN!J>&AKQJp*h`jJ}
CbJL%n7d$4F4gW1H=9IaC%T=8df0%UqwgkYJ`VnIrZSX|IllUKKCW9uLGiCJ`PYFKsc!1Q=h0;<1;@7hFa>CieK9&b
E0HuNTfnr2g!`PV=YjcBGg>H*ebl?k(vDC3p;!pJB;b^~u6H%|&&-7uRMuUN`6+sMy`riYC$4o;qdhTS%S}MB{FXh_
MH8RXBj<lc&73L~KV89@dSb6@=mIARq)*U75;LMDJfWhtSUxH~&X-Zn&?O3zeM3iM|6nT(X93&5X!yz-`p+DDZuGNc
r(s=sF6rri1Ar4j=%^TmXyn{IWU22f-NGz-q%3i|L)o<X>_XP(6C6Z&knNuPtCOU`8yOAd0MJyheRAWtqVEJ)f(jg^
&RDlq!Jk!wEM5%Oo6mR4Bf11yp6+cNfQ%BG31G2*sO%PJ3_0LIM`$FpF)CLRcY=#maX+~LAR;4RQf&%i^zbqyWTjmS
aHjYOsLLQ5fYd|CVZqYg>OFrDzmCOx#cCJ<W)355{#Lc_B&%^iXmX8g$4jHdBA#{)%{HFBN=nK`OeZ}#uRtl~b*!7N
;qGIK5r`+@d6u;oESRqh8WHIVdJOB3Ww*}rP4K3?+cH%0eFJ(e`gXbQu|!HI0_Dw3=)i)i3;#NYoSs~>s5fNfIZ<fu
**ritnL|JPy)2;ZYb144o%yQPQwGaXm*z8vg~*u*`#!6mGiOqfZ7Q8I+;O*x#jrO;t4KXxwJea(-YTO~rb&E(P<wxA
YYt!tk@%_jN<w@T-r>0>Lj_@gx9}(~6MFv%nxYXX^$+HX95P2}a)5~+>#F<8Q2EP19wRQB6#l}8s%-y=x7;3)c&4}@
8wec&6?iiFGMBoQ4u1(>(Vo2&X`+(PSo}>`+%L4<u=W>vMoUw>6MyfB9GG^FqsR2|Bsd+O8Sq|C|5>J3PJ&?lg12qi
@&x6uHp8|6z7Fd7t|b6q$by&3(u>DnLV{mW9aX=t)Y>OMHI;tJ^t14@&WDlQyFpaN&9wcQGCx>MA;N!+{Q~_ER+vW2
Sw7$D4GtCuo>$atM2$1E25JBP07yw6-K3*i6@5xy$iP2<{7Z-a3@z~VNybTXkjbXb{LWkFY@zLqBn4xxb2gZ_`NNB*
nH_bs1$g;I%SM!U$`J`N7^XRG!Lz`I?f(jQ&+x?@(pm6%S!~bNMS$i8&9}CAQVB!JEZB{=%?xf+1%l;kZR+@jr0}t~
kit!!U(I;?cRIBANBb(nBaHbj1y>AXM~hlO6U^q`AQ!bviHKUaskLfW7u$mg(NMDFcuWd1<a-;juq`~=8HfzAJ&)@6
z2&nGg;eCE-Vw%}%#lR2BvKKgP$&ZIb^14(H}zuu>{JBLuaS{(z4TEa9y$Fn-@%Yh><=EAaWHx^iof`CGU}{L_*QBb
JrKJsH}Swchldx&wm;Ov<^BQeZQHfvPKh1{J2eF9qfZ*0qP2<idb(~(@1kIq`!0^TR=^XK>z8##=>((Sp8wki*Nt@N
Z`st!`M9Z`uy1B6<Qnax{jzO+IO$?-=Y!*>chZ@0b9{;FU~EOODKChO1mU#KB*z6Sk>wBFhhK=~bLat>$K^GX=K#@M
+|Zw92fB7)0wi#T5)D|eKkDW5!3d(f&wwjweO0A-Chgo-^Me?ZQbA7frUgz&bi7Oc6OX7iRoV~aOSzhBXC*HH1@FVI
=@Wr`5>UfgFLf*%4=0{z+TZ2^>m*JY6o+8N_>27OF{{ME&VP69b^6L*fov1P?t><FU*c-p$hA|$iZt`@5+&%nV{Gi>
EpQ`noG>@-Qd$4|9+62sQy<f7k0@vzQUe04=va~QW48ncWLK)vX$i+6;?gDGKRHQ^?L)9_-;qi*hfrA4As-~Y_@#{T
^trDxxp{^#d2_MNwvWK~qfOS1=f!rZ4|clpG>OdIou0LFZMc7yRVLD3dr!XJ`E$v_XI`4Y8+#;Wq!DdG$C=2sf!QQ)
tN_A>kQB_&YuqW;LbxC^*YPA#)KY@AGy&j%j{h((-wEwe*6LYan(3|X=IWBOo*5;So=FK}Ugc!PoI&s<{W)GuD4eEZ
B1{sQt1sz9Sevwn;u6wpQ~?qQNS8UP`x|$g#8(NnVV7Y;Zp0;ha~W*$HDs4-54~8tw`<aT=+h+}p^h_XdPVTq;Am*X
L5iODj!g-wRq54Jf;DkG@lgyB_rkkL5weNDC)%xRXvMJLSx-0yy6N3A;hsCTzPCWhoESlPfUS*$AoWgXX%Y8hCX32`
C%Od(l&&n4?exIS`MD{?bnsDnnaa%vnorltg06<PrpkTf%zY6V=))}U)oVYZ3?wY@((z^qc{7}SJ}40#|6qOGv>Ek^
>XKk6=bo}~Ug{3sZclq8Tgn)!K&(jnx)!N+07b+(frnrtP(-E*Gu`rl#*q&scL@8r!74Rv<HYRnl$xZ5?HCARFTBGo
q(-<fauq}`xB2_I{m+tvwb-Ps+~LW<L#S}S&I6eofSF_24N@b2I%%(2^d)iKbMR|`wjl{5L2V#mLyJ|pFDj<j*qcLy
QV{8s=>P1N^GKb*prphMjGF+29MU5jpY4GWhv9hFWSAcEBK}*<YROz4Q;~3H3AfOtZm@`O|E9s9pV5eeO!QnT;03P>
t{79{787g`LqkA0r+vKF%%yIDoi!~vuH|tBkD>D}ZkR~l5*u8-OsqD`9m0AofVg5FzjL2e_=5)$dL0~zDOP$?`vq^L
1QYe27)FG?=HY&U@y6AXNwZVW`n>IA-%_*`lAWs0IkMmX@j~hOcN^q`W={|Hx~<_=-;sJ8vbXqc{F*k!2TM}v5>0xZ
x$ew2vox6PkiEG_=Kf>?f8*k#3{FBieuy4nbZj4=Uw|g+i|?Uq^$XGQeuX{)I_EY>`z9KM!N;@En3cc{?l?n!5d$`O
`n$QN!-FL2C##gjUCgnqJ!vDP3XZp@O~MENRSdA}4ywo!gCMMd%DLX1l9uJpU1`g1+A<s2S5Kl{d22P2*zdGTi(KeN
L45~u*u8PZsBmVgMFetUNIp!Hg0#j1WAR5E7bUBVnb7#_(moV#-GYVk7;(5+x?E=#py^a$+J6^1Eh5sm6<k^q1G$Wm
fX^CH5;SaSw5$Ez&J1RH+(l>`5Sqfi@dY`G1&3!a0hii+!~LS*^bIE90E`btb11(D&jvq1FHx{HWZXit$v!eY0w!;4
>>6_+3|3)_BfM!LyI3wKV|ha{mRLF2>dTkiKEFQrs|NMi$5UUu)=6GZvSOqjxyM(~FfUD$1Ld7U7X@Mi0Y7D#@GO!L
yOZ~D?9P?k7TeZw9JY86O>*Cp<`O()!&}eG_<!0=Jv6?PIdQ68dVv)-o9t-D?O3E)ZAo<d09aj#l{4wy?DAf2e21f=
y?g=1Gsb)rG+SgPl~cZ?Thcvf*18c@YAe(V0WpD~b!T|dErh66AVJ#7dd;2^_;k;Fo_Tn}iY|zKPb>l1KtvpzI)|HN
nY0avxK>9u4r8cecXj-NWk<d=dq)?DGatmP<}A4^mkf2jjV&r--@;av0SrM7ROUalm{5<}Rc&$X3eS8=zriQYhzL8G
%UR#j-d@2>09nE2bD45AE=whThu{tDq6F!1$APfZ0>o>HcRpCvl$Q_&0kZQaC&Tp?mptk}BZXKtC}9y+xQ#xNabN7Y
-x)bvsY{(gp&cb2k%jRwXix%RKla8z8HV!YzeA^0HH85KKl0uJBhJMGj>aoUP|e=-5MMc=U>g~Bb4*J~!!|QTw!Z54
Z!eP@qbk=g+|oz;OaHMbONGacCTc0$TKg-Zxb@;z-sD_iaN|9MAXQ{;l<NLYX54<XB&5FYczT|_9;AbHQwrTQ+QpF!
SFlb7QR@0lIwc0$dwsej71-wjRjIl02}?$`6s77P1lY+&h{m9Z&PrjELda#q&8g|V^8V^`M%Uk&@_Tqe54nT`ONo&n
>`QFwqEE!p$|rrUtd$J5=sM<)zfa;NP11>9o_cxe61%eKI>9ufSiW<)=~7x@T2T~3W9f_MNkBPq5U6%2mhdu{X%QYX
n?IC(R^a5oV=YAr<u@xxOXI6Qb)Or!Ar%-DWR2r0zH9R*EQ~B&Pn8i|PF(?x($IamazaD>H!AH~gwVU*RTDKc+K!>s
86st7qsJXnA=GMB0_3rhPvRcd7hCi??LE{<_Z8LBqF>O^g*uC0#kii9T+j?R+PXx&FJ7i96$C=b3E9REbY~pGKrUlG
>{hg*Ta38J>e$0#O74ZU^XW%pA3*{Q_%FcnNIps_=P+gP(Nwl5&8O=oQoAjy@Y*qP<OcwN^T=s*c>>w0t}DG3h8;Sx
U)62I(t$b)Z;&JXs9TwgcVzC{?sO|C8V<gKqkKT|C@%Z^<GlzMN?a!!M@U5h5%rWg7jM1)TK)h0RE!73f%?7iYYy{7
*N*Tl=oV}F))pW)@xji3XCJHo=Ev=G=_DSBrU~Tk98k0p?c<iQjm)!tJc$qV)rhMm>a%$KsTUVb-`W?j=o^o_$L83q
t+(FTmW7!o@4#Mg5JF5Y@d9G%Z>+A&h)pK?fG!r_t3l2WaZZS_(jjf+RjITvO$Uv-ymiBJzx8(g9~=N9GcFSP($5qd
@{M8QcDb%rsRTx2`5xZepM@NAC~T+b)g^FTCy5lE5BIzaqhi0hBTWYZIGPB|^>p8$#?%!ZlyA2LJdl<=7cg@l0r@>|
INDqu=LQ|G;s%#1IS0q~%*9fRo|jr%HfPR`ACV;DFN`*6W^sd}oOr^qlvnZKFldU!S|S3{yZrF0$L2CScM$H6gabHQ
@N8zq6oFLo)OqTLhp6u<`af(Xt;rQ<^#y?sWRMk=VLFN_X}W?JIqc@>eR=&{UO$t)TDKJ5|9Q4dDhv7#oWNR8ip4{p
<)(0F>EF1qnVUF!ZtWTt;O(t+MH3>mX3u$>I#QU6k*O^!1GAdiu?BA34Fx74%GzUt27}iB2jNQ9F)C`PQ8t5C5EH&x
`NkcNLV<ZQ1&Z~2{q%vnKmp<qhL%G{YIP<-L+!g+*B2u6qS~X}flK$*RmQ#bd|7QYND}PLY>7Kl6~1`B)?%BZ#6TQj
CIq3+k1-Btifb?YdwIvrMjJc_j}1L6_rIKt<@HW5{_9kNw(HUnd_hxw6I|?vS>A-TYJ@$tqRk70ACH@1g^O<Y>~fGH
->c=5!eofr`rDBsmGK;Mf!&okUd9|XQSFqTlVZ>i76(U<)7bKFVhC0EnLiwv&w1(ZT>)CT8_Mzqu9ThUl-fQ84sg#n
FL*{~n0aj=_FZLPrJjmqjS<n1;Oqtn|Jh&Rt5jr*KRi9yuAkJ#rH>F;kXCJI7#{@Bdiv<~@&so`*5w(;Gjd?qJlJ}B
Pt{Yb*nHnALE^1Nu~5GZg$2>Yo|e{o5Uw2ic+gCue<jdC`K<Yqch~h<tQdUpvl)@q2O{|?;q}aOagR>YR&Jl<H*OxR
1IbYh-WDDS0v~G9ZC()$=nFn#P+JQ1k_!E`q~IZvbbujIT3k(Zk`EY@V*`s3t4#w7NFwzpMXEY+un0x`bmk3~$#GOT
e*#~?eqwrmg<*V*c)gFbu1<R%C(%F+#fHV57S*IGbwg8Z#e*T3q+}2+y`~NR9a}W6<;-1L7rV{wB2Tu-Lgoe!SSNv%
>cf99xJxBzD{<JkX=YqSK2-c!$yz?-<2<Uhlit7K4;r@p3<8-V9)U1CaC+m>B6^ynB&_=RY(v-m98Z5V`L75}XOxHG
Z%J+F07V*K6PHt37aan6?HN<nR*oWjKi2kM4Y5o8&Q1FUBJa@f?p8WGd70oyt+!QcMK(<FeP5Cym;I&S?a?(<jAF!M
A@*eYBG1hQJ&nuqF~Sm#q<5XMu$g0L8rHIzB#IqFj~tC$^&CM?-h7Eh(^Ave7bltB#<rb5K7t#h<AYVp7v|^E;?{Rg
**9<#<rxpRF&RG}s<6M!Zt)~d#kc-HzOIx?k(sy6n_898olTYb@Aj0iE^y?`IYptVq>Kzn3F74&cni0G=G>-2Fn8%6
=ckHGrmTHj$(H`qd1M*hXqLbUH^qRHqJ_;s{x#$aq3WP>_r2O#m~rfrz4hB7k<6-Lm=5dmc|GsxYbmc`!C{SydNkhk
DZ1$wzWYiNQbrdSsay;BbJKFlZw{czhOv+`@KVci0hbqNRz;qPsgyoMT0r#-AhXEru($PdxsO?#S`CZ>Yh~zPh?|N)
4)KR`R?XitlAQnKVzS`FC4al6K!vb#OG{AU<#Egq#;<Bb@OZ|;`67J-6g5AP!g3ljkRMeJXJF?Mu|w{-dK}84qr`t+
z{lm_KP7%$ety>d(`32m7>o`Hyqk5S<pV4k+K&Ga`?PX!Vm%`9PG$W^!IA+pk|utoK@n%cET)VuxkoNy_vcK!Z%6{Y
%DdGhFVo}M!W~!<1k@J&r{V0p54)FPnq%xL6$bA_EKl#^;t3lEDdQc^%6=09POwfv(zy102kMB^@Zr?ddlw2iqSR1r
oB&k|8WY)x9HnETSjwOn^wqNxZ3<0$d6qZ-A{i=xFoTE%TxVFqMc+II)@_{`OLp{5V~N89VvwgU6XS+TV7&KwVzc<W
fSu6|q@lLgEYaIW{Mu3Od2G}~MP`n`PGn{gz&7jOgbiu_f+XuKTa<28ss+yX(ez}ihhR1g?*KXQ-4G6^)Ahq0hQ*jT
laM+_oI@X~5dx6vUOf<d$ln)~o{pP{%;#b;$!Qyriz)6ld(zqAZnSoe-eKwKpEs5MurV|S*n?x8I5dSTNPR9Nk&+7B
jWANLyiz79LDPN6znr1cM}q@wAebhv!%_YWuddBsI$)Qcm|HzZxpRr>c9~%SRcOlm>ui36MbBo+Oz#`JzIUsbE93gG
Z?6oGz^~ApoUx_8RKH$9p!?8-;<4kNMu`*Re+^Ue%Mc%vKITybO_S(nNh=HzN9Nt^QdL>l2Eams#zRCpV+^qMc>Cm{
I&1$)$p27He^x#unW^&LsDH+0FbrR_t&q!8x4qir6W03bxixo1SeJNN>&Zxidh!6TVve9(p|J*7w<%2HKvMx%9!79d
D8`-tqeGJ{LX<q=WcUEsq)+~4T0q^A0R4gxexS_7txBxSrD2OixoMN8thyhLuK_$Y8=|xxdOOl=4SwC)6B<$@Bn97}
ynzRfza$8c<Sov*h2Agr7NR54>MI!JRy?^4sJuSx?qnjeb#ekPMVDf2)R!0(V=0sr4Pk$_A4gZOnrUqja2e3PC(J?c
(-SpK#^>z#^EqGvDiniHA!Q@{$dTlNpg%R$oq&4E-nkQp7E7Q4@)fi1VgVZgLQRJY&<a;Dq|oO{B!mVwahKm&6HHFh
%HtVo;Sb*}bTSJaL7eIM3`x%|CsHFx#%|{2rKms#^`!`6(D9l`+39%jd-G7$^QnNAkX|yCCTFA9p9)d+@8rGyi!`xX
ONAYra|d&hF;T0WOd{7Zx3K$8tRv5WJuBJ7OjC<g_6wyb=l37y{zCnMf|}+dw6YcC#b!U<|FnOEM7R2y(N?YZh)V#i
`24<|)dj!w>=YxOo`oZ@NZMc;Rhj>T(z7)d!*zhDd-@zPb!4cg?7xKf@UQl(!zv&UX^{ZV#nFwTMkO-hSV@mr=$(5-
$>HOEC4CGo?oD({&C@w|YUumHH&O+g!iquHcwKHr11!M}c=R3C)^J4Qu-taJU8k*WyLLGD)_F#yFa`Dzs>d6X?~Kx?
`zK#q3;+A_K>_$QB!bI=jgW2x9rfCL%9-3(*n%_%#GYy<7=HNnG-N57i(r;Y#G{;}ekIFGdpAbz==Ui;m7O%3IgW7O
P>#BctT!CjjSzHB@xx@44-N{_Mq7=zurdGu00000mWTfyrx#a_00E(=0ol(4QZxCYvBYQl0ssI200dcD
'''
raw=lzma.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==75737 and hashlib.sha256(raw).hexdigest()=='3212a7a390ca5f9f9dc7a035021f43a8e09d9935e2415ea787fac7bc0eb0d117'
FILES={'pencil_core.py': [11191, 'd272ec9d2ad68879431e0bde4aebbb4be164e542ca95fe546af24007afebb64e'], 'pencil_sharp.py': [4931, '762272d2695d0b97ad03f175b7d258316c63302a84a543d6352ade298c0e1195'], 'pencil_flag.py': [2928, '3037ff12faf13993141ecfff2adb531207fa21e3012c4ddfb527dc23a402608f'], 'pencil_certificate.py': [8843, '2c855e81b4a55959cebbfa874008f6156fe663bdf8783c0a2b2f39c5896c17a4'], 'verify_pencil.py': [15769, '1108f6b347adcaeeb8598717bee2ec2cb6823fddba8c47012e2363904a60468e'], 'locate_pencil.py': [4245, '1b63b5f0ba3146ee0b6966dbc455af428e0fc3741c7cf147ecb91093bc34e2da'], 'prune_pencil_final.py': [1778, '810da7d5e8b16ad926e667dd99cee427717075fc66402988e365d0e3ac0c43e9'], 'pencil_coefficients.json': [24814, 'b8274c3577940c41be83c9211b313c3f1a6ec1e57bdccfc0663d816eb51e86b7']}
OUTPUTS={'pencil_full.json': [1144002, '0946e156dee3942d5c68a26b1219873beae9e34af902227a8c98cc65425dde76'], 'pencil_matrix_stream.txt': [498550, '4e2047398397dca1c420e6a2bf4b7696a4460402304ca450e47b62c89b77c432'], 'pencil_left_progress.json': [29956, 'c6163cb97963ca1b4a8d97b8b305fc28cc445cc93124ce3627100a443c8a2453'], 'pencil_right_progress.json': [75043, '90510a1414c3b809b1f6456ce7b3b45bfac48ea6aa9de6b6db1fb853c4954eed']}
root=Path(__file__).resolve().parent
files=json.loads(raw);assert set(files)==set(FILES)
for n,text in files.items():
 b=text.encode();size,sha=FILES[n];assert len(b)==size and hashlib.sha256(b).hexdigest()==sha
 p=root/n
 if p.exists():assert p.read_bytes()==b, 'Refuse different source: '+n
 p.write_bytes(b)
def checkfile(n):
 b=(root/n).read_bytes();size,sha=OUTPUTS[n];assert len(b)==size and hashlib.sha256(b).hexdigest()==sha
mode=args[0]
if mode=='sources':print('ALL_725_LITERAL_ROWS_THREE_CELLS_AND_SEVEN_COMPLETE_SOURCE_UNITS_RESTORED')
elif mode=='flag':subprocess.run([sys.executable,'-S','pencil_flag.py',args[1]],cwd=root,check=True)
elif mode=='locate':
 for argv in [['locate_pencil.py','left','6'],['locate_pencil.py','right','6'],['prune_pencil_final.py']]:subprocess.run([sys.executable]+argv,cwd=root,check=True)
 for n in ['pencil_left_progress.json','pencil_right_progress.json']:checkfile(n)
 obj={s:json.loads((root/('pencil_'+s+'_compact.json')).read_text())for s in ['left','right']}
 b=(json.dumps(obj,separators=(',',':'))+'\n').encode();assert b==(root/'pencil_coefficients.json').read_bytes()
 print('EMPTY_SEED_LOCATOR_ALL_CHECKPOINTS_AND_725_ROW_PRUNING_BYTE_PARITY_PASS')
else:
 subprocess.run([sys.executable,'-S','pencil_certificate.py',mode],cwd=root,check=True)
 subprocess.run([sys.executable,'-S','verify_pencil.py'],cwd=root,check=True)
 checkfile('pencil_full.json')
 if mode=='dump':checkfile('pencil_matrix_stream.txt')
 print('BEVEL_COMPLETE_PENCIL_SOURCE_ONLY_RECOVERY_PASS')
```

**Итоговая граница:** весь положительный pencil −1/2<h<1 теперь имеет точное минимальное число строгих U, равное2, при полном переборе допустимых SPD-метрик в доказательном смысле. Общая положительная трёхпараметрическая проективная область и остальная11-мерная решётка остаются содержательным следующим вопросом; proper110 и новый глобальный минимум не заявляются.
