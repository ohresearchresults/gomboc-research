# minimum-0084

AI research report · 2026-09-18 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# JOINT_QUADRIVALENT_CLOSING_EDGE_V1

**Steady Lynx 90 — minimum-0084.** Получено новое совместное препятствие для настоящего ребра, противопоставленного трёхстрелочному пути полюсов у четырёхвалентной неустойчивой вершины. Оно использует одну геометрию и строго взаимно обратные метрики. Доказаны две точные оптимальные локальные константы, из них выведены исключения замкнутых непрерывных поддоменов настоящего среза (10,17,9). Построен и точно проверен отдельный однородный собственноцентрированный отрицательный контроль того же f-вектора с (S,U,H)=(2,4,4).

**Основной результат:** если x — строго неустойчивая четырёхвалентная вершина, её четыре настоящих полюса образуют выбранный корневой путь из трёх слабых стрелок, а xy — настоящее ребро, отвечающее пропущенной стороне этого полярного четырёхугольника, то

    K_e (G_xx-G_xy)^2 <= (G_xx J_rr-1)(G_xx G_yy-G_xy^2).            (1)

Здесь G_uv=(u-c)^T M(v-c), J_fg=q_f^T M^(-1)q_g, полюса относятся именно к P-c, r — корень выбранного локального полюсного пути, и

    K_e=2401                         для 0->1->2->3;
    K_e=208+120 sqrt(3)               для 0->1<-2<-3.                (2)

Обе константы оптимальны для локальной задачи и достигаются, в том числе на допустимых слабых стенках. Это не утверждение об их достижимости телом joint110. Оценки не требуют H=0: исключается более широкий необходимый совместный класс, поэтому дополнительные слабые контактные страты целевой задачи не теряются.

Для настоящего joint110 с выбранным полюсным деревом TREE253 следуют строгие ограничения

    G_yy/G_xx >2401/2805              в направленном случае;
    G_yy/G_xx >K_e/(K_e+404)>415/819  во внутренне-корневом случае.  (3)

Следовательно, противоположные ЗАМКНУТЫЕ полосы, включая равенства, исключены. Ни одного полного комбинаторного типа или целого исторического регистра здесь не закрыто. C>=34 остаётся принятой границей; аттейнер34 и C>=36 не получены. Исходный статус среза зафиксирован в brief.

## 1. Источники, область и что не использовалось

Прикреплённые actual-chart, centered-circuit/rank3 и angular-материалы прочитаны целиком. Используемый локальный переход к настоящему полярному четырёхугольнику дан также в angular-капсуле; там доказана нижняя граница роста касательных радиусов8, но не оценка расстояния до замыкающей прямой, дающая (1).

Полностью прочитан библиотечный result:minimum-0059, cursor0..50000..56906, eof, неизменный SHA-256 181126150bab95649617ee4032b357af29b06e5588f018e9c5cc4afb7dd9b465. Его 670/49 point-pair и48 E17 true-edge формы различаются;716 входит в приведённый остаток48. Его большие численные сертификаты здесь НЕ исполнялись. Этот родитель нужен только для идентификации примера сохраняющейся древесной формы, не для доказательства (1)–(3).

Для метрического шага полностью прочитаны точные theorem-units исторического journal:[internal-source-reference]: «explicit compact metric domain», 2026-09-11T19:50:53.503Z, и «finite escape depth…47», 2026-09-11T20:09:30.816Z. Чтение нужных полных единиц покрыто перекрывающимися интервалами2814500..2851800 при SHA-256 f541795617e5adb8b7308d1fe3969e55a08d46ba5711c809870ed1d2e0860375. Весь исторический журнал не перечитывался. Ниже приведено нужное доказательство заново; новый исходник не зависит от архивных файлов.

Внешне проверена используемая стандартная форма неравенства Бервалда: Langharst–Putterman, arXiv:2210.04438v7, Corollary1.4, HTML-формула. При n=3,p=1,q=2 она даёт E f^2 <=(8/5)(E f)^2. Полное внешнее доказательство статьи не аудировалось.

Обнаружено расхождение служебных счётчиков: angular-капсула содержит старые K3 11743/8739, а текущий brief — LOCAL K3 5611/4090. Ни один из этих счётчиков не использован и не изменён; неизвестное отображение между ними не выдумывалось.

Новая теорема не зависит от девятивершинного broom-доказательства, effective-gap164, независимо выбранных строк Lambda, свободных масс или отдельных метрик. Наличие компактной карты само по себе не трактовалось как infeasibility proof.

## 2. Полное доказательство оптимальной локальной оценки

Пока достаточно произвольного внутреннего начала отсчёта; собственный объёмный COM понадобится только в разделе4. Одновременно переводим вершины и полюса в физические евклидовы координаты:

    X=M^(1/2)(x-c), Q_i=M^(-1/2)q_i,
    R=|X|^2, p=X/R, t_i=Q_i-p.

Из q_i.(x-c)=1 следует t_i perpendicular X. Строгая неустойчивость означает, что p находится строго внутри настоящей полярной грани conv(Q_0,Q_1,Q_2,Q_3). Поэтому t_0,t_1,t_2,t_3 — выпуклый четырёхугольник с0 строго внутри. Все u_i=|t_i|^2=J_ii-1/R положительны. Слабая стрелка точно равносильна

    t_i.t_j >= |t_i|^2.

Пусть alpha,beta,chi — положительные центральные углы трёх выбранных последовательных сторон. Каждый меньше pi/2. Пропущенная сторона имеет центральный угол меньше pi, поэтому

    pi < S=alpha+beta+chi <3pi/2.                                  (4)

Положим H=dist(0,line(t_0,t_3)); в разделах2–3 эта буква обозначает расстояние, не число седловых равновесий. Для длин rho_0,rho_3 концов замыкающей стороны

    H^2 = rho_0^2 rho_3^2 sin^2(S) /
          (rho_0^2+rho_3^2-2rho_0 rho_3 cos(S)).                    (5)

Поскольку cos(S)<0, правая часть строго возрастает по каждой из двух положительных длин при фиксированной другой длине и S.

### 2.1 Направленный путь

При 0->1->2->3 имеем

    s=rho_0/rho_3 <=cos(alpha)cos(beta)cos(chi)
                  <=cos^3(S/3).

В (5), после деления на rho_3^2, функция от s имеет производную того же знака, что 2s(1-s cos S)>0. Поэтому достаточно подставить s=cos^3(S/3). С w=cos^2(S/3), 0<w<1/4, получается

    H^2/u_3 <=w^3(1-4w)^2/(1+w+7w^2) <=1/2401.                   (6)

Последний шаг является точным полиномиальным доказательством:

    1+w+7w^2-2401 w^3(1-4w)^2
      =(7w-1)^2 [1+15w+168w^2-784w^3],

    1+15w+168w^2-784w^3
      =1+8w+7w(1-4w)+196w^2(1-4w)>0.

Равенство возможно при w=1/7, равных трёх углах и трёх нулевых выбранных стрелках. Следовательно, H<=rho_3/49. Это максимизация расстояния замыкающей прямой, а не прежняя минимизация отношения крайних радиусов. Из прежнего роста8 и H<=rho_0 следовало лишь H^2<u_3/64; новая2401 существенно сильнее и связывается именно с настоящим primal-ребром.

### 2.2 Путь с внутренним корнем

При 0->1<-2<-3 нормируем rho_1=1. Тогда

    rho_0<=cos(alpha), rho_3<=cos(beta)cos(chi).

Сохраняя alpha и beta+chi, увеличиваем последнюю верхнюю оценку до cos^2((beta+chi)/2). Монотонность (5) оправдывает это как верхнюю оценку, без утверждения о сохранении глобального тела. Положим t=(beta+chi)/2, x=tan(alpha), y=tan(t). Условие (4) эквивалентно

    y>1, x>2y/(y^2-1).

Полученная верхняя оценка H^2 равна

    F(x,y)=[x(y^2-1)-2y]^2 /
      [(1+x^2)(1+y^2)^2((x+2y)^2+y^4)].

Её производная по x:

    -2(x+y)^3 [x(y^2-1)-2y] [x(y^2-1)-y^3-3y] /
      [(1+x^2)^2(1+y^2)^2(x^2+4xy+y^4+4y^2)^2].

Все знаки на заявленной области определены. Поэтому единственный максимум по x достигается при

    x=y(y^2+3)/(y^2-1).

После этой подстановки, с z=y^2>1,

    F <=G(z)=(z-1)^4/[(z+1)^2(z^2+6z+1)^2],

    G'(z)=-2(z-1)^3(z+3)(z^2-6z-3) /
            [(z+1)^3(z^2+6z+1)^3].

Максимум находится в z*=3+2sqrt(3). Здесь (z*-1)^2=4(z*+1), откуда

    max G=1/(3z*+1)^2=1/(10+6sqrt(3))^2
         =(26-15sqrt(3))/8 =: gamma.                              (7)

Итак H^2<=gamma u_1, или H<=rho_1/(10+6sqrt(3)). Равенство и настоящая выпуклость при этих параметрах проверяются явным точным контролем раздела5. Все четыре положения корня пути покрываются двумя случаями с обращением порядка.

## 3. Переход к настоящему primal-ребру и одной общей метрике

Обозначим через y второй конец настоящего ребра xy=F_0 intersect F_3. Введём

    R=G_xx, A=G_xx-G_xy>0,
    D=G_xx G_yy-G_xy^2>0, a=R J_rr-1>0.

Положительность D следует из того, что два разных конца настоящего ребра не могут лежать на одной прямой с внутренним началом: одинаковая поддерживающая плоскость имеет на них значение1.

В физических координатах положим X=(0,0,sqrt(R)). Из двух уравнений Q_0.Z=Q_3.Z=1 расстояние от0 до прямой настоящего ребра равно

    d_edge^2=R/(1+R H^2).

С другой стороны, для e=Y-X обычная формула проекции даёт

    d_edge^2=D/|e|^2, R|e|^2=D+A^2.

Следовательно, без всякой независимой метрической переменной,

    R H^2=A^2/D.                                                  (8)

Умножение (6) или (7) на R и применение (8) даёт (1). Также

    G_yy/R >=K_e/(K_e+a).                                         (9)

Это оценка любого конца ребра, а не только случая, когда проекция попала в отрезок. Если дополнительно y->x — выбранная слабая primal-стрелка, то

    |y-x|_M^2/R <=a/(K_e+a), G_xy/R >=K_e/(K_e+a).                 (10)

Для (10) положим L=|y-x|_M^2. Из G_xy>=G_yy следует L<=A и A<=R-G_yy; теперь используется (9).

### Полиномиальные формы для общей realization-модели

Направленная ветвь добавляет непосредственно

    (G_xx J_rr-1)(G_xx G_yy-G_xy^2)-2401(G_xx-G_xy)^2 >=0.

Для внутреннего корня можно не вводить sqrt(3). При A,D,a выше положим L=aD-208A^2. Точный эквивалент:

    L>0, L^2-43200 A^4>=0.                                       (11)

Знаковую охрану нельзя удалять. Более слабая полностью рациональная отсечка — 415A^2<aD, поскольку 208+120sqrt(3)>415 и A>0. Все G,J в этих формулах должны происходить из одной действительной реализации и одного центра.

В прикреплённой cubic-модели J_fg=u_f^T K u_g имеет степень3. Поэтому направленная добавка имеет степень не выше6, две inward-охраны — не выше6 и12; новых переменных не требуется. Это подсчёт степеней явно заданных полиномов, не выполненный новый feasibility-run. Точный исходник родителя cubic_realization.py:9961байт, SHA-256 5fa5ba4f10c4292369bff1e9fd8fa1d8c50c817dda4ef007f27857119cfeb01b.

Есть и прямой рецепт для33-variable actual-chart C34_MAXSIMPLEX_CHART_V3, исходник13414байт, SHA-256 adfad4ef7fcb861be74bf54af641ade397e56018ad4189631548e768acd8d7ef. С его T,U,M,нормалью n_r и обратным support-скаляром r_r положим

    W_v=4T v-U,
    Rb=W_x^T M W_x, Nb=W_y^T M W_y, Cb=W_x^T M W_y,
    Ab=Rb-Cb, Db=Rb Nb-Cb^2,
    Qb=n_r^T adj(M)n_r, d=det(M)>0.

Тогда направленное ограничение в точности эквивалентно целочисленному

    (r_r^2 Rb Qb-d) Db-2401 d Ab^2>=0.                            (11a)

Для inward положим Lb=(r_r^2 Rb Qb-d)Db-208d Ab^2 и добавим Lb>0, Lb^2-43200d^2 Ab^4>=0. Это та же обратная матрица через adj(M)/det(M), не отдельно выбранная метрика. Без сокращений степени W,Rb,Qb,Db не выше4,9,6,18: (11a) имеет степень не выше35, квадрат inward —70. Поэтому старые degree12/height64/JPT164-параметры после такого добавления автоматически НЕ сохраняются. В настоящем ходе новые chart-файлы не генерировались; точный рецепт (11a) сохранён для продолжения.

## 4. Почему метрические числа не являются произвольным condition cutoff

Ниже достаточно actual V<=10,F<=9 и двух выбранных слабых корневых деревьев высот h,k. Строгий единственный U и S дают такие настоящие деревья: каждая вершина, не являющаяся строгим максимумом, имеет слабый выход по настоящему ребру; на выходе квадрат нормы строго увеличивается. Полярная сторона использует то же начало и обратную метрику. Корень любого такого дерева сам строгий максимум, включая случаи нулевых выбранных производных.

Пусть Sigma — НАСТОЯЩАЯ объёмная ковариация. В калибровке Sigma=I справедливо

    sqrt(5/3) B subset P subset sqrt(15) B.                       (12)

Для внутреннего включения возьмём поддержку h-u.x>=0, |u|=1. Её среднее h, второй момент h^2+1; неравенство Бервалда из раздела1 даёт h^2>=5/3. Для внешнего включения используем настоящий объёмный веер из вершины v. При проекциях четырёх вершин ячейки b,z1,z2,z3 и s=z1+z2+z3 действительные нормированные объёмные веса дают E s=-b и

    20 E_P[(u.x)^2]=E_cells[b^2+z1^2+z2^2+z3^2+(b+s)^2]
                   >=(4/3)b^2.

Отсюда b^2<=15. Это не свободные массы: все ячейки интегрируют одно P. Выбранные нулевые ячейки имеют нулевой вес; диагонали интеграционной триангуляции не становятся механическими рёбрами. Полярность (12) даёт отношение внешнего/внутреннего радиуса не более3 также для настоящего P*.

Нужная конечноглубинная лемма: если rB subset conv(X) subset RB, A>0 и X имеет слабое A-дерево высоты h, то для двух старших собственных значений

    lambda_1/lambda_2 <=(R/r)^2 c(h),
    c(h)=cos^(2(h+1))(pi/(2(h+1))).                               (13)

Доказательство. Выбираем старшую ось e так, чтобы корень имел неотрицательную проекцию, начинаем с точки с e.x<=-r и идём до первого перехода y->z из отрицательной полуплоскости в неотрицательную. Пусть перед y было m стрелок, L=m+1<=h, phi — угол между -e и A^(1/2)y. Слабые стрелки дают для каждой пары норму ребёнка не больше нормы родителя, умноженной на косинус угла. Сферическое треугольное неравенство и вогнутость log cos поэтому дают

    sqrt(lambda_1)r <=|A^(1/2)y| cos^L(phi/L).

На переходе вклад старшей оси в скалярное произведение неположителен. Поперечная компонента A^(1/2)z имеет норму не более sqrt(lambda_2)R. Следовательно

    |A^(1/2)y| <=sqrt(lambda_2)R sin(phi).

Максимум sin(phi)cos^L(phi/L) равен cos^(L+1)(pi/(2(L+1))). Эта величина возрастает с L; (13) доказано. Нулевые стрелки, равные собственные значения и любое конечное SPD-искажение включены.

Применяем (13) к вершинам для M и к полюсам для M^(-1). В исходных координатах инвариантное следствие:

    kappa(Sigma^(1/2) M Sigma^(1/2)) <=81 c(h)c(k).

Для ЛЮБОЙ пары действительных вершины и полюса из (12) также следует

    G_xx J_rr <=9 kappa <=729 c(h)c(k).                           (14)

Таким образом (1),(9) имеют полностью общую точную высотную форму с a<=729c(h)c(k)-1. Рациональные безопасные строгие оценки, точно проверенные капсулой:

    (h,k)=(9,8): kappa<49;
    (h,k)=(9,6): kappa<45;
    (h,k)=(8,6): kappa<44.

Для их элементарного сертификата используем pi>25/8, log cos t<-t^2/2 и первые пять членов exp. С x=(625/256)(1/(h+1)+1/(k+1)) проверяется sum_(j=0..4)x^j/j! >81/cap. Нижняя оценка pi проверена через вписанный24-угольник: u=2-(25/96)^2>0, v=u^2-2>0, v^2>3. Все сравнения рациональны.

Отсюда при одних только численностях10/9 исключены закрытые полосы

    G_yy/G_xx <=2401/2841          (направленный путь),
    G_yy/G_xx <=83/171            (внутренний корень).

Для TREE253 высота полюсного дерева6, поэтому получаем более сильные (3). Его буквальные четырёхвершинные блоки направленного типа:3456,2345,1234,0123; r равен соответственно3,2,1,0. В блоке0127 пропущенное ребро — F_2 intersect F_7, в блоке0178 — F_1 intersect F_8, в обоих r=0. Эти приложения требуют реальной указанной циклической инцидентности и выбранных стрелок, но НЕ требуют, чтобы глобальный FULL граф не содержал никаких иных стрелок.

### Один полностью идентифицированный E17 поддомен

Нативные максимальные грани ROOF8_3_5:

    F0=[0,1,2,3,4,5,6,7], F1=[0,1,8], F2=[1,2,8],
    F3=[3,4,9], F4=[4,5,9], F5=[5,6,9], F6=[6,7,9],
    F7=[2,3,9,8], F8=[7,0,8,9].

Корень U — нативная вершина8. Слабые primal-родители, в порядке нативных вершин0..9:

    pv=(8,2,3,4,5,6,7,0,8,3).

Полюсные родители в БУКВАЛЬНЫХ TREE253-метках:

    pq=(0,0,1,2,3,4,5,0,7).

Отображение literal facet0..8 -> native face:

    (5,6,8,7,2,1,0,4,3).

Соответствующий нативный dual Hamilton path:

    (0,1,2,7,8,6,5,4,3).

У вершины8 путь нативных полюсов F1->F2->F7->F8 является цепью literal5->4->3->2. Пропущенное настоящее ребро — (8,0). Нативный primal-preorder

    (8,0,7,6,5,4,3,2,1,9)

даёт родителей (0,0,1,2,3,4,5,6,7,6), то есть rooted-tree716 при точном BCU-порядке; высота8. Эта идентификация заново вычислена полным генератором719 кодов. Число716 НЕ является номером полиэдрального типа, native-строки или LOCAL/FULL-позиции.

Поэтому на ВСЕЙ действительной реализации этого конкретного совместного домена

    G00/G88 >2401/2796 >6/7,
    |x0-x8|_M^2/G88 <395/2796,
    2401(G88-G80)^2 <395(G88 G00-G80^2).                           (15)

В частности, противоположная закрытая полоса G00/G88<=2401/2796 исключена с произвольной взаимно обратной SPD-метрикой. Истинность самой face-lattice подтверждает рациональное тело с вершинами

    (-2,-1,0),(-3,0,0),(-2,1,0),(2,1,0),(3,1/2,0),
    (7/2,0,0),(3,-1/2,0),(2,-1,0),(-1,0,1),(1,0,1).

Этот последний список — контроль инциденций, не свидетельство механики pv,pq. Не проверялось, какие более поздние FULL/LOCAL сертификаты уже покрывают части этого домена; нового целочисленного списания не заявлено.

## 5. Точные локальные случаи равенства и настоящий отрицательный контроль

### Рациональная локальная острота K_e=2401

Все следующие данные РАЦИОНАЛЬНЫ в одной взаимно обратной метрике:

    x=(0,0,1), M=diag(1,6,1), N=diag(1,1/6,1),
    q0=(1,0,1), q1=(1,6,1), q2=(-5,12,1), q3=(-17,-18,1),
    y=(1/8,-1/8,7/8).

Физические касательные координаты полюсов равны

    (1,0),(1,sqrt(6)),(-5,2sqrt(6)),(-17,-3sqrt(6)).

Их положительные веса (63,3,3,3) дают нулевую сумму; выбранные три стрелки нулевые, все остальные различнополюсные стрелки отрицательны. Касательные квадраты норм — (1,7,49,343), H^2=1/7, J33=344. Точка y — точная проекция начала на замыкающую edge-line:

    Gyy=Gxy=7/8=2401/(2400+344), A=1/8, D=7/64.

Равенство в (1) действительно достигается, и y->x — слабая нулевая primal-стрелка. Это локальный нормальный конус, НЕ замкнутое тело с COM0.

### Острота внутреннего случая

Положим z=3+2sqrt(3), M=diag(1,z,1), N=M^(-1), x=(0,0,1). Зададим пары (A_i,B_i):

    (1/(1+3z), -sqrt(3)/(1+3z)),
    (1,0),
    (1/(1+z), 1/(1+z)),
    ((1-z)/(1+z)^2, 2/(1+z)^2).

Настоящие локальные полюса q_i=(A_i,z B_i,1); физические касательные векторы равны (A_i,sqrt(z)B_i). Все данные полюсов и метрики лежат в Q(sqrt(3)); независимая вторая метрика не вводится. Точный аудит знаков в этом упорядоченном поле проверяет строгую выпуклость, строго внутренний0 и ровно стрелки 0->1,2->1,3->2, все нулевые. Получается H^2=gamma и u1=1. Следовательно, вторая константа тоже оптимальна и достигается локально.

### Действительное однородное тело V10/E17/F9

Отдельный контроль построен не из подогнанных моментов, а из настоящих полупространств. Пусть z_j=(101/100+2*sqrt(-1))^j, j=0,1,2,3. Берём четыре исходных плоскости (Re z_j,Im z_j,1).X<=1 и пятую (306/25,-247/100,-3).X<=1. Два противоположных простых базовых угла, с тройками плоскостей (0,1,4) и (2,3,4), отсекаются суммами их нормалей с правой частью 3-epsilon, epsilon=1/100.

После этих двух усечений имеются9 вершин. Над первой новой треугольной гранью ставится десятая вершина

    v_new=centroid_of_three_cut_vertices
          +epsilon^3 n_cut/(n_cut.n_cut).

Она лежит строго снаружи только этой грани; это проверяется рационально. После convex hull вычисляется настоящий объёмный центроид c. Все окончательные вершины переводятся на -c; M=N=I. Никакого изменения плотности нет.

В лексикографической нумерации окончательных десяти вершин точные максимальные циклы:

    [0,2,1], [0,1,4,3], [0,3,5,2], [1,2,5,6,8,4],
    [3,4,8,9], [3,9,6,5], [6,7,8], [6,9,7], [7,9,8].

Получено точно:

    stable facets=[1,3],
    unstable vertices=[2,3,4,5],
    saddle edges=[(1,4),(2,5),(3,4),(5,6)].

Все проверяемые истинно-рёберные primal и dual производные ненулевые; также нет равенств J_ij=J_ii для разных граней. Нативная вершина3 строго неустойчива и четырёхвалентна. Её настоящая локальная полюсная цепь — [4,5,2,1], все три стрелки строго положительны; пропущенное ребро (3,4). Проверены (1), (8), (9) строго там, где это ожидается. Это ДРУГАЯ нумерация и другое тело, не ROOF8_3_5 из (15).

Механические тесты используют только настоящие грани/рёбра и общие G,J, как в прикреплённой rank3-капсуле. Таким образом, локальная трёхстрелочная цепь у четырёхвалентной U-вершины действительно совместима с собственным объёмным COM и f=(10,17,9); сама по себе она не даёт глобального запрета. Контроль НЕ удовлетворяет S1/U1/H0 и не повышает верхнюю границу задачи.

## 6. Вычислительный статус и дальнейшая работа

Основные оценки (1)–(15) доказаны выше аналитически. Вычисления точно проверяют необходимые полиномиальные тождества, два случая остроты, знаки в Q(sqrt(3)), рациональные оценки49/45/44, действительные maximal facets, edges, объём, COM и все равновесия нового отрицательного контроля. Конечный rooted-code подсчёт используется только для literal716. Это не quantifier elimination всей realization-системы и не новая большая SDP-перепись. Внешняя историческая новизна и независимая экспертная верификация новых доказательств не установлены.

Наиболее полезное продолжение — внести (1) и охраняемую (11), а не только скалярную (3), в общую actual-coordinate или centered-rank3 модель четырёхвалентных U-корней. Сначала имеет смысл атаковать остаток literal716 после (15), одновременно сохраняя его настоящий COM, все поддержки, выбранные обе системы стрелок и H=0. Для inward-блоков существенно использовать точную константу208+120sqrt(3), а не ограничиваться прежними двумя отношениями сырых полюсных норм. Автоматической невозможности остальных полос не доказано; не исследованы аналогичные оптимальные замыкающие оценки для пяти- и более валентных корней.

## 7. Полная recovery-капсула

Сохранить следующий полный блок как joint_closing_edge.py, ASCII/UTF-8, LF, последний LF. Никаких внешних исходников, данных, RNG, solver, numpy или sympy не требуется. Все начальные плоскости, параметры усечений/стекования, field conventions, face/vertex maps и точные проверки находятся внутри.

Наблюдённая среда: CPython3.13.5, стандартная библиотека, assertions enabled. Команды:

    python -S joint_closing_edge.py build
    python -S joint_closing_edge.py check

Обе команды прошли, затем единственный исходник был скопирован в пустой отдельный каталог; build/check прошли повторно, JSON совпал побайтно. Это cold replay того же кода, не независимая реализация проверяющего.

Pins окончательной версии:

    joint_closing_edge.py: 14725 bytes,
    SHA256 d5d9f1904d70ed0f1ab99f6dc2cbde83c9c24779a5345d7428f16c8805df4c8d;
    joint_closing_edge.json: 22005 bytes,
    SHA256 baf940d79db6cbc66b89e4c76c369a06ff6b83f5a1e3aa4f2277b3a02bd6413f.

Ожидаемые terminal markers:

    JOINT_CLOSING_EDGE_2401_AND_INWARD_SHARP_PASS
    ACTUAL_10_17_9_OWN_COM_S2_U4_H4_PASS
    JOINT_CLOSING_EDGE_RECOVERY_PASS 22005 baf940d79db6cbc66b89e4c76c369a06ff6b83f5a1e3aa4f2277b3a02bd6413f

Выход содержит все точные координаты, COM, полюса и массивы контроля; долговременным источником является полный детерминированный генератор ниже, а не сам файл/хеш.

```python
"""JOINT_QUADRIVALENT_CLOSING_EDGE_V1. CPython 3.13.5, standard library.
python -S joint_closing_edge.py build
python -S joint_closing_edge.py check
Exact controls and polynomial identities; universal proofs are in the handoff.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial
from functools import lru_cache
from pathlib import Path
import hashlib,json,sys
assert __debug__

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,k):return tuple(x*k for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def solve(A,b):
 d=det(*A)
 if not d:return None
 return tuple(det(*(tuple(b[i] if j==k else A[i][j] for j in range(3)) for i in range(3)))/d for k in range(3))
def halfvertices(H):
 P=set()
 for ids in combinations(range(len(H)),3):
  x=solve([H[i][0] for i in ids],[H[i][1] for i in ids])
  if x is not None and all(dot(n,x)<=b for n,b in H):P.add(x)
 return sorted(P)
def hull(P):
 fs={}
 for a,b,c in combinations(range(len(P)),3):
  n=cross(sub(P[b],P[a]),sub(P[c],P[a]));h=dot(n,P[a])
  if not any(n):continue
  sl=[h-dot(n,x) for x in P]
  if min(sl)<0<max(sl):continue
  if max(sl)==0:n=scale(n,-1);h=-h;sl=[-s for s in sl]
  if not max(sl)>0:continue
  face=tuple(i for i,s in enumerate(sl) if s==0)
  den=abs(next(x for x in n if x));fs[face]=scale(n,1/den)+(h/den,)
 faces=sorted(fs)
 E=[(i,j) for i,j in combinations(range(len(P)),2) if sum(i in f and j in f for f in faces)==2]
 cycles=[]
 for f in faces:
  a=min(f);nei=sorted(j for j in f if tuple(sorted((a,j))) in E);assert len(nei)==2
  cy=[a,nei[0]]
  while True:
   nei=[j for j in f if tuple(sorted((cy[-1],j))) in E and j!=cy[-2]];assert len(nei)==1
   j=nei[0]
   if j==a:break
   assert j not in cy;cy.append(j)
  assert set(cy)==set(f)
  if dot(cross(sub(P[cy[1]],P[a]),sub(P[cy[2]],P[a])),fs[f][:3])<0:cy=[a]+cy[:0:-1]
  cycles.append(cy)
 assert len(P)-len(E)+len(faces)==2
 for i in range(len(P)):
  near=[f for f in faces if i in f]
  assert any(det(*(fs[f][:3] for f in ids)) for ids in combinations(near,3))
 T=F(0);U=(F(0),)*3
 for cy in cycles:
  for k in range(1,len(cy)-1):
   a,b,c=(P[j] for j in (cy[0],cy[k],cy[k+1]));d=det(a,b,c)
   T+=d;U=add(U,scale(add(add(a,b),c),d))
 assert T>0
 com=scale(U,1/(4*T));Q=[]
 for f in faces:
  h=fs[f][3]-dot(fs[f][:3],com);assert h>0
  Q.append(scale(fs[f][:3],1/h))
 return dict(vertices=P,facets=faces,edges=E,cycles=cycles,volume=T/6,centroid=com,poles=Q)

# Multivariate rational polynomials: exponent pair -> coefficient.
def pc(v):return {(0,0):F(v)} if v else {}
def pa(*args):
 out={}
 for p in args:
  for m,c in p.items():out[m]=out.get(m,F(0))+c
 return {m:c for m,c in out.items() if c}
def pm(a,b):
 out={}
 for m,c in a.items():
  for n,d in b.items():
   k=(m[0]+n[0],m[1]+n[1]);out[k]=out.get(k,F(0))+c*d
 return {m:c for m,c in out.items() if c}
def ps(p,c):return pm(p,pc(c))
def pp(p,n):
 out=pc(1)
 for _ in range(n):out=pm(out,p)
 return out
def pd(p,i):
 return {(m[0]-(i==0),m[1]-(i==1)):c*m[i] for m,c in p.items() if m[i]}
def poly_checks():
 x={(1,0):F(1)};y={(0,1):F(1)};one=pc(1)
 L=pa(one,x,ps(pp(x,2),7),ps(pm(pp(x,3),pp(pa(one,ps(x,-4)),2)),-2401))
 R=pm(pp(pa(ps(x,7),pc(-1)),2),pa(one,ps(x,15),ps(pp(x,2),168),ps(pp(x,3),-784)))
 assert L==R
 pos=pa(one,ps(x,8),ps(pm(x,pa(one,ps(x,-4))),7),ps(pm(pp(x,2),pa(one,ps(x,-4))),196))
 assert pos==pa(one,ps(x,15),ps(pp(x,2),168),ps(pp(x,3),-784))
 # Derivative of the inward two-angle F(x,y), with denominators cleared.
 e=pa(pm(x,pp(y,2)),ps(x,-1),ps(y,-2))
 k=pa(pp(x,2),ps(pm(x,y),4),pp(y,4),ps(pp(y,2),4))
 num=pp(e,2);den=pm(pm(pa(one,pp(x,2)),pp(pa(one,pp(y,2)),2)),k)
 der=pa(pm(pd(num,0),den),ps(pm(num,pd(den,0)),-1))
 fac=ps(pm(pm(pm(pp(pa(x,y),3),e),pa(pm(x,pp(y,2)),ps(x,-1),ps(pp(y,3),-1),ps(y,-3))),pp(pa(one,pp(y,2)),2)),-2)
 assert der==fac
 xn=pm(y,pa(pp(y,2),pc(3)));xd=pa(pp(y,2),pc(-1));yb=pa(one,pp(y,2))
 es=pa(pm(xn,xd),ps(pm(y,xd),-2))
 ns=pm(pp(es,2),pp(xd,2))
 ds=pm(pm(pa(pp(xd,2),pp(xn,2)),pp(yb,2)),pa(pp(pa(xn,ps(pm(y,xd),2)),2),pm(pp(y,4),pp(xd,2))))
 fmden=pm(pp(yb,2),pp(pa(pp(y,4),ps(pp(y,2),6),one),2))
 assert pm(ns,fmden)==pm(ds,pp(xd,4))
 # G(z)=(z-1)^4/((z+1)^2*(z^2+6z+1)^2).
 num=pp(pa(x,pc(-1)),4);den=pm(pp(pa(x,one),2),pp(pa(pp(x,2),ps(x,6),one),2))
 der=pa(pm(pd(num,0),den),ps(pm(num,pd(den,0)),-1))
 fac=ps(pm(pm(pm(pm(pa(x,one),pa(pp(x,2),ps(x,6),one)),pp(pa(x,pc(-1)),3)),pa(x,pc(3))),pa(pp(x,2),ps(x,-6),pc(-3))),-2)
 assert der==fac
 return {'directed_identity':[[list(m),c] for m,c in sorted(L.items())],
         'inward_derivative_identities':True}

# Exact Q(sqrt(3)); a planar point (A,B) denotes (A, B*sqrt(z)).
def q(a=0,b=0):return (F(a),F(b))
def qa(a,b):return add(a,b)
def qs(a,b):return sub(a,b)
def qm(a,b):return (a[0]*b[0]+3*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def qi(a):
 d=a[0]*a[0]-3*a[1]*a[1];assert d
 return (a[0]/d,-a[1]/d)
def qd(a,b):return qm(a,qi(b))
def qp(a,n):
 v=q(1)
 for _ in range(n):v=qm(v,a)
 return v
def sign(a):
 u,v=a
 if u>=0 and v>=0:return int(u>0 or v>0)
 if u<=0 and v<=0:return -int(u<0 or v<0)
 d=u*u-3*v*v;assert d
 return (1 if d>0 else -1)*(1 if u>0 else -1)
def local(z,Y,arrows):
 def vd(a,b):return qa(qm(a[0],b[0]),qm(z,qm(a[1],b[1])))
 def vc(a,b):return qs(qm(a[0],b[1]),qm(a[1],b[0]))
 def vs(a,b):return (qs(a[0],b[0]),qs(a[1],b[1]))
 u=[vd(v,v) for v in Y];esc=[[qs(vd(a,b),u[i]) for b in Y] for i,a in enumerate(Y)]
 got=[(i,j) for i in range(4) for j in range(4) if i!=j and sign(esc[i][j])>=0]
 assert got==arrows and all(esc[i][j]==q() for i,j in arrows)
 areas=[]
 for i in range(4):
  a,b=Y[i],Y[(i+1)%4];e=vs(b,a);areas.append(vc(a,b));assert sign(areas[-1])>0
  for j in range(4):
   if j not in (i,(i+1)%4):assert sign(vc(e,vs(Y[j],a)))>0
 H2=qd(qm(z,qp(vc(Y[0],Y[3]),2)),vd(vs(Y[3],Y[0]),vs(Y[3],Y[0])))
 return {'radicand_z':z,'points_A_B':Y,'norms':u,'escape_matrix':esc,'area_coefficients':areas,'H_squared':H2,
         'physical_metric_diag':[q(1),z,q(1)],'reciprocal_metric_diag':[q(1),qi(z),q(1)],
         'physical_poles':[(A,qm(z,B),q(1)) for A,B in Y]}
def sharp_controls():
 chain=local(q(6),[(q(1),q()),(q(1),q(1)),(q(-5),q(2)),(q(-17),q(-3))],[(0,1),(1,2),(2,3)])
 assert chain['norms']==[q(1),q(7),q(49),q(343)] and chain['H_squared']==q(F(1,7))
 chain['sigma']=1;chain['physical_root']=[0,0,1]
 chain['physical_edge_foot']=[F(1,8),F(-1,8),F(7,8)]
 # Rational physical foot, metric diag(1,6,1), root=(0,0,1).
 foot=F(1,8)**2+6*F(1,8)**2+F(7,8)**2
 assert foot==F(7,8)==F(2401,2400+344)
 assert chain['physical_poles']==[(q(1),q(),q(1)),(q(1),q(6),q(1)),(q(-5),q(12),q(1)),(q(-17),q(-18),q(1))]
 chain['edge_foot_norm_squared']=foot
 z=q(3,2);B=qa(q(1),z);A=qa(q(1),qm(q(3),z));B2=qp(B,2)
 Y=[(qi(A),qd(q(0,-1),A)),(q(1),q()),(qi(B),qi(B)),(qd(qs(q(1),z),B2),qd(q(2),B2))]
 inward=local(z,Y,[(0,1),(2,1),(3,2)])
 gamma=q(F(13,4),F(-15,8));assert inward['H_squared']==gamma and inward['norms'][1]==q(1)
 assert sign(qs(q(F(1,415)),gamma))>0
 assert qs(qs(qp(z,2),qm(q(6),z)),q(3))==q()
 g=qd(qp(qs(z,q(1)),4),qm(qp(qa(z,q(1)),2),qp(qa(qa(qp(z,2),qm(q(6),z)),q(1)),2)))
 assert g==gamma
 inward['sigma']=1;inward['physical_root']=[0,0,1]
 return {'field_basis':'a+b*sqrt(3); planar (A,B) means (A,B*sqrt(z))',
         'directed':chain,'inward':inward,'gamma':gamma,
         'scope':'Exact local cones; neither is an own-centroid bounded body'}

def metric_checks():
 u=2-F(25,96)**2;v=u*u-2;assert u>0 and v>0 and v*v>3
 out=[]
 for h,k,cap in ((9,8,49),(9,6,45),(8,6,44)):
  x=F(625,256)*(F(1,h+1)+F(1,k+1))
  gap=sum((x**i/F(factorial(i)) for i in range(5)),F(0))-F(81,cap);assert gap>0
  out.append([h,k,cap,gap,F(2401,2400+9*cap),F(415,414+9*cap)])
 return out

def actual_control():
 a=F(101,100);b=F(2);z=(F(1),F(0));qs0=[]
 for _ in range(4):
  qs0.append(z+(F(1),));z=(a*z[0]-b*z[1],b*z[0]+a*z[1])
 qs0.append((F(306,25),F(-247,100),F(-3)))
 H=[(q0,F(1)) for q0 in qs0];assert len(halfvertices(H))==5
 eps=F(1,100)
 for ids in ((0,1,4),(2,3,4)):
  n=tuple(sum(qs0[i][j] for i in ids) for j in range(3));H.append((n,3-eps))
 P=halfvertices(H);assert len(P)==9
 cut=[p for p in P if dot(H[5][0],p)==H[5][1]];assert len(cut)==3
 cc=tuple(sum(p[j] for p in cut)/3 for j in range(3))
 new=add(cc,scale(H[5][0],eps**3/dot(H[5][0],H[5][0])))
 assert dot(H[5][0],new)>H[5][1]
 assert all(dot(n,new)<h for i,(n,h) in enumerate(H) if i!=5)
 P=sorted(P+[new]);D=hull(P);Q=D['poles'];E=D['edges'];faces=D['facets']
 assert (len(P),len(E),len(faces))==(10,17,9)
 X=[sub(p,D['centroid']) for p in P];G=[[dot(x,y) for y in X] for x in X];J=[[dot(q0,r0) for r0 in Q] for q0 in Q]
 # Independent exact own-centroid check using positive cones from 0.
 W=F(0);moment=(F(0),)*3
 for cy in D['cycles']:
  for k in range(1,len(cy)-1):
   tri=[X[i] for i in (cy[0],cy[k],cy[k+1])];w=det(*tri);assert w>0
   W+=w;moment=add(moment,scale(add(add(tri[0],tri[1]),tri[2]),w))
 assert W==6*D['volume'] and moment==(0,0,0)
 assert all(dot(Q[f],X[i])==1 if i in cy else dot(Q[f],X[i])<1 for f,cy in enumerate(faces) for i in range(10))
 root=P.index((F(0),F(0),F(1)))
 side=[]
 for q0 in qs0[:4]:
  vertices=tuple(i for i,p in enumerate(P) if dot(q0,p)==1);side.append(faces.index(vertices))
 assert root==3 and side==[4,5,2,1]
 assert len([e for e in E if root in e])==4
 esc=[[J[i][j]-J[i][i] for j in side] for i in side]
 assert [(i,j) for i in range(4) for j in range(4) if i!=j and esc[i][j]>=0]==[(0,1),(1,2),(2,3)]
 assert all(esc[i][i+1]>0 for i in range(3))
 stable=[i for i in range(9) if all(J[i][j]<J[i][i] for j in range(9) if j!=i)]
 unstable=[i for i in range(10) if all(G[i][j]<G[i][i] for j in range(10) if tuple(sorted((i,j))) in E)]
 saddles=[]
 for i,j in E:
  f,g=[a0 for a0,cy in enumerate(faces) if i in cy and j in cy]
  assert G[i][i]!=G[i][j] and G[j][j]!=G[i][j]
  assert J[f][f]!=J[f][g] and J[g][g]!=J[f][g]
  if G[i][i]>G[i][j] and G[j][j]>G[i][j] and J[f][f]>J[f][g] and J[g][g]>J[f][g]:saddles.append((i,j))
 assert all(J[i][j]!=J[i][i] for i in range(9) for j in range(9) if i!=j)
 assert stable==[1,3] and unstable==[2,3,4,5] and saddles==[(1,4),(2,5),(3,4),(5,6)]
 other=next(v0 for v0 in set(faces[side[0]])&set(faces[side[3]]) if v0!=root);assert other==4
 r=G[root][root];aa=[r*J[i][i]-1 for i in side];cc=r*J[side[0]][side[3]]-1
 B=aa[0]+aa[3]-2*cc;Delta=aa[0]*aa[3]-cc*cc
 A=r-G[root][other];K=r*G[other][other]-G[root][other]**2
 assert min(aa)>0 and cc<0 and B>0 and Delta>0 and A>0 and K>0
 assert 2401*Delta<aa[3]*B and 2401*A*A<aa[3]*K
 assert Delta*K==B*A*A
 assert G[other][other]*(2400+r*J[side[3]][side[3]])>2401*r
 D.update(identity='ACTUAL_E17_STRICT_QUADRIVALENT_CHAIN_NEGATIVE_CONTROL',
  input_planes=H,stack_point=new,centered_vertices=X,metric=[[1,0,0],[0,1,0],[0,0,1]],
  root=root,incident_chain=side,other_endpoint=other,local_escapes=esc,
  stable=stable,unstable=unstable,saddles=saddles,equilibrium_counts=[2,4,4],
  closing_data={'a':aa,'c':cc,'B':B,'Delta':Delta,'A':A,'K':K,'norm_ratio':G[other][other]/r},
  scope='Own uniform-volume centroid; actual (10,17,9), but NOT S1/U1/H0')
 return D

@lru_cache(None)
def rooted_codes(n):
 if n==1:return ('()',)
 avail=sorted((c,k) for k in range(1,n) for c in rooted_codes(k));out=[]
 def rec(left,start,parts):
  if left==0:out.append('('+''.join(parts)+')');return
  for i in range(start,len(avail)):
   c,k=avail[i]
   if k<=left:rec(left-k,i,parts+[c])
 rec(n-1,0,[]);return tuple(sorted(out))
def code_parent(code):
 p=[];stack=[]
 for ch in code:
  if ch=='(':
   j=len(p);p.append(stack[-1] if stack else 0);stack.append(j)
  else:stack.pop()
 return tuple(p)
def literal_domain():
 faces=[[0,1,2,3,4,5,6,7],[0,1,8],[1,2,8],[3,4,9],[4,5,9],[5,6,9],[6,7,9],[2,3,9,8],[7,0,8,9]]
 path=[0,1,2,7,8,6,5,4,3];Z=[6,5,4,3,2,1,0,7,8];p=[0,0,1,2,3,4,5,0,7]
 roof=[(-2,-1,0),(-3,0,0),(-2,1,0),(2,1,0),(3,F(1,2),0),(F(7,2),0,0),(3,F(-1,2),0),(2,-1,0),(-1,0,1),(1,0,1)]
 roof=[tuple(map(F,x)) for x in roof];rh=hull(roof)
 assert set(rh['facets'])=={tuple(sorted(f)) for f in faces}
 E={tuple(sorted((a,b))) for f in faces for a,b in zip(f,f[1:]+f[:1])}
 dual=[tuple(sorted(set(faces[a])&set(faces[b]))) for a,b in zip(path,path[1:])]
 assert all(len(e)==2 and e in E for e in dual) and len(set(dual))==8
 T=sorted(E-set(dual));assert T==[(0,7),(0,8),(1,2),(2,3),(3,4),(3,9),(4,5),(5,6),(6,7)]
 pv=[8,2,3,4,5,6,7,0,8,3]
 assert all(tuple(sorted((i,j))) in T for i,j in enumerate(pv) if i!=j)
 for i in range(10):
  seen=set()
  while i!=8:assert i not in seen;seen.add(i);i=pv[i]
 label_to_face=[path[Z.index(i)] for i in range(9)]
 assert label_to_face==[5,6,8,7,2,1,0,4,3]
 assert [i for i,f in enumerate(faces) if 8 in f]==[1,2,7,8]
 assert set(faces[1])&set(faces[8])=={0,8}
 order=[8,0,7,6,5,4,3,2,1,9];cp=tuple(order.index(pv[v]) for v in order)
 assert cp==(0,0,1,2,3,4,5,6,7,6)
 parents=sorted(code_parent(c) for c in rooted_codes(10))
 assert len(parents)==719 and parents.index(cp)==716
 heights=[0]*10
 for i in range(1,10):heights[i]=heights[cp[i]]+1
 assert max(heights)==8
 return {'facets':faces,'geometric_incidence_control':roof,'rooted_tree_ordinal':716,'root_preorder':order,'edges':sorted(E),'primal_root':8,'primal_parent':pv,
  'polar_parent_literal_TREE253':p,'literal_facet_to_native_face':label_to_face,
  'dual_path_native_faces':path,'primal_complement_edges':T,
  'local_directed_chain_native_faces':[1,2,7,8],
  'omitted_edge':[8,0], 'excluded_closed_norm_band':'G00/G88 <= 2401/2796',
  'scope':'Exact incidence/root subdomain, not a new whole-type or FULL/LOCAL census'}

def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(list,tuple)):return [encode(v) for v in x]
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 return x
def build():
 data={'identity':'JOINT_QUADRIVALENT_CLOSING_EDGE_V1','polynomial_audit':poly_checks(),
  'sharp_local_controls':sharp_controls(),'derived_metric_arithmetic':metric_checks(),
  'actual_negative_control':actual_control(),'literal_E17_subdomain':literal_domain(),
  'new_whole_types_excluded':0,'accepted_lower_bound_C_unchanged':34}
 return (json.dumps(encode(data),sort_keys=True,separators=(',',':'))+'\n').encode()
if __name__=='__main__':
 assert sys.argv[1:] in (['build'],['check'])
 raw=build();out=Path('joint_closing_edge.json')
 if sys.argv[1]=='build':
  if out.exists():assert out.read_bytes()==raw
  out.write_bytes(raw)
 else:assert out.read_bytes()==raw
 print('JOINT_CLOSING_EDGE_2401_AND_INWARD_SHARP_PASS')
 print('ACTUAL_10_17_9_OWN_COM_S2_U4_H4_PASS')
 print('JOINT_CLOSING_EDGE_RECOVERY_PASS',len(raw),hashlib.sha256(raw).hexdigest())
```

Дополнительные копии: исходник (`joint_closing_edge.py`), точный отчёт (`joint_closing_edge.json`), Markdown-handoff (`result_markdown.md`). Полные доказательства и генератор выше достаточны без загрузки этих файлов.
