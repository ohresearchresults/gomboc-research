# minimum-0067

AI research report · 2026-09-16 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# C34_R1_EFFECTIVE_SATURATION_GAP_V1

## Результат

**Для всего насыщенного первого среза получен полностью явный универсальный геометрический зазор.** Положим

\[
E=10865\,2^{158}
 =3969803822400065051570758926865603752140426769858560,
\qquad
\boxed{\eta=2^{-(E+20)}}.
\]

Это положительное рациональное число. При принятых в журнале универсальных запретах U1 при V≤9 и S1 при F≤8 оно подходит одновременно для всех настоящих однородных собственноцентрированных тел с **S=U=1, (V,E_{\rm edge},F)=(10,17,9), R=1**, включая разрешённые нулевые нетаргетные механические примитивы.

Именно, следующие величины строго больше η: расстояние каждой вершины до выпуклой оболочки остальных вершин; аналогичное расстояние каждого настоящего полюса до оболочки остальных полюсов; все неинцидентные slacks 1−q_i·x_a и соответствующие расстояния до опорных плоскостей; расстояния между различными вершинами и между различными полюсами; площади треугольников на любых трёх различных вершинах P или P°; объёмы и нормированные объёмные доли всех положительных origin- и vertex-apex клеток, построенных на треугольниках настоящих максимальных граней без новых вершин. Для vertex-apex клетки апекс обязан не принадлежать её базовой грани.

**Не утверждается положительность произвольного четырёхвершинного определителя или всех механических примитивов. Ни один полный тип или корневая орбита не исключены.** Текущий реестр остаётся **632 типа / 52 585 совместных корневых орбит**, глобальная граница — C≥34. Это входное состояние журнала, не заново перечисленный реестр. Журнал до настоящего шага доказывал существование геометрического η, но не его числовое значение.

Существенный шаг — не повтор компактности. Ниже построено **базисно-замкнутое множество в 53 переменных, заданное 145 целочисленными полиномами степени ≤4**. Доказано, что даже его первоначально допускаемые геометрически вырожденные точки обязательно восстанавливают одно настоящее тело, его собственную однородную массу и истинную полярность. После этого к нему применима точная эффективная теорема о ненулевом минимуме. Нет неопределённой константы O(1), произвольной отсечки обусловленности или минимума на выборке.

## 1. Точные посылки и их статус

Буквальные родители аутентифицированы:

| Immutable parent | SHA-256 | Байтов в аутентифицированном v2 JSON |
|---|---|---:|
|minimum-0054|4e39e8c2a461dc76a76e49153b9f70ace7e0e287cb3fe5e6b3c3733a8c24d774|30115|
|minimum-0024|b578a01ead261c6f7745122c22f4bb4767884e46ac46e1531b4e749a19332f95|57975|
|minimum-0029|07da26de37a7076fae43373e6ecd0c85ba0b45ffbe359ed38b707c462083dd8c|36226|

Используются ровно следующие принятые утверждения. U1⇒V≥10 действует при слабых нетаргетных тенях; его явно наследуемая universal285-посылка и прежний запрет V≤8 сохраняются. S1⇒F≥9 относится к настоящему собственноцентрированному однородному P, в том числе при других вырожденных тестах. Для того же физического совместного тела R/r≤27; поляра берётся при том же центре, а не при её собственном центре массы.

Новая капсула ведущего `C34_ACTUAL_CORE_METRIC_FLOOR_AND_SATURATION_COMPACTNESS_V1` полностью декодирована: доказательство 24271 байт / SHA `137f5e255e2da1b528fe91814f36cea7b07a5991def2142b885a1321c578e12a`, точный контроль 3966 байт / SHA `c48689a08505f5d7ac49e28234451f164062a466d491adc9219989c8a8c93ea6`. Её холодный запуск воспроизвёл все пять pins. Это не новый запуск исторических universal285, 39 девятивершинных сертификатов или 1890 восьмиполюсных матриц. Их уже принятые теоремы остаются посылками. Прежние количественные off-centre/repair оценки здесь не используются.

Текущий вход `research-journal(20260916-123126).md`: 4738679 байт, SHA `969add9dd8313881d93a08e127358159b5fcc3b1ceb177983f3ed0307ec64cdc`. Конфликта буквальных утверждений с используемой областью не обнаружено. Исторические C32 и каталожные счётчики родителей не заменяют текущий срез.

## 2. Почему можно убрать независимую переменную метрики

Работаем в настоящих физических ортонормированных координатах. Если исходное описание использует M≻0, собственный центр g и физический радиус R, положим

\[
y_a=M^{1/2}(v_a-g)/R,\qquad z_i=R M^{-1/2}q_i.
\]

Здесь q_i — нормированные полюса относительно g, то есть q_i·(v−g)≤1. Тогда z_i·y_a=q_i·(v_a−g), физические тени умножаются на положительные множители, а **одна пара M,M⁻¹ превращается в I,I**. Аффинное отображение сохраняет однородность и переносит настоящий объёмный центр в ноль. Поэтому фиксированная евклидова метрика при переменной полной геометрии не является ограничением аффинного семейства. Радиус ниже — именно физический R=1, а не радиус произвольной неортонормированной координатной таблицы.

Пусть r — корень вершинного дерева. Он является единственной точкой максимальной нормы. Согласуем внешнюю ориентацию циклов и ортогонально положим x_r=(0,0,1). Для b=min({0,…,9}\{r}) оставшимся вращением вокруг третьей оси сделаем (x_b)_2=0. Никакого деления на поперечную координату b нет: осевой случай также включён. Это исключает четыре координатные переменные из 30+27 и оставляет **53**.

## 3. Полная конечная целочисленная система

Дискретный вход — любые девять согласованно ориентированных циклов настоящих максимальных граней F_i на метках 0,…,9, с 17 настоящими рёбрами и 34 инцидентностями, и любые два направленных к корню дерева на настоящих вершинных и гранных рёбрах. Никаких диагоналей в деревьях нет. Код ниже проверяет циклы, общие границы, триангулированную сферу и оба дерева; он не меняет метки.

Каждую грань триангулируем из её первой указанной вершины. Получаются ровно16 ориентированных треугольников τ=(a,b,c). Обозначим

\[
\Delta_\tau=\det(x_a,x_b,x_c),\quad
s_\tau=x_a+x_b+x_c,\quad D=\sum_\tau\Delta_\tau.
\]

После четырёх буквальных координатных подстановок система состоит из:

| Полином и условие | Число |
|---|---:|
|1−q_i·x_a=0, a∈F_i|34|
|Σ_τ Δ_τ(s_τ)_k=0, k=1,2,3|3|
|1−q_i·x_a≥0, a∉F_i|56|
|1−||x_a||²≥0, a≠r|9|
|729−||q_i||²≥0|9|
|Δ_τ≥0|16|
|4096D−1≥0|1|
|x_a·(x_parent(a)−x_a)≥0, a≠r|9|
|q_i·(q_parent(i)−q_i)≥0, i не корень|8|
|**Всего: 37 равенств и108 неравенств**|**145**|

Все переменные ограничены: вершинные координаты по модулю ≤1, полюсные ≤27. Следовательно множество T данной ветви замкнуто и компактно.

Нижняя граница D не произвольна. Настоящий P содержит октаэдр conv{±e_k/27}, поэтому

\[
D=6\operatorname{Vol}P\ge8/27^3=8/19683>1/4096.
\]

Таким образом, каждая физическая совместная фигура после ортогональной нормировки удовлетворяет хотя бы одной такой системе. Все циклы и пары деревьев образуют конечное дискретное семейство; **доказательство ниже одинаково для каждого входа**, без необходимости заимствовать старую нумерацию деревьев или заново вычислять каталог.

## 4. Главная лемма: замкнутая система не содержит ложной геометрии

Пусть точка T пока допускает совпавшие метки, нулевые Δ и новые контакты. Положим P=conv{x_a}.

### 4.1. Внутренность нуля и настоящая масса

Пусть γ_a=Σ_{τ∋a}Δ_τ. Тогда γ_a≥0, Σγ_a=3D>0 и Σγ_ax_a=0. У некоторого треугольника Δ>0, то есть его три вектора линейно независимы и все три γ положительны. Если бы ноль был граничной точкой оболочки, поддерживающий функционал одного знака на всех x_a обращался бы в ноль на этих трёх независимых векторах. Это невозможно. Поэтому P полноразмерен и 0∈int P.

Каждый образ треугольника лежит в опорной плоскости q_i·x=1. При Δ>0 его вектор площади равен

\[
(x_b-x_a)\times(x_c-x_a)=\Delta_\tau q_i;
\]

он ориентирован наружу. При Δ=0 тот же образ коллинеарен и не имеет площади: опорная плоскость не проходит через ноль.

Теперь используем **весь замкнутый граничный цикл**, а не только три моментных равенства. Проведём на каждой настоящей грани P все образы рёбер треугольников и возьмём их общее конечное разбиение. На каждом открытом двумерном элементе число покрытий — неотрицательное целое. Границы исходных треугольников попарно сокращаются. Коллинеарные треугольники после разбиения также дают нулевой ориентированный одномерный цикл. Поэтому числа покрытий равны по обе стороны каждого ребра разбиения, в том числе настоящего ребра P. Связность поверхности даёт **одну постоянную кратность k≥1 на всей ∂P**. Положительный треугольник исключает k=0.

Конирование от внутреннего нуля потому покрывает P ровно k раз почти всюду. Следовательно

\[
D=6k\operatorname{Vol}P,\qquad
\sum_\tau\Delta_\tau s_\tau=24k\int_Px\,dx.
\]

Наложенные три равенства означают **настоящий однородный объёмный центр P=0**. Нет свободных масс или независимых моментных матриц.

Каждая настоящая грань P покрыта положительными треугольниками, значит её нормированный полюс — один из q_i. Все остальные q_i тоже лежат в P°. Поэтому conv{q_i}=P° и F(P)≤9. Это истинная поляра относительно того же нуля.

### 4.2. Слабые деревья после слияния меток

Для любой слабой стрелки x→y

\[
\|y\|^2-\|x\|^2=2x\cdot(y-x)+\|y-x\|^2\ge\|y-x\|^2.
\]

После удаления повторов каждая различная точка идёт к корню с возрастающей нормой. Корень — единственная различная точка максимальной нормы, поэтому настоящая строго неустойчивая вершина оболочки. У любой другой настоящей вершины первый отличный от неё пункт пути даёт неотрицательную радиальную производную к точке той же оболочки. Все настоящие рёберные производные там не могут быть строго отрицательными, поскольку их направления порождают касательный конус. Значит U(P)=1, даже если прежняя стрелка стала не рёберной.

Тот же аргумент на q_i даёт U(P°,0)=1, то есть S(P)=1. **Объёмный центр P° нигде не подставляется.**

Принятые нижние границы теперь вынуждают V(P)=10,F(P)=9. Следовательно все десять x_a и девять q_i различны и экстремальны. Все исходные34 инцидентности сохранились, а у настоящего трёхмерного многогранника с этими V,F ровно2(V+F−2)=34 инцидентности. Поэтому не возник ни один новый контакт.

Каждое предписанное граничное ребро — пересечение соответствующих двух настоящих граней; действительных рёбер ровно17. Восстановлены именно исходные максимальные полигоны, их циклы и настоящие рёбра, а не симплициальное уточнение. Фаны покрывают каждую грань один раз, поэтому k=1 и все их Δ>0.

Итак, **каждая точка базисно-замкнутого T является настоящей нормированной совместной слабой фигурой данного типа**. Это устраняет ложные граничные компоненты до применения эффективной алгебры. Если T пусто, последующие оценки верны вакуумно; непустота не заявляется.

## 5. Эффективная оценка без неназванных констант

Используется Theorem1 Jeronimo–Perrucci–Tsigaridas, *On the minimum of a polynomial function on a basic closed semialgebraic set and applications*, arXiv:1112.0544v1, печатная стр.2; опубликовано в SIAM Journal on Optimization23(2013),241–255, DOI10.1137/110857751. Формула проверена также по изображению страницы. Для m целочисленных ограничений в n переменных, чётной верхней степени d и модуля коэффициентов ≤H, любой ненулевой минимум целочисленного g с теми же ограничениями степени/коэффициентов на компактной связной компоненте имеет модуль не меньше

\[
\bigl(2^{4-n/2}\widetilde H d^n\bigr)^{-n2^nd^n},
\qquad\widetilde H=\max(H,2n+2m).
\]

Регулярность, изолированность минимумов и невырожденность активных ограничений не требуются.

Для нашей системы выбираем **n=53,m=145,d=4,H=2¹⁹=524288**. Это консервативная доказанная оценка, а не наблюдавшийся максимум на единственном типе. Полиномиальная ℓ¹-норма определителя ≤6; у каждой моментной координаты ≤16·6·3=288; у объёмного ограничения ≤4096·16·6+1=393217<2¹⁹. У полюсного шара она ≤732. Остальные ограничения имеют меньшие нормы. Подстановка нулей и единиц не увеличивает эти нормы.

На каждом непустом T строго положительны следующие целочисленные цели g: любой неинцидентный slack; квадрат расстояния между различными x либо q; квадрат векторного произведения двух сторон любого треугольника на трёх различных вершинах P либо P°; ориентированный origin-определитель любой гранной тройки; определитель такой тройки относительно любого неинцидентного вершинного апекса. Последние порядки берутся по наружным циклам граней. Степени ≤4, ℓ¹-нормы соответственно ≤4,12,192,6,48. Три различные экстремальные точки не могут быть коллинеарны. Остальная положительность следует из восстановленной решётки и внутренности нуля.

Каждая цель рассматривается **отдельно на том же T**. Число целей не прибавляется к m и их произведение не берётся. Полярные гранные циклы определяются исходной инцидентностью; код явно восстанавливает их, не назначая нового каталожного номера.

Здесь 2n+2m=396<2¹⁹, поэтому

\[
2^{4-n/2}\widetilde H d^n=2^{205/2},\qquad
n2^nd^n=53\,2^{159},\qquad
\boxed{g\ge\delta:=2^{-10865\,2^{158}}=2^{-E}}.
\]

Эта вычисленная оценка действует на каждой компоненте каждой ветви и тем самым на всём нормированном срезе. Она не получена из одного лишь существования η.

## 6. Геометрические следствия и область положительных клеток

Для вершины a положим n_a=Σ_{i:a∈F_i}q_i. Для каждой другой вершины b хотя бы одна из этих граней не содержит b. Поэтому n_a·(x_a−x_b)≥δ и ||n_a||≤9·27=243. То же верно для любой выпуклой комбинации остальных вершин, откуда

\[
\operatorname{dist}(x_a,\operatorname{conv}\{x_b:b\ne a\})\ge\delta/243.
\]

На поляре аналогично суммируем инцидентные нормали x_a, получая расстояние до остальных полюсов ≥δ/10. Неинцидентное расстояние вершины P до опорной плоскости ≥δ/27; для P° оно ≥δ. Попарные расстояния ≥√δ. Площадь любого указанного треугольника ≥√δ/2.

Для положительной тетраэдральной клетки ориентированный определитель ≥δ, поэтому её объём ≥δ/6. В P величина D≤16: каждое из16 origin-слагаемых не превосходит произведения трёх норм ≤1. На поляре имеется14 origin-треугольников, нормы q≤27, и D°≤14·27³=275562. Поэтому нормированные положительные клеточные доли не меньше δ/16 и δ/275562 соответственно. Все делители здесь меньше2²⁰. Это доказывает одновременно все строгие оценки с объявленным **η=δ/2²⁰**.

Достаточные для продолжения общие формулы настоящих моментов сохраняются без новых неизвестных. При D_i=Σ_{τ⊂F_i}Δ_τ:

\[
\operatorname{Vol}P=D/6,\quad d_i=3D_i/D,\quad
c_i=\frac{\sum_{\tau\subset F_i}\Delta_\tau s_\tau}{3D_i},
\]
\[
\Sigma=\frac1{20D}\sum_\tau\Delta_\tau
\left(s_\tau s_\tau^T+x_ax_a^T+x_bx_b^T+x_cx_c^T\right),
\quad\Lambda_{ji}=d_i(1-q_j\cdot c_i).
\]

Знаменатели положительны количественно; это одни actual volume/facet меры одной геометрии. Согласование нескольких низких моментов произвольной Λ не заменяет эти формулы.

Есть и ограниченное механическое следствие: вдоль выбранной слабой стрелки прирост квадрата нормы ≥δ. У каждого из двух корней вся исходящая тень к другой метке ≤−δ/2. **Нетаргетные тени по-прежнему могут быть нулевыми**, поэтому отсюда не следует универсальный ненулевой зазор для всех механических тестов.

Плоские произвольные тетраэдры не удалены. Уже34>3·9 вынуждает иметь нетреугольную максимальную грань, а четыре её вершины дают нулевой аффинный четырёхвершинный определитель. Если апекс лежит в базовой грани, соответствующая клетка также нулевая. Только определённые выше положительные fan-клетки получили нижнюю границу.

## 7. Что вычислено и чего вычисления не утверждают

Новый точный исходник строит указанную систему и все геометрические цели для любого корректного входа `facets,vertex_parent,facet_parent`; корни задаются `null`. По умолчанию используются буквальные девять циклов FS и рациональные точки RAW_N/RAW_D, полностью приведённые в коде. Это контрольная решётка, не новый каталожный тип и не joint-кандидат. Ни одной метке не присвоена новая каноническая идентичность.

На этом входе восстановлены145 ограничений и744 геометрические цели. Для всех90 пар BFS-корней контрольной решётки проверены схема и коэффициентные оценки: максимальная степень4, фактический максимальный модуль коэффициента ограничения4096, максимальная ℓ¹-норма286721; для целей — модуль2 и ℓ¹-норма108. Проверка90 BFS-входов — **тест реализации генератора**, а не перебор всех деревьев или всех типов. Полнота теоремы следует из разделов3–5, которые не зависят от выбора дерева.

Тот же исходник независимо перебирает опорные тройки рационального контрольного тела, восстанавливает его девять максимальных граней и настоящую массу. Его объём19903/677600, собственный центр(0,−662559/245204960,−1515121/61301240). В евклидовой метрике строгие устойчивые грани — [1,2,3,4,7], строгие неустойчивые вершины — [0,1,2,3,4,5,7,8,9]. Четырёхнабор[0,2,5,4] точно плоский. Это сохранённый полный рациональный countercontrol против ложного «все тетраэдры положительны», не пример S=U=1 и не новый рекорд. H не подсчитывался и не заявляется.

Не запускались CAD, численная оптимизация или поиск минимума по образцам. Код действительно вычислил точный показатель степени для рационального η и построил полную целочисленную схему; аналитическая теорема о минимуме и геометрическое доказательство определяют его достоверность.

## 8. Размер числа, полная капсула и наблюдавшиеся pins

Точное число задаётся **η=1/2^N**, где

```text
N=3969803822400065051570758926865603752140426769858580.
```

Сам N —172-битное целое. Полная двоичная запись знаменателя имела бы N+1 бит, то есть3969803822400065051570758926865603752140426769858581 бит, и потребовала бы496225477800008131446344865858200469017553346232323 байта в плотной записи. Она **не материализовывалась**. Число полностью определено приведённой степенью; новый вычисленный объект — точная компактная запись рациональной границы, не огромный развёрнутый знаменатель и не неизвестный алгебраический минимум.

Сохранить весь следующий исходник как `c34_gap.py`, UTF-8/LF с конечным LF. **CPython3.13.5, только стандартная библиотека, assertions включены.** В пустом каталоге команда `python -S c34_gap.py` восстанавливает все новые точные объекты без журнала, сети, предыдущих sandbox-путей или пакетов. Дополнительная команда `python -S c34_gap.py --authenticate JOURNAL.md` проверяет конкретный приложенный журнал и три буквальных родителя; она не нужна для построения новых выходов. Пользовательская ветвь строится командой `python -S c34_gap.py branch.json` с полностью указанными циклами и двумя массивами родителей. У неё, естественно, другие pins ветви.

| Объект по умолчанию | Байтов | SHA-256 |
|---|---:|---|
|c34_gap.py|13392|e85a9b5fb2604aba2ab4b333c0a28c80bf2df3d9a16571694ce6efc452546b4f|
|c34_gap_bound.json|1100|50811e67d8b6ed040ae9cb5ee2acc0623f8514a199ff93d606468b2c25b7d438|
|c34_gap_branch.json|337837|1032271d0aad8da923cbc65440d9936900655bfe6e2c51f915846951855276f2|
|c34_gap_audit.json|3720|bbb99061e758e59c53baab98e4f7d4b56696e71a2bd0987cce88c68c4f9ac54f|

В sparse-представлении моном — отсортированный массив индексов переменных, с повторениями для степеней; строка `[коэффициент,моном]` полностью задаёт член. Все названия переменных, циклы, равенства, неравенства и744 цели восстановимы алгоритмом. Никаких опущенных коэффициентов или внешних helpers нет.

Выполнены первоначальный и отдельный холодный запуск; три JSON-выхода совпали побайтно, встроенные pins прошли. Поток90 полных BFS-контролей имеет SHA `6ebe2b26f870c87a84de924c717008a1abad147c4e6d6cd384a855aa059c536c`. Наблюдались:

```text
CURRENT_CORE_AND_THREE_LITERAL_PARENTS_AUTHENTICATED
C34_53_VARIABLE_145_CONSTRAINT_INTEGER_SCHEMA_PASS
C34_JPT_EFFECTIVE_GAP_EXPONENT 3969803822400065051570758926865603752140426769858580
C34_R1_EFFECTIVE_SATURATION_GAP_V1_RECOVERY_PASS
COLD_BYTE_PARITY_PASS
```

Это не автоматизированное доказательство опубликованной теоремы, топологической леммы раздела4 или исторических нижних границ. Их роли явно отделены от нового точного арифметического исполнения.

## 9. Точный оставшийся шаг

Качественная отделённость от геометрического вырождения теперь имеет полностью явную, хотя крайне малую, величину на **всём** нормированном слабом срезе. Не доказана пустота ни одного нового полного типа или корневого класса. Чтобы получить C≥36, остаётся исключить настоящие совместные слабые/строгие ветви внутри этой количественно невырожденной области либо отдельно разрешить возможные механические нулевые стенки. Полученный η не гарантирует остановку обычного интервального локатора: истинные нулевые нетаргетные механические ограничения сохраняются. Наиболее полезное продолжение — использовать замкнутую 53-переменную схему и доказанные геометрические нижние границы в полном совместном алгебраическом сертификате, не заменяя actual determinant массы свободными переменными.

Полная новая капсула:

```python
"""C34 R=1 effective saturation gap. CPython 3.13.5, standard library.
Run: python -S c34_gap.py [branch.json]
A branch file has facets, vertex_parent, facet_parent; roots are null.
No feasibility solver is run. The theorem uses the inherited U9/F8 exclusions.
Sparse monomials are sorted tuples of variable indices, with repetition.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import base64, hashlib, json, re, sys, zlib
assert __debug__
ID = 'C34_R1_EFFECTIVE_SATURATION_GAP_V1'
PARENTS = {
 'minimum-0054':'4e39e8c2a461dc76a76e49153b9f70ace7e0e287cb3fe5e6b3c3733a8c24d774',
 'minimum-0024':'b578a01ead261c6f7745122c22f4bb4767884e46ac46e1531b4e749a19332f95',
 'minimum-0029':'07da26de37a7076fae43373e6ecd0c85ba0b45ffbe359ed38b707c462083dd8c'}
FS = [[0,1,3],[0,2,5,4,1],[0,3,6,2],[1,4,8,9,7,3],
      [2,6,8,5],[3,7,6],[4,5,8],[6,7,9],[6,9,8]]
RAW_N = [[-1,-1,0],[-1,-2,6],[0,-1,-3],[-2,2,3],[1,-2,6],
         [1,-1,0],[0,0,-1],[-1,2,2],[2,2,3],[1,2,2]]
RAW_D = [8,22,5,14,22,8,2,10,14,10]
def js(o): return (json.dumps(o,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b): return [len(b),hashlib.sha256(b).hexdigest()]
def save(name,o):
    b=js(o);Path(name).write_bytes(b);print('PIN',name,*pin(b));return pin(b)
def c(a): return {():a} if a else {}
def add(*ps):
    r={}
    for p in ps:
        for m,a in p.items(): r[m]=r.get(m,0)+a
    return {m:a for m,a in r.items() if a}
def scale(a,p): return {m:a*b for m,b in p.items() if a*b}
def sub(p,q): return add(p,scale(-1,q))
def mul(p,q):
    r={}
    for m,a in p.items():
        for n,b in q.items():
            k=tuple(sorted(m+n));r[k]=r.get(k,0)+a*b
    return {m:a for m,a in r.items() if a}
def dot(a,b): return add(*(mul(x,y) for x,y in zip(a,b)))
def cross(a,b):
    return [sub(mul(a[(i+1)%3],b[(i+2)%3]),mul(a[(i+2)%3],b[(i+1)%3])) for i in range(3)]
def det(a,b,d): return dot(a,cross(b,d))
def diff(a,b): return [sub(x,y) for x,y in zip(a,b)]
def terms(p): return [[a,list(m)] for m,a in sorted(p.items())]
def stats(ps):
    return [max((len(m) for p in ps for m in p),default=0),
            max((abs(a) for p in ps for a in p.values()),default=0),
            max((sum(map(abs,p.values())) for p in ps),default=0)]
def topo(fs):
    assert len(fs)==9 and sum(map(len,fs))==34
    assert set().union(*map(set,fs))==set(range(10))
    owners=defaultdict(list);direct=Counter()
    for i,f in enumerate(fs):
        assert len(f)>=3 and len(f)==len(set(f))
        for a,b in zip(f,f[1:]+f[:1]):
            owners[tuple(sorted((a,b)))].append(i);direct[a,b]+=1
    assert len(owners)==17
    assert all(len(v)==2 for v in owners.values())
    assert all(direct[a,b]==direct[b,a]==1 for a,b in owners)
    for f,g in combinations(fs,2):
        h=set(f)&set(g);assert len(h)<=2
        if len(h)==2:
            a,b=sorted(h)
            assert abs(f.index(a)-f.index(b)) in (1,len(f)-1)
            assert abs(g.index(a)-g.index(b)) in (1,len(g)-1)
    tri=[(f[0],f[j],f[j+1]) for f in fs for j in range(1,len(f)-1)]
    assert len(tri)==16 and len({tuple(sorted(t)) for t in tri})==16
    te=Counter((a,b) for t in tri for a,b in zip(t,t[1:]+t[:1]))
    assert len(te)==48 and all(te[a,b]==te[b,a]==1 for a,b in te)
    for v in range(10):
        link=defaultdict(set)
        for t in tri:
            if v in t:
                a,b=[a for a in t if a!=v];link[a].add(b);link[b].add(a)
        assert all(len(w)==2 for w in link.values())
        seen={next(iter(link))};todo=list(seen)
        for a in todo:
            for b in link[a]-seen:seen.add(b);todo.append(b)
        assert len(seen)==len(link)
    pe=sorted(owners);qe=sorted(tuple(sorted(v)) for v in owners.values())
    assert len(set(qe))==17
    dual=[]
    for v in range(10):
        inc={i for i,f in enumerate(fs) if v in f};i=min(inc);g=[]
        while i not in g:
            g.append(i);f=fs[i];a=f[f.index(v)-1]
            pair=owners[tuple(sorted((a,v)))];i=next(j for j in pair if j!=i)
        assert i==g[0] and set(g)==inc;dual.append(g)
    return pe,qe,tri,dual
def tree(p,edges,n):
    assert len(p)==n and p.count(None)==1;r=p.index(None);es=set(edges)
    for a in range(n):
        if a!=r: assert p[a] in range(n) and tuple(sorted((a,p[a]))) in es
        seen=set();b=a
        while b!=r:
            assert b not in seen;seen.add(b);b=p[b]
    return r
def bfs(edges,n,r):
    p=[None]*n;seen={r};todo=[r]
    for a in todo:
        for b in sorted({v for u,v in edges if u==a}|{u for u,v in edges if v==a}):
            if b not in seen:seen.add(b);p[b]=a;todo.append(b)
    assert len(seen)==n;return p
def build(fs,pv,pq):
    pe,qe,tri,dual=topo(fs);r=tree(pv,pe,10);tree(pq,qe,9)
    b=min(set(range(10))-{r});names=[]
    def var(name):
        k=len(names);names.append(name);return {(k,):1}
    x=[[c(int(k==2)) if i==r else c(0) if (i,k)==(b,1) else var('x%d_%d'%(i,k))
        for k in range(3)] for i in range(10)]
    q=[[var('q%d_%d'%(i,k)) for k in range(3)] for i in range(9)]
    eq=[];ge=[]
    def put(dest,name,p):dest.append((name,p))
    for i,f in enumerate(fs):
        for a in range(10):put(eq if a in f else ge,'slack_%d_%d'%(i,a),sub(c(1),dot(q[i],x[a])))
    for a in range(10):
        if a!=r:put(ge,'vertex_ball_%d'%a,sub(c(1),dot(x[a],x[a])))
    for i in range(9):put(ge,'pole_ball_%d'%i,sub(c(729),dot(q[i],q[i])))
    ds=[det(*(x[a] for a in t)) for t in tri];D=add(*ds)
    for j,p in enumerate(ds):put(ge,'origin_%d'%j,p)
    put(ge,'volume_floor',sub(scale(4096,D),c(1)))
    for k in range(3):put(eq,'moment_%d'%k,add(*(mul(d,add(*(x[a][k] for a in t))) for d,t in zip(ds,tri))))
    for z,p,label in [(x,pv,'vertex'),(q,pq,'pole')]:
        for a,j in enumerate(p):
            if j is not None:put(ge,label+'_arrow_%d'%a,dot(z[a],diff(z[j],z[a])))
    assert len(names)==53 and len(eq)==37 and len(ge)==108
    assert stats([p for _,p in eq+ge])[0]<=4
    assert stats([p for _,p in eq+ge])[2] <= 393217 < 2**19
    obj=[(s,p) for s,p in ge if s.startswith('slack_')]
    for z,faces,label in [(x,fs,'primal'),(q,dual,'polar')]:
        for a,b in combinations(range(len(z)),2):
            w=diff(z[a],z[b]);obj.append((label+'_pair_%d_%d'%(a,b),dot(w,w)))
        for a,b,d in combinations(range(len(z)),3):
            w=cross(diff(z[b],z[a]),diff(z[d],z[a]))
            obj.append((label+'_area4_%d_%d_%d'%(a,b,d),dot(w,w)))
        for i,f in enumerate(faces):
            for inds in combinations(range(len(f)),3):
                a,b,d=[f[j] for j in inds]
                tag=label+'_%d_%d_%d_%d'%(i,a,b,d)
                obj.append((tag+'_origin',det(z[a],z[b],z[d])))
                for k in set(range(len(z)))-set(f):
                    obj.append((tag+'_apex_%d'%k,det(diff(z[a],z[k]),diff(z[b],z[k]),diff(z[d],z[k]))))
    assert stats([p for _,p in obj])[0]<=4 and stats([p for _,p in obj])[2]<=192
    out={'identity':ID,'variables':names,'facets':fs,'dual_facets':dual,
         'vertex_parent':pv,'facet_parent':pq,'true_edges':pe,'dual_edges':qe,
         'equations':[[s,terms(p)] for s,p in eq],
         'nonnegative':[[s,terms(p)] for s,p in ge],
         'positive_objectives':[[s,terms(p)] for s,p in obj]}
    return out,stats([p for _,p in eq+ge]),stats([p for _,p in obj])
def ndot(a,b):return sum(x*y for x,y in zip(a,b))
def nsub(a,b):return [x-y for x,y in zip(a,b)]
def ncross(a,b):return [a[(k+1)%3]*b[(k+2)%3]-a[(k+2)%3]*b[(k+1)%3] for k in range(3)]
def ndet(a,b,c):return ndot(a,ncross(b,c))
def fixture():
    pe,qe,tri,dual=topo(FS)
    x=[[F(a,d) for a in row] for row,d in zip(RAW_N,RAW_D)]
    found=set()
    for a,b,d in combinations(range(10),3):
        n=ncross(nsub(x[b],x[a]),nsub(x[d],x[a]))
        if n==[0,0,0]:continue
        h=ndot(n,x[a]);sg=[h-ndot(n,y) for y in x]
        if all(t>=0 for t in sg) or all(t<=0 for t in sg):
            found.add(frozenset(i for i,t in enumerate(sg) if t==0))
    assert found==set(map(frozenset,FS))
    rawq=[]
    for f in FS:
        a,b,d=[x[j] for j in f[:3]];n=ncross(nsub(b,a),nsub(d,a));h=ndot(n,a)
        assert h>0;rawq.append([t/h for t in n])
    ds=[ndet(*(x[j] for j in t)) for t in tri];assert min(ds)>0
    D=sum(ds);cen=[sum(w*sum(x[j][k] for j in t) for w,t in zip(ds,tri))/(4*D) for k in range(3)]
    x=[nsub(y,cen) for y in x];q=[[u/(1-ndot(z,cen)) for u in z] for z in rawq]
    assert D/6==F(19903,677600)
    assert cen==[0,-F(662559,245204960),-F(1515121,61301240)]
    assert all(ndet(*(q[j] for j in f[:3]))>0 for f in dual)
    U=[i for i in range(10) if all(ndot(x[i],nsub(x[j],x[i]))<0 for j in range(10) if j!=i)]
    S=[i for i in range(9) if all(ndot(q[i],nsub(q[j],q[i]))<0 for j in range(9) if j!=i)]
    assert len(U)>1 and len(S)>1
    # A mandated coplanar four-set is not a positive apex cell.
    assert ndet(nsub(x[2],x[0]),nsub(x[5],x[0]),nsub(x[4],x[0]))==0
    return {'volume':str(D/6),'centroid':[str(t) for t in cen],
            'strict_U':U,'strict_S':S,'joint_candidate':False,'flat_four_set':[0,2,5,4]}
def constants():
    n,m,d,H=53,145,4,2**19
    assert max(H,2*n+2*m)==H and 2*n+2*m==396
    log_base=F(4)-F(n,2)+19+2*n
    exponent=n*2**n*d**n
    E=log_base*exponent;assert E.denominator==1;E=int(E)
    assert log_base==F(205,2) and E==10865*2**158
    T=E+20
    assert 4096*8>27**3 and 4096*16*6+1< H
    assert max(243,10,27,54,6,16,14*27**3)<2**20
    assert T <2**172
    return {'identity':ID,'parents':PARENTS,'n':n,'m':m,'equalities':37,
        'inequalities':108,'d':d,'H':H,'H_tilde':H,'log2_base':str(log_base),
        'outer_exponent':exponent,'E':E,'eta':{'numerator':1,'denominator_base':2,'denominator_exponent':T},
        'dense_denominator_bits':T+1,'dense_denominator_bytes':(T+8)//8,
        'minimum_algebraic_degree_bound':2**158,'global_frontier':[632,52585],
        'new_whole_exclusions':0,'new_root_exclusions':0,
        'numerical_optimization_performed':False,'full_denominator_materialized':False}
def authenticate(path):
    raw=Path(path).read_bytes()
    assert pin(raw)==[4738679,'969add9dd8313881d93a08e127358159b5fcc3b1ceb177983f3ed0307ec64cdc']
    text=raw.decode()
    hs=list(re.finditer(r'^## Parent (asg_\S+)\n\nSHA-256: `([a-f0-9]{64})`\n\n',text,re.M))
    assert {m[1] for m in hs}==set(PARENTS)
    for j,h in enumerate(hs):
        md=text[h.end():hs[j+1].start() if j+1<len(hs) else len(text)].rstrip()+'\n'
        kw={'indent':2} if h[1]=='minimum-0024' else {'separators':(',',':')}
        b=json.dumps({'version':2,'result_markdown':md},ensure_ascii=False,**kw).encode()
        assert hashlib.sha256(b).hexdigest()==h[2]==PARENTS[h[1]]
        print('PARENT_AUTHENTICATED',h[1],*pin(b))
    start=text.index('## Recovery capsule part 1/1 — C34_ACTUAL_CORE_METRIC_FLOOR_AND_SATURATION_COMPACTNESS_V1')
    start=text.index('```python\n',start)+len('```python\n')
    end=text.index('\n```',start);src=(text[start:end]+'\n').encode()
    assert pin(src)==[15270,'87beb4ee75274e73417a803f61eab5dc9f3c53eecdba7902aeb6572eabbd9872']
    enc=re.search(r'B85 = r"""(.*?)"""',src.decode(),re.S)[1]
    pack=zlib.decompress(base64.b85decode(''.join(enc.split())))
    assert pin(pack)==[28562,'550c836842d7de09904d1add00e1980b656875aa4c12d632824954d64bd30966']
    o=json.loads(pack)
    assert pin(o['MINIMUM_C34_core_metric_compactness.md'].encode())==[24271,'137f5e255e2da1b528fe91814f36cea7b07a5991def2142b885a1321c578e12a']
    assert pin(o['core_metric_floor.py'].encode())==[3966,'c48689a08505f5d7ac49e28234451f164062a466d491adc9219989c8a8c93ea6']
    print('CURRENT_CORE_AND_THREE_LITERAL_PARENTS_AUTHENTICATED')
def main():
    if len(sys.argv)==3 and sys.argv[1]=='--authenticate':
        authenticate(sys.argv[2]);return
    assert len(sys.argv)<=2
    report=constants();save('c34_gap_bound.json',report)
    pe,qe,_,_=topo(FS)
    default={'facets':FS,'vertex_parent':bfs(pe,10,0),'facet_parent':bfs(qe,9,0)}
    spec=json.loads(Path(sys.argv[1]).read_text()) if len(sys.argv)>1 else default
    out,st,ot=build(spec['facets'],spec['vertex_parent'],spec['facet_parent'])
    save('c34_gap_branch.json',out)
    stream=hashlib.sha256();rows=[]
    for r in range(10):
        for s in range(9):
            z,ss,oo=build(FS,bfs(pe,10,r),bfs(qe,9,s));stream.update(js(z))
            rows.append([r,s,ss,oo,len(z['positive_objectives'])])
    audit={'identity':ID,'arithmetic_fixture_only':True,'ninety_BFS_controls':rows,
           'stream_sha256':stream.hexdigest(),'actual_nonwinning_fixture':fixture(),
           'branch_constraint_stats':st,'branch_objective_stats':ot}
    save('c34_gap_audit.json',audit)
    print('C34_53_VARIABLE_145_CONSTRAINT_INTEGER_SCHEMA_PASS')
    print('C34_JPT_EFFECTIVE_GAP_EXPONENT',report['eta']['denominator_exponent'])
    if len(sys.argv)==1:
        pins={'c34_gap_bound.json':[1100,'50811e67d8b6ed040ae9cb5ee2acc0623f8514a199ff93d606468b2c25b7d438'],
              'c34_gap_branch.json':[337837,'1032271d0aad8da923cbc65440d9936900655bfe6e2c51f915846951855276f2'],
              'c34_gap_audit.json':[3720,'bbb99061e758e59c53baab98e4f7d4b56696e71a2bd0987cce88c68c4f9ac54f']}
        for name,p in pins.items():assert pin(Path(name).read_bytes())==p
    print('C34_R1_EFFECTIVE_SATURATION_GAP_V1_RECOVERY_PASS')
if __name__=='__main__':main()
```

Дополнительная копия исходника, полного текста, трёх восстановленных JSON и протокола: C34_R1_EFFECTIVE_SATURATION_GAP_V1.zip. Все первичные новые данные восстанавливаются приведённым выше буквальным кодом.
