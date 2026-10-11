# minimum-0113

Historical AI scientific report · saved 2026-09-19 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# STRESS_RIM_LENS_BRIDGE_V1

**Ветка:** [internal-source-reference]. **Исполнитель:** slot-3, Steady Lynx 90.

## 1. Итог

Получен **совместный секущий–гребневой критерий**, допускающий положительный дефицит трёхопорного секущего минимакса. Когда одна половина тела не даёт второго U, тот же дефицит ограничивает общий сдвиг и высоту областью, внутри которой настоящая база становится строго устойчивой, а настоящее внешнее ребро принуждает вторую строгую S. Во всём заявленном секторе доказано

    S_nd>=2 ИЛИ U_nd>=2

при одной M>0 и N=M^-1. Положение предполагаемого U-корня не задано. Метрики с неустойчивой B также охвачены: в них действует U-ветвь альтернативы.

Построено и полностью сертифицировано непрерывное семейство настоящих E17-крыш с параметром a in [173/100,1739/1000], **всеми сдвигами v in R² и всеми положительными высотными параметрами y>0**. На всём этом интервале одновременно не проходят два прежних самостоятельных достаточных теста: сильнейший одноплоскостный all-shear/all-height секущий тест и старый all-height ridge/cap-тест. Новый совместный критерий всё семейство исключает. Это семейное покрытие, не весь SPD-конус каждой фиксированной формы: горизонтальная метрика в данном конкретном примере равна I₂; общая теорема ниже допускает произвольную G>0 при своих явных условиях.

Выполнена также требовавшаяся проверка буквального recovery родителя. **Проблема оказалась шире затенения H/R:** несколько заявленных свойств его 15 контролей и численных pins не воспроизводятся из буквальных входов. Ни один из этих 15 контролей не находится в заявленном строгом старом высотном коридоре; три контроля alpha=1/2 имеют оба апекса выше собственного COM, а не один ниже. Эти противоречия перепроверены независимым восстановлением hull, COM и механики. Общие аналитические секущие теоремы сохраняются; действительные непрерывные сертификаты трёх родительских семейств восстановлены с исправленными числами и новыми pins.

**Весь двухапексный E17 остаётся открытым. Настоящего 110 не получено. 34<=C_min<=622 и все исторические FULL/LOCAL-счётчики не меняются.**

## 2. Источники и исполненный аудит

Полностью прочитан новый research-journal(20260919-112747).md, включая буквальный parent: **308520 bytes**, SHA-256 `84651d6ac9bc05ccda619612e392437a8adc52a95bf949565c342f7e08f50813`. Родитель — `minimum-0102`, заявленный SHA `690f7751a44b598c31c7d3259b8d3f44ec1902b7f0251874edaba663bbb90e2d`, ACTUAL_SECTION_PAIR_SHEAR_CONES_V1. Обнаруженные ниже расхождения относятся к его буквальному коду и утверждениям о контролях, а не разрешаются переименованием объекта.

Обе новые части SECTION_STRESS_HELLY3_E17_V1 прочитаны до EOF: source `[internal-source-reference]`, **10447 bytes**, SHA `e7d76e7640274c9195a90c4f2bd849c08eadf7ba9bea04d9a50fa502a5e5cf97`; полный proof `[internal-source-reference]`, **16600 bytes**, SHA `c5a7ddce398f2e2521bfe68e58a3ac59e1fedf807dfbabb73d325ee0bedffd09`. Их исходный build/check выполнен без изменений; воспроизведён section_stress.json, **18556 bytes**, SHA `cf5ad162fe96541c2826f5c3088fdc3f9dc544fbf35e90a9a5e17c0075b2e988`.

Используются доказанные в этом материале тождество положительного stress, точный минимакс и граница его одноплоскостной применимости. Это наследуемые результаты, не новая заявка на них. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1} Его настоящий balanced-контроль с апексами ±41/40 не отождествляется ни с родительскими B1/B2/B3, ни с новым семейством ниже.

Неизменные ранее предоставленные доказательства сохраняются. В частности, закрытый cap допускает настоящий слабый EF, reflection не исключает U в базе, выбранная полная цепь не равна произвольному available-лесу. Новая работа не использует covariance-оценок; обязательное усреднение covariance и арифметическая поправка 444690 не изменяются. Необходимого отсутствующего источника для нового результата нет.

## 3. Общий мост от малой секущей половины ко второй строгой S

### 3.1. Одна действительная геометрия

Пусть P — полный выпуклый трёхмерный многогранник постоянной плотности, B — его настоящая грань. В исходном аффинном chart B лежит в z=0, а настоящий объёмный COM равен g=(c,gamma), gamma>0. После вычитания g обозначим вершины X_i=(u_i,z_i). Центральная плоскость L задаётся z=0 в этих центрированных координатах, то есть она параллельна B и проходит через настоящий COM.

Пусть K=P_centered intersect L — настоящее сечение и r_k — его настоящие вершины. Зафиксируем G>0 размера 2×2 и положим

    R²=max_k r_k^T G r_k,
    M(G,v,y)=[[G,Gv],[v^T G,v^T Gv+y]],  v in R², y>0,
    N=M^-1.                                               (3.1)

В физическом евклидовом пространстве это единственная аффинная карта

    (u,z) -> (C(u+zv),sqrt(y)z),   C^T C=G.

Она сохраняет настоящий COM в 0. На центральной плоскости метрика равна G, поэтому R² не зависит от v,y.

Для каждой из двух открытых половин I_± выберем неотрицательные веса lambda_i с суммой 1, поддержанные только на настоящих вершинах этой половины. Определим

    S_lambda=sum lambda_i z_i²>0,
    b_lambda=sum lambda_i z_i u_i,
    v_lambda=-b_lambda/S_lambda,
    T_lambda=sum lambda_i u_i u_i^T-b_lambda b_lambda^T/S_lambda,
    E_lambda=tr(GT_lambda).

Унаследованное точное тождество имеет вид

    sum lambda_i |X_i|_M²
      =E_lambda+S_lambda(|v-v_lambda|_G²+y).                (3.2)

Lambda здесь — множители выпуклой двойственности, не свободно назначенные массы тела. COM уже вычислен по настоящему объёму.

### 3.2. Теорема

Предположим, что для **каждой** открытой половины выбран stress, удовлетворяющий одному из двух условий.

**Высокая половина:**

    E_lambda>=R².                                         (H)

**Половина, поглощаемая гребневым запретом:** E_lambda<R². Положим

    d_lambda=(R²-E_lambda)/S_lambda>0,
    beta_lambda=c+gamma v_lambda.

Требуется beta_lambda in relint(B). Пусть

    rho_lambda=dist_G(beta_lambda,boundary(B))>0,

где расстояние вычисляется до настоящих замкнутых рёбер края B. Выберем настоящую точку r=(u_r,z_r) настоящего ребра, **оба конца которого находятся вне B**. Положим w_lambda=u_r+z_r v_lambda. Требуется

    |w_lambda|_G+(gamma+|z_r|)sqrt(d_lambda)<=rho_lambda.    (L)

Точки ребра и stresses для двух половин могут различаться.

**Тогда для всех v in R² и всех y>0 выполняется S_nd>=2 или U_nd>=2.** В частности, S_nd=U_nd=1 невозможно даже при наличии других слабых контактов.

### 3.3. Полное доказательство

Если каждая открытая половина содержит настоящую вершину с квадратом нормы не меньше R², применяем equality-safe секущую лемму. Максимизатор нормы на каждой отсечённой половине можно выбрать настоящей вершиной вне L. Для каждого настоящего реберного направления d и достаточно малого t>0 максимальность даёт

    2t X^T M d+t² d^T M d<=0,

откуда X^T M d<0. Получаются две различные строго неустойчивые вершины. Этот шаг сохраняет равенства исходных радиусов. :contentReference[oaicite:2]{index=2}

Иначе одна открытая половина целиком имеет вершины нормы строго меньше R. Она не может удовлетворять (H): из (3.2) и y>0 её взвешенная средняя норма была бы строго больше R².

Следовательно для неё выполнено (L), а (3.2) даёт

    s:=|v-v_lambda|_G²+y<d_lambda.                         (3.3)

Настоящая стопа базы в исходной базовой плоскости равна beta=c+gamma v. Поэтому

    |beta-beta_lambda|_G<=gamma sqrt(s)<rho_lambda.

Так как beta_lambda лежит внутри B, весь шар радиуса rho_lambda вокруг неё содержится в B. Значит beta находится в relint(B), то есть B строго устойчива.

Для выбранной точки настоящего внешнего ребра треугольное неравенство в физической метрике даёт

    |r|_M<=|w_lambda|_G+|z_r|sqrt(s).

Для любой точки b на настоящем крае B, напротив,

    |b-g|_M>=|b-beta|_G
             >=rho_lambda-gamma|v-v_lambda|_G
             >=rho_lambda-gamma sqrt(s)>0.

Из (L) и строгого s<d_lambda следует

    |r|_M < rho_lambda-gamma sqrt(s)
          <= min_{b in boundary(B)}|b-g|_M.

Применяется действительная ridge/rim-лемма: точка настоящего ребра вне B ниже всего края B по норме принуждает другую строго устойчивую грань. Для полноты её геометрический шаг таков. На настоящем ребре или вершине поверхности квадрат нормы не имеет локального минимума: направление к внутреннему 0 принадлежит касательному конусу и имеет отрицательную производную, поэтому хотя бы одно осуществимое поверхностное направление строго уменьшает норму. Минимум на компактной боковой поверхности вне relint(B) при указанном строгом сравнении не лежит ни на крае B, ни на ребре, ни на вершине; он лежит в relint другой грани и является её строгой стопой. Таким образом, S_nd>=2.

Обе альтернативы доказаны. В частности, при неустойчивой B малая половина невозможна и действует U_nd>=2. Никакого независимого выбора полярной метрики, фиктивного центра или слабого EF вместо второй строгой S в доказательстве нет.

### 3.4. Отношение к трёхопорному минимаксу и точная граница нового метода

Материал SECTION_STRESS_HELLY3_E17_V1 даёт

    min_v max_{i in I}|u_i+z_i v|_G²=max_lambda E_lambda,

с оптимальным stress на не более чем трёх вершинах. Поэтому ветвь (H) можно решать точно с поддержкой <=3. Но новый совместный тест (L) зависит также от v_lambda и S_lambda. **Не доказано, что оптимальный stress для всего нового совместного теста всегда имеет <=3 опор.** Такое расширение границы Helly здесь не делается.

Если E_lambda<R², прежний одноплоскостный тест действительно может провалиться. Новый вывод состоит не в отрицании этого факта, а в том, что вся область его возможного провала ограничена (3.3) и иногда целиком попадает в действительный стабильный режим. Условие (L) достаточное, не необходимое: его провал не является реализацией S1,U1.

Для нескольких центральных плоскостей сохраняется простой совместный принцип. Если при **одной и той же M** несколько открытых половин имеют сертифицированные вершины нормы не меньше максимума своего сечения, каждая такая половина содержит строгий U. Единственный U обязан принадлежать пересечению их множеств настоящих вершин. Пустое пересечение исключает U1. Независимая оптимизация метрики для каждой плоскости этого вывода не даёт. Нового глобального многоплоскостного покрытия всех E17 этим принципом здесь не заявлено.

## 4. Полное семейство, в котором два старых самостоятельных теста не проходят

### 4.1. Буквальная геометрия и настоящий COM

База, в циклическом порядке, равна

    (-1/10,-1), (-1/5,-1/2), (-1/5,1/2), (-1/10,1),
    ( 1/10, 1), ( 1/5, 1/2), ( 1/5,-1/2), ( 1/10,-1),

в плоскости z=0. Два апекса — (-a,0,1),(a,0,1), где

    173/100<=a<=1739/1000.                                (4.1)

Все восемь базовых вершин настоящие. Две горизонтальные опорные стороны базы дают четырёхугольные боковые грани; остальные шесть сторон дают треугольники с соответствующим апексом. Таким образом, на всём интервале V/E/F=10/17/9, база — единственная восьмиугольная грань, степени апексов 5/5. Это не координаторский unit-circle контроль с апексами ±41/40.

Площадь B равна 7/10. Симметрия настоящего объёма даёт c=(0,0), а интегрирование сечений (1-t)B+t[-a,a] даёт

    Vol(P)=(7/10+2a)/3,
    gamma=(7+40a)/(28+80a),
    h=1-gamma=(21+40a)/(28+80a).                          (4.2)

Независимые положительные fan из обоих апексов воспроизводят эти значения точно. Никакого проективного переноса COM нет.

### 4.2. Настоящее центральное сечение и stresses

При G=I₂ настоящее сечение через COM имеет вид

    K=hB+gamma[-a,a]e_x.

Его максимальный квадрат радиуса на всём интервале равен

    R²=(h/10+gamma a)²+h².                                (4.3)

Настоящее расстояние от 0 до края B равно rho=1/5; проверяются замкнутые стороны, не произвольно продолженные прямые.

Нижний stress использует противоположные базовые вершины 0,4 с весами 1/2,1/2:

    E_-=101/100, S_-=gamma², v_-=0.

Верхний stress использует апексы 8,9 с теми же весами:

    E_+=a², S_+=h², v_+=0.

Эти значения являются **точными минимаксами**, а не только нижними оценками: stresses дают нижнюю границу, а v=0 даёт совпадающую верхнюю.

На всём замкнутом интервале доказано

    101/100<R²<101/100+gamma²/25,
    R²<a².                                               (4.4)

Следовательно сильнейший одноплоскостный all-shear/all-height U-тест не проходит: нижний точный минимакс меньше R². Однако для нижней половины

    d=(R²-101/100)/gamma² in (0,1/25).

Возьмём настоящий midpoint апексного ребра: в центрированных координатах r=(0,0,h). Тогда w=0, gamma+|h|=1, beta_lambda=0, и условие нового моста принимает вид sqrt(d)<1/5. Оно выполнено строго.

**Итог:** при каждом a из (4.1), каждом v in R² и каждом y>0 имеем S_nd>=2 или U_nd>=2. Более конкретно,

    |v|²+y>=d  => U_nd>=2;
    |v|²+y<d   => B строго устойчива и S_nd>=2.            (4.5)

Равенство в первой строке безопасно по секущей лемме. Полная обусловленность M не ограничена.

Старый самостоятельный all-height ridge/cap-тест также не проходит при v=0 на всём интервале:

    Phi=a²(1-2gamma)/(4gamma)>rho²=1/25.                  (4.6)

Это утверждение именно о старом достаточном покрытии **всех высот**, а не о провале каждой отдельной ridge-проверки. Новый мост использует ridge там, где секущий аргумент оставляет малую область.

Семейство действительно пересекает строгий старый промежуточный коридор. При v=0,y=1: L=a²/(4gamma)>1, поскольку a²>2>4gamma; минимальная гребневая разность после вычитания базовой высоты равна 1-2gamma=14/(28+80a)>1/25. Вместе с (4.6) это даёт все три старых строгих коридорных неравенства. Новый результат исключает эти метрики через U_nd>=2.

### 4.3. Полный непрерывный сертификат

Положим D=28+80a, g_n=7+40a, h_n=21+40a,

    R_c=(h_n/10+a g_n)²+h_n²,
    R_s=(h_n/5+a g_n)²+h_n²/4.

Проверены пять полиномов на всём (4.1): R_c-R_s, R_c-(101/100)D², (101/100)D²+g_n²/25-R_c, a²D²-R_c и 175a²-2g_n. Их коэффициенты по возрастающим степеням a буквально равны

    (7938/25,5901/5,928,-320),
    (-34643/100,-13993/5,-4575,880,1600),
    (34839/100,2821,4639,-880,-1600),
    (-44541/100,-8631/5,-1105,3600,4800),
    (-14,-80,175).

Все **22 рациональных коэффициента Бернштейна** этих пяти полиномов на одном полном замкнутом интервале положительны. Их генератор и независимое раскрытие сохранены в recovery. Это не проверка знаков по сетке.

Например, при a=173/100:

    gamma=381/832,
    R²=537954533/532480000,
    R²-101/100=149733/532480000,
    d=1703/1270000,
    gamma²/25-(R²-101/100)=56117871/6922240000>0.

На другом конце a=1739/1000 последний запас равен 3537649071/4363921000000>0. Строгие геометрические запасы допускают малые изменения настоящей формы с сохранением инцидентностей; количественный размер такой многопараметрической окрестности здесь не сертифицировался.

## 5. Девять настоящих контролей и полная механика

Выполнены точные проверки при a=173/100,3469/2000,1739/1000 и, для каждого a, при

    (v,y)=((0,0),1/10000), ((0,0),1/4), ((4,-3),1/4).

Все девять — рациональные евклидовы тела с вершинами

    (X_ix+v_x X_iz, X_iy+v_y X_iz, sqrt(y)X_iz).

Для каждого восстановлены все supporting-triple плоскости, максимальные грани, настоящие рёбра, два объёмных fan, COM=0, взаимно обратные M,N и 68 настоящих реберных примитивов. Все примитивы ненулевые, weak000.

В постоянной нумерации hull-кода грани равны

    F0=(0,1,2,3,4,5,6,7), F1=(0,7,9,8),
    F2=(0,8,1), F3=(1,8,2), F4=(2,8,3),
    F5=(3,8,9,4), F6=(4,9,5), F7=(5,9,6), F8=(6,9,7).

При обоих v=0-контролях для всех трёх a:

    S={0,1,5}, U={0,3,4,7,8,9},
    H={(0,7),(0,8),(3,4),(3,8),(4,9),(7,9),(8,9)},
    (S,U,H)=(3,6,7).

При v=(4,-3),y=1/4:

    S={5,8}, U={3,9}, H={(0,8),(4,9)},
    (S,U,H)=(2,2,2).

Последние три тела имеют неустойчивую B и одновременно базовый и внешний U. Они показывают реальность ветви с другой устойчивой гранью, но не являются 110-кандидатами или новой верхней границей.

## 6. Обязательное исправление буквального parent: конфликт данных, не переименование

При содержательном использовании старого исходника я применил указанную автором H/R-поправку. Она необходима, но **недостаточна для исполнения буквального блока**. Родитель действительно предупреждает о затенении переменных; это предупреждение не подтверждает остальные assertions. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}

### 6.1. Что исправлено и независимо проверено

**Строгий коридор.** В буквальных 15 родительских контролях список strict_parent_corridor равен **[]**, а не [1,6,10,11,12,13,14]. У особо заявленных контролей 1,6,11 прямая разность

    dist_M(0,[8,9])²-min_{b in boundary(B)}|b-g|_M²

равна соответственно

    -66828615803/33951999534400,
    -99818780071/35558789281600,
    -865531993977/320152876710400.

Все три отрицательны: прежний pointwise ridge-запрет уже работает. Поэтому эти 15 тел не свидетельствуют о заявленном выходе за прежний строгий коридор. Родительские строки, которым это противоречит, сохранены неизменно. :contentReference[oaicite:5]{index=5}

**Высоты alpha=1/2.** В контролях 4,9,14 меньшие из двух центрированных апексных высот равны

    986669235/10417955488,
    79389691945/797986240736,
    396183541695/3976177030688.

Все положительны. Эти буквальные контроли **не** имеют апекса ниже COM и не являются заявленными контрпримерами к both-apices-above. :contentReference[oaicite:6]{index=6} Это не доказательство универсального both-apices-above: такая общая гипотеза по-прежнему не используется. Никакой новый alpha или иной объект вместо ошибочных контролей не подставлен.

**Полосовые константы.** Фактические минимумы угловой арифметики равны

    min upper_gap=699/9800,
    min lower_gap=1009/19600,

а не равенствам 1399/19600 и 1251/24500 из assertions. Первая старая нижняя оценка была завышена на 1/19600. Вторая старая величина меньше действительного минимума и остаётся допустимой нижней оценкой, но не точным минимумом. Оба исправленных запаса положительны; аналитический полосовой запрет сохраняется.

**Полиномиальный реестр.** Буквальный генератор на своих буквальных входах даёт **198 полиномов,198 замкнутых листьев,10086 положительных коэффициентов**, не 210 листьев и13410 коэффициентов. Все 198 полиномов сертифицируются сразу на полном исходном интервале. Таким образом, сами три непрерывных проективных исключения сохраняются, но старые размеры и pins отчёта не воспроизведены.

**Полярный отрицательный контроль подтверждён.** Утверждение -(q_B+q_i)/2 in conv(other poles) действительно ложно на указанной настоящей геометрии. Например, для m=1,alpha=0, side-pole1 и apex9 превышение настоящего опорного неравенства равно 319938560/307438131>0. Этот отрицательный результат не отозван вместе с ошибочными высотными утверждениями.

### 6.2. Фактическая механика родительских 15 тел

Для каждого m=1,2,3 последовательность пяти исправленных строгих счётчиков одинакова:

    (3,6,7), (3,4,5), (3,4,5), (2,2,2), (3,4,5),

все weak000. Их hull, два истинных COM-интегрирования, U, S по множествам вершин граней, H по настоящим рёбрам и прямые расстояния до ridge/rim согласованы **вторым** геометрическим движком из нового источника SECTION_STRESS_HELLY3_E17_V1. Это независимая проверка нужных физических величин, не только отключение сработавших assertions.

Извлечённый буквальный Python-блок имеет **15228 bytes**, SHA `ea787508fac8b207ee3251a0587b83a8e797cc7283639e8d2fc9d7b2eabfe320`. Он не совпадает с прежним объявленным 17125-byte source. Сохраняются и этот неисправленный буквальный блок, и полный точный patch, и исправленный successor ACTUAL_SECTION_PAIR_SHEAR_CONES_RECONCILED_V2. Старые pins `af1e089...` и `b312d4...` не объявляются восстановленными.

## 7. Полная самодостаточная recovery-капсула

Капсула содержит четыре **полных** source-unit: новый bridge.py; неизменённый извлечённый section_pairs_literal.py; точный repair_parent.py; независимый audit_parent.py. Сжатое DATA ниже содержит все их байты, а не ссылку на sandbox. Сам неисправленный parent-source не исполняется; он является точным входом явного patch.

Среда исполнения: **CPython3.13.5, только стандартная библиотека, assertions enabled**. Сохранить блок UTF-8/LF с последним LF как recover_bridge.py и выполнить

    python -S recover_bridge.py sources
    python -S recover_bridge.py build
    python -S recover_bridge.py check

Все команды выполнены. Затем только wrapper перенесён в чистый каталог; build/check повторены. Все три JSON и исправленный source совпали с pins; stdout build/check совпал побайтно. Это исполненный exact-аудит, не внешнее рецензирование и не proof-assistant формализация геометрических лемм.

| Объект | Bytes | SHA-256 |
|---|---:|---|
|recover_bridge.py|16924|99014a10b894d0f3feb875ae50a6330dcc06252ce2fe1af70befef97f0c15544|
|Полный четырёхисходниковый payload|32721|10760589c3915c017e0350935853cfa5f9bb5d142ebb95d837160463dc784c6f|
|bridge.py|11790|d90a69aeb7bfc85264a0007daa6f2a7d8c2752aed84d8b0f67f9db8eda2b7422|
|bridge.json|36293|88a47c551e64feb056f6a3e9d6e8d297c60d25490f553dcf63f56e359170bab8|
|section_pairs_reconciled.py|15645|e0fb8e0cb37d3aff75d8b2b9ea8a892fe1de8bc6b84f7a070fdd2bbc8680920a|
|section_pairs_reconciled.json|3799163|5ffb07a2c8fb95e2d128fc45d10a902f47896094cf55bd55d2338d8a8923c975|
|parent_audit.json|6928|cf97d2d2960a26871e6e2b28f79ba77adaf44e308ed278a2a2b2880f384ac254|

Ключевые ожидаемые маркеры:

    STRESS_RIM_LENS_ALL_SHEARS_ALL_HEIGHTS_CONTINUOUS_PASS
    OLD_SEPARATE_ALL_HEIGHT_TESTS_BOTH_FAIL_ON_WHOLE_A_INTERVAL_PASS
    POLYNOMIAL_CERTIFICATES 5 22
    STRESS_RIM_LENS_BRIDGE_RECOVERY_PASS
    THREE_WHOLE_PROJECTIVE_INTERVALS_ALL_HORIZONTAL_BOX_METRICS_PASS 198 198 10086
    PARENT_STRICT_HEIGHT_CORRIDOR_CONTROL_IDS []

[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]

```python
"""STRESS_RIM_LENS_BRIDGE_V1: full four-source recovery capsule.
CPython 3.13.5, standard library, assertions enabled. No external inputs.
python -S recover_bridge.py sources|build|check
"""
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
assert __debug__
ROOT=Path(__file__).resolve().parent
DATA="""
c-qx{3s>97vhH8;nZ53^WZGaG2oI;T76}e;HUVNtCfSacmTbwkz?O|9gUy`z@3$V^QcE_3%${@3y?b_y)Q{>{b#--heXT!!bLU==
I5Ri$!(?-|{O$0!AN1c@==n1re!`?Qnvcg@6E}{xCVqe9hCx3rMSg!8_JeWYCc!i;O$Q}+JTBFDOXDE%BX?Ya=p>qs<INx8Y?+K8
P4&7|DD6jhtP1G|eq4g!QZj;nk5kA#nT`F#FU8Y&)Q89*i~|qj11|i*kCvt0JoLss6v37L5e}m1q%?@!KGq5{O=i<5DScD{B{wd8
REcJ8G8zXxo#YB$e}w8~<i;2$ZsTc~2KJ)B8~RA1mxjeY(S;TTQS9hG@jXm6gIYn;1|=V|Ig=o?7UD^KvJZcRB~SJ?<9W||5(~ST
$cekKK3X+fV5*N+-4@l}W-k~+j!(j~xA?`Q7u$yX_mJQ9JctK6eRu3z2}U&|Kbc2iiPPUh`g=$nO&?>~=|a1wQE37lS+eS)A-1U|
80LxxvBdBW6ke@EjNt0v5B}Cgy@pR5`fS{5a_(Sgbz4R5=!}ikj1bqw8kVMGPtG=B1n2J9nh4i!&Z1x%L0HO;7Nilg&9er!1mcGf
8H6K00%r7_p*t(2K(b#Y1a-=h`&jNa2Ls{z!ozVvZr`@P+RcaQSPaDgf{^#EuL2T%?d*3crXhw6F=!Mb54uDeLVVy3izwJqS}FrR
QlaoZpZMjjptoT;mo4@a%l9EIK2QSWpcoRB+|Voik<4LcSTXRQ?^%7@rZMb`5su(s@TZi|q`-J0H*ot%?oTZ9o9r+vE}*8AZh`5(
cAK9mhM23qWsN%9U0_OYn!w}Xb{A6Hf}RxhrLI61$%fNM?3#3ZzKPG=!PrlF1XO#+L7Z5Sp;PWp=V5{km6C=y3!#=%nlI&U8Vk<`
oqV$ggHF)x)Viwm0alI(Ttmx?ePnhEWHa-qqOMhc>9Twu(iJG5IyBV-FQy`J_*8C=Nry0;CY<BZckj3jpCko*0$v1mm8s151`H>@
0b_yWsA7N-6JU%LY}D=lvybsvbs{$$`qn<lic-&weJ7Tozeucr(+CUr#m1C=2#grHi4PqH0R!T`zGA+VjBWOw(G7~UoDDl=eooxp
*yl7rjKdC9YHS!KB}s~nn1j#^CY&6_)TTSb^}zCiKGfBdV?VSo93-QJnLnP5TnW-j0td;Z;8`Sbmi2vHZ6L=`Fw4jsLkXjDlAi?&
6vv(U3kS3N5r~SB9}Gv3yMz7SX>ixW->%>~V-w(?;3drIPa_CNSv1@nLWh;(B!a3th3K;Q=#FEbWVh-IWC1r^TEHB|#LQL^jU%=_
%>yee^#(F_Ijv8*`?i*iJP6J=qF%T2xsYGdoG&#TIP{%KZATo4`VLZyB(8>=<EiV#7Os}i*k@M1O-xy~HzVKmoCMhp34}u#&nFfR
=>TNj+>Jb%5LnoN8jDkK0xAVflx8?i(+_bZVZnbsIRy_%02#EKVLzoY1`hS3Fi!j+{6#txIL1JuB5D6x;ZTHQ5#pq=>IeIR{?%&x
Zy?RIcPkY$Lr(|EQkJh<A8yVrFPy8Rv-Y)fes<GpADuhx)`!cB4`=6RM-+MV<@oHz`PwK0(~q6{uA>G`YgH0QQ_QC0WjLJ#6hU0y
(Uqa4#p#dTV1h$)3q$35606T#RzfKy$~>j&Ta8lBA5R}kA1*&ZC}af%%pVK_(96PPYdTM6^JI%vu~Isz+|V5_lc4YTi~e{XBP)Oc
;szm<bQ8^eXuszsuC$1Ay!ix{;oc@FdsEN1pl57>;@7$JmocRmu@7^>O{P&SEvSYlAC_%<qx|Csa+AsjtGi_OQ}c#&O2u-`+2$jz
`A%<{__2khLnS~6hcGwKE{<DQE%>>(agNT<p;J%4oS!?;Wam@s!|Bn**@tWA=;GLEpB<mHoRg!gYZ#>K>vBfo^86Umw;{o0o07h7
onQV=Bw+Y%+Lu7?{OIh{HH_zf!Z^2%v&^&2(4F`Kd6DWRl$N;}kKD%Y8xGtY`3o<ArGn?oZ{jyrJ5AO6`lj8wh7!&`Ip?j5Yv(=J
_iKH#^x=wC?d{F__U3N01QHL1Ao5_1?L}_1Y%0M`$}x<Ishg(-fmR)iz5nWu{QljK@M2nm84NSW#Tfu>5JNG*g&@4A^SCthrxPEA
9xRko*aZZrsgo8DE5A1#4E~aGj(dn?3Vf~;!FHe*gtXU)1s3Ja`-w_C0dCOghJ8<r`x6nw_faA+*DKV0<Q+X4B3{Pn)OH-t@6Csf
^CLWKNQ+f-)=;&!S|_27YCh`YuISl^C8dS4hOyXKvRcI|_ERvURJPt7pzgIUTlFW|l-BPSGbWWqrpCExdQ{wU#h_fY7M1m-a3giz
el!IYH<#OTJN0g*2P<RMg&%mTgFN7;8iv(4R;Z^shSfPXtCLT468(%WSCb3Gh&1iw!8(G?QlYV!93&w`@R|t{44QG2=Hfln5$Kz_
5*C8UEi>{#2mxwqhSjPZ*?O*&ymvJS{~#@{))6-K2-;=~9niplnh{XLfO?noul(rH?}yGUs+n6J)%rHm*tYEzC2l*bB<@Ta)@%yW
B&NFZqf|;P>6;vh<zfyjx!A>4Izo2E>g$oQt5!Nn6t2_!U@e3;kW{zWzbDmzixT{&b9h*VjI>{iI4vcfVN%FJ5v9iws0Srd>g;!Q
QiZ98QKt%B2*1#?GyAQqL1i~*)0sv3D?BT;aAp@3#i&E&X5CC$POZB^f9qYd>$Y=UH+DlmmVf-IS`~;}afg*PC5=*mvBJ7z)wa15
N*-&RzN!muySg)A2O*4zJ2L|K3Rn!7Ff;;{x~!GL5Js!dGS<hacq}`dWnovnY<e>Rt!$%`7mw|?wYO+bfTt4f_xVvu6)UlGP1;$;
cNi5)mMqn}2&t-74^x5mB0;WN6>G5x&!BUJxK3wPu_~c9PLy2P!3A$ofs}SJNf(F)4-y2mRdFf#Nb;=sXf3w3AkNOquaX+8&ZrA?
)nG01dlxl2*qCgGx`4*wwv`wc_jVZ%j|8Yc)PqEN6V{taZ1Ko?(R9X}r8`P{XU;_|VFUw;(qVxVpGkA~9}?-%(2S?kyZKD-IMYD~
Dp_76W*-LG<cIpvezU)n9VXCObhD0OQNR(lW&mvZ3Rm`*Fbz@$gtuBZ&z%s|SV^Gw_HU6}mY~Ul(i{6cALB$qPyq94K^u$y5}6t*
3VGw?u)6_&596d;Flj(C-c>@=Y%L!^HtB_@zZ6(km0t^!lCg_f+rC~}b+^ziGeWmVZEnaG(qCey^=Z~2d#d%d#LS{4j1t*Ud)P7C
nw2(D=2CaKQQr_F1A*;W*;->3ZVx8%pKr2muCHr_<eT){@w;*WB*>DWWq#g_;j87t*E#>B8fHCc-HO20ky`HQcO$JK@v8VtW!f9G
ccZpQ*~n67rUFw^>e0@dhcI`><$W>)6;?cx2+LZSXEc0kNWlmyN+!Rd5T#}Oo;&1zMY4k$xos}bL`_gTMaQE4hOPnq1)reT)Q(Yg
7o|%V7qS4V<&fz_{(!3fFda)&rJAJyY>^YmTBBXrh5$Fr<Wa6oDW4dML7nyu&|THKninvOKqJA~iad17zZ-RwObM*OshG)$lrAsB
tm0T~_QSenf+dM;d+SZA`#i#;KzX1g8}d=N19e?`61-YGZtVyR16uSqiLhSk2^Mwu1%1g@>jSnuonBBY@n{>o2PKihr3MDAJK73~
&s3}p{T!yMa1!}3niz=`+cBt<G<$-ktAnLvwFBjr4x`eHNrHwo)MVkWhq?s5m_`vLzplx&@L18wD-FdVk9vBW^}!rHwb14BeKXdA
=Q0-;nFi6jk)~2<P`y)B$1hW@_Aq4+l5JgQHjcD}^@VCRnvEK<G$=~-S6s_$(UU!KBX0y-m{P4`>)PDK_@N&Smlp8RNq%P%C!O*Q
*<yjUD<}N7C@30sahf!Y4Fl~;trM~~8{BXLBMSeA0YyGgZ%{(L3;%yd?{ykXj9wCN+)LOl03mGtC)ft6OhP3V_oVw<M1z9sD!7ip
7)#Fr*RKb0Z*S1XqjVv0*YT+!qOtX#)F58Kk8XEP#Q;7=4J(lHcFl%i&8{LFxKH9D>!O@_o@AdlcgISI>5hXOQuStbd@>x$P6xMF
uJ{BaN=4FA{*9~a@^iCvdz&V_$R+%2B>aqm=}W5K<=295HmOwDIm01y!dre&((QI_`rH4I0jWmU&(Qsx(Y?J@bopUD-OmNOG03+u
X_d_q8uCF4XqHB9G=V@4okhVUNP-7b^}G`x^TaJM#sC$HyrO_pG#dxC{5{FE-BsOgVTRn|gMg|Jx}YRi`C*U`8R3I%R!K|XC-W@k
3HMG<z^re1emsGMg7<BB*P8{{P&|=dsM@dT+z}mroTkC828sJbBH1k~C64u=HH6MEv?&9Zqi@)fZ?sS1rNWcCIThWCs%{s|(!wSk
lx<gxd$NjE-tt5h>%ZlhiX=+@MAWN^prp9#;S~X<B5Xb-)r+eH2|hzfwyNQ{2d|^9su&ur9(+*FS#pZ|{78OIHzW5%wccH)&EC^?
x1Q-JpPBd_XxFm*^<x={uy$G#bvs?Uxa!cs(BH9NvdUju#iSHbZhb5>MP$%T(8pljyYq2k%>+qsDhPjASC%uO+QolZC;;=?c6tiA
X1r0|a<Mk)gnj~XuBSpSgWBa{bq-B!^P08GFRX7W)>3LFpG|-wMOHm)xv6@28rebz8Jki&Gu?1b;1emAK<K;dSPNvr2bB2>wA(Cz
9pSaEUR4HsHk6`oICyQyoXK){Y;>zc2Lr1_f+YSH(=ZfIl5YA8Y$!n<YHM634Zj=G@H-!Og5+GAv~479lUP{_e<{4BWGlz_to@yS
?r?b71&a9~l=NJjzm#<B7}Fb2lPH5wiCv1}5*02<itcv-<$cE`FD+&WiGl0jzoLeqkLo^2TtzO#Y_yC6m`%<DTA^`I{yhtuO;Mb-
jYR5zZ<z&U2YpL@(q}RM2<9JQ@{dib$QSuVWM{KdMGBJHbofk@<G~%z{n)~-qGDX<$&aRdaw~P1Fl2i6Xec!4;l?3zdk_a9n&JBt
Dn1%|P7+bVwdt_;vZQ}t+B^GDkyj>?JMlng`n_9i!1!}5EejhdNK3Rcnw>l`O{$xXAiVt`E&Cs(FJbWDMgd5+lD`1iP|A*;VDA_t
BTx{6J~9LhkQanQ^ZW>XfXEsN{bkMA{Kg$Wac9;?kb&3-nQ?HYje|3^2;wp_ORa%9YwApy-e)dbr*$Nj1DiNp$FVowB2ia~#G1Wf
^>Q)2G^VH};5x>61t+xat}ZgR`cUzFk$uzlK1-8MxOUX+4(<TE6-9P~$-<^CHA5CGTW)4HxMd@K76&wEonYg(yCD~qrO`Ru&x#`-
K-MpaN<@26?es&<WV;SpRu3Z?RTdkrVM<jtbU%V25o6F+kVq(bh^qDGecGCE!)Sq9u+7=)HnixqaCqOry1NzJnUhjf8CNP+P=yC;
R2|!u%57Gi4xLzFmdZzqa@?UBMNc6-t*E_sP=q?kC~DAHUtsk2Qh7Yp=`5#O=Yt&x*yVT8$cLB#b$$NB9!!PTeDW27W|2^l>#L&+
G!E4Fw#i{i(BlC<*Yx>PHsh3~(v`*`RPz|$8vFRV4|$qHeBZ;@9ef>8bX~tg_M|Ui-T)u#+Kg;LtU83`AXc-;-CP_lg`9O_C4G_f
DQbkuY_lEfh*-c5Qz!yESrW`XohR}S<Ow{Dh8>_2#E$kQfGJl#1RCu=W`+)HqZFsacoH6ud^buHCw`nb12-7QMjq_c8vC7LsmJ2j
))Yej(YZxE$Kk_HXNC(HXHJ`2%&QyG*rl)`_JOS{*Vm-ypyNc&$Q=(Hcl_usV`uC}L!U`cEb2TrPc)YwPwTOPtUNeey}mmuwvj8d
x2wj(RiqkNE0q3jXzVrUz?qI<pv!Yc?jCH<d0tnL_w1&j9rt={5-I(o)FN3Q7`~uBE|aOxC!X`Z*IpGcQD>1KLn@AUK`Zx%k?(KR
LFe;)Tn0*p{8%Fua9-*?!$<2@grr4>ET74cwvbp~)Zr|8sCTO>z^){wiml|HBr8piEFDTz+(F7p<*s7ECICc?6;|)o3JBg8g?XnW
>{7}7I(_sbP?%G%64~pS8*Rv`wE}fWzEslu3dByOXGkVe>)v-aI#$&c*_;-Z`9_1P-4t2VyRw^K(M7Swn%NaP*Iki^;#c-htmh)w
J5jr>d}Y@}N=Z9<cOtF5jh$M>wYNZ$Z0zHcW{jcI@E{d$L%vE9Feo`T8kl9<pp8R(#fzrz^WVY1CI=bVoa~7Mqaw<7P4>-#FC%1t
eO%?uMrWs6X>35tvTU>*&|2+hHg71bxQ0Xhx=dz&qq8e^k;FIIp@RbL@<>zUid-J^4v){fJDT2(dhWPng@mp~=P|o;*yv*a3Z)ri
ll$|;n4a30>>sMVb!HO0#lLUU{c}~tY*{Kw2iVQ%=NoA~hG>KZZK{d2$n3A;Rz!Be_Kzu`^Y>BKx5+)3PTC=1dRR*SX_O9kXtG`f
&S<tFb}}Es$~4-l*ES#sI0Lp{8>7ld*8&Jioer{UAp?>pn9L_75F9@Fc7Hg(ylx$XGBfwdkC2S+C_+HHF*<R^J8!g{ych53Fy(!A
eB?>&4BTd~ceBQ3&CtafA3Qq2Y(7zs&P2|!8p=%N03>}9PiCKye;p)&K2u8t#EqviHBAE#>}0OaN;7~}IWUs!!?ajQVvNhQQ)Xi-
dcckX^UYFQFD?7ntU8{Gvj$g5EowA#k<c~f!r`ejR<ex(&gNEJN{>ZRdKg5L+nFh5(6`wndY>zfyb#8TE8FdA7K;2g9SkHzZCO|g
lqwnN+FMTXR`n&-qTPNA6(WYY8R=aJZqTZ{WHJM}ixThSph{zOXwx1-{Sj_T#wfGZfq@?rF>*pc&_RTI8PYFG4=_n!$tsZ!i`&l9
be6zg4~k<4C)k)i_#QH2>X4T*Wa>-5#uJ`>;n#S&Q{akkJo~@*r}70y>gHPWY$?8%Y;JzAH<n7g#P{zc_pJ8F?N2iwSu}skMl<q<
0W5Llo8K>;>znr3ha2ZhnJqoBzcyd(xqR1Uu70Pi)GbZ}ti%sZi~?~3+TZ=$MK9FI^@2IjRMj*LlV~);<eA5G3NTUAvOg^vAJA7g
avw8W!xdY$B`%}1tH++4yJHF6sca2jbFReNJ2s{8O|X&Tvq&DN&TJaf{vY%+P`j)_4OU!RXzi4QJ^rL2+`I-%2LaN8EfTuvUcfu{
SfU^i#HkK*s)UKm`lWh@8OrgB=Zz_+66y$;G6FOZ*oP-P-^7~!R=q9MC`~|d1#L#n%dN(4m2;wsdNm5P-}Y$QK=P<YHE05FSv&N%
s<q{GZs>>1FAF^kSrzR=*UH@9rs=}^p_Dp-t2}9_TMeNUKD#;X-NJ-3w5n`J>$<EbNlb(1Guo}cX_#K~Hn3@$X4O14U|ZW%8AoWb
`$y?2t!@<;GIGXq(WRDrd=bh-&Xc}ps?OsjYQzIz7tl<Q9nf^Lsf3211Ml+6<-VZkqH4T@TRx?w;bu>3ZpTepjFCiJFT=(njIOn#
tz9#0Ylq4s2V>Ao+tnzxE60^%VVP1}1!Vz1Vu;MqRx!W}`Wf~o6?|<}bhUDa^IVebfQtUqDU%+J-o!kLPo!5sx~|$O7Tu?x^L{Oh
0B0+Rf9g4M`Iqm-i3F*LJF5rwF~-MbI&(S9^rOa^4)eu@eV4=+p*>vT9XUV@$I~7p?1A|6VrL$rWFDe#_4bZ<(?CBq5N<G0mkzIe
<%`RU7Fpp}oT0U~aGv}%S7^gjHwQfh$o~jI&N~inP#j0fvIDa@2py+vo`)|%W=6vY)RpMG0OT{yM;HT;>d3f^N76K<nysnhwel2Z
mut2-W;9_ADRPHvow0N4$c!-poB&h@ZbC_UTNj7===|KdK5ZSf`SG-Mc5-@iO`g|h7hf*FWbWD}!(aQlb#>G}x@j4CoSW7)WPE>l
bLxCNIy-kRFPz^`FV7*3b9QmlYJWXCU!iq%dH((4^3xeaeQ33B&OV-f0IJtz+TB23At$e8qcZs=F$&>n4GQ5&ZO~sLVASKo<(G>a
D7Mo#;8B^7LOL1Cs;It_b6OCCs52=3-a7iHlaeL<UoW)wzeV}4xV%3%_-dXbPU35;{XHF?-^6c`j|h}CAXeI02+$R0V_X4CoKPDs
G*Z=#ht6oe({h9T-QIO@;1B0l@Bi~O{(5$Frr@U_rq9s#{jh-eR3xBG0s6=+0EtfuXEFj&&-E$CCFPXg8&CUpIhXrl#eal12ygYK
u!3A%-jv)q)Dz?$asgHOF-S%ps5H>!Q2>iHYOGX21<@$Yf-o+6+`k6t8u_?uoJG?<o^g;5yq@jPwYY3Idon+PQ^$EWYfD+*Z8Y|I
6OkYJUT)YyWccph{@!kFA6DZ1UZb|>``eA(x?9`b-|OvfyZip$!Ct?=*Vx~Fvwh(2dyPT=z}xFJe784%q%}}AW7*sEd<7D5WvpBj
>0tCk!ZL73(i8S~S=2vDN3<H1TJ!!G78y4z3zSm#prR5iG6Ip?JB5EBf_bA+7IDWtd;&EjpQz1=@~2s4Lg2<S?i{+^jr)zb^K=Lc
8$w#k=3($|WwKFcCpCr7Nx{0Q4@Wue-guKHKEf8Ulc@k0h}qc16Q8jsQram%4fZFQK@Xu?6JQs%(=j?ICI(|x%xXaZqD`D<SmhtT
l?tFTJSfeMJhTw#U~_i5skm6eE}{Gle)bR1rF2c(kXc{bIQW;om*3W)&)?O`ur`*|)-avdDYi-1ixB2V??Hed(21I5694fVZC<wz
4n+On4enom6CCyif)4g6WPKjsRngelHS>Uul+h{VDj$8g`2q`xi3Q`O4Og?)HK{W{O{6hntz$%rtyFBy^wn!N*6~#szF)8T@t5||
`}3lp{>8?uiurugR#mJU1Yuo$LBtic?!^>BUm!rBOYQ;IGnxNo`K2|XENE81_DN3@I#%uw^0FrCpdL3weOuIbx*~<`842}EN`|0!
1R^6kjJZtn7GfFLhjQM5J+Xr}cLYPFkUJc(^`hGtT$0{eJtKr>oPpdB;6~Ur=lb$X`$LO0oH*4wSC(-j%9QG2FrLRFjRd4Q4~a<Q
R2rgC>L%@Yvh`;(nuk^gRZ4&1!`>88yP{kLF2ZB*nJth`S5RI}UMp!wZG`uoIt<VIcyxZ<G7x*$*QmJx`x)G3C=$;tb*Vz}^J!be
;E5FsUQPqZ&(0$D?r5wrcO<z~g~&9e1oZ%hGgg>#l%^hn=NP5;KZ?7<bfQGgIKOzm#&du>9!c4usrdfl&Gg2Z?}lfK=*?|>^u4xs
QQ!HF2-aN>WN**k9eD0;fA?U!=kM(7yMyh6-oduJQ}b$Xyxl#w-`MN#x;y=vyK~U*ZTo|Ro;%px_jWuqCcQtpZpqG%u!Bd3qKb#1
R+Wx6gr)w}VRMInV2blwb=O9dZ53^{+mxp(3KSp}Ca%6IQo==sPlAD7l?VcfJ@~uxET!rWJv8t%b`42YxhmekvCBlDVMkYIA6nOZ
%Duy9(B?7qn|u&t(7PX*-UPzedcgcRd4Ks$b`%J*2l)w~$LCj~&sQZ7dsv*eQBziI1(!U~N91(c%%!~^RQXCwWe!pKN<d`+PWdvL
GKZ!76)0r^Ncs2RC<`dc=RuSvgmM)@nc^okdQxL2U2$Yomgy3iwByzRCvz^D1RnhRpp%5_`$hC5){`uJ)`b0FltYQ4s4uy|^VdM^
3v^9c@dTpS3B(?V2|ABZ+Jp6JH|k=KQtUyBeNjVJ$2!2q4Qrr_N5GrC1!^L&$Pyon6Jf<gD405vYQ5Xt;HjLtZi8M8>m45KQj?Au
W^$1sOj2YC+c94UDj`0SovR!+Z7s^A+hi08a~@?rMu5l#9iCliTnJ%6^dv@BG>&<WO_;~=)|(XOVeM3oZE=x~93CDEysjcQdKQL=
b#==%oLsyir3O^>moIgL8ma8EA>2byv2Dr2*BlI_W~L^>B0KdBN>xG6(o9&iyQWVCA|a`{SJ@G>r>EUQcv@t%1*YucvA#6NxT%h;
^SAU|bu$1O9$t4-6k30|a=FV2Z1qZG1Fv$hz$=XiOoP)I&Dd1al&k!hLk8X%S<o9e!)CDq$NH4|_7Zkf$*O#1|2j&LJ!MVk9O1Vh
l(BO!zzMGqNqCil2yqJVt1Ute8@$V4gLkX2!O!|6Dji^I@3*vfLrV8+_`RmbR{69Yj7aMVSMj;(8;wXaPw^SG2Ycu}KKDhJL&W(>
xxJHyke9{5&-^Ng(u=MYlZ}ShuTHQEqnMC?si&b(`oS7#HL3*L>sYfe7=1k$t4L`R%>3}6fzq1GTz#3-ES)eK#qjWeP;&xF!wiKt
1VE2sx>${eMWc-$@|+1tbsZi|fd=g^+$%M(jf-Xm144=BJhVtMAs6A{KcDvYr77{68e7%rHshRhXDR2?76Eb@0$g}_e~}6O!(=G2
-Cj(%NbH>+`lI1PUq5*0PL@vgM}??R70}H6XhS^+BazDZ41boxvgv~DHTWevci~wMp!cTom6$U&eaflZa*kNoJCc_GC<AuYeGvx>
<uaZ^(Q-~2EKkux$1XbNn8(J(Ra5wjN67L@e3ReAXZd;M1UW_Pkh^?#j69S>kv|{CAFXckw$GZfS8$TQh(MXt72bkR14U0x*@hN$
g?hTx+^iJFoX3z$?n0?%3ETaIA+0ocE_x^B9EN%nLg98g&0O{vI^?_o<i&V>xt9@ni-dbB(gYDBzEW;yJq!Wd1&=`zD%hrAXL)R+
y4378JFeADV`V|6Is!&)^hlS)>T|eKl@A*!Xa|#tUe>CIS_VZlX=I(E5*vQd;-MyR=A?D8UxpYi^WehuP{V2lHKe8uA2iCaxejAE
d{_@Mq$4*7r+9u-IK$xs0S%k$VTPCnVTPjfEXc6?@1hLz7{jSJSqCZPz$Q*EW^3f`&v*^qD-nkO9>5S5pjU$nRoWMUg$J+46dvTM
{R>6>DgJ0Mp@Ah-!od$bVX-d#9DFbn9N3X4lkoV^01~=gSX`_8;1ZB94e8;->wtv+`gh@jr<wq?=~s}08aU_{{T+KKINS_4=>G&c
sCTLUI^>|Qp@aT^Cw5Tl7eB=gHvbB4(0U0tX#X!F2XiBiTHHco2Nw!EScDF$942`1S?u7cLJjs&3)RbPlf76`Ohh1uBE#O%k2B~O
nxO;WoX&F>&3xlKGJ|1A7{PaH$A<ybfrtyC*{qhg%yX=R<s(@B&R@#0JL!2Km=3k5QSy~9rNJt6xw)BK3cBxPJCim=`u3s0B9!9G
3yD$bQ0J7ad1ObVFfOOR0<~1do>op7WBCe@<>^{{<ywHHg3R-hymeXxRhDKCVwUcdzl+S3E3MdUnCg*?DSMFev@*@^;5Ee8>%f^t
hF3#0v+ibCq=9}^phu-RLW5EV#MzMD&5B3Vu#uWZ9*%&zH2bLZO^|N@JfXK==zFE!5)X7?CTk_MgwB3Y1A<`yQK&c#=m~lap494F
*_(CpVAryDG)F@Y_+O_cC=~V(CtH*>|5|x~k?UY@Gq2d)?q)%|PS3}E-5jZd#ECo+Ma1YD0OzTCfk~CEcDen|X;*_oJFDQ(Q)rNZ
;{4aofuI@sGd-{2o7ehTNV@@pNcbO^=-IR{PQ5IN^1+myoVu}gzIGLNI1>=S!E79$E2zqDJ+D{Vm8H$_O+NOYXCThC@J*2eZPHaI
VL$TS7+t5yP49Um=j<5>C(3JrasI!F;mle5smQ#=e+`DS|94|J`_E!H`?~aK>dma!zt3=gbzA82dist%SE_0nAS6Y=PeGthFM>dy
<Wn95`lJYiAcjxUu1fK8dYb|T(*}fgDFjJtRP@#*i$k+MMe5xPMb*=&3~)*ga!_a8=|4lA-m-;hE$Y<R)Z8-a^bUHv&v39?goC-2
igjCs2dh^_x7fQPlm5-nQ*8x+nVb*|j~mJNEYfu9u@aHpmx#w6c+=s#`k{IMVF%B`?5#%e=t-v+`T<R*c6Vj=McQVaT{kUs4CFGR
G?P%86q2g!8{|!)`W(0M`WUg9OuZ>A>*X?zq$rN8-EEG2H@zN(n~Pa!>>go}L)fwC^&|#nH$tjA3kj%r$P{w6A<QW$d+HKwA%3}l
)oYrjLqng$oc7y#Ls;xK!rq?fH-fcMB~wM9$E7ifJ-a!9b=w+mj9^Tt@tb&gE)5h?-6+?~K)?esOIT((sD^YgaKQtl8bmkD8Oq|*
;Zvuq+hZs=oSa<UvsieA-H0;sQatj2nE)MidwH9{VkN<{K(okZOk1cTkj3o$y;}@ts#KKkD>k^SEwbeI%30N1A$Kp-P0&C#g{=js
4CtPN_^%)andpWwIo!JlD~-{gp0Q#;Wguv+iCz3|h^JXINS4~g9@AtcYIWIU$qFXP^|6#3Wcci6Gl&W46FIs=939IuB*R3ZJ=Yu@
4d_fBgg9!-xf7k{aZR$kAK1;`wZ*r2aX~roxtksCDeJE?7%K~MY6HGnV*|z;>3+outZ!q3bwkxEM>J;`3DPq*wE9BjVU745#Xa8J
_LLpxq}5TId_S7t%Jn343AZnrUeq0OMRV2R1zNJOOnOk|R<772EwB{IdMqJkhmhDc@jDvG7UE(lE}rDYMSecuOox^8UTASfCb)bE
u3PGKh_)pIg3{8(@dnT{Gx2j&ioP6_=^Fk&f<GO%2SU`L3)rCz#|j}1)x3BT0|s)kf3zD!u*{*M2p{PPl6H&YR@THMOQ8!<dKRtM
x;L<o899E1r|A@ue)r-owFRUFLMiDbys)-owJ-zI;p>J2;BP2ofZwX%x(^Tr%ZH?lf<G3NU?1}xbW`X$4?DLrjU%GrLZ+$)0-Mn%
0&&c!P8{2+b96KZQ=zJ5`znO#QSybrikcmnjzzej6ib!DZWbDjC$p;<Uh{Js{JEOP(2wLk>!xzTdg%e3aKWf$gOMALW7`<-i)=iK
Z6xB^c&T>kG38inYjGUuWXXj6LS6VWf<b!O7GEiIlGmfq>nBsC=o3tu=wUh!13~mWuV9ZPcrYh}eS*3P0p=8Ue245DpjBc;JP)%Q
y#VQuCdaCgP&smM>7|mnV+Z@Ke6z>FD>LrokGnq|%=-uaz~gLs=feyvtBYv<Q8GV%#jXG)g8R6z)Ud6AeeP78+5)QUm~mA~0ban`
J-+xLRksb#D){>*bHL(f^0qqU4-{o+^!f(-7uc!KfLbk_%uxWpL1Y?Z6{~^D2@-t^{vK<L71^pTE?{{Zs&4?T`vQ<T=z^|i$&aoD
Trja2x2&pMii9H^nLpb};pbAWR4G5OX7zGRk}VxS=d|0Exz~IpfPUpnjM5%97)WoNjFnz!k>}-_0X4KW%CWO@gM`)<<V=tXEmt&Z
yKs>Qb8~mik!7mt>a_{wDth)KIm2cb%Ry>lGQ;I@7MxoBVptSuzJbUyh8t$B!*{pD5+#ICD;_p8`$U01^vE<oy8nrC64Oct3<_iJ
>C}sl>rwI8;!mBO2yZ=PKOuy^N>7eO22S7D-yoSMAoG+usv##qruTd^uZx)N++FyyXYRtErD=-JDESKqj6orX0w@7h19b^Iz2Y$l
R_1=fdm!42!+wce9<f>pa0z;Out|2tH_wu&d0WN$ZNa`8L+!V{!z9r{Egxm)>tWI6Kf#`(`jdv1Bx$$gzmjGg(!H0R88Ut5J~36F
OY0o&ckw$_6FjmTmT?|6dw$~5Oj1GFT!M6h{UntAUJV82z|k-n+5Aoue=`XiGn(@C^@^b=BlFbDBZ8Ud(4qLHJflKngnqCMVK+_T
Dc$A>o4vNx7!4H9)1!nrsz4_K|7i4cWt3U-bNA9Vy*Y919PJ%*x<1bv$r19|2;S&;QW32&QIz(LiV@_^fmd*L%=yJ`{!?0*xkA4R
h7EbVkqV)Ac=JY?=92o@Dkk$r#9+0z7Uief*jwJ{ZT*lm1{f`v)vzuV;`tCEpphYdW>NSBtt-}f<)7#W5|HWXpTcrCdaxtL>0p}a
@;)JC640AW)8z{x^!Sr*FbRJui-j(^%r(v?+`rH98R2aS&JI7~T%L<7Xcjb06uwg?>Ai}n)_><qT9E4<#H$`%zCEWW%7@|FaH8-M
i#3-7F7S##<A%V6y(S6Y4)~hO0T<6-4Y(*=4EVymfD5Dl7HdHK`U6_BvvwO?Dt>vgyY}Xc;<qXPfA~0MX)4VxQ%2Hsc+lUY%s%pl
LblwMD^l0Exr2`V(AxxbSgy8t*2!NzwBOMY=jtUG#M~NnC#NE<jf_C}O=rF=e?0nhcK+S4YONNij({(}++3d>w;Yw@Q|spR^4K{)
`*e0wwhR6wbU#O@oR)`(KZXz+A6&?;fyjV~=}BwBfSV?!k2Dl0=X&$SFYnpid_7+Sw9MzIrB)3S-MHN?ROwo^^d(Y%D`L_(84UfQ
OGkW)+#zE*qbaD9WDCRFDe&N_8u^2<+N}gJdoa4=z*ApOnht2IGEFb+Kr_8jrDo6d)^2_4+V-R!wA5XPLMa5F$$F?fduYR%b4Sm-
AGPB{l=--!$s5YeaX9J^1hAC>xk<`fp;`u0io${2=Q9Kw;m7Il2(L)BS~o`r3Sg0hveDe%!-_Wn6|(?u*%o`b`yGqe7HSJ#%Yty7
4NSjlSBO*-&tDMy!>cs}wB@3**jQAa@T!iu@>F?Jx7%=4@-rKANL42pi#A_FA=~QO7yLYBz1mi{!{A#?x3TPioU68rH&(%{O0yN_
DVJ>*@v!>#CB8=~2>p9tzaUv6Gd;p?A;HaWEDxY5%~Ak+;q+E7*v)WX!W8$^Mwzc@B9_b7Dy{wtwK5R5bTv!yo{-ldY!%v*p=QF3
dO?B+Jx6H=Q81$$9UlWP8A){$W-<yw6{l{m%nndxT1Szti27mmHk{%|MD@oV^B~b6q#5eaB<2eyvq>z0Z~w}LBnB4t#fwS)>Ngs5
cL@Le7n3NOD;JZj#XA2t+)wh;Pnkjuf9+$Yg$)13=S*Ki>6s6j>Z>=_O`Vh01%0RVnLAi+PFt7lR{9mp)tgvuPTQ@Px@6_5eTg5(
Jp0;8Z(C8+F574S0t!&h`^#^raJ2E8oQxn(KeL(<{do5Arq#M|RD~~pzaX4+`||SRwet}_?x}7fqZ>~6o2o0<x-eo`B~<srq=;et
RnN0yr~!5D3zN3|H(h=5*C6%?VgB>~0=(I+y8
"""
BUNDLE_PIN=[32721, '10760589c3915c017e0350935853cfa5f9bb5d142ebb95d837160463dc784c6f']
SOURCE_PINS={'bridge.py': [11790, 'd90a69aeb7bfc85264a0007daa6f2a7d8c2752aed84d8b0f67f9db8eda2b7422'], 'section_pairs_literal.py': [15228, 'ea787508fac8b207ee3251a0587b83a8e797cc7283639e8d2fc9d7b2eabfe320'], 'repair_parent.py': [2041, 'e89cc4a5c4d1ced5611fcf671c8983b2a1b645fdde3aa2a7071f27e49045cfe1'], 'audit_parent.py': [2908, '60d1abab89d3b7a1823bf72ba2856971cab578d21d3cc10c719dcd0282bf1630']}
OUTPUT_PINS={'bridge.json': [36293, '88a47c551e64feb056f6a3e9d6e8d297c60d25490f553dcf63f56e359170bab8'], 'section_pairs_reconciled.py': [15645, 'e0fb8e0cb37d3aff75d8b2b9ea8a892fe1de8bc6b84f7a070fdd2bbc8680920a'], 'section_pairs_reconciled.json': [3799163, '5ffb07a2c8fb95e2d128fc45d10a902f47896094cf55bd55d2338d8a8923c975'], 'parent_audit.json': [6928, 'cf97d2d2960a26871e6e2b28f79ba77adaf44e308ed278a2a2b2880f384ac254']}
def verify(b,p):
 assert [len(b),hashlib.sha256(b).hexdigest()]==p
blob=zlib.decompress(base64.b85decode(''.join(DATA.split())))
verify(blob,BUNDLE_PIN)
for name,text in json.loads(blob).items():
 b=text.encode();verify(b,SOURCE_PINS[name]);p=ROOT/name
 if p.exists():assert p.read_bytes()==b
 else:p.write_bytes(b)
assert sys.argv[1:] in (['sources'],['build'],['check'])
mode=sys.argv[1]
if mode!='sources':
 def run(*args):subprocess.run([sys.executable,'-S',*args],cwd=ROOT,check=True)
 run('bridge.py',mode)
 # repair_parent.py regenerates AND checks the corrected report; it never
 # executes the intentionally preserved uncorrected literal source.
 run('repair_parent.py')
 run('audit_parent.py')
 for name,pin in OUTPUT_PINS.items():verify((ROOT/name).read_bytes(),pin)
for name,pin in SOURCE_PINS.items():print(name,*pin)
print('STRESS_RIM_BRIDGE_AND_LITERAL_PARENT_RECONCILIATION_COLD_PASS')
```

## 8. Непокрытый остаток и продолжение

Главный новый механизм — не усиление независимой U-оценки, а **покрытие её возможного провала другой физической альтернативой при тех же v,y и том же COM**. Положительный дефицит R²-E больше не означает автоматически открытый метрический сектор: часть таких дефицитов поглощается условием (L).

Для произвольной остающейся формы ещё не доказано, что найдётся грань B, центральная плоскость и stresses, удовлетворяющие этому мосту. В частности, открыты большие дефициты, неблагоприятное расположение beta_lambda относительно настоящего края, различные горизонтальные G вне покрытого сектора и формы, где ни одно удобное настоящее внешнее ребро не попадает в требуемую нормовую область. Предполагаемая единственная S может находиться на любой другой грани; выбор B в общей теореме не является назначением S-корня, но её условия не автоматичны.

Самостоятельный трёхопорный минимакс точно исчерпывает прежний одноплоскостный all-shear U-тест, **не весь совместный S/U-механизм**. Для продолжения полезнее оптимизировать stress вместе с его центром v_lambda и настоящим реберным witness, затем совмещать такие условия для нескольких истинных плоскостей одной формы, чем просто увеличивать число отдельно проверенных лучей. При проективном изменении формы все COM, стороны сечений и поляры должны вычисляться заново; ошибочные родительские alpha=1/2-контроли не дают разрешения на перенос знаков высоты.

Коррекции раздела6 должны сопровождать дальнейшее использование ACTUAL_SECTION_PAIR_SHEAR_CONES_V1: непрерывные исключения сохранены, но прежняя демонстрация коридора, below-COM фикстуры и старые source/output pins заменены конкретным воспроизводимым аудитом. Новый result не обновляет сам журнал.

**Глобальный эффект:** дополнительный доказанный совместный непрерывный сектор внутри двухапексного E17; никакого общего E17-исключения, нового достигающего тела или законной registry-delta. Принятый интервал остаётся **34<=C_min<=622**.

Дополнительные копии: [полный recovery-wrapper](sandbox:/mnt/data/section_bridge/recover_bridge.py), [новый exact-отчёт](sandbox:/mnt/data/section_bridge/bridge.json), [исправленный полный родительский отчёт](sandbox:/mnt/data/section_bridge/section_pairs_reconciled.json), [независимый аудит конфликтовавших контролей](sandbox:/mnt/data/section_bridge/parent_audit.json). Буквальная капсула выше достаточна без этих ссылок.
