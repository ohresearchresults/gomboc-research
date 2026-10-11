# minimum-0182

Historical AI scientific report · saved 2026-09-22 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# UNEQUAL_ENDPOINT_SINGLE_B_FAN_NEGATIVE_APPENDAGE_V1

## 1. Математический итог

**Неравные концевые параметры больше не являются препятствием для всего clipped single-B-fan класса.** Для произвольных `a>b>0`, `0<c,d<a`, без ограничений на отношение c/d, число корневых вершин или допустимую отрицательную глубину доказано:

> Пусть `P=conv(T0,F)` — настоящее proper root-only тело с ровно одной отрицательной по z корневой вершиной. Положим `Q=conv(T0,F intersect {z>=0})`. Если единственные максимальные грани Q, не содержащие B, — корень и основание z=0, то
>
> **`T(P)<max(2,T(Q))`.**

В частности, если `T(Q)>=2`, то первый коэффициент `C1` исходного полинома `12VE-N` неотрицателен. При `tau=T(Q)>2` соответствующий `b_tau` строго положителен: отрицательное корневое продолжение не увеличивает след, уже превышающий два. Если `C1<0`, **весь физически допустимый луч остаётся ниже двух**; свободный дискриминант вне допустимого интервала этого не опровергает.

Есть и расширение за пределы single-B-fan. Для произвольного proper root-only Q с дополнительными настоящими C/D-root гранями тот же результат доказан при `0<e<=1`, где в D-ориентации

```text
e=d*m+(d-b)*r,  m=(r-p_y)/(-p_z),  r=R_y,
```

после нормировки a=1. Более общая достаточная граница — `f1>=0`, с явным полиномом f1 ниже. Это целый геометрический сектор, а не ограничение на малую глубину.

От принятой положительно-октантной теоремы для single-B-fan следует **`T(P)<Cstar<2.029`** для первого класса. Для расширения с дополнительными конусами следует **`T(P)<203/100`** по J55. Число `Cstar≈2.02878303567341172514` и его прежнее доказательство здесь унаследованы; новый сертификат не вычисляет заново этот максимум. :contentReference[oaicite:0]{index=0}

Отправная точка — буквальный `minimum-0179`, SHA-256 `468528fda471c3cab4e5aaed25de7b76d551a6e42c4fae1b2cb3cabd9703301d`. Он закрывал только c=d и явно сохранял поперечный момент и дополнительные non-B конусы как остаток. Новый результат закрывает первое препятствие полностью внутри фактического single-B-fan класса. :contentReference[oaicite:1]{index=1}

## 2. Точная область и настоящая видимость

Нормируем a=1. Везде в новом доказательстве

```text
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
T0=conv(A,B,C,D),
0<b,c,d<1,
alpha=1-b, delta=1-d, epsilon=1-c,
ell=1-delta*x-epsilon*y-alpha*z,
n=nD*x+nC*y, nD=1+b+c, nC=1+b+d.
```

Корень F компактен, выпуклый, положительной площади, лежит в `ell=0,x>0,y>0` и имеет ровно одну вершину p с z<0. Поэтому ABC/ABD — настоящие максимальные треугольники. Все интегралы — исходные равномерные объёмные интегралы одного тела:

```text
V=int 1, J=int (x,y,z), E=int ell, N=int n,
g=J/V, T=N/(6VE).
```

Ни центроид, ни вектор J при добавлении отрицательной части не сохраняются. Стационарность тела, корня, концов или рамки нигде не предполагается.

Пусть `Fplus=F intersect {z>=0}` имеет положительную площадь. Его нулевой отрезок обозначим `[R,S]`, где

```text
R=((1-epsilon*r)/delta,r,0),
S=((1-epsilon*s)/delta,s,0),
0<r<s<1/epsilon, L=s-r,
K0=Q intersect {z=0}=conv(A,D,R,S,C).
```

Положим `h=-p_z>0`. Единственная возможная положительно-ell вершина клипа — `qclip=(p_x/(1+h),p_y/(1+h),0)`. Если она лежит в K0, прежнее стирание отрицательной пирамиды уже даёт сравнение с Q. Иначе отражением x/y, c/d выбираем D-угол. Тогда

```text
m=(r-p_y)/h,
w=((alpha+epsilon*m)/delta,-m,-1),
p=R+h*w,
e=d*m+(d-b)*r>0, eta=e/(6delta).
```

Выпуклость **того же корня** заставляет `y>=r+mz` на Fplus. Принятая paired-wedge геометрия даёт настоящий максимальный треугольник BDR и точное разложение, с непересекающимися внутренностями:

```text
P minus Q = conv(p,K0) union tetra(p,B,D,R).              (2.1)
```

Оно применимо и при дополнительных non-B гранях Q. Объём второго куска равен `h*eta`; его положительная клип-часть имеет объём `h*eta/(1+h)`, отрицательная — `h^2*eta/(1+h)`. Это части одного тетраэдра. Базовый конус не является всем отрицательным колпаком, когда qclip — настоящая новая вершина. :contentReference[oaicite:2]{index=2}

Для single-B-fan используется **дополнительная настоящая** опорная грань вдоль CS, содержащая B. На корне она даёт

```text
y<=s+mS*z,  mS=((b-c)*s-b)/c<0.                         (2.2)
```

При всех этих параметрах, в том числе при m<=0,

```text
c*d*(m-mS)=c*e+bd*(1-epsilon*s)+bc*delta*r+cd*alpha*L>0.
```

Грань BCS может содержать ещё корневую вершину и быть четырёхугольником. Её интеграционный треугольник не рассматривается как независимо подвижная грань.

При фиксированных Q,w сохраняются все точки Fplus, включая R,S. У тела `P_h=conv(Q,R+h*w)` физический интервал равен

```text
0<h<r/m, если m>0;
0<h<infinity, если m<=0,
```

в single-B-fan случае. Действительно, (2.2) даёт `y-s-mz<0` при z>0, а нижняя опора сохраняет R. Для произвольного Q с дополнительными конусами вместо этого остаётся полное условие

```text
h*(y_u-s-m*z_u)<=(s-r)*z_u  для каждой положительной корневой точки u,
```

вместе с положительностью координат p. Его нельзя заменить одним скалярным пределом глубины. Каждая меньшая положительная глубина исходного допустимого тела остаётся допустимой.

## 3. Поперечный первый момент не исчезает — его ограничивают две реальные опоры

Введём

```text
K=(c-d)(b+c+d),
gR=nD+K*r=delta*n(R),
gS=nD+K*s=delta*n(S).
```

На исходном корне выполнено точное равенство

```text
delta*n=nD+K*y-alpha*nD*z.                              (3.1)
```

Именно `K*int y` — отсутствовавший при c=d поперечный вклад. Используем оригинальные yz-координаты корневой плоскости и её моменты

```text
M0=int_Fplus dy dz,
My=int_Fplus y dy dz,
Mz=int_Fplus z dy dz,
G=2M0.
```

Пусть `k=m-mS`. В ветви m>0, нужной ниже, k>0, а две настоящие опоры дают

```text
0<G<=L^2/k,
r*M0+m*Mz<=My<=s*M0+mS*Mz.                              (3.2)
```

Первая оценка — интеграл реальной ширины, не превосходящей `L-kz`. Вторая — интеграл тех же опорных неравенств. Отсюда, положив `g*=max(gR,gS)`,

```text
24delta^2*N_Q <= B0+3b*g*G.                             (3.3)
```

При c>=d используется верхняя опора и mS<0; при c<=d — нижняя и m>0. Никакой искусственный корень, равномерно перезаполненный образ или независимо выбранный My не вводится.

## 4. Полные исходные моменты и полином глубины

Определим базовые величины

```text
Z=1-d*r+c*s=2delta*Area(K0),
H=1+c-d^2*r+c^2*s=Z*(3mean_K0 ell),
B0=delta*r*(delta*nD+gR)
   +L*(gR+gS)
   +(1-epsilon*s)*(gS+delta*nC).                         (4.1)
```

Здесь `B0=24delta^2*int_conv(B,K0) n`. Формула получается из настоящего плоского A-веера ADR, ARS, ASC.

В single-B-fan случае два положительных B-конуса дают **точно**

```text
Dcal=6delta*V_Q=Z+bG,
Ecal=24delta*E_Q=bZ+H+b^2G,
Ncal=24delta^2*N_Q=B0+3b*nD*G+6b*K*My-6b*alpha*nD*Mz.    (4.2)
```

Если kbar и fbar — фактические площадные центроиды K0 и Fplus, то

```text
J_Q=Area(K0)*(B+3kbar)/12+b*M0*(B+3fbar)/(12delta).
```

Постоянный якобиан корневой плоскости делает fbar одинаковым для физической площади и dy dz.

Коэффициенты связанного отрицательного продолжения:

```text
D1=Z+e,
E1=H+(b+d)e,
N1=Z*gR+B0+e*(2gR+delta*nD),
N2=(alpha*nD-K*m)(Z+e).
```

Для исходных равномерных моментов

```text
6delta*V_h=Dcal+hD1,
24delta*E_h=Ecal+hE1,
24delta^2*N_h=Ncal+hN1+h^2N2.                            (4.3)
```

А для полного векторного момента

```text
V1=Area(K0)/3+eta,
J1=Area(K0)*(R+3kbar)/12+eta*(2R+B+D)/4,
J2=V1*w/4,
J_h=J_Q+hJ1+h^2J2, g_h=J_h/V_h.                         (4.4)
```

Таким образом,

```text
T(Q)=Ncal/(Dcal*Ecal),
T(P_h)=(Ncal+hN1+h^2N2)/[(Dcal+hD1)(Ecal+hE1)].
```

Положим

```text
F0=2Dcal*Ecal-Ncal,
F1=2(Dcal*E1+Ecal*D1)-N1,
F2=2D1*E1-N2.
```

Тогда

```text
24delta^2*(12V_hE_h-N_h)=F0+hF1+h^2F2.                 (4.5)
```

F1 — положительный постоянный множитель прежнего C1; это не новый независимо заданный момент.

### Строго положительный квадратичный коэффициент на всей области

Пусть

```text
Zbase=1+c+b^2+bc+2c^2L
      -(d-c)(d^2+cd+bc+b^2)r/d.
```

Точная факторизация:

```text
F2=(Z+e)[Zbase+(bc+bd+c^2+d^2)e/d]>0.                   (4.6)
```

При c>=d положительность Zbase непосредственна. При c<=d используется тождество

```text
Zbase=delta*(b^2c+bc^2+d^2+d)/(d*epsilon)
      +2c^2L
      +(d-c)(d^2+cd+bc+b^2)(1/epsilon-r)/d.
```

Оба случая, включая c=d, проверены символически. Никаких делений на c-d или b-d нет.

## 5. Доказательство всей неравной области

Обозначим чисто базовые выражения

```text
f0=2Z(bZ+H)-B0,
f1=2[Z*E1+(bZ+H)D1]-N1,
AR=2H+4bZ-3gR,
AS=2H+4bZ-3gS,
A*=min(AR,AS).
```

Из исходных моментов следуют

```text
F1=f1+2bG(E1+bD1),
F0>=f0+b*A*G+2b^3G^2,                                 (5.1)
```

причём вторая оценка применяется в ветви m>0 по (3.2).

### 5.1. Отрицательный первый коэффициент заставляет e>1 и m>0

f1 аффинен по e. Новый точный сертификат доказывает на **всей** области

```text
0<b,c,d<1, r>0, L>0, r+L<1/epsilon
```

строгую положительность `f1(e=0)` и `f1(e=1)`. Следовательно, `F1<0` возможно только при e>1.

Если b>=d, то `m=(e+(b-d)r)/d>0` непосредственно. Если b<d, дополнительный сертификат доказывает `f1(e=(d-b)r)>0`. Интерполяция по e между 0 и `(d-b)r` исключает m<=0 при f1<0. Итак,

```text
F1<0 => f1<0, e>1, m>0.                                (5.2)
```

В отличие от прежнего равноконцевого доказательства, не требуется дополнительное неравенство `q<(1-b)/2`: сертификат ниже покрывает всю оставшуюся трёхконцевую область.

### 5.2. Совместные ширина и глубина закрывают отрицательный коэффициент

Пусть F1<0. Определим два положительных знаменателя

```text
MD=e+(b-d)r=d*m>0,
KD=c*e+b(c-d)r+d(c-b)L+bd=c*d*k>0.
```

Физический предел `h<r/m` и (3.2) дают

```text
F0+hF1+h^2F2 >= min(Lambda0,LambdaR,LambdaS),             (5.3)
Lambda0=f0+(r/m)f1,
LambdaR=Lambda0+b*AR*L^2/k,
LambdaS=Lambda0+b*AS*L^2/k.
```

Действительно, при A*>=0 достаточно Lambda0; при A*<0 используется соответствующий корневой предел площади. Остальные отброшенные члены неотрицательны. Умножая на MD*KD, получаем полиномы

```text
Psi0=f0*MD*KD+d*r*f1*KD,
PsiR=Psi0+b*AR*c*d*L^2*MD,
PsiS=Psi0+b*AS*c*d*L^2*MD.                              (5.4)
```

**Все три строго положительны на полной области e>=1**, без верхней границы e и без ограничения отношения c/d. Для этого заключения не используется ни sampled feasibility, ни стационарная реакция.

### 5.3. Полный точный положительно-коэффициентный сертификат

Для пяти неупорядоченных полиномов используем независимые неотрицательные параметры x,y,z,u,v,w:

```text
b=x/(1+x), c=y/(1+y), d=z/(1+z),
r=u/[epsilon*(1+u+v)], L=v/[epsilon*(1+u+v)],
e=1+w для Psi0,PsiR,PsiS.
```

Первые пять переменных строго положительны; w>=0 включает стенку e=1. Для проверки m=0 вместо первой формулы берётся `b=d*x/(1+x)`, покрывающая весь b<d. Равенство b=d уже относится к положительной ветви e=0.

В порядке столбцов ниже положительный множитель равен

```text
[epsilon*(1+u+v)]^n (1+x)^pb (1+y)^pc (1+z)^pd.
```

Полный сертификат имеет следующие размеры:

```text
полином       (n,pb,pc,pd)   положительных коэффициентов
f1(e=0)       (2,1,3,3)      124
f1(e=1)       (2,1,3,3)      134
f1(m=0)       (2,2,3,3)      217
Psi0          (4,3,6,5)      4339
PsiR          (4,3,6,5)      4361
PsiS          (4,3,6,5)      4356
```

Итого **13531 строго положительный ненулевой целый коэффициент**, минимальный коэффициент каждого полинома — **1**. Степени последних трёх по `(x,y,z,u,v,w)` равны `(3,6,5,4,4,2)`. У каждого есть положительный член с w-степенью ноль, поэтому положительность не теряется при e=1.

Полный генератор разворачивает каждую замену точной биномиальной формулой над целыми числами; полный список всех коэффициентов восстанавливается из встроенного источника. Дополнительные рациональные подстановки в коде — только независимая диагностика тождеств, не тест положительности по выборке.

Следовательно, в (5.3) правая часть строго положительна. При F1<0 имеем T(P_h)<2 на **всём** допустимом луче. Также

```text
F0>=min(Lambda0,LambdaR,LambdaS)-(r/m)f1>0,
```

то есть T(Q)<2. Если F1>=0, то F2>0 непосредственно даёт строго положительный двухперекрёстный прирост и `T(P_h)<max(2,T(Q))`. Доказательство основного результата завершено.

При `tau>=max(2,T(Q))` точный пороговый полином имеет коэффициенты

```text
c_tau=tau*Dcal*Ecal-Ncal,
b_tau=F1+(tau-2)(Dcal*E1+Ecal*D1),
a_tau=F2+(tau-2)D1E1>0.
```

При T(Q)>2, tau=T(Q), получаем c_tau=0 и b_tau>0. Это утверждение о настоящей первой вариации, а не наложенная стационарность. Ниже двух сырая монотонность T не утверждается.

## 6. Дополнительные настоящие C/D-root конусы: что уже переносится

Для произвольного proper положительно-октантного Q корень и основание всё равно дают два настоящих непересекающихся B-конуса, но они могут не исчерпывать Q.

Любая дополнительная максимальная грань, не содержащая B, является треугольником `Cuv` или `Duv`, где uv — настоящее корневое ребро. Обоснование: у A положительно-октантного Q ровно три координатные опорные плоскости; другого non-B лица через A нет. Одна плоскость не может содержать одновременно C,D вне основания, поскольку внутренняя часть CD лежит внутри пятиугольника K0 и не является его ребром. Без канонической вершины все вершины были бы корневыми и давали бы сам корень. Оставшаяся одна каноническая вершина плюс настоящий отрезок в корневой плоскости дают треугольник.

Пусть WC,WD — суммы **реальных** объёмов тетраэдров `B,C,u,v` и `B,D,u,v` в одном B-веере. Тогда точно

```text
Dcal_actual=Z+bG+6delta(WC+WD),
Ecal_actual=bZ+H+b^2G+6delta[(b+c)WC+(b+d)WD].             (6.1)
```

Каждый дополнительный тетраэдр объёма omega вносит

```text
J_extra=omega*(B+X+u+v)/4,
E_extra=omega*(b+ell(X))/4,
N_extra=omega*(n(X)+n(u)+n(v))/4, X=C или D.
```

Это фактические детерминанты и фактические моменты; свободные числа WC,WD не объявляются реализацией тела.

Точный первый коэффициент поэтому равен

```text
F1_actual=f1+2bG(E1+bD1)
 +12delta{WC[E1+(b+c)D1]+WD[E1+(b+d)D1]}.                (6.2)
```

Все добавки справа неотрицательны. Значит, **f1>=0 достаточно для того же сравнения даже со всеми дополнительными конусами**. В частности, весь сектор `0<e<=1` закрыт новым сертификатом двух значений f1. В ненормированных концах это условие есть `d*m+(d-b)r<=a`.

Отсюда строгая классификация ещё возможного одно-отрицательного контрпримера к `max(2,TQ)`: после ориентации он должен иметь

```text
e>1, m>0, f1<0,
по меньшей мере одну дополнительную настоящую C/D-root грань,
2bG(E1+bD1)+12delta{WC[E1+(b+c)D1]+WD[E1+(b+d)D1]}<-f1,
```

а также полное корневое условие глубины из §2 и отрицательный интервал настоящего порогового полинома. Ниже двух по-прежнему необходимы и дискриминант, и допустимый интервал. Это новый остаток **произвольных тел**, не условие полного максимума и не механическая классификация E17.

## 7. Точные настоящие объекты и границы неверных упрощений

### 7.1. Небольшой неравноконцевой объект выше двух

Возьмём `b=1/4,c=1/100,d=1/200`. В Q после канонических вершин 0=A,1=B,2=C,3=D идут корневые

```text
4=(9901/9950,1/100,0),
5=(2/199,1,0),
6=(14/199,3/4,1/4),
7=(5551/9950,13/50,1/4).
```

Здесь r=1/100,s=1,m=1,mS=-1. Добавим `p=(24796/24875,9/1000,-1/1000)`. В P точка R теряет статус вершины; сохранённый порядок его вершин — A,B,C,D,Q5,Q6,Q7,p. Настоящие максимальные циклы:

```text
Q: (0,1,2),(0,3,1),(0,2,5,4,3),(1,6,5,2),
   (1,3,4),(1,4,7),(1,7,6),(4,5,6,7).
P: (0,1,2),(0,3,1),(0,2,7),(0,7,3),(1,5,4,2),
   (1,3,7),(1,6,5),(1,7,6),(2,4,7),(4,5,6,7).
```

Их f-векторы — Q `8/14/8`, P `8/16/10`. Оригинальные моменты:

```text
VQ=22049/119400,
EQ=1714283/31840000,
NQ=114679368611/950424000000,
JQ=(450251473/9504240000,1160137/23880000,60439/1273600),
TQ=229358737222/113394677601 approximately 2.022658753253,

VP=88277/477600,
EP=1286723/23880000,
NP=9186603459023/76033920000000,
JP=(4510591733/95042400000,92893291/1910400000,30219541/636800000),
TP=9186603459023/4543521850840 approximately 2.021912463638.
```

Собственные центроиды — точно JQ/VQ и JP/VP. При указанной масштабировке `F1=401503913/400000000>0`, `F2=3492153/3200000>0`. Оба тела — исходные равномерно заполненные оболочки, не формальные моменты.

### 7.2. Одинаковый исходный ell-маргинал не определяет поперечный вклад

Сохранена настоящая пара с `b=1/4,c=1/20000,d=1/10000`. Для её полного восстановления достаточно следующего рецепта, также буквально реализованного в коде:

```text
L0=9999/10000, L=L0/epsilon,
r=(1-L0)/(2epsilon), s=r+L, e=1/10000,
m=(e+(b-d)r)/d, mS=((b-c)s-b)/c, k=m-mS,
zT=L/(2k), h=r/(10m), pad=L/20,
Root(y,z)=((1-epsilon*y-alpha*z)/delta,y,z).
```

Два корня — выпуклые оболочки R=Root(r,0), S=Root(s,0) и

```text
Root(r+m*zT+pad+sigma,zT),
Root(s+mS*zT-pad+sigma,zT),
sigma=-1/100 или +1/100.
```

К обоим добавляется одно и то же `p=R+h*w`. Оба Q имеют `8/15/9`, оба P — `9/19/12`, и все четыре следа превышают 2.0254. У пары совпадают фактические M0,Mz, V,E и **весь оригинальный ell-маргинал**, как для Q, так и для P. Однако

```text
My_plus-My_minus=299940003/212474375750,
N_plus-N_minus=-15009/13598360048000,
TQ_plus-TQ_minus=-624664189114952366952/32439113742870245329399798123.
```

Это точная настоящая иллюстрация того, почему член K*My нельзя удалить при c!=d. Она не опровергает доказанное неравенство: оба отрицательных продолжения имеют меньший след, чем соответствующий собственный Q. Полные V,J,E,N, центроиды, грани и рёбра находятся в воспроизводимом отчёте.

### 7.3. Неравные концы, отрицательный F1 и положительный дискриминант

Два треугольно-трапецеидальных корня используют соответственно `(b,c,d)=(1/100,1/50,1/100)` и `(1/100,1/100,1/50)`. Полный рецепт:

```text
L0=99/100, L=L0/epsilon, r=(1-L0)/(2epsilon), s=r+L,
e=5, m=(e+(b-d)r)/d, mS=((b-c)s-b)/c,
zT=L/[2(m-mS)], h=r/(2m),
Fplus=conv(Root(r,0),Root(s,0),Root(r+m*zT,zT),Root(s+mS*zT,zT)),
p=Root(r-m*h,-h).
```

В обоих случаях старый paired guard отрицателен, F1<0, свободный дискриминант положителен и TP>TQ. Тем не менее все эти следы ниже двух. Для C-доминантного случая

```text
TQ=173037502493301875384/86558438277431116787,
TP=177272213707378997324969516812/88675933766185750818533328045,
0<h<1/98000,
min(Lambda0,LambdaR,LambdaS)>=3238163492483343/3520864816000000000>0.
```

Сохранены также восьмивершинные, не трапецеидальные корни в обоих порядках c/d с тем же отрицательным F1. Эти объекты подтверждают необходимость второй ветви доказательства, но **не являются контрпримером к max(2,TQ)**.

Отдельно сохранён весь неограниченный луч с `b=1/5,c=3/5,d=1/2,L0=1/2,e=1/100,r=(2/25)(1-L0)/epsilon`, m=-1/25 и допустимыми всеми h>0; точный контроль взят при h=100. Полный восьмивершинный положительный корень задан генератором. Большая глубина и низкий след не являются основанием выбрасывать эту конструкцию.

### 7.4. Дополнительный C-root конус: формула меняется, новый сектор всё же работает

В объекте §7.1 заменим Q6 на

```text
Q6new=(69901/995000,7501/10000,1/4),
```

оставив всё остальное, включая p. Получаем Q `8/15/9`, P `8/17/11`, с настоящим дополнительным C-root треугольником. В порядке Q из §7.1 его цикл `(2,6,5)`; максимальные циклы Q теперь

```text
(0,1,2),(0,3,1),(0,2,5,4,3),(1,6,2),(1,3,4),
(1,4,7),(1,7,6),(2,6,5),(4,5,6,7).
```

В порядке P из §7.1 максимальные циклы

```text
(0,1,2),(0,3,1),(0,2,7),(0,7,3),(1,5,2),(1,3,7),
(1,6,5),(1,7,6),(2,5,4),(2,4,7),(4,5,6,7).
```

Его точные значения:

```text
TQ=1529071169412179/755970560349147,
TP=4593340493308037/2271779069124591,
6delta*VQ-(Z+bG)=1/1000000>0.
```

Оба следа превышают 2.02. Это опровергает перенос **двухконусной формулы** без её гипотезы, не сравнение следов. Теперь тело попадает в доказанное расширение §6, поскольку `e=51/20000<1`. Код независимо интегрирует дополнительный настоящий B-тетраэдр и проверяет исправления всего J, E и первого коэффициента. Он не заменён свободной скалярной массой.

## 8. Область применимости, оставшийся вопрос и доказательственный статус

Основная теорема покрывает все низкие положительные неравные концы, все допустимые направления и глубины, произвольное число корневых вершин — при настоящем clipped single-B-fan. Она не требует стационарности и не использует общие J-ограничения полного максимума, свободный height-law fit или независимые конусные массы. Криволинейный вариант под тем же фактическим разложением следует теми же интегральными формулами; полигональные приближения сохраняют R,S и две опоры. Полученные строгие полиномиальные запасы относятся к предельным моментам напрямую, а не выводятся из одного слабого предельного неравенства.

Все знаменатели явны: delta,epsilon,b,c,d положительны; в отрицательной линейной ветви также MD=d*m и KD=c*d*k положительны. c=d, b=d и e=1 допустимы. Нет обратной проективной границы или замены плотности. h=0 — неизменённое Q, а h=r/m — координатная граница, не proper тело основного луча.

Если Fplus имеет нулевую площадь, положительная часть — B-пирамида, а отрицательная часть пирамидальна; прежняя cap-теорема даёт T(P)<2. Если B-проекция находится внутри K0, прежняя теорема напрямую сравнивает с Q. Эти границы не требуют положительной площади несуществующего clipped корня.

Новый неравноконцевой результат **не** закрывает весь proper root-only negative-z класс: остаются дополнительные настоящие C/D-root конусы вне §6 и несколько отрицательных корневых вершин. Для первого остатка §6 даёт необходимые e>1,m>0 и точный бюджет фактических дополнительных конусов. Общие срезовые дефициты остаются возможным усилением этой совместной геометрии; из их формальных сепараторов не извлекается реализация тела. :contentReference[oaicite:3]{index=3}

Полный максимум со стационарными реакциями — отдельная задача. Ни одно новое утверждение не предполагает этих реакций и не переносит их на Q. Механические 110, E17, новая минимальная сложность или изменение регистра здесь не установлены.

## 9. Полное восстановление и выполненные проверки

Сохранить приведённую ниже полную капсулу как `recover_unequal_cap.py`, UTF-8/LF с одним последним LF. Она восстанавливает оба полных исходника, все точные входы, вспомогательные функции и генераторы. Старые файлы родителей, архив, seed, численный оптимизатор или внешние входные данные не требуются.

Выполненная среда: **CPython 3.13.5**, стандартная библиотека для геометрического аудитора; **SymPy 1.14.0** для полиномиального сертификата. Assertions включены. Точный проверяющий слой не использует floating hull, NumPy или SciPy.

```sh
python -S recover_unequal_cap.py unequal_cap_recovered
cd unequal_cap_recovered
python -S unequal_audit.py build controls.json > controls.txt
python -S unequal_audit.py check controls.json > check.txt
python unequal_certificate.py build coefficients.json > certificate.txt
python unequal_certificate.py check coefficients.json > cert_check.txt
cmp controls.txt check.txt
cmp certificate.txt cert_check.txt
```

Ожидаемые терминальные маркеры:

```text
UNEQUAL_ENDPOINT_PAIRED_APPENDAGE_SOURCE_RECOVERY_PASS
UNEQUAL_ENDPOINT_SINGLE_B_FAN_ACTUAL_PAIRED_APPENDAGE_AUDIT_PASS
UNEQUAL_ENDPOINT_SINGLE_B_FAN_WHOLE_DOMAIN_COMPARISON_CERTIFICATE_PASS
```

Точные пины:

```text
recover_unequal_cap.py: 10799 bytes
SHA256 4aa4f95aead7e944fe99df002e6cd1de3b4198b9b35242be47eac20459f5b5c7
unequal_audit.py: 14454 bytes
SHA256 9220c1953e536a4b795a967d69092104fd8a5edb34264f525a208437a3950748
unequal_certificate.py: 5034 bytes
SHA256 91f36dd6f256f406fc935c816ade0730f008f4efee167b4c82569e9c0ffeec80
controls.json: 81909 bytes
SHA256 a338bd7834530566901107c1d86b172020509c124d364a509a3268bca699aca3
coefficients.json: 259595 bytes
SHA256 5105c31de509e5582fa2aa448d239c195fcba97c109a8649ef39eef91a8a6992
controls.txt and check.txt: 2617 bytes each
SHA256 bae337fd24cdef95fa5ec0521608fc257681dc031b96b601b224f92a347c6d4c
certificate.txt and cert_check.txt: 538 bytes each
SHA256 2bab4e9c90719be05c802fad37480ada15b5c1311564b9de6d9b31c5ed0002f0
```

Выполнены обычные build/check и полное восстановление только из капсулы в новом каталоге с повторными build/check. Исходники, оба отчёта и оба stdout совпали побайтно. Два положительных внутренних веера независимо воспроизводят V и весь J каждого тела. Дополнительно проверены настоящий B-веер, оба видимых куска, две независимые оболочки положительного клипа и три фактические промежуточные глубины каждой single-B-fan пары.

Сохранены 15 single-B-fan пар, включая поперечную пару и неограниченный луч, плюс один дополнительный C-root пример. Это контрольные тела, не механические исключённые классы. 13531 коэффициент сертифицирует всю указанную непрерывную область, а не выборку этих тел. Доказательство не является формализацией в proof assistant.

Удобные копии: [капсула](sandbox:/mnt/data/recover_unequal_cap.py), [геометрический аудитор](sandbox:/mnt/data/unequal_cap/unequal_audit.py), [полиномиальный сертификат](sandbox:/mnt/data/unequal_cap/unequal_certificate.py), [точные тела и моменты](sandbox:/mnt/data/unequal_cap/controls.json), [полные коэффициенты](sandbox:/mnt/data/unequal_cap/coefficients.json). Буквальная капсула ниже достаточна без этих ссылок.

```python
# UNEQUAL_ENDPOINT_SINGLE_B_FAN_NEGATIVE_APPENDAGE_V1
# Complete source-only recovery; CPython standard library; no parent imports.
# Parent minimum-0179
# SHA 468528fda471c3cab4e5aaed25de7b76d551a6e42c4fae1b2cb3cabd9703301d
import base64,hashlib,json,sys,zlib
from pathlib import Path
DATA="""
c-rMWYj@hnlHd1NXlFhkiN+wXGZS#<9Bkvn#3uMLzLOBHj*x_r4U!^>mvi#px2n4J!gi9Gxo7voo_k|j-PP6A)%8|uzW%cG-7iaP
ZdyynOZLL;FYRA`RsI<CF8}DBo4vuw@Wa{Q#=Jfoygl!kN9JjFU=Dh3yEkXIJ+nI;0z~(1&%8B0`@bs3!)-DPe5JK#wDt~|5+|1L
SdpX5y-8$6Tc%iX>_&+f__5;p)@1HFd&(eC+)d&}zBN}oKU^m99wK|UoX_hEn4pA_x9}2g<;F_nCYI;Bjxvpc1)zm#Fe|ho*G~ZX
o$0TdbK|bref{Zfb-%sefA2gb@7~@u2<7oIBESOtLDD<FJsW;BCf)GM<@@3G_Wb^$>$(Vj{jRI*zxw^4`TNwd_J1?%mTgV;-2=;V
o#uh#{x<pTm2+@lSg+juroBJ4Tw~I-CkW-d{;kn!H4F#VB~qu6Ws7}#i!g{1<y3Y670Rgu!tEqMFwcPOU@`H0izZ5#&`M^&&J<z@
kDq<{FtcJDWA}03vv><rx?DX~8yd_0Xq}^SmjPYJS(lMQonV(ynt0qD@KKi?v14{J{_H#MRIwaKwb(>!!?`RYUrCnX+*LQ#tuhTF
Wy7{`pvt2c5|Ae5#LLNZb86q4vslj6gjqXt5`81);0#NGIzduGA1@cGy3wD<E_Nm++EEb4rKzelGRFF3)Ew6=_ya9t%w(&9eGM_n
WXr%lLyV@>xI_)JGo*q(u^9GCz##HKBzIudY#mKk?G(ROQ?s?GKZOyPW}r7sHPqUleI?{E$c5{uG0+j>T8cMS=B^J9hulcl389~+
TJx#;g=Q)dAC2)hWAGR1R@O6b?h=Yfdt)e|;3@6Vs0O@%zrdvppl`IJy)Xz>jpjvrRv5azqi*O~t{g#IHfixt8?|A6RXmK^_#nEZ
z(uZQPQ55j<PI&4N7%XNqfAnf?4837SvWG<<0@bTe6$gVZ}8N%$jJ?!+7=!=R+T&TX1Z?==SP-*=c-MueLwQXFs!Q^Y;56=R)2*g
kWEvpH;sHV784?RUpSOjO0s|#r@%S>%H!!wE!&Ox*KcwM9=m4`NJG&MsDdCdU1Ke=9iI!4LhTAi_hZ;F(8t8%gM1{;g8=vekn3+%
Uu)ZepLqV##gQ3D;q(P;XJyS}J`z0}tv1UgAskCQ3(r>(Ogn5GF074cmrx>5I`F2^_Bm>D&0xOPnep08E>bJ#G4=@j4vct`4=WsU
{pAAeec}pyh<wF4oSG8_A;)zDYg!t6aJPJJEhdhocx`JEt3K_&V{P0VYks;dLgxK9M@+PO7zH3x;t-J^z*3rYPqqfIXgLm`blkDG
fY*sfIC0N|L*IZVi8)^oNU9}_YAO4Wx5ZPlQ5f;4Y?Q_9^x&yk?ACyLhmE$q-HY6n8^x~Bum=u3VqrWNdkfnIqQn+p>I29>{Inm&
QqJV=q=i8EF`z)vBPkpSpa-!B5<>|}1KPObI(KDhwYTMC5`gVgoxr%I3TbZ{?pBh7I!Va(KoLM)tmQmWOVkN-t+CNqOYMk<yN3NI
acbngTC|Lyg4Pzxk_K(R!Rbp)ozF>qR-k=N0ukax6o6<g-B=}EDQGG!q}8xVa9S0cVuOGs*L><?k|F`hX!2)Yn1ZPVipvC8K+L%n
Hmonbu%@><wmV0~NKIK`OYLWjlfjS}IKi4BxJ}BVlDr_FJ@K~+eC~i%WRH9lmJSvrnC7j5IY*y`lD7f!NCdZO;}IId<|!#}V8R>T
5Nl5HNvyBjRyjPto-jn{GgNzcuJ1Dn8Q@<4Mui@L95`7`Y&kt#6)0jbfsR3P_LlV-0i~Q=xK_N3fX%|L3YHSf1;=@6bvu?{VCLHO
?q*4h`&LI7<cxJ;Oc^`@leAs-N>eKxM<7)S1B<o3N%^>Dn^d^v0u1KV2}(R`Iloh@Ly8N;rQ0sc#;DyK7sL?Y;5<3UU-XA5Uvx3R
p6oy6(<E@VY8ZGv&;;QHb7X8V_rQ%ho}KJrWC<oSmQZjS$n2*KEpR*!C4_1m3N8_gLX<CWob!=D#y^D=4mh>ko3>F^9gt}qU3FEp
MH9jUbt0NgWP|VL6I7!*soLoTd~n2+oQ-H4VG)Q!3LZ@pLfqrGa>ahWVn1K84=Z*C-1pUf;b3mxG$;=06(a!Tt7In^M+%L?=DA?O
)LglC5=2}|8OtpU%Pow?ZaFZI_t_nJP@@h{8td^M8}I?U;e)#RO25^6C{dq%NtbCl?qqpqnnDb~_k?bwMlR+GQUt`qs3Hihq$+aH
l86pYRU7Op#r)qi26l$pC*L%2&T^fv1@|4IRBXUof@A*1IiM*3V$AWiEE!;z394Y`Qkn$MDrsDsxJhKGVImxgB_x@{b7#fT!>49z
0(k;iD?4pC(2#aZ9?nV_q=Gp@|3VL_9$8ATOplP(43-H9Hc=YVUTFw79D-bc1noqgrKnBnUsG_7nAF6evpEJ|4wzFDfHZ7~JOrrI
-x`9Yws@myMXUIX5(Bn$2a}~YcTC%YAi=j5u3#EFZ!nid5u43e6a-UV0nUc*W8gUz7SFtCLJo;2eKJ9eFRV~KW$N>z!gtQYnZ=FT
q~o~r1Y1tW4P*GVJN^kLJ?;3%)NnfQ!CTcpRaNK(m4*4|{Jc?z37v>Xk**rG^M*#xF^{U}0I=Yyi)sn8BCYOp7U1#V5tKi!O|-h*
dEkrMA}%YwFn>~CF=7-Qha!<_9G*9_W)#V$E5RRxdIv$0+8c0PZ52oZvh;0@cC0@FEx2KHv$&5djx*GVfrq~q?HJo@pq6G-arPpe
Ra-y~1EvP2&iHJmNA(3o(LjVdk6mRp%Xc)Bl&K5Iwjd2tW`_WdQ$a2G=!#vBg_*`vCUq{JbcGJf#n#l@xQ_W{X+hKyRfLE>f)E&N
UrXn6z5^!cIj^ft{ec`=XgU16-fR?Rq)P}`lqv#D;yo<+fVhtYcd85hu?q96Gyyor1gENtSbwY)2gbrl<V!@s5=7nky^=*n32jwS
k2MWYI{0a^18KHkYv+1Wf9S+BY(VpO>VAQ&c(zLq^+-Zuw;fp?Y_6M@wt7(%fSCpA=p?p}T*Uq(h~*88<3X1TMg$zA)}iyFB~WZ=
6dE+XeH`y3jR}UF>hH=kJP>@|FGdaE>Oyd4QdE$HtVu?zM9Pzi0L_sN2%I4}<irT-donw8Hx%?;krA7*wU!0msDU_6fsLesp3w-x
+)GZO%5is44YOFKGc5I1M>u1g4oatXnYD&bgNPcb7R3alsvD}FkhVS(Lii^ldhm~T0tXD`1gW{Z8|JPP&cr~23APr?WG4*Nj~$OY
-S@2jo)-!iBietC180B;JWROSe-A6yX$CBf4OyTn9?B6;`g)nKyz5ZW5+Gn11Sse7v?ZXH0=iFtwI`stf4(fa=8|v!4pE$cJwm2@
dl}Qpi@nL*-A#K6P^7*xgL!$aQM)yMKF3DyDKi;xqtrra!iP7Fwp>5;#IWm~98io?)`+6}6+G^v>tpfeWnzk)lL(L(`BXf9jpffO
u}RY~t-ffmi;JS{fHlxMA6fsAUtDzF@}_>#$Z709N}c)$ItwG9w*5!Z0UApkG4$jU8i#KW!2+JwAE56Ox@bMB+Irl12W}bsu`Zsm
=kAL8C)M|Q)VaGBE%dBM4K8#GJhW)Q(A||*J=fK{tLojgR+a8C2H$>nU6nw`$k~$<{;4|A-*$REKG8o_-@yYu4hH<FQEfpRRPk-~
6*S)KA8Yt4loq;a7bgZFa63JNzk@&kBYn3sfIc0T1`Mtao(Y;MVOnR<<Z6nd_8y$Beq!X@0DAZ<T|mQm-d2Rc1L}BlKkx6!ejqdN
&qfE8g2hO&4GA0PCnwbzEJ@R|sY61^d9Me9y#hTu$cKcS^T7b%1_u0rA1plls+@uGN0G&s8bRdUdH5>jsAdN~WEdcL_I&Ah{+*J{
TntJfdre$L<Q>W)SirPB)VPTii2&te9R#oc2!9J2a49#@eP3_ENnJGRYD<uYK>bTH`e^b2z-Uq|eMByx#U7}3gKaU-Xv&EtC|qC0
w)v8MT(W<OHXVXU7t<UuwR39-QlKB#H=bGl>dE>5TnPHHrwO{ojx=^6R_-?`!MZg7Y+WE_C`qAm#wAN<&sg6OnBh2BzbTN|D?Zba
xQ=~K=<F=jKx<PV3V@RpOYXVIZpgPWG63VuYbGlW=)^X2YTztt>5<s0YO*4!LW?FyWrBH{AlZhD4r|fMmry2<kQ~o||EV{w%Gwh~
Ec0b7TrTE6MGu!bU4Uo`kb>c>j=qGcUoLn}ENugP$x)`A%|fq;1~BMA=maYr0tA{OtZRr6_7(!xKK$#!zd?m~xL&b!#=|dR%E6q9
HSjQ5iA{?zhDa(hah-Ee43?O<z6WHd4Y0T;Cwi|}8w@(920W?wXjFSW&}*$WFgmAAgfXDAM%pO}IBiPXyrb2q3*t1TA*cyGhb2!N
pyQ`P(N7UoVlAo4eX2r03zXdeSm)@5L;n*xO0oighX6$D%SXV`XfdNv)Nnr_M+U=hq=!2-4jZ!4BL|vo34C-z>ChBe@(J=bG~in8
sL`1cTRtH*viAu|z&SoOs!cTax(a|31i=h@?%Y9k;Q)s2dtH53{{*RA6@S2s=qgxk;<(6_C|iVNz5WSi&Vw}{fV~sMBHhIbg)84w
E#x7H%^cE;o^AxIy{qm6F`sHJa2TC#T<*C>unC6Pyc;2U`;a>#((a-cROSsnZB!xk(x*meZt-~oT^UZ$Q}0?#Lgx)Ow=`m3#*xxl
zu`F;;fKvpJ&A(LDfD~33&whCuyYDq8?dBoniwrWG|R#urkCcXpghOO!r3<VY-?_U*GOg@=w_m5dum#V=rq@$i70`%DWFTmyi(Vj
Kpb=2$Xi*28o&i09;SdfZEEC`Zf23|D$~e~XNqMfOM1BvY2(6mJPX_pSP##Q+e&OLT;-CX=3~7@0XHV=D(SoaJsAzAuh6sXu7zn`
Q~Ve*w{vDZh0|x9V6vM#WM09c%%oticAa)G$-TDo)NSK%>bD)~xL@$x2%5TXhkQ5ub)@%B=OEB?9>&RC49&`%OmU)A@SW--R(v>>
eL^dOAK-p0<%q+!Io8jxdc(1R!?A?JsfxqXx)A=61s_q^p)A-W2Z0Hi@7_r{prj9dmyI<tEIhDy4*3{guq8y(ktv^Iw)PwlFY)-m
gapn={z$lqJQ86@er$+LqQG-F_)4*~h*shP7(^;t{t*&_{-eZgTcKrp$rcu|><1Cw*4}EgMhs%_I%4_>oGg}5sfIdW5KW#K41&p?
!61qpz~3exG#MEE(*^^Rb!sp$?w|k@6D{%44RgHM#=9xL<tH!<ic;IxPaCKMv>KQ*Q`ocAu;nb1Dh#U4F8L)J@*x`v#=;+#rb6-;
4$zBIx-qOXZ^7v^YV|ofcXWNwiNORl`#ibNO~4u}$}kLma;L8ko=p%d;z836-09S_y`0SuTJ;SOJC2ekZ!0X5*mGPH-&f>iLS87j
pl1=a7ie_8Qw;nYCAGX*lC9K`1sWr3VZmo#t4fHJntd%BHd^c;?;WS53px6lW@)UJA|RdnKPynU8#q)xvbWFY#psld=(YZjN&{%a
==J|k)dz~uKT#yuDO3^BSQa5X$KR!mU}67h*4r;;y=nan`NB3?{cMxf&$Ld&Q(5T5*wi|Oe3s&aINr(bYM*KtffO@ngervyZ$!BC
1~4`Zlo#pST=4xsV4iKIY6WQ*D1~@gF>{^BQi7EmDK}St^u!(&ac1b${(QNJk+NglDe&`8;AIQnQr)s%KaF;e#??PHOrceJ@zuMn
@0a(JC$+uXQhf?Ihp!Fs2iW=_t5i)VLWeH!6<VFn5+Ot`*-zHNe;`qmY2uSI#ZP6cRpLVqM_ycnsuYqUv{qMBCl2tvrzt6UY1j;$
1eNM%ye2D|oyCHyk$5u3T75R_xZv0H#R6X~PBb0wJpJ$u$X_kEsBtaQex~R`HIs7Dq+B(5QZ~Ue{a#E@!5smV^$VeQ3MWr8fySZh
%GWGY<4r*mQ>>UL?9-9ti9$6M3y^5)6`~I#gaN(cExtMt88|%kMG}tve>D#mN;1}7&b<-q57TcXLT2DkBD6|&1()`0lJ1+wCQhob
EFR`y--J*3aTJzD6atkW_(vwqA=|@K<HAHVWUhkwa^ac_FOEI`&cyeKCWtl>5OcI46d(v>*eT+ITi(NW(!D+fQ5r+*Aj2IRhmg``
AUTkwoEma-T%N0p#u6)mO;kSoadUlk(lby0I6p66H9q>|#ylI);PC3hZSTbFnK1Za&@<om2ED89xp|Bay+3by0QO<fQ3fAw%r5l)
F}Uen_5SQ$3~|DhdC@z5*BzW4<CNaj&Dkk5Z+aCO(YU^?ZYY$&i(tS9yt{0>>V}=>S4opd++N%T!R=;HUlHs<Ya_;$yz?RMuWk0c
#9hQHm3DV=sQ4mR+#1v}T%!UKfueBlV^es=E21z8^C33+jAfG8!$O~#3D*Q15gu!WRgC&R{RMYPzfJmm{d<GD=;45RMgQx%@%pu#
@bqONqt$leTGI(cSZp4bRyt@D9ucuvOi+>i&0kXf2>VG1duf%Q$3DaBIgm8ElGuznIeR3%0%yKj3Xn7BJIGH8$eT~F{4L~ku}G-)
KO!CfX73Q6;{HdJzl=LO)xRSnKS23+1Y;NF+=?JWIyU14#J>_F&Ur0PBO_5f{!q*Wx)X`+I77FC=V#GPtT~zv$4tC=Vopp_^VoE<
vuaB0*lvlQA8dH(PehL_0%dF?47(JibT{iw8ls0BB_#vJdw1e3F`20L&b_z7H5FZ4Q_t?&VhYKAW51Vf9N~?(`|+rfCD;{wD@z4r
IU-yeMAem3<2!@J3?9P##xrXS5e{>JwBu5Clu)KnR8!1}Z!pM0*#Uc{wRg~7?xM}sX_l}2)eNK<>m{XqP&XYDMj^m_3}MzDGQ7Y|
6dOOLTf%0g8hdyCKea*GrIC0h{1PFJXSm&wS^-ur<4Tq`Lo}~eFjA>xRRN9O%~}m+8Jq})5RF?6NQAN?Rb|`}1qC}8RVENj;jb-!
;oJ&Ugr^sWQq}>+V#x@(i>VC-@5W1Gg1yg7eSB%&V|Hoo!QF}%6qmrJVWljvjS&owWy}b8vZr)K(a|dn_Xu}}BkdkQ_?gY1!XmyQ
RiC47D?p#?hZLt&rquqMH=d)IWYowX$``5-c`C{bDM%l*H_e@3*TziPb@2WwD~KhQwuB(CLRpEIN=)fzK$a)#O?VYg20oq0T5}aY
dD?T9i!fF(X2L6QbP3zU8*%(5TDmNDQNofSf>0Vxh*jDZO{-QufA%Zd9!v@xag)A~amQOQQPCY<6mN+DUv@xdC(fFP09^LWwI3>4
CqW~haQrMQn>`ZOcp>5|Oy^wAZHp;;>j<JlbFxib{KR9O-7ZSs0tzUQQbz&-Q2-}}kM0V=u0c-(n=9igJ??N?-k}I1NGa6EQ3W#)
IJwH{ZH4KN(h8-QQgPr0r1`OM#+92Pbquo(2=1@X-VQ1Z@s;iFn}$|<+IuJp1@eSBky$uy&~HIro)>fhyC6}*y+CL-S|+zV=|<c(
k!xJ_h99nODs<Tv+0NugbbIm4Y973zzP*{dalAV>PQ-Tsa_aZLlI$Me;NY-(b_Hom{;6d5kCU?-=)S(j+yjKdH1QBj6C}bkQN&HN
(iWor+5d%QUufERy=>~)R^tA{?=*WGNW+x%ESS4B2&FCjq-B2RP9m%Q<QvZG?P9o9j6Gw2ukqryn!_J|P|5z&UsT$`eD0RNsg$3N
ptX@e3(&*j$CQ8TBT6|CZx`VfKi9l|?uNCv3LCL==CZf!BP7PxdoW`X%ww<;imf<Gq?{|R@>cn%^zrClx*aPoxc<Z?*=K7+-@V84
**|IkVeTdbYo`9qyF0LQc6FzGbLZuYJ9KFW=KaMhJD>fZzUE7pdrB93riHDRUs40!sZkt!uC@h0rzH$0dapLn@V$R=rg-n3&-tnM
$x?nYJf}u&YSeaKh+}>I8PG;;+Ne$RZlu4Z8F~vQ=}qFZDi{qsP(RiHppGvKzmF#V5t_J&X5sMcI64myq3JFVE95e&I@p?M`Z@GD
g*9!=ROYIq!%;c(+5nwt)^CG=KGYr@u>_ctw3rTd&jFY1*-GKHRPjcW%^fDb1y9y!n$WH}F5Yn>6kr>`TzsOMH)sNiDg3jmO&zu2
yrw!RNI;hZ>fz83fWS`bKz&-$2e|^71u(*cLV{2@1GG>_5w4>$?rt`}1yai}i49VrY#yxLNEUNdR3AhtQG#C7fhf>DEhV-35~-?z
x8iH48&7E<ifj3LV*Rin)zgN)0OrGzU<alKv|uY?lmmo#mjPrA&*&Wfw;+Ic7a%SJtgI+*aJ66*(@!equ0`JorPZ=U+YTs#SwM78
8Dd%`qnj4NH~As8N2cD2w(3xRyK=oZ4Ce62bXtuGPX^teJ{9V$umC!1JJ5Dk!Mg~e7MFeML5P1<BEGDT!1mdiYE+lil{RL|IbZGc
?Gfw+_!}>rZ<WbbDUbi#XNphvbv!ewdgi%?Gepl~)EZY8qkZviWg$L6>R?b?aA7LYou<N1m_t!q!u=Yesv)ZM_WOPQfmu>bzXzlj
OUvg*#L%iVRP&bUsIpjy@5B~bXR*L9q4+&EfPU^Rv9*t_m4wDvPJAA>SZFX{2ReSupzHTKx?eS6_gdP5MPw7!W8SK8XhKRTh?n26
1&$M|A+t7K%;fi_L1f}1UHg$Ix8e!j@k+Fgvi899mmwL9W5r-aPr3vZ=a`wCg*Z^pjT9RGx8vSLuB)y}$A<|1;o<F^6`mwv%}%Dw
c`?TC(@!nSTT|fw_@Wkh(FW-9D9n=xX!bLQMCXu^!0x|$7E}U|+VW4gy%-(5wBv&@h}uiE;_wS(N`(ePD86|bGEw`+7Z;}%q*N@3
9LhxLNmvu+b2I@3Gm{y(A%2}2qWO&Z$d_N#WGLGqPx%32gl=Zdl=U0lNUtr4<H^7I6!{l(?s!qAn}}4>B}xJ)+FXA0Ln1C|NNZ-!
T_ITw#q~DG8N&Pv=F<B#e@i?|U)f8s%_ZMUAhw;yfnp`Ni@hfoi-mKImy<a0k|kZlay;wK58&BuE6Geq;o!p!-7^kzw2-VODK|D7
w%xMFN48wD)rzgx;wwWe@`*}WLt|=_8PIMq`f^A84O*fnz2r4P_j5%b)>(5EP#V?EM(fz6Zdk^sZns*;DRslrM)mPA{ZAoCmbWLd
&K<hU7ez&IAQS9481xmmWH9fs)|t<X0I-Q20D4zOg0L=0ia5$OX6$5TxGLavHAMh+Qk*gVmnl@*RMulq59}xFX;KetCF^OCe$Qty
AMW8nsb43sF=n^zm^p1HW>Gr=XWX98ncH^VZ<>yD(57Jye%}J>wb|(Ug8tJOTWr9(kB``Z<(5lqw8r{sg^m5OzFuSFVEnwo7q6)y
RUDRi@s653v!aAoCfw0CXqh)!rKl6cyoy&8Ncm=zd_#q~rnsq=@ta;TX4jo^yKYKd7C%hbcTjC%*}alk-~AN)6~qGMc`<n4qmeXM
u<<er<oEwMC&t>7w{=t;Co@%<8m8N*u&E)A&1G0P&4-NQ5GaAXuBj*)$f7h`-ZRiLLx=UR-C3f<|L8_Rg@p|!K#D_G&>ub1e+~Vy
=r0rlM_54lGO7?~D)NR7{g*FbpI~-IMiUgcwa=QyZ*0HSdJTVGfl{{)UX6ET!o%YQ!@(<mqrOpL5Dj|xpOymdRyGw@*}}g^__u_A
EBLp@LULY9iLoI0mkNw9_W!E380NLb0^2I%wy1-Jc@^=dcXe?sYH49E3aoN*HmETAuacx%Lh4ln8GiUz?+WJXAzq1kNojGBliu5_
UQdEb?Jbq`Za&;#;qAlq8A-?Shu-Pw+3{I#a08Rj%I(ni-A!u$8@0lJz54*|lMff&vjNb1G3;KQU4Ix9FDm?e#qisI{SR0kowo
"""
raw=zlib.decompress(base64.b85decode("".join(DATA.split())))
assert len(raw)==19926 and hashlib.sha256(raw).hexdigest()=="1960f6380585c0d4c367501cc3a686062903576d9e34fbcbfc9d1f900d7317f5"
PINS={'unequal_audit.py': [14454, '9220c1953e536a4b795a967d69092104fd8a5edb34264f525a208437a3950748'], 'unequal_certificate.py': [5034, '91f36dd6f256f406fc935c816ade0730f008f4efee167b4c82569e9c0ffeec80']}
files=json.loads(raw)
assert set(files)==set(PINS)
out=Path(sys.argv[1] if len(sys.argv)>1 else "unequal_cap_recovered")
out.mkdir(parents=True,exist_ok=True)
for name in sorted(files):
 data=files[name].encode()
 assert [len(data),hashlib.sha256(data).hexdigest()]==PINS[name]
 (out/name).write_bytes(data)
 print(name,*PINS[name])
print("UNEQUAL_ENDPOINT_PAIRED_APPENDAGE_SOURCE_RECOVERY_PASS")

```
