# minimum-0090

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. [C622](../../C622/README.md) passes the supplied exact checks. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# TWO_APEX_MAX_ENDPOINT_FULL67_FAN85_V1

## 1. Итог

**Все выбранные полные базовые замыкания степеней 6 и 7 на E17 исключены.** Новый результат не возвращается к уже закрытому xz-сектору. Доказательство использует вынужденный конец **b=y**, настоящий объёмный fan из x и один общий разделяющий линейный функционал для каждого из 11 точно перечисленных случаев. Не нужны ограничение condition number, оценка 497, угловая оптимизация или ковариационная оценка произведения.

**Теорема.** Пусть P — полноразмерный выпуклый трёхмерный многогранник постоянной объёмной плотности, начало — его собственный объёмный центроид, (V,E,F)=(10,17,9), а настоящая максимальная грань B содержит все вершины, кроме x,z. Используются одна M>0 и именно N=M^{-1}. Не существует выбранной дополняющей пары слабых настоящих первичного и двойственного деревьев с первичным корнем x вне B, степенью x равной 6 или 7 и выбранной последовательностью

B -> L0 -> L1 -> ... -> L_(d-1),

где перечислены все d настоящих граней при x в циклическом порядке и замыкающее ребро имеет базовый конец.

Нулевые выбранные стрелки разрешены. Отсутствие дополнительных слабых resting packets не требуется: условный запрет действует уже для слабой пары. Для целевой строгой 110/weak000-механики существование положительной дополняющей пары остаётся входом из literal H0-parent, а не следствием нового комбинаторного подсчёта.

Получены **11 целочисленных сертификатов, 85 положительно определённых матриц 10×10 и 850 положительных ведущих миноров**. С явным отражением они исключают 22 первичные маски без какого-либо условия на второе дерево. Остальные необходимые случаи закрывает непрерывная лемма о треугольной устойчивой конечной грани.

Совместно с прежними результатами это закрывает весь выбранный мотив B -> полная ориентированная звезда внешнего корня на E17 с восьмивершинной базой. Закрытие степеней 4/5 и всех выбранных xz-замыканий — **унаследованные**, не новые части этого следствия. Степень 3 невозможна уже потому, что два последовательных угла слабой полярной цепи строго меньше π/2, тогда как их сумма должна превышать π. Новая работа не исключает весь E17, все root-degree1-конфигурации или все двухапексные тела. Общая принятая граница остаётся **34 <= C_min <= 622**; нового 110-тела и точного минимума нет.

## 2. Источники, идентичности и предел аудита

Весь входной пакет доступен: research-journal(20260919-054045).md, 253671 байт, SHA-256 **49772ee9a3005f9e27d2dd1db9a01af74cd2ed6998d774c585b55d92ecf80360**, включая оба полных literal-parent, и все шесть отдельных материалов прочитаны до EOF. Обязательного недостающего источника нет.

Literal **minimum-0086**, заявленный SHA **8123315ee22b6a0fc370e8f672f299bc19997f89ad023530404946c77f994f10**, сохраняет своё название TWO_APEX_FACET_CLOSING_512_V1 и свой тип **ROOF8_3_5 с внешними степенями 4/6**. Его извлечённый source имеет 14264 байта и SHA d5c213cd025888ecd8f7752dc21b0486bef1fbfc13ade07c0e1a55799d8daf3b, что проверено. Это не balanced5/5.

Literal **minimum-0087**, заявленный SHA **b77264d597b32a5f97ac011c57d4c95e7581fb2d81d202e2bc477b0e6fc867f5**, сохраняет H0_GLOBAL_NERVE129_AND_WEAK_PACKETS_V1. Его полная сжатая капсула извлечена; проверены recover_h0.py, 12390 байт, SHA faf5779856fbd7b3fb0b20aefb2ab4b8f282b98c7b5b0fc41baf4376dd5cfce8, и развёрнутый source, 25506 байт, SHA a939a2de501576029c9bb7f86bfa28d4e83a28b50d8c42104369a08ac2a578df. Развёрнутый source также прочитан целиком. Старый большой H0-аудит повторно не запускался.

Все шесть отдельных файлов совпали с pins пакета. Обе обязательные поправки сохранены: stdout ROOT_LEAF имеет **283**, не 305 байт; covariance-доказательство support497 использует отмену 2b²+2b E_cells(s)=0 **после** настоящего объёмного усреднения. Другого конфликта literal-parent с используемой идентичностью не найдено.

Первичная формула Бервалда дополнительно проверена в Langharst–Putterman, equation (1), но новое исключение ниже на неё не опирается. Поэтому его конечная доказательная цепь не требует заново воспроизводить ковариационную часть 512/497.

## 3. Новый геометрический шаг: треугольный конец невозможен

В единой евклидовой нормировке слабая стрелка v->w даёт

|w|²-|v|² = 2v·(w-v)+|w-v|² > 0.

Полная выбранная двойственная цепь содержит d-1 рёбер цикла при x. Дополнительность деревьев оставляет ровно одно первичное ребро при x. В рассматриваемом базовом замыкании это xb, причём b — единственный первичный ребёнок x. ROOT_LEAF дополнительно устанавливает, что b — единственный максимум нормы среди некорневых вершин, и именно в этом выбранном контексте b=y, L0·b=L_(d-1)·b=1, z->w с w в B. Эти данные не переносятся на произвольную available-arrow цепь.

У каждой базовой вершины в данном E17-комплексе ровно одна апексная спица и две базовые стороны. Стрелка B->L0 использует одну из двух базовых сторон при b и отдаёт её двойственному дереву. Другая базовая сторона bc обязана принадлежать первичному дереву: иначе после удаления листа x вершина b была бы изолирована. Поскольку родитель b уже равен x, ориентация этой стороны вынуждена:

**c -> b -> x.**

Конечная грань L_(d-1) содержит xb и bc. Если она треугольная, то это треугольник (x,b,c). Два его ребра первичные, а третье — последнее ребро выбранной двойственной цепи. Следовательно конечная грань имеет двойственную степень 1. Она не может иметь родителя: её единственная двойственная стрелка уже входит в неё. Значит она является строгим устойчивым корнем S.

Пусть o — её настоящая перпендикулярная стопа после переноса M в евклидову метрику. Строгая устойчивость означает o в относительной внутренности conv(x,b,c). Обозначим a'=a-o для трёх вершин. Поскольку o перпендикулярен плоскости гранных направлений, слабые стрелки сохраняются на касательных векторах. Поэтому

b'·x' >= |b'|² > 0,
b'·b' > 0,
b'·c' >= |c'|² > 0.

Все три вершины лежат в одной открытой полуплоскости относительно o, вопреки o в их выпуклой оболочке. Нулевые стрелки этому не мешают.

Более общая используемая лемма: **строгая устойчивая треугольная грань не может быть листовым корнем выбранного слабого двойственного дерева**. Дополняющие два первичных ребра образуют слабое дерево на её трёх касательных вершинах; для цепи разделяет средний вектор, для вилки — её корень. В обоих случаях получается открытая полуплоскость.

Итак, содержательный остаток имеет **четырёхугольную конечную грань**, а не произвольный базовый конец.

## 4. Полнота оставшихся 3+8 первичных случаев

Краткое восстановление нужной инциденционной классификации. Восемь базовых сторон имеют восемь различных соседних граней: одна другая грань не может содержать три базовые вершины и не совпасть с B. Это все остальные грани. Они треугольные либо четырёхугольные; сумма степеней даёт 34=8+24+q, значит четырёхугольников ровно два. Они имеют общую настоящую сторону xz. Из 17 рёбер восемь базовые, одно xz и восемь спиц; поэтому каждая базовая вершина имеет ровно одну спицу. Два непустых блока треугольников имеют длины t и 6-t. Это тот же полный геометрический класс, что в ROOT_LEAF.

Используются **буквально** следующие метки:

B=(0,1,2,3,4,5,6,7), z=8, x=9;

F = [B]
    + [(i,i+1,8) : 0<=i<t]
    + [(i,i+1,9) : t+1<=i<7]
    + [(t,t+1,9,8),(7,0,8,9)].

При t=1 степень x равна 7; при t=2 она равна 6. Последний список при t=2 совпадает с native ROOF8_3_5 родителя без переименования вершин или граней. Рёбра нумеруются лексикографически по неупорядоченным парам; маска — сумма 2^k для девяти первичных рёбер.

Четырёхугольный конец при базовой вершине b возможен только для b=t+1 или b=7. Достаточно b=t+1: вторую сторону даёт точное отражение

r_t(i)=(t-i) mod 8 для 0<=i<8; r_t(8)=8; r_t(9)=9.

При b=t+1 выбранное ребро B->L0 соответствует отсутствующей первичной базовой стороне (t+1,t+2). Все остальные рёбра вне малой z-части вынуждены связностью. Единственная свобода — выбрать остов малого графа

H_t: вершины {0,1,...,t,8};
рёбра {(i,i+1):0<=i<t} union {(i,8):0<=i<=t}.

После выбора его t+1 рёбер добавляются xb=(9,t+1) и все базовые стороны (i,i+1 mod 8), кроме i=0,...,t-1 и i=t+1. Получается ровно девять первичных рёбер. Обратно, всякий рассматриваемый первичный остов получается именно так: внешняя базовая цепь разрезана у b и не может соединять разные компоненты H_t.

H_1 — треугольник с **3** остовами. H_2 — граф на четырёх вершинах с пятью рёбрами и **8** остовами. Полный малый перебор включён в source и независимо совпадает с таблицей сертификатов:

| t | Степень x | Полный набор representative-масок |
|---|---:|---|
|1|7|10959, 10971, 10974|
|2|6|11055, 11067, 11070, 11111, 11115, 11118, 11123, 11126|

Это полное покрытие четырёхугольных концов, включая случаи, когда двойственный корень находится не в конечном четырёхугольнике. Никакой гипотезы о трёх первичных стрелках внутри этого четырёхугольника не добавлено.

## 5. Настоящий fan и точный общий разделяющий функционал

Для каждого из 11 представителей берётся настоящий fan из x=9. База триангулируется из **того же вынужденного b=t+1**. Если c_j=(b+j) mod 8, список его положительных тетраэдров равен

(9,b,c_j,c_(j+1)), j=1,...,6,
(9,8,i,i+1), i=0,...,t-1.

Других положительных конусов нет: все остальные максимальные грани содержат x. Таким образом имеется 7 или 8 ячеек. Гранные диагонали использованы только для интегрирования и нигде не объявляются механическими рёбрами.

Пусть X_i — вершины относительно **настоящего** центроида, G_ij=X_i^T M X_j. Для выбранных родителей p_i, i=0,...,8, положим

D_i=G_(i,p_i)-G_ii >= 0.

Для ячейки τ обозначим её четырёхвершинный индикатор через χ_τ. Source задаёт один целый вектор d для всех ячеек данного представителя и положительные целые λ_(τ,i). Проверяется матрица

A_τ = d χ_τ^T + χ_τ d^T
      + sum_i λ_(τ,i) [2e_i e_i^T-e_i e_(p_i)^T-e_(p_i)e_i^T] > 0.

Её точное скалярное тождество:

tr(A_τ G) = 2 d^T G χ_τ - 2 sum_i λ_(τ,i) D_i.

G — ненулевая положительно полуопределённая матрица одной физической метрики. Поэтому tr(A_τ G)>0 и, следовательно,

**d^T G χ_τ > 0 для каждой настоящей ячейки.**

Но настоящие нормированные объёмные веса ω_τ>0 удовлетворяют

sum_τ ω_τ=1,
sum_τ ω_τ sum_(i in τ) X_i = 4 COM(P)=0.

Значит sum_τ ω_τ d^T G χ_τ=0, противоречие. Это один общий разделяющий вектор sum_i d_i X_i и настоящие положительные объёмы одного P, а не независимо подбираемые массы или строки.

Весь принимаемый коэффициентный объект приведён в TABLE полного source ниже. Все λ положительны, минимум равен 1, максимум 71. Для каждого из 85 блоков выполнены независимое раскрытие скалярных мономов, целочисленный Bareiss и Fraction–Schur; произведения Schur-поворотов совпали со всеми 850 ведущими минорами. Наименьший ведущий минор среди сохранённых целых матриц равен 8. Отражённые коэффициенты и матрицы проверяются как точная перестановочная конгруэнция.

Алгебраический запрет даже не использует ранг 3. Физическая часть состоит в том, что **именно перечисленные 7/8 ячеек действительно являются fan одного собственного однородного тела**. Положительность численного eigenvalue не является основанием принятия: после поиска все коэффициенты округлены и проверены целочисленно. Один найденный полурациональный набор целиком умножен на 2; конечные 11 таблиц полностью целочисленные.

Это завершает доказательство теоремы: треугольный конец невозможен геометрически; каждый четырёхугольный конец входит в один из точных fan-сертификатов.

## 6. Нативный census и отсутствие незаконного глобального списания

Отдельно перебраны все C(17,9)=24310 первичных подмножеств каждой из двух буквальных моделей, проверены первичная и дополнительная двойственная связности, все девять двойственных корней и точный выбранный полный путь.

| Модель | Все первичные остовы | Полные base-пары | Треугольный конец | Fan-пары | Различные fan-маски |
|---|---:|---:|---:|---:|---:|
|t=1, U9 степени7|3885|38|30|8|6|
|t=2, U9 степени6|4053|88|64|24|16|
|Сумма|7938|126|94|32|22|

Число 24 в последней fan-колонке t=2 относится к **базовым** выбранным парам этого нового реестра. Это не прежние 24 full-xz пары: у всех новых записей единственный ребёнок корня базовый; пересечение с root-leaf-xz масками проверено и равно нулю. Прежние 24 native degree6 fullxz уже были полностью исключены ROOT_LEAF и здесь не исследовались как открытые.

126 — число условных размеченных пар в этих двух самостоятельных нативных моделях, **не** число тел и не новая дельта FULL253/LOCAL/tree410. Полные старые каталоги с буквальными отображениями и пересечениями не входят в данный пакет. Их счётчики не меняются. Полные новые записи mask,U,S,pv,pq,chain,b,certificate,map восстанавливаются из source; никакой список для продолжения не остаётся только в sandbox.

## 7. Дополнительное новое интегральное следствие для более широкого двухапексного класса

Следующий результат сохраняется отдельно: он не понадобился для принятия 11 сертификатов и не объявляется самостоятельным исключением всех двухапексных тел.

Нормируем |x|=1. Пусть b максимален среди всех некорневых вершин, r=|b|<1, σ=|z|<r и b->x. Положим p=B·x, s=B·z, k=|B|. Для настоящего собственного двухапексного тела

**(1-p)c(σ)+kσ >= 3,**

где

c(σ)=[5+3σ-sqrt(9+6σ-3σ²)]/4.

В частности,

**σ <= 3/20  =>  k-4p > 16.**

Это вывод из **второго настоящего fan — из b**, а не усиление старой скалярной строки B·(x+z)<-2 путём свободного выбора коэффициентов. Гипотезы о b и r,σ следуют из ROOT_LEAF уже в общем двухапексном U1-классе; единственность ребёнка для этой отдельной леммы не нужна.

Доказательство. Настоящая масса даёт A=1-p, C=1-s в (0,4) и δ=A+C-4>0. Строгость A,C<4 следует также непосредственно из двух настоящих апексных fan и того, что каждый апекс — настоящая вершина вне пирамиды над B с другим апексом.

В fan из b каждая ячейка содержит b и три разные другие вершины. Поэтому фактические усреднённые коэффициенты x,z равны некоторым α,β в [0,1], а остальные базовые коэффициенты η_i неотрицательны и имеют сумму 3-α-β. Собственный центр даёт

-b = αx+βz+sum_i η_i v_i,
αA+βC=4.

Положим u=1-α, v=1-β. Тогда Au+Cv=δ. Все оставшиеся базовые нормы не превосходят r, откуда

|b+x| <= r+σ+(r+1)u+(r-σ)v.

С другой стороны, b->x даёт |b+x|>=sqrt(1+3r²). Следовательно

K:=sqrt(1+3r²)-r-σ <= (r+1)u+(r-σ)v,
K>r-σ>0.

Если бы (r-σ)/C >= (r+1)/A, правая часть была бы не больше δ(r-σ)/C<r-σ, поскольку δ<C. Противоречие. Поэтому

δ >= A K/(r+1).

После подстановки δ=A+C-4 и C<=1+kσ получаем

A f(r,σ)+kσ >=3,
f(r,σ)=[1+2r+σ-sqrt(1+3r²)]/(1+r).

Для указанного c(σ) выполняется точное равенство

(1+σ-c)²+(2-c)²/3=1.

Коши–Шварц даёт sqrt(1+3r²)>=(1+σ-c)+(2-c)r, то есть f<=c. Основная оценка доказана.

При σ<=3/20 вместо c можно взять строгое рациональное 3/5, поскольку

(2/5+3/20)²+(7/5)²/3 =1147/1200<1.

Следовательно 3A/5+3k/20>3, то есть k+4A>20, или k-4p>16. Никакое внешнее ковариационное неравенство здесь не использовано.

## 8. Сохранённые препятствия к неверным сокращениям и настоящий невыигрышный контроль

**Неверное сокращение:** «четырёхугольный конец всегда является листовым устойчивым корнем и содержит три последовательные первичные стрелки». Оно не следует из выбранности. Буквальный комбинаторный контроль t=1, mask=10959, U9,S7:

pv=(1,2,9,4,5,6,7,0,0,9),
pq=(2,7,3,4,5,6,8,7,7),
chain=(2,3,4,5,6,8,7).

Конечная грань F7=(1,2,9,8) имеет два двойственных ребёнка, а z8->0 идёт к вершине вне F7. Поэтому нельзя универсально выводить маленькую норму z трёхугловой оценкой по первичному пути внутри конечного четырёхугольника. Этот комбинаторный объект **не является физическим контрпримером**: новый fan-сертификат (1,10959) как раз исключает его физическую реализацию. Source сохраняет и проверяет этот отрицательный методический контроль.

**Новый настоящий контроль того же E17-типа**, не 110. Вершины задаются десятью целыми тройками, делёнными на 10:

(-5,-10,0), (-5,10,0), (6,10,0), (14,6,0), (16,2,0),
(16,-2,0), (14,-6,0), (6,-10,0), (-10,0,10), (10,0,10).

M=(1/100)*[[66,-4,42],[-4,3,-2],[42,-2,30]], N=M^{-1}.

Это буквальная t=1 модель. Точные данные:

Vol=47/25,
COM=(3197/11280,0,191/564),
p=s=-373/191, δ=364/191, λ=91/141.

Все координаты перед механическим аудитом перенесены на этот настоящий COM. Ведущие миноры M равны 33/50,91/5000,9/15625. Единственные две крупнейшие нормы имеют вершины x=9 и b=5, именно в таком порядке. При этом

D_(5,9)=367/88125>0,
D_(8,1)=106141/1128000>0.

То есть максимальная базовая вершина действительно уходит к x, а второй апекс действительно уходит в базу. Оба настоящих полюса при ребре (5,9) поддерживают x и b одновременно. Однако

S=[0,7,8], U=[1,9],
H=[(0,7),(1,2),(8,9)],
(S,U,H)=(3,2,3).

Все 68 истинных рёберных примитивов ненулевые; N проверена как точная обратная M. B сама строго устойчива, и все B->L отрицательны. Следовательно это не тело выбранного запрещаемого класса и не новый верхний пример. Оно показывает, что отдельные новые endpoint/rank/escape данные без выбранного полного дерева и нужного B-входа ещё совместимы с настоящей uniform-ownCOM геометрией.

Контроль проверен двумя разными положительными апексными интегрированиями, исчерпывающим восстановлением всех опорных тройных плоскостей, полным S/U/H-аудитом и всеми тремя t=1 weighted fan identities. Он сохранён, несмотря на невыигрышный строгий класс и C=34.

## 9. Полная recovery-капсула и фактический статус

Сохранить единственный полный source ниже как **endpoint_full67.py**, UTF-8/LF с последним LF. В нём буквально находятся все 11 целочисленных таблиц, обе инциденционные модели, отражения, оба независимых перечисления, обе точные PD-проверки, весь настоящий контроль и необязательный воспроизводящий locator. Внешних входных файлов для build/check нет.

Основные команды, без -O:

```bash
python -S endpoint_full67.py build
python -S endpoint_full67.py check > endpoint_full67_check.txt
```

Среда фактической точной проверки: CPython 3.13.5, стандартная библиотека. Выполнены build и check; затем только source перенесён в чистый каталог, и обе команды выполнены повторно. JSON и stdout совпали побайтно.

| Объект | Байты | SHA-256 |
|---|---:|---|
|endpoint_full67.py|23735|261162985f95bde586358d71f0283f37757fa9160fc354378ddfb9eaadbd2617|
|endpoint_full67.json|73431|c981d2acf3a26f142ad6fa1961e7f4f313cfbdfd6102af898e46b2fd389c79c1|
|endpoint_full67_check.txt|345|66fcdae509da8da09df288ecc82f7c9bbce6bb14be813d939a6c2594f85c23d4|
|endpoint_full67_discovery.json|3413|73b7b65b1064dd79b824df02f6ad7017ed76ee1890288f7fe024344121951753|
|endpoint_full67_discovery_check.txt|161|190c00b10e50d8b05b09337173de1258120040eed26e651cab0bd5dbc01f1c2e|

Ожидаемый полный stdout основной проверки:

```text
MAX_ENDPOINT_FAN_11_CERTIFICATES_85_PD_BLOCKS_850_MINORS_PASS
DEG7_BASE38_AND_DEG6_BASE88_FULL_SELECTED_CHAINS_PASS
TRIANGLE_LEAF94_AND_ACTUAL_FAN32_PAIRS_PASS
ACTUAL_OWN_COM_DEG7_CONTROL_S3_U2_H3_PASS
endpoint_full67.json 73431 c981d2acf3a26f142ad6fa1961e7f4f313cfbdfd6102af898e46b2fd389c79c1
TWO_APEX_MAX_ENDPOINT_FULL67_DURABLE_RECOVERY_PASS
```

Для восстановления самого поиска предусмотрено `python endpoint_full67.py discover`. Оно требует NumPy 2.3.5 и SciPy 1.17.0, фиксирует BLAS/OMP/MKL threads=1, использует HiGHS LP и последовательные eigenvector-cuts, не использует RNG. Максимум — 35 итераций на каждую из 11 точных задач. Принимаются только округления, прошедшие оба точных проверяющих и совпавшие с замороженной целой TABLE. Режим фактически выполнен и повторён source-only в чистом каталоге. Наблюдались OpenBLAS 0.3.30 и Linux x86_64/glibc2.41. Его stdout:

```text
FULL67_SOURCE_ONLY_NUMERIC_LOCATION_AND_EXACT_ROUNDING_PASS
endpoint_full67_discovery.json 3413 73b7b65b1064dd79b824df02f6ad7017ed76ee1890288f7fe024344121951753
```

Точная приёмка не зависит от повторения численной траектории на другой BLAS-платформе: build/check используют только сохранённые целые входы и рациональную арифметику. Это исполненная арифметическая проверка и аналитическое доказательство выше, не внешнее рецензирование и не proof-assistant формализация.

## 10. Непокрытый остаток и продолжение

Не покрыты выбранные root-degree1 конфигурации с иным входом B, сходящимся или иначе ориентированным локальным двойственным путём; первичная степень корня больше 1 и соответствующие неполные леса; корни в B; другие E17 face lattices без базовой восьмёрки; большие V/E/F. Available-arrow версия без включения всей заданной цепи в одну дополняющую пару также не доказана.

Для следующего исполнителя имеются два конкретных ресурса: полный новый 126-парный нативный реестр для буквального пересечения с историческими каталогами и отдельная общая b-fan оценка (1-p)c(σ)+kσ>=3 для геометрии, где полная цепь уже отсутствует. Повторный поиск выбранного xz-замыкания не нужен. Исходные доказательства V>=10/F>=9 и точная верхняя конструкция C622 здесь заново не исполнялись; их принятый статус не превращается в новый аудит или в совпадающие нижнюю и верхнюю стороны.

## 11. Полный source

```python
"""TWO_APEX_MAX_ENDPOINT_FULL67_FAN85_V1.
CPython 3.13.5, standard library; no external inputs; assertions enabled.
python -S endpoint_full67.py build
python -S endpoint_full67.py check
The continuous theorem is proved in the accompanying handoff.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys
assert __debug__
IDENTITY = 'TWO_APEX_MAX_ENDPOINT_FULL67_FAN85_V1'
PARENTS = [
 ['minimum-0086','8123315ee22b6a0fc370e8f672f299bc19997f89ad023530404946c77f994f10'],
 ['minimum-0087','b77264d597b32a5f97ac011c57d4c95e7581fb2d81d202e2bc477b0e6fc867f5']]
# Rows: [t, primal lex-edge mask, common direction d, positive multipliers].
# Multipliers are ordered by children 0,...,8 (the primal root is 9).
TABLE = [
[1, 10959, [0, 0, 3, 0, 0, 0, 0, 0, 0, 2], [[9, 9, 4, 5, 7, 12, 7, 10, 1], [9, 9, 4, 1, 6, 8, 9, 8, 1], [12, 9, 3, 2, 2, 5, 13, 8, 1], [10, 11, 3, 1, 3, 4, 7, 12, 1], [8, 9, 3, 4, 2, 3, 3, 7, 1], [7, 9, 5, 2, 2, 4, 3, 9, 1], [12, 11, 4, 1, 2, 3, 5, 9, 4]]],
[1, 10971, [0, 4, 0, 0, 0, 0, 0, 0, 0, 3], [[11, 10, 6, 4, 12, 14, 11, 10, 4], [17, 12, 5, 4, 6, 15, 11, 10, 1], [14, 11, 4, 1, 3, 10, 10, 11, 1], [9, 11, 3, 1, 4, 3, 9, 13, 4], [12, 12, 5, 2, 2, 6, 3, 10, 1], [9, 12, 3, 1, 4, 5, 4, 6, 1], [14, 13, 5, 1, 2, 4, 3, 3, 6]]],
[1, 10974, [0, 2, 2, 0, 0, 0, 0, 2, 0, 2], [[11, 10, 5, 7, 9, 10, 10, 9, 19], [12, 7, 6, 1, 10, 10, 11, 9, 11], [14, 11, 4, 1, 2, 8, 12, 11, 10], [10, 9, 4, 1, 3, 4, 7, 14, 12], [17, 9, 4, 2, 2, 5, 5, 4, 14], [18, 8, 4, 1, 3, 2, 5, 5, 7], [12, 10, 3, 1, 6, 3, 7, 4, 11]]],
[2, 11055, [0, 3, 0, 3, 0, 0, 0, 0, -1, 3], [[9, 15, 8, 5, 5, 10, 12, 7, 1], [10, 13, 11, 5, 1, 4, 7, 12, 1], [13, 12, 8, 4, 1, 2, 8, 10, 1], [9, 12, 9, 3, 2, 4, 3, 9, 3], [7, 13, 9, 4, 2, 2, 4, 4, 1], [5, 6, 14, 4, 1, 2, 5, 4, 1], [26, 31, 13, 8, 1, 2, 4, 5, 9], [15, 8, 12, 3, 1, 2, 4, 4, 7]]],
[2, 11067, [0, 0, 0, 6, 0, 0, 0, 2, 0, 2], [[14, 12, 10, 5, 8, 9, 10, 6, 1], [11, 13, 9, 5, 1, 5, 11, 13, 1], [11, 11, 10, 4, 2, 2, 8, 10, 1], [12, 10, 10, 4, 1, 3, 4, 6, 1], [4, 17, 6, 6, 1, 2, 3, 4, 1], [5, 9, 12, 3, 1, 5, 2, 5, 1], [27, 33, 15, 8, 2, 2, 5, 5, 9], [4, 22, 14, 4, 2, 3, 4, 6, 4]]],
[2, 11070, [0, 0, 1, 6, 0, 1, 1, 1, 0, 4], [[12, 14, 9, 4, 7, 16, 11, 17, 13], [17, 16, 14, 5, 1, 6, 12, 15, 9], [20, 13, 10, 5, 1, 5, 6, 12, 10], [16, 12, 13, 4, 1, 3, 3, 11, 12], [11, 10, 14, 4, 3, 3, 3, 4, 7], [5, 11, 8, 7, 1, 2, 6, 6, 7], [13, 30, 16, 9, 2, 2, 7, 5, 44], [5, 21, 14, 4, 2, 2, 5, 5, 10]]],
[2, 11111, [0, 4, 3, 13, 0, 1, 0, 0, 0, 7], [[31, 6, 19, 10, 16, 33, 27, 19, 22], [21, 2, 23, 13, 3, 16, 23, 34, 25], [29, 2, 31, 8, 3, 4, 18, 26, 20], [25, 3, 21, 8, 2, 5, 9, 15, 30], [22, 8, 15, 8, 2, 5, 8, 16, 25], [18, 5, 22, 7, 3, 4, 9, 6, 34], [53, 51, 37, 15, 4, 4, 13, 20, 71], [31, 8, 35, 10, 3, 6, 7, 12, 34]]],
[2, 11115, [0, 0, 0, 4, 0, 0, 0, 1, 0, 3], [[14, 9, 10, 4, 4, 15, 11, 7, 1], [7, 11, 8, 5, 1, 8, 10, 10, 1], [12, 11, 10, 4, 1, 7, 7, 11, 2], [9, 9, 12, 3, 5, 2, 4, 8, 1], [10, 14, 8, 4, 1, 4, 4, 5, 1], [7, 5, 14, 5, 1, 2, 6, 4, 1], [9, 20, 13, 6, 1, 2, 4, 4, 6], [5, 7, 11, 3, 1, 3, 4, 5, 6]]],
[2, 11118, [0, 0, 0, 5, 0, 0, 0, 0, 0, 2], [[11, 1, 9, 4, 6, 15, 13, 10, 10], [14, 2, 10, 5, 1, 6, 13, 9, 9], [11, 5, 12, 4, 1, 2, 6, 9, 10], [9, 1, 9, 4, 2, 2, 5, 12, 10], [6, 4, 9, 6, 1, 2, 4, 6, 6], [9, 3, 9, 5, 1, 4, 4, 2, 6], [10, 12, 13, 5, 2, 3, 3, 6, 17], [9, 5, 15, 4, 2, 2, 4, 5, 10]]],
[2, 11123, [0, 0, 3, 6, 0, 2, 0, 2, 0, 5], [[16, 12, 18, 6, 9, 11, 16, 13, 9], [12, 9, 8, 5, 1, 10, 17, 14, 12], [12, 14, 13, 4, 1, 2, 12, 14, 10], [12, 15, 12, 4, 2, 2, 5, 8, 12], [6, 16, 14, 5, 2, 3, 4, 8, 12], [7, 8, 12, 3, 1, 3, 5, 6, 7], [14, 35, 17, 8, 1, 3, 5, 8, 35], [7, 13, 15, 5, 1, 4, 4, 7, 21]]],
[2, 11126, [0, 0, 1, 5, 0, 0, 0, 2, 0, 3], [[8, 1, 9, 7, 7, 12, 9, 14, 14], [17, 1, 14, 5, 1, 5, 11, 10, 11], [13, 2, 10, 4, 1, 3, 6, 11, 13], [11, 1, 13, 5, 1, 2, 4, 7, 14], [8, 3, 15, 3, 4, 3, 3, 4, 7], [5, 4, 14, 5, 2, 3, 2, 5, 7], [16, 15, 15, 7, 2, 3, 4, 3, 31], [5, 3, 13, 5, 1, 3, 4, 7, 21]]],
]

def dot(a,b): return sum((x*y for x,y in zip(a,b)),Q(0))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def scale(s,a): return tuple(s*x for x in a)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))
def bil(a,M,b): return dot(a,[dot(row,b) for row in M])
def inv3(M):
    d=det(*M); assert d>0
    C=[cross(M[1],M[2]),cross(M[2],M[0]),cross(M[0],M[1])]
    return [[C[j][i]/d for j in range(3)] for i in range(3)]

def facets(t):
    assert t in (1,2)
    return [tuple(range(8))]+[(i,i+1,8) for i in range(t)]+[(i,i+1,9) for i in range(t+1,7)]+[(t,t+1,9,8),(7,0,8,9)]

def incidence(ff):
    ef={}
    for i,f in enumerate(ff):
        for a,b in zip(f,f[1:]+f[:1]): ef.setdefault(tuple(sorted((a,b))),[]).append(i)
    assert len(ef)==17 and all(len(v)==2 for v in ef.values())
    return sorted(ef),ef

def rooted(n,edges,root):
    adj=[[] for _ in range(n)]
    for a,b in edges: adj[a].append(b); adj[b].append(a)
    p=[None]*n; p[root]=root; todo=[root]
    for a in todo:
        for b in adj[a]:
            if p[b] is None: p[b]=a; todo.append(b)
    return p if all(v is not None for v in p) else None

def edge_mask(edges,chosen):
    return sum(1<<edges.index(tuple(sorted(e))) for e in chosen)

def parent_from_mask(t,mask):
    edges,_=incidence(facets(t))
    chosen=[e for k,e in enumerate(edges) if (mask>>k)&1]
    assert len(chosen)==9
    p=rooted(10,chosen,9); assert p is not None
    child=[i for i in range(9) if p[i]==9]; assert len(child)==1
    return p,child[0]

def cells(t,b,x=9):
    cyc=[(b+i)%8 for i in range(8)]
    return [(x,b,cyc[i],cyc[i+1]) for i in range(1,7)]+[(x,)+f for f in facets(t)[1:] if x not in f]

def block(d,lam,cell,p):
    chi=[int(i in cell) for i in range(10)]; assert sum(chi)==4
    A=[[d[i]*chi[j]+chi[i]*d[j] for j in range(10)] for i in range(10)]
    for i,l in enumerate(lam):
        assert l>0 and p[i]!=i
        A[i][i]+=2*l; A[i][p[i]]-=l; A[p[i]][i]-=l
    return A

def bareiss_minors(A):
    W=[r[:] for r in A]; n=len(W); prev=1; minors=[]
    for k in range(n-1):
        pivot=W[k][k]; assert pivot>0; minors.append(pivot)
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=W[i][j]*pivot-W[i][k]*W[k][j]
                assert v%prev==0; W[i][j]=v//prev
        prev=pivot
    assert W[-1][-1]>0; minors.append(W[-1][-1]); return minors

def independent_check(A,d,lam,cell,p,minors):
    # Independently expand scalar monomials, then use Fraction Schur complements.
    terms={}
    def term(i,j,c):
        key=tuple(sorted((i,j))); terms[key]=terms.get(key,0)+c
    for i in range(10):
        for j in cell: term(i,j,2*d[i])
    for i,l in enumerate(lam): term(i,i,2*l); term(i,p[i],-2*l)
    for i in range(10):
        for j in range(i,10): assert terms.get((i,j),0)==A[i][j]*(1 if i==j else 2)
    W=[list(map(Q,row)) for row in A]; product=Q(1); pivots=[]
    for k in range(10):
        pivot=W[k][k]; assert pivot>0; pivots.append(pivot); product*=pivot
        assert product==minors[k]
        for i in range(k+1,10):
            for j in range(k+1,10): W[i][j]-=W[i][k]*W[k][j]/pivot
    return pivots

def certificate_audit():
    out={}; nb=nm=0
    for t,mask,d,lam in TABLE:
        p,b=parent_from_mask(t,mask); assert b==t+1
        cc=cells(t,b); assert len(cc)==len(lam)==6+t
        matrices=[]; minors=[]; pivots=[]
        for cell,lm in zip(cc,lam):
            A=block(d,lm,cell,p); mi=bareiss_minors(A)
            pi=independent_check(A,d,lm,cell,p,mi)
            matrices.append(A); minors.append(mi); pivots.append(pi); nb+=1; nm+=len(mi)
        out[t,mask]={'t':t,'mask':mask,'b':b,'pv':p,'cells':cc,'d':d,'lam':lam,
                    'integer_matrices':matrices,'leading_minors':minors,'schur_pivots':pivots}
    assert len(out)==11 and (nb,nm)==(85,850)
    return out

def small_fan_exhaustion(certs):
    """Independent 3/8-tree reconstruction of every nontriangular endpoint."""
    counts=[]
    for t in (1,2):
        ee,_=incidence(facets(t)); b=t+1
        small_vertices=list(range(t+1))+[8]
        small_edges=[(i,i+1) for i in range(t)]+[(i,8) for i in range(t+1)]
        index={v:i for i,v in enumerate(small_vertices)}
        outside=[(9,b)]+[(i,(i+1)%8) for i in range(8) if i not in list(range(t))+[b]]
        masks=[]
        for ii in combinations(range(len(small_edges)),t+1):
            chosen=[small_edges[i] for i in ii]
            reduced=[(index[a],index[c]) for a,c in chosen]
            if rooted(t+2,reduced,index[8]) is None: continue
            mask=edge_mask(ee,outside+chosen); p,child=parent_from_mask(t,mask)
            assert child==b and p[t]==b
            masks.append(mask)
        assert len(masks)==(3 if t==1 else 8)
        assert set(masks)=={mask for tt,mask in certs if tt==t}
        counts.append({'t':t,'small_vertices':small_vertices,'small_edges':small_edges,
                       'forced_outside_edges':outside,'representative_masks':sorted(masks)})
    return counts

def reflection(t): return [(t-i)%8 for i in range(8)]+[8,9]

def transported_keys(certs):
    keys={}; maps={}
    for t in (1,2):
        ff=facets(t); edges,_=incidence(ff); vmap=reflection(t)
        fmap=[next(j for j,g in enumerate(ff) if set(g)=={vmap[v] for v in f}) for f in ff]
        assert sorted(fmap)==list(range(9)); maps[t]={'vertices':vmap,'facets':fmap}
        for key,c in certs.items():
            if key[0]!=t: continue
            mask=c['mask']; p=c['pv']; chosen=[(i,p[i]) for i in range(9)]
            image_mask=edge_mask(edges,[(vmap[a],vmap[b]) for a,b in chosen])
            image_p,image_b=parent_from_mask(t,image_mask); assert image_b==7
            for i in range(10): assert image_p[vmap[i]]==vmap[p[i]]
            image_cells={tuple(sorted(vmap[i] for i in cc)) for cc in c['cells']}
            assert image_cells=={tuple(sorted(cc)) for cc in cells(t,7)}
            assert (t,mask) not in keys and (t,image_mask) not in keys
            keys[t,mask]=(key,list(range(10)))
            keys[t,image_mask]=(key,vmap)
            # Verify all transported coefficients and matrices, not only the mask.
            di=[0]*10
            for i in range(10): di[vmap[i]]=c['d'][i]
            for cell,lm,A in zip(c['cells'],c['lam'],c['integer_matrices']):
                li=[0]*9
                for i in range(9): li[vmap[i]]=lm[i]
                Ai=block(di,li,tuple(vmap[i] for i in cell),image_p)
                assert all(Ai[vmap[i]][vmap[j]]==A[i][j] for i in range(10) for j in range(10))
    assert len(keys)==22
    return keys,maps

def census(keys):
    models=[]; totals=[0,0,0]
    for t in (1,2):
        ff=facets(t); edges,ef=incidence(ff); inc={i for i,f in enumerate(ff) if 9 in f}
        assert len(inc)==8-t
        rows=[]; all_trees=0; xz_masks=[]
        for kk in combinations(range(17),9):
            chosen=[edges[k] for k in kk]; pv=rooted(10,chosen,9)
            if pv is None: continue
            all_trees+=1; mask=sum(1<<k for k in kk); ss=set(kk)
            dual=[tuple(ef[e]) for k,e in enumerate(edges) if k not in ss]
            assert rooted(9,dual,0) is not None
            child=[i for i in range(9) if pv[i]==9]
            if len(child)!=1: continue
            b=child[0]
            if b==8: xz_masks.append(mask); continue
            for stable in range(9):
                pq=rooted(9,dual,stable); start=pq[0]
                if start not in inc: continue
                path=[start]
                while pq[path[-1]] in inc and pq[path[-1]] not in path: path.append(pq[path[-1]])
                if set(path)!=inc: continue
                assert set(ff[path[0]])&set(ff[path[-1]])=={9,b}
                r={'mask':mask,'U':9,'S':stable,'b':b,'pv':pv,'pq':pq,'chain':path}
                if stable==path[-1] and len(ff[stable])==3:
                    # General stable-triangle/leaf-root lemma, proved in handoff.
                    degree=sum(stable in e for e in dual); assert degree==1
                    tri=set(ff[stable]); internal=[e for e in chosen if set(e)<=tri]
                    assert len(internal)==2 and set().union(*(set(e) for e in internal))==tri
                    sinks=[v for v in tri if pv[v] not in tri or pv[v]==v]
                    assert len(sinks)==1
                    r['reason']='STABLE_TRIANGLE_CANNOT_BE_DUAL_ROOT_LEAF'; totals[1]+=1
                else:
                    key,vmap=keys[t,mask]
                    r['reason']='ACTUAL_FAN_POSITIVE_DEFINITE_CERTIFICATE'
                    r['certificate']=[key[0],key[1]]; r['vertex_map']=vmap; totals[2]+=1
                rows.append(r); totals[0]+=1
        counts=[len(rows),sum(r['reason'].startswith('STABLE') for r in rows),sum(r['reason'].startswith('ACTUAL') for r in rows)]
        assert (all_trees,counts)==({1:(3885,[38,30,8]),2:(4053,[88,64,24])}[t])
        assert not {r['mask'] for r in rows}&set(xz_masks)
        fan_masks={r['mask'] for r in rows if r['reason'].startswith('ACTUAL')}
        assert fan_masks=={mask for tt,mask in keys if tt==t}
        models.append({'t':t,'facets':ff,'lex_edges':edges,'all_primal_tree_count':all_trees,
                       'counts_full_base_triangle_fan':counts,'new_xz_overlap':0,
                       'full_base_pairs':rows,'fan_primary_masks':sorted(fan_masks)})
    assert totals==[126,94,32]
    return models

CONTROL_POINTS=[(-5,-10,0),(-5,10,0),(6,10,0),(14,6,0),(16,2,0),(16,-2,0),(14,-6,0),(6,-10,0),(-10,0,10),(10,0,10)]
CONTROL_METRIC=[(66,-4,42),(-4,3,-2),(42,-2,30)]

def physical_control(certs):
    P=[tuple(Q(x,10) for x in v) for v in CONTROL_POINTS]
    M=[tuple(Q(x,100) for x in r) for r in CONTROL_METRIC]; N=inv3(M)
    assert [M[0][0],M[0][0]*M[1][1]-M[0][1]**2,det(*M)]==[Q(33,50),Q(91,5000),Q(9,15625)]
    assert all(sum(M[i][k]*N[k][j] for k in range(3))==int(i==j) for i in range(3) for j in range(3))
    ff=facets(1); edges,ef=incidence(ff)
    inside=tuple(sum(v[k] for v in P)/10 for k in range(3)); cycles=[]; normals=[]
    D=Q(0); moment=(Q(0),)*3
    for f in ff:
        cy=list(f); normal=cross(sub(P[cy[1]],P[cy[0]]),sub(P[cy[2]],P[cy[0]]))
        if dot(normal,sub(inside,P[cy[0]]))>0: cy=cy[::-1]; normal=scale(-1,normal)
        assert all(dot(normal,sub(v,P[cy[0]]))==0 if i in cy else dot(normal,sub(v,P[cy[0]]))<0 for i,v in enumerate(P))
        cycles.append(cy); normals.append(normal)
        for j in range(1,len(cy)-1):
            a,b,c=[P[i] for i in (cy[0],cy[j],cy[j+1])]; w=det(a,b,c)
            D+=w; moment=add(moment,scale(w,add(add(a,b),c)))
    center=scale(1/(4*D),moment); X=[sub(v,center) for v in P]
    assert D/6==Q(47,25) and center==(Q(3197,11280),Q(0),Q(191,564))
    poles=[scale(1/dot(n,X[cy[0]]),n) for n,cy in zip(normals,cycles)]
    # Independent exhaustive supporting-triple hull recovery.
    hull=set()
    for a,b,c in combinations(range(10),3):
        n=cross(sub(P[b],P[a]),sub(P[c],P[a]))
        if not any(n): continue
        vals=[dot(n,sub(v,P[a])) for v in P]
        if min(vals)>=0 or max(vals)<=0: hull.add(tuple(i for i,v in enumerate(vals) if v==0))
    assert hull=={tuple(sorted(f)) for f in ff}
    # Two different genuine apex fans integrate the same exact volume and COM.
    fans=[]
    for apex in (8,9):
        cc=cells(1,2,apex); weights=[]; first=(Q(0),)*3
        for cell in cc:
            a,b,c,d=[X[i] for i in cell]; w=abs(det(sub(b,a),sub(c,a),sub(d,a))); assert w>0
            weights.append(w); first=add(first,scale(w,add(add(a,b),add(c,d))))
        assert sum(weights)==D and first==(0,0,0)
        fans.append({'apex':apex,'cells':cc,'six_volume_weights':weights})
    p0=dot(poles[0],X[9]); s0=dot(poles[0],X[8]); delta=-p0-s0-2
    lam=sum(fans[1]['six_volume_weights'][:6])/D
    assert p0==s0==Q(-373,191) and delta==Q(364,191) and lam==Q(91,141)
    assert delta==lam*(1-s0)>0
    G=[[bil(v,M,w) for w in X] for v in X]; J=[[bil(q,N,r) for r in poles] for q in poles]
    U=[i for i in range(10) if all(G[i][j]<G[i][i] for j in range(10) if i!=j)]
    S=[i for i in range(9) if all(J[i][j]<J[i][i] for j in range(9) if i!=j)]
    slopes=[]; H=[]
    for e in edges:
        a,b=e; f,g=ef[e]
        z=[G[a][b]-G[a][a],G[a][b]-G[b][b],J[f][g]-J[f][f],J[f][g]-J[g][g]]
        assert all(v!=0 for v in z); slopes.append(z)
        if max(z)<0: H.append(e)
    assert U==[1,9] and S==[0,7,8] and H==[(0,7),(1,2),(8,9)]
    assert G[9][9]>G[5][5] and all(G[5][5]>G[i][i] for i in range(10) if i not in (5,9))
    assert G[5][9]-G[5][5]==Q(367,88125)>0
    assert G[8][1]-G[8][8]==Q(106141,1128000)>0
    assert all(J[0][j]-J[0][0]<0 for j in range(1,9))
    contractions=[]
    for key,c in certs.items():
        if key[0]!=1: continue
        wts=fans[1]['six_volume_weights']; assert c['cells']==fans[1]['cells']
        arr=[G[i][c['pv'][i]]-G[i][i] for i in range(9)]; assert min(arr)<0
        total=Q(0)
        for w,A,lm,cell in zip(wts,c['integer_matrices'],c['lam'],c['cells']):
            trace=sum(A[i][j]*G[i][j] for i in range(10) for j in range(10))
            rhs=trace+2*dot(lm,arr)
            left=2*sum(c['d'][i]*G[i][j] for i in range(10) for j in cell)
            assert left==rhs; total+=w*rhs
        assert total==0; contractions.append({'mask':key[1],'minimum_selected_arrow':min(arr),'weighted_identity':total})
    return {'scope':'ACTUAL_UNIFORM_OWN_COM_NOT_110_NOT_A_SELECTED_FULL_CHAIN_COUNTEREXAMPLE',
            'input_points_denominator':10,'input_points_numerators':CONTROL_POINTS,
            'M_denominator':100,'M_numerators':CONTROL_METRIC,'M':M,'N':N,
            'facets':ff,'true_edges':edges,'volume':D/6,'raw_centroid':center,'p':p0,'s':s0,'delta':delta,'lambda':lam,
            'centered_vertices':X,'poles':poles,'G':G,'J':J,'edge_slopes':slopes,
            'S':S,'U':U,'saddle_edges':H,'S_U_H':[3,2,3],'zero_edge_primitives':0,
            'unique_two_largest_vertices':[9,5],'b_to_x':G[5][9]-G[5][5],
            'z_to_base1':G[8][1]-G[8][8],'two_actual_apex_fans':fans,
            'certificate_identity_controls':contractions}

def encode(x):
    if isinstance(x,Q): return str(x)
    if isinstance(x,dict): return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [encode(v) for v in x]
    return x

def build():
    certs=certificate_audit(); keys,maps=transported_keys(certs); models=census(keys)
    negative=next(r for r in models[0]['full_base_pairs'] if r['mask']==10959 and r['S']==7)
    assert len(facets(1)[7])==4 and negative['pv'][8]==0 and 0 not in facets(1)[7]
    assert sum(i!=7 and p==7 for i,p in enumerate(negative['pq']))==2
    # Exact rational allowance used in the separate centroid lemma's small-z corollary.
    assert (Q(2,5)+Q(3,20))**2+Q(7,5)**2/3==Q(1147,1200)<1
    obj={'identity':IDENTITY,'literal_parents':PARENTS,'certificates':list(certs.values()),
         'reflections':maps,'models':models,'small_fan_exhaustion':small_fan_exhaustion(certs),'physical_control':physical_control(certs),
         'counts':{'certificate_representatives':11,'positive_definite_blocks':85,'positive_leading_minors':850,
                   'reflected_primal_masks':22,'native_full_base_pairs':126,'triangle_leaf_pairs':94,'fan_pairs':32},
         'failed_shortcut_control':{'scope':'COMBINATORIAL_NOT_A_PHYSICAL_REALIZATION','pair':negative,
                                    'invalid_shortcut':'A stable quadrilateral endpoint need not carry three consecutive primal arrows.'},
         'global_catalog_delta':'NOT_COMPUTED','accepted_C_bracket_unchanged':[34,622]}
    return (json.dumps(encode(obj),ensure_ascii=True,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')

def discover():
    """Optional reconstruction of the integer table; not needed for build/check."""
    import os
    for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
        os.environ[name]='1'
    import numpy as np
    import scipy
    from scipy.optimize import linprog
    assert np.__version__=='2.3.5' and scipy.__version__=='1.17.0'
    receipt=[]
    for t,mask,frozen_d,frozen_lam in TABLE:
        p,b=parent_from_mask(t,mask); cc=cells(t,b); n=10; m=len(cc); k=9
        nv=n+m*k+n
        chis=np.array([[int(i in cell) for i in range(n)] for cell in cc])
        forms=np.zeros((k,n,n))
        for i in range(k): forms[i,i,p[i]]=forms[i,p[i],i]=.5; forms[i,i,i]=-1
        rows=[]; rhs=[]
        def cut(j,v):
            row=np.zeros(nv); row[:n]=-(v@chis[j])*v
            row[n+j*k:n+(j+1)*k]=np.einsum('i,kij,j->k',v,forms,v)
            rows.append(row); rhs.append(-float(v@v))
        for j in range(m):
            for i in range(n): cut(j,np.eye(n)[i])
            for a,b0 in combinations(range(n),2):
                for s in (-1,1): cut(j,(np.eye(n)[a]+s*np.eye(n)[b0])/np.sqrt(2))
        for i in range(n):
            for s in (-1,1):
                row=np.zeros(nv); row[i]=s; row[n+m*k+i]=-1
                rows.append(row); rhs.append(0)
        objective=np.r_[np.zeros(n),np.ones(m*k+n)]
        for iteration in range(35):
            ans=linprog(objective,A_ub=np.array(rows),b_ub=np.array(rhs),
                        bounds=[(None,None)]*n+[(0,None)]*(m*k+n),method='highs')
            assert ans.success, (t,mask,iteration,ans.message)
            d=ans.x[:n]; lam=ans.x[n:n+m*k].reshape(m,k); worst=float('inf')
            for j,(ch,la) in enumerate(zip(chis,lam)):
                A=(np.outer(d,ch)+np.outer(ch,d))/2-np.einsum('k,kij->ij',la,forms)
                eigen,V=np.linalg.eigh(A); worst=min(worst,eigen[0])
                for ii in range(n):
                    if eigen[ii]<.999999: cut(j,V[:,ii])
            if worst>.05: break
        else: raise AssertionError(('LOCATOR_NOT_A_PROOF',t,mask))
        found=False
        for denominator in (1,2,4,8,16,32,64,128,256,512,1024):
            di=[round(float(v)*denominator) for v in d]
            li=[[max(0,round(float(v)*denominator)) for v in row] for row in lam]
            try:
                for cell,lm in zip(cc,li):
                    A=block(di,lm,cell,p); minors=bareiss_minors(A)
                    independent_check(A,di,lm,cell,p,minors)
            except AssertionError: continue
            found=True; break
        assert found and di==frozen_d and li==frozen_lam
        receipt.append({'t':t,'mask':mask,'iteration':iteration,'rounding_denominator':denominator,
                        'd':di,'lam':li,'exact_checks_passed':True})
    obj={'scope':'NUMERIC_LOCATOR_WITH_EXACT_ROUNDING_TO_FROZEN_TABLE',
         'numpy':'2.3.5','scipy':'1.17.0','records':receipt}
    data=(json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode('ascii')
    out=Path('endpoint_full67_discovery.json'); out.write_bytes(data)
    print('FULL67_SOURCE_ONLY_NUMERIC_LOCATION_AND_EXACT_ROUNDING_PASS')
    print(out.name,len(data),hashlib.sha256(data).hexdigest())

def main():
    if sys.argv[1:]==['discover']: return discover()
    assert sys.argv[1:] in (['build'],['check'])
    data=build(); path=Path('endpoint_full67.json')
    if sys.argv[1]=='build': path.write_bytes(data)
    else: assert path.read_bytes()==data
    print('MAX_ENDPOINT_FAN_11_CERTIFICATES_85_PD_BLOCKS_850_MINORS_PASS')
    print('DEG7_BASE38_AND_DEG6_BASE88_FULL_SELECTED_CHAINS_PASS')
    print('TRIANGLE_LEAF94_AND_ACTUAL_FAN32_PAIRS_PASS')
    print('ACTUAL_OWN_COM_DEG7_CONTROL_S3_U2_H3_PASS')
    print(path.name,len(data),hashlib.sha256(data).hexdigest())
    print('TWO_APEX_MAX_ENDPOINT_FULL67_DURABLE_RECOVERY_PASS')

if __name__=='__main__': main()
```

Дополнительные копии, не заменяющие приведённую капсулу: source (`endpoint_full67.py`), точный полный отчёт (`endpoint_full67.json`), receipt восстановления поиска (`endpoint_full67_discovery.json`).
