# minimum-0169

AI research report · 2026-09-22 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# B_FAN_ROOT_BASE_AND_STAR_REDUCTION_V1

## 1. Главный результат

Получена структурная редукция настоящего B-веера, не требующая закона J, корневой моментной стационарности или ограничения T.

**Теорема.** Пусть P — полигедральный локальный максимум отмеченной задачи по всем допустимым телам при фиксированной ell, где a>b>0, c,d>0, корень F0 имеет положительную площадь, а A,B,C,D — настоящие вершины. Тогда:

1. **Всякая свободная грань с единственной отметкой B является треугольником BUV, и её основание UV обязательно есть настоящее минимальное G-ребро корня.** Некорневое основание и максимальное G-ребро корня невозможны.
2. **Такой одноякорный B-треугольник существует не более чем один.** Все остальные свободные B-грани содержат C или D.
3. **Если BC и BD не являются настоящими рёбрами, B автоматически образует настоящий простой корневой угол.** Никакого предварительного предположения о корневом положении её соседей не требуется.
4. **Степень настоящей вершины B не превосходит пяти.** Если обычный B-треугольник соседствует с двухотмеченной гранью BY, Y=C или D, то эта соседняя грань имеет не менее четырёх настоящих вершин и удовлетворяет строгому неравенству G(Y)<L_B, где L_B=(r+qb)/3.

В полном совместном максимуме с принятым J пункт 3 позволяет применить уже закрытый простой сектор. Поэтому

    BC,BD не рёбра  ==>  T<51/25;
    дополнительно min(G(C),G(D))<=0  ==>  T<101/50;
    дополнительно G(C),G(D)<=0       ==>  T<2.

В частности, **весь сектор двух расширенных неположительно отмеченных координатных граней закрыт с T<2**, включая формы 4/4, 4/5, 5/4 и 5/5 без прежнего дополнительного предположения о корневых B-соседях. Здесь принятая V2 и ориентация отрицательной отметки сначала исключают BC и BD; новая теорема уже сама устанавливает простой корневой угол.

Полный оставшийся непростой сектор не исключён. Но он больше не является произвольным многогранным одноякорным B-веером: остаются только строго описанные звёзды степени четыре или пять с настоящими двухотмеченными гранями. Для них дополнительно выведены согласованная совместная B/frame-реакция и точные интегральные формулы настоящего добавления B, использующие один общий веер и исходную однородную меру.

## 2. Прочитанные источники и обнаруженный конфликт памяти

Полностью прочитан новый `research-journal(20260921-214807).md`, включая всю общую память, новую память ветви и буквальный родитель до EOF. Его фактические данные:

    291334 bytes
    SHA256 6f52a736995e8e7c1af97dbc91c3eb6849b3a2e4b83afa851fd8b81057f57790

Новые переданные `b_root_corner_mixed_sign_v4.py`, `.json`, `.out` также прочитаны полностью. При выводе JSON удалялись только незначащие пробелы; все значения прочитаны последовательными полными блоками. Неизменные ранее переданные аналитические материалы остаются доступными.

**В новой памяти имеется существенный конфликт с буквальным родителем.** Парафраза называет результат B_ROOT_CORNER_SIGN_FREE_V4, приписывает ему бюджет `omega*h/6+(A0+eta)rho<=1`, 32 листа и 19522-байтный `b_root_corner_sign_free_v4.py`. Буквальный payload под требуемым assignment ID содержит другой, ранее выполненный результат: **B_ROOT_CORNER_MIXED_SIGN_V4**, бюджет `omega+(A0+eta)rho<=1`, покрытия 1042/1502 листьев и 14603-байтный исходник. Неприложенный 19522-байтный объект, приписанные ему интервалы и формулы здесь не используются.

Авторитетный родитель:

    minimum-0168
    SHA256 ecbdf93a86911ab630e405cb9f17f9bc5ab557744f0d7fa883717b6648daae83

Его идентичность подтверждена: компактный UTF-8 JSON-envelope с завершающим LF внутри result_markdown и без LF после envelope имеет 48228 байт и указанный SHA. Встроенный Python побайтово совпадает с переданным исходником:

    b_root_corner_mixed_sign_v4.py, 14603 bytes
    SHA256 52b7deee96b16fc1408c563b65dba24486fd8821000354031eacea3f9a8d3581

Именно буквальный родитель доказывает простой sign-free сектор T<51/25 и сектор одной неположительной отметки T<101/50. Его вычислительное доказательство заново не исполнялось.

Фраза памяти о корневых вершинах любого одноякорного B-веера также не использована как предпосылка. Ранее безусловно был установлен общий уровень G его вспомогательных вершин, но не их нулевая ell. Это различие является предметом нового доказательства.

## 3. Объект, зависимости и область вариаций

Используются обозначения

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    alpha=a-b>0, s=a+b,
    ell=a+(d-a)x+(c-a)y-alpha*z,
    n=(s+c)x+(s+d)y,
    V=int_P 1, E=int_P ell, N=int_P n,
    r=N/V, q=N/E, T=N/(6VE), G=n-r-q*ell.

Тело содержит T0=conv(A,B,C,D), лежит в x,y,ell>=0; Fx,Fy,F0 — полные настоящие координатные и корневая грани. Все интегралы относятся к одному равномерно заполненному P. ell не является плотностью.

Для геометрической теоремы достаточно следующих принятых условий локального максимума по всем телам при фиксированной ell:

    G(A)=-r-qa<0, G(B)=-r-qb<0;
    G>0 на всех вспомогательных настоящих вершинах;
    max_F G+3 mean_F G<=0 на каждой свободной настоящей грани;
    одноотмеченная свободная грань XUV — настоящий треугольник,
    G(U)=G(V)=-G(X)/3>0.

Это утверждения о полном классе тел, а не о фиксированной решётке граней.

Также используется двухсторонняя реакция настоящей свободной грани F при аффинном нормальном перемещении H, которое обращается в нуль на всех её канонических отметках:

    int_F G*H=0.

Другие опоры остаются фиксированными; возможное расщепление непростых вершин допустимо. Для геометрической теоремы не нужны ни root-реакции, ни B/frame-реакция, ни J. В полном отрицательно-якорном совместном максимуме предпосылку истинности всех четырёх отметок предоставляет ранее принятая отдельная теорема; здесь она записана явно, а не заменена предположением об избыточной D.

Только следствия об оценке T используют полный joint-максимум и принятый

    J: 4(u+v)<=6V+1.

Его первоначальное отдельное доказательство не приложено; он сохраняется как явно принятая предпосылка буквального родителя. Это не новый моментный закон, установленный данным результатом.

## 4. Лемма о положительном горизонтальном ребре

### 4.1. Каждая некорневая грань имеет точку с отрицательным G

Координатные грани содержат A и B с отрицательными значениями. Свободная грань также содержит отрицательную точку. Действительно, иначе G>=0 на всей грани. Поскольку только C,D могут быть неотрицательными каноническими вершинами, а настоящая грань имеет не менее трёх вершин, на ней имеется положительное значение G. Тогда `max G+3 mean G>0`, что невозможно.

### 4.2. Ребро E=[U,V] с G(U)=G(V)=L>0

Если E не лежит на корне, обе его настоящие инцидентные грани имеют отрицательную точку. На каждой из них прямая G=L совпадает с опорной прямой ребра E. Поэтому обе грани лежат в G<=L.

В относительной внутренности настоящего ребра касательный конус P порождён направлением самого ребра и двумя направлениями внутрь его инцидентных граней. На всех этих направлениях приращение G неположительно. Следовательно

    G<=L на всём P.

Более того,

    argmax_P G=E.                                      (4.1)

Максимизирующая грань не может иметь размерность два: свободная грань постоянного положительного G запрещена spike-условием; координатная содержит разные отрицательные значения G(A),G(B); на корне G=n-r непостоянна, поскольку grad ell имеет ненулевую z-компоненту, а ненулевой grad n — нулевую. Поэтому положительная максимизирующая грань, содержащая E, есть ровно это настоящее ребро.

То же заключение верно, если E лежит на корне и является максимальным G-ребром корня, а его вторая грань лежит в G<=L.

Это лемма о настоящем ребре и обеих полных инцидентных гранях. Она не применяется к диагонали интеграционной триангуляции.

## 5. Почему основание обычного B-треугольника обязано быть корневым минимумом

Пусть F_B=BUV содержит только B. Положим

    L=(r+qb)/3, K=r+L=(4r+qb)/3.

Тогда G(B)=-3L, G(U)=G(V)=L. Предположим, что UV не является минимальным G-ребром корня. Если оно некорневое, применяется лемма 4; если корневое, оно является максимальным ребром непостоянной G на корне, и применяется её последний вариант. Получаем

    argmax_P G=[U,V].                                  (5.1)

Рассмотрим другие свободные грани через B.

**Другая одноотмеченная B-грань невозможна.** Её два вспомогательных конца также имеют G=L, а по (5.1) единственные настоящие вершины с этим значением — U,V. Она совпала бы с BUV.

**Двухотмеченная грань F через B,Y, Y=C или D, невозможна.** Поскольку B,Y — настоящие вершины и вместе лежат в соответствующей координатной грани, пересечение последней с F есть настоящее ребро BY. Возьмём аффинную H>=0 на F, нулевую ровно на BY. Триангулируем весь F веером из B.

Для треугольника BRS точная формула имеет вид

    12 int_BRS G*H / Area(BRS)
      =(G(B)+G(R)+G(S))*(H(R)+H(S))
        +G(R)H(R)+G(S)H(S),

так как H(B)=0. Из G(B)=-3L и G(R),G(S)<=L следует неположительность каждого такого вклада. Треугольник BYR, инцидентный BY, даёт строго отрицательный вклад:

    H(R)*(G(B)+G(Y)+2G(R))<0,

поскольку G(Y)<L по (5.1). Значит `int_F G H<0`, вопреки полной двухсторонней hinge-реакции.

**Грань с B,C,D невозможна совместно с BUV.** Она имеет при B настоящие рёбра BC,BD. Вместе с Fx,Fy и AB они уже замыкают треугольную фигуру вершины B; других инцидентных граней быть не может.

Следовательно у B остаются ровно Fx,Fy,BUV, и её настоящие соседи — A,U,V. Рассмотрим аффинную функцию

    H_B=G-L+(4L/b)*ell=n-K+(K/b)*ell.

Она равна нулю в B, положительна в A и неотрицательна в U,V:

    H_B(A)=K*(a-b)/b>0,
    H_B(U)=(4L/b)*ell(U)>=0,
    H_B(V)=(4L/b)*ell(V)>=0.

Настоящие рёбра порождают касательный конус B, поэтому H_B>=0 на P. На корне это означает G>=L. Вместе с (5.1) получаем постоянство G=L на положительно-площадном корне — противоречие.

Итак, UV — настоящее **минимальное** G-ребро F0. Поскольку корень выпуклый и G на нём непостоянна, такое ребро единственно. Все обычные B-треугольники имели бы одно и то же основание и одну плоскость. Их не более одного.

После установления корневого основания H_B=0 уже является самой настоящей опорой BUV, а не только функцией, полученной из касательного конуса. В частности,

    H_B>=0 на P, G>=L на F0.                           (5.2)

## 6. Точная редукция оставшихся звёзд B

Любая свободная грань через B, кроме единственного возможного обычного треугольника, содержит C или D. Грань через B,C требует настоящего BC и существует не более чем одна; аналогично для BD. Грань через B,C,D делает B простой и не сосуществует с другими свободными B-гранями. Отсюда степень B<=5.

### 6.1. Сосед обычного B-треугольника обязан быть настоящим многоугольником

Пусть обычный B-треугольник BPQ соседствует по BQ с двухотмеченной гранью F_BY. На ней BY и BQ — настоящие рёбра при B. В аффинных координатах её плоскости положим

    B=(0,0), Y=(1,0), Q=(0,1).

Тогда F_BY лежит в t,v>=0, содержит треугольник BYQ, а его остальная часть лежит в t+v>=1. Имеем

    G=-3L+(G(Y)+3L)t+4Lv.

Если G(Y)>=L, на остальной части G>=L>0. Для допустимой hinge-функции H=v:

    int_BYQ G*v=Area(BYQ)*(G(Y)-L)/12>=0.

При положительной площади дополнения его вклад строго положителен. Стационарность возможна только при F_BY=BYQ и G(Y)=L. Но тогда YQ — положительное равное-G некорневое настоящее ребро. Лемма 4 делает его всей максимизирующей гранью G, хотя P — ещё одна настоящая вершина с G(P)=L. Противоречие.

Таким образом G(Y)<L. Треугольная F_BY при этом дала бы строго отрицательную hinge-реакцию, поэтому

    |F_BY|>=4, G(Y)<L.                                (6.1)

### 6.2. Какие непростые B-звёзды действительно остаются

При наличии обычного B-треугольника остаются только:

    степень 4: координаты + B-root-треугольник + один BY-многоугольник;
    степень 5: координаты + B-root-треугольник + BC- и BD-многоугольники.

Оба многоугольника во втором случае имеют не менее четырёх вершин, а G(C),G(D)<L. Без обычного B-треугольника непростота требует двух разных специальных граней BC и BD; тогда степень B равна четырём. Нельзя переносить на их общего вспомогательного B-соседа условие ell=0 или уровень G=L.

Есть также простой, но **не root-corner** остаток: одна свободная многоугольная грань BY. Он не покрывается родительской теоремой только из-за простоты B.

### 6.3. Усиление именно для расширенной отрицательной координатной грани

При G(C)<=0 полная mark-реакция и положительность вспомогательных G дают для каждой вспомогательной вершины Fx

    z>0, y+z>1.

Действительно, при z<=0 mark-support даёт y<=1 и

    G=(1-y)G(A)+yG(C)+q*alpha*z<=0.

При z<=1-y та же опора сначала даёт y<=1, после чего

    G=(1-y)G(B)+yG(C)+q*alpha*(z-1+y)<=0.

Оба случая невозможны. Поэтому вместе с V2 расширенная грань имеет порядок A,B,P,C или A,B,P,R,C; AC — настоящее ребро, BC — не ребро.

Если такая Fx расширена и B действительно непростая, новая классификация оставляет ровно степень четыре:

    соседи B: A,D,P,Q;
    BPQ — единственный обычный B-root-треугольник;
    F_BD — единственный другой свободный B-многоугольник;
    P∈Fx∩F0, Q∈F0, x(Q),y(Q)>0;
    BD — настоящее ребро, |F_BD|>=4, G(D)<L.

В смешанном случае это даёт 0<G(D)<L. Не остаётся положительно-ell вспомогательного B-соседа в этой конкретной непростой звезде: некорневой координатный сосед здесь есть каноническая D.

Если же Fx — четырёхугольник A,B,P,C с ell(P)>0, грань через BP не может быть обычной B-гранью. Она содержит D и одновременно имеет рёбра BP и BD. Фигура вершины замыкается, так что **B проста**, но её свободная грань — специальный BD-многоугольник, не родительский root-corner. Это отдельный оставшийся случай, а не скрытое применение оценки простого корневого угла.

## 7. Новые согласованные реакции полного B-веера

Эти формулы действуют и в оставшихся звёздах с многоугольниками. Они не заменяют их независимыми конусными массами.

### 7.1. Настоящая совместная вариация всех B-плоскостей

Каждая свободная B-грань не содержит A и имеет единственную нормировку опоры

    f_F=1-p_F*x-q_F*y-z>=0.

Одновременно заменим все такие опоры на

    f_F+delta*(1-x-y)>=0,

оставив остальные настоящие опоры, включая физическую ell, фиксированными. Все новые B-плоскости проходят через B_delta=(0,0,1+delta). Канонические C,D сохраняют прежние значения каждой опоры, поскольку 1-x-y=0 в них. Малые параметры обоих знаков допустимы; изменения решётки в других непростых вершинах разрешены.

Пусть S=int_P(x+y), psi=1-x-y. Настоящие производные равномерных интегралов равны

    Vdot=sum_B-facets int_F psi/|grad f_F|,
    Jdot=sum_B-facets int_F X*psi/|grad f_F|,
    Edot=sum_B-facets int_F ell*psi/|grad f_F|,
    Ndot=sum_B-facets int_F n*psi/|grad f_F|.

После правильного восстановления z'=z/(1+delta):

    T_delta=(1+delta)*(N_delta-alpha*delta*S_delta)
              /(6*V_delta*E_delta).

Следовательно в полном joint-максимуме

    V*(r-alpha*p)
      +sum_B-facets int_F G*(1-x-y)/|grad f_F|=0.        (7.1)

Это равенство не предполагает простоту B. Для обычного B-root-треугольника его слагаемое равно -L*W_o, где W_o=Vol(ABPQ). Для специальной BD-грани hinge-реакция позволяет заменить 1-x-y на 1-x; но её вклад не равен автоматически -L, умноженному на объём.

Сами производные имеют согласованное объёмное представление. Пусть U_B — объединение различных пирамид conv(A,F) по всем свободным B-граням, а

    W_B=int_UB 1, J_B=int_UB X, M_B=int_UB X X^T,
    e_s=(1,1,0).

Это части одного настоящего A-веера. Конирование однородных полиномов даёт

    Vdot=3W_B-4 e_s·J_B,
    Jdot=4J_B-5M_B e_s,
    gdot=(Jdot-g*Vdot)/V.                              (7.2)

Edot и Ndot получаются из этих же Vdot,Jdot по исходным аффинным ell,n. В частности, M_B не является свободно выбираемой ковариацией. Проверитель независимо сверяет производные настоящих вершин/объёмных вееров с граничными интегралами на контрольном непростом теле.

### 7.2. Точное настоящее добавление внешней B

Для delta>0 возьмём другой конкурент

    P_delta=conv(P,B_delta).

При достаточно малой delta видимы ровно полные свободные B-грани. Добавленная область — объединение пирамид с этими полными основаниями и вершиной B_delta, с непересекающимися внутренностями. Положим для того же U_B

    E_B=int_UB ell, N_B=int_UB n, S_B=int_UB(x+y).

Тогда ТОЧНО

    V_delta=V+delta*W_B,
    E_delta=E+delta*(E_B-alpha*W_B/4)-alpha*W_B*delta^2/4,
    N_delta=N+delta*N_B,
    S_delta=S+delta*S_B.                               (7.3)

В полном максимуме односторонняя производная удовлетворяет

    V*(r-alpha*p)+N_B-rW_B-qE_B+q*alpha*W_B/4<=0.        (7.4)

Неравенство (7.4) и равенство (7.1) относятся к РАЗНЫМ настоящим конкурентам. Превращать первое в равенство или заменять полный многоугольник независимым интеграционным треугольником нельзя.

### 7.3. Где именно перестаёт работать старая простая формула

Если основание обычного B-треугольника — PQ на n=K, зададим порядок x(P)<x(Q) и

    theta=(h_x/K)*(x(Q)-x(P)), 0<theta<=1.

Из настоящего определителя

    W_o=theta*K^2/(6*h_x*h_y).                         (7.5)

theta=1 ровно при двух координатных концах P,Q, то есть в простом корневом угле. В оставшемся B4 или B5 theta<1. Это реальная ширина одного корневого ребра, не назначаемая масса.

Общие root-volume и root-n бюджеты для A-root-пирамиды и ABPQ сохраняются. Однако прежнее `W_o/V=(r-alpha*p)/L` заменено (7.1) со специальными гранными слагаемыми, а полный определитель — (7.5). Поэтому старые трёхпараметрические сертификаты нельзя перенести на непростую звезду подстановкой независимого theta или произвольных масс специальных граней.

## 8. Настоящие контрконтроли и точная граница локального метода

### 8.1. Рациональное непростое тело и настоящая возрастающая B-дуга

Положим

    a=1, b=1/5, c=1/4, d=1/100,
    ell=1-99x/100-3y/4-4z/5,
    n=29x/20+121y/100.

Рассмотрим семейство с параметром K и семью опорами

    x,y,z>=0,
    ell>=0,
    1+(29/(80K)-99/80)x+(121/(400K)-15/16)y-z>=0,
    1-x-z>=0,
    1-x-y+z>=0.

Все восемь вершин в постоянном порядке:

    0=A, 1=B, 2=C, 3=D,
    4=(0,100K/121,5/4-375K/484),
    5=(0,36/31,5/31),
    6=((1875K-605)/2144,(725-475K)/2144,(2749-1875K)/2144),
    7=(130/131,2/131,1/131).

При K=6/5 полные настоящие грани:

    (4,1,0,2,5), (1,0,3), (2,0,3),
    (1,3,7,6), (1,6,4), (5,7,3,2), (4,6,7,5).

Это настоящее 8/13/7, Fx — пятиугольник, Fy — треугольник, B имеет степень четыре и соседей A,D,4,6. Основание обычного B-треугольника — корневое ребро 4–6, но его конец 6 не лежит на Fy. Таким образом один защищённый пятиугольник и наличие B-root-треугольника сами по себе не доказывают простоту B.

Выполнены G(C)<0<G(D), G>0 на всех вспомогательных вершинах и обе mark-support реакции. Точные общие интегралы:

    V=1494161617/6321125184,
    E=14289694391/210704172800,
    N=155263282405549/855669645740800,
    T=40279021774777143776/21351112877692390247.

Оба положительных объёмных веера из A и B совпадают. Тело не стационарно. При настоящем добавлении B_delta с 0<delta<=1/1000 и правильном восстановлении рамки T строго возрастает на всём указанном интервале. Это проверено положительными коэффициентами точного квадратичного полинома после деления разности на delta, а не выборкой параметров.

В конце интервала истинное тело имеет 8/14/8; старая BD-четырёхугольная грань действительно меняется, а не сохраняется по имени. Правильный новый след:

    T_child=377939766052768263965795174/200325798169242572469367281.

Новый конец b равен 249/1250. Все физические и канонические моменты восстанавливаются исходником; центр не удерживается искусственно на прежнем месте.

### 8.2. Алгебраический спутник с ТОЧНО жёстким обычным B-треугольником

В том же настоящем семействе определим K* как единственный корень в

    [12017/10000,6009/5000]

следующего полного полинома:

    6131550199676513671875 K^5
    -3956893728857910156250 K^4
    +332455851577869928906250 K^3
    -642662972390564023525000 K^2
    -6951661358969333031847525 K
    +8698210862310042899357642.

Противоположные знаки на концах и строго отрицательная производная на всём интервале удостоверены точно. При K*:

    G(B)+3G(4)=0, G(4)=G(6), ell(4)=ell(6)=0.

Поэтому ВСЕ mark-fixing affine hinge-реакции обычного B-треугольника и его первое spike-условие выполнены точно. Тем не менее B остаётся непростой степени четыре. Следовательно даже точная локальная жёсткость одной обычной B-root-грани не заменяет анализ остальных B-граней.

Это настоящий алгебраический многогранник, не формальная таблица моментов. Его общие объёмные интегралы задаются

    V(K)=-(190359375K^2-122845250K-1620864817)/6321125184,
    E(K)=-(951796875K^2-614226250K-43502599173)/632112518400,
    N(K)=-(12884157031250K^3-6235932003125K^2-168547363671049)
          /855669645740800.

Подставляется один и тот же K*. Все координаты, полный первый момент и T=N/(6VE) даны восстанавливающим кодом.

На всём замкнутом изолирующем интервале проверены постоянство всех нетривиальных ориентированных тетраэдральных знаков, настоящая решётка 8/13/7, знаки G и mark-supports: 268 полиномиальных проверок, 576 строго положительных коэффициентов Бернштейна. При этом

    G(D)>G(4)=L,
    int_FBD G*y/|grad(1-x-z)|>0.

Значит полная BD-hinge-реакция нарушена. Небольшая настоящая замена `1-x-z>=0` на `1-x-z+epsilon*y>=0` с положительной epsilon повышает след уже при фиксированных канонических точках и ell. Этот объект НЕ является полным joint-максимумом и не опровергает теорему раздела 1.

### 8.3. Локальная BD-четырёхугольная реакция не даёт оставшегося запрета сама по себе

Для настоящего выпуклого четырёхугольника BYRQ в описанных координатах положим

    ell(B)=b, ell(Y)=delta*b, ell(Q)=ell(R)=0,
    Q=(0,1), R=(t,v), v=1+(delta-1)t>0,
    G(B)/L=-3, G(Y)/L=g,
    Acoef=g-1+4delta>0, G(R)/L=1+Acoef*t.

Здесь Acoef — локальный коэффициент, не каноническая вершина A. Очищенный whole-hinge равен

    H=v^2*(g-1+2*Acoef*t)+Acoef*t^2*(2v+1).

Очищенный spike-остаток равен

    S=v*(g-1+2*Acoef*t)+2*Acoef*t^2,
    H=v*S+Acoef*t^2.

Поэтому при H=0 имеем S<0: spike-условие, напротив, строго выполнено.

Точный выпуклый планарный контроль:

    B=(0,0), Y=(1,0), R=(1/2,11/20), Q=(0,1),
    ell=(1,1/10,0,0) на этих вершинах,
    G=(-3,799/1130,2381/2260,1).

Для него

    Area=21/40,
    int G=-52201/271200,
    int G*v=0,
    max G+3 mean G=-110/2373<0.

Это подлинная выпуклая плоская грань с двумя согласованными аффинными функциями. Она НЕ объявляется объёмной реализацией заданных G=n-r-qell. Она показывает точную границу чисто локального hinge/spike-подхода к оставшемуся BD-четырёхугольнику; теперь нужно использовать глобальные настоящие моменты или другие соседние грани.

## 9. Что осталось и как продолжать

Произвольная множественность обычных B-граней, их некорневые основания и корневые максимальные основания исключены аналитически. Весь одноякорный B-веер сводится к закрытому простому корневому углу. Это закрывает, в частности, обе расширенные неположительно отмеченные координатные грани без дополнительных корневых предположений.

Оставшаяся настоящая задача — специальные двухотмеченные B-многоугольники: B4 с обычным корневым треугольником и одним BY-многоугольником; B5 с двумя такими многоугольниками; B4 без обычного треугольника с двумя специальными гранями; и простой специальный, но не root-corner случай. Нулевые ell-концы и избыточные отметки вне явно заданных предпосылок не включены.

Самый полезный следующий шаг — соединить точную совместную реакцию (7.1) и общий моментный тензор (7.2) с root-реакциями на B4/B5, сохраняя настоящий theta и специальные гранные интегралы. Четырёхугольный контроль раздела 8.3 показывает, почему повторения локального spike-теста недостаточно.

Механические S/U/H и слабые пакеты новых тел не вычислялись. Ни одно из них не объявляется 110. Никаких изменений C_min, FULL/LOCAL-регистра или границ 34<=C_min<=622 не следует; полного исключения всех 10/17/9-реализаций нет.

## 10. Полная recovery capsule

Новый исходник самодостаточен. Он восстанавливает рациональное тело, настоящую возрастающую B-дугу и её конечный hull, независимые объёмные веера, совместную B-plane производную, точный алгебраический спутник и локальный выпуклый четырёхугольник. Родительский Python не импортируется.

Среда авторского исполнения: CPython 3.13.5, SymPy 1.14.0, assertions включены. Обычный запуск и отдельный source-only запуск в новой директории выполнены; JSON и stdout совпали побайтово. Аналитическая структурная теорема не выводится из этих контролей и не объявляется proof-assistant-проверенной.

    b_fan_root_reduction_v1.py
    16385 bytes
    SHA256 a8ebfc768d5fc6b2d5951fab77d4b64486e94b6f587f01dbd36ac0577a1ee5d8

    b_fan_root_reduction_v1.json
    30780 bytes
    SHA256 e31e1d55c0317468a2223dfba3bb49f0a572b0ceedb417750ea37b2f9a227a14

    b_fan_root_reduction_v1.out
    527 bytes
    SHA256 c654a70960681f3fa30bc96fde3703a9b99a30020c6a2548332fb6938a24309d

Команды:

    python b_fan_root_reduction_v1.py > b_fan_root_reduction_v1.out
    sha256sum b_fan_root_reduction_v1.py b_fan_root_reduction_v1.json b_fan_root_reduction_v1.out

Полный ожидаемый stdout:


[Encoded source block omitted; the code in this passage is incomplete.]

    SPECIAL_BD_HINGE_POSITIVE_NOT_A_FULL_MAXIMUM_PASS
    LOCAL_CONVEX_QUAD_ZERO_HINGE_NEGATIVE_SPIKE_NOT_A_BODY_PASS
    report_bytes=30780
    report_sha256=e31e1d55c0317468a2223dfba3bb49f0a572b0ceedb417750ea37b2f9a227a14
    B_FAN_ROOT_REDUCTION_V1_RECOVERY_PASS

Дополнительные копии: исходник (`b_fan_root_reduction_v1.py`), точный отчёт (`b_fan_root_reduction_v1.json`), stdout (`b_fan_root_reduction_v1.out`). Полный восстанавливающий источник включён далее.

```python
#!/usr/bin/env python3
"""B_FAN_ROOT_REDUCTION_V1. CPython 3.13.5, SymPy 1.14.0.
Parent minimum-0168:
ecbdf93a86911ab630e405cb9f17f9bc5ab557744f0d7fa883717b6648daae83.
Standalone actual nonsimple body, algebraic B-rigid companion, and real B arcs.
The structural theorem is analytic; these computations are controls, not 110.
"""
from fractions import Fraction as Q
from itertools import combinations
from functools import cmp_to_key
from math import comb
from pathlib import Path
import hashlib
import json
import sympy as S


def dot(a,b): return sum((x*y for x,y in zip(a,b)),Q(0))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def rat(x):
    x=S.Rational(x)
    return Q(int(x.p),int(x.q))


def face_order(pts,ids,normal):
    axes=[i for i in range(3) if i!=next(j for j in range(3) if normal[j])]
    cen=[sum(pts[i][j] for i in ids)/len(ids) for j in axes]
    vec={i:tuple(pts[i][j]-c for j,c in zip(axes,cen)) for i in ids}
    def half(v): return int(v[1]<0 or (v[1]==0 and v[0]<0))
    def cmp(i,j):
        a,b=vec[i],vec[j]
        if half(a)!=half(b): return -1 if half(a)<half(b) else 1
        d=a[0]*b[1]-a[1]*b[0]
        assert d!=0 or i==j
        return -1 if d>0 else (1 if d<0 else 0)
    return tuple(sorted(ids,key=cmp_to_key(cmp)))


def hull(pts):
    found={}
    for i,j,k in combinations(range(len(pts)),3):
        n=cross(sub(pts[j],pts[i]),sub(pts[k],pts[i]))
        if not any(n): continue
        b=dot(n,pts[i]); ss=[b-dot(n,p) for p in pts]
        if min(ss)<0<max(ss): continue
        ids=tuple(i for i,s in enumerate(ss) if s==0)
        found.setdefault(ids,n)
    cycles=[face_order(pts,ids,found[ids]) for ids in sorted(found)]
    edges={tuple(sorted((f[j-1],f[j]))) for f in cycles for j in range(len(f))}
    assert edges=={tuple(sorted(set(f)&set(g))) for f,g in combinations(cycles,2)
                   if len(set(f)&set(g))==2}
    assert len(pts)-len(edges)+len(cycles)==2
    for i in range(len(pts)):
        normals=[n for f,n in found.items() if i in f]
        assert any(det(*ns)!=0 for ns in combinations(normals,3))
    return cycles,sorted(edges)


def fan(pts,cycles,apex=0,only=None):
    V=Q(0); J=[Q(0)]*3
    for f in cycles:
        if apex in f or (only is not None and frozenset(f) not in only): continue
        for j in range(1,len(f)-1):
            ids=(apex,f[0],f[j],f[j+1])
            w=abs(det(*(sub(pts[i],pts[apex]) for i in ids[1:])))/6
            assert w>0
            V+=w
            for k in range(3): J[k]+=w*sum(pts[i][k] for i in ids)/4
    return V,tuple(J)


def law(V,J):
    E=V-Q(99,100)*J[0]-Q(3,4)*J[1]-Q(4,5)*J[2]
    N=Q(29,20)*J[0]+Q(121,100)*J[1]
    return E,N


def ell(p): return 1-Q(99,100)*p[0]-Q(3,4)*p[1]-Q(4,5)*p[2]
def nn(p): return Q(29,20)*p[0]+Q(121,100)*p[1]


def points(K):
    return [(Q(0),Q(0),Q(0)),(Q(0),Q(0),Q(1)),
            (Q(0),Q(1),Q(0)),(Q(1),Q(0),Q(0)),
            (Q(0),100*K/121,Q(5,4)-375*K/484),
            (Q(0),Q(36,31),Q(5,31)),
            ((1875*K-605)/2144,(725-475*K)/2144,(2749-1875*K)/2144),
            (Q(130,131),Q(2,131),Q(1,131))]


def slacks(K):
    return [(Q(0),(Q(1),Q(0),Q(0))),(Q(0),(Q(0),Q(1),Q(0))),
            (Q(0),(Q(0),Q(0),Q(1))),
            (Q(1),(-Q(99,100),-Q(3,4),-Q(4,5))),
            (Q(1),(Q(29,80)/K-Q(99,80),Q(121,400)/K-Q(15,16),-Q(1))),
            (Q(1),(-Q(1),Q(0),-Q(1))),
            (Q(1),(-Q(1),-Q(1),Q(1)))]


EXPECTED_FACES=[(0,1,2,4,5),(0,1,3),(0,2,3),(1,3,6,7),
                (1,4,6),(2,3,5,7),(4,5,6,7)]


def integrate_face(pts,f,values,other=None):
    # For all B faces the normalized plane has z coefficient -1: dA/k=dxdy.
    ans=Q(0)
    for j in range(1,len(f)-1):
        ids=(f[0],f[j],f[j+1]); a,b,c=(pts[i] for i in ids)
        area=abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))/2
        if other is None: ans+=area*sum(values[i] for i in ids)/3
        else:
            ans+=area*(sum(values[i] for i in ids)*sum(other[i] for i in ids)
                       +sum(values[i]*other[i] for i in ids))/12
    return ans


def solve3(ns,rhs):
    d=det(*ns); assert d
    cc=(cross(ns[1],ns[2]),cross(ns[2],ns[0]),cross(ns[0],ns[1]))
    return tuple(sum(rhs[i]*cc[i][j] for i in range(3))/d for j in range(3))


def coordinated_B_derivative(pts,cycles):
    ss=slacks(Q(6,5)); velocities=[]
    for p in pts:
        act=[i for i,(b,n) in enumerate(ss) if b+dot(n,p)==0]
        ids=next(t for t in combinations(act,3) if det(*(ss[i][1] for i in t)))
        rhs=[-(1-p[0]-p[1]) if i in (4,5) else Q(0) for i in ids]
        vel=solve3([ss[i][1] for i in ids],rhs)
        assert all(dot(ss[i][1],vel)+(1-p[0]-p[1] if i in (4,5) else 0)==0 for i in act)
        velocities.append(vel)
    assert velocities[1]==(0,0,1) and velocities[0]==velocities[2]==velocities[3]==(0,0,0)
    dV=Q(0);dJ=[Q(0)]*3
    for f in cycles:
        if 0 in f: continue
        for j in range(1,len(f)-1):
            ids=(0,f[0],f[j],f[j+1]); tri=[pts[i] for i in ids[1:]]
            dtri=[velocities[i] for i in ids[1:]]
            d=det(*tri); sg=1 if d>0 else -1; w=sg*d/6
            dw=sg*(det(dtri[0],tri[1],tri[2])+det(tri[0],dtri[1],tri[2])
                   +det(tri[0],tri[1],dtri[2]))/6
            dV+=dw
            for k in range(3):
                dJ[k]+=dw*sum(pts[i][k] for i in ids)/4+w*sum(velocities[i][k] for i in ids)/4
    dE,dN=law(dV,dJ)
    psi=[1-p[0]-p[1] for p in pts]
    bf=[f for f in cycles if 1 in f and 0 not in f]
    checks=[sum(integrate_face(pts,f,psi) for f in bf),
            sum(integrate_face(pts,f,list(map(ell,pts)),psi) for f in bf),
            sum(integrate_face(pts,f,list(map(nn,pts)),psi) for f in bf)]
    assert checks==[dV,dE,dN]
    return {'velocities':[list(map(str,v)) for v in velocities],
            'dV':str(dV),'dJ':list(map(str,dJ)),'dE':str(dE),'dN':str(dN)}


def bern(expr,x,lo,hi,sign=1):
    p=S.Poly(S.expand(expr),x)
    if p.is_zero: return None
    u=S.symbols('_u'); q=S.Poly(S.expand(expr.subs(x,S.Rational(lo)+(S.Rational(hi)-S.Rational(lo))*u)),u)
    n=q.degree(); co=[rat(q.nth(i)) for i in range(n+1)]
    b=[sum((co[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)),Q(0))*sign
       for i in range(n+1)]
    assert min(b)>0,('BAD_BERNSTEIN_GUARD',str(expr),b)
    return {'degree':n,'minimum':str(min(b))}


def rational_control():
    pts=points(Q(6,5)); cc,edges=hull(pts)
    assert sorted(tuple(sorted(f)) for f in cc)==EXPECTED_FACES
    V,J=fan(pts,cc,0); assert (V,J)==fan(pts,cc,1)
    E,N=law(V,J);r=N/V;q=N/E;T=N/(6*V*E)
    assert (V,E,N)==(Q(1494161617,6321125184),Q(14289694391,210704172800),
                    Q(155263282405549,855669645740800))
    G=[nn(p)-r-q*ell(p) for p in pts]
    assert G[2]<0<G[3] and min(G[4:])>0 and G[4]==G[6]
    assert {j for e in edges if 1 in e for j in e if j!=1}=={0,3,4,6}
    assert all(ell(pts[i])==0 for i in (4,5,6,7))
    for axis,end in ((1,Q(1,4)),(0,Q(1,100))):
        assert max((Q(1,5)+2*end)*(p[axis]-1)-Q(4,5)*p[2]
                   for p in pts if p[1-axis]==0)==0
    star={frozenset(f) for f in cc if 1 in f and 0 not in f}
    W,Jstar=fan(pts,cc,0,star); Estar,Nstar=law(W,Jstar); Sstar=sum(Jstar[:2])
    ds=Q(1,1000); child=pts.copy();child[1]=(Q(0),Q(0),1+ds)
    cf,ce=hull(child);V1,J1=fan(child,cf,0);assert (V1,J1)==fan(child,cf,1)
    E1,N1=law(V1,J1);ss=sum(J[:2]);ss1=sum(J1[:2]);alpha=Q(4,5)
    assert V1==V+ds*W
    assert E1==E+ds*(Estar-alpha*W/4)-alpha*W*ds*ds/4
    assert N1==N+ds*Nstar and ss1==ss+ds*Sstar
    T1=(1+ds)*(N1-alpha*ds*ss1)/(6*V1*E1)
    assert T==Q(40279021774777143776,21351112877692390247)
    assert T1==Q(377939766052768263965795174,200325798169242572469367281)
    assert (len(child),len(ce),len(cf))==(8,14,8) and T1>T
    delta=S.symbols('delta'); sd=lambda v:S.Rational(v.numerator,v.denominator)
    vp=sd(V)+delta*sd(W)
    ep=sd(E)+delta*sd(Estar-alpha*W/4)-delta**2*sd(alpha*W/4)
    np=sd(N)+delta*sd(Nstar);sp=sd(ss)+delta*sd(Sstar)
    gap=S.expand((1+delta)*(np-sd(alpha)*delta*sp)-sd(N/(V*E))*vp*ep)
    quotient=S.Poly(gap,delta).exquo(S.Poly(delta,delta)).as_expr()
    guard=bern(quotient,delta,Q(0),ds)
    jd=coordinated_B_derivative(pts,cc)
    deriv= N-alpha*ss+rat(jd['dN'])-r*rat(jd['dV'])-q*rat(jd['dE'])
    return {'input_K':'6/5','endpoints':['1','1/5','1/4','1/100'],
            'vertices':[list(map(str,p)) for p in pts],
            'facets':[list(f) for f in cc],'edges':[list(e) for e in edges],
            'f_vector':[8,13,7],'V':str(V),'J':list(map(str,J)),
            'g':[str(v/V) for v in J],'E':str(E),'N':str(N),'T':str(T),
            'G':list(map(str,G)),'B_rigidity_defect':str(G[1]+3*G[4]),
            'A_star':{'W':str(W),'E':str(Estar),'N':str(Nstar),'S':str(Sstar)},
            'coordinated_B_planes':jd,'joint_B_derivative_numerator':str(deriv),
            'outward_child':{'delta':str(ds),'vertices':[list(map(str,p)) for p in child],
               'facets':[list(f) for f in cf],'edges':[list(e) for e in ce],
               'f_vector':[8,14,8],'physical_V':str(V1),'physical_E':str(E1),
               'physical_N_old':str(N1),'physical_J':list(map(str,J1)),
               'canonical_T':str(T1),'trace_gain':str(T1-T),
               'whole_interval_positive_trace_quotient':guard},
            'status':'actual uniform nonsimple B control and real ascent; mechanics not audited'}


def algebraic_control():
    K=S.symbols('K');P=[S.Matrix([S.Rational(x) if not isinstance(x,S.Basic) else x for x in p])
                        for p in points(K)]
    assert all(S.factor(ell(P[i]))==0 for i in (4,5,6,7))
    assert S.factor(nn(P[4])-K)==S.factor(nn(P[6])-K)==0
    seed=points(Q(6,5));cc,edges=hull(seed)
    V=S.Integer(0);J=S.zeros(3,1)
    for f in cc:
        if 0 in f: continue
        for j in range(1,len(f)-1):
            ids=(0,f[0],f[j],f[j+1]);d=S.det(S.Matrix.hstack(*(P[i] for i in ids[1:])))/6
            sg=S.sign(d.subs(K,S.Rational(6,5)));w=sg*d
            V+=w;J+=w*sum((P[i] for i in ids),S.zeros(3,1))/4
    V=S.factor(V);J=J.applyfunc(S.factor);E,N=map(S.factor,law(V,list(J)))
    assert S.factor(V+(190359375*K**2-122845250*K-1620864817)/S.Integer(6321125184))==0
    assert S.factor(E+(951796875*K**2-614226250*K-43502599173)/S.Integer(632112518400))==0
    assert S.factor(N+(12884157031250*K**3-6235932003125*K**2-168547363671049)/S.Integer(855669645740800))==0
    gp=[S.factor(nn(p)*V*E-N*E-N*V*ell(p)) for p in P]
    numer=S.fraction(S.factor(3*K*V*E-4*N*E-Q(1,5)*N*V))[0]
    pol=S.Poly(numer,K).primitive()[1]
    if pol.LC()<0: pol=-pol
    expected=[6131550199676513671875,-3956893728857910156250,
              332455851577869928906250,-642662972390564023525000,
              -6951661358969333031847525,8698210862310042899357642]
    assert list(map(int,pol.all_coeffs()))==expected
    lo=Q(12017,10000);hi=Q(6009,5000);mid=(lo+hi)/2
    assert pol.eval(S.Rational(lo))>0>pol.eval(S.Rational(hi))
    guards=[]
    def check(expr,sign=1):
        out=bern(S.expand(expr),K,lo,hi,sign)
        if out is not None: guards.append(out)
    check(-pol.diff().as_expr())
    # Every tetrahedral orientation stays constant on the FULL closed interval.
    for ids in combinations(range(8),3):
        for j in range(8):
            if j in ids: continue
            a,b,c=(P[i] for i in ids)
            ex=S.expand(S.det(S.Matrix.hstack(b-a,c-a,P[j]-a)))
            if ex==0: continue
            check(ex,int(S.sign(ex.subs(K,S.Rational(mid)))))
    check(V);check(E);check(N)
    check(gp[2],-1);check(gp[3])
    for i in range(4,8): check(gp[i])
    check(gp[3]-gp[4])
    for i in (5,7): check(nn(P[i])-K)
    for axis,end in ((1,Q(1,4)),(0,Q(1,100))):
        for p in P:
            if p[1-axis]==0:
                ex=S.expand((Q(1,5)+2*end)*(p[axis]-1)-Q(4,5)*p[2])
                if ex!=0:check(ex,-1)
    F=next(f for f in cc if set(f)=={1,3,6,7})
    hinge=S.Integer(0)
    for j in range(1,len(F)-1):
        ids=(F[0],F[j],F[j+1]);aa,bb,ccc=(P[i] for i in ids)
        ar=((bb[0]-aa[0])*(ccc[1]-aa[1])-(bb[1]-aa[1])*(ccc[0]-aa[0]))/2
        ar*=S.sign(ar.subs(K,S.Rational(mid)))
        yy=[P[i][1] for i in ids];gg=[gp[i] for i in ids]
        hinge+=ar*(sum(yy)*sum(gg)+sum(x*y for x,y in zip(yy,gg)))/12
    check(hinge)
    assert S.factor(gp[1]+3*gp[4]-(3*K*V*E-4*N*E-Q(1,5)*N*V))==0
    return {'definition':'K* is the unique root of the displayed polynomial in the closed interval',
            'interval':[str(lo),str(hi)],'polynomial_high_to_low':expected,
            'P_at_lo':str(pol.eval(S.Rational(lo))),'P_at_hi':str(pol.eval(S.Rational(hi))),
            'vertices_as_functions_of_K':[[str(x) for x in p] for p in P],
            'facets':[list(f) for f in cc],'f_vector':[8,13,7],
            'V':str(V),'J':[str(x) for x in J],'E':str(E),'N':str(N),
            'T':str(S.factor(N/(6*V*E))),'BD_hinge_times_VE':str(S.factor(hinge)),
            'guard_count':len(guards),'positive_coefficients':sum(g['degree']+1 for g in guards),
            'guards':guards,'B_rigidity_exact':True,'special_BD_hinge_strictly_positive':True,
            'status':'actual algebraic nonsimple body; ordinary B facet rigid; NOT a full joint maximum'}


def analytic_algebra():
    A,B,r,q,L,dV,dE,dN,V,E,N,alpha,ss=S.symbols('A B r q L dV dE dN V E N alpha ss')
    z=S.symbols('z')
    vp=V+z*dV
    ep=E+z*(dE-alpha*dV/4)-alpha*dV*z*z/4
    np=N+z*dN
    f=(1+z)*(np-alpha*z*ss)-N*vp*ep/(V*E)
    der=S.diff(f,z).subs(z,0).subs({N:r*V,E:r*V/q})
    assert S.factor(der-(r*V-alpha*ss+dN-r*dV-q*dE+q*alpha*dV/4))==0
    gY,t,delta=S.symbols('gY t delta')
    vv=1+(delta-1)*t;aa=gY-1+4*delta;R=1+aa*t
    hinge=vv**2*(-3+gY+2*R)+t*(R-1)*(2*vv+1)
    spike=vv*(gY-1+2*aa*t)+2*aa*t*t
    assert S.factor(hinge-vv*spike-aa*t*t)==0
    return {'outward_B_union_exact_integral_identity':True,
            'quadrilateral_hinge_minus_v_times_spike':'(gY-1+4*delta)*t^2',
            'structural_theorem':'analytic proof, not inferred from these controls'}


def local_quad_control():
    p=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1,2),Q(11,20)),(Q(0),Q(1))]
    g=[-Q(3),Q(799,1130),Q(2381,2260),Q(1)]
    ellv=[Q(1),Q(1,10),Q(0),Q(0)]
    for i in range(4):
        a,b,c=p[i-1],p[i],p[(i+1)%4]
        assert (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])>0
    assert all(1-Q(9,10)*x-y==h for (x,y),h in zip(p,ellv))
    assert all(-3+(g[1]+3)*x+4*y==z for (x,y),z in zip(p,g))
    area=I=hinge=Q(0)
    for ids in ((0,1,2),(0,2,3)):
        a,b,c=(p[i] for i in ids)
        ar=((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))/2
        area+=ar;I+=ar*sum(g[i] for i in ids)/3
        hinge+=ar*(sum(g[i] for i in ids)*sum(p[i][1] for i in ids)
                   +sum(g[i]*p[i][1] for i in ids))/12
    gap=max(g)+3*I/area
    assert hinge==0 and gap==-Q(110,2373)
    return {'vertices':[list(map(str,v)) for v in p],'G':list(map(str,g)),
            'ell':list(map(str,ellv)),'area':str(area),'integral_G':str(I),
            'integral_G_transverse':'0','spike_gap':str(gap),
            'status':'GENUINE PLANAR CONVEX FACET CONTROL; not a uniform 3D moment realization'}


def main():
    report={'version':1,'parent_assignment':'minimum-0168',
            'algebra':analytic_algebra(),'local_quad_control':local_quad_control(),
            'rational_control':rational_control(),
            'algebraic_control':algebraic_control()}
    raw=(json.dumps(report,sort_keys=True,ensure_ascii=True,indent=2)+'\n').encode()
    Path('b_fan_root_reduction_v1.json').write_bytes(raw)
    c=report['algebraic_control']
    print('ACTUAL_NONSIMPLE_B4_8_13_7_TWO_POSITIVE_VOLUME_FANS_PASS')
    print('COMMON_B_PLANE_VARIATION_TRUE_VOLUME_FIRST_MOMENT_DERIVATIVE_PASS')
    print('WHOLE_OUTWARD_B_INTERVAL_ASCENT_AND_8_14_8_ENDPOINT_PASS')
    print('ALGEBRAIC_B_RIGID_NONSIMPLE_COMPANION_UNIQUE_ROOT_PASS')
    print('interval_guards='+str(c['guard_count'])+' positive_coefficients='+str(c['positive_coefficients']))
    print('SPECIAL_BD_HINGE_POSITIVE_NOT_A_FULL_MAXIMUM_PASS')
    print('LOCAL_CONVEX_QUAD_ZERO_HINGE_NEGATIVE_SPIKE_NOT_A_BODY_PASS')
    print('report_bytes='+str(len(raw)))
    print('report_sha256='+hashlib.sha256(raw).hexdigest())
    print('B_FAN_ROOT_REDUCTION_V1_RECOVERY_PASS')


if __name__=='__main__': main()
```
