# figure-0360

AI research report · 2026-09-13 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Nimble Harbor 72 — проективная перестройка всего тела с зависимым объёмным центром

## 1. Статус

**Новый подтверждённый strict(1,1,0) ниже C630 не получен.** Для нового семейства, определённого ниже, здесь не удостоверены новый полный ценз, два независимых точных аудита и завершённый холодный повтор. Поэтому новый рекорд или принятый точный непобедитель не объявляется.

Получена конструктивная модель, которая меняет одновременно весь радиальный бассейн, его границу и распределение заполненного объёма: конечное проективное изменение выпуклой оболочки H94 и семи физических точек. Собственный центроид в этой модели вычисляется как рациональная функция той же геометрии. Он не является независимо выбираемой переменной.

Неизменённый исходный объект остаётся буквальным `NH72_CUT_H94_E235`: V143/E235/F94, own121, единственная стабильная грань original3, дополнительные U58 и U66 в родительской нумерации, нежелательный бассейн117 вершин и граница67 настоящих рёбер. Его новый допустимый бюджет —79 дополнительных рёбер до E314. Старое ограничение14 рёбер здесь не используется. 

Ниже приведена **точная надстройка над буквальным родителем**, включая все новые параметры и полный исполняемый исходник. Неизменённые94 строки H94 извлекаются из уже приложенного `FINAL_SOURCE_DICT.json`. Они не перепечатаны в этой передаче, поэтому это не автономная транспортная капсула, содержащая родительскую таблицу внутри самого сообщения. Это ограничение не следует скрывать за хешем или объявлением нового принятого объекта.

## 2. Новая конечная геометрия

Пусть

`K = {x : I_i·x ≤ D, i=0,...,93}`,

где `I,D` — неизменённые данные `NH72_CUT_H94_E235`, а не физические координаты вершин.

К точным физическим вершинам K добавляются следующие семь сырых физических точек. Каждая строка делится на `10^12`:

```text
[-140188728918, 416696740554, -447253616886]
[-194346145352, 551872809726, -279887745792]
[-229986457842, 637081596980,  -64192487364]
[-241165392512, 657435790576,  182884005081]
[-223805749295, 603101794212,  439083276571]
[-176347613381, 470933255325,  678547202804]
[-100210995164, 265595179822,  874110062167]
```

Обозначим их W0,...,W6 и положим

`B = conv(K ∪ {W0,...,W6})`.

Это известный исходный семиточечный интерфейс, а не новая заявленная победа. Его прежний численный собственный класс18/36/52 не превращается в110 от наличия правильной цепи при старом центре.

Новая операция применяется ко **всему B**, а не только к семи точкам или к нежелательной вершине. Возьмём

`T = (16,−15,−6)`.

Для каждого рационального L, удовлетворяющего

`L + T·x > 0 для всех x∈B`,

и `s=L−6>0`, определим

`F_L(x) = s x / (L + T·x)`.

Новое заполненное тело:

`Q_L = F_L(B)`,

а предъявляемая центрированная фигура:

`Q_L − centroid_volume(Q_L)`.

### Безусловно допустимый конечный параметр

Не требуется угадывать, пересечёт ли проективный горизонт исходное тело. Пусть X — конечный список всех точных вершин K и семи W-точек. Определим точно

`m = max_{x∈X}|T·x|`,

`L_safe = m + 1`,

`s_safe = L_safe − 6`.

Сырой апекс `(0,0,1)` принадлежит исходному списку, поэтому m≥6 и s_safe≥1. Для всего B выполняется

`L_safe + T·x ≥ 1`.

Следовательно, `Q_safe=F_{L_safe}(B)` — однозначно определённый конечный рациональный полноразмерный выпуклый многогранник. Никакое предельное вырождение не используется. Его собственные равновесия, однако, ещё требуется вычислить: корректность геометрического определения не доказывает110.

Отдельный простой параметр `L=16`, то есть

`F_16(x)=10x/(16+16x−15y−6z)`,

также включён в программу как отдельный эксперимент. Он исполняется только после точной проверки положительности всех знаменателей. Его допустимость не подменяется предположением.

### Что сохраняется, а что меняется

При положительном знаменателе F_L взаимно однозначно переводит отрезки в отрезки и сохраняет решётку граней. Поэтому Q_L имеет **ровно тот же фактический V/E/F, что и точно восстановленная оболочка B**. Проективный этап сам по себе не расходует дополнительных рёбер.

При этом он не сохраняет углы, расстояния до собственного центра, обычный объём или равновесный класс. Старые117 вершин нельзя продолжать считать замкнутым нежелательным бассейном без нового полного расчёта.

Прежний экран семиточечного B давал E285. Это оставляло бы29 рёбер до314, **если точный пересчёт подтверждает такой комплекс**. Здесь численный E285 не объявляется новым точным фактом. Программа восстанавливает действительные вершины, максимальные грани и настоящие рёбра, прежде чем выводить бюджет.

## 3. Полная рациональная система новых опор

Пусть максимальная грань B имеет точное неравенство

`n·x ≤ h`.

Для y=F_L(x) обратная формула имеет вид

`x = L y / (s−T·y)`.

Соответствующая новая опора равна

`(L n + h T)·y ≤ h s`.

Это формула для **каждой** максимальной грани B. Она не является применением одного из исключённых элементарных shear-преобразований и не является поиском почти единичной метрики. Меняется само физическое тело. После очистки знаменателей все новые опоры целочисленны.

Новые грани, появившиеся от W-точек, также проходят через эту формулу. Они не отождествляются со старыми исходными метками supports. Исходник сохраняет полный список физических генераторов и все восстановленные H-строки.

## 4. Собственный заполненный объём и моментное замыкание

Пусть `(a,b,c)` пробегает наружные интеграционные треугольники **максимальных граней B**, а

`w=det(a,b,c)`,

`d_a=L+T·a`, `d_b=L+T·b`, `d_c=L+T·c`.

Определим рациональные суммы

`A = Σ w/(d_a d_b d_c)`,

`R = (1/4) Σ [w/(d_a d_b d_c)]·(a/d_a+b/d_b+c/d_c)`.

Тогда для равномерно заполненного нового тела точно

`Vol(Q_L) = s^3 A/6`,

`Moment(Q_L) = s^4 R/6`,

`centroid_volume(Q_L) = s R/A`.

Таким образом, собственный центр — зависимая рациональная функция тех же физических данных. Нельзя подставить старый центр H94 вместо `sR/A`.

Якобиан преобразования даёт дополнительное объяснение механизма:

`det DF_L(x) = s^3 L/(L+T·x)^4 > 0`.

Это формула замены переменных для вычисления **обычного объёма нового равномерно заполненного тела**. Она не вводит неравномерную плотность в определение нового тела и не подменяет его заполнение точечными массами.

Если дальнейшая физическая оптимизация должна сохранять некоторый прежний центр c0, правильные уравнения —

`s R − A c0 = 0`.

Это три уравнения на физическую геометрию, например на T и координаты W-точек. Назначение `c=c0` без выполнения этих уравнений не является моментным замыканием. Существование подходящего ненулевого решения этих уравнений вместе со strict110 здесь не доказано.

## 5. Полный радиальный тест после перестройки

Для старой физической вершины x_i обозначим `d_i=L+T·x_i`. После проективного изменения и собственного центрирования

`p_i = s(A x_i−d_i R)/(A d_i)`.

Поэтому знак настоящего радиального перехода i→j равен знаку

`(A x_i−d_i R)·(d_i x_j−d_j x_i)`.

Все опущенные множители положительны. Это учитывает изменение собственного объёмного центра.

Для старой максимальной опоры `(n_i,h_i)` положим

`ν_i=L n_i+h_i T`,

`C_i=h_i A−ν_i·R`.

Собственная внутренняя центровка даёт C_i>0. Центрированный полюс новой физической грани:

`Y_i = A ν_i/(s C_i)`.

Знак полярного перехода i→j равен знаку

`C_i(ν_i·ν_j)−C_j(ν_i·ν_i)`.

Примальные и полярные тесты, таким образом, связаны **одними и теми же A,R и заполненным телом**. Центроид полярного объёма нигде не нужен.

Для каждого конечного предложения необходимо заново построить оба графа, вычислить корни и полный бассейн относительно выбранного корня. Перенос прежней117-вершинной принадлежности по старым номерам недостаточен. Положительные свидетели могут ссылаться только на действительные точки нового тела, не на виртуальные углы пересечения старых троек опор.

### Почему жадная смена свидетелей может имитировать прогресс

Для любого ориентированного цикла действительных центрированных точек

`p0→p1→...→pk=p0`

имеем точное тождество

`Σ p_i·(p_{i+1}−p_i) = −(1/2)Σ |p_{i+1}−p_i|^2`.

Поэтому нет нетривиального цикла, на котором все радиальные переходы строго положительны. В частности,

`p·(q−p)+q·(p−q)=−|p−q|^2`.

Если нежелательной вершине назначить выход к соседу, а соседу оставить обратный выход, такая система строгих свидетелей невыполнима при любой форме тела и любом выборе собственного центра. Уменьшение квадратичного штрафа может просто сокращать расстояние между этими точками. Оно не доказывает уничтожения полного бассейна.

Полезный объект оптимизации — ациклическая система действительных выходов, охватывающая все некорневые вершины, и аналогичная система для всех некорневых центрированных полюсов. После изменения геометрии их положительность должна проверяться заново. Это не утверждение о невозможности самой геометрической задачи.

## 6. Полный исходник точного конечного эксперимента

Следующая программа не использует NumPy, SciPy, численные оболочки, сохранённые центроиды или старые инцидентности. Она:

- проверяет точные байты родительского источника и H94;
- восстанавливает физические вершины H94;
- строит полную рациональную оболочку с семью W-точками;
- строит безопасное проективное тело и, когда допустимо, отдельное тело L16;
- восстанавливает максимальные грани и настоящие рёбра;
- вычисляет обычный объём и все первые моменты;
- проверяет собственную центровку отдельным целочисленным интегрированием;
- выполняет исчерпывающий strict/weak ценз граней, вершин и всех четырёх компонент каждого настоящего ребра;
- заново выделяет замкнутый нежелательный бассейн в графе настоящих рёбер.

Это **одна точная реализация с дополнительной проверкой массы**, а не две независимые полные реализации. Код ниже не обозначается как уже наблюдавшийся успешный холодный повтор.

Сохранить как `projective_basin.py`. Требуется Python3.11 или новее, только стандартная библиотека, assertions включены.

```python
import hashlib
import json
import math
import sys
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path

assert __debug__, 'Do not use python -O'
sys.set_int_max_str_digits(0)

SOURCE_SHA = 'a5f009afa5037a0310dcd9dd039be810ceecbec4f751f5bab8c71dbd1deb4aec'
RAW_SHA = 'd4f527efc8acf12badf5158d5b87685c062d9f46fee977d8180d8035e4ac69c5'
BODY = 'exact/bodies/NH72_CUT_H94_E235/'
WNUM = [
    [-140188728918,416696740554,-447253616886],
    [-194346145352,551872809726,-279887745792],
    [-229986457842,637081596980,-64192487364],
    [-241165392512,657435790576,182884005081],
    [-223805749295,603101794212,439083276571],
    [-176347613381,470933255325,678547202804],
    [-100210995164,265595179822,874110062167],
]
T = (16,-15,-6)


def add(a,b):
    return tuple(x+y for x,y in zip(a,b))


def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))


def mul(k,a):
    return tuple(k*x for x in a)


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],
            a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])


def det(a,b,c):
    return dot(a,cross(b,c))


def sign(x):
    return (x>0)-(x<0)


def primitive(a):
    g=math.gcd(*a)
    assert g>0
    return tuple(x//g for x in a)


def homogeneous(x):
    x=tuple(map(Q,x))
    d=math.lcm(*(v.denominator for v in x))
    return primitive(tuple(int(d*v) for v in x)+(d,))


def rational_plane(row):
    row=tuple(map(Q,row))
    d=math.lcm(*(v.denominator for v in row))
    return primitive(tuple(int(d*v) for v in row))


def core_vertices(I,D):
    assert D>0 and len(set(map(tuple,I)))==len(I)
    vertices=set()
    for a,b,c in combinations(I,3):
        u,v,w=cross(b,c),cross(c,a),cross(a,b)
        d=dot(a,u)
        if d==0:
            continue
        p=mul(D,add(add(u,v),w))
        if d<0:
            p=mul(-1,p)
            d=-d
        if all(dot(n,p)<=D*d for n in I):
            vertices.add(primitive(p+(d,)))
    assert len(vertices)>=4
    return sorted(vertices)


def supporting_hull(P):
    H=set()
    for a,b,c in combinations(P,3):
        e=sub(mul(a[3],b[:3]),mul(b[3],a[:3]))
        f=sub(mul(a[3],c[:3]),mul(c[3],a[:3]))
        n=cross(e,f)
        if not any(n):
            continue
        h=primitive(mul(a[3],n)+(dot(n,a[:3]),))
        pos=neg=False
        for p in P:
            z=dot(h[:3],p[:3])-h[3]*p[3]
            pos=pos or z>0
            neg=neg or z<0
            if pos and neg:
                break
        if pos and neg:
            continue
        assert pos or neg, 'The whole input must be full dimensional'
        if pos:
            h=mul(-1,h)
        assert h[3]>0, 'The origin must be strictly interior'
        H.add(h)
    assert len(H)>=4
    return sorted(H)


def audit(P,H):
    assert len(set(P))==len(P)
    assert all(h[3]>0 for h in H)
    assert all(dot(h[:3],p[:3])<=h[3]*p[3] for h in H for p in P)
    owners=[[] for p in P]
    for f,h in enumerate(H):
        for j,p in enumerate(P):
            if dot(h[:3],p[:3])==h[3]*p[3]:
                owners[j].append(f)
    used=[]
    for j,own in enumerate(owners):
        if any(det(H[a][:3],H[b][:3],H[c][:3])!=0
               for a,b,c in combinations(own,3)):
            used.append(j)
    used.sort(key=lambda j:tuple(Q(v,P[j][3]) for v in P[j][:3]))
    A=[P[j] for j in used]
    X=[tuple(Q(v,p[3]) for v in p[:3]) for p in A]
    contacts=[{j for j,p in enumerate(A)
               if dot(h[:3],p[:3])==h[3]*p[3]} for h in H]
    assert all(len(s)>=3 for s in contacts)
    edgeowners={}
    for f,g in combinations(range(len(H)),2):
        shared=contacts[f]&contacts[g]
        if len(shared)>=2:
            assert len(shared)==2
            edge=tuple(sorted(shared))
            assert edge not in edgeowners
            edgeowners[edge]=(f,g)
    E=sorted(edgeowners)
    assert len(X)-len(E)+len(H)==2
    faces=[]
    for f,vs in enumerate(contacts):
        adjacent={i:[] for i in vs}
        for (i,j),fg in edgeowners.items():
            if f in fg:
                adjacent[i].append(j)
                adjacent[j].append(i)
        assert all(len(a)==2 for a in adjacent.values())
        first=min(vs)
        cycle=[first]
        previous=first
        current=min(adjacent[first])
        while current!=first:
            assert current not in cycle
            cycle.append(current)
            nxt=next(j for j in adjacent[current] if j!=previous)
            previous,current=current,nxt
        assert set(cycle)==vs
        a,b,c=(X[cycle[k]] for k in range(3))
        if det(H[f][:3],sub(b,a),sub(c,a))<0:
            cycle=[cycle[0]]+cycle[:0:-1]
        faces.append(cycle)
    triangles=[(cy[0],cy[j],cy[j+1]) for cy in faces
               for j in range(1,len(cy)-1)]
    volume=Q(0)
    moment=(Q(0),)*3
    for i,j,k in triangles:
        a,b,c=X[i],X[j],X[k]
        w=det(a,b,c)
        assert w>0
        volume+=w/6
        moment=add(moment,mul(w/24,add(add(a,b),c)))
    assert volume>0
    centre=mul(1/volume,moment)
    assert all(dot(h[:3],centre)<h[3] for h in H)
    dc=math.lcm(*(v.denominator for v in centre))
    C=tuple(int(dc*v) for v in centre)
    Z=[sub(mul(dc,p[:3]),mul(p[3],C)) for p in A]

    def edge_vector(i,j):
        return sub(mul(A[i][3],A[j][:3]),mul(A[j][3],A[i][:3]))

    def arrow(i,j):
        return dot(Z[i],edge_vector(i,j))

    stable=[]
    unstable=[]
    saddles=[]
    weak_faces=[]
    weak_vertices=[]
    weak_edges=[]
    face_signs=[]
    vertex_signs=[]
    edge_signs=[]
    for f,cy in enumerate(faces):
        values=[sign(dot(H[f][:3],cross(Z[i],edge_vector(i,j))))
                for i,j in zip(cy,cy[1:]+cy[:1])]
        face_signs.append(values)
        if min(values)>0:
            stable.append(f)
        elif min(values)==0:
            weak_faces.append(f)
    for i in range(len(X)):
        value=max(sign(arrow(i,j)) for j in range(len(X)) if j!=i)
        vertex_signs.append(value)
        if value<0:
            unstable.append(i)
        elif value==0:
            weak_vertices.append(i)
    for i,j in E:
        e=edge_vector(i,j)
        ell=dot(e,e)
        d=dot(Z[i],e)
        assert ell>0
        f,g=edgeowners[i,j]
        n,m=H[f][:3],H[g][:3]
        aa,bb,cc=dot(n,n),dot(n,m),dot(m,m)
        assert aa*cc-bb*bb>0
        footnum=sub(mul(ell,Z[i]),mul(d,e))
        values=[-d*A[j][3],dc*ell+d*A[j][3],
                dot(footnum,sub(mul(cc,n),mul(bb,m))),
                dot(footnum,sub(mul(aa,m),mul(bb,n)))]
        signs=list(map(sign,values))
        edge_signs.append(signs)
        if min(signs)>0:
            saddles.append([i,j])
        elif min(signs)==0:
            weak_edges.append([i,j])

    # Separate exact integer integration of the centred body.
    L=math.lcm(*(dc*p[3] for p in A))
    R=[mul(L//(dc*p[3]),z) for p,z in zip(A,Z)]
    total=0
    first=(0,0,0)
    for i,j,k in triangles:
        w=det(R[i],R[j],R[k])
        assert w>0
        total+=w
        first=add(first,mul(w,add(add(R[i],R[j]),R[k])))
    assert Q(total,6*L**3)==volume
    assert first==(0,0,0)

    root=max(range(len(X)),key=lambda i:dot(R[i],R[i]))
    assert root in unstable
    graph=[set() for x in X]
    for i,j in E:
        if arrow(i,j)>0:
            graph[i].add(j)
        if arrow(j,i)>0:
            graph[j].add(i)
    reached={root}
    while True:
        newer=reached|{i for i,a in enumerate(graph) if a&reached}
        if newer==reached:
            break
        reached=newer
    bad=set(range(len(X)))-reached
    assert all(graph[i]<=bad for i in bad)
    boundary=[list(e) for e in E if (e[0] in bad)!=(e[1] in bad)]

    def bits(seq):
        seq=list(map(Q,seq))
        return [max(abs(v.numerator).bit_length() for v in seq),
                max(v.denominator.bit_length() for v in seq)]

    counts=[len(stable),len(unstable),len(saddles)]
    weak=[len(weak_faces),len(weak_vertices),len(weak_edges)]
    edgezero=sum(v==0 for a in edge_signs for v in a)
    return dict(
        V=len(X),E=len(E),F=len(faces),edge_budget=2*len(E),
        source_indices=used,H=[list(h) for h in H],
        raw_vertices=[[str(v) for v in x] for x in X],
        faces=faces,edges=[list(e) for e in E],
        ordinary_volume=str(volume),raw_first_moments=list(map(str,moment)),
        raw_centroid=list(map(str,centre)),centred_first_moments=['0','0','0'],
        counts=counts,weak=weak,stable_faces=stable,unstable_vertices=unstable,
        saddle_edges=saddles,weak_faces=weak_faces,weak_vertices=weak_vertices,
        weak_edges=weak_edges,face_signs=face_signs,
        vertex_max_escape_signs=vertex_signs,edge_signs=edge_signs,
        edge_primitive_count=4*len(E),edge_primitive_zero_count=edgezero,
        face_primitive_zero_count=sum(v==0 for a in face_signs for v in a),
        vertex_max_zero_count=vertex_signs.count(0),
        actual_edge_graph_root=root,root_reaching_vertices=sorted(reached),
        closed_unwanted_vertices=sorted(bad),basin_boundary_edges=boundary,
        fraction_bits=dict(raw_vertices=bits(v for x in X for v in x),
                           centroid=bits(centre),first_moments=bits(moment),
                           volume=bits([volume]),
                           centred_vertices=bits(Q(z,dc*p[3])
                              for p,zz in zip(A,Z) for z in zz)),
        passes_one_implementation_110_gate=(
            counts==[1,1,0] and weak==[0,0,0]
            and edgezero==0 and len(E)<=314))


def write_json(path,obj):
    path.write_text(json.dumps(obj,sort_keys=True,separators=(',',':')),
                    encoding='utf-8')


def main(source_path,out_path):
    source=Path(source_path).read_bytes()
    assert hashlib.sha256(source).hexdigest()==SOURCE_SHA
    archive=json.loads(source)
    raw_text=archive[BODY+'RAW.json']
    assert hashlib.sha256(raw_text.encode()).hexdigest()==RAW_SHA
    raw=json.loads(raw_text)
    labels=json.loads(archive[BODY+'LABELS.json'])
    assert len(raw['I'])==len(labels)==94
    core=core_vertices(raw['I'],raw['D'])
    assert len(core)==143 and (0,0,1,1) in core
    W=[homogeneous(tuple(Q(v,10**12) for v in row)) for row in WNUM]
    P=core+W
    assert len(set(P))==len(P)
    H=supporting_hull(P)
    seed=audit(P,H)
    out=Path(out_path)
    out.mkdir(exist_ok=False)
    (out/'PARENT_RAW.json').write_text(raw_text,encoding='utf-8')
    write_json(out/'PARENT_LABELS.json',labels)
    write_json(out/'SEED.json',seed)
    X=[tuple(Q(v,p[3]) for v in p[:3]) for p in P]
    maximum=max(abs(dot(T,x)) for x in X)
    assert maximum>=6
    parameters=[('SAFE',maximum+1),('L16',Q(16))]
    for name,L in parameters:
        s=L+T[2]
        ds=[L+dot(T,x) for x in X]
        if s<=0 or min(ds)<=0:
            write_json(out/(name+'_REJECTED.json'),
                       dict(reason='projective horizon or orientation',L=str(L)))
            continue
        Y=[homogeneous(mul(s/d,x)) for x,d in zip(X,ds)]
        HH=[rational_plane(tuple(L*h[k]+h[3]*T[k] for k in range(3))
                           +(s*h[3],)) for h in H]
        report=audit(Y,HH)
        assert [report[k] for k in ('V','E','F')]==[seed[k] for k in ('V','E','F')]
        oldedges={tuple(sorted(seed['source_indices'][i] for i in e))
                  for e in seed['edges']}
        newedges={tuple(sorted(report['source_indices'][i] for i in e))
                  for e in report['edges']}
        assert oldedges==newedges
        report['projective_parameters']=dict(L=str(L),T=list(T),s=str(s))
        write_json(out/(name+'.json'),report)
        print(name,[report[k] for k in ('V','E','F')],
              report['counts'],report['weak'],flush=True)
    print('ONE_EXACT_IMPLEMENTATION_FINISHED',flush=True)


if __name__=='__main__':
    if len(sys.argv)!=3:
        raise SystemExit('Usage: python projective_basin.py FINAL_SOURCE_DICT.json fresh-output')
    main(sys.argv[1],sys.argv[2])
```

Команда восстановления конечных экспериментов:

```text
python -S projective_basin.py FINAL_SOURCE_DICT.json first-output
```

Повтор из тех же исходных данных в первоначально отсутствующий каталог:

```text
python -S projective_basin.py FINAL_SOURCE_DICT.json second-output
cmp first-output/SAFE.json second-output/SAFE.json
```

Это команды для воспроизведения, **не сообщения об уже выполненном повторе**. Даже положительный `passes_one_implementation_110_gate` требует второго независимо реализованного полного аудитора до продвижения победителя.

Авторитетный вход — immutable `figure-0355`, SHA-256 `a861e1a5a88344a1bccc8751ff2798fdfffa647b5f53f39d27fe1b7ad36c7d42`, вместе с приложенным полным69-файловым источником. Проверяемые SHA родительского словаря и конкретной H94-таблицы встроены в программу. Компактную10-файловую журнальную капсулу нельзя выдавать за этот69-файловый архив.

## 7. Следующий содержательный шаг

У новой модели есть конечные рациональные физические параметры, связанные формулы собственной массы и точные знаковые тесты обеих сторон. Следующее исследование должно менять проективные параметры и, при необходимости, саму материальную W-область, решая уравнения фактического момента и перестраивая ациклические выходы для **всего** текущего комплекса. После любого изменения W сначала заново строится оболочка; неизменность комплекса доказана только для последующего допустимого проективного этапа.

Остаются неустановленными: собственный класс SAFE и L16 в этой передаче, их точные численные бюджеты после полного исполнения, существование strict110 в предложенном семействе, второй независимый аудит и холодная проверка нового самостоятельного пакета. Ни отсутствие прочитанного результата вычисления, ни отрицательный конечный экран, ни невозможность циклических свидетелей не являются доказательством отсутствия требуемого многогранника.
