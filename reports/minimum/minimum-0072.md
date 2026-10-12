# minimum-0072

AI research report · 2026-09-16 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# SIMPLELEAF894_UNBOUNDED_TILT_AND_COMMON_BODY_BARRIER_V1

## Итог

**Доказано новое полное непрерывное исключение, не требующее семиугольной грани:** во всех 894 буквальных simple-leaf5 областях TREE410 невозможно, чтобы одновременно

\[
\min_{i\in\{1,2,3,6,7,8\}}(v_i)_1\ge\frac{99}{100}
\quad\text{и}\quad A_{43},A_{54},A_{98}\ge0.
\tag{T}
\]

Координаты — фиксированные аффинные координаты настоящего угла \(v_5=0,v_0=e_1,v_4=e_2,v_9=e_3\). Теорема действует для **всех** SPD-метрик M и всех форм остальных настоящих граней. Получен строгий запас

\[
\boxed{\min(A_{43},A_{54},A_{98})<-\operatorname{tr}(M)/16000.}
\tag{T1}
\]

Для настоящего семиугольника на вершинах \(0,1,2,3,6,7,8\), плоскость которого имеет вид

\[
x_1+u x_2+v x_3=1,
\]

отсюда исключён **весь неограниченный по отрицательным наклонам класс**

\[
\boxed{u\le 2/177,\qquad v\le 2/177.}
\tag{T2}
\]

В частности, закрыты все \(u,v\le0\), включая произвольно большие отрицательные наклоны и их нулевые границы. Это не повтор параллельного случая \(u=v=0\) и не локальная проверка около него. Более общий критерий(T) охватывает и неплоскую совокупность шести остальных вершин.

Одновременно найден **точный физический барьер для распространения одного трёхстрелочного механизма на весь наклонный класс**: настоящий рациональный многогранник того же буквального индекса **13749**, с D<15/8, собственными центрами P и Q, настоящими площадями и ковариациями и одной взаимно обратной парой M,N, имеет все три \(A_{43},A_{54},A_{98}>1/500\). Он проходит также унаследованный метрический нижний LMI. Поэтому одних этих трёх стрелок и универсальных геометрических ограничений недостаточно. Полное дерево он **не** реализует: остальные шесть выбранных стрелок отрицательны, а P и Q имеют по три строгие неустойчивые вершины.

**Новых целиком исключённых parent-indices: `[]`.** Весь прежний894-набор остаётся, но каждый индекс получает строгую необходимую дизъюнкцию \(\exists i\in\{1,2,3,6,7,8\}:(v_i)_1<99/100\). Полный буквальный массив894 включён в восстанавливаемый исходник, без перенумерации. Границы V≥10,F≥9,C≥34 и раздельные регистры632/52585 и TREE41024847/14128/10719 не изменены. Это именно прежний статус, а не новая глобальная теорема.

## 1. Источники и проверенная исходная область

Прочитаны актуальная сводка, относящиеся к задаче записи и буквальные материалы родителей:

- `minimum-0070`, объявленный SHA-256 `942eb62a7f656dd01624702c509f6c3b56944e8fb7d6f73047669037727e4b8d`;
- `minimum-0054`, объявленный SHA-256 `4e39e8c2a461dc76a76e49153b9f70ace7e0e287cb3fe5e6b3c3733a8c24d774`.

Текущий файл `research-journal(20260916-154308).md`: **4868784 bytes**, SHA-256 `dd952c7dd0faa4fa22284d6de9124f18bad425766262492aeca4e3bda43a85a2`. SHA сериализованных immutable-payload сохраняются как их объявленные идентичности; они не подменяются хешем извлечённого Markdown. Математического конфликта массивов или инцидентностей не обнаружено.

Запись `SIMPLELEAF894_PARALLEL_HEPTAGON_ALL_D_45_PD_V1` прочитана вместе с полным3950-byte исходником. Его SHA `bac2c6d8c82209d6f2f06d73a2526491534682a4e34edf767ac5b731e4a8f130` подтверждён, и повторный запуск воспроизвёл12059-byte результат с SHA `9b643d731883ec0560b15589570f177aba61c569103b55e134b8b81a694b1f00`. Уже закрытый параллельный подкласс не объявляется новым результатом.

Для буквальной привязки индексов исполнен selector первого родителя на ранее приложенном журнале с полным TREE410-successor. Проверены его исходник55542 bytes/SHA `4a5a219d7eeba66492b882555a0e939fb1627302061bbbd44d7ec10e6db070cd`, decoded source213968/SHA `435c7a2ea5de8a39d7b876a5bfc15208cf1b1491333578c1935c16d63df98233` и regenerated catalogue6510775/SHA `8eff923828decf1613e91309baf4f4f7afd240d4dfd7adc5a64354c63bbebe04`. Selector дал1901 исходных simple049,996 промежуточных,102 уже закрытых cap-случая и894 остатка. Его результат10678 bytes имеет SHA `867430f16c9eb78da703a05967b6a610d7a7013dafafc1971c05c887f93d872f`. Единственный в этом894-массиве индекс с указанным семиугольником — **13749**. Это привязка к старому упорядоченному TREE410-каталогу, не к глобальному632-каталогу.

Сохраняются буквально

```text
p=(0,0,1,2,3,4,0,6,7,8), root=0,
N5=(0,4,9), genuine facet459, (V,E,F)=(10,17,9).
```

Новый основной запрет(T) не использует универсальную девятивершинную теорему. Она остаётся наследуемой посылкой только при формулировке необходимой потери стрелки на настоящем Q ниже. Её universal285 и V≤8 зависимости здесь не объявляются заново холодно проверенными.

## 2. Общая геометрия, площади и точный транспорт центра

Пусть P — одно настоящее равномерно объёмно заполненное выпуклое тело рассматриваемой области. В сырых угловых координатах

\[
K=\operatorname{conv}(0,e_1,e_2,e_3),\quad
D=6\operatorname{Vol}P\in(1,15/8),\quad P\subset\mathbb R_+^3.
\]

Для \(U=\{1,2,3,6,7,8\}\) сохраняются \((v_i)_1>0\), остальные координаты неотрицательны и \(1<\mathbf1^Tv_i<D\). Настоящее удаление простой вершины5 даёт

\[
Q=\operatorname{conv}\{v_i:i\ne5\}=P\cap\{\mathbf1^Tx\ge1\},\qquad P=K\cup Q.
\]

Пересечение внутренних областей пусто. Новая настоящая грань Q — треугольник049. Обозначим настоящие сырые центры c=E_PX и q=E_QX, k=\(\mathbf1/4\). Тогда

\[
q=\frac{Dc-k}{D-1},\qquad
\tau=4(q-c),\qquad
c=\frac{\mathbf1+(D-1)\tau}{4},\quad
q=\frac{\mathbf1+D\tau}{4}.
\tag{1}
\]

Ни c,q,τ, ни фановые массы не выбираются независимо. Исходная нормальная область и эти связи сохранены в актуальной записи.

Краткое восстановление физических неравенств: веер P из e_j даёт c_j≥1/4. Равенство заставило бы все остальные вершины лежать в x_j=0, то есть P было бы пирамидой; V10,F9 это исключает. Для настоящей грани доля конуса от собственного центра не превосходит1/4, причём равенство означает пирамиду с этой базой. Это стандартная singleton-теорема Freyer–Henk–Kipp, а не новый приоритет данного результата. Применив её к049 в Q, получаем

\[
1<\mathbf1^Tq<(D+3)/4,
\qquad \tau_j>0,\quad 1/D<\mathbf1^T\tau<1.
\tag{2}
\]

Для настоящих угловых площадей \(\delta_j=2\operatorname{Area}(P\cap\{x_j=0\})\)

\[
\delta_1=1,\quad1\le\delta_j<D,\quad
4\delta_jc_j<D,\quad
0<\tau_j<\frac{D-\delta_j}{\delta_j(D-1)}.
\tag{3}
\]

Всюду M≻0, N=M⁻¹ — одна механическая пара. С \(e_i=v_{p_i}-v_i\)

\[
A_i^P=(v_i-c)^TMe_i,\qquad
\boxed{A_i^Q=A_i^P-\tau^TMe_i/4.}
\tag{4}
\]

Каждое старое ребро без5 остаётся настоящим ребром Q: его исходный строго экспонирующий функционал по-прежнему экспонирует ровно те же два конца. Знак новой механической стрелки из этого не следует.

## 3. Новая общая фанова связь

Положим \(a=\min_{i\in U}(v_i)_1\). Тогда для всех894 областей

\[
\boxed{D\tau_1\ge a.}
\tag{5}
\]

Доказательство не требует плоскости верхних вершин. Возьмём настоящий веер Q из e_1. Для каждой его тетраэдральной клетки T пусть d_T — настоящий неотрицательный шестикратный объём, s_T — сумма четырёх сырых вершин. Общие объёмные и первые моменты дают

\[
\sum_Td_T=D-1,\qquad
4Dc=\mathbf1+\sum_Td_Ts_T,
\]

\[
\boxed{D\tau=\frac1{D-1}\sum_Td_T(s_T-\mathbf1).}
\tag{6}
\]

В каждой положительной клетке есть e_1 и хотя бы одна вершина из U: кроме них в Q имеются только e_2,e_3. Поэтому \((s_T)_1-1\ge a\). Положительное объёмное усреднение доказывает(5). Плоские клетки имеют именно свой нулевой объём; их удаление не назначает нулевые массы другим четырёхнаборам.

Это новая физическая связь: первая координата того же τ, который переносит все восемь стрелок, контролируется расположением **всех** шести настоящих вершин через один фактический веер Q.

### Дополнительная связь для всего наклонного семиугольника

Пусть \(\ell=(1,u,v)\) задаёт настоящую грань на \(\{0\}\cup U\). Тогда u,v<1, поскольку e_2,e_3 лежат строго под ней. В положительном Q-веере из e_1 возможны только типы

```text
{e1,e2,e3,h};  {e1,e2,h,h'};  {e1,e3,h,h'},   h,h' in U.
```

Четыре верхние вершины копланарны и дают нулевой объём. Значения \(\ell^T(s_T-\mathbf1)\) у трёх типов равны соответственно1,2−v,2−u. Существование настоящего верхнего ребра, не содержащего e_1, гарантирует положительную клетку одного из последних двух типов. Поэтому

\[
\boxed{D(\tau_1+u\tau_2+v\tau_3)>1.}
\tag{7}
\]

Для буквального13749 положим b_1=\((v_1)_2>0\), c_6=\((v_6)_3>0\). Две настоящие четырёхугольные угловые грани дают точные равенства

\[
\delta_3=1+(1-u)b_1,\qquad \delta_2=1+(1-v)c_6.
\tag{8}
\]

Подстановка в(7) вместе с \(\sum\tau<1\) даёт полностью физическое полиномиальное необходимое условие

\[
\boxed{D[(\delta_3-1)c_6\tau_2+(\delta_2-1)b_1\tau_3]
 <(D-1)b_1c_6.}
\tag{9}
\]

Это дополнительный общий area/centroid-фильтр на оставшемся наклоне; сам по себе он не исключает весь13749. Все четыре восстановленные физические пары P,Q проходят(7)–(9).

## 4. Полное доказательство(T):180 точных матриц

Пусть a≥m=99/100. Из(5), D≤15/8 получаем τ_1≥g=66/125. Вместе с(2) это помещает c в выпуклую оболочку следующих **пяти** точек:

\[
\begin{split}
C=\{&(1/4,1/4,1/4),\ (731/2000,1/4,1/4),\ (15/32,1/4,1/4),\\
 &(731/2000,1413/4000,1/4),\ (731/2000,1/4,1413/4000)\}.
\end{split}
\tag{10}
\]

Действительно, τ принадлежит тетраэдру с вершинами \(g e_1,e_1,g e_1+(1-g)e_2,g e_1+(1-g)e_3\), а \(c=k+(D-1)\tau/4\), \(0<D-1<7/8\).

Обе p=v_3 и r=v_8 принадлежат многограннику \(x_1\ge m,x_2,x_3\ge0,1\le\sum x_j\le15/8\). Его **полный** список вершин:

\[
\begin{split}
E=\{&(1,0,0),(15/8,0,0),\ (99/100,1/100,0),\ (99/100,0,1/100),\\
 &(99/100,177/200,0),(99/100,0,177/200)\}.
\end{split}
\tag{11}
\]

Полнота списка следует пересечением боковых координатных граней со стенками \(x_1=m\), \(\sum x=1\), \(\sum x=15/8\). Это замкнутое внешнее покрытие, а не выборка возможных тел.

С \(\operatorname{sym}(x,y)=(xy^T+yx^T)/2\) определим

\[
B(c,p,r)=-441\operatorname{sym}(e_2-c,p-e_2)
+310\operatorname{sym}(c,e_2)
-249\operatorname{sym}(e_3-c,r-e_3).
\tag{12}
\]

Восстановитель точно доказывает \(B-I/16\succ0\) на всех5·6·6=180 вершинах C×E×E. Проверены все540 ведущих миноров двумя независимыми арифметическими алгоритмами: формулой Лейбница для определителя и рациональным LDLᵀ с обратной сборкой матрицы. Дополнительная проверка шести квадратичных тестов восстанавливает каждый B непосредственно из трёх скалярных стрелок. Минимумы ведущих миноров по180 матрицам в точности равны

```text
13657/80
4921953619/512000
66355635548832433/40960000000000
```

B отдельно аффинна по c,p,r. Следовательно на **всём замкнутом** произведении выпуклых оболочек она является выпуклой комбинацией этих180 матриц, и

\[
B(c,v_3,v_8)\succ I/16.
\]

Для одной фактической SPD-матрицы M

\[
441A_{43}+310A_{54}+249A_{98}
=-\operatorname{tr}(MB)<-\operatorname{tr}(M)/16.
\tag{13}
\]

Сумма весов равна1000. Поэтому хотя бы одна из трёх стрелок меньше \(-\operatorname{tr}(M)/16000\), что доказывает(T),(T1).

**Полнота области.** Проверка не разделяет тело на независимо выбираемые occurrence-строки: исходный c выведен из одного настоящего веера Q и того же P. После этого применяется внешнее произведение многогранников, которое только увеличивает необходимую область. Его точная несовместимость с тремя стрелками доказывает физический запрет. Все слабые механические стенки, нестрогая граница99/100, внешняя стенкаD=15/8, нулевые координаты и границы симплекса центров включены в конечное доказательство. Требование положительного нижнего собственного числа M не используется: матричное противоречие действует даже для любого ненулевого PSD M в замыкании, без объявления такого предела физическим телом.

Никаких предположений о простоте остальных вершин или положительности каждой выбранной фановой клетки нет. Если при геометрическом пределе меняется настоящая инцидентность, утверждение применяется к той сохранившейся физической области, где указанные гипотезы и настоящие рёбра остаются верны. Триангуляционные диагонали нигде не становятся обязательными механическими рёбрами.

## 5. Полный неограниченный наклонный подкласс

Пусть все семь верхних вершин лежат на \(x_1+u x_2+v x_3=1\), и u,v≤η=2/177. Для каждой такой вершины с S=\(x_1+x_2+x_3<15/8\)

\[
x_1=1-u x_2-v x_3\ge1-\eta(x_2+x_3),
\]

\[
x_1>\frac{1-(15/8)\eta}{1-\eta}=99/100.
\]

Теорема(T) доказывает(T2) целиком. Никакого ограничения снизу на u,v нет. В настоящих площадях(8) тот же полный подкласс задаётся

\[
\delta_3-1\ge(175/177)b_1,\qquad
\delta_2-1\ge(175/177)c_6.
\tag{14}
\]

Граница обеих нестрогих отсечек включена. Более того, критерий(T) может закрыть отдельную геометрию и при max(u,v)>2/177, если отрицательный второй наклон либо форма H всё равно удерживает все шесть x_1≥99/100. Поэтому остаток задаётся прежде всего отрицанием(T), а не только наклонным прямоугольником.

### Настоящее семейство с произвольно большими отрицательными наклонами

Возьмём исходный параллельный многогранник P₀: v₅=0,v₄=e₂,v₉=e₃, а меткам(0,1,2,3,8,7,6) присвоим

\[
(1,\varepsilon y/8,\varepsilon z/8),
\]

где полный список(y,z) —

```text
(0,0),(4,0),(6,1),(6,2),(2,6),(1,6),(0,4).
```

Его девять настоящих граней перечислены ниже для13749. Для \(0<\varepsilon\le1/16\), любых u,v≤0 положим t₂=1/(1−u),t₃=1/(1−v) и применим к вершинам

\[
\Phi(x,y,z)=\frac{(x,t_2y,t_3z)}{1+(t_2-1)y+(t_3-1)z}.
\tag{15}
\]

Знаменатель положителен на всём P₀: на трёх базовых вершинах он равен1,t₂,t₃, а на верхней грани не меньше1−ε. Поэтому это настоящая projective image с той же полной инцидентностью; четыре угловые вершины сохраняются. Она используется **только для задания геометрии**, не для переноса равномерной плотности или старого центра.

На верхних вершинах новый x₁≥1 и новая сумма координат не больше1/(1−ε). Образ содержит K и строго больше K. Следовательно

\[
1<D\le(16/15)^3<15/8.
\]

Это полное семейство настоящих V10/E17/F9 тел при неограниченных отрицательных наклонах, целиком исключённое для буквального дерева при любой M≻0. В точной проверке восстановлены случаи \((\varepsilon,u,v)=(1/16,-1,-2),(1/16,-10,-100)\). Третий контроль \((1/2,1/100,1/100)\) лежит в новом положительном наклонном секторе и также точно проверен. Существование этих тел не означает существования заданной мононеустойчивой механики.

## 6. Точный барьер для трёхстрелочного продолжения

Полный рациональный контроль вне нового сектора имеет в порядке0,…,9 вершины

```text
(1,0,0)
(1/9,10/9,0)
(1/15,1,1/6)
(1/17,15/17,5/17)
(0,1,0)
(0,0,0)
(1/9,0,10/9)
(1/15,1/6,1)
(1/17,5/17,15/17)
(0,0,1)
```

Его настоящие максимальные грани — буквально грани13749:

```text
(0,1,2,3,8,7,6),(0,1,4,5),(0,5,9,6),
(1,2,4),(2,3,4),(3,4,9,8),(4,5,9),(6,7,9),(7,8,9).
```

Именно семиугольная грань имеет \(u=v=4/5\). Тело также получается по(15) из ε=4, но все моменты образа интегрированы заново по его настоящему равномерному объёму.

Возьмём

\[
M=\frac1{400}\begin{pmatrix}300&-120&-120\\-120&50&49\\-120&49&50\end{pmatrix},
\quad
N=\begin{pmatrix}44&160/3&160/3\\160/3&800/3&-400/3\\160/3&-400/3&800/3\end{pmatrix}.
\]

Точно проверены M≻0, MN=I, trM=1 и

\[
M\succ\frac{64}{921375}(4-\mathbf1^TM\mathbf1)(I+\mathbf1\mathbf1^T).
\]

Действительные интегралы дают

\[
D=11756/7803,
\]

\[
c_P=(1161979/4496670,\ 8717399/28778688,\ 8717399/28778688),
\]

\[
c_Q=(3326537/12096180,\ 3941963/9676944,\ 3941963/9676944),
\]

\[
\delta=(1,11/9,11/9),
\quad
\tau=(3856773/58089335,\ 77659077/185885872,\ 77659077/185885872).
\]

Все(1)–(3),(5),(7)–(9) выполнены с указанными строгими знаками. Но

\[
\boxed{A_{43}=A_{98}=4371081/1279052800>1/500,}
\]

\[
\boxed{A_{54}=9792457/3837158400>1/500.}
\]

Таким образом универсальный запрет всего наклонного класса из только трёх стрелок **математически ложен**, даже если вернуть настоящие площади, центры, ковариации и edge measures. Это барьер не только для постоянных весов(18,13,10) или(441,310,249): сами три неравенства физически совместимы.

**Что контроль не доказывает.** Остальные шесть стрелок буквального дерева здесь отрицательны. Нормовые порядки на четырёх внутренних звеньях также не проходят. P и Q имеют ровно три строгие неустойчивые вершины `[0,3,8]`; root0 действительно глобально самый удалённый. Поэтому это не realization полного необходимого TREE410-системы, не S1/U1-свидетель и не барьер для метода, использующего остальные стрелки или дополнительные tree-dependent теоремы.

После удаления5 настоящие грани Q равны

```text
(0,1,2,3,8,7,6),(0,1,4),(0,9,6),(1,2,4),(2,3,4),
(3,4,9,8),(6,7,9),(7,8,9),(0,4,9).
```

Получены counts(9,16,9); каждый из восьми сохранившихся старых tree-edges проверен как настоящее ребро, а его новый зазор проверен именно по(4).

## 7. Что именно проверяет восстановитель

Все новые вычислительные утверждения имеют один полностью воспроизводимый источник. В нём нет численного оптимизатора, случайного входа, независимых fitted-masses или скрытого файла. Зафиксированные рациональные входы и точный verifier достаточны для воспроизведения результатов, независимо от способа нахождения коэффициентов.

Проверены180 PD-матриц/540 ведущих миноров. Для четырёх пар настоящих P,Q код независимо восстанавливает все поддерживающие плоскости перебором троек, сверяет полные максимальные грани, строгую выпуклость циклов, все настоящие рёбра и Euler counts. Объём, центр и ковариация каждого тела совпадают в трёх разных настоящих веерах.

Для каждого P и каждого Q заново вычислены собственные центрированные poles, d, полный Λ, H и все K_i из настоящих area measures. Проверены \(\Lambda Q_{poles}=-Q_{poles}\), \(\Lambda^2+\Lambda=4\mathbf1d^T\), \(d_i=(\Lambda^2)_{ii}/4\), \(\sum K_i=5H-2\mathbf1\mathbf1^T\), \(K_i(d/3)=\Lambda[:,i]\). Под Q_{poles} здесь понимается матрица полюсов соответствующего тела, не удалённое тело Q.

Настоящие линейные и квадратичные edge moments определяются общими концами каждого ребра, а не отдельно в двух гранях. Через них проверено **2160** скалярных компонент facet-divergence identities для мономов степеней0,1,2. Подтверждены все32 транспорта сохранившихся tree-arrows между четырьмя парами P/Q. Полная mechanical face/saddle census не заявляется; контроль не предназначен для демонстрации S1/U1.

## 8. Полный остаток и полезное продолжение

Новый whole-excluded array пуст. Все894 буквальных индекса сохранены в переменной `INDICES` полного исходника; поле `whole_remaining_parent_indices` вывода повторяет тот же массив. Наклонный геометрический подкласс(T2) относится к13749, но **не** закрывает его целиком. На прочие893 индекса наличие именно этого семиугольника не переносится.

Для каждого физического survivor теперь необходимо \(\min_{i\in U}(v_i)_1<99/100\), при сохранении точной общей связи(5). Для13749 дополнительно остаются(7)–(9), и хотя бы один из u,v должен превосходить2/177. Все прежние метрические, площадные и механические ограничения сохраняются.

Если предположить, что исходное полное дерево P действительно проходит, девятивершинная посылка требует

\[
\exists i\in\{1,2,3,4,6,7,8,9\}:\quad
\tau^TMe_i>4A_i^P\ge0.
\]

Это относится к собственному центру Q по(4). Ни одно такое строгое нарушение не устранено автоматически новой теоремой; все восемь транспортных ветвей вне закрытого сектора остаются.

Самое полезное изменение направления: для полного наклонного13749 необходимо удерживать шесть стрелок внутри настоящего семиугольника совместно с его площадными моментами и(7)–(9). Перенастройка только трёх входящих стрелок не закроет весь класс — это уже исключено точным физическим контролем. Для остальных893 областей пригодна та же фанова формула(6), но нельзя подставлять несуществующую семиугольную грань. Неудачные численные поиски нигде не используются как невозможность.

## 9. Самодостаточный recovery capsule

Сохранить весь следующий блок как `recover_vivid_tilt.py` (UTF-8/LF, один завершающий LF). Reference environment: **CPython3.13.5**, standard library, assertions enabled. Единственный необязательный аргумент — выходная директория. Числовые параметры, все894 индекса, оба точных алгоритма проверки, полные генераторы всех P/Q и их действительные поля находятся внутри архива; никакой parent sandbox или загрузка не нужны.

```text
python -S recover_vivid_tilt.py run1
python -S recover_vivid_tilt.py run2
cmp run1/tilt_exact.json run2/tilt_exact.json
cmp run1/tilt_exact.log run2/tilt_exact.log
```

Два чистых запуска полного исходника совпали побайтно; отдельно исполнен старт из одного восстановителя в новой директории, и все его pins прошли. Выходное сообщение `TWO_CLEAN_EXACT_REPLAYS_MATCH` наблюдалось после сравнений. Дополнительный заключительный запуск восстановителя снова дал те же output/log SHA. Никакой ещё не исполненный кандидат не повышен до принятого результата.

|Объект|Байты|SHA-256|
|---|---:|---|
|`recover_vivid_tilt.py`|9257|`5eb4b4caf80e19f66b487d394d0d6e0eccee91cc36c11fadd002bcc4a2a44caf`|
|Полный `tilt_exact.py`|17719|`ae79ee3cf0e5ace7731985d12663a68b699a876eacf19efbbd12636cf9cff70f`|
|Встроенный XZ, preset9|6124|`84105e5146e126f9a69092e542e20395ba20e6dae35bfc560b6babe698ce2abd`|
|`tilt_exact.json`|647477|`d77b2c45c514c202d77562a4305daa17d7a42ae4b870a12d993fea888e48cc87`|
|`tilt_exact.log`|775|`1164c0e5efc1850bff1e70ef4f42ceb7b230cdf2fc7536dc50bd4424fe91b34a`|

Наблюдаемые решающие маркеры:


[Encoded source block omitted; the code in this passage is incomplete.]


Готовые дополнительные копии: полный читаемый исходник (`tilt_exact.py`), recovery (`recover_vivid_tilt.py`), точный результат (`tilt_exact.json`). Они не являются единственным источником данных: весь необходимый источник восстанавливается из следующего полного блока.

```python
"""Complete Vivid Raven tilted-simple-leaf recovery; CPython 3.13.5, stdlib.
Run: python -S recover_vivid_tilt.py NEW_DIRECTORY
All 894 literal indices, all 180 certificates, and all exact P/Q controls are embedded.
"""
from pathlib import Path
import base64, hashlib, lzma, subprocess, sys
assert __debug__ and sys.version_info[:3] == (3,13,5)
def pin(b): return [len(b),hashlib.sha256(b).hexdigest()]
DATA = r'''
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;6*kUs$BpPXbn#W6DFf$V&nO+xl%J~oKStAPk^|xAY8|D@4WCx(U~U`BzxbE#Hb$fwD>lQ
$~J($!$pF08=d}Il~i8wRvq}DApT(!VQ<u!X`-zTBnjg%qMt|uA?tKyxJbt;fV1JEd-GXoxE=EA_ddD_@;Ayo32S%71))E6EF+f$
=Td-
9+C>1@Lg_z7ycVCx7{5i>8xEaHZ)w9hJ(rvh48U2f;?W3U0)ccFuu0q@Nff#Yq~v}DasuEgHd==v{uW#f{ZA|3*l=k<g!m$jt%W;
VTSVTml2e^MsZ`k@j&L852=~d*c%aKv9%*$NN%NfxgVJBoYNa9-
c>QTlfqSDcD03NziJSinH545b*l&7Gamu;pGexa4R8lsy>S?%(Gf<tHOfL4z<*RiDGYRo$T82{yr!eY|S{>fdv^91hdRKHX71ZQ!
A@7{VK$D$RIm<WuTUE1Fzo7-
qwa?nfen*II@T*JX>X&)V?dNx+|Iwje2!Xcc$(&Q`8W+wvUll@V6v2I6z;s2``7T=RWDmciXcgear%`)o%pMHMvuu!~VPeYxqvDu
-B*Elmk7QTojkE0r5-P};{E%7?Jtax-i}Cv=>!1A<U=f3wxE?$cNVi+N=f;(zGi`eQ<e6mL!$-jG-mTKk)`+4)JHMxJjjm-
N#W9jS)X1yR;qk`sNVMQN`IH|0Vh65&<m)i#iNG@zMJU8XBCu?6L_b9(u9-
MZn+A(PbQO$&lgbIS7<qu5A@RpuG*}g255&{s6M{7b+_eL&3BXRNXAP+Oma`zrsk3Ctlu&s%?4%pc@=bh0y<aazf#F4PNbhV@QCu
De5KU8I>~ROGwVvO$tp$kmA7dIEWAN8Gr|h4L+Ql71cB$&)|1;+So2SVH;$0IC{;qW^FUKfE({S@k0;+WZsU@d`*>s&l7@72WPQ2
DT0*lN03$2Rr^$j8$XJg*a_w;oRL*U^DXM5SRKES@qp?xXlxf<8$YXGZFPqeDV%c^D@w;KM`H&OqZ+Chh)Gz<53Q-
OplQQn)y*wR=z#ZrfyE0Q^vO;=9pzN=FYJon2$+0IDMbYBR0Wv4Buk1gBFw#zIb-Gf{fBa1(?{H6H>PM)q?HuM8JvcC9hut}v0?c
>TMor}eCN9+MbDlub;18_AP;j{$I+coiIH)b6wV~$(-
0EjPK2kh247QZHI@j~j&A$z0wR7C@fwYusTFT=x6oBZDNe(hZYJFPY(puXyz!lmexc2EtOb)#p+ZP{;18xLzSZNpxkja;ultLl!K
Lo~zx&5nro(|WBs4XF&Cpo5(HiczjI^b^TywdDmd$|~KD*#;pGH>3NNw1DJ}!u_?Cs(uo8idI;C>6P)ggbs({pYJ)CjOg)^@n4J9
&ni6SMQn9iJuhJWFh3I>W0Z34XC^sW+F=+Y68k$bfhKu<4`Lmz64hk&SHD!53O>cAF*677#l#*G4vh=3_6zB_`MV8p(%~z+L5KU4
T)x_+NcQUUT#o#k=>=I&yn9Z*(|EoIf+sy0xzEB;cxe|3VH)s1SdcpFWChPS{yezO(RQmkAvvE7h#!q>lKv!muxD&hUn(k7jS6~b
VL=t_0=v#2fy|{An-);T@Zr|~wN$e@LTxa#ZR@MahM#2sLTQ?9yZrHxZxC31Imcl*A=F$^%-
B~<8iM5oYu?E+EADlUfjx9(8KSO@9`_T8I9n~-
dyE1Uc@RYWNAUthB7+}C>)d@)ebpJiOR*I|L@a@ICDYiJW6C<t#=^t889N|XF?d|y?mHg?-
<u^)Ooob<3*WG0BJA#L`BnNt18xtkJ6y~OzA=Ujnln~IR=|g@NVS9&GY}EGyTwUSk!KA7z-
&a5OlK_>@>1xJ3B}o2g{r19(0_A?)j5K`Cdjf@fbSZr#1*<Ao(fbGU6i2H+$~`#qbx)r24{&<B<m^E*Z3k#<w&Udu+`uY`{t46#Y
6s#eVbL#Gkm$X987E00{5*Fiu{P?kg{AYgqxzXih!dgaM<E3=Jb>gbPeF3{|_`Hv#yPF&Vljdq0Uu`7$M<8;?Cv~Qj|ke8;M(#1(
r1-
VX**vSq$s*H}exrhk)MsTP^xTcCPzh!l;UPS=&N5lubTjN%|*E9g)>c<K~uQ+e?HZE}DlYmTAG#J%et(X;S}eXPlW@W)&)~lM(2P
o7LH>B}}^I69)=1U0)<|j5tugUN+GbvO5hErMuKZ?C2>V_}FJcjTUgd1(t&Rd8d#L$e|lKm+$YX$}BLu{Po>8*M{wRVhf_KbrsWc
vSXfZfw=mWPhw`I#lc<wGy1VBrG}S?%?J+97U#NC*cc0Ao8j=}OB9h`(ta~kL8sR4H2;nZCnJI8hP)KECn_tY6Wh5gb?pl`39xt}
41QgwG{Xef3*a4&9}d|}g~4JzxKfuRAfiC1j`uZV4U|uHaaHi_qB%9q5I_6yfzQArdkBW8u_T`$hD|Sa<|SI{<mozd@!0rR*}GXD
A|ZQw14oK>HSVF7SXmd;&JuL3v2X!^*z+w1&ya8C+M+(|Kk>I$jYP7&?x>sZRJlxwO^}q40@j44xY{F~`!*>LnJU3+9;^b}i%kqj
&*L(tMC|n4>iwV-N3l?Oa%2Gx_w>ovUF{lQ^z^(yE60vi_J8l)mZLNZX)+^fa_vV;eC-zyA^z^enLLy>1HuyS$ws#1eG`o>iAAo*
jvAr(G$eW1Vgoh$?t~?!=L_S7eeGq3QgJ%B9M@qd0Di!KL(r?j`+U(i{zHcser%4k9|}pol7HM7XbTzvjrdIY)H=5Cc9IW>PR;;J
?6u>ifWK9&jZLw&rQu?xF$t1(%yZ@AhWzco73JOK@a^bG9f{T@75LdCyWY8#+&|qjU2xnZuFLoImILrXWRo8%A%UOI?xSL{<f%?6
?`goDu*=IhLRq`5{J-TQg0r49GAT9rp&+-
7D#cWv)hSj#`?XkP&$W17UDEmodmRI+<b=3onM!Zjd3O&Q7|S3k;|2;4C<vyHcXY=a57Z+!wBw+PRIA=SD0upG^B*&7_^oOJLp&l
_cerYMP>ot+sTn)E8l^Ni<GfAR<}LM7%WcT{C3&B{F%XkN+xdRMu)iHFqg~QHu-
?md)efKENG7icVEL4%bPgV@XNT$=sn5QjhFb2t`9aUQgH?xLbAFZ&u5FC1Wd-
<3+>X<=Ia6!%_9lm$5NsDgG~1PMS5*{aX)0sHa;|b5u@_7tBCCVH*|CiEYmf!?FA9o1Dyiu#FeE{q65Jj-
Z>z!hxZh<^djTB~2}_8u*yL^{P-
8hn&<bY7d6l<cS^}0k(Vdz7#hvj)5N+H6kvFcWh#UIP%Z*0lo5SdWLqsb`F0`BHz)v;gdSbJa>V3gf>j;uN^7>zirKSLk7~L|_T7
uALB>RyA2k8O`9zV<ZTX>fvAPP)5L@~VDq8~I$1AT}9tDOCvpMHXHIPVQQnYHDrtq@O-
I?9>U;4p4pxLrFdu}*Yin2;{rj10i#kW+%`SOsaRowoEvW%45k(S@z``v7tq?6fl3>|CkOJ&Djg=>0Z5If&}OhO~w#0Wj~&0kg4A
UKq_b#HjY8rRCh&!~_a+xNd17E?xp+azsy0*{y<+aMhmrxfi3q>UNswce{+Lrel{-rokRibcQ6c-
l7x(2Wu*4j#HZn^CBmWHrq+WU-&RqbcH;p>*0kJZGx<HW6u4%?bnD^3j8@)W0}-
6I!E{wRx_Dv$&pf=JSKYodSYk|U~3@S#n^W{SVJ6Cb7O;r4}10M2J`S$wqgpQ0dq<5*t3(ag(Fi98jjsfZ_>@>ZDYXv4H99CA1<n
tZ$PT?e1s0a@|_qpyfO%3AR$oj$reE0q9X0@ua5Wbj-
$wq(pg+ODo(uP{e{{F8A=mK1rs#~7g|6GSIhJL{6~O4>vD?0Nz+qkN?g}jfwetuu!_sO)NV`jaIk|~Ozk0w-
;dOwxjM`RfpEB?Fl|;^CgseM?6Js`3I;!#p&wYPo^7>Cd9;y<BVf06lo%*L<PeVR4Y7SK;}_y_;trnPKVdCFyG(8^l{})U8EUtim
BNbETN3dBwDoSj8UZr7<|%g}*b6q>n1E|hOj`z((C(^cxON@1w6J_$A7kAD|MuXKY8-
tgwdz#}M|`c6OT5M*X*5WIzOlY1`6k8%E5iA%*3S$vLEN!4Q}$72?Y5#iuAaS|elwuoDp(ErVJUxa29vud$k*h$bG&r5E^PI&Cg6
ays9qy+o!&v&qH14m+mJvyDZ{0b=hKU49^B*~YrA#py9{3&BYwLv<Z_MfZV@uL^xzq&vpI)hJV|=Nf6gB3SwCq&fXWhLe((BwaM_
Gm3Z2tZ9Z2j4Eyr?KkWoB}lBwm+bc?x26meA7H5)l0yRH5FMsuTp&)2+{?_I3#)a)vbc;^S-
E*>9Ssmhaozls{zAunGD&|KO~!Qf*_$5qmI1jc(_T?4S3Md!{H5-Nn76-|&RqBjL|7^TGofht9p=o@oxs-X!{dk|drP=C{51S-
p}=Y*^unT7twx1MPv|EJ}5uNZ2r#{PcA<W=f_1rXnqR1<*3dWL|ql4q+tF1A<!J$i1a(4sfuM1>b~E9TJIynNyzwKVW)zHss?O!A
s<4=sut8>u!U^c@F=@VLtj-KMVD$bk$q(sE`2>?Dy_b>v|DZzwxE_MpAl(-Y14z=yYIQgC?%^ewn-
z1WW!7y<MFh?F4;QN4;IB~)MjVR~m>=}r};I9YL%D(zr<*57Z(QbHEZ=1u>e3jyF<%v{}P<|1vl8(Qz>5_1h+#J%~PYn61FML%Tv
H<I=~0rUxex^vW`)w=YFb;CbiN8rO~^PIPjdU#=>-ewxpDAP?mSgpW)3cU9aKq6_P!k9Lj9%pvKdsa-
)zjE(p4QH&;0rV?cD@itGT}ayA?j|9Xd;@4z7wJ^H12)_=K>dIpF0gYzALYU||35N~f~HQ34JEDL%g>$|!tP=YE-oED`R)+LiQn@
U1HNs16W4LVfbf?d_N+Qp74rfchE(9;SM?cm4+z0s$!x9Smk{Y6uohbIDZu)>BPJPH*JD&UvJir7`8_bQ@C(z8tL)iO^bnpL8GF@
a;P_^xvNDVkb`f$b1r6PIFwfcFRs)%txDy*JAG9)+GmMhbpmkWR9Q8U%r{ny;stYD{wB~YfN^G=E2zqwIgH%6o965n{(hOmIWWR(
V1DEz|g{v~Gbvf5}Ol{?rg>(${9p_R81u&VXZ7wyJ!xSFO9KQbmr{-
_!>e`$z%Eo1BfzJquqc1R|QD#TUJ#YYkeSqrn*TzO&6z+DrkAh7gbxE`hje^9eibncA9!}m$yp@bjU=IQ-sg}jwP+(*hNo9iny&I
QaTw1yf_jLs|cY7Ji@wk){p_|h7ZodupSO2$tlT9^YUU1O9S7%;k7z~b4Ry75<7{ZiTSnI~L+VC6!5TZusfv94rWEBLC6V>ni{^{
kvQ+86N2td38U%=7j$%#SSK*lk~XKw}M4nyC)H2t2G(1bhhx8<OI@H<B`M-|}HXu-
T3k@zR_5ZjuI7sykw%Ez6o0BDDur1!o2(I^WZ+cK}^s>_px28}fyz`RoD`#S@k{YB36K>&OSDn42aX=jRpY_5qDbh|7_J1-
(4GGjnit7Ztr#yF-
h=qj#heN6z?Vlm6fxY^cBxg*j;ThZtWU#Gx8(ENN53&E1bbvSgi83sTk4Rb_Cc3`uf(L+@!bxH2YT1WlY{AIqc$x$IOM5!$@etZc
2XR~|Ei!(~B`6xOm%!V{O$V`5jf2&HfCBN(Dn*l@&_m>UOD!;uR`nxEOnVqla<gg=xm?06@+IHAt;+8*SEU**(GjH6qG`I!Fmm|y
wpMh5Z6W+ybVT@+phWCJ~){+c*e8BjM`I~OmI1~}zs60LpBvK7B<XQ#Pa-CNy)P4;L$}YTu<v-
IMo&g!utKO90V{dwc84kK<#3O>i&w9&U?aWb#%?kq<i)9(Iv~GL$(e&G(dn{aAhX!51GS^i#RprCBf8`a}wjgG)n|kIq>oc~ni+H
msj#@I|P$4z%o5HbLwYjUDu{;Qm2fh~2#kNTVc#<V{#4kWp{HW2@pcNs?Dr^vz$^c{(L6{^EY;x5o2?@eUBXxoB)q7lm)SNa8Oj0
B($9Am5q2et!6>)twSnBcv+!-5>7UpjMV*9TOcSyFBekewmfr)=`wN4=sBUS-YgJlty4F`W1ZL;+p94F?}*8N^fr|&q`Q|zfR8Qc
72=(p`+v!*(fBimaDM#Wr2=H$D5vjw<*1c*9c)GbM+oFMKPsw*9gkF}XmJvcCw+vgGLWF2Y?&q_O%;xsT^0M)v>CD_4>8G;jyz3;
zDQI`XIwFvsRN+)A2VlI(9QGn_biR1CM*|L>}ql+C6tIDhC1D+5dad=v$!aake+R^_=z-
Sg@)@9VQiJpGx>Q?Hwp8>zp8RSCkN!X&*wh0^b&Sg!1FcCyxPO0M@)HvK!{}R0oY_HCU_xk!M{zi9JYg!sicS8&qpK$k3!zd4KqS
oDX3=r~*&Wwcj@>EvqYX?#X20y~aR~-)K6^B{`2X34;IAT>-
c97ICkYJI^#|hB9pH7MeIUq;r5Dme1>sh6U0l3^Q7<1jmQkOkdxK|F?5I*FV7r=E6On1k(p#u@`!sm8Z#S6=mH0aipJ(?yzYa6Bs
#UhPp+GR}SB_C}Y$|+N||8g0Bd?8v@LDy8IgH!i|&jM@L4jI3BL6!Ip*Qnm8H7^2jhjq#ZB?M0fDd#|C7J4)maT%a4+i#thcoMR=
9|`=cnvHr7YbwbQ1~*Gl*)Jdz3P<iHljuC?yVmEoV}$+9jd1oeJwgBj-eL=o?rz=L;6ajyWQ_6Ul?k7DzJlkw$N4#Aqe?htejPl1
%Er<X&I=o$!~Hr5Cdp$r$3@yFFFcl@570>E=jX2+%CHRn0|nrp+J__zI`*oF%SIDL`2_ulM{MY7O3!uHjR|Qbg>oV=<Z=3miD72E
joL}LY6p%DVlHBt%SYh!VbwnnoP7xweS{^_a&3mM<K_&T11c^o^KSns@Z0>`n6CFW`$cKMA(;JFDHRv0ceoYCBIgEzL64fY_^ug2
g#&)-
SvMxkZ5|kXhzRK*I)4JkbVfI5fd#bGQ5vAkQ?ptx7l%D+6@a)AUW%9xxBjk>V94yp^o~+l6ww9VleS|SGRQClagmXsu4t<+4VvQ;
HV^i*<hU7n2f<Ga)57M41HHPZRExmF_=0{9GAD$^?~%oBf8@C1cE-
k&RulZ9WnuQe`!FQ|Y5B>Tt#M8QKJ#fI71`VHrhx}eR3X%AQW1j@#BMZ4KkRS`xxYG-aD}B^6Hp!>lJl#g<%^s7gxJ;R3H9d&vlH
{Us07GDNy{rXz)fU-(a7?QW?(`oHkWc1##5Fbi{wLDf3yVZtCjB%$?tAt{e59RgNBVLkxr3vF?9RBzE-TCD8gM6jI9O_nO#y97Xb
B2>?2C5ona5QZb?l;Ke(0zN1A~OO$vg3_1Esy+k9U<XQZ;N(?_Yn2<>-
J4xP=oWF$fWNa@_Nw&vp}3gpeqd<}F%`qaQ|@mSFIc&p9wam@Erdf*y#yhcBJVbW)e$LNn#l$E0sj-
9TJixB+%qgg6%Z*eL@A1!}uigDvW)(oKRJ^7~7;t#1RSo_~$e8B|W61@3#w&%T2J$g6d-
Kuty*hhPywH|SzDyMkK7N_h+TC|i2pseTXGLMrxBmMC`Lz0#5W$co%=QeXlL#_aF@H0A~h~859c@JeyDkc=H0HjqU(?Gw3{@uRAs
bggk1~E}O=wLv=j0aPuKkJ+2F{jU2{qH)Q?$h&c`V$P#NUdwThm5E76uWhS(qOfV*$wD@Ce?Wj#rCOYPp?l(y=@H()2+6$#X7J&w
4_QOw;wn6AVDSj00000@kP_v(aJw^00G7?w~7G(l}KqavBYQl0ssI200dcD
'''
PACK = [6124,'84105e5146e126f9a69092e542e20395ba20e6dae35bfc560b6babe698ce2abd']
SOURCE = [17719,'ae79ee3cf0e5ace7731985d12663a68b699a876eacf19efbbd12636cf9cff70f']
OUTPUT = [647477,'d77b2c45c514c202d77562a4305daa17d7a42ae4b870a12d993fea888e48cc87']
LOG = [775,'1164c0e5efc1850bff1e70ef4f42ceb7b230cdf2fc7536dc50bd4424fe91b34a']
z=base64.b85decode(''.join(DATA.split())); assert pin(z)==PACK
source=lzma.decompress(z); assert pin(source)==SOURCE
assert len(sys.argv)<=2
root=Path(sys.argv[1] if len(sys.argv)==2 else 'vivid_tilt_recovered').resolve()
root.mkdir(parents=True,exist_ok=True)
p=root/'tilt_exact.py'
if p.exists(): assert p.read_bytes()==source
p.write_bytes(source)
r=subprocess.run([sys.executable,'-S','tilt_exact.py'],cwd=root,capture_output=True)
assert r.returncode==0 and not r.stderr,(r.returncode,r.stderr.decode())
assert pin(r.stdout)==LOG
assert pin((root/'tilt_exact.json').read_bytes())==OUTPUT
(root/'tilt_exact.log').write_bytes(r.stdout)
sys.stdout.buffer.write(r.stdout); sys.stdout.buffer.flush()
print('VIVID_TILT_COMPLETE_SOURCE_AND_ALL_OUTPUT_PINS_PASS')
```
