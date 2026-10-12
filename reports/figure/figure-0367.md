# figure-0367

AI research report · 2026-09-15 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Nimble Harbor72 — перестройка критической области с внутренней компенсацией массы и точное ограничение на её выход

## 1. Итог

**Нового own-volume-centred strict110/weak000 с C<624 не получено. Положительный уровень C624 не изменяется.** Построен новый конечный рациональный многогранник **NH72_PAIR99_CRITICAL12_LOCAL_MASS_R12**: фактические **V173/E309/F138**, бюджет **2E=618**, собственный строгий класс **(4,6,8)**, weak-only000. Он прошёл два независимых полных точных аудита, отдельное центрированное интегрирование и завершённый source-only cold replay.

В отличие от родителя, компенсация здесь выполняется изменением самой критической области: меняются10 физических вершин и7 её опор, а обе удалённые компенсирующие крышки возвращены к тождественному положению. Восемь прежних кап-индуцированных стабильных равновесий исчезают; остаются три другие дополнительные стабильные грани и пять дополнительных U. Это новый механизм перераспределения материала, не решение110.

Главный точный результат шире прежних frozen-star исключений: **все10 внутренних вершин этой области можно перемещать произвольно**, включая изменение критического конуса124. При сохранённом внешнем интерфейсе и указанной области собственного центра/метрики область всё равно не может вывести все радиальные траектории к апексу. Необходимы как минимум12 строгих звеньев, тогда как существующий граф допускает не более10, а произвольная его внутренняя перестройка с не более10 внутренними вершинами — не более11. Это ограничение конкретного интерфейса, не глобальное исключение C<624.

## 2. Источник и различие объектов

Координатный источник — **COORD_CAP_RL_C624_STRONG_G8, S8**, а не COORD_TRIPLE_C624_OWN121_G14, FINCH_SEQUENTIAL_C618 или F49_50. Полный BASE_GENERATOR.json9599 байт с SHA-256 `bf9fdaf05231ceb11fba9fde10c8a638e664b52233b2da5cb11977b2f4ff27b2` включён в новую капсулу. Сначала восстанавливаются все137 опор S8 с прежним anchor137; затем **явно удаляется исходная H-строка99**. Поле active_ids не заменяет фильтрацию.

Получаемый K99 имеет175/309/136, собственный121. Все номера вершин ниже — **декартовы raw-lex номера этого K99 после удаления поддержки99**, не исходные номера вершин S8. Номер вершины99 не означает удалённую поддержку99.

Evidence-parent — `[internal-source-reference]-`, metadata SHA `7e8eda113c99db67ace3bff7aa33826a111440287005131cf80f9803a973b359`. Его23 исходных файла полностью декодированы из буквального payload и побайтово сопоставлены с приложенным архивом. Совпали decoded83582 байта/SHA `03f6c84c0dc60d90d2f5744646d1a855be12a796d1dd6fe5ef1131e00f9be087` и нормализованная base64-строка35068 символов/SHA `da1b64945f3f80c622d10720596c27ab567bd5dd7fe152cde0aeadee4f03ec07`. Родительские929/10,3,11 не переименованы в победителей. 

Байтовое расхождение сохранено явно: rendered Markdown-срез родителя содержит62668 UTF-8 байт и имеет SHA `d9a951e519d769bfd6f9f5dbd1a7d24031014fcc10b13eebe9917743f20bcff0`, отличный от metadata SHA. Равенство этих потоков не утверждается. Координатная капсула и все её исходники совпали; альтернативного геометрического определения не обнаружено. PROVENANCE.json сохраняет обе идентичности.

## 3. Полное определение нового конечного тела

### Исходный корпус

Из точного K99 удалить физические вершины **129 и145**. Удалить эти номера из всех старых максимальных циклов; остальные старые грани сохранить. Добавить наружные треугольники

`[124,149,146]`, метка `PAIR99_CUT_0`,

`[112,124,146]`, метка `PAIR99_CUT_1`.

Это исходный PAIR99-корпус до изменения крышек. Новая операция не сохраняет его старый критический конус.

### Двенадцать точных управляющих приращений

Пусть q_i=n_i/h_i — исходные точные нормали K99 с правой частью1, а P_i — его точные физические вершины. Вектор исходных управляющих координат:

```text
u0=(q72x,q72y,q72z,q73x,q73z,
    P124x,P112x,P112y,P146x,P146y,P148y,P149x).
```

Прибавить к нему следующую полную целую строку, делённую на **10^14**:

```text
[-820002103986,-1548086488676,-112992330957,
 1089876949456,-1127081554446,844574678379,
 558751400795,-514007562035,-45599803363,
 29336576723,7513593536,-25355875470]
```

В PARAMETERS.json это эквивалентно control_denominator=10^12 и control_scale=1/100. Обозначение R12 относится к сетке приращений поисковых координат, не к знаменателям окончательных физических вершин.

Точная реконструкция:

- q72 получает первые три новые координаты. У q73 задаются x,z, а y решается из **q73·P69=1**.
- X106 — пересечение опор15,71,72; X109 —15,72,75; X114 —17,71,73; X117 —71,72,73; X120 —3,72,73.
- У X124 свободна x, остальные координаты решаются по3,72. У X112 свободны x,y, z решается по75. У X146 свободны x,y, z решается по80. У X148 свободна y, остальные координаты решаются по69,80. У X149 свободна x, остальные координаты решаются по3,69.

Все остальные оставшиеся вершины имеют исходные координаты K99. Обе крышки тождественны, физическая A=I. Для каждой максимальной грани выводится рациональная плоскость по трём её вершинам, проверяются точная планарность полного цикла и строгие зазоры всех неинцидентных точек. После этого оба независимых аудитора заново восстанавливают пересечение полупространств, а не принимают заданную сетку за результат.

Относительно некомпенсированного PAIR99 изменены ровно

`[106,109,112,114,117,120,124,146,148,149]`

и опоры

`[44,72,73,81,100,PAIR99_CUT_0,PAIR99_CUT_1]`.

Относительно **компенсированного PAIR99_R120** изменены23 вершины: эти10 плюс13 возвращённых точек крышек

`[0,2,83,85,87,91,93,96,98,102,105,110,113]`.

Поэтому прежняя предпосылка о неизменённых P124, support44 и PAIR99_CUT_0 здесь действительно нарушена. Полные карты обеих сравнительных нумераций и изменённых supports сохраняются в REPORT.json.

## 4. Настоящий заполненный объём и полный ценз

Фактически восстановлены **173 крайние вершины,309 настоящих рёбер и138 максимальных граней**; все138 неравенств активны.342 треугольника используются только для интегрирования и не объявляются физическими гранями.

В исходных метках K99:

```text
S supports = [3,71,72,81]
размеры этих граней = [18,12,5,3]
U vertices = [95,114,124,146,148,149]
H edges = [[106,117],[109,124],[114,117],[118,146],
           [124,146],[146,148],[148,149],[149,150]]
weak faces/vertices/edges = [] / [] / []
```

Все **1236** реберных примитивов ненулевые. У каждого настоящего ребра проверены оба условия положения линейной проекции на отрезке и оба коэффициента инцидентного нормального конуса. Нулевые счётчики сторон граней и максимальных вершинных выходов также равны0. H=8 не выводится лишь из Эйлера.

Контрольные приближения:

```text
V ≈ 0.4889525117874195
M ≈ (-0.00612837030201649,
      0.003070548539166089,
     -0.004346355723883533)
g ≈ (-0.012533671786680389,
      0.006279850220916879,
     -0.008889116262016843).
```

Полные точные дроби выдаются A/B. Для действительных наружных треугольников используются конечные рациональные выражения `V=Σdet(a,b,c)/6`, `M=Σdet(a,b,c)(a+b+c)/24`, `g=M/V`. Новое тело предъявляется после вычитания **именно этого собственного g**.

Относительно исходного собственного центра c0 тела K99 точно проверено `||g−c0||∞<10^−12`; значение приблизительно **6.558895478649486·10^−15**. **Равенство g=c0 не заявляется.** Приближённое моментное замыкание достаточно близко для исследования механики, но не подменяет точную собственную центровку. После неё третье независимое целочисленное интегрирование342 положительных тетраэдров даёт тот же объём и первые моменты **точно[0,0,0]**.

Максимальные битовые длины:

|Данные|Числитель/знаменатель либо целый максимум|
|---|---:|
|Примитивные H-коэффициенты|848|
|Сырые вершины|439/440|
|Объём|22778/22779|
|Сырые первые моменты|45209/45217|
|Собственный сырой центроид|45209/45216|
|Центрированные вершины|45218/45220|
|Общий центрированный знаменатель|45454|

Это не одновременное улучшение всех арифметических показателей: H сложнее родительского PAIR99_R120, тогда как сырые и центрированные координаты существенно короче его609/613 и54440/54441 бит. 

### Полные бассейны

Заново построенные графы настоящих рёбер дают глобальный primal-корень95; до него достигают28 вершин, остальные **145** образуют замкнутый нежелательный бассейн с **67** граничными рёбрами. Полярный глобальный корень — original support3. Замкнутый нежелательный полярный бассейн содержит **11** supports:

`[16,18,44,71,72,81,94,117,119,129,PAIR99_CUT_1]`.

Его граница содержит30 пар соседних supports. Используются полюса относительно собственного физического центра, не центроид полярного объёма. Уменьшение полярного бассейна со105 до11 не названо близостью к110: дополнительные U возросли, а следующий точный результат препятствует выходу всего критического участка.

## 5. Новое ограничение: все внутренние точки могут двигаться

Пусть критическая область содержит10 внутренних вершин

`J=[106,109,112,114,117,120,124,146,148,149]`.

Её внешний интерфейс фиксирован в точках

`[69,99,111,115,118,123,150]`.

Вход — u=P111, выход — z=P150. Внешние соседи входа69 и107 дают строго отрицательные радиальные переходы. Остальные возможные выходные якоря

`LOW=[69,99,115,118,123]`

имеют квадрат радиуса строго меньше радиуса входа. Все эти знаки доказаны точно с запасом в областях центра и метрики ниже.

Дополнительно сохраняются апекс P95 и три его поддерживающие плоскости с исходными метками **[0,2,35]**. Их положительная точная нормальная комбинация удостоверяет отдельную строгую U. Изменения крышек разрешены, пока эти плоскости остаются поддерживающими и не создаются новые внешние выходы из рассматриваемого интерфейса.

### Энергетическая необходимая оценка

Для любой строгой восходящей цепи из n рёбер между u и z, при собственном центре c и положительно определённой физической метрике G=AᵀA:

`|z−c|_G²−|u−c|_G² > Σ|e_i|_G² ≥ |z−u|_G²/n`.

Первое неравенство следует из тождества приращений квадратов радиусов, второе — из Коши. Поэтому необходимо

`n (|z−c|_G²−|u−c|_G²) > |z−u|_G²`.

При c=c0,G=I точные рациональные величины имеют readouts:

```text
D = |z−u|² ≈ 0.12246151176913979
Delta = |z−c0|²−|u−c0|² ≈ 0.010926949212751523
11 < D/Delta ≈ 11.207292116470144 < 12.
```

Следовательно, нужно **не менее12 строгих звеньев**. Это необходимая нижняя граница, не доказательство достаточности12 и не построенная12-звенная цепь.

Полный точный перебор существующего графа даёт18 простых вход-выходных путей и максимальную длину **10 рёбер**. Один из максимальных:

`111→114→117→120→124→109→112→146→148→149→150`.

Даже **произвольная внутренняя смена рёбер и сокращение вершин** при не более10 внутренних точках разрешает не более11 звеньев простого пути. Строго восходящий путь не может повторить вершину. Через LOW он выйти не может из-за меньшего радиуса; прямые внешние выходы входа отрицательны; выход150 исключён энергетической оценкой. Поэтому путь заканчивается внутри J∪{111} в дополнительной слабой или строгой U, отличной от отдельного строгого апекса95. **Strict110/weak000 исключён при этих предпосылках.**

Это не frozen-star доказательство для неподвижного124: положения всех10 внутренних вершин и их нормали могут меняться произвольно.

### Точные области действительного собственного центра

Для сохранённого графа, G=I, достаточно `||c−c0||∞<rho10`, где

`615129628/10^12 < rho10 < 615129629/10^12`.

Для произвольной внутренней перестройки с не более10 вершинами, тем же внешним интерфейсом и отсутствием новых внешних выходов достаточно меньшего куба:

`96016170/10^12 < rho11 < 96016171/10^12`.

Полные рациональные радиусы и все запасы воспроизводятся ENERGY_CERT.py. Они учитывают не только энергетическую разность, но и радиусы LOW, два внешних выхода111 и строгий апексный конус.

Также доказаны совместные области центра и физической метрики:

```text
Сохранённый граф:
||c−c0||∞ ≤ 1/100000,  max_ij |Gij−Iij| ≤ 1/1000.

Произвольная внутренняя перестройка с ≤10 вершинами:
||c−c0||∞ ≤ 1/1000000, max_ij |Gij−Iij| ≤ 1/10000.
```

G симметрична; эти интервалы сами обеспечивают положительную определённость. c — собственный центр заполненного тела **до** линейного A; после A он равен Ac. Никакой свободный reference centre не подставляется. Каждая граница проверена положительными рациональными остатками, сохранёнными в сертификате.

Изменение входа111, выхода150, других якорей, внешней связности, числа внутренних точек, апексных опор либо выход за указанные области снимает соответствующие предпосылки. Для таких изменений никакого глобального запрета не доказано.

## 6. Реально выполненные поиски и их границы

Последовательно расширены шестикоординатная и двенадцатикоординатная карты критических опор, с отдельными вариантами двух физических крышек, собственной массы и физической метрики. Завершены4 старта/16 внешних состояний reference6 и8 стартов/48 состояний reference12, без принятого110. Guarded SLSQP остановился на лимите700 итераций с нарушенным ограничением: это не допустимый endpoint и не сертификат невозможности.

Поиск local_mass с тождественными крышками завершил первое предложение и дал использованные12 координат. Комплексно-шаговые производные учитывают настоящие V,M,g изменённого тела; полная контрольная точка сохранена. Её точное ties-to-even округление воспроизвело буквальные PARAMETERS с наблюдённым `EXACT_R12_PARAMETERS_FROM_COMPLETE_FROZEN_PROPOSAL_PASS`.

Новый компенсированный сдвиг именно вершины124 прошёл31 конечную оценку; s=1 вырожден и не принят как отдельный endpoint. Это не повтор старого сдвига145. Поиски two_roots и free_metric остались **частичными**: наблюдены1 из30 и2 из5 завершённых стартов соответственно; окончательных маркеров полного поиска нет. Их нельзя объявлять полностью отрицательными сериями.

Все материально использованные программы, помощники, параметры, seeds, завершённые и прерванные статусы включены в RUN_STATUS.json и капсулу. Только полный local_mass checkpoint определял новые рациональные координаты; дальнейший floating replay не нужен для их восстановления. Неуспех конечных численных поисков не используется как доказательство энергетического ограничения.

## 7. Завершённые точные проверки

Аудитор A независимо перечисляет допустимые пересечения троек опор; B независимо обрезает линии пересечения пар. Каждый восстанавливает максимальные грани, настоящие рёбра, заполненную массу и весь строгий/слабый механический ценз. В первом и холодном запусках все четыре нормализованных A/B-записи совпали побайтово. Третья целочисленная масса меняет якоря гранных вееров и подтверждает342 положительных тетраэдра и нулевые центрированные моменты.

Фактически завершён холодный запуск из28 декодированных исходников без сохранённых координат, центроида или отчётов как входных данных. Его завершающий маркер:

`NH72_CRITICAL_DISK_AND_ENERGY_BARRIER_SOURCE_ONLY_COLD_PASS`.

Контрольный тетраэдр strict446/weak000 и контрольная призма strict446/weak123 согласованно отклонены воротами110. Оба аудитора отвергают дублированную H-строку и нулевую правую часть. Assertions должны быть включены.

```text
raw.json:16254 bytes
76a37ee0949e0c76c1d9200c927ba4f48eaab86fd0ae287e3b095350e5d6ce9f

A.json=B.json:254869 bytes
f143be086323d7c5a036fd140586eb69e8ce861a40260e9abd3df8b239b57c29

REPORT.json:292242 bytes
c90fef085900defcb2dbe999c942dc04e5e2fc733c30348773c762d999972ce1

ENERGY_CERT.json:1214211 bytes
efb721bad6ed04bbee85f8c2ffa6e659c3c7de66b71d062ade93264c05bf6c54

Cold RECEIPT.json:1135 bytes
d9d397859f7b56575f4cd7d715ded3e46e6c71710e489bde9e2272c7df45a774
```

Две независимые реализации относятся к полному конечному многограннику. Энергетическое исключение — отдельное аналитическое доказательство с точным рациональным вычислением его предпосылок; две независимые реализации полного непрерывного исключения не заявляются.

## 8. Полная самостоятельная recovery capsule

Включены28 файлов: полный S8-генератор, RECONSTRUCT, оба аудитора, BUILD и CRITICAL, все12 рациональных параметров, полный материальный checkpoint и FREEZE, REPORT с собственной массой/картами/бассейнами, ENERGY_CERT со всеми18 путями и рациональными запасами, REPLAY, MANIFEST/EXPECTED/PROVENANCE/RUN_STATUS и все существенно использованные поисковые программы с помощниками. Никакого старого attachment или внешнего download для восстановления не требуется.

```text
Формат: base64(LZMA(UTF-8 JSON dictionary))
Файлов:28
Decoded JSON:87442 bytes
SHA-256:91a931bdc8b2470fad2b527b5455f2eaf5f1de62524aecb9c3d462f95d308152
Normalized base64:35896 characters
SHA-256:0a45fce544afa3efce761946508184e050a1a80cb31f122d2e582af52f3d4f2b
```

Точный запуск: CPython3.13.5, только standard library. Численные методы: NumPy2.3.5/SciPy1.17.0, BLAS/OMP1. Сохранить декодированное значение result_markdown как result.md и следующий декодер как restore.py:

```python
import base64,hashlib,json,lzma,subprocess,sys
from pathlib import Path
assert __debug__
sys.set_int_max_str_digits(0)
s=Path(sys.argv[1]).read_text(encoding='utf-8')
u=s.split('NH72_CRITICAL_'+'B64_BEGIN',1)[1].split('NH72_CRITICAL_'+'B64_END',1)[0]
u=''.join(u.split())
assert len(u)==35896
assert hashlib.sha256(u.encode()).hexdigest()=='0a45fce544afa3efce761946508184e050a1a80cb31f122d2e582af52f3d4f2b'
b=lzma.decompress(base64.b64decode(u,validate=True))
assert len(b)==87442
assert hashlib.sha256(b).hexdigest()=='91a931bdc8b2470fad2b527b5455f2eaf5f1de62524aecb9c3d462f95d308152'
f=json.loads(b);assert len(f)==28
out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=False)
for name,text in f.items():
    p=Path(name)
    assert not p.is_absolute() and '..' not in p.parts
    target=out/p;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_bytes(text.encode('utf-8'))
subprocess.run([sys.executable,'-B','-S',str(out/'REPLAY.py'),'--out',sys.argv[3]],check=True)
```

Команда: `python -B -S restore.py result.md recovered-source recovered-output`; оба каталога первоначально отсутствуют. Раздельные точные стадии: BASE,BUILD,A,B,REPORT,ENERGY,FINISH. Именно они завершены в холодном исполнении. Необязательное численное продолжение: `python recovered-source/SEARCH_REPLAY.py local_mass recovered-output fresh-search`; это поиск, не сертификат нового тела.

```text
NH72_CRITICAL_B64_BEGIN
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
Z/sCAAAAAARZWg==
NH72_CRITICAL_B64_END
```

## 9. Продолжение

Следующий содержательный шаг должен изменить внешний вход111, выход150, их геометрию или доступную длину внутреннего пути, либо выйти из доказанного собственного центроидно-метрического региона. Повторное повышение точности тех же крышек и тех же10 внутренних точек не устраняет энергетическую преграду. Добавление точек может снять только необходимое ограничение по числу звеньев; физическая выпуклость, бюджет настоящих рёбер и отсутствие полярных рождений остаются отдельными задачами.

Strict110 ниже624, достаточность12 звеньев и глобальная минимальность не установлены. Поиск C<32 не проводился. Новый рациональный468, внутренняя компенсация материала и точное ограничение целого подвижного участка сохранены независимо от дальнейшего исхода.

Дополнительный архив полных источников, точных отчётов, холодного receipt и поисковых записей (`NH72_critical_disk_energy_handoff.zip`):1261181 байт, SHA-256 `f8d02b624b502aa8050eea01a58c02c1376eefb4009c2837bda4ff4718398c92`. Буквальная капсула выше достаточна без ссылки.
