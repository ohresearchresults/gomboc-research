# minimum-0092

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# TWO_APEX_BISECTOR_REFLECTION_AND_BASE_ROOT_CAP_V1

**Ветка:** [internal-source-reference]; slot-3, Steady Lynx 90.

## 1. Результат и область утверждений

Получены две независимые геометрические отсечки, не требующие полной локальной dual-цепи, выбранной complementary-пары или ограничения глубины деревьев.

**Первая отсечка** исключает единственный неустойчивый корень вне восьмиугольной базы для целого количественно заданного класса почти центрально-симметричных баз. Она действует при степенях апексов 3/7, 4/6 и 5/5, допускает произвольные разрывы и слияния локальных dual-стрелок и любой выход B. В частности, полностью исключены внешние единственные U-корни во всех аффинных образах равновысоких крыш с центрально-симметричной базой и осью, соединяющей её центр с серединой верхнего отрезка. Метрика при этом произвольная, а не инвариантная относительно симметрии.

**Вторая отсечка** исключает строгий 110 во всём классе тел, у которых B строго устойчива, а оба апекса лежат в явно заданном замкнутом параболическом диапазоне. Она охватывает также корень U в базе. Строгая внутренняя часть диапазона даёт S_nd >= 2; на границе доказана точная альтернатива: дополнительная строгая S либо настоящий слабый EF-packet. Это не запрет всех слабых complementary-пар на граничной страте.

Дополнительно получена полная проективная нормальная форма двухапексного E17 с одним параметром неравенства высот и формула настоящего объёмного центроида равновысокой крыши через два настоящих центра базовой геометрии.

Построены и точно проверены **семь настоящих однородных тел E17**, в том числе три тела S=2,U=2,H=2 с парами степеней апексов 3/7, 4/6, 5/5. Это не 110-кандидаты в смысле уже выполненных условий: они имеют шесть строгих положений покоя. Сохранены как небольшие точные исходные тела для продолжения. У последнего тело имеет сходящийся и разорванный локальный dual-лес и выходы B не в начало старой полной цепи.

**Весь восьмиугольный слой не исключён. Нового 110 нет. Границы остаются 34 <= C_min <= 622.** Семь контролей не являются census и не переименовываются в FULL/LOCAL.

## 2. Входная власть источников и ограничения целостности

Использован полностью прочитанный предоставленный журнал, оба буквальных parent и все девять exact-материалов, включая обе обязательные поправки. Журнал: 245911 bytes, SHA-256 `f1b53e6d7a92adca362faa0cda14cba118942b7832753576a3d28005bb32d629`. Старый ROOF8_3_5 из 512 имеет степени 4/6; новый balanced — 5/5. Их объекты и каталоги не отождествлялись.

Радиусная лемма ниже заимствована из полного 546-proof, а не объявляется новой; её короткое доказательство воспроизведено, чтобы новые результаты не зависели от недоступного архива. :contentReference[oaicite:0]{index=0}

Поправка covariance принята именно в усреднённом виде: при настоящих объёмных весах E_cells s=-b,

    20 E_P(e.X)^2 >= E_cells[2b^2+2bs+(4/3)s^2]
                   = (4/3)E_cells s^2 >= (4/3)b^2.

Промежуточный член 2b(b+s) не объявляется положительным по отдельным тетраэдрам. Новые отсечки ниже вообще не используют общий порог 29160/59. :contentReference[oaicite:1]{index=1} Арифметическая поправка также сохранена: `1952*819-122*9459=444690`, не 444210; область selected-chain не расширяется до arbitrary available arrows. :contentReference[oaicite:2]{index=2}

**Проверка parent-хешей имеет одно конкретное ограничение.** Для `minimum-0086` воспроизводится заявленный `8123315ee22b6a0fc370e8f672f299bc19997f89ad023530404946c77f994f10`: компактный UTF-8 JSON `{"version":2,"result_markdown":BODY}`, BODY с завершающим LF, имеет 52537 bytes. Для `minimum-0087` журнал заявляет `b77264d597b32a5f97ac011c57d4c95e7581fb2d81d202e2bc477b0e6fc867f5`, но аналогичное хеширование видимого блока этого значения не воспроизводит. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4} Его видимый Markdown от `# H0_GLOBAL_NERVE129_AND_WEAK_PACKETS_V1` до EOF имеет 64050 bytes и SHA `2cf20edd91eacafac01d2fab97bb4616d9e2bcc5fbcecbb06eabeca07ba3cd54`; компактная v2-обёртка — 64600 bytes, SHA `63cd502e57cbaaf4844c99a8cdc4244c19e2f68affa626fd80ba7f89aa4453ec`. Добавление завершающего LF даёт другой, также несовпадающий хеш. Это не установленное математическое противоречие: не установлено точное хешируемое представление второго parent. Невидимую обёртку не реконструирую догадкой. Новые доказательства и все семь тел ниже самодостаточны и от этой обёртки не зависят.

## 3. Обозначения и настоящая радиусная лемма

P — однородный выпуклый трёхмерный многогранник с собственным COM в 0. Его настоящая грань B содержит все вершины, кроме x,z. Пишем q_B(v)=1 на B, q_B(v)<1 на остальных вершинах. Primal-метрика M положительно определена; dual-метрика всегда N=M^{-1}. Норма точки обозначается |v|_M, норма полюса — |q|_N. Все утверждения можно доказывать после единственного физического whitening M=I.

Пусть x — единственная строго неустойчивая вершина. Нормируем |x|=1. Каждый другой истинный vertex имеет слабый выход по истинному ребру, а такой выход строго увеличивает норму, даже когда примитив равен нулю. Поэтому все остальные нормы меньше 1.

Положим r=max_{b in vertices(B)}|b|, sigma=|z|. Тогда

    r > sigma;    b.(x-b) >= 0 для каждого максимального b.       (R)

Для полноты докажем используемую часть. Для настоящего площадного центра g_B и единичного e:

    3e.g_B >= max_B e.b + 2min_B e.b.

Это следует из положительной площадной смеси треугольников с общей вершиной, максимизирующей e.b. Предположим r<=sigma. Тогда z не выходит в B, следовательно z->x и x.z>=sigma^2. Максимальная базовая вершина b выходит либо в x, либо в z.

В первом случае берём e=x. Центр конуса conv(B,x) имеет e-проекцию не меньше (1-r)^2/4>0. Каждый оставшийся ненулевой тетраэдр x,z,b_i,b_j имеет проекцию центра не меньше (1+sigma^2-2r)/4>0. Во втором случае b->z, поэтому r<sigma; с e=z/sigma соответствующие нижние оценки равны (sigma-r)^2/(4sigma)>0 и (sigma-r)/2>0. Настоящая положительная объёмная смесь не может иметь центр 0. Следовательно r>sigma. Теперь у максимального b невозможен выход в другую базовую вершину или в z; остаётся истинное ребро b->x.

Отдельно настоящий apex-fan даёт, без предположения U=1, при p=q_B(x), t=q_B(z) и lambda=Vol(conv(B,x))/Vol(P):

    0=lambda(p+3)+(1-lambda)(p+t+2),
    -(p+t)-2=lambda(1-t)>0.                                  (V)

Здесь 0<lambda<1; нулевые тетраэдры, если они встречаются в выбранном разбиении плоских граней, не получают положительного веса. Формула использует настоящие объёмы, не completion.

## 4. Теорема бисектора и количественной асимметрии базы

Положим

    s=x+z,
    beta=-1/q_B(s)>0,
    c_*=-beta s=s/q_B(s) in aff(B).

Точка c_* — каноническое пересечение базовой плоскости с лучом, противоположным середине двух апексов. Это не свободно выбираемый центр базы.

### 4.1. Необходимая положительная сторона бисектора

Из (R) для каждого максимального b следует

    b.s >= r^2-r*sigma = r(r-sigma)>0.                         (B1)

Поэтому весь класс `max_{b in B} <b,x+z>_M <= 0` исключён для единственного внешнего U-корня, без каких-либо dual-предпосылок.

В физических координатах с B на высоте -h, COM в 0, высотами апексов H_x,H_z над B и горизонтальным смещением d их середины относительно проекции COM, это даёт необходимое условие

    2 R_B |d| > h(H_x+H_z-2h),                               (B2)

где R_B — максимальное горизонтальное расстояние базовой вершины от проекции COM. Более точный тест использует support-function B вместо оценки R_B|d|. В частности, если середина апексов находится точно над проекцией COM, единственный U-корень не может быть апексом. Условие со строгим обратным запасом в (B2) задаёт открытый непрерывный класс, а не только симметричную подмногообразную семью.

### 4.2. Отражённая база обязана заметно выйти за радиус r

Для того же максимального b имеем

    |2c_*-b|_M^2
      = r^2+4|c_*|_M^2+4 beta <b,s>_M
      >= r^2+4|c_*|_M^2+4 beta r(r-sigma)
      > r^2+4|c_*|_M^2.                                    (B3)

Обозначим через epsilon настоящий Hausdorff-distance, в метрике M, между двумя плоскими выпуклыми телами B и 2c_*-B. Если

    epsilon <= sqrt(r^2+4|c_*|_M^2)-r,                      (B4)

то единственный U-корень вне B невозможен.

Доказательство полного охвата (B4): отражённая точка 2c_*-b находится не далее epsilon от некоторой точки B. Поэтому её норма не больше r+epsilon, что противоречит (B3). Это покрывает обе возможности внешнего корня; c_*, r и epsilon не зависят от того, какой апекс назван x.

Для точной рациональной проверки достаточно положить E=epsilon^2, C=4|c_*|_M^2 и проверить

    C>=E,    (C-E)^2 >= 4r^2 E.                             (B4-exact)

Расстояние до выпуклого многоугольника вычисляется точно: для внешней точки минимум по замкнутым рёбрам, для внутренней — 0; максимум distance-функции по выпуклому многоугольнику достигается на вершинах. Код ниже выполняет именно эту проверку, а не заменяет Hausdorff-distance расстоянием между несопоставленными вершинами.

**Центральная база.** Если B=2c_*-B, то epsilon=0 и внешний единственный U исключён для всякой M. В равновысокой крыше с центрально-симметричной базой и верхним отрезком, центр которого находится на оси её симметрии, настоящая объёмная симметрия помещает COM на эту ось. Поэтому геометрический центр базы действительно равен c_*. Последующее произвольное невырожденное аффинное преобразование сохраняет это равенство и настоящий COM. Это не довод «симметрия переставляет равновесия»: после аффинного shear евклидова метрика обычно не сохраняет исходную симметрию.

**Точный остаток этой теоремы:** она не исключает единственный U-корень в B. Для внешнего корня остаются только базы, нарушающие (B4), причём (B1) и усиленный зазор (B3) обязательны.

## 5. Теорема для устойчивой базы: реальный overhang и слабая граница

Положим k^2=q_B^T N q_B. Для a=x,z определим

    p_a=q_B(a),
    Delta_a=(2-p_a)^2-k^2 |a|_M^2.                          (P1)

Предположим, что B строго устойчива и Delta_x,Delta_z>=0.

**Тогда строгий 110 с ровно двумя положениями покоя невозможен.** Если обе Delta положительны, имеем S_nd>=2. При нестрогих неравенствах имеем S_nd>=2 либо дополнительный настоящий слабый EF-packet.

Доказательство. После физического whitening рассмотрим dual-диаметральный шар

    D_B={q: |q-q_B/2| <= |q_B|/2}.

Слабое q->B эквивалентно q in D_B. Максимум a.q на этом шаре равен

    (p_a+k|a|)/2 <= 1

в силу (P1) и p_a<1. Каждый настоящий боковой полюс q инцидентен хотя бы одному из двух апексов, то есть a.q=1. Поэтому при строгом Delta_a такой полюс вообще не может иметь слабый выход в B; при Delta_a=0 возможна только граница q.q_B=q.q.

Выберем боковой полюс q максимальной нормы среди всех восьми боковых полюсов. Для любого другого бокового полюса r строго q.r<q.q: равенство в Cauchy при |r|<=|q| потребовало бы r=q. Если q.q_B<q.q, q даёт вторую строгую устойчивую грань P.

Если q.q_B=q.q, точка f=q/(q.q) принадлежит B и грани q, а все прочие фасетные неравенства в f строги. Значит f лежит в относительной внутренности настоящего базового ребра B intersect q. Оба primal-примитива этого ребра строго отрицательны. Dual-примитив со стороны q равен 0, со стороны B строго отрицателен, поскольку |q_B|^2>|q|^2. Получен настоящий EF-packet со знаками `(-,-,0,-)`, а не безвредный нуль при положительном примитиве. Именно этот дополнительный resting packet не допускает строгую приёмку 110.

Это доказательство не запрещает на границе систему S_nd=U_nd=1,H_nd=0 **с дополнительным слабым покоем**. Подмена этого различия дала бы ложное расширение результата.

### Физический смысл и непустота класса

Пусть h=1/k — расстояние COM до B, H_a=(1-p_a)/k — настоящая высота апекса над B, u_a — его горизонтальное смещение относительно проекции COM на B. Тогда

    Delta_a>=0  iff  |u_a|^2 <= 4 h H_a.                    (P2)

Таким образом, это параболический диапазон, а не запрет любого overhang. Первые четыре точных тела ниже имеют **оба ортогональных апексных проецирования вне B**, но B строго устойчива и обе Delta строго положительны. Одно из этих тел имеет неравные высоты апексов и степени 3/7. Строгие запасы сохраняются при достаточно малых непрерывных изменениях настоящей геометрии с тем же комплексом.

Другая, неравносильная достаточная геометрическая отсечка: если ортогональная проекция всего P на плоскость B равна B, то S_nd>=2. Действительно, проекция настоящего COM лежит внутри B, а все прочие наружные нормали имеют неотрицательную вертикальную компоненту. Максимальный по норме боковой полюс строго убывает к любому другому боковому полюсу и к q_B, направленному вниз. Здесь вообще не требуется (P2).

## 6. Полная нормальная форма и настоящий центроид равновысокой крыши

Эта редукция охватывает геометрию всего рассматриваемого слоя, но сама по себе не является его исключением.

После обмена апексов и аффинного выбора координат всякая настоящая двухапексная E17-крыша представляется как

    P = affine_image(T_alpha(K)),
    T_alpha(u,v,w)=(u,v,w)/(1+alpha*u),
    K=conv(B_0,(-1,0,1),(1,0,1)),                           (NF)

где -1<alpha<1, все десять знаменателей положительны, B_0 — настоящий выпуклый восьмиугольник в w=0 с двумя горизонтальными опорными рёбрами и двумя строго выпуклыми боковыми цепями. Треугольные блоки имеют размеры m и 6-m; можно брать m=1,2,3. Степени апексов m+2 и 8-m.

**Почему это полный охват.** При равных высотах обе четырёхугольные грани уже требуют параллельности соответствующих базовых рёбер и верхнего отрезка. При неравных высотах прямая xz пересекает базовую плоскость в L вне B: иначе меньший по высоте апекс не был бы вершиной. Возьмём положительную на B аффинную функцию d_0, обращающуюся в 0 в L. Продолжим её в пространство с подходящим коэффициентом высоты. Проективное деление на d делает высоты x,z равными, сохраняет выпуклость и все инцидентности и отправляет L на бесконечность; два базовых опорных ребра становятся параллельными.

Можно выбрать аффинные координаты до деления так, чтобы alpha=(H_x-H_z)/(H_x+H_z), координаты апексов были `(-1/(1-alpha),0,1/(1-alpha))` и `(1/(1+alpha),0,1/(1+alpha))`, а d=1-alpha*u. На базе это достигается выбором u=(1-d_0)/alpha; продолжение по высоте согласовано на обоих апексах, поскольку L лежит на их прямой. Обратное преобразование — ровно T_alpha из (NF). При alpha=0 используется аффинный случай. Это также доказывает положительность знаменателей на всём теле, а не только формально на двух апексах.

Код ниже выбирает конкретные B_0 для семи контролей; эти параболические цепи **не объявляются параметризацией всех** B_0. Полная нормальная форма разрешает произвольные базовые цепи указанного типа.

### Точная формула центроида при равных высотах

Пусть B лежит в высоте 0, верхний отрезок имеет высоту H, центр 0 в горизонтальных координатах и полудлину a вдоль u. Пусть A — настоящая площадь B, w — его ширина поперёк отрезка. Сечения B горизонтальными линиями имеют концы u_-(v),u_+(v). Определим настоящий смешанный центр

    g_mix = ( (1/(2w))*integral[u_-(v)+u_+(v)]dv,
              (v_min+v_max)/2 ).

Это среднее середин настоящих хорд с равномерной мерой dv, не свободная строка completion. Для многоугольника интеграл — конечная сумма трапеций. При g_B, настоящем площадном центре B,

    Vol(P)=H(A+a*w)/3,
    COM_vertical=H(A+2a*w)/(4(A+a*w)),
    COM_horizontal=(3A*g_B+2a*w*g_mix)/(4(A+a*w)).            (CM)

Доказательство: сечение на доле высоты t равно `(1-t)B+t[-a,a]`; его площадь `A(1-t)^2+2a*w*t(1-t)`, а горизонтальный первый момент `(1-t)^3 A*g_B+2a*w*t(1-t)^2*g_mix`. Интегрирование даёт (CM). В частности, H/4<COM_vertical<H/2; ошибочная более сильная граница H/3 здесь не используется.

При alpha!=0 центроид не переносится проективно! В recovery он заново вычисляется по настоящему телу T_alpha(K): для ориентированных граничных треугольников a,b,c суммируются det(a,b,c)/6 и det(a,b,c)(a+b+c)/24. После единственного вычитания полученного COM применяются аффинная карта A и взаимно обратные M=A^T A, N=A^{-1}A^{-T}.

## 7. Точные действительные тела и место разрыва старой геометрии

Семь восстановимых записей имеют следующие результаты. Везде V=10,E=17,F=9; единственная максимальная восьмиугольная грань — F0; остальные грани — две четырёхугольные и шесть треугольных. Все COM настоящие объёмные.

| Запись | Степени апексов | alpha | S,U,H | B строго устойчива |
|---|---:|---:|---:|---|
| D3_D7_OVERHANG | 3,7 | 0 | 5,6,9 | да |
| D4_D6_OVERHANG | 4,6 | 0 | 7,8,13 | да |
| D5_D5_OVERHANG | 5,5 | 0 | 5,6,9 | да |
| D3_D7_UNEQUAL_HEIGHT_OVERHANG | 3,7 | 1/4 | 5,6,9 | да |
| D3_D7_AFFINE_SHEAR | 3,7 | 0 | 2,2,2 | нет |
| D4_D6_AFFINE_SHEAR | 4,6 | 0 | 2,2,2 | нет |
| D5_D5_AFFINE_SHEAR | 5,5 | 0 | 2,2,2 | нет |

Оба апекса во всех семи телах реально выступают за ортогональную проекцию B. Во всех семи проверено (B4-exact). В последних трёх единственные строгие U — базовая вершина 0 и апекс 9; степени последнего соответственно 7,6,5. Никаких слабых resting packets в этих телах нет. В последних трёх нет вообще нулевых примитивов.

### Полностью буквальное целочисленное тело S2,U2,H2

Последняя запись, умноженная на 3204, имеет вершины в порядке 0,...,9:

    (-5949,-5778,-1287)
    (-6305,-3642,-1287)
    (-6305,-1506,-1287)
    (-5949,  630,-1287)
    (-4347,  630,-1287)
    (-3991,-1506,-1287)
    (-3991,-3642,-1287)
    (-4347,-5778,-1287)
    ( 4464, 3834, 1917)
    (10872, 3834, 1917)

Евклидова метрика I; собственный COM=(0,0,0); объём `36139530816`. Настоящие наружные циклы граней:

    F0=(0,1,2,3,4,5,6,7)
    F1=(0,8,1)
    F2=(1,8,2)
    F3=(2,8,3)
    F4=(3,8,9,4)
    F5=(4,9,5)
    F6=(5,9,6)
    F7=(6,9,7)
    F8=(7,9,8,0)

Строгие S: F1,F5. Строгие U: 0,9. Строгие H: рёбра (3,8),(7,9). Эти данные относятся к одному телу; координаты, полюса, рёбра и массы не склеены из разных контролей.

В цикле полюсов апекса 9, `(F4,F5,F6,F7,F8)`, точные положительные локальные стрелки образуют

    F4 -> F5 <- F6 <- F7,     F8 изолирован.

На обеих парах F7--F8 и F8--F4 оба dual-примитива строго отрицательны. Выходы B в этот цикл имеются ровно в F5,F6,F7. Поэтому available-лес действительно сходится и разрывается, а выход B не задаёт прежнюю полную начальную цепь. Здесь нельзя подставить growth16/growth64 как для однонаправленного полного обхода. Отражательная теорема вместо этого объясняет неизбежность дополнительного U при попытке сохранить эту центральную базу и сделать 9 единственным корнем. Пример не объявляется слабой complementary-парой: U=2, а H=2.

## 8. Recovery capsule

Ни один исходный файл из старого архива не нужен для восстановления новых тел. Входы буквально находятся в `base`, `native` и `specs` следующего исходника. Зависимости: **CPython 3.13.5, только standard library**; assert должны быть включены. Никаких NumPy, SciPy, SDP, сетевых загрузок или неявных checkpoints нет.

Сохранить следующий блок с LF и завершающим LF как `roof_geometry_capsule.py` и выполнить:

    python -S roof_geometry_capsule.py build
    python -S roof_geometry_capsule.py check
    sha256sum roof_geometry_capsule.py roof_bisector_overhang.json

Оба запуска фактически выполнены. Ожидаемые последние маркеры:

    SEVEN_ACTUAL_OWN_COM_E17_ROOFS_AND_RECIPROCAL_METRICS_PASS
    roof_bisector_overhang.json 35355 0789d2f901517ceb1723c7686d26c065fd2f91c3144ac21dc12f31e3455c094a
    ROOF_BISECTOR_OVERHANG_RECOVERY_PASS

Исходник: **9167 bytes**, SHA-256 `6c29261c6c95308a6e7f5000df944ea1d010bc9ad4294c4bee8ac3b66e9a5936`. JSON: **35355 bytes**, SHA-256 `0789d2f901517ceb1723c7686d26c065fd2f91c3144ac21dc12f31e3455c094a`.

Проверяются все опорные тройки и максимальные грани, строгая выпуклость каждого фасетного цикла, оба ориентированных использования каждого настоящего ребра, степени, COM до и после аффинной карты, M*N=I, совпадение обеих механик, все четыре примитива каждого ребра, положительные cap-запасы первых четырёх тел, настоящий Hausdorff-тест всех семи и указанный разорванный лес последнего тела.

```python
"""ROOF_BISECTOR_OVERHANG_V1. CPython 3.13.5; standard library; assertions on.
Actual homogeneous bodies, not 110 examples. No parent data files required.
Run: python -S roof_geometry_capsule.py build|check
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json,sys
assert __debug__
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def mul(t,a):return tuple(t*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def mv(A,v):return tuple(dot(row,v) for row in A)
def tr(A):return tuple(zip(*A))
def mm(A,B):return tuple(tuple(dot(a,b) for b in tr(B)) for a in A)
ID=tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
def inv(A):
 d=det(*A);assert d
 return tuple(tuple(v/d for v in row) for row in tr((cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))))
def edge(a,b):return tuple(sorted((a,b)))
def native(m):
 assert m in (1,2,3)
 faces=[tuple(range(8))]
 faces += [(i,8,i+1) for i in range(m)]
 faces += [(m,8,9,m+1)]
 faces += [(i,9,i+1) for i in range(m+1,7)]
 faces += [(7,9,8,0)]
 assert len(faces)==9
 return faces

def base(m,w=F(1,4),s=F(1,8)):
 L=[(-w-s*(1-y*y),y,F(0)) for y in (F(-1)+F(2*j,m) for j in range(m+1))]
 R=[( w+s*(1-y*y),y,F(0)) for y in (F(1)-F(2*j,6-m) for j in range(7-m))]
 return L+R

def moment(V,faces):
 total=F(0);mom=(F(0),)*3
 for f in faces:
  for j in range(1,len(f)-1):
   a,b,c=(V[i] for i in (f[0],f[j],f[j+1]))
   d=det(a,b,c);total+=d;mom=add(mom,mul(d,add(add(a,b),c)))
 assert total>0
 return total/6,mul(1/(4*total),mom)

def hausdorff2(P,Q,M,n):
 def dist2(p,C):
  if all(dot(cross(sub(b,a),sub(p,a)),n)>=0 for a,b in zip(C,C[1:]+C[:1])):return F(0)
  ans=[]
  for a,b in zip(C,C[1:]+C[:1]):
   e=sub(b,a);t=dot(e,mv(M,sub(p,a)))/dot(e,mv(M,e));t=max(F(0),min(F(1),t))
   d=sub(p,add(a,mul(t,e)));ans.append(dot(d,mv(M,d)))
  return min(ans)
 return max([dist2(p,Q) for p in P]+[dist2(q,P) for q in Q])

def audit(name,m,alpha,A):
 A=tuple(tuple(map(F,row)) for row in A);assert det(*A)>0
 W=base(m)+[(F(-1),F(0),F(1)),(F(1),F(0),F(1))]
 den=[1+alpha*v[0] for v in W];assert min(den)>0 and abs(alpha)<1
 V=[mul(1/d,v) for d,v in zip(den,W)];faces=native(m)
 vol,g=moment(V,faces);X=[sub(v,g) for v in V]
 normals=[];Q=[];arcs={}
 for f,cy in enumerate(faces):
  n=cross(sub(V[cy[1]],V[cy[0]]),sub(V[cy[2]],V[cy[0]]));assert any(n)
  for i,v in enumerate(V):
   val=dot(n,sub(v,V[cy[0]]));assert val==0 if i in cy else val<0
  for a,b in zip(cy,cy[1:]+cy[:1]):
   assert (a,b) not in arcs;arcs[a,b]=f
   assert all(dot(cross(sub(V[b],V[a]),sub(V[v],V[a])),n)>0 for v in cy if v not in (a,b))
  h=dot(n,X[cy[0]]);assert h>0;normals.append(n);Q.append(mul(1/h,n))
 # All supporting triples: no missing maximal facets, merged coplanar faces.
 hull=set()
 for i,j,k in combinations(range(10),3):
  n=cross(sub(V[j],V[i]),sub(V[k],V[i]))
  if not any(n):continue
  vals=[dot(n,sub(v,V[i])) for v in V]
  if min(vals)>=0 or max(vals)<=0:hull.add(tuple(t for t,z in enumerate(vals) if z==0))
 assert hull=={tuple(sorted(f)) for f in faces}
 edges=sorted({edge(a,b) for a,b in arcs});assert len(edges)==17
 dual=[(arcs[a,b],arcs[b,a]) for a,b in edges]
 assert len(arcs)==34 and 10-17+len(faces)==2
 deg=[sum(v in e for e in edges) for v in range(10)]
 assert deg==[3]*8+[m+2,8-m]
 assert sorted(map(len,faces))==[3]*6+[4,4,8]
 v0,g0=moment(X,faces);assert v0==vol and g0==(0,0,0)
 Ai=inv(A);M=mm(tr(A),A);N=mm(Ai,tr(Ai));assert mm(M,N)==ID
 Y=[mv(A,x) for x in X];R=[mv(tr(Ai),q) for q in Q]
 vp,gp=moment(Y,faces);assert vp==det(*A)*vol and gp==(0,0,0)
 G=[[dot(a,mv(M,b)) for b in X] for a in X]
 J=[[dot(a,mv(N,b)) for b in Q] for a in Q]
 assert G==[[dot(a,b) for b in Y] for a in Y]
 assert J==[[dot(a,b) for b in R] for a in R]
 assert all(dot(q,x)==1 if i in faces[f] else dot(q,x)<1 for f,q in enumerate(Q) for i,x in enumerate(X))
 U=[i for i in range(10) if all(G[i][j]<G[i][i] for j in range(10) if j!=i)]
 S=[i for i in range(9) if all(J[i][j]<J[i][i] for j in range(9) if j!=i)]
 Z=[];H=[];weak=[];harmless=[]
 for eid,((a,b),(f,k)) in enumerate(zip(edges,dual)):
  z=(G[a][b]-G[a][a],G[a][b]-G[b][b],J[f][k]-J[f][f],J[f][k]-J[k][k]);Z.append(z)
  assert z[0]+z[1]<0 and z[2]+z[3]<0
  if max(z)<0:H.append(eid)
  elif max(z)==0:weak.append(eid)
  elif any(t==0 for t in z):harmless.append(eid)
 assert len(S)+len(U)-len(H)==2
 k2=J[0][0];p=[dot(Q[0],X[i]) for i in (8,9)]
 cap=[(2-p[j])**2-k2*G[i][i] for j,i in enumerate((8,9))]
 foot=mul(1/k2,mv(N,Q[0]));Bstable=all(dot(Q[f],foot)<1 for f in range(1,9))
 assert Bstable==(0 in S)
 proj=[add(X[i],mul((1-p[j])/k2,mv(N,Q[0]))) for j,i in enumerate((8,9))]
 over=[any(dot(q,a)>1 for q in Q[1:]) for a in proj]
 if Bstable and min(cap)>0:
  assert all(J[f][0]-J[f][f]<0 for f in range(1,9))
  assert len(S)>=2
 svec=add(X[8],X[9]);pairing=[dot(x,mv(M,svec)) for x in X[:8]]
 r2=max(G[i][i] for i in range(8));bb=[i for i in range(8) if G[i][i]==r2]
 pb=dot(Q[0],svec);assert pb < -2
 center=mul(1/pb,svec)
 reflected=[sub(mul(2,center),x) for x in X[:8]]
 iscentral=all(v in X[:8] for v in reflected)
 hd2=hausdorff2(X[:8],reflected,M,Q[0]);C=4*dot(center,mv(M,center))
 near=(C>=hd2 and (C-hd2)**2>=4*r2*hd2)
 if near:assert not(len(U)==1 and U[0] in (8,9))
 if iscentral:
  assert all(dot(X[b],mv(M,center))>=dot(center,mv(M,center)) for b in bb)
  assert not(len(U)==1 and U[0] in (8,9))
 return dict(name=name,m=m,alpha=alpha,parallel_vertices=W,perspective_denominators=den,
  affine_map=A,M=M,N=N,raw_vertices=V,raw_volume=vol,raw_centroid=g,
  physical_vertices=Y,physical_volume=vp,physical_centroid=gp,
  faces=faces,edges=edges,dual_pairs=dual,vertex_degrees=deg,poles_raw=Q,
  physical_poles=R,raw_slopes=Z,S=S,U=U,H=H,weak_edge_ids=weak,harmless_zero_edge_ids=harmless,
  base_stable=Bstable,cap_margins=cap,apex_projections_overhang=over,
  bisector_products=pairing,canonical_base_center=center,centrally_reflected_base=iscentral,
  hausdorff_squared=hd2,reflection_C=C,reflection_exclusion=near,
  base_maximum_radius_squared=r2,base_maximizers=bb,S_U_H=[len(S),len(U),len(H)])

def serial(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [serial(v) for v in x]
 return x

def build():
 specs=[('D3_D7_OVERHANG',1,F(0),ID),('D4_D6_OVERHANG',2,F(0),ID),
        ('D5_D5_OVERHANG',3,F(0),ID),('D3_D7_UNEQUAL_HEIGHT_OVERHANG',1,F(1,4),ID),
        ('D3_D7_AFFINE_SHEAR',1,F(0),((1,0,4),(0,1,3),(0,0,1))),
        ('D4_D6_AFFINE_SHEAR',2,F(0),((1,0,4),(0,1,2),(0,0,1))),
        ('D5_D5_AFFINE_SHEAR',3,F(0),((1,0,4),(0,1,2),(0,0,1)))]
 reports=[audit(*sp) for sp in specs]
 assert all(r['reflection_exclusion'] for r in reports)
 for r in reports[4:]:
  assert r['S_U_H']==[2,2,2] and r['U']==[0,9]
  assert not r['weak_edge_ids'] and not r['harmless_zero_edge_ids']
 for r in reports[:4]:
  assert r['base_stable'] and min(r['cap_margins'])>0 and all(r['apex_projections_overhang'])
  assert set((8,9))<=set(r['U'])
  assert not r['weak_edge_ids']
 assert reports[-1]['centrally_reflected_base'] and not reports[-1]['base_stable']
 r=reports[-1]
 assert r['S']==[1,5] and r['U']==[0,9] and r['H']==[8,15]
 assert not r['weak_edge_ids'] and not r['harmless_zero_edge_ids']
 integer_vertices=[[-5949,-5778,-1287],[-6305,-3642,-1287],[-6305,-1506,-1287],
  [-5949,630,-1287],[-4347,630,-1287],[-3991,-1506,-1287],[-3991,-3642,-1287],
  [-4347,-5778,-1287],[4464,3834,1917],[10872,3834,1917]]
 assert [list(mul(3204,v)) for v in r['physical_vertices']]==integer_vertices
 vi,gi=moment(integer_vertices,r['faces']);assert gi==(0,0,0) and vi==3204**3*r['physical_volume']
 r['integer_representative_vertices']=integer_vertices;r['integer_representative_volume']=vi
 local=[(4,5),(6,5),(7,6)]
 q=r['physical_poles']
 assert all(dot(q[a],sub(q[b],q[a]))>0 for a,b in local)
 assert all(dot(q[a],sub(q[b],q[a]))<0 for a,b in [(7,8),(8,7),(8,4),(4,8)])
 assert [f for f in (4,5,6,7,8) if dot(q[0],sub(q[f],q[0]))>=0]==[5,6,7]
 r['root9_local_dual_forest']=local;r['base_exits_in_root9_cycle']=[5,6,7]
 for r in reports:assert r['S_U_H']!=[1,1,0]
 data=dict(identity='ROOF_BISECTOR_OVERHANG_V1',not_a_110_attainer=True,
           C_lower=34,C_upper=622,reports=reports)
 return reports,(json.dumps(serial(data),sort_keys=True,separators=(',',':'))+'\n').encode()

if __name__=='__main__':
 if sys.argv[1:] not in (['build'],['check']):raise SystemExit('usage: python -S roof_geometry_capsule.py build|check')
 reports,data=build();p=Path('roof_bisector_overhang.json')
 if sys.argv[1]=='build':p.write_bytes(data)
 else:assert p.read_bytes()==data
 for r in reports:
  print(r['name'],r['S_U_H'],'DEGREES',r['vertex_degrees'][8:],
        'CAP',*[str(x) for x in r['cap_margins']],'OVERHANG',r['apex_projections_overhang'])
 print('SEVEN_ACTUAL_OWN_COM_E17_ROOFS_AND_RECIPROCAL_METRICS_PASS')
 print(p.name,len(data),hashlib.sha256(data).hexdigest())
 print('ROOF_BISECTOR_OVERHANG_RECOVERY_PASS')
```

Удобные дополнительные копии: [исходник](sandbox:/mnt/data/research_work/roof_geometry_capsule.py), [полный точный отчёт](sandbox:/mnt/data/research_work/roof_bisector_overhang.json). Буквальный исходник выше достаточен без этих ссылок.

### Воспроизводимость отмеченной проверки parent-контейнера

Следующий отдельный минимальный probe использует только именно предоставленный журнал; отсутствие совпадения для второго parent не превращается в выдуманный новый parent.

```python
from pathlib import Path
import hashlib,json
p=Path('research-journal(20260919-050836).md')
s=p.read_text(encoding='utf-8')
for aid in ('minimum-0086','minimum-0087'):
    body=s.split('## Parent '+aid+'\n',1)[1].lstrip('\n')
    body=body.split('\n\n',1)[1].split('\n## Parent ',1)[0]
    b=json.dumps({'version':2,'result_markdown':body},ensure_ascii=False,separators=(',',':')).encode()
    print(aid,len(b),hashlib.sha256(b).hexdigest())
```

## 9. Непокрытый остаток и продолжение

Результат не изменяет **34 <= C_min <= 622**. Из семи конечных контролей не вычитается ничего из старых FULL/LOCAL-каталогов. Ни число оставшихся classes, ни полный геометрический census не заявляются.

После новых отсечек остаются:

* Внешний единственный U: только базы с нарушением отражательного порога (B4), с обязательной положительной бисекторной стороной (B1). Сюда по-прежнему могут входить сильно асимметричные тела любой из трёх пар степеней и разорванные/сходящиеся selected dual-леса.
* Единственный U в B: отражательная теорема не действует. Если B — единственная строгая S и нет дополнительных слабых resting packets, необходимо нарушение хотя бы одного закрытого cap-неравенства, то есть Delta_x<0 или Delta_z<0. При иной стабильной грани остаются, в частности, тела с неустойчивой B и достаточно общим overhang.
* Границы истинной инцидентности и случаи со слабой B не покрываются расширением «по непрерывности». Их нельзя принимать за строгий 110 без отдельного аудита packets.

Наиболее полезное продолжение — не локально шевелить центральную базу в надежде убрать второй U: количественный зазор (B4) доказывает бесполезность всей такой окрестности для внешнего единственного корня. Следует использовать полную форму (NF), выйти за настоящий Hausdorff-порог, после каждого изменения заново вычислять объёмный COM и следить за четырьмя примитивами всех 17 реальных рёбер. Три точных тела S2,U2,H2 дают стартовые геометрии степеней 7,6,5, но никакая конкретная последовательность уничтожения их лишних равновесий здесь не доказана. Переход через нулевой примитив надо различать с реальным EF/VE/VF-событием; граничный слабый объект не является искомой строгой конструкцией.
