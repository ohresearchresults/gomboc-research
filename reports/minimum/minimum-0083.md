# minimum-0083

AI research report · 2026-09-18 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# TILTED_ROOT_GRAPH_AND_IMBALANCE_V1

**Keen Raven 13 / slot-2.** Assignment `minimum-0083`; run `[internal-source-reference]`.

## 1. Основной результат

Получены два результата, не сводящиеся к неудаче оптимизатора.

**Новая общая исключённая область.** Для любой настоящей соседней треугольной пары ABC, ABD, любой ненулевой неотрицательной аффинной ell и её значений a,b,c,d в A,B,C,D положим M=max(a,b,c,d). Тогда

```text
T >= 51/25  =>  49|a-b| + 28|c-d| > M.                 (I)

T >= 51/25 и h <= 3/10
             =>  49|a-b| + 13|c-d| > M.                (II)
```

Здесь h=Vol(ABCD)/Vol(P). В частности, при c=d высокий след требует |a-b|>M/49 при ВСЕХ h. Вместе с принятой равноконцевой оценкой для h>=3/10 получаем также: при a=b высокий след требует |c-d|>M/13. Это усиливает прежнее отдельное необходимое условие |c-d|/M>63/20005; полная анизотропная равноконцевая задача этим не решена. В концевом случае a=b=0 непосредственно T=h(cg_x+dg_y)/(dg_x+cg_y)<=1, поскольку 1/4<=g_x,g_y<=1/(4h); поэтому исключение a=b>0 в нормировке прежнего endpoint-parent не оставляет здесь пробела.

**Точная редукция по настоящим графикам волокна.** При фиксированных проекции Omega, длине вертикального волокна L и наклонной функции ell весь бесконечный класс допустимых положений верхнего/нижнего графиков описывается конечным объединением многогранников параметров, рациональных при рациональных исходных данных. Максимизация T есть точная линейная оптимизация собственного первого момента Z на каждом из них. Условие настоящей корневой грани включается явно, а не теряется при симметризации.

Эта редукция полностью исполнена на новом двухпалаточном L: доказано, что все его допустимые положения с заданной настоящей корневой гранью образуют ровно один отрезок P_theta, 0<=theta<=1. В более общем из двух сохранённых контролей корень не содержит НИ A,B, НИ C,D; при этом

```text
T(P_0) < T(P_1/2) < 2 < T(P_1) < 51/25.
```

P_1/2 — настоящая вертикальная аффинная Steiner-симметризация P_1. Она сохраняет выбранную корневую плоскость как максимальную грань, обе настоящие треугольные грани, L, V, X,Y и их две конусные массы, но уменьшает T. Это точный отрицательный результат против сохранения или неуменьшения следа при такой операции ДАЖЕ ПОСЛЕ проверки сохранения корня. Он не опровергает приложенную другую симметризацию x<->y.

Ни T<=51/25 для всех наклонных корней, ни T(P)<=max(2,T(P')) при продлении C,D не доказаны и не опровергнуты. Новые тела не объявляются телами 110. Глобальная граница остаётся C>=34; счётчики FULL/LOCAL не меняются. Принятая исходная граница и открытый слой (10,17,9) зафиксированы в brief.

## 2. Источники и точная нормировка

Прочитан приложенный brief целиком. Для новых доказательств используются полностью прочитанные непрерывные источники:

* `material:[internal-source-reference]`, BALANCED_EDGE_ROOT_TRACE_V1, 26356 байт, SHA-256 `90382e7d0bfe3f38770fd33f5b488fe40bd5ce52f70ab48ccd6b883d371e188f`. Получен через read-only library целиком, cursor 0..17161, eof=true. Используется не только утверждение T<=2, но точная корне-усечённая функция из разделов 3–7.
* Приложенный JOINT_MASS_QUANTITATIVE_STABILITY_V1, 32383 байта, SHA-256 `af3463f771f6c72c11d5fbe3fe39c11ae80c8dbd31a798e74f460f2372a6671d`: радиальная выпуклость, массовые оценки, h>7/45 при высоком следе. Нужные аргументы содержатся в его приложении A и разделе 7.
* Приложенный ENDPOINT_CORRIDOR, SHA-256 `5b4c6f78a38746bd4a9843a184e68d6ba3dcd4a76dcf8e1e2832b1592b670745`: центроидная полоса и ранее закрытая равноконцевая область h>=3/10. Его старый конечный сертификат здесь повторно не запускался; ниже новый сертификат независим от его 3600 коэффициентов.

Для сравнения областей также полностью прочитан root-CD proof `material:[internal-source-reference]`, SHA-256 `38ebfd67777b2aa3069815a8c82eab614595b511ff4d6e445f4c1f5e09ffd2a7`, cursor 0..13493, eof=true. Его константа и старый вычислительный source не являются предпосылкой (I),(II). Формальный scalar barrier не декодировался и не использовался как тело. Ни FULL253, ни дискретные исключения, ни C650 не были скрытыми входами.

Выбираем канонические координаты

```text
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
P subset {x>=0,y>=0}, T0=conv(A,B,C,D) subset P,
V=Vol(P), X=int_P x, Y=int_P y, Z=int_P z,
h=1/(6V), (g_x,g_y,zeta)=(X,Y,Z)/V, s=g_x+g_y,
ell=a+(d-a)x+(c-a)y+(b-a)z,
mu=int_P ell/V,
T=h[(a+b+c)g_x+(a+b+d)g_y]/mu.
```

Последняя формула использует настоящие площадные центроиды треугольников и собственный объёмный COM. Для настоящего ell=0 это именно сумма двух Lambda, для вспомогательной неотрицательной функции — явно заданный функционал, не новая фиктивная грань. Такая область определения имеется и в приложенном parent.

## 3. Перенос наклона на том же теле

Переставляя A,B аффинным отражением z->1-x-y-z и при необходимости C,D перестановкой x,y, считаем a>=b, c>=d. Делим ell на M, так что M=1, и пишем

```text
alpha=a-b, epsilon=c-d, r=(1-h)/h.
```

Для всякой точки (x,y,z) тела сравнение с conv(T0,(x,y,z)) даёт

```text
1+(-z)_+ +(x+y+z-1)_+ <= 1/h,
```

откуда z+r>=0 на всём P. Это настоящий объём видимых пирамид T0, включая случай одновременной видимости обеих некоординатных граней.

Определим на НЕИЗМЕНЁННОМ P

```text
ell_plus = ell + alpha(z+r) + epsilon x
         = (a+alpha r)+(c-a)(x+y).
```

Она неотрицательна; её четыре значения равны (a+alpha r,a+alpha r,c+alpha r,c+alpha r). Нулевая плоскость ell_plus не обязана быть гранью. Никакая симметризация тела и никакое сохранение старого COM после изменения тела здесь не предполагаются.

Если T_plus есть её функционал, то ТОЧНО

```text
mu_plus-mu = alpha(zeta+r)+epsilon g_x,
T_plus mu_plus - T mu
  = h[alpha(1+3r)s + epsilon g_y].                     (3.1)
```

Поэтому из любого верхнего ограничения T_plus<k следует

```text
T < k + {alpha[k(zeta+r)-h(1+3r)s]
             +epsilon[k g_x-h g_y]}/mu.               (3.2)
```

Нужные общие моментные оценки:

```text
mu>=1/4,  g_x<=1/(4h),  g_y>=1/4,  s>=1/2,
zeta<=1/2-s+1/(4h).                                  (3.3)
```

Веер из вершины с ell=1 даёт первую оценку, веера из C,D — нижние координатные оценки. Для верхней координатной оценки применяется к настоящей базе ABC неравенство A0 int_K height <=3 Vol(K)^2/4; оно следует сравнением корня площади сечения с линейным пирамидальным профилем при равной массе. Для центроидной полосы разрезаем P при z=0: база нижней части содержит ACD и имеет площадь >=1/2, поэтому -int_(z<=0)z <=(3/2)(V-1/6)^2. Добавляем момент T0 и затем отражаем A,B. Это даёт (3.3) с собственными моментами каждой части, как в явном parent.

Из (3.2),(3.3) получается полезная самостоятельная общая оценка

```text
T < k + max(0, C_alpha(h,k) alpha+C_epsilon(h,k) epsilon),
C_alpha(h,k)=k(5/h-4)-6+4h,
C_epsilon(h,k)=k/h-h.                                (3.4)
```

Разбор знака обязателен: при неположительном числителе поправки уже T<k; только положительный числитель можно умножить на верхнюю оценку 1/mu<=4.

**Мост непосредственно к a=b направлению.** Можно НЕ добавлять epsilon x. Тогда ell_equal=ell+alpha(z+r) имеет лишь a_equal=b_equal, сохраняет c-d, а формулы (3.1),(3.2) содержат только alpha-слагаемое. Любая новая анизотропная равноконцевая оценка подставляется сюда без изменения P. Кроме того, для конкретного тела разрешено взять более точное r=-min_P z вместо (1-h)/h и сохранить реальные zeta,s в (3.2).

## 4. Усиленная равноконцевая оболочка и полный сертификат

Для двупарно-равной неотрицательной функции запишем ell_0=1-p(x+y), p<=1, когда её значение на A положительно. Обозначим её след T_bal. Нужное усиление parent имеет вид

```text
T_bal < min(2,U_49(h),U_28(h)),  7/45<=h<1,
T_bal < min(2,U_49(h),U_13(h)),  7/45<=h<=3/10,

U_49(h)=h(2649-100h)/[125(9h+1)],
U_28(h)=h(1428+25h)/[25(28h+1)],
U_13(h)=h(663+25h)/[25(13h+1)].                       (4.1)
```

### Геометрический вход (4.1)

Пусть L — настоящая длина вертикального волокна. На луче u задаём R(u)^2=6 int rL(ru)dr. Радиальное тело K={ru:0<=r<=R(u)} выпукло, содержит xy-треугольник OCD, Area(K)=3V. Максимум L в начале не требуется; соответствующее квантильное доказательство полностью имеется в указанном V1-parent.

Одномерное сравнение для вогнутой f>=0, f(0)=1, с сохранённым концом H даёт

```text
int_0^H r^2 f(r)dr <= (3/4)H int_0^H r f(r)dr-H^3/24.
```

Его доказательство: аффинный q с тем же интегралом с весом r неотрицателен; (f-q)/r невозрастает, поэтому разность имеет одну смену знака и её момент с дополнительным r неположителен. Положительное f(H) допускается.

При p>0 реальный корень ограничивает H<=1/[p(u_x+u_y)]. Поэтому, если A_K=Area(K), I=int_K(1-p(x+y))_+, то

```text
X+Y <= (A_K-I)/(4p),
int_P ell_0 >= (V+I)/4,
T_bal <= (3-p)(A_K-I)/[2p A_K(A_K/3+I)].              (4.2)
```

На K сечения выше x+y=1 имеют вогнутую длину. Сравнение при равной площади с треугольным профилем высоты 1/h даёт

```text
I >= (p^3-3p^2+3p-h)/[6p^2(1-h)]   при h<=p<=1.
```

Это сравнение убывающей функции (1-pt)_+ со всей длиной сечения, не предположение о четырёхугольности K. При p<=h, включая p<=0, получается T_bal<=1+h. В случае нулевого общего значения ell_0(A)=ell_0(B) имеем T_bal=h и тот же вывод.

При h<=p<=1 правая часть (4.2) равна Phi=N/D, где

```text
N=h(p-3)(-h^2+h p^3+3h p-3p^2),
D=p(-h^2+h p^3-4h p^2+3h p+p^2)>0.                   (4.3)
```

Неравенство T_bal<2 и случай h=1 уже доказаны полным balanced-parent. Новая конечная часть доказывает именно Phi<U_49,U_28,U_13 в заявленных областях, а не проверяет значения нескольких тел.

### Точный сертификат

Подставляем p=h+(1-h)u, 0<=u<=1. Если U_n=A_n/B_n в буквальном виде (4.1), то

```text
A_n D-B_n N = h(1-h) Q_n(h,u).
```

Каждый Q_n имеет степень (5,4). Все коэффициенты исходных Q, подстановка, проверка тождества и обратное раскрытие Bernstein-разложения содержатся в полном source ниже. Использованы следующие полные двоичные разбиения прямоугольников; биты поочерёдно делят h,u, начиная с h:

```text
Q49, [7/45,1]x[0,1]:
000000,00000100,00000101,0000011,00001,0001,001,01,1.

Q28, [7/45,1]x[0,1]:
0,10,110,1110,11110,11111.

Q13, [7/45,3/10]x[0,1]:
000000,000001,00001,0001,0010,0011,01,10,11.
```

Всего 24 ячейки, 720 строго положительных коэффициентов. Точные минимумы соответственно

```text
2100341747/50388480000,
7727/7200,
2025511/21870000.
```

Каждое из 24 разложений независимо развёрнуто обратно в степенной базис. Полнота покрытия проверена префиксным деревом. Поэтому Q_n>0 на всей соответствующей замкнутой области.

Для p<=h сравниваем U_n с 1+h. Числители разностей равны

```text
-1225h^2+1399h-125,
-675h^2+703h-25,
-300h^2+313h-25.
```

Они вогнуты и положительны на концах соответствующих интервалов; для третьего концевые значения 2218/135 и419/10. Следовательно (4.1) покрывает все p<=1. Строгость сохраняется при h<1; h=1 — непосредственно T0.

### Завершение (I),(II)

Берём k из (4.1) в (3.4). Точные эквивалентности:

```text
k+C_alpha(h,k)/49 <=51/25  iff k<=U_49(h),
k+C_epsilon(h,k)/n<=51/25  iff k<=U_n(h), n=28 или13.
```

На треугольнике alpha,epsilon>=0, 49alpha+n epsilon<=1 линейный функционал C_alpha alpha+C_epsilon epsilon не превосходит max(0,C_alpha/49,C_epsilon/n). Поэтому T<51/25 во всей заявленной области.

Если h<7/45, высокий след уже исключён принятым общим конусным хвостом: при ell(g)=1 имеем E(ell-u)_+<=(1-u/4)_+^4; Jensen по действительным двум центроидным пирамидам при u=11/8 исключает m1+m2<=13/15. Точный положительный запас в граничной точке равен 29035697/279130931200. Совместная масса m1+m2<=3(1+h)/4 даёт h>7/45. При h=1 непосредственно T=(2a+2b+c+d)/(a+b+c+d)<=2. Это завершает общие утверждения, без предположения о числе остальных вершин.

## 5. Полная конечная редукция настоящих верхнего и нижнего графиков

Пусть alpha=a-b>0, ell=E(x,y)-alpha z. Запишем

```text
P={(x,y,z):(x,y) in Omega, u(x,y)<=z<=v(x,y)},
u convex, v concave, L=v-u,
H=E/alpha,
V=int_Omega L, X=int_Omega xL, Y=int_Omega yL,
Z=int_Omega L(v-L/2),
B_ell=int_Omega E L-alpha Z.                          (5.1)
```

В отличие от a=b, положение середины волокна действительно входит в B_ell. При фиксированном L весь числитель T, V, X,Y, h и обе треугольные массы фиксированы. T строго возрастает по Z.

**Лемма конечности.** На любой выпуклой двумерной клетке, где L аффинна, u и v также аффинны. Действительно, дефицит равенства в вогнутости v и дефицит равенства в выпуклости u неотрицательны, а их сумма есть нулевой дефицит аффинной L. Оба дефицита нулевые на каждом отрезке клетки.

Берём конечное разбиение Omega на клетки D_i с L=L_i аффинной; при рациональных Omega,L разбиение выбирается рациональным. Для неизвестных аффинных v_i задаём следующие ЛИНЕЙНЫЕ условия во всех вершинах q клетки D_j:

```text
v_j(q)<=v_i(q)                 для всех i,j;
v_j(q)-L_j(q)>=v_i(q)-L_i(q)   для всех i,j;
v_j(q)<=H(q);
v_j(q)=1-x(q)-y(q)             на осях x=0 или y=0.   (5.2)
```

Первая группа делает v минимумом его опорных плоскостей; вторая делает u=v-L максимумом его опорных плоскостей. Они одновременно обеспечивают непрерывность на общих рёбрах клеток. Последняя группа сохраняет фактические осевые сечения точно ABC,ABD, а не расширенные многоугольники. Omega и L берутся от исходной настоящей пары, поэтому их осевые носители уже ровно OC,OD.

Настоящая корневая грань при alpha>0 имеет двумерную xy-проекцию. Следовательно она существует ТОГДА И ТОЛЬКО ТОГДА, когда v_i=H тождественно хотя бы на одной двумерной клетке. Таким образом весь класс с настоящим корнем есть конечное объединение систем (5.2), по одному дополнительному тройному аффинному равенству v_i=H на ветвь. Это не релаксация.

Каждая система компактна: она строит тело, содержащее T0, с фиксированным V; видимые пирамиды дают общие поточечные высотные границы -(6V-1)<=z<=6V-x-y. Они ограничивают коэффициенты каждой аффинной плоскости по трём неколлинеарным точкам клетки. Все условия замкнуты. Поэтому максимум линейного Z достигается; при рациональных данных достаточно рациональной вершины многогранника параметров.

Для сборки целевой функции достаточно точных интегралов L(1,x,y) и L^2 по каждой рациональной клетке. Полигональная триангуляция здесь служит только интегрированию. Восстановленное тело определяется плоскостями u_i,v_i и Omega; его максимальные грани заново объединяются в своих опорных плоскостях. Никакие диагонали клеток не становятся объявленными рёбрами тела.

Это также даёт интерфейс строгого сертификата: для желаемого tau проверяется линейная оценка

```text
Z <= [int E L-N/(6V tau)]/alpha
```

на каждой корневой ветви; точный допустимый двойственный вектор доказывает её для ВСЕХ положений волокон данного L. При a=b член alpha Z исчезает: равноконцевое планарное направление действительно не нуждается в этой дополнительной оптимизации.

## 6. Точный действительный пример и полная классификация его волокон

Положим Omega={x,y>=0,x+y<=1}, t=x+y, f=1-t и

```text
g1=min(20x,20y,t/160,203/600-t/3),
g2=min(20x,20y,t/16, 203/600-t/3),
L=f+g1+g2,

u_theta=-(1-theta)g2-theta g1,
v_theta=f+(1-theta)g1+theta g2,
P_theta={Omega, u_theta<=z<=v_theta}, 0<=theta<=1,

ell=1-(800/803)(x+y)-(600/803)z.
```

Это полное точное задание тела. Верхний график — минимум 16 явно заданных аффинных плоскостей, нижний — максимум 16 плоскостей; исходник перечисляет все их пересечения без плавающего допуска. Оба графика имеют требуемые выпуклость/вогнутость. На x=0 и y=0 g1=g2=0, поэтому настоящие максимальные грани в этих плоскостях в точности ABC и ABD, с настоящим общим ребром AB.

Корневые значения равны

```text
(a,b,c,d)=(1,203/803,3/803,3/803).
```

На области, где обе палатки равны 203/600-t/3, верхний график совпадает с (803-800t)/600. Область имеет положительную площадь. Значит 800x+800y+600z=803 — настоящая максимальная грань каждого P_theta, не содержащая ни одной из A,B,C,D. Причём 253(c+d)=1518/803>1: это не прежний малый sum-gap регион. Нужный коэффициент здесь и в принятом условии —253, не252.

### Почему это весь класс при данном L, а не только подобранная кривая

У L ровно семь двумерных аффинных клеток. Индексы активных плоскостей (g1,g2), считая порядок их четырёх плоскостей с нуля, равны

```text
(0,0),(1,1),(2,0),(2,1),(2,2),(2,3),(3,3).
```

Любой верхний график с тем же L аффинен на этих клетках. После вычитания f условия непрерывности и нулевых значений на осях дают однородную рациональную систему из19 уравнений на21 коэффициент. Выполнено точное RREF: ранг19, размерность ядра2. Два линейно независимых вектора, задаваемых g1,g2 на всех клетках, лежат в ядре. Поэтому любой такой верхний график имеет вид

```text
v=f+lambda g1+nu g2,
u_lower=-(1-lambda)g1-(1-nu)g2.
```

На ребре между клетками (2,3),(3,3) изгибается только g1; вогнутость верхнего и выпуклость нижнего дают 0<=lambda<=1. Аналогично ребро (2,2)|(2,3) даёт 0<=nu<=1. Общая cap-клетка (3,3) заставляет lambda+nu<=1 из ell>=0. При строгом неравенстве корневого двумерного нуля нет, поскольку cap=203/600-t/3>0 на Omega. Поэтому настоящий корень требует lambda+nu=1. Получен в точности theta-отрезок выше. Все клетки, вся система19x21 и оба вектора ядра восстанавливаются source; ранговое утверждение не является выводом численного LP.

### Собственные центроиды, следы и истинные комплексы

Для всего отрезка

```text
V=17797628724033/95914090000000,
h=47957045000000/53392886172099,
g_x=g_y=215429480342292151/826788842374953015,
g_z(theta)=(14922897868352197783
            +1828594798525101474 theta)
           /66143107389996241200.
```

Последний коэффициент строго положителен. Поскольку B_ell линейно убывает по theta, T строго возрастает и

```text
1/T(theta)=(1-theta)/T(0)+theta/T(1),

T(0)=51162422255950122058658548000000
     /27161916092044512597428777461917,
T(1/2)=4169737413859934947780671662000000
       /2140470696052220491162131311215791,
T(1)=438919727774729994503228596000000
     /217604761116085600593033395714247.
```

Приближённо это 1.8836087293, 1.9480469513, 2.0170502039. Точный максимум по ВСЕМ допустимым положениям волокон данного L с этим настоящим корнем равен последней дроби, а не результату оптимизатора.

Для theta=0,1/2,1 независимо реконструированы истинные f-векторы соответственно (12,21,11), (16,31,17), (12,21,11). Вычислены собственные площадные центроиды всех максимальных граней, объёмные COM и вся физическая Lambda. Проверены Lambda*1=3*1, Lambda*Q=-Q, Lambda^2+Lambda=4*1*d^T, sum d=3 и настоящий баланс площадных центроидов. Изменение числа граней при сдвигах не скрывается.

Аффинная вертикальная Steiner-симметризация центрирует волокна в плоскости z=(1-x-y)/2 и переводит P_1 в P_1/2. Настоящий корень сохраняется на общей cap-клетке, но T падает через2. Это не касается принятой x<->y симметризации, которая сохраняет другой набор моментов и для которой в parent доказано сохранение следа.

Сохранён и более простой non-record контроль: заменить в обоих палаточных cap 203/600-t/3 на (1-t)/3, а t/160 в g1 на t/1000. Тогда ell=1-t-3z/4, корень содержит C,D; та же точная классификация даёт 21 коэффициент, ранг19, размерность2. Максимум равен 1503959363759153290543/741914692015700017221>2, а симметризованный след равен 28575227911423912520317/14641912611956997724335<2. Истинные f-векторы трёх контролей (8,16,10), (12,26,16), (8,16,10). Это не рекорд и не заменяет более общий положительный-gap пример.

## 7. Реальный контроль новой исключённой области

Другой точный семивершинный контроль — T0 и

```text
(7/10,143/80,-1/5),
(17/10,153/200,-3/10),
(6/5,509/400,-1/10),
ell=1-41x/100-2y/5-z/100.
```

Его корневая грань — настоящий треугольник трёх добавленных точек; ABC,ABD — настоящие максимальные треугольники. Значения (1,99/100,3/5,59/100) дают

```text
h=2000/8679 in (7/45,3/10),
49alpha+13epsilon=31/50,
V=2893/4000,
g=(49499/86790,16553683/27772800,605/4208),
T=20933318335/15857756739,
новая верхняя оценка (3.4)=114725307579/62703966875<51/25.
```

Таким образом контроль лежит в реальной низко-h части новой области, а не в уже исключённом h<=7/45 секторе. Его полный максимальный комплекс и оба точных приращения (3.1) проверены. Изменялась функция на одном P, не тело; собственный COM для этой операции действительно остаётся тем же.

## 8. Связь с одной общей матрицей и дальнейшая работа

Для настоящих треугольников i=ABC,j=ABD в одной геометрии

```text
d_i=(Lambda^2)_ii/4, d_j=(Lambda^2)_jj/4,
h=sqrt(Lambda_ij Lambda_ji).
```

Это именно принятая физическая связь, не свободный выбор масс. При нормировке ell(g)=1 имеем

```text
c-d=3(Lambda_ai/d_i-Lambda_aj/d_j).
```

Поэтому (I) становится связанным необходимым условием

```text
49|ell(A)-ell(B)|
 +84|Lambda_ai/d_i-Lambda_aj/d_j|
 > max(ell(A),ell(B),ell(C),ell(D)),
```

а при h<=3/10 число84 заменяется39. Значения в вершинах относятся к ТОЙ ЖЕ root-row и ТОЙ ЖЕ инцидентной геометрии. Удалять их и произвольно выбирать правую часть нельзя.

В построенном волоконном примере фиксированы даже оба d_i,d_j и обе взаимные Lambda_ij,Lambda_ji, но корневые Lambda_ai,Lambda_aj изменяются через собственный z-COM. Это показывает конкретно, какой общий геометрический момент должен сохраняться при соединении планарного a=b направления с полной матрицей.

Самое полезное продолжение — использовать (3.2) без epsilon-поправки с новой анизотропной равноконцевой оболочкой, а оставшуюся свободу середины волокон устранять точной системой (5.2), а не симметризацией с неподтверждённым сохранением root-row. Для каждого перспективного L можно получить рациональный двойственный сертификат максимального Z, после чего искать или доказывать ограничения уже на сам L.

## 9. Попытки, отрицательные методы и границы

До доказательной части проверялись: усечение C,D у известного высокого root-CD тела; свободные три точки настоящего корневого многоугольника при произвольных p,q и наклоне; поиск T(P)>max(2,T(P')) при T(P)>=2.001. Первый поиск вернулся к отсутствию усечения. Второй дал приблизительно2.0287828758615007 при p=q=1 и почти осевых точках. Третий подошёл к разности T(P')-T(P) примерно2.6e-13, то есть не дал строгого контрпримера. Это ограниченные численные попытки, не исключения непрерывных классов и не новые точные рекорды. Их полный самостоятельный source с seed713/714 и всеми параметрами сохранён ниже; доказательный source его не импортирует.

Известное опровержение безусловного T(P')>=T(P) при продлении C,D остаётся в своей прежней области, где оба следа<2; оно не доказывает отрицание слабой версии. Новый пример здесь относится к ДРУГОЙ операции — изменению верхнего/нижнего графиков при фиксированном L.

Внешне проверена библиографическая основа affine cone-volume concentration: Freyer–Henk–Kipp, arXiv:2207.08477. Авторы указывают расширение на произвольные центрированные многогранники. Этот внешний источник не подменяет приведённые доказательства моментных оценок и не используется для новых численных констант; историческая новизна и внешняя рецензия не заявляются.

## 10. Самодостаточная recovery-капсула

Ни один новый объект не опирается только на sandbox или на один хеш. Ниже приведены оба ПОЛНЫХ исходника. Первый реконструирует все720 коэффициентов с обратной проверкой, обе полные системы графиков, семь настоящих тел, максимальные грани/настоящие рёбра, собственные центроиды, полные физические Lambda и все точные сравнения. Второй сохраняет исключённые из доказательства поиски.

Точные файлы UTF-8/LF с конечным LF:

```text
tilted_root_exact.py:15016 bytes,
SHA256 9a2d20024a128d43474f6430eddb6d8f684b8b2c49efff7bb0aa5dfcc4ec1f3b.
tilted_root_explore.py:2279 bytes,
SHA256 8f8302e33e2d4ba8c0df0f2664aae42b56d142db6d78d51367ec4942b9da22f6.
```

Доказательный запуск, CPython3.13.5, только стандартная библиотека, assertions включены:

```text
python -S tilted_root_exact.py build
python -S tilted_root_exact.py check
```

Выход `tilted_root_exact.json`:101701байт, SHA-256 `fe59580182b354de19b96876c1ee1e679bd86ec171cb2ef4c1bd2c6f3760a081`.

```text
BALANCED_ENVELOPE_EXACT_BERNSTEIN_PASS 3 24 720
FIXED_CHORD_GRAPH_SPACE_EXACT_PASS 2 21 19 2
TRUE_ROOT_STEINER_TRACE_DROP_PASS 2
NEW_LOW_VOLUME_TILTED_REGION_PHYSICAL_PASS 2000/8679
TILTED_ROOT_EXACT_RECOVERY_PASS 101701 fe59580182b354de19b96876c1ee1e679bd86ec171cb2ef4c1bd2c6f3760a081
```

Обе команды исполнены; затем один полный доказательный source перенесён в новый каталог, обе команды повторены, выходы побайтно совпали. Дополнительно самостоятельный восстановитель с обоими полными source-байтами перенесён в третий чистый каталог, распаковал исходники и повторил build/check с тем же результатом. Исследовательские general/weak/shrink заново исполнены отдельным сохранённым source под CPython3.13.5, NumPy2.3.5, SciPy1.17.0, OPENBLAS_NUM_THREADS=1; их результаты не включены в доказательство.

Копии для удобства: доказательный source (`tilted_root_exact.py`), поисковый source (`tilted_root_explore.py`), точный выход (`tilted_root_exact.json`). Содержание для восстановления полностью включено далее.

### tilted_root_exact.py

```python
# TILTED_ROOT_GRAPH_AND_IMBALANCE_V1; CPython 3.13.5, standard library only.
# Mathematical parent: material:[internal-source-reference],
# SHA256 90382e7d0bfe3f38770fd33f5b488fe40bd5ce52f70ab48ccd6b883d371e188f.
# No imported parent source, credential, random seed, or optimizer is needed.
# Run with assertions: python -S tilted_root_exact.py build; then check.
import json,hashlib,sys
from pathlib import Path
assert __debug__

from fractions import Fraction as F
from math import comb

def C(x):return {} if not x else {(0,0):F(x)}
def add(*ps):
    q={}
    for p in ps:
        for k,a in p.items():q[k]=q.get(k,F(0))+a
    return {k:a for k,a in q.items() if a}
def scale(p,a):return {k:a*b for k,b in p.items() if a*b}
def mul(p,q):
    r={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():r[i+k,j+l]=r.get((i+k,j+l),F(0))+a*b
    return {k:a for k,a in r.items() if a}
def pw(p,n):
    r=C(1)
    for _ in range(n):r=mul(r,p)
    return r
def evaluate(p,x,y):return sum(a*x**i*y**j for (i,j),a in p.items())
def local(p,box):
    l,r,b,t=box;q={}
    for (i,j),a in p.items():
        for k in range(i+1):
            for z in range(j+1):
                w=a*comb(i,k)*l**(i-k)*(r-l)**k*comb(j,z)*b**(j-z)*(t-b)**z
                q[k,z]=q.get((k,z),F(0))+w
    return {k:a for k,a in q.items() if a}
def bernstein(p,box):
    q=local(p,box);n,m=5,4
    B=[[sum(q.get((k,z),F(0))*F(comb(i,k),comb(n,k))*F(comb(j,z),comb(m,z))
             for k in range(i+1) for z in range(j+1)) for j in range(m+1)] for i in range(n+1)]
    back={}
    for i in range(n+1):
        for j in range(m+1):
            for k in range(i,n+1):
                for l in range(j,m+1):
                    a=B[i][j]*comb(n,i)*comb(n-i,k-i)*(-1)**(k-i)*comb(m,j)*comb(m-j,l-j)*(-1)**(l-j)
                    back[k,l]=back.get((k,l),F(0))+a
    assert {k:a for k,a in back.items() if a}==q
    assert min(x for row in B for x in row)>0
    return B

QM=[
 [[0,0,-1125,3024,0],[0,-1125,7644,-12994,2524],[-375,11567,-31032,30787,-8797],
  [4322,-26963,50982,-39588,11247],[-5074,21421,-33819,23671,-6199],[1225,-4900,7350,-4900,1225]],
 [[0,0,-225,1503,0],[0,-225,2643,-6518,1403],[-75,5224,-14979,16139,-4884],
  [2134,-13911,26979,-21436,6234],[-2728,11612,-18468,13012,-3428],[675,-2700,4050,-2700,675]],
 [[0,0,-225,738,0],[0,-225,1428,-3053,638],[-75,2479,-6834,7319,-2214],
  [964,-6231,12084,-9631,2814],[-1213,5177,-8253,5827,-1538],[300,-1200,1800,-1200,300]]]
CODES=[
 ['000000','00000100','00000101','0000011','00001','0001','001','01','1'],
 ['0','10','110','1110','11110','11111'],
 ['000000','000001','00001','0001','0010','0011','01','10','11']]
MINS=[F(2100341747,50388480000),F(7727,7200),F(2025511,21870000)]

def certificates():
    h={(1,0):F(1)};u={(0,1):F(1)};one=C(1);p=add(h,mul(add(one,scale(h,-1)),u))
    N=mul(mul(h,add(p,C(-3))),add(scale(pw(h,2),-1),mul(h,pw(p,3)),scale(mul(h,p),3),scale(pw(p,2),-3)))
    D=mul(p,add(scale(pw(h,2),-1),mul(h,pw(p,3)),scale(mul(h,pw(p,2)),-4),scale(mul(h,p),3),pw(p,2)))
    out=[]
    for index,n in enumerate([49,28,13]):
        hi=F(3,10) if n==13 else F(1)
        un=mul(h,add(C(51*n+150),scale(h,-100))) if n==49 else mul(h,add(C(51*n),scale(h,25)))
        ud=scale(add(scale(h,n-4),C(5)),25) if n==49 else scale(add(scale(h,n),one),25)
        q={(i,j):F(a) for i,row in enumerate(QM[index]) for j,a in enumerate(row) if a}
        assert add(mul(un,D),scale(mul(ud,N),-1))==mul(mul(h,add(one,scale(h,-1))),q)
        small=add(un,scale(mul(add(one,h),ud),-1))
        assert all(j==0 and i<=2 for i,j in small) and small.get((2,0),F(0))<0
        ends=[evaluate(small,F(7,45),F(0)),evaluate(small,hi,F(0))];assert min(ends)>0
        codes=set(CODES[index])
        def cover(s):
            if s in codes:return
            assert any(c.startswith(s) for c in codes)
            cover(s+'0');cover(s+'1')
        cover('');cells=[]
        for code in CODES[index]:
            box=[F(7,45),hi,F(0),F(1)]
            for k,bit in enumerate(code):
                ax=k%2;mid=(box[2*ax]+box[2*ax+1])/2
                box[2*ax+(1 if bit=='0' else 0)]=mid
            B=bernstein(q,box);cells.append(dict(code=code,box=box,B=B))
        mm=min(x for c in cells for row in c['B'] for x in row);assert mm==MINS[index]
        out.append(dict(n=n,Q=QM[index],uncut_endpoints=ends,minimum=mm,cells=cells))
    assert sum(len(c['cells']) for c in out)==24
    return out

def envelope(h,low=False):
    n=13 if low else 28
    return min(F(2),h*(2649-100*h)/(125*(9*h+1)),h*(51*n+25*h)/(25*(n*h+1)))

from fractions import Fraction as F
from itertools import combinations,product
from math import gcd,lcm

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def plane(n,d):
    z=tuple(map(F,(*n,d)));den=lcm(*(a.denominator for a in z))
    a=tuple(int(x*den) for x in z);g=gcd(*a)
    return tuple(F(x//g) for x in a)
def vertices(H):
    H=sorted(set(plane(h[:3],h[3]) for h in H));pts=set()
    for a,b,c in combinations(H,3):
        ns=[a[:3],b[:3],c[:3]];ds=(a[3],b[3],c[3]);dd=det(*ns)
        if not dd:continue
        cols=list(zip(*ns));p=tuple(det(*(ds if j==k else cols[j] for j in range(3)))/dd for k in range(3))
        if all(dot(q[:3],p)<=q[3] for q in H):pts.add(p)
    return sorted(pts)
def hull(P):
    P=[tuple(map(F,p)) for p in P];faces={}
    for i,j,k in combinations(range(len(P)),3):
        n=cross(sub(P[j],P[i]),sub(P[k],P[i]));d=dot(n,P[i])
        if not any(n):continue
        ss=[dot(n,p)-d for p in P]
        if min(ss)<0<max(ss):continue
        if max(ss)>0:n=tuple(-x for x in n);d=-d
        H=plane(n,d);ids=tuple(i for i,p in enumerate(P) if dot(H[:3],p)==H[3]);faces[ids]=H
    facets=sorted(faces);H=[faces[f] for f in facets]
    for i in range(len(P)):
        normals=[H[j][:3] for j,f in enumerate(facets) if i in f]
        assert any(det(*q)!=0 for q in combinations(normals,3)),('nonvertex',i)
    edges=sorted({tuple(sorted(set(a)&set(b))) for a,b in combinations(facets,2) if len(set(a)&set(b))==2})
    assert len(P)-len(edges)+len(facets)==2
    cycles=[]
    for f in facets:
        adj={i:sorted(j if i==k else k for j,k in edges if i in (j,k) and j in f and k in f) for i in f}
        assert all(len(q)==2 for q in adj.values())
        cyc=[min(f)];pr=None;cu=cyc[0]
        while True:
            nx=next(j for j in adj[cu] if j!=pr)
            if nx==cyc[0]:break
            assert nx not in cyc
            cyc.append(nx);pr,cu=cu,nx
        assert len(cyc)==len(f);cycles.append(cyc)
    ref=tuple(sum(p[k] for p in P)/len(P) for k in range(3));V=F(0);M=[F(0)]*3
    cen=[];area=[]
    for cyc,hh in zip(cycles,H):
        kk=next(k for k in range(3) if hh[k]);aa=F(0);cc=[F(0)]*3
        for i in range(1,len(cyc)-1):
            tri=[P[j] for j in (cyc[0],cyc[i],cyc[i+1])]
            vv=abs(det(*(sub(p,ref) for p in tri)))/6;V+=vv
            for k in range(3):M[k]+=vv*(ref[k]+sum(p[k] for p in tri))/4
            at=abs(cross(sub(tri[1],tri[0]),sub(tri[2],tri[0]))[kk]);aa+=at
            for k in range(3):cc[k]+=at*sum(p[k] for p in tri)/3
        cen.append(tuple(x/aa for x in cc));area.append(aa/(2*abs(hh[kk])))
    assert V>0;g=tuple(x/V for x in M)
    sl=[hh[3]-dot(hh[:3],g) for hh in H];assert min(sl)>0
    mass=[aa*ss/V for aa,ss in zip(area,sl)]
    Lam=[[mass[j]*(H[i][3]-dot(H[i][:3],cen[j]))/sl[i] for j in range(len(H))] for i in range(len(H))]
    assert sum(mass)==3
    for i in range(len(H)):
        assert Lam[i][i]==0 and sum(Lam[i])==3
        for j in range(len(H)):
            assert sum(Lam[i][k]*Lam[k][j] for k in range(len(H)))+Lam[i][j]==4*mass[j]
        for k in range(3):
            assert sum(Lam[i][j]*H[j][k]/sl[j] for j in range(len(H)))==-H[i][k]/sl[i]
    assert all(sum(mass[i]*cen[i][k] for i in range(len(H)))==3*g[k] for k in range(3))
    return dict(points=P,facets=facets,edges=edges,H=H,V=V,g=g,facet_centroids=cen,mass=mass,Lambda=Lam)
def audit(P,nodes):
    out=hull(P);P=out['points'];a,b,c,d=map(F,nodes)
    ell=lambda p:a+(d-a)*p[0]+(c-a)*p[1]+(b-a)*p[2]
    assert min(map(ell,P))>=0
    A=P.index((F(0),F(0),F(0)));B=P.index((F(0),F(0),F(1)))
    C=P.index((F(0),F(1),F(0)));D=P.index((F(1),F(0),F(0)))
    f1=tuple(sorted((A,B,C)));f2=tuple(sorted((A,B,D)))
    assert f1 in out['facets'] and f2 in out['facets'] and tuple(sorted((A,B))) in out['edges']
    root=tuple(i for i,p in enumerate(P) if ell(p)==0)
    assert root in out['facets'];ri=out['facets'].index(root)
    ii=out['facets'].index(f1);jj=out['facets'].index(f2)
    V=out['V'];g=out['g'];mu=ell(g);h=1/(6*V)
    T=((a+b+c)*g[0]+(a+b+d)*g[1])/(6*V*mu)
    assert T==out['Lambda'][ri][ii]+out['Lambda'][ri][jj]
    assert out['Lambda'][ii][jj]*out['Lambda'][jj][ii]==h*h
    out.update(nodes=tuple(map(F,nodes)),root=root,triangles=(f1,f2),T=T,h=h,mu=mu)
    return out

def val(f,p):return f[0]+f[1]*p[0]+f[2]*p[1]
def turn(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def hull2(P):
    P=sorted(set(P));lo=[];hi=[]
    for arr,seq in [(lo,P),(hi,P[::-1])]:
        for p in seq:
            while len(arr)>1 and turn(arr[-2],arr[-1],p)<=0:arr.pop()
            arr.append(p)
    return lo[:-1]+hi[:-1]
def cell2(H):
    pts=[]
    for a,b in combinations(H,2):
        de=a[1]*b[2]-a[2]*b[1]
        if not de:continue
        p=((a[2]*b[0]-a[0]*b[2])/de,(a[0]*b[1]-a[1]*b[0])/de)
        if all(val(q,p)>=0 for q in H):pts.append(p)
    poly=hull2(pts)
    return poly if len(poly)>=3 else []
def rref_rank(A):
    A=[list(r) for r in A];i=0
    for j in range(len(A[0])):
        k=next((k for k in range(i,len(A)) if A[k][j]),None)
        if k is None:continue
        A[i],A[k]=A[k],A[i];a=A[i][j];A[i]=[v/a for v in A[i]]
        for k in range(len(A)):
            if k!=i and A[k][j]:
                z=A[k][j];A[k]=[v-z*w for v,w in zip(A[k],A[i])]
        i+=1
        if i==len(A):break
    return i

def tents(e,beta1):
    cap=(F(1,3)+e,F(-1,3),F(-1,3))
    return [[(F(0),F(20),F(0)),(F(0),F(0),F(20)),(F(0),b,b),cap] for b in [beta1,F(1,16)]]

def graph_space(e,beta1):
    g=tents(e,beta1);f=(F(1),F(-1),F(-1));cells=[]
    for i,j in product(range(4),repeat=2):
        H=[(F(0),F(1),F(0)),(F(0),F(0),F(1)),f]
        H +=[sub(q,g[0][i]) for q in g[0]]+[sub(q,g[1][j]) for q in g[1]]
        pp=cell2(H)
        if pp:cells.append(dict(pair=(i,j),H=H,polygon=pp))
    assert [c['pair'] for c in cells]==[(0,0),(1,1),(2,0),(2,1),(2,2),(2,3),(3,3)]
    area=sum(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(c['polygon'],c['polygon'][1:]+c['polygon'][:1]))/2 for c in cells)
    assert area==F(1,2)
    pts=sorted({p for c in cells for p in c['polygon']});m=3*len(cells);eq=[]
    for p in pts:
        inc=[i for i,c in enumerate(cells) if all(val(q,p)>=0 for q in c['H'])]
        for i in inc[1:]:
            row=[F(0)]*m
            for k,x in enumerate((F(1),*p)):row[3*i+k]+=x;row[3*inc[0]+k]-=x
            eq.append(row)
        if p[0]==0 or p[1]==0:
            row=[F(0)]*m
            for k,x in enumerate((F(1),*p)):row[3*inc[0]+k]=x
            eq.append(row)
    rank=rref_rank(eq);assert (m,len(eq),rank)==(21,19,19)
    basis=[[a for c in cells for a in g[v][c['pair'][v]]] for v in [0,1]]
    assert rref_rank(basis)==2 and all(dot(row,v)==0 for row in eq for v in basis)
    return dict(cells=cells,vertices=pts,equations=eq,basis=basis,rank=rank,dimension=m-rank)

def fiber_family(theta,e,beta1):
    theta=F(theta);f=(F(1),F(-1),F(-1));gs=tents(e,beta1)
    H=[(-1,0,0,0),(0,-1,0,0),(1,1,0,1)]
    for u,v in product(gs[0],gs[1]):
        up=tuple(f[i]+(1-theta)*u[i]+theta*v[i] for i in range(3))
        lo=tuple((1-theta)*v[i]+theta*u[i] for i in range(3))
        H.extend([(-up[1],-up[2],1,up[0]),(-lo[1],-lo[2],-1,lo[0])])
    alpha=1/(F(4,3)+e)
    return audit(vertices(H),(1,1-alpha,alpha*e,alpha*e))

def transfer_control(out):
    a,b,c,d=out['nodes'];assert a>=b and c>=d and max(a,b,c,d)==1
    h=out['h'];V=out['V'];x,y,z=out['g'];mu=out['mu'];T=out['T'];s=x+y
    al=a-b;ep=c-d;r=(1-h)/h
    assert all(p[2]+r>=0 for p in out['points'])
    assert mu>=F(1,4) and x<=1/(4*h) and y>=F(1,4) and s>=F(1,2)
    assert z<=F(1,2)-s+1/(4*h)
    aa=a+al*r;cc=c+al*r;mup=aa+(cc-aa)*s
    Tp=h*(2*aa+cc)*s/mup
    assert mup==mu+al*(z+r)+ep*x
    assert Tp*mup-T*mu==h*(al*(1+3*r)*s+ep*y)
    k=envelope(h,h<=F(3,10))
    ca=k*(5/h-4)-6+4*h;ce=k/h-h
    bound=k+max(F(0),al*ca+ep*ce)
    assert Tp<k and T<bound
    return dict(plus_nodes=(aa,aa,cc,cc),plus_mu=mup,plus_T=Tp,kappa=k,C_alpha=ca,C_epsilon=ce,bound=bound)

def run():
    cert=certificates();classes=[]
    for e,beta1 in [(F(0),F(1,1000)),(F(1,200),F(1,160))]:
        sp=graph_space(e,beta1);members=[fiber_family(t,e,beta1) for t in [0,F(1,2),1]]
        q0,qm,q1=members
        assert q0['V']==qm['V']==q1['V'] and q0['g'][:2]==qm['g'][:2]==q1['g'][:2]
        assert qm['g'][2]==(q0['g'][2]+q1['g'][2])/2==(1-sum(q0['g'][:2]))/2
        assert q0['g'][2]<q1['g'][2] and q0['T']<qm['T']<2<q1['T']<F(51,25)
        assert 1/qm['T']==(1/q0['T']+1/q1['T'])/2
        if e:
            assert 253*(q0['nodes'][2]+q0['nodes'][3])>1
            for q in members:assert not any(i in q['root'] for i,p in enumerate(q['points']) if p in [(0,0,0),(0,0,1),(0,1,0),(1,0,0)])
        classes.append(dict(e=e,beta1=beta1,beta2=F(1,16),K=20,k=F(1,3),graph_space=sp,members=members))
    P=[(0,0,0),(0,0,1),(0,1,0),(1,0,0),(F(7,10),F(143,80),F(-1,5)),
       (F(17,10),F(153,200),F(-3,10)),(F(6,5),F(509,400),F(-1,10))]
    q=audit(P,(1,F(99,100),F(3,5),F(59,100)))
    assert F(7,45)<q['h']<F(3,10) and q['h']==F(2000,8679)
    assert 49*(q['nodes'][0]-q['nodes'][1])+13*(q['nodes'][2]-q['nodes'][3])==F(31,50)
    q['transfer']=transfer_control(q)
    assert q['transfer']['bound']<F(51,25)
    return dict(version=1,certificates=cert,fiber_classes=classes,new_region_control=q)

def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x

if __name__=='__main__':
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    result=run();data=(json.dumps(serial(result),sort_keys=True,separators=(',',':'))+'\n').encode()
    assert len(data)==101701 and hashlib.sha256(data).hexdigest()=='fe59580182b354de19b96876c1ee1e679bd86ec171cb2ef4c1bd2c6f3760a081'
    target=Path('tilted_root_exact.json')
    if sys.argv[1]=='build':target.write_bytes(data)
    else:assert target.read_bytes()==data
    print('BALANCED_ENVELOPE_EXACT_BERNSTEIN_PASS 3 24 720')
    print('FIXED_CHORD_GRAPH_SPACE_EXACT_PASS 2 21 19 2')
    print('TRUE_ROOT_STEINER_TRACE_DROP_PASS 2')
    print('NEW_LOW_VOLUME_TILTED_REGION_PHYSICAL_PASS 2000/8679')
    print('TILTED_ROOT_EXACT_RECOVERY_PASS',len(data),hashlib.sha256(data).hexdigest())
```

### tilted_root_explore.py

```python
# Exploratory, NOT an exclusion proof. CPython 3.13.5, NumPy 2.3.5,
# SciPy 1.17.0. Run with OPENBLAS_NUM_THREADS=1.
# Commands: python tilted_root_explore.py general | weak | shrink
import sys,json
import numpy as np
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import differential_evolution

def moments(p):
    p=np.asarray(p,dtype=float);hull=ConvexHull(p);f=hull.simplices;ref=p.mean(axis=0)
    a=p[f[:,0]]-ref;b=p[f[:,1]]-ref;c=p[f[:,2]]-ref
    v=np.abs(np.einsum('ij,ij->i',np.cross(a,b),c))/6
    V=v.sum();g=(v[:,None]*(p[f].sum(axis=1)+ref)/4).sum(axis=0)/V
    return V,g
T0=np.array([[0,0,0],[0,0,1],[0,1,0],[1,0,0]],float)

def model(v):
    alpha,p,q=v[:3];xy=np.reshape(v[3:],(3,2));z=(1-p*xy[:,0]-q*xy[:,1])/alpha
    pts=np.concatenate((T0,np.column_stack((xy,z))));V,g=moments(pts)
    mu=1-p*g[0]-q*g[1]-alpha*g[2]
    T=((3-alpha-q)*g[0]+(3-alpha-p)*g[1])/(6*V*mu)
    return T,pts

def pair(v):
    T,pts=model(v);alpha,p,q=v[:3]
    ext=np.vstack((pts,[0,1/q,0],[1/p,0,0]));V,g=moments(ext)
    mu=1-p*g[0]-q*g[1]-alpha*g[2]
    Tp=(2-alpha)*(g[0]/q+g[1]/p)/(6*V*mu)
    return T,Tp

def shrink(v):
    l,m=v;alpha=.8
    pts=np.array([[0,0,0],[0,0,1],[0,l,0],[m,0,0],[.01,.8,.2375],[.75,.02,.2875],[.5,.5,0]])
    V,g=moments(pts);mu=1-g[0]-g[1]-alpha*g[2]
    return (l*(3-alpha-l)*g[0]+m*(3-alpha-m)*g[1])/(6*V*mu)

if __name__=='__main__':
    mode=sys.argv[1];assert mode in ('general','weak','shrink')
    def fun(v):
        try:
            if mode=='shrink':return -shrink(v)
            if mode=='general':return -model(v)[0]
            T,Tp=pair(v);return Tp-T+100*max(0,2.001-T)
        except QhullError:return 10. if mode=='general' else 100.
    if mode=='shrink':
        o=differential_evolution(fun,[(.1,1),(.1,1)],seed=713,atol=1e-11,tol=1e-10)
    else:
        bounds=[(.01,.999),(.05,1),(.05,1)]+[(.00001,3 if mode=='general' else 4)]*6
        o=differential_evolution(fun,bounds,seed=713 if mode=='general' else 714,popsize=12,maxiter=700,tol=1e-9,atol=1e-10,polish=True)
    result=dict(mode=mode,objective=float(o.fun),v=o.x.tolist(),nfev=int(o.nfev))
    if mode=='weak':result['T_and_Tprime']=[float(t) for t in pair(o.x)]
    else:result['T']=float(-o.fun)
    print(json.dumps(result,sort_keys=True))
```
