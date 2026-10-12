# minimum-0188

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# K2_05_ACTUAL_QUAD_TRIANGLE_HIGHPAIR_FULL_POSITIVE_PENCIL_EXCLUSION_V1

## 1. Главный результат и его граница

Получены два связанных результата на настоящем остаточном K2-домене без контакта056.

**Точный контрконтроль:** существует однородное тело (V,E,F)=(10,17,9), у которого настоящие F0,F5,F6 имеют размеры (3,4,3), W={0,5}, контакта056 нет, но **Λ05+Λ06>207/100>51/25**. Более того, F0 можно сделать строго устойчивой, стрелку6→5 — строго положительной, одновременно сохранив очень сильное отделение терминального ребра от F0 и все три унаследованные малые ограничения на корневую строку. Значит, даже внутри K2 нельзя заменить действительную механическую связь общим геометрическим pair-cap для соседних четырёхугольника и треугольника.

**Полное непрерывное исключение:** для всей положительной однопараметрической проективной орбиты этого точного тела, после каждого преобразования с новым равномерным заполнением и настоящим собственным центроидом, **никакая SPD-метрика не реализует буквальный FULL253**. Параметр покрыт целиком: 0<ρ<∞. На двух внешних интервалах работает настоящий trace<51/25; на оставшемся замкнутом интервале — положительно определённые напряжения всего трёх настоящих полярных стрелок. Ограничения на обусловленность нет, U1 не используется.

Это не исключение всего пространства реализаций данной инцидентности, всех55K2 или всего слоя10/17/9. Также не доказано, что тела этой орбиты не могут иметь110 с другой полярной ориентацией. Исключён именно FULL253 на указанном полном непрерывном классе, включая все его физические аффинные образы.

## 2. Авторитет источников и почему здесь нельзя подставить triangular33

Используется буквальный parent `minimum-0069`, SHA-256 `d0f91982420a008eef0bc169a4c7b9f999710361057096a930facbf9715942ff`. Его FULL253 означает полный неотрицательный полярный граф ровно из восьми стрелок i→p_i, где p=(0,0,1,2,3,4,5,0,7). Его вывод Λ05+Λ06>51/25 нельзя переносить на произвольный граф, только содержащий этот остов.

Переданный геометрический pair-cap требует ДВУХ настоящих треугольников ABC,ABD и корневой грани через C,D, но не A,B. Он не разрешает заменить одну грань четырёхугольником. Его точное инцидентностное следствие закрывает20доменов, ни одного вK2. Мой контроль находится вне этих гипотез буквально, а не вследствие переименования.

Прочитан весь поставленный журнал с полным parent-payload и все три остальных поставленных файла. Новая капсула автономна: старые `k3_census.py` и скалярные recovery-файлы pair-cap не являются её исполняемыми зависимостями; их новый replay здесь не заявляется.

## 3. Буквальная настоящая решётка и точный генератор тела

Вершины0…9; ориентированные наружу циклы настоящих максимальных граней:

```text
F0=(0,1,2)
F1=(3,4,5,1,0)
F2=(6,7,4,3)
F3=(2,7,6,8)
F4=(0,2,8,9)
F5=(9,6,3,0)
F6=(9,8,6)
F7=(5,7,2,1)
F8=(7,5,4)
```

Полный список incident-facet sets, в порядке вершин:

```text
(0,1,4,5), (0,1,7), (0,3,4,7), (1,2,5), (1,2,8),
(1,7,8), (2,3,5,6), (2,3,7,8), (3,4,6), (4,5,6).
```

Все17 настоящих рёбер:

```text
01,02,03,09,12,15,27,28,34,36,45,47,57,67,68,69,89.
```

Профиль граней: (3,5,4,4,4,4,3,4,3). Терминальное ребро F5∩F6=[6,9]; F0∩F5={0}, F0∩F6=∅. Все восемь родительских дуальных рёбер существуют. Для порядка (6,5,4,3,2,1,0,7,8) точное окно **W={0,5}**, не{0,6}. Дополнение дуального остова в настоящих рёбрах — гамильтонов путь

```text
1–5–4–7–2–0–3–6–8–9.
```

Это один из контактно-неисключённых K2-доменов. В родительской таблице W={0,5} имел15доменов,14после контакта056; новая работа не объявляет все14 закрытыми.

### Детерминированные геометрические входы

Плоские вершины0,1,2 задаются как (0,0),(1,0),(0,1). На остальных14рёбрах, в указанном выше лексикографическом порядке после удаления01,02,12, поставить положительные **геометрические пружинные коэффициенты**:

```text
(1,5,12219,1,14102,14220,32,8740,81,76,111,18,19,1).
```

Это не плотности и не свободные физические массы. Координаты3…9 — точное рациональное решение семи внутренних уравнений взвешенного Лапласиана отдельно для x,y. Три внешних напряжения находятся из шести уравнений равновесия вершин0,1,2. Подъём плоскостей граней интегрируется по формуле

```text
Δ∇z = ωab · rot90(xyb−xya),
Δconstant = −Δ∇z·xya,
```

начиная с плоскостиF0:z=0; весь обход проверяется на точную согласованность. Высоты масштабируются так, что min z=−1, max z=0. Единственная нижняя вершина —9. Полученное тело обозначим Pbase.

Капсула не полагается на непроверенную геометрическую интерпретацию этой конструкции: она проверяет все строгие неинцидентные опорные неравенства, точные incident sets, все84пересечения троек опорных плоскостей и полный набор настоящих рёбер. Получаются ровно эти10вершин и9максимальных граней.

Полный исследуемый класс:

```text
Pρ = { X/[1+(1−ρ)Xz] : X∈Pbase },  ρ>0.
```

Поскольку −1≤Xz≤0 и значение−1 достигается, ρ>0 — ровно положительная область этого проективного карандаша. При каждом конечномρ решётка сохраняется. После преобразования тело заново заполняется равномерно; gρ вычисляется интегрированием, а не преобразованием старого центроида.

## 4. Настоящий высокий quad–triangle контроль

При **ρ=7/100** exact-generator даёт:

```text
207/100 < T=Λ05+Λ06 <259/125,
Λ05>999/1000,
Λ06>107/100.
```

Для ориентира, не в качестве точных входов:

```text
T≈2.0714529187042463,
Λ05≈0.9998219826219195,
Λ06≈1.0716309360823266,
Vol≈8.420268585922381,
g≈(4.3530079378552,1.2157500188687977,−5.933048566666892).
```

Все координаты, объём, центроид, настоящие центры площадей, d_i и полная Λ выводятся рационально. Два различных настоящих тетраэдральных веера дают одинаковые объём и первый момент. Проверены Λ1=3·1, ΛQ=−Q, Λ²+Λ=4·1dᵀ, Σd_i=3, оба физических баланса и все off-diagonal entries в(0,10/9). Полярное тело независимо не центрируется.

Одновременно выполняются точные усиленные корневые оценки:

```text
Λ01<1/1000000,
2Λ01+Λ07<7/5000,
Λ01+Λ02+Λ07+Λ08<13/5000.
```

То есть три малые строковые посылки parent не устраняют этот настоящий высокий контроль. Сами унаследованные границы равны1/32,1/10,1 соответственно.

Также **Y0>11/5 на всём настоящем ребре[6,9]** и **Y5+Y6>3 на всейF0**. Проверки на концах ребра и трёх вершинахF0 достаточны по аффинности. Это намного сильнее родительских необходимых отделений4/25 и18/125; следовательно, просто усиленное отсутствие контакта не восполняет механическую связь.

### Одна взаимно обратная механическая семья

Пусть g — настоящий центроид этого контроля и

```text
u=(1/10,11/20,0)−g,
v=(1,2/3,0), w=(0,1,0),
Nε=uuᵀ+εvvᵀ+ε²wwᵀ,  Mε=Nε⁻¹,
0<ε≤1/100.
```

Векторыu,v,w независимы, поэтому Nε≻0. На ВСЁМ указанном интервале:

```text
S=[0,5], U=[3,9], H=[(0,9),(6,8)],
strict(S,U,H)=(2,2,2), physical weak=0.
```

Все68 настоящих примитивов ненулевые. После умножения primal-примитивов на положительноеε² каждый становится квадратичным полиномом. Для каждого проверены три строго положительных коэффициента Бернштейна с его установленным знаком: всего204. Это непрерывная проверка, не выборка метрик.

Имеем q0ᵀNεq0=1 и Nεq0=u: настоящая стопаF0 — точка(1/10,11/20,0) внутри корневого треугольника. Стрелки6→5,7→0,8→7 положительны. Первые пять родительских стрелок1→0,2→1,3→2,4→3,5→4 отрицательны. **Контроль не FULL253 и не110.** Именно эта разница, а не ошибка центровки или замена граней, остаётся существенной.

## 5. Полное доказательство исключения положительного карандаша

### 5.1. Реальные объёмные полиномы

Возьмём фиксированные исходные опоры n_i·X≤b_i, каждую разделив на max(|b_i|,|n_i1|,|n_i2|,|n_i3|), как в source. Пусть 𝒯 — граничная триангуляция настоящих граней, δτ=det(Xa,Xb,Xc)≥0; веер имеет апексX0=0. Нулевые ячейки допускаются и ничего не вносят.

Определим полиномы отρ:

```text
lv=1+(1−ρ)Xv,z,              L=∏v lv,
D=Στ δτ L/∏v∈τ lv,
R=Στ δτ (L/∏v∈τ lv) Σv∈τ Xv (L/lv),
G=4DL,
n_i(ρ)=n_i+b_i(1−ρ)e_z,
W_i=b_iG−n_i(ρ)·R.
```

Каждое записанное частное — буквальное произведение оставшихся линейных множителей; деления полиномов и скрытых рациональных ветвей нет. Проективный детерминант тетраэдра даёт

```text
Vol(Pρ)=D/(6L),   gρ=R/G,
q_i(ρ)=G n_i(ρ)/W_i.
```

L,D,W_i положительны дляρ>0. Для W_i дополнительно непосредственно проверяются неотрицательные степенные коэффициенты и ненулевой полином; это согласуется с положительной настоящей высотой относительно объёмного центроида. Здесь gρ не свободная переменная.

Для базового треугольникаτ⊂Fi положим mτ=Area(τ)/||n_i||. После проективности его coarea-масса равна mτ/∏τlv. Поэтому, если

```text
Z_i = −Στ⊂Fi mτ (L/∏τlv) Σv∈τ Xv,z (L/lv),
NUM=2(W5 Z5+W6 Z6),
DEN=DL(−Rz)>0,
```

то интегрирование настоящих граней и F0:z=0 дают **T(ρ)=NUM/DEN**. Это равенство также точно сверено с отдельным direct-hull/fan вычислением приρ=1/60,7/100,3/20,1; доказательство континуума обеспечивается полиномиальной формулой, а не этими контрольными точками.

### 5.2. Два полных внешних trace-сектора

Пусть Psc=51DEN−25NUM. Источник точно получает Psc=ρ·p(ρ), deg p=24. Оба полинома

```text
p(t/60),
(1−t)^24 p((3/20)/(1−t))
```

имеют **все25 коэффициентов Бернштейна строго положительными** на[0,1]. Обратное восстановление степенного полинома из каждого набора проверено точно.

Следовательно:

```text
T(ρ)<51/25  при  0<ρ≤1/60  или  ρ≥3/20.
```

Второе преобразование покрывает весь неограниченный хвост, не обрезаетρ сверху. Всего50 положительных коэффициентов.

### 5.3. Высокий trace возможен только там, где запрещены настоящие стрелки

Остаётся замкнутый интервал[1/60,3/20]. Зафиксируем матрицуS, обратную матрице со строками q0,q1,q7 приρ=7/100. Эти три настоящих полюса независимы. Положим a_i=Sᵀn_i(ρ), j=p_i и

```text
A_i=a_i(W_i a_j−W_j a_i)ᵀ+(W_i a_j−W_j a_i)a_iᵀ,
s_i=max_ab |A_i(7/100)_ab|>0,
Â_i=A_i/s_i,  i=1,…,8.
```

Нормировкаs_i существенна: следующие целые веса относятся именно кÂ_i. Для ЛЮБОЙ общей физической N≻0 положим Nhat=S⁻¹NS⁻ᵀ≻0. Имеется точное тождество

```text
tr(Nhat Â_i) = [2 W_i² W_j/(G² s_i)] · q_iᵀN(q_j−q_i).
```

Множитель положителен. Это одно конгруэнтное преобразование общей метрики, не независимый выбор нескольких Gram-матриц. M везде равнаN⁻¹.

На каждой строке следующей таблицы доказано Cμ(ρ)=−Σ_i μ_iÂ_i(ρ)≻0:

| Замкнутый интервалρ | μ1,…,μ8 |
|---|---|
| [1/60,1/40] | (0,0,10,3,0,100,0,0) |
| [1/40,1/30] | (0,0,9,3,0,50,0,0) |
| [1/30,1/20] | (0,0,33,9,0,100,0,0) |
| [1/20,1/12] | (0,0,29,10,0,50,0,0) |
| [1/12,3/20] | (0,0,37,0,100,84,0,0) |

Каждая матрица имеет степень≤15. Все16 её матричных коэффициентов Бернштейна на соответствующей ячейке положительно определены: **80PD-матриц,240положительных ведущих миноров**, дополнительно независимое Fraction-LDL-разложение с точным восстановлением матриц. Также обратно восстанавливается каждый исходный степенной матричный полином. Пять интервалов покрывают весь промежуток, включая все стыки; source независимо проверяет полное префиксное дерево кодов0000,0001,001,01,1.

Первые четыре строки запрещают одновременные D32≥0,D43≥0,D65≥0; последняя — D32≥0,D54≥0,D65≥0. Если соответствующие реальные стрелки неотрицательны, тождество даёт tr(Nhat Cμ)≤0; но обе матрицы положительно определены, значит тот же след>0. Противоречие.

Таким образом средний интервал закрыт даже для графа, содержащего требуемые три стрелки, независимо от дополнительных стрелок. На внешних интервалах, напротив, используется именно FULL253⇒T>51/25. Объединение двух механизмов исключает FULL253 для **всехρ>0 и всехSPD**. Ни один шаг не предполагает треугольностьF5, какую-либо гипотезу об единственности primal-U или независимо выбранный центр поляры.

## 6. Что это добавляет и что остаётся

Работа велась в реальном пространстве реализаций: положительные геометрические коэффициенты, согласованный выпуклый подъём, действительная проективная деформация, истинные объёмы и площадь граней. После обнаружения высокого4,3контроля я не пытался объявить его невозможным по triangular33. Вместо этого реальный COM был включён в полиномы опор и трёхстрочные общие метрические напряжения. Полученная связь — **высокая пара локализует форму в область, где её настоящие полюса несовместимы с требуемыми стрелками**.

Универсальный механически усиленный pair-cap из этого ещё не следует. Целый инцидентностный домен не закрыт: остаются другие значения геометрических коэффициентов, другие положительные проективные направления и другие K2-инцидентности. Поэтому55K2 не уменьшается. Также нельзя вычитать этот результат из202577контактного остатка либо202557остатка после отдельного20-domain pair-cap: это пространства разной полноты покрытия. Глобальные34≤Cmin≤622 не меняются.

Наиболее полезное продолжение — расширять одновременно реальные геометрические коэффициенты и эти контактно-нормированные трёхстрочные напряжения; затем устанавливать компактное покрытие более широкого класса с точными actual-COM полиномами. Полная нормальная геометрия, входные коэффициенты, высокая точка и все полиномиальные сертификаты ниже сохраняются. Строгие коэффициентные запасы дают удобную отправную точку, но численный радиус геометрического расширения здесь не сертифицирован.

## 7. Полная recovery-капсула и фактический статус проверки

**Только CPython3.13.5, стандартная библиотека, assertions включены.** Внутренний source явно устанавливает sys.set_int_max_str_digits(0) для длинных рациональных чисел. Нет RNG, оптимизатора, внешних таблиц, данных parent или пакетов NumPy/SciPy в цепи доказательства.

Сохранить следующий полный блок как `recover_k2_pencil.py`, ASCII/UTF-8, LF с конечнымLF. Его размер11195байт, SHA-256:

```text
55505bded9f5fafcbd542cd0506a143c4ab1448db1af5cc8f092b5a826a6eb62
```

Команда:

```text
python -S recover_k2_pencil.py NEW_EMPTY_DIRECTORY
```

Восстановитель содержит без потерь ВЕСЬ исполняемый source, проверяет его pin, выполняет build и check, затем проверяет exact report. Получаются:

```text
k2_pencil_full.py
18892 bytes
0b024d28f201c812ad924ba324c1582e3a1c1d52b19c1d13ed248967fabf0fb6

k2_pencil_full.json
7788617 bytes
49d66aca7680a90236f19a9f1f3463d65a05945b0e48427168fb7914e4edc6f6
```

JSON содержит полную рациональную геометрию, actualCOM, Λ,68примитивов,204коэффициента механической семьи, trace-полиномы,50скалярных коэффициентов,80PD-матриц со240минорами и LDL-pivots. Это не файл, который требуется заранее получить: он полностью регенерируется из нижеследующего source-only блока.

Фактически выполнены обычные build/check, build/check в новом каталоге и отдельный запуск самого lossless-восстановителя в ещё одном новом каталоге. Все pins совпали. Это мои точные холодные исполнения; не заявляется независимый replay координатором или proof-assistant-формализация.

Основные terminal markers:

```text
K2_TRUE_10_17_9_WINDOW_0_5_NO056_PASS
K2_ACTUAL_QUAD_TRIANGLE_HIGHPAIR_GT_207_100_PASS
K2_FLAG_222_68_GUARDS_204_COEFFICIENTS_PASS
K2_POSITIVE_PENCIL_TRACE_OUTSIDE_50_COEFFICIENTS_PASS
K2_HIGHPAIR_WINDOW_5_CELLS_80_PD_240_MINORS_PASS
K2_FULL253_COMPLETE_POSITIVE_PROJECTIVE_PENCIL_PASS 7788617 49d66aca7680a90236f19a9f1f3463d65a05945b0e48427168fb7914e4edc6f6
K2_PENCIL_SOURCE_ONLY_COLD_RECOVERY_PASS 7788617 49d66aca7680a90236f19a9f1f3463d65a05945b0e48427168fb7914e4edc6f6
```

Дополнительные удобные копии, не необходимые для восстановления: полный bundle с отчётом и логом (`K2_05_highpair_pencil_bundle.zip`), сам восстановитель (`recover_k2_pencil.py`), распакованный source (`k2_pencil_full.py`).

### Полный исполняемый восстановитель

```python
"""Complete source-only recovery of the actual K2 high-pair pencil certificate.
CPython3.13.5 standard library; no supplied parent executable is needed.
Run: python -S recover_k2_pencil.py NEW_EMPTY_DIRECTORY
The child source builds and independently rechecks all exact output data.
"""
import base64,hashlib,subprocess,sys,zlib
from pathlib import Path
SOURCE_PIN=[18892,'0b024d28f201c812ad924ba324c1582e3a1c1d52b19c1d13ed248967fabf0fb6']
REPORT_PIN=[7788617,'49d66aca7680a90236f19a9f1f3463d65a05945b0e48427168fb7914e4edc6f6']
DATA=(
 'c-pOeYjfI2v+#F*h4$Hc3ke1rfsJkOq>9)$@mbq(>^RA@Ivka5U||r7B;!je|NV6L%;*9ndA82Go1oELdU|^LKBN4p{nfGC`}XkU'
 ')7|jG{&+V$wLjgQ53k-`jO_R4@7`Yz&u{FryNe6^`orz{r}NJv`+9VBa(-ctzMfp%-JXBAvOk-(KebzD6==b;<7M*~%}KR~jvWV)'
 '7tZa;<9xmozYMgK>zC|)8FhEe?#@2b(#(l`C-Jp;=q66`qAjEO%MO5wshifi-2|e!kKx?^O&{+*@E&Ua`q#fkh>n&ej{z)G)4Obs'
 'bq#oTyg>7ok5LvR-ZILP<$Omg;|8etfYc6vs7;dPLYu&lEL=vZ7B1ptl4)nM0#|w_`h);2TQ28$A8)yE!^oj=HCZ=Hml3;n(t7~U'
 '(wDRbe|OR#v%@H}7tXVtW{K^G(=bc*wjlt=PKMnT*lT#LoefV$pKiIXx0%U02BWp@L%9v*9y_3wGQ9((9y^3mn|0VBJA%>?)O4xe'
 '5!CeHxevWM%!JYbz}Pd4+WFOqgbh$>w8;+WiSu9yW~CN<9@6uGo*n41Pf)QW>TnF!>`{wR`!WK?LhMaMxzjO^0KB<pwgHK~P6s9d'
 'm<M}pb_h^=%rv3(kYO*Q_TlDqbi-kZ`?y3zo3&}0!S(QFboGe?jzkkCC<2W}%?~D;zsz)pxkf(;vd1LS(#M7V+<4I@%S3x-FIpIB'
 'uVGAG#DMhCtqjN><9VPzw|+6i@%?Q>n!gybc%17G%vl@q(0CR@aDXFvddV_P%iwj#GRF<q>Wo_s{6NVZGg)e5U0bv=Su(NC6s?jb'
 '0nvnc`SgNHVk)ecq*%^Zfj-2kYnsEYd6;JU!in`WmKa9UI@4Fim=I3bO05yQj|U4r4**kR5QzfL-7*I;Z`WwR47(>zG!66!p=%F3'
 '3Z64Pq}H%#joHG`LZGn~j;-0)7&umpOM4h|{9*VySaEznGqrN-d3RN!BUFuHhBd$onifHafAE;f8o~)BoDku(R$EvFnrK=Bp~g*a'
 '0&&t5w1DQ!=X$h+XY`^cRzDgWQ1msdN~}ndO5harVJ(%-r>SM9uuLAY8DX^2him+T=rnY-O%^B<J>-05ti!-97#hadSf{;gFceoV'
 '0L<I9NyIO5NCKQe5IjYT##_TERyCAR08zGDgCfSSHhV80L4j@&A1OqV{zQG(*pQBelcDrAhFeFYu*)5#k&c*moeEuJgJNAHhc85R'
 '`vet%O*R*o#(rtjh9Cv-=S`cqLcTSIAe<<q^bT^`=*SKzrm(O#?b_({-RPFfHGwe*eEoanO=uP|KeCD@424)UbJccD*u*mX<L1Qb'
 'n`7e#tZ{V4%j=Qi#|TCcJuZU8$pT$K6LN?x6T*+cPK@#-gs4#iS3-i-L#9t)VKDKGewr|`@#|UEcE@DMr4vvefUguZtPyi@ZXOUe'
 'D0^7_3{{<CQ$}Y-jkdyd(m+R<2kU;lOv5Y$$0d!EFq&$?!VP>MOY!_M&D|N0r(lYx`C1ZqVVo>IXAW-5BqJ9A+M^)hRzR}_j5eXV'
 'B!MH+4RyeG=<ws1e<wrr1GI<h=c7yOJ)i*r4S`ykWjuJ|pl{p8xM3dD<b;meSL(u~eKq<|RxsvgpnYrF+=;oR2DWLOU7D(mIt(jc'
 '3+xf#6BC&CVZ7yx;ZKvl4)Dbt!yonH;7hA$aqy+4J-={E$2l4PfCq4<o24?<!)A_~*3~i!#tm2y=rC>xMP?;dw_nng2pcNK%xWb{'
 'kSh%(jzPafEvYQc3|88IenF*<>JlX_Y<0&B%cdv;v4%ORy6cqcflW*9Q*KG%PFYp-p=AfGR}lGn3w4g9&1~F&IcH<AQyWa(mQwIg'
 ')OCQrg?eQ{m5p4Vj1}w<r+tC_l?JUcyg#%$4X61qw!ATinH`+D1qBxi18jARR#&xBx0?3ka%D+iJ%(bkSH%;q&z@Y#T(28cKmsF*'
 'g&{;jVCRO8lacP=+|z=23SM|+ZbJ!>_X`2Sxu^rkcY7=8;<*zAT=LY>fL>vzxnMb?(H&$<f61W=7JDDg0}bC1>j}rwPP~lK`__IZ'
 '&&qL_C=nf<!8-dGQ-slDfUWl%?hN&j?#9HB5TwqtCgYtj@`GpHHCpRcj$!;iRBU;@@dr2i$O|rW5RU)M{1=XXEA1*HvKj+_%Jmj)'
 'fd9h8^BHPm?oXR~3+=H#m3^5pc;#qE1<fX7=En*}QFRZfry7#BuPQ+7iE2(9BjexG0NmZaWP-e-&<U^LPoV@h$rlif5OAP*ZjZ-S'
 'zeAXZW23pz22C3lTIjC(Ae`Q396~7FaZ`N-T}4mwM`2QM7zH+>Cm2(K$_giJ(tusj#Hs_wYTyF+4!c#sa^5n@?%>qhn%j~g3!O1x'
 'ah02>owzB2t%}i1!Y_F90wH7I@)#fwQqYYq?O3Eds2s~0Z4%;`&W+=CKjP@Gv`iM^@Rm!1TPY1naZoxRugU2fDNnLl_^jWRE09)k'
 '#&(!6g$4fL975O<UkZ^+6-NNJu2N|sBS8VjKye3oH^8y4)~ZCi%rM>{>8g<w5R{3cn8B#M9o~-E^~LZC{32o5g_Q@x{pif~<bH{C'
 'g$LL{d{LVT<u~oY12<bx8u&pZ{S>qL(5UVr&R~>z06L>DrhSz|kk00=uXe;QLLlhLXt<(?a)waEB3772<~AO{CQ83H5<Zkz70}HG'
 '))7?tx=tfuo^qOw2d5m>t)J!?pTaUf^V8j4O}pWRH|#g?7vU*WDnZIM=m0eL0{oN#aATXlJeYE^etoZTYOotX_XHSyuz>0Dd5=He'
 '@W)94$BvfCB9{Yj38M|oDmNB|;XPN(KFyc&9+q>j80)<;_@>GNi}%3p#=u)H6JIFa*(T29g<%K@Q)GZ-MqQRq=sGDvVjrsEJOq~u'
 'dWo1AmFrh41KAuie1cLkn5yiQDh-Q}81F{1K$8&oEG-EhGSpKF`~;CQ8Oqey?G&`iSBJ=YrTu&T<^H{jg^&lAvMe=>UA^0o@V9Q`'
 'iJA!);{m}9+QNMP#{1pR$|BALhZlSH)lkA*XeU%As6X_g3RDIB)k$}wQl~BWC>Qn382me5pR2C`g<@G>q2q<KsDvnp9@vG3Zqfwb'
 '9EN6MGlDykRo}=-`3R8y)IL2ewJG2qMu8Tq7+~T=Dbt)dcovvD=yLl3u0Mz}3IdW4ogL_*=_^<+JRNvC)4<rNX-kp>@MzJ=WW`pk'
 'Dm(Ob8~KgFYQ<3z3}!Rs-gj$T_)>a*%;OunVBm995+ZH26kO@5f(M0MhJ4_*)vC#TR0^Be^k*}`7@8aU5(^IgxcKAYmhE=-@;nD%'
 '%|8>dWa?t~bKwupX0Y4Syf2ah_Y5k#wRQhcZRW>PkY3$G<?K}n_ftS8{}|AkAA3}GV-Yg&AG%0@JuO(g!XL8mTd24(^mprPeH5{R'
 'gyvRo*$NFyA%<RC;5B787ZBWQ5Lw)Dg<S1pIes=i2Ci+hqb;(tzOW-hx~{V-?U84XxfI0^g#DQB39%z^9}7<Xw~<?QKlC!R${hYO'
 '6sXVx8~JaRI8S!|`jtuBDIRRKoP*xspP3h6>OS=Ol*P+Aboj`8Ug!pcO&l-CY}HK}-xGtux?SJl@Q~gD^hqC6-FGsFT~U%#k~{YG'
 'D`RlUG3j=d3lLUc8t4Jw2&=Aet&ayEWffrr@3Din&!^wm@g8#HM?nSCLpICJECm&8bVi&Pb8?Tr!XC24O23p=#zhkYYzW?hXm%^j'
 '4mP{k45m>)K$gQUSJdSrre8jiq7)FQqSPE>^Gra99Tm;SpkDHqZw4(z*@n3J4QO%4EoVzCND&+G$FJ9N++JsSIn@1wJLuluax2`z'
 'oF(8tU*>UpI}^|T;32|(&n*>9%YZLgb4g&aGy+}x1mJ;35I7J2a2V)`LjEw0yEU5lxHDS#cu(mnl_f^_c{b~n;8V<iFolJuH<ZD|'
 '1Mfue(La!0ky!jC-QEzwWl_E4m+XpPv0Hx2?)V*h&)+km1pctVp9VG}7=TxWPlg9_Hb{b#*n}qjuo#@1D1(Y*`J`lW8zSO72P$)f'
 'HX=XJSTa33nLAS<zCjEQ&wY?NU{5;?G&=~>R0^e11t6D?6es7_8lEQW<cTWqH&<L_s|c2;9z5|PYbC03`pEpVNMb*-M}x_XG2$a?'
 'SD+Qk)s3R*i9M;61d*pdBht80X&B)tsRyACJ1dT^vIM$p_P{;LJAHrXBPbb^JP4QVc_++*MXDP=Hb)D$is9LgkwdXcFa(5xC7wlQ'
 '8=N9%9=-;MwQSMxm~+Q}T*Rp^*26GAZ9fDrDgTr_1}qJL4V-M5q+G8v_`hEVlU4uksBY}Qh^3E#9D<L*KQ2xLER+;boALy8C%tz%'
 '`#q@HxeuQGa2lkU4kBHg{Q~p7M9T$WsCmmoq*!4`@oW|ro0Yu3I9bjDkBWbFG;yL_900?v-IvdGYk#Y3(%{3@NV1B+I7`BX?ue5z'
 'Iw-^Rt4K46qp&w-F6NHaGRJ*~5>CciuqzKXVn=U0r^TTILbvGf5`=;_@mOTLMMAAzWV~V2##t9=B0RT)5e%B~BuGq>f`{m=P2yD!'
 'Ayv<XIHIXRG$I{UT`a39_NHa#k^Xa49}-Pu0P(Vx*EIT`6*kf9d~UoHgg`tzIWeA^J|GAX84g6Rt*2(85t{%*crd4+C%g&}fCEIe'
 '0OFOL?OOS4u;0h6c;&B+tofV|eU(RUAfzh?b=eb0Ys@4Gd^*#N@j&w)VpXS#IPFqwJ&YU3G5P~&=!Vm1=npL@+&3Dt_2lJ@`Au^('
 'Ji|&!eK$xVF+KBxX%Yk+GjUZ^kS9c=%G3$Y5OsruZ(YqA^C9X9qJE|m@*$9(QOSqWM#dVW*pQBA5@djU6=8K1xk#f}rX_`eQeIXh'
 '$}IztrK6g8s4^#J6SFg{wU*$cEDKNp!6!=}c3c-Z1V^xn<j8rI?dD-|_N!93Y2V?*<Z}#nC4R887d!_HQ5F~j<TXpxeGh+ZO-v3>'
 '`QL*ZZvD;R|MAZvIuW@wbX)~Wbq**)3!_er{BmMB&MNpoN0<t9#VG?>_E{`O7Jz7-F&B-%mKj<eGOO6I8NJ+qBY^Pmi6A9v^oC>J'
 'og%C=ea}E}r|hE0aVZbClE%XMQ_q<Pl%lmTN9*Fj4;G$F$GOpF_E2PYXfTTm=87UBadlnE2<VvAY3g*uFhg%jXhegx)~d*K|LpKr'
 'qOB5)+7~$o5F^G*5${e7*3fD3!0NdAt7}P_8*-et#rMC>cU7Y)l&3gPq2Mio*eIO9F9y@<bgM}@G}_dOl_?9empbM+&c&hSTw79F'
 '_%Q{aaS4%%7C7F$xD<r}64RbSv~5`m;)Z!AZ4o%>V-oDtw7<{(<6NEh`*hnN=6_3`+!TR4;Ra55<p9NDD+YcS@!za;e3lu51uv3v'
 'D^U34I6gtau)OiE-f2YeEK;|av)v{*6#>ZlF|vJ(Jl|S0<g}=A3aO#!2uA&VmWM#djCYqpBs#zp0AZnjvG&L8?=$!%Hu+-p=(Q(?'
 'pN_6j(MaiGIYZr`W-|uYTrk|3z7LhqS#{~`8w}<uaSU<`)+m0#cN{<o^gp!^5&Api=%MoxO=0UJ+<3f8muckRh;%vbKnr;)NCID@'
 '5LR<C?O@kzw}BlN5Nn_52jDQbjlsKj9PH`4QwFsVYkuRF5R-TB8Zo+)SiK9SFXYz4OCjSVFC}#;ua}Jnw-jf8!*KHIsv_Fx1tB$V'
 '!6u=k36WDLh7VhW?bp{jj*xuA8;r_Hn-p4WExthBobfysfv}*^1`Dyct1ILXJUuHbg)fBW6{6|n!Hct&bJB+Et3-7o2eB1K@(62%'
 'Z=%{&3dY@B-v;zT;i8(&x21eNrF?58PjBEbl9u6(;_wQZX|9jUs=Ipa#gK%}^U9>O1&tHxL%~;%!YRR1Q0U4a%rvC+R_8bccCZX!'
 'b_O-bUcl#A<Q&2~k=Ci>Q6b1&bFHSg7R+Ao3wFv+nK~7@F+jC*VCXOW3-A}ex<)bMI2Vd4PIS$$*--T#!hossI1L~emOLbVCwhSm'
 'IN`#95phzM1Zj%V@QeOL$9n13n?wZ<NtQp;pA0sXx88_+Pi&ZH_XQ+&V%3K?b;{cOgG)^kC%P}2gOa}OkZ;3y;1fILzUCSu#gdWU'
 'zU7uxc2-N)D=FRF7{Z=FXq8r^K>WUaE0(<F&cyZ=t!o0|aONHy=7%Y5NBu6bAI?kxc`DpZT&eA$jfBMk2|#0F!cMQ(S?RLMU>-Ot'
 'sW3!XNBzhMLfne$<y0f0x`CVWf)Yk?OzWl<1ONP{6uP;>sDkpog;0XxSY_L_B?L4eQF%}@0E6tuOL)~@1F(l07;$k08gw{XGzfR$'
 'FL2^w2Vn~IbMH#w%wSGDIm<0?DN}`gjN{H8)9ZIvH>2AR7oSI`_U*~=0+@~|2)MQd*PW(|M_7UcGGk~Fh-TfavjwF+#cR6`;}#g)'
 'RHF}pqU2GKCMU7M?xvwHqJfwLyI<GGgJt3e2^zT~ypGG^HJ+sRsZ*2VozoaEy+JgweA*0x)DELYLN-?{jusSC)OvRpRMW0*wjRO#'
 '0-rPs<9X=O^={35(Wv2nM34n^z6W{XN`zw(Ns)4EG#(hlvg#@nUS?x{>)|K-i$<Q8_!3a3+W<ukPE@!8pb?=9Ya8<FpnNw=?>L~+'
 'fhtTo(yrv?g9S|B+pu^+Bu<o6fv3-qj1HrP!rs^Z)GqJ}JY`yBa>bi3Q(!_ul);YRnOh+4(Rr9MpCJ7(G8JcR-pfwy<ilsY->ui%'
 '@L!#Y+uV5V93S{XcgL{Rl&we9xL<BlP2DcEt_@Ueog;)>8JG_{kb@5QM4Jpp=l(pyTbwmbTxK2`gA2MTmfyEEHt#fVxyL&O_OhyH'
 'F;c&CK17ulZW*)**{E&yLap)230gR&D`*$OQED_g4PWWf5|@R=vEb{Q_P|$q;nmnY)C!w;o1}jsP~^JARZc^yx}m1~$y~<n>rb%W'
 'ybLbU%1KjRjW6aZ%)`SPWvX|Mg(^t`;KMYqNgWFnD>f3!Et3NJzg4v3t|h2anOt%xxrBkB$m&EaBo|HHEeo467q}thQ7feT)#a>|'
 '$X#QW{2qREb<~BJO_q<5Pxor%KA$5-<!?%K<;t=yQBe7k0*1IURnYppoJkNDipz1<D!=n*730nF_^||_4qPHS<a4*g%zeUr2lL^p'
 'LN$p6(TcvxC9PPpd{VB=S9X4NlJ9!;8uHI$Ps(=X_X}M33m|LSbeWZD7qZ#Usn;Ru0n>v`UsdrcrbFCBo(TC2T2Xn<<cqv~g{*{N'
 'z^-@tCG$yjoOcF*6;VYjj;ag#Aj*WZygQwrYuF`SNoO4Y*CP#aF!Iwgjlo-9d{yv>;WyTuQ*8DY@O^nvr>yXPUI_u#k3)^Y>#NG#'
 '(aA6#jEKTY6`s`ni~@i>JVjZ-Ga?Amf;i=3VJdC=yYo}J$R<(@y6o#>YCtB!1X3?AR!aH=OBvloRaGT>tkYLUKm^1lcbvcjVK9M6'
 'hgGLTq?kSf)li-8^;Jy=B{7|<+7`&J&G)f1UlKrQ;S*`p2}Y_usd)$^p8*QumLbBR<Xbq6I3<T;{Fnv^iY@@9!$9}tPHL)SN0>x7'
 'M0iBiF{;;<+*COa>k5@`xK*3ri~`}NQofXEr3K}yEf&EDf?F09N;HcBFlX;jcrrO1c&EKr(>#xtkM%1jgoV-bJga_N2kT;iD=;QN'
 'SanBL;64;p@2N^}(?@jpQC(rdvAJ@rS;qiW5()L?^Kr?!-`2aoFFz4N0&nZk>yODpQ&)KK)^1r=@Xjd6BM!Z)kJ)+~-Y+q${+-$?'
 'DgQ_nhJl6cWHts8;-JoT(lF(38404KITLinj*qZiiLC+<?s@rzid<#cNr1;@dg)q)ZTo@yIJIqBGJXPyd<0tA4x`D^>UV+Ccvrv6'
 '_EFk%`&hc{iDzoSBE=E%#`OU4^#q1is8s2@K`ZQs&F&b?7FNNMWX3`$dsOi`Unt=CJ>h=AdFrFC?``~+@yE{r)inRnnd6ao%GW;8'
 '30a;_`pKd8k7Az{kmEHdfgBl#E9Ec(y>9+peS<RDP>M*63Wy1SkcS@mG(QITwW;_rbB{g?Mc=zepN<ynjx+rVADkEAF#N%o3s;0+'
 '*kpSBua5oc=5A!0ZQDGskL)k!SEnDo*ll~?zWUJK@7dSG+uJ&b>tlLPEQq88ZdREfl`Jv_1z!kmFW(v}M1b4`v_y%tn5CRhz9O)Q'
 'Z2|T;!PHS=_3%zqXCH!u&c2XLY<P2~A01)f06k@84=YVMItQ45?{q8;Ry*(AX<$7-KfuNVh&@z`IBzTEx9P)L{I1nNFkR8Lrr{<{'
 '9c53%b*l|Mux^E|Rq3b<RM!!imSt7|>JT7wO{&25*ELCRZ2Shi_#nBOoR(M{Z^$RvFEpLR!g$jy^T)40Mt}FohRp*0X>Vhd$%JqB'
 'nFa;?vy0(7yVL2|y+ixm-SFo079j4~Cm%*<XXhv9Aey(^K#NQSUr$Jsv!+f0Y`7jbqumfW3Dre}&{&UmDd|geWxOM2K_aBrA-t}$'
 'I)>Nv@>N8%eG(4#9Sg-SJ{KxdIdqa)>eXMj-vgSpWPw#u1;usnA7n`WQG%nhw=Kf~l2u}qiZh`og+!q2Z5J0hmwxxwu0*M#FTM)f'
 'P2}bK?J|q4|6>N9ZiXi#`@`L*+w;?rz2E*VGa#)&vwQM8Ez<jxyZ9kap+$0r5@&r89bj1mAuv*AeoG%<pq<)DGbhPXJdhJZi_bA='
 '6z1m?Sj?VP-_1JVg%$OB!Iq#|aML=C2C<H@0hAcX3+D4wT-?WuBYKkqU>3ZfBRP|}OXh*|)vht7N)vN_n9I1T%TK4A=c2AHzh*0r'
 '0*Hsy71%ISXp$d|2T(G<D31)G2j@VEzRRJp`0z-+{UnL4gkd9-E$nwWmkp-<n49|m%XO<cZFAqK^cz<|Z28b!MCm`jDO~lYU77LU'
 '@Tp}!L}gsv`O<q3+30ooGJ9gi%Sw7(LH>^u>(yJY1K;PA2)m?%)5Rj<`la}SnaOA4Qhv#NnSaU5DCKZzR6eAEv4R8SB9!w_?kVx%'
 'Grwf>z`-waZOM%=h{61J9IlpG%6*@{R1iFiSzghtiFeEeQ&*rOD{<oF!u_S-Q1S*>ry$-kn1J~R!3l@Zh|nt=H6<kcFh6od<UpTS'
 ')J$%)q?faApNuXpZtX*`U8gp5wlB}GKHO~8Fcn`Nzd#7H7heDW^3S!@<t0pR)tz)|U(Vh}mr2_D^4EO+9ABKjKaA(*MG}Mg@!OLl'
 '^XRa%*J(TL_F)iA+OB8zj+{O3z&)CPGjw3KyFIhLf6zYaIY-_0#PQq-)b1bcbtV(=!xUxZSIHPr1jX%ca_Ol`-X0O|y|}v#F+Y7%'
 '2Aky}3A})VZ_R{PEgW0AbSgWK&X{uB<&%k2^a4XEa%{;fmH*}o7ttUBKu<_IDGYrQs*uhJMUH$jVf63D*fJxuOwe9l-Ce>8MFZfs'
 'Twr!dG@Xtx4wKG8$s3XW1CxqLoFGDfD&PoFFHaPqL6nLXp{eOt23rdUgsFUM9ReyRnXb^3lP_V_>7UI37*?H5hD2_K;xb;`yV@4C'
 '83Qm$(;(yc&(7$!JqhQ5Z5umiqil37^!nOAz=L-`>!lM3bn^%ps50x|;P9|#9<ch}k>Be%o^#MUY&%EoPPaEPkDQ~4IqB~8x_)op'
 'X#)rCyX|1_aIbS<_6{fR!I8Na>;=BpoAl~qy1`m36`U!#wmgMMi0>qzKWz6U3sN1kgM>;=m<ieADG6c4qKibeEW{{Io&7Gj1eezr'
 'qfeufXx)7HuhB_a%7h#@N{g-vwS;>6;qK;SBs;EAwv2CeG_2Pqn%g!k*0yoqZM)tV`(OKCZ^%IV'
)
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def main():
 assert __debug__ and sys.version_info[:3]==(3,13,5) and len(sys.argv)==2
 source=zlib.decompress(base64.b85decode(DATA));assert pin(source)==SOURCE_PIN
 root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True)
 f=root/'k2_pencil_full.py'
 assert not f.exists() or f.read_bytes()==source
 f.write_bytes(source)
 print('K2_PENCIL_FULL_SOURCE_RECOVERED',*SOURCE_PIN,flush=True)
 for command in ('build','check'):
  subprocess.run([sys.executable,'-S',f.name,command],cwd=root,check=True)
 assert pin((root/'k2_pencil_full.json').read_bytes())==REPORT_PIN
 print('K2_PENCIL_SOURCE_ONLY_COLD_RECOVERY_PASS',*REPORT_PIN,flush=True)
 print('RECOVERY_SOURCE',*pin(Path(__file__).read_bytes()),flush=True)
if __name__=='__main__':main()
```
