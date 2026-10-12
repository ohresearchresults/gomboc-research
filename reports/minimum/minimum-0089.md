# minimum-0089

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# FREE_FIBRE_PRISM_TRACE_203_AND_SEGMENT_CORE_V1

## 1. Доказательное определение результата

**Закрыт весь класс произвольных тел, проекция которых на плоскость z=0 не выходит за треугольник OCD, при произвольном наклоне корня вдоль AB.** Для этого класса доказана более сильная оценка **T < 203/100 = 2.03**. Длина волокна L, оба его графика, остальные вершины и грани не фиксируются. Не требуется ни симметрия, ни c=d, ни ограничения c,d≤a.

Для совершенно произвольной проекции получена новая количественная редукция к настоящему усечённому телу и внутреннему телу — сумме Минковского с AB. Она исключает весь замкнутый геометрический сектор

`max_P(x+y) ≤ (204/203)^(1/4)`

и более широкую область, определённую ниже через один действительный интегральный коэффициент Ψ.

**Весь универсальный наклонный запрет пока не доказан. Действительного контрпримера T≥51/25 не получено.** Сохраняется существенный отрицательный результат: отсечение выступа x+y>1 может уменьшать T даже тогда, когда обе треугольные грани и настоящий корень сохраняются и оба следа строго больше 2. Поэтому переход к призматической проекции нельзя объявить монотонной редукцией без количественной поправки.

Новые результаты не меняют доказанную нижнюю границу **C≥34** и не изменяют FULL/LOCAL счётчики. Унаследованный первый открытый слой остаётся **(V_count,E,F_count)=(10,17,9)**.

## 2. Источники и граница зависимости

Полностью прочитан единственный приложенный файл `research-journal(20260919-045956).md`: 246177 байт, SHA-256 `379dd70cefce4ad43064c97cf43c887554ca9a051a51eb45aa94087f49727ab3`. Прочитаны весь общий notebook, вся память ветви и оба буквальных parent, включая полные исходники:

- `minimum-0082`, SHA-256 `f1793b348240dce32e3de0ca3e06e50e64942c2561980cb2dc1c75bb9b6b636c`;
- `minimum-0083`, SHA-256 `3e86de882ea208c90af36b6583bb49754e528559555e8db9ce7efe04cd37020d`.

Общая равноконцевая теорема уже доказана первым parent; она не выдаётся здесь за новую. Историческое утверждение второго parent о незакрытом равноконцевом случае именно историческое, а не конфликт буквальных тел или идентификаторов. Его fixed-L редукция и контрконтроль Steiner остаются действительными.

Новые доказательства ниже самодостаточны: не импортируют parent-код, старые finite certificates, single-facet localization или cone-tail theorem. Более сильные общие endpoint-gap результаты из notebook не переаудировались и не используются как посылки. Их отдельные полные материалы `[internal-source-reference]` и `[internal-source-reference]` в данном пакете отсутствуют. Это не пробел нового доказательства; это точная граница доступности для дальнейшего подключения той старой капсулы. Пины parent выше сохранены как идентификаторы поставленных immutable payloads, а не как самостоятельно восстановленные байты исходных JSON-envelope.

## 3. Формулировка новых теорем

Работаем в канонических координатах

```text
A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
T0=conv(A,B,C,D), O=(0,0), Δ={(x,y):x≥0,y≥0,x+y≤1}.
```

Пусть P — компактное полноразмерное однородное выпуклое тело, ABC и ABD — его настоящие максимальные треугольные грани, AB — настоящее общее ребро. В частности, P лежит в x,y≥0 и содержит T0. Для ненулевой аффинной функции

```text
ell=a+(d-a)x+(c-a)y+(b-a)z ≥0 on P
```

положим

```text
V=∫P1, X=∫P x, Y=∫P y, B_ell=∫P ell,
n(x,y)=(a+b+c)x+(a+b+d)y,
N=∫P n, t=6V, T=N/(6V B_ell),
Ω=projection_xy(P), ρ=max_P(x+y)≥1.
```

Все интегралы — от указанного тела. Нулевая плоскость ell не обязана быть гранью для аналитических теорем; когда она настоящая грань, T есть сумма двух физических Lambda. Нормировка совпадает с буквальными parent.

**Теорема P — произвольная форма внутри призмы.** Если ρ=1, то Ω=Δ и

`T < σ := 203/100`.

Это утверждение охватывает весь бесконечномерный класс допустимых L,u,v над Δ, включая все разрешённые равенства в endpoint-параметрах. Оно не является оптимизацией одного фиксированного L.

**Теорема Q — произвольная проекция.** Обозначим

```text
Pc=P∩{x+y≤1},  Vc=Vol(Pc),  Bc=∫Pc ell,
λ=1/ρ,  HN=∫Ω n(x,y) dxdy,
Ψ=[(Vc/V)(Bc/B_ell)]/[λ^4+λ^3(1-λ)HN/N].
```

Тогда

`T(P) < (203/100) Ψ ≤ (203/100) ρ^4`.

Следовательно,

```text
T≥51/25 ⇒ Ψ>204/203
             и ρ>(204/203)^(1/4).
```

Четвёртый корень приблизительно равен `1.00122925862038739765`; доказательная граница — точное алгебраическое число. Весь замкнутый сектор ρ≤этой границы исключён, включая равенство. В частности, достаточно рационального условия ρ≤1001/1000:

```text
(203/100)(1001/1000)^4 = 203813218812203/100000000000000,
51/25 − эта величина = 186781187797/100000000000000 >0.
```

## 4. Геометрическая редукция: отрицательную часть можно удалить с порогом 2

Сначала доказываем теорему P. Перестановка A,B осуществляется отражением `z↦1-x-y-z`; оно сохраняет x,y, проекцию, T и обе выбранные грани. Поэтому считаем a≥b, α=a-b≥0.

### 4.1. Центроид произвольной вогнутой плотности на Δ

Если g≥0 вогнута на Δ и имеет положительный интеграл, то её взвешенный центроид принадлежит

`Dcent=conv((1/4,1/4),(1/2,1/4),(1/4,1/2))`.

Действительно, тело под графиком g имеет в основании Δ. Веер из каждой из трёх вершин основания показывает, что среднее каждой из трёх барицентрических координат Δ не меньше 1/4: в каждой положительной тетраэдральной ячейке одна вершина имеет соответствующую координату 1, остальные — неотрицательны. Значит средние x,y≥1/4 и x+y≤3/4. Это доказывает ровно указанное треугольное ограничение. Для неполиэдрального графика те же нестрогие неравенства следуют приближением; они не требуют фиксированной триангуляции.

### 4.2. Действительное разрезание P

При Ω=Δ сечение z=0 в точности равно Δ. Положим P+=P∩{z≥0}, P−=P∩{z≤0}. Обозначим их объёмы V+,W, а интегралы ell через B+,B−. P+ имеет вид

`P+={(x,y,z):(x,y)∈Δ, 0≤z≤v(x,y)}`,

где v вогнута и v≥1-x-y. P− есть тело под неотрицательной вогнутой высотой −u. Если W>0, его средние xbar,ybar принадлежат Dcent.

На P− имеем ell≥a+(d-a)x+(c-a)y. Пусть S0=a+b+c+d, kx=a+b+c, ky=a+b+d. На всём Dcent выполняется

`kx xbar+ky ybar ≤ 2[a+(d-a)xbar+(c-a)ybar]+S0/2`.

Это аффинное неравенство проверяется на трёх вершинах Dcent: разности левой и правой частей там равны соответственно

```text
-a-3(c+d)/4,
[-(a-b)-2c-5d]/4,
[-(a-b)-5c-2d]/4,
```

и все неположительны. Следовательно

`N−≤2B−+(S0/2)W`.

Из T0⊂P+ следуют V+≥1/6 и B+≥S0/24. Поэтому для

`Dcross=6(V+ B−+W B++W B−)`

получаем N−≤2Dcross, причём неравенство строго при W>0: остаётся положительный член 12WB−. Разложение полного знаменателя даёт

`T(P) ≤ max(2,T(P+))`.

Здесь нет симметризации, сохранения старого COM после изменения тела или предположения о том, что ell=0 остаётся гранью P+. Последнее вообще не нужно: теорема доказывается для любой неотрицательной аффинной ell. Достаточно закрыть произвольную крышу P+ над Δ.

## 5. Новая одномерная выпуклая моментная лемма

Пусть f≥0 выпукла на [0,1], f(0)=b, и 0≤q≤3/4. Тогда

`∫_0^1 s(s-q)f(s)ds ≥ -8bq^3/81`.                         (R1)

Доказательство полностью элементарно. Вычтем минимум f. Часть слева от минимума — неотрицательная убывающая выпуклая функция, часть справа — неотрицательная возрастающая выпуклая функция. Первая представляется положительной смесью петель `(1-s/h)+`, 0<h≤1, с суммарным значением в нуле b-min f; вторая — положительной смесью `(s-h)+`, 0≤h≤1. Для кусочно-аффинной функции это конечное разложение по скачкам производной; общий случай следует выпуклым приближением.

Для убывающей петли

```text
∫ s(s-q)(1-s/h)+ ds = h^3/12-qh^2/6,
h^3/12-qh^2/6+8q^3/81
  = (h-4q/3)^2(h+2q/3)/12 ≥0.
```

Для постоянной функции, при r=4q/3∈[0,1], нужная разность равна

`1/3-q/2+8q^3/81=(1-r)(8-r-r^2)/24≥0`.

Для возрастающей петли точное тождество имеет вид

```text
∫_h^1 s(s-q)(s-h)ds
 =h(1-h)^2(2h+1)/24
  +(3/4-q)(1-h)^2(h+2)/6 ≥0.
```

Суммирование доказывает R1, включая q=0, q=3/4, нулевые концы и минимум на конце.

**Двумерное следствие.** Пусть R≥0 выпукла на Δ, R(0,0)=b, 0<k≤K, m=6∫ΔR. Для любого 0≤r≤1

`24∫Δ(Kx+ky)R ≥ 3rkm − br^3 k^2/K`.                    (R2)

Параметризуем лучи как x=su,y=s(1-u), 0≤s,u≤1; якобиан s. Для `k(u)=Ku+k(1-u)` применим R1 с `q(u)=3rk/[4k(u)]` и умножим её на k(u). После интегрирования по u используется точное равенство

`∫_0^1 k(u)^(-2)du=1/(kK)`,

верное также при K=k. Получается R2. Именно это сравнение работает для произвольной выпуклой функции R, а не для выбранной конечной формы L.

## 6. Произвольная крыша: весь непрерывный диапазон

Рассмотрим P+ и сначала a>b. Делим ell на a, так что a=1, 0≤b<1, α=1-b. Перестановкой x,y обеспечиваем c≥d≥0. В этом разделе t=6Vol(P+), а все N,B_ell также относятся к P+.

Введём

```text
A0=1+b, S=c+d, K=A0+c, k=A0+d,
E=1+(d-1)x+(c-1)y,
R=E-αv ≥0,
m=1+S-αt=6∫Δ R ≥0,
D0=bt+1+S.
```

R — одна настоящая неотрицательная выпуклая функция; её значения в O,C,D равны b,c,d.

### 6.1. Две совместимые необходимые оценки

**Настоящий веер из B.** Основание ACD является настоящей треугольной гранью P+. Его ячейка с апексом B есть T0. Во всех остальных ячейках ell имеет среднее не меньше b/4. Поэтому

`B_ell ≥ bV/4+(1+c+d)/24 = D0/24`.                      (F1)

**Вогнутая добавка крыши.** Функция g=v-(1-x-y) неотрицательна и вогнута. Лемма 4.1 и ∫g=(t-1)/6 дают

`24N ≤ (2t-1)K+t k`.                                   (F2)

Следовательно T<σ достаточно доказать посредством

`Gσ=σtD0-(2t-1)K-tk>0`.                                (G)

Альтернативная оценка использует ту же R. Прямое интегрирование даёт

```text
EN := 24∫Δ(Kx+ky)E
    =2A0+(3A0+1)S+S^2+2cd.
```

Из `αN=∫Δ(Kx+ky)(E-R)`, R2 и F1 следует достаточное условие

`Fσ,r = K[σαtD0-EN+3rkm]-br^3k^2 >0`.                  (F)

Оба достаточных теста получены от одного действительного P+. Они не утверждают реализуемости независимых наборов скалярных моментов.

### 6.2. Неограниченные параметры исключаются без вычислительного разбиения

При σ=2 имеется точное тождество

`G2=m+b(2t^2-4t+1)+(t-1)d`.

Поэтому при t≥2 имеем T≤2. Для высокого следа остаётся только 1≤t≤2; прежний общий cone-tail здесь не нужен.

При σ=203/100

```text
Gσ=b(σt^2-3t+1)
   +c[1+(σ-2)t]+d(σ-1)t+1+(σ-3)t.
```

На 1≤t≤2 коэффициент при b положителен. Если c≥1, то

`Gσ≥2-(94/100)t≥3/25>0`.

Таким образом весь оставшийся непрерывный диапазон содержится в замкнутом кубе

`b,c,v,u∈[0,1], d=cv, t=1+u`.                           (CUBE)

Случай c=0,d=0 включён при любом v. Ограничение m≥0 в конечной части даже не требуется.

### 6.3. Полный точный сертификат куба

На всём CUBE доказывается дизъюнкция: Gσ>0 либо Fσ,r>0 для одного из r=j/32. Подстановка d=cv,t=1+u даёт многочлены, укладывающиеся в общую тензорную степень `(3,3,2,2)`. Используются 144 коэффициента Бернштейна на ячейку, точные целые midpoint subdivisions и полный двоичный cover, без floating point.

Восстановлены и проверены:

```text
785 узлов дерева;
393 замкнутые листовые ячейки;
72 ячейки G и 321 ячейка F;
56592 строго положительных коэффициента;
максимальная глубина 20;
нулевое число отброшенных «нефизических» ячеек;
общий исходный знаменатель 3600.
```

Распределение F-ячеек по j:

```text
j:      20 21 22 24 25 26 27 28 29 30 31 32
count:   7  4  3 29 24 91 57 69 19  6  9  3
```

Минимальная сохранённая нижняя Bernstein-оценка соответствующего G или F равна `1050903/3355443200>0`. Базисные функции Бернштейна неотрицательны и суммируются в 1. Исходное разложение независимо развёрнуто обратно в степенной базис; все 393 листа дополнительно проверены непосредственной аффинной подстановкой исходных степенных многочленов, независимо от функции разбиения. Полнота проверена отдельно по префиксному дереву и сумме 2^(-depth)=1. Это покрывает границы и все разрешённые равенства, не только внутренность куба.

Полный автономный генератор ниже детерминированно восстанавливает все 393 пути и метки. Их компактный JSON с LF имеет 9533 байта, SHA-256 `bcec297e032396037e95f741f41a8979d1774f199bc9de1f85898c33c7cb9383`. Отдельная непредоставленная таблица не требуется.

### 6.4. Оставшиеся нулевые и равноконцевые ветви

Для a=b>0 нормируем a=b=1. Тот же настоящий веер и F2 дают

`G2=2(t-1)^2+c+td≥0`,

поэтому крыша имеет T≤2 при любых c,d≥0. Это вспомогательный разбор для новой призматической теоремы, а не повторное заявление уже известной общей равноконцевой теоремы.

Если a=b=0, то ell=dx+cy, c+d>0. Лемма 4.1, применённая к g, даёт для крыши `1/4≤gx,gy≤1/2-1/(4t)≤t/4`. Отсюда `cgx+dgy≤t(dgx+cgy)` и T≤1.

Вместе с разрезанием из §4 получаем T(P)<203/100 при любой ell. Для общего компактного выпуклого тела нестрогие веерные и моментные оценки переходят от полиэдральных приближений; затем положительный полиномиальный тест применяется к его точным предельным параметрам. Строгость поэтому не выводится только из предела строгих неравенств. Теорема P доказана.

## 7. Настоящий внутренний сегментный корпус и доказательство теоремы Q

Тело Pc сохраняет ABC,ABD и AB в точности и имеет проекцию Δ. Поэтому к нему применима теорема P, даже если после разреза ell=0 уже не является гранью.

Положим

`Qλ=λP+(1-λ)AB`, λ=1/ρ.

Из выпуклости и AB⊂P следуют Qλ⊂P и Qλ⊂Pc. Если исходное волокно над (x,y) равно [u,v], то волокно Qλ над λ(x,y) равно `[λu,λv+1-λ]`. Следовательно

```text
Vol(Qλ)=λ^3V+λ^2(1-λ)Area(Ω),
N(Qλ)=λ^4N+λ^3(1-λ)HN.
```

Это точные собственные моменты одного явного внутреннего тела. Qλ не объявляется телом с теми же треугольными гранями; теорема P применяется к Pc, а не к Qλ.

Поскольку n≥0, N(Pc)≥N(Qλ). Точное тождество

`T(P)=T(Pc)[N/N(Pc)](Vc/V)(Bc/B_ell)`

даёт `T(P)<(203/100)Ψ`. Наконец Vc≤V, Bc≤B_ell и знаменатель Ψ≥λ^4, откуда Ψ≤ρ^4. Все массы, интегралы ell и проекционные интегралы берутся от P, его настоящего пересечения и его явно построенного внутреннего тела. Теорема Q доказана.

## 8. Точные действительные тела, включая отрицательный результат выше 2

### 8.1. Полная компактная конструкция

Для любого из указанных далее наборов c,d используем

```text
a=1, b=1/4,
ell=1-(1-d)x-(1-c)y-(3/4)z,
Root(x,y)=(x,y,(4/3)[1-(1-d)x-(1-c)y]),
e=1/10000, r=5/6.
```

К T0 добавляются четыре точки Root(x,y) с парами

```text
(r-e,e), (e,r-e), (e,1-2e), (1-2e,e).
```

Это тело обозначается P(c,d;none). Для P(c,d;ρ) дополнительно добавляется `Root(ρ/2,ρ/2)`. Это полные точные входные координаты; никаких найденных floating-point координат для восстановления не нужно.

Капсула проверяет 16 тел: четыре при `(c,d)=(1/10000,1/20000)` и ρ=`none,101/100,3/2,2`; ещё по три при каждой паре

```text
(c,d)=(3/1000,1/500), (1/200,1/400),
      (1/100,1/200), (1/500,1/500),
ρ=none,101/100,51/50.
```

Для каждого заново реконструированы максимальные фасеты, настоящие рёбра, собственные объём и первый момент двумя веерами, площадные центроиды всех фасетов, полный физический Lambda и его точные матричные тождества. Все исходные тела имеют настоящие ABC,ABD,AB и настоящий нулевой фасет ell. Для их пересечений и Qλ заново считаются собственные моменты, без переноса COM от P. Никакое тело не объявляется 110; у всех 16 исходных тел нулевых edge primitives нет.

### 8.2. Высокий, но не объявляемый рекордом контроль

Для `P(1/10000,1/20000;none)`:

```text
f=(8,17,11), strict(S,U,H)=(4,4,6),
V=7438774662527/40500000000000,
T=81214133818257964563408984375
  /40033190249549828568680931046
 ≈2.0286700438312235.
```

T строго больше 253/125 и меньше 203/100. Корень — настоящий четырёхугольник; a≠b, c≠d>0, корень не содержит A,B,C,D.

Более низкоарифметический положительный-gap спутник `P(1/200,1/400;none)` имеет те же f и strict(S,U,H), и

```text
T=1320033850569185372296875/651219507908961827893342
 ≈2.027018285750926,
253(c+d)=759/400>1.
```

Наличие E=17 у этих тел не помещает их в открытый слой (10,17,9): у них восемь вершин, одиннадцать граней и четыре строгих U. Они не являются C34-аттейнерами механической задачи.

### 8.3. Усечение до призмы НЕ монотонно даже выше 2

Возьмём `P*=P(1/100,1/200;101/100)` и `Pc*=P*∩{x+y≤1}`. Тогда

```text
f(P*)=(9,19,12), strict(S,U,H)=(5,5,8),
T(P*)=2155518603728164661400000/1065579991917354553894843
     ≈2.022859494433286,
T(Pc*)=317136889441260199286440200000
       /156805732128382273017653918249
      ≈2.022482757081924,
2<T(Pc*)<T(P*)<51/25.
```

ABC, ABD, AB и корневая плоскость сохраняются как настоящие грани/ребро также у Pc*. Здесь `253(c+d)=759/200>1`; это не контроль с исчезающим c+d. Тем самым опровергнута универсальная редукция

`T(P)≤max(2,T(P∩{x+y≤1}))`.

Это **другой оператор**, не продление C,D из старого parent. Не следует объявлять этот пример отрицанием недоказанной там иной редукции.

Для этого же тела

```text
Ψ=132757974806209899335808403880999259155597011490689
  /132011137376244357238601567893416100794508900000000
 ≈1.0056573819816201 >204/203.
```

Следовательно оно находится вне нового достаточного Ψ-теста, оставаясь настоящим телом с T<51/25. Отказ достаточного теста не является контрпримером к универсальному запрету. Всего точно сохранены девять случаев `2<T(Pc)<T(P)`; восемь из них имеют `253(c+d)>1`.

Большие невыигрышные тела `P(1/10000,1/20000;3/2)` и `P(1/10000,1/20000;2)` также не отброшены. Их следы соответственно

```text
4205391046965498077770140000000/2504277028012898070119717005243,
6939555600406104319945140000000/4631974902407559318308619610243,
```

а strict(S,U,H) равны (5,5,8) и (3,4,5). Они сохраняют выход проекции далеко за новую закрытую область и точную проверку сегментного корпуса.

## 9. Что пробовалось и что не является доказательством

Исходный поиск варьировал плоскость настоящего потенциального корня, три либо четыре точки на ней и дополнительные точки с положительным slack. Два ограниченных запуска дали приблизительно 2.028783019352459 и 2.0287829967467195, но не T≥51/25. Это численный поиск на конечных параметрических семействах, не исключение свободных тел; найденные floating-point массивы не повышаются до точных физических свидетелей.

Полезным поворотом стало не увеличение числа точек поиска, а отделение отрицательной части тела и использование выпуклости R=E-αv. В результате L перестала быть фиксированным входом. Точные тела §8 выбраны рационально и проверены отдельно от оптимизатора. Аналитические и Bernstein-доказательства не импортируют поисковый код.

Полный поисковый source также сохранён ниже: CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, OPENBLAS_NUM_THREADS=1. Команды `python search_free.py wide 851` и `python search_free.py many 853`; все bounds, population, tolerances и maxiter находятся в source. Байты численных отчётов относятся к этим фактическим запускам, а не к обещанию побитовой переносимости плавающей арифметики на любую платформу.

## 10. Исполнение и recovery capsule

Доказательный запуск: CPython 3.13.5, только стандартная библиотека, assertions включены. Окончательный source был перенесён один в новый пустой каталог; build и check выполнены заново, JSON побайтно совпал с исходным запуском. Старые parent-капсулы не переисполнялись и не выдаются за новые исполнения.

Сохранить следующий полный код как `free_fibre_prism_exact.py`, UTF-8/LF, с одним завершающим LF. В пустом каталоге:

```bash
python -S free_fibre_prism_exact.py build
python -S free_fibre_prism_exact.py check
sha256sum free_fibre_prism_exact.py free_fibre_prism_exact.json
```

Пины:

```text
free_fibre_prism_exact.py
18642 bytes
0e5727d6a4d02105ce1a225f0a8ac8fb990650e9477dc81bcd3dc0f7f3c38d71

free_fibre_prism_exact.json
604422 bytes
7c7957213edd8f6923d58b95fc1b70b189192cb53625f5a81850575a293543b0

search_free.py
1295 bytes
10d924fe2b362ab21dd1a7cbcfd4b8d942daeb22ef122615f251aeeaba14fb59

wide851.json
458 bytes
e8294d3798fe9d4bb213365877941ed23848a79e144d3123eab1737c34d3022a

many853.json
814 bytes
b4ea31912599b82a42439a41fbfbc7ee0f522ec5006d07b9d0734b2ee73adf99
```

Ожидаемые маркеры каждого доказательного запуска:

```text
CONVEX_RADIAL_MOMENT_IDENTITIES_PASS 3
FREE_ROOF_203_CONTINUOUS_CUBE_PASS 393 72 321 56592 20
INDEPENDENT_POWER_BASIS_ALL_393_CLOSED_CELLS_PASS
TRUE_BODY_FACETS_TWO_FANS_LAMBDA_AND_SEGMENT_CORE_PASS 16
TRUE_ROOT_PRISM_CUT_TRACE_DROP_ABOVE_TWO_PASS 9
OVERHANG_SUFFICIENT_TEST_FAILURE_IS_NOT_A_COUNTEREXAMPLE_PASS
FREE_FIBRE_PRISM_EXACT_PASS 604422 7c7957213edd8f6923d58b95fc1b70b189192cb53625f5a81850575a293543b0
```

Это точная арифметическая и физическая проверка, не формализация в proof assistant и не внешняя рецензия.

### Полный доказательный source

```python
"""FREE_FIBRE_PRISM_TRACE_203_AND_SEGMENT_CORE_V1.
CPython 3.13.5, standard library only, assertions enabled.
Mathematical parents (not imported):
minimum-0082
f1793b348240dce32e3de0ca3e06e50e64942c2561980cb2dc1c75bb9b6b636c
minimum-0083
3e86de882ea208c90af36b6583bb49754e528559555e8db9ce7efe04cd37020d
Run: python -S free_fibre_prism_exact.py build; then check.
All bounds and subdivisions are exact. No numerical solver or external data.
"""
from fractions import Fraction as F
from math import comb,lcm,gcd
from itertools import product,combinations
import json,hashlib,sys
from pathlib import Path
assert __debug__
DIMS=(3,3,2,2)
KS=list(product(*(range(n+1) for n in DIMS)))
INDEX={e:i for i,e in enumerate(KS)}
def C(x):return {(0,0,0,0):F(x)} if x else {}
def var(i):
    e=[0]*4;e[i]=1;return {tuple(e):F(1)}
def add(*ps):
    o={}
    for p in ps:
        for e,v in p.items():o[e]=o.get(e,F(0))+v
    return {e:v for e,v in o.items() if v}
def sc(p,a):return {e:v*a for e,v in p.items() if v*a}
def mul(p,q):
    o={}
    for e,a in p.items():
        for f,b in q.items():
            k=tuple(x+y for x,y in zip(e,f));o[k]=o.get(k,F(0))+a*b
    return {e:v for e,v in o.items() if v}
def pw(p,n):
    o=C(1)
    for _ in range(n):o=mul(o,p)
    return o

def polys():
    b,c,v,t=map(var,range(4));one=C(1);d=mul(c,v);S=add(c,d);al=add(one,sc(b,-1));A=add(one,b)
    k=add(A,d);kk=add(A,c);mass=add(one,S,sc(mul(al,t),-1))
    base=mul(t,add(mul(b,t),one,S))
    NE=add(sc(A,2),mul(add(sc(A,3),one),S),pw(S,2),sc(mul(c,d),2))
    G=add(sc(base,F(203,100)),sc(mul(add(sc(t,2),C(-1)),kk),-1),sc(mul(t,k),-1))
    P0=mul(kk,add(sc(mul(al,base),F(203,100)),sc(NE,-1)))
    P1=sc(mul(mul(kk,k),mass),3)
    P3=sc(mul(b,pw(k,2)),-1)
    return [G,P0,P1,P3,mass]

def bern(p):
    # Substitute t=1+u; the other three variables already range over [0,1].
    q={}
    for (i,j,k,l),a in p.items():
        for z in range(l+1):
            e=(i,j,k,z);q[e]=q.get(e,F(0))+a*comb(l,z)
    assert all(all(e[i]<=DIMS[i] for i in range(4)) for e in q)
    B=[sum(a*prodfrac(e,k) for k,a in q.items() if all(k[i]<=e[i] for i in range(4))) for e in KS]
    # Independent inverse tensor Bernstein expansion, including degree elevation.
    back=B[:]
    for ax,n in enumerate(DIMS):
        nxt=[F(0)]*len(KS)
        for e in KS:
            k=e[ax];value=F(0)
            for j in range(k+1):
                z=list(e);z[ax]=j
                value+=(-1)**(k-j)*comb(k,j)*back[INDEX[tuple(z)]]
            nxt[INDEX[e]]=comb(n,k)*value
        back=nxt
    assert all(back[INDEX[e]]==q.get(e,F(0)) for e in KS)
    return B
def prodfrac(e,k):
    o=F(1)
    for i in range(4):o*=F(comb(e[i],k[i]),comb(DIMS[i],k[i]))
    return o

def initial():
    vals=[bern(p) for p in polys()];den=lcm(*(v.denominator for p in vals for v in p))
    return [[int(v*den) for v in p] for p in vals],den

LINES=[]
for ax,n in enumerate(DIMS):
    o=[]
    for others in product(*(range(DIMS[i]+1) for i in range(4) if i!=ax)):
        e=list(others);e.insert(ax,0)
        row=[]
        for j in range(n+1):e[ax]=j;row.append(INDEX[tuple(e)])
        o.append(row)
    LINES.append(o)

def split(arr,ax):
    n=DIMS[ax];left=[0]*len(arr);right=left.copy()
    for row in LINES[ax]:
        z=[arr[i] for i in row]
        for j,idx in enumerate(row):
            left[idx]=2**(n-j)*sum(comb(j,k)*z[k] for k in range(j+1))
            right[idx]=2**j*sum(comb(n-j,k-j)*z[k] for k in range(j,n+1))
    return left,right

def choose(data):
    G,P0,P1,P3,mass=data
    if max(mass)<0:return 'X'
    if min(G)>0:return 'G'
    # r=j/32. Positive scale 32^3.
    for j in (26,24,28,20,32,25,27,23,29,21,30,22,31,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0):
        if all(32768*x+1024*j*y+j**3*z>0 for x,y,z in zip(P0,P1,P3)):
            return str(j)
    return None

def direct_leaf(p,box):
    # Independent affine substitution in the original power basis; no split() call.
    q={}
    for e,a in p.items():
        for k in product(*(range(j+1) for j in e)):
            z=a
            for i in range(4):
                lo,hi=box[i];z*=comb(e[i],k[i])*lo**(e[i]-k[i])*(hi-lo)**k[i]
            q[k]=q.get(k,F(0))+z
    return [sum(a*prodfrac(e,k) for k,a in q.items()
                if all(k[i]<=e[i] for i in range(4))) for e in KS]

def proof_data():
    data,den=initial();assert den==3600
    stack=[('',data)];leaves=[];nodes=0;hist={};maxdepth=0
    while stack:
        path,data=stack.pop();nodes+=1;maxdepth=max(maxdepth,len(path))
        label=choose(data)
        if label is not None:
            assert label!='X'  # No infeasible-cell pruning is used by this certificate.
            leaves.append((path,label));hist[label]=hist.get(label,0)+1
            continue
        assert len(path)<44,('unresolved',path)
        lr=[split(a,len(path)%4) for a in data]
        stack.append((path+'1',[a[1] for a in lr]))
        stack.append((path+'0',[a[0] for a in lr]))
    raw=(json.dumps(leaves,separators=(',',':'))+'\n').encode()
    assert len(raw)==9533
    assert hashlib.sha256(raw).hexdigest()=='bcec297e032396037e95f741f41a8979d1774f199bc9de1f85898c33c7cb9383'
    assert (nodes,len(leaves),maxdepth)==(785,393,20)
    assert hist['G']==72 and sum(hist.values())==393
    # Separately check exact prefix coverage and reconstruct each accepted polynomial.
    table=dict(leaves);assert len(table)==len(leaves)
    def cover(path):
        if path in table:return
        assert any(q.startswith(path) for q in table)
        cover(path+'0');cover(path+'1')
    cover('')
    assert sum(F(1,2**len(path)) for path,label in leaves)==1
    minimum=None
    for path,label in leaves:
        data,den=initial_data,initial_den
        for depth,bit in enumerate(path):
            ax=depth%4;data=[split(a,ax)[int(bit)] for a in data]
            den*=2**DIMS[ax]
        if label=='G':coeff=data[0];scale=1
        else:
            j=int(label);coeff=[32768*x+1024*j*y+j**3*z for x,y,z in zip(data[1],data[2],data[3])];scale=32768
        assert min(coeff)>0
        box=[(F(0),F(1))]*3+[(F(1),F(2))]
        for depth,bit in enumerate(path):
            ax=depth%4;lo,hi=box[ax];mid=(lo+hi)/2
            box[ax]=(lo,mid) if bit=='0' else (mid,hi)
        pp=polys()
        p=pp[0] if label=='G' else add(pp[1],sc(pp[2],F(int(label),32)),sc(pp[3],F(int(label),32)**3))
        assert direct_leaf(p,box)==[F(x,den*scale) for x in coeff]
        low=F(min(coeff),den*scale)
        minimum=low if minimum is None else min(minimum,low)
    return dict(identity='PRISM_FREE_FIBRE_203_CERTIFICATE_V1',degree=DIMS,
        cube='b,c,v,u in [0,1]; d=c*v; t=1+u; r=j/32',initial_denominator=3600,
        leaves=leaves,nodes=nodes,maxdepth=maxdepth,histogram=hist,
        positive_bernstein_coefficients=144*len(leaves),minimum_bound=minimum,
        leaf_bytes=len(raw),leaf_sha256=hashlib.sha256(raw).hexdigest())

initial_data,initial_den=initial()

def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def primitive(n,d):
    zz=tuple(map(F,(*n,d)));l=lcm(*(x.denominator for x in zz));ns=[int(l*x) for x in zz];g=gcd(*ns)
    return tuple(F(x//g) for x in ns)
def hull2(P):
    pts=sorted(set(P));lo=[];hi=[]
    def orient(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    for arr,seq in ((lo,pts),(hi,pts[::-1])):
        for p in seq:
            while len(arr)>1 and orient(arr[-2],arr[-1],p)<=0:arr.pop()
            arr.append(p)
    return lo[:-1]+hi[:-1]
def poly2_mom(P):
    V=X=Y=F(0)
    for i in range(1,len(P)-1):
        a,b,c=P[0],P[i],P[i+1];w=((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))/2
        assert w>0;V+=w;X+=w*(a[0]+b[0]+c[0])/3;Y+=w*(a[1]+b[1]+c[1])/3
    return V,X,Y

def hull3(points):
    P=list(dict.fromkeys(tuple(map(F,p)) for p in points));planes={}
    for i,j,k in combinations(range(len(P)),3):
        n=cross(sub(P[j],P[i]),sub(P[k],P[i]));d=dot(n,P[i])
        if not any(n):continue
        ss=[dot(n,p)-d for p in P]
        if min(ss)<0<max(ss) or min(ss)==max(ss)==0:continue
        if min(ss)>=0:n=tuple(-x for x in n);d=-d
        H=primitive(n,d);ids=tuple(i for i,p in enumerate(P) if dot(H[:3],p)==H[3]);planes[H]=ids
    fs=[]
    for H,ids in planes.items():
        n=H[:3];drop=next(i for i,x in enumerate(n) if x);axes=[i for i in range(3) if i!=drop]
        mp={tuple(P[i][j] for j in axes):i for i in ids};q=hull2(list(mp));f=[mp[p] for p in q]
        if dot(cross(sub(P[f[1]],P[f[0]]),sub(P[f[2]],P[f[0]])),n)<0:f.reverse()
        start=f.index(min(f));f=f[start:]+f[:start];fs.append((tuple(f),H))
    fs=sorted(fs);FCS=[f for f,h in fs];H=[h for f,h in fs]
    verts=sorted(set(i for f in FCS for i in f));edges=sorted(set(tuple(sorted(e)) for f in FCS for e in zip(f,f[1:]+f[:1])))
    assert len(verts)-len(edges)+len(FCS)==2
    for i in verts:
        nn=[h[:3] for f,h in fs if i in f]
        assert any(det(*triple) for triple in combinations(nn,3))
    V=F(0);M=[F(0)]*3;cen=[];area=[]
    for f,h in fs:
        kk=next(k for k in range(3) if h[k]);aa=F(0);cc=[F(0)]*3
        for i in range(1,len(f)-1):
            tri=[P[j] for j in (f[0],f[i],f[i+1])];a,b,c=tri;vv=det(a,b,c)/6;assert vv>=0
            V+=vv
            for k in range(3):M[k]+=vv*(a[k]+b[k]+c[k])/4
            at=abs(cross(sub(b,a),sub(c,a))[kk]);aa+=at
            for k in range(3):cc[k]+=at*sum(p[k] for p in tri)/3
        cen.append(tuple(x/aa for x in cc));area.append(aa/(2*abs(h[kk])))
    ref=tuple(sum(P[i][j] for i in verts)/len(verts) for j in range(3));V2=F(0);M2=[F(0)]*3
    for f,h in fs:
        for i in range(1,len(f)-1):
            tri=[P[j] for j in (f[0],f[i],f[i+1])];vv=det(*(sub(p,ref) for p in tri))/6;assert vv>0;V2+=vv
            for k in range(3):M2[k]+=vv*(ref[k]+sum(p[k] for p in tri))/4
    assert V2==V and M2==M and V>0
    g=tuple(x/V for x in M);sl=[h[3]-dot(h[:3],g) for h in H];assert min(sl)>0
    poles=[tuple(h[k]/s for k in range(3)) for h,s in zip(H,sl)];d=[ar*s/V for ar,s in zip(area,sl)]
    Lam=[[d[j]*(H[i][3]-dot(H[i][:3],cen[j]))/sl[i] for j in range(len(H))] for i in range(len(H))]
    assert sum(d)==3
    for i,row in enumerate(Lam):
        assert row[i]==0 and sum(row)==3
        for j in range(len(H)):assert sum(Lam[i][k]*Lam[k][j] for k in range(len(H)))+row[j]==4*d[j]
        for k in range(3):assert sum(row[j]*poles[j][k] for j in range(len(H)))==-poles[i][k]
    U=[i for i in verts if all(dot(sub(P[i],g),sub(P[j],P[i]))<0 for j in verts if j!=i)]
    S=[i for i,p in enumerate(poles) if all(dot(p,sub(q,p))<0 for j,q in enumerate(poles) if j!=i)]
    sadd=[];zeros=0
    for e in edges:
        i,j=e;ij=[k for k,f in enumerate(FCS) if i in f and j in f];assert len(ij)==2;k,l=ij
        ds=[dot(sub(P[i],g),sub(P[j],P[i])),dot(sub(P[j],g),sub(P[i],P[j])),dot(poles[k],sub(poles[l],poles[k])),dot(poles[l],sub(poles[k],poles[l]))]
        zeros+=sum(v==0 for v in ds)
        if max(ds)<0:sadd.append(e)
    return dict(points=P,vertices=verts,faces=FCS,planes=H,edges=edges,f_vector=(len(verts),len(edges),len(FCS)),volume=V,moment=M,centroid=g,facet_centroids=cen,cone_d=d,Lambda=Lam,strict_SUH=(len(S),len(U),len(sadd)),stable=S,unstable=U,saddle_edges=sadd,zero_edge_primitives=zeros)

nodes=(F(1),F(1,4),F(1,10000),F(1,20000))
def ell(p,nd=nodes):
    a,b,c,d=nd;return a+(d-a)*p[0]+(c-a)*p[1]+(b-a)*p[2]
def rootpoint(x,y,nd=nodes):
    a,b,c,d=nd;return (x,y,(a+(d-a)*x+(c-a)*y)/(a-b))
def body(rho=None,nd=nodes):
    e=F(1,10000);r=F(5,6)
    P=[(0,0,0),(0,0,1),(0,1,0),(1,0,0)]
    P += [rootpoint(x,y,nd) for x,y in ((r-e,e),(e,r-e),(e,1-2*e),(1-2*e,e))]
    if rho is not None:P.append(rootpoint(rho/2,rho/2,nd))
    return P

def trace(P,root_required=True,nd=nodes):
    z=hull3(P);a,b,c,d=nd;P=z['points'];sets=[frozenset(f) for f in z['faces']]
    assert frozenset((0,1,2)) in sets and frozenset((0,1,3)) in sets and (0,1) in z['edges']
    assert min(ell(p,nd) for p in P)>=0
    root=frozenset(i for i in z['vertices'] if ell(P[i],nd)==0)
    if root_required:assert root in sets
    V=z['volume'];X,Y,Z=z['moment'];B=sum([a*V,(d-a)*X,(c-a)*Y,(b-a)*Z]);N=(a+b+c)*X+(a+b+d)*Y;T=N/(6*V*B)
    if root in sets:
        ri=sets.index(root);ii=sets.index(frozenset((0,1,2)));jj=sets.index(frozenset((0,1,3)))
        assert T==z['Lambda'][ri][ii]+z['Lambda'][ri][jj]
    z.update(nodes=nd,root=sorted(root),root_is_maximal_facet=root in sets,B_ell=B,N=N,T=T,rho=max(p[0]+p[1] for p in P))
    return z

def cut(P,audit):
    out=P.copy()
    out=[p for p in out if p[0]+p[1]<=1]
    for i,j in audit['edges']:
        p,q=audit['points'][i],audit['points'][j];s=p[0]+p[1]-1;t=q[0]+q[1]-1
        if s*t<0:
            h=s/(s-t);out.append(tuple(p[k]+h*(q[k]-p[k]) for k in range(3)))
    return out
def actual_controls():
    out=[]
    cases=[(nodes,rho) for rho in (None,F(101,100),F(3,2),F(2))]
    for c,d in ((F(3,1000),F(1,500)),(F(1,200),F(1,400)),
                (F(1,100),F(1,200)),(F(1,500),F(1,500))):
        cases.extend(((F(1),F(1,4),c,d),rho) for rho in (None,F(101,100),F(51,50)))
    for nd,rho in cases:
        P=body(rho,nd);r=trace(P,nd=nd);pc=cut(P,r);rc=trace(pc,False,nd)
        proj=hull2([(p[0],p[1]) for p in r['points']]);ar,mx,my=poly2_mom(proj)
        a,b,c,d=nd;hn=(a+b+c)*mx+(a+b+d)*my;lam=1/r['rho']
        denom=lam**4+lam**3*(1-lam)*hn/r['N']
        psi=(rc['volume']/r['volume'])*(rc['B_ell']/r['B_ell'])/denom
        # Rebuild the same-body inner Minkowski core, with no claim about its facet types.
        Q=[tuple(lam*p[k]+(1-lam)*j*(k==2) for k in range(3))
           for p in r['points'] for j in (0,1)]
        rq=hull3(Q)
        assert all(dot(h[:3],p)<=h[3] for h in r['planes'] for p in Q)
        assert max(p[0]+p[1] for p in Q)<=1
        qn=(a+b+c)*rq['moment'][0]+(a+b+d)*rq['moment'][1]
        assert rq['volume']==lam**3*r['volume']+lam**2*(1-lam)*ar
        assert qn==lam**4*r['N']+lam**3*(1-lam)*hn
        assert rc['N']>=qn and rc['volume']<=r['volume'] and rc['B_ell']<=r['B_ell']
        assert rc['T']<F(203,100) and r['T']<F(203,100)*psi<=F(203,100)*r['rho']**4
        assert r['T']<F(51,25)
        assert r['zero_edge_primitives']==0
        out.append(dict(body=r,cut=rc,projection=proj,projection_moments=(ar,mx,my),
                        core=rq,core_N=qn,H_N=hn,Psi=psi,claim_110=False))
    assert out[0]['body']['f_vector']==(8,17,11)
    assert out[0]['body']['strict_SUH']==(4,4,6)
    assert out[0]['body']['T']==F(81214133818257964563408984375,40033190249549828568680931046)>F(253,125)
    assert out[1]['body']['f_vector']==(9,19,12)
    assert out[1]['body']['strict_SUH']==(5,5,8)
    assert out[1]['body']['T']==F(2115385842511271275163640000000,1047917007864357861652165294843)
    assert out[1]['Psi']>F(204,203)
    assert out[1]['cut']['root_is_maximal_facet']
    assert F(2)<out[1]['cut']['T']<out[1]['body']['T']
    assert len(out)==16
    for i in (5,6,8,9,11,12,14,15):
        B=out[i]['body'];C=out[i]['cut']
        assert C['root_is_maximal_facet'] and F(2)<C['T']<B['T']
        assert 253*(B['nodes'][2]+B['nodes'][3])>1
        assert out[i]['Psi']>F(204,203)
    assert out[7]['body']['T']>F(253,125)
    return out

def scalar_identities():
    # Polynomial identities underlying the radial convex-moment inequality.
    h,q,r,t=map(var,range(4));one=C(1)
    left=add(sc(pw(h,3),F(1,12)),sc(mul(q,pw(h,2)),F(-1,6)),sc(pw(q,3),F(8,81)))
    right=sc(mul(pw(add(h,sc(q,F(-4,3))),2),add(h,sc(q,F(2,3)))),F(1,12))
    assert left==right
    assert add(C(F(1,3)),sc(r,F(-3,8)),sc(pw(r,3),F(1,24)))==sc(mul(add(one,sc(r,-1)),add(C(8),sc(r,-1),sc(pw(r,2),-1))),F(1,24))
    integ=add(C(F(1,4)),sc(pw(h,4),F(-1,4)),sc(mul(add(h,q),add(one,sc(pw(h,3),-1))),F(-1,3)),sc(mul(mul(q,h),add(one,sc(pw(h,2),-1))),F(1,2)))
    rhs=add(sc(mul(mul(h,pw(add(one,sc(h,-1)),2)),add(sc(h,2),one)),F(1,24)),
            sc(mul(mul(add(C(F(3,4)),sc(q,-1)),pw(add(one,sc(h,-1)),2)),add(h,C(2))),F(1,6)))
    assert integ==rhs
    # Verify the roof formulas independently of the Bernstein conversion.
    b,c,v,t=map(var,range(4));d=mul(c,v);S=add(c,d);A=add(one,b)
    k=add(A,d);K=add(A,c);m=add(one,S,sc(mul(add(one,sc(b,-1)),t),-1))
    base=mul(t,add(mul(b,t),one,S))
    EN=add(sc(A,2),mul(add(sc(A,3),one),S),pw(S,2),sc(mul(c,d),2))
    integral=add(mul(K,add(one,c,sc(d,2))),mul(k,add(one,sc(c,2),d)))
    assert EN==integral
    G2=add(sc(base,2),sc(mul(add(sc(t,2),C(-1)),K),-1),sc(mul(t,k),-1))
    assert G2==add(m,mul(b,add(sc(pw(t,2),2),sc(t,-4),one)),mul(add(t,C(-1)),d))
    G=polys()[0];sigma=F(203,100)
    assert G==add(mul(b,add(sc(pw(t,2),sigma),sc(t,-3),one)),
        mul(c,add(one,sc(t,sigma-2))),sc(mul(d,t),sigma-1),one,sc(t,sigma-3))
    collar=F(1001,1000);upper=F(203,100)*collar**4;gap=F(51,25)-upper
    assert upper==F(203813218812203,100000000000000)
    assert gap==F(186781187797,100000000000000)>0
    return dict(radial_identities=3,roof_identities=3,rational_collar=collar,upper=upper,gap=gap,
                exact_collar_fourth_power=F(204,203))

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def main():
    assert len(sys.argv)==2 and sys.argv[1] in ('build','check')
    report=dict(version=1,identity='FREE_FIBRE_PRISM_TRACE_203_AND_SEGMENT_CORE_V1',
                algebra=scalar_identities(),certificate=proof_data(),controls=actual_controls(),
                universal_tilted_question_closed=False,lower_bound_changed=False)
    raw=(json.dumps(encode(report),sort_keys=True,separators=(',',':'))+'\n').encode()
    assert len(raw)==604422
    assert hashlib.sha256(raw).hexdigest()=='7c7957213edd8f6923d58b95fc1b70b189192cb53625f5a81850575a293543b0'
    target=Path('free_fibre_prism_exact.json')
    if sys.argv[1]=='build':target.write_bytes(raw)
    else:assert target.read_bytes()==raw
    print('CONVEX_RADIAL_MOMENT_IDENTITIES_PASS 3')
    print('FREE_ROOF_203_CONTINUOUS_CUBE_PASS 393 72 321 56592 20')
    print('INDEPENDENT_POWER_BASIS_ALL_393_CLOSED_CELLS_PASS')
    print('TRUE_BODY_FACETS_TWO_FANS_LAMBDA_AND_SEGMENT_CORE_PASS 16')
    print('TRUE_ROOT_PRISM_CUT_TRACE_DROP_ABOVE_TWO_PASS 9')
    print('OVERHANG_SUFFICIENT_TEST_FAILURE_IS_NOT_A_COUNTEREXAMPLE_PASS')
    print('FREE_FIBRE_PRISM_EXACT_PASS',len(raw),hashlib.sha256(raw).hexdigest())

if __name__=='__main__':main()
```

### Полный отдельный численный source — НЕ доказательство

```bash
OPENBLAS_NUM_THREADS=1 python search_free.py wide 851 > wide851.json
OPENBLAS_NUM_THREADS=1 python search_free.py many 853 > many853.json
```

```python
import numpy as np,json,sys
from scipy.spatial import ConvexHull,QhullError
from scipy.optimize import differential_evolution
T0=np.array([(0,0,0),(0,0,1),(0,1,0),(1,0,0)],float)
def evaluate(v):
    al,p,q=v[:3];xyz=np.asarray(v[3:]).reshape(-1,3);x,y,w=xyz.T
    pts=np.vstack((T0,np.column_stack((x,y,(1-p*x-q*y-w)/al))))
    hull=ConvexHull(pts);f=hull.simplices;ref=pts.mean(axis=0)
    v6=np.abs(np.einsum('ij,ij->i',pts[f[:,0]]-ref,np.cross(pts[f[:,1]]-ref,pts[f[:,2]]-ref)))
    t=v6.sum();g=(v6[:,None]*(pts[f].sum(axis=1)+ref)/4).sum(axis=0)/t
    mu=1-p*g[0]-q*g[1]-al*g[2]
    T=((3-al-q)*g[0]+(3-al-p)*g[1])/(t*mu)
    return T,pts
mode=sys.argv[1] if len(sys.argv)>1 else 'wide'
if mode=='wide':bounds=[(.03,1),(-3,1),(-3,1)]+[(1e-6,3),(1e-6,3),(0,0)]*3
elif mode=='many':bounds=[(.03,1),(.1,1),(.1,1)]+[(1e-6,2),(1e-6,2),(0,0)]*4+[(1e-6,2),(1e-6,2),(0,2)]*2
else:raise ValueError(mode)
def obj(v):
    try:return -evaluate(v)[0]
    except (QhullError,ValueError,ZeroDivisionError):return 10.
seed=int(sys.argv[2]) if len(sys.argv)>2 else 851
opt=differential_evolution(obj,bounds,seed=seed,popsize=10,maxiter=300,tol=1e-9,atol=1e-10,polish=True)
T,P=evaluate(opt.x)
print(json.dumps(dict(mode=mode,seed=seed,T=T,x=opt.x.tolist(),points=P.tolist(),nfev=opt.nfev),sort_keys=True))
```

## 11. Связь с физическим Lambda и точная граница продолжения

При настоящем корневом фасете r нормируем его slack как ell/μ, где μ=ell(gP). Для i=ABC и j=ABD имеем в одной действительной геометрии

```text
d_i=3gx/t, d_j=3gy/t,
Lambda_ri=d_i(a+b+c)/(3μ),
Lambda_rj=d_j(a+b+d)/(3μ),
T=Lambda_ri+Lambda_rj,
Lambda_ij Lambda_ji=1/t^2.
```

Именно реальные площадные центроиды двух треугольников дают их арифметические средние в этих формулах. Во всех новых контролях полный Lambda вычислен от того же объёма, того же COM и всех настоящих фасетов; отдельно проверяются `Lambda·1=3·1`, `Lambda·Q=-Q` и `Lambda²+Lambda=4·1·dᵀ`. Это согласовано с физической семантикой parent, а не с независимым выбором строк.

Таким образом любой FULL253-подобный сектор, в котором требуемая высокая пара действительно имеет размеры **3,3**, исключается, когда его действительная геометрия удовлетворяет Ψ≤204/203, в частности ρ≤(204/203)^(1/4). **Это нельзя применить к 5,3-паре.** Не произведено соответствие непрерывного сектора полному списку labelled incidence domains; поэтому никакой FULL/LOCAL счётчик не увеличен и не уменьшен. Различие типов пары уже существенно в поставленном notebook.

После нового результата непокрытая область сформулирована без скрытых численных стен: настоящая соседняя 3,3-пара, неравноконцевой неотрицательный корень и одновременно

```text
ρ>(204/203)^(1/4),
Ψ>204/203.
```

Все равенства в этих двух тестах уже закрыты. Для поиска T≥51/25 эта область дополнительно пересекается с унаследованными необходимыми условиями

```text
1<t<45/7,
49|a-b|+28|c-d|>M, M=max(a,b,c,d),
при 1/t≤3/10: 49|a-b|+13|c-d|>M.
```

Первое следует из прежнего конусного хвоста, остальные — из буквального Raven-parent; они не новые. Более сильные принятые endpoint-gap фильтры notebook также не отменяются; их отдельная точная капсула обозначена в §2 как недоставленная зависимость, не как использованное новое доказательство.

Содержательно остаётся контроль над выступом проекции и его сопряжением с изменившимися моментами Pc. Наиболее полезное продолжение — сохранять не только круглую константу 2.03, но реальные запасы Gσ и Fσ,r и точный смешанный знаменатель Dcross из разрезания. Их можно сопоставлять с объёмом и ell-массой видимых пирамид, вынуждаемых внешними вершинами. Отдельное тело P* показывает, почему нельзя просто заменить это сопоставление утверждением о монотонности отсечения даже выше 2.

**Доказанная нижняя граница 34 не изменена:** не закрыты все действительные геометрии (10,17,9), не закрыты пары других размеров и не предъявлен строгий 110-аттейнер. Результат — полный запрет существенного свободно-форменного класса, новая общая интегральная редукция и точные отрицательные контроли к более сильной, но неверной редукции.

Копии для удобства: доказательный source (`free_fibre_prism_exact.py`), полный точный отчёт (`free_fibre_prism_exact.json`), численный source (`search_free.py`). Восстановление не зависит от этих ссылок: все входы, доказательство и оба полных исходника приведены выше.
