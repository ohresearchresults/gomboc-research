# figure-0563

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Nimble Finch 93 — внутренняя двухфартучная перестройка и два точно исключённых луча

## 1. Результат

**Собственный strict110 не получен. Получен новый точный конструктивный нерекорд `NF93_DOUBLE_FLAP25`: V/E/F = 92/224/134, strict(S,U,H) = (2,2,2), additional weak = (0,0,0), primitive-zero = (0,0,0).** В JOINT56_L30 действительно добавлены 25 новых настоящих вершин; все 67 прежних настоящих вершин сохранены. Исходная 26-угольная грань сохранена. Дополнительно появились 14- и 15-угольные максимальные грани. Старое Q-седло на ребре 6–70 исчезло; его заменило настоящее ребро **90–91 между двумя новыми вершинами**. P-седло 13–22 осталось. Это фактическая перестройка merged hull и Q-разреза, не подавление малого численного штрафа.

Вторая завершённая часть — два семейства внутренней протяжки, построенные из L18 и L30. Для каждого **точно доказано U≥2 при любом t>0**, с фактическим центроидом однородного заполненного тела, на всём неограниченном луче параметра. Свидетельствующие вершины меняются. Следовательно, исключение не основано на искусственном закреплении исходной пары корней.

Это ограниченный отрицательный результат для двух конкретных направлений, не исключение всех добавлений, всех внутренних протяжек или задачи E≤249.

## 2. Источник и граница воспроизводимости

Полностью прочитан единственный приложенный файл: 2121 строка, 410253 байта, SHA-256 `12d1da46dd12ea5da2118cf6f3b88c75a0c4ab5cc3506066094bf39d4d935e61`. Извлечённые буквальные модули проверены:

| Модуль | Байты | SHA-256 |
|---|---:|---|
| audit56.py | 42703 | 1ca8d69e38bc029a0cb3e4d707cede38f65139e4d3c88010683c5fccbec24258 |
| methods56.py | 29721 | 9404f7ec6996c3d6b7f439ac143f66a36135ad23eb4be7333d526ec529a0d05e |

F18, L18, F30 и L30 независимо повторно прошли родительский exact audit. Новые конструкции используют именно решёточные L18/L30. FULL76 и C622 не использованы. Решёточные координаты восстановлены по буквальному родительскому правилу, включая точную проекцию контактных строк.

Есть неразрешённая **неоднозначность хеширования родительской оболочки**. В pack родителю `figure-0559` приписан SHA `e0181e33bc72dfc97e64bd431ef4a23f627e5c083036b4ed931e2393205b22db`. Естественная буквальная UTF-8-подстрока от `# Clear Harbor 55 — продолжение:` до EOF имеет 96005 байт и SHA `844968b8215b0b59a927bfd42113dd963d9023a48a28c9b9b2dcd0125ddf6cca`. Причина различия не установлена; другая хешируемая оболочка не предоставлена. Поэтому e018… не объявляется пересчитанным. Содержательного конфликта использованных массивов не обнаружено. Новые результаты привязаны к проверенному pack и совпавшим хешам буквальных модулей.

Предыдущая временная директория незавершённого исполнения не сохранилась. Ранние численные черновики не использованы как точные преемники или доказательства. Все принятые ниже объекты заново вычислены из приложенного pack.

## 3. Новый механизм: два плоских фартука на обоих седельных рёбрах

Нумерация здесь — исходные материальные строки L30, начиная с нуля. Старые 75 строк остаются в наборе; восемь из них уже не были настоящими вершинами.

На P-ребре 13–22 и Q-ребре 70–6 построены две отдельные плоские выпуклые цепочки. Для пары a,b и t_i=i/(m+1) новая точка задаётся точно:

`w_i = p_a + t_i (p_b-p_a) + 4 t_i(1-t_i) u / 1024`.

Полные параметры:

| Фартук | a,b | m | Новые материальные номера | Точный u |
|---|---|---:|---|---|
| P | 13,22 | 12 | 75–86 | `(1918777/604052500, 1, -193949/151013125)` |
| Q | 70,6 | 13 | 87–99 | `(179328288526762213/213245086998660969, 7070786827652000/30463583856951567, 1)` |

Направления получены без округления нормалей. Для каждого ребра взята сумма рационально нормированных внешних нормалей большой грани и соседней треугольной грани. Вектор u лежит в новой плоскости, направлен за соседнюю треугольную грань, но строго внутрь полупространства большой грани.

Точный общий предел амплитуды из всех сохраняемых опорных неравенств и индивидуальных свидетелей старых вершин равен

`114961718385488923 / 87804941690777445216`.

Выбранная двоичная амплитуда 1/1024 строго меньше этого предела. Каждая новая точка нарушает ровно одну прежнюю опорную плоскость — свою соседнюю треугольную грань. Все 25 новых точек строго по внутреннюю сторону плоскости большой грани. Старые вершины защищены отдельными строгими опорными функционалами; их сохранение не предположено по рисунку.

Три большие максимальные грани фактического exact hull:

```text
C30 = [0,1,2,3,5,7,8,9,13,22,26,30,34,37,41,44,48,50,49,52,55,58,62,70,6,4]
FP  = [13,75,76,77,78,79,80,81,82,83,84,85,86,22]
FQ  = [6,70,87,88,89,90,91,92,93,94,95,96,97,98,99]
```

Остальные 131 максимальная грань — треугольники. Настоящие устойчивые носители — C30 и `[6,72,69]`; U = `[6,70]`; H = `{13–22,90–91}`. Для положительного Q-бара достигающая пара полярных вершин соответствует **FQ и треугольнику `[91,90,72]`**. Прежнее достигающее ребро 6–70 больше не является H. Для P достигающее ребро осталось 13–22.

Все положительные бары этого тела:

`P = [0.16553266013146867]`, `Q = [0.2186843995118498]`.

P слегка уменьшен относительно L30, Q увеличен. Это не парето-рекорд и не приближение, объявленное 110. Полезность нерекорда — точная новая контактная геометрия, перенос Q-седла на новые вершины и дополнительный бюджет.

### Бюджет, который действительно освободился

Из Эйлера и суммы длин максимальных граней:

`E = 3V - 6 - sum_faces(|f|-3)`.

У DOUBLE_FLAP25 суммарный дефицит триангуляции равен `(26-3)+(14-3)+(15-3)=46`, поэтому E=224. **Остаётся место ещё для восьми произвольных добавляемых точек, если они строго сохраняют эти три грани:** V≤100 и E≤3·100−6−46=248. Сохранение остальных старых вершин для этой верхней оценки не требуется.

Более общая двухфартучная формула при m=m1+m2 и сохранении всех вершин цепочек даёт E=174+2m. Значение m=37 допускает E=248. Это параметрическая геометрическая оценка, **не отдельно выполненный census 37-точечного тела**. Фактически проверен вариант m=25.

## 4. Два полностью исключённых внутренних луча

Исследованы семейства

`K18(t)=JOINT56_L18 + [0,t(1,0,0)]`,

`K30(t)=JOINT56_L30 + [0,t(511,308,-803)/1000]`, `t>0`.

Это `conv(K,K+tD)`. Скалярные произведения D с исходными нормалями больших граней отрицательны: −272 для L18 и −46879/1000 для L30. Поэтому исходная большая грань, её плоскость и все её углы сохраняются при любом t>0. Добавленная геометрия находится по внутреннюю сторону этой плоскости.

Каждая исходная грань либо остаётся, либо переносится на tD. Каждое ребро силуэта рождает настоящую четырёхугольную грань. При k рёбрах силуэта:

`V'=V+k, E'=E+2k, F'=F+k`.

Точный результат:

| Семейство | k | V/E/F для каждого t>0 | Максимальные грани |
|---|---:|---|---|
| L18 | 15 | 90/234/146 | 130 треугольников, 15 четырёхугольников, 18-угольник |
| L30 | 31 | 98/234/138 | 106 треугольников, 31 четырёхугольник, 26-угольник |

Это настоящие максимальные грани, не интеграционная триангуляция. У L18 в конечном hull 43 неперенесённые и 47 перенесённых вершины; у L30 — 58 и 40. Приросты V равны 15 и 31, а не количеству строк второй копии. Значение 31 совместимо с E≤249 благодаря дополнительным четырёхугольникам.

### Масса и строгий сертификат

Объём и первый момент интегрированы формально по коэффициентам:

`V(t)=V0+A t`, `M(t)=M0+B t+(A/2)D t^2`, `g(t)=M(t)/V(t)`.

Все коэффициенты рациональны. Исчезновение более высоких коэффициентов проверено тождественно. Значения в конечных телах сверены с двумя независимыми тетраэдральными интегрированиями exact audit. Здесь не используется прежний центроид или среднее вершин.

Для каждой настоящей ориентированной пары соседей i→j строится точный числитель

`P_ij(t) = (M(t)-V(t)p_i(t)) · (p_j(t)-p_i(t))`.

Положительность всех таких числителей эквивалентна строгому U в вершине i. Удаляются только множители t, положительные на t>0. После t=s/(1−s) применяются коэффициенты Бернштейна. Все необходимые полиномы квадратичны.

Восстановитель проверяет **строгую положительность каждого коэффициента**, а не float-знаки. Получены следующие свидетели:

| Семейство | Диапазон t | Две гарантированно строгие U |
|---|---|---|
| L18 | 0<t≤1 | 6⁰, 62¹ |
| L18 | 1≤t<∞ | 0⁰, 74¹ |
| L30 | 0<t≤1/3 | 6⁰, 70¹ |
| L30 | 1/3≤t≤1 | 6⁰, 53⁰ |
| L30 | 1≤t<∞ | 6⁰, 50¹ |

Здесь i⁰=p_i, i¹=p_i+tD. Для L18 достаточно двух листьев двоичного покрытия, для L30 — трёх. Геометрическая часть дополнительно проверяет, что опорные зазоры всех сохраняемых граней являются неотрицательными линейными полиномами на всём луче и вне соответствующей грани не обращаются в ноль при t>0.

**Следствие: оба указанных целых луча не содержат собственного110.** При t=0 это отдельно следует из exact222 исходных тел. Между перечисленными ниже конечными телами не заявляется постоянство остальных S/U/H, отсутствие слабых равновесий или отсутствие primitive-zero. Для исключения110 достаточно доказанных двух строгих U.

Это ограничение общего направления переноса, не доказанное препятствие самой большой грани. Оно не распространяется на индивидуальные перемещения, независимые фартуки, гомотетическую вторую копию, поворот D или произвольные добавления.

## 5. Принятые конечные тела, масса и полный census

Все строки — filled homogeneous, density=1, с новым собственным центроидом. Во всех пяти строках additional weak и primitive-zero равны 000. Объёмы и центроиды в таблице округлены; восстановленные audit JSON содержат точные дроби.

| Тело | V/E/F | strict S/U/H | Объём | Центроид |
|---|---|---|---:|---|
| DOUBLE_FLAP25 | 92/224/134 | 2/2/2 | 1.217343895893200 | (−0.156439111688498, −0.085355089447633, −0.097341775175655) |
| L18, t=1/10000 | 90/234/146 | 2/2/2 | 1.289514639644005 | (−0.193501630305900, −0.133821641137761, −0.142911747110600) |
| L30, t=1/1000 | 98/234/138 | 2/2/2 | 1.218560475993689 | (−0.156086752167121, −0.085102096251173, −0.097763748710427) |
| L30, t=1/100 | 98/234/138 | 17/15/30 | 1.230162624601646 | (−0.152858730008358, −0.083027894004265, −0.101545460110498) |
| L30, t=1 | 98/234/138 | 13/10/21 | 2.506398971476898 | (0.149743425867132, 0.106237007123874, −0.508026367892022) |

Полные положительные P/Q-бары всех пяти тел восстанавливаются кодом ниже без порога отсечения: он печатает все глубины и записывает точные `birth`, `death`, `depth`, компоненты, разрезы и достигающие пути. Числа баров соответственно: 1+1, 1+1, 1+1, 14+16, 9+12. Их полные численные списки дополнительно приведены в полном отчёте с буквальными автономными исходниками (`HANDOFF.md`). Этот файл не является единственным способом восстановления: полный точный патч и проверочные хеши находятся ниже.

При t=1/100 у L30 обе самые глубокие особенности мельче, чем при t=1/1000, но появляются ещё 28 положительных баров: всего P=14 и Q=16. Поэтому уменьшение только двух глубин здесь действительно скрывает ухудшение полного census.

### Корни и носители

Для L18 при t=1/10000: U={6⁰,62¹}; S — исходный 18-угольник и треугольник [14,16,24]⁰; H — 6¹–63¹ и 13⁰–22⁰.

Для L30 при t=1/1000: U={6⁰,70¹}; S — C30⁰ и [6,72,69]⁰; H — 6⁰–70⁰ и 13¹–22¹. Уже этот переход заменяет материальный P-корень и переносит P-достигающее ребро.

Полные U при t=1/100:

`[6⁰,7¹,8¹,9¹,14⁰,13¹,50¹,49¹,52¹,55¹,51¹,58¹,65¹,70¹,57¹]`.

Все S этого тела — C30⁰ и следующие 16 неперенесённых треугольников:

```text
[3,10,15], [11,21,20], [11,24,21], [16,18,31],
[19,33,32], [18,32,31], [11,20,15], [12,14,24],
[11,12,24], [18,19,32], [17,36,33], [16,31,24],
[24,31,20], [28,43,60], [6,72,69], [6,70,72].
```

Полные U при t=1:

`[6⁰,53⁰,60⁰,66⁰,72⁰,50¹,49¹,51¹,65¹,57¹]`.

Полные S при t=1: C30⁰; треугольники [45,60,56]⁰, [6,72,69]⁰, [6,70,72]⁰, [51,57,71]¹; восемь новых четырёхугольников над рёбрами

`[3,15], [15,20], [20,31], [53,56], [60,66], [56,60], [69,72], [70,72]`.

Четырёхугольник над [i,j] означает conv(p_i,p_j,p_j+tD,p_i+tD). При t=1 старый 70¹ уже не U; старший P-корень остаётся 6⁰, пик крупнейшего конечного P-бара — 50¹. Пик крупнейшего Q-бара теперь несёт новый четырёхугольник над [20,31], а не исходный малый S-треугольник. Достигающая Q-пара — четырёхугольники над [60,66] и [56,60]. Полные H-носители сохранены в exact audit каждого тела.

## 6. Отличие от прежних опытов и полезное продолжение

В родителе десять меридиональных узлов добавлялись на длинной угловой дуге; проверялись 4096 float-проб. Forest-проектор локально ремонтировал ориентированные леса. Здесь сначала перестроен весь нормальный веер внутренней протяжкой, и два выбранных целых луча закрыты точным U≥2. Затем общность переноса снята: построены два рациональных многоугольных фартука на обоих седельных рёбрах. Они дают 25 новых настоящих вершин, два дополнительных многократных контакта и фактическую миграцию Q-седла. Ни минимальный forest, ни штраф за две глубины в точном построении не использовались.

Следующий полезный ход — продолжать **DOUBLE_FLAP25**, а не увеличивать длину исключённых переносов: снять требование сохранения всех старых нетривиальных вершин, усилить P-перестройку до смены носителя 13–22 и использовать запас до восьми неплоских добавлений для совместного управления массой и Q-разрезом. Сохранять три большие грани следует только пока это полезно. Сертификат сохранения всех прежних вершин в текущем генераторе — достаточное удобное ограничение, не доказанная необходимость. Новые корни, носители и положительные бары должны определяться заново. Такое более широкое семейство этой работой не исключено.

## 7. Капсула восстановления

Ниже — **полный точный патч к уже предоставленному неизменяемому родителю**. Его единственный внешний вход — приложенный в этой транзакции journal с проверяемыми байтами и SHA. Патч извлекает из него полный буквальный auditor и все исходные массивы; никаких архивных ID, недоступных путей, установленных родительских модулей или исследовательских коннекторов не требуется. Все новые операции, параметры, проверки и генераторы приведены полностью.

Фактическая среда: **Python 3.13.5, только стандартная библиотека**. Сохранить код как `finch93_patch.py` и выполнить:

```sh
python3.13 -B -S finch93_patch.py 'research-journal(20260926-065407).md' --out finch93_verified
```

Обязательные префиксы/конечные маркеры:

```text
STRICT_U2_ALL_POSITIVE_T JOINT56_L30 5 2 3
STRICT_U2_ALL_POSITIVE_T JOINT56_L18 3 1 2
FINCH93_EXACT_RAYS_PASS_NO_110
FINCH93_DOUBLE_FLAP25_PASS_222_NOT_110
```

Самостоятельный вариант с повторно включёнными обоими 75-строчными массивами, без необходимости передавать journal, также сохранён: `finch93_recover.py`, 20681 байт, SHA `274cf091e4bd787c59bb54169cb87c95d3b143ec8c2d2fc183caaeef33bade1b`; `flaps93_exact.py`, 3726 байт, SHA `6a4881f2a1b7cbfcd3267b0cd360cd2e258024eff1b88aec078ced42aa127310`. Полный пакет исходников и точных отчётов (`finch93_handoff.zip`) — дополнительная копия, не замена приведённому патчу.

Проверочные объекты:

| Файл | Байты | SHA-256 |
|---|---:|---|
| inputs.json | 6606 | ca1a7a0957370411ba6f053541ef9779c77c1677ccf3213d4b94efc153583c5b |
| ray30/t_1_1000.json | 20625 | 5cc11376a0e348b49ba6ab8a4502297265e4c06b58566e9ca7a45b116188a7c8 |
| ray30/t_1_100.json | 36566 | b76291369d2d81e2f4a7d8f55cc8209383e5976db206c94e75ecdeeb5e9c78c8 |
| ray30/t_1.json | 30513 | 7debe5c92f6bba9f9d02dbb04b359b9fd3f2cca4fd8b5a65539811272eb71760 |
| ray30/cover.json | 1347 | 1e95903cd40c1961ae41d4b43b3b3b9ed3ebd93f1d8870f4e5afb85c3fde45d8 |
| ray18/t_1_10000.json | 21477 | d5eb798567084f4d333ec0f05eb8d959b741719118e66aa0868153b75221aef9 |
| ray18/cover.json | 1213 | 1822c309f6f0f85331fe1196c2783bc50d0d3fa6cc613fc49f6b9a7cff522f09 |
| flap25/audit.json | 24690 | 5c69b37212fa14bc9290f939c3d8796da96a47d22f252cfeccffc86963f59724 |
| flap25/meta.json | 448 | 73e3be02b02ccc0a0400bd7ddfe9e84de5724e37d5b5b0b3076dc5adf64e0cf0 |

## 8. Полный runnable patch

```python
'''Exact patch against the supplied literal parent.
Python 3.13.5, standard library only.
Usage: python -B -S finch93_patch.py JOURNAL --out finch93_verified
'''
from pathlib import Path
import hashlib,sys,types
if len(sys.argv)<2:
    raise SystemExit('usage: finch93_patch.py JOURNAL [--out DIR]')
journal=Path(sys.argv.pop(1)).read_bytes()
assert len(journal)==410253
assert hashlib.sha256(journal).hexdigest()=='12d1da46dd12ea5da2118cf6f3b88c75a0c4ab5cc3506066094bf39d4d935e61'
text=journal.decode('utf-8')
code=text[text.index('## Модуль1 — audit56.py'):].split('```python\n',1)[1].split('\n```',1)[0]+'\n'
assert len(code.encode())==42703
assert hashlib.sha256(code.encode()).hexdigest()=='1ca8d69e38bc029a0cb3e4d707cede38f65139e4d3c88010683c5fccbec24258'
parent=types.ModuleType('audit56')
parent.__file__='<verified-literal-parent>'
exec(compile(code,parent.__file__,'exec'),parent.__dict__)
globals().update({k:v for k,v in vars(parent).items() if not k.startswith('_')})
from math import comb

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def mul(s,a):
    return tuple(s*x for x in a)

def ray_model(K):
    P=K['points']
    N=len(P)
    positive=[dot(z[:3],D)>0 for z in K['planes']]
    assert all(dot(z[:3],D)!=0 for z in K['planes'])
    ff=[[i+N*positive[k] for i in f] for k,f in enumerate(K['faces'])]
    silhouette=[]
    for (i,j),(f,g) in zip(K['edges'],K['edge_faces']):
        if positive[f]==positive[g]:
            continue
        q=[i,j,j+N,i+N]
        normal=cross(sub(P[j],P[i]),D)
        if dot(normal,sub(add(K['centroid'],mul(F(1,2),D)),P[i]))>0:
            q.reverse()
        ff.append(q)
        silhouette.append((i,j))
    ids=sorted({i for f in ff for i in f})
    ix={v:i for i,v in enumerate(ids)}
    pts=[(P[i%N],D if i>=N else (F(0),)*3) for i in ids]
    ff=[[ix[i] for i in f] for f in ff]
    ee=sorted({tuple(sorted((i,j))) for f in ff for i,j in zip(f,f[1:]+f[:1])})
    k=len(silhouette)
    assert len(ids)==K['V']+k
    assert len(ee)==K['E']+2*k
    assert len(ff)==K['F']+k
    # Formal polynomial integration, not interpolation.
    vp=[F(0)]*4
    mp=[[F(0)]*5 for _ in range(3)]
    for f in ff:
        for j in range(1,len(f)-1):
            pp=[pts[i] for i in (f[0],f[j],f[j+1])]
            dc=[F(0)]*4
            for bits in product((0,1),repeat=3):
                dc[sum(bits)]+=det(*(pp[i][bits[i]] for i in range(3)))/6
            for r in range(4):
                vp[r]+=dc[r]
                for s in (0,1):
                    for x in range(3):
                        mp[x][r+s]+=dc[r]*sum(p[s][x] for p in pp)/4
    assert vp[2:]==[0,0]
    assert all(q[3:]==[0,0] for q in mp)
    assert vp[0]==K['volume']
    assert tuple(q[0] for q in mp)==K['moment']
    assert vp[1]>0
    # U numerator: (M(t)-V(t)*p_i(t)) dot (p_j(t)-p_i(t)).
    poly=[[] for _ in pts]
    for i,j in ee+[(j,i) for i,j in ee]:
        aa,bb=pts[i]
        cc,dd=pts[j]
        z=[]
        for r in range(3):
            z.append(tuple(mp[x][r]-(vp[0]*aa[x] if r==0 else vp[0]*bb[x]+vp[1]*aa[x] if r==1 else vp[1]*bb[x]) for x in range(3)))
        p=[F(0)]*4
        for r in range(3):
            p[r]+=dot(z[r],sub(cc,aa))
            p[r+1]+=dot(z[r],sub(dd,bb))
        # Only remove factors strictly positive on t>0.
        while len(p)>1 and p[0]==0:
            p.pop(0)
        while len(p)>1 and p[-1]==0:
            p.pop()
        assert any(p)
        n=len(p)-1
        # Bernstein coefficients after t=s/(1-s).
        poly[i].append(tuple(v/F(comb(n,r)) for r,v in enumerate(p)))
    return dict(pts=pts,faces=ff,edges=ee,ids=ids,k=k,
                volume=vp[:2],moment=[q[:3] for q in mp],poly=poly)

def half(b):
    rows=[list(b)]
    while len(rows[-1])>1:
        rows.append([(a+c)/2 for a,c in zip(rows[-1],rows[-1][1:])])
    return tuple(r[0] for r in rows),tuple(r[-1] for r in reversed(rows))

def quota_cover(model,depth_limit=60,node_limit=20000):
    todo=[(0,0,model['poly'])]
    leaves=[]
    visited=0
    maxdepth=0
    while todo:
        dep,idx,pp=todo.pop()
        visited+=1
        maxdepth=max(maxdepth,dep)
        # Strict positivity of EVERY Bernstein coefficient.
        roots=[i for i,rows in enumerate(pp) if all(min(b)>0 for b in rows)]
        if len(roots)>=2:
            leaves.append([dep,idx,roots[:2]])
            continue
        if dep==depth_limit or visited>=node_limit:
            return dict(proved=False,visited=visited,pending=len(todo)+1,
                        maxdepth=maxdepth,failed=[dep,idx],leaves=leaves)
        ll=[[] for _ in pp]
        rr=[[] for _ in pp]
        for i,rows in enumerate(pp):
            for b in rows:
                a,c=half(b)
                ll[i].append(a)
                rr[i].append(c)
        todo.extend([(dep+1,2*idx+1,rr),(dep+1,2*idx,ll)])
    leaves.sort(key=lambda v:F(v[1],2**v[0]))
    right=F(0)
    for dep,idx,rr in leaves:
        assert F(idx,2**dep)==right
        right=F(idx+1,2**dep)
    assert right==1
    return dict(proved=True,visited=visited,pending=0,
                maxdepth=maxdepth,leaves=leaves)

def at(model,t):
    return [add(a,mul(t,b)) for a,b in model['pts']]

def value(coeff,t):
    return sum(x*t**i for i,x in enumerate(coeff))

def support_identity(K,R):
    # Certify the support planes on the ENTIRE positive ray.
    one=at(R,F(1))
    g=tuple(value(p,F(1))/value(R['volume'],F(1)) for p in R['moment'])
    full=[(p,b) for p in K['points'] for b in [(F(0),)*3,D]]
    for f in R['faces']:
        q0,q1,q2=[one[i] for i in f[:3]]
        n=cross(sub(q1,q0),sub(q2,q0))
        assert dot(n,sub(g,q0))<0
        a,b=R['pts'][f[0]]
        for c,d in full:
            assert dot(n,sub(a,c))>=0
            assert dot(n,sub(b,d))>=0
        for i,(c,d) in enumerate(R['pts']):
            z=(dot(n,sub(a,c)),dot(n,sub(b,d)))
            assert z==(0,0) if i in f else z[0]+z[1]>0

def run_case(name,d,ts,folder,prefix,expected_leaves):
    global D
    D=tuple(map(F,d))
    out=Path(folder)
    out.mkdir(exist_ok=True,parents=True)
    source=points(name)
    K=audit(source,name)
    R=ray_model(K)
    support_identity(K,R)
    cap=max(range(K['F']),key=lambda f:len(K['faces'][f]))
    n=K['planes'][cap][:3]
    capset=frozenset(K['points'][i] for i in K['faces'][cap])
    assert dot(n,D)<0
    labels0={p:i for i,p in enumerate(source)}
    N=K['V']
    labels=[(labels0[K['points'][i%N]],int(i>=N)) for i in R['ids']]
    print('ARCHITECTURE',name,R['k'],len(R['pts']),len(R['edges']),len(R['faces']),flush=True)
    for t in ts:
        p=at(R,t)
        A=audit(p,prefix+'_t_'+str(t))
        assert (A['V'],A['E'],A['F'])==(len(p),len(R['edges']),len(R['faces']))
        assert A['E']<=249
        assert max(map(len,A['faces']))==len(capset)
        assert capset in {frozenset(A['points'][i] for i in f) for f in A['faces']}
        # Equality with conv(all original rows, all translated rows).
        for old in source:
            for q in [old,add(old,mul(t,D))]:
                assert all(dot(f[:3],q)<=f[3] for f in A['planes'])
        assert A['volume']==value(R['volume'],t)
        assert all(A['moment'][k]==value(R['moment'][k],t) for k in range(3))
        assert A['additional_weak']==A['primitive_zero']==[0,0,0]
        amap={v:labels[i] for i,v in enumerate(p)}
        A['material_U']=[amap[A['points'][i]] for i in A['U']]
        A['material_S']=[[amap[A['points'][i]] for i in A['faces'][f]] for f in A['S']]
        A['material_H']=[[amap[A['points'][i]] for i in e] for e in A['H']]
        write_json(out/('t_'+str(t).replace('/','_')+'.json'),A)
        print('EXACT',name,str(t),A['V'],A['E'],A['F'],A['strict'],
              A['additional_weak'],A['primitive_zero'],
              'P',[float(b['depth']) for b in A['P_bars']],
              'Q',[float(b['depth']) for b in A['Q_bars']],flush=True)
    C=quota_cover(R)
    assert C['proved'] and C['pending']==0
    assert len(C['leaves'])==expected_leaves
    C.update(direction=D,labels=labels,volume_coefficients=R['volume'],
             moment_coefficients=R['moment'])
    write_json(out/'cover.json',C)
    print('STRICT_U2_ALL_POSITIVE_T',name,C['visited'],C['maxdepth'],len(C['leaves']),
          [(dep,i,[labels[v] for v in vs]) for dep,i,vs in C['leaves']],flush=True)

EXPECTED_FILES={
'ray30/t_1_1000.json':(20625,'5cc11376a0e348b49ba6ab8a4502297265e4c06b58566e9ca7a45b116188a7c8'),
'ray30/t_1_100.json':(36566,'b76291369d2d81e2f4a7d8f55cc8209383e5976db206c94e75ecdeeb5e9c78c8'),
'ray30/t_1.json':(30513,'7debe5c92f6bba9f9d02dbb04b359b9fd3f2cca4fd8b5a65539811272eb71760'),
'ray30/cover.json':(1347,'1e95903cd40c1961ae41d4b43b3b3b9ed3ebd93f1d8870f4e5afb85c3fde45d8'),
'ray18/t_1_10000.json':(21477,'d5eb798567084f4d333ec0f05eb8d959b741719118e66aa0868153b75221aef9'),
'ray18/cover.json':(1213,'1822c309f6f0f85331fe1196c2783bc50d0d3fa6cc613fc49f6b9a7cff522f09')}

def main(out):
    out=Path(out)
    out.mkdir(exist_ok=True,parents=True)
    inp={name:points(name) for name in ['JOINT56_L18','JOINT56_L30']}
    write_json(out/'inputs.json',inp)
    run_case('JOINT56_L30',(F(511,1000),F(308,1000),F(-803,1000)),
             [F(1,1000),F(1,100),F(1)],out/'ray30','RAY93',3)
    run_case('JOINT56_L18',(F(1),F(0),F(0)),
             [F(1,10000)],out/'ray18','RAY18',2)
    for path,want in EXPECTED_FILES.items():
        raw=(out/path).read_bytes()
        assert (len(raw),hashlib.sha256(raw).hexdigest())==want,path
    print('FINCH93_EXACT_RAYS_PASS_NO_110',flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',default='finch93_verified')
    a=ap.parse_args()
    main(a.out)

# The double-flap construction uses the same verified exact auditor.
r=sys.modules[__name__]

def flaps(m1=12,m2=13):
    p=r.points('JOINT56_L30')
    K=r.audit(p,'JOINT56_L30')
    cap=max(range(K['F']),key=lambda f:len(K['faces'][f]))
    cn=K['planes'][cap][:3]
    ns=[tuple(r.F(x,max(map(abs,z[:3]))) for x in z[:3]) for z in K['planes']]
    pc={q:i for i,q in enumerate(K['points'])}
    items=[]
    newplanes=[]
    side=[]
    dirs=[]
    for (aa,bb),m in zip([(13,22),(70,6)],[m1,m2]):
        a,b=p[aa],p[bb]
        e=r.sub(b,a)
        fs=[i for i,f in enumerate(K['faces']) if pc[a] in f and pc[b] in f]
        assert len(fs)==2 and cap in fs
        adj=next(i for i in fs if i!=cap)
        side.append(adj)
        n=r.add(ns[cap],ns[adj])
        u=r.cross(n,e)
        if r.dot(cn,u)>0:
            u=r.mul(-1,u)
        u=r.mul(r.F(1,max(map(abs,u))),u)
        assert r.dot(cn,u)<0
        assert r.dot(ns[adj],u)>0
        assert r.dot(n,u)==0
        dirs.append(u)
        newplanes.append((n,r.dot(n,a)))
        for i in range(1,m+1):
            t=r.F(i,m+1)
            base=r.add(a,r.mul(t,e))
            delta=r.mul(4*t*(1-t),u)
            items.append((base,delta,adj))
    witnesses=[]
    for i,v in enumerate(K['points']):
        n=tuple(sum(ns[j][k] for j,f in enumerate(K['faces']) if i in f) for k in range(3))
        h=r.dot(n,v)
        assert all(r.dot(n,q)<h for j,q in enumerate(K['points']) if j!=i)
        witnesses.append((n,h))
    bound=r.F(1)
    for a,u,adj in items:
        inequalities=[(ns[i],r.dot(ns[i],K['points'][f[0]]))
                      for i,f in enumerate(K['faces']) if i!=adj]+witnesses+newplanes
        for n,h in inequalities:
            v=r.dot(n,u)
            gap=h-r.dot(n,a)
            assert gap>=0
            if v>0:
                assert gap>0
                bound=min(bound,gap/v)
    amp=r.F(1,2)
    while amp>=bound:
        amp/=2
    new=[r.add(a,r.mul(amp,u)) for a,u,_ in items]
    for q,(_,_,adj) in zip(new,items):
        assert r.dot(cn,q)<K['planes'][cap][3]
        for i,f in enumerate(K['planes']):
            assert (r.dot(f[:3],q)>f[3])==(i==adj)
    meta=dict(m=[m1,m2],amplitude=amp,bound=bound,directions=dirs,
              side_faces=side,flap_planes=newplanes)
    return p+new,meta

def flap_main(out='flap25'):
    out=Path(out)
    out.mkdir(exist_ok=True)
    p,meta=flaps()
    A=r.audit(p,'NF93_DOUBLE_FLAP25')
    mapping={q:i for i,q in enumerate(p)}
    A['material_U']=[mapping[A['points'][i]] for i in A['U']]
    A['material_S']=[[mapping[A['points'][i]] for i in A['faces'][f]] for f in A['S']]
    A['material_H']=[[mapping[A['points'][i]] for i in e] for e in A['H']]
    assert (A['V'],A['E'],A['F'])==(92,224,134)
    assert A['strict']==[2,2,2]
    assert A['additional_weak']==A['primitive_zero']==[0,0,0]
    assert sorted(A['material_U'])==[6,70]
    assert sorted(sorted(e) for e in A['material_H'])==[[13,22],[90,91]]
    assert sorted(map(len,A['faces']),reverse=True)[:3]==[26,15,14]
    assert meta['amplitude']==r.F(1,1024)
    r.write_json(out/'audit.json',A)
    r.write_json(out/'meta.json',meta)
    expected={
      'audit.json':(24690,'5c69b37212fa14bc9290f939c3d8796da96a47d22f252cfeccffc86963f59724'),
      'meta.json':(448,'73e3be02b02ccc0a0400bd7ddfe9e84de5724e37d5b5b0b3076dc5adf64e0cf0')}
    for name,want in expected.items():
        data=(out/name).read_bytes()
        assert (len(data),r.hashlib.sha256(data).hexdigest())==want
    print('DOUBLE_FLAP25',A['V'],A['E'],A['F'],A['strict'],
          A['additional_weak'],A['primitive_zero'],
          'maxfaces',sorted(map(len,A['faces']),reverse=True)[:4],
          'U',A['material_U'],'S',A['material_S'],
          'amp',str(meta['amplitude']),
          'P',[float(b['depth']) for b in A['P_bars']],
          'Q',[float(b['depth']) for b in A['Q_bars']],flush=True)
    print('FINCH93_DOUBLE_FLAP25_PASS_222_NOT_110',flush=True)

if __name__=='__main__':
    flap_main()
```
