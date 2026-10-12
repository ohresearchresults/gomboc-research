# minimum-0066

AI research report · 2026-09-16 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# TREE410: все 355 строгих AC-каповых остатков исключены

**Доказано полное непрерывное исключение всех 355 буквальных строгих AC-областей родителя. Остаток внутри назначенного класса — пустой список `[]`.** Четыре новых точных сертификата содержат 545 положительно определённых матричных блоков размера 10×10 и 5 450 положительных ведущих миноров. Их геометрические посылки и матрицы проверены отдельным точным верификатором.

Вместе с ранее доказанным закрытием другой диагонали и её стены это завершает **весь класс из 477 корневых инцидентностей** со следующими свойствами: истинные соседи вершины4 равны `{0,3,5,9}`, их цикл в вершинной фигуре — `(0,3,9,5)`, и `589` не является настоящей максимальной гранью. Везде предполагается буквальное слабое дерево

`p=(0,0,1,2,3,4,0,6,7,8)`.

Регистр TREE410 становится **14 483/24 847 полных исключений, 10 364 оставшихся инцидентностей**. Это не исключение всех деревьев на соответствующих некорневых типах. Полное TREE410, весь срез `(10,17,9)`, `V≥11` и `C≥36` здесь не доказаны. Общие границы **V≥10, F≥9, C≥34**, регистры деревьев **670/49** и **671/48**, а также отдельный совместный регистр **632/52 585** не изменяются. Исходное разграничение регистров соответствует актуальному синтезу журнала.

## 1. Источники и обнаруженное уточнение родителя

Аутентифицированы полные буквальные JSON-конверты, без завершающего перевода строки конверта:

| Родитель | Байты конверта | SHA-256 |
|---|---:|---|
|`minimum-0065`|79020|`527818c9f0336bb95f2b19dc9cd19de7b48ed66ecb57eef669d244958a06a22a`|
|`minimum-0054`|30115|`4e39e8c2a461dc76a76e49153b9f70ace7e0e287cb3fe5e6b3c3733a8c24d774`|

Первая зависимость USED для исходной области355, закрытого BD-капа, истинно-рёберного регистра, проекционных/нормовых неравенств, действительной оценки `d0459/D>8/15` и ковариационной оценки. Самодостаточный 58-source восстановитель прочитан и распакован; при новом построении прочитаны полностью именно использованные исходные модули. Нового холодного запуска всей исторической цепочки не заявляю. Второй родитель сохраняет роль основания глобального `V≥10`; **он не нужен для четырёх новых сертификатов**. Его явно наследуемая universal285-посылка не заменяется новым утверждением.

**Внутреннее расхождение прозы и исходника первого родителя:** фраза «All remaining simple-leaf5 cases have N5=(0,4,9)» слишком широка. Его `driver.py` проверяет это только среди простых листьев в ещё открытом секторе `A59≥0`, а поле `simple5_remaining` специально фильтрует соседей049. По тому же буквальному каталогу и тому же полному регистру14128 получаются:

| Истинные соседи5 в P | Старый полный остаток | Новый полный остаток |
|---|---:|---:|
|`(0,4,9)`|894|894|
|`(4,6,9)`|1121|946|
|`(4,7,9)`|1559|1440|
|`(4,8,9)`|1917|1917|

Все 322 оставшихся простых листа в секторе `A59≥0` действительно имеют соседей049. Например, прежний открытый индекс23 имеет соседей5=`(4,7,9)` и входит в назначенные355. Поэтому это **уточнение формулировки, не откат сертификатов, списка14128 или области355**. Полный точный пересчёт и буквальные грани23 включены в `parent_correction.py`. Из355 новых полных исключений294 имеют простой лист5 уже в P; остальные61 — нет. Нельзя смешивать степень5 в P со степенью5 в Q.

## 2. Новая геометрическая редукция: удалить4, затем5

Пусть P — одно настоящее полноразмерное выпуклое тело с десятью истинными вершинами,17 истинными рёбрами, равномерной объёмной плотностью и собственным центром объёма `cP`. Положим `xi=vi−cP`, `Gij=xiᵀM xj`, `ni=Gii`, `Aij=Gij−ni`, где **одна и та же произвольная SPD-матрица M** используется во всём доказательстве. Предполагаются девять слабых стрелок `Ai,p(i)≥0`. Их равенства разрешены. Для различных вершин

`np(i)−ni = 2Ai,p(i)+‖xp(i)−xi‖²_M > 0`.

Условие `S(P)=1` не использовано: доказательство закрывает более широкий класс, поэтому включает требуемую одновременную моностабильность. Никакая стрелка относительно центра Q или R заранее не предполагается.

После первого удаления `Q=conv{vi:i≠4}` имеет девять настоящих вершин. На рассматриваемом строгом AC-остатке его новые настоящие грани — `039` и `059`, а новое истинное ребро — `09`. Удалённая часть состоит из двух действительных тетраэдров

`K4={0349,0459}`.

**Решающая новая конечная классификация:** вершина5 настоящего Q попадает ровно в три класса:

| Соседи5 в Q | Инцидентности P | Второе удаление |
|---|---:|---|
|`(0,6,9)`|187|угловой тетраэдр0569|
|`(0,7,9)`|130|угловой тетраэдр0579|
|`(0,6,7,9)`, цикл `(0,6,7,9)`|38|два возможных диагональных капа|

Определим **настоящее восьмивершинное тело** `R=conv{vi:i∉{4,5}}`. В последней строке возможны:

`AC5: новые треугольники067,079; удалённые тетраэдры0567,0579`;

`BD5: новые треугольники069,679; удалённые тетраэдры0569,5679`.

BD5 входит в необходимое геометрическое покрытие всех38 инцидентностей. AC5 входит ровно в десять:

`[2563,7440,10493,10503,10513,10515,16511,16520,21572,23178]`.

У этих же десяти комбинаторно совместима общая кофациальная стена0679. У других28 и AC5, и эта стена противоречат сохранённым истинным рёбрам/пересечениям граней. Допустимость в этом конечном покрытии не объявляется доказательством реализации.

Полный список38 четырёхвалентных случаев:

`[38,2563,4259,6114,6192,6194,6196,7440,9051,10106,10108,10493,10503,10513,10515,10820,10832,10838,10959,10961,10963,16511,16520,20467,20482,21229,21572,21698,22173,22229,22236,22239,22241,22243,23178,23269,23322,23324]`.

### Почему это исчерпывает физическую геометрию

Если видимая из удаляемой вершиныv новая грань остатка содержитw, то `vw` — истинное ребро исходного тела. Действительно, нормаль видимой грани строго предпочитаетv, а функционал, строго выделяющийw в исходном теле, строго предпочитаетw. Подходящая положительная комбинация этих функционалов имеет максимум ровно на `conv(v,w)`: для остальных вершин второй функционал даёт строгое неравенство. Поэтому новый видимый кап использует только настоящих соседейv.

Радиальная проекция на вершинную фигуру даёт триангуляцию её выпуклого многоугольника. При степени3 она единственна; при степени4 существуют две диагонали и их общая кофациальная стена. Сохранённые двумерные грани получаются удалениемv из прежних циклов; двухугольники исчезают. Новая видимая опорная плоскость не может слиться с сохранённой: v лежит строго снаружи первой и внутри либо на второй. Сохраняется каждое прежнее истинное ребро, не содержащееv, поскольку его строго выделяющий функционал остаётся выделяющим после удаления вершины.

Все оставшиеся вершины остаются крайними. Q и R полноразмерны: иначе удаляемая вершина была бы вершиной пирамиды, соединённой со всеми остальными вершинами, что несовместимо с указанными степенями3/4.

Именно эти факты, а не перенос старого дерева в старом центре, оправдывают второе удаление. Независимый `finite_audit.py` заново строит все грани Q/R, проверяет кратности рёбер, пересечения граней, Эйлера,3-связность и сохранение истинных рёбер, без вызова родительского перечислителя капов.

## 3. Один набор действительных масс и восемь интегрирований P

Для четырёхмножестваT положим

`dT=|det(vj−vi,vk−vi,vl−vi)|`, `sT=Σi∈T xi`,

`chiT=1T`, `JT=diag(chiT)+chiT chiTᵀ`, `D=6Vol(P)>0`.

Столбцы X — те же десять векторовxi. Каждый новый сертификат использует **ровно восемь разложений одного P**:

`[Pfan0,Pfan4,Pfan9,K4+Qfan0,K4+Qfan3,K4+K5+Rfan0,K4+K5+Rfan3,K4+K5+Rfan9]`.

Числа0,…,7 в поле `apices` записи — номера этих интегрирований, **не новые геометрические вершины**. Все отображения P/Q/R используют исходные метки; корень0 сохраняется. Полный массив отображения вершин/корня — `[0,1,2,3,4,5,6,7,8,9]`.

В каждом интегрированииa действуют точные физические равенства

`ΣT f[a,T]dT=D`,

`X ΣT f[a,T]dT chiT=0`,

`ΣT f[a,T]dT X JT Xᵀ=20D Cov(P)`.

Это не ковариации независимо подобранных тел. Разложения Q и R дополняются настоящими удалёнными кусками до P; тем самым используются именно `cP` и `Cov(P)`.

Для каждого T запись хранит точную битовую маску активных интегрирований. В объединённом сертификате один T может иметь разные допустимые маски у разных инцидентностей, но **у конкретного тела активна ровно его собственная пара `(T,mask)`**. Неактивное в разложениях T не объявляется плоским. В частности, вспомогательные массы с маской0 сохраняются в действительных Cramer-равенствах. Выбранная плоская клетка получает её настоящий нулевой детерминант; неизвестная кофациальность второй диагональной стены не удаляется искусственно из списка выбранных клеток.

### Полные используемые Cramer-строки

Первая строгая AC-геометрия, `U=(0,3,4,5,9)`, имеет строки `(T,пропущенная вершина,gamma)`:

`[(3459,0,1),(0459,3,-1),(0359,4,-1),(0349,5,-1),(0345,9,1)]`.

Для второй четырёхвалентной геометрии, `U=(0,5,6,7,9)`, строки равны

`[(5679,0,1),(0679,5,epsilon),(0579,6,-1),(0569,7,1),(0567,9,-1)]`,

где `epsilon=-1` в AC5 и `epsilon=+1` в BD5. В обоих случаях

`Σ gamma*dT=0`, `Σ gamma*dT*x_missing=0`.

На общей второй стене `d0679=0`, так что обе записи согласованы. Знак0359 в первой таблице соответствует **строгому AC4**, а не старому BD4. Все знаки проверены символически после аффинной нормировки четырёх лучей; сами тождества — разложение определителя по кофакторам однородной матрицы пяти вершин.

В сертификате AC5 скалярная Cramer-строка второй пятёрки буквально совпадает с `volume2_minus7`, то есть с разностью интегрирований `Pfan9` и `K4+K5+Rfan9`. Её точная комбинация по восьми оставленным скалярным строкам — `[0,0,1,0,0,0,0,0]`. Эта дублирующая строка удалена перед уточнённым локатором; **обе векторные Cramer-связи сохранены**. Это фиксированное точное равенство конечных массивов, не предположение о типичном ранге физической реализации.

## 4. Четыре непрерывных сертификата и независимая проверка

| Запись | Полный геометрический сектор | Физические пары `(T,mask)` | Все PD10-блоки | Миноры |
|---|---|---:|---:|---:|
|`double_6_1`|все187 с `NQ(5)=069`|163|165|1650|
|`double_7_1`|все130 с `NQ(5)=079`|148|150|1500|
|`quad5_BD_0`|закрытый BD5-сектор всех38|134|136|1360|
|`quad5_AC_0_reduced`|закрытый AC5-сектор всех10|92|94|940|
|Итого|355 различных инцидентностей|537|545|5450|

Десять последней строки уже входят в38 предпоследней; это покрытие диагональных секторов, не десять дополнительных типов. Два дополнительных блока в каждой записи проверяют положительность множителя ковариационной оценки и положительно определённого матричного множителя массового среза.

Наследуемые входы включают точные десять нормовых строк `(i,j,c,d)`, означающих `c ni−d nj≤0`:

`[(0,9,1,10),(5,0,3,1),(0,5,3,32),(4,0,30,11),(9,0,26,9),(9,5,5,12),(5,9,4,11),(0,4,9,80),(4,0,11,4),(5,0,100,31)]`.

Кроме того, используются14 буквальных симметричных проекционных форм,43 наследуемые отрицательные пары, и обе отрицательные ориентации общих **истинных P-рёбер**, кроме девяти родителей и59/95. Все эти матрицы и пары полностью включены в исходники. Ни новое Q-ребро09, ни диагонали R не получают отрицательную предпосылку как будто это истинные P-рёбра.

Действительные массовая и ковариационная строки:

`8D−15d0459≤0`,

`100000 tr(M Cov(P))−26799 n0≤0`.

В исходнике последней соответствует `5000 JT−26799 E00` на клетках одного полного P-фана. Более сильные строгие родительские оценки используются только через безопасные закрытые строки.

### Почему проверенные матрицы исключают настоящий P

Каждая клеточная матрица B составлена из свободных членов первого момента, разностей объёма/ковариации, скалярных и векторных Cramer-связей, а также неотрицательных множителей перечисленных допустимых неравенств. Массовый срез умножен на отдельную PD-матрицу. Верификаторы доказывают **`B−I10≻0`** для каждого физического блока и положительность обоих вспомогательных множителей.

Подставим один действительный G=`XᵀMX` и один действительный набор dT с его точными масками. Сумма `Σ dT tr(BG)` после сокращения физических тождеств неположительна. С другой стороны, G ненулевой PSD, все активные dT неотрицательны, а полный P-фан содержит положительную массу. Поэтому та же сумма строго положительна. **Сумма различных сгруппированных масс не заменяется на8D**; для строгого противоречия достаточно положительной массы в одном полном фане.

Авторская проверка сравнивает целочисленные ведущие миноры по Барейсу с рациональным LDL. Новый `independent.py` не вызывает ни её сборщик матриц, ни эти два определителя: заново строит матрицы из примитивных внешних произведений, вычисляет точные рациональные дополнения Шура и сравнивает полный поток матриц/миноров. Он также независимо восстанавливает для каждой инцидентности все восемь разложений и точные активные маски.

Проверены27 687 выбранных вхождений клеток и2 903 принудительно плоских вхождения по365 модельным записям четырёх секторов; число365 учитывает повторные десять диагональных областей. Проверены767 вспомогательных вхождений с маской0. Эти счётчики относятся к конкретным разложениям, не к различным геометрическим тетраэдрам.

## 5. Собственные центры Q/R: точные законы, не ошибочное наследование дерева

Для любого из двух настоящих остатков T обозначим удалённые тетраэдры через K, положим

`e=ΣK dK`, `q=D−e>0`,

`W=ΣK dK sK`, `Z=ΣK dK(Σi∈K xi xiᵀ+sK sKᵀ)`.

Тогда в P-центрированных координатах

`cT=−W/(4q)`,

`4q(20D Cov(P)−Z)−5WWᵀ=80q² Cov(T)≻0`.

Для Q берутся ровно0349,0459; для R добавляются соответствующие настоящие клетки K5. Следовательно, сохраняются требуемые

`0<DQ=D−d0349−d0459<7D/15`,

`cQ=−(d0349*s0349+d0459*s0459)/(4DQ)`.

**USED:** настоящие разложения и их общие P-моменты. **Не USED как дополнительное ограничение в четырёх сертификатах:** предположение о слабом дереве у собственного центра Q/R; такого предположения не делалось.

Есть полезное отдельное аналитическое следствие. В R сохраняются семь истинных рёбер со стрелками

`[(1,0),(2,1),(3,2),(6,0),(7,6),(8,7),(9,8)]`.

В метках `[0,1,2,3,6,7,8,9]` это дерево `(0,0,1,2,0,4,5,6)`. В собственном центре R оно не может быть целиком слабым: у его самых глубоких трёх вершин проекционные константы равны `(11+5√5)/64,1/4,1/4`, и их сумма меньше1. Поэтому каждый корневой тетраэдр имел бы строго положительную проекцию суммы вершин, вопреки действительному первому моменту R.

Итак, для хотя бы одной из семи стрелок обязательно

`4q Aij^P+WᵀM(xj−xi)<0`.

Точное равенство слева — `4q Aij^R`, а не старая стрелка в старом центре. При старых слабых P-стрелках это требует `WᵀM(xj−xi)<0` хотя бы на одном ребре. Тем же проекционным аргументом, теперь интегрируя R в старых P-координатах, получаем

`x0ᵀM cR≥((21−5√5)/256)n0>(3/80)n0`.

Это воспроизводимый дополнительный закон реального сдвига центра; он **не нужен для принятия545 блоков**. Таким образом, универсальное9 не применялось незаконно к старому центру Q. Новое полное исключение получено уже из настоящей геометрии второго удаления и общих моментов P.

## 6. Точный остаток и новые строгие59-секторы

Назначенный остаток355 полностью закрыт, включая все13 ранее не закрытых положительных59-секторов. Область13 не была отдельной предпосылкой ни одного из четырёх сертификатов.

Через прежнюю явную инволюцию

`m=[0,6,7,8,9,5,1,2,3,4]`, `m(0)=0`, `m({0,4,5,9})={0,4,5,9}`

получаются13 дополнительных строгих `A59<0` на ещё не полностью закрытых инцидентностях. Полная таблица `исходный индекс → новый закрытый AC-индекс`:

`[(12478,6196),(12484,10108),(12490,10963),(12491,10961),(12499,23324),(13393,22230),(13426,22239),(13427,22236),(13428,22243),(14976,10453),(18001,10803),(18348,10838),(24360,10515)]`.

Если исходное A59≥0, эта инволюция даёт буквальное слабое TREE410 в указанной закрытой области; все остальные отображённые родители — исходные родители. Грани, рёбра и карта корня проверяются по каталогу, а не по псевдониму410.

Таким образом, полный новый глобальный TREE410-остаток10364 разбит на **7404 строгих отрицательных59** и **2960 с ещё открытым сектором A59≥0**. Восстановитель выдаёт все массивы `old_whole`, `new_whole`, `whole`, `remaining`, обе59-части, все477 инцидентностей, обе диагональные карты Q/R и полную инволюцию. Никакой индекс не обозначает ordinal глобального каталога632.

Первые BD4/кофациальные стены уже закрыты родителем; вторые BD5/AC5 и стена0679 закрыты здесь. Слабые механические стены, допустимые равенства норм, выбранные нулевые клетки и любые обусловленности M покрыты точным аргументом. Иные истинные инцидентности вне закрытого477-класса остаются именно указанным остатком, а не объявляются реализуемыми.

## 7. Нерекордная настоящая конструкция и использованные поиски

Сохранено новое точное рациональное **контрольное P/Q/R**, а не мононеустойчивый пример. Это инцидентность23 с буквальными P-гранями

`[012,0134,026,04576,123,23498,2678,459,5789]`.

Полный рациональный генератор `fixture.py` использует треугольник459, гармонические плоские координаты и интегрирование точных скачков градиента. Его17 положительных проводимостей, в лексикографическом порядке истинных рёбер, равны

`[5,10,6,4,4,6,10,5,2,1,2,5,10,6,4,4,6]`.

Все десять координат,210 действительных детерминантов, грани Q/R, собственные центры и ковариации восстановимы без численного оптимизатора. Исчерпывающий точный перебор опорных троек подтверждает действительные оболочки. Их шестикратные объёмы имеют общий знаменатель11742448959723 и числители

`P:4324142140840; Q:2341447349180; R:791988518500`.

Для одной и той же матрицы

`M=[[5,1,2],[1,4,1],[2,1,6]]`

ведущие миноры равны5,19,97. В собственных центрах строгие неустойчивые вершины равны соответственно `[4,5,9]`, `[0,5,9]`, `[0,7,9]`: во всех трёх телах U=3. Девять старых TREE410-стрелок этот P не удовлетворяет; оценки на массу/ковариацию из гипотезы дерева ему не приписываются. Контроль отдельно подтверждает все восемь общих P-интегрирований, оба точных закона новых центров/ковариаций, Cramer-связь и точное скалярное сокращение одного принятого сертификата. Это проверка формул на настоящем теле, не доказательство универсальности из примера.

Пять интегрирований `P0,P4,P9,K4+Q0,K4+K5+R0` не дали точного сертификата на двух простых Q-классах. Добавление ещё одной кофациальной связи при тех же пяти интегрированиях также не закрыло их. Полный восьмиинстансный план закрыл317. У четырёхвалентного AC5 первая переопределённая система не прошла рациональное округление; после удаления указанного точного дубля и уточнения локатора получен принятый94-блочный сертификат. Эти неуспехи не объявлялись физической невозможностью.

Все эти локаторы и их точные входы сохранены. Ранний одноинцидентный сертификат23 является избыточным относительно130-класса, но также восстановим командой `python double_search.py 7 1 23`; его файл32365 байт, SHA `16ffe9d528ad1805e6bc72127c8075f399b9bbfd48043815a0fd552a640dacf6`,41 PD-блок/410 миноров. Он не прибавлен повторно к545. Генератор знаков опорных Cramer-систем тоже сохранён; отсутствие найденного им противоречия не используется как свидетельство реализации.

## 8. Полная воспроизводимость

Ниже один самодостаточный восстановитель **24 полных исходных/входных единиц**. Он не требует исходного sandbox, скачивания коэффициентов или дополнительных material-файлов. Родительские математические леммы явно наследуются от указанного immutable результата; новый модуль не выдаёт себя за повторную проверку всей старой цепи. Все новые модели, точные входы, четыре численных генератора коэффициентов, независимые проверки, списки индексов и настоящая контрольная конструкция содержатся внутри.

Среда наблюдённого построения: **CPython3.13.5**, **NumPy2.3.5**, **SciPy1.17.0**, **OpenBLAS0.3.30/SkylakeX**. `PYTHONHASHSEED=0`; потоки OpenBLAS/OMP/MKL равны1; одновременно не более двух независимых локаторов. Единственная совместительная правка старого перечислителя каталога — снятие его проверки конкретной версии3.12.14; код перечисления не меняется, выходной SHA совпадает с родителем.

Первые три задания: `eps=1e-8,maxouter=16`. Четвёртое: `eps=1e-12,maxouter=18`, положительный порог остановки локатора `1e-6`, удалён только дублирующий скалярный Cramer5. Во всех заданиях70 шагов Ньютона,60 попыток уменьшения шага, `tau=.05*.18**outer`, пробуемые степени округления8,10,12,14. Приняты степени10,10,10,14. Это параметры поиска коэффициентов, не ограничения физического тела.

Сохранить следующий код как `recover_ac355.py`, UTF-8/LF с завершающим LF:

```sh
python -S recover_ac355.py unpack
python recover_ac355.py build
python -S recover_ac355.py check
```

`build` с пустого каталога восстанавливает каталог и все коэффициенты; `check` после построения использует только стандартную библиотеку. Все четыре записи отдельно холодно восстановлены побайтно. Полный итоговый24-source build и отдельный check: **оба выполнены до конечного PASS, все19 выходных pins совпали**.

Ожидаемый конечный маркер:

`TREE410_AC355_COMPLETE_DOUBLE_DELETION_545_PD_BLOCKS_5450_MINORS_RECOVERY_PASS`.

| Объект | Байты | SHA-256 |
|---|---:|---|
|Восстановитель|36604|`3d8f480eda9fa3f59c8f628ec1a6daf7bdd9f3e95a6fe656d9205bd118594101`|
|Распакованный словарь исходников/входов|95282|`25970d60106eb57af8b7dc045d4859d689e90baf54ce4fdf07af31b905377ea7`|
|Манифест24 исходных единиц|2318|`0f58735b61f00a5749d2529030154f37a837d7ed3cc9653565ff34323a59517e`|
|Точный каталог24847|6510775|`8eff923828decf1613e91309baf4f4f7afd240d4dfd7adc5a64354c63bbebe04`|
|Буквальные355 с Q-гранями|153455|`6797a5f16fd54a09f3cec98e8f2fe721c333f969458f2837eee531ae06add374`|
|Сертификат187|129541|`d7abaa55d869245225a3f8af19205068391059c9e581d6e681fa228a1246f1a3`|
|Сертификат130|119350|`0bcfcec3e8c7278c653562d319bcf73642effef59ec467be919fc4b078709d8c`|
|Сертификат38/BD5|109036|`02c1df95ba5e93f54197aa1b222d2109e32f578541b9411b5afccd92caa09776`|
|Сертификат10/AC5|47743|`22ac85415241bca104c6aadcb6b4b092df16df79506600ab9f08e72161612be7`|
|Независимый точный аудит|3885|`d9f42fc2fcf4a1bc53af426645f319e2889acd74d928ff2f6eb5b3c88946d6a0`|
|Независимое конечное покрытие|8173|`1a3174c2dd476f1dac434d835d0eef4b9af2e4cced6f1396eb56123885eb2ca8`|
|Новая полная область/остаток|282316|`3dad44ed0b51ee23d6e25c631c7f56820df45976b6e89b012d04d5df2e5abb81`|
|Полный регистр с отображениями59|7589748|`3babab2a3b7eaa312541125d172cbbb6b5e1bc46d8d68d67fb318f47c37eba06`|
|Настоящий физический контроль|22487|`bc41040bb29174bd57e752292ba238a872498379e15ba3a11bfd6b010ad41d3d`|
|Уточнение простой-листовой формулировки|2509|`552a0a67a402966ba49eb369470a10e3646ce5cdee0844115b0a1b1dac015911`|

Встроенный `expected_outputs.json` содержит полные19 выходных pins, включая все четыре полных входа моделей. Манифест исходников содержит отдельные размеры и SHA всех24 единиц. Все helpers раскрываются восстановителем; вспомогательные файлы ниже не являются единственным источником ни одного результата.

Наиболее полезное продолжение теперь — перенос **двухступенчатого настоящего удаления и общих детерминантных интегрирований** на другие ещё открытые корневые инцидентности; повторный поиск на закрытых355 больше не нужен. В частности,894 области с простым P-листом5 и соседями049 остаются открытыми и не смешиваются с закрытыми простыми листьями настоящего Q.

```python
"""Complete AC355 actual P/Q/R recovery. CPython3.13.5, assertions enabled.
python recover_ac355.py build [directory]
python -S recover_ac355.py check [directory]
python -S recover_ac355.py unpack [directory]
Build: NumPy2.3.5, SciPy1.17.0, OpenBLAS0.3.30/SkylakeX, one BLAS thread.
Two coefficient jobs may run concurrently; all exact checking is standard library.
"""
import base64,hashlib,json,lzma,os,sys,subprocess
from pathlib import Path
assert __debug__ and sys.version_info[:3]==(3,13,5)
RAW_PIN=[95282, '25970d60106eb57af8b7dc045d4859d689e90baf54ce4fdf07af31b905377ea7']
MANIFEST_PIN=[2318, '0f58735b61f00a5749d2529030154f37a837d7ed3cc9653565ff34323a59517e']
PARENTS=[['minimum-0065','527818c9f0336bb95f2b19dc9cd19de7b48ed66ecb57eef669d244958a06a22a'],['minimum-0054','4e39e8c2a461dc76a76e49153b9f70ace7e0e287cb3fe5e6b3c3733a8c24d774']]
PAYLOAD="""
/Td6WFoAAATm1rRGAgAhARwAAAAQz1jM4XQxY5pdAD2IiCcDz/geItsgwbQlwHa2Vjgs2O+L3pY5odz5SGBCZI4Zwtr8BsSLcE5V
c5QpjrNtJ6S4F6geahKiEZCeVltN9PIO/tgFvKa+3G5mqimCcVlo1YX007PYgPSgCjOlhM8yC0Njsu4jlPjw5NwQ46tQsTxflt/M
GiNWAVWAf9/T5pJ754dwrN4Xvhy/LNb6+Q45ycNYX5tQsm8Ztw6/dJH0G7u6caY5WImKOiSy1mNlfJcw60MAGWIoaPFUUZ9G/iIY
C9XTzb4ovpkXfsZ0HI38+AKwhqJ+jGSqljT7YWPej4zag0/dw5xzL4X9/ulJ5z09bu+iS4Ae91IGSU6E+rZ5FKOF8m4qbbWinLVA
icsIr3YSUb+AL8lKxhdRBGD4Hx+qbfNN4ge/9YWkdQIiS707TsZUfwLhPgQD7GFjFq0IWAl9rXS89rEGGSCAizbcF4m9t+sA9yZp
9z66vIkvtDQ8q+UuvmFAtWfXU2GvmWjUnLIoVUE71m/MMh+ZKUIL5bQNyBkv4xUXoh9jJv6xWxHaZW2ZRtS8yshkwt0CaraPIZx6
9y7WidJ0I8hywKHXYMA/fcBp0j77UVwRT5K8Q9MUPZAiURfoF85G+hb3s6iLzHlEZRg8Ht3A9mcRXpBCSDaiBlgTNVuerh5FaYMZ
QEEOxb2agsLoaqWhDXFKOe4j23g5BHkyh4/1pYGBjSYrZP9WPob/WB5dA+u1o1u5hO3JPjCgiaHAJUQ4W2m5rUNJcUJSzDu2xYbT
qSJWXsJ00CCKqWzqCtxoyVkp5UEyUWvK54MEozQsY0ZbKpwVdcdyevYk/BgNKEvz2kRxikUiVSOqyEFjayWF68ly6sMW2W50AGcC
M/igXnkjBl/SzGfpBdN2aokxqTleT01imLuSykUBBQjaafqzmizRihWJhf7Drhz0cAHSnAwm6/KSMZWdmuuniu/3whixNx6QPrTk
lmHdoljY6b/NwzUbw0PxsD8tkgKprqgl/Act5dV4Wxut28aHq28tn+xL3YxaDlbDrX23RfUThWhRu40NAEMfiNBIxLrtRR6DdsgV
zjdlWM+PdUatsfWe6d4Wd2XP7GFR4X7xU/ftACIhmBbBwkvfgXtDe/glUujUr3x1YcyAU9Ta/vjUCG8MhixlaTXBDfeKkjAcONFG
kN7e6in3MZwMeZbfKyB3SPz/RAMnLvGN2GzPYxLM/QWiXOov6pS76pkOAWM4RUCLtYoWvbpEU5tKO2JEbrmshRaOJd+Oz8WIXfv2
sBmnhI7449qzFQlltUgL05z/s5SXY5eghjG4jIEJCTYeEHnVMGMHKd3YhOkOV3hKC8oj0R9BKZBbVuTiRNCvtlkJyqSGixZl8/fj
RQp3wy1jyfixJ4fdf1Q6hZPnURexyNyPda8PE9Sl5AXL6zacQHxjD+XXZhVr20Ic8CdXfJcYCJuGqlLMQzUdd0M4GjTikCOJ/9hP
WCFvdeX2WCh0McyRTh62wwavizp8WC3KNPzc/6MObxpcPzXCg+JrCWeKlqSbv+vTcE0/HaCI8PVhDnPumI7PFW91ClZUJwUp1eQs
2ls09vEY+3c1A5CBhp5C2JZ2078lFVv7DBfrjTPyFEDjjo3YNQkUtGOGlfbyjfrRkZRdKB4FS3eOp+fL2HelzJmH4RmrcSE5AYuB
E/sQFMjt/3NQ5WRIm9+NAbNFNpHY7sQBomHWVbZebai5ZumIjHz6GnoUkN047Q7l4B/+y7VYteGtAztlXS6J9KoGW+XhDBVoT8XN
Ff/SCiE7UweyPmXMESbMNs3QWxz52MH/39ugKpi5ihbEa1oZn9kN79ICvQnww9ZYxK1vSRabcGCgyjWopjUFDuJvncvChvITDM7S
LWxNtdrjFdz4iR/2qcW7DGmUUfnGMWflGu//J9yzs50DeqKeJEWiuhtCV3Qo05mKQIph7nLO7HEhekR3KwyJiOJSVS/FzpKIGCCd
NlPInwI/hA86h2z/WhH73N7Y7apC0jEkqf0kl2mGqBN7WcPob2qPiHk6Y2zsl4UngFcdTZujct5w253yMKbkURVBNbXIqy/Kosap
qTFqefLHM/b9nN7TQnQOIRLlad3TOLWFig/gJDmRZRa+LPG6dC674h9kSsHX4qy5YcL8wa/yMrWPrZoubNZouo1ZmSGWECd1Y0nr
6qGXRvq8Yls1LhoijuriuZ1JAmoLBlWBUDtkcdgFPQWOYB2RDxf1iNhpV6xjYztEzMHSjg6KjZcbNZtspT1us5LhlBpEBZFABpb6
qxzqNmcp3UDvkqS06f/zA0L936ThpA0g0ABhibgD3VvJ0aNRYs3DSbI4j7izECHi5guJojY1qtRyy2GvhFrK3B60Ct4qkHb3EZAT
KmmdVjTIlYVdwyxJe/gqexNCIPfzHZethlAKow454Y9LA2d3IBCBRSjO9CWJYXc61KfXYbeY+Dgd0aARJGqvvvktAUF/vsQa4l9+
cckhswE01zeCG0dHvxTMWcdtjU8sI7lnpzKUrzLc6rITxeih868Z7FT5ZCl18Zystne70KVUOtrTiLGxMsmKSUCUNCeP/VKZnNSu
jlB67UaVzkY5sdrsUaW72mBfQIe/TePcRprzOavzj3eKph9yr4zlVROzdSjvle/94mRbyswkUwaUMUpVOfEKh+R57Eh835n9o7D3
xqqDvVJzpevnfQ1NADk0yHs+BmLFMjigiE0MR3weLDH1NzAZaBL10dyAFmJsdK7jsh0Cr7gJhJQzocMiTq5RbGUptDo0JXXl7cmw
NLvV+3bRCqyjaetGky7FhY+3J4jEJ+fHo6sWViwvkTbyoTqftfw/5KF3hRngB+YTUq1ESnepov0c3O6n1qWcb2HcR4nf5DxjFU0w
kio6nG0XaOty4Q20rkfPbVBlV/NGbCOsgi57ATq0TRIZA7A74Bufy++9q8qnNNUPl/wHy3SneKmuJLOpq5Q84k9hwRmbyu4kqMGX
DYQNTIxIPwjeT2TZUSaGDaMU6qZfV5rWhjcQHwwyAhNazrthi1KD3l+0u1DtKi0gJPxGrcscnNVnaiWe9veNp0KZ8pofH3QwJmJn
wmcWGK6vdnJpFiNg5JIvAWGiwAn/ESfPSAUuNDMB8NCJJQpeD25OvkASVj/VnsAUnZjHme2bNFvWapqR95IijrqH6iiT9/AqNhj4
UDvgCMfFuo4alifnEXSAh/kQ3x6qykkob6QVc89Bl3KvJv2oEg10raZcBxmJtCqFCgcgbKgcmlWU/2+6O3j3uhEYksd/pLdfyDd8
jS5Axv5oLuO+6raEdMDKDbCQJMUrqAUPrHpkFlRbWD66F/cOJ7TBlH4OTxb8Zes9fB3+LbQrj+lfH92htEjH8YHXllWhKroBmgkb
7qVYoPtJs0+Q+LF95nmXawjRF/bPSXlfRB8M+VsrMQZ29Tb/jOEiH3qK/kz1mqwjwIz2fagR3eE6qkZHyqFYxy/qPCR0CU6Tuzci
9RlfFNJ3902zX4bDuxK8n9BEwVbLIdJErS9vV0bABSRofRh9NE6P36wQRKEqh+nQmJtWOh1PC9+gVo8XWW7QBtUXUmFiPDg8LzkZ
skJQku27qbGyZNvPUAN6azNxJV9kUCXNBTk3Lr/MtGsERoWVkkCq8iTHhA2HJ3PmMOuOOZpnEJ1rd/TGbf7ZDhIoZov9pMHoB6Ca
ViojmTratWTr3h2+mbHwWx96lS404I3jO++sEgvx76aHjty1geW10i/ARE0U5x6bCrn+wpq1kTAzFBuUYLMA7N4i1cqJPPH3NVYz
DYKJDc3M/LlZDOC+kRhZBzaX23IEknR/yK8foqg25Xe3mX0ssY8ZGwkGdWxuOA7ZbT2uN6RtR67yUjwg/zmm5bU1xn2eGBJCu9qK
BIi1OB9HOStoU/6fnL0CT0VIlheqmGUhlC/wzpJPcVZoEMrBg9i72wFNpHzRLhLsAEq/HM4+IEtOwGW4hU626wK68I+VsvSbkDbh
bFVt+ZUvOgDwYItVrQrOtLr9SC+fQKyriz0SD50u7BvNMe1+K2363ymyq6/68mlhy3u+5zzt/KOxDAdgHTOg4BBml2KvvX9u+Mlb
4rfc7B0+GbuYtk04Pa+tXWdIQ5LJNdzvej4b82HTA3LOwxlg/+EDg8B3WXjbgebbPOGEulH+TYaML2uJ2pOfalnM1adTgnHHB/64
AsOYNHJfFAMJN+I4NQn2lWi0I6uggoO576ZSiBl+HvcqkO84cRV36xEoN8FBOTJhwYIVqWtsCzYJCBtpMp9dJmK9LrNOIi0rUe03
UqpZGNINGgcoHApY5mFp6w5syOv4rziki9vWbW+BUbh3redw74fY1ttEarhINtSX2JN0aFFcYvEvCtqPv8yBBSAdblvDLT+XEPtK
mElXbsvSYVQGBJTYsl2Rv6rI71V+7ekF/6AYJM7BqIktCxr8QZ/eHzDxI+CeXRH6MrCnRYBXkQOA28PTRDspoP4DI9PJ6zQXVF8x
gLAdjaCCGoSMzE93p6l9L7XDDrs9AEbfmOUCNMEIkpCNRvTFouTK1mlguKKJ/m7AnR/pH4seK/bLSJ1AXvNwdSqEhGfPzETTtPg6
ggsgBmgNCr/spu10T2tmf2kSsZ0n09Qnlh3rwgHvMf5Ja5vxnAmoMHRkRSCbcIIApYD08pO0R5JDTFp1s8h9r2SsEIe731xU0VB9
7aB3bPugj0FZuO/6JGmM0NwukL0/AgT18xyuemfLtymqSKo72oeLJoI4ZCZysa2JfLvJs205a/yHW6k04hXQjlrvkIwfGAg+4b7L
mJ/Jsmq650g7zBdeadQjwp0SsJKkwoquwIBtSG+o3qAWJMcMoEzzt2/Eb3RFjJpJC9iscdraO+M7OlvFg17U/2frK+valFfYXC9R
6AOEcPSstMKuNxXxVd0eL9IGtJGFzQ1sRyVdW3Bjgk5Y+aFZtFa+rp5dvd2T3cX4uzvIRxsYpTC3tUOal2aWMTXHuHIxIZbEzF6U
ZOXQks8+aCKEo32kkXWdRW1Ai0atDJLyfxrhjeTKgO49Fq8Cp4HUcuaYvdA7mY5gpp/tydTJroiCetEq3M++6GySI8VubKy9VTsB
bEIvRbT7J8x+HJiP8P1nHYM0RM2ZnhzITiEJqcGP/Q+uo4SpUUa/3HbCb58cvsswUWYOS9/r72rRXd1saFYWUknh8oy5trrznwjL
XoRHwv9Le4RZ0nEthTE+BPAjg8LSME/2MlatRTkW6Kr1umCUc+gqe7yH/OLHyEkpCoM2P6ATA67gblBrZ0lx6Av4ORGSGUVcZhuh
0Jy9zrnKeEdB5SFJ3MSNUwsUfrwhfKmsrSPSpAXZgBc2TXseGtIjsPGQxOq2aa22eoHb8cOMBKZuZuAKZC7kKEN8dI8w69NX1sQi
kvVfOPwh8NSKaEfIo/Fom7I9tImQ33JEsyQHmTWwvpDy9juaMsHCqknmbCYIqE9mzGYOoS3KSgheh1+y/7p0aZGMtgenvOP7rOu5
kOcWvYnAORWSgof2TDkEImuCCN5hqLkV7UtDqW17IKrKzyf9yadN32cAVBBwwDzQXZP2c+yTX92QW8Vg3a6KYch9gGQ0y9v5Gr4R
ue8Bs4c443bChM3uSxOvzwxUYR6D4n9Mg47cld7omwNCE+8qbKu8CzyPd153CKG8i1frqZGKXAu1DyH7Nnk5nDhWtzlft5ZDgfnn
zy78199NL857kfIShr+hviw+U8yxLqRhsYuLuMP+71T+HAjW4l/8D7SOmrcazY4A+mNY132Na4azFX7cIQS4IBSLwrF7cclJgNjp
NvFjdqiNMBsMRubBKnLUWTr20fM8J5bLHBL/39pO/OHyIF9zWwe0PpeOEPGuB8ClxgQ8CHbFjhDwmLwaNC1+Hyq7tT13KHRAPz+H
ut3jK7ojVzrv6AYmiFzSC3Iiqs4qjtBYE/yrtP5ljKzSpzEdmuRrQxIZQBZhrJAddXF557haa45GWev2rMM7aHkFePKFUOY7Svtf
EOiHQo11yLb4+fS5wkwDp2MOl5pGWDuOJTH39mzPpMoARwKaA0MBEm4N9VPnm4FbAsO2S3Iz9NWvRKt1UtB8wiFCm7WSzx7X4rV8
wbWEvAXyYYOIP9wMSjla4j1vZ19SbHvn1MdNNfJ6Vn1mNsbt4ygBj6L+qio03/rKu9SYqwSCZwrGc1v8KPXfjgr32RGZ2FG4trTJ
j5gdvjS5noUFeXcJGW2iYUUJ5HXlKPpfhwF/NGzsntpFoUX9WtIg4MZool3JXVDGqLIT+JIWeepvP4w6+NmE+XWcB44uq4AZ1JRo
bQ1WlhbiF15SFKoYkf8IEl3gltgpgqjhpK7OJgVnGQD1f4afvkQ4rvY3saGFXfz11EB8FH0sb0m9kAf4xcpBPuF8N1IJR27Saudq
DEn337IcG6lDEYjElGsxSXCi5hiC75nO47+YHQKHNt6FDJEjb2rv61Niir5BbclIYLN6AcjWCtanTvmqb9Eu2ME64Ngvy2zp0qD7
kodhBvVWPu49D33HmlLDo/U5ZzkV8GaFtLYQyq2LoWl0ODR2C58hMxa0QlMtJ3duXNaBA/RWLQ8lNADE13isGKH8qY9KdfyY7/9v
ULSUpeYFcTrlCQdYs6IrrFXgOk5jFYGTGv8b4lfEyvGyqEsZm/fAQanHIqvcVQRF2MKxJDphZ4VSbNtiVIsyFDj0L/h+0njHgefE
i0DMikSVOyDZyw/cRWGRxSbnWNDCb/QyQgj3cQoPGlhA7TOsW3T01yoElp4G+MxVxl/O7hmtXJrc9sy18w8/etEwYCqCs541pBxJ
U9YLVuW5J+lUfJ4iCFS4smKfqPMcddz0MInbOZqfpKg0rhTLoRlH6RUuczGZOzk7Ybf+U/7cvZnb0TgEF2UMkFChOSaVAP1bRPj4
/Jxc2XK0+r1vFFYtn6MnAqbwOk9KF1hiT0WO5ZcETiNfzqQKIrGDZ13o/6ke3ny9Dts1wa72wbosqhZ9KJmqHjC3hdYblFlZ8CKA
1iTgSufWGAcW7NvKKHNX20TPh/AqHHi42etOIyAbDFnZLChnL3zemPfgSch9c3Mha9j3GE8d3t6oaberzB/HHpBtESo0d+s0D01P
KgwO7iOuQ8WGSUpw90lIyrRvHAPytDcGAIqrliA8eWCS/zuIvvR/wdFsW1nrsoP8Lg10CbW0jemPfOLhom80eLgZQNSsRSi/O3T3
k7dP/yy55ahMtd2LRDCKZ/HC9SnOq4fd0yE8OVoQlfHLeXfcVeFHATFi5UTRH6rZgLJ8q7DrqXQHVdD9VxvTkaq1vqThiiKf18Wg
74qKwujN6zLsSsQI+ZqBRYbU737n6SgxcVKUX5/pstaNKUm18pGGFIYe02yRDpL/MTqi4DyDejA8ui9zLXiQhOOy4uPKm8ryYNM+
E9h3HYZmPEPmaoSJ8Vt30ap57yPX2Dvyw4ieIhJKylZh+Cpuj0Gn9bT7snQuIz2oJ8F3W7KeZri8ic5IDcvCy0f77QJ+/2vE2H9c
TvE+mJLznCxEfG/3N7IvePwrQ11vXa6M3346Trl7vlkXkuAJ9NYGvDHDgs/b0gu0wET9pkrETVDKa1BtTW1p1Ip7hzUcZ3VCVxiW
8tOmjlH+08e+p5VvMlJrmty7tXIMteY6NgN04OuiAWqKPkFZrSMhBgAOTk4JtiqJwT74j5p4Qzzg2GybVRELHkeCWmwwUXZc58Fs
cOY9SxFqCjIVRFCz2UaVkdIT/+qvSZ8cdreXRz20ys32nFlLKOHGQbgHr0G20a8bjbGjdU9tVJsB1elITjUvvmOqgSFwbc8wVj4m
QbfcsvT4ddeV9ICQgpz0XxILBIioRVhAqh+UfHovwaYXrTKGLlSXeu5rxAlMqzOdO8DZMS5A5+xM/OpM7nRIJkC7SJXk2L6zBEZd
FbtQpoLaejzCljcEqz0ZhgEQ7NUNI0XyoC6kBj2iTiyBX+D1B2gz1m5RBLosVoFqt5xXP3OV+KO974NhVVVJ5oUjmLslfHalTkru
twvkLj32R0aiX43fMQNdF1Q10sfbSnivOk27k62+gfhMcgdlOucWb32DmhqjeFlaagrN2IeSB2eh5pMpw0NYrrNq23/rHfMkt/0G
hYNkW0SVqqUwSK+33psHFLTW74oUYUnjfjy+pxdnKoTOszA7VxadkkVBV5dL2OW6EaH/m80fzYiI7HHJRWM4+ayQ7pbinH/zL0jT
nTG7pGuNA1nyZL6mRZCJqAzGfeCxQygmAbjmVcox+FJXDxuxlbtTOXPEKRMdcmSJdvJSKRmgFOc/MrsSFHsDqJHG9gB54q//0pjX
OQhJShVSZO2Sp88MALhNxJCB3Gd619VKmLKDcC/iJYaDOdG0svU9wQWHAMYo7pukEuAvx6hqc4EFqEe9pE3ALeHXGm6i/XI/IqHj
biNxVhDj3M5pHqePkJuLpK3TLnvlVwzYaXKUk4cXQWZxzdcdFkPLGpW2rLBW4N0hJdIXOU80yGyLn1JJUIuwRwqm53SOdESB67ie
SAi41xWU+59WPvfZKkpVS7lVJnXp2RybnLWCl/8y8oMW1rClPLFRPuDHei5cqqBXjELrgPbp+wxe1KW/x2zn7ryPrj/N0Ysg9mNd
/dmGYldqXL0FO0hLADP30Fyq4VED+KZxZR81NWxzKj3l//3uiPvFY7lQQ3i+G6/XJa7D4xL05LtO/2mbiTLRpr+sa0AUJlknulwT
J6qWjgCBvKCwS8DAfmEYhv0i1+BBAHdOac0PSGJyH2nKO8hj77RU+3s3DxjnmIbU5B4vExxhISMHSosvBmVsqAzbdsIZsgOsbJzV
p2s05Do3ChizgGY6DTnz7UIrnuC560zd3F14EsVRrw1gRyE6RqadIONy/hcumN8EhJbe4ki/vzQpBNskN8p7XPCh+xCFQUze0qY6
62KfJsi6nRf/dF5U2yftVcs+1XCiPQ6FQycaiPy6axiPSr46kBnVsMmo2G+u+8XlVwexsts5qRpm15ZQkdqUnGZIfSLrZt46BN81
8KRH24bqLiAxGJiOGOMEhvlWnSYjxLnfiRw4UEEo2ol1WXLcVmPr7f3hx60l9KfNe8JIG12ugTkGL2Q7ulhYS1HxPVYek/Ha21RF
N3ZrIz/F8E7DU5uX4M9UfRsqfVBetOc064kdq3yTRFOdVXY5VUS9ZzpwfRZjeh4zmVUbLIL3mLBrVPA7gTDvzQZepgP1Z8FfSXtd
oY9Gh1ktu8ho7yQ0LE5xuvQSiIY6GJNddKedxk9NjqKA7q8IVAf9gmZ/3eVJwV5J2vK2HsvIwqUijOPycA5eF8qtKC6S5sNlI5FF
wc2grI9SGJzvZmmqtiZEDgV7IouOOGdC6S2TfE9eKB1Y58QKdLXVnX8P778HgcTaV+3pwOoIB7b92pg18/N2V2OMCn/kUfysIZv+
WGX3O//wiiDfUwL28m/rr9+BMINV0ePkc4TVVtpcnn2w0SIyQCfkcma0iRhGVXQxgE8+ke7VBGunLwJlW6CmxKtjUSEmjY9P+GK0
63tW7FnAnGSJsGJeeEx+M7w35Yx3FFPsOODx5RVU2YyKfqS/FJ5ikO4hmxTTcjxxEZ9GykWrgIP71DSlGULF+tVQ8V0NFYe0lMZZ
VqiQgW2jKkQtJxncma4nfD4PMzPmCG2t1ypkLQFz8iGT+h7sGvcyaS6YT/yaOc0PzQgy52V7fbtGzMsXRRrrAPHCqnwW5qaCD6xw
os0VziXamGTFfDVZG325ijCEI1ZvwVUgBfpniFUP5EiXpYxLSjmx8GN1qZKZpbPWdaAy7qKR58g2c75deAxK+22uBu7x+3Jv5Ki6
daLHXiJGinZptGT4o/NulpguDREBCUuELE8G6tUWpTDnOFuKwYTmJK0h9HalSnKF1M42tk6duA4L3LtdA8aHkx3kjvXQNYosj8Y/
K5gKGVwRih0o8rlg65ma2oE0xYGd2j8033OXDUDI8tmhPHD5JcW2vbSkGfpNTT8vxs51n2ka0lohIfGvcRP+Wlz29ngC8Ry+hb/q
RsjZJdg/2CTaefjn1Km9DYiMcJMavhqmh8K/5SUUh5iqQwO1VOWKyrr1BwdJoAekjJqIN+S9bSNZA0wGSH162JPulbk5p/xLiU0q
BsT8SJxHeK5O2CSJRkA58l2ec2n7I+kMP+WVqT4H5U/4nxg0OWg5yfntsopt3S2OnDSuCJQGh5EsocUtQdBKbW0XMebxOjeGvtSE
sw8EQjt82IqGcylDE8hZTzvbvjlUH9NS82dg1lWI7NixSVhcc7CYUOIPgsvIdt2YG6xnQKW3ifHiT7oN9XvVtNgsoeUotJ+WF30a
gD4icg7S0JHVOYadt2r9UHmC/o/lMR7iueU3n2u8EBR1etsihjpE8szuyasEHJBaLOazsG3WfmjoquVz+VpmX+50tyfZ+uEvnGgx
lroJKyoTrJNtjd4o8k2krgth4xqnwDxXWMBVIhnx+wtkaBhbjN2s7VK4xmuxNzeNb8i2+szzQKncCtZ5S6/vIfOBRyCyWiZlj67i
MhPxv1n/spKcvAkPv8fe4n4FKjq1ZhUJmAULgZXSHXsa8SrodZomoCVCl7z2v2sisJI9pb3eQtsXLoekqOIcmRCfc+wLDx/H4HhJ
0iMSLowbD7ygV3+xfID1hjA/ZpRUdj5NP6q6J4aXdjDTO2+ADI1GgK+7AvEPmjAraFwqfeRg7DKRhUcp//zD9wTgvtJJw0tSleYs
9xojh1+joKFlyqPBvSxBPU9oyzWyKfIMz4fsY7C4gYpw7DW1aAAJ0VlMhGeyWVDv7KQDJE9XZGHPhvCQ2nVrFpdbZMPkMi+23qy2
drg4HGqyzuFMlXxH+0g+Tv3F52qAgnEDv9ZiempKmdC429UE0evZXmDpX+2LJAluRkRNEQ1D5TmXeVjt4yUJSCn78OrZYdFDYM6c
B2agkMnohAdX/bsjR0vPHee/8gHXtHp/MINoCOaklju6qivKTTba4KvcEppom2lLbnEt//re6m2v3MkVcsq8jWF3d+6YQQ8Aqmbw
nBp5Fe6THOU+7pQGGKu+XpLJ7xcrvuPz6DuGrtOTfaTxgPVa7efTo7eHdCFex1Q/IAw9t0jLcpDf/qvLlP1JXq0VMJfZ5qEw+l6h
7ohn3Ar/ksv5J5NIzWRneADI3cJy0cjWcgBqJUabJEo7yknk2os+Gyh46w9g7vRyOiA2Ho836g19Hg2kqgUGtxISkrUoTMvRMgkY
4A3KmgbKg5LbaR+ACcwSdqVhlA55G3lqMTBqGZCtEmJMuaLnGxkLy4GJFHZI9qDTXs0EXMDyiriOQ3Z37aqSl4mZiHEfNtIGhIMv
9ClpKgb3gQQFLPx8dQaMIdZXyey35MdIWMSY2iXjY8BXBQmFf02TkT8ZTY/R8mnZFmKYPDyLMvIBG9RPERKdi7NEImuRVAQwJbQ4
wQCw414ExqssTdt4Ma2xtMdQKYAzSgIuPOYICUDC7MSmFFFgilFFzMO+CeYTTZfdJ910QaeqsDB/pfJ1fmQycng5J4AFeOB7vFRI
heE2WMmnU9B/6GwyQ0MeZpF6PoNIWw+OHSJzGFWT5DzxprUqvvHlTgf3nO42Wxrk38VU2ekvp9gPmhok5MRMUMYDp6RB9HPdAdOf
wal6OojFA8Z/iZtoo51Oi/4Iv0OjOv7DPM42tQwKU3JHoF3XACOrk2PUzvo6hjKahr+Kt4Q+2rBb4bakf7yGdNS5h3ZTbmprZ0t4
PevH/gIzhZ0KFR7avQ5ZbMOiSlGm3Y/RbIhILgw7NiD1OWF4SaTyTbnT/wnDJZ4rlbosjony2SHvNkHXiliOwca+qMELEKZajLAz
4R96z8I8JWQr5vdsRLeah2hHBBD/RcXC+gwWkCtp6okj6Bp7Ki2tEh3QCp4cR8TUJm2t+J+NDf7ZQ1nBNEAQVP0fdRmM490gwqft
xGtiBumv16QvfKt3dDsQ3Va5yYuHJi7h4+KCHDCDo2qwabm061EFYdTccUiy5QWxOZNefBIP6Uho/EOBaQZkbNi8TO2J6B4vKymF
1XFUUxkoMIRYmLaTFumkdP2w80iMHTUy8qTTmyO0KW4gXDENciykBwUgpsO4/+p56BvvsOoZUCjpCa/yXGwjcVO5am9iOxCisHrt
MjSgxkzBeYqXFwwAPex8Xm13D7EWxG5AfRVw3MC0xYvoOfYktEKdLulWNsK2TDG184FiRTLe+7Sn7fwY1Zm8ybRNWb1yEmvUL/TR
DTpIdQL4XxILgNIl+0b3YRLmXv0UFY2uX0gN4HROrRO2ZF0Dkk8aIS6QxBzzgEj5RS7EMHOjzuOc06YqqBKQ/bPVwIx52cKQOFlP
d8nFrWfbUwj2/pF9Q+zF+QuvqK6edFBRb7PL+U01B6vnRSMHhYES5ZqxfQqpOW8ieab+1GnzI2byWiXCp699ecvemxr22JEESoFV
s8GhInQBsWoOVLjdKhTtSmvq2wvXC6+ia1XOJW50dkSSXGcdFI2Y4gprUAEjxbnbtbQE0e2HWnXizbURqc8jA9Ryso9oOlmuEvMp
xdwIONbCeGimusjJ/aZjLwZ8tXKi16ueHa/o3LQ89og8jAavTESftCZ64F/lh8abs48Fp+p1O3692VrjSo22JLkFZKzcp1B2g2pZ
04zc3rahp8UsKvxi8YFufXZP6i7bM/LY1g09Mhq4kSpmeLI8xveCn+Ad24KBSVucuZwIFl90Dj9G4W+jM6B0HNgmkxWw3i6xKUyc
ympFY6icff+YNvj0nyLp0RhIRs/BcRiyxCvr2iYx5d7TRqVfVfWNjPMCQZwdCki0hB1QUoIJSIkj9yzWnpR1qog1q60ji0wbfsHK
JBuzoAtHQkjcNc9eX0J56DGGO5cMn3X+N8iQXq4Nc++IjtqaKFdA9AxoUn7EQuXX6Hst12PmP7jiqvBEFTQH9EFe8FNCYBg5bxG8
k6lPr64YVhYfZg7aqOgpZJbTYcidIZTGgvlntFoX8hncj/Wb1dFo56T2nA3pKpV0XeCVuLpQyRoWaVsisDFKDEAw8aQT2+vlhLyM
cVIA+drqIbE+MTqmN+a/tRy7GRly6ieo07pxAiZp/EfMzUV4JfFAv1slkARXHhyr4ZX/iHslxjLZ65i7cnGBmO07N2Qgrz/9bBmX
fMmm5OQtuJU1UAlFOjPIsAa7biJ/oGMNgfCm4lxgDUYNXznY6JcBaq3GkuNe95Tb5tpbrnWaiDwu9V5QxszKedZfyjpa0kX22VzQ
w/XJcHV8dWzKLGhoyEndswGd65khrvPeFJ9ciPZssd6l13uJ7dXdn0+rRIXybAWQAQIoIp4P6b8oDTlvXcF8pjn1R1dxi9tWLxb0
WrIKGOeuS6Y51W1NeAG72T48tK7vqvH+3+ySPwMJTao4XTWRb5689TEk0vykUW007Z6OMgG1UIRkfQxMDvLiA0AhFNpuAsoOetdD
x17VH7TnWK1eyx+jXdbxt7ulSyzkrxKRTLOxtZFCKZFb7ttYxn/I1438RjfOM1E5shTRxOPENIobgr7E4Q/qy7MW7AdusOmLzblG
N5QZ3Xx6sNSV5csXgvdSflXonPUo3bf9giufnnEzI2rBjF8WFSUY2FnFpn+Jp3JOkjQaX+W5msi1+Cd6EZQJmpYBb20Jllf3axjA
/mAgKv48TKLZdEuHvzWt21nrRrgW5f+rV47aQlD9CEXu+Nlfi0+zEC9PW9gCtc0KIhIMPw/7IKH1QN653lX7UZWr2MlBZfkMZbXg
qO/BzBG9wpnffGa9FtIJ9mX8L/EUzfxOJ11Xj16XS2dkeI4UYrRcbnjJaunMKJcs4SYZPXSmdl2daBbjNZM/KG5ePmN2t7b4yg18
IFSNMC7HNwpMuWt4eicgXUCex2WipWNDyssMM9vlmVVzwECNJV5ot8urDGeXpj0w8jKLMlL9kUdGneZCD7wbsK/oW5Slg90cssc5
1iDgf5ojrWbA/OpusBLZI5cgjWfDPNqx5CYvyTgzj55rmA1MOfczjqSVWBDqkU7uJCsERYQUo8vr7BClbXFNGXEPIOBlB7tse/hP
rJbXX5zC2VW8IWxx/kzD4RdDCteL7QSWuRNd9DkfkWnZ4cHFM+ns+r7RwKYfw+GB5t8KFIIg0LRqO2pR4hVzgV91I9pWKSsBORWM
KWkrr1AIJha19XePYLx/08FpQtvkFE6PxwlU/Q4eeuPDMxowNjySuvwTb0Ma9pFqPO0c8Gknnd2iDPIEZy24Hx8m4JBxC9ZhcWLy
J5bgiVXlRde5d1bQyXYspPcwbiomsAJRbWApNECQE/I4fZJQja1Nh2Djcw01PsDho1TAh04BAPli/xmh1h/9WnBB3vVOp2G1g6ne
gqKP4ETjaK5OOuKTY7sR43vk9RfAeMeXr1vsL9gvu7bV2926xFb3NjqF/cIWe1LjwJhhZ4W5A2m7B+Jv/NbRhZnzugMbIVJBuFkI
87ORs3ozYA5M27QHGtjAPdaAdGf8MiTpcnYYMu6GVGG+XBBK1gJVHCQkaMydwXcjFqKhotioIDFqgmU+PW1p/7/AKB1roPQJprNl
/Dohz86FGChk6vVlEdoGDxvzE2JeR43PFwPYaT6htlR5tBkLyJJYtbL0H8yPkKKFWEsX3gwwTG6ImqRfjAmE8HpE/IdwsgtF5chN
ZXQnfgyP7Wxb19CzcR8LjhnTz/LUvEluP0UgRxh+9fuj0uiP/JvrLdsi4SvC32/AING4NxOODhZexEKfNrsBMFCl9ZhiqvmODVqg
4XEMZKduRZmugkfNmqtj+9THPQHzA6ig0psMh6pjbOg4Q85eX4J2hkNE8lnYUjWbo3lU/KIihOf77Jb4N1djt+1bMf48fZLYhn3h
0P7pTQpAPhnhc3TyDrYLlE/Y99BrhlvNqFTQ8lXS/urnqS3TMisK4JAExxQlITQ5Z+vvShuj2robBUwxI6nlfkIdMNte1HvRKmEJ
R7X4SyYerBaY+mvd14Ug/O+gqv00ofngnQtOT3fBGJp4hJq1p38Z6GEWm1grJZwoH1MABuuTZamk5/NNV1BQMyW5Nw7fpLJroWLz
TNoNfGp7YBRNj5xjcPXw0sMkh/s2EBGC/RXuw/+w+6BsMnoOHdoRY2ykQ2ojm1hjGjvsH38eVMErnHAHzoCKxs0UMon9t8arGp/h
7wegntb6zgu6FTwAE/u/Vrt41cRW8uGTmsfaKz3PD3wVE51ThRQ9IE7G2Fe9a4IKDo2vJGTBARQyvyIUR4YBhbkUEqNiuTSaB7TS
ODS6Wv+ezr/PcxslB5acdaCW0/Z/j3PaogJ8RO3Lxyo7hIcs86hzglulyRrDkbuMGGMlybgyr7zAkG1Q15F6m9yzB75NLwbGPxRu
4egmY+HP6Ndwiq8lKrOF3s/lx/7mAHj+bfdkZQ/UEHrnQLDLuWYQjYOJxi9+yZKAbKWRELbKHHm4S6xDKj4CqoC4PbnRWCog1SlV
FLjabyISvlPE58sVZZ9dSmRDsLGZHkaLGC9uf760uoXthD0uwUpgGyBZRuYK2Rv5xD2xpN49Xv62l3Uo+pkHS9heMcX02hE6SMJV
BR4SlGY7kPkSmhSoZ6BMf9Ps5CNHulayRYvQ3hBY1pC4y53DoGlN8cp1owPfbt4ZhnKKRWcwQUP3sSuD9PhAj0kY0wzFkrKOkiH0
CHkp4UXO7uaJvXKa4rQ2mFVvS5T8lqrWPPz/yLDIkKgc+ZSmDAz9myzaroJ1PxvHkaMBaQrB3I0bcOJDVWaZGgJQvBAzMOKA7BG7
idfy88Xu6vSPJZo/Rvv+LgYXh6C49/igV6HwaVjDJmHdamygBsYV/OMR1ND1e1RZJbftom0lKTYp2GgnlKSvehStzNJiIwfisKfG
2HrhfsJ0Akv6Yy45RFmgf4Za69n2FCANGZp3FaO2dUFpDYZRQ5aiLDsDEK4CM4DWCpXiAd2QkusX1XriRNgFzLaqCYPvMsM30wV1
mcqIZ+9cef4pXJXj7f14/fEkC+e9O6Kh/15AYNLnGoyaJu8IsQ9U98NQpCWNeAS0s67U7y3RhAGESvpnyC/WlQDRYT1RbMzeqa90
94DNrUx+txfLlnCBPGtruvZRu45xA+LHrWlh5myAEiAqo4wKP19ijjGbDlOsrU4V8GxHL6uSKh4RZS7a1eF0BRbXQ0DiZBvkgIhI
OaA5ix0LR6y4yTeOkzEUZnzcaV4nYRL9TvtmKg1jrazoraqXk99iMewQgYEUrGAL8GlRJ+rqujrk1aZB7myd7Ainwr7V8v0IWKmP
fPeehJsQHkFeYFLhdLocCRHyyUi79wFgm2O1EbfhJxGFSbHdNEYpIulsoqRQNiN1aftm7XLNWj1/eUfMHpBYgmsnyrEGBzNI8bWl
ARMODLGyafhwP15robFmT74ag2HvqUcgeNYGSKZE7ShwrhQWJq+AySewGq6Q/PsmVfAN8KFwV+IYi0BnhWT22G/Rxp+nDVwW6sq3
6I0mKIGlnMdn8xoLRL5ZOmcRFDNbNYp8VUztaIiMjKIa7wfcmt3sS6aHTpvmtPc7EbfHPwtcjovzko3PHY6RAIA6T7Aq8rIPm2ZE
fbXOPufV21LNojeOMCH0JldY4fdA9bsXCCkQYPsG+heys11s/mzOPA88rboVBSPy/9f5NdkCgpYPErJPaXYu0WYu736VpwMlCEsY
w9UWa4yoX6tIlXsJ/9gD57NtVtEyqEg5u6ydgDZ/tt5yvPfU+zNS1XJbR8rYX7z6aBMnYaQA7y8sN9+n2R71gIboLL/SswaAL54a
I1H2d7Tt/A5GnU3IOttmzLF/dRh6YkTDmL+RSj1NhH5bBbN6pkNKGRQiBscMcJb7jYIC+dcUabLLgxCCvhz+S9g+QG0+nE0A2YRT
KiX4zxzL+B5O0izfwUahmpcbzVfax63Igk116YsfFD5oUhRcRcRNR1pfuezNhuBxDqtzwD2BBE1Sn8moXaxjKzSTko0gG3GSUEKR
yOSbgJnePdCw9sYhOI8imJTZuqaWNn3NaQ0TG30LeseWxiGlIH1BPVzKybJo4L84q/W5LFcfIDQiQbKLmnZUAs40fk4deFG7WObw
M7+dtPKIyhQbDIq3d6dHBEJNxSYYx2dV5Mi6zVP58xZrQ6k6XkfoN9JY1PUh49RSHZqzvIRrJ5l96tFqzanWIhqN5DqD8U5FgnO2
nfthXIs6Th6T8OS7Q88GUXflt4QBbyJQBveXdz78dC6pZ5edJvLoYrV4+LtcOEZqWS3GxYYe0CtbnsI9D9kGeoqq93v0rQSXg7g+
E/EohU/SxXGylPV/IKRrjpgvJHcTQJX11lLu+YINXLOUiaQbTF+TGEvU/UVBkIhKaoju0Y629sdCgevmI76rC8vRVr1vBOFVM9A/
JSTKmvFdJ18TJMv++3lFH+slgUkMfnOnPr7PElmZ+qWgn7V/MptpY4+mTJU6RoYRKfk3rIBaoHNODTTDGyMlfViFR0omTVSaWiFk
taskw9lBedvhIkYSkZELKyuwC3WAsse6weBSQPWvTjssfypBC/LDzAxKxePwPAWcpbPWNDKcOiUVbkYur3K9fDaZBBwBZ1jB4zjT
PfIBYywCZeQxbmtEziX5BG85qiN5qzJ2pcKSVHeZZpHcqG+VJWfFVRortkSYyzmOhYsRRhGbAgxBUD2TZf3/8cesW3vmfEeiShiz
9lQfQsz1nP2gUwUdCMA7hBlaGIIe+BIM8cxP/DCyJHc/JObi8n9X7h+3C4s7szS6BrJW9ncZ2xCTeeTn6HnUqoh98H/sy0Ca/70y
+LCOJMRFTciHlBs78UE6oaqFziVKQ6tbKfj5/Ca1QTHSnySo6yeqKB2641yUFJmu6suhaewMYaKnU2JEEBJiEoUpzHqFnZgASFLQ
XE3uZc/Dg/PVL4P96x8d719vdAUWZP5zIEpDFsCYGuWwKCLtbELZZDYTW+Cg6CadpQs5lfIz03ZI1YzbBqSh7WUgUak9olNzG6B5
hJd2xrM1QqzYe3O/eG575SOrd/jHN2CJ/mmtUlC24Lxs+RhpfwCnoqciRX0CUiOALJxXvTD4FNlpEcRMLG5uTz6kIDplxHa+T5Nv
iiIRRyj4lB4zGMvnrpsPIyDb/IdTf+Ps/ODQ3fRlGnRNREmDYBroXHD0InGz68QxbktT+oUwzy/sVPDFDMENKlmzRxx+DCRYSsv3
9mgKuXAXlZF/nC0hnpxqoRKoV2HeDQaR2LwvIVZ/BXcMAC+4K0/i7ZvHGBNFPLDsIde29PF1B6jT5loEU30esP9FaJVmc+SYzxbw
4ECzN2ZXGfWn0G05oPFoIawHhRT5Hm/N3upoS3cMAa2JxEGBZZK/XWHHrWQBcOoG5v0M15wQWAAKqdUhHQIcWiMpU0Mj76pVFN89
jBZvyckBxoLavnKaokF129usj4JqZYaC7pN04q5Hk1aWBqYlDIQNTq0+fKuGYpIRCmnZO2p8GdJ1qDVLbDQFMFszbmIjWV0vuz8Y
tGvaWRNCXPAkptChBlUPzx10Xu82zNHLcdPyYem1tpcy6hh+hVQZeiAAS/z++OKYpTaOQMe6GHFwP44DbZTsq1qqzR+/nsKMxM0D
DF+v5iuo22Saw4vM5FmIGX1xWGIvCFpW16puDK8Jw4IDaEHkGOnzKVc0EpXNmWcwf716rviFiX2xdMnepnkbD73EYZTNJ0QK4HME
2Ia39s3iUi1eQxrAPmGug0HjNs9SHHN9KOE/H8YcZbLALAot/uNFkvR/aH6OcgaxC7tl4q+JbO7yjJonyCHf9pvJkjza0MC9GKR9
AcUJXe1MdtSgx98lsbWG60ZyEVXCQ5wXLqBSAk1hTLomvbesE2/tEssgw8TjKTkooPta14z0VOIH4Nsqdavn+YHRIl7yECoEVKE+
wKQzEVdDFTs44RsKRAaZUiiycJ8XdFBY/iKFaqzal6sApZ4FW/bE7YL+vo2QoQusLhl9mCSOW+DUZk8JNIyFE63n1VcI1DdRgPt7
Oqiqhr9Y5pGDdK8+D5EsDDWzpoJcauaDD/WYOfTmZzrm3sBfOSK8lkhQS+fx9JTvvu/pmS0zHSSFbzKcZE5EaSgkZs31waVKsHfG
g3rxD2n65USZZkPuiUZQ/OrHaiEi525juvwUfBuGm7sE0MZIOTDwiycEri1/oZmd2T/zslWsZjGYuhzXM6yWhOSBzd8hirr75jt+
ovuJua5UspspLVHh72BIEajvmUlpLdreM9Njr0OqBLW7kMMr7oL5i9tT62ZJRiDX3D0ingnsOX9hKbgQZP3Nd1VW4uhJJ36jDErS
eIdSq6ch3hH4lHLsBUaAOQw148H1AnSX4BKO5wDtYAVRFpNJ1cI8jVdczYyh2j2OhOECactuR1YI/kQrcubH/N8ZHlVyrmLSnlfw
2o3YE/vh2evmEpMS5k+Qoj7gNnelSI/r9DB/050pW6mGdukZzZo+oHIhB48c1BD3Ko6JVimqqUosEW6MtJOHRuY0S57yGwDIHaRp
YMCmS7VefDGt2+ijYjWoNe126tY4lfr+NlVSdqQ097xAmq+dTJHBP1RY7NCy4tHoELSYPM9gIy6OVChgEYle3kmoj+iW2yXMFLGx
9wWZNA3XwtWXQPPll3O+i5Na43JxF8MSyW/a6+MS37CisQBauRTp8NxfFWZ9nqS83Y08xtn438Ox+C49cD0srJ6oEKXVdB3NGr/K
juefjvkKpcKrBK1nes9O4uX6lrJS/2nKSdXYARtb9IaVUnbWQe6VUaGSNHB/Vn1QWBJBD9wPpwNdSHVeM1s1F4PXcyY54P4BLMq2
0sAIeS9/sBLpYQRWFqsM9d7bWlL3tTkEF4RLSOq16p+nb8/05PAocB0db0rT/iT6CVekAsIBoxyd53nJi2jAv/TRxTFpDdYCNfCK
7ZOaOKWP1dUw7zV/q2OJVReRNV0QsVKW7itN63db4BHUWtAMt+hDLFy5Tc6FHSR4+oqcmkeoFj+2hcMFx2webeE+1PiDYgbvkwd+
bgFAqmzwMBJARB0k2zV2aDAmFnKg3Zdg12eKFu7jhoQADQnDxND4atDhcPXaA1S8icFSo9bRN1P9pJde3yT4UhO265M1ic+EYdDF
FGKuFElHFjQivtQxVX2VvUOfOGVWne9T1F8dUHh60ljZs1IoVhg0DkOEyglb52Z9gx3zEEjBLfPR52k2jq+Wp6K2+TjLkbbgow9k
9y7QTBZTVbnNNUcZhigSlyS+ek4wyXmsC2gYVH+SWd6mJSIFnQxs20EEqJxlxU3slsj5KKCVsGLZ9+WMaAcUYd7ceBvFvFWz7PmO
UPLlXbK6A5zsTJh/p0F9Ad8SQsqumg6wOdb+fXJV8cePm8FX23L/j/KGnR3hT3k/ObQPF5CwTocx96fTPTmsVJ3VKHEjmGL97Pfc
r3bL5GrBgkY1Z+A4oKbMfEGBf8UWPQRBRmETVBYkJpury7GJnAg68zfnJ/HX5p7eVDcT4PiYJPUF3/iMXhVcCeLohHNmImPARmXH
z6z6JEFuyIr4YNGd+AVOP1xLn1O/DFkcqo3ziuR1iextnoygMPCJDJ85kC/+aCWcvw2qh2WNhLWc0mxXHpAsXQxDuBuOjMg0NhMM
iulrgU0Qu90MQi1lMiilUQ6j/ZA0ZOn//WFG5ztzTNar3CsEpn5Hwz3Fgt1pRqI1J33FWPxBoS9jd2ALQOsm4bvP1FO5vf11tAx8
1b4C/Hf8IZ9IRmcQwJ3k3WAnBo+sHWLpaZlsNrC3yNLIKzdiaPXhnV287YA1g709HOysGbFAZ/zX42Ou8AhQE9w/a6kg5GX+hrzT
6cKRnOn5fpGPxeCH/EFIbSh/+3MZtT4aRT8M9YWLl+AYqmbnBJ3LBu9KEhpoH37A1x1CQxxrculHlBEjODfbOgTQs32wM2NGLVl6
gBh2nTt2h0QkRsehbIbkc2ddRD8L2O6kTybLgMoCaI/4Af5KWxGsy1n060xVMsTVk9genibi9vUrQ30wL8xSyuVkVqLl5W+2EOOS
uchBO0H5zvL4vSkqZZLD+i9tWjLdjjfmNybze5sK6qz7NERYKA+Ns5MTr3g7gBfTJJF33QGZXWeF/Gy5nEpmmlp9LxTa+82UZAmC
piQPfwxPCQnPqD0WsyYGS4Zm50uxqRxzvEyY2O7LXygAZK6xK3qnANguhAFuG6B1efvvbwBm0LYG9kN6LaYogtYBW5A2OMwhvCSD
3Vqz2VUvLD3soqtgyTdXTgV6X/HYmGrZ8pPsenDw4ohdwa08gj59nmvESw7AfNCp9mEzRNJ1m4aI2qfvEZNKT/tkFFtbMoonjBhm
HZbtExf5o7eApeEJeNGuLDkWqwzI3S8cho3mYmyoNoxgslbzSjBCAqd98q/7b6AZrjK3++M8NcwrfA/GvUezcXcmXGuOcHi19CO2
jb1kxo/kj1haSdFZQICtXl9EJGNRg7Cj1sTtZLg2PsaEnR0o+1zGRvSI87CRSUlTGW/sB2rg/8M9cu+VCFz5sFQ3hbxPePDu9q+C
qOjO6/jnEx74fUs1y0FR45GpjQKeMM3XY6vbUQmtc2/JArD2H6gs7D0D2Q5NwKi0+EundeQN88l18M2eRYqkFBXXnuJ+Np82EwSW
FHSUX2rCkQLCSuGuCPqYwVIkstVO4T4A3/iLsdEVQ5uC6s5vY+CHIrEBtkK/jLu7KDL7eX+u5oTtrZ0yqR8RTwDH56vOKY26AIoK
+VeGOHrC6PnP338fwk8a/qv0cl/Te7FKMn9ZH8uLln649JNjFketArKiIm1FwFctYt+BGwDeBz8xCn8jEFU42vI8osXylRlS4Aag
tkOLDc1p5PdrqeE4qbVqlmtTguc5NVBpelP2WsHwWG4dTnxiCDG3sPMGEcJzlwvIdR2c+UcYjF7wFIDiLalxlcB/hSkElqIcYzTR
4rBT4jAwAwXBASZKaYRdlC4dokA/hZBPmdPyeN33nbSx/7DDV5Tx1LwjnweE79zy2xdWhhI/buaxNPN+ANJO2aVIE4pEu3ezkoqs
F+6huBbrc0nKSftZWc3+lMPVhyW903dJNE7DI30T2DZKeiDV2WGzqcLXYZQjE4dJmJ0v+RJEIB3VjR2k4T9/WEyfjbwbfx+vOYJ9
MpafpNFCCx/bS8Jsc52Orp4bAdqMRt0cAKlxbGnLrZRn2HHiOJny3BDGJA8tO09YB0S3Ck5ylIvi04nulQcnyhFenEvcn8Rj2wyV
ZgSHxh1G7I+Av3BqWVR5IRSUbinYRp9m+FjHwYydugeoIFnbclGRbJWt4sUiHhL8dzgbRjeW/YmYXyOvdu2USi4Ii3Fmv41Ea/fj
MFf+b1ygDOMcg9+J3ImTiH/2K2BI3tpcWGI6Llt/p7J14erqg1y93fltjNHr5Zg9eqFuOIV90gr31TV4wfCX5/FrOqZmrqOBCBwx
38Y9PpwayN/rQwSC9SSAwzy0LggIfrW4bSd0gG9Dltv63u1L7JPxCVT84rC2kaZwb2ctxAo5EVr7m8CRg1aKc+3UzxWWFmnoWzLb
u35apotlrZfBhz4+W7kkySeVsZGqRZCdzZYfwfv7cXCPt+hpWKC08E+luTVJl/lxWPX++o0xB8mWKpLQ0/cXsItCCMLbGOzYEsoL
+ZxIDDZKvhCB72PxoJxTSGw4k05AcZ/DQZMpYwXtTQ3cw7KYQ+ECW7LBoPkAIlzkfDe4mE4/A2azWkRx1Z5LWPKUJMh46DE0svcC
lCXNIgR109uvdPvtBA82x7UZA1bhD18CDUztr1c8Nx7rOiOc9BK+iDeFsTQ3d8F8nyg6iHxKWgJowE7y5OlAA+uVFe9HrrNTew2O
fSMa2XwBndiLA2oJ/efq1JS7CqoOOnCxKMf2G/p4TOyXL4xKvn2g1aiy10rvMJdvYaAKXj8dHJ/PYmqwoyxboPDqUqHqPrJ0zFPE
Se9aJ/1dYDqLRjo3gIcQ6ApouT5Dr1N7Raz6j6UTJfqYFW7cnNGXMZVp6+WbwnyEsYP3IRcnVFtU+iyrPY3ahcq77bz1UrBosYJq
baq/Q6dfZgVLBW58MxhLf0F55G5Nl1WAZ1+lhnA2e8ZuxG8xPiq2qKp+9GYbfI+yOSXQQr5e34kKgLY/iEFZkOFZ9nWfrx4ZN/Cf
PIZSqKOgfdmlI1LT6ql0LraQ7VuYPuiua6BTY+N2KZzbO/3+bC11gbIm9Wb2uoXsqrqBoWPEtNOFlwtB00fZjdatTP3Dp5oqsbtJ
uGrZsqKBStVExpUCE8XAlkfzicvcQxH2BGi19z4Qiu+dWh4xijgF4GC1LcEHxXml/FfU6VXfiBuCDlbyK+a4m4s2yA7Lz+Db3XrL
BCV/bjozKO8YadtUP9hjvk+HUguRGAYmLyIWYCXx0rgWo3CbeSb4UU3X+FYTjTHx6ad/2r07lRrTXD2JabasFM042nzCJzuREFj+
Ewo7epTrpRtYnsdgNVvTzVVFpzyuwk2hdxkwAO2XM5vhhJpkCofqAlMQiyhHfzs/0K+crKhIsbWMb5NU7zgynxFD5SoLisefI+DI
fyXbwX4ey+Z0yCi/mag1USrDNdU3ONronKerr7J3cZJXJTS4bZx4ZORSN0CDLShtD8A7eHDOQhtFdwUuGXh7RT3LrI1ixBw0iMmJ
tKK9gZLkBwHPsTgUjLqC2VsCXTnEsxTlGO24e87P09hIUZ/OdUomqDD1UmMvfH1QiBWVqygccKb3FUAWL5U4m76m7WKf98fJZXxv
np3axOqPEVnOaC9lcVq6gGtYq+hy8vr7VnT23mC6KwYwJl6C6dhdocRBjGcHC/vYP982ghhJFfAIVc+RBD/tOfYZN0JUZu9DwPCj
Ocrq8NiIv0FSV4B6mKbLZz6b26oJEBSE5b2IkCg2B8qWpck1TbEoRFJcGg068qM6PXMKLoXq/Lw/iV/Zq8COcN2M8pdgwGZKQmlu
fM8RsrO1t3Fy/geVXFqt8GT0SPGyNeRU+8lUvPo+wlMl8obIrI3FKTi+d+pMgtu06qVYBR0Wmw6DPyogqHDTAv7oJ8H5jgpVPKoy
FIABcBHUgF1yvHLBAw5lLOgVHsHOu8z2QnPQMQFW7jtgTootFfHPvwzULtfwbbsZVWja4ZPG6wg32QI9FDamWIlovekl+KL6XqjU
2/y5kbGzFav8vf8qX6Wfgsr3ckh8jfsmrQd+de/tsEb7qObAww448KUtTlEkmvvNi9dz/QNz89NdKnwz8Q5WdYybuHItdmBuWTfF
Qhk+rOfo3nllI5t4XWwYxL70alHN69Wl6Ng7rQkOlnKQyf8ft4uSgplju92yAdxdu+PjS0eTbzKenY8Hc7wDAURcDXxbfqLjnh68
Cou0HnbSaxtY/2EiOm5wf8ZTmkHAzCoZNHpHpE6P2QjH0t6coMAkD5TuEFsX/gua+nspDG8JokF5IWcfiaSLShtaaphjytncn7yU
cBkhDo8j76tkijyaOUFoaz7hhpQEbGUrYL7NQr2mUkNZjNEi2/2YqfJfMbMOCWrHSuX/P33SDj544zw+4GMHBdu3lrQbjE0l+Vmx
2xy21UWOuQYKuRYVDjHvrN92xobX/hBPYozCvCVdQYJCieV/5rx6j2K/1igeuwOYlQfTS0X8veYEuJmmqaOwI/mFNibshKUi8uzW
/swPYJ34fWOGtjTR0Zimq4IhM/OCcbU4x83yIu3CwX9VFFIALhJGyRXHU0dY2Jhb5nJI6NPlu4Kmp2nxVyCXYcS/WwSdoFv6YyNZ
1350CWHZBg5C5PaBOqmO/FkaxsONFUjFwsO7sA0nXdPb6pPM+cNE5iHg/ePyPt+tS3kBv8E/c6IBoakD/YFVeIge0/sQptgwrnib
gi9RP8eSVd058EU0/YW2tARFILtmLeQ/KOAY+ZNr5Z56Uspc+6+tOtlMUNs0xHobVs4+OF7WxODXf6zPwrcf9+CxmRxq8CeWiYku
xin+oAoykAJvicOW0SZFLF+VGR2EzQRihwdyDcj6PqCNPzfbZsz8ZhGMdqfDgSf8bVUVxkqxRe/2j9XUDCAb5/Eeck0+XMxAJSFD
BcFCtsu0R0A9pJg0pzRINLJ21q5dGCzgwOA7HtmSE724ew/Pk+MSSu9BBGmJcEHXdR/ZxKYJXRWCm7p4Fq8DSxPjJHtDgz2asiJs
0SfDPTb/Y5md5IqEmgscjy+HTaQCU3h6OfKY8Qg1JjLgGEBh1bdZMgPbOpsCqmytBV+SlDYKeucewQSy4JBjcY4BO9zffmPfCGK6
6oCHRz8dVEH5ed+44W3exV5ADh9HeblrBvsb3SPEXi+EkHQ6fcVG0/3Gx3+jqYVmeUCVp9G8ck/xARCI8D3ILlOGljTu/n5wCBYL
cOKQr9mgPGba7XzwNNTnCnrDDjrQHnWjTLPNrtOLLDue/w8orsrhEQw4YxMGQnfg9bOHPpHa0rE/9JeeE2DnQepqqpu8WKD/Tymw
MkFcJwRJu1qsnfSKhWokdJQFhydu17zzSuG4JQA03F2grdbMfXAgfWR6+2YCAPbibxa/adCaVvqlSkPkqiylWGUZNp6COYdcbV6c
3ye2ofkruyvbA2COqms4myGvyEuMe1sFpJzaUvzYSPL8IUutwj6KSdq4EWW8+HtH2FVvf1uV2D6V2/JzyvgX+SVfb1B/A6hNK6cC
IM1spZZmNPpmO61z5aOjlOHkRIc9NxygBDsSVtBMT9u/ryYDymyCjvcl+zJO62IB2nI0LLLajzcD9DLtqv16gZo15+cG8sIJBoGY
kL3h4p9+HBXrDpB8VOd9kTHBKReQsTZmp1b6FVG9ID1CYOP3S4X4lTuSgwplrt7RG6MjA0cxLkaTHhmKjX74of4hydFb9SK7Hs8r
jIIjm0wETyCPHQbTwqxsrG/x7GKQeYcHBhh8vw+LkDT0O+xoYCEeiD67NFj4+zbZ/wA9wpwjCRfWeqAzmlT+3m0jdAFFFRnM2FVM
QPJER1S6mtyRa5aSu/xOU1kYlV5pdGbXOyp2npVibA8kqEYabiXQgdZGkHJcRKmM3yavKEjDi2t1I9laZBiZIOUln9rHAagS3Bhg
c40Xl8JvfEo+HJPzRU8igdo5QAuFzq67p4eFihFFaR2uOLwT/f83k2vSIk8+xa1G8JN4CYjviBM9WLysffSFZRZPle74rYNN0oVE
k1+/ezOobvcKWTvq92MbjGxUpmtq6eFSVRsLuBlO5w6KZY5nNydDQoW6DIiANqepzVNWsUAaZT8PnpXwxCKdH0aa6u35E3gHbh5o
g86jYGQey/uHdrGl0NbV6/xVRcZ72eopsSqCkPQOUtuLpSQwF4+8gzqNtdVfn+To/lM6Z1OBKyyKrI5OKZajrr7PT8Rq0KVCiKTF
2/Df42K5XnJXB2NqXRH2vjCvSk2EmXNT7gTL3Xdc/EcQhwxnTMY8TLtouKgZJrccxHuumzkbYxgOeM1cc47DoEoAi8GFB2SoJBvz
316fPOn8ok7xJ/uHPpJZB3w6Ax4q2Z/WifqieCT3s3Zvw7CaMmtGU7bZPYaepPs2Civ67r35obBB3hN0uLIeltnDZzyir4fw+gPB
Stk79etyzcXfcddfSRO2w7mkb2Z9eqepMvcSiSONOl+BH/R3TvCKNx8Brge7FpA3u2O5cTWO3exeb1BYa66WCaIs3FGrUsuw8laQ
1EoINjpTBP90SoKBjVY37Cr6c6Wb5JCPGAeehnwfdbXXL6SieMeTlm7UbMsGtlAPutiO2BcJkezvW9PMWj8NWAVikxCn9ZnCY926
CqC//DYuEeOk4j+Xs6D1bTAR5TTa5MVepH1PDtZJ5dKdyqSgf/OuTAVT7tXf6DtaBq1ZoLT3mwvpZ9DxmC/nzWNaZrfvSvXdtoZZ
1E+zOV1H97fB71QWTVaNZ++VimCix/JSpU0DYSrW7o/v6QSnK4cG1TKkrVyt5+h0+BTjDvnz9pPmDTkMh+G0YrRxhVB9jX3Cqd87
Dp4N0liTbwxtXQ4Clgu90kwDOGd/Bo4a+MRrt2tN3HdxDWnhEIYE5QvhrBk94zT2UGSTS3PazxUDsTxB4zhkUYO8xxai3xQfiujU
3RTi7RoyevVxodQIODTArT4qHCVa6n/OJXrjJKsuMvI1GxQmEGZUWBUqI3xs1j+d2nuBV/+tV4k2rsExEzIINT6gXB4hrTYJiat6
KBb8c8vr4Wo1yOETdKp07rUDlpGKPwedXE0dicVF42MNPiu0n+sp1P/ATH+WQOvu7eA58JUiimjH0Nzb1A1rfjQfCgwSaQ1rYi4w
uHEd8LGBj1fzyu3FOnwQPTvcQxb6HJSc09Oq3gluSvXzKwrwJBF6iaoR53lJ/A1+W0a1+1qZJ33OozSO9a/h/HI+yTOzqxYgbtRt
yNO3J/NNsBF1+jZG5SVQMmi5B65OMjJrS74e3QpD5UqSObIAerLo8EFuHmnjPkdM+ayK7/NnX74DSaVLFzDQTI2R8RG6Tp7ckDXp
tOK06k9vRUsCxPspWu+sIIeF9hw0G4+2ZEj+wESSGBo1lwRzD808eOFRjo06BVt2V4G9/CW5yh/YH1yaUi8pEncW3D9vpF9HXuG/
gxfX9XKNK/VxakD5mdJA71wmFEKHSAAfiJQqJ/RF18YT3NTcV+32GQ+jVOO+OAyx3pY+SqPzMII+gAPR97bLwp2R7ByqrOR1IYK4
PQnk7pPPYqZ8Eafhh6lCZpcmP8sJ82KRYqg80kYi9B1QfSdwn5Iaw/7GwmEu6kSZXQLth6FTBnK6gXDOgk2cUZFs8qMF6rcXBIxs
xrixOLPmffrulGPespkCKGi1Qop7huFV8OV2lFR/bAT+2/4d7wjRboRWPWVIryHW8kBtOha7E51T+BWnKqxVLbhXU694b4MVD8SX
IPuhACzWranO0KyKIO7PUFldEmaoTWhgEpgl2TKNJIxg8aAXuuojzIdifL6Pfc/RLSxUY9tVdNDOdL54XB0lF5J7uy50FW4aAZdR
OpJk2h0blPT7vOvJNpfft1Rpof5nznecBl5rjJYyKWj0hqcyRc3TNFWDoKJs6MK7PbjYLhhM9Zg3/AYtpuSPyDL9l2UU9W8CQaZm
u7EocoK4Ws53KQo9EOOyTA/jw2Ig9Fog7b/uNHKJh07/AsNat/51AUYIn/82w1FV0PHq/wsjf3NOGU7b7waXfI+mhziwQVI9MI7y
8uFXkZc5xBYZgYSVUl71aXfNCnvfFXEj8zUzoVn0XdAtAFfaK+3V5oU4Vuo8CgVg/dx4QoGoqPZsL6p8oO3wPjmxl3pvRXJp7D0H
7lZJmHmn0J8DB63zjbmVboKKdQFeR0ITOcJPYK3DiYY2C9qMYvt9cFI+cIi3WZu7OXF6qYh/a31gma8QY4eabrad+fqGNk4LtH/F
uahE30+QCapObaKDub8qrbr3qZvz7uTc+WYyMd0pfjI+HjpHzyTWl5JYYv94RBecA+3J6BUhfLPRmrWDzeo9mUPSTKiu23aHLliF
0YDlHm9q6Pr1bgeu46URYPGe7QT7MpnOVfKisKvPJOEJfp1U18In32wNUJibvy/ireAL79Cx/7VKkdYqa68lFQN9m+vXz+OWmGkj
hhfKFERkPOVPwjNGjP1zKKnv61mOICyx64km4UvxG89iX7vcIm2zkRSmrcRAqjrNgiSXvN0xyxiQ3MdDxMeXrF3KTd2AU+jI3LVs
9Z3ThCRhzceOVSgSH7vwZTaF4r61qTfYjqK41DHVYpKxiryE4jarQVYyjvpA+0sd/IUpxDjqUm1OYUVQqgZjxLc5Ozh8vOjFqJBq
3I9U8PaHH08h0AzwuS8FosJhPeEy3jcr26WDbAzV1rldN+1w8oOhScOeTk1B/NCI+OG+cukgM5i5lfZqHw915TUlogXI99/yI9Xl
Ilgi/W2L19TJJl0Lfafr9nYYgEkgD3K3aAaZm0az4tL5KTGJooD+CGoqIgykXAsUy5qq7kQhxHbYSlQ14tYfSmeAHV0PLJN0ifHD
Voby9EVbaQburfmZgDyjLJUz9oXgsp5T2k1aaTLhBtxEisz+EVpHZcbZBNZB0KX67ofMbPHkKJI9iH7PaZgsgOIYxZASODlBzVJa
1bNG6ej2m1Rlwv0UvtwCi+21QR+2rqIVuwd9KI/xKEoWiVW9cYynQkDAyTguc2+3FZZiJ5yHy3qyI69TUN9JmZQ+a6otWTAgsrz4
FSQGICZ8dzvU0iNdl/7Gz7tJ1SSWmtbOyTJDEOJ8HLl1+leMtYyYkyc0GTqk0uwZ2MZ+JGWqVKVSGw+D2vucEwGe0nglWNjABYkh
D/rhU+oX0RAC7IxUDn8Ucag2VtzUTEM+L+xxaGkQ2pTciFur9L6W47hlI1od3rRGNVvsGnJZFZ4xvF+nC6LmDsQr32WruvDs+/s2
+HEag9VCCeBg6nB74tP1tbPKP0rnIBO0U4d+V4+iKLdpfE1o3cP36ZNyvFLOqOQ+TkhlXBJttgHxoD7zjsHkQIgPQecyTbkwZsgJ
LNdlUNGI2rPKSPP5jNc45b8XW9AWqImz+CX0kVuykoO4OX5MPt9P5/E74+Bl/0lvtr3S7fQ7fgren6TpN+zPrv4P6xhHRYpHsmOa
3XZjZFZJDfWdM1iDBvBtv42rs9XuY3VaIyTs03C8QqMVyPCv79HUH3QsEJsdHAvMrIh02Nw+lU7ql9GiAjUF3kyHIcNObeCoCdba
jTm7I08ZIkbO1qM8h1NKIGXqZRA2ymy5A1j9GZ1oM9RUmQO3MHub0C1DKiKItJcmVGhD/yvriTYYaxYn4lqJKeIuS914h+EqpNEA
EE8UcE3gBV/miUUR3IJHCMYJfDieREQ9gusGL3uiyzYiXuRCEV/xxNqz6xS9MK3lDZJyv+snJPbiedYYDLM1ify18oSPJ+0Wf95u
uFZSiLCCY8ivY0E9YnGuxP+o0IfkAJnImrJ522CsskHMQ4XwIpKq/cfMvpx5l6KXMYjS9PcIGnUlpnbJN3TIbGbL2kEf04ZI1wnC
8tPj++4yx4ZoAxODsnYxH6AOPYNyynZdHC0gE4JA1lLGGpmR1MjmkPaIHLDKpH8FDNBRFUFZdT40k+COJxPhYTOZvc010cDp6w8b
g8eoXs3lmVXt37Rcb3Jn2KYAPsOTY1fFe+iB512h7awNXcvPowTk9oSX9TJMudGng0kOvMIW6Fce5Fp+3VQedHqGA+i4+4ns6pIW
/cIVnoYl2bY6t4KiHpLuq4lfRD6nmrju52kfcvJMyE7foskUcyuQPTuU69w1Qc+9bkcCOPn4A72gy59+VvYEjgYpQGfGAJjiIEu0
q169wBsja02vT7U+0Ulb4TTK0eKMssQe25tXtKolRJ0qGZB/CUMfSNAWUNCah3X8x8PSjiZZJtNe39ae72S4zOOgvZdZVi4TAGpS
n+WXYbfFTCDW+aocg5yctBaOgsRGlTFI0c4fKjnVLaVIgitqipd+KJEGUlJBZZNEHc+XBrfGWF/qpKKaxrDWDhuoANRF+f+DQ4la
1W6DuW4ZiOdvUJCOfNCrLNtv0o5TTdR3imHNow6vhl7ORCXPYJFCHbL8Fwe0nFzQWGxzivrRq/X99EcXtri4qFCe9e+iQvqUCcF2
zix1M6icZ6U2I+YcO6IhADA8f/PO+zkgLRMciJFNUYZ5mrNkfpFk/PlqXgg79rtbMibrx2N0scsVkrGkntuPc6e8EO+SQhceI1WX
sN1sePSshFAcElojw1neDo5GKHS5AGgXz1jQnbZQrnaLU3FPXrxWs9tS4k/cD/LNrJ0KSY3oe8w4U8TNseiWpnhdnyQofMH+UdKM
fV3pXL3uki7GLtSm3RFzEIZjsjO8alrmjVxc2wg6kjJ4hR2s6PvlfSSkGhtMtdL7H/RUHU2oa/UST7tYhcGkkM6EiVESEDytD5Yb
Ji3wiQMmiFl3OFdjEs8xsk4Pfs5KC+1RonvlOryEZQiMphiRjq2tIhI5t6edd14h8RSmvjLSZ3507dot84XF58hW/fy/fRSzTQIC
1086c6mYd42m0oo07I76TiYVDk1XAFjUNHVFFjO76AJW+SUFNSuPo5yp3mJhHvvvHuRUPw+TxH5jrQjCBLjvDYsrR3sh7gaNX+6l
36svXhFfcPAH3p0TI2N9qcQp9GqprkqcGf1+lkfIZEFIA+R80F7oMzpp7Kod3cootL4lzfiTDxmDDuPvuuMymmgniFASgcQvgsLd
uyjXzH/Tyhu0Am6DcO7nF9Vag9qM8z1KF/m/4Ey/CtstFXw9/hqA61EGd39ycuBmYnKc4t9xGVzIwBeQQvRcO+lWCrYjPdeArVTm
bjHkCfER1Zd5rsunRZCjbPmZaXw+V/tTm27OgOVgY6CE+eYLlIxp0PqeUQunkBYKkIiqzGTKo5Cn3kvKHgOy81NsdUPB7yTw6A7g
72VzyM+83opsNwAGTVn6kfmp9oK6wFYaT20lZTqYVjlxJxJrbV6n0VGCQGYJN4lc1A2JcUjH1iOIs8CHieHRIj+SG3GQH1zZOPcE
uuIGipBJfl8RUzIdIhOfk3i+8ywEFB4Po42C5/bpiyKaZOKS79EtLzxBoFNvKp9YnE8+qAV9haobZKKa5W7zs0uYQjMc5sTyWXpN
j8dqcmxzKoOEXVJEcnGi2Y/QFXC1cD6b5VMWZbgwWVPBABxEMobbxH+N0mkLF69eWH8UAfhJSLUhX1gms85pyfMAAkwCWtStZnmH
QSNWjHk+Oo+15ZEMZa1vN3C6tmMk+FwL2i+22mv//HI2RKaxGbZwyDgM4rJy73JARQFnN3omztY2BO/ZzhvmE+JFRMyafES4qxmf
R0kDHoiOikoyj3VE2IOP3DEoxZa5JP1WfoZRrzm+Sk7LK1zV98Xpv/AKwWXaV9Fc9RalQHHj6ljtkQwzhVzzjEiWmDgD5aQy/FyP
awnzDn5yyQs8IlQ17IxSfXQRr9JxPSRrC/YiOs5efYOpPTDFOr7ZwhCj0JNsDeVXZzdHrAJoLvF+Q/qifMZs3EEc/TLwgdc+dECv
ScsrrrMY2luGAFdZt3J5LGyVokzRJyGavDyIWBzh7FpRrwvUnCqCW5ol8ZsyUm7175cUxcnS8e5cs7ptIspc4wF9xLFaTf9uEmXX
9H4rDL2Yz+ZYZHysfqQ3SrLjMCLHm6acFxL8Pw9nn0gre9TGgnzErVuGvChnMoigWK0JG0y5tM3hPdvs+Nqd4Qh8wY7PX6kCS+uu
E2ms8GJTaL03aGuUr9rsVSWhK0I4hOwbE7/YAMKQ/U3zfbXpj0syoZJMDj0V2wo/kfY8eyb8Be06OVaf3/3lOe76Y0AV2SDO0kQx
hNxE3b4a1pbdPziw1ceVpLpB1JDZHG7WfF7kAAjmx6mRHV3sfpFSx8PjyidUvLuWj1K+S3qVoheNgwOB2oTacBf/7AHxJM2wQuPm
1FgXxAF4ZUrwGRuwBJ0LLWCPJj4WQmMF+wZ4g3IA0Xl5jleGQeWUYMOMfgNSfo0CQsObo7gbaW9/MEYAd0xZQIs3r+FaCxuuvIEC
k1VNt97IGSuV3tNa6xxYmnlk4pVHt7oD3CxfzamYSr9oDfVeybhuCCpFsWtnJd5+t+BIMfhNm9Womwtop4hDhLObkAz6iTBk6ibb
lpPzUuTELAXjXixs6uMIullJ4Nn+pb+HQ5zdzf37KibKdoLhTINN8y1R8JlCAjDUK5RAE8hYxc7TqSSx0bwP0g/VHtiwpJ+/NkhY
nS2IuaBKZBFytzZF/li56d0J/YEgtamRGZKNJqCZlhpKkBElwJTHpVlJG0HhSscAZ8XutJh5OYpDSjLd7szvkl1Xl9Z8vZDpd/Oe
l3C0YuDctJKaoMNARYx1uhA7U78fe2mk4s06r+jcElSZ101ebpYHsINraTggidRUyhvg2K47+pV2yS1zE3Af/B1B5pow93EyuLvW
7SE7rfrSA82fWBl/PbV5nOZoEpsqouUahlX46XreL0QVapjuqFmdmFsV3WSAq8AxEuhafy+brz4xrt/hg31hvQIP31Ajgkmr5ORT
AHhSNwdcAM0JY4E5AY7gSb2wsAww4LwBxmhZvYrzvIki5tjwUvbqQ+G+CCZzQF9FUWx142XA5oZnKQrLn/UhXDuWhAG60O79vkhy
YBSNiLPr39StL6lGrOjcCCDLSGlomxOawc3CC+M67boVh5Z+VR9h3rJDzK5w4+tlVyZG7ZAnQgvd1TBeze1+3ar5QNrS9ovhVK2f
cvWd7ypPWGubEXRkW5UNOdRr3+0+h9R7c5tUo8ner8MqwcrvJcrKz16rirykopFFSf91vit5hVwuI63HH8eSZ+J+ElGGJEexvkhS
7+1HlmXffXiVHaXu94dzLtlijFZhhlXk/yrSGoti6aKJHLjgIbtsp64Z3a6jjVbjJlXT25xnoy40PxDr5dwHSc15Y74o3xAbHsdG
sEUQ0rTelSbm9VLkMurDbP+2H8HXIXvmbyxueKEsYG7G8K97bp/yD9xdMFnzGBjhBcARiV9SKtICK74WGMOnpDV8M9fNuTqLBsyF
w4lUjj67HYU0iRszCHWEFw1JTu3Pr2vbIdeCY1C575KMJADlhht6RZFbkfiS6A5fObmTFg64tV7ZDWcSKogB60l2CCj7mtwt9orh
0JWdx7WLbitephhpmlSZG8LbxzcRPhzs1p1VcBrv3DJmhmw3lCrIZelcZA05GvRe9t3xE3iN076LjldQ4h/w2PniVd1AxNJHENpd
UguxWZmIx7lk1qiMpDx0R5eiWjixpEUhy7L/MXMkF00PLFuRbfqmHSShEcRG+SVWz8quYFra9QPnX3uLStftdWRnhV4zAcWiV1tl
ipcxQeCFvk4gmPoTYiRIMc4VZeZz8fUnLJHDcBoIyXfQpKbitF5n76i9v77HYXq+qEAKz47WcEyFkkURTwGunVrcqtRSmFIL0YVr
Zy0eptvgxyz1jbFqX+Yx3S4diEt/QNCU2gyipcNVIkMj6VQl7Iub08v38Ddcn4VC4lKz8xn/I9zQnsPUPmnuiYi0Kv2dOFegvJim
k8PcanqHgV4eVANw0mAxu5Re3aim/G6INjnAqZSC410psdhpDG6Ddhr6gZUyyc2nUc7nhmfeRvXKQFKh1Hn2pIqcxQmSRxdrv7xr
fOPMMpcWtgOy+q10OMrfOY4eUeyU6OnP4fQVik2gos2FXc46B51I/YaIEQ0UTttNPE7AfVcJEskpdvUsfKi6S3JygdBhSJVb7QOk
5G4lsnE6iN3jiKYkC1iB20y0Q7F4+vMKnlWyAAAAAAAOWFcRxSg4VAABtscBsugFDtBYzLHEZ/sCAAAAAARZWg==
"""
def enc(x):return(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def pin(b):return[len(b),hashlib.sha256(b).hexdigest()]
raw=lzma.decompress(base64.b64decode(''.join(PAYLOAD.split()),validate=True));assert pin(raw)==RAW_PIN
files=json.loads(raw);assert len(files)==24
mode=sys.argv[1]if len(sys.argv)>1 else'unpack';assert mode in('unpack','build','check')
root=Path(sys.argv[2]if len(sys.argv)>2 else'ac355_recovered').resolve();root.mkdir(parents=True,exist_ok=True)
for name,s in sorted(files.items()):
 p=Path(name);assert not p.is_absolute()and'..'not in p.parts
 target=root/p;target.parent.mkdir(parents=True,exist_ok=True);b=s.encode()
 if target.exists():assert target.read_bytes()==b,('SOURCE_MISMATCH',name)
 target.write_bytes(b)
manifest=enc({n:pin(s.encode())for n,s in sorted(files.items())});assert pin(manifest)==MANIFEST_PIN
(root/'source_manifest.json').write_bytes(manifest)
print('AC355_COMPLETE_24_SOURCE_AND_INPUT_UNITS_UNPACKED',RAW_PIN,MANIFEST_PIN,flush=True)
if mode!='unpack':
 env=dict(os.environ,PYTHONHASHSEED='0',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',OPENBLAS_CORETYPE='SkylakeX')
 subprocess.run([sys.executable]+([]if mode=='build'else['-S'])+[str(root/'driver.py'),mode],cwd=root,env=env,check=True)
```

Копии для удобства: исходный восстановитель (`recover_ac355.py`), полный Markdown-handoff (`ac355_handoff.md`), исходники, точные выходы и протоколы (`ac355_support.zip`).
