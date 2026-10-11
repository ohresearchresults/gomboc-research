# figure-0564

Historical AI scientific report · saved 2026-09-26 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Clear Harbor 55 — статус продолжения и точное устранение дрейфа центра

## Статус результата

**Новый собственный строгий110 не получен и новый численно найденный endpoint не заявляется.** В этой попытке не удалось получить наблюдаемые содержимое и stdout от обращений к среде исполнения. Отсутствие такого вывода не доказывает, что команды не исполнялись; оно не позволяет подтвердить результат их исполнения. Поэтому здесь нет приписанных вычислению новых координат, census, рангов матриц, уменьшений P/Q или контрольных сумм.

Сохранившаяся запись предыдущей попытки содержит последовательное чтение последнего журнала вплоть до запроса окна символов[352000,368000). Подтверждение общей длины декодированного текста и достижения EOF восстановить не удалось. **Полное чтение обновления417332байта в этой попытке не подтверждено.** Сам файл и буквальный родитель не объявляются отсутствующими: это ограничение наблюдаемости чтения и исполнения, а не установленный пробел источников.

Контролирующий родитель остаётся **figure-0559**, SHA-256 `e0181e33bc72dfc97e64bd431ef4a23f627e5c083036b4ed931e2393205b22db`. Его буквальный результат и полные модули присутствуют в предыдущем ответе этого чата. Значения ниже сохраняют статус родительской проверки, а не нового независимого повторения:

| Родитель | V/E/F | Собственный(S,U,H) | Additional-weak | P-depth | Q-depth |
|---|---|---|---|---|---|
| JOINT56_F18 |75/204/131|(2,2,2)|(0,0,0)|0.09747142366897970|0.06236768950811229|
| JOINT56_L18 |75/204/131|(2,2,2)|(0,0,0)|0.10018756794854827|0.06712194454711798|
| JOINT56_F30 |67/172/107|(2,2,2)|(0,0,0)|0.15765389077162698|0.20976043811490092|
| JOINT56_L30 |67/172/107|(2,2,2)|(0,0,0)|0.16556674536333255|0.21784122208643897|

Полезное продолжение, выведенное ниже аналитически, — **конечное рациональное компенсирование изменения собственного момента двумя непересекающимися звёздами вершин**. Оно позволяет совместно двигать несколько взаимодействующих критических носителей, не подменяя собственный центр заданным и не исправляя массу весами. Приведён полный самостоятельный модуль для L18. **Модуль не был наблюдаемо исполнен или протестирован в этой попытке.** Его возможный результат не является уже найденным телом.

## Конечное физическое компенсирование момента

Перенесём исходный однородный корпус так, чтобы его собственный центр был0. Зафиксируем на время одной координатной карты настоящий комплекс граней. Большая грань может сохраняться контактным уравнением в этой карте; это не требование ко всему дальнейшему пути.

Пусть свободно изменяется группа основных вершин. Изменения внутри этой группы могут взаимодействовать: допускаются общие рёбра и треугольники. Выберем ещё две управляющие вершины u и v со следующими свойствами:

* все инцидентные им максимальные грани треугольны;
* ни одна грань управляющей вершины не содержит изменяемую основную вершину;
* u и v не принадлежат общей грани.

Таким образом, обод каждой управляющей звезды остаётся неподвижным, а вклады двух звёзд в формулы объёма и момента не пересекаются.

Для одной звезды с ориентированными треугольниками(z,b,c) положим

`a = Σ(b×c)/6`,

`B = Σ (b+c)(b×c)^T/24`,

`τ = a·z`.

Её вклады в объём и первый момент равны

`Vstar(z)=a·z`,

`Mstar(z)=(a·z)z/4+Bz`.

Следовательно, при любом **конечном**, а не только бесконечно малом перемещении d с a·d=0,

`ΔVstar=0`,

`ΔMstar=(τI/4+B)d`.

Выберем по два рациональных базисных вектора в плоскостях a_u⊥ и a_v⊥. Их четыре образа под соответствующими операторами(τI/4+B) образуют матрицу3×4. Если её ранг3, можно выбрать обратимую матрицу C из трёх столбцов. Это проверяемое точное условие, **не утверждение о уже вычисленном ранге L18**.

Теперь сначала исполним произвольное конечное основное перемещение и вычислим его полный момент M_primary по исходному ориентированному комплексу. Коэффициенты управляющих перемещений задаются точно:

`λ = -C^(-1) M_primary`.

После добавления этих трёх управляющих направлений полный момент становится тождественно нулевым. Объём может измениться: основные движения не обязаны сохранять его. Но собственный центр остаётся0, поскольку получено **M=0 при фактическом положительном V**, а не использован старый центр вместо нового.

Это утверждение действует, пока проверяемый комплекс действительно является границей выпуклого корпуса. За пределами этой области сумма по старой поверхности не должна называться массой нового hull. Модуль ниже сначала проверяет все опорные и контактные условия и затем независимо перестраивает точный hull принятого endpoint.

### Что здесь добавляется к линейной проекции момента

Если основные координаты аффинны по параметру t, то V_primary имеет степень не выше3, M_primary — не выше4. Поэтому управляющие координаты, полученные указанной формулой, являются **точными рациональными полиномами степени не выше4**. Нет накопления ошибки интегрирования, итерационного восстановления центра или невязки, которую можно спутать с физической массой.

Для одной такой карты все условия выпуклости и механики можно исследовать как полиномиальные условия одного параметра. Грубые достаточные верхние границы степеней: опорные условия —12, примитивные U-условия —8, S-условия —16, H-условия —36. Последняя оценка следует из степеней d² и t_edge не выше8, R=(p-c)d²+t_edge d не выше12, нормалей не выше8 и выражений вида |m|²(R·n)-(n·m)(R·m). Таким образом, точное разбиение параметрического отрезка по всем контактам и механическим нулям конечно. **Такое разбиение в этой попытке не построено; отсутствие слабых равновесий на интервале не заявляется.**

## Совместное направление P/Q без фиксации конечных корней

Для первой карты L18 в модуле выбраны основные материальные строки13,22,14,16,24. Первые две принадлежат критическому P-ребру и двигаются в плоскости18-угольника; три последние свободно изменяют малый устойчивый треугольный носитель. Это13 основных степеней свободы до выбора направления. Две компенсирующие звезды выбираются точным перебором, а не предполагаются по названию вершины.

На массо-замкнутой карте вычисляются точные производные двух текущих положительных глубин. Если их градиенты gP и gQ линейно независимы, система

`gP·d=-1`, `gQ·d=-1`

имеет рациональное решение. Оно строится через обратную матрицу Грама2×2. При совпадающих положительно сонаправленных градиентах также существует совместное направление уменьшения. Противоположность градиентов означает препятствие только для выбранной дифференциальной карты и её двух текущих функций; она не исключает другую пару компенсаторов, другой контактный комплекс или конечную экскурсию.

При найденном строгом совместном направлении непрерывность гарантирует достаточно малый конечный шаг с уменьшением обеих глубин и сохранением исходного строгого census. Модуль проверяет конечные рациональные шаги, а не использует эту гарантию вместо аудита. Он допускает endpoint с S≤2 и U≤2, включая121,211 или110, но принимает его только после полного собственного census и проверки всех положительных баров. **Наличие подходящего ранга и совместного направления у конкретного L18 пока не наблюдалось.**

## Самостоятельный модуль — masslift57.py

Ниже нет зависимости от непереданного локального файла. Включены буквальный L18, точный hull максимальных граней, объёмный центр, строгий и дополнительный closed-weak census, полный положительный P/Q barcode с разрезами и достигающими путями, производитель конечной массо-замкнутой карты и независимая проверка принятого endpoint.

Требуется только стандартная библиотека Python3.11 или новее. Случайность отсутствует. Основные строки фиксированы как `[13,22,14,16,24]`; остальные параметры видны в коде. Проверяются шаги2^-j, j=0,…,127. Исчерпание этого списка не является исключением карты.

```python
from fractions import Fraction as F
from itertools import combinations, groupby
from collections import deque
from functools import reduce
from math import gcd, lcm
from pathlib import Path
import argparse, hashlib, json, sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

TEXT = '''
-114525,0,2815;-114408,0,-21012;-110220,0,-38817;-102074,0,-55623;-95244,0,65065
-93745,0,-67376;-84871,0,89483;-83812,0,-77505;-76508,0,-83525;-64581,0,-90582
-61476,25894,-14839;-62395,23368,463;-56261,23741,8340;-52412,0,-95480;-51315,23453,14016
-52494,34497,-19706;-42771,21590,23057;-42863,2890,42398;-41427,18386,27657;-41360,12530,33866
-41047,44227,-22695;-39278,42001,-8155;-34778,0,-100114;-33227,5517,41437;-34030,41543,3065
-32655,47126,-31146;-27505,0,-101349;-26092,6359,40643;-29349,-3094,46727;-23601,48813,-36091
-20202,0,-101916;-22835,44187,7116;-19759,39126,14237;-15413,37019,17653;-12669,0,-101808
-11758,47157,-43142;-9937,36825,18784;-5171,0,-100970;-4354,45931,-43781;-656,39016,17643
-285,7861,35467;2454,-27623,-99473;1609,5616,35659;7524,7250,33248;9975,-29293,-97278
8760,16281,29866;12615,42039,15586;23787,44736,-31885;17334,-30836,-94391;30460,-17220,-87918
24468,-32254,-90824;38470,40587,-9618;31322,-33549,-86591;29555,47228,10455;33038,0,-80951
37731,-34969,-81714;36888,40349,12838;41804,34722,13816;43728,-36211,-76251;41605,0,-68494
44676,31334,13390;47360,27874,12796;49134,-37619,-70267;49897,24291,12029;52973,-47543,-55156
53765,-8364,-59155;55076,17110,8707;59503,9479,4527;58901,-42244,-45006;63005,1560,-490
63029,-35973,-35698;65329,-6139,-5970;66608,-13854,-12187;65610,-28928,-27007;66746,-21494,-19185
'''
PATCH = [0,1,2,3,4,5,6,7,8,9,13,22,26,30,34,37,54,59]
PRIMARY = [13,22,14,16,24]
ZERO = (F(0), F(0), F(0))

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def mul(a,s): return tuple(x*s for x in a)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2],
            a[0]*b[1]-a[1]*b[0])
def det(a,b,c): return dot(a,cross(b,c))

def parent_points():
    a=[list(map(int,r.split(','))) for r in TEXT.replace('\n',';').split(';')
       if r.strip()]
    assert len(a)==75
    p=[tuple(F(x,100000) for x in r) for r in a]
    n=(-272,-1000,-409); h=F(68526367,100000)
    for i in PATCH:
        x,_,z=p[i]
        p[i]=(x,(h-n[0]*x-n[2]*z)/n[1],z)
    return p

def polygon(ids,p,n):
    drop=max(range(3),key=lambda k:abs(n[k]))
    u,v=[k for k in range(3) if k!=drop]
    ids=sorted(ids,key=lambda i:(p[i][u],p[i][v]))
    def turn(i,j,k):
        return ((p[j][u]-p[i][u])*(p[k][v]-p[i][v])
                -(p[j][v]-p[i][v])*(p[k][u]-p[i][u]))
    def half(seq):
        out=[]
        for i in seq:
            while len(out)>1 and turn(out[-2],out[-1],i)<=0:
                out.pop()
            out.append(i)
        return out
    f=half(ids)[:-1]+half(reversed(ids))[:-1]
    assert len(f)>=3
    if dot(cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]])),n)<0:
        f.reverse()
    k=f.index(min(f))
    return f[k:]+f[:k]

def triangles(faces):
    for f in faces:
        for j in range(1,len(f)-1):
            yield (f[0],f[j],f[j+1])

def mass(p,faces,o=ZERO,positive=False):
    V=F(0); M=ZERO
    for ids in triangles(faces):
        a,b,c=[p[i] for i in ids]
        w=det(sub(a,o),sub(b,o),sub(c,o))/6
        if positive:
            assert w>0
        V+=w
        M=add(M,mul(add(add(o,a),add(b,c)),w/4))
    return V,M

def hull(points):
    p=list(dict.fromkeys(tuple(F(x) for x in q) for q in points))
    assert len(p)>=4
    D=lcm(*(x.denominator for q in p for x in q))
    z=[tuple(int(x*D) for x in q) for q in p]
    planes=set()
    for i,j,k in combinations(range(len(z)),3):
        n=cross(sub(z[j],z[i]),sub(z[k],z[i]))
        if not any(n):
            continue
        h=dot(n,z[i]); pos=neg=False
        for q in z:
            s=dot(n,q)-h
            pos=pos or s>0; neg=neg or s<0
            if pos and neg:
                break
        if pos and neg:
            continue
        if not pos and not neg:
            continue
        a=tuple(n)+(h,)
        if pos:
            a=tuple(-x for x in a)
        g=reduce(gcd,(abs(x) for x in a),0)
        planes.add(tuple(x//g for x in a))
    assert len(planes)>=4
    faces=[]
    for a in sorted(planes):
        ids=[i for i,q in enumerate(z) if dot(a[:3],q)==a[3]]
        faces.append(polygon(ids,z,a[:3]))
    keep=sorted({i for f in faces for i in f})
    remap={i:j for j,i in enumerate(keep)}
    faces=[[remap[i] for i in f] for f in faces]
    owners={}
    for fi,f in enumerate(faces):
        for i,j in zip(f,f[1:]+f[:1]):
            owners.setdefault(tuple(sorted((i,j))),[]).append(fi)
    edges=sorted(owners)
    assert all(len(owners[e])==2 for e in edges)
    assert len(keep)-len(edges)+len(faces)==2
    return dict(points=[p[i] for i in keep],material=keep,faces=faces,
                edges=edges,edge_faces=[owners[e] for e in edges])

def normals(p,faces):
    return [cross(sub(p[f[1]],p[f[0]]),sub(p[f[2]],p[f[0]])) for f in faces]

def mechanics(x,faces,edges,owners,n):
    strict=[[],[],[]]; weak=[[],[],[]]; zeros=[0,0,0]
    nb=[set() for _ in x]
    for i,j in edges:
        nb[i].add(j); nb[j].add(i)
    def record(k,label,values):
        zeros[k]+=sum(a==0 for a in values)
        if all(a>0 for a in values):
            strict[k].append(label)
        elif all(a>=0 for a in values):
            weak[k].append(label)
    for fi,f in enumerate(faces):
        values=[dot(cross(n[fi],sub(x[j],x[i])),mul(x[i],-1))
                for i,j in zip(f,f[1:]+f[:1])]
        record(0,fi,values)
    for i in range(len(x)):
        record(1,i,[-dot(x[i],sub(x[j],x[i])) for j in sorted(nb[i])])
    for (i,j),(f,g) in zip(edges,owners):
        d=sub(x[j],x[i]); dd=dot(d,d); t=-dot(x[i],d)
        R=add(mul(x[i],dd),mul(d,t))
        a,b=n[f],n[g]; aa=dot(a,a); ab=dot(a,b); bb=dot(b,b)
        assert aa*bb-ab*ab>0
        record(2,[i,j],[t,dd-t,bb*dot(R,a)-ab*dot(R,b),
                               aa*dot(R,b)-ab*dot(R,a)])
    return dict(strict=list(map(len,strict)),additional_weak=list(map(len,weak)),
                primitive_zero=zeros,S=strict[0],U=strict[1],H=strict[2],
                weak_S=weak[0],weak_U=weak[1],weak_H=weak[2])

def gate(u,v):
    A=dot(u,u); B=dot(u,v); C=dot(v,v); D=A+C-2*B
    if D==0 or B>=A:
        return A
    if B>=C:
        return C
    return (A*C-B*B)/D

def bars(x,edges):
    edges=sorted({tuple(sorted(e)) for e in edges})
    birth=[dot(p,p) for p in x]
    weight={e:gate(x[e[0]],x[e[1]]) for e in edges}
    par=list(range(len(x))); peak=par.copy()
    members=[{i} for i in par]; result=[]
    def find(i):
        while par[i]!=i:
            par[i]=par[par[i]]; i=par[i]
        return i
    def path(s,t,level):
        adj=[[] for _ in x]
        for i,j in edges:
            if weight[(i,j)]>=level:
                adj[i].append(j); adj[j].append(i)
        prev={s:None}; todo=deque([s])
        while todo and t not in prev:
            i=todo.popleft()
            for j in sorted(adj[i]):
                if j not in prev:
                    prev[j]=i; todo.append(j)
        assert t in prev
        out=[]; i=t
        while i is not None:
            out.append(i); i=prev[i]
        return out[::-1]
    ranked=sorted(edges,key=lambda e:(-weight[e],e))
    for level,ee in groupby(ranked,key=lambda e:weight[e]):
        adj={}
        for i,j in ee:
            a,b=find(i),find(j)
            if a!=b:
                adj.setdefault(a,set()).add(b)
                adj.setdefault(b,set()).add(a)
        unseen=set(adj); groups=[]
        while unseen:
            a=min(unseen); unseen.remove(a); cc={a}; todo=[a]
            while todo:
                u=todo.pop()
                for v in adj[u]:
                    if v in unseen:
                        unseen.remove(v); cc.add(v); todo.append(v)
            groups.append(sorted(cc))
        for cc in groups:
            elder=max(cc,key=lambda a:(birth[peak[a]],-peak[a]))
            for a in cc:
                if a==elder or birth[peak[a]]==level:
                    continue
                assert birth[peak[a]]>level
                comp=members[a]
                cut=[e for e in edges if (e[0] in comp)!=(e[1] in comp)]
                assert cut and max(weight[e] for e in cut)==level
                pp=path(peak[a],peak[elder],level)
                assert min(weight[tuple(sorted(e))] for e in zip(pp,pp[1:]))==level
                result.append(dict(peak=peak[a],elder=peak[elder],
                    birth=birth[peak[a]],death=level,
                    depth=(birth[peak[a]]-level)/birth[peak[a]],
                    component=sorted(comp),cut=cut,
                    attaining_edge=next(e for e in cut if weight[e]==level),
                    attaining_path=pp))
            merged=set().union(*(members[a] for a in cc))
            for a in cc:
                par[a]=elder
            members[elder]=merged
    assert len({find(i) for i in range(len(x))})==1
    return sorted(result,key=lambda b:(-b['depth'],b['peak'],b['elder']))

def report(K):
    p=K['points']; faces=K['faces']; V,M=mass(p,faces)
    assert V>0
    o=tuple(sum(q[k] for q in p)/len(p) for k in range(3))
    VV,MM=mass(p,faces,o,positive=True)
    assert (V,M)==(VV,MM)
    c=mul(M,1/V); x=[sub(q,c) for q in p]; n=normals(x,faces)
    h=[dot(a,x[f[0]]) for a,f in zip(n,faces)]
    assert all(s>0 for s in h)
    q=[mul(a,1/s) for a,s in zip(n,h)]
    R=dict(K,volume=V,moment=M,centroid=c,density=1,
           V=len(p),E=len(K['edges']),F=len(faces),C=2*len(K['edges']))
    R.update(mechanics(x,faces,K['edges'],K['edge_faces'],n))
    R['P_vectors']=x; R['Q_vectors']=q
    R['P_bars']=bars(x,K['edges'])
    R['Q_bars']=bars(q,K['edge_faces'])
    if not any(R['additional_weak']):
        s,u,hh=R['strict']
        assert s+u-hh==2
        assert len(R['P_bars'])==u-1
        assert len(R['Q_bars'])==s-1
    return R

def audit(p):
    return report(hull(p))

def null_plane(a):
    k=next(i for i in range(3) if a[i]!=0)
    out=[]
    for j in range(3):
        if j==k:
            continue
        v=[F(0)]*3; v[j]=F(1); v[k]=-F(a[j],a[k])
        out.append(tuple(v))
    return out

def solve_columns(C,b):
    D=det(*C)
    assert D!=0
    return [det(*(b if j==k else C[j] for j in range(3)))/D
            for k in range(3)]

def star(x,faces,i):
    a=ZERO; B=[[F(0) for _ in range(3)] for _ in range(3)]
    for f in faces:
        if i not in f:
            continue
        assert len(f)==3
        k=f.index(i); b=x[f[(k+1)%3]]; c=x[f[(k+2)%3]]
        w=cross(b,c); a=add(a,mul(w,F(1,6)))
        for r in range(3):
            for s in range(3):
                B[r][s]+=(b[r]+c[r])*w[s]/24
    tau=dot(a,x[i]); assert tau>0
    D=[[B[r][s]+(tau/4 if r==s else 0) for s in range(3)]
       for r in range(3)]
    basis=null_plane(a)
    images=[tuple(dot(row,v) for row in D) for v in basis]
    return basis,images

def moment_derivative(x,d,faces):
    out=ZERO
    for ids in triangles(faces):
        a,b,c=[x[i] for i in ids]; da,db,dc=[d[i] for i in ids]
        w=det(a,b,c)
        dw=det(da,b,c)+det(a,db,c)+det(a,b,dc)
        out=add(out,mul(add(mul(add(add(a,b),c),dw),
                            mul(add(add(da,db),dc),w)),F(1,24)))
    return out

def polar_velocity(x,d,faces):
    q=[]; dq=[]
    for f in faces:
        a,b,c=[x[i] for i in f[:3]]
        da,db,dc=[d[i] for i in f[:3]]
        n=cross(sub(b,a),sub(c,a))
        dn=add(cross(sub(db,da),sub(c,a)),cross(sub(b,a),sub(dc,da)))
        h=dot(n,a); dh=dot(dn,a)+dot(n,da)
        q.append(mul(n,1/h))
        dq.append(mul(sub(mul(dn,h),mul(n,dh)),1/(h*h)))
    return q,dq

def gate_derivative(u,v,du,dv):
    A=dot(u,u); B=dot(u,v); C=dot(v,v)
    dA=2*dot(u,du); dB=dot(du,v)+dot(u,dv); dC=2*dot(v,dv)
    D=A+C-2*B
    if D==0 or B>=A:
        return A,dA
    if B>=C:
        return C,dC
    N=A*C-B*B; dN=dA*C+A*dC-2*B*dB; dD=dA+dC-2*dB
    return N/D,(dN*D-N*dD)/(D*D)

def depth_derivative(x,d,b):
    i,j=b['attaining_edge']; k=b['peak']
    g,dg=gate_derivative(x[i],x[j],d[i],d[j])
    r=dot(x[k],x[k]); dr=2*dot(x[k],d[k])
    return -dg/r+g*dr/(r*r)

def chart(R):
    x=R['P_vectors']; faces=R['faces']
    material_to_vertex={v:i for i,v in enumerate(R['material'])}
    primary=[material_to_vertex[v] for v in PRIMARY]
    big=max(faces,key=len)
    assert len(big)==18 and all(material_to_vertex[v] in big for v in [13,22])
    n=cross(sub(x[big[1]],x[big[0]]),sub(x[big[2]],x[big[0]]))
    axes=[tuple(F(i==j) for i in range(3)) for j in range(3)]
    modes=[]
    for material,i in zip(PRIMARY,primary):
        choices=null_plane(n) if material in [13,22] else axes
        if material not in [13,22]:
            assert all(len(f)==3 for f in faces if i in f)
        for v in choices:
            d=[ZERO for _ in x]; d[i]=v; modes.append(d)
    forbidden=set(primary)
    for f in faces:
        if set(f).intersection(primary):
            forbidden.update(f)
    eligible=[i for i in range(len(x)) if i not in forbidden
              and all(len(f)==3 for f in faces if i in f)]
    for u,v in combinations(eligible,2):
        if any(u in f and v in f for f in faces):
            continue
        controls=[]; images=[]
        for i in [u,v]:
            basis,im=star(x,faces,i)
            controls.extend((i,b) for b in basis); images.extend(im)
        for selected in combinations(range(4),3):
            C=[images[j] for j in selected]
            if det(*C)==0:
                continue
            selected_controls=[controls[j] for j in selected]
            gp=[]; gq=[]; full_modes=[]
            for d0 in modes:
                d=list(d0)
                coeff=solve_columns(C,mul(moment_derivative(x,d0,faces),-1))
                for a,(i,b) in zip(coeff,selected_controls):
                    d[i]=add(d[i],mul(b,a))
                assert moment_derivative(x,d,faces)==ZERO
                q,dq=polar_velocity(x,d,faces)
                gp.append(depth_derivative(x,d,R['P_bars'][0]))
                gq.append(depth_derivative(q,dq,R['Q_bars'][0]))
                full_modes.append(d)
            aa=dot(gp,gp); ab=dot(gp,gq); bb=dot(gq,gq)
            G=aa*bb-ab*ab
            if G>0:
                a=(ab-bb)/G; b=(ab-aa)/G
                weights=[a*p+b*q for p,q in zip(gp,gq)]
            elif aa>0 and ab>0:
                weights=[-p for p in gp]
            else:
                continue
            assert dot(gp,weights)<0 and dot(gq,weights)<0
            primary_direction=[ZERO for _ in x]
            full_direction=[ZERO for _ in x]
            for w,d0,df in zip(weights,modes,full_modes):
                for i in range(len(x)):
                    primary_direction[i]=add(primary_direction[i],mul(d0[i],w))
                    full_direction[i]=add(full_direction[i],mul(df[i],w))
            scale=max([F(1)]+[abs(a) for p in full_direction for a in p])
            primary_direction=[mul(p,1/scale) for p in primary_direction]
            return dict(primary_material=PRIMARY,controls=selected_controls,
                        control_material=[R['material'][i] for i,_ in selected_controls],
                        C=C,determinant=det(*C),direction=primary_direction,
                        derivative_P=dot(gp,weights)/scale,
                        derivative_Q=dot(gq,weights)/scale)
    return None

def construct(x,faces,ch,t):
    y=[add(p,mul(d,t)) for p,d in zip(x,ch['direction'])]
    V0,M0=mass(y,faces)
    coeff=solve_columns(ch['C'],mul(M0,-1))
    for a,(i,b) in zip(coeff,ch['controls']):
        y[i]=add(y[i],mul(b,a))
    V,M=mass(y,faces)
    assert V==V0 and M==ZERO
    return y

def valid_complex(x,faces):
    for f in faces:
        n=cross(sub(x[f[1]],x[f[0]]),sub(x[f[2]],x[f[0]]))
        h=dot(n,x[f[0]])
        if h<=0:
            return False
        sf=set(f)
        for j,p in enumerate(x):
            gap=h-dot(n,p)
            if (j in sf and gap!=0) or (j not in sf and gap<=0):
                return False
        for i,j in zip(f,f[1:]+f[:1]):
            normal_in_face=cross(n,sub(x[j],x[i]))
            for k in f:
                if k not in (i,j) and dot(normal_in_face,sub(x[k],x[i]))<=0:
                    return False
    return mass(x,faces)[0]>0

def dump(path,value):
    raw=(json.dumps(value,sort_keys=True,separators=(',',':'),default=str)+'\n').encode()
    Path(path).write_bytes(raw)
    print('FILE',str(path),len(raw),hashlib.sha256(raw).hexdigest(),flush=True)

def main(out,halvings):
    out=Path(out); out.mkdir(parents=True,exist_ok=True)
    R=audit(parent_points())
    assert [R[k] for k in ['V','E','F']]==[75,204,131]
    assert R['strict']==[2,2,2]
    assert R['additional_weak']==R['primitive_zero']==[0,0,0]
    assert len(R['P_bars'])==len(R['Q_bars'])==1
    dump(out/'parent_audit.json',R)
    print('L18_PARENT_EXACT_PASS',flush=True)
    ch=chart(R)
    if ch is None:
        print('NO_FULL_RANK_JOINT_DIRECTION_IN_SELECTED_CHARTS',flush=True)
        return
    dump(out/'chart.json',ch)
    x=R['P_vectors']; c=R['centroid']; faces=R['faces']
    oldp=R['P_bars'][0]['depth']; oldq=R['Q_bars'][0]['depth']
    for j in range(halvings):
        t=F(1,2**j); y=construct(x,faces,ch,t)
        if not valid_complex(y,faces):
            continue
        trial=dict(points=y,material=R['material'],faces=faces,
                   edges=R['edges'],edge_faces=R['edge_faces'])
        T=report(trial)
        if T['additional_weak']!=[0,0,0] or T['primitive_zero']!=[0,0,0]:
            continue
        if T['strict'][0]>2 or T['strict'][1]>2:
            continue
        dp=max((b['depth'] for b in T['P_bars']),default=F(0))
        dq=max((b['depth'] for b in T['Q_bars']),default=F(0))
        if not (dp<oldp and dq<oldq):
            continue
        points=[add(p,c) for p in y]
        A=audit(points)
        assert A['centroid']==c
        assert A['E']<=249
        assert A['strict']==T['strict']
        assert A['additional_weak']==A['primitive_zero']==[0,0,0]
        assert max((b['depth'] for b in A['P_bars']),default=F(0))==dp
        assert max((b['depth'] for b in A['Q_bars']),default=F(0))==dq
        A['parameter']=t
        dump(out/'body.json',dict(points=points,density=1))
        dump(out/'audit.json',A)
        print('EXACT_FINITE_MASSLIFT_PASS',A['strict'],A['E'],str(t),
              'P',str(dp),'Q',str(dq),flush=True)
        if A['strict']==[1,1,0]:
            print('OWN110_WEAK000_E249_CERTIFIED',flush=True)
        return
    print('NO_CERTIFIED_STEP_IN_THIS_FINITE_RUN',flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',default='masslift57_output')
    ap.add_argument('--halvings',type=int,default=128)
    args=ap.parse_args()
    if args.halvings<1:
        ap.error('--halvings must be positive')
    main(args.out,args.halvings)
```

## Проверка и границы продолжения

Команда восстановления и проверки:

```sh
python -B -S masslift57.py --out masslift57_output --halvings 128
```

**Ни один из следующих маркеров не наблюдался в этой попытке.** Они описывают ветви исполнения переданного модуля:

`L18_PARENT_EXACT_PASS` означает новое полное воспроизведение родительского census. `EXACT_FINITE_MASSLIFT_PASS` означает конечный физический endpoint с точным собственным центром, E≤249, полным weak000 и строгим уменьшением обеих максимальных положительных глубин. Сам по себе этот маркер не означает110. Только отдельный `OWN110_WEAK000_E249_CERTIFIED` связан в коде с exact(S,U,H)=(1,1,0).

`NO_FULL_RANK_JOINT_DIRECTION_IN_SELECTED_CHARTS` и `NO_CERTIFIED_STEP_IN_THIS_FINITE_RUN` обозначают ограниченные неудачи данного перебора. Они не исключают собственный110, полный класс массо-компенсированных движений или даже все карты на том же L18.

Контрольные суммы новых файлов будут вычисляться модулем из фактически записанных байтов. Они здесь не приведены, поскольку новые файлы и их содержимое не были наблюдаемо получены. Никакой непроверенный координатный объект не передаётся как преемник F18/L18.

Наиболее полезное продолжение — исполнить эту конечную массо-замкнутую карту и получить точный ранг, совместное направление и полный endpoint-аудит; затем использовать фактические новые носители для следующей карты, включая освобождение большой грани, когда её сохранение перестанет помогать. Аналитическое устранение дрейфа центра не устраняет оставшиеся положительные P/Q-бары само по себе.
