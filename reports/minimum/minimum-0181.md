# minimum-0181

Historical AI scientific report · saved 2026-09-22 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# PROPER33_NEGATIVE_Z_A_HINGE_EXCLUSION_V1

## 1. Основной результат

**Оставшийся strongly mixed U_D полностью исключён при T>=51/25.** Более сильный вывод: при принятом условии общих моментов J этот граф не может быть полным стационарным максимумом уже при T>=2. Ограничение снизу на G(D)/r из родителя больше не оставляет открытого подслучая в целевом диапазоне.

Новая теорема не ограничивается восьмивершинным графом. Пусть P — настоящее равномерно заполненное proper33-тело с a>b>0, c,d>0, положительной площадью корня и

    gx,gy>=1/4,  4(gx+gy)<=t+1,  t=6V.               (J)

Если P содержит точку с z<0, то полный локальный максимум по телу/корню/отмеченному реперу удовлетворяет

    T < Theta(a,b),
    Theta(a,b)=(-b+sqrt(b^2+12a(a+b)))/(2a),
    sqrt(3)<Theta(a,b)<2.                            (THEOREM)

Точнее, при T>=Theta(a,b) имеется строго улучшающее малое **внутреннее вращение целой настоящей грани через AC** после перестановки C,D, обеспечивающей c>=d. Корневая плоскость, все четыре отмеченные точки и обе защищённые треугольные грани сохраняются. Это действительная вариация одного тела, а не движение интеграционных треугольников по отдельности.

В доказательстве не нужны знаки G(C),G(D), число дополнительных вершин, отсутствие обычной грани B или какой-либо иной special-B граф. Поэтому оно, в частности, закрывает весь заданный strongly mixed U_D, включая его некомпактные геометрические концы. Отрицательные z в **произвольном нестационарном** теле не исключены.

В сочетании с принятыми теоремами «proper33 + отрицательный якорь + положительный октант => root-only» и об оценке всего положительно-октантного root-only класса получается:

> При прежних положительных endpoint-предпосылках и J полный proper33 отрицательно-якорный максимум имеет T<51/25.

Здесь положительно-октантная часть — принятое основание, а не новый пересчёт её сертификата. Произвольный low-endpoint negative-z root-only VALUE, увеличенные защищённые грани, нулевые endpoints и мост к механическому E17 не объявляются закрытыми. :contentReference[oaicite:0]{index=0}

## 2. Прочитанные входы и уровень доказательства

Новый журнал прочитан последовательно до EOF, включая общий notebook, обновление ветви, буквальный родитель и его полный исходник: 1704 строки, 283972 байта, SHA-256

    9954e9154f255dd163da13f019039c1aba013e01b7bfd65d5ad56dc3374ea9ab.

Дополнительный полный материал [internal-source-reference] — 24804 байта, SHA-256

    44a7131baef2f1c769ca096116c1ef1fd646349a148785410b0b6da9fd7605d6.

Он содержит как коконвексный контекст, так и положительные корневые реакции; обе части и вложенный исходник прочитаны. Неизменённые предыдущие материалы остаются доступны в этом чате. Приложенные source/JSON/stdout предыдущего результата также прочитаны полностью. Пропущенных точных зависимостей для нового вычисления нет.

Буквальная родительская власть:

    minimum-0178
    SHA256 0b682f869b95faf978639f9d90de9eb3f3849cfd64cdda13a5cfca250767aa8f.

Его исключение L_D и малых G(D)/r принято без повторного пересчёта старого доказательства. Настоящая структура U_D унаследована от minimum-0176, SHA256 9b2d327e6f4fbd2bfdf827e072ff769efde7981b0257bb418cc5e5f4df5aabe2. Коррекция старого B-B значения ell(vertex7)=61/2040 уже внесена во вход; нового конфликта с буквальными родителями не обнаружено. :contentReference[oaicite:1]{index=1}

Основная новая часть — аналитическое доказательство из J и полного конусного бюджета. Новый код проверяет точные тождества, настоящие контрольные тела и весь непрерывный путь; это не формализация доказательства в proof assistant. Нормальный запуск и независимое восстановление из одного исходника в пустом каталоге фактически выполнены с побайтовым совпадением результатов.

## 3. Общие моменты одного тела

Обозначения неизменны:

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    alpha=a-b, s=a+b, hc=s+c, hd=s+d,
    ell=a+(d-a)x+(c-a)y-alpha*z,
    n=hc*x+hd*y,
    V=int_P 1, J=(X,Y,Z)=int_P(x,y,z),
    E=int_P ell, N=int_P n,
    g=J/V, mu=E/V, r=N/V, q=N/E,
    t=6V, T=N/(6VE), r=Tt*mu, q=Tt,
    G=n-r-q*ell.

E — интеграл ell, не число рёбер. Proper33 означает, что ABC и ABD сами являются настоящими максимальными треугольными гранями. Все приведённые объёмные и поверхностные интегралы относятся к одному P с его исходной равномерной плотностью.

Используется принятый родительский полный бюджет

    24E >= n(p)+t*ell(p)  для каждого p в P.           (CONE)

Он получается веером **всей** настоящей границы из p. Пирамиды над ABC и ABD имеют объёмы x(p)/6 и y(p)/6; вклад ell(p) использует полный V. Поэтому t здесь не заменяется объёмом локальной шапки. Условие J также сохраняется в точной принятой формулировке, а не подменяется независимыми координатными массами. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}

После отражения c>=d. Из J следует

    4r=4hc(gx+gy)-4(c-d)gy <= hc*t+hd.               (M)

Из CONE в C, учитывая 24E=4t*mu,

    hd+c*t <= 4t*mu.                                 (CC)

Складывая неотрицательные дефициты (M) и (CC), получаем новое решающее совместное ограничение

    4(T-1)*mu <= a+b.                                (MEAN)

Именно эта связь полного объёма, собственного центра и endpoint-значений не использовалась в прежнем однотреугольном исключении U_D. Она не содержит геометрических параметров u,v,kappa,lambda.

## 4. Поточечный барьер ниже уровня A-шарнира

Положим

    L_A=-G(A)/3=t*T*(mu+a)/3,
    D_mu=a+b-4(T-1)*mu>=0,
    Psi(T)=a*T^2+b*T-3(a+b).

Из CONE в произвольной точке следует

    G(p) <= t[(4-T)*mu-(T+1)*ell(p)].                 (POINT)

Точное тождество:

    3(T-1)[L_A-t(4-T)*mu]
      =t[Psi(T)+(3-T)*D_mu].                         (ID)

В рассматриваемом диапазоне T>=Theta>1 коэффициент 3-T положителен. Действительно, CONE в A даёт 4mu>=a; вместе с MEAN это даёт T<=2+b/a<3. Положительный корень Psi равен Theta(a,b). Кроме того,

    Psi(sqrt(3))=b(sqrt(3)-3)<0,
    Psi(2)=a-b>0,

так что sqrt(3)<Theta<2. При T>=Theta тождество ID доказывает

    G(p) <= L_A-t(T+1)*ell(p) <= L_A.                (BARRIER)

В частности, поскольку c>0,

    G(C) <= L_A-t(T+1)c < L_A.                       (C-STRICT)

При T>=2 имеется равномерно строгий вариант. Используя

    Psi(T)-(a-b)(T-1)=(T-2)[a(T+1)+2b]>=0,

получаем для **всех точек того же тела**

    G(p) <= L_A-t(a-b)/3-t(T+1)*ell(p).              (BARRIER2)

Ни один G на корне или на дополнительных вершинах здесь не назначен независимо. Неравенство построено из собственного r=N/V и q=N/E.

## 5. Почему целый A-многоугольник даёт противоречие

### 5.1. Правильная настоящая грань

При наличии z<0 плоскость ACD, то есть z=0, не является опорной: B имеет z=1. Настоящее ребро AC уже принадлежит защищённому треугольнику ABC. Его вторая максимальная грань F_AC поэтому свободна и содержит **ровно два** канонических знака A,C. Она не может быть корнем, поскольку a,c>0, не может содержать B, поскольку это снова плоскость ABC, и не может содержать D.

Её внутреннюю опору можно записать

    f_AC=z+u*x>=0, u>0.

Положительность коэффициента z следует из строго внутреннего положения B относительно этой второй плоскости. Удержание D даёт u>=0; случай u=0 означал бы запрещённую опору z>=0. Пересечение F_AC с x=0 есть ровно AC. Поэтому все остальные вершины F_AC имеют x>0.

В буквальном U_D эта грань — именно **четырёхугольник A,C,P,Q**, а не AD-пятиугольник и не BDU-треугольник. Его настоящие рёбра AC,CP,PQ,QA входят в родительскую решётку. :contentReference[oaicite:4]{index=4}

### 5.2. Интегрирование многоугольника, а не независимые движения его частей

Разобьём весь выпуклый F_AC веером из A только для интегрирования. Для одного его треугольника A,V,W и H=x, H(A)=0, имеем

    int_AVW G*H/k
      =Area_AVW/k/12 * {
          H(V)[G(A)+2G(V)+G(W)]
         +H(W)[G(A)+G(V)+2G(W)] },                   (TRI)

где k=|grad f_AC|. Из G(A)=-3L_A и BARRIER оба коэффициента неположительны. Треугольник, прилегающий к настоящему ребру AC, имеет вид A,C,P, x(P)>0. В нём C-STRICT делает коэффициент при H(P) строго отрицательным. Следовательно,

    I_AC:=int_F_AC G*x/k <0.                         (WORK)

Это противоречит **одному** необходимому уравнению целого шарнира I_AC=0. Не предполагалась отдельная стационарность APQ или ACP.

Для буквального U_D при T>=2 сохраняется количественный сертификат:

    I_AC <= -t(a-b)/4 * int_F_AC x/k
             -t(T+1)c*x(P)^2/24 <0.                 (QWORK)

Действительно, BARRIER2 даёт в каждом коэффициенте TRI как минимум -t(a-b), а дополнительный вклад c берётся только из интеграционного ACP. В данной нормировке dS/k=dxdy, Area_xy(ACP)=x(P)/2 и int_ACP x/k=x(P)^2/6. Все параметры реальной грани могут быть сколь угодно малы или велики; знаки сертификата не зависят от компактной сетки по ним.

### 5.3. Действительный рост исходного T при фиксированном корне

Заменим только целую опору на

    f_AC-delta*x=z+(u-delta)x>=0, delta>0 малое.

Все остальные опоры, включая ell>=0, фиксированы. Точки A,B,C,D и оба защищённых треугольника остаются. Площадь корня остаётся положительной при достаточно малом delta. Для буквального U_D точки P,Q скользят по той же корневой плоскости, а U,R не двигаются.

Настоящие первые вариации:

    V'=-int_F_AC x/k,
    J'=-int_F_AC (x,y,z)*x/k,
    E'=-int_F_AC ell*x/k,
    N'=-int_F_AC n*x/k,
    T'=-I_AC/(6VE)>0.                               (ASCENT)

Собственный центр не фиксируется искусственно: он меняется как J/V. При T>=2 из QWORK дополнительно следует

    T' >= [(a-b)+(T+1)c]*x(P)^2/(24E)>0.

Поэтому одновременная стационарность четырёх настоящих шарниров и трёх независимых реакций корня невозможна. Для противоречия достаточно уже одного обязательного шарнира; корневая реакция не может устранить рост при разрешённом движении с фиксированной корневой плоскостью. Это закрытие необходимой подсистемы полной задачи, а не объявление решения свободной моментной релаксации настоящим телом.

## 6. Реакции корня: сохранённая дополнительная связь

Из приложенного материала сохраняются, с p=gx+gy и k0=|grad ell|,

    I0=int_root G/k0=V(q-3p),
    Ix=V(q*gx-gy), Iy=V(q*gy-gx), Iz=V(q*gz-p),
    I2=int_root G^2/k0=V[3rp-hc*gy-hd*gx].

Положительность G на корне и отрицательность всех его z в U_D дают q>3p и q*gz<p. Эти условия не переинтерпретируются как независимый выбор поверхностных моментов. :contentReference[oaicite:5]{index=5}

Есть небольшое самостоятельное усиление приведённого там Cauchy-ограничения. Пусть M=max(a,b,c,d). Настоящая пирамида от соответствующей канонической вершины к корню имеет объём M*Area(root)/(3k0), строго меньший V: другая истинная каноническая вершина вне корня не может лежать в этой пирамиде, иначе она не была бы крайней точкой P. Следовательно Area(root)/k0<3V/M. На положительно-площадном корне G=n-r непостоянна, поскольку grad n не параллелен grad ell при a>b. Поэтому

    (q-3p)^2 < (3/M)[3rp-hc*gy-hd*gx].                (ROOT-STRICT)

Это заменяет коэффициент 3/b на более сильный 3/M и делает неравенство строгим. Основное исключение из разделов 3–5 не зависит от ROOT-STRICT. На контрольных телах ниже проверены исходные настоящие поверхностные интегралы и строгий Cauchy, но **не подставлены ложные стационарные правые части**: их корневые остатки ненулевые.

## 7. Настоящий непрерывный strongly mixed контроль

Чтобы сохранить геометрический смысл отрицательного целого AC-шарнира, построен и точно проверен путь одного настоящего четырёхугольного support-motion, не удаления U. Он начинается в неизменённом родительском U_mixed и меняет только u:

    (a,b,c,d)=(1,1/2,7/10,1/20),
    v=2, kappa=1/50, lambda=101/49,
    u=1-theta/2, 0<=theta<=1.

Все восемь вершин восстанавливаются без внешнего файла:

    A=(0,0,0), B=(0,0,1), C=(0,1,0), D=(1,0,0),
    U=(101/98,1/100,-1/50),
    P(u)=(175/(164-50u), (250u-15)/(2(164-50u)), -175u/(164-50u)),
    Q(u)=(20/(19-7u), 10u/(19-7u), -20u/(19-7u)),
    R=(25/22,5/44,-5/22).

Полные максимальные грани в порядке Fx,Fy,AC,AD,BC,BD,root:

    (012),(013),(0256),(03476),(12574),(134),(567).

Полные истинные рёбра:

    (01),(02),(03),(06),(12),(13),(14),
    (25),(34),(47),(56),(57),(67).

Внутренние опоры:

    x,y,1-19x/20-3y/10-z/2,z+u*x,z+2y,
    1-z-y-49x/50,1-z-x+52y/49 >=0.

Весь закрытый интервал имеет эту настоящую решётку 8/13/7, положительный корень, отрицательные z всех четырёх дополнительных вершин, положительные собственные G на них и G(C)<0<G(D). Исходный T строго возрастает на всём пути. На **всём подынтервале 2/5<=theta<=1** дополнительно

    G(D)/r>581537111/3371659200.

Таким образом, это действительно непрерывный strongly mixed U_D-контроль. Он не является контрпримером теореме: всюду T<2, и AC-шарнир имеет ненулевую отрицательную работу.

Четыре точных контрольных положения u=1,9/10,4/5,1/2 имеют соответственно

    T=5374273708344352525/3838421850974805261,
      3147271609330452659300/2212222038658103635267,
      6385366243338046165075/4417637259822776781208,
      1976251858817961923100/1301913993047207150389.

Это приблизительно 1.40012586344, 1.42267437641, 1.44542565806, 1.51795884319. Их собственные евклидовы strict(S,U,H) равны 345,345,334,648; все четыре weak000, все 208 примитивов истинных рёбер ненулевые. Механическая неизменность на всём пути не утверждается: промежуточные слабые стены не перечислялись.

Для конечного нового strongly mixed тела u=1/2 исходные моменты равны

    V=199381613/696765300,
    J=(121374910115699/1078848629520200,
       89724755514601/1100865948490000,
       300702785530151/13210391381880000),
    E=6529759557353/45521999600000,
    N=403316705881216719/1078848629520200000,
    G(D)/r=4615811333234691295345709416579/
           7900683344604011324563508954421.

Последнее отношение приблизительно 0.584229380157. Все V,J,E,N остальных положений и рациональные функции этих моментов на целом пути воспроизводятся полным кодом ниже. Независимые положительные веера из A и B совпадают. Каждый контрольный собственный центр и полярные примитивы пересчитаны; плотность не переносится из начального тела.

Полезная отрицательная граница: хотя **весь корень конечного тела лежит ниже z=0**, его собственный объёмный центр имеет

    gz=300702785530151/3780195629834800>0.

Следовательно, геометрия отрицательного корня сама по себе не позволяет требовать gz<=0. Более слабая реакционная связь q*gz<p в приложенном материале не заменяется таким ложным утверждением.

## 8. Что было отвергнуто при проверке пути

Первоначальная проверка требовала, чтобы каждая независимая тройка семи опорных плоскостей сохраняла ненулевой определитель. Это избыточно: при theta=1/25, то есть u=49/50, тройка Fy/AC/BC имеет rank2, а расширенная система rank3. Это **несовместная неинцидентная тройка**, а не событие настоящей решётки.

Окончательная проверка использует все строгие off-facet-slacks, действительную выпуклость каждого целого facet-cycle и закрытую двустороннюю инцидентность всех 13 рёбер. Семь полученных настоящих граней замкнуты по соседству; связность двойственного графа выпуклой оболочки доказывает полноту списка. Положительная нормальная зависимость исключает лучи рецессии. Таким образом, ложный тест общего положения не превращён в исключение физического пути.

Численный просмотр определителей не проводился. Сначала рассматривались предложенные положительные реакции корня; решающей оказалась более сильная поточечная оценка, получаемая из полного конусного бюджета и J. Глобальная монотонность удаления отрицательной части или полного удаления U не доказана и не использована.

## 9. Полная recovery capsule

Выполненные версии и команды:

    CPython 3.13.5; SymPy 1.14.0;
    assertions enabled; no RNG; no external input; no parent import.

    python ud_abarrier_v1.py > ud_abarrier_v1.out
    sha256sum ud_abarrier_v1.py ud_abarrier_v1.json ud_abarrier_v1.out

Точные байты:

    ud_abarrier_v1.py: 15216 bytes
    SHA256 b384d4e24dfb87ec93f82ba99201d4b09f9cba425e18f69c6e537a83fe8a44eb
    ud_abarrier_v1.json: 74438 bytes
    SHA256 2bb386cd015c2f6ea7576f02fed34a49924e4e5de6b582d35a390a7562a325e8
    ud_abarrier_v1.out: 750 bytes
    SHA256 708f376e8b42a037d2b0bf8c9cc44ce65a578307fd3ee6dc3470a0ea99fd22a8

Весь замкнутый параметрический интервал проверен 113 рациональными строгими guards и 465 положительными коэффициентами Бернштейна. Среди них 50 guards настоящих многоугольных facet-cycles. Это полное одномерное покрытие, а не проверка только четырёх рациональных точек. Алгебраическая универсальная теорема отделена от этой проверки конкретного пути.

Полный ожидаемый stdout:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]

    u=9/10 T=3147271609330452659300/2212222038658103635267 SUH=(3, 4, 5)
    u=4/5 T=6385366243338046165075/4417637259822776781208 SUH=(3, 3, 4)
    u=1/2 T=1976251858817961923100/1301913993047207150389 SUH=(6, 4, 8)
    positive_rational_guards=113
    positive_Bernstein_coefficients=465
    strict_facet_cycle_guards=50
    report_bytes=74438
    report_sha256=2bb386cd015c2f6ea7576f02fed34a49924e4e5de6b582d35a390a7562a325e8
    PROPER33_NEGATIVE_Z_A_HINGE_EXCLUSION_V1_RECOVERY_PASS

Исходник отдельно перенесён в пустой каталог; повторное выполнение дало побайтово тот же report и stdout. Удобные копии: [исходник](sandbox:/mnt/data/ud_abarrier_v1.py), [полный отчёт](sandbox:/mnt/data/ud_abarrier_v1.json), [stdout](sandbox:/mnt/data/ud_abarrier_v1.out). Ни один новый объект не требует этих ссылок: полный исходник включён далее.

```python
#!/usr/bin/env python3
"""PROPER33_NEGATIVE_Z_A_HINGE_EXCLUSION_V1.
CPython 3.13.5; SymPy 1.14.0; assertions enabled; no RNG/external data.
Parent: minimum-0178,
0b682f869b95faf978639f9d90de9eb3f3849cfd64cdda13a5cfca250767aa8f.
Input U_mixed is the parent's unchanged rational body. The three other
controls and the entire inward AC QUADRILATERAL arc are new. All are
nonstationary, T<2, not 110. The universal theorem is analytic.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import hashlib
import json
import sympy as S

EP=tuple(map(F,('1','1/2','7/10','1/20')))
FACES=((0,1,2),(0,1,3),(0,2,5,6),(0,3,4,7,6),(1,2,5,7,4),(1,3,4),(5,6,7))
EDGES=((0,1),(0,2),(0,3),(0,6),(1,2),(1,3),(1,4),(2,5),(3,4),(4,7),(5,6),(5,7),(6,7))
PARAMS=tuple(map(F,('1','9/10','4/5','1/2')))


def dot(x,y):return sum(a*b for a,b in zip(x,y))
def sub(x,y):return tuple(a-b for a,b in zip(x,y))
def cross(x,y):return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def det(x,y,z):return dot(x,cross(y,z))
def solve(rows,rhs):
    den=det(*rows)
    if den==0:return None
    co=(cross(rows[1],rows[2]),cross(rows[2],rows[0]),cross(rows[0],rows[1]))
    return tuple(sum(rhs[i]*co[i][j] for i in range(3))/den for j in range(3))
def points(u):
    return ((0,0,0),(0,0,1),(0,1,0),(1,0,0),
            (F(101,98),F(1,100),-F(1,50)),
            (175/(164-50*u),(250*u-15)/(2*(164-50*u)),-175*u/(164-50*u)),
            (20/(19-7*u),10*u/(19-7*u),-20*u/(19-7*u)),
            (F(25,22),F(5,44),-F(5,22)))
def planes(u):
    # Outward inequalities n.X<=h; f=h-n.X is the inward slack.
    return (((-1,0,0),0),((0,-1,0),0),((-u,0,-1),0),((0,-2,-1),0),
            ((F(49,50),1,1),1),((1,-F(52,49),1),1),((F(19,20),F(3,10),F(1,2)),1))
def ell(p):return 1-F(19,20)*p[0]-F(3,10)*p[1]-F(1,2)*p[2]
def nn(p):return F(11,5)*p[0]+F(31,20)*p[1]
def en(v,j):return v-F(19,20)*j[0]-F(3,10)*j[1]-F(1,2)*j[2],F(11,5)*j[0]+F(31,20)*j[1]
def facet_product(pts,face,ff,hh):
    ans=0
    for j in range(1,len(face)-1):
        ids=(face[0],face[j],face[j+1]);p,q,r=(pts[i] for i in ids)
        area=abs((q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0]))/2
        f=[ff[i] for i in ids];h=[hh[i] for i in ids]
        ans+=area*(sum(f)*sum(h)+sum(x*y for x,y in zip(f,h)))/12
    return ans

def fan(pts,hs,apex):
    out=[]
    for k,face in enumerate(FACES):
        if apex in face:continue
        v=F(0);j=[F(0)]*3;o=pts[apex]
        for a in range(1,len(face)-1):
            pp=(pts[face[0]],pts[face[a]],pts[face[a+1]])
            w=abs(det(*(sub(p,o) for p in pp)))/6
            assert w>0
            v+=w
            for h in range(3):j[h]+=w*(o[h]+sum(p[h] for p in pp))/4
        e,n=en(v,j);out.append(dict(facet=k,V=v,J=j,E=e,N=n))
    return out

def total(pieces):
    return (sum(z['V'] for z in pieces),tuple(sum(z['J'][i] for z in pieces) for i in range(3)),
            sum(z['E'] for z in pieces),sum(z['N'] for z in pieces))

def normplane(n,h):
    s=abs(next(x for x in n if x));return tuple(x/s for x in n),h/s

def audit(u):
    pts=tuple(tuple(map(F,p)) for p in points(u));hs=tuple((tuple(map(F,n)),F(h)) for n,h in planes(u))
    assert len(set(pts))==8
    for face,(n,h) in zip(FACES,hs):
        assert all((h-dot(n,p)==0 if i in face else h-dot(n,p)>0) for i,p in enumerate(pts))
    hull=set()
    for i,j,k in combinations(range(8),3):
        n=cross(sub(pts[j],pts[i]),sub(pts[k],pts[i]))
        if not any(n):continue
        h=dot(n,pts[i]);sg=[h-dot(n,p) for p in pts]
        if min(sg)<0<max(sg):continue
        if max(sg)<=0:n=tuple(-x for x in n);h=-h
        hull.add(normplane(n,h))
    assert hull=={normplane(n,h) for n,h in hs}
    allv=set()
    for tri in combinations(range(7),3):
        p=solve([hs[i][0] for i in tri],[hs[i][1] for i in tri])
        if p is not None and all(h-dot(n,p)>=0 for n,h in hs):allv.add(p)
    assert allv==set(pts)
    ed={tuple(sorted((face[j-1],face[j]))) for face in FACES for j in range(len(face))}
    assert ed==set(EDGES) and 8-13+7==2
    assert all(sum(i in f and j in f for f in FACES)==2 for i,j in EDGES)
    af=fan(pts,hs,0);bf=fan(pts,hs,1)
    V,J,E,N=total(af);assert (V,J,E,N)==total(bf)
    g=tuple(x/V for x in J);t=6*V;q=N/E;r=N/V;T=N/(6*V*E)
    ev=[ell(p) for p in pts];gv=[nn(p)-r-q*ell(p) for p in pts]
    assert all(ev[i]>0 for i in range(5)) and ev[5:]==[0,0,0]
    assert gv[2]<0<gv[3] and min(gv[4:])>0 and all(pts[i][2]<0 for i in range(4,8))
    assert 0<T<2 and g[0]>=F(1,4) and g[1]>=F(1,4) and 4*(g[0]+g[1])<=t+1
    hinge=[facet_product(pts,FACES[i],gv,[p[axis] for p in pts]) for i,axis in ((2,0),(3,1),(4,0),(5,1))]
    assert hinge[0]<0
    pp=J[0]+J[1];rhs=[q*V-3*pp,q*J[0]-J[1],q*J[1]-J[0],q*J[2]-pp]
    surf=[facet_product(pts,FACES[6],gv,[F(1)]*8 if i==0 else [p[i-1] for p in pts])/F(1,2) for i in range(4)]
    residual=[x-y for x,y in zip(surf,rhs)]
    assert any(residual) and residual[0]-F(19,20)*residual[1]-F(3,10)*residual[2]-F(1,2)*residual[3]==0
    area=facet_product(pts,FACES[6],[F(1)]*8,[F(1)]*8)/F(1,2)
    g2=facet_product(pts,FACES[6],gv,gv)/F(1,2)
    assert g2==F(11,5)*surf[1]+F(31,20)*surf[2]-r*surf[0]
    assert surf[0]**2<area*g2 and area<3*V
    root=next(z for z in bf if z['facet']==6);assert root['E']==F(1,2)*root['V']/4
    # Each endpoint has its OWN uniform centroid, one Euclidean metric,
    # and the same-origin polar; no mechanics claim for the whole arc.
    xx=[sub(p,g) for p in pts];poles=[tuple(x/(h-dot(n,g)) for x in n) for n,h in hs]
    pu=[[] for _ in pts];pd=[[] for _ in hs];packets=[]
    for i,j in EDGES:
        f,k=[h for h,face in enumerate(FACES) if i in face and j in face]
        z=(dot(xx[i],sub(xx[j],xx[i])),dot(xx[j],sub(xx[i],xx[j])),
           dot(poles[f],sub(poles[k],poles[f])),dot(poles[k],sub(poles[f],poles[k])))
        assert all(z)
        pu[i].append(z[0]);pu[j].append(z[1]);pd[f].append(z[2]);pd[k].append(z[3])
        packets.append(dict(edge=(i,j),facets=(f,k),primitives=z))
    suh=(sum(max(x)<0 for x in pd),sum(max(x)<0 for x in pu),sum(max(z['primitives'])<0 for z in packets))
    assert suh[0]+suh[1]-suh[2]==2
    return dict(u=u,endpoints=EP,vertices=pts,planes=hs,facets=FACES,edges=EDGES,
                V=V,J=J,E=E,N=N,T=T,g=g,G=gv,ell=ev,GD_over_r=gv[3]/r,
                A_fan=af,B_fan=bf,whole_hinges=hinge,root_reaction_residual=residual,
                root_integrals_1_x_y_z=surf,root_integral_G_squared=g2,root_coarea=area,
                strict_SUH=suh,weak_packets=0,edge_packets=packets,
                status='actual NONSTATIONARY uniform body, T<2, not 110')


def algebra():
    a,b,c,d,T,t,mu,L,n,G,H0,H1,H2=S.symbols('a b c d T t mu L n G H0 H1 H2')
    hc=a+b+c;hd=a+b+d
    cm=hc*t+hd-4*T*t*mu;cc=4*t*mu-hd-c*t
    assert S.expand(cm+cc-t*(a+b-4*(T-1)*mu))==0
    LA=t*T*(mu+a)/3;D=a+b-4*(T-1)*mu
    psi=a*T*T+b*T-3*(a+b)
    assert S.expand(3*(T-1)*(LA-t*(4-T)*mu)-t*(psi+(3-T)*D))==0
    assert S.expand(psi-(a-b)*(T-1)-(T-2)*(a*(T+1)+2*b))==0
    assert S.expand(psi.subs(T,2)-(a-b))==0
    g1,g2,eps=S.symbols('g1 g2 eps')
    formula=(-3*L+g1+g2)*(H1+H2)+g1*H1+g2*H2
    assert S.expand(formula-(((-3*L)+2*g1+g2)*H1+((-3*L)+g1+2*g2)*H2))==0
    assert S.expand(formula.subs({g1:L-eps,g2:L-eps})+3*eps*(H1+H2))==0
    return dict(mean_budget='4*(T-1)*mu<=a+b',threshold_polynomial=str(psi),
                threshold='theta=(-b+sqrt(b*b+12*a*(a+b)))/(2*a)',
                point_gap_T_ge_2='G(p)<=LA-t*(a-b)/3-t*(T+1)*ell(p)',
                whole_AC_gap='int_AC G*x/k<=-t*(a-b)*int_AC x/k/4-t*(T+1)*c*xP*xP/24',
                scope='analytic same-body J and full-boundary cone premises; not a formalization')


def positive(expr,z):
    # Bernstein positivity on the WHOLE CLOSED unit interval, not sampling.
    num,den=map(S.expand,S.fraction(S.cancel(expr)))
    if den.subs(z,0)<0:num=-num;den=-den
    if num==0:return None
    out=[]
    for poly in (num,den):
        p=S.Poly(poly,z);degree=int(p.degree());co=[p.nth(i) for i in range(degree+1)]
        bc=[S.factor(sum(co[j]*S.Rational(comb(i,j),comb(degree,j)) for j in range(i+1))) for i in range(degree+1)]
        if min(bc)<=0:return None
        out.append([str(x) for x in bc])
    return out


def arc(controls):
    z=S.symbols('theta');u=1-z/2
    pts=tuple(tuple(map(S.Rational,p)) if i<5 or i==7 else tuple(S.cancel(x) for x in p)
              for i,p in enumerate(points(u)))
    hs=tuple((tuple(S.sympify(x) for x in n),S.sympify(h)) for n,h in planes(u))
    guards=[]
    def check(expr):
        bc=positive(expr,z);assert bc is not None,(expr,z)
        guards.append(bc)
    for face,(n,h) in zip(FACES,hs):
        for i,p in enumerate(pts):
            sl=S.cancel(h-dot(n,p))
            if i in face:assert sl==0
            else:check(sl)
    # Positive normal circuit spans all three dimensions for the whole arc.
    assert tuple(S.expand(hs[6][0][i]+S.Rational(1,2)*hs[2][0][i]
                         +(S.Rational(19,20)-u/2)*hs[0][0][i]+S.Rational(3,10)*hs[1][0][i]) for i in range(3))==(0,0,0)
    check(S.Rational(19,20)-u/2)
    assert det(hs[0][0],hs[1][0],hs[6][0])!=0
    # Whole true facet polygons: all vertices on each support form the
    # strict convex cycle listed in FACES, for every theta in [0,1].
    # Every edge already has two such facets. The hull's facet-adjacency
    # graph is connected, hence these are ALL its facets. No requirement
    # that an irrelevant triple of support planes remain independent.
    oriented=[];cycle_guards=0
    for k,face in enumerate(FACES):
        axes=(1,2) if k==0 else ((0,2) if k==1 else (0,1))
        def turn(i,j,h):
            p,q,r=(pts[v] for v in (i,j,h));a,b=axes
            return S.cancel((q[a]-p[a])*(r[b]-p[b])-(q[b]-p[b])*(r[a]-p[a]))
        sign=S.sign(turn(*face[:3]).subs(z,0));assert sign
        for j in range(len(face)):
            i0,i1=face[j-1],face[j]
            for other in face:
                if other not in (i0,i1):
                    check(sign*turn(i0,i1,other));cycle_guards+=1
        normal=hs[k][0]
        ori=dot(cross(sub(pts[face[1]],pts[face[0]]),sub(pts[face[2]],pts[face[0]])),normal)
        oriented.append(face if ori.subs(z,0)>0 else tuple(reversed(face)))
    directed=[(face[j-1],face[j]) for face in oriented for j in range(len(face))]
    assert len(directed)==26 and len(set(directed))==26
    assert all((j,i) in directed for i,j in directed)
    # Preserve the nonincident parallelism as an exact diagnostic, not a
    # purported lattice wall: Fy/AC/BC is inconsistent at theta=1/25.
    irrelevant=(1,2,4)
    dd=S.cancel(det(*(hs[i][0] for i in irrelevant)))
    assert dd.subs(z,S.Rational(1,25))==0
    atwall=[(tuple(x.subs(z,S.Rational(1,25)) for x in hs[i][0]),hs[i][1]) for i in irrelevant]
    assert S.Matrix([n for n,h in atwall]).rank()==2
    assert S.Matrix([list(n)+[h] for n,h in atwall]).rank()==3
    def symfan(apex):
        V=S.Integer(0);J=[S.Integer(0)]*3
        for face in FACES:
            if apex in face:continue
            for j in range(1,len(face)-1):
                ids=(apex,face[0],face[j],face[j+1]);o=pts[apex]
                w=S.cancel(det(*(sub(pts[i],o) for i in ids[1:]))/6)
                if w.subs(z,0)<0:w=-w
                check(w);V+=w
                for k in range(3):J[k]+=w*sum(pts[i][k] for i in ids)/4
        return S.cancel(V),tuple(S.cancel(x) for x in J)
    V,J=symfan(0);vb,jb=symfan(1)
    assert S.cancel(V-vb)==0 and all(S.cancel(x-y)==0 for x,y in zip(J,jb))
    E,N=map(S.cancel,en(V,J));T=S.cancel(N/(6*V*E));r=N/V;q=N/E
    gv=[S.cancel(nn(p)-r-q*ell(p)) for p in pts]
    # The AC quad is integrated from A, with both projected areas positive.
    def prod(face,ff,hh):
        ans=0
        for j in range(1,len(face)-1):
            ids=(face[0],face[j],face[j+1]);p,p1,p2=(pts[i] for i in ids)
            area=S.cancel(((p1[0]-p[0])*(p2[1]-p[1])-(p1[1]-p[1])*(p2[0]-p[0]))/2)
            if area.subs(z,0)<0:area=-area
            check(area)
            f=[ff[i] for i in ids];h=[hh[i] for i in ids]
            ans+=area*(sum(f)*sum(h)+sum(x*y for x,y in zip(f,h)))/12
        return S.cancel(ans)
    work=prod(FACES[2],gv,[p[0] for p in pts])
    assert S.cancel(S.diff(T,z)+work/(12*V*E))==0
    for val in (V,E,N,2-T,-work,-gv[2],gv[3],*gv[4:],
                J[0]/V-S.Rational(1,4),J[1]/V-S.Rational(1,4),
                6*V+1-4*(J[0]+J[1])/V,*[-pts[i][2] for i in range(4,8)]):check(val)
    # A complete strongly mixed subarc, not a sampled sign assignment.
    strong=S.cancel(gv[3]/r-S.Rational(581537111,3371659200))
    check(strong.subs(z,S.Rational(2,5)+S.Rational(3,5)*z))
    for control in controls:
        zz=2*(1-S.Rational(control['u']))
        for expr,value in ((V,control['V']),(E,control['E']),(N,control['N']),(T,control['T'])):
            assert expr.subs(z,zz)==S.Rational(value)
        assert all(expr.subs(z,zz)==S.Rational(value) for expr,value in zip(J,control['J']))
    assert S.Rational(controls[2]['GD_over_r'])>S.Rational(581537111,3371659200)
    return dict(parameter='0<=theta<=1; u=1-theta/2',vertices=[[str(x) for x in p] for p in pts],
                V=str(V),J=[str(x) for x in J],E=str(E),N=str(N),T=str(T),whole_AC_work=str(work),
                positive_rational_guards=len(guards),positive_Bernstein_coefficients=sum(len(x) for g in guards for x in g),
                strict_facet_cycle_guards=cycle_guards,strongly_mixed_subarc='2/5<=theta<=1',
                irrelevant_parallelism='Fy/AC/BC inconsistent at theta=1/25',
                coefficients=guards,
                status='entire actual quadrilateral-facet arc; original T strictly increases; no full-stationarity or whole-arc mechanics claim')


def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def main():
    cert=algebra();controls=[audit(u) for u in PARAMS];path=arc(controls)
    assert controls[0]['T']==F('5374273708344352525/3838421850974805261')
    report=dict(version=1,parent='minimum-0178',certificate=cert,controls=controls,arc=path)
    raw=(json.dumps(encode(report),sort_keys=True,indent=2)+'\n').encode()
    Path('ud_abarrier_v1.json').write_bytes(raw)
    print('SAME_BODY_CONE_PLUS_J_POINT_BARRIER_IDENTITIES_PASS')
    print('TRUE_WHOLE_A_FACET_NEGATIVE_WORK_IDENTITY_PASS')
    print('FOUR_ACTUAL_8_13_7_BODIES_TWO_FANS_AND_208_OWN_EDGE_PRIMITIVES_PASS')
    print('WHOLE_INWARD_AC_QUADRILATERAL_ARC_TRUE_HULL_AND_ORIGINAL_T_ASCENT_PASS')
    for obj in controls:print('u='+str(obj['u'])+' T='+str(obj['T'])+' SUH='+str(obj['strict_SUH']))
    print('positive_rational_guards='+str(path['positive_rational_guards']))
    print('positive_Bernstein_coefficients='+str(path['positive_Bernstein_coefficients']))
    print('strict_facet_cycle_guards='+str(path['strict_facet_cycle_guards']))
    print('report_bytes='+str(len(raw)))
    print('report_sha256='+hashlib.sha256(raw).hexdigest())
    print('PROPER33_NEGATIVE_Z_A_HINGE_EXCLUSION_V1_RECOVERY_PASS')

if __name__=='__main__':main()
```

## 10. Что остаётся и наиболее полезное продолжение

При принятом J больше нет целевого strongly mixed U_D стационарного остатка. Самая полезная независимая проверка новой части — короткая цепочка MEAN → ID → целый AC-шарнир, особенно строгий вклад ACP при T=Theta. Здесь нет зависимости от последующего численного оптимизатора, полного удаления U или перехода между разными special-B графами.

Следующая содержательная граница — не повтор семипараметрического U_D поиска при T>=51/25, а перенос этого полного A-шарнирного механизма туда, где защищённые координатные грани увеличены и тождественные вклады hc*x/24,hd*y/24 уже не следуют из двух максимальных треугольников. Его автоматический перенос туда не утверждается. Отдельная задача VALUE для произвольных negative-z root-only тел также остаётся: такое тело не обязано удовлетворять шарнирной стационарности полного отмеченного максимума.

Результат не превращает вспомогательные trace-counts 8/13/7 в исключение механических 10/17/9. Не получен новый 110 attainer, не закрыты нулевые endpoints и все остальные защищённые patterns, не дан недостающий incidence/mechanics bridge. Принятая глобальная граница остаётся 34<=C_min<=622; точный механический минимум этим результатом не установлен. :contentReference[oaicite:6]{index=6}
