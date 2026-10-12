# minimum-0085

AI research report · 2026-09-18 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# FINCH22_INTRINSIC_COMPLETION_CORE_AND_ALL_REFERENCE_SECTOR_V1

**Calm Finch 22 · slot-4 · assignment minimum-0085.**

## 0. Результат и точная область действия

Получены три совместных результата.

**А. Универсальная структурная теорема.** Все допустимые начала отсчёта для одной неотрицательной Lambda на фиксированном настоящем многограннике образуют один аффинно-ковариантный выпуклый многогранник K(P), задаваемый положительными весами настоящих контактов «грань–вершина». Его размерность в трёхмерном случае полностью определена: **3 для любого непирамидального P, 2 для нететраэдральной пирамиды, 0 для тетраэдра**. Настоящий объёмный центроид принадлежит относительной внутренности K(P). Поэтому на **каждом** E17-теле одна Lambda, даже с точным спектром и реальной rank-3 геометрией, допускает открытое трёхмерное множество ложных центров. Это строгое препятствие попытке идентифицировать uniform density одними общими первыми балансами; это не утверждение о возможности 110 в этом множестве.

**Б. Новое доказательное покрытие девятиполюсного сектора.** Для неизменённой THICK_NINE_VECTOR_DISTINCT_TRIPLE_V1 построены **19 точных проективных полей**, проверенных на всех **42 настоящих контактах**, всего 798 строгих знаков. Они доказывают гораздо больше исключения исходного начала: **при любом начале отсчёта из K(P) полюс 0 и хотя бы один из полюсов 2,7,8 строго неустойчивы**. Следовательно никакое перемещение начала внутри этого фиксированного P не даёт одновременно одной неотрицательной завершённой Lambda и S=1. Доказательство не предписывает исходное escape-tree: оно покрывает все возможные выходы нужных полюсов, включая слабые стрелки. Дана полная полуалгебраическая область переменных Q и одной метрики N, на которой те же 19 сертификатов действуют для **всех** начал отсчёта. Она имеет непустую внутренность; все её аффинные переносы с взаимно-обратной метрикой также исключены.

**В. Новый точный контроль оставшейся свободы на E17.** На неизменённой геометрии E17-контроля parent построено целое семейство, t∈[0,1/5250], общей Lambda с **настоящими объёмными массами d_i**, настоящими гранями и одной rank-3 геометрией. Все её off-diagonal entries строго между 0 и 1, пары имеют product<1, спектр точно 3,-1,-1,-1. При t>0 начало не является настоящим COM: он равен -t e_z. Ложная центровка исправляется одним общим rank-one изменением трёх столбцов, а не независимыми строками. Все настоящие первые и вторые моменты пересчитаны отдельно. Один настоящий скалярный quadratic-flux residual равен **-2t** и выбирает единственный physical fixed point t=0.

**Не получено:** универсальное F>=10, исключение целого E17-типа, TREE253 или всех SPD-метрик фиксированной THICK9-геометрии. THICK9 имеет polar-body f-vector (14,21,9), не (10,17,9). Принятая нижняя цепь остаётся V>=10, F>=9, E>=17, C>=34. :contentReference[oaicite:0]{index=0}

## 1. Авторитетные зависимости и разграничение объектов

Литеральный parent **minimum-0080**, SHA-256 **3c9f2896c5e1bd7a4ffa21a2e8ec0e469d1f843282293d32313af000f581b1cd**, прочитан полностью, включая recovery-капсулу. Прочитан весь приложенный plaintext-аудитор; его 14090 bytes / SHA 712bb32799f8272e31efe6efdd3a1e30e93e7f9957318900bc214b9d47a41928 совпали с указанным pin. Старый полный P0-аудит не перезапускался: новые проверки независимо восстанавливают нужные геометрии и моменты, не возвращаясь к P0.

Исходная система parent при фиксированных полюсах — q_i.u_i=d_i, sum d_i=3, sum d_iq_i=0, sum u_i=0, sum q_i u_i^T=I, Lambda_ai=d_i-q_a.u_i. Её спектральная совместность не идентифицирует actual area centroids. :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2}

THICK9 сохраняет parent array **(-1,0,1,2,3,4,5,6,0)**. Это не FULL TREE253 с parent (0,0,1,2,3,4,5,0,7). Независимые cap-one строки исходной THICK9 допустимы, но не являются одной physical Lambda и не называются оптимальными строками. :contentReference[oaicite:3]{index=3}

Целевой поиск библиотеки также прочитал полный аналитический §2 «A complete characterization of the remaining false-mass freedom» в историческом journal, source SHA 61f45c1411c065e1f8815e4081acbe9060b990225680d8a6a5db38d8a19139d3, внутри диапазона UTF-16 [929800,944800). Там уже имеется линейный false-center domain для специальной семьи весов интеграционных треугольников. Поэтому сам приём «линейный образ положительных весов» не выдаётся за новую идею. Здесь доказана эквивалентность **всей** facet-Lambda completion, классифицирована размерность её полного контактного ядра и получено новое all-reference покрытие. Старые вычислительные объекты того исторического результата не использованы как входы.

Независимо проверен первоисточник I. Izmestiev, *Fitting centroids by a projective transformation*, arXiv:1409.6176v1, §§2.1 и 4.2–4.3: проективная параметризация и вариационная связь объёма, центроида и вторых моментов. Это контекст проективной интерпретации, не источник наших 19 сертификатов или утверждения о размерности K(P). Все используемые ниже формулы и знаки выведены самостоятельно. Внешняя первизна общей конструкции не установлена. :contentReference[oaicite:4]{index=4}

## 2. Внутреннее контактное ядро одной Lambda

Пусть P={x:q_i.x<=1} — настоящий ограниченный полноразмерный 3-многогранник, 0∈int P. Его настоящие вершины обозначим x_v, множество контактов — I={(i,v):x_v∈F_i}. На этих и только этих контактах введём μ_iv>=0 и систему

    sum_(i,v) μ_iv q_i = 0,
    sum_(i,v) μ_iv q_i x_v^T = I_3.                 (A)

Определим

    K(P)={ c=(1/4)sum_(i,v) μ_iv x_v : μ>=0, (A) }.

Обозначения для реализации: A — 12-строчная матрица (A), b=(0,0,0,vec I_3), L — 3-строчная матрица с контактным столбцом x_v/4. Все строки и столбцы полностью задаются настоящими инциденциями.

### Теорема 1. Точная эквивалентность всем началам отсчёта

K(P) — непустой компактный выпуклый многогранник, лежащий строго внутри P. Для c∈int P следующие условия эквивалентны:

1. c∈K(P).
2. Для полюсов q_i(c)=q_i/(1-q_i.c) тела P-c существует одна неотрицательная Lambda, удовлетворяющая всей системе общих первых балансов parent.

Строго положительные контактные веса дают строго положительные off-diagonal entries. И наоборот, строгая completion допускает представление со всеми μ_iv>0.

**Доказательство.** Контакт q_i.x_v=1 и след второго уравнения дают sum μ=3. Поэтому множество μ компактно. Для μ положим α_i=sum_v μ_iv и v_i=sum_v μ_iv x_v. Тогда

    sum α_i=3,  sum α_iq_i=0,
    q_i.v_i=α_i,  sum q_i v_i^T=I,
    sum v_i=4c.                                      (B)

Для любого r∈P веса μ_iv(1-q_i.r) неотрицательны, имеют сумму 3 и

    sum μ_iv(1-q_i.r)x_v=4c-r.

Следовательно (4c-r)/3∈P. Выбрав r∈int P, получаем c=(r+3z)/4∈int P. Дополнительно доказано настоящее включение

    -(P-c)/3 ⊆ P-c.

Это необходимое следствие, а не замена полной системы (A).

Пусть h_i=1-q_i.c>0. Зададим

    d_i=h_i α_i,
    u_i=h_i(v_i-α_i c),
    Lambda_ai=(h_i/h_a)(α_i-q_a.v_i).              (C)

Из (B) непосредственно следуют все пять групп уравнений parent. В частности sum u_i=sum v_i-c-3c=0. Поскольку v_i/α_i∈F_i при α_i>0, все entries неотрицательны. Общий rank-four оператор и спектр следуют из этих уравнений, а не навязываются отдельным строкам.

Обратно, у неотрицательной completion d_i=(Lambda²)_ii/4>=0. Если d_i=0, все q_a(c).u_i<=0; ограниченность P-c заставляет u_i=0. При d_i>0 точка u_i/d_i находится в соответствующей настоящей грани P-c. Возвращая её в P, полагаем α_i=d_i/h_i и v_i=u_i/h_i+α_i c. Получаем (B), а каждую точку v_i/α_i разлагаем по вершинам своей грани. Это даёт μ и (A). Для точки относительной внутренности полигона существует выпуклое представление с положительными коэффициентами всех его вершин, что доказывает строгую версию.

Непустота получается из настоящих площадных центроидов: α_i=Area(F_i)/(Vol(P)||q_i||), v_i=α_i C_i удовлетворяют (B) с c=g(P). Триангуляция каждой настоящей грани даёт положительные коэффициенты всех её вершин. Поэтому g(P)∈relint K(P). При переводе базового начала на r контактные веса переходят в μ'_iv=(1-q_i.r)μ_iv, а центр в c-r. При невырожденном линейном преобразовании меняются только координаты контактных векторов. Тем самым K аффинно-ковариантно. ∎

### Теорема 2. Полная трёхмерная классификация размерности

    dim K(P)=3, если P не пирамида;
    dim K(P)=2, если P — пирамида, но не тетраэдр;
    K(P)={g(P)}, если P — тетраэдр.

**Доказательство.** Сначала rank A=12 для любого P. Левый аннулятор A имеет вид (a,B) и удовлетворяет

    q_i.(a+B x_v)=0  на всех контактах.

Нормали при настоящей вершине порождают R³, поэтому a+B x_v=0 на всех вершинах. Их аффинная полноразмерность даёт a=0,B=0.

Аннулятор [A;L], после безвредной перенормировки последнего множителя, соответствует проективному полю

    f(x)=a+B x-(w.x)x,

равному нулю на всех настоящих вершинах. Для матрицы

    T=[[0,w^T],[a,B]]

это означает, что все подъёмы (1,x_v) — собственные векторы T. Они порождают R⁴, значит T диагонализируема и все её собственные значения вещественны.

Если значений несколько, подъёмы вершин распадаются по прямой сумме собственных подпространств. Одномерное подпространство содержит только одну вершину; все остальные лежат в дополнительной аффинной плоскости, то есть P — пирамида. Если одномерных слагаемых нет, в R⁴ остаётся только разбиение 2+2. В каждом таком слагаемом вершины лежат на аффинной прямой, где может быть не более двух настоящих вершин. Тогда P — тетраэдр. Следовательно у непирамидального P матрица T скалярна; условие T_00=0 делает её нулевой. Поэтому rank[A;L]=15.

Для нететраэдральной пирамиды ограничение T на трёхмерное пространство подъёмов её основания скалярно: иначе тот же аргумент разбил бы многоугольное основание на не более чем три вершины. На подъёме апекса скаляр независим. После исключения общего скаляра остаётся один параметр аннулятора, так что rank[A;L]=14. Для тетраэдра четыре подъёма образуют базис; диагональные значения произвольны, и после удаления скаляра размерность аннулятора равна 3, то есть rank[A;L]=12.

Наконец, положительность настоящего контактного решения позволяет все достаточно малые изменения в ker A. Поэтому

    dim K(P)=rank[A;L]-rank A.

Это даёт 3,2,0 соответственно. ∎

В частности, **ни один E17-многогранник не является пирамидой**: пирамида с девятью гранями имеет восемь вершин основания и один апекс, то есть девять, а не десять вершин. Следовательно на каждом E17 настоящая центровка — внутренняя точка трёхмерного множества строгих совместных completion. Успех решения (A) не может сам по себе выбирать uniform COM.

## 3. Геометрический смысл dual-сертификата

Для a,w∈R³ и произвольной матрицы B определим

    f(x)=a+B x-(w.x)x/4.

Это инфинитезимальное проективное поле: оно получается дифференцированием (x+ε(a+B x))/(1+ε(w.x)/4). На грани F_i его нормальная компонента аффинна:

    q_i.f(x)=q_i.a+q_i^T B x-(w.x)/4.

Если она неотрицательна во всех настоящих вершинах F_i, то неотрицательна на всей грани. Для любого c∈K(P), суммируя по одному общему μ, получаем

    w.c <= tr B.                                      (D)

При настоящей плотности тот же вывод следует из div f=tr B-w.x и дивергенции: поток наружу равен Vol(P)(tr B-w.g(P)).

Обратно, **все** опорные полупространства K(P) получаются этим способом. Для фиксированного w обычная двойственность конечной линейной программы даёт

    max_{μ>=0, Aμ=b} w^T Lμ
      = min_{a,B: q_i.a+q_i^T Bx_v-(w.x_v)/4>=0} tr B.

Прямая задача непуста и компактна; её конечный максимум и двойственный минимум достигаются. Эквивалентно, (b,c) должен принадлежать конечнопорождённому конусу контактных столбцов (q_i,vec(q_i x_v^T),x_v/4). Отделение точки от этого замкнутого конуса даёт коэффициенты a,B,-w, неотрицательные нормальные значения и tr B-w.c<0. Это полная геометрическая dual-форма Farkas, а не выбранный достаточный подкласс независимых apex rows.

Именно здесь проявляется механизм прежнего расхождения THICK9: независимые строки не обязаны быть одной положительной контактной квадратурой. Поле может иметь положительный наружный поток на всех гранях и отрицательную дивергенцию в ошибочно выбранном начале; настоящий g(P) компенсирует это, а фиктивная общая центровка — нет.

## 4. Девятнадцать полей: все начала, не только исходное дерево

### 4.1. Постоянные геометрические метки

THICK9 задаётся следующими числителями полюсов с общим знаменателем 10^6:

    (1000000,0,0), (489108,499458,2170), (144132,583880,-2431),
    (-145658,497435,18119), (-317895,309738,64261),
    (-373438,103862,67557), (-346628,-58016,8799),
    (-272656,-120913,-105895), (241874,-415725,100624).

Её 14 настоящих полярных треугольников, в постоянном порядке:

    (0,7,1),(0,1,8),(0,8,7),(1,2,4),(1,7,2),(1,4,8),
    (2,3,4),(2,7,3),(3,7,4),(4,7,5),(4,5,8),(5,7,6),
    (5,6,8),(6,7,8).

Прямая вершина x_v — единственное решение q_i.x_v=1 для трёх меток соответствующего треугольника. Контакты I перечисляются лексикографически по (i,v), где i входит в треугольник v. Их 42. Это полностью определяет вход сертификатов и не требует загрузки parent-файла.

### 4.2. Механические функции линейны по общему началу

Пусть N>0 — одна полюсная метрика, а прямая метрика M=N^{-1}. При фиксированном P и переменном c∈int P положим G_ij=q_i^T Nq_j и

    e_ij(c)=s_ij+w_ij.c,
    s_ij=G_ij-G_ii,
    w_ij=G_ii q_j-G_ij q_i.

Тогда

    q_i(c)^T N(q_j(c)-q_i(c))
      = e_ij(c) / [(1-q_i.c)^2(1-q_j.c)].            (E)

Знаменатель положителен. Следовательно это точный numerator стрелки, а не линейная аппроксимация. Настоящие соседства не меняются при переводе начала.

Для положительных λ_ij, имеющих сумму 1, положим w=sum λ_ij w_ij и s=sum λ_ij s_ij. Проективное поле раздела 3 с этим w доказывает

    sum λ_ij e_ij(c) <= s+tr B,  c∈K(P).            (F)

В recovery находятся все 19 полных рациональных векторов (a_x,a_y,a_z,B_xx,B_xy,...,B_zz), с общим знаменателем 10^12. Для каждого поле проверено во всех 42 контактах. На точной THICK9 и N=I:

    q_i.f(x_v)>1/(2·10^6)  на всех 798 контактах;
    s+tr B < -1/30000      для всех 19 полей.

Наименее отрицательная верхняя оценка точно равна -34912251/10^12; никаких float-знаков в сертификате нет.

### 4.3. Полное конечное исключение стрелок

Первые 17 полей запрещают следующие настоящие направленные рёбра на всём K(P):

    0→1, 0→7, 0→8;
    2→3, 2→4, 2→7;
    7→0, 7→1, 7→2, 7→3, 7→4, 7→8;
    8→1, 8→4, 8→5, 8→6, 8→7.

Поэтому 0 строго неустойчив, а у 2,7,8 остаются только выходы

    2→1;   7→5 или 7→6;   8→0.

Восемнадцатое поле запрещает одновременные слабые стрелки 2→1 и 7→5, используя веса

    (324869,675131)/10^6.

Девятнадцатое запрещает одновременные 2→1,7→6,8→0, используя веса

    (24751,817764,157485)/10^6.

Если 2,7,8 все не являются строго неустойчивыми, у каждой есть слабый выход на настоящее ребро. Ветвь 7→5 противоречит полю 18, ветвь 7→6 — полю 19. Следовательно хотя бы один из 2,7,8 строго неустойчив наряду с 0. Это доказательство включает нулевые стрелки и не использует ни H0, ни genericity, ни выбор полного escape-tree.

По обычной полярной формуле foot_i=Nq_i(c)/(q_i(c)^TNq_i(c)) эти две строгие полюсные неустойчивости означают две строгие устойчивые грани P-c. Поляр не центрируется по собственной плотности.

### 4.4. Полный рецепт исключённого переменного сектора

Рассмотрим любые девять полюсов Q с 0∈int conv(Q) и теми же 14 настоящими треугольниками и метками. Это условие проверяется конечным рецептом: решить указанные 14 тройных систем, проверить все строгие неинциденции и перебрать все 84 тройки, убедившись, что других допустимых вершин P нет. Никаких новых меток при изменении Q не вводится.

Пусть N>0 и ρ=G_00. Для ν-го буквального сертификата из recovery берём поле с a=ρa_ν, B=ρB_ν, а w_ν,s_ν заново вычисляем из Q,N и его неизменённых λ. Определим Ω следующими **всеми** условиями:

    q_i.(ρa_ν)+q_i^T(ρB_ν)x_v-(w_ν.x_v)/4 > ρ/(4·10^6)
        для каждого ν=1,...,19 и каждого настоящего контакта;
    s_ν+ρ tr B_ν < -ρ/60000
        для каждого ν=1,...,19.

Вместе с указанной настоящей инциденцией и N>0 это полный полуалгебраический рецепт Ω. Координаты x_v — заданные рациональные функции Q; знаменатели контролируются невырожденностью выбранных троек. Точная проверка более сильных запасов выше доказывает (Q_THICK9,I)∈Ω и непустую внутренность Ω. Условия однородны по N; свободного масштаба метрики не потеряно.

**Для каждого (Q,N)∈Ω и каждого c∈int P_Q одновременно completion и S=1 невозможны.** Вне K(P_Q) запрещена completion; внутри K(P_Q) работают те же 19 полей и доказаны S>=2. Таким образом c не дискретизируется и не покрывается только окрестностью нуля.

Можно дополнительно взять всю аффинную сатурацию пар «тело–начало»: P↦TP+b, c↦Tc+b, N↦TNT^T, det T≠0. При этом P-c↦T(P-c), а именно **полюса относительно соответствующего начала** переходят как q_i(c)↦T^{-T}q_i(c). Матрица Lambda и механические знаки сохраняются. Для чисто линейного изменения проективное поле переносится как a↦Ta, B↦TBT^{-1}, w↦T^{-T}w; перевод тела вместе с началом уже учтён аффинной ковариантностью K(P). Полюса, нормированные относительно неподвижного нуля, при переводе тела требуют отдельной перенормировки и здесь не объявляются неизменными. Независимой второй метрики это не вводит.

Открытый сектор пересекается с исходным S=1 относительно нуля и всеми девятью независимыми cap-one условиями: настоящие исходные стрелки строги, а все 36 барицентрических коэффициентов исходных четырёх тройных сумм положительны. Эти факты также пересчитаны точно. Не заявлено, что Ω содержит весь прежний 13-entry сектор parent, весь THICK9-комбинаторный тип или все метрики N.

## 5. Физические массы не закрывают fixed point: точный E17-контроль

### 5.1. Общий механизм rank-one исправления центроида

Пусть при произвольном внутреннем начале настоящие q,d,C дают actual Lambda_0, а настоящий COM равен g≠0. Тогда

    Lambda_0 1=3·1-4Qg,  Lambda_0 Q=-Q.

Ищем rank-one изменение, сохраняющее **те же настоящие d** и всю систему completion. Оно существует с неотрицательными итоговыми entries ровно тогда, когда существует вещественный вектор v с

    sum v_i=4,  sum v_iq_i=0,  v_i(q_i.g)=0 для всех i,
    Lambda=Lambda_0+(Qg)v^T >=0.                    (G)

При строгих off-diagonal знаках это строгая completion.

**Доказательство.** Rank-one изменение должно посылать 1 в 4Qg≠0. Нормируя его второй множитель, оно обязательно равно (Qg)v^T с sum v=4. Сохранение действия на Q и диагонали даёт остальные два линейных условия. Обратно, изменим u_i=d_i C_i на u_i-v_i g. Сумма новых u равна нулю, общий tensor sum q_i u_i^T=I и контакты q_i.u_i=d_i сохраняются. Значит выполнена вся система parent. ∎

Следовательно rank-one ремонт при g≠0 должен быть поддержан только на гранях, чьи полюса ортогональны g. В общем положении таких граней может не быть; это препятствие только rank-one ремонту, не всем completion ранга изменения 2 или 3.

### 5.2. Постоянная геометрия и непрерывное семейство

Сохраняется буквально родительский E17: нижние вершины 0..4 равны (B_i,-1), верхние 5..9 — (B_i,1), где

    B=((-3,1),(1,-3),(2,0),(1,3),(-1,3)),

кроме вершины 8=(5/4,13/4,1). Порядок девяти настоящих граней:

    (0,1,2,3,4), (0,1,5,6), (0,4,5,9), (1,2,6,7),
    (2,3,8), (2,7,8), (3,4,8), (4,8,9), (5,6,7,8,9).

Настоящие Vol=35 и g_raw=(-47/560,943/1680,1/140) совпали с parent. Не создан новый псевдо-E17 и не изменена нумерация. :contentReference[oaicite:5]{index=5}

Среди исходных полюсов

    q_1=(-1/2,-1/2,0), q_2=(-1/4,1/4,0), q_3=(1/2,-1/6,0).

Их настоящие исходные cone masses α_1=16/35, α_2=16/35, α_3=12/35. Вектор

    k=(0,1/2,2,3/2,0,0,0,0,0)

удовлетворяет sum k=4, sum k_iq_i=0 и k_i q_i.z=0.

Для любого t∈[0,1/5250] возьмём начало c(t)=g_raw+t e_z, нормализованные полюса q_i(t)=q_i/h_i(t), h_i(t)=1-q_i.c(t), и **настоящие** массы

    d_i(t)=α_i h_i(t).

Если C_i — настоящий исходный площадной центроид, положим

    Ctilde_i(t)=C_i-c(t)+(t k_i/α_i)e_z,
    Lambdatilde_ai(t)=d_i(t)[1-q_a(t).Ctilde_i(t)].    (H)

Это одна общая матрица. Контактная реализация полностью задана добавлением t z к настоящим контактным весам, где единственные ненулевые z_iv:

    z_(1,0)=-1/4, z_(1,5)=1/4,
    z_(2,0)=-1,   z_(2,5)=1,
    z_(3,1)=-3/4, z_(3,6)=3/4.

Все настоящие facet mass sums остаются неизменными; A z=0 и Lz=e_z проверены точно. На всём интервале веса положительны. Поэтому (H) удовлетворяет общей первой системе, Lambda²+Lambda=4·1d^T, rank Lambda=4, rank Q=3 и точному спектру 3,-1,-1,-1.

Кроме того, на **всём** интервале 0<Lambdatilde_ai<1 при a≠i и 0<d_i<3/4. Это не вывод из двух выборочных тестов: числитель

    h_i(t)[α_i(1-q_a.C_i)-t k_i q_a.z]

аффинен по t, поскольку k_i q_i.z=0, а знаменатель h_a(t) положителен. Неравенства 0<Lambda<1 эквивалентны положительности двух аффинных функций; точные проверки концов доказывают весь интервал. Для масс аргумент ещё проще. Поэтому все reciprocal products<1 также выполняются.

В конечной точке t=1/5250:

    c=(-47/560,943/1680,11/1500),
    actual COM in this frame=(0,0,-1/5250),
    Ctilde_1-Cactual_1=(0,0,1/4800),
    Ctilde_2-Cactual_2=Ctilde_3-Cactual_3=(0,0,1/1200).

Остальные шесть facet points настоящие. Максимальный entry completion точно равен 105719/105770<1; при t=0 он равен 9869/9870. Метрика M=N=I общая, rank Gram=3. Конечный настоящий механический класс — строгий (S,U,H)=(9,10,17), не 110.

### 5.3. Свобода с настоящими массами здесь трёхмерна

Пусть Fmat имеет девять строк индикаторов принадлежности контакта соответствующей грани. Точный расчёт на этой неизменной геометрии даёт

    rank A=12, rank[A;L]=15,
    rank[A;Fmat]=17, rank[A;Fmat;L]=20.

При ограничении Fmat μ=α_actual настоящее μ по-прежнему строго положительно. Значит image(ker[A;Fmat]) под L имеет размерность 3. Поэтому вблизи g_raw имеется **трёхмерное открытое множество** completion с правильными настоящими cone masses при каждом выбранном начале, не только показанный вертикальный отрезок. Строгие entry bounds исходного actual Lambda сохраняются при достаточно малых таких изменениях. Это локальное существование; глобальный радиус и S1 на нём не заявляются.

### 5.4. Настоящие вторые моменты не подменены псевдомоментами

Аудитор интегрирует каждую настоящую грань и тело при обоих концах интервала. При g=E_P x, R=E_P xx^T, Sigma=R-gg^T и Y=1-Qx вычисляются именно

    m=E Y=1-Qg,
    H_actual=J-1(Qg)^T-(Qg)1^T+Q R Q^T,
    K_i_actual=d_i E_Fi(YY^T).

Проверены все общие тождества в правильной нецентроидной форме:

    sum K_i=5H_actual-1m^T-m1^T,
    K_i(d/3)=Lambda_actual[:,i],
    sum d_i T_i=5R,
    sum d_i q_i[k](T_i)_ab=delta_ka g_b+delta_kb g_a,
    T_i q_i=C_i_actual.

Все площадные covariance matrices имеют rank 2 и PSD; actual K_i имеют rank 3; actual H имеет rank 4. Sigma вычислена из объёма и не равна механической I.

Напротив, H_formal=J+Q Sigma Q^T удовлетворяет (I+Lambdatilde)H_formal=4J, но при t>0 **не равна** настоящей H_actual. Настоящие K_i возвращают Lambda_actual, не Lambdatilde. В частности

    sum_i d_i q_i[z](T_i)_zz=-2t,

а в конечной точке это **-1/2625**. Требование нулевого собственного COM quadratic flux выбирает на всём семействе ровно t=0. Уже линейное контактное равенство T_iq_i=C_i_actual запрещает подставлять Ctilde_i вместо настоящего среднего при сохранении actual T_i.

Это не контрпример к приложенной actual-moment mass-identification теореме: она требует настоящие C_i,T_i,Sigma, а не подобранные массивы. :contentReference[oaicite:6]{index=6}

## 6. Полная recovery-капсула и фактическая проверка

Капсула ниже содержит все байты нового самостоятельного аудитора: обе точные геометрии, неизменные номера граней/контактов, все девять старых triple-сертификатов, **все 19 новых рациональных полей**, точные hull/84-triple проверки, rank computations, положительный контактный транспорт, первые и вторые настоящие интегралы, полные actual/fake Lambda,H,K и проверки механики. Внешний checkpoint или исходный parent-файл не требуется.

Для треугольника (a,b,c) с s=a+b+c и D=det(a,b,c)>0 используются точные стандартные интегралы: mean origin-cone=s/4, его второй момент=(ss^T+aa^T+bb^T+cc^T)/20; площадные mean=s/3 и второй момент=(ss^T+aa^T+bb^T+cc^T)/12. В одной грани веса D пропорциональны настоящим площадям. Никакие PSD-массивы вместо интегрирования не подставлены.

Сохранить следующий полный код как recover_finch22_core.py, UTF-8/LF с конечным LF, и выполнить в пустом каталоге:

    python -S recover_finch22_core.py

Проверенная среда — CPython 3.13.5, только стандартная библиотека, assertions включены. Численный locator использовал NumPy 2.3.5 / SciPy 1.17.0 лишь для подбора полей; конечный источник не импортирует их и не принимает solver status за доказательство. Коэффициенты полей округлены до 10^-12 с малым наружным диагональным сдвигом; все окончательные знаки затем проверены рационально.

Pins:

    recover_finch22_core.py: 11756 bytes
    SHA256 8b251dacad6d203ca444fa992112f90e422e76c240e66ba5fc101adc01db5e87
    finch22_core.py: 20964 bytes
    SHA256 0866d3fa7d44adc3d57558ba295c0524c21a883d2e8bd5fad122ed2ba2f4874e
    finch22_core.json: 164934 bytes
    SHA256 ac56328643e1b00a87e94956aa2c6920a3a1aaf39c5e36d3327fd6c41032083c

Два отдельных чистых запуска исходника дали побайтно одинаковые JSON и log. Отдельный чистый запуск именно этой самодостаточной капсулы также прошёл. Непрерывные теоремы разделов 2–5 доказаны выше; исполнение не выдаётся за их proof-assistant формализацию.

```python
"""FINCH22_INTRINSIC_COMPLETION_CORE_AND_ALL_REFERENCE_SECTOR_V1 recovery.
CPython 3.13.5, standard library, assertions enabled, no external input.
Run: python -S recover_finch22_core.py
"""
from pathlib import Path
import base64,hashlib,zlib,subprocess,sys
assert __debug__
DATA=r"""
c-p0W`&ZjWxAyP;E7YE~zF1^TG`b6-u0;qmG?X;Jo90_SK3>8WAn*-KHju9V@8{WjMmL+Zeb1XxTN=&m*|RUt-gA+E{PD-*le5DQ
wmm#KyF5QRyEr)<9)9}ux6`A`lTT;3JU<#9oV_0&oSqKPkB*PdkIoK{h8IVNm!HmuU*vA*@VDpUc0MzlUFqz4`$k?QvvIN<8<Xs6
nJl08jU><0Ws%KixslG2t4TWEH)eAqn=MvFZp@d)5-sM_S(@j&o%7Xf&sZpuy$j<yn~iS4+-SZ`cNfo{-;!lID?svQc>im<xc?a5
J$^m;`T5>=pQ0ii|MKXI&c%lV+w%=)6kXe4<d3{mUX6pqy}nLtnb>KVj;z%6qp`dWUB?b>J95U3?MNrNwk+$~3+0s@jdwejkHqF}
y39b@xJl>Jv{+_oZrrEo!YFRjY-voAt8|j@8fWRFF~7P?M;H^BG-PBfmUFt#)@koLODE&bh~#jcjgkU1FlZye0H4xvFBui9WYU{L
RK|5O$<y8l!vvLVR;0^yGBF?y^k*#8_>W|;+c`@!6fHqyHA5fE9Mz7cMcvM?Az^wVaX*6Oi{)xWDloEK>m$YZe*E#r&h>IWHLjP*
NNFgWF6PU^IMxNIY#ggPkioK;&nH!#(R_N9%@S^>sw|S?7HTgm{D#|(zP?RzdL-`h`K+TjFowf%dbPS44m+K3dTos7MK=*w=H4<b
R?C@@ucqCnooC}3BY6_fkcIIrTW}SV8|162R)hXi@5R~!uAPj>8?|5mMeWgYp6BiQNnZ|juKM<%m*4|eav=1TMP-(HD)g14GO3;_
n&Y(S9+-O_1OJk^Kgsf<J53hdW3e<%W@Sl?91Qkn@g$vf6LWtZA9tn6E$I0@J%_v8q}`b&ME~yMS^89TyLVjauC8=1W~Py0?ESkz
|9)VKv-vDFt9E#DM;1Y)<uH%CR=dIv@%<jP$GGkXF?|TS1#7)^RdK-&@VCF-i5FGzCOfaCX!1?}idZxEX3;9ArjxCvTz4|)#l;SH
I2mvw&HGvzQn4g4>#|D9bRkH|I|rsVpy{-GAl}s)?vn{F#Yib*M7@L7J9E%fj%t~2wEUjwaUrhCLTaT+B%35&|GOmeQ8Gz!Uo@x`
J5P!VRZn!|2Iun?{J3q{{nE?0->X5hJ-5lm03EWps>N|Pi{m?UQ^7OMZPqGc8o0avht{9P)=L)8E&*pU|B2;iLV3_XHh-XGk<C_V
^)%^c%F<(P{n=oj%sgW=r|-D`^k&fz7K#SnGkwiX+xC@vW$nV!o$ho$chpaB@d6N*Y?*bh+3Q#~#|JH`p7*YnX>#9mmP|Rz?P@aV
e$k9wC!;iv|M;^Ke>TpkyC&3k>j8Z+P2n`g1gjFGxc>z_)n)(^1ZWCS39_$5VhXw#;i9FD*&LyL_Dq(xrH<Q}oO6aI`+3|~*K4zP
%N?z$qc4Ldtpvk*`YE<*{p9A}EbjLj?lBwe-^RULBG@d>+l0W-(@$+W+s2|I+U-wPRdk;|$Hi&^2hEf)1h-CSt7*DK2GGsfHlO0S
0l2JyKAN&|-8Nb6Xrg(X&nbL&xvpxOj&IVc{14TuzRMAG67&Dj7viSb1e2CliL$VnB~op>SsdGcs-70}2{`BvY6nf(AgOu75XN`$
AM3sTpw<p5{Mm92%>=W)<ra)spu$<wmA=`-|NUgJn=BUTYz)5kso<(ANX$)rkP*;mzR?J{*KeBEE|RKMns*xpIC_TdPO}+_!i32_
6*1jWA9zGjysrCrn@v&!Rep%ov-SuU%XG~TdUCLj?~+3_Fqtr;*1DDsb%OE%jeY$?OzpP@L%IMh427<U$)=f-N7O#{g;|z^f%sA}
FX{(&>wzh1voqgXdn^e3@HKt!S$h~r9qh>l${`U)O;}+&>T8078pEl4AXwXi2`KoX1owvB;fpHPaDwEI%xr&}CNsXsQ#jqYGQBY>
#FVS-UuVm_i2HOs*l~2dxL+192g4eO9kaGw@J<i7-&%p_gb9yoqL+V9?*+`49D_(eJ-LDWNY{&;kg`xBDyUUg$z0Iao&I_)oAA!;
#gs=f0XTp%jqy(wff!}X>r(1$SE|}(By~1OzKc~>kc-^hO2TS7d+%Z-E$@V?yaxQXYmf8S@fc#GOnW5y<DI8BP7_s4$PolCh00sr
iSZk0Z_!vyiHg!HQQ|8_&23ZDss>4Q)u3xz4Z37YrMZqFG`6X-05FRfSJ53+bgLSQ>ZOpVXtr#fn0@05Cb62<M407)W=HcTxsECN
&dz3a;%^|BE1~;V&XLb2Ys&AgUQV0lkEZz=cDXJS)cK=W*ID9~SxzJlC~MkZ#@7BKTer}A^lwfmmRo7n=-*DOmhH4^IoPK;z>-Mq
(>F!FqM24L|4(VvQq8axkJ~Aho_CDu6s!1dinVO|Ac?R7KS;IAxEdjcQU)lazc(A0hEfbgf>>uGxaEPF&2}^rA`N(-arsjTKeI|(
cVg5|A-KWb6Gov%Q=)W(7s7;cWJNtPvXv(a?CY0Jr)B3)${Z05=a^cFlWHPBNYw8iASn0sw1H#wNn_e^GEj4^MLu@w{J-X}CR!$I
3{(J58@VMHoO~w*bxd)uXL9LmG#{sw=XT1>H_v9Y7BxbtIIb5JFrm|e->fvwM)gGM52|=??rFknjiE|N$!=Dpm;#!AzDTIc378;P
HS0N3o6=fOuNqQLl$6P1l2I`nCq>fzEWWDXTn=o8sD#Olrjm*4wn3=6bq{5#sO=YOhWmd;e*T(2p}3u|{dJ|iq!}Y>eO6IJcgm!}
iXwUtLsUfB+&2#C8k0~B)g0ESgRPb=`$7SsSuPI5p%TL4_Bqc0pF=H;y!(~n;RMM8Dr;d(SEY-P^HBM|QOt{E5?6~Ds@KtTTS|&j
12s0{V;Q)&<2EKUF&?NWO-mv4Nillgc+YXUPou5nPm>?BTmm)TH>L-SLB#Cq`2EW<7j5@2#y$qNo6W}QQ<oKQ4$2nQLe?85R72);
HBe$Ca~RH-V}$Fk;<FwLXJ`+3GZ%|_7Wh@kjO#ap!~@a%TnmDP@Ru{2uV$H%J^*CmSelK<Lfz}}WE71{;XLGo!|}tuVxWZByDgNY
?3b$$d{F^W)R&)Ic10O2QLUo}w=2`oK9Bu{=bg@f8JD*y?y?(T&cwL<aB}!DqC^qRc$#{7espAe&Ti)n{wOW}C-9#sx^5UrD->=N
xn3x28Bn2gUFq1u3!N~uM9+2|X$s=C+mo*6dsIJg9Z$$m$_Nd5jts)c6OI)HPAGiW_9Yhwj*EL~IiYV0Kk&SuB;>fhZ-=7ig_iV1
7(`6R4s74^MNisRBprNP9_ZqU?aDB4MbDL9V54Kp@@*GD@tKp|0tGuezFGV6vat+yHt1X)W8{_y1hHiaDMJ1ZML@#^db|7`U{Xon
E<I=EbOG%A(8fbxc-O%<-Mjeq_}gP*9`1eq_W9n&eFz5GfXAz3qV=fUS=lfQK${9rmE(SEGF+IA@mwAc%DP=;JM8vMQ(dxQ!Lqs$
)F`BDcD^FX=A?|_vtH!59*90_2p|C$Uh57j>;4+Y#4!x(=;=0D<sAHs(5-FkL$6q73pTLFthhyzO>I|*k2gl1O&61Floijr9klz(
GeEQR*DEwpy*Q)SRv4f@Z>`Rldqyiwdx~EiBUP<N*=a1Zl#c#3mJPfBRbq9Qa(JZ#<Qttj@_$wHSjuHpy!?vC9KXauLz7nQ28y+m
_El+W(a@TTfuuI+lHMY-(+n{2cLMBw6Jsct#Ib9aeNo(P1>QPXL^|AVhT_X(MnP>JB_X{G3QV*)KUMdy52?iKAfmk#`4)}P*SV^u
rLSAdu-R7ZzH86;GzYY%F<qHIS=>J_f%jX}P(%-K(=NLjbbc2%;#?$?#cd*zWttrF=Ve^a;44Ne73l?abXP;iAwd47qc*Z)pr0V@
U`P<;=vLE4x-IX8_*FAn^Q0+=UOn0zKB?U7r1?m#6OtA4+Q;X9)qEg6Gm)2?wj>2A5XNyA;AsVsZ8^fT>VFllsvnEUS|mNGCLfh^
JeY5rzR{O^a3SsQ5H&-duc0q!K_EcS8~`}`-+5NSBG<9_x?LySs-xPKb>)k6N<44Z{cAeTi*#(R<LS8IXsGvIs3Tbh7V3l?9{g4v
)t6nxmq6End<LCSvQWwGVE-yvswGOb%2?!WztmFK$T*r$NC7lU`mC1rYm+EmS~wx6lV-y;3cXys)~JaDn22Jg-&|Avj8wa9TSE<5
*xLN*n8w5Aq?7b=DW^<LM6of3yvCN|1w?Ai0%`V{@Z^(hk_gkvK^!}kjaqNxrxLuGTdL3`0hH*Y4Cc+qur)B%pVmQ{xe*bijIv~H
wqQ`#2g#_jSOQ17uT-KnJUzKQIzKoa{(SW5*Q3kx|35rD_-%Op>Gumhi@=8x&JWH$4y8Sm-tf1Bi;Gt#C2hyFn{K2}z)geTeb4BQ
vt>G>?Ry0k6k3tT<r!_u8;@yrb6Xf%uJh%aaXOn%DUQyU0`vgV)iVV%$?!=e!)N^eO}raEJ<-Rr*xlX5#kX&!Fd7sLY5kA1cRPni
=a(08UnM{Nz9kH){s2S$zzdPuxpw3_!U#P(@I4tufsf~*BW(|9p+^ZHh`B-JhDakVPZ&K<26kk79xw@aw(SOP=tZd4lb#j&L4ahA
pGe1Z>@bji6yY`stiW>p&_Qo#AB47TM`7R)Mc=Xm8G51ZxOgZ-$Mf94@*HnaW^T-UP&02M4Moc7SPrq|*kCFQBV?+?2NGDMpwbR)
FG2&~b0RnL1IJSgBS-Z;peo(T2(>IEsx~o#axV<QiI1-A(29`PI+lfK&V584(p)Q~9w8GC>9A!>AIY`Rb1g^=q%A+<%8rd5X|R5K
2w^>hUg$bt6B&5mGkwRB(v2W@bb#F1MNg2jk3_<7T;eLSqL4)Eg5l7OEQh5RL2wc|wzR03j~Rf37y`%~ECtf@NkiZfnSUT1$B~Yt
q1s_+L-|2~$YMZR7`YW%RzxJBIrQs6gKmR;&~O^;2e$3|(uJ%^FD_^!t+#0&02R723VmoBdB5RCn0jD5tX<4FU?mtj#w<g~kM#j1
`Mza^cIeXs=)}kD!?V3maT8cjQsBB&&%uybYj{L9>${j;ko`&5w|w-9!MC|~8(d3Edae)M(4+|RiYyzZ9eE^lNLBjinbeG)VDvUR
c1f_IL%MaP1R=~~Q0_ocAPP@$AVdekfOufgJ|<5Tt-*H~I*|j(+N4m+_b~t`fMm$z(Fs)Tv8y-^+>hAs!ZzbUQ{3<v35|pjrM=K`
VGG<ThUAcjLq7~cNuvO12U9!WXWI`k8b7qSkq3Ww;G|@+7^fp$*eTk$Vdz_U5V%axc6=$x9jPlj@L(j+uFpN&aAzO&p<r?ZmnL^`
R@-T?j(S$ZS3USWEDYKqbA{Q$Ssck=5_*nL4i*Ix<Mk|9uIqY|Q6Y*v*oQ;*-}8uw1!o}^B(zTCB#jUl;5i@}vg-o`TnxnGu7EEt
Bm-qT%4abzhWJUVJP>pT7Ypq+=dx)n07vu&5>y1M4bj#jDfe8=buIFKSTv~@90AcBaxO?ak`X#(WQZIeMyAFD5nBKSNDxMV+B8A7
Fkl)X7{L$$gv6=~MOhxy$gE0$7vLvEiLyBl5Cw0x+ML@h&S7sh?A2l`uza$EK(bh1u)xB=3789)5XiC_F~ARu3>pcTS&R^TNRJ!g
nd4##FWDw|6fU_#&jBtn!)(}*;}O0F5nGaj0lMUD%y<AC11FK?w;6B1igcmo5DiFPp+h!E{V1RdfT(^*0ONWV)r3IU(Hxkh@47CV
Ke|S6BBv)fAkz(86`cUbFnfB`v&k9Y7liGI4z@((^VO&WHg3jDNxl={nRMG6w;%;>4KRgcSsW~3wZt_E-U;F4U=q#+Y7xv7Vap@f
h8qAyV2=#;0DoA0L<ox*03!pCGtV+`p(TvK;;0gm8v^;!k0g9zSml5N^9L$gHi_M)l^YM;L{XdTu<4XgbSPn#q$iKO1Uv>F!7^k6
@;2asOoIF?gaeaJNEwm&yAHQPd`E$_NbwQC4XpYqVSwF%Pq-)~MFWDdkgfFs4<Qv$=TS9?DDY5E(oiu-LeZcp=dk6BU=Rk4>I7I&
W<-71>@NVQD2R}4cnlT<UI7I#hIosEPsHg8^kP%YRY>N9lw?Fo?ckPzp-XLiAP0=VAsCnByD(he;)H>85!&S5R4)R)!!x2NY_sjQ
;-pKkfKcU;0A0F<c~DT0V8%h%hv$b5xhdH$MG1m31RReP$>9gM24<0Iv2+m}T>w5u8Q2#HSW0uS6B}`o!X`8b=3ImXiwqgxAOX}Q
AF(OXa4fiX)aKi3@Es8xNhD#CsX+_@+`ywz0Er-Kh|(pkq8QK)6Jn$A!-!TPJu(+s0CY&&<oqCkSOcjBWby=IoKmr2gH_6|Jkq62
0m7viM*as&gEJzg6C41#;lVJ2HrIZWYakXR3Mo@6>A5aJC-MzSI+3CvIYqw|>xmRHfxu^I@hDY92IR8$SfqX$0Du#C0C4nFbVs;G
E)tT#_!h}Ca2O8*XavbJibz=$XuyL{17(v(fQFs4nQq2*q_PeT&SGgGW%dxw0ej@xv^Hy#RY2a54nPKG0xw_?v(RZkk(&(xsYd{w
7&u@o5hv0Xi4>>};N`ToN23N(2Al>W4u=u^TykRB3+U2?<1k_Zlwc*mKi6*OC6tjOUm@k|73hI52w*%)n>@}i%Lk0<FnHIC0)i?V
LX(tLlN6nh$OmK@DzL%Lfc!)W1^_>{BwGPxM*(XD)`hg5)~Y!!LJlxOi;@ReJ%R$Dins$H*wDU5ibv*vN;HQd+yoRL5+W`0x5k7-
*^`??q7(zr<h!j0p~`SPn)|fJidcl;h^X#UT4hnJCIq2yFA-WI0I17B3zBxo{Kz>Fp9x???ga^_1>pufl|gWh;Hb9Bd!RUi4|04c
36j9@DZazKkvhSLII)2d0GQcc;0WjvI&nBB9&~<=F{S=2ie>k+Y3>^%bsR)3SrqAVnhVT3dEtU5k7})gACxQFMPntKA8hUXuJjV$
S|47^#GP2F9XM{#n&H#3z;Sm~Z!B)qjrA_KUYbx<ce+2*nn^a;`K*pB_W1se?s+ZcJH)<s9wm>rXy0j?+4pF1!)IC(UGt8Gv>V%>
Bt%7eajO;sX`}nu?9t_;puIX%Z&lI*wZ2>LkgF9}MPRj9q{}#e{oHp3_z37jwzu19HD__FmveUX_6cc#+rI5lxnou9JpW~!r=#0+
bk8UI%VktPq)+E<v*OuE3Vx<u52!Xp4SqRbo{e`mHCXI?(;NNY%3(}b0z5%~8;ola+$dhy0IM@H*{J9$V^g-sZ!Zi-^Yr>U8)fJ`
kDtY3{3xI>v30USpQh8R?CP9dytoxgg8W%;1n@>HA5wyaMb!!w7x!PaiM$##4rZ5);AP}BSJ@asi~HSW{}nU+YS6dnPqYil4Vq;|
qrWGE!GN|^=8x$({=?eq4}`r(r~8Awz9;;F2=~zRPqp15=4`mSdU+6_b*w=zSF6J_X}wHcuGppZ>U>(B0p^jz{_afPsi8fCa!?rL
{JxZzVi_D)qoREYTfnkZD9|8iif%w_$|?+$g@X+;;WinCzD+8=(8yaChO}s}P`4(n_Drv{8DwI-o6jd{GBd_mez%&bcS%-xI%dZu
lb%d^%k(;3rn6D1URl{?0jK#WS)>7<0iiW<z12@I6&3U4bNmN!$$aUWiXD9vqlCZNbN3G=%?;2PRRjL>ZCp{^Fe}KH*5|inwe1M7
D!A3(RSEvS3S9E7)hTYX(S6Jg$eYdaXWr->7RwAsNd=e3f)3+lbWmGuT@`AFOmFDNdh@K)aKb#M4KR9#YB)_m>S;*puQ9@Pvbvdq
fpn}(JfW~=xSmf|(=`5F(b0t^?!-4`HSWJE&tttY)O=VT+~nONp~1Ml$2C;zuz3uyf=-9LlCM{Xg<7w#s_=rcs6eZHohoMe3YgWf
GAklKnyhlzUi^y0X{dmh5bPv*Va#W#F~2rwA3EfhwsLefDkjgyica%fp@n|$YBZmM3ASPq<14dVux`H>r<bqw>v1v~9-kbYzP}g(
q=pxl=O>4k!^2N!mj{QJ7mZcxONRgQHM1ib82K$MTY!tvEd@y0CVVtXweuKQw&lxbovS2I;lDkHT|<hV!+Rr^+Hs*%0Q5EJfDCW$
KbhjV`%E9-^i~GP3#ul~<{>yD%+2~C!RKpw9Z9&zSagxBiuBg)=j~%9sA_i7rv)#=$9lg<?*q}br+0m5PbkuRJG`^hh%9_&Ak=3D
LOwI#>W!|D8}VisUso8XUS^2Po>^@520y}0z<ZituiVze<sp4EH#Kpq4<?s%e~)9wV`?`s<sCg2Nb6f9O<Kg4e#qB!V1QupBD<L;
@sxJu(UCekdxN-J?*i4w;JB{PZ#<diPumCL{(3K)nAN-4FK#7QgHc<_$7;*0{Wed1M(d@0rE+6e?_-N<|GK<ln(aG0rSJl{0lr|)
Z(H>itJ;2U9+@h)pPOY@b;pz)Ojq^JSe3KYyJIvq{qoEGR<0QlFRX5O-YLD*h=ht>yzDKODY{tGc?;!glxZo+83h{W^djSK=iBC?
GnE&t1t%%gQNIgiu?_UdGhm&#_moYjTf2O0nlI!}^juZv%Iws~<lL^l_vxN*^}*I}jYDGD8Y5(0nj7hABc9%auo~}LX>Dz6*MHmC
t?$#xCZxLe$PW`WdLD~SU$)}KRy(647q8RENVyFir6^Au^tq(mN#rwAgF%zi`<;iZZ&!z9@5Mt_=Ca%rEdeL9@nQ}qW$>X@X?Rmv
h5$gCs^?SeKFoDlrP};u?Z*A&b+NP7Z>6jonKRIFzmeSQ`ldd{r%t-xh*Bc>C>oo)<=ce1QCp@Xra;GuR#%w0j2e>`IO(8$P%jmu
=kkc&e(QJ>J3EUuO#yX;Y-*Z@%$|;GjK>JZA}Ly@G)B*@so&#c9RIHH>_#iQR}7TC@@@rLz^ogZM=(Zp)GJwi*;D5mH2>;!!`7te
wmfa}Kqs>3#isIL5pN+sl&3=<+J5|5PrVQ{lAYU3>*uyI2L;-<W_`+P9LM9aI=47NBYNX^M5jM^P{j`05ANS^OF9Pf-M#az;`;bw
l?5>tY4y^imtx|Y&eWFBbp2gux{l+_tk~#{`pF9ia0i=j098H5*EB4Cd<ub%X$s!ey2wFG@N@H}(QS594)`>Akx=q)6GBpz$LgTN
PPG4vezk;31$~(Ny!P=xi5)&ob933^R899w|8I4=RoQxbs#Xc~@tW;(S$C}xiV8o(cQ1De6`s;MMpjW1ci%r-XTQWv@>T(JEu3+y
7Msknfd!|8uMQ+t;^Qeio?h|dcSj(lo@}4QNV;6<)Wly|ts&yENxfGm%T6ok<=da>*vIC<j`2WsS)p+S)nhWG7EZUDDh&#4H;qFf
Y<@504<M#qCU(ph*ho}oZj;o_O}pD|2_`JUp1Y%<2q;x!(L;GSXC3zmbSen=n=><f{AS&XTkG|voLVEuNhuWRlrs7+Gb7gPa`ERt
E$XQ05zRglwOYp$FJn5Vd6_<JtZy*4E+~;L=E!aDQ{z;v|2*8p-|21Nm_8FmH^ljHquBmHuT6nz{QV*t_VWOY*Y^)M%3)1`;VYLt
H%qToqxb;2(_})leyMA5gxILrJoobfQc@SHIf;408bDClNkn!o>Wa$Xf1wEnwfNXPr~W;>p05*{K95q$!V^0Fr$?xQgNC?$enX|M
Tt!-SR;ezJV|x>r!Lg!?;MNRmImZ}|dCj-#N3A!-*QNRtBiqKy1I_f%Usl_?(%O1UY0O!z4nfYk^>Qf>@?%yV3q#Y784c%+)8Krp
26LLw8$YFozYqhM<8nC>RLfU7KkB1)AJw}j<!dKxjNg3k<S$}P?X4f<ScyeR=>sLu4f#x;D*;WPwS-!z!fY{&vAF&*bB_5^;4ba-
9BjPwQwFV<=G*UTF%N7w{rkUTh7P9QV>V;%+}xnXYrebUyW}6e&{G}bF1Gmj@I$P<j_u(z`5`{tND`~udn-|)r1pBmKafJ7rf$I#
pwRk$1DhMz)IgUwT;jAyNc&|HE#cXv@ND{fQFuH6+qboj(n+4~Rl|=rh9AeL8n`cbk;s^)v^bNEfYGa*CXKY3#6J);GJcKE;uD44
42G?RdM^3l#W+Ytptn8V>TQqzD6Jt}`ATUVN%JdAM9`gSzO^>3Lt0zrK}B@J{|A^<^(zA-mEP5$`|@l2$eiN-wR#mo=vNfB-cl>y
^QY(4d;av6K}9Bw+l=oUMY4)})v!|Y4PB?A@%rh4XJ!1jkJ`;#A_ax_ak*#pGv#`B^`6yE1J);TcjK}7=KcOv8kaj>jp9v1wBDlI
x8(_NJ@dIr8}EMUii?<8?I)8alPYM4{#CkBde{5`f=U-9%F<7|2y`rxiMUF&XKzl4TRS|9WSPKT(`8(UYRxnrHJ6vw8uUYBlSeP@
9)9{YzNuD$iIE|#p`h~kyGz5PEh-xe#6^4YSwD!+>u#z*t`^ER>76Fit8o&aCZb-itqPlEs$&*Sj=9tpp%3wgveS?8N1=d#O4XIv
T({QuHJyupeW167q$OlvirR6iE3;ZbK9a%k_~h%+`{BXi<-ZP2hrb?NTr|%(2SeN9bI)g==qK8~oS@Fh+2zss7hLF7<Z?AyQ~31j
(b?t2@XN*U_~7Hw@buu<ckd5KX~SPn&i-{Vl*3P7j?RY!-X(=p25R2{v)Ex}0_B3@#vX%O<E{1xs7YgQK%HVoS-FM5&l@&Ut+s9%
39rCzZ(VGyWb#fyx%SB?ylIjD8!UfP4AnZ7S}aog4W*?I%imMet5~If40yeActBes>gtg8Li9jz&p*?~?8h<?8%4uv7bUi>iYBDA
;eBRDT_`!1o4oO>|L7O^UR6V+_i0}J)i2|<st)tp#P<C7)qnakd73KkTtzW|2{I=9FRCA=8y-t*xLD5DkkK*yz@2!!g>ekY_>1R7
nh(>b(PTBoW6SIyQH#6uOL4p7)pU_}^{dlLdZwWL)giBcT`pIt$WziUozRcFuLS<vdu5uhU;X#&mAR{1njQKry6&si&k0fosPahL
F2k$mBF$+cUHQ`a(Qlv5FJJL1WmGQoPuT4$!ExE{ZTd9M;0p!)kW9WD#oW&j#(}{N&0Wmu#+o)J7>e-4r+=Lv9x1|TvPGE6+Jtq(
(oU2~w9J7FM1csS$I(|HLFw853w~gNj{
"""
s=zlib.decompress(base64.b85decode(''.join(DATA.split()).encode('ascii')))
assert len(s)==20964
assert hashlib.sha256(s).hexdigest()=='0866d3fa7d44adc3d57558ba295c0524c21a883d2e8bd5fad122ed2ba2f4874e'
Path('finch22_core.py').write_bytes(s)
subprocess.run([sys.executable,'-S','finch22_core.py'],check=True)
b=Path('finch22_core.json').read_bytes()
assert len(b)==164934
assert hashlib.sha256(b).hexdigest()=='ac56328643e1b00a87e94956aa2c6920a3a1aaf39c5e36d3327fd6c41032083c'
print('FINCH22_CORE_SELF_CONTAINED_RECOVERY_PASS')
```

Ожидаемые содержательные маркеры:


[Encoded source block omitted; the code in this passage is incomplete.]

## 7. Что добавлено, что не доказано и наиболее полезное продолжение

Первоначальная попытка фиксировать Q и независимо решать отдельные строки была заменена одной контактной квадратурой на настоящем теле. Перевод начала оказался не новым нелинейным поиском: его допустимые значения — один полигональный core K(P), а все механические стрелки после очистки положительных знаменателей аффинны по тому же началу. Девятнадцать outward-полей использовали именно это пересечение общей плотностной релаксации с механикой и исключили весь reference-domain, а не рациональную точку.

Затем была проверена более сильная гипотеза: достаточно ли сохранить настоящие массы на настоящих гранях? Контроль E17 отвечает отрицательно даже с cap<1, rank-four спектром и одним rank-three Gram. Геометрически причина — общий перенос площадных средних вдоль пояса граней; аналитически это rank-one исправление центроидного дефекта. Полные настоящие вторые моменты выявляют ошибку и оставляют ровно физическую центровку. Поэтому formal H и выбранные c_i не повышены до actual moments.

Универсальная размерность K(P) доказывает, что эта ложная центровочная свобода не является исключительной особенностью неудачного rational sample: у любого непирамидального тела она трёхмерна. Но это не означает, что внутри неё существует S1 или 110. Наш сектор THICK9 демонстрирует обратное: геометрически допустимые общие completion имеют не менее двух стабильных граней.

**Границы результата:** новые whole-E17/TREE253 исключения — 0; F>=10 не доказано; гёмбёц не построен. Сектор Ω не охватывает все SPD-метрики или все реализации своего типа. Ни P0(I+Lambda), ни long-cycle product<=1, ни тождество Sigma=metric не использованы. Старые отрицательные контроли independent rows и TREE253 остаются в своих прежних областях действия. Никакого конфликта с литеральными данными parent не выявлено. Доказательства и точные исполнения не заменяют внешнего рецензирования или proof-assistant проверки.

Наиболее полезное продолжение — строить K(P) для оставшихся **настоящих E17** геометрических секторов и искать конечные общие outward-поля для их аффинных reference-arrow систем. Положительные контактные сертификаты допускают проверяемое покрытие переменных Q,N, подобное Ω, без сетки по центру и без независимых apex rows. Там, где такое совместное пересечение непусто, следующий обязательный шаг — действительные C_i,T_i и actual flux: универсальная теорема о dim K=3 и фиксированно-массовый E17-контроль точно показывают, почему одни первые балансы этот шаг не заменяют.

Дополнительные копии проверенных материалов: [полный exact-аудитор](sandbox:/mnt/data/finch22_core.py), [точный отчёт](sandbox:/mnt/data/finch22_core.json), [самодостаточная recovery-капсула](sandbox:/mnt/data/recover_finch22_core.py). Восстановление не зависит от этих ссылок: полный источник закодирован выше.
