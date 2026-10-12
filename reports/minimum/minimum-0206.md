# minimum-0206

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# K2_WHOLE_LITERAL_INCIDENCE_CORNER_SPLIT_TRACE_V1

## 1. Основной результат

**Остаток малого released-объёма и выхода настоящего центроида закрыт целиком.** Ограничения `D≥7/2`, `U+W≤3D`, прежняя пружинная форма и принадлежность её проективному классу больше не нужны для механически обусловленного следа.

Для любого настоящего released-тела K из раздела 2, всех `0<s,t<1` и нового равномерно заполненного тела P после терминального усечения доказано:

```text
J≤0                       ⇒ T<λK+33/40<697/360<2;
D65≥0, D54≥0, D43≥0        ⇒ T<λK+2/3<16/9.
```

Здесь `T=Λ05(P)+Λ06(P)` использует ПОЛНЫЕ настоящие грани P, а `λK=Λ05(K)` — один настоящий цельногранный след вспомогательного равномерно заполненного K при его собственном центроиде. Это не перенос плотности или центроида из K в P. Все механические знаки относятся только к одному фактическому P и одной SPD-паре `N,M=N⁻¹`.

Кроме того, раздел 7 закрывает **ВСЕ действительные однородные реализации буквальной K2-инцидентности**, перечисленной там, для FULL253 при любой SPD. Доказательство включает три исчерпывающих геометрических случая, в том числе конечную стенку линейной зависимости трёх соседних нормалей. Это целореализационный результат, а не ещё одно семейство или проективное покрытие.

Он не исключает110 при других полярных ориентациях и не отождествляет данный список граней со всеми55 оставшимися K2-доменами. Регистровые счётчики и глобальные границы не изменяются без отдельного буквального отображения.

Буквальный parent: `minimum-0204`, SHA-256 `140ee3332dfc4afa0050579dc304cbda4f223aa94081bc072993b481802212c9`. Его прежние объёмно-центроидные критерии и отдельный пятипараметрический chamber сохраняют правильность; новая теорема снимает их ограничения для указанного механического вывода.

## 2. Более общая реальная геометрия

Пусть K — конечный полноразмерный выпуклый многогранник в положительном октанте, содержащий

```text
O=(0,0,0), e1=(1,0,0), e2=(0,1,0), e3=(0,0,1).
```

Пусть настоящий корневой зазор равен

```text
L=1−x−y−kz≥0 на K,   k<1,
```

и его нулевая грань F0 содержит e1,e2. Координатные грани обозначим `F3:x=0`, `F4:z=0`, `F5:y=0`. Тогда F4 в точности `conv(O,e1,e2)`. F5 может быть любым настоящим многоугольником; она содержит `conv(O,e1,e3)`.

В отличие от старого released-chart, здесь **не требуется, чтобы e3 был концом осевого ребра K**: достаточно `e3∈K`. Поэтому механизм переносится и на некоторые другие инцидентности.

Для `0<s,t<1` берём

```text
P=K∩{x/t+y/s+z≥1}.
```

Удалённая область в точности `conv(O,t e1,s e2,e3)`, а новая F6 — весь треугольник `(t e1,s e2,e3)`. Обратное включение тетраэдра следует из выпуклости K; никакие свободные тетраэдральные массы не вводятся. P содержит e1,e2,e3. Его настоящие стрелки65,54,43 проходят соответственно по рёбрам

```text
e3—t e1,   t e1—e1,   s e2—e2.
```

Это аффинная карта реального тела, не заранее выбранная физическая ортонормальная система. Произвольная SPD N в карте учитывает все физические аффинные реализации.

## 3. Настоящие моменты и тождество объединения двух граней

Определим по одному и тому же равномерному K:

```text
D=6Vol(K),
(U,W,Z)=24∫K(x,y,z),
B=6∫F5(K) L dA,
E=24∫K L=4D−U−W−kZ.
```

Положим `p=st`, `d=D−p`, `C=3−s−t−k` и

```text
e=E−p(C+1),
Vol(P)=d/6,
g=(U−pt, W−sp, Z−p)/(4d),
L(g)=e/(4d).
```

Все эти равенства — реальные объём и первые моменты после удаления указанного тетраэдра. В частности, `d,e,C>0`.

Введём величины фактического центроида P:

```text
A=gx/t+gz,  b=gy/s,  H=A+b−1>0,
Wp=W−s²t=4d gy,
ρ=p/D,
λK=WB/(DE).
```

Буква A здесь — скаляр, не вершина или площадь. `ρ` — настоящая доля удалённого объёма K.

Полная F5 теряет ровно треугольник `(O,e3,t e1)`, для которого

```text
6∫ L =t(3−t−k)=t(C+s).
```

Для всей F6 coarea равна `st/2`, а средний L равен `C/3`. Следовательно физический след точно равен

```text
T=[4gy(B−p)+4p(A−1)C]/e.                         (1)
```

Эквивалентно, при `n=deT`,

```text
n=Wp(B−p)+4dp(A−1)C.                            (2)
```

Это ключевое **тождество объединения полного поверхностного вклада**. B не заменён маркированным треугольником: в нём сохранён весь многоугольный избыток F5(K). Вторая часть тождества учитывает реальный наклон новой F6 и фактическое изменение центроида.

Однофасетная теорема из принятой памяти применяется к координате y и функции L на настоящем K и даёт

```text
0<λK=WB/(DE)<10/9.                              (3)
```

Используется именно эта однофасетная теорема, не завершённый маркированный двухтреугольный функционал.

## 4. Реальный объёмный контроль, отсутствовавший в старой организации доказательства

Для неотрицательной аффинной функции f на настоящем трёхмерном выпуклом многограннике и любой точки a этого тела положительный тетраэдральный веер из a даёт `4 mean(f)≥f(a)`. Допускаются нулевые клетки и несобственная вершина веера: все положительные клетки принадлежат одному настоящему телу.

Применяя это к K из e1,e3,O и к P из e1,e3, получаем

```text
U≥D,  Z≥D,
E≥D·max(1,1−k),
gx≥1/4,  gz≥1/4,  A≥(1+t)/(4t)≥1/2.             (4)
```

Особенно важно `E≥D(1−k)`: при отрицательном k оно следует из веера **из e3**, поэтому не требует прежнего условия `U+W≤3D`. Именно этот реальный объёмный вклад закрывает весь неограниченный отрицательный k-хвост, включая центроидный выход.

Есть второй реальный контроль:

```text
W≤D².                                           (5)
```

Доказательство. Для выпуклого тела с настоящей базой площади a0 в плоскости y=0, объёмом V и первым моментом Jy справедливо `a0 Jy≤3V²/4`. Действительно, корень нормированной площади сечения `f(y)` вогнут, `f(0)=1`. Если `I=∫f²`, то высота тела не больше `3I`. Сравнение с `(1−y/(3I))₊` имеет равный интеграл квадратов и не более одной перемены знака с плюса на минус; поэтому `∫yf²≤3I²/4`. Здесь настоящая F5(K) содержит треугольник площади1/2, то есть `a0≥1/2`, откуда `W=24Jy≤36V²=D²`. Это не выбор отдельной массы или свободного профиля вместо K.

Из(4), для всех `k<1`, следуют

```text
DC/E≤3−t,   D(C+1)/E≤4−t.                       (6)
```

При `k≥0` достаточно `E≥D`. При `k=−a<0` используем `E≥D(1+a)` и точные положительные разности

```text
(3−t)(1+a)−C=s+a(2−t)>0,
(4−t)(1+a)−(C+1)=s+a(3−t)>0.
```

Ни верхняя граница D, ни нижняя граница k не введены.

## 5. Геометрическая половина J≤0 уже целиком низкоследовая

Сохраним буквальный полином parent:

```text
J=3sU−tW+st(4D+3Z)−9s²t²
 =4dp(3A−b+1).                                  (7)
```

Предположим только `J≤0`, пока без метрики. Тогда `b≥3A+1`. Следующее тождество использует реальные ограничения(4),(5):

```text
J−(D−p)(9p−D)
 =3s(U−D)+t(D²−W)+3p(Z−D)+(1−t)(3Ds+D²)>0.
```

Отсюда

```text
0<ρ<1/9.                                        (8)
```

Вторая точная связь геометрии с долей удалённого объёма:

```text
4bρ(1−ρ)=t(W−s²t)/D²≤t.                        (9)
```

Положим `a=(A−1)₊`. Из полного тождества(2), `Wp>0`, (3) и (6):

```text
T < [λK/(1−ρ)+4ρa(3−t)]/[1−ρ(4−t)] =: R.       (10)
```

Знаменатель положителен по(8). Пусть `Δ=(1−ρ)[1−ρ(4−t)]`, так что `0<Δ<1`. Прямая алгебра даёт

```text
(2−R)Δ
 =2−λK−2ρ−ρ(1−ρ)[2(4−t)+4a(3−t)].
```

Из `2ρ<(9/4)ρ(1−ρ)`, (9) и `0<t<1` получаем

```text
(2−R)Δ > 2−λK−[33/4+8a]/(4b).                  (11)
```

Здесь используются только

```text
33/4−t(41/4−2t)=(1−t)(33/4−2t)≥0,
2−t(3−t)=(1−t)(2−t)≥0.
```

Если `1/2≤A≤1`, то `b≥3A+1≥5/2` и дробь в(11) не больше33/40. Если `A≥1`, то она не больше

```text
(8A+1/4)/[4(3A+1)] <2/3<33/40.
```

Поскольку `2−λK−33/40>0` и `Δ<1`, из(10),(11) следует

```text
J≤0 ⇒ T<λK+33/40<697/360<2.                    (12)
```

Это уже общая новая геометрическая связь: высокий настоящий цельногранный след `T≥697/360` требует `J>0`, а не только выхода из старых достаточных объёмно-центроидных условий. Конечная стенка `J=0` включена в строгий вывод(12).

## 6. Одна общая метрика улучшает границу до16/9

При собственном центроиде P его настоящие координатные полюса удовлетворяют

```text
q6=ξq4+ηq5+ζq3,
ξ=gz/H, η=b/H, ζ=gx/(tH),
τ=ξ+ζ=A/H>0,  τ+η=1+1/H>1.
```

Ни полюса, ни центроид поляры независимо не перенормируются. Нормируем `||q5||N=1`, обозначим `r=||q4||N>1`, `u=q4ᵀNq5∈[1,r)`. Из `D65≥0` полюс q6 лежит в шаре с центром q5/2 и радиусом1/2. Независимость q3,q4,q5 делает оценку

```text
q4ᵀNq6<(u+r)/2
```

строгой. Из `D43≥0` одновременно следует `q4ᵀNq6≥τr²+ηu`. Значит

```text
(1−2η)u+r−2τr²>0.                              (13)
```

При `η≤1/2` правая верхняя оценка через `u<r` отрицательна из `τ+η>1`. Поэтому `η>1/2`. Теперь `u≥1` даёт `1−2η+r−2τr²>0`. Если `τ≥1/4`, этот полином убывает на `r>1` и уже при r=1 отрицателен. Следовательно `τ<1/4`; его максимум на всей прямой дополнительно даёт

```text
8τ(2η−1)<1.
```

Подставляя `H=A+b−1`, получаем полную нужную скалярную необходимость

```text
b>3A+1+4√A.                                    (14)
```

Все три исходные стрелки могут быть слабыми. Строгость(13),(14) обеспечивает положительная определённость и линейная независимость реальных полюсов, не скрытое предположение о строгих стрелках.

В(11) при `A≥1` дробь по-прежнему строго меньше2/3. При `1/2≤A≤1` из(14) имеем `b>9/2`, и дробь строго меньше `11/24<2/3`. Поэтому

```text
(2−R)Δ>4/3−λK>0,
T<λK+2/3<16/9.                                 (15)
```

Таким образом механика вынуждает достаточно малую реальную долю удалённого объёма и ограничивает добавку к **одному полному старому поверхностному следу**. Доказательство не устанавливает универсальное `Q=F+J/4≥0` и не нуждается в нём.

## 7. Вся буквальная K2-инцидентность: исчерпание геометрии

Рассмотрим ЛЮБУЮ настоящую однородную реализацию циклов

```text
F0=012; F1=34510; F2=6743; F3=2768; F4=0289;
F5=9630; F6=986; F7=5721; F8=754.
```

Её настоящие рёбра:

```text
01,02,03,09,12,15,27,28,34,36,45,47,57,67,68,69,89.
```

Три соседа настоящего треугольника F6 — F3,F4,F5. Нормируем их неотрицательные аффинные зазоры так, чтобы на F6 они были тремя барицентрическими координатами. Их градиенты имеют ранг2 или3; ранг1 невозможен для треугольника.

### 7.1. Ранг2: вся конечная стенка

Любая линейная зависимость трёх полных градиентов ограничивается на плоскость F6. Единственная зависимость трёх барицентрических градиентов там имеет равные положительные коэффициенты. Поэтому сумма трёх нормированных зазоров тождественно1 во всём пространстве. На настоящем центроиде это даёт положительную зависимость

```text
h3 q3+h4 q4+h5 q5=0,  h3,h4,h5>0.
```

Но `D54≥0` даёт `q4ᵀNq5≥||q5||²>0`; скалярное произведение зависимости с Nq4 делает `q4ᵀNq3<0`, несовместимым с `D43≥0`. Эта стенка закрыта для любой SPD без следового аргумента.

### 7.2. Ранг3 и сторона содержащего тетраэдра

Три зазора являются аффинными координатами `u1,u2,u3≥0`, а F6 имеет уравнение `u1+u2+u3=1`. Если P лежит на стороне суммы≤1, он содержится в соответствующем тетраэдре и содержит всю его треугольную базу F6.

В настоящем вершинном веере P средние трёх базовых барицентрических координат не меньше1/4; средняя апикальная координата положительна и не больше1/4. Отсюда

```text
q6=−αq4−βq5−γq3,  α,β,γ≥1.
```

Точная общиметрическая идентичность

```text
0=2||q6−q5/2+q4/4||N²
 +(α+γ−1/8)||q4||N²+β||q5||N²
 +2D65+(β+1/2)D54+γD43
```

исключает три слабые стрелки. Использован центроид P, не центроид содержащего тетраэдра.

### 7.3. Ранг3 и внешняя сторона: released-тело действительно существует и ограничено

Пусть теперь P лежит на стороне суммы≥1, а O — точка нулевых координат. Нужно обосновать освобождение F6, а не предположить его допустимость.

Для другого некоординатного настоящего зазора f предположим `f(O)=−a≤0`, а значения f в трёх вершинах F6 равны `b1,b2,b3≥0`. Тогда

```text
f(u)=a(u1+u2+u3−1)+b1u1+b2u2+b3u3.
```

При a>0 его нулевая область на P содержится в F6 и имеет размерность меньше2, если f не задаёт саму F6. При a=0 нулевая область может быть гранью размерности2 только для одной из трёх координатных граней. В обоих случаях новый настоящий некоординатный сосед невозможен. Следовательно O имеет СТРОГО положительный зазор во всех оставшихся некоординатных гранях.

Удалим только опору F6 и назовём пересечение остальных полупространств K. Оно содержит O и P. Его ненулевой луч рецессии лежал бы в положительном октанте и имел положительную сумму координат, а значит при большом параметре вошёл бы в P, противореча ограниченности P. Поэтому K ограничено. Более того,

```text
K=conv(P,O)=P∪conv(O,9,8,6),
```

с непересекающимися объёмными внутренностями.

Из буквальных рёбер09,28 и четырёхугольника F4 внешними концами двух осей являются0,2. Нормируем аффинно `O=0`, `0=e1`, `2=e2`, `6=e3`. Получаем `9=t e1`, `8=s e2`, `0<s,t<1`. Настоящая F0 содержит e1,e2; её зазор в O положителен, а в6 строго положителен, поэтому он имеет вид `L=1−x−y−kz`, `k<1`. Все предпосылки раздела2 теперь ДОКАЗАНЫ для этой произвольной реализации. Применяется(15).

### Итог исчерпания

В первых двух случаях три стрелки невозможны. В последнем они влекут `T<16/9`. Следовательно буквальный FULL253 — весь неотрицательный граф

```text
(1,0),(2,1),(3,2),(4,3),(5,4),(6,5),(7,0),(8,7)
```

невозможен на ВСЕХ реализациях указанных циклов: его принятое условие `T>51/25` противоречит(15). Запас между порогами равен `59/225`. Наличие только указанного дерева внутри большего графа не используется как источник высокого следа.

Тот же proof-pattern переносится на треугольную F6 с двумя простыми вершинами8,9 вдоль общего ребра с четырёхугольником F4, противоположное ребро которого принадлежит F0, не содержащей6. Другие грани и степень6 не обязаны совпадать с K2. Непроверенное перечисление всех таких инцидентностей здесь не выдаётся за регистровый результат.

## 8. Точные реальные контрконтроли и границы утверждений

Пять новых реальных форм и шесть общих метрических пар сохранены полностью. Это НЕ переименованный spring-base. Его исходная геометрическая14-ка остаётся `(1,5,12219,1,14102,14220,32,8740,81,76,111,18,19,1)`; новые формы имеют отдельные имена.

Для двух исходных новых форм используется только следующий точный генератор при фиксированных параметрах из таблицы. Положим

```text
I=(1−c,1−c,1),
V0=e1, V2=e2, V6=e3,
V1=(1−ch,1−ch,h),
V3=(1−c,0,1), V7=(0,1−c,1),
V4=(1−r)I+rV3, V5=(1−v)I+vV1,
V8=s e2, V9=t e1.
```

| Имя | (c,h,r,v,s,t) | Настоящие released-параметры |
|---|---|---|
|NEW_CUBICAL_CENTROID_EXIT|`(0,1/10,1/3,1/2,1/100,2/3)`|`D=23/4`, `k=−10`, `gK,x+gK,y=112/115>3/4`|
|NEW_SMALL_VOLUME_POSITIVE_K|`(3/5,9/10,1/3,1/2,1/100,2/3)`|`D=1663/750<7/2`, `k=4/45>0`|

Для каждой формы берём её собственные полюса и точные ξ,η,ζ из `q6=ξq4+ηq5+ζq3`. Метрическая конструкция:

```text
x=(101/100,7/2,0), y=(1,0,0), w=(501/800,7/16,1/20),
z=(w−ξx−ηy)/ζ,
Ametric=[x y z][q4 q5 q3]⁻¹,
N=Ametricᵀ Ametric, M=N⁻¹.
```

Обе новые формы реализуют все три стрелки СТРОГО. Для первой:

```text
Vol(P)=1723/1800,
g=(10121/20676,167249/344600,13741/27568),
T=19888883479/35692827176,
(D65,D54,D43)=(25699/640000,1/100,88531817843/1619360000),
S=[1,3], U=[1,6], H=[02,67], strict222, physicalweak000.
```

Для второй:

```text
Vol(P)=829/2250,
g=(74539/248700,597137/1989600,6999/16580),
T=8286280522/8971790325,
(D65,D54,D43)=(25699/640000,1/100,75546919493/1490780000),
S=[0,3], U=[2,6], H=[02,67], strict222, physicalweak000.
```

Во втором контроле F0 действительно строго устойчива. Полные неотрицательные полярные графы имеют15 и18пар соответственно, не8: ни один не FULL253.

Для первой формы заменить только x на `(1,7/2,0)` и заново вычислить z,Ametric,N. Тогда D54=0, остальные две стрелки положительны; census остаётся222weak000. Единственный нуль среди68примитивов находится на ребре09 с полным пакетом

```text
(2694430797756/1807430181649, −2060708/1344407, −49/4, 0).
```

Это безвредная слабая стрелка, а не физическое слабое равновесие.

Для ещё трёх форм применяем к `NEW_CUBICAL_CENTROID_EXIT` настоящую проективность

```text
(x,y,z) ↦ (x,y,1)/(a+x+2y+3z),
a=−1/100, 0, 1/100.
```

Все фактические знаменатели положительны; при отрицательном a их минимум1/100. Каждый образ заново равномерно заполнен и центрирован настоящим объёмным центроидом. При

```text
R=((1,1/5,1/7),(0,3/2,1/11),(0,0,2)), N=RᵀR, M=N⁻¹
```

все три имеют strict323weak000 и ненулевые68примитивов. Они реализуют соответственно сторону содержащего тетраэдра, точную ранг2-стенку и released-сторону. Их реальные трёхстрелочные примитивы отрицательны, как и должно быть; это контроли геометрического исчерпания, не предположение о постоянстве census на проективном интервале.

Всего407ненулевых примитивов и один указанный безвредный нуль. Ни одного110тела нет. Q положителен в двух исходных новых формах; никаких контрпримеров к универсальному Q из них не следует. Отрицательный результат о Q не заявляется вообще.

## 9. Статус и точный оставшийся фронтир

Новый журнал, включая буквальный parent, прочитан последовательно через EOF. Новое доказательство не требует старых коэффициентных сеток, проективных вееров, отсутствующих каталогов или вычислительного переноса весов. Его единственный глубокий принятый вход — настоящая однофасетная граница(3); остальные используемые геометрические и метрические леммы доказаны выше.

Таким образом, в указанном released-классе **нет остатка малого D или центроидного выхода для механически обусловленного следа**. Для приведённой буквальной K2-инцидентности нет остатка FULL253 ни по форме, ни по метрике, ни на ранг2-стенке. Неустановленная универсальность Q — отдельный функциональный вопрос, больше не препятствующий этому выводу.

Это не весь регистр K2=55 и не запрет110 с любой полярной ориентацией. Глобальные `34≤Cmin≤622` и численные регистры здесь не меняются. Следующий полезный шаг — точное сопоставление доказанного треугольно-четырёхугольного шаблона с буквальным FULL253-регистром, отдельно от иных инцидентностей без этого шаблона.

Статус: авторское аналитическое доказательство относительно явно названного принятого входа. Точные идентичности и шесть физических контролей исполнены, затем воспроизведены из одного исходника в другом каталоге с совпадением байтов. Это не независимая реализация всего верификатора и не proof-assistant-формализация.

## 10. Автономная recovery-капсула

Ни один старый генератор не является вычислительной зависимостью нового source. Он содержит буквальные циклы, все новые точные входы, построение настоящего hull, перечисление всех независимых троек опор, две реальные объёмные центровки, полный Lambda, одну взаимно обратную пару метрик и все68механических примитивов каждого контроля. Алгебраические проверки восстанавливают точные тождества нового доказательства; конечные контроли не подменяют доказательство полноты.

Среда: CPython3.13.5, SymPy1.14.0, assertions включены. Сохранить приведённый ниже полный source как `k2_corner_split.py`, UTF-8/LF с конечным LF, и выполнить:

```text
python k2_corner_split.py build
python k2_corner_split.py check
```

Фактически выполнены build, check, затем перенос только source в новый каталог и новый build. Оба140321-байтных отчёта совпали побайтно.

```text
k2_corner_split.py:13939 bytes
SHA256 068e9f98dd14314ac924a8b2005e6ff01a71bb8ff88502e4c899a407ef8bb3f4
corner_split_report.json:140321 bytes
SHA256 afd180fff481ef587cfc3bea5b99141ae41bc158dbe5116dc7263fd1915a821e
```

Terminal markers:

```text
CORNER_SPLIT_TRUE_MOMENT_MERGE_AND_SCALAR_PROOF_IDENTITIES_PASS
K2_SIX_ACTUAL_OWN_COM_RECIPROCAL_CONTROLS_407_NONZERO_ONE_HARMLESS_ZERO_PASS
K2_WHOLE_LITERAL_INCIDENCE_THREE_CASE_PROOF_RECOVERY_PASS 140321 afd180fff481ef587cfc3bea5b99141ae41bc158dbe5116dc7263fd1915a821e
```

Дополнительные копии: полный bundle (`K2_CORNER_SPLIT_WHOLE_INCIDENCE_bundle.zip`), исходник (`k2_corner_split.py`). Следующий полный источник достаточен без этих ссылок.

### Полный runnable source

```python
"""K2 actual corner-split trace theorem: exact identities and realized controls.
CPython 3.13.5, SymPy 1.14.0; rational inputs; assertions enabled.
Run: python k2_corner_split.py build|check
The universal proof is the accompanying Markdown, not inferred from controls.
"""
from fractions import Fraction as F
from itertools import combinations
from math import gcd,lcm
from functools import reduce
from pathlib import Path
import hashlib,json,sys
import sympy as S
assert __debug__ and sys.version_info[:3]==(3,13,5) and S.__version__=='1.14.0'
sys.set_int_max_str_digits(0)
HERE=Path(__file__).resolve().parent
PARENT=['minimum-0204','140ee3332dfc4afa0050579dc304cbda4f223aa94081bc072993b481802212c9']
FAC={0:(0,1,2),1:(3,4,5,1,0),2:(6,7,4,3),3:(2,7,6,8),4:(0,2,8,9),5:(9,6,3,0),6:(9,8,6),7:(5,7,2,1),8:(7,5,4)}
KC={0:(0,1,2),1:(3,4,5,1,0),2:(6,7,4,3),3:(2,7,6,8),4:(0,2,8),5:(8,6,3,0),7:(5,7,2,1),8:(7,5,4)}
FULL=((1,0),(2,1),(3,2),(4,3),(5,4),(6,5),(7,0),(8,7))
I=tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(c,a):return tuple(c*x for x in a)
def cross(a,b):return(a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def solve(A,b):
 a=[list(map(F,r))+[F(v)] for r,v in zip(A,b)];m=len(a);n=len(a[0])-1
 for j in range(n):
  k=next(i for i in range(j,m) if a[i][j]);a[j],a[k]=a[k],a[j];v=a[j][j];a[j]=[z/v for z in a[j]]
  for i in range(m):
   if i!=j:v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[j])]
 assert all(not any(r) for r in a[n:])
 return tuple(a[i][n] for i in range(n))
def inv(A):return tuple(zip(*(solve(A,[int(i==j) for i in range(len(A))]) for j in range(len(A)))))
def mm(A,B):return tuple(tuple(dot(r,c) for c in zip(*B)) for r in A)
def mv(A,v):return tuple(dot(r,v) for r in A)
def spd(A):return A==tuple(zip(*A)) and A[0][0]>0 and A[0][0]*A[1][1]>A[0][1]**2 and det(*A)>0
def primitive(x):
 x=tuple(map(F,x));d=lcm(*(v.denominator for v in x));a=tuple(int(v*d) for v in x);g=reduce(gcd,map(abs,a));assert g
 return tuple(F(v//g) for v in a)
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [encode(v) for v in x]
 return x
def serial(x):return (json.dumps(encode(x),sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(x):return [len(x),hashlib.sha256(x).hexdigest()]
def actual(X,faces):
 X=tuple(tuple(map(F,x)) for x in X);assert len(set(X))==len(X)
 o=tuple(sum(x[j] for x in X)/len(X) for j in range(3));planes={};cycles={};tri=[];coarea={};centers={}
 for i,f in faces.items():
  a,b,c=(X[v] for v in f[:3]);n=cross(sub(b,a),sub(c,a));b0=dot(n,a)
  if b0-dot(n,o)<0:f=tuple(reversed(f));n=scale(-1,n);b0=-b0
  b0,*n=primitive((b0,)+n);n=tuple(n);planes[i]=(n,b0);cycles[i]=f
  gaps=[b0-dot(n,x) for x in X];assert min(gaps)>=0 and {j for j,z in enumerate(gaps) if z==0}==set(f)
  for a,b in zip(f,f[1:]+f[:1]):assert min(dot(n,cross(sub(X[b],X[a]),sub(X[v],X[a]))) for v in f if v not in (a,b))>0
  ts=[(f[0],f[j],f[j+1]) for j in range(1,len(f)-1)];tri.extend((i,t) for t in ts);j=next(j for j in range(3) if n[j]);weights=[]
  for t in ts:
   av=cross(sub(X[t[1]],X[t[0]]),sub(X[t[2]],X[t[0]]));w=av[j]/(2*n[j]);assert w>0 and av==scale(2*w,n);weights.append(w)
  coarea[i]=sum(weights);centers[i]=tuple(sum(w*sum(X[v][j] for v in t)/3 for w,t in zip(weights,ts))/sum(weights) for j in range(3))
 assert all(sum(coarea[i]*planes[i][0][j] for i in faces)==0 for j in range(3))
 verts=set()
 for ids in combinations(faces,3):
  A=[planes[i][0] for i in ids]
  if det(*A):
   x=solve(A,[planes[i][1] for i in ids])
   if all(b-dot(n,x)>=0 for n,b in planes.values()):verts.add(x)
 assert verts==set(X)
 edges=tuple(sorted({tuple(sorted((a,b))) for f in cycles.values() for a,b in zip(f,f[1:]+f[:1])}));ef=tuple(tuple(i for i,f in cycles.items() if a in f and b in f) for a,b in edges)
 assert len(X)-len(edges)+len(faces)==2 and all(len(x)==2 for x in ef)
 def fan(apex):
  D=F(0);mom=[F(0)]*3;positive=0
  for _,t in tri:
   a,b,c=(X[v] for v in t);d=det(sub(a,apex),sub(b,apex),sub(c,apex));assert d>=0;positive+=d>0;D+=d
   for j in range(3):mom[j]+=d*(apex[j]+a[j]+b[j]+c[j])
  assert D>0
  return D,tuple(mom),positive
 D,mom,count=fan(o);D1,mom1,count1=fan(X[1]);assert (D,mom)==(D1,mom1)
 g=scale(1/(4*D),mom);V=D/6;q={i:scale(1/(b-dot(n,g)),n) for i,(n,b) in planes.items()}
 masses={i:coarea[i]*(b-dot(n,g))/V for i,(n,b) in planes.items()};L={a:{i:masses[i]*(1-dot(q[a],sub(centers[i],g))) for i in faces} for a in faces}
 assert sum(masses.values())==3
 for a in faces:
  assert L[a][a]==0 and sum(L[a].values())==3
  for j in range(3):assert sum(L[a][i]*q[i][j] for i in faces)==-q[a][j]
  for b in faces:assert sum(L[a][i]*L[i][b] for i in faces)+L[a][b]==4*masses[b]
  assert all(0<L[a][b]<F(10,9) for b in faces if a!=b)
 return dict(raw_vertices=X,vertices=tuple(sub(x,g) for x in X),facets=cycles,edges=edges,edge_facets=ef,planes=planes,volume=V,centroid=g,D=D,moments24=mom,poles=q,masses=masses,Lambda=L,coarea=coarea,facet_raw_centroids=centers,fan_counts=(count,count1))
def mechanics(P,N):
 assert spd(N);M=inv(N);assert spd(M) and mm(M,N)==I
 X=P['vertices'];q=P['poles'];pack=[];weak={}
 def primal(i,j):return dot(X[i],mv(M,sub(X[j],X[i])))
 def polar(i,j):return dot(q[i],mv(N,sub(q[j],q[i])))
 for (a,b),(i,j) in zip(P['edges'],P['edge_facets']):
  z=(primal(a,b),primal(b,a),polar(i,j),polar(j,i));pack.append(z)
  if max(z)==0:
   v=sub(X[b],X[a]);u=-z[0]/dot(v,mv(M,v));assert 0<=u<=1;point=add(X[a],scale(u,v));kind='VF' if u in (0,1) and 0 in z[2:] else ('VE' if u in (0,1) else 'EF')
   if point not in weak:weak[point]=dict(point=point,kind=kind,edges=[])
   else:assert weak[point]['kind']==kind
   weak[point]['edges'].append((a,b))
 stable=[i for i in q if all(polar(i,j)<0 for j in q if j!=i)];unstable=[i for i in range(len(X)) if all(primal(i,j)<0 for j in range(len(X)) if j!=i)];saddle=[e for e,z in zip(P['edges'],pack) if max(z)<0]
 if not weak:assert len(stable)+len(unstable)-len(saddle)==2
 arcs=tuple((i,j) for i in q for j in q if j!=i and polar(i,j)>=0)
 return dict(N=N,M=M,S=stable,U=unstable,H=saddle,weak=list(weak.values()),packets=pack,zero_primitives=sum(z==0 for p in pack for z in p),full_polar_arcs=arcs,literal_FULL253=arcs==FULL,three_arrows=[polar(i,j) for i,j in ((6,5),(5,4),(4,3))])
def shape(c,h,r,v,s,t):
 c,h,r,v,s,t=map(F,(c,h,r,v,s,t));assert 0<=c<1 and 0<h<1 and all(0<x<1 for x in (r,v,s,t))
 apex=(1-c,1-c,F(1));x1=(1-c*h,1-c*h,h);x3=(1-c,F(0),F(1));x7=(F(0),1-c,F(1))
 return ((F(1),F(0),F(0)),x1,(F(0),F(1),F(0)),x3,add(scale(1-r,apex),scale(r,x3)),add(scale(1-v,apex),scale(v,x1)),(F(0),F(0),F(1)),x7,(F(0),s,F(0)),(t,F(0),F(0)))
def local_metric(P,weak=False):
 q=P['poles'];basis=tuple(zip(q[4],q[5],q[3]));xi,eta,zeta=solve(basis,q[6]);assert min(xi,eta,zeta)>0
 x=(F(1) if weak else F(101,100),F(7,2),F(0));y=(F(1),F(0),F(0));w=(F(501,800),F(7,16),F(1,20));z=scale(1/zeta,sub(sub(w,scale(xi,x)),scale(eta,y)))
 A=mm(tuple(zip(x,y,z)),inv(basis));N=mm(tuple(zip(*A)),A);assert spd(N)
 return N,dict(circuit=(xi,eta,zeta),images=(x,y,z,w),factor=A)
def corner(P):
 planes=P['planes'];A=[planes[i][0] for i in (3,4,5)]
 if not det(*A):
  q=P['poles'];alpha,beta=solve(tuple(zip(q[4],q[5])),scale(-1,q[3]));assert min(alpha,beta)>0
  return dict(region='rank_two',positive_circuit=(alpha,beta))
 O=solve(A,[planes[i][1] for i in (3,4,5)]);n,b=planes[6];slack=b-dot(n,O)
 if slack>0:
  q=P['poles'];c=solve(tuple(zip(q[4],q[5],q[3])),scale(-1,q[6]));assert min(c)>=1
  return dict(region='containing_tetrahedron',O=O,negative_circuit=c)
 assert slack<0
 assert all(b-dot(n,O)>0 for i,(n,b) in planes.items() if i not in (3,4,5,6))
 X=P['raw_vertices'];H=inv(tuple(zip(sub(X[0],O),sub(X[2],O),sub(X[6],O))));Y=tuple(mv(H,sub(x,O)) for x in X);K=actual(Y[:8]+((F(0),)*3,),KC);Paxis=actual(Y,FAC)
 assert Y[0]==(1,0,0) and Y[2]==(0,1,0) and Y[6]==(0,0,1)
 s=Y[8][1];t=Y[9][0];assert Y[8]==(0,s,0) and Y[9]==(t,0,0) and 0<s<1 and 0<t<1
 k=(1-Y[1][0]-Y[1][1])/Y[1][2];assert k<1
 D=K['D'];U,W,Z=K['moments24'];E=4*D-U-W-k*Z
 cn,cb=K['planes'][5];area=K['coarea'][5]*abs(cn[1]);mu=1-dot((1,1,k),K['facet_raw_centroids'][5]);B=6*area*mu
 assert area>=F(1,2) and W*area<=D*D/2 and min(U,Z)>=D
 assert E>=D*max(1,1-k) and B>0
 lam=W*B/(D*E);assert lam==K['Lambda'][0][5] and lam<F(10,9)
 p=s*t;d=D-p;e=E-p*(4-s-t-k);wp=W-s*s*t
 assert d/6==Paxis['volume'] and scale(1/(4*d),(U-s*t*t,W-s*s*t,Z-s*t))==Paxis['centroid']
 n=wp*(B-t*(3-t-k))+(s*U+t*W+p*(Z-4*D+p))*(3-s-t-k)
 T=n/(d*e);assert T==Paxis['Lambda'][0][5]+Paxis['Lambda'][0][6]==P['Lambda'][0][5]+P['Lambda'][0][6]
 gx,gy,gz=Paxis['centroid'];aa=gx/t+gz;bb=gy/s;rho=p/D;J=3*s*U-t*W+p*(4*D+3*Z)-9*p*p;Q=2*d*e-n+J/4
 assert n==wp*(B-p)+4*d*p*(aa-1)*(3-s-t-k)
 if J<=0:assert rho<F(1,9) and T<lam+F(33,40)<F(697,360)
 return dict(region='released',O=O,axis_map=H,axis_body=Paxis,released_body=K,quantities=(D,U,W,Z,B,k),lambda_merged=lam,trace=T,J=J,quarter_Q=Q,rho=rho,A=aa,b=bb,cap=(s,t),bulk_tests=(D>=F(7,2),U+W<=3*D))
def algebra():
 D,U,W,Z,B,k,s,t=S.symbols('D U W Z B k s t');p=s*t;d=D-p;E=4*D-U-W-k*Z;C=3-s-t-k;e=E-p*(C+1);wp=W-s*s*t;A=(U-p*t)/(4*d*t)+(Z-p)/(4*d)
 n=wp*(B-t*(3-t-k))+(s*U+t*W+p*(Z-4*D+p))*C;J=3*s*U-t*W+p*(4*D+3*Z)-9*p*p
 assert S.cancel(n-wp*(B-p)-4*d*p*(A-1)*C)==0
 rem=3*s*(U-D)+t*(D*D-W)+3*p*(Z-D)+(1-t)*(3*D*s+D*D)
 assert S.expand(J-d*(9*p-D)-rem)==0
 rho,aa,bb,lam,q=S.symbols('rho aa bb lam q');b0=(W-s*s*t)/(4*d*s)
 assert S.cancel(4*b0*(p/D)*(1-p/D)-t*(W-s*s*t)/D**2)==0
 H=aa+bb-1
 assert S.expand(H**2-8*aa*(2*bb-H)-(bb-3*aa-1)**2+16*aa)==0
 v=lam/(1-rho)+4*rho*q*(3-t);den=1-rho*(4-t)
 R=(2-lam-2*rho-rho*(1-rho)*(2*(4-t)+4*q*(3-t)))/((1-rho)*den)
 assert S.cancel(2-v/den-R)==0
 assert S.expand(S.Rational(33,4)-t*(S.Rational(41,4)-2*t)-(1-t)*(S.Rational(33,4)-2*t))==0
 assert S.expand(2-t*(3-t)-(1-t)*(2-t))==0
 assert S.cancel(S.Rational(2,3)-(8*aa+S.Rational(1,4))/(4*(3*aa+1))-S.Rational(29,48)/(3*aa+1))==0
 assert S.Rational(33,4)/(4*S.Rational(9,2))==S.Rational(11,24)<S.Rational(2,3)
 assert S.Rational(10,9)+S.Rational(33,40)==S.Rational(697,360)<2
 assert S.Rational(10,9)+S.Rational(2,3)==S.Rational(16,9)<S.Rational(51,25)
 a=S.symbols('a')
 assert S.expand((3-t)*(1+a)-(3-s-t+a)-s-a*(2-t))==0
 assert S.expand((4-t)*(1+a)-(4-s-t+a)-s-a*(3-t))==0
 # For L(O)=-a<0, alpha_i=L(A_i)>=0 and sigma=sum x_i>=1.
 x,y,z,alpha,beta,gamma=S.symbols('x y z alpha beta gamma');L=-a+(a+alpha)*x+(a+beta)*y+(a+gamma)*z
 assert S.expand(L-a*(x+y+z-1)-alpha*x-beta*y-gamma*z)==0
 print('CORNER_SPLIT_TRUE_MOMENT_MERGE_AND_SCALAR_PROOF_IDENTITIES_PASS',flush=True)
 return dict(parent=PARENT,merging_identity=str(S.factor(n-wp*(B-p))),J_positive_remainder=str(rem),first_halfspace_bound=F(697,360),three_arrow_bound=F(16,9),FULL253_gap=F(59,225),conditions='Actual geometry, own uniform moments, one SPD; no freely fitted moments.')
def controls():
 inputs=[('NEW_CUBICAL_CENTROID_EXIT',(0,F(1,10),F(1,3),F(1,2),F(1,100),F(2,3))),('NEW_SMALL_VOLUME_POSITIVE_K',(F(3,5),F(9,10),F(1,3),F(1,2),F(1,100),F(2,3)))]
 records=[]
 def keep(name,P,N,extra):
  m=mechanics(P,N);c=corner(P);T=P['Lambda'][0][5]+P['Lambda'][0][6];assert not m['literal_FULL253']
  if min(m['three_arrows'])>=0:
   assert c['region']=='released' and c['J']<0 and T<c['lambda_merged']+F(2,3)<F(16,9)
   assert (c['b']-3*c['A']-1)>0 and (c['b']-3*c['A']-1)**2>16*c['A']
  records.append(dict(name=name,body=P,mechanics=m,corner=c,trace=T,extra=extra));print(name,'SUH',len(m['S']),len(m['U']),len(m['H']),'weak',len(m['weak']),'zeros',m['zero_primitives'],'T',float(T),'region',c['region'],flush=True)
 for name,par in inputs:
  P=actual(shape(*par),FAC);N,extra=local_metric(P);keep(name,P,N,dict(parameters=par,metric=extra))
  if name==inputs[0][0]:
   assert corner(P)['bulk_tests']==(True,False);N,extra=local_metric(P,True);keep(name+'_D54_WALL',P,N,dict(parameters=par,metric=extra));assert records[-1]['mechanics']['three_arrows'][1]==0
  else:assert corner(P)['quantities'][0]<F(7,2) and corner(P)['quantities'][-1]>0
 R=((F(1),F(1,5),F(1,7)),(F(0),F(3,2),F(1,11)),(F(0),F(0),F(2)));N=mm(tuple(zip(*R)),R);X=shape(*inputs[0][1])
 for a,label in ((F(-1,100),'CONTAINING_TETRAHEDRON'),(F(0),'FINITE_RANK_TWO_WALL'),(F(1,100),'RELEASED_OTHER_PROJECTIVE_SIDE')):
  ds=[a+x[0]+2*x[1]+3*x[2] for x in X];assert min(ds)>0
  Y=tuple(scale(1/d,(x[0],x[1],F(1))) for x,d in zip(X,ds));P=actual(Y,FAC)
  keep(label,P,N,dict(source_parameters=inputs[0][1],denominator_constant=a,denominator_coefficients=(1,2,3),numerator='(x,y,1)',positive_denominators=ds,metric_factor=R))
 expected=['released','released','released','containing_tetrahedron','rank_two','released'];assert [x['corner']['region'] for x in records]==expected
 assert all(not x['mechanics']['weak'] for x in records)
 assert len(records)==6 and sum(x['mechanics']['zero_primitives'] for x in records)==1
 print('K2_SIX_ACTUAL_OWN_COM_RECIPROCAL_CONTROLS_407_NONZERO_ONE_HARMLESS_ZERO_PASS',flush=True)
 return records

def main():
 assert sys.argv[1:] in (['build'],['check']);proof=algebra();records=controls();out=dict(identity='K2_WHOLE_LITERAL_INCIDENCE_CORNER_SPLIT_TRACE_V1',proof=proof,controls=records,source_pin=pin(Path(__file__).read_bytes()),scope='ALL actual realizations of listed incidence: FULL253 impossible, not all orientations110. General released theorem T<16/9 under weak65/54/43; J<=0 gives T<697/360. Unconditional quarter Q undecided; no canonical count changes.')
 data=serial(out);path=HERE/'corner_split_report.json'
 if sys.argv[1]=='check' or path.exists():assert path.read_bytes()==data
 else:path.write_bytes(data)
 print('K2_WHOLE_LITERAL_INCIDENCE_THREE_CASE_PROOF_RECOVERY_PASS',*pin(data),flush=True)
if __name__=='__main__':main()

```
