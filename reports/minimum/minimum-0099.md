# minimum-0099

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# RAVEN_QUANTITATIVE_CAP_110_V1

## 1. Результат и его уровень доказательства

**Получен количественный конструктивный переход к настоящему рациональному однородному полиэдру собственного строгого класса (1,1,0), без дополнительных слабых равновесий.** Ниже полностью заданы его конечный генератор, явные масштабы и аналитическое доказательство. Грубая гарантированная сложность — **C<2^350**. Это существенно хуже принятого C622 и не меняет скобку минимума.

Ключевое изменение архитектуры: вместо сохранения семи меридиональных узлов сначала строится внутренняя пространственная сетка нового гладкого тела; около U добавляется выступающая вершина, а около S производится плоское отсечение. При этих операциях изменение настоящего объёмного центра имеет порядок h^(3/2), тогда как нужные механические запасы имеют порядок h. Центр конечного тела не назначается: он определяется его собственным объёмным интегралом, и доказательство работает для всего полученного точного интервала его возможного положения.

**Граница исполнения:** огромное тело не было перечислено. Его фактические V,E,F, полные рациональные значения объёма и COM и файл полного конечного census не вычислялись. Выполнены точные проверки всех используемых числовых запасов и тест полного геометрического аудитора на кубе. Таким образом, это запрошенная самостоятельная количественная конструктивная теорема с конечным рецептом, а не новый перечисленный computational endpoint. Точный произвольный элемент сетки вычисляется исполнимой командой `point`. Полный перебор `build` приведён как эталон конечного алгоритма, но выбранный размер превосходит адресное пространство среды; он не выдаётся за выполненный или практически запускаемый расчёт.

Само качественное утверждение о полиэдральной аппроксимации гладкого собственного тела с сохранением равновесий уже имеется в теореме2 Z. Lángi, *A solution to some problems of Conway and Guy on monostable polyhedra*, arXiv:2008.02090v3. Оно здесь проверено по первичному тексту; приоритет для общей идеи аппроксимации не заявляется. Ниже вместо ссылки на «достаточно мелкую сетку» дан конкретный рациональный рецепт и собственные количественные оценки. Геометрическое доказательство не использует теорему Lángi как недоказанную вычислительную подпрограмму. :contentReference[oaicite:0]{index=0}

## 2. Источники и родительство

Прочитан весь `research-journal(20260919-084207).md` до EOF, включая обновления и буквальный parent: 303608 байт, 2586 текстовых строк, SHA-256 `c5a802ea4e83002b9283df5bdf314ef237a905543382ab8340fc2ef24df2d3ff`. Неизменённые ранее предоставленные источники сохраняют своё прежнее прочтение.

Буквальный parent `minimum-0097` аутентифицирован: компактная оболочка версии2 — 47669 байт, SHA-256 `83057dd4c80cce9cfbdfdeaa1c154ed52f849a9292cba9aae47dc348164ecbe7`. Его два встроенных исходника совпадают с ранее приложенными: `raven_meridional_barrier.py`,13978 байт,SHA `4c86997ed4fd9d8f267660a519f4b51e9422bb52392936773a63889dfec902b9`; `search_hull.py`,3882 байта,SHA `b0e8e1e25e8555417e6bb1c4e091b0033417ce735924ed136541d4fbaa7a54ea`.

Старый U7-запрет не ослабляется: он действительно включает все допустимые общие угловые сетки прежнего профиля. Новая конструкция не является ещё одним его подразделением. H61 и старые численные checkpoints не использованы; файлов C622 эта конструкция не требует и его потомком не является. Научного конфликта с буквальным parent не найдено. :contentReference[oaicite:1]{index=1}

## 3. Полностью заданное тело и количественная теорема

Обозначим e1=(1,0,0). Берётся член ранее сохранённого гладкого семейства с **k=1, ε=1/50**, а не прежний семиузловой многогранник:

    a=3π/2,
    Φ(z)=a(z−z³/3),
    c(z)=ε(cosΦ(z),sinΦ(z)),
    K={(c(z)+sqrt(1−z²)u,z): |u|≤1, −1≤z≤1}.

Само гладкое семейство, его настоящий COM и нормали присутствуют в прочитанном источнике; его использование не переносит гладкий COM в конечную механику. :contentReference[oaicite:2]{index=2}

Положим

    r=49/50, ρ=51/50,
    S0=−r e1, U0=ρ e1,
    h=2^−60, μ=2^−160,
    σ=2^−190, Lgrid=2^170,
    A=(ρ+h)e1, ccut=−r+h.

**Теорема о конечной сетке.** Пусть X — любое конечное подмножество K такое, что каждая точка ∂K находится на расстоянии не больше μ от некоторой точки X. Тогда

    Q=conv X,
    P0=conv(Q∪{A}),
    P=P0∩{x1≥ccut}

— полномерный выпуклый полиэдр, который при равномерном объёмном заполнении и относительно собственного g=g(P) имеет ровно два физических равновесия:

    строгая U-вершина A;
    строгая S-грань P∩{x1=ccut}, с точкой (ccut,g2,g3).

Иных равновесий — строгих или слабых VE/EF/VF — нет. Теорема не требует регулярной сетки, простоты, симплициальности, заданной комбинаторики или отсутствия безвредных нулевых примитивов. Механическая пара во всём доказательстве **M=I, N=M^−1=I**.

Следующий рациональный X удовлетворяет её гипотезам и делает P полностью определённым без трансцендентного oracle.

### Рациональный генератор X

Для всех целых −Lgrid≤i,j≤Lgrid и s∈{−1,1} положить u=i/Lgrid,v=j/Lgrid и

    w=(2u,2v,s(1−u²−v²))/(1+u²+v²).

Это две рациональные стереографические сетки сферы. Ввести

    atan128(q)=Σ_{j=0}^{127} (−1)^j/[(2j+1)q^(2j+1)],
    πhat=16 atan128(5)−4 atan128(239),
    φhat=(3πhat/2)(w3−w3³/3),
    C256(t)=Σ_{j=0}^{255}(−1)^j t^(2j)/(2j)!,
    S256(t)=Σ_{j=0}^{255}(−1)^j t^(2j+1)/(2j+1)!.

В X включаются все точки

    (1−σ)(w1+ε C256(φhat), w2+ε S256(φhat), w3).

Совпадающие точки удаляются. Никакой произвольный выбор округления, случайное семя или скрытый checkpoint не используется.

Если m0=2(2Lgrid+1)² — число строк до удаления совпадений, то у P0 не больше m0+1 вершин. Одно отсечение добавляет не больше одной новой вершины на каждое настоящее ребро. Поэтому для настоящего конечного тела

    V≤4(m0+1)−6,
    E≤12(m0+1)−24,
    F≤8(m0+1)−16,
    C=2E<24(m0+1)<2^350.

Здесь используются общие полиэдральные неравенства Эйлера, а не счёт диагоналей триангуляции. Эти верхние оценки не выдаются за фактический f-vector.

## 4. Гладкие оценки, необходимые для доказательства

### Настоящий центр, выпуклость и радиусы

Площадь горизонтального сечения K равна π(1−z²). Поэтому Vol(K)=4π/3, вертикальный момент нулевой, а горизонтальный момент равен

    (πε/a)∫_{−π}^{π}(cos t,sin t)dt=0.

Это непосредственно интеграл равномерного объёма K. Для t=1−z²

    t³ |c″(z)|²/ε² = a⁴t⁷+4a²(1−t)t³ ≤a⁴.

Поскольку εa²<1/2, все горизонтальные опорные профили sqrt(1−z²)+n·c(z) строго вогнуты. Их пересечения доказывают выпуклость K. Гладкость, включая концы z=±1, следует из регулярного неявного уравнения

    F(x,y,z)=|(x,y)−c(z)|²+z²−1=0.

При w∈S² и Ψ(w)=(w1+c1(w3),w2+c2(w3),w3), пусть T(w) поворачивает горизонтальные координаты на −Φ(w3). Тогда

    |Ψ(w)|²=1+ε²+2ε[T(w)]1.

Отсюда единственные гладкие критические точки — S0,U0, а также r B³⊂K⊂ρ B³.

### Равномерная квадратичная опорная оценка

На K справедливы |c′|<1/10, |c″|<7/10 и

    (1/2)D²F[(v,t)]²=|v−c′t|²+(1−((x,y)−c)·c″)t².

Неравенство 2|v||t|/10≤|v|²/5+t²/20 даёт D²F≥(2/5)I; аналогично D²F≤4I. На ∂K имеем 9/5≤|∇F|≤11/5. Если Y∈∂K, nY — единичная внешняя нормаль, то для каждого p∈K

    nY·(Y−p) ≥ |Y−p|²/16.                         (1)

Это следует из формулы Тейлора вдоль отрезка в K. Если также p∈∂K, обратная верхняя оценка равна2|Y−p|². Для двух граничных точек

    |nY−np|≤5|Y−p|.                               (2)

Последняя оценка использует D²F≤4I и нижнюю границу |∇F|, а не предполагаемую регулярность конечной сетки.

### Явное исключение гладких почти-критических точек

Операторы производных T и T^−1 имеют нормы меньше6, а Ψ — меньше11/10. На сфере градиент координатной функции w↦w1 имеет норму sqrt(1−w1²). Следовательно

    |proj_(nY⊥)Y| ≥ sqrt(1−[T(w)]1²)/330.

Кроме того, расстояние от Y до ближайшей из S0,U0 не больше (33sqrt2/5)sqrt(1−[T(w)]1²). Так как 2178sqrt2<4096,

    |proj_(nY⊥)Y| ≥ dist(Y,{S0,U0})/4096.           (3)

Это глобальная оценка, включая окрестности полюсов z=±1.

### Два локальных графа с проверенными константами

В координатах t=(y,z), |t|≤r0=2^−24, запишем две стороны ∂K как

    x1=ρ−f(t),       x1=−r+F_s(t).

Обе функции и их градиенты равны0 в t=0. Если B(t)=1−z²−(y−c2(z))², то

    f=1+ε−c1(z)−sqrt B,
    F_s=1−ε+c1(z)−sqrt B.

Их точные гессианы при0:

    K_U=[[1,−εa],[−εa,1+(ε²+ε)a²]],
    K_S=[[1,−εa],[−εa,1+(ε²−ε)a²]].

На всём диске |t|≤r0 доказаны

    (981/1000)I ≤D²f≤(3/2)I,
    (1/2)I ≤D²F_s≤(51/50)I.                       (4)

Арифметическая часть проверяется без плавающей точки. Формула Мэчина и остатки знакопеременных рядов заключают π между 3141592653589793/10^15 и3141592653589794/10^15. При обоих концах проверяются положительные главные миноры с дополнительным запасом1/100000 в каждой из четырёх границ. Определители зависят аффинно от a², поэтому это покрывает весь интервал π, а не две выборки.

Для распространения с0 на диск: в квадрате |y|,|z|≤1/100 имеем |y−c2(z)|≤11/1000, B≥1/2, |B_i|≤1, |B_ij|≤3, |B_ijk|≤2 и |c‴|<6. Дифференцирование sqrt B даёт модуль каждой третьей частной производной обоих графов меньше32. Отсюда изменение гессиана по операторной норме не больше128|t|. При r0=2^−24 это меньше1/100000. Все числовые сравнения включены в выполненный `check`.

## 5. Рациональная сетка действительно лежит внутри того же K

Для πhat из генератора

    |π−πhat|≤eπ=16/(257·5^257)+4/(257·239^257).

При |φhat|<4 остатки полиномов синуса и косинуса ограничены соответственно4^513/513! и4^512/512!. Так как |(3/2)(z−z³/3)|≤1, суммарная евклидова ошибка аппроксимации Ψ(w) меньше

    ε(2eπ+4^512/512!+4^513/513!) <2^−440<σr.

Поэтому каждая генерируемая точка принадлежит

    (1−σ)K+σ int(r B³) ⊂ int K.

Две стереографические карты покрывают всю сферу при параметрах в[−1,1]². Ближайшая пара сеточных параметров изменяет точку сферы меньше чем на2/Lgrid; перенос Ψ увеличивает расстояние меньше чем в11/10 раза. С учётом внутреннего сжатия получаем покрывающий радиус

    4/Lgrid+2σ+2^−440 <μ.

Следовательно, у Q=conv X во всех единичных направлениях

    h_K(n)−μ≤h_Q(n)≤h_K(n).

В частности,

    (1−μ/r)K⊂Q,
    K_{−μ}:={x:x+μ B³⊂K}⊂Q.                       (5)

Таким образом, существование требуемой конечной сетки доказано конкретными рациональными формулами, а не оставлено условием теоремы.

## 6. Собственный объёмный центр конечного P

Здесь g всегда означает **Vol(P)^−1∫_P x dx**, не центр K и не внутреннее начало, выбранное для механики.

Положим L=conv(K,A). Из(5) потеря K\Q имеет объём меньше32μ. Отсечённая часть K при x1<−r+h лежит, по(1) при S0, в цилиндре высоты h и поперечного радиуса4sqrt h. Её объём меньше64h².

Для добавленной части L\K рассмотрим видимую из A точку Y∈∂K. Видимость даёт nY·(A−Y)≥0. Применяя(1) к U0,

    |Y−U0|²/16≤nY·(Y−U0)≤h.

Каждая точка L\K находится на отрезке от A до такой видимой точки. Поэтому L\K⊂B(U0,5sqrt h), и его объём меньше2^10 h^(3/2). Этот аргумент относится ко всему добавленному объёму, не только к выбранным треугольникам.

Итак,

    Vol(P△K)<32μ+64h²+2^10h^(3/2)<2^11h^(3/2),
    Vol(P)>1.

Все точки обоих тел имеют норму меньше2. Используя настоящий нулевой момент K, получаем

    |g(P)|<2^12h^(3/2)<b:=2^15h^(3/2)=2^−75.       (6)

Это необходимая связь формы и плотности. Она получена из разности настоящих объёмных интегралов.

Для буквального рационального восстановления g используется не(6) как присвоенное значение, а точная формула по истинной ориентированной границе P. Если τ=(i,j,k) пробегает только интеграционные треугольники настоящих максимальных граней,

    W=Στ det(v_i,v_j,v_k),
    Vol(P)=W/6,
    g(P)=Στ det(v_i,v_j,v_k)(v_i+v_j+v_k)/(4W).       (7)

Генератор дополнительно проверяет(7) независимым положительным веером из настоящей вершины. Полюсы после собственного переноса равны q_f/(1−q_f·g). Обе механические метрики остаются I.

## 7. Полный строгий и слабый механический охват

Используется определение физического равновесия: p∈∂P — равновесие тогда и только тогда, когда плоскость через p с внешней нормалью p−g поддерживает P. Оно включает строгие вершины, грани, седловые рёбра и все слабые контакты. Доказательство ниже исключает все лишние точки сразу, а не заключает weak000 из одного счётчика110.

### 7.1. A — строгая U

Для любой точки q∈K

    (A−g)·(q−A)≤−(ρ+h)h+4b<0.

Линейность по q даёт строгое экспонирование A в P0 и P. Все прочие вершины P лежат в K: добавленные рёбра у A, как также следует ниже, расположены возле U0 и не пересекаются с плоскостью отсечения. Следовательно, A — настоящая строгая неустойчивая вершина.

### 7.2. Ни на одной грани конуса около A нет другого равновесия

Пусть единичная n экспонирует в P0 грань любого размера, содержащую A и некоторую другую вершину q∈X. Обозначим через Y точку поддержки K в направлении n. Тогда

    0≤h_K(n)−n·q≤μ,
    |q−Y|≤4sqrt μ,
    n·(A−Y)≥−μ.

Из(1) следует |Y−U0|²≤16(h+μ), поэтому |Y−U0|<5sqrt h<r0. Запишем Y=(ρ−f(t),t). Нормаль пропорциональна(1,∇f(t)). Указанное неравенство даёт

    t·∇f−f≤h+2μ,
    |t|²≤2(h+2μ)/(981/1000)<3h,
    0≤f<3h.

По(4)

    Y·(A−Y)
      =(ρ−f)(h+f)−|t|²
      ≥2h(ρ−1000/981)−5μ−12h²
      >h/1000.

После возвращения к q и настоящему g, используя |A−q−Y|<4,

    (q−g)·(A−q)>h/1000−16sqrt μ−3b>h/2000>0.       (8)

Все такие грани находятся при x1≥ρ−3h−4sqrt μ>ccut и не затрагиваются отсечением.

Функция D(p)=(p−g)·(A−p) вогнута; она равна0 в A и строго положительна на остальных вершинах каждой из этих граней. Поэтому D>0 во всей грани, кроме A. Но радиальная опорная плоскость, содержащая также A, требовала бы D(p)=0. Это исключает не только граневые, но и рёберные и вырожденные равновесия на всём конусном участке.

### 7.3. Вне плоскости отсечения и A-конуса равновесий нет

Пусть p — равновесие с p1>ccut. Его радиальная нормаль n поддерживает также P0: иначе короткий отрезок к точке P0 с большим n·x всё ещё оставался бы над плоскостью отсечения. Если экспонированная грань содержит A, применим7.2. Иначе p∈Q⊂K.

Для точки Y поддержки K в том же направлении из(5) и(1)

    |p−Y|≤4sqrt μ.

Так как p−g параллелен n, (3) и(6) дают

    dist(Y,{S0,U0})≤d:=4096(4sqrt μ+b)<h/4.      (9)

Близость к S0 невозможна: p1≥−r+h требует |p−S0|≥h, а d+4sqrt μ<h.

При близости к U0 имеем n1>1/2 по(2). Верхняя опорная оценка из раздела4 даёт

    n·(A−Y)≥h/2−2d²>0.

Тогда A имеет больший опорный уровень, чем p∈K, — противоречие. Это покрывает всю остальную неизменённую часть границы.

### 7.4. Плоскость отсечения: единственная S и отсутствие слабого обода

Пусть p=(ccut,u) — равновесие в плоскости отсечения, n=(p−g)/|p−g|, Y — точка поддержки K по n. Сначала p∈K: вся добавленная часть L\K лежит в B(U0,5sqrt h), не пересекающем эту плоскость.

Если Y1≥ccut+2μ, покрывающая точка X возле Y сохранена отсечением. Поэтому h_K(n)−n·p≤μ, и применима та же локализация(9) с теми же двумя противоречиями.

Остаётся Y1<ccut+2μ. По(1) при S0 имеем |Y−S0|<5sqrt h. Запишем

    Y=(−r+F_s(t),t),
    n=(-1,∇F_s(t))/sqrt(1+|∇F_s(t)|²).

Радиальность p−g даёт точное равенство

    u−g_perp=α∇F_s(t),   α=r−h+g1>0,
    α(51/50)<9997/10000.                           (10)

Все участвующие t,u и нужный отрезок градиентного спуска лежат в диске |t|≤r0, поскольку10sqrt h<r0. Из выпуклости и верхнего гессиана L_s=51/50 следуют

    |∇F_s(t)|²≤2L_s F_s(t),
    F_s(u)≤L_s|u|²/2.

Первое неравенство получается применением квадратичной верхней оценки в точке t−∇F_s(t)/L_s и F_s≥0. Применим к(10) неравенство Юнга с ζ=1/10000. Тогда

    F_s(u)≤c F_s(t)+2^14 b²,
    c=(10001/10000)(9997/10000)²<9996/10000.

Поскольку F_s(t)<h+2μ, точные константы дают

    F_s(u)<(1−1/10000)h.                           (11)

Это строго отодвигает p внутрь поперечного сечения K, а не оставляет его на слабом ободе. Положим m=h/10000. На локальном диске |∇F_s|<1. Из(11) следует B(p,m/4)⊂K: изменение нижнего графа и x1 по отдельности не превосходит m/4; противоположная сторона K далеко. Так как μ<m/8, из(5) получаем B(p,m/8)⊂Q. Значит p лежит в относительной внутренности единственной плоской грани отсечения. Её нормаль — только −e1, так что u=g_perp.

Обратно, точка (ccut,g_perp) действительно лежит в относительной внутренности этой грани: F_s(g_perp)≤L_s b²/2<h/2 и та же внутренняя шаровая оценка применима непосредственно. Она — строгая S.

Таким образом, **физический weak-census пуст: VE=EF=VF=0; H=0; S=U=1**. Безвредные нули отдельных примитивов не запрещены и не удаляются искусственно. Ни регуляризация трёх контактов, ни предположение о generic position в доказательстве не используются.

## 8. Восстановление, реальные проверки и предел машинного свидетельства

Ниже полный автономный исходник, CPython3.13.5, только стандартная библиотека. Никаких внешних данных и случайных семян нет. Сохранить его с LF и конечным LF как `raven_quantitative_cap.py`; assertions должны быть включены.

Режим `check` действительно выполнен, затем повторён в пустой директории только из копии исходника. Он проверяет рациональную ошибку генератора, все числовые запасы разделов4–7, гессианы на полном интервале π и количественный C-bound. Общие hull/true-edge/moment/weak-процедуры фактически проверены на кубе: V8/E12/F6, Vol8, собственныйCOM0, строгие6/8/12, weak000. Куб — тест реализации, не новый110-кандидат.

Режим `point` даёт точный произвольный элемент огромной сетки без прохода по предыдущим элементам. Режим `build` фиксирует полный конечный алгоритм перечисления именно заданного P; массив такого размера не помещается даже в адресные ограничения этой среды. Он строит настоящие опорные плоскости по всем тройкам, объединяет копланарные грани, удаляет внутренние/коллинеарные точки их границ, извлекает настоящие рёбра, выполняет отсечение, повторно строит hull, интегрирует два настоящих веера и делает полный собственный VE/EF/VF-census. Этот режим **не запускался**; его заключительный маркер не является исполненным свидетельством. Аналитическая теорема выше не предполагает успешный запуск этого огромного перебора.

```python
"""RAVEN_QUANTITATIVE_CAP_110_V1.
CPython 3.13.5, standard library only, assertions enabled.
check: executed arithmetic certificate and cube unit test.
point: exact random access to the rational net.
build: reference enumeration, NOT executed; giant size exceeds machine addressing.
"""
from fractions import Fraction as R
from itertools import combinations, product
from collections import defaultdict
from math import factorial, lcm
from pathlib import Path
import hashlib, json, sys
assert __debug__
sys.set_int_max_str_digits(0)
E=R(1,50); RMIN=1-E; RMAX=1+E
H=R(1,2**60); MU=R(1,2**160); SIGMA=R(1,2**190)
GRID=2**170; R0=R(1,2**24); GB=R(1,2**75)
KU=R(981,1000); LU=R(3,2); KS=R(1,2); LS=R(51,50)
APEX=(RMAX+H,R(0),R(0)); CUT=-RMIN+H

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(t,a): return tuple(t*x for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def sign(t): return int(t>0)-int(t<0)
def serial(x):
    if isinstance(x,R): return str(x)
    if isinstance(x,dict): return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [serial(v) for v in x]
    return x

def pi_data():
    def at(q): return sum((R((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(128)),R(0))
    p=16*at(5)-4*at(239)
    err=R(16,257*5**257)+R(4,257*239**257)
    return p,err

def trig(t):
    cs=R(0);sn=R(0);ct=R(1);st=t
    for j in range(256):
        cs+=ct;sn+=st
        ct*= -t*t/R((2*j+1)*(2*j+2))
        st*= -t*t/R((2*j+2)*(2*j+3))
    return cs,sn

def net_point(i,j,s,p):
    assert isinstance(i,int) and isinstance(j,int) and -GRID<=i<=GRID and -GRID<=j<=GRID and s in (-1,1)
    u=R(i,GRID);v=R(j,GRID);d=1+u*u+v*v
    x=2*u/d;y=2*v/d;z=s*(1-u*u-v*v)/d
    phi=3*p*(z-z**3/3)/2;c,t=trig(phi)
    return scale(1-SIGMA,(x+E*c,y+E*t,z))

def net_points():
    p,_=pi_data()
    for i in range(-GRID,GRID+1):
        for j in range(-GRID,GRID+1):
            for s in (-1,1):yield net_point(i,j,s,p)

def planar_cycle(points,ids,q):
    k=next(i for i in range(3) if q[i]);a=(k+1)%3;b=(k+2)%3
    order=sorted(ids,key=lambda i:(points[i][a],points[i][b]))
    def turn(i,j,k):
        p=points[i];r=points[j];s=points[k]
        return (r[a]-p[a])*(s[b]-p[b])-(r[b]-p[b])*(s[a]-p[a])
    halves=[]
    for seq in (order,order[::-1]):
        hull=[]
        for i in seq:
            while len(hull)>=2 and turn(hull[-2],hull[-1],i)<=0:hull.pop()
            hull.append(i)
        halves.append(hull[:-1])
    out=halves[0]+halves[1]
    assert len(out)>=3
    if q[k]<0:out.reverse()
    return out

def hull(points):
    points=sorted(set(points));planes={}
    for i,j,k in combinations(range(len(points)),3):
        n=cross(sub(points[j],points[i]),sub(points[k],points[i]))
        if n==(0,0,0):continue
        h=dot(n,points[i]);s=[dot(n,x)-h for x in points]
        if max(s)>0 and min(s)<0:continue
        if max(s)==min(s)==0:continue
        if min(s)>=0:n=scale(-1,n);h=-h;s=[-t for t in s]
        assert h>0,'Origin must be interior'
        q=scale(1/h,n)
        if q not in planes:planes[q]=planar_cycle(points,[i for i,t in enumerate(s) if t==0],q)
    assert len(planes)>=4
    keep=sorted(set(i for C in planes.values() for i in C));index={v:i for i,v in enumerate(keep)}
    X=[points[i] for i in keep];Q=sorted(planes);F=[]
    for q in Q:
        C=[index[i] for i in planes[q]];j=C.index(min(C));F.append(tuple(C[j:]+C[:j]))
    return X,F,Q

def geometry(X,F,Q):
    uses=defaultdict(list)
    for f,(C,q) in enumerate(zip(F,Q)):
        assert len(C)>=3
        for i,x in enumerate(X):assert dot(q,x)==1 if i in C else dot(q,x)<1
        for a,b in zip(C,C[1:]+C[:1]):
            assert all(dot(cross(sub(X[b],X[a]),sub(X[v],X[a])),q)>0 for v in C if v not in (a,b))
            uses[tuple(sorted((a,b)))].append((f,a,b))
    edges=[]
    for (a,b),L in sorted(uses.items()):
        assert len(L)==2 and L[0][1:]==L[1][1:][::-1]
        edges.append((a,b,L[0][0],L[1][0]))
    assert len(X)-len(edges)+len(F)==2
    seen={0};todo=[0]
    for a in todo:
        for i,j,_,_ in edges:
            if a in (i,j):
                b=j if a==i else i
                if b not in seen:seen.add(b);todo.append(b)
    assert len(seen)==len(X)
    for v in range(len(X)):
        ff=[f for f,C in enumerate(F) if v in C]
        assert any(det(*(Q[f] for f in t)) for t in combinations(ff,3))
        link=defaultdict(set)
        for f in ff:
            C=F[f];i=C.index(v);a=C[i-1];b=C[(i+1)%len(C)]
            link[a].add(b);link[b].add(a)
        assert all(len(s)==2 for s in link.values())
        seen={next(iter(link))};todo=list(seen)
        for a in todo:
            for b in link[a]:
                if b not in seen:seen.add(b);todo.append(b)
        assert seen==set(link)
    W=R(0);T=[R(0)]*3
    for C in F:
        for j in range(1,len(C)-1):
            a,b,c=(X[i] for i in (C[0],C[j],C[j+1]));d=det(a,b,c);assert d>0
            W+=d
            for k in range(3):T[k]+=d*(a[k]+b[k]+c[k])
    vol=W/6;g=tuple(t/(4*W) for t in T)
    a=X[0];W2=R(0);T2=[R(0)]*3
    for C in F:
        if 0 in C:continue
        for j in range(1,len(C)-1):
            b,c,d=(X[i] for i in (C[0],C[j],C[j+1]))
            w=det(sub(b,a),sub(c,a),sub(d,a));assert w>0;W2+=w
            for k in range(3):T2[k]+=w*(a[k]+b[k]+c[k]+d[k])
    assert W2==W and tuple(t/(4*W2) for t in T2)==g
    return edges,vol,g

def homogeneous(v):
    d=lcm(*(x.denominator for x in v))
    return tuple(x.numerator*(d//x.denominator) for x in v),d

def audit(X,Q,edges,g):
    G,D=homogeneous(g);VX=[homogeneous(x) for x in X];QQ=[homogeneous(q) for q in Q]
    C=[tuple(D*a-d*b for a,b in zip(v,G)) for v,d in VX]
    B=[d*D-dot(q,G) for q,d in QQ];assert min(B)>0
    ps=[[] for x in X];qs=[[] for q in Q];sgn=[];packets=defaultdict(list);harmless=[]
    for k,(i,j,f,h) in enumerate(edges):
        ai,di=VX[i];aj,dj=VX[j];e=sub(scale(di,aj),scale(dj,ai))
        af,_=QQ[f];ah,_=QQ[h];d=sub(scale(B[f],ah),scale(B[h],af))
        s=tuple(sign(t) for t in (dot(C[i],e),-dot(C[j],e),dot(af,d),-dot(ah,d)))
        sgn.append(s);ps[i].append(s[0]);ps[j].append(s[1]);qs[f].append(s[2]);qs[h].append(s[3])
        assert not(s[0]>=0 and s[1]>=0) and not(s[2]>=0 and s[3]>=0)
        if max(s)>0:harmless.extend((k,j) for j,t in enumerate(s) if t==0)
        elif max(s)==0:
            pr=[j for j in (0,1) if s[j]==0];du=[j for j in (2,3) if s[j]==0]
            assert len(pr)<=1 and len(du)<=1
            if pr and du:key=('VF',(i,j)[pr[0]],(f,h)[du[0]-2])
            elif pr:key=('VE',(i,j)[pr[0]],k)
            else:key=('EF',k,(f,h)[du[0]-2])
            packets[key].append(k)
    U=[i for i,s in enumerate(ps) if max(s)<0];U0=[i for i,s in enumerate(ps) if max(s)==0]
    S=[i for i,s in enumerate(qs) if max(s)<0];S0=[i for i,s in enumerate(qs) if max(s)==0]
    saddle=[i for i,s in enumerate(sgn) if max(s)<0];zero=[i for i,s in enumerate(sgn) if max(s)==0]
    vu=set();fq=set()
    for (kind,a,b),ee in packets.items():
        assert len(ee)==(2 if kind=='VF' else 1)
        if kind in ('VE','VF'):vu.add(a)
        if kind in ('EF','VF'):fq.add(b)
    assert vu==set(U0) and fq==set(S0) and len(zero)==len(U0)+len(S0)
    assert len(S)+len(U)-len(saddle)==2
    def roots(A,T,C):
        strict=[];weak=[]
        for i,(v,d,c) in enumerate(zip(A,T,C)):
            m=max(dot(c,sub(scale(d,u),scale(e,v))) for j,(u,e) in enumerate(zip(A,T)) if i!=j)
            if m<0:strict.append(i)
            if m==0:weak.append(i)
        return strict,weak
    assert roots([a for a,d in VX],[d for a,d in VX],C)==(U,U0)
    assert roots([a for a,d in QQ],B,[a for a,d in QQ])==(S,S0)
    return dict(SUH=[len(S),len(U),len(saddle)],S=S,U=U,H=saddle,S0=S0,U0=U0,
                weak_packets=[dict(kind=k[0],a=k[1],b=k[2],edges=v) for k,v in sorted(packets.items())],
                harmless_zero_incidences=harmless,edge_signs=sgn)

def save(name,data):
    b=(json.dumps(serial(data),sort_keys=True,indent=2)+'\n').encode()
    Path(name).write_bytes(b)
    print('REPORT',name,len(b),hashlib.sha256(b).hexdigest())

def check():
    p,pe=pi_data();pl=R(3141592653589793,10**15);ph=R(3141592653589794,10**15)
    t=R(1,5);tan4=4*t*(1-t*t)/(1-6*t*t+t**4)
    assert (tan4-R(1,239))/(1+tan4/239)==1
    assert pl<p-pe<p+pe<ph and 3<pl<ph<R(22,7)
    err=E*(2*pe+R(4**512,factorial(512))+R(4**513,factorial(513)))
    assert err<R(1,2**440)<SIGMA*RMIN
    assert R(4,GRID)+2*SIGMA+err<MU
    cs,sn=trig(R(0));assert (cs,sn)==(1,0)
    assert net_point(GRID,0,1,p)==scale(1-SIGMA,(RMAX,R(0),R(0)))
    assert net_point(-GRID,0,-1,p)==scale(1-SIGMA,(-RMIN,R(0),R(0)))
    assert 3*ph/2<5 and E*(3*ph/2)**2<R(1,2)
    assert E*5<=R(1,10) and E*(25+10)<=R(7,10) and E*(10+150+125)<6
    assert 2*(1-R(26,25)*R(7,10)-R(1,20))>R(2,5)
    assert 2*(1+R(26,25)*R(7,10)+R(11,100))<4
    assert R(1,5)/R(11,5)>R(1,16) and R(4)*2/R(9,5)<5
    assert 2*2178**2<4096**2
    assert 1-R(1,100)**2-R(11,1000)**2>R(1,2)
    assert 2*R(1,100)+2*R(11,1000)*R(1,10)<1
    assert 2+2*R(1,10)**2+2*R(11,1000)*R(7,10)<3
    assert 6*R(1,10)*R(7,10)+2*R(11,1000)*6<2
    assert R(1,2)*R(3,2)*2+R(1,4)*3*9+R(3,8)*6+6<32
    matrices=[]
    for a in (3*pl/2,3*ph/2):
        for coeff,lo,hi in ((E*E+E,KU,LU),(E*E-E,KS,LS)):
            d=1+coeff*a*a;o=-E*a;l=lo+R(1,100000);u=hi-R(1,100000)
            assert 1-l>0 and (1-l)*(d-l)-o*o>0
            assert u-1>0 and (u-1)*(u-d)-o*o>0
            matrices.append(((R(1),o),(o,d)))
    assert 128*R0<R(1,100000)
    sh=R(1,2**30);smu=R(1,2**80);crit=4096*(4*smu+GB)
    assert sh*sh==H and smu*smu==MU
    assert 32*MU+64*H*H+1024*H*sh<2048*H*sh
    assert 4-32*MU-64*H*H>1 and 4096*H*sh<GB
    assert crit<H/4 and crit+4*smu<H and 5*crit<R(1,2)
    assert H/2-2*crit*crit>0 and 25*H>16*(H+MU)
    assert 10*sh<R0 and RMAX-5*sh>CUT
    assert 2*(H+2*MU)/KU<3*H and LU*3*H/2<3*H
    assert 2*H*(RMAX-1/KU)-5*MU-12*H*H>H/1000
    assert H/1000-16*smu-3*GB>H/2000
    assert RMAX-3*H-4*smu>CUT and (RMAX+H)*H>4*GB
    assert (RMIN+GB)*LS<R(9997,10000)
    c=R(10001,10000)*R(9997,10000)**2
    assert c<R(9996,10000)
    assert LS*R(10001,2)<2**14
    assert c*(H+2*MU)+2**14*GB*GB<(1-R(1,10000))*H
    assert MU<H/80000 and LS*GB*GB/2<H/2 and GB+H/4<R0 and LS*R0<1
    count=2*(2*GRID+1)**2;cbound=24*(count+1)
    assert cbound<2**350
    X,F,Q=hull([tuple(map(R,x)) for x in product((-1,1),repeat=3)])
    edges,vol,g=geometry(X,F,Q);a=audit(X,Q,edges,g)
    assert [len(X),len(edges),len(F)]==[8,12,6] and (vol,g)==(8,(0,0,0))
    assert a['SUH']==[6,8,12] and not a['weak_packets'] and not a['harmless_zero_incidences']
    report=dict(name='RAVEN_QUANTITATIVE_CAP_110_V1',execution='ARITHMETIC_AND_CUBE_ONLY',
        epsilon=E,h=H,mu=MU,sigma=SIGMA,grid=GRID,pi_bracket=(pl,ph),trig_error_bound=R(1,2**440),
        local_radius=R0,local_hessian_bounds=((KU,LU),(KS,LS)),local_endpoint_hessians=matrices,
        centroid_norm_bound=GB,critical_localization_bound=crit,apex=APEX,cut=CUT,
        apex_face_escape_lower=H/2000,cut_interior_depth_lower=H/10000,stable_contraction_upper=c,
        raw_net_count=count,C_upper_exclusive=cbound,power_of_two_C_upper=350,
        cube=dict(vertices=X,maximal_facets=F,poles=Q,true_edges=edges,volume=vol,centroid=g,audit=a))
    save('raven_quantitative_certificate.json',report)
    print('RATIONAL_NET_AND_GRAPH_HESSIAN_CONSTANTS_PASS')
    print('UNIFORM_COM_BOUND_AND_CONTACT_INEQUALITIES_PASS')
    print('CUBE_ACTUAL_HULL_TWO_FANS_FULL_WEAK_CENSUS_PASS')
    print('QUANTITATIVE_RECIPE_C_LESS_THAN_2_POWER_350_PASS')
    print('GIANT_POLYHEDRON_NOT_ENUMERATED')

def build():
    X,F,Q=hull(list(net_points())+[APEX]);edges,_,_=geometry(X,F,Q)
    points=[x for x in X if x[0]>=CUT]
    for i,j,_,_ in edges:
        a=X[i];b=X[j]
        if (a[0]-CUT)*(b[0]-CUT)<0:
            t=(CUT-a[0])/(b[0]-a[0]);points.append(tuple((1-t)*u+t*v for u,v in zip(a,b)))
    X,F,Q=hull(points);edges,vol,g=geometry(X,F,Q);a=audit(X,Q,edges,g)
    assert a['SUH']==[1,1,0] and not a['weak_packets']
    assert X[a['U'][0]]==APEX and Q[a['S'][0]]==(1/CUT,0,0)
    assert dot(g,g)<GB*GB and 2*len(edges)<2**350
    save('raven_quantitative_polyhedron.json',dict(vertices=X,maximal_facets=F,true_edges=edges,poles=Q,
         volume=vol,centroid=g,metric=((1,0,0),(0,1,0),(0,0,1)),pole_metric=((1,0,0),(0,1,0),(0,0,1)),audit=a))
    print('GIANT_EXACT_OWN_COM_STRICT_110_WEAK000_PASS')
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'check'
    if mode=='check':check()
    elif mode=='point':
        i,j,s=map(int,sys.argv[2:5]);p,_=pi_data()
        print(json.dumps(serial(net_point(i,j,s,p)),separators=(',',':')))
    elif mode=='build':build()
    else:raise SystemExit('Use check, point i j sign, or build')
```

### Команды выполненной проверки

```sh
python -S raven_quantitative_cap.py check
mkdir cold
cp raven_quantitative_cap.py cold/
(cd cold && python -S raven_quantitative_cap.py check > check.stdout)
sha256sum raven_quantitative_cap.py raven_quantitative_certificate.json
```

Полный фактически полученный stdout:

```text
REPORT raven_quantitative_certificate.json 5962 9cb79690d02044c9b8408aed211bfdcefcd3ad987561c27ac4336cca9ebbe240
RATIONAL_NET_AND_GRAPH_HESSIAN_CONSTANTS_PASS
UNIFORM_COM_BOUND_AND_CONTACT_INEQUALITIES_PASS
CUBE_ACTUAL_HULL_TWO_FANS_FULL_WEAK_CENSUS_PASS
QUANTITATIVE_RECIPE_C_LESS_THAN_2_POWER_350_PASS
GIANT_POLYHEDRON_NOT_ENUMERATED
```

| Исполненный объект | Байты | SHA-256 |
|---|---:|---|
| raven_quantitative_cap.py | 12901 | f6e0aa811c7ae075b95e81247b5b2d14f1b87dfabb3b4db424f29a47e678467e |
| raven_quantitative_certificate.json | 5962 | 9cb79690d02044c9b8408aed211bfdcefcd3ad987561c27ac4336cca9ebbe240 |
| check.stdout | 336 | a0a7f693ad431d6c89b0f42c62a7477dd70c62a9487c6a57b953f84e1c002068 |

Рецепт каждой отдельной рациональной строки доступен непосредственно через `net_point(i,j,s,pi_data()[0])` либо команду `point i j sign`. Его восстановление не требует материализовать предшествующие строки. Полный giant JSON отсутствует: для него не заявляются байтовый размер, SHA или исполненный терминальный маркер.

## 9. Сохранённый более консервативный вариант

До уменьшения констант проверен и сохранён второй конкретный вариант того же нового cap/net-механизма:

    h=2^−100, μ=2^−400, σ=2^−430,
    Lgrid=2^410, r0=2^−30, b=2^−135,
    d=4096(4sqrt μ+b)<h/2^20,
    C<2^830.

Это другой конечный рациональный рецепт, с большим запасом по смещению COM относительно h и худшей сложностью. Его полный полиэдр также не перечислялся. Все арифметические guards и тот же exact unit audit выполнены; он не объявляется более сильным результатом.

Следующий **полный точный patch** восстанавливает его из зафиксированного выше исходника, включая проверки входного и выходного pin. Сохранить как `recover_companion830.py`:

```python
"""Exact patch from the C<2^350 capsule to its preserved C<2^830 companion."""
from pathlib import Path
import hashlib
p=Path('raven_quantitative_cap.py')
b=p.read_bytes()
assert len(b)==12901 and hashlib.sha256(b).hexdigest()=='f6e0aa811c7ae075b95e81247b5b2d14f1b87dfabb3b4db424f29a47e678467e'
s=b.decode()
for a,b in (
 ('H=R(1,2**60); MU=R(1,2**160); SIGMA=R(1,2**190)', 'H=R(1,2**100); MU=R(1,2**400); SIGMA=R(1,2**430)'),
 ('GRID=2**170; R0=R(1,2**24); GB=R(1,2**75)', 'GRID=2**410; R0=R(1,2**30); GB=R(1,2**135)'),
 ('sh=R(1,2**30);smu=R(1,2**80);crit=', 'sh=R(1,2**50);smu=R(1,2**200);crit='),
 ('crit<H/4', 'crit<H/2**20'),
 ('350', '830')):
    assert a in s
    s=s.replace(a,b)
b=s.encode()
assert len(b)==12908 and hashlib.sha256(b).hexdigest()=='32528322958978402e165cc128d60d87201a49b117e0e3da905cfa2c404821aa'
p=Path('companion830');p.mkdir(exist_ok=True)
(p/'raven_quantitative_cap.py').write_bytes(b)
print('CAP830_COMPANION_EXACT_SOURCE_RECOVERED')
```

Команды:

```sh
python -S recover_companion830.py
(cd companion830 && python -S raven_quantitative_cap.py check)
```

| Объект консервативного варианта | Байты | SHA-256 |
|---|---:|---|
| recover_companion830.py | 967 | 53ae3ad2303d6196557af3c3683411c21bc4510e62a14ecc77a99cc43315fb28 |
| companion830/raven_quantitative_cap.py | 12908 | 32528322958978402e165cc128d60d87201a49b117e0e3da905cfa2c404821aa |
| companion830/raven_quantitative_certificate.json | 6625 | 7df44af86367ab5c875f9b8fc6bfce5c394b1425fec88bcd7100242fcb2bbcb5 |
| companion830/check.stdout | 336 | 9d08e598cd461cfc98bb9fc2fa43549b5f8c0d8f2a077c2ad864a81da08129c4 |

У него те же конечные маркеры с заменой `350` на `830`; последний маркер по-прежнему `GIANT_POLYHEDRON_NOT_ENUMERATED`. Новых плавающих оптимизационных checkpoints в этом продолжении нет. Первоначальный подбор констант полностью заменён точными проверками и восстановимым patch, а не потерянным численным вектором.

## 10. Что осталось и наиболее полезное продолжение

Основной физический переход теперь не условен по COM: капы дают собственный интегральный запас(6), и вся механика доказана равномерно для реального центра в этом шаре. Неопределёнными остаются фактическая огромная комбинаторика и вычисленный рациональный момент, а не выбор плотности или механической метрики. Аналитическое доказательство не проходило внешнюю рецензию или proof-assistant формализацию; рациональный `check` проверяет именно его константы, а не автоматически доказывает выпукло-геометрические рассуждения.

Следующая содержательная цель — уменьшение конечной конструкции посредством **неравномерных опорных допусков и отдельных конечных капов**, а не возврат к прежним семи слоям. В доказательстве явно видны две цены грубой оценки: глобальная μ-сетка на всей поверхности и оценка перемещения q−Y без разложения на нормальную и касательную части. Возле A нормальное отклонение уже ограничено μ, а касательное умножается на малый наклон; сохранение этой структуры может позволить гораздо более редкий конечный обод. Вдали от двух капов допустимая сетка должна определяться локальным радиальным наклоном(3), а не самым малым глобальным допуском. Это направление продолжения, не заявленная здесь новая оценка числа граней.

**Итог:** самостоятельный рациональный cap/net-рецепт с доказанным собственным строгим110/weak000 и явным конечным C<2^350 получен как аналитическая количественная конструкция; малый перечисленный endpoint не получен. Принятый C622 не заменён, точный минимум не объявлен.

Дополнительные файлы: [самостоятельный исходник](sandbox:/mnt/data/raven3/raven_quantitative_cap.py), [капсула с доказательством, исходниками и фактическими арифметическими отчётами](sandbox:/mnt/data/raven3/raven_quantitative_cap_bundle.zip). Вся continuation-critical информация, включая оба рецепта, уже содержится в этом handoff.
