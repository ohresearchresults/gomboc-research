# minimum-0168

AI research report · 2026-09-21 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# B_ROOT_CORNER_MIXED_SIGN_V4

## 1. Главный результат

**Весь заданный смешанный simple-corner сектор закрыт.** Пусть P — полигедральный локальный максимум ПОЛНОЙ совместной отмеченной задачи, a>b>0, c,d>0, корень имеет положительную площадь, а B образует настоящий простой корневой угол в точном смысле родителя. При принятом общем моментном законе

    (J)  4(u+v)<=6V+1

доказаны два результата:

    Без ограничений на G(C),G(D):      T<51/25.
    Если min(G(C),G(D))<=0:            T<101/50=2.02.

В частности,

    G(C)<0<G(D), а также G(D)<0<G(C)  ==>  T<2.02.

Никаких ограничений на beta, c/d, симметрию тела, число остальных граней или положительно-ell вспомогательные вершины вне угла не вводится. Во втором результате положительность другой G-отметки не требуется: достаточно одной неположительной. Для двух неположительных отметок сохраняется более сильная уже принятая родительская оценка T<2; она здесь не переобъявляется новым результатом.

Новый механизм не требует анализа положительного D-веера или второго B-jet. Оказалось, что настоящие root-volume и root-n бюджеты, интервал корневого момента и determinant floor сохраняются при смешанных знаках. Теряют силу два других шага родителя: `p(1+chi)>=1` и `Z<=1+chi`. Они полностью удалены. Вместо них получено новое необходимое условие от ОДНОЙ неположительной отметки:

    h*p*(1+4*p*chi)>sigma.

Оставшиеся условия дают два полных точных покрытия замкнутого трёхмерного куба: 1042 и 1502 ячейки, суммарно 213404 строго отрицательных коэффициента Бернштейна. Это непрерывные исключения, включая границы, а не численная сетка.

## 2. Точный домен и источники

Настоящий простой корневой угол означает: B — простая настоящая вершина, инцидентная ровно защищённым граням Fx,Fy и одной свободной настоящей грани BUV; последняя — треугольник с единственной канонической отметкой B, причём U принадлежит Fx и F0, V принадлежит Fy и F0. Это не предположение, что любые два замеченных корневых соседа автоматически замыкают весь B-веер. Остальные грани и вершины не ограничиваются.

Максимум берётся по настоящим равномерно заполненным телам, корневой аффинной функции и отмеченной рамке. Максимум только при фиксированной ell, фиксированной решётке граней или внутри искусственно ограниченного sign-сектора не наследует весь использованный набор реакций. Нулевые канонические ell-концы не включены.

Полностью прочитан новый `research-journal(20260921-204841).md`, включая весь буквальный родитель до EOF. Фактическая идентичность журнала:

    299816 bytes
    SHA256 e1f31602e2b38ccb8f5bfbf9b9f2340afed1aa313c0d04408aabd71abdf23240

Буквальный родитель `minimum-0167`, B_ROOT_CORNER_ALL_ASYMMETRIES_V3, имеет SHA256 `54d717262bdd7d55643e5593eeeac441afce686e14a736e3f128ad80a25c2d62`. Подтверждён его 45926-байтный компактный UTF-8 JSON-envelope без конечного LF. Встроенный исходник побайтово совпадает с переданным `b_root_corner_all_asymmetries_v3.py`, 13751 байт, SHA256 `f13a5ecbe56f01c961280b964a6e6c8c1fd480af752b9bc6d1978624af603722`. Новые переданные `.py`, `.json` и `.out` прочитаны полностью; JSON — все 5235 строк. Неизменные ранее прочитанные аналитические источники и предыдущие результаты этой ветви остаются доступными. Конфликта родительской идентичности не обнаружено.

Используются принятые точные утверждения: G>0 на всех вспомогательных настоящих вершинах; одноякорная свободная грань является жёстким настоящим треугольником; полный аффинный root-тест при a,b,c,d>0.

Закон (J) используется как явно принятая предпосылка родителя. Его первоначальный отдельный proof-файл не приложен и здесь не восстанавливался по догадке. Переход этого нестрогого закона с proper-пары к расширенным patches тот же: для q0 в относительной внутренности корня с положительными x,y тела `conv(T0,(1-epsilon)P+epsilon q0)` имеют proper-пару и сходящиеся настоящие V,u,v. Таким образом результат можно независимо читать как теорему с дополнительной гипотезой (J).

Ниже даны аналитическое доказательство редукций и полный runnable-сертификат. Авторски исполнены обычный запуск и отдельный source-only запуск в новой директории; JSON и stdout совпали побайтово. Это не proof-assistant-формализация вариационной допустимости. Механические S/U/H не вычислялись.

## 3. Знаконезависимая часть настоящей геометрии

### 3.1. Обозначения

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    alpha=a-b>0, s=a+b,
    ell=a+(d-a)x+(c-a)y-alpha*z,
    h_x=s+c, h_y=s+d, Delta=h_x*h_y,
    n=h_x*x+h_y*y,
    V=int_P 1, E=int_P ell, N=int_P n,
    g=(u,v,z_g), p=u+v, mu=E/V, t=6V,
    r=N/V, q=N/E, T=q/t, G=n-r-q*ell,
    m=3p/t, w0=(v/(3p),u/(3p),1/3).

P содержит T0=conv(A,B,C,D) и лежит в x,y,ell>=0. Все величины принадлежат одному исходному равномерному телу. ell не является плотностью; n не заменяется следом по полным площадям расширенных координатных граней.

### 3.2. Настоящий B-тетраэдр и совместное восстановление рамки

Одноякорная жёсткость настоящего BUV даёт

    G(U)=G(V)=L=(r+qb)/3,
    n(U)=n(V)=K=(4r+qb)/3,
    U_y=K/h_y, V_x=K/h_x,
    W=Vol(conv(A,B,U,V))=K^2/(6*Delta).

Плоскость BUV имеет уравнение

    H_B=n-K+(K/b)*ell=0.

Её внутренняя сторона есть H_B>=0, поскольку H_B(A)=K*alpha/b>0. Поэтому на настоящем корне G>=L. Это минимальное, не максимальное G-ребро корня.

Оставим физическую ell и все вершины, кроме B, на месте, положив B_delta=(0,0,1+delta). Малые параметры обоих знаков допустимы: единственная свободная грань B — настоящий треугольник, остальные неинцидентные опоры имеют строгий запас, защищённые плоскости не меняются. В положительном A-веере меняется только ABUV, поэтому

    V_phys=V+W*delta,
    E_phys=E+b*W*delta/2-alpha*W*delta^2/4,
    N_phys=N+K*W*delta/2.

Восстановление рамки z'=z/(1+delta) имеет якобиан 1/(1+delta), новый конец b_delta=b-alpha*delta, а правильный числитель в физических координатах равен `n-alpha*delta*(x+y)`. Следовательно, при S_phys=int_(P_delta)(x+y),

    T_delta=(1+delta)*(N_phys-alpha*delta*S_phys)
             /(6*V_phys*E_phys).

Первая двусторонняя совместная реакция имеет вид

    V*(r-alpha*p)-L*W=0,
    W/V=(r-alpha*p)/L.                                  (B)

Ни знак G(C), ни знак G(D) в этой реакции не использованы.

### 3.3. Безразмерные величины

    eta=b/mu, A0=alpha/mu, c0=c/mu, d0=d/mu,
    sigma=A0+2*eta,
    chi=(c0*u+d0*v)/p,
    H=2*eta+chi, h=A0+H=(r/p)/mu,
    D_eta=(1+eta)*(4+eta)^2,
    kappa=Delta/(r/p)^2,
    hcross=(h_x+h_y-r/p)/mu,
    lambda=Delta/((r/p)*(h_x+h_y-r/p)),
    Z=hcross/(h*p)=3*n(w0)/r,
    omega=W/V.

Тождество

    h*hcross=Delta/mu^2+(c0-d0)^2*u*v/p^2

показывает 0<lambda<=1. Из настоящего W и реакции (B):

    omega=3H/(h*(1+eta)),
    p=27*kappa*H/(T*D_eta),
    Z=T*D_eta/(27*lambda*H),
    T/m=h/3.                                           (3.1)

## 4. Общие root-volume и root-n бюджеты сохраняются при смешанных знаках

Положим k=|grad ell| и

    rho=mu*Area(F0)/(3*V*k).

Это настоящая доля пирамиды conv(g,F0). Полная вариация единственной корневой опоры и самой функции `ell+epsilon*f`, для любого аффинного f и обоих знаков epsilon, даёт

    int_F0 G*f/k=6V^2*(T*f(g)-m*f(w0)).                 (4.1)

Здесь нужны положительные a,b,c,d, но НЕ неположительность G(C),G(D). Все корневые вершины вспомогательные, поэтому G>0 на F0. Отсюда

    h>3, 0<Z<3.

Для настоящих площадных средних:

    rho*mean_F0(G)=r*(h-3)/(3h),
    rho*mean_F0(G^2)=r^2*(3-Z)/(3h).

G непостоянна на положительно-площадном корне: grad ell имеет ненулевую z-компоненту, grad n — нулевую и сама не равна нулю. Строгое Коши–Шварц даёт

    rho>rho0=(h-3)^2/(3h*(3-Z)).                       (4.2)

Теперь используем ОДИН положительный A-веер настоящего P. Пирамида conv(A,F0) имеет долю `(A0+eta)*rho`, а тетраэдр ABUV — долю omega. Их внутренности не пересекаются, поскольку основания — разные настоящие максимальные грани. Поэтому

    omega+(A0+eta)*rho<=1.                             (V-root)

Та же корневая пирамида имеет среднее n, равное 3/4 площадного среднего n на F0, поскольку n(A)=0. Используя n|F0=r+G и (4.1), её доля от полного N равна

    3*(A0+eta)*rho/4+(A0+eta)*(h-3)/(4h).

Среднее n на ABUV равно K/2, поэтому его доля от N равна `omega*(4+eta)/6`. На остальных частях этого же A-веера n>=0. Следовательно

    3*(A0+eta)*rho/4+(A0+eta)*(h-3)/(4h)
      +omega*(4+eta)/6<=1.                             (N-root)

Подстановка (4.2) даёт строгие необходимые условия

    omega+(A0+eta)*(h-3)^2/(3h*(3-Z))<1,

    (A0+eta)*(h-3)*(h-Z)/(4h*(3-Z))
      +omega*(4+eta)/6<1.                              (4.3)

Оба становятся жёстче при увеличении Z: производная `(h-Z)/(3-Z)` равна `(h-3)/(3-Z)^2>0`. Никакая независимая корневая площадь или масса здесь не подставлена.

## 5. Что действительно зависит от знаков и чем это заменено

### 5.1. Сохраняющийся determinant floor

Настоящее конирование неотрицательной аффинной функции из точки X тела даёт `4*mean_P(f)>=f(X)`. В частности,

    u,v>=1/4, A0+eta<=4, c0,d0<=4.

Из H_B>=0:

    H_B(g)=r*(4-eta^2)/(3eta)>0,
    H_B(A)=r*A0*(4+eta)/(3eta),

поэтому

    0<eta<2,
    A0*(4+eta)<=4*(4-eta^2),
    0<A0<=4, 0<chi<=4.                                (5.1)

Закон (J) вместе с u,v>=1/4 даёт 4u,4v<=t. Следовательно

    4p*chi=4*(c0*u+d0*v)<=t*(c0+d0),
    c0+d0>=4T*chi/h.

Отсюда

    Delta/mu^2=(sigma+c0)*(sigma+d0)
      >=sigma^2+4T*sigma*chi/h,

    kappa>=sigma*(sigma*h+4T*chi)/h^3.                 (DET)

Таким образом именно этот родительский determinant floor ЗНАКОНЕЗАВИСИМ. Его область не была расширена молча: вывод выше использует только положительные ell-концы, настоящие координатные моменты и (J).

Из p>=1/2 и (J) также следует h>=2T. Полные координатные пирамиды дают

    t*(4mu-c)>h_y, t*(4mu-d)>h_x.

Обе координатные грани действительно расширены, поскольку имеют корневого соседа B при трёх положительных канонических ell-значениях. Поэтому неравенства строги. Взвешивая их теми же настоящими u,v и используя (3.1), получаем

    T^2*D_eta<27*lambda*H*(4-chi)<=27H*(4-chi).         (5.2)

### 5.2. Два удалённых знаковых шага

При смешанных знаках НЕ используются

    p*(1+chi)>=1,
    Z<=1+chi.

Вторая формула эквивалентна неположительности `u*G(C)+v*G(D)`. Из одного отрицательного G(C) она не следует. Настоящий контроль в разделе 8 нарушает ОБЕ формулы, сохраняя simple-corner геометрию, смешанные знаки, положительность вспомогательных G и опорные реакции обеих отметок.

Само равенство

    G(D)-G(C)=(c-d)*(1+q)

показывает, что G(C)<0<G(D) требует c>d. Для нового запрета это следствие не нужно.

### 5.3. Новая связь от одной неположительной отметки

Сначала докажем знаконезависимый факт:

    T>=2 ==> h<8.                                     (5.3)

При h>=8 из A0+eta<=4 следует chi>=4-eta. На этом интервале `(2eta+chi)*(4-chi)` убывает по chi, поскольку её производная не больше -4. Поэтому из (5.2)

    4*(1+eta)*(4+eta)^2
      <27*eta*(4+eta).

Это требовало бы `4eta^2-7eta+16<0`, что невозможно:

    16*(4eta^2-7eta+16)=(8eta-7)^2+207>0.

Теперь пусть G(C)<=0. В безразмерных переменных

    sigma+d0<=h*p*(1+c0).

Но `p*chi=c0*u+d0*v>=c0/4`, значит c0<=4p*chi. Поскольку d0>0,

    h*p*(1+4p*chi)>sigma.                              (ONE-NEG)

При G(D)<=0 доказательство отражается и даёт ТО ЖЕ условие. Именно здесь входит знак одной отметки; знак второй не нужен.

Пусть T>=tau>=2. По (5.3), h<8<=4tau. Закон (J) даёт

    p<=T/(4T-h)<=tau/(4tau-h),

где последняя монотонность имеет производную `-h/(4T-h)^2<0`. Подстановка в возрастающую по p левую часть ONE-NEG даёт

    h*tau*(4tau-h+4tau*chi)
      -sigma*(4tau-h)^2>0.                             (5.4)

Это корректная смешанная замена двух потерянных родительских оценок; она не утверждает существования тела по заданным скалярам.

## 6. Полное непрерывное исключение

Для перехода J/DET к фиксированному порогу нужна отдельная монотонность. Положим

    j(s)=s^2*D_eta-27*kappa*H*(4s-h).

Из (J) имеем j(T)>=0. На tau<=s<=T величина `p_s=27*kappa*H/(s*D_eta)` не меньше настоящей p>=1/2, поэтому

    j'(s)=2s*D_eta*(1-2p_s)<=0,
    j(tau)>=0.

Подстановка DET с T>=tau даёт

    tau^2*h^3*D_eta
      -27H*sigma*(sigma*h+4tau*chi)*(4tau-h)>=0.         (6.1)

При 4tau-h<0 это выражение положительно автоматически; при неотрицательной скобке применяется нижняя граница kappa.

Предположим T>=tau. Введём следующие девять полиномов, каждый из которых необходимо неотрицателен:

    P0=4-A0-eta,
    P1=4*(4-eta^2)-(4+eta)*A0,
    P2=h-2tau,
    P3=27H*(4-chi)-tau^2*D_eta,
    P4=h*(1+eta)-3H,
    P5=81H-tau*D_eta,
    P6=[h*(1+eta)-3H]*(81H-tau*D_eta)
         -9H*(1+eta)*(A0+eta)*(h-3)^2,
    P7=tau^2*h^3*D_eta
         -27H*sigma*(sigma*h+4tau*chi)*(4tau-h),
    P8=[4h*(1+eta)-2H*(4+eta)]*(81H-tau*D_eta)
         -(A0+eta)*(1+eta)*(h-3)*(27Hh-tau*D_eta).

P6 и P8 получены из настоящих root-volume и root-n бюджетов заменой

    Z>=Z0=tau*D_eta/(27H),

которая их ослабляет по доказанной монотонности. Настоящее Z<3 гарантирует положительность очищаемых знаменателей. Строгие необходимые неравенства безопасно ослаблены до нестрогих.

При одной неположительной отметке добавляется десятый полином

    P9=h*tau*(4tau-h+4tau*chi)-sigma*(4tau-h)^2.

Все настоящие кандидаты лежат в параметрическом замкнутом кубе

    eta=2X, A0=4Y, chi=4Zc,  (X,Y,Zc) in [0,1]^3.

Это параметры, не физические координаты тела. На искусственных границах куба не предполагается допустимость root-вариаций: куб является большим алгебраическим множеством, содержащим все настоящие кандидаты.

Точный алгоритм попеременно делит куб по оси `depth mod 3`. На каждом конечном замкнутом параллелепипеде один из необходимых P_i имеет ВСЕ коэффициенты Бернштейна строго отрицательными. Поэтому P_i<0 на всей ячейке, включая границу.

| Домен | Порог tau | Листьев | Глубина | Отрицательных коэффициентов |
|---|---:|---:|---:|---:|
| Девять знаконезависимых условий | 51/25 | 1042 | 31 | 88170 |
| Те же условия и ONE-NEG | 101/50 | 1502 | 36 | 125234 |

Распределения листьев по P_i:

    tau=51/25:  [0,7,29,348,1,0,62,397,198],
    tau=101/50: [0,7,18,523,1,0,57,574,273,49].

Минимальные запасы `-max(Bernstein coefficient)`:

    3/16,
    1628892577475/17592186044416.

Степени по (X,Y,Zc):

    (1,1,0),(2,1,0),(1,1,1),(3,0,2),(2,1,1),
    (3,0,1),(5,3,3),(6,4,3),(6,3,3),

и у добавленного P9 — (3,3,2).

Каждый лист независимо перепроверен прямой биномиальной подстановкой концов его dyadic-ячейки в исходный степенной полином. Этот проверитель не наследует коэффициенты de Casteljau; вычисление выполняется через точные целочисленные числители и общие знаменатели. Проверены полное префиксное двоичное дерево и точная сумма `sum 2^(-depth)=1`. Следовательно покрыты все непрерывные области и все границы, без отсечения по предполагаемой физической нереализуемости.

Это доказывает обе теоремы раздела 1.

## 7. Точная граница дальнейшего уменьшения порога

Новая десятиполиномиальная релаксация при tau=201/100 допускает точную точку

    eta=9/25, A0=82/25, chi=17/50.

Её полные немасштабированные остатки P0,...,P9:

    [9/25,
     738/625,
     8/25,
     23458473/78125000,
     3403/1250,
     13240374/390625,
     7301025669/976562500,
     265315300665201/9765625000000,
     188153732571/24414062500,
     4258957/3125000].

Все строго положительны. Поэтому именно эти десять условий не могут исключить порог 2.01. Это точный отрицательный результат для указанной релаксации, а не численная неудача поиска сертификата.

Точка НЕ является телом; не утверждается существование c0,d0,u,v, полного B-jet, корневой площади или всех настоящих моментов, реализующих её. Дальнейшее усиление до T<2 в смешанном секторе потребует дополнительной геометрии, более точного сохранения lambda/индивидуальных моментов либо иных совместных реакций. Для требуемого порога 51/25 эта неопределённость уже не оставляет остатка внутри simple-corner домена.

## 8. Настоящий смешанный контроль и его транспонированная копия

Построен и точно проверен равномерный многогранник с семью настоящими опорами:

    x>=0, y>=0, z>=0,
    100-99x-82y-90z>=0,
    4230-4013x-3299y-4230z>=0,
    2-2x+15z>=0,
    23-23y+45z>=0.

Используются

    ell=1-99x/100-41y/50-9z/10,
    (a,b,c,d)=(1,1/10,9/50,1/100),
    n=32x/25+111y/100.

Все десять настоящих вершин, в постоянном порядке:

    0=(0,0,0),             1=(0,0,1),
    2=(0,1,0),             3=(1,0,0),
    4=(0,94/111,1696/4995),
    5=(0,73/64,23/320),
    6=(2/11,1,0),
    7=(47/64,0,1747/5760),
    8=(1,1/82,0),
    9=(112/111,0,2/1665).

Все настоящие максимальные грани:

    (4,1,0,2,5), (7,1,0,3,9), (6,2,0,3,8),
    (4,7,9,8,6,5), (1,7,4), (9,3,8), (5,2,6).

Тело имеет настоящие 10/15/7, две защищённые пятиугольные грани и шестиугольный корень. B простая, её единственная свободная грань — B47, а 4 и 7 лежат на разных координатных сторонах корня. Все канонические точки настоящие. Проверены

    G(C)<0<G(D), все вспомогательные G>0,

а также обе полные опорные реакции отметок. Геометрический уровень n(4)=n(7)=47/50 не отождествляется со стационарным K.

Точные общие моменты:

    V=11684821/54065880,
    E=1226641429/21626352000,
    N=16065409920339913/110862009085132800,

    J=(7499285847707/135197572055040,
       33555116685449/503918223114240,
       61312407135611/1106161953177600),

    g=(7499285847707/29219156871168,
       33555116685449/108907766519808,
       61312407135611/239065828945920),

    T=3614717232076480425/1834634947718298752.

Две потерянные знаковые оценки действительно не выполняются:

    p*(1+chi)-1
      =-60608685509521863453413/244916426980602010196992<0,

    zeta=(u*G(C)+v*G(D))/(r*p)
      =15375424326553443600311904344581861487619
       /33332407360696184228434998362547388179755>0.

Это настоящий геометрический контроль против их переноса только по смешанному знаку и simple-corner геометрии. Он НЕ стационарен:

    G(B)+3G(4)
      =-4318910258527792054979419/36737464047090301529548800 !=0.

Кроме того, настоящая свободная грань (9,3,8) содержит только положительную каноническую D и имеет G>0 на всей грани. Поэтому она нарушает необходимое `max G+3 mean G<=0`; небольшой настоящий spike над её относительной внутренностью повышает след уже при фиксированной ell. Это объясняет отсутствие противоречия с теоремой о максимуме.

Полное перечисление опорных троек, максимальные грани, истинные рёбра и положительные объёмные веера из A и B проверены точно. Отдельно восстановлена транспонированная копия x↔y,c↔d: она имеет противоположные смешанные знаки и ТОТ ЖЕ T. Полные данные обеих копий восстанавливаются исходником. Механические S/U/H и слабые пакеты не вычислялись; ни одна не объявляется 110 или E17-аттайнером.

## 9. Положение результата в оставшейся карте

В полном all-positive-ell joint-максимуме с принятым (J) любой высокий кандидат T>=51/25 теперь НЕ может иметь настоящий простой B root corner, независимо от знаков G(C),G(D). В смешанном simple-corner секторе получен более сильный запас до 2.02. Обе неположительные отметки сохраняют родительскую границу 2.

Остаются реальные непростые B-веера, в том числе с положительно-ell соседями B, нулевые ell-концы и прочие конфигурации без доказанной simple-corner структуры. Новый proper33 positive-octant root-only результат координатора является отдельным дополнением; он не подменяет доказательство простоты в расширенных mixed patches.

Самая полезная следующая геометрическая задача — установить, какие из оставшихся расширенных смешанных конфигураций действительно вынуждают simple corner, либо получить аналог общих двух root-бюджетов для непростого веера с его настоящими положительно-ell соседями. Перенос данного вычислительного сертификата без такой геометрии не лицензирован.

Ни C_min, ни механический реестр, ни границы 34<=C_min<=622 не изменены. Полного исключения всех 10/17/9-реализаций и нового attaining 110-тела нет.

## 10. Полная recovery capsule

Самодостаточный источник ниже включает точные полиномы, оба полных непрерывных покрытия, независимую проверку каждого листа, формальный отрицательный контроль и настоящие mixed/transpose тела. Он не импортирует родительский исходник и не требует внешних файлов данных.

Исполненная среда: CPython 3.13.5, SymPy 1.14.0; assertions включены. Все доказательные вычисления рациональные. Seed и параметры численного оптимизатора отсутствуют. Обычный и отдельный source-only холодный запуск дали побайтово одинаковые JSON и stdout.

    b_root_corner_mixed_sign_v4.py
    14603 bytes
    SHA256 52b7deee96b16fc1408c563b65dba24486fd8821000354031eacea3f9a8d3581

    b_root_corner_mixed_sign_v4.json
    315155 bytes
    SHA256 0a8de2c63247841e35d3237e281520aa8a5f927177be8c273d8a1fe3504d9e3f

    b_root_corner_mixed_sign_v4.out
    550 bytes
    SHA256 4afc663f7f1df144d6eb3f35c2f8136148b14162d3c62d0075211203e6e41e21

Команды после сохранения полного Python-блока с LF:

    python b_root_corner_mixed_sign_v4.py > b_root_corner_mixed_sign_v4.out
    sha256sum b_root_corner_mixed_sign_v4.py b_root_corner_mixed_sign_v4.json b_root_corner_mixed_sign_v4.out

Полный ожидаемый stdout:

    SIGN_FREE_ROOT_AND_DETERMINANT_ONE_NEGATIVE_MARK_ALGEBRA_PASS
    CUBE tau=51/25 one_nonpositive=False leaves=1042 depth=31 negative_coefficients=88170
    CUBE tau=101/50 one_nonpositive=True leaves=1502 depth=36 negative_coefficients=125234
    ALL_CLOSED_CUBES_INDEPENDENT_BINOMIAL_REPLAY_PASS
    ACTUAL_MIXED_10_15_7_AND_TRANSPOSE_TWO_POSITIVE_VOLUME_FANS_PASS
    FORMAL_201_OVER_100_TEN_POLYNOMIAL_CONTROL_NOT_A_BODY_PASS
    report_bytes=315155
    report_sha256=0a8de2c63247841e35d3237e281520aa8a5f927177be8c273d8a1fe3504d9e3f
    B_ROOT_CORNER_MIXED_SIGN_V4_RECOVERY_PASS

Дополнительные удобные копии: исходник (`b_root_corner_mixed_sign_v4.py`), полный точный отчёт (`b_root_corner_mixed_sign_v4.json`), stdout (`b_root_corner_mixed_sign_v4.out`). Они не заменяют следующий полный источник.

```python
#!/usr/bin/env python3
"""B_ROOT_CORNER_MIXED_SIGN_V4. CPython 3.13.5; SymPy 1.14.0.
Parent minimum-0167, SHA256
54d717262bdd7d55643e5593eeeac441afce686e14a736e3f128ad80a25c2d62.
Standalone exact inputs, two complete closed-cube covers, and genuine bodies.
No external data, RNG, numerical optimizer, or inherited code.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from functools import lru_cache, cmp_to_key
from math import comb, prod, lcm
from pathlib import Path
import hashlib
import json
import sympy as S


def rat(x):
    x = S.Rational(x)
    return Q(int(x.p),int(x.q))


def expressions(e,A,c,T,negative):
    # e=eta, A=alpha/mu, c=chi, NOT the canonical endpoint c.
    H=2*e+c; h=A+H; sig=A+2*e; D=(1+e)*(4+e)**2
    f=[4-A-e,4*(4-e*e)-(4+e)*A,h-2*T,
       27*H*(4-c)-T*T*D,h*(1+e)-3*H,81*H-T*D,
       (h*(1+e)-3*H)*(81*H-T*D)-9*H*(1+e)*(A+e)*(h-3)**2,
       T*T*h**3*D-27*H*sig*(sig*h+4*T*c)*(4*T-h),
       (4*h*(1+e)-2*H*(4+e))*(81*H-T*D)
       -(A+e)*(1+e)*(h-3)*(27*H*h-T*D)]
    if negative:
        f.append(h*T*(4*T-h+4*T*c)-sig*(4*T-h)**2)
    return f


def algebra():
    e,A,c,h,H,Z,T,k,s,p,u,v,C,D=S.symbols(
        'e A c h H Z T k s p u v C D',positive=True)
    rho0=(h-3)**2/(3*h*(3-Z)); w=3*H/(h*(1+e))
    rootn=3*(A+e)*rho0/4+(A+e)*(h-3)/(4*h)
    assert S.factor(rootn-(A+e)*(h-3)*(h-Z)/(4*h*(3-Z)))==0
    assert S.factor(S.diff((h-Z)/(3-Z),Z)-(h-3)/(3-Z)**2)==0
    De=(1+e)*(4+e)**2; z0=T*De/(27*H)
    ff=expressions(e,A,c,T,True); sub={H:2*e+c,h:A+2*e+c}
    vc=(3*h*(1+e)*(3-Z)*(1-w-(A+e)*rho0)).subs(Z,z0)*9*H
    nc=(4*h*(1+e)*(3-Z)*(1-rootn-w*(4+e)/6)).subs(Z,z0)*27*H
    assert S.factor(vc.subs(sub)-ff[6])==0
    assert S.factor(nc.subs(sub)-ff[8])==0
    hb=((s+C)*u+(s+D)*v)/(u+v); hc=2*s+C+D-hb
    assert S.factor(hb*hc-(s+C)*(s+D)-(C-D)**2*u*v/(u+v)**2)==0
    assert S.expand((s+C)*(s+D)-s*s-s*(C+D)-C*D)==0
    z=S.symbols('z',positive=True)
    j=z*z*De-27*k*H*(4*z-h)
    assert S.factor(S.diff(j,z)-2*z*De*(1-2*27*k*H/(z*De)))==0
    assert S.factor(S.diff(z/(4*z-h),z)+h/(4*z-h)**2)==0
    assert S.expand(16*(4*e*e-7*e+16)-(8*e-7)**2-207)==0
    pcap=T/(4*T-h)
    assert S.factor((h*pcap*(1+4*pcap*c)-s)*(4*T-h)**2
                    -(h*T*(4*T-h+4*T*c)-s*(4*T-h)**2))==0
    # Mixed signs force c>d without any geometric inference.
    r,q,s,c,d=S.symbols('r q s c d')
    GC=s+d-r-q*c; GD=s+c-r-q*d
    assert S.expand(GD-GC-(c-d)*(1+q))==0
    return {'determinant_floor_sign_independent':True,
            'root_interval_sign_independent':True,
            'discarded_parent_sign_conditions':['p*(1+chi)>=1','Z<=1+chi'],
            'one_nonpositive_mark_condition':'h*p*(1+4*p*chi)>sigma',
            'h_upper_when_T_ge_2':'8',
            'positive_quadratic_identity':'16*(4*eta^2-7*eta+16)=(8*eta-7)^2+207'}


def polynomials(tau,negative):
    x,y,z=S.symbols('x y z')
    out=[]
    for f in expressions(2*x,4*y,4*z,S.Rational(tau),negative):
        num,den=S.fraction(S.factor(f))
        assert den.is_Rational and den>0
        P=S.Poly(S.expand(num),x,y,z)
        degree=tuple(int(P.degree(t)) for t in (x,y,z))
        power={ij:rat(a) for ij,a in P.terms()}
        back=sum(S.Rational(a)*x**i*y**j*z**k for (i,j,k),a in power.items())
        assert S.expand(back-den*f)==0
        out.append((degree,power,rat(den)))
    return out


@lru_cache(None)
def positions(d):
    return tuple(product(*(range(n+1) for n in d)))


def bernstein(d,power):
    return [sum((a*prod(Q(comb(i,j),comb(n,j)) for i,j,n in zip(ix,ij,d))
                 for ij,a in power.items() if all(j<=i for i,j in zip(ix,ij))),Q(0))
            for ix in positions(d)]


@lru_cache(None)
def lines(d,axis):
    lookup={p:i for i,p in enumerate(positions(d))}; out=[]
    for p in product(*(range(n+1) if j!=axis else (0,) for j,n in enumerate(d))):
        row=[]
        for t in range(d[axis]+1):
            q=list(p);q[axis]=t;row.append(lookup[tuple(q)])
        out.append(tuple(row))
    return out


def split(b,d,axis):
    left,right=[Q(0)]*len(b),[Q(0)]*len(b)
    for inds in lines(d,axis):
        row=[b[i] for i in inds]; ll,rr=[row[0]],[row[-1]]
        while len(row)>1:
            row=[(a+c)/2 for a,c in zip(row,row[1:])]
            ll.append(row[0]);rr.append(row[-1])
        for i,a,c in zip(inds,ll,reversed(rr)):
            left[i],right[i]=a,c
    return left,right


@lru_cache(None)
def direct_axis(n,lo,hi):
    rows=tuple(tuple(sum((Q(comb(k,j)*comb(i,j),comb(n,j))*lo**(k-j)*(hi-lo)**j
                          for j in range(min(k,i)+1)),Q(0))
                     for i in range(n+1)) for k in range(n+1))
    den=lcm(*(c.denominator for row in rows for c in row))
    return tuple(tuple(int(c*den) for c in row) for row in rows),den


def direct_replay(d,power,path):
    box=[[Q(0),Q(1)] for _ in range(3)]
    for depth,bit in enumerate(path):
        axis=depth%3;lo,hi=box[axis];mid=(lo+hi)/2
        box[axis]=[lo,mid] if bit=='0' else [mid,hi]
    pairs=[direct_axis(n,*b) for n,b in zip(d,box)]
    tr=[p[0] for p in pairs]
    dp=lcm(*(a.denominator for a in power.values()))
    integer=[(ij,int(a*dp)) for ij,a in power.items()]
    den=dp*prod(p[1] for p in pairs)
    return [Q(sum(a*tr[0][i][x]*tr[1][j][y]*tr[2][k][z]
                  for (i,j,k),a in integer),den) for x,y,z in positions(d)]


def certificate(tau,negative,expected):
    pp=polynomials(tau,negative)
    initial={i:bernstein(d,p) for i,(d,p,den) in enumerate(pp)}; leaves=[]
    def rec(blocks,path):
        pending={}
        for i,b in blocks.items():
            if max(b)<0:
                other=direct_replay(pp[i][0],pp[i][1],path)
                assert other==b and all(c<0 for c in other)
                leaves.append([path,i,str(-max(b))]);return
            if min(b)<0:pending[i]=b
        assert pending,('UNCLOSED_BOX',path)
        assert len(path)<66,('DEPTH_LIMIT',path)
        cc={i:split(b,pp[i][0],len(path)%3) for i,b in pending.items()}
        for side in (0,1):rec({i:b[side] for i,b in cc.items()},path+str(side))
    rec(initial,'')
    paths={r[0] for r in leaves};assert len(paths)==len(leaves)
    prefixes={p[:i] for p in paths for i in range(len(p)+1)}
    def partition(p):
        if p in paths:
            assert not any(q!=p and q.startswith(p) for q in paths);return
        assert p+'0' in prefixes and p+'1' in prefixes
        partition(p+'0');partition(p+'1')
    partition('')
    assert sum((Q(1,2**len(p)) for p in paths),Q(0))==1
    counts=[sum(r[1]==i for r in leaves) for i in range(len(pp))]
    depth=max(map(len,paths));total=sum(prod(n+1 for n in pp[i][0]) for path,i,b in leaves)
    gap=min(Q(r[2]) for r in leaves)
    assert (len(leaves),depth,counts,total,str(gap))==expected
    return {'tau':tau,'one_nonpositive_mark':negative,'leaf_count':len(leaves),
            'maximum_depth':depth,'by_polynomial':counts,'negative_coefficients':total,
            'minimum_gap':str(gap),'leaves':leaves,
            'polynomials':[{'degree':list(d),'positive_scale':str(den),
                            'powers':[[*ij,str(a)] for ij,a in sorted(p.items())]}
                           for d,p,den in pp]}


def formal_control():
    v=expressions(Q(9,25),Q(82,25),Q(17,50),Q(201,100),True)
    expected=['9/25','738/625','8/25','23458473/78125000','3403/1250',
              '13240374/390625','7301025669/976562500',
              '265315300665201/9765625000000','188153732571/24414062500',
              '4258957/3125000']
    assert list(map(str,v))==expected and min(v)>0
    return {'eta':'9/25','alpha_over_mu':'82/25','chi':'17/50','T':'201/100',
            'ten_unscaled_residuals':expected,
            'status':'FORMAL THREE-VARIABLE RELAXATION ONLY; no body or moment completion asserted'}


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),Q(0))


def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


def det(a,b,c):
    return dot(a,cross(b,c))


def ordered_face(points,inds,normal):
    axes=[i for i in range(3) if i!=next(j for j in range(3) if normal[j])]
    center=[sum(points[i][j] for i in inds)/len(inds) for j in axes]
    vec={i:tuple(points[i][j]-c for j,c in zip(axes,center)) for i in inds}
    def half(v):return int(v[1]<0 or (v[1]==0 and v[0]<0))
    def compare(i,j):
        a,b=vec[i],vec[j]
        if half(a)!=half(b):return -1 if half(a)<half(b) else 1
        d=a[0]*b[1]-a[1]*b[0]
        assert d!=0 or i==j
        return -1 if d>0 else (1 if d<0 else 0)
    return tuple(sorted(inds,key=cmp_to_key(compare)))


def actual_control(transpose=False):
    # Constants followed by inward normal; every inequality is >=0.
    slacks=[(0,(1,0,0)),(0,(0,1,0)),(0,(0,0,1)),
            (100,(-99,-82,-90)),(4230,(-4013,-3299,-4230)),
            (2,(-2,0,15)),(23,(0,-23,45))]
    c,d=Q(9,50),Q(1,100);b=Q(1,10);alpha=1-b
    if transpose:
        slacks=[(s,(n[1],n[0],n[2])) for s,n in slacks];c,d=d,c
    slacks=[(Q(s),tuple(map(Q,n))) for s,n in slacks]
    vertices=set()
    for ids in combinations(range(7),3):
        ss=[slacks[i][0] for i in ids];ns=[slacks[i][1] for i in ids]
        den=det(*ns)
        if not den:continue
        cof=[cross(ns[1],ns[2]),cross(ns[2],ns[0]),cross(ns[0],ns[1])]
        p=tuple(-sum(ss[i]*cof[i][j] for i in range(3))/den for j in range(3))
        if min(s+dot(n,p) for s,n in slacks)>=0:vertices.add(p)
    canonical=[tuple(map(Q,p)) for p in [(0,0,0),(0,0,1),(0,1,0),(1,0,0)]]
    assert set(canonical)<=vertices
    points=canonical+sorted(vertices-set(canonical));cycles=[]
    for s,n in slacks:
        ids=[i for i,p in enumerate(points) if s+dot(n,p)==0]
        assert len(ids)>=3
        cycles.append(ordered_face(points,ids,n))
    found={}
    for i,j,k in combinations(range(len(points)),3):
        n=cross(sub(points[j],points[i]),sub(points[k],points[i]))
        if not any(n):continue
        z=dot(n,points[i]);v=[z-dot(n,p) for p in points]
        if min(v)<0<max(v):continue
        f=frozenset(i for i,a in enumerate(v) if a==0)
        found.setdefault(f,n)
    assert set(found)=={frozenset(c) for c in cycles}
    edges={tuple(sorted((c[j-1],c[j]))) for c in cycles for j in range(len(c))}
    assert edges=={tuple(sorted(f&h)) for f,h in combinations(found,2) if len(f&h)==2}
    assert (len(points),len(edges),len(cycles))==(10,15,7)
    for i in range(10):
        nn=[n for f,n in found.items() if i in f]
        assert any(det(*ns)!=0 for ns in combinations(nn,3))
    assert sum(1 in c for c in cycles)==3 and len(cycles[4])==3
    rb=[i for i in cycles[4] if i!=1]
    ell=lambda p:1+(d-1)*p[0]+(c-1)*p[1]-alpha*p[2]
    nn=lambda p:(1+b+c)*p[0]+(1+b+d)*p[1]
    assert all(ell(points[i])==0 for i in rb)
    assert sorted((points[i][0]==0,points[i][1]==0) for i in rb)==[(False,True),(True,False)]
    def fan(apex):
        V,E,N=Q(0),Q(0),Q(0);J=[Q(0)]*3
        for f in cycles:
            if apex in f:continue
            for j in range(1,len(f)-1):
                ids=(apex,f[0],f[j],f[j+1])
                vol=abs(det(*(sub(points[i],points[apex]) for i in ids[1:])))/6
                assert vol>0
                V+=vol;E+=vol*sum(ell(points[i]) for i in ids)/4
                N+=vol*sum(nn(points[i]) for i in ids)/4
                for k in range(3):J[k]+=vol*sum(points[i][k] for i in ids)/4
        return V,E,N,tuple(J)
    V,E,N,J=fan(0);assert (V,E,N,J)==fan(1)
    g=tuple(a/V for a in J);p=g[0]+g[1];mu=E/V;r=N/V;q=N/E;T=N/(6*V*E)
    G=[nn(a)-r-q*ell(a) for a in points]
    neg,pos=(3,2) if transpose else (2,3)
    assert G[neg]<0<G[pos] and min(G[4:])>0
    assert nn(points[rb[0]])==nn(points[rb[1]])==Q(47,50)
    assert G[1]+3*G[rb[0]]!=0
    for axis,endpoint in [(1,c),(0,d)]:
        face=[a for a in points if a[1-axis]==0]
        assert max((b+2*endpoint)*(a[axis]-1)-alpha*a[2] for a in face)==0
    chi=(c*g[0]+d*g[1])/(mu*p)
    weighted=g[0]*G[2]+g[1]*G[3]
    assert p*(1+chi)-1<0 and weighted>0
    # The positive-mark free facet is a real triangle, not a triangulation cell.
    fp=cycles[5]
    assert len(fp)==3 and set(fp)&set(range(4))=={pos} and min(G[i] for i in fp)>0
    area2=cross(sub(points[fp[1]],points[fp[0]]),sub(points[fp[2]],points[fp[0]]))
    assert any(area2)
    return {'transpose':transpose,'support_slacks':[[str(s),list(map(str,n))] for s,n in slacks],
            'vertices':[list(map(str,a)) for a in points],'facets':[list(f) for f in cycles],
            'edges':[list(e) for e in sorted(edges)],'f_vector':[10,15,7],
            'V':str(V),'E':str(E),'N':str(N),'J':list(map(str,J)),'g':list(map(str,g)),
            'T':str(T),'mu':str(mu),'chi':str(chi),'p':str(p),
            'G_vertices':list(map(str,G)), 'p_sign_bound_residual':str(p*(1+chi)-1),
            'weighted_G':str(weighted),'zeta':str(weighted/(r*p)),
            'B_triangle_residual':str(G[1]+3*G[rb[0]]),
            'positive_mark_triangle':list(fp),'positive_triangle_mean_G':str(sum(G[i] for i in fp)/3),
            'status':'ACTUAL UNIFORM MIXED-SIGN SIMPLE CORNER; NOT STATIONARY; mechanics not audited'}


def main():
    cs=[certificate('51/25',False,(1042,31,[0,7,29,348,1,0,62,397,198],88170,'3/16')),
        certificate('101/50',True,(1502,36,[0,7,18,523,1,0,57,574,273,49],125234,
                                 '1628892577475/17592186044416'))]
    controls=[actual_control(False),actual_control(True)]
    assert controls[0]['T']==controls[1]['T']
    report={'version':4,'parent_assignment':'minimum-0167',
            'algebra':algebra(),'certificates':cs,'formal_control':formal_control(),
            'actual_controls':controls}
    raw=(json.dumps(report,sort_keys=True,ensure_ascii=True,indent=2)+'\n').encode()
    Path('b_root_corner_mixed_sign_v4.json').write_bytes(raw)
    print('SIGN_FREE_ROOT_AND_DETERMINANT_ONE_NEGATIVE_MARK_ALGEBRA_PASS')
    for c in cs:
        print('CUBE tau='+c['tau']+' one_nonpositive='+str(c['one_nonpositive_mark'])+
              ' leaves='+str(c['leaf_count'])+' depth='+str(c['maximum_depth'])+
              ' negative_coefficients='+str(c['negative_coefficients']))
    print('ALL_CLOSED_CUBES_INDEPENDENT_BINOMIAL_REPLAY_PASS')
    print('ACTUAL_MIXED_10_15_7_AND_TRANSPOSE_TWO_POSITIVE_VOLUME_FANS_PASS')
    print('FORMAL_201_OVER_100_TEN_POLYNOMIAL_CONTROL_NOT_A_BODY_PASS')
    print('report_bytes='+str(len(raw)))
    print('report_sha256='+hashlib.sha256(raw).hexdigest())
    print('B_ROOT_CORNER_MIXED_SIGN_V4_RECOVERY_PASS')


if __name__=='__main__':
    main()
```
