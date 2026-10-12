# minimum-0095

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# TWO_APEX_RIDGE_RIM_ALL_HEIGHTS_V1

**Ветка:** [internal-source-reference]. **Исполнитель:** slot-3, Steady Lynx 90.

## 1. Основной результат

Получен новый геометрический запрет, не использующий выбранные деревья, длину локальной цепи, степень внешнего корня, covariance или ограничение обусловленности метрики.

**Теорема о гребне и крае грани.** Если B строго устойчива и расстояние от настоящего центра до настоящего ребра двух апексов не больше расстояния до края B, то существует вторая **строго** устойчивая грань. Равенство также включено. Доказательство действует при произвольной асимметрии, неравных высотах апексов и любом положении предполагаемого U-корня, включая U в B.

Из этой теоремы и строгой части принятого параболического cap выведен **полный замкнутый сектор, исключённый при всех положительных высотах**. Его условие — одна явно вычислимая скалярная оценка Phi<=rho². В секторе разрешены произвольные настоящие базовые цепи и произвольные фиксированные горизонтальная метрика и сдвиг по высоте; оставшийся положительный параметр высоты не ограничивается сверху или снизу. Это не только окрестность центральной базы и не объединение нескольких проверенных тел.

Дополнительно создан точный анализатор **всей положительной полуоси высоты**: все 68 механических примитивов сводятся к аффинным функциям от квадрата высоты. Он проверил 14 полных метрических лучей, включая четыре луча, не прошедшие простое условие Phi<=rho². Во всех 14 лучах S_nd>=2 на всей полуоси, в том числе на 235 точных стенках; всего проверено 484 полных знаковых страты.

Сохранены 42 рациональных действительных тела при явно выбранных высотах, их настоящие COM, все грани, рёбра, полюса и полная строгая/слабая механика. Среди них есть точные двухапексные тела **без единой строго неустойчивой базовой вершины**. Поэтому соответствующую часть теоремы о пирамидах нельзя просто перенести на крыши.

**Весь двухапексный слой E17 не исключён. Строгого 110 не получено. Границы остаются 34<=C_min<=622. Автоматической дельты FULL/LOCAL нет.**

## 2. Источники и граница аудита

Новый журнал research-journal(20260919-070945).md прочитан последовательно до EOF, включая обе полные буквальные payload. Его размер 300952 bytes, SHA-256 `18422a514a758de52888c00988c99cb7f6cec35a2816ea6bd70b279b0c345407`. Полностью прочитан новый material [internal-source-reference]: 9366 bytes, SHA `024d92650bd9a876b5a3bb0a7c8b12ee7511d86e0ba427f6ad62bb402bd75020`. Ранее предоставленный неизменный контекст не перезапускался как новое исследование.

Буквальные parents сохранены раздельно: minimum-0092, заявленный SHA `33edfe049eef1952a3ac3a5789eb77f540643321f9e44f7c8671928cf1039d1e`, и minimum-0090, заявленный SHA `b80d930ce686da64e2396f60642caaac2dc0a6eac08198f422037c15d1c2fb7d`. Старые семь контролей Steady, контроль 3/2/3 Willow и новые 42 контроля — разные объекты. Native 4/6 не называется balanced 5/5.

Принятое закрытие Willow относится к выбранной полной звезде; оно не переносилось на произвольный available-лес. Новая работа не повторяет его 85 PD-блоков. Отражательная теорема родителя по-прежнему не исключает U в B. Закрытый cap координатора по-прежнему даёт вторую строгую S **или настоящий слабый EF**, а не запрет строгих счётчиков 110 при добавочном слабом покое.

Обе обязательные старые поправки учтены буквально: covariance-сокращение проводится после настоящего объёмного усреднения E_cells s=-b; арифметический числитель равен 444690. Новые доказательства ниже не используют covariance-оценку или пороги 512/546/497. Старое замечание о представлении H0-envelope не решалось и не является зависимостью нового доказательства. Недостающего необходимого нового источника нет.

## 3. Общая геометрическая лемма о крае устойчивой грани

Пусть P — полный выпуклый трёхмерный многогранник, 0 — заданная внутренняя точка, M>0 — одна физическая метрика. Обозначим |p|_M²=p^T M p. Пусть B — настоящая максимальная грань, e — настоящее ребро, оба конца которого не принадлежат B. Положим

    R_B² = min_{b in boundary(B)} |b|_M².

**Лемма.** Если некоторый r in e удовлетворяет |r|_M²<=R_B², то у P имеется строго устойчивая грань, отличная от B. Если B сама строго устойчива, то S_nd>=2.

Лемма верна для любого числа вершин и любого внутреннего начала. Для задачи применяется исключительно собственный объёмный COM. У E17 с восьмиугольной B ребро e=[a8,a9] действительно является общим ребром двух настоящих четырёхугольных граней.

### Доказательство, включая равенство

Сначала заметим: точка на настоящем ребре или вершине не может быть локальным минимумом функции f(p)=|p|_M² на поверхности P.

В вершине касательный конус порождён направлениями настоящих рёбер. В относительной внутренности ребра он порождён двумя направлениями вдоль ребра и по одному направлению внутрь каждой из двух соседних граней. Все эти направления осуществляются на поверхности. Направление к внутренней точке 0 принадлежит этому конусу и имеет производную

    df_r(-r) = -2 r^T M r < 0.

Следовательно, хотя бы одно из перечисленных поверхностных направлений имеет строго отрицательную производную. Вдоль достаточно короткого поверхностного отрезка норма строго уменьшается. Этот аргумент не требует ненулевых остальных примитивов.

Оба конца e находятся строго по внутреннюю сторону плоскости B. Поэтому e не пересекает B, и указанное малое уменьшение остаётся на боковой поверхности. Даже при исходном равенстве получается точка p вне B с

    f(p) < R_B².

Рассмотрим компактную боковую поверхность T=boundary(P) minus relint(B). Её минимум f не лежит на boundary(B), где f>=R_B². Он не лежит на настоящем ребре или вершине по предыдущему абзацу. Значит минимум лежит в относительной внутренности некоторой настоящей грани F!=B. Производные по её плоскости равны нулю: это физическая перпендикулярная стопа в relint(F), то есть строгая S. Лемма доказана.

Таким образом, **для единственной строгой устойчивой грани B необходимо**

    dist_M(0,e)² > min_{b in boundary(B)} |b|_M²             (R)

для каждого настоящего ребра e с обоими концами вне B. Дополнительных слабых положений лемма не предполагает и не создаёт вместо второй строгой S.

## 4. Теорема: замкнутый сектор всех положительных высот

Возьмём произвольное настоящее двухапексное тело P=conv(B,a8,a9), B в плоскости z=0. Запишем a_i=(p_i,z_i), z_i>0. Пусть его **настоящий равномерный объёмный центр** равен g=(c,gamma), gamma>0.

Зафиксируем любую положительно определённую симметричную матрицу G размера 2x2 и любой v in R². Для y>0 положим

    M_y = [[G, Gv], [v^T G, v^T Gv+y]],
    N_y = [[G^-1+vv^T/y, -v/y], [-v^T/y, 1/y]].           (4.1)

Это взаимно обратные матрицы. Если C^T C=G, соответствующее действительное евклидово тело получается единственной аффинной картой

    (p,z) -> ( C[p-c+v(z-gamma)], sqrt(y)(z-gamma) ).       (4.2)

Его настоящий COM равен 0, объём равен sqrt(det G)*sqrt(y)*Vol(P). Здесь y — квадрат физического масштаба высоты, а не свободная масса. Всякая SPD-метрика в данном базовом аффинном chart имеет единственное представление (4.1): G — её верхний блок, v=G^-1 M_horizontal,vertical, y — положительный Schur complement.

Положим

    beta = c+gamma v.

Предположим beta in relint(B). Это точно условие строгой устойчивости B **при всех y>0**: её стопа в исходной базовой плоскости равна beta.

Определим настоящие геометрические величины

    rho² = min_{b in boundary(B)} (b-beta)^T G(b-beta)>0,
    u_i = p_i+v z_i-beta,
    L = max_{i=8,9} [u_i^T G u_i/(4 gamma z_i)].           (4.3)

Для t in [0,1] на настоящем ребре двух апексов положим

    u(t)=(1-t)u8+t u9,       z(t)=(1-t)z8+t z9,
    U(t)=u(t)^T G u(t),      K(t)=z(t)[z(t)-2 gamma],
    Phi=min_{0<=t<=1} { U(t)+L max(K(t),0) }.              (4.4)

Здесь U(t) — горизонтальная квадратичная функция, не механический счётчик U_nd.

**Теорема. Если Phi<=rho², то для каждого y>0 тело (4.2) имеет S_nd>=2.** Граница Phi=rho² включена со второй строгой S. Никакой гипотезы о primal-корне, выбранной complementary-паре, локальном dual-лесе или B-входе нет.

### Доказательство

Расстояние до ближайшего края базы в метрике M_y равно

    y gamma²+rho².

Для точки ребра с параметром t разность её квадрата нормы и этой величины равна

    U(t)+y K(t)-rho².                                     (4.5)

Пусть t* достигает минимум (4.4). При 0<y<=L:

    U(t*)+y K(t*) <= U(t*)+L max(K(t*),0)
                  = Phi <=rho².

Применяется лемма раздела 3, в том числе при y=L и при равенстве Phi=rho². Имеется вторая строгая S.

При y>L оба внешних апекса удовлетворяют строгим настоящим cap-неравенствам

    u_i^T G u_i < 4 y gamma z_i.

Напомним короткое доказательство нужной строгой части, чтобы theorem-unit оставался самодостаточным. В единой физической евклидовой калибровке полюс B обозначим q, k=|q|. Шар D с центром q/2 и радиусом k/2 имеет support в направлении внешней вершины a, равный (q.a+k|a|)/2. Строгий cap делает этот support меньше 1. Каждый настоящий боковой полюс r инцидентен хотя бы одному апексу: a.r=1. Поэтому r находится вне замкнутого D, то есть r.(q-r)<0. Максимальный по норме боковой полюс имеет строго отрицательные производные также ко всем другим боковым полюсам, по строгому случаю Cauchy для различных точек. Он задаёт вторую строго устойчивую грань. При L=0 сразу действует этот второй случай для любого y>0.

Случаи покрывают всю положительную полуось. Закрытый cap сам по себе не был усилен: его опасная граничная высота обработана **другим, гребневым доказательством**.

### Простое самостоятельное следствие для неравных высот

Если на настоящем ребре существует t с

    z(t)<=2 gamma,    U(t)<=rho²,                          (4.6)

то гребневое доказательство уже само даёт S_nd>=2 для всех y>0, без cap. В частности, можно взять пересечение ребра с плоскостью z=2 gamma. Ни равенство высот апексов, ни центральная симметрия здесь не предполагаются.

## 5. Почему условие проверяется точно и где его предел

Все величины (4.3)–(4.4) рациональны для рационального chart и рациональных G,v. Расстояние rho² вычисляется по настоящим замкнутым базовым рёбрам: параметр ортогональной проекции зажимается в [0,1]. Расстояние до бесконечной опорной прямой вместо отрезка не подставляется.

Пусть du=u9-u8, dz=z9-z8. Коэффициенты по возрастающим степеням t:

    U=(u8^T G u8, 2u8^T G du, du^T G du),
    K=(z8(z8-2gamma), 2dz(z8-gamma), dz²).

Поскольку z(t)>0, знак K может смениться внутри [0,1] только в t=(2gamma-z8)/dz. На каждом из одного или двух замкнутых интервалов минимизируется выпуклый квадратный многочлен U либо U+LK. Достаточно проверить оба конца и внутреннюю стационарную точку, когда она существует. Это исчерпывающая алгебра, не сетка по t.

Более того,

    Phi = max_{0<=y<=L} min_{0<=t<=1} [U(t)+yK(t)].        (5.1)

Значение y=0 в (5.1) — только алгебраическая граница, не принимаемое плоское тело. Короткое доказательство без внешней minimax-зависимости: F(t)=max(U(t),U(t)+LK(t)) выпукла. В её минимизаторе t* подходящая выпуклая комбинация производных активных ветвей удовлетворяет условию минимума на [0,1]. Эта комбинация есть производная U+y*K для некоторого y* in [0,L]. Активные ветви имеют значение F(t*), а U+y*K выпукла, поэтому её минимум равен Phi. Обратное неравенство очевидно из U+yK<=F. На концах интервала используется одностороннее условие производной. Исходник сохраняет точный y* и независимо проверяет минимум соответствующего квадратичного многочлена.

Следовательно Phi<=rho² — точный критерий покрытия всей низкой полуоси 0<=y<=L **именно гребневым барьером**. Это не необходимое условие наличия второй S: четыре сохранённых луча имеют Phi>rho², но их полная механика всё равно даёт S_nd>=2.

### Равновысокое следствие с настоящими площадными центрами

В физических горизонтальных координатах положим исходную высоту верхнего отрезка равной 1, его полудлину a, центр m, настоящую площадь B — A, ширину поперёк отрезка — w. Если g_B — настоящий площадной центр, а g_mix — среднее середин настоящих поперечных хорд с равномерной мерой по поперечной координате, то

    gamma=(A+2aw)/(4(A+aw)),
    c=[3A g_B+2aw g_mix+(A+2aw)m]/[4(A+aw)].              (5.2)

Это подлинные моменты сечений (1-t)B+t[m-ae,m+ae], а не completion. Формула при m=0 была полностью доказана в parent; член при m получается переносом каждого сечения на tm.

При v=0 обозначим через d² расстояние от c до проекции верхнего отрезка, через R² — максимум квадратов расстояний до двух его концов. Тогда условие всей полуоси имеет вид

    A R² <= 2(A+2aw)(rho²-d²).                            (5.3)

Это полный непрерывный класс с произвольным настоящим многоугольником B, а не только три специально выбранные базовые цепи ниже. Неравные высоты охвачены основной теоремой, а не переносом (5.2) через проективную карту.

## 6. Полная механика метрического луча: 235 стенок вместо сетки

Для фиксированных P,G,v матрицы (4.1) имеют вид

    M_y=M_0+y ee^T,       N_y=N_0+ww^T/y.

Поэтому каждый настоящий primal-примитив имеет вид a+by. Каждый dual-примитив после умножения на положительное y также имеет вид c+dy. Это сохраняет знаки, включая точные нули. На E17 получается 68 аффинных функций.

Строгий U определяется отрицательностью всех исходящих примитивов настоящих рёбер вершины; строгая S — тем же тестом на настоящем полярном комплексе. Направления настоящих рёбер порождают касательный конус, поэтому не требуется добавлять механические диагонали или проверять события неинцидентных пар. Строгое седло имеет четыре отрицательных примитива. Четыре неположительных примитива с хотя бы одним нулём дают настоящий слабый контакт; нуль при положительном другом примитиве — harmless zero.

Все положительные корни этих функций рациональны. Их полный упорядоченный список разбивает y>0 на открытые интервалы и отдельные стенки. На открытом интервале знаки всех 68 функций постоянны; проверка одного рационального представителя доказывает механику **всего интервала**, включая последний неограниченный интервал. Стенки проверяются отдельно и точно. Это не предположение об отсутствии события между образцами: список событий полный по аффинной формуле.

В данной капсуле ни одна из 68 функций не тождественно нулевая. Для другого входа такой случай необходимо сохранять отдельно, а не пропускать. На стенках настоящий контакт восстанавливается из t=D_a/(D_a+D_b). Для слабых контактов также проверяется физическое тождество

    M_y r = lambda_f q_f+lambda_h q_h,
    lambda_f,lambda_h>=0,

и точные инцидентности. Совпадающие физические точки объединяются; harmless zero не считается resting packet.

**Исполненный итог:** все 14 ниже определённых лучей имеют минимум S_nd=2 на всей полуоси. Числа положительных стенок в их точном порядке:

    (14,17,17,22,13,16,17,20,14,17,17,21,19,11).

Всего 235 стенок и 484 страты. На стенках получены 58 настоящих VE и 83 настоящих EF; VF нет. Остальные 94 стенки содержат только harmless zeros. Это подсчёт событий в новых фиксированных метрических лучах, **не FULL/LOCAL census**.

## 7. Настоящие новые геометрии и отрицательный пример к переносу пирамидальной леммы

Полный exact input состоит из следующих трёх базовых восьмиугольников. Все пары делятся на 10; вторая координата 13/2 во второй строке тоже затем делится на 10:

    B1=[(-10,-10),(-7,10),(7,10),(14,6),(16,1),(14,-5),(8,-9),(3,-10)]
    B2=[(-10,-10),(-14,1),(-6,10),(7,10),(14,13/2),(16,-1),(13,-7),(4,-10)]
    B3=[(-10,-10),(-14,-4),(-12,5),(-6,10),(7,10),(14,6),(16,-3),(5,-10)].

До проективного преобразования апексы равны

    a8=(-17/10,0,1),   a9=(23/10,0,1).

Для m=1,2,3 берётся Bm и T_alpha(p,z)=(p,z)/(1+alpha p_x), alpha в порядке (0,1/5,-1/5,1/3). После каждого T_alpha заново интегрируются объём и COM: сначала по ориентированной границе, затем независимо по двум настоящим положительным fan из апексов 8 и 9.

Настоящие наружные циклы:

    F0=(0,1,2,3,4,5,6,7);
    (i,8,i+1), i=0,...,m-1;
    (m,8,9,m+1);
    (i,9,i+1), i=m+1,...,6;
    (7,9,8,0).

Все 120 опорных троек проверяются независимо; иных максимальных граней нет. V/E/F=10/17/9, база — единственная восьмиугольная грань, степени апексов m+2 и 8-m.

Первые 12 лучей имеют G=I, v=0. Ещё два имеют

    G=[[1,1/5],[1/5,2]],
    (m,alpha,v)=(2,1/3,(1/5,-1/10)), (3,1/5,(1/10,0)).

Для каждого выбраны H=sqrt(y) в (1/5,1,3), итого 42 рациональных евклидовых тела. Для дополнительного G можно взять рациональный C=[[1,1/5],[0,7/5]], C^T C=G. Все физические евклидовы координаты, объёмы и полюса буквально восстанавливаются в отчёте, а не остаются только формальными Gram.

Во всех 42 контролях weak000 и все 68 примитивов ненулевые. Оба апексных проецирования лежат вне настоящей B. Во всех 28 контролях при H=1/5 или 1 **не проходят ни старый all-apex cap, ни старый Hausdorff-reflection test**. Поэтому новые запреты действительно работают за их проверенными границами; это не повторный запрет тех же семи родительских тел.

### 7.1. Непустой открытый сектор с простыми точными числами

Для B1, alpha=0, G=I, v=0:

    Vol=551/200,
    g=(2104/8265,-49/13224,2453/6612),
    rho²=12275088849/12629801600,
    L=18290999561/6487694400,
    Phi=273728370319/376286275200,
    rho²-Phi=11360735685499/46471354987200>0,
    t*=32309/66120.

Это строгий запас в полном скалярном условии. Положительность сохраняется при непрерывных изменениях настоящего базового многоугольника, апексов и G,v с тем же комплексом; высота всё время остаётся совершенно свободной. Сам сектор определяется общей оценкой, а не этой локальной проверкой.

### 7.2. Неравновысокий сектор: отношение высот 53/13

Для B2, alpha=1/3, G=I, v=0 апексы после T_alpha имеют высоты 30/13 и 30/53. Их отношение равно 53/13. Настоящий центр:

    g=(-110581120251718704345/83937477439422834656,
       -12517294883790567/243650152218934208,
        458546502015/766648532026).

Точка t*=28403197201/44507897360 на настоящем ребре удовлетворяет K(t*)=0, а

    rho²-Phi=
    6469027149149950190776880085089293290732279 /
    33508398565458044104795767045939680419926016 >0.

Здесь самостоятельное следствие (4.6) исключает всю полуось высот уже без cap. При H=1/5 полная механика:

    S=[F0,F8], U=[0,8,9],
    H-edges=[(0,7),(0,8),(2,8)],
    S/U/H=2/3/3, weak000.

### 7.3. Настоящая крыша без базового U

Для B1, alpha=-1/5, G=I, v=0, H=1/5:

    S=[F0,F2,F8], U=[8,9],
    H-edges=[(2,3),(6,9),(8,9)],
    S/U/H=3/2/3, weak000.

Ни одна из восьми базовых вершин не является строгим U. Это настоящий uniform-ownCOM контроль и прямой отрицательный ответ на попытку утверждать для всякой двухапексной крыши пирамидальное «самая дальняя базовая вершина всегда строго неустойчива». Унаследованная radius-lemma с гипотезой **единственного** внешнего U не опровергнута: здесь внешних U два. Аналогичные точные контрконтроли с обоими U в апексах сохранены для m=2 и m=3.

## 8. Что пробовалось численно и что не является доказательством

До геометрической редукции исследовался 18-параметрический NF-locator: восемь базовых x-координат, четыре внутренние y-координаты цепей, alpha и пять аффинных метрических параметров. В каждом запросе центра заново считалась фактическая ориентированная объёмная формула, а не T_alpha от старого COM. Нефизические промежуточные итерации не принимались как тела.

Использованы NumPy 2.3.5, SciPy 1.17.0, seed 193701, по одному BLAS/OMP/MKL thread; least_squares max_nfev=600, ftol=xtol=gtol=1e-9. Целевой нормированный запас стрелок 0.005, выпуклостный/порядковый запас 0.002, положительность проективного знаменателя 0.02. Все bounds, формулы остатка и стартовый генератор находятся в полном numeric_probe.py внутри капсулы.

Завершены по шесть стартов для совместной цели и для S. U-кампания была запрошена на девять стартов, но прервана лимитом исполнения; сохранены улучшения вплоть до старта с индексом 5. Завершение всех девяти не утверждается. Лучшие сохранённые нормы residual соответственно 0.010636474519192937, 0.007094355702600614 и 0.007211316967381544. Это **не нижние границы**, не точные оптимумы и не исключения.

Все десять улучшавших checkpoints сохранены полными 18-векторами в FROZEN. Режим audit восстановил их численные проверки с допуском 1e-10. Ни один не объявляется exact-телом. Новая геометрическая теорема, её рациональные тела и весь конечный height-audit от численного locator независимы.

## 9. Самодостаточная recovery-капсула

Капсула ниже содержит **оба полных исходника**, включая все геометрические входы, все helpers, точный height-verifier и все десять численных checkpoints. Данные DATA — полное сжатое содержимое исходников, не ссылка и не хеш вместо данных. Ничего из старого sandbox или архива не требуется.

Сохранить блок как recover_ridge_ray.py, UTF-8/LF с заключительным LF, assertions enabled:

    python -S recover_ridge_ray.py sources
    python -S recover_ridge_ray.py build
    python -S recover_ridge_ray.py check

Основное восстановление использует CPython 3.13.5 и только стандартную библиотеку. Необязательное

    python -S recover_ridge_ray.py numeric

проверяет сохранённые численные checkpoints и требует NumPy 2.3.5/SciPy 1.17.0; дочерний процесс запускается без -S. Для нового locator-запуска уже восстановленный numeric_probe.py принимает `search COUNT both|u|s`. Это не часть exact-proof.

| Объект | Bytes | SHA-256 |
|---|---:|---|
|recover_ridge_ray.py|15050|eb21444156306f612f497781aff4bc2e2e2b7cc00ad704f811e8f08d227d41f9|
|полный двухисходниковый payload|25348|2cab48105ada679e873e439fdd10ff70ca1cdca1ed4c0a4d3cb2b4b84b61beef|
|ridge_ray.py|15653|73b5fd7be22e7ce5f44d776b296695dd37b36efc59b62a20fafea7923d601eca|
|ridge_ray.json|1206540|d8133e6253707ae259cf975340a19a0464bffdcc48e5abe6ee3afa16309cb3cf|
|numeric_probe.py|9273|7b7f85e814d1cc648912adbe3c242a94851fb0b73c53b5bb8d9d09de39f96c59|
|numeric_checkpoints.json|4695|a860f2898cb2ff35731dd6d5c4330a14b8cdd209d2e772411a8c94aba011bf1c|

Build/check выполнены, затем повторены в чистом каталоге, получившем **только recovery-wrapper**. Совпали полный exact JSON и stdout. Optional numeric audit также выполнен из этого source-only каталога. Это фактическая арифметическая проверка, не proof-assistant формализация непрерывной леммы.

Последние строки exact check:

    ACTUAL_TWO_POSITIVE_FANS_ONE_COM_AND_RECIPROCAL_METRIC_PASS
    RATIONAL_PIECEWISE_QUADRATIC_ALL_HEIGHT_CERTIFICATES_PASS 10 14
    TRUE_E17_FULL_STRICT_WEAK_AUDITS_PASS 42
    ALL_14_HEIGHT_RAYS_SECOND_STRICT_S_ON_235_WALLS_484_STRATA_PASS
    ridge_ray.json 1206540 d8133e6253707ae259cf975340a19a0464bffdcc48e5abe6ee3afa16309cb3cf
    TWO_APEX_RIDGE_RIM_ALL_HEIGHTS_RECOVERY_PASS
    TWO_APEX_RIDGE_RIM_SELF_CONTAINED_RECOVERY_PASS

```python
"""Complete source-only recovery; CPython 3.13.5; assertions enabled.
python -S recover_ridge_ray.py sources|build|check|numeric
Only optional numeric mode needs numpy2.3.5/scipy1.17.0.
"""
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
assert __debug__
DATA = """
c-pOedw1GMw(tM<Q)v3Edy(vd=miLq>NSo-
;&fh4Y^Rf<xhw$!l<;avIJSHGeD?F(yGjo*NqXkYiUU&Bu3c68z3agrKdrXQD2d0zO|l+Ejm_OpCqMnh|DHx!lq};_oM!RZ&|u-
hU_fEKd3$AqD<ircFScpCUUdm%bLTd^M$<^g@#fBHIPHerP}qK3#mmh)$&7XS+iJQ_jFl0u472w3qW9*>tJBNjo9oxZtMm80)2Ej
;QG5IPVz1=&%U3%k*2y|;M5~)PS+Dx5fvh>Tq7NR45vIm!BR;3=l}PW>qLRmkF(m7ydTy*YS-gzzBSS+hqA<;d>F?VxiO?=g(}<9
68pGjDl+a{{Ln&)K)f$K}(Rg;N)%0t+r%jm67x5_X;sUR~t$tfgqNy<r$5Co7t&`tYMiOP)WM%Xhpt_lat65|QmNhu;_hS)=_}Cd
3M7)@Yr>d7+yF_hAEK#puJBMM99nog^HXs6F4+i-
lwyRAz{$kz;HI9+Qbnl~NotkDKJj?2i`X_*wH~o`fKmh#{!sZMJFd6pij=1RuC&BTu?hH`OAb>b2K^TJSPaJn3>J0NM)!n2S^=*z
spYYgdBKqokU|E0)7n^yAuF<ahLH_#4bdI^`=vNw)c(Yzb1A;pxY+;gwcV@qj$LMxrqLnwW(6!SX&}VA^<hCeleO235<*L(?6TgZ
N;xs4HELtz4EV(Pl#I>?QyY6%<bAF;eOXBK~rhR)Lrv1<SLA+uHO^HF%DL;QMndOK@v@)kw-LZH;H#hP_9|#BC3E_<5Rk~f8wfM7
$Ki7YbYvSgHSwvGCgK??J1)wE=yNZ<AItv$a(xA3hceaCx5q++S30g2fcpInEv8+d?f5Z(5!$)a;sL!mwpEj=W_D=SRkCk~4U5u4
1M)48T##HMcdHMrE-){L%D2;cGaI=Y46La;*T>U+-u^4|rzjyQ=r80#AMHBOnY`a-
RrhYR+F|sV{0YOnrZ};)WoPz4k$>4a}KXC@upM-6a%DzJLS&?6G+lZ}Qm__DvY8mm=2pJ=*I-
{FfRpe1R*b^8r6CcGp5v5|1=E6hxKn)R1W>L!0Gm{_x{;_e@WnxX@aAwY|ZbC29?P6h?#Q%?$P+yj)yA4Z|I`5cJF}(pZ%jVQH{X
NOdWq50@`r+Vs)gKM&?$NA|7EsHm?%B}ggkPnpit7YvJ<8jvH-
!+8BN0|1M>~+C0<t7P(xBe8=oFKW(s;5B7o;R&xt>I_Hd<%%TB$`<lF1!KBh*`-8dz-
>WK3xy>0bFev_|=Qn<=>j@2EHBYq&>I+mi3tX3+nPMQ+m|FSmreCtDJbdc(Gx!e;S1)IR-
o`*gqkNWw$~;sk~(Vl%h~V@EK4f(c|>^%0=PGAa$(kvZzqgCO0lliB4rh-
{spoCi>L1<Gc9T88Nt`QN14ckmx#lHF}0Ia;q5*8ltOd=Q6fg&r31%{V;8`nXTnd6KT4<Y7pb>FLxgJcU)X>3#!u*+hE|>&M+V$L
trBE1+TJ;9493x(ZjrY(0cho4_IPDxIh$HtRHAP5E&Z&FHa?=R#!Rlt`>rGi~ed7R0~>j3umnWP*hbIb5rIm+VwH#NBqC<@T%8eg
<e7+f@wRU2;ousF=vXYL~0ic|6VJgLXiAo4eevb;5CEI`zB7(UEJ3ug66}LIs0k#<D{UG`tme3kWJX>bpcg*bTAYmjK3{GEd;2Rf
G)5c4dy&+f~L2t-
_ZTdlWdZ$$HrUP`F)WLzJ3M$7|alRuYZZ37Opi2#{t(eQnd?tn_`1mN6Pj=^V$||Mj{zvdR&v3RkJziPg;9%!nHiCbLwU%Gg)}CT
X~uMmMr$+hUrn7wEX&5x2$DtauusZw$~>w91WfAnJi7@;6`98=X$aqOYa^Vd&4X^Z)FFcN*`sRZXcSQ4~%1Px(9JCd}n5T+A9PB0
T1arYo!a9YaYlx0)`nmK7^WMzUfY86X<VNj%QXSjOO<)Fzoe#CQ#^+z<&R<7|L16pTU^!msi}`8t!c^5s;XmM_=r!WLn+TCXUEgk
61XTV?&_gZgx*ew)Z-TfU}vO^a8a0L(Im_?RTffauUOc-LZqF<7o(9!z==s4Ju{k23ITbvH@80tGVdkO)wqqF=kL4b;Om9;V1{=J
G1pM%*z6?q+SV9)qI8+A*~}t~Dshs9BA#NsQ7AM#`j;#sql?2_<(fVrb1Oldg4K`|US?S0=)PA0<)vg_P^r`?vq-
y)mTG|DzVyP7GTZwI#kC`bLL%)V|255xWSaVK-
ZD;P_sr<usjE(`%#h1~q+z4Q|j5f@afoJDp~`(`pF=g?`iaT6W8~omLR|Ems&$qt)rOTW!a7J==4d?SRTUp5xg-
h_<c3cbmchLc9gdR=a82f!AyXTo!cf!0p)0w&OT0w?$=6%V~FPui5c@8_<ld-NcLIwK2+;?V!wVGy}KUY_<H3>$O^e*P=4p3GBe{
U@Dys@BtA<jpDZ732ev57r<Liz@?ZAO}+&ZxIo(WxzzK6pyPB}owkd*w#R+7+fK*D7}1k&WB61C`gl#J3EDWFz_$qy&0P$+1#-
49@|NeesMKi$zT>tXw-
a=H+i!b5&B?Z@k4^yk1UAqNK>JIgJvhfN*YpDR0YxzQQy7Y`j^?ZTUA{V<CdS)#nZF&k;422`f|tJMxwhkC*mjEt=sC9S0~nKc?M
~BUX16@gcYz3Fw|yUz_8VT{G=0~G5IDAD)9jiJI|u^Mv`NqoQQT_;4%lF~&@jMb$EPyT4xRcf&-
cLsMOMclBD5hGPRnDef+fDwveAW066QEm=y#fa2O{AE7pUqfz!n6zZG(gz@U%m+1Nu8Iq@>;U;Wr?bzGgMJgJ;M91Q4)(hbN8ZO&
=ob(lmn(&l&9NG%+ersqJ|r^-
iPd2QKDkV~7ydfaIjrKo5QsAQ&tLrn+g`feq3^F;Lp}3XWpHttwOTjs~5Qsoq~wRt(E)L5Q0UM9%G0wAE?2G;s_L|J#_7l4S^M0I
;A9{b_-<EOuaZ8xv}_?WW&mh4VU1=sF-gyWMUPQ$5Hr*aDSt0tZ-JUzY(9)EEj4ma(qlkrV(N!@yc?>H%`z>_Ew(m|h$0iCa|fp`
4V$W4R%&IMhX}1CIG1chmEAG3*YY!2<LQIa8d4C4%5UE?@{;sJ3Evn`jPe0vWP_j15C404~&YT9C(<D)T+R-
2t2(G)XR4`fLw_$2(Nh$Glk50#KnHK;X$-
bQ}isVQMgVkP+JIL(r?L+A6q;7l1cQt{yVM+g+A|VXY1Xs7bSGvtX7iMgKN+47<}*5=#adLnQu#i^}{u0gEh{LgcdB%$7Fh;6iQ4
GPhVIp$;U*ZPzE0-d6mCIyE5;m?_xYRABVvdf+?>1>5M3525y9yTEnk9r%eS$MHN6rR}=`Yb5%I<hMyvI&E-
X*+bX0n*qcIWOqptm0-d$wn&Zx@Ez7qSzd^@)AR!9G<DTv%in^Sy5Jhb2dwXKM-HSH#PVRL(H<J7#HQ(CZtyQqO5cHzL8%8b0Wv{
n!O(!oYd63|5EKTi19`V;S*he^^V^2k`wQGueLGD|xe2%DRJduA+`}PZ>X?uhXa&VgLH__U=h?($@DpSJ1)(gkw5<-
iPS_qua?tYNlmPBiSqH`do(94R%hn`KhK+@~L2l7W8(93NE(0X_G8jJPy1)ilDAy$~(Y9TsG{6M<g0CP+lfgh^xYKs438#SBcuEg
}1B4F9B|yG>#XDH$re_B&vXPKIr8hQ71e^(qn&61zs-
8%lAkrSXfiKXe08H@$&xaC|U@)6~uLXnM?2u4{<t%nV3qvI4f*LFhYy$#lcYtBSgh9-
LDnni3VMRlmq_G80{R7VQ0Z++lxQG#eKEU8AArg#<M_$yyl$y4RkU$tne5*r~fo)Ol6*>i0!_LBhbzGmR1HRbcdI0wYhXYisxE(U
jAbAVo&~7Sa?zoUxs5A)Hv{~odkoutMK&PPtE-
3(9I4nD~4?5U(J*AO$lbj%YGe|_yfQnl%T4*Df)FQD9+N#j*ut3=G?y#Pks{wQrV-
6fJ6?(?1Pu`A5!Epk7yQ8eO0|x{Ifej+Tagzj*4fEUNmJkR)WNaN`!BE3b!EQh@K`UPo4))52Y_ut41V>r>?T!O$Kv5(}1lw2js3
lwdeN}C0wtC-VD|`b8MsA*B8o!K?@PeQO11F=}akU)-pCNlK5?tS9Z$YK-5EMc-
c_MBeY}i1FQ6sK^^+Gg4Q*pgEIWL3|l+`j9p*^reu+KL5;M)v_h&FI2gn-TMD02q_!R>$q5JcDmWkEqz$cGP<ZK$0NQ!zwF=95_=
Ys+#*&V`i2fk3*p)?!#dun}?s)G%62ZVz%$&<?kaCLp?+B!M*{WgVXa#}3<2gkF#pM8Fs)0^+8cIl?s14l+PdP@7bRl*B`Dhaeka
Ib{+mk|0}#7z>gJfp`6aua5Ge2$uHrw!OpPL!LF=XE3}!Yzh<;deXFa_130v7ePH_-Lcg;K|=&T5C{+&qM_0lm|KV-I1dT-
NE9gKfxkuA1Dv3><8fI)^lU-jeMMo2vqMP$5|I{3nSz3ghe@Oas6&AV^#H2~T_Bs+g4OkuZ-tG3=LbRrF%BC(NEgTt>w%aG^zG!n
)xkT=14UNK7`A9g5Ia!66~L$}W^?3CAq^=L+`W?1fLc=Cg~$@A4F^gd6d0+SODYZ)YNRcSnGt~_Q3H8=R&AId(o0w-
$guBf)h17mNEF<K)5WyD>0B`_6&C*>w|T%;7&)3CLU!1jW;I@F!ufgN4Wbf?)>Mp-s1zYV3-$-
Jw>@Q*DBFQcX^{Xh{}K2=X5m|!FbYTjTS`hvk-!{}2;#CcWx=MPsqNcMS3x13qKtvucA#<{A~?j`ZBZht2xF51ASOl73F-
6NI<J9&AcIZuiMBL&fD!1BB}dNNZWhKE(tscWNjk@)%83xS0qjy{i%=&}pb(#+&4B_1c24fMp$!--
>^He(mdG~sPr)Nmq1jQ%s!dTD{0(^PQl6o-
7~vM=6fq<vmR^~yx_h~e&3vse)jeR0A28J>Q;5M(fZuW|#u$`$DRM%R3~$lYiA@_5Mw9?WaVTkZ)VL|Dap{%JlI!Z!pOSEj>OC^~
o-(p9R7knu9*ImH4yQmWcvFPUElMAhOxWbGDK#ON)>dtyyYR0NaQJ>uPSKWliX_M<-
`|0`;l&6F)=&YV13!FTK|vw33qh4jJ{B>*=2wUEXNvA9Vd`jAqGbUDL~t?ST-#Az1Pb5ATp-WLhCDrSi~|FL=?T0hdrmSU@cT4Qh
Xf`F^x_13608SB?UXB`u-Ryl8d0jpF=4CpvHqSFR-
9IeYq6diZYObO@~W%erJjc=ZCdLE+Jx3;)!Gy<wB3|jb4ede9(;F!@<sq?SsN6KoYTcR%*?%|&dNTK0_QIhwSlFU{`78qI7&@msi
T^OZ(z|PnqyZ$_7@q;CDH0?qm&7+^!=zIFP=VVc*zadqt9wRH65=vk*vMBe%*Wj;%xZ#&8tttH*c?oXTA4VFP^>VJsm!I`}9Tca`
^WBu=nxo)%E3zw{L2K`c9*0BGoFnm_)Qp8Lh@~lq$r0q9H$WAo#dJal*jj_Uj~`5g~`kcBLE9vV*Lp@vYj+NR9D&xmiS6Gy#flRq
!h3R@PSWD$1*q==W`uqPhza$f6|KZt!A^?u_U*8gH|By)qW@GS0e28s4A=@{_D@qGhx~>ujE^x3jrIW;DCTYHf@cVZ1cL#lqlz%K
p`4@?8QYZM;((W}&REs)FW%HvWcRqPvtAXhj-rLNIHcq|&Sj{5z>x`C@AW)PxwBgli+!DsF!CWjv3@Up8w@E!8Wz-
Hl$$9o-S{sdH|~OUAXU-kV|0;<NMK*~^Q!FWy{T4&V3A-
hSx42bYQG7w4ZYU!0x3%9($5deytEm1t;RY8mnFF5?$k+ZyRSgxgSsjd^rCiD!{s`HrW?a7fMggvoHY4CB>sSUXWWmFZmyeVpCUC
Zv@88Y^^daH18PcFz|8qaJfmNU^U@uoP|4w3bF;GM?9VYrMhUHmceRrEMUZPXXr+EKzBs`c0#gB#hI@xV(cPEqk{ZQEhXV%^^DbN
05{yGX80(VHjs`uiso5)a^gF|4fO5KZ&1`cruHIFh12YOIN?X9iCqFJ`Uf%c>27D&)37#SFeWWy%*2V!JrRL*EqXSox-
z2mjp@WY7!<B2=FKgle@-mtKMxm&Wvfif&@S`S6Q-
Nq)ZFgsR&R4A`BB`e4Vcsk<oM7<uNGQj&K~?2(t{li4vgGv#ehl)iE2RZM>NLlV#87YSRM*sj=LqnK6otXcdkY(F7RsBUF5nXqsS
j45+R2GhILjo}OtSj6BKKG;9q74I9BcaKrB%N#dF%9`oXuw)%_1Q(8tVr>eBg91bVZXgeDYe_K5{z3g4eKG;sjdGv-@zup%7t-
lZ$wCJm)4*U3`4sX>DM7@JA-
b@<|#6Aju5p=z^kLsC;;N7(p!a8FF4n#8WeBVS>_xZsU&4W1g@ai7En+gkT{prPvGn$?G%&a>EY@u`ha4bup)b;iXsnM&8^HVg+3
q_N@>iXMJo2pt!2`aCk53YORO4HN@w(2KGZ)xW}neY*q6TQ=`PPN<~-
?8hy6?ge57(OSXceuBsLv8BcYqQ)g%uIxPZL*_V)rMMx8g#PGcF@y_BJ=j>Fm^RD)li)qsx~!4*rlTpOiMk)2cE!V{bW;_t!jmSa
;VHvwfSfw9*r0mNY(gMXH=fg@Wwn9H+vH#*kt_`<th|ff2Gl%>L#Oj0ZgZr0V~{$svupw!YhYY6G@{vI<>l5dnP|q;4)rIQw`^o=
6A}LG%s+ez^)Y7RNxG%XB{*%_;bAOe;)MX!K2Ck!7@)DlZtnW_Rb>a2N4yr>PbXXpG33{o<uZ@lZYC&a~L*1iD>GRh$Q7qO4@yg8
6Gaz6g`+1Vmf7-
J(VOOT@*_t{nn9p;NaP}57DX3VHN?|zW`;*F`4@Z^DH`KS4s@Ge0nS=+&!rpz6GhmM6lv%<s%{D^NNbAPnoNll20GCxP?Q9>7H5w
7;@DeXB6=+1)phDC!*NEY-
m)<m~2QOa=W6axuKD>t?kp9%fYcSO(b5?O7`<3l7ys$|8<ay9Bq&T(Bd&($i5oeL~Jy6G0FAwS3z)t>e0q71?%C0k8!|7r}B?Kb6
&&;j?n2Nfl6}8>RhNZf#O1+^b>iZTPZBGBV65?tD?{1sNhaIuvoB;t{Bs%#37|kp;4?3@KGFM9E5vpD{&B;-
O*pDtmC^!3AJRYk+2|ed_blUv|$3N19#K73Ym|&N|q5#KP(6m>sLz<qe_9DsyXRia{Fw|w~K{LBNglEA&W7ARNcSUW|AiF5Nr0vF
wV!I&ns}~!yGxG*eG6YBc0Mg9Cm3-txDOu7-$S6dIWC$4CbJg&I|JUV`-
nz92%rh%JRgTE!i$x7(5?MR#iHtf!sYDI^8`OO0vpFCl4PbjWl$WbMVhX63LjT^P5s4>Z6d5iU<fLo=?gLU554+Oc(q_rzoulM>h
wotTWjs*T{^G%AQp}`-T%-D^!@8N<`R4!Et|i?24eiB#bxfg_y~MhO|4SGgHNh-
Eb4J$2MWIl_ZSEq|#rbcs9>iyH)EQll#Et@(EduYPus7KQzb2I0Cy&YAqfZ;Vz4>nCzQtYBNyHze-
vNAWKa$2P!M69p?|Q&sJ$jzOu2SUdOo=AzW5I;k@vxmCsw-`iKs>!9af9HTU#@@mae|6U0o75JJ&90zX(%3hQ45U`GJ-
fSfUH>ClxP1}E`E8p-sbp{8;?7D(KOKnh(*Wr2rJX7`om&33e|dt-~4{Xif-vOwrD-`G;-
;{>cU=_I_Z4q)f5fmJ&{n+=1+eXNwZC!?tCGoc-
n`uGmu8eiRcG^3cNtjtZ|@8Xs;s<hN32Bo#8>c@^gq5b==C3vS*MBMI{f2;;ZOi4QDrfw4Or`RM>ybNcNWCyoil6|DL1H6a}34I}
FC#O?&Vq5a3VD;uBhS0twqV<_*CKNZM(!81YC_jpK@*STr&ElJA$ZAI)c`zDN+BuHgVH(Yt8yi8w{+!h!lDRN<GfA<f;wnV?xrnS
sR1)zcs>yb;Zjw>u3_)4LiPVi)R#ns<kt%445RwUyOp4$%jVF<d7Eh`dQHVii5o23N9EfmiZPm>p&gSwQMtjnVw|pX=u(y1|-
col63%;c&730l=O@yrW;258X+%x({e4ia<`TFFT669%2C-2NPhJM2X)splaP4NdONg}M@j-
CS*{(k0nU_ElnYFg;vdV9bT(7Io{s13R^dYI8exLk&k1hzYhvXD)|tbc+yoT$mQ7=qP(BKsREuBaT{k*TOaPFq3)@)CD6|H)%M5C
sNP((rvs4!X&F?ebB_0wH1FDmy>}-V_7gPzHhV3PNAC5B=a|FzDXXEOsYB<-
A(8{v4?l2iZT2^FXWhO_a=G^U(yc!oMg&KmSOC$_^`|qi$cZLa2P~IW&gMEwk!qo)dGP<J^jSuy3+uP1#a_y`|2(lY4nj!@5_JaV
;4i)d3}g2=}N`G}(fvq)uD)LM(VGO=^C`pL79(#z5^R_qt4%;C*t>OJsEDxL6^u^yP)gJ^M*GV2y)EWj&hQ>sZQuoIQ3<sB!K!vK
*Vb7h!eB5czmQi`eAQH*v&rm&X7Lk>muSMuI+w)XG8U7ECI2eJRYvabi7kDRkp_VJ%hc6ds$ejz%=1yooa3_5&Hd7B5SW%u23tQN
V%G<WVA5sVE_nb+!tRKm{(g@~~rp=_e=I?&J+M#~nAy>(;dGz+H%!!_|7Vie@2CE+4Y^eH%{TJ>sz>!^BJ8!%S-
TYLtY`?;)5KD~3OwDo3grE8=F3z?Jp0Y+6hml~R-S8f}kX9Tm1bC$=)>|7EBJNxtzA-Wp%yY!#*Hi4hue_Wp)C{%-
J!O5YZ*2FBNUgaX|rzK>Gl`uOf;gRU{;Qub=l-
EQPH$a?G^U9+w2e%Z*Es^BFTC?Wi^VXJ9Bmi6uC(U;9*`Re4ZAg?Op+YV}ARq5g(-
KjfD6<N81s2miFEZft8QWCN(@A09}+ZPWVko^t-sk05mCT#`S24q>D(lDH?@KQ=}=cJfV-
tk=}bSWxn;s_hE;T?BXl<$Wh6vGWmb2VIVGja>VQJ6+DH<v=8TCBeg6>s&`hKbaDi0AUTNas<Q$Qw50lHG-NR_v6LcsZP}llUHic
(^DKkgwo63S@?*2P&S#EBQ)XOE5yd6xvLvFL41`Rl<xoI80_B7on?DS#^Q^vUm3O&C}uK)%zD`SHnwb0^l)&TE)GZdALm{>ts50V
b#yXYebT~CPrZq!jCIucqpZKkRKQEJq1IY6Uzsl;!0exr?^s{B9ARdUewMKzgB(beh~KB`T@?8u_TFo8ueLqO=fV+Wlt()XZbQ@!
Z|pz1;+VSg)m|yWA)z9@#{LVL|#-
0POG8wQ7B~vUR_Q+8c|`TMLE`IoU^D=Z02_<UFJp{H5TVQh#~;`NDm+J@Qxnd)p+3tPaF>8?YSKHYtQj;Lk}#9RC*(qHzoyT!1Y?
1rVhb`j<v+|8}^*04!ML5&8Xbr@*6ItH}<AC9N`_GADzQ2ypgnc`g$*Opgig|GQ<9t!O<IhP|iRU|FW~NDJ9?Ykn;0^WzPd^qv+!
k5_pP6j%iFs9OY2ZLO0Fy>p6ezFK!&pygzZG72R&2_|QWWR3n|OF&WAihp?*HlTa6#*?J)*SEwYTHc&~LlsQIr5ueB)%?;XXkH-d
ICVeg(%ZO7WBJZ)dGqQPPq~S6uxNr2f;{{Amh;(2*xii8kd?dWeW)ZH!B=;)GdYzHu7$<U9cr}Nu?ituUPI68^8YlS%#XdZ9yj}+
5k8%`D^?!isM-ZYj!4ak<_DK8*B6lxl_YVmC4<c|W8aMY+p6LYOO!Zmh;Aky%Co|Pao{{#7<oUkR=ReSABxccrK6^Xaa|G{kuR4g
T$#d_U*P~0L*3)aDz3N(MPp^gcDp#R_t?+=AjJ#K7<Se_N4y^)!cCViw&`Q0Xw6B!AyG)g>Cgb^q?DtiC{hAg!sRy=`AC>Nf>bd(
%0rqAG>|F)yT_r~X-V*WiohF|?RodW%0Q0@25~^1L>QxZ`@(u9nKzi>~px=)VEVt#Z=s7Jy!NfdP4|+lB^8?t=f0HqXE|&-
JbqaL9Xl%b6M%LNIr6+SO|D7@Nav}@}uVBD_<f|-
E*=cmBw@dji&mixLR!IIzPw8U4QF%!kPB=XY$6un1HWa$^Fj+1TN|h?~MW}oJ!ki+KvvwDJ$WfP*6vZGc6;RwuqE0xV3-
Rh9guGWuM)V+l=}!m!`Jm3<)9U-
2zOAkrajuB>)rCJw&5kK`e5_U>?xDhX_wb&td?Q}Cw;tOkm~D>Y3!~tZ8LC=JyGVNo<s*~7>V&y4IS9tH$I@XqKDxr|6CY_(YO#l
Gz(<<VM_z_k8B=z*k!I~fjWb7%Zg}N_GqqZ;W*wWgXVpsgq*AH+Qv7M8QKql=n%uqM7?-b-
<3p$+sT#F>*2f?U?i`rA>hUCJ`VNF%=huCoR2Jhetz-JSw(5MUC7ghIZYjZx^ipAfr~OW-
O2=fXXn$rj<8T9~<krc4&_X7N8Dk!BT@VPp#8lO^xL8dmk<BPT$`Bm!xev{tV3$E1!Wn1=&Cng0K!%5X<!`HQA_zJHDh}^!<T#J<
b~wzhRhL%@U!K;e>#P|^R7XYGOD?N_2i;#Jo)&N*e@wG}RnilKc&rk9J_S_Segt*Z_Twgulaf3{6sx-#$%5)sU*^pt<FQd^?nIQ-
OXUnVBMtUMex&s`L?!G8sn!(=)GBs2Rh&*+W)t}!A$iA9P2%!e(nJ0ho8jHFGwJh6kV229x*u8qTTGH@x=_iUJUjbY&L?aY%(Jul
d_pqxGg>F^(R{L(DdzFnFv{aI`eC6gri82~irUS3K?U#1l6)EZzAQR>`&vSl&gHpyEnkZ_@{QPl)u@>z;Zi=o5QIj({32l1ReDG;
yd;uJW$?tMyyWEYTmi%r)Pxgpd3`SXN@ax7M3HOaKzxnDFT>oT^Qp<)e6RqfrbVaTl)?|`tmRPIio8rfLWU~eOeLNLh&rS(axP7k
8wiCo3t^H7RS2e}yn@(ahA0?b<i_)fs5ChPyXY4K==UW!Js;B6Mwv*vN-
>A%cAE}Kaq=q2x(KJ!cohxD>vb}r94soC_vt{Tir6J$o&ycbZH0%G%-
Q_d#uh};3kJ(*JP%j#IHlx{ecyi>r;CNr3XC+Ktx|)6dWDV`XXN?+cXjArEZwCLop?1f*0h|rKrTQ(0FlyxPdXoGAT!fRps1vPwC
ABxN1+qPourU|KnY@&ns>@0{|B?gyWJeI_!+Ig5UGm47^lu0@!64T0vru@XRi3{79}o9q8mE!s&?SJOtLa|sRS<hvckb=g-
Me*vOjZlY@#0E*sCQfTKVkg@I*aKcS|^8;YBpqvi{7?Te~^FN{Pbf9+{ur9D%D)TKlCc5E|$uJ-ElCus#x_diY@7BymLI(#a7bMX
}?$-
ak<>UhkZs2<c3~C|}_nvC*uDk48V+CyKy)Jb+4e*UbmV`362iAymr}IyGDg9~ZkJBem58m%Q%%g?==RRy>cL$Gq2104f5apV!e&Z
gHY8?<_EXiB}U@`xRcY1`9aN<N{U#`iSp4xlr-fH=EI~;O#X_&`dA3Q=f?%#p2kp^1~ha5Sl{Dv$&He>(}mR_i7_P%Us=Pcc&j7k
M!BQg6vAh$7{|^iARH+GxzroLv7;dz4$?x4G)&Uj6&Qtxo~ZAajTRlal3<H<#Lq^+fG?U)QTV*8NBL)O240DeJ0mEA3XkCapCiQ!
1!-
+uDbX^0*GNNbn4+DJ`GzUJpXP+qY|cgBJS_^G8wBlR>2toXAI}L*r0_9#mkhTk~8pPV#%LApa)$_B=Sr`r4rxFCH{qE!hmGRg8!<
gNwk2*X=Wa22G%u05%QErR{)ov##l_Hxd&=JVu<cyE=`SXuS(BW$Lv#D3FhNC^ZZFgk1&ZmBTz^c%*z5j<JTLWZtjbYxSCSAe4$D
eINBTSLO8n+YT<<UM!Coxe9vcDI|F#Vsjj#@zuE2SrrJ;5QcoWU)JYZeyO@f1tVsMa7c}D>{9*d{{rvAx0{9=!0C%NXcl#g<%%R8
-l7%CyS)+>zY&cIUYr>f}UyP{SkGsFG9$))mB6+UU$lW}$IPaCGhcuYRc0>Dm=7IS5{C^(+E7A}`j@@9!X)!zd*|zHZ@YuGhlN?l
MKiJ=aqNpxH0Ifnv#;Sr8{wz<ce5DXu|D=}8_k)G@rs|6arhkHMm{J6r4KI2Bi|C^+Mp@;pG1Z7S?5ZuUt1Ye%wJ3It^z|LJVM0b
WMNYumH|DK)R-Q4>62Ke)Ap#Uoe-PLg>qH~fhq}Lr8|wMC5oZzHruF9mG$t`o@HS?-
x76Roqp(zd67n{m1Yh}3H|)|)GzL5A)USBqRuo?!Zdme4f+Jj^Hz_z0RTl{e_4D#V0Nobg#aexBz*UBYdoYfrfe20CGJxSRtJe=4
>Q0zmekVa!7w3%Gi$TUKVJwaJxgr#Iz+Pu9%QMVYcPt;C)afRP?C<P4Rd-_bvcf>C)ZPI&Mm<!g%i?<oaI#)c<ys`+-
LTS=91C@2Cr^a(n>#W|M1H~SL6RiDojNJ2sqcKfKmAk_OHu+8a$LJS@14G{iK9LhR5$)_2BNxBQWHN~IRUQg^P1?B&fsBCsz8!d*
K$}(KpXN~ep%et+Vjl`!ZX(nYW9x05oTIgryDkH`g2|3c!I9y;Mo>sImDwQ9H+8OOhez}1$Fw}SwHNVZ}2?};cLWq9``;D)eLqw3
CZ4%`n9Sh)>~-
0=79ax03*$kzkx2o5%%7w%VZG*I4pX#{lkv*|1i0}cRb($tM;%`5$%6|a}*TFkbwoA1JSAMlEO5!*bE#b+QH?PUFscJZK?e`bmGl
8I!Y1JA=iF-07a@%d{@+!-%wi*X(dqL#EeAaD{MJM<6ll_`*_o@QN%(ZU&>B+5amK)x-
ULfg@CmWy_%@?p5f!evl=@M)dd<6nj!7W4tInM7$kL0zqx9r-
;h9SZ#dPXCu$1nlJAF}YzCtDOa`9#@J!m`o4v}8Z&fcVvoTO}8uAZrrcz-RG5t_soZZRV4=+^GWn{kde0p|uefmnnJvn{<{zdQo@
Dxg4!Vh6YFZpilujg-H^@csCT@#~(M<Dy2FIq0*WeC<V96F9Y%<oXD+r6waG)!5TLZNktd_s7aGEx86#>mRuh;}@q^@Ofr6K-
v5zp3l{h?v4^%$4T<0aJ~rQJ)UdLD^r#o@>VgbV)?lJ5!k(mj~Cab%+DuvHsm_*E$-
ai`#_$ySJJ1qx6*<&8%(x8plv@o0utGomCb#$0>D$)y=PXmp5+J#qRx!(qtMG#*@QWzN>o{n?@3a6AeHKCC?&{5VQi2#$3F;d~x;
SLvQ%(^v&h)?VBDg*0M6Z@14E4c>k8Jg}?5R01husFRQo05olb!c>4zR7cY8ey<cBk_J;4SPoGlpSyh*+x5^a~0V;qhJ1RjdG*nt
BkD^z8k^TKOYvJ(OH4tls__cTXa(H_E^u^T<-a|^UgN(-J_&ch;r)i+X(Dj-
_vc;D}Kk%vM^y+k<2LH~@_+m=mH(2_L{->hLpZ@$m{{v9FBwz
"""
ROOT=Path(__file__).resolve().parent
BUNDLE_PIN=[25348, '2cab48105ada679e873e439fdd10ff70ca1cdca1ed4c0a4d3cb2b4b84b61beef']
SOURCE_PINS={'ridge_ray.py': [15653, '73b5fd7be22e7ce5f44d776b296695dd37b36efc59b62a20fafea7923d601eca'], 'numeric_probe.py': [9273, '7b7f85e814d1cc648912adbe3c242a94851fb0b73c53b5bb8d9d09de39f96c59']}

OUTPUT_PINS={
 'ridge_ray.json':[1206540,'d8133e6253707ae259cf975340a19a0464bffdcc48e5abe6ee3afa16309cb3cf'],
 'numeric_checkpoints.json':[4695,'a860f2898cb2ff35731dd6d5c4330a14b8cdd209d2e772411a8c94aba011bf1c']}
def check(b,pin):
 assert len(b)==pin[0] and hashlib.sha256(b).hexdigest()==pin[1]
b=zlib.decompress(base64.b85decode(''.join(DATA.split())))
check(b,BUNDLE_PIN)
for name,text in json.loads(b).items():
 b=text.encode();check(b,SOURCE_PINS[name]);p=ROOT/name
 if p.exists():assert p.read_bytes()==b
 else:p.write_bytes(b)
assert len(sys.argv)==2 and sys.argv[1] in ('sources','build','check','numeric')
mode=sys.argv[1]
if mode=='sources':
 for name,pin in SOURCE_PINS.items():print(name,*pin)
 print('TWO_APEX_RIDGE_RIM_FULL_SOURCES_PASS')
else:
 if mode=='numeric':
  cmd=[sys.executable,'numeric_probe.py','audit'];name='numeric_checkpoints.json'
 else:
  cmd=[sys.executable,'-S','ridge_ray.py',mode];name='ridge_ray.json'
 subprocess.run(cmd,cwd=ROOT,check=True)
 check((ROOT/name).read_bytes(),OUTPUT_PINS[name])
 print('TWO_APEX_RIDGE_RIM_SELF_CONTAINED_RECOVERY_PASS')
```

## 10. Точный непокрытый остаток и наиболее полезное продолжение

Для потенциального строгого 110 без дополнительных слабых точек, у которого именно B является единственной строгой S, новые необходимые условия в chart (4.1) имеют вид

    beta in relint(B),
    0<y<L,
    min_{0<=t<=1}[U(t)+yK(t)]>rho²,
    Phi>rho².

Первое — настоящая устойчивость B. Второе использует исходный закрытый cap с его честной EF-границей; третье — новый строгий гребневой барьер. Они оставляют конкретный промежуточный геометрический диапазон, а не утверждают его существование. Четыре луча, не прошедшие Phi-test, показывают лишь неполноту простого теста: все четыре здесь отдельно исключены полным height-audit, но произвольные другие формы с Phi>rho² не исключены.

Когда B не является строго устойчивой, полный all-height сектор выше неприменим. Корни U в B в этом остатке, другие стабильные грани, более общие G,v, достаточно сдвинутые или асимметричные основания остаются открыты. Общую лемму раздела 3 можно применять к иной предполагаемой стабильной грани с её собственным настоящим краем и настоящими внешними рёбрами; автоматического полного покрытия таких корней здесь не доказано. Для внешнего единственного U дополнительно сохраняются старые radius/reflection и actual-fan условия, но они не подменяются новыми 14 лучами.

Продолжение, нацеленное на оставшийся класс, должно искать в указанном строгом промежуточном диапазоне либо совместимость настоящих положительных fan с единственным U, либо действительное тело. Exact height-pencil уже устраняет необходимость сетки по одному неограниченному метрическому параметру; менять нужно саму геометрию и горизонтально-сдвиговый профиль, каждый раз заново интегрируя проективно изменённый uniform COM. Пирамидальное существование базового U нельзя использовать как недоказанное сокращение — для него теперь имеются три точных отрицательных контроля.

Ни C_min>=36, ни V>=11/F>=10, ни новая верхняя конструкция не заявлены. Принятый интервал **34<=C_min<=622** и исторические FULL/LOCAL численности не меняются. Нижний и верхний результаты унаследованы; C622 заново здесь не аудировался.

Дополнительные удобные копии, не заменяющие буквальную капсулу: recovery-wrapper (`recover_ridge_ray.py`), полный exact source (`ridge_ray.py`), полный exact отчёт (`ridge_ray.json`), численный source и checkpoints (`numeric_probe.py`).
