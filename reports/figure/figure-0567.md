# figure-0567

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# NF94 — освобождение большой грани без выхода за бюджет

## Статус результата

**Новый собственный strict110 не подтверждён. Последним полностью подтверждённым вычислительным родителем остаётся NF93_DOUBLE_FLAP25: 92/224/134, own222, additional weak000, primitive-zero000.**

В этом продолжении возникло ограничение возврата инструментов: результаты последних вызовов не поступали в читаемый контекст, вместо содержимого отображалось `Skipped … message`. Поэтому я не могу подтвердить сохранность новых координатных файлов, прочитать их полные массивы, сверить receipts или объявить новые сообщения PASS наблюдёнными. Это не утверждение об отсутствии файлов и не отрицательный результат о геометрическом семействе. Рабочие имена NF94, использованные в попытках вычисления, не предлагаются как новые точные родители.

Ниже переданы **аналитически доказанный новый геометрический переход, ограниченное собственно-массовое исключение и полный детерминированный exact-патч**. Патч восстанавливает исходное тело, строит конечное рациональное тело с действительно разрушенной старой 26-угольной гранью, пересчитывает его заполненную массу, максимальные грани, настоящие рёбра, весь strict/closed-weak census и все положительные P/Q-бары. Его новые конечные receipts здесь не считаются наблюдёнными.

## 1. Существенная свобода: старую 26-угольную грань можно полностью отпустить

У NF93_DOUBLE_FLAP25 имеется 92 настоящие вершины и три большие максимальные грани: исходный 26-угольник, P-фартук с 14 углами и Q-фартук с 15 углами. Для любого выпуклого трёхмерного многогранника

`E = 3V − 6 − Σ_f (|f|−3)`.

**Два фартука сами дают дефицит 11+12=23. Следовательно, при сохранении только этих двух максимальных многоугольников и не более 92 входных точек всегда E≤247.** Сохранять старый 26-угольник ради бюджета не требуется. Его полная триангуляционная замена может добавить до 23 настоящих рёбер: 224→247, то есть C448→C494, всё ещё ниже целевой границы500.

Это отдельная возможность от прежних восьми добавлений при сохранении всех трёх граней. Она позволяет освободить 26 вертикальных координат старой большой грани, не добавляя ни одной входной точки. Условия сохранения двух фартуков остаются реальными геометрическими условиями; одна лишь формула их параметризации не гарантирует, что они опорные.

## 2. Конкретная неаффинная рациональная деформация

Используется именно буквальный L30 и точные два фартука NF93, а не FULL76 или C622. Материальная нумерация сохраняется.

Обозначим исходные 92 настоящие точки через p_i. Восемь уже внутренних исходных строк `[35,40,42,54,59,64,68,73]` удаляются из рабочего списка, но номера оставшихся строк не меняются. Старый максимальный 26-угольник имеет цикл

`[0,1,2,3,5,7,8,9,13,22,26,30,34,37,41,44,48,50,49,52,55,58,62,70,6,4]`.

Для его старых углов положим

`β_i = p_ix² + p_iz²`.

Для остальных старых настоящих вершин β_i=0. Скорости новых точек задаются совместимо с фартуками:

`β_(75+i−1) = (1−t_i)β_13 + t_i β_22`, где `t_i=i/13`, i=1,…,12;

`β_(87+i−1) = (1−s_i)β_70 + s_i β_6`, где `s_i=i/14`, i=1,…,13.

Деформация всех точек:

`p_i(ε) = p_i + ε β_i (0,1,0)`.

Это меняет геометрию корпуса и обоих фартуков совместно. Смещение каждой точки различно; семейство не является одним из исключённых общих Minkowski-лучей. Центр не назначается и не удерживается искусственно.

### Фартуки остаются плоскими тождественно

Исходная формула каждого фартука имеет вид

`p_a + t(p_b−p_a) + 4t(1−t)u/1024`.

После указанного движения она становится

`p_a(ε) + t(p_b(ε)−p_a(ε)) + 4t(1−t)u/1024`.

Следовательно, все точки каждого фартука по-прежнему лежат в одной плоскости. Пока векторы `p_b(ε)−p_a(ε)` и u линейно независимы, его 14 или 15 точек остаются вершинами выпуклого плоского многоугольника. Опорность и строгие зазоры к остальным точкам отдельно обеспечиваются ниже.

### Старый 26-угольник действительно перестаёт быть плоским

Для четырёх его материальных углов 0,1,4,6 прямое рациональное вычисление даёт

`det(p_1(ε)−p_0(ε), p_4(ε)−p_0(ε), p_6(ε)−p_0(ε))`

`= −114809492704140 ε / 10^16`.

Поэтому при **каждом ε>0** эти четыре точки некомпланарны. Речь не о независимом округлении, ложном разделении одной плоскости допуском или смене названия грани.

Полная размерность не исчезает: точки 10,17,38,69 вообще не движутся, а

`det(p_17−p_10, p_38−p_10, p_69−p_10) = −132326887319 / 10^12 ≠0`.

Эти четыре фиксированные аффинно независимые материальные точки также показывают, что описанное движение остальных точек не является просто общей аффинной заменой координат, фиксирующей сохранившийся материал.

## 3. Точный конечный интервал геометрической допустимости

Все точки движутся параллельно одной оси. Поэтому для любой четвёрки материальных точек её ориентированный объём является **аффинной функцией ε**: члены степени≥2 содержат два параллельных вектора и обращаются в ноль.

В частности, для каждой старой треугольной грани и для обеих плоскостей фартуков все опорные зазоры имеют вид

`s(ε)=s0+ε s1`.

У каждой точки вне соответствующей старой максимальной грани s0>0. Для сохранения строгой опорности достаточно включить в верхнюю границу ε каждое положительное число

`s0/(−2s1)` при s1<0.

Аналогично ограничивается изменение выбранной ненулевой компоненты нормали. Для сохранения всех старых настоящих вершин используются фиксированные строгие опорные функционалы: в вершине i суммируются положительно нормированные внешние нормали всех её старых инцидентных граней. Их зазоры к другим вершинам также аффинны по ε. Все эти проверки рациональны и конечны.

Патч вычисляет положительную рациональную границу η_geo по всем указанным неравенствам. На всём закрытом интервале `0≤ε≤η_geo` сохраняются оба фартука, все 131 старые треугольные грани и все 92 настоящие вершины. При ε>0 старая большая грань разрушена. Следовательно,

**`V=92`, `225≤E≤247`, `135≤F≤157`**

для положительной части этого интервала. Конкретные истинные E/F, новые опорные грани и их механика должны быть получены полным exact hull; верхние границы не заменяют этот аудит.

На каждом фиксированном новом hull-комплексе объём V(ε) аффинен, а первый момент M(ε) имеет степень не выше двух. Центроид равен действительному `M(ε)/V(ε)`, а не прежнему центру и не среднему вершин. Это даёт удобную основу для последующего точного анализа конечных событий.

## 4. Ограниченное собственно-массовое исключение

Малое разрушение большой грани само по себе не отменяет два старых U. Следующий сертификат учитывает изменение заполненного центра.

Пусть c0 — точный центроид NF93, `x_i=p_i−c0`. Выбираются рациональные величины

`R = max_i ||x_i||_1`,

`r = min_f (h_f−n_f·c0)/||n_f||_1`,

`μ = min_{i∈{6,70}, j≠i} −x_i·(p_j−p_i)`.

Здесь r>0 — нижняя оценка собственного инрадиуса, R — верхняя оценка радиуса, μ>0. Последнее следует из того, что строгий U является строгой опорной вершиной в радиальном направлении; проверка в патче выполняется против **всех** остальных точек, а не только выбранного леса.

Если максимальное смещение точек равно δ и δ≤r/4, то для центрированных относительно c0 тел

`(1−δ/r)K ⊂ K_ε ⊂ (1+δ/r)K`.

Из объёма и первого момента оболочки между этими двумя гомотетическими телами следует грубая, но достаточная оценка

`||c_ε−c0|| < 20Rδ/r`.

Действительно, внутреннее тело имеет нулевой первый момент; добавленная область имеет объём не более `((1+τ)^3−(1−τ)^3)V0`, радиус не более `(1+τ)R`, а знаменатель объёма не меньше `(1−τ)^3V0`, где τ=δ/r≤1/4. Получающийся коэффициент при Rτ меньше20.

При таком движении изменение каждого исходного радиального скалярного произведения в вершинах6/70 по абсолютной величине меньше

`55R²δ/r`.

Поэтому условие

`δ ≤ min(r/4, μr/(128R²))`

оставляет все эти произведения строго отрицательными, с запасом больше μ/2. Обе движущиеся материальные вершины6 и70 остаются строгими U относительно **нового однородного центроида**.

Для рассматриваемой деформации `δ≤ε B`, где `B=max_i |β_i|`. Положим

`η_mass = min(r/4, μr/(128R²))/B`.

Патч выбирает определённое двоичное рациональное ε* строго меньше `min(1,η_geo,η_mass)`.

**На всём `0≤ε≤ε*` доказано U≥2.** На положительной части интервала при этом уже разрушена исходная 26-угольная грань и сохраняется E≤247. Следовательно, этот конкретный малый переход не содержит собственного110.

Область вывода ограничена. Это не исключение полного cap-free семейства, больших амплитуд, иных скоростей корпуса, поворота фартуков, замены корней или всех тел с двумя большими гранями. Зафиксированные здесь корни — свидетели локального отрицательного сертификата, а не требование к следующему поиску. Никакого отсутствия дополнительных слабых равновесий на всём интервале не утверждается; для исключения110 достаточно двух доказанных строгих U.

## 5. Что это меняет в направлении исследования

Сохранение исходной большой грани больше не должно служить бюджетным ограничением поиска: **двух фартуков достаточно для E≤247 на 92 точках**. Новая геометрия не повторяет общий перенос тела, десятиузловой меридиональный опыт или локальный forest-проектор.

С другой стороны, бесконечное уменьшение амплитуды cap-free движения заведомо останется в собственно-массовой области с двумя U. Полезный следующий переход должен выйти из указанной области защиты корней, совместно изменяя P-носитель13–22, фартуки и корпус. После каждого выхода из опорной ячейки нужно заново строить истинный hull и центр. Две большие грани тоже могут быть заменены, если фактический E остаётся допустимым.

Ни один нечитавшийся рабочий NF94-файл не заменяет NF93. Полные strict/closed-weak значения нового двоичного контрольного тела, его точные V/M/c и все положительные P/Q остаются **заданием на выполнение приведённого ниже аудитора**, а не объявленными здесь receipts.

## 6. Источники и восстановление

Точные зависимости доступны в уже предоставленном контексте:

- NF93: `figure-0563`, объявленный SHA-256 `75a49e39ed5c26fb74e569bd80937e6e586d92b463edb78d8f666514c800c035`.
- JOINT56: `figure-0559`; буквальный `audit56.py`, 42703 байта, SHA-256 `1ca8d69e38bc029a0cb3e4d707cede38f65139e4d3c88010683c5fccbec24258`.

Ниже — полный патч к этому точному аудитору. Он принимает либо сам неизменённый `audit56.py`, либо старый журнал, содержащий его буквальный код. **Хеш нового журнала не подставляется вместо старого:** после извлечения проверяются байты самого модуля. Унаследованная неоднозначность хеша внешней родительской оболочки не объявляется разрешённой.

Сохранить код как `nf94_release.py`. Для CPython3.13.5 достаточно стандартной библиотеки:

```sh
python -B -S nf94_release.py --parent audit56.py --out NF94_RELEASE
# Альтернатива с ранее предоставленным журналом:
python -B -S nf94_release.py --parent 'research-journal(20260926-065407).md' --out NF94_RELEASE
```

Программа записывает полный исходный аудит, полный новый аудит и рациональный сертификат. `write_json` печатает фактические байты и SHA-256 каждого результата. Терминальный маркер `NF94_RELEASE_CAP_GEOMETRY_AND_OWN_U2_PASS` здесь **ожидаемый, не наблюдённый**. Для новых выходных файлов не приводятся неподтверждённые размеры или хеши.

## 7. Полный runnable source

```python
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import types

PARENT_BYTES = 42703
PARENT_SHA = '1ca8d69e38bc029a0cb3e4d707cede38f65139e4d3c88010683c5fccbec24258'
CAP = [0,1,2,3,5,7,8,9,13,22,26,30,34,37,41,44,48,50,49,52,55,58,62,70,6,4]
DROP = {35,40,42,54,59,64,68,73}
FP = [13] + list(range(75,87)) + [22]
FQ = [6,70] + list(range(87,100))
EY = (F(0), F(1), F(0))


def load_parent(path):
    path = Path(path)
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != PARENT_SHA:
        text = raw.decode('utf-8')
        heading = '## Модуль1 — audit56.py'
        if heading not in text:
            raise ValueError('Supply the literal audit56.py or the earlier journal containing it')
        section = text[text.index(heading):]
        code = section.split('```python\n', 1)[1].split('\n```', 1)[0] + '\n'
        raw = code.encode('utf-8')
    assert len(raw) == PARENT_BYTES
    assert hashlib.sha256(raw).hexdigest() == PARENT_SHA
    module = types.ModuleType('nf94_literal_parent')
    module.__file__ = str(path)
    exec(compile(raw.decode('utf-8'), str(path), 'exec'), module.__dict__)
    return module


def add(a, b):
    return tuple(x+y for x,y in zip(a,b))


def scale(t, a):
    return tuple(t*x for x in a)


def initial(a):
    p = list(a.points('JOINT56_L30'))
    directions = [
        (F(1918777,604052500), F(1), F(-193949,151013125)),
        (F(179328288526762213,213245086998660969),
         F(7070786827652000,30463583856951567), F(1))
    ]
    for (i,j),m,u in zip([(13,22),(70,6)],[12,13],directions):
        for k in range(1,m+1):
            t = F(k,m+1)
            q = add(add(scale(1-t,p[i]), scale(t,p[j])),
                    scale(4*t*(1-t)/1024,u))
            p.append(q)
    labels = [i for i in range(100) if i not in DROP]
    p = [p[i] for i in labels]
    assert len(p) == len(set(p)) == 92
    return p, labels


def material_data(K, p, labels):
    ids = dict(zip(p,labels))
    K['material_vertices'] = [ids[q] for q in K['points']]
    K['material_faces'] = [[ids[K['points'][i]] for i in f] for f in K['faces']]
    K['material_U'] = [ids[K['points'][i]] for i in K['U']]
    K['material_S'] = [K['material_faces'][i] for i in K['S']]
    K['material_H'] = [[ids[K['points'][i]] for i in e] for e in K['H']]
    for bar in K['P_bars']:
        bar['material_peak'] = ids[K['points'][bar['peak']]]
        bar['material_elder'] = ids[K['points'][bar['elder']]]
        bar['material_component'] = [ids[K['points'][i]] for i in bar['component']]
        bar['material_cut'] = [[ids[K['points'][i]] for i in e] for e in bar['cut']]
        bar['material_path'] = [ids[K['points'][i]] for i in bar['attaining_path']]
    for bar in K['Q_bars']:
        bar['material_peak_face'] = K['material_faces'][bar['peak']]
        bar['material_elder_face'] = K['material_faces'][bar['elder']]
        bar['material_attaining_faces'] = [K['material_faces'][i] for i in bar['attaining_edge']]
    return K


def speeds(p, labels):
    by_label = dict(zip(labels,p))
    beta = {i:F(0) for i in labels}
    for i in CAP:
        x,y,z = by_label[i]
        beta[i] = x*x + z*z
    for first,(i,j),m in [(75,(13,22),12),(87,(70,6),13)]:
        for k in range(1,m+1):
            t = F(k,m+1)
            beta[first+k-1] = (1-t)*beta[i] + t*beta[j]
    return [beta[i] for i in labels]


def geometric_bounds(a, A, p, labels, beta):
    # All stored guards are exact affine functions s0 + epsilon*s1.
    # A factor 1/2 is retained in every decreasing strict guard.
    at = {label:i for i,label in enumerate(labels)}
    by_point = {q:i for i,q in enumerate(p)}
    face_rows = [[by_point[A['points'][i]] for i in f] for f in A['faces']]
    cap_index = next(k for k,f in enumerate(face_rows)
                     if {labels[i] for i in f} == set(CAP))
    bounds = [F(1)]
    guards = []

    def retain(s0, s1, tag):
        assert s0 > 0, tag
        guards.append(dict(tag=tag, constant=s0, linear=s1))
        if s1 < 0:
            bounds.append(s0/(-2*s1))

    for fi,f in enumerate(face_rows):
        if fi == cap_index:
            continue
        i,j,k = f[:3]
        e = a.sub(p[j],p[i])
        d = a.sub(p[k],p[i])
        de = scale(beta[j]-beta[i],EY)
        dd = scale(beta[k]-beta[i],EY)
        n0 = a.cross(e,d)
        n1 = add(a.cross(de,d), a.cross(e,dd))
        assert a.cross(de,dd) == (0,0,0)
        assert n1[1] == 0
        nc = max(range(3),key=lambda q:abs(n0[q]))
        assert n0[nc] != 0
        sign = 1 if n0[nc] > 0 else -1
        retain(sign*n0[nc],sign*n1[nc],['normal',fi,nc])
        for q in range(len(p)):
            v = a.sub(p[i],p[q])
            dv = scale(beta[i]-beta[q],EY)
            s0 = a.dot(n0,v)
            s1 = a.dot(n1,v) + a.dot(n0,dv)
            assert a.dot(n1,dv) == 0
            if q in f:
                assert s0 == s1 == 0, (fi,labels[q])
            else:
                retain(s0,s1,['face',fi,labels[q]])

    # Positive normalized sums of incident outward normals uniquely expose
    # every original true vertex. These normals are held fixed in this test.
    ns = [tuple(F(x,sum(abs(t) for t in plane[:3])) for x in plane[:3])
          for plane in A['planes']]
    for i in range(len(p)):
        incident = [k for k,f in enumerate(face_rows) if i in f]
        w = tuple(sum(ns[k][q] for k in incident) for q in range(3))
        assert any(w)
        for j in range(len(p)):
            if i == j:
                continue
            s0 = a.dot(w,a.sub(p[i],p[j]))
            s1 = w[1]*(beta[i]-beta[j])
            retain(s0,s1,['vertex',labels[i],labels[j]])
    return min(bounds), guards, cap_index, face_rows


def mechanical_bound(a, A, p, labels, beta):
    c = A['centroid']
    x = [a.sub(q,c) for q in p]
    R = max(sum(abs(t) for t in q) for q in x)
    r = min((plane[3]-a.dot(plane[:3],c)) /
            sum(abs(t) for t in plane[:3]) for plane in A['planes'])
    assert 0 < r <= R
    at = {label:i for i,label in enumerate(labels)}
    all_margins = []
    for root in [6,70]:
        i = at[root]
        for j in range(len(p)):
            if i == j:
                continue
            q = -a.dot(x[i],a.sub(p[j],p[i]))
            assert q > 0
            all_margins.append(dict(root=root,other=labels[j],margin=q))
    mu = min(q['margin'] for q in all_margins)
    B = max(abs(q) for q in beta)
    assert B > 0
    delta = min(r/4,mu*r/(128*R*R))
    eta = delta/B
    return eta,dict(R=R,r=r,mu=mu,B=B,delta=delta,
                    centroid_constant=20,radial_error_constant=55,
                    global_root_margins=all_margins)


def run(parent,out):
    a = load_parent(parent)
    out = Path(out)
    out.mkdir(parents=True,exist_ok=True)
    p,labels = initial(a)
    A = a.audit(p,'NF93_DOUBLE_FLAP25_BASE')
    material_data(A,p,labels)
    assert (A['V'],A['E'],A['F']) == (92,224,134)
    assert A['strict'] == [2,2,2]
    assert A['additional_weak'] == A['primitive_zero'] == [0,0,0]
    assert sorted(A['material_U']) == [6,70]
    sets = {frozenset(f) for f in A['material_faces']}
    assert frozenset(CAP) in sets
    assert frozenset(FP) in sets and frozenset(FQ) in sets
    assert sorted(map(len,A['faces']),reverse=True)[:3] == [26,15,14]

    beta = speeds(p,labels)
    at = {label:i for i,label in enumerate(labels)}
    fixed = [10,17,38,69]
    assert all(beta[at[i]] == 0 for i in fixed)
    q = [p[at[i]] for i in fixed]
    assert a.det(a.sub(q[1],q[0]),a.sub(q[2],q[0]),a.sub(q[3],q[0])) == F(-132326887319,10**12)

    eta_geo,guards,cap_index,old_faces = geometric_bounds(a,A,p,labels,beta)
    eta_mass,mechanical = mechanical_bound(a,A,p,labels,beta)
    limit = min(F(1),eta_geo,eta_mass)
    assert limit > 0
    epsilon = F(1)
    while epsilon >= limit:
        epsilon /= 2
    new = [add(q,scale(epsilon*b,EY)) for q,b in zip(p,beta)]

    # This identity proves actual loss of the old supporting polygon.
    q = [new[at[i]] for i in [0,1,4,6]]
    lost_plane_det = a.det(a.sub(q[1],q[0]),a.sub(q[2],q[0]),a.sub(q[3],q[0]))
    assert lost_plane_det == -F(114809492704140,10**16)*epsilon
    assert lost_plane_det != 0

    K = a.audit(new,'NF94_CAP_RELEASE_DYADIC_CONTROL')
    material_data(K,new,labels)
    assert K['V'] == 92
    assert 225 <= K['E'] <= 247
    assert 135 <= K['F'] <= 157
    new_faces = {frozenset(f) for f in K['material_faces']}
    assert frozenset(CAP) not in new_faces
    assert frozenset(FP) in new_faces and frozenset(FQ) in new_faces
    for fi,f in enumerate(A['material_faces']):
        if fi != cap_index:
            assert frozenset(f) in new_faces

    # This is a direct endpoint check in addition to the uniform mass bound.
    # It uses the NEW filled centroid and ALL other actual input points.
    for root in [6,70]:
        i = at[root]
        radial = a.sub(new[i],K['centroid'])
        assert all(a.dot(radial,a.sub(new[j],new[i])) < 0
                   for j in range(len(new)) if j != i)
    assert set([6,70]) <= set(K['material_U'])

    certificate = dict(
        source_module_sha256=PARENT_SHA,
        epsilon=epsilon,
        geometric_limit=eta_geo,
        mechanical_limit=eta_mass,
        interval=[F(0),epsilon],
        labels=labels,
        speeds=beta,
        affine_geometry_guards=guards,
        mass_and_root_bound=mechanical,
        cap_nonplanarity_determinant=lost_plane_det,
        guaranteed_U=[6,70],
        no110_scope='This closed parameter interval only; no global family exclusion'
    )
    a.write_json(out/'parent_audit.json',A)
    a.write_json(out/'candidate_audit.json',K)
    a.write_json(out/'certificate.json',certificate)
    print('ACTUAL_CENSUS',K['V'],K['E'],K['F'],K['strict'],
          K['additional_weak'],K['primitive_zero'])
    print('ACTUAL_VOLUME',str(K['volume']))
    print('ACTUAL_MOMENT',[str(v) for v in K['moment']])
    print('ACTUAL_CENTROID',[str(v) for v in K['centroid']])
    print('ALL_POSITIVE_P',[str(b['depth']) for b in K['P_bars']])
    print('ALL_POSITIVE_Q',[str(b['depth']) for b in K['Q_bars']])
    print('NF94_RELEASE_CAP_GEOMETRY_AND_OWN_U2_PASS')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--parent',required=True)
    ap.add_argument('--out',default='NF94_RELEASE')
    args = ap.parse_args()
    run(args.parent,args.out)
```

## Граница handoff

Воспроизводимы исходная NF93-геометрия, новое рациональное семейство, правило выбора конечной амплитуды и полный код проверки. Доказаны возможность разрушения большой грани внутри бюджета и отсутствие110 на явно определённом малом собственно-массовом интервале. **Новый численно прочитанный и полностью сверенный equilibrium endpoint в этом ответе не заявляется.**
