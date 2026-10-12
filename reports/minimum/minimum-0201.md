# minimum-0201

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# K2_TERMINAL_PLANE_TWO_NONPROJECTIVE_ALL_POSITIVE_PROJECTIVITIES_V1

## 1. Новый результат

**Полностью закрыто пятипараметрическое пространство формы: две независимые непроективные степени свободы настоящей терминальной грани F6 и ВСЕ положительные проективности каждого полученного тела.** Для каждого тела берётся новый собственный объёмный центроид равномерного заполнения. При любой общей SPD-метрике N, с M=N⁻¹, доказано

```text
D65≥0, D54≥0, D43≥0  ⇒  T=Λ05+Λ06<2.
```

Λ05 использует всю настоящую четырёхугольную F5, Λ06 — всю настоящую треугольную F6. Ограничения на обусловленность, устойчивость F0, primal-U1, отсутствие дополнительных слабых равновесий или отрицательные нетеревянные тени для этой импликации не нужны.

Следовательно, **буквальный FULL253 невозможен на всём указанном классе**. Здесь FULL253 — весь неотрицательный граф из ровно восьми пар

```text
(1,0),(2,1),(3,2),(4,3),(5,4),(6,5),(7,0),(8,7),
```

а не произвольный граф, содержащий это дерево. Его принятая концентрационная посылка T>51/25 используется только для последнего вывода о FULL253. Новый результат не является запретом всех ориентаций110 или всех реализаций инцидентности. Предыдущий принятый результат закрывал лишь проективный класс одного фиксированного spring-base.

Новый механизм — точная формула удаления настоящего тетраэдра и единый **четвертной объёмно-гранный бюджет**. Он связывает цельногранный избыток с необходимым отношением настоящих полюсов. Старые матричные сетки, веса и нормировки fs/js не переносились.

## 2. Полный непроективный класс и его идентичность

Обозначим неизменённые вершины исходного spring-base через X0,…,X9. Его настоящие грани:

```text
F0=012; F1=34510; F2=6743; F3=2768; F4=0289;
F5=9630; F6=986; F7=5721; F8=754.
```

Настоящие рёбра:

```text
01,02,03,09,12,15,27,28,34,36,45,47,57,67,68,69,89.
```

Инцидентности вершин:

```text
(0,1,4,5),(0,1,7),(0,3,4,7),(1,2,5),(1,2,8),
(1,7,8),(2,3,5,6),(2,3,7,8),(3,4,6),(4,5,6).
```

Это та же маркировка10/17/9, W={0,5}, без контакта056. Соседи F6 — F3,F4,F5; стрелки65,54,43 проходят по настоящим рёбрам69,09,28. Исходные14геометрических коэффициентов сохранены буквально:

```text
(1,5,12219,1,14102,14220,32,8740,81,76,111,18,19,1).
```

Они относятся к14лексикографическим рёбрам после удаления01,02,12. Внешние плоские вершины0,1,2 равны(0,0),(1,0),(0,1); рациональный Лапласиан, внешние напряжения и согласованный Maxwell-подъём от F0:z=0 с minz=−1,maxz=0 полностью восстановлены в капсуле. Это параметры формы, не массы. Исходное тело не заменено изменённым набором пружин под прежним именем.

Пусть

```text
O=plane(F3)∩plane(F4)∩plane(F5)=(469/379)X9,
K=conv(X0,X1,X2,X3,X4,X5,X6,X7,O).
```

K получается удалением всей опоры F6. Новое семейство определяется **ровно** так:

```text
V_i(s,t)=X_i,                      i=0,…,7,
V_8(s,t)=(1−s)O+sX2,
V_9(s,t)=(1−t)O+tX0,
P(s,t)=conv(V_0,…,V_9),            0<s<1, 0<t<1.             (1)
```

Это полный терминальный plane-chamber при фиксированных остальных восьми опорных плоскостях и сохранённой инцидентности. F6 перемещается как одна настоящая максимальная грань через неизменённую вершину6. Интеграционные треугольники не получают независимых движений.

Исходный spring-base является членом(1) при

```text
s0=267938/268317,  t0=90/469.
```

Обе точные равенства V8(s0,t0)=X8 и V9(s0,t0)=X9 проверены. Все пять четырёхточечных определителей репера(0,1,2,3,6) ненулевые. Любая размеченная проективность между двумя членами(1) фиксировала бы этот репер, значит была бы тождественной. Поэтому разные пары(s,t) действительно дают разные размеченные проективные классы. Добавление трёх параметров положительного знаменателя даёт пять независимых параметров формы modulo аффинные преобразования.

**Полная область новой теоремы:** для всех0<s,t<1 и всех аффинных форм ℓ(X)=a+p·X, строго положительных во всех десяти V_i(s,t), рассматривается

```text
{V_i(s,t)/ℓ(V_i(s,t))},
```

с новым равномерным заполнением и настоящим центроидом. Все конечные слабые механические стенки и все неограниченные проективные подходы внутри этой области включены. Грани s=0,1 или t=0,1 меняют решётку и не объявляются дополнительными10/17/9телами.

## 3. Настоящая геометрия вырезаемого тетраэдра

Перейдём к фиксированной аффинной карте

```text
Y=[X0−O, X2−O, X6−O]⁻¹(X−O).
```

O становится0, X0=e1, X2=e2, X6=e3. Исходный корневой зазор равен1−x−y−k0z, где

```text
k0=1027684771516514730560324461/5226845180087214772917470469.
```

Выпуклый K лежит в положительном октанте. Его три координатные грани — F3:x=0, F4:z=0, F5:y=0. Все остальные настоящие вершины лежат строго вне тетраэдра conv(0,e1,e2,e3). Формула(1) становится

```text
P(s,t)=K∩{x/t+y/s+z≥1}.
```

Удалённая трёхмерная область — точно тетраэдр conv(0,t e1,s e2,e3), без свободного выбора объёмных весов. Все остальные вершины сохранены; меняются только два простых конца8,9 и целые F3,F4,F5,F6. Точные опорные проверки и полный перебор независимых троек плоскостей восстанавливают именно указанную решётку.

Теперь произвольная ℓ, положительная на P(s,t), разбивается по знаку ℓ(O).

### ℓ(O)<0: универсальная тетраэдральная механика

Барицентрические функции удалённого тетраэдра до преобразования равны x/t,y/s,z,1−x/t−y/s−z. На P первые три неотрицательны, последняя неположительна. После проективности умножим каждую функцию на значение ℓ в соответствующей вершине тетраэдра и разделим на ℓ(X). Получаются четыре неотрицательные аффинные функции с суммой1. Их четыре конечные вершины аффинно независимы: образ P лежит в ограниченном тетраэдре, чья полная базовая грань — настоящая F6.

Для нового равномерного P его барицентрические средние t3,t4,t5≥1/4,0<t6≤1/4: каждый из трёх базовых вершинных вееров даёт соответствующее1/4. Поэтому

```text
q6=−αq4−βq5−γq3, α,β,γ≥1,
0=2‖q6−q5/2+q4/4‖N²
 +(α+γ−1/8)‖q4‖N²+β‖q5‖N²
 +2D65+(β+1/2)D54+γD43.
```

Строго положительная квадратичная часть исключает три слабые стрелки. Использован центроид реального P, не центроид содержащего тетраэдра. Это общий механизм родителя, не специфический новый коэффициентный расчёт.

При ℓ(O)=0 три преобразованные координатные функции уже суммируются в1. Их положительная зависимость на настоящем центроиде исключает D54≥0,D43≥0 скалярным произведением с Nq4. Эта конечная физическая стенка также закрыта.

### ℓ(O)>0: полная нормальная карта без потери параметров

Поскольку K=conv(P(s,t),O), ℓ положительна на всём K. После проективности перенесём образ O в0 и аффинно вернём три его соседние вершины к e1,e2,e3. В этой карте

```text
Y ↦ diag(l1,l2,l3)Y/[a+p_x x+p_y y+p_z z],
a=ℓ(O)>0, l_i=ℓ(e_i)>0.
```

На каждой оси доля θ преобразуется в l_i θ/[a+(l_i−a)θ], биекцию(0,1) на(0,1). Следовательно, можно свободно выбирать положительную проективность K и затем **любые** новые cap-доли s,t∈(0,1). Это ровно вся нужная сторона, а не независимое ослабление плотности или потеря части исходных пар.

Во всём дальнейшем K обозначает этот новый, равномерно заполненный и аффинно нормированный released-образ. Его корневая плоскость имеет зазор

```text
L=1−x−y−kz,  k<1.
```

k может быть отрицательным и неограниченным; нигде не вводится k≥0.

## 4. Общая формула реального тела и четвертной бюджет

Определим только по настоящему released-телу K:

```text
D=6 Vol(K),
(U,W,Z)=24 ∫_K(x,y,z),
B=6 ∫_{F5(K)}L dA,                 F5(K) лежит в y=0,
E=4D−U−W−kZ.
```

Здесь D — шестикратный объём, не механический примитив. B использует всю настоящую F5(K). Для P=K∩{x/t+y/s+z≥1} имеем точно

```text
d=D−st>0,
e=E+st(s+t+k−4)>0,
Vol(P)=d/6,
g=((U−st²),(W−s²t),(Z−st))/(4d),
L(g)=e/(4d).                                             (2)
```

Удалённый тетраэдр имеет объём st/6 и первый момент st(t,s,1)/24. На F5 удаляется ровно треугольник conv(0,e3,t e1), для которого6∫L=t(3−t−k). Новая F6 имеет coarea st/2 и среднее L=(3−s−t−k)/3. Поэтому цельногранный след равен

```text
n=(W−s²t)[B−t(3−t−k)]
  +[sU+tW+st(Z−4D+st)](3−s−t−k),
T=Λ05+Λ06=n/(de).                                        (3)
```

Это интегралы нового равномерного тела, не перенос старого g или старой плотности.

Положим

```text
F(s,t)=2de−n,
J(s,t)=3sU−tW+st(4D+3Z)−9s²t².                          (4)
```

**Новый непрерывный объёмно-гранный результат:** на всех положительных проективных образах нашего released K, для всего замкнутого квадрата cap-параметров,

```text
F(s,t)+(1/4)J(s,t) ≥ 0,   0≤s,t≤1.                       (5)
```

На вырожденных cap-границах это только полиномиальный сертификат. Физическая теорема использует0<s,t<1.

### Почему одна общая метрика заставляет J<0

В нормальной карте настоящие координатные полюса независимы, и

```text
q6=ξq4+ηq5+ζq3,
H=gx/t+gy/s+gz−1>0,
ξ=gz/H, η=(gy/s)/H, ζ=(gx/t)/H>0,
ξ+η+ζ=1+1/H>1.
```

Три слабые стрелки65,54,43 требуют ξ+ζ<1/4. Для полноты нужный строгий шаг: нормируем ‖q5‖N=1; пусть r=‖q4‖N>1,s*=q4ᵀNq5∈[1,r), τ=ξ+ζ. Стрелка6→5 помещает q6 в шар с центром q5/2 и радиусом1/2. Независимость трёх координатных полюсов делает максимум q4ᵀNq6 строго меньше(s*+r)/2. Из4→3 одновременно следует q4ᵀNq6≥ηs*+τr². Значит,

```text
(1−2η)s*+r−2τr²>0.
```

При η≤1/2 это невозможно из η+τ>1 и s*<r. При η>1/2 левая часть не больше1−2η+r−2τr²; если τ≥1/4, последний полином убывает приr>1 и уже отрицателен приr=1. Поэтому τ<1/4 даже для слабых стрелок и любой полноранговой N.

Подстановка настоящего g из(2) даёт

```text
gy/s−3gx/t−3gz−1>0  ⇔  J(s,t)<0.                        (6)
```

Из(5),(6) следует количественный результат

```text
2−T=F/(de) ≥ −J/(4de)>0.                                 (7)
```

В частности, на этой геометрической стороне **T≥2 заставляет ξ+ζ≥1/4**, то есть запрещённое общиметрическое отношение. Это искомая связь именно цельногранного избытка с настоящими полюсами. Порог2 здесь не отождествлён с FULL253-порогом51/25.

## 5. Полное доказательное покрытие(5)

Каждая опора released K переводится в примитивный целочисленный зазор R_i=(b_i,−n_i) в только что указанной фиксированной осевой карте. Общий положительный знаменатель снимается, затем делится положительный НОД; знак опоры не меняется. Это **новая буквальная нормировка**, не перенос прежних fs/js или стрелочных весов.

Все положительные формы на released K покрыты семью полными конусами:

```text
0125, 0128, 0178, 0235, 0237, 0278, 0345,
```

где, например,0125 означает cone(R0,R1,R2,R5). Полный перебор активных базисов в сечении ℓ(gK)=1 восстанавливает ровно восемь лучей. Звёздный веер из R0 соответствует вершинам3,4,5,6,7,O. Единственная четырёхугольная параметрическая грань имеет цикл(2,3,7,8) и разделяется диагональю2–7. Это диагональ пространства параметров, не новое физическое ребро. Полнота проверена по настоящей released-решётке, без отбрасывания каких-либо ячеек.

На каждом конусе r=Σλ_iR_i, λ_i≥0. Обозначим l_v=ℓ(Y_v), v=0,…,7, и a=ℓ(O). Пусть

```text
A0=l_0 l_2 l_6,
Lprod=∏_{v=0}^7 l_v,
Rprod=l_1 l_3 l_4 l_5 l_7,
Hpoly=Rprod²>0,
k_d=l_6>0, k_n=a k0+p_z.
```

Для настоящего веера released K из O=0, δ_abc=det(Y_a,Y_b,Y_c)≥0, в source построены

```text
D0poly=Σ_τ δ_τ∏_{v∉τ,v≤7}l_v,
R_j=Σ_τ δ_τ(∏_{v∉τ,v≤7}l_v)
                     Σ_{w∈τ}(Y_w)_j∏_{v≠w,v≤7}l_v.
```

После осевой нормировки реальные величины удовлетворяют

```text
D=D_num/Hpoly, D_num=D0poly Rprod,
U=U_num/Hpoly, U_num=R_x/(l_2 l_6),
W=W_num/Hpoly, W_num=R_y/(l_0 l_6),
Z=Z_num/Hpoly, Z_num=R_z/(l_0 l_2),
k=k_n/k_d,
B=B_num/(Hpoly k_d).
```

B_num получается интегрированием полной F5(K), с точными coarea-массами каждого её треугольника. Все указанные деления полиномов проверяются обратным умножением. D_num,U_num,W_num,Z_num,Hpoly имеют степень10; B_num —11. Семь независимых прямых физических проверок точно сопоставляют эти полиномы настоящим объёмам, первым моментам, k и B.

Умножение(5) на положительное Hpoly²k_d даёт многочлен степени21 по четырём λ и бистепени(3,2) по(s,t). Для всего квадрата[0,1]² его12тензорных коэффициентов Бернштейна — однородные многочлены отλ со следующими полными точными знаковыми счётчиками:

| Конус | Положительных | Нулевых | Отрицательных |
|---|---:|---:|---:|
|0125|16680|7608|0|
|0128|16140|8148|0|
|0178|13344|10944|0|
|0235|21036|3252|0|
|0237|18672|5616|0|
|0278|17988|6300|0|
|0345|23032|1256|0|

Всего126892положительных и43124нулевых из170016слотов. Для каждого из84полиномов проверен полный обратный переход в степенной базис cap-параметров. Все рациональные коэффициенты генерируются и сохраняются без потерь. Неотрицательность на всей замкнутой области следует из базиса Бернштейна и λ_i≥0; строгий физический вывод обеспечивается J<0, а не удалением нулевых границ.

Универсальный множитель здесь **ровно1/4 в нормировке реальных D,U,W,Z,B,k из раздела4**. Старое число10⁻5 из проективного родителя не используется.

### Форма механизма вне фиксированного released K

Формулы(2)–(4),(6) верны для любого настоящего компактного выпуклого K в положительном октанте с простым O, настоящими осевыми рёбрами Oe1,Oe2,Oe3 и настоящей корневой гранью в плоскости1−x−y−kz=0,k<1 черезe1,e2. Если12коэффициентов

```text
b_ij=Σ_{a≤i,b≤j} [s^a t^b](F+J/4)
                   ·binom(i,a)binom(j,b)/[binom(3,a)binom(2,b)],
i=0,…,3, j=0,…,2,
```

неотрицательны, то весь его терминальный cap-квадрат удовлетворяет трёхстрелочной импликации T<2. Это достаточное условие на **шесть настоящих объёмно-поверхностных величин**, пригодное при движении других граней и не ограничивающее число остальных вершин. Не утверждается, что эти12неравенств автоматически верны для всякого K. Новое точное покрытие доказывает их для всех положительных проективных образов именно нашего released K.

## 6. Сохранённые действительные контрконтроли

Новые тела имеют отдельные идентичности и не выданы за исходный spring-base.

**NONPROJECTIVE_HIGH_0:** raw-доли(s,t)=(99/100,1/5), затем ℓ=1+(93/100)z в исходной карте. Настоящий T>207/100, приблизительно2.0711451351458514.

**NONPROJECTIVE_HIGH_1:** raw-доли(99/100,1/4), тот же знаменатель. T>51/25, приблизительно2.059350192734460.

Для обоих использована одна явно заданная взаимно обратная пара

```text
R=((1,1/5,1/7),(0,3/2,1/11),(0,0,2)), N=RᵀR, M=N⁻¹.
```

Их полный настоящий census одинаков:

```text
S=[3,4,5,6], U=[0,2,6],
H=[(0,2),(0,9),(3,6),(6,8),(8,9)], strict435, weak000.
```

Все68примитивов ненулевые. Знаки восьми родительских стрелок: семь отрицательных и только8→7 положительная. Полные неотрицательные графы имеют12 и11стрелок, поэтому это не FULL253. Эти тела показывают, что новая теорема не является безусловным низким следом всего расширенного семейства.

**NONPROJECTIVE_THREE_STRICT:** в осевой карте released K без проективности берём(s,t)=(1/100,1/2). Его настоящий объём

```text
40857276960616273168855523525071764641 /
48262980410829175455234916147331772300.
```

Пусть q — его реальные полюса при собственном g, а ξ,η,ζ решают q6=ξq4+ηq5+ζq3. Полная рациональная метрика задаётся без численных входов:

```text
x=(101/100,7/2,0), y=(1,0,0), v=(501/800,7/16,1/20),
z=(v−ξx−ηy)/ζ,
H=[x y z][q4 q5 q3]⁻¹,
N=HᵀH, M=N⁻¹.
```

Получены D65=25699/640000,D54=1/100,D43>14 и

```text
1<T<101/100, T≈1.0093728051377113,
S=[0,3], U=[1,2], Hsaddle=[(0,2),(1,2)], strict222, weak000.
```

F0 строго устойчива. Полный неотрицательный полярный граф имеет18пар:

```text
(1,0),(2,3),(2,7),(2,8),(4,2),(4,3),(4,7),(4,8),
(5,0),(5,1),(5,4),(6,0),(6,1),(6,4),(6,5),(7,3),(8,3),(8,7).
```

Он не совпадает с FULL253. Это новый непроективный пример осуществимости трёх стрелок, не контрпример к доказанному T<2.

**NONPROJECTIVE_THREE_WEAK_WALL:** в этой же точной конструкции заменить толькоx на(1,7/2,0) и заново определитьz,H,N. Тогда D54=0, остальные две выделенные стрелки положительны. Census остаётся222weak000. Единственный нулевой edge-примитив находится на настоящем ребре09; его четырёхпакет имеет знаки(+,-,-,0). Поэтому нуль является безвредной слабой стрелкой, **не физическим слабым равновесием**. Неотрицательный граф тот же18пар.

В капсуле сохранены также семь физических представителей конусов, все с собственным census323weak000. Итого11тел/метрик,747ненулевых примитивов и один указанный безвредный нуль. Это endpoint-контроли, не утверждение о постоянстве census на всём семействе. Ни один из них не110.

## 7. Что было сделано и точная граница продолжения

Исследована независимая целоплоскостная свобода F6, а не новая точка старого проективного класса. Настоящее разбиение на released K и удалённый тетраэдр дало низкую степень по двум новым параметрам. Попытка оставить только безусловную положительность2−T не дала полного доказательства; универсальная связь с J и единый множитель1/4 закрыли весь квадрат во всех семи конусах. Неуспешный коэффициентный тест не трактовался как осуществимость или исключение тела.

**Внутри класса(1) плюс все его положительные проективности остатка нет.** Остаются движения остальных восьми плоскостей released K, другие реализации этой маркированной инцидентности и остальные K2-домены. Невозможность110 с иной полярной ориентацией здесь не доказана. Ни один canonical/incidence/root-счётчик не уменьшен; K2=55 и34≤Cmin≤622 сохраняются.

Наиболее полезное продолжение — двигать независимые грани released K и контролировать12моментных неравенств раздела5 либо найти действительный контрконтроль к их расширению. Старый фиксированный проективный класс и теперь весь терминальный двухпараметрический chamber больше не являются открытыми направлениями.

## 8. Наследственная recovery-цепь полностью восстановлена

Буквальный parent — minimum-0198, SHA af7d186c2061dd246a000737609a26b4da65470652649ba74e3e03b6e2ebd8d3. Его прежний усечённый DATA действительно не был исполняемой передачей, как прямо указано в конце источника.

**Ниже эта зависимость устранена полностью.** Капсула содержит пять исходных единиц родителя без изменения байтов и три новые полные единицы. Из исходной source-map и полного шаблона она детерминированно восстанавливает именно старый recover_k2_projective.py — все17549байт с прежним SHA. Его полное DATA регенерируется стандартным zlib-level9/base64 с буквальным разбиением112; никаких отсутствующих строк или внешних файлов нет. Восстановленный старый декодер отдельно исполнен в ещё одном пустом каталоге и вернул те же пять точных исходников. Это исправление поставки, не новая версия старой геометрии.

Предыдущий большой проективный коэффициентный proof заново не переаудировался. Его старые author-reported исполнения остаются на прежнем уровне свидетельства. Новая теорема использует собственное полное покрытие и новые actual-moment полиномы; старые коэффициентные таблицы не являются её входом.

## 9. Полный runnable source и реально выполненные проверки

Новый журнал прочитан полностью через EOF, включая буквальный parent. В новой цепи выполнены prepare, все семь cone-проверок, controls и finish. Затем полный нижеследующий source-only decoder восстановил всё в новом каталоге, и **все те же вычисления выполнены с нуля**. Все17доказательных выходов и девять файлов исходников совпали побайтно. Это точный холодный повтор одного генератора; не заявляется независимая реализация всего верификатора, coordinator replay или proof-assistant-формализация.

Дополнительные проверки: полное активнобазисное покрытие нормального конуса, все опорные инцидентности, два разных настоящих объёмных веера каждого контроля, полные физические Λ-идентичности, точное совпадение независимых физических моментов с полиномами, обратные полиномиальные деления и восстановление всех84Бернштейн-полиномов.

Среда: **CPython3.13.5, стандартная библиотека, zlib1.3.1, assertions включены**. zlib-пин относится также к точному воспроизведению сжатых файлов; все математические коэффициенты рациональные. Никаких NumPy/SciPy/SymPy, оптимизатора, RNG, pickle-cache или внешней таблицы в доказательной цепи нет.

Сохранить полный блок ниже как recover_k2_caps.py, UTF-8/LF с конечным LF:

```text
python -S recover_k2_caps.py fresh
cd fresh
python -S cap_family.py check
```

Для раздельных коротких вызовов: decoder с --extract-only, затем cap_family.py prepare; cone0,…,cone6; controls; finish. Старый проективный proof независимо регенерируется восстановленным recover_k2_projective.py в другом каталоге. Новый check действительно пересчитывает коэффициенты и физические контроли, а не только проверяет имеющиеся хэши.

Pins:

```text
recover_k2_caps.py:27776bytes
c404d8872e603a1dcb1ac8ab0c49b8159f27eb2715705a5efafa691eef49c248
payload:55299bytes
5fd4075095c0498aa9bdaa90570140c72c82895d224e94ae40cc9f046aab39f8

Восстановленный неизменённый recover_k2_projective.py:17549bytes
041c31b00f32e44bb8bde71563de4b1a38a40d73588f75790f04307171cc3456
Его неизменённая source-map:30237bytes
a392b0970a424785b3814579f244f3d5b1e97eef159eb997ffd2c2bdc23771e2

cap_polys.py:4436bytes
ec6d975d32e641be6d09f75aafe3f363ee1af67bb9b4b19b08803e874734e10b
cap_actual.py:5286bytes
2282b233f442d69fe6889cfe6b6d837871888e9398108b1427cded0c5dd72724
cap_family.py:13106bytes
c79123db512a8dfb4bd3eb19a4b994f3f35896ab8f13e2bc2e2567f65178cf64

cap_result.json:2443bytes
9c8ea59971bb58e1198f0c9783769917fd201a03987bf93311f64e386a46c702
cap_controls.json.gz:995193bytes
48c303a53027a4030b5ba0b5e173ff644d0b83996c65bdecf80fcecd510b0b32
```

cap_result.json содержит остальные точные pins. Все126892ненулевых коэффициента регенерируются и сохраняются полностью в семи cap_coefficients_i.json.gz. Их исходный рациональный формат имеет один положительный знаменатель на полином и полные целые числители с radix64-кодом четырёх показателей; декодирование однозначно и включено в исходный polynomial unit.

Главные маркеры:

```text
K2_INHERITED_FULL_17549_BYTE_RECOVERY_RESTORED_PASS
K2_FULL_NONPROJECTIVE_TERMINAL_CHAMBER_TRUE_LATTICE_SEVEN_CONE_COVER_PASS
K2_CAP_FULL_CONE_QUARTER_TRACE_METRIC_COUPLING_PASS [семь конусов]
K2_CAP_ELEVEN_ACTUAL_COM_RECIPROCAL_CONTROLS_747_NONZERO_ONE_HARMLESS_ZERO_PASS
K2_TWO_NONPROJECTIVE_PLUS_ALL_PROJECTIVITIES_FULL253_ALL_SPD_PASS 2443 9c8ea59971bb58e1198f0c9783769917fd201a03987bf93311f64e386a46c702
K2_ACTUAL_CAP_QUARTER_BUDGET_FORCE_WHOLE_TRACE_LT_2_PASS
```

Дополнительные удобные копии: полный bundle с коэффициентами и восстановленным родителем (`K2_CAP_NONPROJECTIVE_FULL_bundle.zip`), декодер (`recover_k2_caps.py`). Они не заменяют следующий полный источник.

### Полный автономный восстановитель

```python
"""Complete K2 nonprojective cap family, including exact inherited recovery.
CPython3.13.5 standard library, zlib1.3.1. No other files are required.
python -S recover_k2_caps.py NEW_DIRECTORY [--extract-only]
"""
import base64,hashlib,json,lzma,subprocess,sys,zlib
from pathlib import Path
PAYLOAD_PIN=[55299, '5fd4075095c0498aa9bdaa90570140c72c82895d224e94ae40cc9f046aab39f8']
PARENT_MAP_PIN=[30237,'a392b0970a424785b3814579f244f3d5b1e97eef159eb997ffd2c2bdc23771e2']
PARENT_RECOVERY_PIN=[17549,'041c31b00f32e44bb8bde71563de4b1a38a40d73588f75790f04307171cc3456']
RESULT_PIN=[2443, '9c8ea59971bb58e1198f0c9783769917fd201a03987bf93311f64e386a46c702']
DATA=(
 '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'
 'LOAN2rHEZ/sCAAAAAARZWg=='
)
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def main():
 assert __debug__ and sys.version_info[:3]==(3,13,5)
 assert zlib.ZLIB_RUNTIME_VERSION=='1.3.1' and len(sys.argv) in (2,3)
 if len(sys.argv)==3:assert sys.argv[2]=='--extract-only'
 raw=lzma.decompress(base64.b64decode(DATA,validate=True));assert pin(raw)==PAYLOAD_PIN
 files=json.loads(raw);head=files.pop('_parent_header');tail=files.pop('_parent_footer')
 old=('geometry.py','actual_form.py','fastpoly.py','fullcore.py','projective.py')
 assert set(files)==set(old)|{'cap_polys.py','cap_actual.py','cap_family.py'}
 prior=json.dumps({n:files[n] for n in old},sort_keys=True,separators=(',',':')).encode()
 assert pin(prior)==PARENT_MAP_PIN
 encoded=base64.b64encode(zlib.compress(prior,9)).decode()
 restored=head+'DATA=(\n'+''.join(' '+repr(encoded[i:i+112])+'\n' for i in range(0,len(encoded),112))+')\n'+tail
 assert pin(restored.encode())==PARENT_RECOVERY_PIN
 files['recover_k2_projective.py']=restored
 root=Path(sys.argv[1]).resolve();root.mkdir(parents=True,exist_ok=True)
 for name,text in files.items():
  assert name==Path(name).name and name.endswith('.py')
  f=root/name;b=text.encode();assert not f.exists() or f.read_bytes()==b;f.write_bytes(b)
 print('K2_INHERITED_FULL_17549_BYTE_RECOVERY_RESTORED_PASS',*PARENT_RECOVERY_PIN,flush=True)
 print('K2_ALL_EIGHT_SOURCE_UNITS_RECOVERED_PASS',*PAYLOAD_PIN,flush=True)
 if len(sys.argv)==2:
  subprocess.run([sys.executable,'-S','cap_family.py','all'],cwd=root,check=True)
  assert pin((root/'cap_result.json').read_bytes())==RESULT_PIN
  print('K2_NONPROJECTIVE_CAP_FULL_SOURCE_ONLY_RECOVERY_PASS',*RESULT_PIN,flush=True)
if __name__=='__main__':main()
```
