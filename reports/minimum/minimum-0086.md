# minimum-0086

Historical AI scientific report · saved 2026-09-18 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# TWO_APEX_FACET_CLOSING_512_V1

**Steady Lynx 90 · minimum-0086**

## Результат

**Весь действительный совместный домен ROOF8_3_5 с буквальными родителями и отображением из parent minimum-0084 исключён.** В частности, закрыта вся оставшаяся область `G00/G88 > 2401/2796`, а не только ещё одна её нормовая полоса. Для этого конкретного домена достаточно уже заданных двух слабых деревьев: дополнительно предполагать невырожденность стрелок или использовать H=0 не требуется.

Получено также более общее препятствие. Пусть у настоящего однородного тела с собственным COM имеется грань B, содержащая все вершины, кроме двух x,z. Пусть x — единственная строго неустойчивая вершина, её степень4, а четыре инцидентных полюса в циклическом порядке имеют слабую цепь

    L0 -> L1 -> L2 -> L3,

причём B и L0 — настоящие соседние грани и имеется слабая стрелка `B -> L0`. **На срезе (10,17,9) это несовместимо с S=1,H=0.** Выбранные стрелки разрешено иметь нулевыми; дополнительных отсутствующих стрелок в FULL-графе не предполагается.

Механизм состоит из двух новых совместных оценок. После физической нормировки `Gxx=1`, при `u=J_L0,L0-1`, `a=J_L3,L3-1` и квадрате расстояния h от0 до замыкающей прямой касательного полярного четырёхугольника:

    a > 64u + 576h,                                              (A)
    u + 9h > 8                                                  (B)

во втором случае ниже. Оценка (B) использует один настоящий полюс большой грани, собственный объёмный COM и реальное замыкающее primal-ребро. Она не следует из независимо выбранных скалярных строк. В результате `a>512`, или в исходной нормировке

    Gxx J_L3,L3 >513.

Настоящая совместная механика с10 вершинами и9 гранями, напротив, даёт

    Gxx J_L3,L3 <29160/59 <513.

Здесь нет произвольно обрезанного condition number: обе противоречащие оценки выведены из геометрии и механики. Более точная оценка родителя `a<395` делает запрет заданного716 ещё короче.

**Граница результата.** Это не запрет всех реализаций rooted-tree716, не запрет всех корней комбинаторного ROOF8_3_5 и не доказательство C>=36. FULL/LOCAL-перепись не выполнялась; численного списания из этих регистров нет. Принятая общая граница C>=34 и отсутствие аттейнера34 остаются без изменения. :contentReference[oaicite:0]{index=0}

## 1. Точная идентичность закрытого домена и источники

Буквальный immutable parent: `minimum-0084`, SHA-256 `77ad9a46f5f13c16d66d477e79c5ca8bbcd53f7c2b5a17819bb7a7e17481fa39`. Прочитаны весь прикреплённый current brief, весь literal parent с исходником, полный CENTERED_CIRCUIT_RANK3 theorem-unit и оба его complete source. Самостоятельно проверен pin имеющегося parent-исходника:14725байт, SHA-256 `d5d9f1904d70ed0f1ab99f6dc2cbde83c9c24779a5345d7428f16c8805df4c8d`. Его большие исторические предки заново не исполнялись.

Существенного конфликта с literal parent нет. В новом проверяющем некоторые гранные циклы обращены для согласованной внешней ориентации интегрирования; их номера, вершины и настоящие рёбра не изменены. Целенаправленный library-search по `ROOF8_3_5` был сделан после первого геометрического вывода; полученные текущие ссылки совпали с attached parent. Это не объявляется аудитом всей истории или установлением приоритета.

Домен задан следующими **native** максимальными гранями:

    F0=[0,1,2,3,4,5,6,7], F1=[0,1,8], F2=[1,2,8],
    F3=[3,4,9], F4=[4,5,9], F5=[5,6,9], F6=[6,7,9],
    F7=[2,3,9,8], F8=[7,0,8,9].

Native primal-родители, корень8:

    pv=(8,2,3,4,5,6,7,0,8,3).

Literal TREE253 polar-родители и literal-facet -> native-facet отображение:

    pq=(0,0,1,2,3,4,5,0,7),
    map=(5,6,8,7,2,1,0,4,3).

То есть native polar-стрелки:

    6->5, 8->6, 7->8, 2->7, 1->2, 0->1, 4->5, 3->4.

Primal-preorder `(8,0,7,6,5,4,3,2,1,9)` имеет родителей `(0,0,1,2,3,4,5,6,7,6)`: это inherited rooted-tree ordinal716, **не** polytope ordinal, FULL-row или LOCAL-row. Высоты деревьев8 и6. Эти точные данные принадлежат parent, а не восстанавливаются по созвучному имени. :contentReference[oaicite:1]{index=1}

Для новой теоремы здесь

    B=F0, x=vertex8, z=vertex9, y=vertex0,
    (L0,L1,L2,L3)=(F1,F2,F7,F8).

Стрелки `B->L0` и `y->x` буквально входят в заданные деревья. Замыкающее ребро — настоящее `(8,0)=F1 intersection F8`. F0 содержит ровно остальные8 вершин. Поэтому весь этот weak-tree domain входит в доказанное ниже исключение.

Явная отражённая копия также покрыта без нового геометрического аргумента:

    vertex reflection=(2,1,0,7,6,5,4,3,8,9),
    facet reflection=(0,2,1,6,5,4,3,8,7),
    reflected pv=(7,0,8,2,3,4,5,6,8,7),
    reflected literal-facet map=(4,3,7,8,1,2,0,5,6).

Это две labelled записи одного явно отображённого случая, не два вычитаемых элемента неизвестного регистра.

## 2. Одна метрика, настоящее начало и точная огибающая замыкающего ребра

Пусть c — настоящий равномерный объёмный центроид, `x_v=v-c`, `M>0`, `N=M^(-1)`,

    G_vw=x_v^T M x_w,       J_fg=q_f^T N q_g,
    q_f^T x_v<=1.

При `R=Gxx` исходная полярная проекция есть **Mx/R**, не x/R. Одновременно переводим координаты в

    X_v=M^(1/2)x_v/sqrt(R),
    Q_f=sqrt(R) M^(-1/2)q_f.

После вращения X_x=(0,0,1). В этой нормировке incident Q_i=(t_i,1), а0 находится строго внутри настоящего касательного четырёхугольника `conv(t0,t1,t2,t3)`. Это тот же физический переход, что в literal parent. :contentReference[oaicite:2]{index=2}

Положим

    u=|t0|^2=R J_L0,L0-1,
    a=|t3|^2=R J_L3,L3-1,
    h=dist(0,line(t0,t3))^2.

Здесь h — нормированное расстояние в касательной плоскости; это **не** H-число седловых точек, не старый tetrahedron-volume ratio и не ковариация. Все три числа положительны.

Пусть alpha,beta,chi — центральные углы выбранных трёх сторон, S их сумма. Из слабых стрелок получаем

    0<alpha,beta,chi<pi/2,     pi<S<3pi/2,
    sqrt(u/a)<=cos(alpha)cos(beta)cos(chi)<=cos^3(S/3).

Первое строгое неравенство S>pi следует из строгой внутренности0 и того, что замыкающая сторона имеет центральный угол меньше pi. Нулевые выбранные стрелки этому не мешают.

Введём фактическое отношение

    w=(u/a)^(1/3),          0<w<1/4.

Теперь `S<=3 arccos(sqrt(w))`. При фиксированном `s=sqrt(u/a)` формула расстояния есть

    h/a = s^2(1-cos^2 S)/(1+s^2-2s cos S).

На `-1<cos S<0` правая часть возрастает по cos S: знак её производной есть знак `s cos^2 S-(1+s^2)cos S+s`, который положителен. Следовательно,

    h/a <= F(w),
    F(w)=w^3(1-4w)^2/(1+w+7w^2).                               (2.1)

Это **связанная огибающая по действительному отношению u/a**, а не независимое применение максимума1/2401 и роста64. Проверка сокращений полностью полиномиальна:

    1-w(4w-3)^2=(1-w)(1-4w)^2,
    1+6w^2-7w^3=(1-w)(1+w+7w^2).

Огибающая локально точна для каждого w: при `theta=arccos(sqrt(w))`, `r0=sqrt(a w^3)` положить `t_j=r0(1+i tan(theta))^j`, j=0,1,2,3, отождествляя комплексное число с плоским вектором. Все три стрелки равны0; четырёхугольник строго выпуклый и содержит0 внутри. Это рецепт локального конуса, не утверждение о его замыкании в однородное тело.

Для дальнейшего достаточно следующего строго положительного полинома:

    1+w+7w^2-64w^3[(1+w+7w^2)+9(1-4w)^2]
     =(1-4w) Q(w),
    Q(w)=2416w^4-532w^3+27w^2+5w+1.

На `[0,1/4]` коэффициенты Q в Bernstein-базисе степени4, с аргументом t=4w, в точности равны

    (1, 21/16, 61/32, 45/64, 81/16).

Все положительны. Поэтому из (2.1), при `0<w<1/4`, следует

    **a >64u+576h.**                                            (2.2)

Число576 не объявляется оптимальной линейной константой; точный нелинейный объект — (2.1). Строгость (2.2) сохраняется на стенках нулевых стрелок. В частности, повторно получается `a>64u`.

Для настоящего замыкающего ребра xy эта же h имеет координатно-инвариантное выражение

    h=(R-Gxy)^2/(R Gyy-Gxy^2).                                 (2.3)

Знаменатель строго положителен: два разных конца настоящего ребра не могут быть коллинеарны с внутренним COM. Формула также заново проверена на точных локальных edge-controls ниже.

## 3. Собственный объёмный COM большой грани: не свободное массовое уравнение

Предположим теперь, что B содержит все вершины, кроме x,z. В физической нормировке обозначим

    p=Q_B.X_x,      s=Q_B.X_z,
    lambda=Vol(conv(B,x))/Vol(P).

Имеем p<1,s<1 и `0<lambda<1`.

Построим действительный tetrahedral fan из x. Треугольники B дают tetrahedra типа x+3 base vertices. Любая другая грань, не содержащая x, является треугольником z+2 base vertices: три различные base-вершины уже определили бы плоскость B. Остальные грани содержат x и имеют нулевые fan-cones. Поэтому средние значения функционала Q_B по положительным tetrahedra равны соответственно `(p+3)/4` и `(p+s+2)/4`. Они усредняются **настоящими объёмами одного P**. Поскольку COM=0,

    0=lambda(p+3)+(1-lambda)(p+s+2),
    p+s+2=-lambda(1-s)<0.

Таким образом определено истинное положительное число

    **delta=-p-s-2=lambda(1-s)>0.**                              (3.1)

Не предполагаются параллельность ridge и B, равные высоты апексов, фиксированные площади, независимые строки Lambda или отдельный центр полярного тела.

Слабое primal-дерево к x либо U=1 делает x единственным максимумом физической нормы: вдоль каждой стрелки

    |parent|^2-|child|^2
      =2 child.(parent-child)+|parent-child|^2>0.

Следовательно `|X_z|<1`. Если `k=|Q_B|`, то `s>-k`; из (3.1) получаем

    **k-p-2>delta.**                                            (3.2)

Именно это место требует собственного равномерного COM, а не произвольной положительной центрирующей комбинации.

## 4. Новый общий полюсный SOS: случай замыкающего конца y в B

Пусть xy — настоящее ребро между L0 и L3, y принадлежит B, и имеется слабая primal-стрелка `y->x`. Для указанного716 это заданная стрелка0->8. Для более общего H=0-класса она будет выведена в разделе6.

Повернём касательные координаты так, чтобы замыкающая прямая имела уравнение `t.n=H`, H>0, где n — единичная внешняя нормаль этой стороны. Положим

    Q_L0=(H,T,1),      Q_B=(v,m,p),
    h=H^2,            u=H^2+T^2.

m здесь — координата полюса, не масса. Направление настоящего primal-ребра к y имеет вид

    Y=X_x+tau(n,-H),        tau>0.

Оно удовлетворяет всем incident support-неравенствам; остальные касательные вершины лежат строго по внутреннюю сторону замыкающей прямой. Из `Y.(X_x-Y)>=0` следует

    tau<=H/(1+h).

Условие `Q_B.Y=1`, p<1, теперь даёт

    H v+p>=1+h.                                                (4.1)

Слабая полюсная стрелка B->L0 есть другое неравенство той же реальной координатной тройки:

    I1=v^2+m^2+p^2-Hv-Tm-p<=0.

Положим также

    I2=1+h-Hv-p<=0,
    Qmass=v^2+m^2-4p-4=k^2-(p+2)^2.

Наконец `y->x` означает, что Y лежит в шаре с диаметром `[0,X_x]`. Из `Q_B.Y=1` получаем `p+k>=2`. Совместно с (3.2) это даёт

    Qmass=(k-p-2)(k+p+2)>4delta.

Все выражения относятся к ОДНОМУ Q_B; замена его независимо подобранными скалярными строками разрушает следующий шаг. Прямое тождество:

    2I1+6I2-Qmass
     =(v-4H)^2+(m-T)^2+2(p-1)^2+8-u-9h.                        (4.2)

Неотрицательность квадратов и знаки I1,I2 доказывают

    **u+9h>8+4delta>8.**                                       (4.3)

Это универсальный геометрический вывод, не найденная численная infeasibility-метка. В совокупности с (2.2):

    **a>512+256delta>512.**                                    (4.4)

Полезно сохранить и параметризованное тождество. Для любого r>=2, `Qr=v^2+m^2-2rp-r^2`,

    2I1+(2r+2)I2-Qr
     =[v-(r+2)H]^2+(m-T)^2+2(p-1)^2
       +r(r+2)-u-(r+1)^2h.

При доказанном `k-p>r` оно даёт `u+(r+1)^2h>r(r+2)`. В частности, можно подставлять `r=2+delta`; это дополнительная точная совместная mass/edge-оценка, хотя для запрета716 она не нужна.

## 5. Второй случай: первая локальная грань содержит оба апекса

Если L0 содержит и x, и z, можно обойтись без y->x и без H=0. Из B->L0 следует

    |Q_B-Q_L0/2|<=|Q_L0|/2.

Поскольку `Q_L0.(X_x+X_z)=2`, а `Q_B.(X_x+X_z)=-2-delta`, Cauchy–Schwarz даёт

    |Q_L0| |X_x+X_z| >=6+2delta.

Здесь знак **>=** сохранён намеренно: слабая полюсная стрелка может быть нулевой. Но `|X_x+X_z|<2`, так что

    u>(3+delta)^2-1=8+6delta+delta^2,
    a>64u>512+384delta+64delta^2.                               (5.1)

Это самостоятельный настоящий two-apex bridge. В исходных G,J его точная несокращённая версия:

    J_L0,L0 (Gxx+2Gxz+Gzz) >=4(3+delta)^2 >36.

Полярная плотность нигде не возникает.

## 6. Роль H=0 и все слабые граничные стрелки

У направленной локальной цепи `pi<S<3pi/2`, поэтому `t0.t3<0`. Значит,

    J_L0,L3 <1/R < J_L0,L0, J_L3,L3.

На замыкающем настоящем ребре xy обе dual-производные строго отрицательны. У x также `R-Gxy>0`. Поэтому строгая седловая точка на этом ребре существовала бы в точности при `Gyy-Gxy>0`. Отсутствие строгих седловых точек даёт

    Gyy-Gxy<=0,

то есть нужную слабую стрелку y->x. Используется точный настоящий feature-test, включая положение перпендикулярной ноги на сегменте и внутри normal cone. :contentReference[oaicite:3]{index=3}

Если L0 не содержит z, второй конец замыкающего ребра не может быть z, а значит находится в B: применим раздел4. Если L0 содержит z, применим раздел5. Это исчерпывает случаи и доказывает заявленный общий H0-pattern obstruction.

При `Gyy=Gxy` перпендикулярная нога совпадает с концом y. Эта стена не выбрасывается: в (4.1),(4.2) остаются нестрогие неравенства, и противоречие сохраняется. Все нулевые выбранные primal/polar-стрелки разрешены. Доказательство требует лишь отсутствия **строгого** saddle, поэтому покрывает и более сильную конвенцию H0 без normal-boundary контактов.

Это не повторное объявление bare tree-cotree теоремы. Новый ресурс — знак именно замыкающей пары, вытекающий из её касательного углового охвата, плюс actual-COM identity (3.1) и один общий полюс в SOS (4.2). Для literal716 H0 вообще можно удалить из предпосылок, поскольку y->x уже входит в pv.

## 7. Полученная несовместимость с любой конечной SPD-метрикой

Для полноты ниже приведён достаточный метрический аргумент без использования численных49/45/44 родителя.

Пусть Sigma — НАСТОЯЩАЯ объёмная ковариация. После аффинной калибровки Sigma=I:

    sqrt(5/3) ball subset P subset sqrt(15) ball.               (7.1)

Внешняя оценка получается из actual fan из каждой вершины. Если проекции четырёх вершин ячейки равны b,z1,z2,z3 и s=z1+z2+z3, то собственное центрирование даёт `E_cells s=-b`, а точное интегрирование tetrahedron —

    20 E_P[(e.X)^2]
     =E_cells[b^2+z1^2+z2^2+z3^2+(b+s)^2]
     >=(4/3)b^2.

Отсюда b^2<=15. Для внутренней оценки поддержка `f=h-e.X>=0`, |e|=1, имеет `Ef=h, Ef^2=h^2+1`. Используется классическое неравенство Бервалда в точной форме `Ef^2<=(8/5)(Ef)^2` для неотрицательной аффинной f на равномерном трёхмерном выпуклом теле; оно даёт `h^2>=5/3`. Эта внешняя входная формула проверена по первичному HTML Langharst–Putterman, arXiv:2210.04438v7, формула(1); применяется n=3,p=1,q=2. Доказательство всей статьи заново не аудировалось. :contentReference[oaicite:4]{index=4}

Полярность (7.1) даёт отношение внешнего/внутреннего радиуса не более3 и для настоящего P*. Ковариация при этом не отождествляется с M. Тот же факт и конечноглубинная лемма имеются в полностью прочитанном parent; здесь они изложены с более грубой, но достаточной рациональной константой. :contentReference[oaicite:5]{index=5}

Лемма знакового перехода. Если `r ball subset conv(X) subset R0 ball`, A>0 и существует корневое слабое A-дерево на n точках, то

    lambda1(A)/lambda2(A)
      <(R0/r)^2 exp[-9/(4n)].                                  (7.2)

Действительно, выберем старшую ось e со знаком, при котором корень имеет неотрицательную проекцию; начнём с точки с проекцией <=-r. До первого перехода y->z к неотрицательной проекции пусть было m предыдущих стрелок, L=m+1<=n-1. В A^(1/2)-координатах, при угле phi между -e и y, слабые радиальные неравенства, сферическое треугольное неравенство и вогнутость log cos дают

    sqrt(lambda1) r <=|A^(1/2)y| cos^L(phi/L).

На переходе вклад старшей оси неположителен, а поперечная компонента z ограничена `sqrt(lambda2) R0`. Отсюда

    sqrt(lambda1/lambda2)
      <=(R0/r) sin(phi) cos^L(phi/L).

Максимум последнего углового множителя равен `cos^(L+1)(pi/(2(L+1)))`: его logarithmic derivative есть `cot(phi)-tan(phi/L)`. Из `log cos t<-t^2/2`, `pi>3` и L+1<=n получаем (7.2). Это включает нулевые стрелки и кратные старшие собственные значения.

Применим лемму к настоящим вершинам для M и к настоящим полюсам для N=M^(-1). U1 и S1 дают соответствующие слабые деревья; либо они уже заданы как в716. Их высоты не ограничиваются экспериментально: число точек даёт n<=10 и f<=9. В ковариационной калибровке для m1>=m2>=m3:

    m1/m2 <9 exp[-9/40],
    m2/m3 <9 exp[-1/4],
    kappa <81 exp[-19/40] <81/(1+19/40)=3240/59<57.

В произвольных исходных координатах это утверждение о

    kappa = condition(Sigma^(1/2) M Sigma^(1/2)).

Из (7.1) для любой настоящей вершины и любого настоящего полюса

    Gxx Jrr <=9 kappa <29160/59<513.                             (7.3)

Разделы4–6, напротив, требуют `Gxx Jrr>513`. Противоречие закрывает весь описанный общий pattern-class на (10,17,9). Никакого поиска по ограниченной SPD-сетке нет.

### Самый короткий запрет непосредственно указанного716

У parent имеется `a<395`, где `a=G88 J_F8,F8-1`. Его два отдельных локальных вывода дают `u<a/64` и `h<=a/2401`. Новое SOS (4.3) уже противоречит им:

    8 <u+9h
      <395(1/64+9/2401)
      =1175915/153664
      =8-53397/153664 <8.

Следовательно, **для whole716-proof даже новая полная огибающая (2.1) не обязательна**: новым решающим входом является совместная actual-mass/SOS оценка. Огибающая усиливает результат до512 и позволяет распространить его на все8 локальных направленных цепей у native-вершины8, без предпосылки literal TREE253 или её высоты6.

Полное перечисление этих8 локальных clauses получается из cyclic list `(F1,F2,F7,F8)`: выбрать любой из4 стартов и одно из2 направлений, взять4 последовательных полюса, добавить B->первый и общий H0/единственный U8. Четыре начала находятся на F7/F8 и используют раздел5, остальные4 — раздел4. Полные literal paths и closing edges сохраняет генератор. Это8 запрещённых локальных геометрических условий, **не**8 новых элементов FULL/LOCAL-реестра.

## 8. Точные полиномиальные добавки для одной centered-rank3 реализации

Никакой новый свободный центр, новая метрика или independent-row block не нужны. В обозначениях раздел2 положим

    R=Gxx, A=R-Gxy, D=R Gyy-Gxy^2>0,
    u=R J_L0,L0-1, a=R J_L3,L3-1,
    delta=-B_xB-B_zB-2,

где `B_vf=x_v.q_f` — общая матрица настоящих support-инциденций, а delta>0 доказана интегрированием.

На соответствующем домене раздел4 можно добавить строго положительные полиномы

    (u-8-4delta)D+9A^2 >0,
    (a-64u)D-576A^2 >0,
    R J_L3,L3-513-256delta >0.

Последний следует из первых двух; это не независимое предположение. Для случая L0 содержит z имеется

    J_L0,L0 (Gxx+2Gxz+Gzz)-4(3+delta)^2 >=0,
    R J_L3,L3-513-384delta-64delta^2 >0.

В точной cubic-модели родителя G имеет степень1, B —2, J —3. Поэтому перечисленные максимальные степени равны6 и4; число292 переменных не увеличивается. Обе координатные грам-матрицы уже принадлежат одному настоящему телу по полной determinant/first-moment/support системе. :contentReference[oaicite:6]{index=6}

Новая система quantifier elimination не запускалась, а новые33-variable chart-файлы не строились. Старый JPT164 не переобъявляется автоматически. Принципиальное отличие от supported-moment SDP — все исходные support-инциденции и собственное объёмное центрирование сохраняются; на свободные строки эти условные полиномы переносить нельзя.

## 9. Что проверялось, отрицательные контроли и предел результата

Сначала были проверены отдельные bounds64/2401 вместе со скалярной two-apex centroid identity. Они оставляют формальные точки, не имеющие установленной общей геометрии. Решающий шаг — сохранить в обеих механических операциях ОДИН полюс большой грани и получить точное square-completion (4.2). Затем фиксированное отношение u/a заменило два независимо используемых локальных максимума и дало более сильное512-препятствие.

Для продолжения сохранены два точных formal scalar controls. В порядке `(p,k,s,a,u,h)`:

    (1/3,12/5,-19/8,360,11/2,7/50),
    (7/10,271/100,-541/200,420,13/2,17/100).

Оба имеют положительную действующую только формально `lambda=delta/(1-s)`, выполняют отдельно `a>64u`, `2401h<a`, `a<440`, обычные scalar Cauchy/edge-band tests из исходника. Первый нарушает новую mass-SOS нижнюю оценку, второй её проходит, но нарушает связанную локальную огибающую и (2.2). Они **не** названы координатными реализациями, actual Lambda или телами. Это точные барьеры к возвращению к перечисленным независимым скалярным тестам, не контрпримеры к теоремам.

Есть собственноцентрированный геометрический контроль ТОГО ЖЕ ROOF8 face lattice, взятый из literal parent и теперь дополнительно полностью механически проверенный:

    (-2,-1,0),(-3,0,0),(-2,1,0),(2,1,0),(3,1/2,0),
    (7/2,0,0),(3,-1/2,0),(2,-1,0),(-1,0,1),(1,0,1).

При M=N=I:

    Vol=17/4,    c=(19/136,0,59/204),
    lambda=43/51, p=s=-145/59, delta=172/59,
    stable native facets=[0,7,8],
    unstable native vertices=[1,5],
    saddle edges=[(0,7),(2,3),(8,9)],
    (S,U,H)=(3,2,3).

Все настоящие edge-производные ненулевые; все различные polar-pair derivatives также ненулевые. Этот контроль НЕ реализует заданные деревья: в частности, B->F1 и vertex0->8 строго проваливаются. Он проверяет собственный COM, настоящие максимальные грани, все17 настоящих рёбер и actual-fan identity, но не служит основанием универсального исключения.

Отдельно сохранён локально точный конус (не bounded body): `w=1/5,a=250`, x=(0,0,1),

    q0=(1,0,1), q1=(1,1,1), q2=(-3,2,1), q3=(-11,-1,1),
    M=diag(1/2,1/8,1), N=diag(2,8,1).

Касательные нормы `(2,10,50,250)`, h=2/37, положительные веса `(35,1,1,3)`. Все3 стрелки нулевые. Направление замыкающего ребра `(1,-12,-1)`, параметр ноги `tau*=2/39`. Проверены `tau=tau*/2,tau*,3tau*/2`: соответственно слабая primal-стрелка с положительным запасом, нулевая стрелка на конце и строгий локальный saddle. Это явно показывает, где используется H0 и почему equality wall не удалена.

Генератор сохраняет также формальную границу `w=1/4,a=512`: closing area=0, strict normal-cone interior потерян, два максимума нормы совпадают в построенном partial control. Она НЕ предъявляется как допустимое замкнутое граничное тело или sharpness of512 среди однородных тел. Оптимальность512 в полном физическом классе не установлена.

Не выполнена новая FULL/LOCAL census, не получен новый110-кандидат и не доказан запрет всех других направлений базовой стрелки. Материальный следующий рубеж — наложить этот точный запрещённый pattern на реальные facet-labelled регистры, сохраняя отображения, и затем исследовать случаи, где большая грань выходит не в первый полюс локальной цепи, либо где неустойчивая внебазовая вершина имеет степень6. Оставшиеся rooted716 реализации на других face lattices не объявляются закрытыми.

## 10. Полная восстановительная капсула

Ниже весь единственный исходник; внешних программных зависимостей, старого sandbox, coefficient-файла, RNG или solver нет. Сохранить как `two_apex_closing.py`, UTF-8/LF, последний LF, assertions enabled.

Наблюдённая среда: CPython3.13.5, стандартная библиотека. Команды:

    python -S two_apex_closing.py build
    python -S two_apex_closing.py check

Обе прошли. Затем только этот исходник скопирован в отдельный чистый каталог; build/check прошли повторно, JSON побайтно совпал. Это cold replay одного исходника, не независимая реализация доказательства. Универсальная часть дана аналитически выше; код точно проверяет полиномиальные identities,5 Bernstein coefficients, рациональные метрические сравнения, карты, actual hull/COM/mechanics и все перечисленные controls.

Окончательные pins:

    two_apex_closing.py:14264 bytes,
    SHA256 d5c213cd025888ecd8f7752dc21b0486bef1fbfc13ade07c0e1a55799d8daf3b;
    two_apex_closing.json:6089 bytes,
    SHA256 fe5d217a7bdb1a38bfa931cc1f0430758f63ee52d5ac799bd8d3997e00ff4eb5.

Ожидаемые terminal markers:

    TWO_APEX_SOS_AND_COUPLED_ENVELOPE_512_PASS
    ROOF8_3_5_LITERAL716_WHOLE_JOINT_DOMAIN_PROOF_AUDIT_PASS
    ACTUAL_ROOF_10_17_9_OWN_COM_S3_U2_H3_PASS
    TWO_APEX_CLOSING_RECOVERY_PASS 6089 fe5d217a7bdb1a38bfa931cc1f0430758f63ee52d5ac799bd8d3997e00ff4eb5

Никакой claimed exact successor не остаётся только в sandbox. Исторический или внешний приоритет, независимая экспертная проверка и proof-assistant formalization не установлены.

```python
"""TWO_APEX_FACET_CLOSING_512_V1. CPython 3.13.5, standard library.
Save this complete source with UTF-8/LF, final LF, assertions enabled.
python -S two_apex_closing.py build
python -S two_apex_closing.py check
Universal geometric proofs are in the accompanying handoff, not sampled here.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib,json,sys
assert __debug__
PARENT=['minimum-0084','77ad9a46f5f13c16d66d477e79c5ca8bbcd53f7c2b5a17819bb7a7e17481fa39']
PARENT_SOURCE=[14725,'d5d9f1904d70ed0f1ab99f6dc2cbde83c9c24779a5345d7428f16c8805df4c8d']
# These provenance pins are not external runtime dependencies.
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(a,s):return tuple(s*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def bil(a,d,b):return sum((a[i]*d[i]*b[i] for i in range(3)),F(0))
def edge(a,b):return tuple(sorted((a,b)))
# Sparse exact polynomials. Sorted variable-ID tuples are monomials.
def const(x):return {():F(x)} if x else {}
def var(i):return {(i,):F(1)}
def pa(*ps):
 d={}
 for p in ps:
  for m,c in p.items():d[m]=d.get(m,F(0))+c
 return {m:c for m,c in d.items() if c}
def pm(a,b):
 d={}
 for m,c in a.items():
  for n,e in b.items():
   k=tuple(sorted(m+n));d[k]=d.get(k,F(0))+c*e
 return {m:c for m,c in d.items() if c}
def ps(p,c):return pm(p,const(c))
def pp(p,n):
 d=const(1)
 for _ in range(n):d=pm(d,p)
 return d
def pe(p,x):
 s=F(0)
 for m,c in p.items():
  for i in m:c*=x[i]
  s+=c
 return s
def packed(p):return [[c,list(m)] for m,c in sorted(p.items())]
def polynomial_audit():
 H,T,v,m,p,r=map(var,range(6));one=const(1)
 u=pa(pp(H,2),pp(T,2));h=pp(H,2)
 I1=pa(pp(v,2),pp(m,2),pp(p,2),ps(pm(H,v),-1),ps(pm(T,m),-1),ps(p,-1))
 I2=pa(one,h,ps(pm(H,v),-1),ps(p,-1))
 Q=pa(pp(v,2),pp(m,2),ps(p,-4),const(-4))
 squares=pa(pp(pa(v,ps(H,-4)),2),pp(pa(m,ps(T,-1)),2),ps(pp(pa(p,const(-1)),2),2))
 assert pa(ps(I1,2),ps(I2,6),ps(Q,-1))==pa(squares,const(8),ps(u,-1),ps(h,-9))
 # Parameterized identity for k-p>r, r>=2.
 Qr=pa(pp(v,2),pp(m,2),ps(pm(r,p),-2),ps(pp(r,2),-1))
 sqr=pa(pp(pa(v,ps(pm(pa(r,const(2)),H),-1)),2),pp(pa(m,ps(T,-1)),2),ps(pp(pa(p,const(-1)),2),2))
 rhs=pa(sqr,pm(r,pa(r,const(2))),ps(u,-1),ps(pm(pp(pa(r,one),2),h),-1))
 assert pa(ps(I1,2),pm(pa(ps(r,2),const(2)),I2),ps(Qr,-1))==rhs
 w=var(0);den=pa(one,w,ps(pp(w,2),7));z=pa(one,ps(w,-4))
 assert pa(one,ps(pm(w,pp(pa(ps(w,4),const(-3)),2)),-1))==pm(pa(one,ps(w,-1)),pp(z,2))
 assert pa(one,ps(pp(w,2),6),ps(pp(w,3),-7))==pm(pa(one,ps(w,-1)),den)
 quartic=pa(one,ps(w,5),ps(pp(w,2),27),ps(pp(w,3),-532),ps(pp(w,4),2416))
 lhs=pa(den,ps(pm(pp(w,3),pa(den,ps(pp(z,2),9))),-64))
 assert lhs==pm(z,quartic)
 beta=[F(1),F(21,16),F(61,32),F(45,64),F(81,16)]
 bern=pa(*(ps(pm(pp(ps(w,4),i),pp(z,4-i)),beta[i]*comb(4,i)) for i in range(5)))
 assert bern==quartic and min(beta)>0
 # The two older sharp local bounds, as algebraic cross-checks.
 old=pa(den,ps(pm(pp(w,3),pp(z,2)),-2401))
 old_rhs=pm(pp(pa(ps(w,7),const(-1)),2),pa(one,ps(w,15),ps(pp(w,2),168),ps(pp(w,3),-784)))
 assert old==old_rhs
 return {'sos_multipliers':[2,6],'parameterized_sos_verified':True,
         'quartic':packed(quartic),'bernstein_on_0_to_quarter':beta,
         'strict_local_tradeoff':'a > 64*u + 576*h',
         'strict_two_apex_mass_cut':'u + 9*h > 8 + 4*delta',
         'strict_combined_cut':'a > 512 + 256*delta'}
def arithmetic_audit():
 x=F(9,4)*(F(1,10)+F(1,9));assert x==F(19,40)
 kappa=81/(1+x);product=9*kappa
 assert kappa==F(3240,59)<57 and product==F(29160,59)<513
 old=395*(F(1,64)+F(9,2401));gap=8-old
 assert old==F(1175915,153664) and gap==F(53397,153664)>0
 return {'V_F':[10,9],'exponential_argument_lower':x,'kappa_strict_upper':kappa,
         'R_J_strict_upper':product,'gap_to_513':513-product,
         'parent_395_short_proof_upper':old,'parent_395_gap_to_8':gap}
def envelope(w):return w**3*(1-4*w)**2/(1+w+7*w*w)
def local_control():
 w=F(1,5);a=F(250);u=a*w**3;s=(1-w)/w
 q=[(F(1),F(0),F(1)),(F(1),F(1),F(1)),(1-s,F(2),F(1)),(1-3*s,3-s,F(1))]
 N=(u,u*s,F(1));M=tuple(1/x for x in N);x=(F(0),F(0),F(1))
 J=[[bil(v,N,z) for z in q] for v in q];norm=[J[i][i]-1 for i in range(4)]
 assert norm==[2,10,50,250]
 arrows=[(i,j) for i in range(4) for j in range(4) if i!=j and J[i][j]>=J[i][i]]
 assert arrows==[(0,1),(1,2),(2,3)] and all(J[i][j]==J[i][i] for i,j in arrows)
 weights=[(s+1)*(s+3),s-3,s-3,F(3)]
 assert min(weights)>0 and all(sum(weights[i]*q[i][j] for i in range(4))==0 for j in (0,1))
 areas=[q[i][0]*q[(i+1)%4][1]-q[i][1]*q[(i+1)%4][0] for i in range(4)]
 assert min(areas)>0
 for i in range(4):
  d=sub(q[(i+1)%4],q[i]);e=sub(q[(i+2)%4],q[(i+1)%4])
  assert d[0]*e[1]-d[1]*e[0]>0
 c=J[0][3]-1;h=(norm[0]*norm[3]-c*c)/(norm[0]+norm[3]-2*c)
 assert h==F(2,37)==a*envelope(w)
 assert a>64*u+576*h
 direction=(F(1),F(-12),F(-1));tau=F(2,39);cases=[]
 assert all(dot(qi,x)==1 for qi in q)
 for ratio in (F(1,2),F(1),F(3,2)):
  y=add(x,scale(direction,ratio*tau));A=1-bil(x,M,y);C=bil(y,M,y)-bil(x,M,y)
  assert dot(q[0],y)==dot(q[3],y)==1 and all(dot(qi,y)<1 for qi in q[1:3])
  assert A>0 and J[0][0]>J[0][3] and J[3][3]>J[0][3]
  assert (C<0,C==0,C>0)==(ratio<1,ratio==1,ratio>1)
  D=bil(y,M,y)-bil(x,M,y)**2
  assert D>0 and A*A==h*D
  cases.append({'ratio_to_edge_foot':ratio,'y':y,'A':A,'C':C,'strict_saddle':C>0,'weak_y_to_x':C<=0})
 # Formal boundary at w=1/4, a=512: NOT a true strict normal cone.
 wb=F(1,4);ub=F(8);sb=F(3)
 qb=[(F(1),F(0),F(1)),(F(1),F(1),F(1)),(F(-2),F(2),F(1)),(F(-8),F(0),F(1))]
 Nb=(ub,ub*sb,F(1));Mb=tuple(1/v for v in Nb)
 nb=[bil(qi,Nb,qi)-1 for qi in qb];assert nb==[8,32,128,512]
 b=tuple(-Nb[j]*qb[0][j]/3 for j in range(3))
 assert bil(b,Mb,b)==1 and dot(qb[0],x)==1 and dot(qb[0],b)==-3
 assert qb[0][0]*qb[3][1]-qb[0][1]*qb[3][0]==0
 return {'scope':'LOCAL_NORMAL_CONES_AND_EDGE_CONTACTS_NOT_BOUNDED_OWN_COM_BODIES',
         'w':w,'a':a,'u':u,'s':s,'x':x,'poles':q,'M_diagonal':M,'N_diagonal':N,
         'J':J,'positive_weights':weights,'h':h,'edge_cases':cases,
         'degenerate_boundary':{'w':wb,'poles':qb,'M_diagonal':Mb,'N_diagonal':Nb,
          'x':x,'b':b,'u_values':nb,'closing_area_zero':True,'not_admissible_true_geometry':True}}
def scalar_controls():
 rows=[]
 for p,k,b,a,u,h in [(F(1,3),F(12,5),F(-19,8),F(360),F(11,2),F(7,50)),
                      (F(7,10),F(271,100),F(-541,200),F(420),F(13,2),F(17,100))]:
  delta=-p-b-2;lam=delta/(1-b);j=k*k
  assert p<1 and b<1 and -k<b and k-p>2 and k+p>2
  assert 0<lam<1 and p+b+2+lam*(1-b)==0
  assert j<1+u and u*(j-p*p)>(j-p)**2
  assert h*(j-p*p)>(1-p+h)**2
  assert a>64*u and 2401*h<a and a<440
  assert u/a>F(49,200)**3
  assert h>a*envelope(F(49,200))
  rows.append({'p':p,'k':k,'b_projection':b,'a':a,'u':u,'h':h,'delta':delta,'lambda':lam,
   'passes_mass_SOS_scalar_cut':u+9*h>8+4*delta,
   'violates_coupled_envelope_and_linear_tradeoff':a<64*u+576*h})
 assert not rows[0]['passes_mass_SOS_scalar_cut'] and rows[1]['passes_mass_SOS_scalar_cut']
 return {'scope':'FORMAL_SCALARS_ONLY_NO_COMMON_VECTORS_OR_BODY_CLAIM','rows':rows}

FACES=[(0,1,2,3,4,5,6,7),(0,8,1),(1,8,2),(3,9,4),(4,9,5),
       (5,9,6),(6,9,7),(2,8,9,3),(0,7,9,8)]
VERT=[(-2,-1,0),(-3,0,0),(-2,1,0),(2,1,0),(3,F(1,2),0),
      (F(7,2),0,0),(3,F(-1,2),0),(2,-1,0),(-1,0,1),(1,0,1)]
def geometric_roof_control():
 P=[tuple(map(F,v)) for v in VERT];normals=[];arcs={}
 for cy in FACES:
  n=cross(sub(P[cy[1]],P[cy[0]]),sub(P[cy[2]],P[cy[0]]));normals.append(n)
  assert any(n)
  for i in range(10):
   z=dot(n,sub(P[i],P[cy[0]]));assert z==0 if i in cy else z<0
  for a,b in zip(cy,cy[1:]+cy[:1]):arcs[a,b]=arcs.get((a,b),0)+1
 assert len(arcs)==34 and all(v==1 and arcs.get((b,a))==1 for (a,b),v in arcs.items())
 E=sorted({edge(a,b) for a,b in arcs});assert len(E)==17
 # Exhaust all supporting triple planes, recovering maximal facets independently.
 hull=set()
 for i,j,k in combinations(range(10),3):
  n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
  if not any(n):continue
  values=[dot(n,sub(v,P[i])) for v in P]
  if min(values)>=0 or max(values)<=0:hull.add(tuple(t for t,z in enumerate(values) if not z))
 assert hull=={tuple(sorted(cy)) for cy in FACES}
 triangles=[(f,cy[0],cy[j],cy[j+1]) for f,cy in enumerate(FACES) for j in range(1,len(cy)-1)]
 assert len(triangles)==16
 T=F(0);U=(F(0),)*3
 for f,i,j,k in triangles:
  d=det(P[i],P[j],P[k]);T+=d;U=add(U,scale(add(add(P[i],P[j]),P[k]),d))
 assert T==F(51,2);c=scale(U,1/(4*T))
 assert c==(F(19,136),F(0),F(59,204))
 X=[sub(v,c) for v in P];Q=[scale(n,1/dot(n,X[cy[0]])) for n,cy in zip(normals,FACES)]
 W=F(0);moment=(F(0),)*3
 for f,i,j,k in triangles:
  d=det(X[i],X[j],X[k]);assert d>0;W+=d
  moment=add(moment,scale(add(add(X[i],X[j]),X[k]),d))
 assert W==T and moment==(0,0,0)
 fan=[];W0=F(0);W1=F(0)
 for f,i,j,k in triangles:
  if 8 in FACES[f]:continue
  d=det(sub(P[i],P[8]),sub(P[j],P[8]),sub(P[k],P[8]));assert d>0
  fan.append([(8,i,j,k),d,f])
  if f==0:W0+=d
  else:assert 9 in (i,j,k);W1+=d
 assert W0+W1==T
 lam=W0/T;p=dot(Q[0],X[8]);b=dot(Q[0],X[9]);delta=-p-b-2
 assert lam==F(43,51) and p==b==F(-145,59) and delta==F(172,59)
 assert p+b+2+lam*(1-b)==0 and delta==lam*(1-b)>0
 G=[[dot(v,z) for z in X] for v in X];J=[[dot(v,z) for z in Q] for v in Q]
 stable=[i for i in range(9) if all(J[i][j]<J[i][i] for j in range(9) if j!=i)]
 unstable=[i for i in range(10) if all(G[i][j]<G[i][i] for j in range(10) if edge(i,j) in E)]
 saddles=[]
 for i,j in E:
  fs=[f for f,cy in enumerate(FACES) if i in cy and j in cy];assert len(fs)==2
  f,g=fs
  assert G[i][i]!=G[i][j] and G[j][j]!=G[i][j]
  assert J[f][f]!=J[f][g] and J[g][g]!=J[f][g]
  if G[i][i]>G[i][j] and G[j][j]>G[i][j] and J[f][f]>J[f][g] and J[g][g]>J[f][g]:saddles.append((i,j))
 assert all(J[i][j]!=J[i][i] for i in range(9) for j in range(9) if i!=j)
 assert stable==[0,7,8] and unstable==[1,5] and saddles==[(0,7),(2,3),(8,9)]
 assert J[0][1]-J[0][0]<0 and G[0][8]-G[0][0]<0
 return {'scope':'ACTUAL_OWN_UNIFORM_COM_ROOF_NOT_110_AND_NOT_THE_ASSIGNED_WEAK_TREES',
  'vertices':P,'faces':FACES,'edges':E,'volume':T/6,'centroid':c,'centered_vertices':X,'poles':Q,
  'M_diagonal':[1,1,1],'N_diagonal':[1,1,1],'apex8_fan':fan,'lambda':lam,'p':p,'b_projection':b,'delta':delta,
  'stable':stable,'unstable':unstable,'saddle_edges':saddles,'S_U_H':[3,2,3],'zero_true_edge_derivatives':0,
  'failed_selected_arrows':{'B_to_F1':J[0][1]-J[0][0],'vertex0_to_8':G[0][8]-G[0][0]}}
def domain_audit():
 pv=[8,2,3,4,5,6,7,0,8,3];pq=[0,0,1,2,3,4,5,0,7];mp=[5,6,8,7,2,1,0,4,3]
 E={edge(a,b) for cy in FACES for a,b in zip(cy,cy[1:]+cy[:1])}
 for i,j in enumerate(pv):
  if i!=j:assert edge(i,j) in E
 dual=[(mp[i],mp[pq[i]]) for i in range(9) if pq[i]!=i]
 assert dual==[(6,5),(8,6),(7,8),(2,7),(1,2),(0,1),(4,5),(3,4)]
 assert all(len(set(FACES[i])&set(FACES[j]))==2 for i,j in dual)
 def height(p):
  result=[]
  for i in range(len(p)):
   seen=set();k=i
   while p[k]!=k:assert k not in seen;seen.add(k);k=p[k]
   result.append(len(seen))
  assert len({i for i in range(len(p)) if p[i]==i})==1
  return max(result)
 assert height(pv)==8 and height(pq)==6
 order=[8,0,7,6,5,4,3,2,1,9];cp=[order.index(pv[v]) for v in order]
 assert cp==[0,0,1,2,3,4,5,6,7,6]
 cycle=[1,2,7,8];patterns=[]
 for start in range(4):
  for direction in (-1,1):
   path=[cycle[(start+direction*j)%4] for j in range(4)]
   common=set(FACES[path[0]])&set(FACES[path[-1]])
   assert len(common)==2 and 8 in common
   other=next(i for i in common if i!=8)
   patterns.append({'base_arrow':[0,path[0]],'pole_chain':path,'closing_edge':[8,other],
                    'leaf_contains_other_apex':9 in FACES[path[0]],
                    'argument':'both_apices_on_leaf' if 9 in FACES[path[0]] else 'mass_closing_SOS_H0'})
 assert len(patterns)==8 and sum(p['leaf_contains_other_apex'] for p in patterns)==4
 assert any(p['pole_chain']==[1,2,7,8] and p['closing_edge']==[8,0] for p in patterns)
 reflection=[2,1,0,7,6,5,4,3,8,9];fmap=[]
 for cy in FACES:
  fc={reflection[i] for i in cy};fmap.append(next(j for j,cj in enumerate(FACES) if set(cj)==fc))
 assert fmap==[0,2,1,6,5,4,3,8,7]
 pv2=[0]*10
 for i,j in enumerate(pv):pv2[reflection[i]]=reflection[j]
 assert pv2==[7,0,8,2,3,4,5,6,8,7]
 return {'identity':'ROOF8_3_5_NATIVE_DOMAIN','faces':FACES,'primal_parent':pv,
  'literal_TREE253_parent':pq,'literal_facet_to_native':mp,'native_dual_arrows':dual,
  'primal_preorder':order,'preorder_parent':cp,'ordinal716_is_inherited_rooted_tree_label':True,
  'heights':[8,6],'eight_local_forbidden_patterns':patterns,
  'reflection_vertex_map':reflection,'reflection_facet_map':fmap,'reflected_primal_parent':pv2,
  'reflected_literal_facet_to_native':[fmap[i] for i in mp],
  'scope':'FULL_CONTINUOUS_EXCLUSION_OF_THE_SPECIFIED_JOINT_DOMAIN_NOT_ALL_ROOTED716_REALIZATIONS',
  'FULL_LOCAL_census_change':'NOT_COMPUTED_NO_INTEGER_SUBTRACTION'}
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,(list,tuple)):return [encode(v) for v in x]
 if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
 return x
def build():
 out={'identity':'TWO_APEX_FACET_CLOSING_512_V1','parent':PARENT,'parent_source_pin':PARENT_SOURCE,
      'polynomial_audit':polynomial_audit(),'metric_arithmetic':arithmetic_audit(),
      'local_sharp_envelope_control':local_control(),'formal_scalar_controls':scalar_controls(),
      'actual_roof_negative_control':geometric_roof_control(),'domain':domain_audit(),
      'global_lower_C_unchanged':34,'whole_polytope_types_excluded_by_census':0}
 return (json.dumps(encode(out),sort_keys=True,separators=(',',':'))+'\n').encode()
if __name__=='__main__':
 assert sys.argv[1:] in (['build'],['check']);b=build();path=Path('two_apex_closing.json')
 if sys.argv[1]=='build':
  if path.exists():assert path.read_bytes()==b
  path.write_bytes(b)
 else:assert path.read_bytes()==b
 print('TWO_APEX_SOS_AND_COUPLED_ENVELOPE_512_PASS')
 print('ROOF8_3_5_LITERAL716_WHOLE_JOINT_DOMAIN_PROOF_AUDIT_PASS')
 print('ACTUAL_ROOF_10_17_9_OWN_COM_S3_U2_H3_PASS')
 print('TWO_APEX_CLOSING_RECOVERY_PASS',len(b),hashlib.sha256(b).hexdigest())
```

Дополнительные копии: [исходник](sandbox:/mnt/data/lynx90_next/two_apex_closing.py), [точный отчёт](sandbox:/mnt/data/lynx90_next/two_apex_closing.json), [Markdown handoff](sandbox:/mnt/data/lynx90_next/result_markdown.md). Весь код и точные входы приведены выше; загрузка файлов для восстановления не обязательна.
