# minimum-0204

Historical AI scientific report · saved 2026-09-23 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# K2_RELEASED_BULK_QUARTER_AND_FULL_FIVE_SHAPE_CHAMBER_V1

## 1. Два новых результата

Получен **общегеометрический объёмно-центроидный критерий**, не привязанный к пружинным коэффициентам, числу остальных граней или проективному классу фиксированного тела.

Для настоящего released-тела K в описанной ниже осевой нормировке обозначим D=6Vol(K), U=24∫K x, W=24∫K y. Если

```text
D≥7/2,   U+W≤3D,
```

то для ВСЕГО настоящего терминального cap-квадрата 0<s,t<1, при новом равномерном заполнении и собственном объёмном центроиде,

```text
D65≥0, D54≥0, D43≥0  ⇒  T=Λ05+Λ06<367/180=51/25−1/900.       (A)
```

Используется одна произвольная SPD N и M=N⁻¹. Устойчивость F0, primal-U1, ограничение обусловленности и отсутствие дополнительных физических слабых точек не предполагаются. Поэтому весь этот непрерывный класс исключён для буквального FULL253.

При немного более сильном объёмном условии D≥18/5 получена именно исходная механически обусловленная граница2:

```text
F(s,t)+J(s,t)/4≥3/100,
D65,D54,D43≥0  ⇒  T<2.                                    (B)
```

Условие U+W≤3D — это проверяемое условие на НАСТОЯЩИЙ центроид released K: gK,x+gK,y≤3/4. Если корневой зазор L=1−x−y−kz имеет k≥0, оно автоматически следует из настоящего вершинного веера. Если k<0, оно остаётся дополнительным геометрическим условием; доказательство допускает отрицательные k без нижнего ограничения.

Независимо закрыто **полное новое пятипараметрическое семейство с пятью непроективными степенями свободы**, где движутся настоящие F0 и F8, а не только прежняя F6. На всём этом семействе доказана более сильная безусловная оценка T<2. Его геометрия буквально K2, оно не является повторной параметризацией принятого пружинного проективного класса.

Авторитет продолжения: `minimum-0201`, SHA `e645b20cf17f2913ad0d4128d86988b5f2bfa03417289e58772517f71dfccfcb`. Принятый терминальный chamber и его полная recovery-цепь не переобъявляются новыми результатами. :contentReference[oaicite:0]{index=0}

## 2. Буквальная геометрическая область общего критерия

Пусть K — настоящий конечный полноразмерный выпуклый многогранник в x,y,z≥0. Вершина O=0 простая, а концами трёх её настоящих рёбер являются

```text
e1=(1,0,0), e2=(0,1,0), e3=(0,0,1).
```

Предполагается настоящая корневая грань F0 с зазором

```text
L=1−x−y−kz≥0,  k<1,
```

содержащая e1,e2, но не O,e3. Координатные грани обозначены F3:x=0, F4:z=0, F5:y=0. Остальная граница K может иметь произвольную настоящую геометрию. В частности, F5 не обязана быть треугольником.

В этой нормировке K содержит тетраэдр Δ0=conv(O,e1,e2,e3), а его настоящая грань при z=0 в точности равна conv(O,e1,e2). Последнее следует из L≥0 при z=0 и обратного включения по выпуклости.

Для 0<s,t<1 определим реальное тело

```text
P(s,t)=K∩{x/t+y/s+z≥1}.
```

Удаляется в точности тетраэдр conv(O,t e1,s e2,e3). Новая настоящая F6 — треугольник(t e1,s e2,e3). Стрелки65,54,43 идут по настоящим рёбрам e3—t e1, t e1—e1, s e2—e2. Никакие диагонали интегрирования в эти предпосылки не входят.

Для буквальной K2-инцидентности сохраняются циклы

```text
F0=012; F1=34510; F2=6743; F3=2768; F4=0289;
F5=9630; F6=986; F7=5721; F8=754,
```

и настоящие рёбра

```text
01,02,03,09,12,15,27,28,34,36,45,47,57,67,68,69,89.
```

В осевой карте вершины0,2,6 — e1,e2,e3; вершины8,9 после усечения — s e2,t e1. Ориентация циклов при построении заново приводится наружу.

Вся нормировка аффинная. Поэтому утверждение допускает произвольные физические аффинные образы и все SPD, а не предполагает, что эти координаты ортонормальны в заранее заданной физической метрике.

## 3. Шесть настоящих величин и точная масса после усечения

Определим по одному и тому же равномерно заполненному K:

```text
D=6Vol(K),  (U,W,Z)=24∫K(x,y,z),
B=6∫F5(K) L dA,  E=4D−U−W−kZ=24∫K L.
```

B — интеграл по ПОЛНОЙ настоящей F5(K). После удаления настоящего тетраэдра:

```text
d=D−st,
e=E+st(s+t+k−4),
Vol(P)=d/6,
gP=(U−st², W−s²t, Z−st)/(4d),
L(gP)=e/(4d).
```

Это новый собственный объёмный центроид P. Ни центроид K, ни старая плотность не переносятся.

Положим

```text
n=(W−s²t)[B−t(3−t−k)]
  +[sU+tW+st(Z−4D+st)](3−s−t−k),
T=n/(de),
F=2de−n,
J=3sU−tW+st(4D+3Z)−9s²t²,
Q=F+J/4.                                                  (1)
```

Здесь d,e>0. Формула T использует всю оставшуюся F5 и всю новую F6: из F5 удалён реальный треугольник(O,e3,t e1), для которого 6∫L=t(3−t−k); coarea-масса F6 равна st/2, а средний L на ней равен(3−s−t−k)/3. Эти формулы сохраняют буквальную нормировку принятого cap-родителя. :contentReference[oaicite:1]{index=1}

## 4. Почему реальные геометрические ограничения дают бюджет

### 4.1. Необходимые ограничения именно настоящего K

Настоящие положительные тетраэдральные веера из e1,e2,e3 и O дают

```text
U≥D, W≥D, Z≥D, E≥D.
```

Действительно, среднее неотрицательной аффинной функции, равной1 в вершине веера, не меньше1/4. При дополнительном U+W≤3D получаем U,W≤2D. При k≥0 это дополнительное условие автоматически: E≥D и E=4D−U−W−kZ.

Есть ещё две существенные геометрические границы:

```text
Z≤D²,  B≥2−k.                                             (2)
```

Вторая следует из занятого настоящего треугольника conv(O,e1,e3)⊂F5 и L≥0.

Для первой используется настоящая треугольная база K при z=0 площади1/2. Для любого выпуклого тела с базой площади A0, объёмом V и первым моментом Iz=∫z справедливо A0 Iz≤3V²/4. Краткое доказательство: нормированный корень площади параллельного сечения f(z) вогнут, f(0)=1. При I=∫f² положим H*=3I. Вогнутость даёт H* не меньше высоты тела. Разность f(z)²−(1−z/H*)² меняет знак не более одного раза, с плюса на минус, и имеет нулевой интеграл. Следовательно её первый момент неположителен, откуда ∫zf²≤3I²/4. При A0=1/2 получается Z=24Iz≤36V²=D². Никакой ковариации центров ячеек вместо реальной массы здесь нет.

Последний вход — принятая настоящая однофасетная граница:

```text
WB/(DE)<10/9.                                             (3)
```

Это граничный след для координаты y и функции L на released K, с его собственными объёмом и центроидом. Она допустима для произвольной настоящей F5, а не только для треугольника. Здесь НЕ используется завершённая маркированная двухтреугольная теорема как оценка цельногранной пары. :contentReference[oaicite:2]{index=2}

### 4.2. Полное сокращение до двенадцати скалярных оценок

Q из(1) имеет бистепень(3,2) по(s,t). Пусть b_ij — его12тензорных коэффициентов Бернштейна на[0,1]². В каждом из них выделим A=2DE−BW. По(3), A>8DE/9.

Оставшаяся часть имеет неотрицательный коэффициент при B. После использования B≥2−k она записывается как R0_ij(2)+kΔ_ij. Полная матрица Δ равна

```text
[0,       0,                         0]
[U/3,     (U−D)/3+Z/2,               (U−2D)/3+Z]
[2U/3,    2(U−D)/3+Z−1/6,            2(U−2D)/3+2Z−1/3]
[U,       U−D+3Z/2−1/2,              U−2D+3Z−1].
```

Из D≥1, D≤U≤2D и Z≥D следует одновременно 0≤Δ_ij≤3Z.

При k≥0 используем E≥D. При k=−a<0 используем реальное E=(4D−U−W)+aZ≥D+aZ. Поэтому для D≥7/2, в ОБОИХ случаях,

```text
b_ij ≥ 8D²/9+R0_ij(2).
```

На отрицательной стороне оставшийся множитель a имеет коэффициент не меньше(8D/9−3)Z≥0. Так покрывается весь неограниченный отрицательный k-хвост, а не только конечный интервал.

Минимизация последней аффинной формы по

```text
(U,W)∈conv((D,D),(2D,D),(D,2D)),  D≤Z≤D²
```

даёт следующую буквальную нижнюю матрицу L_ij(D):

```text
[8D²/9,                   D(32D−9)/36,                 D(16D−9)/18]
[D(16D−27)/18,            D(37D−45)/72,                D(17D−24)/36]
[D(8D−21)/9,              (22D²−57D+24)/72,            (14D²−51D+21)/36]
[D(16D−45)/18,            (19D²−63D+72)/72,            (23D²−90D+27)/36].
```

Все12полиномов имеют

```text
L_ij(D)≥−25/144 при D≥7/2,
L_ij(D)≥3/100   при D≥18/5.                               (4)
```

Это проверяется раскрытием по D−7/2 и D−18/5: соответствующие коэффициенты неотрицательны. В полной капсуле заново получены сами b_ij, все Δ, все вершины указанной области минимизации и каждое полиномиальное тождество. Поскольку базис Бернштейна неотрицателен и суммируется в1, из(4) следуют Q≥−25/144 и более сильное Q≥3/100.

Область минимизации — безопасное ослабление реальных геометрических ограничений. Никакая произвольно выбранная шестёрка моментов не объявляется реализованным телом.

## 5. Общая метрика, порог2 и отдельный порог51/25

В осевой карте при настоящем g=gP положим

```text
H=gx/t+gy/s+gz−1>0,
q6=ξq4+ηq5+ζq3,
ξ=gz/H,  η=gy/(sH),  ζ=gx/(tH).
```

Коэффициенты положительны, их сумма равна1+1/H>1. Три слабые стрелки65,54,43 требуют ξ+ζ<1/4.

Полный нужный аргумент: нормируем ||q5||N=1, обозначим x=q4, r=||x||N>1, u=xᵀNq5∈[1,r), τ=ξ+ζ. Стрелка6→5 помещает q6 в шар с центром q5/2 и радиусом1/2. Линейная независимость q3,q4,q5 делает верхнюю границу xᵀNq6<(u+r)/2 строгой. Стрелка4→3 даёт xᵀNq6≥ηu+τr². Следовательно

```text
(1−2η)u+r−2τr²>0.
```

Если η≤1/2, это несовместимо с η+τ>1. Если η>1/2 и τ≥1/4, правая верхняя оценка1−2η+r−2τr² убывает при r>1 и уже отрицательна при r=1. Значит τ<1/4. Слабые равенства стрелок включены; исключена только вырожденная метрика.

Подстановка реального центроида даёт

```text
J=4dst(3gx/t−gy/s+3gz+1)<0.                               (5)
```

Используется лишь необходимое условие. J<0 не объявляется достаточным для трёхстрелочной SPD-осуществимости; второй локальный тест здесь не заменён и не требуется.

При D≥18/5 из Q≥3/100 и(5):

```text
2−T=F/(de)≥[3/100−J/4]/(de)>0.
```

Для более широкого D≥7/2 нужна отдельная оценка знаменателя. Веер P из настоящей e3 даёт e≥d(1−k). Если k>0, K содержится в тетраэдре x,y,z≥0,x+y+kz≤1, поэтому D≤1/k. Если k≤0, 1−k≥1. В обоих случаях

```text
de≥(D−1)³/D≥125/28.
```

Функция(D−1)³/D возрастает при D>1. Теперь F=Q−J/4>−25/144, и

```text
T<2+(25/144)/(125/28)=367/180=51/25−1/900.
```

Таким образом, для возможного высокого T≥51/25 с тремя требуемыми стрелками необходимо

```text
D<7/2  ИЛИ  gK,x+gK,y>3/4.                              (6)
```

При k≥0 остаётся только первая альтернатива. Для возможного T≥2 аналогичный необходимый остаток имеет D<18/5 или тот же центроидный выход.

Буквальный FULL253 имеет весь неотрицательный граф

```text
(1,0),(2,1),(3,2),(4,3),(5,4),(6,5),(7,0),(8,7).
```

Его принятая цельногранная концентрация T>51/25 противоречит(A). Содержание только дерева в более широком графе не лицензирует эту концентрацию. :contentReference[oaicite:3]{index=3}

## 6. Отдельное полное семейство с пятью непроективными параметрами

Пусть

```text
0<h<9/5,  0<r,v,s,t<1,
I=(2/5,2/5,9/5),
V0=e1, V2=e2, V6=e3,
V1=(1−h/3,1−h/3,h),
V3=(1/2,0,3/2), V7=(0,1/2,3/2),
V4=(1−r)I+rV3,
V5=(1−v)I+vV1,
V8=s e2, V9=t e1.                                       (7)
```

Берётся настоящий convex hull этих десяти точек, заново равномерно заполненный. Все циклы и17рёбер — буквально из раздела2.

Фиксированные released-плоскости:

```text
F1: x+z/3=1,
F2: −x−y+z=1,
F7: y+z/3=1,
F3:x=0, F4:z=0, F5:y=0.
```

Движущаяся F0 имеет k=2/3−1/h; F8 — целая плоскость через V4,V5,V7; F6 — целая плоскость через V6,V8,V9. Это полный открытый chamber указанных движений. h=0 или9/5, r,v,s,t=0 или1 — геометрические вырождения, не дополнительные10/17/9члены. В частности, h→0 покрывает k→−∞ без отсечения хвоста.

### Настоящие два тетраэдральных удаления

До удаления F8-капюшона released-тело K0(h) имеет вершины O,e1,e2,e3,V1,V3,V7,I. Его точные моменты:

```text
D0=26/5−h,
U0=W0=h²/3−3h+212/25,
Z0=304/25−h².
```

Положим δ=(9/5−h)/4. Удалённая верхняя область — настоящий тетраэдр(I,V4,V5,V7), и

```text
D=D0−δrv,
(U,W,Z)=(U0,W0,Z0)−δrv(I+V4+V5+V7),
B=7(h+3)/(6h),  k=2/3−1/h.                              (8)
```

δrv — шестикратный объём, не объём сам по себе. Верхний удаляемый тетраэдр лежит в x+y+z≥2, а нижний терминальный — в x+y+z≤1. Поэтому их объёмные внутренности действительно не пересекаются. Сложение моментов основано на реальных разностях тел, не на назначенных независимых массах.

### Полное доказательство T<2 и бюджета

Подставим(8) в F,J из(1). После умножения на положительное h оба полинома

```text
hF,  h(F+J/4)
```

имеют степень(3,3,3,3,2) по(h,r,v,s,t). После h=(9/5)u весь замкнутый единичный пятикуб покрывается одним тензорным базисом Бернштейна. Получены:

```text
hF:        768/768 коэффициентов строго положительны, минимум159/25;
h(F+J/4):  768/768 коэффициентов строго положительны, минимум5939/300.
```

Все степенные коэффициенты восстановлены обратно точно. Поэтому на всём физическом chamber

```text
F≥159/(25h)>0,
F+J/4≥5939/(300h)>0,
T<2 независимо от механических знаков.                    (9)
```

Настоящая решётка подтверждена не только счётом V/E/F:218полиномиальных строгих опорных/внутригранных guards, из них120 для P и98 для released K, имеют2265неотрицательных коэффициентов Бернштейна и ненулевой положительный коэффициент у каждого guard. В открытом физическом пятикубе это даёт строгие неинцидентные зазоры и строгую выпуклость всех настоящих циклов. Все грани замыкаются указанной сферической двухмерной решёткой; дополнительных граней у hull нет. У конечных контролей дополнительно перечислены все независимые тройки опор.

### Это действительно выход из прежнего класса

Виртуальные O=F3∩F4∩F5 и I=F1∩F2∩F7, вместе с e1,e2,e3, образуют проективный репер. Любая размеченная проективность между двумя членами(7) фиксирует этот репер и тождественна. Все пять параметров затем однозначно восстанавливаются по вершинам. Это пять непроективных, а не пять взаимозависимых координат одной проективной орбиты.

Более того, проективный инвариант

```text
χ=x3 I_z/(z3 I_x)
```

в осевой карте O,e1,e2,e3 равен3/2 для всего нового семейства. Для буквально восстановленного исходного spring-base и всего его принятого терминально-проективного класса он равен

```text
178724241416596140046977385443/163013511778867908597681112525
≈1.0963768553065727,
```

то есть не3/2. Новые тела не переименовывают старую конструкцию. При этом исходный released spring-K строго удовлетворяет новому общему объёмно-центроидному критерию; критерий распространяется на настоящие движения его остальных плоскостей, а не только на отдельное семейство(7).

## 7. Действительные контрконтроли границ применения

В капсуле сохранены четыре реальные формы и шесть общих метрических пар. Во всех случаях настоящий hull имеет10/17/9 и собственный равномерный центроид.

Для параметров

```text
(h,r,v,s,t)=(1,1/2,1/2,1/100,1/2)
```

получен точный T=643198267/867387674≈0.7415349402. Пусть q — его собственные полюса, а ξ,η,ζ — точное решение q6=ξq4+ηq5+ζq3. Возьмём

```text
x=(101/100,7/2,0), y=(1,0,0), a=(501/800,7/16,1/20),
z=(a−ξx−ηy)/ζ,
H=[x y z][q4 q5 q3]⁻¹,
N=HᵀH, M=N⁻¹.
```

Тогда

```text
D65=25699/640000,
D54=1/100,
D43=2787799731/84800000,
S=[1,3], U=[2,3], Hsaddle=[(0,2),(4,7)], strict222, weak000.
```

F0 здесь НЕ устойчива. Полный неотрицательный полярный граф имеет14пар:

```text
(0,1),(2,3),(4,3),(5,0),(5,1),(5,4),(6,0),
(6,1),(6,4),(6,5),(7,1),(7,8),(8,0),(8,1).
```

Это не FULL253. Контроль показывает, что выделенная трёхстрелочная система действительно осуществима на новой непроективной геометрии.

Заменим только x на(1,7/2,0) и заново определим z,H,N. Теперь D54=0, остальные две стрелки положительны. Census остаётся222weak000. Единственный нулевой edge-примитив находится на ребре09, и его полный пакет равен

```text
(211995656924/53620496721, −991484/231561, −49/4, 0).
```

Знаки(+,-,-,0) делают нуль безвредной слабой стрелкой, а не физическим слабым равновесием.

Остальные метрические контроли используют

```text
R=((1,1/5,1/7),(0,3/2,1/11),(0,0,2)), N=RᵀR, M=N⁻¹.
```

При той же форме h=1 получен strict(7,8,13). При(h,r,v,s,t)=(1/1000,1/3,2/3,3/4,1/4) — strict(6,8,12), T=128926160558509/217855779016672. Этот released K имеет D=91783/18000>18/5, но gK,x+gK,y=336033463/413023500>3/4. При(1799/1000,2/3,1/3,1/4,3/4) — strict(6,6,10), T=174514569106719/168568556760488; здесь D=61217/18000<7/2. При(3/2,1/2,1/2,1/2,1/2) — strict(7,7,12), T=329160/297253. Все эти контроли physicalweak000.

Итак, имеются две разные действительные причины выхода из общего достаточного критерия, но на всей новой семье бюджет и T<2 всё равно доказаны отдельно. **Выход из критерия не является нарушением бюджета.** Всего сохранены407ненулевых примитивов и один указанный безвредный нуль; ни одного110тела нет.

## 8. Что остаётся открытым

Общий критерий закрывает всю указанную геометрическую область при всех cap-параметрах, включая D=7/2,D=18/5, центроидную стенку U+W=3D и любые слабые механические стрелки. Новая семья(7) закрыта полностью на своём максимальном открытом chamber, включая все подходы к его геометрическим границам.

Не доказана универсальность четвертного бюджета для произвольного released K. Не построен и действительный контрпример к нему: нижняя оценка−25/144 — не пример нарушения. Конечное исследование более широкого support-chart не превращалось в исключение или в утверждение существования тела.

Для общего высокого следа с тремя стрелками существенный оставшийся released-класс локализован формулой(6): малый нормированный released-объём либо действительный центроидный выход. При k≥0 остаётся малый объём. Произвольные положительные проективные образы НОВОЙ семьи(7) не объявляются автоматически закрытыми: после нового равномерного заполнения к ним применим общий критерий, если выполняются его реальные объёмно-центроидные условия. Полный старый проективный класс остаётся закрытым прежним результатом.

Ни один полный K2-incidence domain или canonical/root register здесь не вычитается. Сохраняются K2=55 и34≤Cmin≤622; общий110-вопрос отличен от буквальной FULL253-ориентации. :contentReference[oaicite:4]{index=4}

## 9. Полная воспроизводимость

Новый журнал и буквальный parent прочитаны через EOF. Старую большую проективную коэффициентную проверку заново не запускал. Новая автономная капсула включает только нужный неизменённый `geometry.py` родителя с14пружинными входами, полный actual-hull/centroid/mechanics модуль и новый полный генератор доказательства. Старых коэффициентных файлов или неподанных вспомогательных функций ей не нужно.

Фактически выполнены новый build, затем полное source-only восстановление в другом каталоге, новый build и новый check. Все выходные pins совпали. Check пересчитывает коэффициенты, обратные преобразования, настоящие геометрические контроли и метрики; это повтор одного генератора, не заявленная независимая реализация всего верификатора или proof-assistant-формализация.

Среда: CPython3.13.5, SymPy1.14.0, mpmath1.3.0; доказательные вычисления рациональные. Команды:

```text
python recover_released_budget.py fresh
cd fresh
python release_budget.py check
```

Pins:

```text
recover_released_budget.py:15232bytes
aa2d7b40a930028c486918a89acfd82698207070526c94e8bbe6dee490eb9f16
source-map:27077bytes
84a7e55613cf4957711f102181d6e2ea0c0bd735ab45b0d43cbfa2235260ef8d
geometry.py:5457bytes
7c3b5e68963a3f0f216e0c2e18bedf21b2d1b966d5d32ee1c0a9783500f9c1e8
actual_k2.py:4811bytes
22630b452487283d52f9ac53bcd09bef9b728da47aace65b167d1f96a00b210d
release_budget.py:16286bytes
e2e3e447953f66aab2ff576f6fac3672ced376f0f2e39640b94c6144691457ca
released_result.json:1342bytes
bd9ea0cebecdeb5c8da6c271f18ca52e4d4db9e7c91b25a9e6c1db135a9f8821
released_family.json:111290bytes
37fc60d155546dcf1204ce3685126b72f66d5bc8aa11a974745bf22a8e223e67
released_controls.json:49118bytes
e1181a0bc4dbc053a89e6e4c135d1be51d05007f1ac76293c4c9346646d325c1
released_universal.json:17224bytes
6f93b99499185e7ebbe09fdec6ed14f1439097d2321044b21bcd774006e0484c
```

Главные terminal markers:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


Дополнительные копии: [полный bundle](sandbox:/mnt/data/K2_RELEASED_BULK_FIVE_SHAPE_bundle.zip), [восстановитель](sandbox:/mnt/data/recover_released_budget.py). Следующий блок самодостаточен и восстанавливает все три полных исходника без этих ссылок.

### Полный исполняемый восстановитель

```python
"""Standalone released-K2 bulk theorem and full five-shape family recovery.
CPython3.13.5, SymPy1.14.0. No other source/data files are needed.
python recover_released_budget.py NEW_DIRECTORY [--extract-only]
"""
import base64,hashlib,json,lzma,subprocess,sys
from pathlib import Path
PAYLOAD_PIN=[27077, '84a7e55613cf4957711f102181d6e2ea0c0bd735ab45b0d43cbfa2235260ef8d']
RESULT_PIN=[1342, 'bd9ea0cebecdeb5c8da6c271f18ca52e4d4db9e7c91b25a9e6c1db135a9f8821']
DATA=(
 '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'
)
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def main():
 assert __debug__ and sys.version_info[:3]==(3,13,5) and len(sys.argv) in (2,3)
 if len(sys.argv)==3:assert sys.argv[2]=='--extract-only'
 raw=lzma.decompress(base64.b64decode(DATA,validate=True));assert pin(raw)==PAYLOAD_PIN
 files=json.loads(raw);assert set(files)=={'geometry.py','actual_k2.py','release_budget.py'}
 root=Path(sys.argv[1]).resolve();root.mkdir(parents=True,exist_ok=True)
 for n,text in files.items():
  assert n==Path(n).name
  f=root/n;b=text.encode();assert not f.exists() or f.read_bytes()==b;f.write_bytes(b)
 print('RELEASED_K2_THREE_COMPLETE_SOURCE_UNITS_RECOVERED',*PAYLOAD_PIN,flush=True)
 if len(sys.argv)==2:
  subprocess.run([sys.executable,'release_budget.py','build'],cwd=root,check=True)
  assert pin((root/'released_result.json').read_bytes())==RESULT_PIN
  print('RELEASED_K2_SOURCE_ONLY_COLD_RECOVERY_PASS',*RESULT_PIN,flush=True)
if __name__=='__main__':main()
```
