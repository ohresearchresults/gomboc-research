# minimum-0166

Historical AI scientific report · saved 2026-09-21 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

---

# B_ROOT_CORNER_SECOND_JET_V2

## 1. Главный результат продолжения

В оставшемся отрицательно-якорном секторе получена оценка настоящего T, существенно усиливающая предыдущий результат: ограничение b/mu >= 16/9 больше не требуется. Закрыт непрерывный сектор настоящего корневого угла при B, включая защищённые пятиугольники с близкими, но не обязательно равными c,d, произвольные остальные настоящие грани и положительно-ell вспомогательные вершины вне этого угла.

Пусть P — полигедральный локальный максимум ПОЛНОЙ совместной отмеченной задачи, a>b>0, c,d>0. Все моменты ниже принадлежат одному настоящему равномерному телу. Обозначим

    g=(u,v,z_g), p=u+v, mu=E/V, t=6V,
    h_x=a+b+c, h_y=a+b+d, Delta=h_x h_y,
    hbar=r/p=(h_x u+h_y v)/p,
    beta=hbar(h_x+h_y)/(2 Delta),
    zeta=[u G(C)+v G(D)]/(r p).

**Корневой угол B** означает: B — простая настоящая вершина, инцидентная Fx, Fy и единственной свободной настоящей грани BUV; эта грань — треугольник, содержит из канонических отметок только B, а U принадлежит Fx intersect F0 и V принадлежит Fy intersect F0. Остальные вершины и грани P не ограничиваются этим определением.

Доказаны следующие два вывода, использующие принятый общий моментный закон 4p<=t+1:

    beta<=1, zeta<=0              ==> T<101/50=2.02;
    beta<=1001/1000, zeta<=1/1000 ==> T<203/100=2.03.

Первый вывод имеет аналитическую редукцию и полный точный сертификат из 70 замкнутых прямоугольников; второй — из 50. Их общий объём точной проверки составляет 1800 строго положительных коэффициентов Бернштейна. Это покрытие непрерывных областей необходимых условий настоящего тела, не численная сетка и не перечисление реализованных тел.

**Следствие для назначенного отрицательного сектора.** Если G(C),G(D)<=0 и обе защищённые грани — настоящие пятиугольники, корневой угол B получается автоматически. Поэтому:

    (c-d)(h_x u-h_y v)<=0 ==> T<2.02.

В частности, c=d даёт T<2.02 без условия на b/mu и без геометрической симметрии тела. Кроме того,

    |c-d| <= min(h_x,h_y)/500 ==> T<2.03.

Последнее — настоящий непрерывный сектор неравных положительных концов, а не только сечение c=d. Те же выводы действуют для защищённых форм 5/4, 4/5 и 4/4, когда оба настоящих соседа B на координатных гранях корневые.

**Смешанные отметки.** Основная теорема требует не отдельных знаков G(C),G(D), а указанной настоящей величины zeta. Поэтому второй вывод применим также при положительной избыточной D и отрицательной C, если корневой угол B действительно установлен, beta<=1001/1000 и zeta<=1/1000. Эти условия не объявляются автоматическими для избыточной отметки.

Есть и самостоятельный результат, НЕ использующий общий закон 4p<=t+1: при корневом угле B, beta<=1 и b>=mu,

    T < 81/40 + (27/20) max(zeta,0).

Следовательно zeta<=1/90 в этом секторе достаточно для T<51/25. При двух неположительных отметках получается T<81/40=2.025.

Ни весь отрицательно-якорный сектор, ни все защищённые четырёхугольники, ни механический слой 10/17/9 не закрыты.

## 2. Прочитанный контекст, зависимости и доказательный статус

Неизменные исходные журнал и три аналитических материала остаются доступными в этой беседе и используются после полного чтения в предыдущем ходе. Новые переданные `expanded_patch_b_fan_audit.py` и `expanded_patch_b_fan_audit.json` прочитаны полностью через EOF. Их фактические идентичности подтверждены:

    expanded_patch_b_fan_audit.py
    6973 bytes
    SHA256 68bfcdf161687658b3b9b9d29cd92507d4888dbc67f13edf0727dc6be1eab401

    expanded_patch_b_fan_audit.json
    5085 bytes
    SHA256 f2c48b76664addf70c34c58db6fafa270b8df0b637ce8b64004081a5d664940a

Родитель нового вывода — предыдущий полный результат `EXPANDED_PATCH_B_FAN_AND_ROOT_FLOOR_V1`; новый код ниже не импортирует его исходник и не требует его файла данных.

Использованы принятые утверждения о положительности G на вспомогательных настоящих вершинах и о жёстком настоящем треугольнике с единственной канонической отметкой. Это условия максимума по всем допустимым телам, не только внутри одной решётки граней. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

Для применения к пятиугольникам используется принятая V2: вспомогательное ребро неположительно отмеченного защищённого пятиугольника корневое. :contentReference[oaicite:2]{index=2} Опорная реакция движения отметки берётся в её полной совместной области. :contentReference[oaicite:3]{index=3}

Единственный дополнительно использованный принятый моментный результат —

    (J)  4(u+v)<=6V+1.

Его точное утверждение присутствует в приложенном журнале как принятый actual joint-mass input; его первоначальное полное доказательство не находится в трёх отдельных аналитических заметках и здесь заново не проверялось. :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5} Ниже отдельно доказан перенос (J) из proper-класса в закрытый отмеченный класс. Таким образом основные оценки можно независимо читать как теоремы с дополнительной явно указанной гипотезой (J); в принятой научной базе журнала эта гипотеза уже является общим законом. Самостоятельная оценка 81/40+(27/20)max(zeta,0), геометрия корневого угла, второй B-jet и точное снятие угла не используют (J).

Новые аналитические доказательства приведены ниже. Авторски исполненная точная проверка удостоверяет алгебру, полное покрытие двух непрерывных квадратов, настоящие максимальные грани контрольных тел и их общие объёмные моменты двумя положительными веерами. Она не является формализацией всей вариационной допустимости. Численное исследование скалярной релаксации не используется как доказательство; его полезная граница сохранена точным формальным контролем в разделе 9. Механические S/U/H контрольных тел не вычислялись.

## 3. Геометрический вход: какие защищённые грани дают корневой угол

Сохраняются исходные обозначения

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    alpha=a-b>0,
    ell=a+(d-a)x+(c-a)y-alpha z,
    n=h_x x+h_y y,
    q=N/E, r=N/V, G=n-r-q ell.

### 3.1. Ориентация расширения и свободные грани B

При G(C)<=0 полная реакция отметки даёт на Fx

    (b+2c)(y-1)-alpha z<=0.

Каждая вспомогательная вершина (0,y,z) этой грани имеет z>0 и y+z>1. Действительно, при z<=0 реакция даёт y<=1, и

    G=(1-y)G(A)+yG(C)+q alpha z<=0.

При z<=1-y та же реакция сначала даёт y<=1, после чего

    G=(1-y)G(B)+yG(C)+q alpha[z-(1-y)]<=0.

Оба вывода противоречат строгой положительности вспомогательной вершины. Поэтому AC — настоящее ребро, а при расширенной Fx отрезок BC не является ребром. Вместе с V2 остаются именно порядки A,B,U,C или A,B,U,V,C. Отражённое утверждение действует на Fy.

Если обе отметки неположительны и обе грани расширены, всякая свободная грань через B содержит только B: совместное наличие C или D сделало бы BC или BD настоящим ребром пересечения с координатной гранью. Пара AB уже принадлежит двум защищённым граням.

Тот же вывод о гранях B действует при расширенной неположительной Fx и избыточной D: свободная грань через B,D содержала бы минимальное настоящее ребро точки D и вместе с B имела бы двумерное пересечение с Fy. Это невозможно для двух различных максимальных граней.

Следовательно все свободные грани B в этих случаях — настоящие треугольники; все их вспомогательные вершины имеют общий уровень

    L=(r+qb)/3,  G=L,
    K=r+L=(4r+qb)/3.

На всём P неотрицательна аффинная функция

    H_B=G-L+(4L/b)ell=n-K+(K/b)ell.                 (3.1)

Короткое доказательство из родительского результата: H_B(B)=0, H_B(A)=alpha K/b>0, а на каждом другом настоящем соседе B значение равно (4L/b)ell>=0. Настоящие рёбра порождают касательный конус B. Поэтому H_B>=0 на всём P.

### 3.2. Новый локальный вывод из одного пятиугольника

Пусть Fx имеет порядок A,B,U,V,C, U,V корневые, и все свободные грани B содержат только B. Пусть US — другое настоящее ребро корня при U, отличное от UV. Тогда его вторая грань обязательно есть настоящий треугольник BUS. В частности, минимальное G-ребро корня, начинающееся при U, принадлежит свободной грани B.

Доказательство. Вторая грань F ребра US не может содержать A или C: её пересечение с Fx тогда содержало бы U и A либо C, тогда как единственные настоящие рёбра Fx при U — BU и UV. Если F содержит B, одноякорная жёсткость даёт G(S)=G(U)=L. Если F не содержит B, единственная возможная каноническая отметка — D, и та же жёсткость снова даёт G(S)=L. Поэтому H_B равна нулю на B,U,S. Эти точки неколлинеарны; H_B=0 есть настоящая свободная грань через B, а значит ровно BUS. У настоящего ребра US уже есть две грани, F0 и BUS, поэтому F=BUS. Случай отдельной грани DUS исключён.

**Граница вывода:** из одного пятиугольника не установлено S∈Fy. Нельзя объявлять B простой лишь потому, что у неё найдены два корневых соседа. Это дало бы необоснованное расширение предыдущего результата.

Если оба координатных соседа B корневые, они лежат на разных координатных осях корня. Плоскость H_B=0 содержит их вместе с B и является настоящим треугольником. Два его ребра при B вместе с Fx,Fy замыкают треугольную фигуру вершины; B простая. В частности, это всегда происходит при двух неположительно отмеченных защищённых пятиугольниках. Аналогично подходят формы 5/4, 4/5 и 4/4 с корневой единственной вспомогательной вершиной соответствующего четырёхугольника.

Корневое ребро UV этого B-треугольника минимизирует, а не максимизирует G на F0. Прежний тест максимального G-ребра сюда не переносится. :contentReference[oaicite:6]{index=6}

## 4. Точный второй совместный jet простого B-угла

Теперь предполагается корневой угол из раздела 1. Поскольку n(U)=n(V)=K,

    U_y=K/h_y, V_x=K/h_x,
    W=Vol(conv(A,B,U,V))=K^2/(6 Delta).

Обозначим

    S0=int_P(x+y)=pV,
    S_B=(WK/4)(1/h_x+1/h_y).

Сдвинем физическую B в B_delta=(0,0,1+delta), оставив все остальные вершины и физическую ell неизменными. Малые параметры обоих знаков допустимы: свободная грань BUV остаётся одним настоящим треугольником с фиксированными U,V; защищённые плоскости остаются прежними; остальные настоящие опоры имеют строгий запас относительно B. Положительность канонических значений ell сохраняется.

Настоящие физические интегралы имеют точные формулы

    V_phys(delta)=V+W delta,
    E_phys(delta)=E+(bW/2)delta-(alpha W/4)delta^2,
    N_phys(delta)=N+(KW/2)delta,
    S_phys(delta)=pV+S_B delta.                         (4.1)

Это формулы одного положительного A-веера тела, а не свободно задаваемые приращения.

После аффинного восстановления рамки z'=z/(1+delta) новый канонический конец равен b-alpha delta, числитель в физических координатах равен n-alpha delta(x+y), а якобиан равен 1/(1+delta). Поэтому

    T_delta=(1+delta)[N_phys(delta)-alpha delta S_phys(delta)]
            /[6 V_phys(delta) E_phys(delta)].          (4.2)

Положим

    F(delta)=(1+delta)[N+(KW/2)delta-alpha delta(pV+S_B delta)]
             -(N/(VE))(V+W delta)
              [E+(bW/2)delta-(alpha W/4)delta^2].

Знак F(delta) — точный знак T_delta-T. В полном локальном максимуме F'(0)=0, а коэффициент delta^2 неположителен. Первая реакция даёт

    W/V=(r-alpha p)/L.                                (4.3)

Для второй удобно ввести безразмерные величины

    eta=b/mu,
    A0=alpha/mu,
    chi=(c u+d v)/(mu p),
    H=2eta+chi,
    h=hbar/mu=A0+H,
    x=A0/h,
    w=W/V=3H/[h(1+eta)].

Точный нормированный коэффициент второго порядка равен

    C2=F_2/(rV)
      =w^2(2-eta)^2/18-x+A0 w/4
        +w(4+eta)x(1-beta)/6 <=0.                     (4.4)

В (4.4) используется полная совместная вариация рамки. При фиксированной ell в уже восстановленных канонических координатах это условие само по себе не лицензировано.

### 4.1. Новое ограничение средней высоты из H_B

Из (3.1)

    H_B(g)=r(4-eta^2)/(3eta)>0,
    H_B(A)=r A0(4+eta)/(3eta).

Поэтому 0<eta<2. Конирование настоящего P из A для неотрицательной аффинной H_B даёт H_B(A)<=4H_B(g), откуда

    A0<=U(eta):=4(4-eta^2)/(4+eta).                   (4.5)

Здесь не использована корневая стационарность и не выбрана новая плотность.

### 4.2. Контроль асимметрии второго jet

Пусть beta<=1+epsilon, epsilon>=0. Из (4.4) следует

    2H^2(2-eta)^2
      <= A0 h(1+eta)
         [4(1+eta)-3H+2epsilon H(4+eta)/h].           (4.6)

Поскольку A0>0, H>0, eta<2 и H/h<1, получаем строгий необходимый предел

    H<4(1+eta)/3+4epsilon,
    chi<(4-2eta)/3+4epsilon.                          (4.7)

Коэффициенты 2epsilon в (4.6) и 4epsilon в (4.7) существенны; точный проверитель явно проверяет этот множитель.

## 5. Связь с общими настоящими объёмными моментами

Определим

    hcross=h_x+h_y-hbar,
    kappa=Delta/hbar^2,
    lambda=Delta/(hbar hcross),
    D_eta=(1+eta)(4+eta)^2.

Непосредственная алгебра даёт

    hbar hcross=Delta+(h_x-h_y)^2 u v/p^2,
    0<lambda<=1.                                    (5.1)

Кроме того,

    beta<=1+epsilon ==> kappa>=(1+epsilon)^(-2),       (5.2)

поскольку hbar не превосходит (1+epsilon), умноженного на гармоническое среднее h_x,h_y, а гармоническое среднее не превосходит геометрического.

Совмещение НАСТОЯЩЕГО W=K^2/(6Delta) с (4.3) даёт точное равенство

    p=27 kappa H/(T D_eta).                           (5.3)

### 5.1. Отметки и координатные пирамиды

Из определения zeta имеем точное равенство

    hcross=r(1+chi+zeta).

Следовательно

    T=27 lambda H(1+chi+zeta)/D_eta.                 (5.4)

Если zeta<=zeta0, zeta0>=0, то

    T D_eta<=27H(1+chi+zeta0).                        (5.5)

При G(C),G(D)<=0 автоматически zeta<=0. Но (5.5) сохраняет смысл и для смешанных знаков, включая избыточную положительную отметку.

Конирование из C и D, с сохранением ПОЛНЫХ защищённых граней, даёт

    t(4mu-c)>h_y,  t(4mu-d)>h_x.                     (5.6)

Строгость обеспечивается действительным расширением соответствующих защищённых граней и положительностью ell почти всюду на добавленной площади. Взвешивая эти неравенства настоящими u,v и используя (5.3), получаем

    T^2 D_eta<27 lambda H(4-chi)<=27H(4-chi).         (5.7)

Конирование из D для x и из C для y также даёт u,v>=1/4, то есть p>=1/2.

### 5.2. Принятый совместный массовый закон и его отмеченная область

Используется (J): 4p<=t+1. Его перенос с proper-тел на рассматриваемые увеличенные patches не требует предполагать, что такая грань сама является каноническим треугольником. Выбираем q0∈relint F0 с x(q0),y(q0)>0 и берём

    P_epsilon=conv(T0,(1-epsilon)P+epsilon q0).

Тогда координатные максимальные грани P_epsilon — ровно ABC и ABD, корень имеет положительную площадь, а V,u,v сходятся к настоящим моментам P. Поэтому нестрогий закон (J) проходит к пределу. Геометрическая допустимость именно этого восстановления proper-пары дана и в приложенном материале. :contentReference[oaicite:7]{index=7}

Из (J), t=h p/T, (4.5) и (5.3) следует

    27 kappa H[4T-U(eta)-H]<=T^2 D_eta.              (5.8)

Для сведения всего T>=tau к одной tau недостаточно просто подставить порог в произвольное квадратное выражение. Здесь монотонность доказывается отдельно. Положим

    j_k(s)=s^2 D_eta-27 kappa H[4s-U(eta)-H].

На tau<=s<=T имеем p_s=27kappa H/(sD_eta)>=p_T>=1/2 и

    j_k'(s)=2sD_eta(1-2p_s)<=0.

Поэтому j_k(tau)>=j_k(T)>=0. Используя (5.2), получаем необходимое условие

    27H[4tau-U(eta)-H]<=(1+epsilon)^2 tau^2 D_eta.    (5.9)

Если квадратная скобка отрицательна, (5.9) верно автоматически; если неотрицательна, применяется нижняя граница kappa. Знак не теряется.

## 6. Полное точное исключение двух непрерывных областей

Предположим T>=tau, beta<=1+epsilon и zeta<=zeta0. Из (4.7), (5.5), (5.7), (5.9) следует

    0<eta<2,
    0<chi<(4-2eta)/3+4epsilon,
    J<=0, Epoly<0, Npoly<=0,

где

    H=2eta+chi, D_eta=(1+eta)(4+eta)^2,

    J=27H[(4tau-H)(eta+4)-4(4-eta^2)]
      -(1+epsilon)^2 tau^2 D_eta(eta+4),

    Epoly=tau^2 D_eta-27H(4-chi),

    Npoly=tau D_eta-27H(1+chi+zeta0).                 (6.1)

J — положительно умноженный числитель (5.9). Здесь не выбираются новые моменты тела; это необходимая релаксация уже доказанных настоящих реакций.

Введём

    eta=2u,
    chi=[(4-2eta)/3+4epsilon]v,
    (u,v)∈[0,1]^2.

Каждый из трёх полиномов имеет степень не более (4,2). Проверитель строит полное двоичное разбиение квадрата, попеременно деля u и v пополам. В каждой конечной ячейке один из J,Epoly,Npoly имеет все 15 коэффициентов Бернштейна строго положительными. Это противоречит необходимым знакам из (6.1).

Точные результаты:

| tau | epsilon | zeta0 | Ячеек | Глубина | Победители J/Epoly/Npoly | Положительных коэффициентов |
|---|---|---|---:|---:|---|---:|
| 101/50 | 0 | 0 | 70 | 20 | 35/17/18 | 1050 |
| 203/100 | 1/1000 | 1/1000 | 50 | 16 | 25/8/17 | 750 |

Минимальные положительные коэффициенты соответственно

    41363/104857600,
    689575417/13107200000.

Второй независимый способ в коде непосредственно подставляет каждую dyadic-ячейку в исходные степенные коэффициенты, преобразует их в базис Бернштейна и сверяет с результатом de Casteljau. Отдельно проверены полнота префиксного двоичного дерева, отсутствие перекрывающихся внутренних ячеек и точное равенство суммы 2^(-depth) единице. Не используется отсечение ячеек по предполагаемой физической нереализуемости.

### 6.1. Удобные геометрические следствия

Тождество

    beta-1=(c-d)(h_x u-h_y v)/(2 Delta p)

даёт указанный моментно-геометрический сектор beta<=1.

Для ограничения только на концы пусть M=max(h_x,h_y), m0=min(h_x,h_y). Тогда

    beta<=M(M+m0)/(2Mm0)=1+(M-m0)/(2m0).

Следовательно |c-d|<=m0/500 достаточно для beta<=1001/1000. При двух неположительных отметках zeta<=0, и второй сертификат применяется с запасом по zeta0.

Никакая симметрия P, отсутствие отрицательных z, отсутствие положительно-ell вспомогательных вершин вдали от B или ограничение числа свободных многоугольников здесь не предполагаются.

## 7. Самостоятельная аналитическая оценка без закона (J)

Этот результат полезен, когда не хочется использовать принятый совместный массовый вход или когда положительная другая отметка даёт заметный дефект zeta.

Пусть beta<=1, 1<=eta<2. Из (4.6) при epsilon=0 и (4.5) необходимо

    F(A0,H)=A0(A0+H)(1+eta)[4(1+eta)-3H]
             -2H^2(2-eta)^2 >=0,
    A0<=U(eta).

Докажем H<(2+3eta)/2. Если H не меньше этого значения, функция F(U(eta),H) строго убывает по H: её производная имеет верхнюю оценку с множителем

    4(1+eta)-6H <= -2-5eta<0.

При H0=(2+3eta)/2 точное значение равно

    F(U(eta),H0)
      =-(eta-2)^2 P(eta)/[2(eta+4)^2],

    P(eta)=19eta^4+86eta^3+100eta^2-72eta-96.

На eta>=1 положительность P очевидна из

    P(1+y)=19y^4+162y^3+472y^2+462y+37.

Это противоречит F(A0,H)>=0, поскольку в необходимой области положительной скобки F возрастает по A0. Итак,

    chi<1-eta/2.

Из (5.4), lambda<=1 теперь следует

    T<R(eta)+C(eta) max(zeta,0),

    R(eta)=27(2+3eta)(4-eta)/[4(1+eta)(4+eta)^2],
    C(eta)=27(2+3eta)/[2(1+eta)(4+eta)^2].

Нужные точные разности:

    81/40-R(eta)
      =27(eta-1)(3eta^2+60eta+32)/[40(1+eta)(4+eta)^2]>=0,

    27/20-C(eta)
      =27(eta-1)(eta^2+10eta+4)/[20(1+eta)(4+eta)^2]>=0.

Получается заявленная строгая оценка 81/40+(27/20)max(zeta,0). При zeta<=1/90 правая часть не больше 51/25.

Этот вывод использует настоящую геометрию B, второй совместный jet, конусную оценку неотрицательной H_B и определение zeta. Полные корневые моментные реакции и (J) ему не нужны.

## 8. Снятие корневого B-угла: точная настоящая операция

Есть дополнительный геометрический результат, пригодный для продолжения независимо от оценки T.

Положим

    O=(0,0,a/alpha), ell(O)=0.

В корневом угле B тело

    Q=conv(P,O)

получается добавлением РОВНО тетраэдра OBUV. Никаких дополнительных видимых граней нет.

Доказательство удобно записать в аффинных координатах тетраэдра OBUV:

    lambda_B=ell/b,
    lambda_U=h_y y/K,
    lambda_V=h_x x/K,
    lambda_O=1-lambda_B-lambda_U-lambda_V.

На P первые три координаты неотрицательны, а lambda_O<=0 по H_B>=0. Пусть f>=0 — слабина любой другой настоящей опоры, отличной от BUV. Если f(O)<0, то на P с lambda_O<0 имеем f>0, поскольку f(B),f(U),f(V)>=0. Тогда нулевая грань f могла бы лежать только в BUV, что противоречит её отличию как настоящей максимальной грани. Значит O удовлетворяет всем остальным опорам. Область lambda_O>=0 внутри трёх защищённых полупространств — ровно OBUV, что доказывает утверждение.

Если vcap=Vol(OBUV), то

    vcap=(b/alpha)W,
    V_Q=V+vcap,
    E_Q=E+b vcap/4,
    N_Q=N+K vcap/2,
    S_Q=pV+(K vcap/4)(1/h_x+1/h_y).                 (8.1)

N_Q здесь по-прежнему использует исходный n. При новой канонической B=O, после восстановления рамки, конец b становится нулём и правильный след равен

    T_Q,new=(a/alpha)(N_Q-b S_Q)/(6V_Q E_Q).         (8.2)

Из (8.2) не утверждается универсальная монотонность относительно T(P). Это также НЕ предыдущая замена ell на H_B при фиксированном теле: здесь меняется настоящее тело и каноническая рамка.

### Новый точный настоящий преемник родительского контроля

Исходное тело остаётся буквальным родителем

    P0={x,y,z>=0; z<=1; x+y+z<=2; z>=3(x+y-1)},
    ell=1-(x+y+z)/2.

Постоянный порядок его восьми вершин и все циклы граней полностью включены в исходник ниже. Новый преемник заменяет только физическую B на

    B_delta=(0,0,1+delta), delta=1/1000,

то есть заменяет одну целую верхнюю опору на

    z<=1+delta-delta(x+y).

Все остальные семь вершин остаются прежними. После восстановления z'=z/(1+delta) канонические значения ell равны

    (a,b,c,d)=(1,999/2000,1/2,1/2).

Тело имеет настоящие 8/12/6 и две защищённые пятиугольные грани. Его физические интегралы для старой физической ell и старого 2(x+y):

    V_phys=7627/12000,
    E_phys=11064499/48000000,
    N_phys,old=46133/48000.

Правильный новый отмеченный след с изменившимся числителем и якобианом равен

    T_child=184670352867/168777867746,
    T_child-T_parent=318912520077/607431546017854>0,
    T_parent=3936/3599.

Все вспомогательные вершины положительны по G, обе G(C),G(D) отрицательны, опорные реакции отметок выполнены. Однако это не стационарные тела. Уже у родителя

    G(B)+3G(U)=-7680/3599 !=0.

Поэтому они не являются контрпримером к новым оценкам полного максимума.

Для этого же родителя операция снятия угла имеет геометрический уровень K_geo=2; он НЕ отождествляется с K из стационарного уравнения. Получается настоящее тело 6/9/5 с вершинами

    A, O=(0,0,2), C, D,
    (0,5/4,3/4), (5/4,0,3/4).

Его физические интегралы равны

    V_Q=77/96, E_Q=193/768, N_Q,old=433/384,

а правильный след после новой рамки с b=0 равен 20784/14861. Старые две нижние вершины корня становятся избыточными, поэтому в аудите заново восстановлены настоящие максимальные грани, а не сохранена старая решётка по имени.

Это сохранённые невыигрывающие настоящие конструкции. Их механические S/U/H и слабые пакеты не заявляются.

## 9. Сохранённая граница метода: почему три полинома пока не дают T<2

У трёхполиномиальной релаксации, использованной в разделе 6, при пороге T=2 есть точный формальный контроль:

    mu=1, eta=1/20, chi=2/3, A0=197/50,
    H=23/30, h=353/75,
    p=9200/15309, t=64952/45927,
    beta=1, zeta=-73/27600.

Он удовлетворяет строгим необходимым остаткам

    4(1+eta)-3H                 =19/10,
    U(eta)-A0                  =11/1350,
    p-1/2                      =3091/30618,
    p(1+chi)-1                 =73/45927,
    p(4-chi)-T                 =146/45927,
    t-4p+1                     =479/45927.

Это НЕ тело и НЕ доказательство существования стационарного максимума с T=2. Более того, оно нарушает настоящий корнево-объёмный бюджет предыдущего результата. При

    w=3H/[h(1+eta)],
    rho0=(h-3)^2/[9h(1-1/(3p))]

получаем

    1-w-(A0+eta)rho0
      =-185591543/2277829575<0.

Таким образом именно восстановление полной связи с объёмом корневой пирамиды — содержательное следующее усиление, а не дальнейшее повторение только трёх новых скалярных условий. Контроль сохранён в исходнике и полном JSON как формальный, с явным провалом настоящего корневого бюджета.

## 10. Оставшиеся препятствия и следующий полезный шаг

Для двух защищённых пятиугольников с G(C),G(D)<=0 высокий полный максимум T>=51/25 теперь должен одновременно иметь

    beta>1001/1000,
    |c-d|>min(h_x,h_y)/500.

В частности, равноконцевой случай полностью исключён с более сильной оценкой 2.02. Это не утверждает невозможность всех сильно асимметричных концов: именно положительный асимметричный член, ослабляющий второй B-jet, остаётся реальной свободой.

Для 5/4 с некорневой единственной вспомогательной вершиной четырёхугольника доказана только новая обязательная корневая B-грань из раздела 3.2. Остальной B-веер может содержать положительно-ell соседей; формулы простого угла туда не переносятся. Сектор 4/4 с некорневыми соседями B также остаётся вне главной теоремы.

Полезное продолжение — добавить к точному второму B-jet сохранённый настоящий бюджет корневой пирамиды и первые/вторые G-моменты, не заменяя их независимой площадью. Для простого угла операция снятия OBUV теперь полностью контролируется формулами (8.1)–(8.2), а формальный контроль раздела 9 точно показывает, какого дополнительного ограничения не хватает трёхполиномиальному доказательству.

В смешанном случае положительной избыточной D остаётся установить, когда геометрия действительно даёт простой корневой B-угол, и ограничить её реальный взвешенный дефект zeta. Теорема уже принимает такой дефект количественно, но не подменяет его свободно выбираемой массой.

Активная proper33-ветвь с >=3 свободными многоугольниками не использована как объект этого доказательства: рассматриваемый B-угол заставляет обе координатные грани быть расширенными при c,d>0. Новые 70/50 ячеек не являются уменьшением механического реестра. Общие границы 34<=C_min<=622 и отсутствие полного исключения 10/17/9 остаются неизменными. :contentReference[oaicite:8]{index=8}

## 11. Полная recovery capsule

Полный самодостаточный исходник ниже восстанавливает оба сертификата, новые настоящие контрольные тела, их точные общие моменты и формальный отрицательный контроль. Внешние исходники, файлы данных, случайные числа и численный оптимизатор не нужны.

Среда авторского исполнения: CPython 3.13.5, SymPy 1.14.0; assertions включены. Выполнены обычный запуск и отдельный source-only запуск в новой директории. JSON и stdout совпали побайтово.

    b_root_corner_second_jet_v2.py
    12294 bytes
    SHA256 0a2940dc8143387a262a71948cbe5e903019eb17382a21cc5a02856eade6d110

    b_root_corner_second_jet_v2.json
    28873 bytes
    SHA256 df83c9fcaf70b36d7159ef31947607b38241ff4d131e97fa59dac28b6807c9fc

    b_root_corner_second_jet_v2.out
    520 bytes
    SHA256 97b8ff3eff99cba5a6cd751729ef09430717724ed05b2a302b039b1db440db6b

Команды:

    python b_root_corner_second_jet_v2.py > b_root_corner_second_jet_v2.out
    sha256sum b_root_corner_second_jet_v2.py b_root_corner_second_jet_v2.json b_root_corner_second_jet_v2.out

Полный ожидаемый stdout:

    B_ROOT_CORNER_EXACT_SECOND_JET_ALGEBRA_PASS
    COVER tau=101/50 eps=0 zeta=0 leaves=70 depth=20 positive_coefficients=1050
    COVER tau=203/100 eps=1/1000 zeta=1/1000 leaves=50 depth=16 positive_coefficients=750
    INDEPENDENT_BINOMIAL_REPLAY_AND_FULL_CLOSED_SQUARE_COVER_PASS
    ACTUAL_B_PATH_UNTRUNCATION_TWO_POSITIVE_VOLUME_FANS_PASS
    FORMAL_T2_RELAXATION_PASS_BUT_ACTUAL_ROOT_BUDGET_FAILS
    report_bytes=28873
    report_sha256=df83c9fcaf70b36d7159ef31947607b38241ff4d131e97fa59dac28b6807c9fc
    B_ROOT_CORNER_SECOND_JET_V2_RECOVERY_PASS

Удобные дополнительные копии: [исходник](sandbox:/mnt/data/b_root_corner_second_jet_v2.py), [полный точный отчёт](sandbox:/mnt/data/b_root_corner_second_jet_v2.json), [stdout](sandbox:/mnt/data/b_root_corner_second_jet_v2.out). Они не заменяют следующий полный источник.

```python
#!/usr/bin/env python3
"""B_ROOT_CORNER_SECOND_JET_V2. CPython 3.13.5, SymPy 1.14.0.
Exact algebra, complete two-square-domain covers, and actual uniform bodies.
No RNG, external data, numerical optimizer, or inherited code is needed.
Geometric admissibility and the accepted joint-mass premise are in the proof.
Parent geometry: EXPANDED_PATCH_B_FAN_AND_ROOT_FLOOR_V1;
parent audit.py SHA256 68bfcdf161687658b3b9b9d29cd92507d4888dbc67f13edf0727dc6be1eab401.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
from pathlib import Path
from collections import Counter
import hashlib
import json
import sympy as S


def rat(x):
    x = S.Rational(x)
    return Q(int(x.p), int(x.q))


def algebra():
    e, A, H, beta = S.symbols('e A H beta', positive=True)
    h = A+H
    x = A/h
    w = 3*H/(h*(1+e))
    d = beta*x
    f2 = w*(4+e)*(1-d)/6-x+A*w/4-e*w*w/2
    base = w*w*(2-e)**2/18-x+A*w/4
    assert S.factor(f2-base-w*(4+e)*(x-d)/6) == 0
    eps = S.symbols('eps', nonnegative=True)
    budget = A*h*(1+e)*(4*(1+e)-3*H+2*eps*H*(4+e)/h)-2*H**2*(2-e)**2
    assert S.factor(budget+4*h*h*(1+e)**2*f2.subs(beta,1+eps)) == 0
    U = 4*(4-e*e)/(4+e)
    F = A*(A+H)*(1+e)*(4*(1+e)-3*H)-2*H*H*(2-e)**2
    htest = (2+3*e)/2
    P = 19*e**4+86*e**3+100*e**2-72*e-96
    assert S.factor(F.subs({A:U,H:htest})+(e-2)**2*P/(2*(e+4)**2)) == 0
    y = S.symbols('y')
    assert S.expand(P.subs(e,1+y)) == 19*y**4+162*y**3+472*y**2+462*y+37
    R = S.Rational(27,4)*(2+3*e)*(4-e)/((1+e)*(4+e)**2)
    C = S.Rational(27,2)*(2+3*e)/((1+e)*(4+e)**2)
    assert S.factor(S.Rational(81,40)-R-27*(e-1)*(3*e*e+60*e+32)/(40*(1+e)*(4+e)**2)) == 0
    assert S.factor(S.Rational(27,20)-C-27*(e-1)*(e*e+10*e+4)/(20*(1+e)*(4+e)**2)) == 0
    hx, hy, u, v = S.symbols('hx hy u v', positive=True)
    hb = (hx*u+hy*v)/(u+v)
    hc = hx+hy-hb
    assert S.factor(hb*hc-hx*hy-(hx-hy)**2*u*v/(u+v)**2) == 0
    assert S.factor(hb*(hx+hy)/(2*hx*hy)-1-(hx-hy)*(hx*u-hy*v)/(2*hx*hy*(u+v))) == 0
    # Exact physical B displacement followed by canonical frame restoration.
    a,b,r,q,V,W,p,K,SB,t = S.symbols('a b r q V W p K SB t')
    al = a-b
    FF = ((1+t)*(r*V+K*W*t/2-al*t*(p*V+SB*t))
          -(q/V)*(V+W*t)*(r*V/q+b*W*t/2-al*W*t*t/4))
    L = (r+q*b)/3
    assert S.factor(S.diff(FF,t).subs(t,0).subs(K,(4*r+q*b)/3)-(V*(r-al*p)-L*W)) == 0
    coef2 = K*W/2-al*p*V-al*SB+q*al*W/4-q*b*W*W/(2*V)
    assert S.factor(S.diff(FF,t,2).subs(t,0)/2-coef2) == 0
    return {'curvature_error_factor':2, 'coarse_chi_enlargement_factor':4,
            'eta_ge_1_no_joint_mass_trace':'81/40',
            'eta_ge_1_defect_coefficient':'27/20',
            'mixed_defect_threshold':'1/90'}


def power_to_bern(power, n=4, m=2):
    return [[sum((c*Q(comb(i,k),comb(n,k))*Q(comb(j,l),comb(m,l))
                  for (k,l),c in power.items() if k<=i and l<=j),Q(0))
             for j in range(m+1)] for i in range(n+1)]


def split1(row):
    left,right = [row[0]],[row[-1]]
    while len(row)>1:
        row = [(row[i]+row[i+1])/2 for i in range(len(row)-1)]
        left.append(row[0]); right.append(row[-1])
    return left,list(reversed(right))


def split2(b,axis):
    if axis==1:
        pairs = [split1(row) for row in b]
        return [p[0] for p in pairs],[p[1] for p in pairs]
    pairs = [split1(list(col)) for col in zip(*b)]
    return ([list(t) for t in zip(*(p[0] for p in pairs))],
            [list(t) for t in zip(*(p[1] for p in pairs))])


def direct_box_bern(power,box):
    out = {}
    (a,b),(c,d) = box
    for (k,l),z in power.items():
        for i in range(k+1):
            for j in range(l+1):
                term = z*comb(k,i)*a**(k-i)*(b-a)**i*comb(l,j)*c**(l-j)*(d-c)**j
                out[i,j] = out.get((i,j),Q(0))+term
    return power_to_bern(out)


def certificate(tau,eps,zeta,expected):
    u,v = S.symbols('u v')
    ta,ep,ze = map(S.Rational,(tau,eps,zeta))
    e = 2*u
    chi = ((4-2*e)/3+4*ep)*v
    H = 2*e+chi
    D = (1+e)*(4+e)**2
    expressions = [
        27*H*((4*ta-H)*(e+4)-4*(4-e*e))-(1+ep)**2*ta*ta*D*(e+4),
        ta*ta*D-27*H*(4-chi),
        ta*D-27*H*(1+chi+ze)]
    pp = [S.Poly(S.expand(f),u,v) for f in expressions]
    assert max(p.degree(u) for p in pp)==4
    assert max(p.degree(v) for p in pp)==2
    powers = [{ij:rat(c) for ij,c in p.terms()} for p in pp]
    bs = [power_to_bern(p) for p in powers]
    leaves = []
    def rec(blocks,path,box):
        mins = [min(c for row in b for c in row) for b in blocks]
        for k,mn in enumerate(mins):
            if mn>0:
                independent = direct_box_bern(powers[k],box)
                assert independent==blocks[k]
                assert all(c>0 for row in independent for c in row)
                leaves.append({'path':path,'polynomial':k,'minimum':str(mn)})
                return
        assert len(path)<42, 'NO_CERTIFICATE_AT_DEPTH_42'
        axis = len(path)%2
        pairs = [split2(b,axis) for b in blocks]
        lo,hi = box[axis]; mid = (lo+hi)/2
        for side in range(2):
            child = list(box); child[axis] = (lo,mid) if side==0 else (mid,hi)
            rec([p[side] for p in pairs],path+str(side),tuple(child))
    rec(bs,'',((Q(0),Q(1)),(Q(0),Q(1))))
    paths = {l['path'] for l in leaves}
    prefixes = {p[:i] for p in paths for i in range(len(p)+1)}
    def check_partition(p):
        if p in paths:
            assert not any(q!=p and q.startswith(p) for q in paths)
            return
        assert p+'0' in prefixes and p+'1' in prefixes
        check_partition(p+'0');check_partition(p+'1')
    check_partition('')
    assert sum((Q(1,2**len(p)) for p in paths),Q(0))==1
    counts = [sum(l['polynomial']==i for l in leaves) for i in range(3)]
    depth = max(map(len,paths))
    minimum = min(Q(l['minimum']) for l in leaves)
    assert (len(leaves),depth,counts,str(minimum))==expected
    return {'tau':tau,'epsilon':eps,'zeta':zeta,'bidegree':[4,2],
            'leaf_count':len(leaves),'maximum_depth':depth,'by_polynomial':counts,
            'positive_coefficients':15*len(leaves),'minimum':str(minimum),
            'powers':[[[i,j,str(c)] for (i,j),c in sorted(p.items())] for p in powers],
            'leaves':leaves}


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),Q(0))


def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


def det(a,b,c):
    return dot(a,cross(b,c))


def actual(points,cycles,Bheight):
    pts = [tuple(Q(x) for x in p) for p in points]
    found = {}
    for i,j,k in combinations(range(len(pts)),3):
        n = cross(sub(pts[j],pts[i]),sub(pts[k],pts[i]))
        if not any(n):continue
        z = dot(n,pts[i]);sl = [z-dot(n,p) for p in pts]
        if min(sl)<0<max(sl):continue
        if max(sl)<=0:n,z,sl=tuple(-x for x in n),-z,[-x for x in sl]
        f = frozenset(i for i,s in enumerate(sl) if s==0)
        found.setdefault(f,(n,z))
    assert set(found)=={frozenset(f) for f in cycles}
    edges={tuple(sorted((c[i-1],c[i]))) for c in cycles for i in range(len(c))}
    assert edges=={tuple(sorted(f&h)) for f,h in combinations(found,2) if len(f&h)==2}
    assert len(pts)-len(edges)+len(found)==2
    for i in range(len(pts)):
        ns=[n for f,(n,z) in found.items() if i in f]
        assert any(det(*t)!=0 for t in combinations(ns,3))
    ell=lambda p:1-(p[0]+p[1]+p[2])/2
    ev=[ell(p) for p in pts]
    assert min(ev)>=0
    def fan(apex):
        V,E,N=Q(0),Q(0),Q(0);J=[Q(0)]*3
        for c in cycles:
            if apex in c:continue
            for j in range(1,len(c)-1):
                ids=(apex,c[0],c[j],c[j+1])
                w=abs(det(*(sub(pts[k],pts[apex]) for k in ids[1:])))/6
                assert w>0
                V+=w;E+=w*sum(ev[k] for k in ids)/4
                N+=w*sum(2*(pts[k][0]+pts[k][1]) for k in ids)/4
                for z in range(3):J[z]+=w*sum(pts[k][z] for k in ids)/4
        return V,E,N,tuple(J)
    V,E,N,J=fan(0)
    assert (V,E,N,J)==fan(1)
    b=1-Bheight/2
    Nm=(Q(3,2)+b)*(J[0]+J[1])
    T=Bheight*Nm/(6*V*E)
    G=[(Q(3,2)+b)*(p[0]+p[1])-Nm/V-(Nm/E)*ell(p) for p in pts]
    return {'vertices':[[str(x) for x in p] for p in pts],
            'facets':[list(c) for c in cycles],'edges':[list(e) for e in sorted(edges)],
            'f_vector':[len(pts),len(edges),len(found)],
            'physical_V':str(V),'physical_E':str(E),'physical_N_original_2s':str(N),
            'physical_J':[str(x) for x in J],'canonical_b':str(b),
            'canonical_T':str(T),'G_vertices':[str(x) for x in G],
            'status':'actual uniform nonstationary control; mechanical counts not audited'}


def controls():
    cycles=[(0,1,4,5,2),(0,1,6,7,3),(0,2,3),(1,4,6),(4,6,7,5),(2,3,7,5)]
    records=[]
    for delta in (Q(0),Q(1,1000)):
        pts=[(0,0,0),(0,0,1+delta),(0,1,0),(1,0,0),
             (0,1,1),(0,Q(5,4),Q(3,4)),(1,0,1),(Q(5,4),0,Q(3,4))]
        r=actual(pts,cycles,1+delta)
        assert Q(r['physical_V'])==Q(61,96)+delta/6
        assert Q(r['physical_E'])==Q(59,256)+delta/24-delta*delta/48
        assert Q(r['physical_N_original_2s'])==Q(123,128)+delta/6
        assert Q(r['G_vertices'][2])<0 and Q(r['G_vertices'][3])<0
        assert all(Q(x)>0 for x in r['G_vertices'][4:])
        b=Q(r['canonical_b'])
        for cyc,axis in ((cycles[0],1),(cycles[1],0)):
            assert max((b+1)*(Q(pts[i][axis])-1)+(b-1)*Q(pts[i][2])/(1+delta) for i in cyc)==0
        r['physical_B_displacement']=str(delta);records.append(r)
    assert records[0]['canonical_T']=='3936/3599'
    assert records[1]['canonical_T']=='184670352867/168777867746'
    gain=Q(records[1]['canonical_T'])-Q(records[0]['canonical_T'])
    assert gain==Q(318912520077,607431546017854)>0
    old=records[0]
    assert Q(old['G_vertices'][1])+3*Q(old['G_vertices'][4])==-Q(7680,3599)
    pts=[(0,0,0),(0,0,2),(0,1,0),(1,0,0),(0,Q(5,4),Q(3,4)),(Q(5,4),0,Q(3,4))]
    cyc=[(0,1,4,2),(0,1,5,3),(0,2,3),(1,4,5),(2,3,5,4)]
    uncut=actual(pts,cyc,Q(2))
    assert uncut['f_vector']==[6,9,5]
    assert Q(uncut['physical_V'])-Q(old['physical_V'])==Q(1,6)
    assert Q(uncut['physical_E'])-Q(old['physical_E'])==Q(1,48)
    assert Q(uncut['physical_N_original_2s'])-Q(old['physical_N_original_2s'])==Q(1,6)
    assert uncut['canonical_T']=='20784/14861'
    return {'B_path':records,'B_path_trace_gain':str(gain),'untruncated':uncut}


def formal_limit():
    e,c,A,T=Q(1,20),Q(2,3),Q(197,50),Q(2)
    H=2*e+c;h=A+H;D=(1+e)*(4+e)**2
    p=27*H/(T*D);t=h*p/T;w=3*H/(h*(1+e))
    rho0=(h-3)**2/(9*h*(1-1/(3*p)))
    vals=[4*(1+e)-3*H,4*(4-e*e)/(4+e)-A,p-Q(1,2),
          p*(1+c)-1,p*(4-c)-T,t-4*p+1]
    assert vals==[Q(19,10),Q(11,1350),Q(3091,30618),Q(73,45927),Q(146,45927),Q(479,45927)]
    bad=1-w-(A+e)*rho0
    assert bad==-Q(185591543,2277829575)
    return {'status':'FORMAL ONLY, NOT A BODY; fails inherited root-volume budget',
            'eta':str(e),'chi':str(c),'alpha_over_mu':str(A),'T':str(T),
            'p':str(p),'t':str(t),'six_positive_residuals':[str(x) for x in vals],
            'root_volume_budget_residual':str(bad)}


def main():
    cs=[certificate('101/50','0','0',(70,20,[35,17,18],'41363/104857600')),
        certificate('203/100','1/1000','1/1000',(50,16,[25,8,17],'689575417/13107200000'))]
    report={'algebra':algebra(),'certificates':cs,'actual_controls':controls(),
            'formal_limit':formal_limit()}
    raw=(json.dumps(report,sort_keys=True,ensure_ascii=True,indent=2)+'\n').encode()
    Path('b_root_corner_second_jet_v2.json').write_bytes(raw)
    print('B_ROOT_CORNER_EXACT_SECOND_JET_ALGEBRA_PASS')
    for c in cs:
        print('COVER tau='+c['tau']+' eps='+c['epsilon']+' zeta='+c['zeta']+
              ' leaves='+str(c['leaf_count'])+' depth='+str(c['maximum_depth'])+
              ' positive_coefficients='+str(c['positive_coefficients']))
    print('INDEPENDENT_BINOMIAL_REPLAY_AND_FULL_CLOSED_SQUARE_COVER_PASS')
    print('ACTUAL_B_PATH_UNTRUNCATION_TWO_POSITIVE_VOLUME_FANS_PASS')
    print('FORMAL_T2_RELAXATION_PASS_BUT_ACTUAL_ROOT_BUDGET_FAILS')
    print('report_bytes='+str(len(raw)))
    print('report_sha256='+hashlib.sha256(raw).hexdigest())
    print('B_ROOT_CORNER_SECOND_JET_V2_RECOVERY_PASS')


if __name__=='__main__':
    main()
```
