# figure-0583

Historical AI scientific report · saved 2026-09-27 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Keen Harbor 93 — радиальный скос текущего седла: новое S возникает раньше, чем исчезает оставшийся Q

## Статус и граница источников

**Новой подтверждённой own110-конструкции в этом продолжении нет.** Ниже дано аналитическое препятствие для конкретной конечной операции на нынешнем интерфейсе R82: радиального скоса физического седлового ребра. Эта операция уменьшает ведущий Q в первом порядке, но неизбежно создаёт второй положительный Q во втором порядке. Поэтому она особенно опасна для численного отбора с порогом малых баров.

Новый файл `research-journal(20260927-220235).md`, заявленный как297106 байт с SHA-256 `0a719577ebc14a0f356d5d7f15577426893124865ce5f4bdc5530b031779fabc`, в этом исполнении не удалось прочитать: инструментальные обращения не предоставили мне доступного текста или доступного вывода, в том числе контрольные обращения к контейнеру. **Не утверждаю, что новый журнал прочитан, что его хеш перепроверен или что перечисленные ниже программы успешно исполнены.** Утрата файлов также не установлена. Поэтому новые положения журнала не используются, а возможное совпадение следующего аналитического результата с непрочитанным обновлением не исключается.

Доступная научная опора — уже приведённый полностью в этом чате неизменяемый parent `figure-0581`, SHA-256 `f4d4df1390c5e9bd18047aad823f3cd12e8c85751a66dbfc62ae50f67c779461`, и его буквальный82-строчный `KH93_C434_R82_G6`. Старый47-файловый recovery не объявляется потерянным. Нового численного checkpoint или новой исполненной точной квитанции в данном handoff нет.

## 1. Применимость к буквальному R82

Используется именно `KH93_C434_R82_G6`: V160/E240/F82, own strict211, additionalweak000, P[], единственный Q≈0.11600403115840405. Его текущий полярный седловой переход — ребро между опорами43 и55. Соответствующее физическое седловое ребро имеет конечные точки64/104 в порядке прежнего аудитора; уникальная U7 не является его концом. Индексы43/55 ниже относятся к строкам буквального H-входа, а не к новой сортировке вершин.

Из E240 и V160 следует, что каждая вершина имеет степень ровно3: сумма степеней равна480=3V, а степень вершины выпуклого трёхмерного многогранника не меньше3. Следовательно, рассматриваемый скос является скосом простого ребра.

Пусть K — это точное тело, g — его **настоящий однородный центр**, e — указанное седловое ребро, s — ортогональная проекция g на прямую e, m=s−g и r²=m·m. Строгость седла означает, что s лежит внутри e, а m — внутри конуса двух внешних нормалей его граней.

Рассмотрим рациональное однопараметрическое семейство:

`K_ε = K ∩ {x : m·(x−g) ≤ r²/(1+ε)},   ε>0.`

Нормаль нового среза фиксирована и равна m. Центр g используется для **определения плоскости**, но центр получившегося тела после среза равен заново вычисляемому g_ε, а не назначается равным g.

### Утверждение о всём достаточно малом интервале

Для всех достаточно малых положительных ε это ограниченное полноразмерное однородное тело имеет:

- **V162/E243/F83**, то есть C486;
- **own strict(S,U,H)=(3,1,2)**;
- **additionalweak000**;
- P[], **ровно два строго положительных Q**.

Таким образом, этот конкретный малый радиальный скос нынешнего седла **не может завершить отмену Q**. Он заменяет одно седло двумя и создаёт новую стабильную грань между двумя сохранившимися стабильными бассейнами.

Это локальное утверждение о явно определённом семействе. Оно не исключает большие скосы, наклон новой плоскости, совместное движение старых опор, исчезновение старых стабильных граней или независимую перестройку массы первого порядка.

## 2. Почему утверждение относится к собственной массе

### Комбинаторика и ограниченность

При достаточно малом ε плоскость отсекает только два конца e. Четыре пересечения с четырьмя остальными инцидентными рёбрами становятся новыми вершинами. Изменения равны ΔV=2, ΔE=3, ΔF=1. Новая грань — четырёхугольник. Все прежние максимальные грани сохраняются как максимальные грани, хотя четыре из них изменяют границу.

Ограниченность наследуется от K. Полноразмерность не требует численного предположения: g остаётся строго внутри всех старых полупространств и удовлетворяет новому неравенству строго, поскольку0<r²/(1+ε).

### Настоящее смещение центра имеет второй порядок

Обозначим удалённый объём через v_ε, его центр через c_ε, а исходный объём через V. Точная формула заполненной однородной массы:

`g_ε−g = v_ε (g−c_ε)/(V−v_ε).`

Срез простого ребра удаляет клин, у которого обе поперечные ширины имеют порядок ε, а длина ограничена. Поэтому `v_ε=O(ε²)` и `g_ε−g=O(ε²)`. Это также видно непосредственно по точным пересечениям: четыре новые вершины аффинны по глубине среза `ε/(1+ε)`, а объём и первый момент удалённого клина имеют нулевые постоянный и линейный коэффициенты.

Здесь не предполагается ни точное сохранение центра, ни переменная плотность. Сдвиг центра обычно ненулевой.

### Новая стабильная грань сохраняется при этом смещении

При исходном центре g её ортогональная проекция —

`p_ε = g + m/(1+ε).`

Это строгая выпуклая комбинация g и s. Поэтому p_ε лежит строго внутри K и внутри новой грани среза.

Пусть `Π=I−mmᵀ/r²`, `d_ε=g_ε−g`. При настоящем центре проекция на ту же новую плоскость равна **точно**

`p_ε + Π d_ε.`

Запишем старые опоры как `n_j·x≤h_j`, положим

`γ_j = h_j−n_j·(g+m)`,

`c_j = n_j−(n_j·m)m/r²`.

Точный запас этой проекции относительно старой опоры j:

`γ_j + [ε/(1+ε)] n_j·m − c_j·d_ε.`

Для двух граней43/55 имеем γ_j=0 и `n_j·m=h_j−n_j·g>0`. Положительный член имеет первый порядок ε, а поправка от фактической массы — второй. Для остальных граней γ_j>0. Следовательно, новая грань остаётся **строго стабильной относительно собственного g_ε** на целом достаточно малом положительном интервале.

Это даёт конкретный критерий выхода из ловушки. Пока остальные запасы не исчезли, для исключения новой S без слабой S необходимо, чтобы хотя бы для j=43 или55 выполнялось

`c_j·(g_ε−g) > [ε/(1+ε)] n_j·m.`

Голый скос не может выполнить это при малом ε: его смещение центра имеет недостаточный порядок. Компенсация, которая оставляет смещение центра o(ε), тоже не устраняет новую S в таком локальном chart.

### Остальной census

Две старые S сохраняются: их строгие проекции отделены от срезаемого ребра. Старые нестабильные грани остаются нестабильными по открытости соответствующих строгих исключающих условий.

У обоих удаляемых концов e есть положительная выходящая хорда к сохраняемой старой вершине. Хорда к другому концу e не может быть таким свидетелем, поскольку проекция на e внутренняя. Четыре новые вершины сходятся к этим двум старым не-U вершинам и наследуют положительные свидетели при малом ε. Старая уникальная U сохраняется. Так получается собственная U1 без слабых U.

Два длинных новых ребра, разделяющие новую грань и старые грани43/55, являются строгими седловыми. Их предельная продольная проекция лежит внутри старого e; новые конусные запасы положительны в первом порядке. Собственная поправка центра второго порядка их не уничтожает. Два коротких новых ребра сходятся к старым не-U вершинам; их нормальные конусы содержатся в соответствующих старых вершинных конусах и не приобретают радиального направления. Остальные рёбра сохраняют отсутствие равновесий. Получаются ровно два строгих H и никаких дополнительных слабых равновесий.

## 3. Почему ведущий Q улучшается, скрывая настоящий дополнительный бар

Следующие формулы сначала точны при исходном центре g; затем учтём собственную массу.

Пусть q_a и q_b — центрированные полярные вершины опор43/55. Обозначим через q_* внутренний минимум квадрата радиуса на их отрезке:

`q_* = m/r²`, `R=|q_*|²=1/r²`,

`A=|q_a−q_*|²>0`, `B=|q_b−q_*|²>0`.

Новая полярная вершина равна `(1+ε)q_*`. Её квадрат радиуса — `R(1+ε)²`. Квадраты радиусов двух новых седловых уровней равны

`h_a = R(1+ε)² − R² ε²(1+ε)²/(A+R ε²)`,

`h_b = R(1+ε)² − R² ε²(1+ε)²/(B+R ε²)`.

Следовательно, новый положительный относительный бар, рождённый новой стабильной физической гранью, имеет при фиксированном g точную глубину

`Q_new = R ε² / (max(A,B)+R ε²) > 0.`

Старые два бассейна соединяются на уровне `min(h_a,h_b)=R+2Rε+O(ε²)`. Если B₀ — исходный квадрат рождения старого конечного Q-бара, то его глубина меняется как

`Q_old(ε)=Q_old(0)−(2R/B₀)ε+O(ε²).`

Возвращение к **настоящему собственному центру** меняет старые полярные вершины на O(ε²). У нового максимума отрицательные исходящие скалярные произведения имеют первый порядок ε. Поэтому его положительный бар не исчезает, и сохраняются асимптотики

`Q_new,own(ε) = [R/max(A,B)] ε² + O(ε³)`,

`Q_old,own(ε) = Q_old(0)−(2R/B₀)ε+O(ε²).`

Итак, у этого механизма есть реальное уменьшение главного дефекта первого порядка и одновременно **реальный дополнительный дефект второго порядка**. Отсечение малых баров способно ошибочно представить такой own312 как улучшенный own211. Это вывод о геометрическом семействе, а не результат численного сканирования.

## 4. Полностью заданный точный проверочный эксперимент

Ниже — самостоятельная программа только на Python standard library. Она включает все82 буквальные нормали R82, строит его точную геометрию для получения необходимой собственной массы, выбирает ребро по опорам43/55, выполняет рациональный скос и уменьшает ε до полного точного census312/weak000 с двумя положительными Q.

Программа не использует плавающий hull, старый sandbox, внешний архив или предполагаемый центр. Перечисляются настоящие максимальные грани и рёбра; новый центр интегрируется по положительным тетраэдрам. Все знаки и все бары рациональные, без численного floor.

**Статус программы: приведена как воспроизводимый проверочный источник, но её успешное исполнение и конечное значение k в этом ответе не наблюдались.** Поэтому алгоритмически определённый свидетель `KH93_RADIAL_SADDLE_BEVEL312` не повышается здесь до нового runtime-verified endpoint. Доказательство выше обеспечивает остановку точного уменьшения ε при корректной реализации; сам код всё равно обязан пройти свои проверки.

Сохранить как `radial_bevel93.py` и выполнить `python radial_bevel93.py`. Ожидаемый, но не наблюдённый в этом продолжении маркер:

`KH93_RADIAL_SADDLE_BEVEL_OWN312_EXACT_PASS_NOT_110`.

На успешном выполнении записываются полный рациональный H-вход и полный отчёт с собственными объёмом, первым моментом, центром, вершинами, максимальными гранями, рёбрами и обоими списками баров. Программа печатает их фактические размеры и SHA-256. Неизвестные мне новые выходные хеши не выдуманы.

```python
from fractions import Fraction as F
from itertools import combinations, count
from functools import cmp_to_key
from pathlib import Path
import hashlib
import json
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

DATA = '''82 1000000
-725174 1362065 699290
-876644 1271151 690615
-1099310 1231174 294886
-817964 1365431 563226
-1081003 1264128 151488
-621649 1353152 816931
-910427 1348627 429305
-518139 1328018 931336
-1150535 1200456 6778
-1020626 1165129 671462
-1000361 1313225 295844
-1194316 1138885 290932
-1092629 1226455 -152925
-1154723 1038071 651530
-1018232 1244394 -303529
-826413 1255634 -573231
-413284 1274995 1033847
-712036 1248759 -690383
-565903 -2054257 -854847
-307427 1210004 1127958
-587643 1233564 -794247
-200527 1134456 1212109
-455233 1210233 -883762
-928979 1254154 -443961
-92885 1049729 1285004
-316806 1179053 -958168
-193819 -1291659 -912554
18238 952579 1348058
-174313 1140389 -1016977
-5177 -1016438 -923390
126983 847597 1397922
-11369 1085575 -1065309
231228 735671 1434828
330275 -1762331 162369
151779 1022336 -1093263
30004 1300793 -698627
219511 -659625 -911359
322219 610162 1464118
1094885 47914 75899
412797 485892 1476567
312873 951248 -1101019
394488 -437948 -877153
372181 573535 -1047196
751040 -363347 1338736
494318 358585 1477376
482341 -441422 -830169
502322 597143 -1020344
986434 79237 -460427
565401 225769 1467982
1050351 419486 112141
1083749 -76462 20200
570962 315730 -946952
315382 1317869 -337108
631111 96499 1445527
618364 -68927 -830846
685954 -34720 1413641
769199 -342229 -602838
779840 -1029259 1003128
816852 -402173 -515337
803000 -801799 1145327
813560 70446 -729507
796119 -578783 1253080
873889 -555249 -338841
940788 -543762 -95731
905170 -119352 -513537
748587 944500 20227
956411 -355836 -265735
889363 454940 -604392
917283 703683 114724
1033644 -185828 -146671
1044375 -230785 26003
1003015 537275 125496
1077079 104258 162986
1081632 235703 135814
1081426 316201 94169
570808 -432037 -763436
714032 -374886 -651118
654625 -473702 -663065
648347 -407882 -703531
589983 -151107 549377
727139 -1270183 798804
579789 -1442685 583018
'''
# Guarded correction of the single literal row in this source string.
# The authoritative R82 row79 is -1511107, not -151107.
DATA = DATA.replace('589983 -151107 549377',
                    '589983 -1511107 549377')
raw = DATA.strip() + '\n'
assert len(raw.encode()) == 1888
PARENT_SHA = '9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7'
assert hashlib.sha256(raw.encode()).hexdigest() == PARENT_SHA
rows = [tuple(map(int, line.split())) for line in raw.splitlines()]
M, D = rows[0]
N = rows[1:]
assert M == len(N) == 82 and D == 1000000


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def mul(t, a):
    return tuple(t*x for x in a)


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def det(a, b, c):
    return dot(a, cross(b, c))


def mean(points):
    return tuple(sum(p[k] for p in points)/len(points)
                 for k in range(3))


def polygon_order(ids, points, normal):
    ids = list(ids)
    assert len(ids) >= 3
    k = next(k for k in range(3) if normal[k])
    a, b = (k+1) % 3, (k+2) % 3
    centre = mean([points[i] for i in ids])
    xy = {i: (points[i][a]-centre[a], points[i][b]-centre[b])
          for i in ids}

    def half(v):
        return 0 if v[1] > 0 or (v[1] == 0 and v[0] >= 0) else 1

    def compare(i, j):
        u, v = xy[i], xy[j]
        if half(u) != half(v):
            return -1 if half(u) < half(v) else 1
        z = u[0]*v[1]-u[1]*v[0]
        if z:
            return -1 if z > 0 else 1
        return (i > j)-(i < j)

    ids.sort(key=cmp_to_key(compare))
    if normal[k] < 0:
        ids.reverse()
    at = ids.index(min(ids))
    ids = ids[at:] + ids[:at]
    for i in range(len(ids)):
        p, q, r = [points[ids[(i+j) % len(ids)]] for j in range(3)]
        assert dot(normal, cross(sub(q, p), sub(r, q))) > 0
    return ids


def initial_hull():
    vertices = set()
    directions = [(s if k == j else 0 for k in range(3))
                  for j in range(3) for s in (-1, 1)]
    directions = [tuple(v) for v in directions]
    bounded = {}
    for i, j, k in combinations(range(M), 3):
        a, b, c = N[i], N[j], N[k]
        bc, ca, ab = cross(b, c), cross(c, a), cross(a, b)
        denominator = dot(a, bc)
        if not denominator:
            continue
        for u in directions:
            if u not in bounded:
                numerators = [dot(u, v) for v in (bc, ca, ab)]
                if all(z*denominator >= 0 for z in numerators):
                    bounded[u] = ([i, j, k],
                                  [F(z, denominator) for z in numerators])
        numerator = mul(D, add(add(bc, ca), ab))
        if denominator < 0:
            denominator = -denominator
            numerator = mul(-1, numerator)
        if all(dot(n, numerator) <= D*denominator for n in N):
            vertices.add(tuple(F(v, denominator) for v in numerator))
    assert len(bounded) == 6, 'No complete boundedness certificate'
    points = sorted(vertices)
    faces = []
    for n in N:
        ids = [i for i, p in enumerate(points) if dot(n, p) == D]
        faces.append(polygon_order(ids, points, n))
    return points, faces, bounded


def edges_of(faces):
    edges, orientation = {}, {}
    for f, face in enumerate(faces):
        for i, j in zip(face, face[1:]+face[:1]):
            e = tuple(sorted((i, j)))
            edges.setdefault(e, []).append(f)
            orientation[e] = orientation.get(e, 0)+(1 if i < j else -1)
    assert all(len(v) == 2 for v in edges.values())
    assert all(v == 0 for v in orientation.values())
    return edges


def geometry_check(points, faces, normals, supports):
    assert len(faces) == len(normals) == len(supports)
    for face, n, h in zip(faces, normals, supports):
        equality = {i for i, p in enumerate(points) if dot(n, p) == h}
        assert equality == set(face)
        assert all(dot(n, p) <= h for p in points)
        polygon_order(face, points, n)
    edges = edges_of(faces)
    assert len(points)-len(edges)+len(faces) == 2
    neighbours = [set() for _ in points]
    for i, j in edges:
        neighbours[i].add(j)
        neighbours[j].add(i)
    assert all(len(v) >= 3 for v in neighbours)
    reached, todo = {0}, [0]
    for i in todo:
        for j in neighbours[i]:
            if j not in reached:
                reached.add(j)
                todo.append(j)
    assert len(reached) == len(points)
    return edges, neighbours


def mass(points, faces):
    o = mean(points)
    W = F(0)
    numerator = (F(0), F(0), F(0))
    for face in faces:
        a = points[face[0]]
        for j in range(1, len(face)-1):
            b, c = points[face[j]], points[face[j+1]]
            w = det(sub(a, o), sub(b, o), sub(c, o))
            assert w > 0
            W += w
            numerator = add(numerator, mul(w, add(add(o, a), add(b, c))))
    assert W > 0
    volume = W/6
    g = mul(F(1, 1)/(4*W), numerator)
    return volume, mul(volume, g), g


def bars(points, edges):
    radius = [dot(p, p) for p in points]
    events = []
    for i, j in sorted(edges):
        d = sub(points[j], points[i])
        dd = dot(d, d)
        assert dd > 0
        t = -dot(points[i], d)/dd
        if t <= 0:
            level = radius[i]
        elif t >= 1:
            level = radius[j]
        else:
            level = radius[i]-dot(points[i], d)**2/dd
        events.append((level, i, j))
    parent = list(range(len(points)))
    peak = parent[:]

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    result = []
    for level, i, j in sorted(events, key=lambda z: (-z[0], z[1], z[2])):
        a, b = find(i), find(j)
        if a == b:
            continue
        if (radius[peak[a]], peak[a]) < (radius[peak[b]], peak[b]):
            a, b = b, a
        birth = radius[peak[b]]
        assert birth >= level
        if birth > level:
            result.append(dict(root=peak[b], elder=peak[a],
                               birth=birth, death=level,
                               relative_depth=(birth-level)/birth,
                               attaining_edge=[i, j]))
        parent[b] = a
    return result


def audit(points, faces, normals, supports):
    edges, neighbours = geometry_check(points, faces, normals, supports)
    volume, moment, g = mass(points, faces)
    X = [sub(p, g) for p in points]
    S, U, H = [], [], []
    weak = [0, 0, 0]
    polar = []
    for f, (face, n, support) in enumerate(zip(faces, normals, supports)):
        h = support-dot(n, g)
        nn = dot(n, n)
        assert h > 0 and nn > 0
        polar.append(mul(1/h, n))
        guards = []
        for i, j in zip(face, face[1:]+face[:1]):
            z = sub(mul(h, n), mul(nn, X[i]))
            guards.append(dot(n, cross(sub(X[j], X[i]), z)))
        if all(z > 0 for z in guards):
            S.append(f)
        elif all(z >= 0 for z in guards):
            weak[0] += 1
    for i in range(len(points)):
        guards = [-dot(X[i], sub(X[j], X[i])) for j in neighbours[i]]
        if all(z > 0 for z in guards):
            U.append(i)
        elif all(z >= 0 for z in guards):
            weak[1] += 1
    for (i, j), (a, b) in sorted(edges.items()):
        d = sub(X[j], X[i])
        dd = dot(d, d)
        t = -dot(X[i], d)
        z = add(mul(dd, X[i]), mul(t, d))
        n, q = normals[a], normals[b]
        nn, qq, nq = dot(n, n), dot(q, q), dot(n, q)
        assert nn*qq-nq*nq > 0
        alpha = dot(z, n)*qq-dot(z, q)*nq
        beta = dot(z, q)*nn-dot(z, n)*nq
        guards = [t, dd-t, alpha, beta]
        if all(v > 0 for v in guards):
            H.append([i, j])
        elif all(v >= 0 for v in guards):
            weak[2] += 1
    dual_edges = {tuple(sorted(v)) for v in edges.values()}
    P = bars(X, edges)
    Q = bars(polar, dual_edges)
    return dict(V=len(points), E=len(edges), F=len(faces),
                strict=[len(S), len(U), len(H)], additional_weak=weak,
                stable_faces=S, unstable_vertices=U, saddle_edges=H,
                volume=volume, first_moment=moment, centroid=g,
                vertices=points, maximal_facets=faces,
                edges=[list(e) for e in sorted(edges)],
                P_bars=P, Q_bars=Q)


def clip(points, faces, normal, support):
    value = [dot(normal, p)-support for p in points]
    registry, new_points, new_faces = {}, [], []

    def index(p):
        p = tuple(p)
        if p not in registry:
            registry[p] = len(new_points)
            new_points.append(p)
        return registry[p]

    for face in faces:
        polygon = []
        for i, j in zip(face, face[1:]+face[:1]):
            if value[i] <= 0:
                polygon.append(index(points[i]))
            if value[i]*value[j] < 0:
                t = value[i]/(value[i]-value[j])
                p = add(points[i], mul(t, sub(points[j], points[i])))
                polygon.append(index(p))
        assert len(polygon) >= 3
        new_faces.append(polygon)
    cut = [i for i, p in enumerate(new_points) if dot(normal, p) == support]
    assert len(cut) == 4
    new_faces.append(polygon_order(cut, new_points, normal))
    return new_points, new_faces


def encode(obj):
    return (json.dumps(obj, default=str, sort_keys=True,
                       separators=(',', ':'))+'\n').encode()


def main():
    points, faces, bounded = initial_hull()
    edges, unused = geometry_check(points, faces, N, [D]*M)
    assert (len(points), len(edges), len(faces)) == (160, 240, 82)
    volume, moment, g = mass(points, faces)
    a, b = 43, 55
    ends = sorted(set(faces[a]) & set(faces[b]))
    assert len(ends) == 2 and set(edges[tuple(ends)]) == {a, b}
    u, v = [points[i] for i in ends]
    d = sub(v, u)
    t = -dot(sub(u, g), d)/dot(d, d)
    assert 0 < t < 1
    foot = add(u, mul(t, d))
    normal = sub(foot, g)
    rr = dot(normal, normal)
    assert rr > 0
    na, nb = N[a], N[b]
    aa, bb, ab = dot(na, na), dot(nb, nb), dot(na, nb)
    assert aa*bb-ab*ab > 0
    assert dot(normal, na)*bb-dot(normal, nb)*ab > 0
    assert dot(normal, nb)*aa-dot(normal, na)*ab > 0
    kept = [i for i in range(len(points)) if i not in ends]
    for i in ends:
        assert any(dot(sub(points[i], g), sub(points[j], points[i])) > 0
                   for j in kept)
    gap = min(rr-dot(normal, sub(points[i], g)) for i in kept)
    assert gap > 0
    epsilon0 = min(F(1, 2), gap/(2*rr))
    qstar = mul(1/rr, normal)
    qa = mul(1/(D-dot(na, g)), na)
    qb = mul(1/(D-dot(nb, g)), nb)
    A, B = dot(sub(qa, qstar), sub(qa, qstar)), dot(sub(qb, qstar), sub(qb, qstar))
    R = dot(qstar, qstar)
    assert A > 0 and B > 0
    assert dot(qstar, sub(qa, qstar)) == 0
    assert dot(qstar, sub(qb, qstar)) == 0
    attempts = []
    for k in count():
        epsilon = epsilon0/(2**k)
        support = dot(normal, g)+rr/(1+epsilon)
        p, f = clip(points, faces, normal, support)
        normals, supports = list(N)+[normal], [F(D)]*M+[support]
        z = audit(p, f, normals, supports)
        attempts.append(dict(k=k, epsilon=epsilon, strict=z['strict'],
                             additional_weak=z['additional_weak'],
                             P_count=len(z['P_bars']), Q_count=len(z['Q_bars'])))
        good = (z['strict'] == [3, 1, 2]
                and z['additional_weak'] == [0, 0, 0]
                and not z['P_bars'] and len(z['Q_bars']) == 2)
        if not good:
            continue
        assert (z['V'], z['E'], z['F']) == (162, 243, 83)
        z.update(parent_sha256=PARENT_SHA, k=k, epsilon=epsilon,
                 parent_volume=volume, parent_first_moment=moment,
                 parent_centroid=g, removed_volume=volume-z['volume'],
                 centroid_change=sub(z['centroid'], g),
                 polar_local_constants=dict(R=R, A=A, B=B),
                 fixed_reference_extra_depth=R*epsilon**2/(max(A, B)+R*epsilon**2),
                 attempts=attempts)
        assert z['removed_volume'] > 0
        raw_input = dict(name='KH93_RADIAL_SADDLE_BEVEL312',
                         normals=normals, supports=supports,
                         parent_sha256=PARENT_SHA, k=k, epsilon=epsilon)
        out = [('KH93_RADIAL_SADDLE_BEVEL312_INPUT.json', raw_input),
               ('KH93_RADIAL_SADDLE_BEVEL312_EXACT.json', z)]
        for filename, obj in out:
            data = encode(obj)
            Path(filename).write_bytes(data)
            print(filename, len(data), hashlib.sha256(data).hexdigest())
        print('k', k, 'epsilon', epsilon)
        print('own volume', z['volume'])
        print('own centroid', z['centroid'])
        print('P_bars', json.dumps(z['P_bars'], default=str))
        print('Q_bars', json.dumps(z['Q_bars'], default=str))
        print('KH93_RADIAL_SADDLE_BEVEL_OWN312_EXACT_PASS_NOT_110')
        return


if __name__ == '__main__':
    main()
```

## 5. Что переносить в следующий исследовательский шаг

Доказанный результат — не новое уменьшение рекордного Q и не исключение произвольной опорной перестройки. Он устанавливает конкретную причину, по которой естественная попытка поднять нынешнее полярное седло радиальной вставкой обманывает ведущий бар: **новая S защищена первым порядком геометрического запаса, тогда как собственная масса голого скоса реагирует лишь во втором порядке**.

Следующая содержательная вариация этого интерфейса должна нарушить именно эту защиту: совместно наклонять новую плоскость и двигать границу либо создавать физическое смещение центра первого порядка, достаточное для нарушения выведенного точного проекционного неравенства. При этом необходимо заново удерживать или восстанавливать собственную U1. Малый компенсатор, только возвращающий старый центр, сам по себе проблему новой S не решает.

Последний принятый точный геометрический вход остаётся **KH93_C434_R82_G6** и его ранее сохранённые siblings. Новое аналитическое препятствие имеет явно ограниченную область; новый выполненный exact successor в данном ответе не заявлен.
