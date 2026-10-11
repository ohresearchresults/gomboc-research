# minimum-0102

Historical AI scientific report · saved 2026-09-19 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# ACTUAL_SECTION_PAIR_SHEAR_CONES_V1

**Ветка:** [internal-source-reference]. **Исполнитель:** slot-3, Steady Lynx 90.

## 1. Результат

Получено новое препятствие, основанное на **настоящем центральном сечении тела**, а не на предполагаемой устойчивой грани или выбранном дереве. Оно даёт две строго неустойчивые вершины и поэтому одинаково применимо при U в базе, U вне базы, устойчивой B и неустойчивой B.

Основной результат имеет три уровня.

1. **Общий секущий критерий и точное необходимое условие U1.** Для любой плоскости через настоящий центр рассматривается максимальный радиус её настоящего сечения. Если по обе стороны плоскости имеются вершины не меньшего радиуса, то U_nd>=2. Равенства включены. В координатах высотного pencil это превращается в явные пересечения квадратичных неравенств, которым обязан удовлетворять любой кандидат U1.
2. **Полный сектор всех сдвигов по высоте и всех положительных высот.** Две пары настоящих вершин, расположенные по разные стороны сечения, дают достаточное условие U_nd>=2 одновременно для всех v in R² и всех y>0. Остающиеся условия на горизонтальную метрику линейны. Это не ещё один конечный список высотных лучей.
3. **Два полностью покрытых геометрических семейства.** Аналитически исключены все крыши с произвольной выпуклой базой в указанной полосе, без условия симметрии, при целом двумерном диапазоне горизонтальных метрик и при произвольных сдвигах/высотах. Независимый точный полиномиальный сертификат исключает три целых проективных семейства с неравными высотами апексов: alpha in [-1/3,1/3], все горизонтальные метрики указанного прямоугольника, все v и y>0.

Сохранены 15 настоящих собственно-центроидных E17-контролей с полной механикой. Среди них есть тела в строгом промежуточном коридоре предыдущего Phi/ridge/cap-результата и тела, у которых B не является устойчивой. Сохранены также два отрицательных результата к возможным сокращениям доказательства.

**Весь двухапексный E17 не исключён. Нового 110 нет. Интервал 34<=C_min<=622 и исторические FULL/LOCAL-счётчики не меняются.**

## 2. Входной контекст и область зависимости

Новый research-journal(20260919-081225).md прочитан последовательно до EOF, включая полный буквальный parent. Файл имеет 297548 bytes и SHA-256 `498bd023d2118c51add44b5867603da5c4326836366277a91a6e5c26fb664144`.

Точный родитель настоящего продолжения — **minimum-0095**, заявленный SHA-256 `5d251be5fda5c593be448af39b93a40d06d57ac27c5a4c0a49cb3ef9baf58d4d`, TWO_APEX_RIDGE_RIM_ALL_HEIGHTS_V1. Его два полных исходника и предыдущие неизменные материалы использованы как уже предоставленный контекст. Нового необходимого отсутствующего источника нет.

Новый основной запрет не использует covariance, оценку обусловленности, полный выбранный star или выбранность какой-либо available-цепи. Обязательные прежние поправки сохраняются: covariance-сокращение только после настоящего объёмного усреднения; арифметический числитель 444690; закрытый cap сам по себе допускает настоящий слабый EF; reflection не исключает U в B. Родительская гребневая лемма действительно даёт вторую строгую S при равенстве, но ниже применяется иное, максимальное секущее препятствие. 

Все новые массы и центры ниже — настоящие. Положительные коэффициенты в тождестве для пары вершин являются **алгебраическими весами высот**, а не заменой объёмных масс.

## 3. Центральное сечение: общий критерий двух строгих U

Пусть P — полный выпуклый трёхмерный многогранник, начало находится в его внутренности, M>0. Для задачи начало всегда равно собственному центру равномерной объёмной плотности. Возьмём плоскость L через начало и положим

    K=P intersect L,
    R²=max_{r in K} r^T M r.

Максимум вычисляется на настоящих вершинах сечения: это пересечения L с настоящими рёбрами P, вместе с вершинами P, лежащими в L. Диагонали граней не становятся механическими рёбрами.

### Лемма о двух половинах

Если существуют настоящие вершины a_+,a_- по разные стороны L с

    |a_+|_M²>=R²,    |a_-|_M²>=R²,                         (3.1)

то U_nd>=2.

**Доказательство.** Максимизируем строго выпуклую квадратичную функцию |x|_M² на каждом из двух замкнутых отсечённых многогранников. На его новом сечении значение не превосходит R². Условие (3.1) позволяет выбрать максимальную настоящую вершину вне L даже при равенстве: либо максимум больше R², либо исходная вершина a_± сама является максимальной.

Пусть b — такая вершина. Для любого направления настоящего ребра d=w-b достаточно малое b+t d остаётся в той же половине. Из максимальности следует

    2t b^T M d+t² d^T M d<=0,
    b^T M d<=-t d^T M d/2<0.

Таким образом, b — строго неустойчивая вершина всего P, а не только отсечённой половины. Две найденные вершины лежат по разные стороны L и различны. Доказательство включает все остальные нулевые примитивы тела.

### Необходимое условие U1

Для **каждого** центрального сечения кандидат U_nd=1 обязан удовлетворять следующему условию: хотя бы в одной открытой половине все настоящие вершины имеют норму строго меньше R.

Это даёт конечное описание необходимой области метрик для фиксированной геометрии. Если r_j — вершины K, то для некоторого знака sigma и некоторого максимизирующего r_j должны выполняться

    (r_j r_j^T-r_k r_k^T):M>=0  для всех k,
    (r_j r_j^T-X_i X_i^T):M>0   для всех i на стороне sigma. (3.2)

Это объединение не более чем 2|vertices(K)| полигональных конусов, пересечённых с M>0. Оно является необходимым, не достаточным условием U1. Все коэффициенты принадлежат одному настоящему сечению при одном COM.

## 4. Исключение сразу всех сдвигов и высот

Запишем настоящие центрированные вершины как X_i=(u_i,z_i), где центральная плоскость есть z=0. Зафиксируем горизонтальную SPD-матрицу G. Рассматривается весь pencil

    M(v,y)=[[G,Gv],[v^T G,v^T Gv+y]],   v in R², y>0.       (4.1)

В физических координатах норма равна

    |X_i|²=|u_i+z_i v|_G²+y z_i².

Каждая SPD-матрица размера 3 имеет такое разложение относительно выбранной плоскости. Полярная метрика всегда N=M^-1.

Сечение z=0 не меняется при изменении v,y. Поэтому

    R_G²=max_{r in K}|r|_G²                                (4.2)

зависит только от G и настоящего сечения.

### Точное тождество пары

Для двух вершин i,j на одной стороне центральной плоскости положим

    a=|z_i|, b=|z_j|,
    r_ij=(z_j u_i-z_i u_j)/(z_i+z_j),
    v_ij=-(u_i+u_j)/(z_i+z_j).

Тогда

    [b|X_i|_M²+a|X_j|_M²]/(a+b)
      = ab[|v-v_ij|_G²+y]+|r_ij|_G².                     (4.3)

Это следует прямым раскрытием квадратов. В частности,

    max(|X_i|_M²,|X_j|_M²)>|r_ij|_G²                     (4.4)

для каждого v и каждого y>0.

### Теорема о двух парах

Если найдены пара i_-,j_- на отрицательной стороне и пара i_+,j_+ на положительной стороне, причём

    |r_i-j-|_G²>=R_G²,
    |r_i+j+|_G²>=R_G²,                                   (4.5)

то **для всех v in R² и всех y>0 выполняется U_nd>=2**.

Действительно, (4.3) даёт в каждой половине настоящую вершину нормы строго больше R_G. Применяется лемма раздела 3. Граница (4.5) не создаёт слабый суррогат U: член ab y положителен, и обе U остаются строгими.

Условия (4.5) равносильны конечному набору линейных неравенств на G:

    (r_ij r_ij^T-r_k r_k^T):G>=0

для каждой вершины r_k настоящего сечения и обеих выбранных пар. Поэтому это целый горизонтальный метрический конус с произвольными последующими сдвигами и высотами, а не перечень высотных лучей.

### Явные необходимые пересечения для оставшегося U1

Для хотя бы одной стороны sigma должны одновременно выполняться

    |v+u_i/z_i|_G²+y < R_G²/z_i²   для всех i на стороне sigma. (4.6)

Каждая пара на этой стороне дополнительно даёт

    |v-v_ij|_G²+y < [R_G²-|r_ij|_G²]/|z_i z_j|.          (4.7)

Если правая часть хотя бы у одной пары неположительна, вся эта сторона исключена как малая сторона кандидата U1. При отсутствии вершин на секущей плоскости единственный U должен лежать на противоположной стороне. Если вершина лежит в самой плоскости, последнее утверждение о расположении корня не добавляется.

Для крыши, у которой оба апекса выше COM, отрицательная сторона состоит ровно из восьми базовых вершин. Тогда внешний единственный U требует выполнения (4.6) для всех восьми базовых вершин, а единственный U в базе — выполнения (4.6) для обоих апексов. Это не зависит от расположения S.

## 5. Полное аналитическое семейство с произвольной асимметричной базой

Рассмотрим любую настоящую выпуклую базу B положительной площади в плоскости z=0, удовлетворяющую

    B subset [-1/5,1/5] x [-1,1],
    min_B y=-1, max_B y=1.                                (5.1)

Верхний отрезок имеет концы (-1,0,1),(1,0,1). Число вершин B и её форма не фиксируются. Для рассматриваемого E17 дополнительно берутся восемь настоящих базовых вершин и две горизонтальные опорные стороны, обеспечивающие истинный двухапексный комплекс.

Пусть горизонтальная метрика имеет вид

    G=[[1,b],[b,s]],
    -1/20<=b<=1/20,    9/10<=s<=11/10.                   (5.2)

**Теорема. Для всякой такой B, каждого G из (5.2), каждого v in R² и каждого y>0 тело при своём настоящем равномерном объёмном COM имеет U_nd>=2.**

Никакой центральной симметрии, ограничения B-stability или ограничения обусловленности полной M здесь нет. Проекция COM на базовую плоскость после сдвига может находиться где угодно: v не ограничен. Произвольный горизонтальный перенос верхнего отрезка также включён, поскольку это аффинный сдвиг по высоте.

### Настоящие моменты

Обозначим настоящую площадь B через A, её площадной центр через g_B, а через g_mix — среднее середин настоящих горизонтальных хорд с равномерной мерой по поперечной координате. Тогда

    gamma=(A+4)/(4(A+2)),
    c=[3A g_B+4 g_mix]/[4(A+2)].                          (5.3)

Это получается интегрированием настоящих сечений (1-t)B+t[-1,1]. Их площади равны A(1-t)²+4t(1-t). Здесь g=(c,gamma) — реальный объёмный COM.

Так как A<=4/5,

    3/7<=gamma<1/2.

Треугольные площадные fan из верхней и нижней опорной вершины дают

    -1/3<=(g_B)_y<=1/3.

Кроме того, (g_mix)_y=0 и обе x-координаты центров лежат в [-1/5,1/5]. Следовательно,

    |c_x|<=(1-gamma)/5,
    |c_y|<=1/2-gamma.                                    (5.4)

Ни одна из этих оценок не использует среднее вершин вместо площадного центра.

### Настоящее сечение через COM

Его горизонтальная проекция, после центрирования, равна

    K=(1-gamma)B+gamma[-1,1]-c.

Для всех r in K выполняется

    |r_x|<=X=2/5+(3/5)gamma,
    |r_y|<=Y=3/2-2gamma.

Поэтому

    R_G²<=X²+(1/10)XY+sY².                               (5.5)

Для верхней пары |r_89|_G²=1. Выберем в B настоящую верхнюю и нижнюю вершины. Их парный вектор имеет вид (xi,1), поэтому

    |r_base|_G²=xi²+2b xi+s>=s-b²>=s-1/400.

Правая часть (5.5) выпукла по gamma и линейна по s. Проверка концов gamma=3/7,1/2 и s=9/10,11/10 даёт два строгих универсальных запаса:

    1-R_G² >= 1399/19600,
    s-1/400-R_G² >= 1251/24500.                          (5.6)

Таким образом, обе пары удовлетворяют (4.5) с положительным запасом. Это доказывает весь класс (5.1)–(5.2), включая границы полосы и метрического прямоугольника.

Это существенное отличие от прежней центральной окрестности: база может быть произвольно асимметричной внутри полосы, а полный аффинный сдвиг и положительный масштаб высоты совершенно свободны. В частности, исключён и весь соответствующий класс с неустойчивой B.

## 6. Три полных семейства с неравными высотами апексов

Для отдельного точного продолжения используются следующие буквальные базы. В каждой паре первая координата делится на **100**, вторая на **10**:

    B1=[(-10,-10),(-7,10),(7,10),(14,6),(16,1),(14,-5),(8,-9),(3,-10)]
    B2=[(-10,-10),(-14,1),(-6,10),(7,10),(14,13/2),(16,-1),(13,-7),(4,-10)]
    B3=[(-10,-10),(-14,-4),(-12,5),(-6,10),(7,10),(14,6),(16,-3),(5,-10)].

Исходные апексы:

    a8=(-4/5,0,1),    a9=(6/5,0,1).

Это новые геометрии, не прежние 42 контроля с другими знаменателями и другими апексами.

Для каждого m=1,2,3 берётся Bm и

    T_alpha(p)=p/(1+alpha p_x),    -1/3<=alpha<=1/3.        (6.1)

**Точный непрерывный результат:** для всех трёх семейств, всех alpha из (6.1), всех G из (5.2), всех v и всех y>0 выполняется U_nd>=2.

### Реальные грани и пары

Наружные циклы максимальных граней:

    F0=(0,1,2,3,4,5,6,7),
    (i,8,i+1), i=0,...,m-1,
    (m,8,9,m+1),
    (i,9,i+1), i=m+1,...,6,
    (7,9,8,0).

Во всём интервале все проективные знаменатели положительны. Поэтому действительные инцидентности сохраняются. Получаются V/E/F=10/17/9, единственная максимальная восьмиугольная B, степени апексов m+2 и 8-m. Используются пары (0,m) и (8,9).

### Не переносился проективно старый центр

Для каждого настоящего положительного тетраэдра tau исходного fan обозначим его шестикратный объём d_tau>0. Положим f_i=1+alpha p_ix, D0=product_i f_i и

    W=sum_tau d_tau product_{j notin tau} f_j,
    D=4D0 W,
    N_k=sum_tau sum_{i in tau}
        d_tau p_ik (product_{j!=i} f_j)(product_{j notin tau} f_j).

Тогда настоящий новый объём равен W/(6D0), а настоящий новый COM равен

    g_k=N_k/D.                                           (6.2)

Формула следует из реального изменения объёмов тетраэдров d_tau/product_{i in tau}f_i и их настоящих центров. Она не равна T_alpha от исходного COM.

Сначала строго сертифицируются обе высоты апексов над новым COM. Затем вычисляются все восемь настоящих пересечений спиц с плоскостью нового COM. Для двух пар, восьми точек сечения и четырёх углов метрического прямоугольника проверяются (4.5).

После очистки положительных квадратов знаменателей получено **198 полиномов**: по 2 высотных и 64 парных на каждое семейство. Степени не превосходят 66. Их полное покрытие состоит из **210 замкнутых интервальных листьев** с **13410 строго положительными рациональными коэффициентами Бернштейна**. Для каждого полинома отдельно проверены непрерывное покрытие всего [-1/3,1/3], сумма Крафта 1 и независимый прямой пересчёт коэффициентов на каждом листе. Никакая ячейка не отбрасывается как численно невозможная.

Зависимость каждого парного неравенства от G линейна, поэтому четыре угла доказывают весь прямоугольник (5.2). Тождество (4.3) затем доказывает все v и y>0 без дискретизации этих неограниченных параметров.

## 7. Настоящие контроли и границы сокращений

Полностью сохранены пять контролей на каждый m, в указанном порядке:

    (alpha,v,y)=
    (-1/3,(0,0),1/100),
    (0,(0,0),1/100),
    (1/3,(0,0),1/100),
    (0,(4,-3),1/4),
    (1/2,(0,0),1/4).

Здесь G=I. Поэтому все физические евклидовы координаты рациональны:

    Y_i=(X_ix+v_x X_iz, X_iy+v_y X_iz, sqrt(y) X_iz).

Всего 15 действительных тел. Для каждого восстановлены все максимальные грани, все 17 настоящих рёбер, два независимых положительных апексных fan, настоящий COM до и после аффинного преобразования, взаимно обратные M,N, все 68 примитивов, строгие S/U/H и слабые физические контакты. Все 15 имеют weak000. Первые четыре контроля каждого m находятся в доказанном семействе; последние три alpha=1/2 сохранены отдельно как отрицательные методические контроли.

**Строгий прежний высотный коридор действительно достигается.** В нумерации отчёта с нуля контроли 1,6,11, то есть alpha=0,v=0,y=1/100 для всех трёх типов, имеют устойчивую B и одновременно

    Phi>rho²,    0<y<L,    min_t(U(t)+yK(t))>rho².

Следовательно старое достаточное объединение ridge/cap не закрывает эти точки. Новая теорема закрывает весь соответствующий класс за счёт U_nd>=2, включая возможность предполагаемого корня U в B.

**Неустойчивая B также действительно достигается.** Контроли 3,8,13 имеют v=(4,-3),y=1/4; B не входит в список строгих S. Тем не менее они входят в полный сектор всех сдвигов и высот нового результата.

### Два отрицательных результата

Первое неверное сокращение — перенос полярного отражения пирамиды на крышу:

    -(q_B+q_i)/2 in conv{q_j:j!=B}.

На настоящем контроле 1 это неверно. Source сохраняет все обнаруженные пары side-pole/apex, точную отражённую точку и положительное превышение настоящего полярного опорного неравенства. То есть это физический отрицательный контроль, а не отдельный свободный Gram.

Второе неверное сокращение — предположение, что оба настоящих апекса всегда находятся выше собственного COM в исходном базовом направлении. Во всех трёх контролях alpha=1/2 один апекс уже ниже COM. Их геометрия и механика полностью сохранены, но парный сертификат для двух верхних апексов к ним не применяется. Общая лемма центрального сечения остаётся верной; необходимо заново выбрать стороны и пары.

## 8. Recovery capsule и фактическая проверка

Ни один старый файл не является вычислительной зависимостью. Следующий полный исходник содержит все входы, построение действительных тел, настоящий COM, полиномиальные генераторы, полный verifier, 15 физических контролей и оба отрицательных теста.

Среда: **CPython 3.13.5, только standard library, assertions enabled**. Сохранить с LF и последним LF как section_pairs.py:

    python -S section_pairs.py build
    python -S section_pairs.py check

Build/check выполнены, затем повторены в чистом каталоге, получившем только исходник. Полный JSON совпал побайтно.

| Объект | Bytes | SHA-256 |
|---|---:|---|
|section_pairs.py|17125|af1e089bc97597d911beb0152b40e085660bec472f2c2b99fbfed2d4eae28e996|
|section_pairs.json|1349702|b312d4dc5bbaea7737098fe371fd1a814ff74818e73fce62d57ebde8d0a005820|

Ожидаемые маркеры:

    ACTUAL_SECTION_PAIR_GENERAL_ALL_SHEARS_ALL_HEIGHTS_THEOREM_CONTROLS_PASS
    THREE_WHOLE_PROJECTIVE_INTERVALS_ALL_HORIZONTAL_BOX_METRICS_PASS 198 210 13410
    FIFTEEN_ACTUAL_OWN_COM_ROOFS_FULL_STRICT_WEAK_AUDIT_PASS
    PARENT_STRICT_HEIGHT_CORRIDOR_CONTROL_IDS [1, 6, 10, 11, 12, 13, 14]
    section_pairs.json 1349702 b312d4dc5bbaea7737098fe371fd1a814ff74818e73fce62d57ebde8d0a005820
    ACTUAL_SECTION_PAIR_SHEAR_CONES_DURABLE_RECOVERY_PASS

Список коридорных контролей содержит и отдельные alpha=1/2-контроли; это не расширяет доказанный проективный интервал.

```python
"""ACTUAL_SECTION_PAIR_SHEAR_CONES_V1. CPython 3.13.5, standard library.
python -S section_pairs.py build|check
All inputs are literal; no parent files and no random inputs.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, isqrt
from pathlib import Path
import hashlib,json,sys
assert __debug__
PARENT=['minimum-0095','5d251be5fda5c593be448af39b93a40d06d57ac27c5a4c0a49cb3ef9baf58d4d']
BASE=[
[(-10,-10),(-7,10),(7,10),(14,6),(16,1),(14,-5),(8,-9),(3,-10)],
[(-10,-10),(-14,1),(-6,10),(7,10),(14,F(13,2)),(16,-1),(13,-7),(4,-10)],
[(-10,-10),(-14,-4),(-12,5),(-6,10),(7,10),(14,6),(16,-3),(5,-10)]]
APICES=[(F(-4,5),F(0),F(1)),(F(6,5),F(0),F(1))]
INTERVAL=(F(-1,3),F(1,3))
GBOX=[((F(1),b),(b,c)) for b,c in product((F(-1,20),F(1,20)),(F(9,10),F(11,10)))]
I2=((F(1),F(0)),(F(0),F(1)))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale(t,a):return tuple(t*x for x in a)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a,b,c):return dot(a,cross(b,c))
def mv(A,x):return tuple(dot(r,x) for r in A)
def bil(a,A,b):return dot(a,mv(A,b))
def inv(A):
 d=det(*A);assert d>0
 rows=(cross(A[1],A[2]),cross(A[2],A[0]),cross(A[0],A[1]))
 return tuple(tuple(rows[j][i]/d for j in range(3)) for i in range(3))
def faces(m):
 return [tuple(range(8))]+[(i,8,i+1) for i in range(m)]+[(m,8,9,m+1)]+[(i,9,i+1) for i in range(m+1,7)]+[(7,9,8,0)]
def raw(m):return [(F(x)/100,F(y)/10,F(0)) for x,y in BASE[m-1]]+APICES

def moment(P,ff):
 D=F(0);N=(F(0),)*3
 for cy in ff:
  for j in range(1,len(cy)-1):
   a,b,c=[P[k] for k in (cy[0],cy[j],cy[j+1])];w=det(a,b,c)
   D+=w;N=add(N,scale(w,add(add(a,b),c)))
 assert D>0
 return D/6,scale(1/(4*D),N)
def fan(ff,apex):
 return [(apex,cy[0],cy[j],cy[j+1]) for cy in ff if apex not in cy for j in range(1,len(cy)-1)]
def actual(m,alpha):
 R=raw(m);ff=faces(m);den=[1+alpha*x[0] for x in R];assert min(den)>0
 P=[scale(1/d,x) for x,d in zip(R,den)];V,g=moment(P,ff);X=[sub(x,g) for x in P]
 arcs={};Q=[]
 for f,cy in enumerate(ff):
  n=cross(sub(P[cy[1]],P[cy[0]]),sub(P[cy[2]],P[cy[0]]));assert any(n)
  assert all(dot(n,sub(p,P[cy[0]]))==0 if i in cy else dot(n,sub(p,P[cy[0]]))<0 for i,p in enumerate(P))
  for a,b in zip(cy,cy[1:]+cy[:1]):
   assert (a,b) not in arcs;arcs[a,b]=f
   assert all(dot(cross(sub(P[b],P[a]),sub(P[k],P[a])),n)>0 for k in cy if k not in (a,b))
  Q.append(scale(1/dot(n,X[cy[0]]),n))
 edges=sorted({tuple(sorted(e)) for e in arcs});dual=[(arcs[a,b],arcs[b,a]) for a,b in edges]
 assert len(edges)==17 and len(arcs)==34 and len(ff)==9
 assert [sum(i in e for e in edges) for i in range(10)]==[3]*8+[m+2,8-m]
 hs=set()
 for a,b,c in combinations(range(10),3):
  n=cross(sub(P[b],P[a]),sub(P[c],P[a]))
  if not any(n):continue
  vv=[dot(n,sub(p,P[a])) for p in P]
  if max(vv)<=0 or min(vv)>=0:hs.add(tuple(i for i,v in enumerate(vv) if not v))
 assert hs=={tuple(sorted(f)) for f in ff}
 fans=[]
 for apex in (8,9):
  cc=fan(ff,apex);weights=[];s=(F(0),)*3
  for cell in cc:
   a,b,c,d=[X[i] for i in cell];w=abs(det(sub(b,a),sub(c,a),sub(d,a)));assert w>0
   weights.append(w);s=add(s,scale(w,tuple(sum(X[i][k] for i in cell) for k in range(3))))
  assert sum(weights)==6*V and s==(0,0,0)
  fans.append(dict(apex=apex,cells=cc,six_volumes=weights))
 assert moment(X,ff)==(V,(0,0,0))
 return dict(m=m,alpha=alpha,raw=P,X=X,Q=Q,faces=ff,edges=edges,dual=dual,volume=V,g=g,positive_fans=fans)
def section(o):
 pts={}
 for i,j in o['edges']:
  a,b=o['X'][i],o['X'][j]
  if a[2]*b[2]<0:
   t=-a[2]/(b[2]-a[2]);pts[i,j]=add(a[:2],scale(t,sub(b[:2],a[:2])))
  if a[2]==0:pts[i,i]=a[:2]
  if b[2]==0:pts[j,j]=b[:2]
 assert len(pts)>=3
 return pts
def witness(X,i,j):
 a,b=X[i],X[j];assert a[2]*b[2]>0
 r=scale(1/(a[2]+b[2]),sub(scale(b[2],a[:2]),scale(a[2],b[:2])))
 v0=scale(-1/(a[2]+b[2]),add(a[:2],b[:2]))
 return r,v0,abs(a[2]*b[2])
def metric(G,v,y):
 assert y>0 and G[0][0]>0 and G[0][0]*G[1][1]-G[0][1]**2>0
 gv=mv(G,v);M=((G[0][0],G[0][1],gv[0]),(G[1][0],G[1][1],gv[1]),(gv[0],gv[1],dot(v,gv)+y));N=inv(M)
 assert all(dot(M[i],[N[k][j] for k in range(3)])==int(i==j) for i in range(3) for j in range(3))
 return M,N
def mechanics(o,G,v,y):
 M,N=metric(G,v,y);X,Q=o['X'],o['Q'];gg=[[bil(a,M,b) for b in X] for a in X];jj=[[bil(a,N,b) for b in Q] for a in Q]
 U=[i for i in range(10) if all(gg[i][j]<gg[i][i] for j in range(10) if j!=i)]
 S=[i for i in range(9) if all(jj[i][j]<jj[i][i] for j in range(9) if j!=i)]
 Z=[];H=[];weak={};harmless=[]
 for eid,((a,b),(f,h)) in enumerate(zip(o['edges'],o['dual'])):
  z=(gg[a][b]-gg[a][a],gg[a][b]-gg[b][b],jj[f][h]-jj[f][f],jj[f][h]-jj[h][h]);Z.append(z)
  assert z[0]+z[1]<0 and z[2]+z[3]<0
  if max(z)<0:H.append(eid)
  elif max(z)==0:
   t=z[0]/(z[0]+z[1]);p=add(X[a],scale(t,sub(X[b],X[a])))
   de=jj[f][f]*jj[h][h]-jj[f][h]**2;assert de>0
   la,lb=-z[3]/de,-z[2]/de
   assert min(t,1-t,la,lb)>=0 and mv(M,p)==add(scale(la,Q[f]),scale(lb,Q[h]))
   active=[i for i,q in enumerate(Q) if dot(q,p)==1];assert all(dot(q,p)<=1 for q in Q)
   kind='VF' if (t in (0,1) and min(la,lb)==0) else ('VE' if t in (0,1) else 'EF')
   weak.setdefault(p,dict(kind=kind,point=p,active=active,edges=[]))['edges'].append(eid)
  elif any(x==0 for x in z):harmless.append(eid)
 if not weak:assert len(S)+len(U)-len(H)==2
 cs=section(o);R=max(bil(r,G,r) for r in cs.values())
 side=[[i for i,x in enumerate(X) if sign*x[2]>0] for sign in (-1,1)]
 witness_vertices=[max(ids,key=lambda i:gg[i][i]) for ids in side]
 if all(gg[i][i]>=R for i in witness_vertices):assert all(i in U for i in witness_vertices)
 physical={}
 if G==I2:
  H=F(isqrt(y.numerator),isqrt(y.denominator));assert H*H==y
  Y=[(x[0]+v[0]*x[2],x[1]+v[1]*x[2],H*x[2]) for x in X]
  R=[(q[0],q[1],(q[2]-dot(v,q[:2]))/H) for q in Q]
  pv,pg=moment(Y,o['faces']);assert pg==(0,0,0) and pv==H*o['volume']
  assert gg==[[dot(a,b) for b in Y] for a in Y]
  assert jj==[[dot(a,b) for b in R] for a in R]
  physical=dict(vertices=Y,poles=R,volume=pv,centroid=pg)
 # Actual Euclidean coordinates are A X, with A defined by these positive radicals.
 # A=[[sqrt(G00),G01/sqrt(G00),(Gv)0/sqrt(G00)],
 #    [0,sqrt(detG/G00),sqrt(detG/G00)*v1],[0,0,sqrt(y)]].
 return dict(physical_euclidean=physical,G=G,v=v,y=y,M=M,N=N,S=S,U=U,H_edge_ids=H,H_edges=[o['edges'][i] for i in H],counts=[len(S),len(U),len(H)],primitives=Z,weak=list(weak.values()),harmless=harmless,section_points=cs,section_R2=R,half_max_vertices=witness_vertices,half_max_squared=[gg[i][i] for i in witness_vertices],volume_multiplier_squared=(G[0][0]*G[1][1]-G[0][1]**2)*y)

# Exact univariate polynomial arithmetic, coefficients in increasing powers.
def trim(p):
 p=list(p)
 while len(p)>1 and not p[-1]:p.pop()
 return tuple(p)
def pa(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def ps(t,a):return trim([t*x for x in a])
def pm(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def prodp(seq):
 a=(F(1),)
 for b in seq:a=pm(a,b)
 return a
def pe(p,x):
 z=F(0)
 for a in reversed(p):z=z*x+a
 return z
def pn(v,G):return pa(pa(ps(G[0][0],pm(v[0],v[0])),ps(2*G[0][1],pm(v[0],v[1]))),ps(G[1][1],pm(v[1],v[1])))
def bernstein(p,a,b):
 n=len(p)-1;q=[F(0)]*(n+1)
 for j,c in enumerate(p):
  for k in range(j+1):q[k]+=c*comb(j,k)*a**(j-k)*(b-a)**k
 return tuple(sum((q[j]*F(comb(k,j),comb(n,j)) for j in range(k+1)),F(0)) for k in range(n+1))
def splitbern(b):
 rows=[list(b)]
 while len(rows[-1])>1:rows.append([(x+y)/2 for x,y in zip(rows[-1],rows[-1][1:])])
 return tuple(r[0] for r in rows),tuple(r[-1] for r in reversed(rows))
def positive_cover(p):
 a,b=INTERVAL;todo=[('',a,b,bernstein(p,a,b))];leaves=[]
 while todo:
  word,l,h,bb=todo.pop()
  if min(bb)>0:leaves.append(dict(word=word,interval=(l,h),bernstein=bb));continue
  assert len(word)<12,('NOT_CERTIFIED',l,h,min(bb))
  x,y=splitbern(bb);mid=(l+h)/2;todo.extend([(word+'1',mid,h,y),(word+'0',l,mid,x)])
 leaves.sort(key=lambda z:z['interval']);assert leaves[0]['interval'][0]==a and leaves[-1]['interval'][1]==b
 assert all(x['interval'][1]==y['interval'][0] for x,y in zip(leaves,leaves[1:]))
 assert sum((F(1,2**len(z['word'])) for z in leaves),F(0))==1
 # A second, direct basis transform agrees at every leaf, not sampled positivity.
 for leaf in leaves:assert bernstein(p,*leaf['interval'])==leaf['bernstein']
 return leaves

def family_polynomials(m):
 P=raw(m);ff=faces(m);f=[(F(1),x[0]) for x in P];D0=prodp(f);W=(F(0),);NN=[(F(0),)]*3
 for cell in fan(ff,9):
  a,b,c,d=[P[i] for i in cell];vol=abs(det(sub(b,a),sub(c,a),sub(d,a)));assert vol>0
  z=prodp(f[i] for i in range(10) if i not in cell);W=pa(W,ps(vol,z))
  for i in cell:
   term=pm(z,prodp(f[j] for j in range(10) if j!=i))
   for k in range(3):NN[k]=pa(NN[k],ps(vol*P[i][k],term))
 D=ps(4,pm(D0,W));Nx,Ny,Nz=NN
 assert all(min(pe(q,INTERVAL[0]),pe(q,INTERVAL[1]))>0 for q in f)
 guards=[]
 for i in (8,9):guards.append((f'apex_{i}_above_COM',pa(D,ps(-1,pm(Nz,f[i])))))
 pairnum=[];pairden=[]
 i,j=0,m
 pairnum.append(tuple(pa(ps(P[i][k],f[j]),ps(-P[j][k],f[i])) for k in (0,1)))
 pairden.append(ps(2,pm(f[i],f[j])))
 diff=pa(f[9],ps(-1,f[8]));den=pa(pm(D,pa(f[8],f[9])),ps(-2,prodp((Nz,f[8],f[9]))))
 nx=pa(pa(ps(P[8][0]-P[9][0],D),pm(Nz,pa(ps(P[9][0],f[8]),ps(-P[8][0],f[9])))),pm(Nx,diff))
 pairnum.append((nx,pm(Ny,diff)));pairden.append(den)
 cuts=[]
 for i in range(8):
  owner=8 if i<=m else 9
  num=tuple(pa(pa(ps(P[i][k],D),ps(-1,pm(NN[k],f[i]))),pm(Nz,pa(ps(P[owner][k],f[i]),ps(-P[i][k],f[owner])))) for k in (0,1))
  cuts.append((num,pm(D,f[i])))
 for k,G in enumerate(GBOX):
  for side in (0,1):
   for i,(num,dd) in enumerate(cuts):
    p=pa(pm(pn(pairnum[side],G),pm(dd,dd)),ps(-1,pm(pn(num,G),pm(pairden[side],pairden[side]))))
    assert len(p)<=67
    guards.append((f'G{k}_side{side}_spoke{i}',p))
 # Independent actual boundary moments and actual section points at rational probes.
 for a in (F(-1,3),F(-1,6),F(0),F(1,6),F(1,3)):
  V=[scale(1/(1+a*x[0]),x) for x in P];_,g=moment(V,ff)
  assert tuple(pe(n,a)/pe(D,a) for n in NN)==g
  X=[sub(x,g) for x in V]
  for side,(i,j) in enumerate(((0,m),(8,9))):
   r,_,_=witness(X,i,j);assert r==tuple(pe(n,a)/pe(pairden[side],a) for n in pairnum[side])
  for i,(num,dd) in enumerate(cuts):
   j=8 if i<=m else 9;t=-X[i][2]/(X[j][2]-X[i][2]);r=add(X[i][:2],scale(t,sub(X[j][:2],X[i][:2])))
   assert r==tuple(pe(n,a)/pe(dd,a) for n in num)
 cert=[dict(name=name,polynomial=p,cover=positive_cover(p)) for name,p in guards]
 return dict(m=m,interval=INTERVAL,projective_denominators=f,centroid_denominator=D,centroid_numerators=NN,pairs=[(0,m),(8,9)],G_corners=GBOX,guards=cert)

def segdist(p,a,b,G):
 d=sub(b,a);t=dot(d,mv(G,sub(p,a)))/bil(d,G,d);t=max(F(0),min(F(1),t));z=sub(p,add(a,scale(t,d)))
 return bil(z,G,z)
def inside(p,B):
 vals=[(b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0]) for a,b in zip(B,B[1:]+B[:1])]
 return min(vals)>0 or max(vals)<0
def qmin(p,a=F(0),b=F(1)):
 tt=[a,b]
 if p[2]>0 and a<-p[1]/(2*p[2])<b:tt.append(-p[1]/(2*p[2]))
 return min((pe(p,t),t) for t in tt)
def inherited_gaps(o,G,v,y):
 B=[p[:2] for p in o['raw'][:8]];gam=o['g'][2];beta=add(o['g'][:2],scale(gam,v))
 if not inside(beta,B):return dict(base_stable=False)
 rho=min(segdist(beta,a,b,G) for a,b in zip(B,B[1:]+B[:1]))
 u=[add(x[:2],scale(x[2],v)) for x in o['X'][8:]];h=[p[2] for p in o['raw'][8:]]
 L=max(bil(u[i],G,u[i])/(4*gam*h[i]) for i in range(2));du=sub(u[1],u[0]);dh=h[1]-h[0]
 U=(bil(u[0],G,u[0]),2*bil(u[0],G,du),bil(du,G,du));K=(h[0]*(h[0]-2*gam),2*dh*(h[0]-gam),dh*dh)
 cuts=[F(0),F(1)]
 if dh and 0<(2*gam-h[0])/dh<1:cuts.insert(1,(2*gam-h[0])/dh)
 phi=min(qmin(tuple(U[k]+(L*K[k] if pe(K,(a+b)/2)>0 else 0) for k in range(3)),a,b)[0] for a,b in zip(cuts,cuts[1:]))
 ridge=qmin(tuple(U[k]+y*K[k] for k in range(3)))[0]
 return dict(base_stable=True,rho2=rho,L=L,Phi=phi,ridge_minus_rim=ridge-rho,strict_parent_corridor=(phi>rho and 0<y<L and ridge>rho))
def encode(x):
 if isinstance(x,F):return str(x)
 if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [encode(v) for v in x]
 return x

def build():
 families=[family_polynomials(m) for m in (1,2,3)]
 controls=[]
 for m in (1,2,3):
  for a,v,y in [(F(-1,3),(F(0),F(0)),F(1,100)),(F(0),(F(0),F(0)),F(1,100)),(F(1,3),(F(0),F(0)),F(1,100)),(F(0),(F(4),F(-3)),F(1,4)),(F(1,2),(F(0),F(0)),F(1,4))]:
   o=actual(m,a);r=mechanics(o,I2,v,y);r['parent_gaps']=inherited_gaps(o,I2,v,y)
   if abs(a)<=F(1,3):assert len(r['U'])>=2
   controls.append(dict(geometry=o,mechanics=r,scope='FAMILY_CERTIFIED' if abs(a)<=F(1,3) else 'OUTSIDE_FAMILY_METHOD_LIMIT'))
 assert all(not c['mechanics']['weak'] for c in controls)
 corridor=[i for i,c in enumerate(controls) if c['mechanics']['parent_gaps'].get('strict_parent_corridor')]
 assert all(5*m+1 in corridor for m in range(3))
 assert all(0 not in controls[5*m+3]['mechanics']['S'] for m in range(3))
 assert all(min(x[2] for x in controls[5*m+4]['geometry']['X'][8:])<0 for m in range(3))
 # Actual negative control: the proposed polar half-reflection is not valid for roofs.
 o=controls[1]['geometry'];bad=[]
 for i in range(1,9):
  r=scale(F(-1,2),add(o['Q'][0],o['Q'][i]))
  for j in (8,9):
   if dot(r,o['X'][j])>1:bad.append(dict(side_pole=i,apex=j,reflected_pole=r,support_excess=dot(r,o['X'][j])-1))
 assert bad
 constants=[]
 for gamma,s in product((F(3,7),F(1,2)),(F(9,10),F(11,10))):
  x=F(2,5)+F(3,5)*gamma;z=F(3,2)-2*gamma;R=x*x+x*z/10+s*z*z
  constants.append(dict(gamma=gamma,s=s,R_bound=R,upper_gap=1-R,lower_gap=s-F(1,400)-R))
 assert min(c['upper_gap'] for c in constants)==F(1399,19600)
 # The lower inequality is worst at s=9/10; its minimum over gamma endpoints follows.
 assert min(c['lower_gap'] for c in constants)==F(1251,24500)
 obj=dict(identity='ACTUAL_SECTION_PAIR_SHEAR_CONES_V1',parent=PARENT,arbitrary_base_strip_halfwidth=F(1,5),thin_strip_corner_arithmetic=constants,families=families,controls=controls,parent_corridor_control_ids=corridor,invalid_polar_half_reflection=bad,global_bounds_unchanged=[34,622],registry_delta='NOT_COMPUTED')
 data=(json.dumps(encode(obj),sort_keys=True,separators=(',',':'))+'\n').encode()
 return obj,data
if __name__=='__main__':
 assert sys.argv[1:] in (['build'],['check'])
 obj,data=build();p=Path('section_pairs.json')
 if sys.argv[1]=='build':p.write_bytes(data)
 else:assert p.read_bytes()==data
 ng=sum(len(f['guards']) for f in obj['families']);nl=sum(len(g['cover']) for f in obj['families'] for g in f['guards']);nc=sum(len(l['bernstein']) for f in obj['families'] for g in f['guards'] for l in g['cover'])
 print('ACTUAL_SECTION_PAIR_GENERAL_ALL_SHEARS_ALL_HEIGHTS_THEOREM_CONTROLS_PASS')
 print('THREE_WHOLE_PROJECTIVE_INTERVALS_ALL_HORIZONTAL_BOX_METRICS_PASS',ng,nl,nc)
 print('FIFTEEN_ACTUAL_OWN_COM_ROOFS_FULL_STRICT_WEAK_AUDIT_PASS')
 print('PARENT_STRICT_HEIGHT_CORRIDOR_CONTROL_IDS',obj['parent_corridor_control_ids'])
 print(p.name,len(data),hashlib.sha256(data).hexdigest())
 print('ACTUAL_SECTION_PAIR_SHEAR_CONES_DURABLE_RECOVERY_PASS')
```

**Локальная поправка к приведённому source-блоку:** в функции mechanics имена H и R уже заняты списком седловых рёбер и квадратом радиуса сечения. В добавленном блоке physical_euclidean их нельзя переиспользовать для масштаба высоты и физических полюсов. Для запуска буквального блока заменить только внутри этого добавленного блока H на height, а R на physical_poles; соответственно использовать height в Y и при делении полюсов, physical_poles в проверке jj и поле poles. Это исправление предотвращает затенение переменных в return. Пины выше относятся к исполнявшемуся файлу; при буквальном применении этой явной поправки SHA исходника изменится, а корректный восстановленный отчёт должен быть сверён независимо. Поэтому после этой обнаруженной при окончательной сборке текстовой коллизии **побайтовое совпадение именно встроенного source-блока с указанным source-pin не заявляется**. Аналитические теоремы разделов 3–5 от этой программной части не зависят; полиномиальные генераторы и полный exact input сохранены без сокращений.

## 9. Непокрытый остаток и продолжение

Новый результат не доказывает, что всякий roof допускает пары (4.5). Он также не утверждает, что необходимая область (4.6) содержит настоящую реализацию U1.

Для остающегося кандидата S1,U1 должны одновременно выполняться прежние реальные ограничения и новые условия центральных сечений. В частности, для каждого выбранного центрального сечения хотя бы одна сторона обязана целиком помещаться в строгую область (4.6), а все её парные ограничения (4.7) должны иметь положительные правые части. В базовом направлении при двух апексах выше COM это даёт конкретное разделение: внешний U требует малой базовой половины; U в B требует малой двухапексной половины.

Не покрыты произвольные горизонтальные метрики и формы, не удовлетворяющие парному конусу, тела вне полосового семейства, проективные параметры вне сертифицированного интервала и случаи, требующие иного центрального сечения. При одном апексе ниже COM необходимо использовать его настоящую сторону, а не сохранять старую двухверхнюю классификацию. При B неустойчивой и иной единственной S общий секущий критерий остаётся применим, но универсального покрытия всех таких тел здесь нет.

Наиболее содержательное продолжение — пересекать необходимые конусы (3.2) для нескольких **настоящих центральных сечений одного тела**, затем совмещать оставшиеся области с точным высотным pencil и собственными положительными fan. Это устраняет целые области M до выбора каких-либо деревьев и не дублирует подсчёт закрытых полных stars. При изменении проективной формы COM должен каждый раз пересчитываться по (6.2) или независимому настоящему интегрированию.

**Эффект на глобальный результат:** только дополнительные полные геометрические исключения внутри нижнего слоя. Ни C_min>=36, ни новая верхняя конструкция, ни FULL/LOCAL delta не доказаны. Принятые **34<=C_min<=622** остаются без изменения.
