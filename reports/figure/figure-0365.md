# figure-0365

AI research report · 2026-09-14 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Nimble Harbor72 — S8 после удаления опоры: два точных глобальных образа и ограниченная координата собственного центра

## 1. Итог

**Нового однородного strict110 с C<624 не получено. Принятый положительный уровень C624 не изменяется.** Завершены два новых рациональных проективно-метрических образа укрупнённых S8-геометрий. Оба имеют **V175/E309/F136, strict222, weak000**, а не110. Для обоих действительно завершены два независимых полных точных аудита, третье интегрирование заполненного объёма и холодное восстановление из полной капсулы ниже.

Дополнительно закрыт прежний пробел восстановления двух исходных удалений: DEL99 и DEL117 теперь имеют самостоятельное точное определение, полные источники и холодный повтор. Они остаются известными own121, не новыми рекордами. Новые222 не улучшают число равновесий относительно этих121; их ценность — далёкая точная смена носителей при коротких дополнительных данных.

Новый аналитический результат — глобальная координата **c(t), прообраз настоящего собственного центроида**, принимающая все значения внутри исходного укрупнённого K. В отличие от неограниченной координаты b=g(t), её область ограничена самим физическим телом. Получены полный обратный механизм, невырожденный якобиан и исполненный поиск в этой координате с совместной физической метрикой.

## 2. Источник и явные новые рациональные данные

Координатный родитель — исключительно **COORD_CAP_RL_C624_STRONG_G8, S8**. Его шесть буквальных блоков журнала действительно соединены в правильном порядке:59100 base85-символов, SHA `e3c07742531ebe37a1a3332748807c7154f5d7a9c669b57bb78612041dbd1c00`; декодировано170010 байт, SHA `44319c99762df191373664c4e89bbeb7fb70db771c7c38e0a19e4e0ea2645fd3`. Полный S8-генератор9599 байт, SHA `bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2`, включён ниже целиком как BASE_GENERATOR.json. :contentReference[oaicite:0]{index=0}

Аналитический parent `figure-0363`, SHA `c5ea8fda8761454dd25eacd0b1140dd5c53332e513b4b4c09f64617ad11f33d3`, используется для теоремы g:D→R³. Его старый COORD_TRIPLE_C624_OWN121_G14 и два NH72_PM_222 **не являются координатными родителями этой работы**.

Сначала RECONSTRUCT восстанавливает все137 точных неравенств S8, сохраняя исходный anchor137. Затем явно удаляется H-строка99 либо117. Поле active_ids не используется вместо фильтрации: исходный recover его игнорирует. Оба результата — K_j, j∈{99,117}, с действительными175/309/136 и own121. :contentReference[oaicite:1]{index=1}

Для каждого K_j новые сырые физические тела определены как

`Q_j={A_j x/(1+t_j·x):x∈K_j}`,

после чего вычитается **собственный обычный объёмный центроид Q_j**. Плотность равна1 во всём новом заполненном объёме. Все новые параметры имеют общий знаменатель **4**:

```text
NH72_S8_DEL99_PM_D4_OWN222_E309   [case P4_DEL99]
t99 = [-1,1,3]/4
A99 = [[3,4,-4],[0,11,-3],[-1,0,3]]/4

NH72_S8_DEL117_PM_D4_OWN222_E309  [case P4_DEL117]
t117 = [0,9,-3]/4
A117 = [[10,6,4],[-4,2,7],[-2,0,3]]/4
```

Это буквальные рациональные **физические A**, не подразумеваемые численные Cholesky-факторы. Точные detA равны **67/64** и **1**. Рациональная оценка через нормы Фробениуса доказывает κ₂(A99)<13 и κ₂(A117)<27. Вырожденные пределы не приняты.

Для всех физических точек соответствующих K строго доказано:

```text
614063993102/10^12 < min(1+t99·x) < 614063993103/10^12;
19148358250/10^12  < min(1+t117·x) < 19148358251/10^12.
```

Сертификат не ограничивается численным перебором. Точно решено `−t=Σα_k q_ik`, α≥0, Σα<1, для исходных supports **[14,15,71]** и **[25,32,61]** соответственно. Их тройное пересечение точно допустимо по всем136 сохранённым неравенствам и достигает нижней границы `1−Σα`. Полные рациональные α и достигающая вершина восстанавливаются в ADMISSIBILITY.json.

Каждая новая опора из исходной `n_i·x≤h_i` равна

`A^(-T)(n_i+h_i t)·y≤h_i`.

Очищаются все знаменатели и общий целочисленный делитель. Подлинная решётка граней сохраняется, но это также проверено непосредственным независимым восстановлением и точным сопоставлением всех вершин, максимальных циклов и настоящих рёбер.

## 3. Полный конечный ценз и настоящая масса

Все номера supports ниже — исходные метки S8. Номера вершин — декартовы raw-lex метки **соответствующего K99 либо K117 до проективного изменения**, не метки исходного S8 и не прежняя примитивно-полярная нумерация H94.

| Тело | V/E/F | Strict | S supports | U vertices | H edges |
|---|---|---|---|---|---|
|DEL99|175/309/136|121|3|95,145|145–146|
|DEL117|175/309/136|121|3|81,93|81–84|
|P4_DEL99|175/309/136|222|107,124|79,111|44–95;109–115|
|P4_DEL117|175/309/136|222|58,61|83,93|89–93;79–88|

**У всех четырёх weak-only000**, все136 поданных опор активны, все1236 компоненты настоящих рёбер ненулевые. Седла проверены непосредственно по двум условиям положения ортогональной проекции на отрезке и двум коэффициентам инцидентного нормального конуса. Их число не выведено только из S/U или Эйлера. В каждой полной записи также618 проверок сторон граней и полный вершинный ценз; A использует30450 упорядоченных попарных вершинных сравнений.

В новых raw-lex метках P4_DEL99 имеет U=[4,166], H=[[3,98],[82,130]]; P4_DEL117 — U=[0,174], H=[[3,174],[4,11]]. Полные взаимно обратные карты сохранены в DETAILS.json и перепроверены холодным драйвером.

Контрольные приближения — не заменяющие данные определения:

```text
P4_DEL99
V ≈ 0.7741932400351083
M ≈ (0.18140347177054744,0.08862209353286407,-0.15512779568975)
g ≈ (0.23431291102764099,0.11447024973874122,-0.20037348257227774)

P4_DEL117
V ≈ 234.73998738266172
M ≈ (-3721.343263139867,-489.8979437646001,280.3451098013379)
g ≈ (-15.85304363620636,-2.0869812136693704,1.1942793084687908)
```

Полные точные V, три M и g воспроизводятся из буквального генератора и параметров. На действительных наружных интеграционных треугольниках используются `V=Σdet(a,b,c)/6`, `M=Σdet(a,b,c)(a+b+c)/24`, `g=M/V`. Затем третья реализация интегрирует346 положительных центрированных целочисленных тетраэдров, получает тот же объём и **первые моменты точно[0,0,0]**. Никаких поверхностных или точечных масс нет.

Максимальные битовые длины; в дробных столбцах указан максимум числителя или знаменателя:

|Тело|Целые H|Сырые вершины|Объём|Первые моменты|Сырой COM|Центрированные вершины|
|---|---:|---:|---:|---:|---:|---:|
|DEL99|216|440|22238|44355|44354|44358|
|DEL117|216|440|22247|44362|44361|44365|
|P4_DEL99|222|449|24268|48494|48488|48489|
|P4_DEL117|221|449|24459|48908|48908|48910|

Малый знаменатель4 новых физических параметров не означает малых итоговых дробей. Бюджет2E=618 меньше624, но это **не рекорд strict110**. Для дальнейшего strict110 ниже624 допустимо E≤311, то есть здесь остаются лишь два настоящих ребра, не старые бюджеты E314 или H94.

## 4. Что действительно произошло с полными бассейнами

Для каждого конечного тела заново вычислены графы **всех настоящих рёбер** с положительным радиальным выходом и граф соседних физически центрированных полюсов. Полярный объёмный центроид не используется.

|Тело|Замкнутый primal-бассейн вне глобального корня|Его граничные рёбра|Замкнутый polar-бассейн|Его граница|
|---|---:|---:|---:|---:|
|DEL99|144|70|0|0|
|DEL117|126|81|0|0|
|P4_DEL99|70|37|74|22|
|P4_DEL117|167|12|17|17|

В P4_DEL99 глобальные корни — вершина111 и support107. **Все три старых равновесных носителя S3/U95/U145 потеряли прежние равновесия**, хотя сами соответствующие физические грань и вершины сохранились.78 из144 старых нежелательных вершин теперь достигают нового глобального корня. Однако часть старого бассейна остаётся в новом замкнутом компоненте, и родились новые равновесия: полной отмены нет.

В P4_DEL117 глобальный максимум — вершина83, минимальная высота соответствует support58; прежняя дополнительная U81 исчезает как равновесие, а apex93 остаётся другой U. Новый глобальный primal-корень достигается лишь из8 вершин. Меньший polar-бассейн17 не означает близость к110.

Это подтверждается точными перепадами. Для нежелательной U и граничного седла использовано `1−|h|²/|u|²`, для нежелательной стабильной грани — `1−d_f²/|h|²`. В P4_DEL99 все четыре соответствующих перепада **>89/100**, в P4_DEL117 — **>95/100**. Полные рациональные величины и строгие соседние интервалы сетки10^−12 восстанавливаются в DETAILS.json. Остатки глубокие, не численный шум.

## 5. Новая глобальная координата: прообраз собственного центроида

Для укрупнённого K пусть `F_t(x)=x/(1+t·x)`, D — вся область положительных знаменателей, b(t) — настоящий объёмный центроид F_t(K), Σ(t) — его заполненная ковариация. Аналитический parent даёт

`Db=−5Σ−bbᵀ`,  `b:D→R³` — аналитическую биекцию.

Определим

`δ=1−t·b>0`,  `c(t)=b/δ=F_t^(-1)(b)∈int K`.

**Тогда c:D→int K также является глобальным аналитическим диффеоморфизмом.** Его точный якобиан:

`Dc=−5(δI+btᵀ)Σ/δ²`,

`det Dc=−125 detΣ/δ⁴<0`.

Вывод: дифференцировать b/δ и подставить Db; слагаемые bbᵀ сокращаются. Для глобального утверждения возьмём любой c∈int K и L=K−c. По родительской строго выпуклой задаче существует ровно один u, при котором F_u(L) имеет собственный объёмный центр0. Поскольку −c∈int L, число `d0=1−u·c` положительно. Положим `t=u/d0`. Тогда t∈D и

`F_u(x−c)=[(I+ctᵀ)F_t(x)−c]/d0`.

Взятие обычных объёмных центроидов даёт b(t)=d0c и δ=d0, то есть c(t)=c. Обратно, всякий t даёт u=δt с этим свойством; единственность u доказывает инъективность. Невырожденный якобиан завершает аналитическую обратимость.

Это **не право назначить c центром старого K**: c выбирает другую физическую геометрию через единственное решение по u. Функция, минимизируемая при восстановлении u, — настоящий логарифм заполненного проективного объёма L. В капсуле полностью реализован этот обратный алгоритм. Отдельная точная программа проверяет отображающее тождество на каждой из175 вершин всех четырёх объектов, положительность знаменателей и нулевые новые первые моменты через точную аффинную ковариантность массы.

У новых конечных объектов прообразы центров приблизительно

```text
P4_DEL99:  c=(-0.002632061218520104,-0.02609270780181102,-0.2219934355584212)
P4_DEL117: c=(-0.04645254453964577,-0.4119968235022555,0.03886752408651582).
```

Оба строго внутри своего исходного удалённого тела — проверено всеми136 точными неравенствами.

Для физической метрики использована дополнительная полная координатная карта: `Σ=LLᵀ`, `W=det(Σ)^(1/6)L^(-1)`, `A=M W`, где M — верхнетреугольная матрица с положительной диагональю и detM=1. С точностью до несущественных поворота и масштаба сохраняются все пять метрических степеней свободы. Производные учитывают изменение **самой заполненной ковариации**. Численный Cholesky служит только поисковой картой; финальные A заданы рационально выше.

## 6. Что было исполнено и что не доказано

Завершены200 прямых восьмипараметрических стартов и80 стартов с обновляемыми корнедостижимыми лесами;2000 стартов в ковариационно-нормированной карте;1600 стартов с регистрацией промежуточных физических состояний —480915 оценок;400 стартов с явной сменой стабильного и неустойчивого корней. Ни один не дал принятого110.

В новой ограниченной карте отдельно завершены **800 внутренних c-целей**, по400 на каждое удаление, с тремя метрическими стартами на цель. Все800 задач собственного моментного замыкания завершились без отказа. Наибольшая численная ошибка возвращённого c — менее2.0·10^−12. Поиск действительно выходил далеко от единицы: минимальный наблюдённый положительный знаменатель около8.78·10^−5, компоненты настоящего b доходили примерно до1200.35. Это численные диагностические пределы, не точные сертификаты тех временных предложений.

Дополнительно выполнены600 конечных центроидных задач с полуположительно-определёнными метрическими релаксациями;48 смешанно-целочисленных задач в более узких метрических конусах. **Все48 последних остановились по пятиисекундному лимиту без incumbent**, а не с доказанной неразрешимостью.287 дополнительных точно определённых удаляемыми метками подмножеств S8 прошли только численный геометрический экран; там110 также не наблюдался. Они не повышены до точно проверенных endpoint.

Три защищённых локальных продолжения приняли6,7,17 шагов соответственно и не дали110; их остановки не исключают проективный класс. Полные источники, семена, границы, лимиты и сохранённые входные параметры всех этих экспериментов включены. Приоритетный новый метод — глобальные c/b-карты, а не этот локальный отказ.

D4-объекты получены из сохранённых полных предложений413 и118 экспериментов `iso_99_cauchy_none` и `iso_117_cauchy_none`. Их буквальные t,A округлены на сетку1/4 и затем независимо реконструированы точно. Точное восстановление целых параметров из сохранённых десятичных предложений завершилось с маркером `TWO_COMPLETE_FROZEN_PROPOSALS_RECOVER_LITERAL_D4_PARAMETERS_PASS`.

**Ни конечные выборки, ни интервальные лимиты поискового кода, ни отрицательные численные оптимумы не являются исключением полного проективно-метрического семейства.** Глобальность доказана для координатных карт, а не для покрытия алгоритмом всех их точек.

## 7. Завершённый точный и холодный контроль

A независимо перечисляет допустимые пересечения троек опор; B независимо обрезает линии пар опор. Каждый сам строит максимальные грани и истинные рёбра, интегрирует свою массу и выполняет полный strict/weak ценз. Это две программные реализации внутри исследования, не внешнее рецензирование.

Холодный драйвер стартовал в новой папке **только от28 декодированных исходных файлов**. Заново восстановлены оба удалённых тела и оба новых образа, выполнены все восемь полных A/B-проходов, третья масса каждого, полные карты бассейнов и точные обратные сопоставления комплексов. Контроли tetra446/weak000 и призма446/weak123 согласованно отвергнуты воротами110; оба аудитора отвергли нулевой RHS и дублированную строку.

Непосредственно наблюдён маркер:

`NH72_S8_C618_FOUR_NONWINNERS_SOURCE_ONLY_COLD_PASS`.

```text
P4_DEL99 raw.json:12679 bytes
3c4f5fae2157df168d5074b4637e32528d77c5c0e67077b08f087e426f6f12d7
P4_DEL99 A.json=B.json:265282 bytes
ee569b387939ed8b2473209e220bcc4c9384f1a553e00e35c7e9a3f46d6e3adb

P4_DEL117 raw.json:12550 bytes
3abed1e96dbf5cf362316fd382ffb2d51384237551bed1bb816459d578c5d260
P4_DEL117 A.json=B.json:267380 bytes
4c4d346dc7bdc53590f4efa8db1c082b7b9b70deebb044d63b4f4ad50ecb274c

Полный холодный RECEIPT.json:4570 bytes
760192e4879a6498f01ece75b6cd603e5b43c8b996af81f9dcbf681672d23b7b
```

## 8. Полная самостоятельная капсула

Включены **весь S8 BASE_GENERATOR, все точные параметры и selector удаления, реконструктор, оба независимых аудитора, третья масса, бассейны и label maps, проверка ограниченной центроидной карты, все существенно использованные численные программы с помощниками, полные выбранные предложения, параметры поисков, manifest и ожидаемые результаты**. Старые вложения, журнал и внешние downloads для восстановления не нужны.

Формат base64(LZMA(UTF-8 JSON dictionary)): **28 файлов,118588 декодированных байт**, SHA `3ac9a8a2ab883259d9e40753b5d48ba8ce544450d161ebbed5a85cd83a76fe53`; нормализованная строка44392 символа, SHA `90696271f17317024576b1d7b5ad4e9f094ed1577188abe28f4080e1c4263962`.

Точное исполнение: CPython3.13.5, только стандартная библиотека, assertions включены. Численное продолжение: NumPy2.3.5/SciPy1.17.0, BLAS/OMP1. Траектории floating solver могут зависеть от платформы; точное восстановление четырёх тел от них не зависит.

Сохранить значение result_markdown как result.md, декодер как restore.py и выполнить:

```text
python -B -S restore.py result.md recovered-source recovered-output
python recovered-source/SEARCH_REPLAY.py pullback99 recovered-output fresh-search
```

Все новые каталоги должны отсутствовать. Первая команда воспроизводит точные проверки. Вторая — отдельный численный поиск, не сертификат нового результата.

```python
import base64,hashlib,json,lzma,subprocess,sys
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
s=Path(sys.argv[1]).read_text(encoding='utf-8')
u=s.split('NH72_S8_'+'B64_BEGIN',1)[1].split('NH72_S8_'+'B64_END',1)[0]
u=''.join(u.split())
assert len(u)==44392
assert hashlib.sha256(u.encode()).hexdigest()=='90696271f17317024576b1d7b5ad4e9f094ed1577188abe28f4080e1c4263962'
b=lzma.decompress(base64.b64decode(u,validate=True))
assert len(b)==118588
assert hashlib.sha256(b).hexdigest()=='3ac9a8a2ab883259d9e40753b5d48ba8ce544450d161ebbed5a85cd83a76fe53'
f=json.loads(b);assert len(f)==28
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in f.items():
    p=Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    target=out/p;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(text.encode('utf-8'))
subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY.py'),'--out',sys.argv[3]],check=True)
```

```text
NH72_S8_B64_BEGIN
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
NH72_S8_B64_END
```

## 9. Продолжение

У текущего метода есть глобальная ограниченная физическая координата c∈int K и пять независимых метрических направлений; совместная смена всех прежних равновесных носителей действительно реализована в P4_DEL99. Однако остались глубокие другие бассейны. Следующее содержательное продвижение требует нового finite endpoint с полным собственным цензом, а не уменьшения числа вершин одного бассейна или относительного штрафа при плохой обусловленности.

Новый110, полное исключение этих орбит и глобальная минимальность C не установлены. Два новых222, оба восстановленных121, полный конечный поиск и новая центроидная карта сохранены независимо от последующего результата.

[Дополнительный архив исходников, точных отчётов, холодного receipt и поисковых журналов](sandbox:/mnt/data/NH72_S8_C618_projective_handoff.zip). Буквальная капсула выше достаточна без этой ссылки.
