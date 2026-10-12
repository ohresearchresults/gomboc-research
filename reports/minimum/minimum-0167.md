# minimum-0167

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# B_ROOT_CORNER_ALL_ASYMMETRIES_V3

## 1. Главный результат: весь simple-corner сектор, без ограничения асимметрии

**Теорема.** Пусть P — полигедральный локальный максимум ПОЛНОЙ совместной отмеченной задачи с a>b>0, c,d>0, настоящим положительно-площадным корнем и настоящим простым корневым углом при B в точном смысле принятого родителя. Если G(C),G(D)<=0, то

    T=N/(6VE)<2<51/25.

Ограничений на beta, отношение c/d, положение объёмного центроида относительно диагонали, число остальных граней или положительно-ell вспомогательные вершины вне угла нет. В частности, закрыт ВЕСЬ запрошенный сектор beta>1001/1000, а не только новая окрестность равных концов.

Используется принятый общий моментный закон

    (J)  4(u+v)<=6V+1.

Как и в родителе, его можно оставить явно записанной дополнительной гипотезой теоремы. В принятой научной базе это закон настоящего отмеченного тела. Его первоначальное отдельное доказательство здесь не переисполнялось; точная зависимость раскрыта ниже.

Новая связь оказалась сильнее первоначально намеченного соединения со вторым B-jet: достаточно ПЕРВОЙ совместной B/frame-реакции, ПЕРВЫХ/ВТОРЫХ корневых G-моментов, настоящих объёма И n-момента корневой пирамиды и нового ограничения произведения концов. Второй B-jet остаётся верным, но для нового запрета не нужен.

**Следствия для защищённых граней.** При двух неположительно отмеченных защищённых пятиугольниках simple B root corner получается из принятой V2 и ориентации расширений. Поэтому все такие полные максимумы имеют T<2 при любых положительных c,d. То же относится к формам 5/4, 4/5 и 4/4, когда оба настоящих координатных соседа B корневые. Из одного пятиугольника или из одного корневого соседа B простота не выводится.

Это теорема о максимуме в ПОЛНОМ классе. Максимум только внутри sign-сектора, фиксированной решётки граней или при фиксированной ell не наследует весь использованный набор реакций. Не утверждается T<2 для каждого нестационарного тела с такой геометрией. Константа 2 не объявляется точной.

## 2. Контекст, источник и доказательный статус

Новый `research-journal(20260921-195203).md` прочитан полностью через EOF, включая буквальный неизменный родитель. Файл имеет 302988 байт, SHA256 `061263b5745b2bf765a053e0da1dbf9c57ae40cdee62e6ce9facb3adef8403a7`. Новые `b_root_corner_second_jet_v2.py`, `.json`, `.out` также прочитаны полностью. Неизменные прежний журнал, три аналитических материала и предыдущая root-floor работа остаются в этой беседе; повторное начало их исследования не требовалось.

Буквальный родитель — `minimum-0166`, `B_ROOT_CORNER_SECOND_JET_V2`, SHA256 `b1e72d665eb66625c3f695177a0ced15c0bc4f2f6befd1f0acde30cc5f4a32f0`. Проверено: компактный UTF-8 JSON-envelope `{"version":2,"result_markdown":...}` с его полным Markdown и одним конечным LF имеет ровно 55666 байт и этот SHA. Встроенный Python побайтово совпадает с приложенным 12294-байтным исходником SHA `0a2940dc8143387a262a71948cbe5e903019eb17382a21cc5a02856eade6d110`. Конфликта родительской идентичности нет.

Аналитические зависимости: строгая положительность G на вспомогательных настоящих вершинах и жёсткость одноякорной настоящей треугольной грани; полная аффинная root-реакция при ВСЕХ положительных канонических ell-значениях; общий закон (J).

Самостоятельного исходного proof-файла для (J) среди трёх аналитических заметок нет. Используется именно принятый вход родителя, а не придуманное восстановление его доказательства. Его переход к расширенным patches прозрачен: для q0 в относительной внутренности корня с положительными x,y тела `conv(T0,(1-epsilon)P+epsilon q0)` имеют настоящую proper-пару ABC/ABD, положительную площадь корня и сходящиеся настоящие V,u,v. Нестрогий (J) проходит к пределу.

Новый аналитический вывод и полное точное непрерывное покрытие даны далее. Авторски исполнены обычный запуск и отдельный source-only запуск в новой директории; результаты совпали побайтово. Проверка не является формализацией всей вариационной допустимости. Ни численная оптимизация, ни механический S/U/H-подсчёт не используются как доказательство запрета.

## 3. Настоящий B-угол и первая совместная реакция

### 3.1. Объект и обозначения

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    alpha=a-b>0,
    ell=a+(d-a)x+(c-a)y-alpha z,
    h_x=a+b+c, h_y=a+b+d, Delta=h_x h_y,
    n=h_x x+h_y y,
    V=int_P 1, E=int_P ell, N=int_P n,
    g=(u,v,z_g), p=u+v, mu=E/V, t=6V,
    r=N/V, q=N/E, T=q/t, G=n-r-q ell.

P содержит T0=conv(A,B,C,D), лежит в x,y,ell>=0. Fx,Fy — полные настоящие координатные грани; F0=ell0 — полный настоящий корень. Все интегралы относятся к одному исходному равномерно заполненному P. n — исходный канонический числитель, не след по полным площадям увеличенных защищённых граней.

Простой корневой угол означает, что B инцидентна ровно Fx,Fy и одной свободной настоящей грани B U0 V0. Последняя — треугольник с единственной канонической отметкой B; U0 лежит на Fx и F0, V0 — на Fy и F0.

По одноякорной жёсткости

    G(U0)=G(V0)=L=(r+qb)/3,
    K=r+L=(4r+qb)/3,
    n(U0)=n(V0)=K.

Следовательно

    (U0)_y=K/h_y, (V0)_x=K/h_x,
    W=Vol(conv(A,B,U0,V0))=K^2/(6 Delta).

Плоскость настоящего треугольника B U0 V0 задаётся равенством

    H_B=n-K+(K/b)ell=0,

а сторона P имеет H_B>=0, поскольку H_B(A)=K alpha/b>0. В частности, G>=L на настоящем корне. Это МИНИМАЛЬНОЕ G-ребро корня, не максимальное; тест максимального root-edge здесь не применяется.

### 3.2. Почему реакция является B/body/frame-реакцией

Оставим физическую ell и все вершины, кроме B, на месте и положим B_delta=(0,0,1+delta). Оба знака малого delta допустимы: единственная свободная грань через B — настоящий треугольник, другие неинцидентные опоры имеют строгий запас относительно B, а ell(B_delta)=b-alpha delta остаётся положительной.

В положительном A-веере меняется только тетраэдр A B U0 V0. Поэтому для физических интегралов

    V_phys=V+W delta,
    E_phys=E+(bW/2)delta-(alpha W/4)delta^2,
    N_phys=N+(KW/2)delta.

Пусть S_phys=int_(P_delta)(x+y); тогда S_phys(0)=pV. Восстановление рамки z'=z/(1+delta) имеет якобиан 1/(1+delta), а новый числитель в старых физических координатах равен `n-alpha delta(x+y)`. Значит ТОЧНО

    T_delta=(1+delta)[N_phys-alpha delta S_phys]
             /[6 V_phys E_phys].

Числитель первой производной после положительного общего множителя равен

    V(r-alpha p)-L W.

Полная двусторонняя стационарность даёт

    W/V=(r-alpha p)/L.                                  (B)

При фиксированной ell в уже восстановленной канонической рамке этот вывод отдельно не лицензирован.

### 3.3. Безразмерные величины одного тела

    eta=b/mu, A0=alpha/mu, c0=c/mu, d0=d/mu,
    sigma=A0+2eta,
    chi=(c0 u+d0 v)/p,
    H=2eta+chi,
    h=barh/mu=A0+H,  barh=r/p,
    D_eta=(1+eta)(4+eta)^2,
    kappa=Delta/barh^2,
    hcross=(h_x+h_y-barh)/mu,
    lambda=Delta/[barh(h_x+h_y-barh)],
    Z=hcross/(h p)=3 n(w0)/r,
    w0=(v/(3p),u/(3p),1/3), m=3p/t.

Эти отношения не меняют плотность или тело. Имеем T=hp/t и T/m=h/3. Тождество

    h*hcross=Delta/mu^2+(c0-d0)^2 uv/p^2

даёт 0<lambda<=1. Сравнение формулы настоящего W с (B) даёт

    omega:=W/V=3H/[h(1+eta)],
    p=27 kappa H/(T D_eta),
    Z=T D_eta/(27 lambda H).                            (3.1)

Именно здесь используются общие настоящие объёмы, а не независимо выбранная масса B-угла.

## 4. Два общих root/body бюджета: объём и исходный n-момент

### 4.1. Полные корневые реакции

Положим k=|grad ell| и

    rho=mu Area(F0)/(3Vk).

Это НАСТОЯЩАЯ доля пирамиды conv(g,F0). При замене единственной корневой опоры на ell+epsilon f>=0 и одновременной замене вспомогательной функции на ell+epsilon f оба знака допустимы для всякой аффинной f, поскольку a,b,c,d>0. Полная реакция даёт

    int_F0 G f/k=6V^2[T f(g)-m f(w0)].

Все настоящие вершины корня вспомогательные, поэтому G>0 на F0. Отсюда T>m, r>n(w0), то есть

    h>3, 0<Z<3.

Для площадных средних по F0

    rho*mean(G)=r(T-m)/(3T),
    rho*mean(G^2)=r m[r-n(w0)]/(3T).

Коши–Шварц, строгое из-за непостоянства G на положительно-площадном корне, даёт

    rho>rho0=(h-3)^2/[3h(3-Z)].                         (4.1)

Непостоянство следует из ненулевой z-компоненты grad ell и нулевой z-компоненты ненулевого grad n. Эти реакции не переносятся на нулевые канонические концы.

### 4.2. Настоящий объём корневой пирамиды

Пирамида conv(A,F0) имеет долю `(a/mu)rho=(A0+eta)rho` от V. Она и тетраэдр A B U0 V0 — различные части одного положительного A-веера: их основания — разные настоящие максимальные грани. Следовательно

    omega+(A0+eta)rho<=1,
    omega+(A0+eta)rho0<1.                               (V-root)

Это прежняя полезная root-floor связь, теперь включённая в полное непрерывное исключение.

### 4.3. Новый бюджет n на ТОМ ЖЕ веере

У корневой пирамиды n(A)=0 и n|F0=r+G. Её вклад в N/N поэтому равен

    (3/4)(A0+eta)rho
      +(A0+eta)(h-3)/(4h).

У тетраэдра A B U0 V0 среднее n равно K/2. Его вклад в N/N равен

    omega*K/(2r)=omega(4+eta)/6.

Оставшиеся части A-веера имеют неотрицательные n-интегралы, так как n>=0 на P. Поэтому

    3(A0+eta)rho/4
      +(A0+eta)(h-3)/(4h)
      +omega(4+eta)/6 <=1.                              (4.2)

Подстановка (4.1) даёт новое необходимое условие

    (A0+eta)(h-3)(h-Z)/[4h(3-Z)]
      +omega(4+eta)/6 <1.                               (N-root)

Ни площадь, ни распределение G на корне здесь не задаются отдельно: в обоих бюджетах стоит одна и та же настоящая rho, а её средние определены полными root-реакциями. Для h>3 функция `(h-Z)/(3-Z)` строго возрастает по Z. Поэтому увеличение Z, в том числе вызываемое lambda<1, делает этот бюджет более жёстким.

## 5. Новый контроль асимметрии через общий endpoint determinant

### 5.1. Элементарные настоящие моментные ограничения

Конирование из точки X для неотрицательной аффинной f даёт `4 mean_P(f)>=f(X)`. В частности,

    u,v>=1/4, c0,d0<=4, A0+eta<=4.

Для неотрицательной H_B:

    H_B(g)=r(4-eta^2)/(3eta)>0,
    H_B(A)=r A0(4+eta)/(3eta).

Значит

    0<eta<2,
    A0(4+eta)<=4(4-eta^2),
    0<A0<=4, 0<chi<=4.                                 (5.1)

Знаки G(C),G(D)<=0 дают более сильное, чем одно взвешенное среднее, ограничение на p. Например, при c0>=d0:

    r(1+d0)>=h_x>=barh,
    p>=1/(1+d0)>=1/(1+chi).

При d0>=c0 используются отражённые величины. Следовательно всегда

    p>=1/2, p>=1/(1+chi).                               (5.2)

Из (J), t=hp/T и (5.2) следуют

    h>=2T, h>=T(3-chi).                                 (5.3)

Взвешенные знаки G(C),G(D) и полные координатные пирамиды также дают

    T D_eta<=27 lambda H(1+chi)<=27H(1+chi),
    T^2 D_eta<27 lambda H(4-chi)<=27H(4-chi).             (5.4)

Для второго неравенства используются `t(4-c0)>h_y/mu` и `t(4-d0)>h_x/mu`. Строгость обеспечивается настоящим расширением обоих patches: корневой сосед B не может лежать в каноническом треугольнике с тремя положительными ell-значениями.

### 5.2. Произведение h_x h_y не является свободной асимметричной переменной

Из (J) и u,v>=1/4 следуют 4u,4v<=t. Поэтому

    4p chi=4(c0u+d0v)<=t(c0+d0),
    c0+d0>=4T chi/h.

При sigma=A0+2eta получаем

    Delta/mu^2=(sigma+c0)(sigma+d0)
      >=sigma^2+4T sigma chi/h,

то есть

    kappa>=sigma(sigma h+4T chi)/h^3.                  (DET)

Эта оценка использует индивидуальные настоящие координатные моменты того же тела. Она заменяет прежний почти-симметричный вход `kappa>=(1+epsilon)^(-2)` и не требует какого-либо контроля beta.

### 5.3. Правильный переход от T>=tau к одному порогу

Из (J) и (3.1)

    j(T)>=0,
    j(s)=s^2 D_eta-27 kappa H(4s-h).

На tau<=s<=T величина `p_s=27 kappa H/(s D_eta)` не меньше настоящей p>=1/2. Поэтому

    j'(s)=2s D_eta(1-2p_s)<=0,
    j(tau)>=j(T)>=0.

Применяя (DET) с T>=tau, получаем

    tau^2 h^3 D_eta
      -27H sigma(sigma h+4tau chi)(4tau-h)>=0.           (J-DET)

Если 4tau-h>=0, используется нижняя граница kappa. Если 4tau-h<0, выписанное неравенство автоматически строго положительно. Никакая неподтверждённая монотонность квадратного выражения по T не предполагается.

## 6. Полный точный непрерывный запрет

Предположим T>=tau, где tau=2 или 101/50. Из уже доказанных реакций все следующие полиномы должны быть неотрицательны. Положим H=2eta+chi, h=A0+H, sigma=A0+2eta, D=(1+eta)(4+eta)^2:

    F0 = 4-A0-eta,
    F1 = 4(4-eta^2)-(4+eta)A0,
    F2 = h-2tau,
    F3 = h-tau(3-chi),
    F4 = 27H(1+chi)-tau D,
    F5 = 27H(4-chi)-tau^2 D,
    F6 = h(1+eta)-3H,
    F7 = 81H-tau D,
    F8 = [h(1+eta)-3H](81H-tau D)
         -9H(1+eta)(A0+eta)(h-3)^2,
    F9 = tau^2 h^3 D
         -27H sigma(sigma h+4tau chi)(4tau-h),
    F10= [4h(1+eta)-2H(4+eta)](81H-tau D)
         -(A0+eta)(1+eta)(h-3)(27Hh-tau D).

F8 — очищенный (V-root), F10 — очищенный (N-root), с заменой

    Z>=Z0=tau D/(27H).

Такая замена ослабляет оба бюджета: h>3, Z<3, rho0 возрастает по Z, а монотонность N-root доказана в разделе 4. F7 гарантирован настоящим Z<3. Положительные множители при очистке знаменателей сохраняют знаки. Некоторые исходные неравенства строги; их ослабление до F_i>=0 безопасно. Для F3 при chi>3 правая часть отрицательна и условие автоматически верно; при chi<=3 используется T>=tau.

Весь образ настоящих кандидатов содержится в замкнутом кубе

    eta=2x, A0=4y, chi=4z, (x,y,z) in [0,1]^3.

На его искусственных границах не заявляется допустимость root-вариаций: они включены только в больший алгебраический домен исключения.

Проверитель последовательно делит куб пополам по осям `depth mod 3`. В каждом конечном замкнутом прямоугольном параллелепипеде ОДИН из необходимых F_i имеет ВСЕ коэффициенты Бернштейна строго отрицательными. Поэтому там F_i<0, что противоречит необходимым условиям.

| Использованный набор | tau | Замкнутых листьев | Максимальная глубина | Строго отрицательных коэффициентов | Минимальный положительный запас -max(coeff) |
|---|---|---:|---:|---:|---|
| F0,...,F9: root-volume, без нового N-root | 101/50 | 342 | 33 | 25096 | 7/256 |
| F0,...,F10: оба общих root-бюджета | 2 | 229 | 28 | 17332 | 1/256 |

Число листьев по индексам F0,... соответственно:

    tau=101/50: [0,6,7,90,2,35,1,0,98,103],
    tau=2:     [0,6,5,72,5,0,2,0,46,63,30].

Векторы степеней по (x,y,z):

    (1,1,0),(2,1,0),(1,1,1),(1,1,1),(3,0,2),(3,0,2),
    (2,1,1),(3,0,1),(5,3,3),(6,4,3),(6,3,3).

Каждый лист независимо перепроверен прямой биномиальной подстановкой его концов в исходный степенной полином, без наследования результатов de Casteljau. Проверены полное префиксное двоичное дерево и точная сумма `sum 2^(-depth)=1`. Покрываются все границы и все непрерывные внутренние точки; численная сетка не используется. Всего проверено 42428 строго отрицательных коэффициентов.

Таким образом первый, сохранённый более слабый шаг уже даёт T<101/50 при ВСЕХ асимметриях. Добавление настоящего N-root завершает доказательство T<2.

## 7. Сохранённые отрицательный результат и настоящий геометрический контроль

### 7.1. Новая точная граница volume-only релаксации

Точка

    eta=1/100, A0=77/20, chi=18/25, T=2

имеет H=37/50, h=459/100, sigma=387/100. Её полные НЕМАСШТАБИРОВАННЫЕ остатки F0,...,F10 равны

    [7/50,
     5611/10000,
     59/100,
     3/100,
     941899/500000,
     142699/250000,
     24159/10000,
     13729099/500000,
     3474815763/5000000000,
     19939496099229/250000000000,
     -5229032273413/250000000000].

Первые десять строго положительны, новый N-root нарушен. Следовательно трипараметрическая volume-only релаксация сама по себе НЕ исключает T=2; новый n-момент не является её избыточным повторением.

Это ФОРМАЛЬНАЯ точка релаксации, НЕ тело, НЕ утверждение о реализации полного B-jet или всех настоящих моментов. Она отличается от родительского формального T=2-контроля, который уже нарушал прежний root-volume бюджет.

### 7.2. Настоящее асимметричное тело с двумя защищёнными пятиугольниками

Сохранён новый равномерный многогранник, заданный семью настоящими опорами:

    x>=0, y>=0, z>=0,
    ell=1-7x/10-3y/10-z/2>=0,
    45-8x+18y-45z>=0,
    3-3x+z>=0,
    100-100y+z>=0.

Его канонические концы `(a,b,c,d)=(1,1/2,7/10,3/10)`, исходный `n=11x/5+9y/5`. Полный постоянный порядок настоящих вершин:

    0=(0,0,0), 1=(0,0,1), 2=(0,1,0), 3=(1,0,0),
    4=(0,1,7/5), 5=(0,510/503,700/503),
    6=(9/11,0,47/55), 7=(1,1,0), 8=(25/22,0,9/22).

Полные циклы максимальных граней в порядке опор:

    (0,2,5,4,1), (0,3,8,6,1), (0,3,7,2),
    (8,7,5,4,6), (6,4,1), (3,7,8), (2,7,5).

Это настоящее 9/14/7. B=1 простая, её соседи 0,4,6; единственная свободная B-грань — треугольник 1,4,6 с двумя корневыми концами. Обе защищённые грани пятиугольные, корень также пятиугольный. Точно:

    V=58463/66396,
    E=250427/885280,
    N=140305271/89059168,
    J=(721307/1947616,18817163/44529584,6219422659/14694762720),
    g=(2163921/5144744,2971131/6190924,6219422659/12939031160),
    T=15433579810/14640713701,
    beta=7015263550/6991155063>1001/1000.

G(C),G(D)<0, все вспомогательные G>0, обе полные опорные реакции отметок выполнены. Поэтому сама эта геометрия, знаки G и mark-supports НЕ влекут beta<=1.001.

Однако тело НЕ стационарно:

    G(B)+3G(4)=-9836442130177/2165964409295 !=0.

Нарушены также обе проверенные полные root-реакции. Оно не опровергает новую теорему о полном максимуме. Геометрический уровень `n(4)=n(6)=9/5` нельзя отождествлять с необходимым стационарным K.

Полный supporting-triple hull, настоящие рёбра, простота B и положительные объёмные веера из A и B проверены точно. Дополнительно настоящие остатки A-веера после удаления B-тетраэдра и A-root-пирамиды положительны:

    V_remaining=19927/66396,
    N_remaining=788757647/1335887520.

Это невыигрывающий геометрический контроль. Его механические S/U/H и слабые пакеты не вычислялись; ему не приписывается статус 110.

## 8. Что закрыто и что остаётся

Внутри точного simple B root corner, при G(C),G(D)<=0 и принятом (J), больше нет остаточного сильно асимметричного сектора: запрещён даже T>=2. Следующее содержательное применение — использовать это как готовый запрет, когда другая геометрическая ветвь устанавливает простоту угла.

За пределами доказательства остаются настоящий НЕпростой B-веер, включая положительно-ell соседей B; simple corner с положительной настоящей другой отметкой; нулевые канонические ell-концы, где root-реакции требуют нового одностороннего анализа; нестационарные тела и общий мост к механике. Избыточная положительная каноническая отметка больше не открытый остаток: отдельная принятая координаторская теорема уже исключает её в полном отрицательно-якорном максимуме.

Новый результат не изменяет C_min, механический реестр или границы 34<=C_min<=622. Он не является полным исключением 10/17/9 и не поставляет нового attaining 110-тела.

## 9. Полная recovery capsule

Самодостаточный источник ниже содержит точные входы, оба полных непрерывных сертификата, независимую проверку каждого листа, новый формальный контроль и полный настоящий 9/14/7-контроль. Он не импортирует родительский код и не требует скачивания данных. В обозначениях источника `e=eta`, `A=A0`, `c=chi`; последний `c` НЕ канонический конец c.

Исполненная среда: CPython 3.13.5, SymPy 1.14.0; assertions включены. Все вычисления доказательной части рациональные; seed и параметры численной оптимизации отсутствуют.

    b_root_corner_all_asymmetries_v3.py
    13751 bytes
    SHA256 f13a5ecbe56f01c961280b964a6e6c8c1fd480af752b9bc6d1978624af603722

    b_root_corner_all_asymmetries_v3.json
    93029 bytes
    SHA256 4b7ac76bfe5e6b6b0b013c0c2073fd7fa5f311b381db925b0de9185c3e9e9da3

    b_root_corner_all_asymmetries_v3.out
    543 bytes
    SHA256 bb0c2ede9a1d844f4088814b545a9ad92d7f0a97512e9669d24df32377f07d0f

Команды после сохранения полного блока как указанного `.py` с LF:

    python b_root_corner_all_asymmetries_v3.py > b_root_corner_all_asymmetries_v3.out
    sha256sum b_root_corner_all_asymmetries_v3.py b_root_corner_all_asymmetries_v3.json b_root_corner_all_asymmetries_v3.out

Полный ожидаемый stdout:

    ACTUAL_ROOT_VOLUME_N_MOMENTS_AND_ENDPOINT_DETERMINANT_ALGEBRA_PASS
    CUBE tau=101/50 root_n=False leaves=342 depth=33 negative_coefficients=25096
    CUBE tau=2 root_n=True leaves=229 depth=28 negative_coefficients=17332
    INDEPENDENT_DIRECT_BINOMIAL_REPLAY_AND_COMPLETE_CLOSED_CUBES_PASS
    FORMAL_T2_VOLUME_ONLY_PASSES_ROOT_N_BUDGET_FAILS
    ACTUAL_ASYMMETRIC_9_14_7_TWO_VOLUME_FANS_NONSTATIONARY_CONTROL_PASS
    report_bytes=93029
    report_sha256=4b7ac76bfe5e6b6b0b013c0c2073fd7fa5f311b381db925b0de9185c3e9e9da3
    B_ROOT_CORNER_ALL_ASYMMETRIES_V3_RECOVERY_PASS

Дополнительные удобные копии: исходник (`b_root_corner_all_asymmetries_v3.py`), полный точный отчёт (`b_root_corner_all_asymmetries_v3.json`), stdout (`b_root_corner_all_asymmetries_v3.out`). Весь восстанавливающий источник включён далее.

```python
#!/usr/bin/env python3
"""B_ROOT_CORNER_ALL_ASYMMETRIES_V3; CPython 3.13.5, SymPy 1.14.0.
Exact closed-cube certificates and a genuine nonstationary uniform control.
Parent: minimum-0166,
SHA256 b1e72d665eb66625c3f695177a0ced15c0bc4f2f6befd1f0acde30cc5f4a32f0.
No external inputs, inherited code, numerical optimization, or RNG.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from functools import lru_cache
from math import comb, prod
from pathlib import Path
import hashlib
import json
import sympy as S


def rational(x):
    x = S.Rational(x)
    return Q(int(x.p), int(x.q))


def expressions(e, A, c, T):
    H = 2*e+c
    h = A+H
    s = A+2*e
    D = (1+e)*(4+e)**2
    return [
        4-A-e,
        4*(4-e*e)-(4+e)*A,
        h-2*T,
        h-T*(3-c),
        27*H*(1+c)-T*D,
        27*H*(4-c)-T*T*D,
        h*(1+e)-3*H,
        81*H-T*D,
        (h*(1+e)-3*H)*(81*H-T*D)
        -9*H*(1+e)*(A+e)*(h-3)**2,
        T*T*h**3*D-27*H*s*(s*h+4*T*c)*(4*T-h),
        (4*h*(1+e)-2*H*(4+e))*(81*H-T*D)
        -(A+e)*(1+e)*(h-3)*(27*H*h-T*D)]


def algebra():
    e,A,c,h,H,Z,T,k,p,s,u,v,C,D = S.symbols(
        'e A c h H Z T k p s u v C D', positive=True)
    rho0 = (h-3)**2/(3*h*(3-Z))
    omega = 3*H/(h*(1+e))
    root_n = 3*(A+e)*rho0/4+(A+e)*(h-3)/(4*h)
    assert S.factor(root_n-(A+e)*(h-3)*(h-Z)/(4*h*(3-Z))) == 0
    assert S.factor(S.diff((h-Z)/(3-Z),Z)-(h-3)/(3-Z)**2) == 0
    De = (1+e)*(4+e)**2
    z0 = T*De/(27*H)
    volume = 1-omega-(A+e)*rho0
    numerator = 1-root_n-omega*(4+e)/6
    F = expressions(e,A,c,T)
    substitution = {H:2*e+c,h:A+2*e+c}
    vclear = (3*h*(1+e)*(3-Z)*volume).subs(Z,z0)*9*H
    nclear = (4*h*(1+e)*(3-Z)*numerator).subs(Z,z0)*27*H
    assert S.factor(vclear.subs(substitution)-F[8]) == 0
    assert S.factor(nclear.subs(substitution)-F[10]) == 0
    hb = ((s+C)*u+(s+D)*v)/(u+v)
    hc = s+C+D-(hb-s)
    assert S.factor(hb*hc-(s+C)*(s+D)-(C-D)**2*u*v/(u+v)**2) == 0
    assert S.expand((s+C)*(s+D)-s*s-s*(C+D)-C*D) == 0
    z = S.symbols('z', positive=True)
    j = z*z*De-27*k*H*(4*z-h)
    assert S.factor(S.diff(j,z)-2*z*De*(1-2*27*k*H/(z*De))) == 0
    floor = s*(s*h+4*T*c)/h**3
    assert S.factor((T*T*De-27*floor*H*(4*T-h))*h**3
                    -(T*T*h**3*De-27*H*s*(s*h+4*T*c)*(4*T-h))) == 0
    return {'root_variance_denominator':'3*h*(3-Z)',
            'root_n_budget':'a*(h-3)*(h-Z)/(4*h*(3-Z))+omega*(4+eta)/6<=1',
            'determinant_floor':'kappa>=sigma*(sigma*h+4*T*chi)/h^3',
            'uses_second_B_jet':False}


def polynomials(tau, use_n):
    x,y,z = S.symbols('x y z')
    ff = expressions(2*x,4*y,4*z,S.Rational(tau))
    if not use_n:
        ff = ff[:10]
    out = []
    for f in ff:
        num,den = S.fraction(S.factor(f))
        assert den.is_Rational and den>0
        poly = S.Poly(S.expand(num),x,y,z)
        degree = tuple(int(poly.degree(t)) for t in (x,y,z))
        power = {ij:rational(a) for ij,a in poly.terms()}
        replay = sum(S.Rational(c)*x**i*y**j*z**k for (i,j,k),c in power.items())
        assert S.expand(replay-den*f) == 0
        out.append((degree,power,rational(den)))
    return out


@lru_cache(None)
def positions(degree):
    return tuple(product(*(range(d+1) for d in degree)))


def bernstein(degree,power):
    return [sum((c*prod(Q(comb(i,j),comb(n,j)) for i,j,n in zip(ix,ij,degree))
                 for ij,c in power.items() if all(j<=i for i,j in zip(ix,ij))),Q(0))
            for ix in positions(degree)]


@lru_cache(None)
def lines(degree,axis):
    pos = positions(degree)
    index = {p:i for i,p in enumerate(pos)}
    groups = []
    for p in product(*(range(d+1) if j!=axis else (0,) for j,d in enumerate(degree))):
        row = []
        for t in range(degree[axis]+1):
            q = list(p); q[axis] = t
            row.append(index[tuple(q)])
        groups.append(tuple(row))
    return groups


def split(b,degree,axis):
    left,right = [Q(0)]*len(b),[Q(0)]*len(b)
    for inds in lines(degree,axis):
        row = [b[i] for i in inds]
        ll,rr = [row[0]],[row[-1]]
        while len(row)>1:
            row = [(a+c)/2 for a,c in zip(row,row[1:])]
            ll.append(row[0]); rr.append(row[-1])
        for i,a,c in zip(inds,ll,reversed(rr)):
            left[i],right[i] = a,c
    return left,right


@lru_cache(None)
def direct_axis(n,lo,hi):
    # Coefficient of B_i^n(t) in (lo+(hi-lo)*t)^k, by binomial expansion.
    return tuple(tuple(sum((Q(comb(k,j)*comb(i,j),comb(n,j))*lo**(k-j)*(hi-lo)**j
                            for j in range(min(k,i)+1)),Q(0))
                       for i in range(n+1)) for k in range(n+1))


def direct_replay(degree,power,path):
    box = [[Q(0),Q(1)] for _ in range(3)]
    for depth,bit in enumerate(path):
        axis = depth%3; lo,hi = box[axis]; mid = (lo+hi)/2
        box[axis] = [lo,mid] if bit=='0' else [mid,hi]
    transforms = [direct_axis(n,*b) for n,b in zip(degree,box)]
    return [sum((c*prod(transforms[j][ij[j]][ix[j]] for j in range(3))
                 for ij,c in power.items()),Q(0)) for ix in positions(degree)]


def certificate(tau,use_n,expected):
    polys = polynomials(tau,use_n)
    initial = {i:bernstein(d,p) for i,(d,p,den) in enumerate(polys)}
    leaves = []
    def rec(blocks,path):
        pending = {}
        for i,b in blocks.items():
            if max(b)<0:
                check = direct_replay(polys[i][0],polys[i][1],path)
                assert check==b and all(c<0 for c in check)
                leaves.append([path,i,str(-max(b))])
                return
            if min(b)<0:
                pending[i] = b
        assert pending, ('UNCLOSED_BOX',path)
        assert len(path)<66, ('DEPTH_LIMIT',path)
        children = {i:split(b,polys[i][0],len(path)%3) for i,b in pending.items()}
        for side in (0,1):
            rec({i:pair[side] for i,pair in children.items()},path+str(side))
    rec(initial,'')
    paths = {r[0] for r in leaves}
    assert len(paths)==len(leaves)
    prefixes = {p[:i] for p in paths for i in range(len(p)+1)}
    def partition(p):
        if p in paths:
            assert not any(q!=p and q.startswith(p) for q in paths)
            return
        assert p+'0' in prefixes and p+'1' in prefixes
        partition(p+'0'); partition(p+'1')
    partition('')
    assert sum((Q(1,2**len(p)) for p in paths),Q(0))==1
    counts = [sum(r[1]==i for r in leaves) for i in range(len(polys))]
    depth = max(map(len,paths))
    assert (len(leaves),depth,counts)==expected
    total = sum(prod(n+1 for n in polys[i][0]) for path,i,bound in leaves)
    return {'tau':tau,'uses_root_n':use_n,'leaf_count':len(leaves),
            'max_depth':depth,'by_polynomial':counts,'negative_coefficients':total,
            'minimum_gap':str(min(Q(r[2]) for r in leaves)),
            'polynomials':[{'degree':list(d),'positive_scale':str(den),
                            'powers':[[*ij,str(c)] for ij,c in sorted(p.items())]}
                           for d,p,den in polys], 'leaves':leaves}


def formal_control():
    vals = expressions(Q(1,100),Q(77,20),Q(18,25),Q(2))
    expected = ['7/50','5611/10000','59/100','3/100','941899/500000',
                '142699/250000','24159/10000','13729099/500000',
                '3474815763/5000000000','19939496099229/250000000000',
                '-5229032273413/250000000000']
    assert list(map(str,vals))==expected
    assert all(v>0 for v in vals[:10]) and vals[10]<0
    return {'eta':'1/100','alpha_over_mu':'77/20','chi':'18/25','T':'2',
            'eleven_unscaled_residuals':expected,
            'status':'FORMAL RELAXATION ONLY; NOT A BODY; root n-budget fails'}


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),Q(0))


def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


def det(a,b,c):
    return dot(a,cross(b,c))


def actual_control():
    # Seven true supporting slacks, all >=0. No stationarity is assumed.
    slacks = [(0,(1,0,0)),(0,(0,1,0)),(0,(0,0,1)),
              (1,(-Q(7,10),-Q(3,10),-Q(1,2))),
              (45,(-8,18,-45)),(3,(-3,0,1)),(100,(0,-100,1))]
    pts = [(0,0,0),(0,0,1),(0,1,0),(1,0,0),(0,1,Q(7,5)),
           (0,Q(510,503),Q(700,503)),(Q(9,11),0,Q(47,55)),
           (1,1,0),(Q(25,22),0,Q(9,22))]
    pts = [tuple(map(Q,p)) for p in pts]
    cycles = [(0,2,5,4,1),(0,3,8,6,1),(0,3,7,2),
              (8,7,5,4,6),(6,4,1),(3,7,8),(2,7,5)]
    assert all(b+dot(n,p)>=0 for b,n in slacks for p in pts)
    for (b,n),cyc in zip(slacks,cycles):
        assert {i for i,p in enumerate(pts) if b+dot(n,p)==0}==set(cyc)
    found = {}
    for i,j,k in combinations(range(len(pts)),3):
        n = cross(sub(pts[j],pts[i]),sub(pts[k],pts[i]))
        if not any(n):
            continue
        b = dot(n,pts[i]); ss = [b-dot(n,p) for p in pts]
        if min(ss)<0<max(ss):
            continue
        f = frozenset(i for i,s in enumerate(ss) if s==0)
        found.setdefault(f,n)
    assert set(found)=={frozenset(c) for c in cycles}
    edges = {tuple(sorted((c[i-1],c[i]))) for c in cycles for i in range(len(c))}
    assert edges=={tuple(sorted(f&h)) for f,h in combinations(found,2) if len(f&h)==2}
    assert (len(pts),len(edges),len(found))==(9,14,7)
    assert len(pts)-len(edges)+len(found)==2
    for i in range(9):
        ns = [n for f,n in found.items() if i in f]
        assert any(det(*tri)!=0 for tri in combinations(ns,3))
    assert {j for e in edges if 1 in e for j in e if j!=1}=={0,4,6}
    ell = lambda p: 1-dot((Q(7,10),Q(3,10),Q(1,2)),p)
    nn = lambda p: Q(11,5)*p[0]+Q(9,5)*p[1]
    def fan(apex):
        V,E,N = Q(0),Q(0),Q(0)
        J = [Q(0)]*3
        for c in cycles:
            if apex in c:
                continue
            for j in range(1,len(c)-1):
                ids = (apex,c[0],c[j],c[j+1])
                vol = abs(det(*(sub(pts[i],pts[apex]) for i in ids[1:])))/6
                assert vol>0
                V += vol
                E += vol*sum(ell(pts[i]) for i in ids)/4
                N += vol*sum(nn(pts[i]) for i in ids)/4
                for k in range(3):
                    J[k] += vol*sum(pts[i][k] for i in ids)/4
        return V,E,N,tuple(J)
    V,E,N,J = fan(0)
    assert (V,E,N,J)==fan(1)
    assert (V,E,N)==(Q(58463,66396),Q(250427,885280),Q(140305271,89059168))
    g = tuple(x/V for x in J); p = g[0]+g[1]
    r,q,mu,T,m = N/V,N/E,E/V,N/(6*V*E),p/(2*V)
    G = [nn(z)-r-q*ell(z) for z in pts]
    assert G[2]<0 and G[3]<0 and min(G[4:])>0
    assert G[1]+3*G[4]!=0
    assert G[4]==G[6]
    for cyc,axis,end in ((cycles[0],1,Q(7,10)),(cycles[1],0,Q(3,10))):
        assert max((Q(1,2)+2*end)*(pts[i][axis]-1)-pts[i][2]/2 for i in cyc)==0
    beta = (r/p)*Q(4)/(2*Q(11,5)*Q(9,5))
    assert beta==Q(7015263550,6991155063)>Q(1001,1000)
    assert T==Q(15433579810,14640713701)
    root = cycles[3]; moments = [Q(0)]*3
    for j in range(1,len(root)-1):
        ids = (root[0],root[j],root[j+1])
        a,b,c = (pts[i] for i in ids)
        # dA/|grad ell|=2 dxdy on the root plane.
        weight = abs((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))
        gg = [G[i] for i in ids]
        moments[0] += weight
        moments[1] += weight*sum(gg)/3
        moments[2] += weight*(sum(gg)**2+sum(z*z for z in gg))/12
    W = abs(det(pts[1],pts[4],pts[6]))/6
    rootV = moments[0]/3
    rootN = (moments[1]+r*moments[0])/4
    bN = W*(nn(pts[4])+nn(pts[6]))/4
    assert V-W-rootV>0 and N-bN-rootN>0
    w0 = (g[1]/(3*p),g[0]/(3*p),Q(1,3))
    res1 = moments[1]-6*V*V*(T-m)
    res2 = moments[2]-6*V*V*m*(r-nn(w0))
    assert res1!=0 and res2!=0
    return {'vertices':[[str(x) for x in p] for p in pts],
            'support_slacks':[[str(b),[str(x) for x in n]] for b,n in slacks],
            'facets':[list(c) for c in cycles],'edges':[list(e) for e in sorted(edges)],
            'f_vector':[9,14,7],'V':str(V),'E':str(E),'N':str(N),
            'J':list(map(str,J)),'g':list(map(str,g)), 'T':str(T),'beta':str(beta),
            'G_vertices':list(map(str,G)), 'B_triangle_residual':str(G[1]+3*G[4]),
            'root_integrals_1_G_G2':list(map(str,moments)),
            'root_stationarity_residuals':[str(res1),str(res2)],
            'A_fan_volume_remainder':str(V-W-rootV),
            'A_fan_n_remainder':str(N-bN-rootN),
            'status':'GENUINE UNIFORM BODY; NOT STATIONARY; mechanical S/U/H not audited'}


def main():
    checks = algebra()
    certificates = [
        certificate('101/50',False,(342,33,[0,6,7,90,2,35,1,0,98,103])),
        certificate('2',True,(229,28,[0,6,5,72,5,0,2,0,46,63,30]))]
    report = {'version':3,'parent_assignment':'minimum-0166',
              'algebra':checks,'certificates':certificates,
              'formal_control':formal_control(),'actual_control':actual_control()}
    raw = (json.dumps(report,sort_keys=True,ensure_ascii=True,indent=2)+'\n').encode()
    Path('b_root_corner_all_asymmetries_v3.json').write_bytes(raw)
    print('ACTUAL_ROOT_VOLUME_N_MOMENTS_AND_ENDPOINT_DETERMINANT_ALGEBRA_PASS')
    for c in certificates:
        print('CUBE tau='+c['tau']+' root_n='+str(c['uses_root_n'])+
              ' leaves='+str(c['leaf_count'])+' depth='+str(c['max_depth'])+
              ' negative_coefficients='+str(c['negative_coefficients']))
    print('INDEPENDENT_DIRECT_BINOMIAL_REPLAY_AND_COMPLETE_CLOSED_CUBES_PASS')
    print('FORMAL_T2_VOLUME_ONLY_PASSES_ROOT_N_BUDGET_FAILS')
    print('ACTUAL_ASYMMETRIC_9_14_7_TWO_VOLUME_FANS_NONSTATIONARY_CONTROL_PASS')
    print('report_bytes='+str(len(raw)))
    print('report_sha256='+hashlib.sha256(raw).hexdigest())
    print('B_ROOT_CORNER_ALL_ASYMMETRIES_V3_RECOVERY_PASS')


if __name__=='__main__':
    main()
```
