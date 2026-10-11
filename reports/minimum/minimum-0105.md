# minimum-0105

Historical AI scientific report · saved 2026-09-19 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# RAVEN_INDEPENDENT_EAR_OWN_COM_MILP_V1

## 1. Результат и существенное ограничение

**Новый перечисленный exact110-экземпляр в этом продолжении не принят.** Получен другой конструктивный механизм: для конечного семейства совместимых удалений настоящих вершин задача сохранения собственного однородного strict110weak000 сводится к **бинарной линейной задаче с точными коэффициентами**, причём собственный объёмный центр и все физические слабые контакты входят в эту задачу, а не проверяются относительно назначенного начала.

Параллельно численный локатор вышел далеко за пределы старой семиуровневой архитектуры. Адаптивное добавление настоящих опорных точек гладкого прототипа дало конечные облака с пересчитанным объёмным центром и floating-census `(1,1,0)`. После симметризации, округления координат к сетке `10^-10` и удаления совместимых пар вершин численный этап дошёл до входа из **10326 целочисленно заданных точек**.

Однако **точное согласование максимальных граней, моментов и weak-census этого входа не завершено**. После записи входного массива и запуска целочисленного построителя последующие обращения к вычислительной среде стали возвращать `ServerError`. Не получены завершённый точный отчёт, его SHA-256 и аутентифицированная выгрузка полного координатного checkpoint в текст handoff. Поэтому этот численный вход остаётся **ephemeral, не является долговечным exact successor и не даёт новой принятой верхней границы**. Последний принятый самостоятельный exact endpoint этой ветви остаётся аналитическим рецептом родителя; лучший общий верхний пример остаётся C622.

Ниже сохранены доказанный механизм, полный аналитический контроль его слабой границы и исполнимый источник численного маршрута. Источник маршрута — восстановление метода и параметров, **не утверждение о побайтном восстановлении потерянного терминального массива**: в частности, использованный ограниченный по времени MILP-локатор не определяет переносимую последовательность всех бинарных решений.

## 2. Прочитанные источники и родительство

Полностью прочитан текущий `research-journal(20260919-095436).md`: **333289 байт, 2456 строк**, SHA-256:

`707b380f34141d81321e7669d4c1a2616faa24a9a80c884ccdf823096c3a7bc3`.

Буквальный parent — `minimum-0099`, **50892 байта**, SHA-256:

`e2e0a0b9aa8335049f730cfc70a1499089685ddd7ccb178848df7ad46f07f849`.

Его основной источник `raven_quantitative_cap.py` — **12901 байт**, SHA-256:

`f6e0aa811c7ae075b95e81247b5b2d14f1b87dfabb3b4db424f29a47e678467e`.

Неизменённые ранее предоставленные источники не были заново подменены краткими извлечениями. Буквальный parent, а не отличающаяся предпубликационная JSON-оболочка в дополнительном zip, использован как источник авторитетного результата. Научного конфликта с parent не найдено.

Файлы C622 не использовались. Ни численный маршрут, ни новая теорема об удалениях не являются его потомками. Новая геометрия не сохраняет старые семь меридиональных узлов и не получается одной лишь заменой общего углового многоугольника.

## 3. Что практически исследовалось

### 3.1. Другой конечный маршрут

Использовалось гладкое тело с `ε=1/25`, `a=3π/2`:

    Φ(z)=a(z−z³/3),
    c(z)=ε(cosΦ(z),sinΦ(z)),
    K={(c(z)+sqrt(1−z²)u,z): |u|≤1, −1≤z≤1}.

На каждом шаге строилась настоящая численная выпуклая оболочка, при необходимости отсекалась плоскостью, и **заново интегрировались объём и первый момент этой конечной оболочки**. Гладкий COM=0 не подставлялся вместо конечного COM.

Добавлялась вершина

    A=(1+ε+1/1000,0,0),

и использовалось отсечение

    x1≥−1+ε+1/500=−0.958.

При лишней неустойчивой вершине добавлялась точка поддержки K в направлении её радиального вектора относительно вычисленного конечного COM. При лишней устойчивой грани — точка поддержки в направлении её нормали. Аналогично использовались направления радиальных проекций на седловые рёбра. Это адаптация по фактической механике конечного тела, а не глобальная сетка с фиксированным μ.

Для нормали `n=(nx,ny,nz)`, `s=sqrt(nx²+ny²)>0`, высота опорной точки определяется единственным нулём

    εa(1−z²)(−nx sinΦ(z)+ny cosΦ(z))
      −s z/sqrt(1−z²)+nz=0.

После этого

    Y(n)=(c(z)+sqrt(1−z²)(nx,ny)/s,z).

Уникальность здесь следует из строгой вогнутости соответствующего опорного профиля при выбранном ε. В численной программе корень вычислялся `brentq`; принятность конечного тела из этого вычисления сама по себе не следует.

### 3.2. Диагностированная ошибка первоначального seed

В первом seed были дополнительно включены точки `(ε,0,±1)`. Они **не лежат на выбранном K**: правильные точки при `z=±1` имеют координаты `(-ε,0,±1)`. Первое облако всё равно определяло обычное однородное выпуклое тело, но уже не заявленную аппроксимацию K. Две неправильные выступающие точки объясняли сохранявшиеся лишние U.

Ошибка была обнаружена по координатам неустойчивых вершин, после чего обе точки удалены и заменены правильными. Она не скрыта в recovery-коде: исторический маршрут воспроизводит эту фазу отдельно и исправляет её до терминальной конструкции.

### 3.3. Сокращение числа точек

После достижения floating-census `(1,1,0)` координаты были округлены к целой сетке с знаменателем `10^10`. Затем использовалась точная на уровне входных целых симметрия

    R(x,y,z)=(x,−y,−z).

Она физически гарантирует `gy=gz=0` для равномерного объёма; это не свободное назначение двух компонент центра.

Удалялись пары `(v,Rv)` с непересекающимися локальными окрестностями. Для каждой предлагаемой пары вычислялись действительные удаляемые объём и первый момент. MILP выбирал бинарный набор удалений с малым суммарным остатком первого момента. После каждого принятого набора **снова строилась вся оболочка и пересчитывался её собственный центр**, затем повторялся численный census.

Исполненный численный вариант балансировал момент, но **ещё не содержал полного линейного weak-сертификата**, доказанного в разделах 4–6. Это важное различие между фактически использованным локатором и новым точным механизмом.

### 3.4. Что численные результаты не доказывают

Объединение почти совпадающих численных плоскостей использовало допуск. Поэтому даже `(1,1,0)` на этом этапе не исключает ошибку в максимальности граней или скрытый слабый пакет. Точное объединение копланарных граней и проверка всех четырёх примитивов обязательны.

Целочисленный инкрементальный построитель успел сообщить **20564 граничных треугольника** для последнего входа. Это не число максимальных граней и не завершённый сертификат оболочки. Последующего принятого вывода `own110weak000` нет.

Неудача точного завершения здесь связана с незавершённой проверкой и потерей доступа к исполнению, а не с доказанной невозможностью выбранного тела или архитектуры.

## 4. Точная линейная геометрия пространства опорных центров

Пусть фиксирован настоящий выпуклый 3-полиэдр P с вершинами `v_i`, максимальными гранями

    n_f·x≤h_f,

и одной фиксированной рациональной SPD-метрикой M. Всюду `N=M^-1`. Пока `g∈int P`, положим

    a_f(g)=h_f−n_f·g>0.

Для настоящего ребра с концами `i,j` и инцидентными максимальными гранями `f,h` определим четыре числителя:

    L_e,0(g)=(v_i−g)^T M(v_j−v_i),
    L_e,1(g)=(v_j−g)^T M(v_i−v_j),

    L_e,2(g)=(n_f^T N n_h)a_f(g)
                −(n_f^T N n_f)a_h(g),
    L_e,3(g)=(n_h^T N n_f)a_h(g)
                −(n_h^T N n_h)a_f(g).

**Все четыре функции аффинны по g.** У полярных примитивов отброшены только положительные знаменатели:

    q_f(g)=n_f/a_f(g),
    q_f(g)^T N(q_h(g)−q_f(g))
      =L_e,2(g)/(a_f(g)^2 a_h(g)).

Следовательно, физический критерий ребра можно записать без независимой полярной центровки и без квадратичного поиска по g:

    настоящее ребро несёт равновесие
      ⇔ L_e,k(g)≤0 для всех k=0,1,2,3.                 (A)

Все четыре строгих отрицательных знака дают строгий H. Наличие нуля при остальных неположительных даёт физический VE, EF или VF-пакет. Если хотя бы один числитель положителен, ребро не несёт равновесия; другие нули могут быть безвредны.

Для primal-части (A) следует непосредственно из проекции на прямую ребра. Если `e=v_j−v_i`, то

    L_e,0+L_e,1=−e^TMe<0,
    t_foot=L_e,0/(L_e,0+L_e,1).

Два неположительных primal-примитива эквивалентны `t_foot∈[0,1]`. Аналогичный критерий для отрезка между двумя полюсами определяет принадлежность радиальной нормали нормальному конусу ребра. Совместность использует именно `N=M^-1`.

Отсюда точное множество опорных центров proper110 для **фиксированных P,M** имеет описание

    int P \ ⋃_e {g: L_e,k(g)≤0 для всех четырёх k}.    (B)

Действительно, вне объединения в (B) нет ни седловых, ни слабых рёберных равновесий, а слабые вершины и слабые грани также попали бы в один из этих рёберных пакетов. Остаются только строгие S и U. Их индексы равны +1; сумма индексов на сферической границе равна2, и существуют как минимум один минимум и один максимум. Поэтому `S=U=1`.

Важно: (B) — утверждение о механике относительно внутреннего референса. Оно **ещё не делает g объёмным центром**. Следующий раздел устраняет именно этот разрыв для реального семейства изменений тела.

## 5. Совместимые настоящие удаления и их объёмные моменты

### 5.1. Проверяемая область семейства

Пусть `v_1,…,v_k` — удаляемые вершины P. Предположим:

1. Никакие две из них не лежат на одной максимальной грани.
2. Их замкнутые множества настоящих рёберных соседей попарно не пересекаются.
3. Среди неудаляемых вершин заранее сохранены четыре аффинно независимые точки.

Для `b∈{0,1}^k` определим настоящий полиэдр

    P_b=conv{v∈V(P): v≠v_i при b_i=1}.

Это целиком определённое конечное семейство из `2^k` возможных тел. Параметры b — выбор геометрии, **не независимо назначенные массы**.

### 5.2. Почему локальные удаления действительно коммутируют

Для одной вершины v новые грани `conv(V(P)\{v})` имеют вершины только среди настоящих соседей v.

Краткое доказательство: новая опорная плоскость `ℓ=h` имеет `ℓ(v)>h` и `ℓ≤h` на остальных вершинах. Любая вершина u новой грани должна иметь возрастающее по ℓ настоящее ребро в старом P; единственным возможным концом является v. Следовательно, u — сосед v.

Обратно, видимая из v грань выпуклой оболочки соседей является новой настоящей опорной гранью после удаления v. Если бы какая-то другая старая вершина имела больший уровень, вершина максимального уровня среди всех оставшихся должна была бы быть соседом v: её возрастающее ребро могло бы вести только к v. Это противоречит опорности плоскости на всех соседях.

При условиях 5.1 удаление одной выбранной вершины не меняет звезду другой выбранной вершины. По индукции все локальные замены коммутируют. Изменённые рёберные пакеты принадлежат только одной локальной замене; общие неизменённые рёбра остаются общими. Новые максимальные грани объединяются по настоящим плоскостям, а не по интеграционным треугольникам.

### 5.3. Реальные удаляемые «ушки»

Обозначим

    E_i=P\conv(V(P)\{v_i}).

Их внутренности попарно не пересекаются, и

    P_b=P\⋃_{i:b_i=1} E_i

с точностью до границ нулевого объёма. Пусть

    V=Vol(P),    J=∫_P x dx,
    δV_i=Vol(E_i)>0,    δJ_i=∫_(E_i) x dx.

Тогда **для каждого** бинарного b

    V_b=V−Σ_i b_i δV_i,
    J_b=J−Σ_i b_i δJ_i,
    g_b=J_b/V_b.                                      (C)

Каждая пара `(δV_i,δJ_i)` вычисляется по настоящим положительным тетраэдрам: вершина `v_i` плюс триангуляция видимых из неё новых максимальных граней. Диагонали этого интегрирования не становятся механическими рёбрами.

Таким образом, (C) не является moment-completion relaxation. Это точное интегрирование равномерно заполненного **того же** P_b.

## 6. Полный собственно-центроидный бинарный линейный сертификат

### 6.1. Целочисленная запись

Для наглядности пусть координаты после одного общего масштабирования целые и `M=N=I`. Масштабирование не меняет механический класс. Для ориентированной настоящей границы положим

    W=Σ det(a,b,c)=6Vol(P),
    G=Σ det(a,b,c)(a+b+c)=4Wg.

Для удаляемого ушка аналогично вычислим целые `w_i,t_i`, где `w_i=6δV_i`, `t_i=24δJ_i`. Тогда

    W_b=W−Σ b_i w_i,
    G_b=G−Σ b_i t_i,
    D_b=4W_b,
    g_b=G_b/D_b.                                     (D)

Для каждого возможного настоящего ребра-пакета с фиксированными концами a,b и фиксированными плоскостями f,h определим

    A_f(b)=D_b h_f−n_f·G_b.

После умножения на положительные знаменатели четыре механических числителя равны

    P_0(b)=(D_b v_a−G_b)·(v_b−v_a),
    P_1(b)=(D_b v_b−G_b)·(v_a−v_b),
    P_2(b)=(n_f·n_h)A_f(b)−(n_f·n_f)A_h(b),
    P_3(b)=(n_h·n_f)A_h(b)−(n_h·n_h)A_f(b).           (E)

**Каждая строка (E) — целочисленная аффинная функция бинарного вектора b.** Для одной фиксированной рациональной пары `M,N=M^-1` используются соответствующие скалярные произведения и один общий положительный знаменатель; вывод остаётся тем же.

### 6.2. Настоящие рёбра, а не все потенциальные отрезки

Локальные оболочки задают конечный атлас возможных пакетов `(a,b,f,h)`. При условиях 5.1 активность пакета имеет вид

    1,    b_i,    либо 1−b_i.

Пакеты с теми же концами, но разными инцидентными плоскостями различаются. Включать в атлас диагональ триангуляции максимальной грани недопустимо.

Отсутствие всех физических рёберных равновесий есть точная конечная система

    активен пакет e ⇒ max_k P_e,k(b)≥1.              (F)

Число1 здесь **не численный запас**: после целочисленного очищения `P>0` эквивалентно `P≥1`.

### 6.3. Явная MILP-форма без неопределённого big-M

Пусть одна строка имеет вид

    L(b)=ℓ0+Σ ℓ_i b_i.

Её точная нижняя граница на бинарном кубе:

    m_L=ℓ0+Σ min(0,ℓ_i).

Положим `K_L=max(0,1−m_L)`. Для бинарного селектора z ограничение

    L(b)≥1−K_L(1−z)

ничего не требует при z=0 и требует строгого положительного примитива при z=1. Для четырёх селекторов одного пакета достаточно

    Σ_k z_e,k=activation_e(b).

Получается обычная бинарная линейная система с полностью явными целыми коэффициентами. При необходимости положительность объёма и активных гранных знаменателей записывается такими же условными линейными ограничениями; геометрически она уже следует из полномерности P_b и его настоящего COM.

**Теорема.** Для семейства 5.1 бинарный вектор b удовлетворяет этой системе тогда и только тогда, когда настоящий равномерно заполненный P_b имеет собственный proper110 и не имеет дополнительных слабых равновесий.

Охват — все `2^k` геометрических состояний этого семейства, включая все нулевые механические стены. Это не вывод из конечного численного опробования нескольких удалений.

При непересекающихся локальных заменах число настоящих рёбер также аффинно по b. Поэтому минимизация C в этом семействе — линейная целевая функция. В симплициальной части без слияний максимальных граней удаление одной вершины уменьшает E на3 и C на6. При многоугольных гранях следует использовать фактические локальные изменения E.

### 6.4. Граница теоремы

Теорема не гарантирует существование нетривиального допустимого удаления и не утверждает, что локально несократимый результат минимален среди всех полиэдров. Она не разрешает одновременно произвольно менять M: при свободной метрике коэффициенты перестают быть фиксированными.

Численный MILP-солвер остаётся только locator. Найденный бинарный вектор проверяется целыми строками (D)–(F). Сообщение солвера о неуспехе не является сертификатом исключения семейства.

## 7. Точный небольшой контроль: совместные удаления создают шесть EF-контактов

Этот контроль полностью определён буквально и проверяется непосредственно аналитически. Он **не110** и не улучшает никакой верхней границы.

Исходные восемь вершин, в постоянном порядке:

    0=(-1,-1,-1), 1=(-1,-1,1), 2=(-1,1,-1), 3=(-1,1,1),
    4=(1,-1,-1),  5=(1,-1,1),  6=(1,1,-1),  7=(1,1,1).

Удаляемые вершины —0 и7. Они удовлетворяют условиям 5.1. Обозначим их индикаторы через `b_-` и `b_+`. Сохраняются плоскости `±x_i≤1`; при `b_-=1` добавляется настоящая грань `−x−y−z≤1`, при `b_+=1` — `x+y+z≤1`.

Точные собственные моменты:

    W_b=48−8b_-−8b_+,
    G_b=16(b_-−b_+)(1,1,1),
    Vol(P_b)=W_b/6,
    g_b=G_b/(4W_b).

Удаляемые ушки — настоящие тетраэдры объёма4/3 с центрами соответственно `(-1/2,-1/2,-1/2)` и `(1/2,1/2,1/2)`.

| `(b_-,b_+)` | Настоящие V,E,F | Объём | Собственный COM | Строгие S,U,H | Физические weak |
|---|---|---|---|---|---|
| `(0,0)` | `8,12,6` | `8` | `0` | `6,8,12` | нет |
| `(1,0)` | `7,12,7` | `20/3` | `(1/10,1/10,1/10)` | `7,7,12` | нет |
| `(0,1)` | `7,12,7` | `20/3` | `(-1/10,-1/10,-1/10)` | `7,7,12` | нет |
| `(1,1)` | `6,12,8` | `16/3` | `0` | `2,6,6` | **6 простых EF** |

В последней строке строгие S — две новые треугольные грани. Шесть слабых физических точек:

    (±1,0,0), (0,±1,0), (0,0,±1).

Их настоящие рёбра в исходных метках:

    (1,2), (5,6), (1,4), (3,6), (2,4), (3,5).

У каждого такого ребра два primal-примитива равны−4; на соответствующей паре полюсов примитивы равны0 и−2. Это именно EF, не VF и не безвредный ноль. Шесть остальных рёбер имеют два primal-примитива−2 и два dual-примитива−1, поэтому являются строгими H.

Все оставшиеся вершины лежат на сфере радиуса `sqrt3`, и каждая строго экспонируется своим радиальным вектором, что даёт шесть строгих U. Эти вычисления одновременно объясняют, почему по отдельности допустимые геометрические операции нельзя объединять без собственного центра и полного weak-census.

## 8. Минимальный exact recovery-контроль для теоремы

Следующий полный источник использует **только аутентифицированный исходник текущего parent**, уже буквально присутствующий в пакете. Новых скрытых помощников нет. Он восстанавливает все четыре действительных тела, проверяет два массовых веера через parent, весь census, а затем восстанавливает все аффинные строки (E) и все активности пакетов.

**Статус исполнения:** этот новый собранный контроль после отказа среды не запускался. Таблица раздела7 доказана выше непосредственно; нижеследующие terminal markers — ожидаемые, а не полученные в текущем исполнении. Для нового файла не изобретаются неполученные byte-count или SHA. При запуске источник сам печатает их.

Сохранить как `ear_family_certificate.py` рядом с буквальным `raven_quantitative_cap.py`:

```python
from pathlib import Path
from fractions import Fraction as R
from itertools import product
from math import lcm
import importlib.util, hashlib, json
assert __debug__
p=Path('raven_quantitative_cap.py')
data=p.read_bytes()
assert len(data)==12901
assert hashlib.sha256(data).hexdigest()=='f6e0aa811c7ae075b95e81247b5b2d14f1b87dfabb3b4db424f29a47e678467e'
spec=importlib.util.spec_from_file_location('cap_parent',p)
P=importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)
RAW=[tuple(map(R,x)) for x in product((-1,1),repeat=3)]
STATES=list(product((0,1),repeat=2))
EXPECTED={(0,0):(6,8,12,0),(1,0):(7,7,12,0),
          (0,1):(7,7,12,0),(1,1):(2,6,6,6)}

def canon_packet(X,Q,e):
    a,b,f,h=e
    a,b=sorted((RAW.index(X[a]),RAW.index(X[b])))
    f,h=sorted((tuple(Q[f]),tuple(Q[h])))
    return a,b,f,h

def moments(state):
    bm,bp=state
    W=R(48-8*bm-8*bp)
    G=(R(16*(bm-bp)),)*3
    return W,G

def forms(packet,state):
    a,b,n,m=packet
    W,G=moments(state)
    D=4*W
    e=P.sub(RAW[b],RAW[a])
    A=D-P.dot(n,G)
    B=D-P.dot(m,G)
    u=P.sub(P.scale(D,RAW[a]),G)
    v=P.sub(P.scale(D,RAW[b]),G)
    return (P.dot(u,e),-P.dot(v,e),
            P.dot(n,m)*A-P.dot(n,n)*B,
            P.dot(m,n)*B-P.dot(m,m)*A)

def affine(values):
    z=values[(0,0)]
    a=values[(1,0)]-z
    b=values[(0,1)]-z
    assert values[(1,1)]==z+a+b
    return z,a,b

def integer_row(row):
    d=lcm(*(x.denominator for x in row))
    out=tuple(int(d*x) for x in row)
    lower=out[0]+sum(min(0,x) for x in out[1:])
    return dict(coefficients=out,positive_scale=d,big_M=max(0,1-lower))

records={}
packets={}
for state in STATES:
    bm,bp=state
    pts=[x for i,x in enumerate(RAW) if not(i==0 and bm) and not(i==7 and bp)]
    X,F,Q=P.hull(pts)
    edges,V,g=P.geometry(X,F,Q)
    audit=P.audit(X,Q,edges,g)
    W,G=moments(state)
    assert V==W/6 and g==tuple(x/(4*W) for x in G)
    expected=EXPECTED[state]
    assert tuple(audit['SUH'])==expected[:3]
    assert len(audit['weak_packets'])==expected[3]
    assert not audit['harmless_zero_incidences']
    assert all(x['kind']=='EF' for x in audit['weak_packets'])
    keys={canon_packet(X,Q,e) for e in edges}
    for e,key in zip(edges,[canon_packet(X,Q,e) for e in edges]):
        a,b,f,h=e
        ni=RAW.index(X[a]);nj=RAW.index(X[b])
        if ni>nj:a,b=b,a
        qf,qh=Q[f],Q[h]
        if tuple(qf)>tuple(qh):qf,qh=qh,qf
        xc=P.sub(X[a],g);yc=P.sub(X[b],g)
        qf=P.scale(1/(1-P.dot(qf,g)),qf)
        qh=P.scale(1/(1-P.dot(qh,g)),qh)
        z=(P.dot(xc,P.sub(yc,xc)),P.dot(yc,P.sub(xc,yc)),
           P.dot(qf,P.sub(qh,qf)),P.dot(qh,P.sub(qf,qh)))
        assert tuple((x>0)-(x<0) for x in z)==tuple((x>0)-(x<0) for x in forms(key,state))
    packets[state]=keys
    records[str(state)]=dict(vertices=X,maximal_facets=F,poles=Q,true_edges=edges,
        volume=V,centroid=g,W=W,G=G,audit=audit)

atlas=sorted(set().union(*packets.values()))
rows=[]
for packet in atlas:
    activation=affine({s:R(int(packet in packets[s])) for s in STATES})
    assert activation in ((1,0,0),(0,1,0),(0,0,1),(1,-1,0),(1,0,-1))
    guards=[]
    for k in range(4):
        guards.append(integer_row(affine({s:forms(packet,s)[k] for s in STATES})))
    rows.append(dict(packet=packet,activation=activation,guards=guards))

for state in STATES:
    proper=all(max(forms(p,state))>0 for p in packets[state])
    assert not proper

report=dict(name='RAVEN_INDEPENDENT_EAR_OWN_COM_MILP_V1_CUBE_CONTROL',
            states=records,edge_packet_atlas=rows)
b=(json.dumps(P.serial(report),sort_keys=True,indent=2)+'\n').encode()
Path('ear_family_certificate.json').write_bytes(b)
s=Path(__file__).read_bytes()
print('SOURCE',len(s),hashlib.sha256(s).hexdigest())
print('REPORT',len(b),hashlib.sha256(b).hexdigest())
print('FOUR_ACTUAL_EAR_STATES_TWO_MASS_FANS_PASS')
print('ALL_EDGE_PACKET_GUARDS_AFFINE_IN_TRUE_MOMENT_REMOVALS_PASS')
print('JOINT_DELETION_HAS_SIX_EXACT_EF_PACKETS_PASS')
```

Команда восстановления:

```sh
python -S ear_family_certificate.py
```

Зависимости этого контроля: **CPython3.13.5, стандартная библиотека и ровно указанный полный parent-source**. Исходный parent не изменяется.

## 9. Полный источник численного маршрута

Ниже один полный runnable unit, сохраняющий конструктивные операции, фиксированные параметры, две версии углового merge-допуска, исправление неправильных концов, пересчёт настоящего конечного COM и моментно-балансированные удаления.

Это **численный locator**, а не точный verifier. Новая сборка источника не прошла cold replay после потери исполнения. Она намеренно печатает SHA и полный целочисленный checkpoint при каждом дальнейшем принятом этапе, чтобы следующий исполнитель не оказался с одним непереносимым `.npz`.

Использованные версии: **CPython3.13.5, NumPy2.3.5, SciPy1.17.0**, один BLAS-поток. MILP использует бинарные геометрические решения; его `time_limit=10` и `mip_rel_gap=.002` являются locator-параметрами, не доказательными допусками.

Сохранить как `raven4_locator.py`:

```python
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[k]='1'
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import brentq,milp,LinearConstraint,Bounds
from collections import defaultdict
from pathlib import Path
import json,hashlib,sys

EPS=.04
APEX=np.array([1.041,0.,0.])
CUT=-.958
DEN=10**10

def oriented(p):
    h=ConvexHull(p)
    t=h.simplices.copy()
    n=np.cross(p[t[:,1]]-p[t[:,0]],p[t[:,2]]-p[t[:,0]])
    bad=np.einsum('ij,ij->i',n,h.equations[:,:3])<0
    t[bad]=t[bad][:,[0,2,1]]
    return h,t

def measure(p,cut=None,merge=1e-13,tol=0.):
    p=np.asarray(p,dtype=float)
    h,t=oriented(p)
    if cut is not None:
        points=list(p[p[:,0]>=cut])
        ee=set(tuple(sorted((int(a),int(b))))
               for T in t for a,b in zip(T,np.roll(T,-1)))
        for a,b in sorted(ee):
            if (p[a,0]-cut)*(p[b,0]-cut)<0:
                u=(cut-p[a,0])/(p[b,0]-p[a,0])
                x=(1-u)*p[a]+u*p[b]
                x[0]=cut
                points.append(x)
        p=np.asarray(points)
        h,t=oriented(p)
    keep=h.vertices
    remap=np.full(len(p),-1,dtype=int)
    remap[keep]=np.arange(len(keep))
    p=p[keep]
    t=remap[t]
    d=np.einsum('ij,ij->i',p[t[:,0]],np.cross(p[t[:,1]],p[t[:,2]]))
    V=d.sum()/6
    g=np.einsum('i,ij->j',d,p[t].sum(axis=1))/(4*d.sum())
    parent=list(range(len(t)))
    def root(i):
        while parent[i]!=i:
            parent[i]=parent[parent[i]]
            i=parent[i]
        return i
    for i,nei in enumerate(h.neighbors):
        for j in nei:
            if j>i and np.max(np.abs(h.equations[i]-h.equations[j]))<merge:
                parent[root(j)]=root(i)
    groups=defaultdict(list)
    for i in range(len(t)):
        groups[root(i)].append(i)
    fi=np.empty(len(t),dtype=int)
    Q=[]
    for f,ts in enumerate(groups.values()):
        fi[ts]=f
        q=h.equations[ts[0],:3]/(-h.equations[ts[0],3])
        Q.append(q)
    Q=np.asarray(Q)
    raw=defaultdict(list)
    for f,T in zip(fi,t):
        for a,b in zip(T,np.roll(T,-1)):
            raw[tuple(sorted((int(a),int(b))))].append(int(f))
    edges=np.array([(a,b,*fs) for (a,b),fs in sorted(raw.items())
                    if len(set(fs))==2],dtype=int)
    x=p-g
    q=Q/(1-Q@g)[:,None]
    a,b,f,k=edges.T
    e=x[b]-x[a]
    v=q[k]-q[f]
    z=np.column_stack((np.einsum('ij,ij->i',x[a],e),
                       -np.einsum('ij,ij->i',x[b],e),
                       np.einsum('ij,ij->i',q[f],v),
                       -np.einsum('ij,ij->i',q[k],v)))
    pm=np.full(len(p),-np.inf)
    qm=np.full(len(Q),-np.inf)
    np.maximum.at(pm,a,z[:,0])
    np.maximum.at(pm,b,z[:,1])
    np.maximum.at(qm,f,z[:,2])
    np.maximum.at(qm,k,z[:,3])
    U=np.flatnonzero(pm<-tol)
    S=np.flatnonzero(qm<-tol)
    H=np.flatnonzero(np.max(z,axis=1)<-tol)
    weak=np.flatnonzero(np.max(z,axis=1)<=tol)
    return dict(p=p,T=t,Q=Q,q=q,edges=edges,z=z,g=g,V=V,U=U,S=S,H=H,
                SUH=(len(S),len(U),len(H)),
                VEF=(len(p),len(edges),len(Q)),weak_edges=len(weak)-len(H))

def support(normals):
    out=[]
    a=1.5*np.pi
    for n in normals:
        s=np.hypot(n[0],n[1])
        if s<1e-14:
            z=float(np.sign(n[2]))
            r=0.
        else:
            def derivative(z):
                ph=a*(z-z*z*z/3)
                return (EPS*a*(1-z*z)*(-n[0]*np.sin(ph)+n[1]*np.cos(ph))
                        -s*z/np.sqrt(1-z*z)+n[2])
            z=brentq(derivative,-1+1e-15,1-1e-15,xtol=1e-14)
            r=np.sqrt(1-z*z)/s
        ph=a*(z-z*z*z/3)
        out.append([EPS*np.cos(ph)+r*n[0],EPS*np.sin(ph)+r*n[1],z])
    return np.asarray(out)

def initial(wrong_tips):
    count=50
    i=np.arange(count)
    z=(i+.5)/count
    theta=i*np.pi*(3-np.sqrt(5))
    r=np.sqrt(1-z*z)
    p=np.column_stack((r*np.cos(theta),r*np.sin(theta),z))
    ph=1.5*np.pi*(z-z*z*z/3)
    p[:,0]+=EPS*np.cos(ph)
    p[:,1]+=EPS*np.sin(ph)
    end=EPS if wrong_tips else -EPS
    return np.concatenate((p,p*np.array([1,-1,-1]),
                           [[end,0,1],[end,0,-1],[1+EPS,0,0],[-1+EPS,0,0]]))

def add_supports(p,merge):
    r=measure(np.concatenate((p,[APEX])),cut=CUT,merge=merge,tol=1e-12)
    x=r['p']
    g=r['g']
    normals=[x[i]-g for i in r['U'] if np.linalg.norm(x[i]-APEX)>1e-8]
    normals.extend(r['Q'][i] for i in r['S']
                   if np.linalg.norm(r['Q'][i,1:])>1e-8 or r['Q'][i,0]>0)
    for k in r['H']:
        i,j,f,h=r['edges'][k]
        e=x[j]-x[i]
        t=-np.dot(x[i]-g,e)/np.dot(e,e)
        normals.append(x[i]+t*e-g)
    if normals:
        p=np.concatenate((p,support(np.asarray(normals))))
        keys=np.round(p*1e13).astype(np.int64)
        _,ids=np.unique(keys,axis=0,return_index=True)
        p=p[np.sort(ids)]
    return p,r,len(normals)

def save(name,p,extra=None):
    ints=np.unique(np.round(p*DEN).astype(np.int64),axis=0)
    data=(json.dumps(dict(denominator=DEN,vertices=ints.tolist(),extra=extra),
                     sort_keys=True,separators=(',',':'))+'\n').encode()
    Path(name+'.json').write_bytes(data)
    np.savez(name+'.npz',X=p)
    print('CHECKPOINT',name,len(data),hashlib.sha256(data).hexdigest(),flush=True)

def grow(historical=True):
    p=initial(historical)
    if historical:
        for stage,steps,merge in [('initial',14,1e-9),('resume',11,1e-13)]:
            for i in range(steps):
                p,r,count=add_supports(p,merge)
                print('SUPPORT',stage,i,len(p),r['VEF'],r['SUH'],r['weak_edges'],flush=True)
        bad=((np.abs(p[:,0]-EPS)<1e-12)&(np.abs(p[:,1])<1e-12)
             &(np.abs(np.abs(p[:,2])-1)<1e-12))
        p=np.concatenate((p[~bad],[[-EPS,0,1],[-EPS,0,-1]]))
        steps=6
    else:
        steps=100
    for i in range(steps):
        p,r,count=add_supports(p,1e-13)
        print('SUPPORT','correct',i,len(p),r['VEF'],r['SUH'],r['weak_edges'],flush=True)
        if not count:
            break
    r=measure(np.concatenate((p,[APEX])),cut=CUT,merge=1e-13,tol=0)
    save('support_terminal',r['p'],dict(SUH=r['SUH'],VEF=r['VEF']))
    ints=np.unique(np.round(r['p']*DEN).astype(np.int64),axis=0)
    keep=(ints[:,2]>0)|((ints[:,2]==0)&(ints[:,1]>=0))
    half=ints[keep]
    ints=np.unique(np.concatenate((half,half*np.array([1,-1,-1]))),axis=0)
    r=measure(ints.astype(float)/DEN)
    save('symmetric_terminal',r['p'],dict(SUH=r['SUH'],VEF=r['VEF']))
    return r['p']

def delete_batches(p,rounds=16):
    rng=np.random.default_rng(89173)
    for iteration in range(rounds):
        r=measure(p)
        if r['SUH']!=(1,1,0):
            print('LOCATOR_NOT_110',r['SUH'],flush=True)
            break
        p=r['p']
        g=r['g'].copy()
        code=np.round(p*DEN).astype(np.int64)
        lookup={tuple(v):i for i,v in enumerate(code)}
        twin=[lookup.get((v[0],-v[1],-v[2]),-1) for v in code]
        assert min(twin)>=0
        g[1:]=0
        neigh=[set() for _ in p]
        for i,j,f,h in r['edges']:
            neigh[i].add(j)
            neigh[j].add(i)
        fixed=set(np.flatnonzero(p[:,0]<p[:,0].min()+1e-9))|set(r['U'])
        blocked=set(fixed)
        proposals=[]
        for v in rng.permutation(len(p)):
            v=int(v)
            tv=twin[v]
            if v in blocked or tv in blocked or tv==v:
                continue
            ns=sorted(neigh[v])
            pp=p[ns]
            if len(ns)<4 or tv in ns or set(ns)&neigh[tv]:
                continue
            try:
                hh=ConvexHull(pp)
            except Exception:
                continue
            visible=hh.equations[:,:3]@p[v]+hh.equations[:,3]>1e-13
            new=hh.simplices[visible].copy()
            if len(new)!=len(ns)-2:
                continue
            n=np.cross(pp[new[:,1]]-pp[new[:,0]],pp[new[:,2]]-pp[new[:,0]])
            bad=np.einsum('ij,ij->i',n,hh.equations[visible,:3])<0
            new[bad]=new[bad][:,[0,2,1]]
            a,b,c=pp[new[:,0]],pp[new[:,1]],pp[new[:,2]]
            e=b-a
            f=c-a
            z=a-g
            ee=np.einsum('ij,ij->i',e,e)
            ff=np.einsum('ij,ij->i',f,f)
            ef=np.einsum('ij,ij->i',e,f)
            ze=np.einsum('ij,ij->i',z,e)
            zf=np.einsum('ij,ij->i',z,f)
            de=ee*ff-ef*ef
            u=(ef*zf-ff*ze)/de
            w=(ef*ze-ee*zf)/de
            if np.any((u>=-1e-9)&(w>=-1e-9)&(u+w<=1+1e-9)):
                continue
            extra={i:set() for i in ns}
            for T in new:
                T=[ns[i] for i in T]
                for i in T:
                    extra[i].update(j for j in T if j!=i)
            if any(max(np.dot(p[i]-g,p[j]-p[i])
                       for j in (neigh[i]-{v})|extra[i])<=1e-13 for i in ns):
                continue
            dv=-np.einsum('ij,ij->i',a-p[v],np.cross(b-p[v],c-p[v]))/6
            if np.min(dv)<=0:
                continue
            mass=2*dv.sum()
            moment=2*np.dot(dv,(a[:,0]+b[:,0]+c[:,0]+p[v,0])/4)
            proposals.append((v,tv,mass,moment,moment-g[0]*mass))
            for vv in (v,tv):
                blocked.add(vv)
                for i in neigh[vv]:
                    blocked.add(i)
                    blocked.update(neigh[i])
        if not proposals:
            break
        weights=np.array([p[4] for p in proposals])
        scale=max(np.max(np.abs(weights)),1e-20)
        result=milp(-np.ones(len(proposals)),integrality=np.ones(len(proposals)),
            bounds=Bounds(0,1),
            constraints=LinearConstraint(weights[None,:]/scale,-1e-10/scale,1e-10/scale),
            options={'time_limit':10,'mip_rel_gap':.002})
        if result.x is None:
            break
        chosen=[i for i,x in enumerate(result.x) if x>.5]
        accepted=False
        for attempt in range(10):
            gone=[proposals[i][j] for i in chosen for j in (0,1)]
            keep=np.ones(len(p),dtype=bool)
            keep[gone]=False
            rr=measure(p[keep])
            if rr['SUH']==(1,1,0):
                accepted=True
                break
            chosen=chosen[:len(chosen)//2]
            if not chosen:
                break
        if not accepted or not chosen:
            break
        p=rr['p']
        meta=dict(iteration=iteration,deleted=len(gone),SUH=rr['SUH'],
                  VEF=rr['VEF'],centroid=rr['g'].tolist(),
                  selected_local_proposals=chosen)
        print('NUMERICAL_EAR_BATCH',meta,flush=True)
        save('ear_batch_%03d'%iteration,p,meta)
    return p

if __name__=='__main__':
    historical=len(sys.argv)<2 or sys.argv[1]=='historical'
    p=grow(historical)
    p=delete_batches(p)
    r=measure(p)
    save('numerical_terminal',p,dict(SUH=r['SUH'],VEF=r['VEF'],centroid=r['g'].tolist()))
    source=Path(__file__).read_bytes()
    print('SOURCE',len(source),hashlib.sha256(source).hexdigest())
    print('NUMERICAL_LOCATOR_ONLY_EXACT_ACCEPTANCE_NOT_CLAIMED')
```

Команды:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  python raven4_locator.py historical
```

Режим `clean` начинает непосредственно с правильных двух концов K; его результат не был вычислен в этом продолжении:

```sh
python raven4_locator.py clean
```

**Ограничение recovery:** этот источник сохраняет весь метод, точные параметры и историческую последовательность стадий, но не заменяет отсутствующий побайтно закреплённый терминальный массив. Для любого вновь полученного checkpoint принятность начинается только после его отдельного exact hull/COM/weak replay. Численные сообщения `NUMERICAL_EAR_BATCH` не являются сертификатами proper110.

## 10. Практический exact-аудит: что требуется завершить

Для координат на общей целой сетке `v_i=a_i/D` не нужно repeatedly складывать огромные дроби с индивидуальными знаменателями. Следует работать с целыми `a_i`.

Сначала строятся и аутентифицируются настоящие максимальные грани. Для каждой плоскости `n·a≤h` проверяются **все** входные точки, а все точки равенства проходят точную плоскую convex-hull процедуру. Затем проверяются противоположные ориентации каждого истинного ребра, ссылки вершин, связность и Эйлер. Только после этого интеграционные треугольники используются для W,G.

При `g_int=G/(4W)` четыре знака истинного ребра вычисляются целыми числами:

    C_i=4W a_i−G,
    B_f=4W h_f−n_f·G>0,

    sign primal(i→j)=sign[C_i·(a_j−a_i)],
    sign dual(f→h)=sign[n_f·(B_f n_h−B_h n_f)].

Физические объём и центр:

    Vol=W/(6D³),
    g=G/(4WD).

Это практически значительно дешевле, чем строить центрированные полюсы как огромные Fraction-объекты для каждого ребра. Второй веер из настоящей вершины должен независимо дать те же W,G.

В текущем исполнении именно завершённого отчёта этой стадии нет. Промежуточные треугольники или найденные плоскости не подменяют его.

## 11. Наиболее полезное продолжение

Первый приоритет — не ещё один запуск общего escape-loss. Следует восстановить численный поток, **сразу закрепить полный целочисленный checkpoint и его SHA**, а затем довести один точный полный аудит до терминального результата. Даже пример с десятками тысяч настоящих рёбер был бы содержательным практически перечисленным результатом этой независимой ветви, хотя не улучшал бы C622.

После такого exact endpoint разделы4–6 дают более сильный путь сокращения: заменить ограничение на малость моментного остатка полными целочисленными строками (E)–(F). Тогда бинарный выбор одновременно учитывает реальную потерю массы, собственный центр, истинные новые рёбра и все weak-пакеты. Это устраняет конкретный разрыв между использованным численным удалением и необходимым физическим сертификатом.

Итоговые границы утверждения: **доказан полный конечносемейный own-COM MILP-механизм; аналитически сохранён точный четырёхсостоянийный weak-контроль; практически малый exact110 пока не принят; ни нижняя34, ни верхняя622 не изменены.**
