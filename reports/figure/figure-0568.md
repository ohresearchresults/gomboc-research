# figure-0568

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Vivid Nova 40 — конечный выход из второго U-бассейна; собственное110 не получено

Ветвь `[internal-source-reference]`, slot-1. Научный родитель — буквальный R22-B7, `figure-0566`, SHA-256 `1dd2a815454fdcdf5442f539f13181506b8ecd85c884a433f8061ea92c9f08be`.

**Цель own strict110/weak000/E≤249 не достигнута. Получен действительный конечный выход из лишнего нестабильного бассейна R22-B7, с пересборкой поверхности и физическим центром: сохранены14 точных однородных own211-потомков. Среди них V22/E51/F31,C102; это211, не110.** Дополнительно сохранены промежуточное тело12/1/11 и намеренно не замаскированный222-контроль. Все16 новых тел имеют additional-weak000 и primitive-zero000.

Одностороннее211 уже встречалось в журнале; я не объявляю сам этот класс новым открытием. Новое выполненное продолжение здесь — самодостаточная цепочка именно от R22-B7, уменьшение до22 вершин/51 ребра, реальное освобождение18-грани в отдельном потомке, новые стабильные носители и точный211 на общей координатной сетке10^-6 с62-битным знаменателем центра. Глобальная минимальность или превосходство над всем недоставленным архивом не доказаны. Каноническое собственное110 этой работой не заменяется.

## 1. Прочитанный пакет и источник полномочий

Прочитан весь единственный фрагмент задания, полные первичный J75-источник и файл методов, а также весь1278-строчный журнал, включая полный неизменяемый родительский payload и оба его исходника. Проверены буквальные байты:

| Вход | Байты | SHA-256 |
|---|---:|---|
| J75_REFERENCE110_CAP233.py.txt |11412|e16788d0d477fef56c4a8ac979d2b201c9691d0f6ee302939f7699209a740b82|
| J75_NOMINATION_METHODS_AND_RECOVERY.md |13734|a37a9ae91b2d2ec323564eb74c6c3c7954a18403c587e1da7245f37312b84d74|
| research-journal(20260926-212651).md |119416|f5b9358108e0b4ebaa571d545f4f5bd6e35dd062b7c09c21ea3265f92552f814|

Родительский SHA воспроизведён сериализацией его полного Markdown в компактный JSON `{version:2,result_markdown:...}` с UTF-8 и одним конечным LF в Markdown. Конфликта буквального родителя с выбранным J75-checkpoint не обнаружено. Воспроизведён `J75_REFERENCE110_CAP233_EXACT_PASS` с указанными в поставке хешами parent/cap/report. Это именно R22-B7 с объёмом1546682134640604290783573/1200000000000000000000000 и собственным центром приблизительно(-.1933531024991415,-.1335206170323686,-.14312371015614422), не L18/F18.

Недоставленные исходники J71/J72, FULL76 и старый optimizer workspace не объявлялись доступными и не использовались как численные входы. Исторический пробел общего архива, описанный в журнале, не устранён. Все новые доказательные входы и методы находятся в капсуле ниже; research MCP, планировщик и журнал не использовались и не изменялись.

## 2. Полный каталог новых точных endpoint

Десятичные глубины — приближения. В отчётах восстанавливаются полные рациональные birth/death/depth, компоненты, cuts и attaining paths. Пустой P здесь означает отсутствие всех положительных P-баров, а не глубины ниже порога. Обозначения G3/G4/G7/G8 относятся к параметрической рационализации; окончательная общая сетка может быть мельче из-за точного уравнения плоскости.

| Имя в DATA | V/E/F | strict S/U/H | C=2E | Все P | Q |
|---|---:|---:|---:|---|---|
|`V49_U1_G7`|49/126/79|12/1/11|252|∅|11 баров; max 0.497982082923513|
|`V48_211_G7`|48/123/77|2/1/1|246|∅|0.5067715665072031|
|`V46_211_G7`|46/117/73|2/1/1|234|∅|0.3609636828649262|
|`V47_FREE211_G8`|47/135/90|2/1/1|270|∅|0.3367461055964542|
|`V46_211_G4`|46/117/73|2/1/1|234|∅|0.3662542845755203|
|`V46_211_G5`|46/117/73|2/1/1|234|∅|0.3662111858696296|
|`V49_211_G4`|49/126/79|2/1/1|252|∅|0.3742748472206271|
|`V49_211_G5`|49/126/79|2/1/1|252|∅|0.3742951779308277|
|`V48_222_G3`|48/123/77|2/2/2|246|1.478341785952544e-06|0.4242531638760701|
|`V48_211_G3`|48/123/77|2/1/1|246|∅|0.4234692543485882|
|`V49_211_G3`|49/126/79|2/1/1|252|∅|0.5013460868494878|
|`V36_211_G8`|36/91/57|2/1/1|182|∅|0.5843416202415197|
|`V24_211_G8`|24/57/35|2/1/1|114|∅|0.896478577662301|
|`V23_211_G8`|23/54/33|2/1/1|108|∅|0.9248054458770236|
|`V22_211_E52_G8`|22/52/32|2/1/1|104|∅|0.9481868033276482|
|`V22_211_E51_G8`|22/51/31|2/1/1|102|∅|0.9475099103276099|

Полные11 положительных Q-глубин промежуточного `V49_U1_G7`:

```text
0.49798208292351304
0.0029029246365712973
0.0006687577901093999
0.0005393637914143449
0.0004606060484656798
0.00034792486524217576
0.0002541929434943108
0.0001933840311274041
0.000022476465858327876
0.000014485814467921198
0.0000019772624486662336
```

Два наиболее полезных различных входа для дальнейшего уничтожения Q — `V46_211_G4` и `V47_FREE211_G8`. Первый имеет более простую арифметику и меньший E; второй — меньшую оставшуюся глубину и уже не сохраняет18-грань. `V22_211_E51_G8` сохраняется как существенный запас сложности, но его Q≈.94751 велик: это не близость к110, измеренная числом рёбер.

## 3. Что действительно изменилось в геометрии и массе

Первая цепочка дала75/204/131,222 →49/126/79,12/1/11 →48/123/77,211. В первом чистом211 объём равен приблизительно1.6998526443344144, то есть1.3188380000750977 родительского объёма; собственный центр равен приблизительно(-.4450038753091847,-.1283509322060524,-.10551219532864468). Его infinity-смещение от центра R22-B7 составляет.2516507728100432. Это физическое изменение всего однородного hull, не перенос начала координат и не заданная плотность.

На ключевых211-потомках материальная вершина62 всё ещё является настоящей вершиной, но уже не U. Единственный U — материальная6. Для каждой прочей вершины точный отчёт строит положительный исходящий radial witness и конечный путь к6. Поэтому установлено исчезновение лишнего U-бассейна в endpoint, а не только исчезновение старой метки62 или её миграция в58/69. Старые фиксированные anchors/fans и малые дрейфы не сохраняются; численные множества недоставленных старых сертификатов для этого вывода не нужны.

У `V46_211_G4` настоящие S — треугольник[2,53,3] и18-грань, U=[6], H=[6,69], в исходных материальных индексах R22. Старый стабильный треугольник[14,16,24] уже не является носителем. Объём4498245989213877/2500000000000000; центр:

```text
(-985229863659472818181/2159158074822660960000,
 -419182476101091735735287/3598596791371101600000000,
 -2744623152864165781/29988306594759180000)
```

Общий координатный знаменатель равен50000000, максимальные битовые длины числителя/знаменателя центра79/82; у исходного R22 они115/118.

У `V47_FREE211_G8` все90 максимальных граней треугольные. **Старая18-грань действительно исчезла**, а не была пересчитана как18 интеграционных треугольников. S=[2,59,6] и[2,53,3], U=[6], H=[6,69]. E=135 и Q=.33674610559645424. Центр приблизительно(-.4611816358774645,-.12095591720524396,-.08886725576811118).

У `V22_211_E51_G8` максимальные грани —30 треугольников и один12-угольник. Большая12-грань **не стабильна**. S=[6,41,64] и[2,66,3], U=[6], H=[6,73]. Объём2320131542727992515433137683831377/3000000000000000000000000000000000≈.7733771809093308; центр приблизительно(-.4537138803263231,-.1472122111838545,-.16118941340349177). Объём составляет.6000280188836891 родительского. Это другой устойчивый носитель и другой интерфейс, не сохранение старого18-гранного stable root.

Материальные индексы нельзя заменять компактной нумерацией hull: например, у последнего тела компактный U5 — исходный материальный6. Поле `source_material` в новых точных отчётах восстанавливает соответствие, включая случаи совпадающих удалённых внутренних строк.

## 4. Исполненный производящий механизм

Сначала использована согласованная неаффинная полиномиальная деформация всей75-точечной поверхности. При X=x-cx, Z=z-cz, W=y+.272x+.409z+.68526367 берутся все мономы суммарных степеней2 и3. Для каждой степени есть x/z-моды с компенсирующим y-смещением, сохраняющим W=0, и нормальные y-моды, делящиеся на W. Получается41 коэффициент, каждый базисный столбец нормирован максимальным модулем координаты; bounds[-.8,.8], нулевой seed, L-BFGS-B1400 итераций, loss=sum(P)+.001sum(Q). Это не общий affine/projective поиск. При каждом вычислении заново строится текущий hull и интегрируется его собственная масса.

Затем применён ремонт всех нежелательных roots. Для текущего центрированного вектора v и соседнего w используется

`score(v,w)=v·(w-v)/(|v| |w-v|)`.

Каждая невыбранная корневая вершина выбирает лучший текущий исходящий witness; loss суммирует квадраты недостающего положительного запаса. Для полярных векторов q=n/[n·(p-c)] та же конструкция контролирует стабильные равновесия primal. Сначала допускается один primal-root, затем один primal и два polar-roots. Полный центр c остаётся функцией действительной поверхности, не независимой переменной.

Ключевой исполнимый вариант карты задаёт внутренние относительно большой плоскости вершины как `y=a*x+b*z+d+exp(h)`, а точки плоскости — двумя координатами и общими a,b,d. Положительная высота сохраняет опорную сторону, но не старую триангуляцию, не старые звёзды и не физический центр. Эта карта сконсолидировала11 Q-баров промежуточного тела в один. Последующий Q-спуск штрафовал новые primal/polar roots; после конечных шагов снова выполнялся ремонт. Отдельный свободный запуск снял саму плоскостную параметризацию и дал полностью треугольный V47-потомок.

Далее исполнено удаление действительных вершин с повторным ремонтом. Удаляемая материальная строка помещается во внутреннюю точку тела либо внутрь сохраняемой плоской грани; затем заново строятся hull, масса и все witness-соседства. Цепочка дала в частности36/91/57,24/57/35 и23/54/33. Два22-вершинных результата были отброшены численным условием достижения запаса1e-4, но **спасены последующим точным аудитом**: положительный solver loss не означает отсутствие strict211. Для E51 он был около2.03623e-8, однако все точные знаки endpoint строгие. Это не доказательство невозможности следующего удаления и не доказательство минимальности22.

Отдельный арифметический контроль важен: округлённый `V48_222_G3` действительно имеет новый U69 и P=1.4783417859525436e-6. Единственная целочисленная поправка материальной69, `(481,-44,63)/1000 → (481,-44,62)/1000`, при неизменной плоскости `y=-269x/1000-79z/200-137/200` даёт `V48_211_G3`. Его все P исчезают точно; Q=.4234692543485882. Общий координатный знаменатель1000000, максимальные битовые длины центра59/62. Старый222-контроль сохранён отдельно.

## 5. Что проверено и что не доказано

Qhull только номинирует тройки. Каждая опорная плоскость проверяется на всех рациональных точках целыми знаками; затем строится точный максимальный многоугольник. Проверяются два противоположно ориентированных владельца каждого истинного ребра, связность граней и Euler2. Неполная номинация вызывает остановку. Никакой старый комплекс для новой массы не используется. Этот тип проверки полноты соответствует поставленному родительскому аудитору.

Для каждого нового тела объём и первый момент пересчитаны с тремя центрами тетраэдрирования: исходным нулём, собственным центром и средним крайних вершин. Для двух внутренних центров все тетраэдры строго положительны, а объём и момент совпадают точно. Все S/U/H, closed-but-not-strict weak и primitive-zero вычисляются рационально. Grouped-level алгоритм сохраняет каждый положительный P/Q-бар, без числового пола. Дополнительно exact forests дают пути от всех не-root векторов к действительным roots: положительный исходящий score строго увеличивает квадрат радиуса, поэтому циклов нет.

Это несколько проверок одной восстановленной вычислительной системы, **не независимые физические движки**. Плавающие пороги в поисковых функциях служат только номинации/печати; они не входят в сертификацию endpoint. Ни непрерывная слабосвободная траектория, ни изолированная последовательность бифуркаций, ни соблюдение бюджета на каждом ненаблюдавшемся промежуточном параметре не доказаны.

Двенадцать дополнительных стадий с одним primal и одним polar root не дали принятого110. Проверенные численные reciprocal-chain cuts также не дали физического110: изменённая масса рождает другие равновесия. Это результаты конечных запусков, не исключения этих семейств. Два дополнительных точных reference110-центра для V46/V47 сохранены в DATA и проверяются отдельно; ни один не равен собственному центру. Они не засчитываются как физический успех, точно так же как reference110 и малый cap233 из J75 не были own110.

## 6. Воспроизводимость и практически полезное продолжение

В новом каталоге заново выполнена производящая цепочка. **Все16 файлов body совпали побайтно с первыми точными endpoint**, включая два спасённых22-вершинных состояния. Наблюдён `N40_ALL_16_COLD_NOMINATED_BODY_HASHES_MATCH`. Это локальная воспроизводимость в указанной среде, не обещание одинаковой траектории плавающего оптимизатора при иных версиях/платформах. Доказательное восстановление не запускает оптимизатор вообще: оно читает полные фиксированные рациональные строки из капсулы.

Среда: CPython3.13.5, NumPy2.3.5, SciPy1.17.0; численный производитель дополнительно torch2.10.0+cpu, float64, один поток. Точные отчёты новой схемы имеют единый `manifest.json`:3630 байт, SHA-256 `92da5c2db47ddaefad5f9ddd3d12811a72092abdf1e4704ba144f1036d78d7f3`. Receipt холодного производителя:1677 байт, SHA-256 `1db0d2bd34b341220f4c79c835d6c032acd6f725a3cde00a3953a1ac897f22b8`. Сравнивать следует хеши body; старые рабочие audit JSON имеют другую схему/индексацию.

Продолжать разумнее от V46_G4 либо уже свободного V47, сохраняя возможность смены roots и исходящих witnesses при контактах. В точном входе теперь есть глобальный однокорневой primal-лес, а нерешённая часть — оставшийся polar/Q-бассейн и его связь с физической массой. Повторное удаление одной метки62 не нужно. V22_E51 — отдельный контроль с большим запасом сложности, но более тяжёлым Q.

Чисто комбинаторно сохранение m-грани даёт E≤3V-m-3. Поэтому добавление точек строго с внутренней стороны18-грани V46 допускает до44 дополнительных материальных точек при E≤249; для12-грани V22 — до66. Это только бюджет, не сохранение census/массы. Точный аудитор допускает произвольное число точек; численный75-строчный chart для добавления новых строк потребуется обобщить.

`N40_METHODS.expand_exact(name)` возвращает75 рациональных материальных строк, восстанавливая отсутствующие как внутренние представители, а `start_exact(name)` — их численную копию для нового поиска. Для всех16 тел проверено побайтное сохранение body после такого расширения: `N40_ALL_EXACT_REENTRY_EXPANSIONS_PRESERVE_BODY_HASH`. Это новый вход из точного checkpoint, не восстановление скрытого состояния L-BFGS.

## 7. Идентичности body

Все следующие хеши относятся к каноническому компактному JSON `{density:1,points:[...]}` с сортировкой ключей, рациональными строками и конечным LF.

| Имя | Байты | SHA-256 body |
|---|---:|---|
|`V49_U1_G7`|3083|`3eb06c6dc90eaa54fd1bee8dfaad4ee3bc3b398b05482f81f45d0b2e4360804c`|
|`V48_211_G7`|3039|`f56ea12bea38f08f4a0e0eba8416c49960724f5b86473c65166ead8698b1d6d9`|
|`V46_211_G7`|2942|`34c423f5d4a1de52501e1959dba7bd84d4be3f5c08b8e946cea2560a66aaca66`|
|`V47_FREE211_G8`|2985|`222e77d0d97b19a45432464c0707b4c30ead746e3dda5d9e43ad9e11c259be42`|
|`V46_211_G4`|1967|`4b95e639c24f8caecfebff9d5fb0fc236686a199167294190c2007c67b6c947b`|
|`V46_211_G5`|2271|`bdde9fb2638a1a235e3e6e5a9f7a2f88e07b88c44ac6cadaa9dee25936d8aa41`|
|`V49_211_G4`|2099|`d9872dd465aa2ff147d9c95ac781b5edd16409b84d325ece4d4a7b27407377d9`|
|`V49_211_G5`|2414|`7e9d71ce94d7769584f35763ae13272c528d8a79dee44b9a7378a881a829a1e1`|
|`V48_222_G3`|1719|`964830d7b70532e2804be9bc2131f8850c0cd6a7d2996ca826c3e537ca078aa9`|
|`V48_211_G3`|1718|`898038ea0c7fe96992aa900e02acbb2fa6ee012d2aeae09c0f456fc80961beb6`|
|`V49_211_G3`|1775|`f4bfea3ecfb3797918b1b0b9140112c949f926db5c2b7f8182c1518735536fd2`|
|`V36_211_G8`|2518|`30473e6bb8927e9e14a7d08b602b30e7b09339204fc9692de65acbe2bffe22bb`|
|`V24_211_G8`|1763|`4b849d38c7fc1fa6bd81d2bd5f0077fa8447d5dde3b9c05b97ae814a43362ef3`|
|`V23_211_G8`|1683|`51e992a8b4700da53bcf5f20a8295210c0a9223d528ff69f39d91b3d12fdcbef`|
|`V22_211_E52_G8`|1628|`b2270c80fcaf3de2f06e81ffdff2216c92b0b499b78eb79372583939a26ba7f1`|
|`V22_211_E51_G8`|1629|`73d03038beeea75928b5a9335dbcc296338e751be2b5bd873d00e950701ee417`|

## 8. Полная самодостаточная исходная капсула

Следующий runnable файл содержит оба полных читаемых Python-исходника как буквальный LZMA/base85-пакет. Внутри находятся все75 строк R22-B7, полные рациональные данные всех16 новых тел, все геометрические/массовые/механические helpers, все параметры численных методов и их драйверы. Это не ссылка на недоставленный архив. После распаковки извлекаются:

| Исходник | Байты | SHA-256 |
|---|---:|---|
|N40_RECOVER.py|36472|79c1bdde8c7f1e70e3d068cb3a1b3f94843f09305aa2987897967d849b288f99|
|N40_METHODS.py|35537|a579bddcb895b00755a54c44f62931405fc30f70f016309785e3573fe0fb6ee3|

Декодированный JSON исходников:73468 байт, SHA-256 `0ccaef5185744cb412efca5dda25232b1081b7a8684629d338e1300d6cf80b4d`. Сам `N40_SOURCE_CAPSULE.py`:30072 байта, SHA-256 `7f488872b6eb69013c74c1f602d09b8b69a54bd4808eb37ea1360c637391e07c`. Сохранить блок с LF и конечным LF.

```sh
python N40_SOURCE_CAPSULE.py N40
cd N40
OPENBLAS_NUM_THREADS=1 python N40_RECOVER.py --out exact
```

Наблюдавшиеся финальные маркеры:

```text
N40_SOURCE_CAPSULE_VERIFIED
N40_COMPLETE_EXACT_REPLAY_NO_110 17
N40_SOURCE_ONLY_RECONSTRUCTION_MATCHED_ALL17
```

Последняя строка получена сравнением manifest с восстановлением в чистом каталоге: совпали все17 точных отчётов/body, включая родителя. Полная численная история, не требуемая для доказательного replay:

```sh
for phase in first q_a q_b q_c robust simplify_a simplify_b simplify_c compare; do
  OPENBLAS_NUM_THREADS=1 python N40_METHODS.py "$phase" --work nomination
done
```

Дополнительные конечные отрицательные/референсные запуски доступны фазами `negative` и `references`; они не нужны для восстановления точных тел.

### N40_SOURCE_CAPSULE.py

```python
"""N40 source-only capsule. All exact inputs and all producer helpers are embedded."""
from pathlib import Path
import base64,lzma,json,hashlib,sys
COUNT=73468
SHA='0ccaef5185744cb412efca5dda25232b1081b7a8684629d338e1300d6cf80b4d'
FILES={'N40_RECOVER.py': (36472, '79c1bdde8c7f1e70e3d068cb3a1b3f94843f09305aa2987897967d849b288f99'), 'N40_METHODS.py': (35537, 'a579bddcb895b00755a54c44f62931405fc30f70f016309785e3573fe0fb6ee3')}
PAYLOAD=r"""
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;U4>0R$Tx+h=s#JjZO8<Sn0~6jXftvDJNq#krx4j1;cs^r;xT#xexoW<1TWe1BbciqwxD;
kVsp;gdffi3JElsW<oNlt)bmM$f^8SY3w7!2HJ|HJUw%+=}r-3jW@XX!^%w=_VI{^KY7<<Mm8XCd#jW78!p&>=GXOrc}3I<%0+T9
497;9(Xw1@x>*n~Dr~r{Eh~{0j7o}4{zMb<gCJ0Zn`hju0|g`$x?f<4bJ2|E&}T{dEy~R}FKH4Kn@*Sy10_BYl=16+3QPp!D&ZgK
%zmUikELsfG`I&!9)Z9Fw$qNr)Hm%1l!6dhfjW~ZU^h+~<NXkd&jB9=`Ivf&iYG?g_6x2~`665ZT$2w(;pK@uoJO}lO%A%sEp$lm
5o^=im=fqWGX~KJmSbeEbYsbhNK?fMm}k4f^5a3-gb??onzrFF!2uFBWuUn+EUB<Yj}Dywd?xbX8o##B_-bJ!<JoZn32Aoohn`s)
akK9~t;*xSj#1CM%ic47-ZcYx;h1^2i*O@{sp(0qc4<Jl3X6Rj0*mvzdmY-wjRu^6RR9l-=l7yT8yHb1-qsuQMSK%h#jA86FG(+M
w8@ZCUm7xifJD*;ow-fZ`7`j;q&BDNoHIrRpgFlaV4Z0@o|OrR?e8Z8ta;BgZ#GI6JBnq^(@xAYY}iSRaY$a=n-LeDBa~O2Q`3kD
oK3n6VvJb05g9Te@he{^$>bNM+Qvg4*i=7FC*qrWhk~j;9o;hLtJ7slJ@R)CERg+t6Ui=i*vtntee^9sP2~)3qqAOZ9ScDM=%Oh{
Se~3nYv1iWgmEbM-y305L&<>;-EPbjF@sH<IbV;!N5fddX6F;sr?UZADf(TczL5o!ep9S0KJ2(4sDe&WohBZvK<x5rw$M<UA?vA7
_OGe?MLcoX122ZL0P0g16Y?==3K9K7a9_(nI47PHsVt6)m5dIra;63|MYQYyfMOfeLHyqg3d+{XR1ccd66pOtt?W6f_?=rp>co}X
?d;(#JlwJcktH-(_N2WO{e<gnw4#=>fjtSM|AORN9I_Ok`pod}DHBxP{n~>%iA<Lm#~2jmL%LJh@Db9QSH_Hu;QutX@o_0Th{>Ad
XnphpFcNH)S2Wf^))I|B*S`p8=l2O`F=4NoYrAtEo)gpJjOeuVWx29h^TL)Gvc#zC^yu6XXDg_Uz&i>M*mI$HfafEWd*tdR)_9*@
&{YHNv|1fv-%6LDZKo@^=IIS=?*_N_7{uu0N;Ol@7+iY!C6sXNwcjaf0|G}E77LFUxVy}?7W9h9-BzHnn0BY*N~5*NKTC^;bCO%>
k}L*<8MKWbb~=2I8>gW9$U=9<xc11>w6)*d&F>3oWGL+>LefmzOgTO>ZmB{o#l=LzTjozFH#`9>SJId=?VF;1bT8AqJFZs6ea=*x
`c{Dtze%FJa~*%asr+%{9yLsq?#ZiA2soK)R&+uhP8G!)?&Q>5=r9xOmEMuCCteN&MeyvWnv0EVgs9CL>{A%`mdjbS=Hl^1+7|Pt
u1TWJzk#8)E6eoJjqkczWD_*-#Du#>gc1C^QN$`Qol4vMT9D-7y2dHj{qP)Xsm`497&1_}w2+^hFv`T(5#7{TT-qZE*&ybCQKNf4
tZ$W~rXu_|aM-czPg>Xb(?!J<ItF*Zm!cI&t|^HXP6c1Szs||!(?+vFWIDimCel;&41F3DMYb;m!kprDnPz*uwSqv>*qUSLbFj{I
0=s9=LU8kt^fm`Rw!er|wIzCacawx!)J1}_R{wa{eO|zAnIb}f4pJOp32T3yl54!zpr6o`x>7=5Mdf^(Yh3N{6La+IspWiPS;zde
1$-;mptAh+RHUCQz!A^Ap`8KoW~ny3?iN#3RleRgJg9CwH7TL9Gj$JBJ|8tATi<TAU<18An=qFio1BW#j^OWw1g%)5H$1dBh{RHK
jZ0=5#j42Y_)YUqwT%<cYa{Yk>bdePH8>1`N~cu+irb$l&$hAQ8#ctCm;XqMMN=^omv=`c?K8kLzR}G3N+?&Jg{E-&kh#vHXA?KL
zCfSdscpYPVL3iP+1WQE9@QzU-d>Y&3Ziwz<%CySq2ao*DI{e9%~l)KraOy3{3{a~<EdZahC{#5l>~PiZ{}i=$?RN!fmyp1_5kh5
S0yySKh;n|fA(U1)oE+`(GvAMoYZjPu`MK~VvpOKOfuAYPsfCUe2?mjxvUDn13~)(6@hj<ApeFSikNWJ1>tN(oz-k7U12iNo1@yX
Bt*P8>*-mWCtkn7Lkd6H4*E=?#8MJ+T{ii74#Y+~1|iumsyW;2ttFi75t)*~Pd43+j2A$9_nYIFWTE#BIAGbmPxzldb7Zb;U>{SH
zQP{TxZMYpjKYr7DGz-#d=?jz$*!MZUj79jz6pUxJk)JsU}gst0p|`;<bwQ!m@FIvy=0JRPC(uUKc4Dw3)<HT>11EO*{etKQdjH0
5fcV941LFoUB;zZv(Y1HdKP6Ivv$_v88*L1x1JxYT#jgR6#4icceR1jS;G5%m+2SKtMpBe*IX)v@1QU#Yhg4aGdwwHs0mRY@ir;t
rYm<Dctq=u_=L*yCf+W|T%4xz2x#iEJK(g5+w3v?HkKm(d%CeLoINzn`arS~=q*i9x%2r@*{CTc84i8W78_7{f_vD>0PALpumAMq
bb8ZuRhH-)6;Im6dbzQXpJxZfq<v5?UvKVsQ;+AXR=7_hzah{^wi$?=U~?2TPf>vet)?jc*~*_HYh)~@S|~sW!TpN@(l&1c7^JVt
BgDfNY>PL29v@gp7Og|)D(w9e6*(&ry_<t`qO<z($;j6$*H|26sAL<&vMIXvtu`m4E$SWxU9A(3hHQa3(DkurW4^Q|bb-_q65Z`4
U>RT-P`VP{$Q215IgA?v3Rs_N<f)CbM|MK&pqjeN$sI!QI}B<KaW4N1a9oc~<sR-~!i)f)XYQXJW$YR36k#mAQ_YyPmBmb5Cdjtw
z{g2|H@<r0slY|ld;fwOx2FT~`l9d`YC{QMZ$Lh+lT4lWVd+II*_Ya%EgQs0zMzR;2;cTPq`kj`z8YHf?zxtr{7n+{`j0zM>NgMF
i_8rWntMgYf~43iW`ShtrG2+-?W4pIa~ofz4O4$*Q_=*HMKwedc4|rBG&$J~@+)D0JROU4QcG7{xylQAKBLtUAfo`CLjmHS`1usE
#c|`kUO0^-3~O`5WT^<HXQ9<to35r!%44rGu$w~0893}U*eOK{^^Z9KiPhpq6=>uor8nw1Bxsh9NdFVU4|_j!-=75&j2x4)RT&n3
@k!)q<!SoHHv!wqvN1mi<3H;MbBvJx)^F>wnnaJG51tRL8v`(wffx7{)sQYN&KQKY44UP0>X6f&9Cb#o`IYSsP*FGX#U#=50F<i}
2Ym0p+~DpNGd|*b97jFBfS7rd)QpXhyoeU#P;Hv(x?nbi08(vMQa%+@_uidR8L@rTSqr{XDh5{+N|<_w&?K3nCbok_{LD`rPv?{+
1%}uIxi2&4h?DKipq-Q;1ChIpp|<+R5TtG&TQ_8HW!kPfIj?77i2_p(3hGJ|l5hjEFkY$0Y{)i{TD{ipS?cUKz9{YoC>@6zJ=Up~
=zE>+FH@F9P0JGkpY4#<WH`b<n712F^1BWp>&!^aaspKB60#R-s9U}?!*Ib;>je1vm|W%}KiZr^JAh8FVk#P9E|8!;Tt)#a*$FfU
)~J{pO>75aP>H^yrXvkf1&4U+K>{Mw;@@w4B?cPmxkWuHqOa7-=o4bgoL^-G;C4@X`wi(k9!u^yc-*c;MBT%5UKc}O{7g=^?PuyW
RoT)!^2=3MF5do}?wVL4*KIzQLeQly9;GnawLW_sABO79UU3wAp?n7BK?Tf^bd0j{&tLX;bGWyk1h_x65wf*M?e!HPa(R2sU|Mmk
IqdNS`*@KW&kLfA5wPIhJvbe&DHO7LbG1#F)b|S~noK-S=T(LPzkdrI9E!q_GYd)iG7pu;!n~1IY=JGkk=?S4&Eu_}WWK;qZbIF!
SgNt-wZKDt;^wWDs*;mEwgnC{MQnV$$f4rPU{2EWg74SIg!)z~$%b;Z^?L^|wr1&Pr(W!2e4fB2So-O+noGPyiq&iK+k!U5>yY!Z
heBYarG{ws#M$H&n!*J<INKALeTzX>yf`B-L~MV3)1hEdgauPC71voVu|OfmFh!1cm`YA=dLom<oJ>(Zkcvlndf;8((eY1G`8*Gh
u((ywuUqmt^WAOla7&KC|50h2u;?=>mh+0kzh};361ViYEwHt5GKKDxXfOhLjve_=-IT?*P>ltUeUwBsQr$O>itD}jqPC|*Ea9D@
d5-gE>60y+GW%|;1WD|Xi;JzdHQTTNsX}NFx_0A3)mHRfd=W=6jW~~*WjIUynITXhj&3;scOmM+O`jyf11dsb`dendUXPY~fhs@q
vh0xr*`5J3r)l^~s6zzHqF2y?=LWDTql4Hg*c-XU&aHMq`0bMR?2gl5s-N`FTSmyvrTyeH)IH=vmPj-wVN*kSAU;h?lB2-B2^>CV
@wtmU8G}ipC6jHQQf%LlV`=O7|M>O1^s?=Vq6z(B<&Rxoz@Aw+k}49fO(r*WvX+%PgW{r1e$S<4d&#=S`me?-k^M$D0m2w3P07dZ
;s)exWTq@hPOZ1+jSn&dO9~GVHL%(ivJ6NbF@meMEa$$DFX@XZU7n~a_YG-*cMII8Gi1n2bDKvnU=hhH1(Rqi6{5~S`^}B40bvxl
7_I{~v&i4`59j(rIA=Jqb*cCj>NA~{OR98Ik7{~p1!jidlNFd0bdq(s;Z-;CFw=YzF8hLx-JcRrlx$P4HxU=GY&n_wpl00g!0fHK
*O3ZCNXD*otvE}o$8JpbOUFk{gDf9turqYi_^0XL7vtcoGfRiuZ&B$1q6!isd7huh2=Se_OB%422hV||a|1*?LnIzVmY@W&-EV(b
K54+yloO*%trB-Lb#u$!>3&-ep@~?!(7xX(+sYw(DrAxUJA>FLQ!PfOT<*RIN7U<W-`vra3|^h>avJDfl#)mL!JK25dzOOMUQ5Eh
*Xp5-Lrh(a5L?nCduBJFZ+H9Xatm>IMk_!lv*C_V5lvW>HSz8OlL7ZR$5lbM+iJL$l0eg?s@<17WH#IU`CY+XkEwk(j;i-m;2EVL
$=i0Q<BizEY__UHfm<Mte?JPs!pe>@J7OtJ#7JlG&E%lE2apsR9)C6>KvWGGE##c*6&8`GHb>to5flwSjj3Hh0UP+l7JNm?1-1!@
6R7`Ra|@jMqaU2}bT_yS2y>``(Nf@}l3Pgd2;H5HXenFsU>n~cB{a?#Hk>?tK)ziqr~@9N`_M~yxe=Ya8iCvP!hF5V%QcBxCwCuR
7M3Fvy(;}^2>H=Oc+PC`fTb{r;JHg~ZH~0F{qr#-)Yu_>(BGZ~SBVIh4J$z#@^N^YWLFwNiUC@&<`(fM-G;shcx-i-U-<)Vi$$j9
v`(_Yf+@s8(GW5Z@DWvsypRg0*+8~?K>VLs%})~QTrUkGkJ+%xyk%0<tO_h4duBj4#~Pnq)1zJzkoDjWaWysrm5mo&IxrUJ*jH;D
UTF1pOEYiU{<%p;^wH_uLhrG-76@N_1`j3QQtR*K_^}fX+($V-3xArFc;@~#-*)U(05+$pmvm&!VUBN-UGkN|yF27wOH4F;<iPT}
maXE3JP#^hXM*pF`oR`vdZTPN>iqTt#beb>nu6U~zl<R_tw)MNsB?FDZ8h)kuERnV4F#q4&o8o!eC21%bd@&U-eEpZIy1(r<s}j{
>9ZK)R3}}>#A^Uv1M>_Rga<>Ad&3TM1)ANj(ziNs7k$GRc7P$^F4fEPs=ba_u|Z&+7c>`PqS9OcHXJNgSItONVo-nfRfb9P_5Cd}
Upp=k(RB?#6^%nw1LIf@DcMUU>;bI?O!UZgD|;Gsyk49&Xmr{3j>?}e33Ez~T6qO&bR`zu4QFEwS94NrbUf&>m+*nFy5`t%biIV?
?Qe8Sv}7Q|(+}*~5>t@yyW!daAxJ%Vk3l9A%EUE(0Y$Z^<k1#DB-K$;_<Y7>XOIS!%0Ig48Ou$3x4<$!n!NCPBaKqHGoR?dDYQD4
R0&Hxy4y&vp;ij10DO+eOhjkho7Pki4587}&iqA**Xs7V5Q8`4#8C?sR2x$+|J9dpraslaX!cR?BhKhG4kwS%@7;GAR0ZIg!^3&z
!J!@2)bI)A)xP{(yodi<G#gcF!LrOuz52RV*N&33y@{$d*c%Zy$eXlO<=pk7Yu*ay32#Ph4s&&CjGpdH#0#H#M!L`v5wyno8Wh<C
^EuKA6wEKYLo6>Y^rT`e5<Mz*oYMLEA=3Wjy${btL232qS8%8DY?EPW>V7>0+X&z(V_FSf?TW+$9%FTA`l4+yH5H{S2)I5-9CVVA
)DS;)EAiuw$a1ChZ*FK?d~{3B$gex8YQ*&YLZLPaxs)6Bbc3V)G3G%*xd#{^B6_?$uS$OMcUObbJCPGu3$ZLi{dca%j%dQAEjKqe
5AD~aPC%NGwYyV@for(+qzx#PSC_*nkNL?7<FJ|U=m?;X<cU=DfU+|8;TiEqFShooY5*?8rG-Mo(@P^>+IVOGkm7E0>_L~){i-P=
)pK)ts!-mqGP7U<^5)v4U|hp`p@Zqf7l9&jLAVKtu~0L6*i}}#sbsFxcrG@1HPJeT3ol)Y6DL|!gwOsV$J24srpQZw%`4eoGawy3
c8;t9|1`bV`FcUAsmwM{B{o3Qt=@96O+4HO)t0M9xb(`6U_|{)m55IaARWN8Q4^Kv9==A&1&S^|b5U0OUM_-LGaEYdyXnNS*k{x)
yHha2kO!h;%AX6x;kC_j1-P9X`4vStGJGQO0^xfN-Sg>Uu`xsXvC-!svtkEkLlT;!z{?3f`Cef5y<!A$#$0^(I5bmPg|LL?3Vlm=
PQJ`U9-q@@9kK)gXJ)UujN>p54wWXUXI1=&?#o~M4GN>vJ7wYLRB#J8Kr;&*D#zNWoE5Z6zirio4e)go@JP3N6o{?E+v`UcF!Ms{
jw!5k*$tGzbY_T2C$a5*V0)N9&yyG^Y-T2P#Qtgl!`Jr3?O4<6Dh-EV$%I=>6^DcNToy_LaQ;!?!&O;h13zTR=IEsxAU0e<+!G@c
hFXN{R|KPUksOut)!vLM-@0WuPFWzIyBL=$b=Nvori{oEI@qqNKshZQ9hJ+pVKZzIxHzBWVT?b@i|p9-x{&g9f2N@*9lMg>z|?~z
w@U2a(XXFP5o!PaI(^dM;UL@@ZZVTte4;QKELRA!)%FtjEn-~PWXq0T7x;{Sz8KQ%o2zRgcw<7*4omfwwCtb_G;vR=f7}p}d#(}f
5eST)ZX`civeV!{{x3-E?!lxsx>BG^wK3$}RTx8S15OZi8P>fnd!n}DWE7frS%+e@Z0beKuCw`CO3zBzJDqsu7tp@~=b>-q+FwR^
BS1S`?t_Pr#>tuya~+LOu|?k{>ap}^rN#<B(|0eUuGKP~%-BRO<5XCBx}C!eDsNsc3tS_f+`AfJ+dapoXilPPq{WnsdOr)K&Ru!u
nAQ)ADoocp0Fv02dgi3qK&msmp%$x9DJcWfPgWH+|9;0IiE{la>tAv5Aq?*oDt-}207LZkZR*i`EI@_UmCjCzNZZp_dSkpWgH}8e
i%5jq3ND^J{A6AtSfa~9*YBG5z24%uP3Lw&e^t`!Fpe{zm4UsEd|VFRjn~y31|y}@%1XsB)YzLLAoS%LD#%#qc?o5I1Me&+5g4iV
%!XFi%xTgaQsuSJGj0Kse4P0;hAUJ)9)*z8w2`?Equ^QmJxrWMhtaDG#whhaU=;2XBVJeJu$4p%x{p;THOqna>?<my0vsnK8jw_m
O?exFo1tWMh?)XboA}AnaWye?Y1xd~OFI0Z>0(QoiT{M-5XR``zr3_7U_%MZM(c#j1e`&!s!d=hT`}{pL|3fG#sF14%C*dbi#^<)
@EcW~9J69>rN{SFX$6uU|Fbe8j?&T49q4V!3E@FWdB03b+q0nOdX{E{(W@a7A!WH>_l^(QHJOCjm%l@}&B;-2`DoLPxuaMeZx0Ca
Q@AI=niBY4$0rv@{q5WTt$vZYpm^65OfrNWynTi-cNsp_{JIoiBGsV?R~V={FS&Ec>0uS)vF%ecv#dV_fhE+q2J|X8$WiXrN`I#<
YW^_)`mUbI4I6DCo*fBzQIo*-k^V)6kbSL`6aU<C9v_Z@$Qw1D&`7j0lwTTJ|15cC8G1yQVK+&><SO)y)zjM}uQ=+lgyFuG_J_iY
S{B1)MMLX;PZ1#05*T0rDS169-L`nFLRmL}ai=?*iU@1!0?KQs8@Q({CW!!qGvmbL2wAqR@ZaW@Ov3rqfI6TA^Q><JKTconV=Se}
cDm)RQEn;}7&zluuVAt+u5pZ*kZKb=X+|C|!e~!~^*h4mO1Q0N9%dGtXe$E5%ZriCq4q(vOtfcWUHF%!&O~K`Of}@3kn_<e9VBN%
X+MD-Uy|UWY0fOlXqp%O;iR%p9(#7BCOhS)+mA>>!OKZ>diJ_MKYG+@yA<MzgIW2?UD0t(<UM>kHthrUF0Dj)V*c!3b@d=H3k|Zv
8y7a$SxX=ZiT%bGM2pk-xff$8wVZn7Su_D4yM@mdfV-Zac_RF+!VWS1>kzYJ7;<I!Odhk}FcMp?X$BbC(77Nh!n}m7PQP#2>w2&*
+d?(1m^$VG<xP_E#ufr$K602c%_U>;Vy=jFPu4z&riE85dT?|<yl|_9G1)55G~h4V8o5xxzV#25&|wpg{zY7!_>>|Y1YdwT?C`Kb
hYDEsMm?~wt_CeG1ter@b~5paq5L6D$>u)rYgZEg`y0I3V(q7Ifwq%rN1t<$;HB#|FLm3_Yt#nXwGbAr@o)RR{F(c=@?IoYDmV*<
8c=LE+(g+VG1%j!9pN5`muj7H?<VJYntZ|SoSX%Zm9xpwr=K0y!LP=MgzPP}-Z96VoNsW7oF)&2^N)3twp0(J0a9*{a;zu$`u0!P
k382tLvHMx*XKo<T1$o~6MGem*y?1M=>`%S4v=e#MBv4`-<_z>l*)OSIae(2i<AKHzev9t7ww^2elz;$={zFGv+VzeMA0q|GmhU3
;y*#+uN1@bxBJg~ng3rLdff&?Fuotn3lO{Rq62-Ort$HM7wn=5YY~6xL8~vOy%oLN`}usOq;8fpgP@5q{2=ZH&Z5$MBZ$7TIo}zE
+HuQa{2S+*>NR#;p+=NPz$Fy<lxnSh`(&cDyz{?<v=`1`U0=kTphgvhf5C3{c=-0<ovLmbPa*<FBrhvDeu2+zZo)5S=NXy_p8H?8
v<DthdvlbHDbSIKm&(5^nI231SmYV5N?Hj=|4Ze^T^9;gm$)$BZI#WPH~<5vULo<2xlgXWG2KtdC+`_H-0I-Z1r#0LgbVRJjKIO>
&TB|U5s%b#+#~S0k^|lQ4cv}}q0*~nZ%FdA&OYH4>7u8ZnQO)_GkQcHORY~pGo>{r-K>?^)k|1->@i+517S>a%xv?R2wO8W29ucW
FJyTAGa_n4A(d4AS3hG<`Y}Yyw^(L7e0i;kK2jbZj3UHUky)n)M09KGA`zgN($MEE`TZCp$Ob-3J{c2Ts?W)eif>ruzO|why%c;x
8|iM)YX=r*yo`Ev2RBw%tQXu%^ZfNXTCqXf*cZE~gL7naYI~d}HQiq+V}w4oJLWlAmX(4cl?>?`1Um+sk`d%K!p&u3GWZuvt>`2X
rb)(|i2v3&wnX?3aB?xX1E}b1Yngv4#M|`TItUWun=rkdXIMm4p!hCy6+;xw2Z9Z;{ZJwv0H1VW4pMO^9LB_=J9yw$W~zX;j*QI(
nUON*WXtr#%VcJkn09rkc`#h6-2>(&hVM`1ud5*wj{_3a$9^9Z#RfEW0LQ`Vz+rtd^Xbe0B2e5>@EU!mZD!~R-5Bj!IMuFAYSTA`
0SYLlU>I6Gx^~TqlbFe+#p9<LxLP`yvG?HW(*~&O5Iw;0Dg;A*AG+M(Kj+Y}U<6i<U7%<mmgfzqpakzj?$wR;^WpKvgJ}txAIove
`_`@r)u=Lop{sd<f5Ag~Vy8(rZahat;@0w0-0o>Y2lzFS=YWY#4>O4`|3ekJ3~Axto5DP<(Zl2U(_RCey)j0U<a91py+2X7cigw%
O${|YC}WHdy7EItktCZU(g_00D6tV(dP$YQ9CfQJe+lION50RF8&`y5UPg#D24-}R&RZb}kR__mm-7MDaWqu%oxgDTNofJKogoDs
c%U(E$$*`1$pE^|OMJwi`Fy+@_3^%e(gcsVZMe<$5B{hhPBXY_!~=mc@j8zr=V+wTfydBxuq#2La-@b)uOiQ-)(p<!P0~ODFs6;T
e{pkDwX;&@51D&X-GmB~caJ7Oq_v@|Q94=3!&;`T?vzQ=7Ju{Uj@tCMsOQ-owj4bxy_;HSw}3^qwSsLJejZ6d@a`7fd)ywgS;jIx
@5O|7JuF8HE?H2DJBls@MNF*H6J=OuF8dr3XK7?<aP+8CMzwoY>=c%p8{3BMfxV-&oVc>%+=7c>HaPkr$EoQrmI>*cIKoBa5^k$y
7re)G!M?gX>c^YSsXQPxfUdSZe(eBK`!{z|1+3FgK2qh9#I#G8Hjq$+s_aAe31FJa_j-2JpE--Yv{ZG46(LVf29h$#Zwc~MuF)Nr
rR&G$g3FOb_Yr?m=-}Z(k|({Ve@Y3Rj-6unw5lKHTz2R<ilyCSFTezQn>+!BJ?#o-)j_EzBxczik-pa5&AxXL_ih79HH|zljz8A|
vvFXVW5gl|8;fr!`Ep7iQ~n(WPlhQD$$nG(JGCx<24Kv7&F{+=X}%XUh<C*>^B)?@^6DYpKs}Q$LlBmFlY6EwD18ufy!cr|qb_9V
HBeEh!rT$)dufn)^kGSLMaGa<hy8|NjGo`b+8fR@vu29Qs$VutssjB^1C7d5cbo}Z-lsdYe5`VCr`V38=PahFtsohiN}RzFI6!CT
px-Qd$es21xy4Tcr<2_WtwYqT!pUH4-eX;Edz!JW(fj(R5@LS?<Bru$eYMr3I`ru`>8Fgh!2GL&e=!S}u{maL7%mDalq8l(J6*G+
3n^B~`t$J)TJ70A`NABdSSQ4b65*!9wdD?*Bnp68xjE-75jj2o-m)OA>_Ws-i&cdGr#5_klRbaj<rW*)?KlL*Y4ZhBHtPii-tQ>U
Y($OZi!t-wm>&skvk3!6KU28wj{9Wckms6aZerxZ*mY62B)#>;AuI-Gwa5KCv;Y<+i8SG%H!3_T51ISaHS(^WY8jzdX~N!7-^;(Q
`)yGb^qtUoruPD7-CQRHoaSd(9dz%LZOF7)DOQL?cwv$3t83hyvFcpRPZZwb5ur5&IuF=AWTl(88R^Z3sIwwG2XIW_nN%N=DD-v8
{*mFukqQSyq7i&@R^ps6)xnrvJ`slL3ua!4*jQV)c_3CyuVf=k=DeY8%=;7sPdsoIf!x#g_~_U7ZPo@*7o4uq30Dz7cIqO1tZXT0
_WI8mp3GV52V2|SIEx$QteqjJqIBxs1O@ZI+NnpV$UKVT>(Paimi>^%W(U2Q`_o|UpDwM{j#MR7#8a51n`HjWhboER1pa$$IrN*}
Oh}ckc8H2r>nlyFT5Ls0-t7Sexs^kS_Bu1IdQvIis37?TCFh9!=rX)WMX_!Xuqc6gQv?6e?u&1M%1Q2U>aVnr%j+OI{LfbGy6POM
M?dpltiCLtMkBLZLcc0EX3+(6I6Q-AJT#1kq!T$SpWI)YGLr~F)sLt>KnYu^Qr&o>FuGt@<`Lt2u~#v7+ZF0xg;KiRyu5vj;0z#Y
=A(Gg66SgBjF;Zhw$voFm6l?Rwy}f<l?+4uEb`A3O@GT{qL~=Y2qvyy4;h~Ce~qEmUReG4pq|kIQECl49)$;Iuf<_yca@$^k`2oX
fPX~VmoDFMoDz*Ldyt}D>PA=g2Tdcc@)%}fgk+-n8Dz0hTiZEbu)?IS>4oM@xxzcyPO^LHe1maNh+|Xe`%T&dqBW1*T=n^*3gKfF
tQ?0*IqPlvt5D_srJ~~xXORq4V~dxbzUYIeRvAkf@(-p2f}O7!6*{ELyBpeRgZn}wo`7j~#VW*KHPk#uc2PJnzn^ltY3E4FaR-Q^
Z6)@JqEE??*_VgrA-Dy$J(8c6otsxl#tym~JZ!(@Jcz+^Z<qOjfvnbvF>sOSeAfE?O1f30K6Z8{dtBp0_T+5ij80WK%E{q^*Ss8?
iwC6F0*dtXFmK5AXM*|$X>FFzpGU?my50N+PM~6?@_Zcf5R~cQ{Spf2`5rYZrv?M3WVqa3L$Z7-AI2?qqu1kNl=`sz*x-{|$=11;
BT*yeWN}iQH68{q>ESo2O<p{aB=a%KRtJ5b_(OuKVmO6JrOT6wn%k+5<3qI`9dRk9(ta~L5?dszx|{pUfm3ZN`Pm-o-b_?j$+SWL
HO&gIt$2y<P>{WZd3NbeYkVI-uIvS<NA6(Xs!&)|1rv$phsxG$3v5hX@3_Y=COin!?xr%naO!ZR#$8vp<mcxnSu>Tq%>h^I?F>{g
TFBdx!B9*AZgaWK|0hEQhF^gTuE|KMTcf^kJ&-Q{uGpH<vpw+z5q`O{QHht>pco})Qp=69{zR5%@%=MAgH$E)eQT4LA@U<P;Uc{W
m{^Gi-puAqCpM!uTn~!wCevo*tH~aZs7CT)wELc34OIL6VL_LFV70>C!IY#ZmGI^LI>j&!@=rNL0)X`skQ_lHFY!^<-fh^SEjDuO
hs<qBRC{T@{VL=yhp7liC2=(0Nb(FwiOXYpu32k>!&>{<5Wy*=xpOS#!*MlYtNKlMDS7d|R1fSHuUSm$wyXSQ4jj*S93g!~o~?Rq
BAh58YH7+8@Pcs&^;|^J^}z8#0d^B<E`l!+sxl5Rf?_->4Gm;bEkEY5Y)C1#-)z})U}<cNCbce(9fZxZl5ok=oTN?u{B66x=uA~B
GCm-C?v=WzyP0nTW9LBkdqd9UXc)(<p;Q(!mT=B437uzDe0b^i_#!d{Hob2m{OW5#S+~Hg6#aX0{uwzwe3Ow{K{K~Gc-AkOt-+PT
5Cu2^8w-Z~g_^vXYe{HH&55d|U!6DNB%wq_BJ)amK>T^BbxfIB?dq<4&qk#1bqv~ZqbsQ<$fFHQx?|BL3Y0CU<fOHs>;hESuc&qB
<+mgCy~d7b_yG&t64z9=8pCsy5fYoV)GF^I!TT~!g6$9)@Z~>pOo9}l;uOM;=w%F-45R|S1~)#f!0pl3<FKhrKepj@>?`b(pVN$D
&@|R9jmfq>j;qPl$C;tPexgwgSN-0O_5#ZlW%)dyaitMqoW#dI&h3ZqE<(tvK^o>R@~lO86}J~{tD&jaFUeDAFXA%6rw29?b#}cs
)>U5V&%-Z6k;hoK;=YbT0d$>onCo*h4!OWBs(jX}Tn2rRqT8uBC62M>k7=PHtC%c$1lY=b+9wT?Ab(`tT>K?Y462k+1{Nm~Zibmq
y1C2Ah|0UtTf3}|Qtrqx_lg&#bU(V^j^H@}KXApjs{#fxSLgq@0NZY1N>f}eu0R=up97su282!g4%JsqSH92Rj#&j1Re`i<bzhJp
>LgzjZ#qV|Sh-x<i`HWUX=aVEERo+5vlTWrc%ha0PwH$m=~xowNKBTlXV+ZcvBR`4@6j8BJD@aLdgdV^7wcN}3e!9<S0i*cJi^2K
Jj*hu<0_*G6khPeYC=v^U_<ahQIIl>t1aXSFw&}7mQeN8YJ$dqsKNHs4ibFe+F%3n%6nER7QRwuOD3}F8?qxlmu(Lf8rQ>DGaj%*
9;3nz0i}8Ji7N382IGfY4=ZfUE+N@m7w>z7#!nvws^8b^si6?zy33orCNJre23%PXF+|b_Gw$u6e~RLKb4-0(fR<g{I~Rr%O^<!c
{;#nGECmd#YwOLq6KL=u1gWZbn{;YFqkJ5;e?_W~elpobgCk|qW>#>?zKs62(Vmh2*H>`?61AU#4CJrln1B^>vnSaMG0@sF$Ax?0
Z#jj>OCq0CL$zkEm-dVP#UC!nCCNR7Xhy!|Wua8PH){FWak`3(kaaG%KB3lk8#$^#fwuKbf)5M3ixe>UpZ+VCqzY!R@VUA7)pt-)
T~0$YeZm2OT`X)`)QfggrzOq_^obNIl}F9l)Z#P>5+m^Yw#|9GX}p-jOj;!h$7#{#{IaQLc~6sdtMH$-YXeLTXom?2oj6RBv^w^i
`c}BqDv|Tl>NeDW!l(L2>*bILpHmI^&%=pJ-rzKTi;UpmzfDbvl7lgZBQ5~Iu&(&R=E!}LEBSf^E~r#fuVSLbsPJ}5a{VD9#gZK+
OX8adyoTI;;@&VI)m1+qYPC*k;tbM%8-V1^{}_S-LG+JVq6o!LL4Iw1-Katcjvnq#2}Jr5@$n@+`PFIGhLv&A@KNcZ8N|ta(RA%p
qw@d9ffuYgi~b!S1S}(boiSsQFZ1P6qF}OhWV4lAYga&MY-cxlc@G)Q8_L2C8D{d$lnFTtdtqg4lb>(>A~;i3MnPHQrb1K3)cMf0
N&G{k>qDGopbwVmc+BH5u<Y_I#z;B!vBH~0_*g|aifXwp&j??_U#<g+l;~w>|5)Pz@Aprw$_Hkn8cv-}{R2%BQ(;q3SJ&QdkKqfI
azURk1KIW($RFEamXK~Ire7`vrlv_>Yyv9rPGJkc8}&{^5+A|sy4CD1&GV_^&_mlaK>w!q5g2XlOE&S~vOuNjQnv65K28N~sVIqw
M%#+MVK`uSt!61><lAj#m3-$B5VK_JgV=F?BgK4gFt~864g#e@YNW~==0}8-I`J^;W^}WtIa3<hCQCtix&LbIyf;69RWziqoZya8
iy<ezZ?3cCs5Y}S!UM(-KeIq1FtUkYG~xC65i=DS$vHGD!5FMx=EqnFvl$vgh7|A~An5oFgwi^kX5W#CpYzild7ESVWK7EX00%9<
qM$KWES0FftWPSJ7Jz;LP0rAlFgP7X?KY3m8>w}xQEwwtSx$GQVsvd;ONhg6jCsVC=&2r!0kum@=PPrhbo&B{5&NJW5V^|yf2lW#
ABLphRrbACuL!}PU{kuw`*y>ok#wM%T`UZ7lY2gN0SqzKyPfS=E>0vxV(D|u&*@Y13p1Eoe<I7G$E2gH!>N!Sq)6c>8Npsmm2%Lm
7agliTf^NxV+ASS$rcjlLJm%}02)+0QU={1YA7C&*HP8dyK-%g4~qn^@hy^-b}JWH-FNom2)~d0Zl+Js<zs!0qh`(Zfd8JxKDOZ6
z`Wh&RHRFSuw`UEHfW5BhA(5WAgS^1^4@stFoi2v!uB>n&6epMg>$MVvP}wvc7cVT7UF2{KVCq_yMxbCrZjK<P?kMRk2H<&u)tZN
c5>jMf8PJ%=7|nZ>s8pM@M3M%`xI0&CNHIDUg0LdE8h@Bbt$>{(@cQ}F|fEHS*{te4wL-Vc!qh^4Tc_J>GGKVLQ&#Iy@QtSq%?-k
pCr=cK?L_vNx$*ytSkO6M@zPISkE8J21m6=MVM)Y3n=|LFOI@69q(_^a-~*s`Vk2}QZn+_TUp<42G55|I|il#8kKz8HlLF=f>J|s
w3|MiC$`EU!uIr<9na95>H>vOW%3>HAj+`n;RYqX3r1TH`I$IcutCJx1xrv?KgCcCf3Fd!k-PwIjAxM)5b)>hVTw8@&kfs5wV)J|
MjWiAGy^+v>`UQGbz|Z@a@_5bdOQ}^+yT{f!Y8ow`e3VRQ22<4a<jm_qkMWbI!>D6?J+p`x(iqp%q;(1fh_BH0*GL1M86ezL&h+v
cylNGFET=!jlFMh89<w=zb87eIBMBIX`lY37n(#kVrF3aL@d=zy#GeVvgge%y!|Yo=E0Fo7SJN_n`INjvb-r<rZl?za#dSQmzosy
hK?vc1j5eeK_jdcF$rLQJpu1`1~AisE0o#tFzljwF(#&l_=c|t0hOK9goJp>@~MfgV|J%&^?s$m@1LzwX3|zd4HAdJ841+C;kGa0
Ggh;lFQ_hM^$o7UTyS8yp+p+bETp*LLLE1IQ)Fbp2YQE%O3C$ro~kVUm&^d4)geJ1q&m<_%7#1v@?WW~>yRLO_$<FEtFbhgv8vH8
oIIg9ffNm0pRcWwyuGr1Kvu#~3~)*mq2_eb@kK^a5S%zeSA1AvRWf6~<2^YF`~0w9$ZNY$omR20e_~&=N@CP#xKD$qTj&H?xPHq`
xX!W%5A!eIJ;md^-P@7T=YU)BhT=PME1K){V5>ydR)V+eq`lGyK&6>xreA}r>mEDLQRQ3gf_DpRD~V_1XvjBk!A_@#R%&J_(4aS_
4IWnneZ$#^$nX*)a@77Itn{Pc7EIf@wG}HO#!ST_UH@*n|1}z5=R;?;b0$_g7X>vfqP7=DV0U7|FSi^~N)IY4?Lg!hWK{D5-Crg6
I!p7hWnn6DBKDz@IZ{!u>f8hII0XL>*zXN%_9SeeRCD&Trp8O*b3$1n@vr9}1|pHP>`#nQH-fBEu!P@SJs;P{A9&cJsX;Ls`u!QS
8Jnl{OefbHOGa<HkDV(lUCNOnc%4s>l98Y7%f3e$u`cnUnv1JkcL3`N)c2I}y-i7CCiL!fG|ya=u!vvJG@EDfp5)ZsOdV?l8|(5=
Y6FtiF^cjsId6?3D3d^bQ5u8v%sUB@VCQ~bMyx@-iJn&%D73U@R;GlG{r!@Vd#X&Jn@&#HSC$k~tqO5pDc?a6GN6``G@lNc^xehy
<wi^c#O=52jPT>phF+4QJxBd;bjp#u=rmq$)c?#lU^y|q>(mpiY*Yu8AOSqNob*XPCPF?zo_HOA{FL>iPJyT-=oQZ5>-$iin9A?A
w~{MYtOdh#YQ_c3kr!j>?x|5*&e85y0!PNdVZ)WuaXzOa6iZbenYVDT-Bq*~Bng>}w_lvoB$*<v88_&?(nb^Aihz0_@*p_L3xz&*
Bo?K=oQu@hks%Njk(CN1RAWx?rr`8y*D}z3C<K;<Ns6L-^Nu}zxPm1`WxSde4euK-V<qqr_KGMlWA)TUu3D3Wvctys^9zH=|FD38
_h{nENs=Nj*Xi8EAkp-fDJka$R(zyO{etFd1=unkn)x#n$2LJJS{{|rc0s3_kO^$QLg+=|hD;v&k+FUN!my|@^<$;jKbbE6k-)ww
xSn>thtdJacnEdHh_4ZksjNA&2?ScnC(mMb^Qf^c_D*^Dedwg`bm{;p_5pyOX3<V&R6Lbhge--VB&6bsw<pbMIBR#@#+0Fro)+M;
p%{QeMy}yz2c0hN&F>b?R}h9*TRhK=?Y`vx7}7&q9XHUxT-%WRLJwGJ&Eg#HtWGTUT|x7|F_)h~1tZ;_!)A0E!8w<tt@62DsASE7
?AS4&O|pT%<Gh3Oph)5><!zYkbXjBnP#Ihc`x-olRtwDE3bc|Los<a+a?*{pHJ_3fMk}YRtHb)2Uj{kpX>0g-57Ysw({-sBP(n=t
#K{lzR-SL<cwa+T?H`}JTWsf*@~5u7wRfFCbUsam44s6p7l!1Wf<quin;png;1?*M&1hRki_1@Mm2nICT_nKy`6zM{p+manW9X{x
f=DlfvDJEPP-CxvwD{_{14siE-Dh$;+;W9{J(&CxR^GK%3a?|DVfhTfWlUUR)o`&t?y=$;TzsO$&jXywIGr6qAp|8naKMYkS#+{t
{<&j@uvnW@qxn`wbRXsqwj-WasVhy3jW{Yq{r(>*V;+#ntvaD=C-xx&1@7w}$1Pu1Z}+$jT#^0+qK)Uvlx{)v7dN-tqN5G|t+Rl6
gD+=<RM2<4?>o!8l9C-j()+LoERu&=Iu(A_heGzkwr+GWU6t3z^kri_Lg~&%f3DyENlku0=Bwe2+^25p^~RZ9bv7u(i^ADJ?g(?z
7}0&C5C7;~-O%`^zrY_3VjF^#zA!1eO9iXsSI2d3(}OpxpJgl2?zHebSiQ%nuUTF+*x%upMY6Ha`s^+^jriLPj2#;Q`2_1>eY{Rm
Qs0)>Y`C=PBV*G)@89fc$#j>zMWxyB*ZO60U$QyY$qucET2m<IA`~nGGZMs5RjKG;$Ec6BpQNpili~Tq;lnK@pVJh2R^`+&EfxW_
c(pzH+1$mCU>YtNNPlY-7=2R*7~d;Lio*gfHk=CWi;Ac&rW;i&&%9iQMwg3Z7sWhz#uv|+dtG3v_QWM>(NBNGCp+^dYch+cfoeV3
@Q(LjeJB(EIo}$9@ar=IgUDCT-Y_?87EAy*l|ZejrNHy|6W%Uq{wd)voM4sgs^=2?4N7uH^mHYw=_t)kn;kkm_6vqncDf4<H>mSJ
aI>>x1^(3<O9yKoeJC0(X(t~iNjXlgvfQxKxEE-i{D;8+cy;Son=2RDTRIeanq|%Jz)!g-DdEcfbB;P1wnn~~zPB6QA0^p?`i2K8
a*2G7Rmx91w|!*ET=r-%Z@-jMgi$phwFZ?nn_-!!<&yyu6UR!Wn5%#3uVzbJ!~qezOP=eF&RrPTZJ?y7%Tx{*dtzKrxsOocW6@D#
B5%{3?U8RNwc1PSv29y3bo<845}|EzkQoC;!`(c|O8aFU04y9!gUj<?CMUqV(3*8yr6aEhXRU>o$gNYr)Do4Gq+6ti;j)VzSj)Qo
g&@tF#?ZZ3>n|d@*1^cR*ebBQ-9&cWax57>zL@^;U@Sh&9MGOAZEUK@jo#&BU9E!+>%-Sf3KvZJWn!)*y)C}AV=l1quI@hpc?4z@
D02OWxFLMc+n0G<fWO}oduJt89$f=qs@B%TE4_3(@A~tjcL}P-+F+e7&(w@ZPqBU>sVO$6l-tfiTiDZS`f-=<`p1g7*D^%;@H2Yj
05B}(&hFCtEyIUk84ZLx8+&pD3c#&pOE?l3X_rVlaxT>i)lMo;@x0;!MrY#HE`7rk5iBhtL{y!-DI9tp*XkabujhiKZU)8$?l9%p
I~Bnf0{y^;^2t`2j^Lw~&prnav&1}$fY=%0)qcSxKVfu%<U*fpE8&y+JNdX0+DIdi8yoYLAq+<5WX1lOyUoHAM*(2dm+>6k%Fshf
4SlWi1HysAT8s^*HKFG##u@^-dMQ^Sgj)b{Vmm{y0UcI5GrU2Wi*$bEWB|A=Ajq@0LaB;}eG+^xPT|chVPGbgLgO)kEj_b9g6PM_
NpN0DX^yegwOWqT2p-DPTVmRpL_mC(gTf%Si}?L3+XN!-J2^or^d7$Q@2z}YEY*a!yH%KEpibkf<F(U|&s9;AsBUPTsnup`8!qne
OOpYHSJCebM&XE}>lxOGW3)yzE`Nvt{6{mtS#cC5^{ZK~x=*~c7OKU2!9eut{<yUI3{4-dL*!;%ic>3@paqti1zMlPXBnK)F$yIo
QQE)n!Z0DQwmGJ4Qa^$f>Q6r<Mml=yo!xQRJQGRohO+-67bNGxK%bHIk}Yhv`7}R+Xw@&x|4)g#6e<~Ao;P2ekS}j6YXSW=ZALej
1goy#X)Y>_0?9ojKerhlK`<t!XnqbaC0?jr0*2)I%K*eoGQ`u2YCRa3nYA*>5`1IsN_zi$=Gy)$9$dkg*UNR`x-jbyq8hVFNAm<)
iQ5->943(9?sonpx3ai{vNNv8O2ggaMupm1q;jpG(Sh#3>2;N%N4zyWBHyYu+?RC_|N8#T#cc8{;dKOi<s1dI0;jsB!DCVB+J>zf
Lx7A552HU~Tu)#N`q+_M)iAQ41*GS#H-`t%vt?wO15Y7x^#w@$76AOPr}C*o;~9cC)CZa#9xLQYw!yxo7M0$lqB8t4H~sixY*OsR
*9`U{8sXdl_opJGJB6Ze{PY-XN5i&Eya8)5yo0%2*BoOk8^wd|8pxPTWuPh0Z26G69%c=TyaV+(Q-^RZw)LW18&4UHdVPek{S^9&
Y<=;@(VPNRj8cUxLHW)3L9${UX?BhXZSVh^ENWb|+B}E@zLcN6Dxcyfn6>cBgJ?zzm7bf&Tu`EJt!?pK0p6vHblO}u!9mJn$zgzU
XNTAW!a6WIwWan__feAavf=OrelB5%x@z@5RcXHe?=#4fNQy92u?KFLy(lAV;uC{nEBxh5Y}lgi16HfkO$XV0gax{P!^(yrtQ+EY
0{{JZ?Hat4w-5<)+Amg}<F?sw5eB7nBPhJk74MX}LGRkMS?RRUhJy7*;m=k1;9^0UY2Yc4fjtLx2l&4Oq&1tzpa2$|vfGOW)<Ljx
%b#>ucgfll%SCekqwMZ7I$<x?P)%f}Mykt_v5|@ipW$KTyXffmC*aQ3W)QJ)?Zn1wL0yF7$~<{yb;={3+)z!<#y+luF3qM1PV7YF
oi~q)TfIQZ5IyYdmttBz3fH<_8y=;m3%W6n&cD7pExGylDoLn_G*aWP6CPcInY)BOCR~L@Z>C$Gly+=XH0y`_A6gEdWHJzv3|C3?
oOsh}ntreD1F$^q_`_Lv48*~CsjTsS;CWFaNSqBNDt!+$2|-lg&FIPu^;S4bdVGh);~~5wfva02it4>r&kq}DN>!rWQLQ3cZWNC)
aETADlC1jDS+YaR%;7<p;|(oCdl>pDmXoDWInP<S`N(EpIJNKBO&VpcL2ykf(<x9Y_~mk%0eQ2~-E4~~!vFf=akD9Ffi;;w(YSKb
BeFiAlz=;Ed>Vl5QbSpLBdZ|IbSEN=Xw4%1E-!@8U=10UjDErI6Yj0i4`xhsd<eo)&ou!k)IgXz)@XS>j0!*jOSDv~3qW*B45A_v
qM6Zr8lnP1ZR8O$suO5l+?l)Q$F{^l0mTU~T^`wP_S0#A96qbuM~!VL+49oZ7`o<Iprxp+fo${P65$g!f?2@HYT8|ka75-OA=yH9
(U2~e8t5F(>B(->?#HeOE)WtxdyqhGPSMK8{x3o4pTVKDdx)t7UA5#w>yB8T85OI#eog49W>7<v*D=1ahMv;opYhO|4I$vIpnn6%
gr?e*E6A4sxu1kYR89CE&{9i0$YIOJ^&gZy#MMDGMsa{*fzq&8d9+TWExG*SDWtgfq^X-d(y~26Rd{^DjUHOL@by>YINt|tBo^;)
&dJr4_;INF=zf6NdXFPITouY&Uc-&+d-!b4n1nrnCu(^cc~b11X}3`ESnj&T5z)E1uQ!<=G~P+c*srscgv4(?(0E;wbV{box33r>
!L^N5LTpZ8^4B%CTZJ4=vO31eL&ucf5wBGb44unOq^;d_B){K<&)2lMfe-1U_Z(T9Gz7C8et>!?C(Zq_h=28^w=P%yK4Lc$^jj{G
%q7SLKDS2g|KH^Ao!9`Ta(Us<_RYfOdlL`Elc9+GX{&yAN3WXB|3P9Rx#|@fQX2b@@op8MF;=Yw#@XEsf4CkUfb{spg&mkpnzv(S
(8!$t@PuBuRBx~B>=(7ov1^OQ*+`ccalUg9aIp70n}xY`e%!&=$t*bT`}{I+dQ|ISjRCl?gJs-Bl~$gnc|sURa8xbk5dK$_``+!|
`zN(V$H1htpeq39{O*mQAF)0%V1ylG3G7r}EvxrORCcf<LLfXc0f>B5i62cHc)_#`>B$x{0#K}`E{4Gv$|wEXe&88dTNHBJfKYm7
2d1?Gv}>8N$51=<#MI!hAZG0~+vA+yjBx$&G1!#GSVR<7I+qWJf!vH<D)`IY@F1C+0<{auS@)}opcQAb9g2v7fM+zknFY_2E!$>c
fg}*ur|Y^xx_H#EYWsQ^baPNm%i)W<&GZfmErd`G%5Ya$j2!UG=hd#WT=e+mGQsJIIb_wuy8R$2h)9mw8wHb5g_|j-YLXhElOtL7
3a(cPY?51cTEEhSqyQ!}c)qgl+w)i*tM<-VTS{Ux_&$AIwD)|oUDW{$Sx55!l1Z-X!d_vjSK7Ep`0-H95^{$2#<c!!E@X#dL%_4t
on2-)jmgh6Z*Bw^>cXqGl`kf#X%(RILd%R}%H{XiodMy|!w%GaUsxN2w$Ss46JI~X*-YTsVqi-p&=N9}ZA5k(=H+MV=m0cV#H{^b
&IzHRz{5foV79}kSEYZZDzFm)Be{8Hm0l`*y+OCA+ogDYf-ucfeN{wQP4Ol#D;|{aN<gMK2)h)c{arTR>JnzRxIaM)Jkp$>E`0cn
S?2_viEu)ewe*EcWB@+SY-?&#%R!pzXd}A>GX8$Yjan-8f0vM9FLXp5qg;5K?+OW0bD^O+2<;^P!9b7q&n@QOb2_g^+B9}htY)}V
I1T{kinuLY-`CxJf-+WT`vwRiz*ml?OmwHV>>Kky<^(IqLSM+8f^VbJW>`%*!C&Z|V!+z>Kzsp<@sfR%|HO<k)NY~e5qbhDN9`g=
HGuWO8sX@)8Tnoj5rTj>gD0isf#C<nGf0a51ow<Q8cRPtZR^EwF_C00h_8z=5^0oFuBWXRiGvT$muT`6PI9Zc1y7WNmC?Kr5f4wo
txv2FH-LsasOt-Wpv@+|xr`nYeNV?qENPz?>8I&85`3p7t*OC$i<<G471|c+P1bel*-6n{Aw?eI$)^XN(;rk~f(~5=KbA^oaTcNW
Y?pb&=!6^DR;wZP=tBe0w;I_GGxEjZt}JAts6qUaEl_&g!g9FA>XLNZ<N)&iE7(tdjd%WyZ`nj`H*sG0H;&7YKipZ)cT%@u4_N&@
_^MHc18Z}I{$1ygh|bJ!vv7*oc!D;rThTB?^X1i3uInwr=rI=+FTpxal$?Wj+6fbV+H&JMCIbteg;+a|`Kclo`WcpVSDO5MOuWOS
#Qm^Cv1RcxF|FNCuI{+rqP^&o=iHGEOlvcw;UQP2e0C&(9Z}w?&|S1H+^RoR&;fJac3Ug4O2vln(lau8wZ!rbQP#*u<1Zdj(6_P7
#`zbI8#$<yZP#nyOvyBaV8I9V<Pr*CO($eR7RuTE3tYg8{t11<#49Fnl#G0={sMejvS8oM_Fxq5Q_{By(eEox0zOq4o*;Hii^;81
B$2s*sETq?Al|h;q+*n~g<5I|CR%ccrq1FN&~FIbqT>v+oF^pOsi=z?)PlBL6$(qd;k<ejsg~yJ0^5gR=*${0s3_IK?W){q{pSya
qKpl{-C{x_w??uGdIiwrn(QP#_ApCO>IoYqZ8DlU(v4wK;>FRcP`~>ba=Ng>;ekdCm;ONCB0o-JjVKvA2r+CFHYP@OWKUb&rewA#
ooD8Z`#oKYH<1?*BUEq)2|5MmShKnzhWw;7ggl2-p!*)9N%UAleHt$f>fAP?A;jZm#71aYRhdF`9C|b<styO??!$@qqZrN0lAo+O
`NIrBNg+)lw+7KV=)mI{#t2XpAwjsNz<{q)hElVrKi*fY%Htd)B1kmc!X;6Tp_zZT?-6Lxdj5(=aGDSiH=v>aFTj6w^7PuMwrRlR
R4_wuRrPfJD<AobM#Km;?t7+)wGPB06qIE#vF~_tu$tl<QnV$iCyyI=<eFjt8FP{lcqM>}^DKU+V$(#Me23@IN90X&|GD3K!G;^E
S|MZgWQHdx_LsBy1H_u$(jbN^oN;)e%@9H?B4vg)<3uMzaG+u|Jj|g{$c;F7(a3n}*P;R}i?I$Bp^k)M`?3iRC1aQXs1kMq=x%Hd
eiAiffSX!s!z=YuW7bBYK=Shhh&q_XhH(4nA}`J`4co#DN`Q{@*?yB#Rt9B@4tSfIpdh#toT^TjGr^K5Z?<2LqvXgYdYII;6<8eU
Non?!srqG+@7D@Fa@7+Y(qXEa!4KLjgV0MX^^|9;PX*P3j>ZQNN`blm)u|5#rJT#ULE=G<otruh+?00b&!lE>xeVFk!d2&O?9kK^
-N@NDi{EOy`p^(vU7cC7^OoxgEh;K_^`*zAipg_AJMU8`Oa--3+N}S_ITvMwR6MAbK)H8ac3(Inm_Ey75S}H<hDP+h&@d4%zW1|q
ia-ouELRE~CgXF*gjvn#uBpc@p7ux{(F3nVmlAnPzeobkj2~Potl)*U*my^bUv{$ZjUaKSZQ;&uTlN{k1qWcQcQQ%1&na~!zZC9I
HO6!ma4y@dHDcrY-s#KCXnaLB&qdPrTfdbP(u7@y#@Qof;aIg&VMPh6!PP#tO^q~~1Q;l0p);mkLC)J=>%V5&kd<!lh|w^?2fzI^
Jw8lyGJU!*f#~7M4KW1M0R6l&<*B(IW(3(}C=+csrAc$`-)PPX9XVdYV|8T*<}Ph?>S3drCcXGulxiS@<J!awd<!z+s$R}U-U)FR
f5D1$+y*x6W2S_=SWG@%_uyp?5DW#8|IYG@7gT*&JN7%JBDs|>iW$Zg#m=vuA6=SS3us}aj8fKC7-pY#!Vd`f4sn(X+70?pO8HzQ
k+CcNi`Xo4w*!9}Uc6b%gXtI`*?_^+w3UF>e3GnO0aerZa>?Zp|IKVZ5)1W*u%Jh7a^h_<c;QTB+72Jbp4&rd`v16nDJwCiG-}u}
7F#&*EECg-5bxkGyhN-zOL^6tC$gw3ltL}Y*1Wl#w(rsctMXA5nJGVzGD6AX1#@}6X<x&3X-6q1>7G7PP-t=+67Cf!7+Wr`Q>!HQ
U(vLDbL`S-=bP$~lc=W`Ygjbxb8A|f&^elMVj65o&hhDvF}?#z#ma4uSWMQcQeKbIw-4^+P`Q_zGYWlp&KhQ&8!~_MKl&faaPQZ#
n&}JEEHi6DbTrjF$@McV7GLe%(L-*f^yjpw6_~zF->E7$0#P>bm4wD=Cg<%!l&rbiS4X^TcJJ6yis5#r{jx3q##m?=lQb6ljuFwD
fPUP#n*MbWz}#JPUq(@G7F2?r$QQ*8l20%c-LCEg7ZjgwJUGRGm}_2ux1S{gaP;%(0%J&wC;g(VfjucqjZ4JLp2KNwC?(oEwfXd3
B1p0L@>urj?33BOuv~(TtB;S$82&fA#{iY^I6<93yXVAY`~FHfkMNX?&}=rWo>?R#k}HoE8zz(}W{;O|%D$mt1Xv$I{1JX(HOtMZ
1dkOB5>lwoS<h49Uq!ezDb!BF2zl(h6WClB>I%wQr6l0%Fo`Lh-qi3{49Rt@2a>7$1>yQFho#gs!x`izq}f3*VI(3TpkLL>m2|k<
NZERww*>cQ=&?^nC}x+*2Z;yp0Ut)Uij?~|I3>LR@Lslb%j@R1<Y{F*g&f?(6sf%h-xgMgZCGcJBv}gf^5hhgW6KX%arRXp42_7V
l7zAwbYXXNNAsrc4I$hAN|VC$LrmONa_2Mz`cyv*?140Y16nyIUV08SC9A)BN@uT+FLf!wYR34L-+IVSK$|4%1-|OlaG41=;AwMc
YCBJ5YSo3xsGVxM3>qO1?|M`(>rFC^tYyj4qsrqID@|!!2aOml$rQZ~m>MP!o1!`_n&&l%{r!u|CP&YUoWA;ySa?rCKGiAlLXF_9
lzkfyD^eAJsVC?hw9l~unuxCQH5y?J1Y4-5)%xj{{p3H{+&QiHaTo%X!1=fc;1GMp+5#`6(V~2}92>xb5eNVQ7=~mt;VJZT?g34|
7oyQkygFLK?2EDwGuhMgfpKt)y5>@hC*jOzavmy9XW(5>L|wjhte$=`lS1U$6b{2;bwtfQEorQW&;75)3c_=GlDA<k8?ewgKK4o@
%;uZ4GG34#i|_&QX#o@`>HYX=#oelR9s6W+S3T&j(*|(6d6WwPs(L+x>E{%^I{q=RQFIT{d?)9aPQP*s$w*c<AyVp(+HF?|5&F#M
Y^Izi{wX7~H{->NAG+W!Weg~zZI?Z%;F$RI_9o<}1#gDoz$1U4w>$}z+|cx+kMZZ2<%{T%{rck2nFkMR)TR6PqJ{Lpl}gPgYoABR
n)(v2&&h!lH6De5VxT7R=}XrnL>_2gEBS@&xmMTJ?n<60R3udkWEqR%lM@s`iy;ERk%x`TOZxnGh|ox~k89JkL#?K1+r#w0j8&Ns
GX+L%6aalo;sQL_Xzg<<QZ76@OpsLQHU~qHJj$vJFMfp&?xIR$KyIza1oL9{lW6fRqA{TD@-(9OWHY?Wf_8?kBR_7vhE{E0d1B@9
DO;Q>7c?O6h+R+9R?w|RQC?bKI!sJ)1x%S$RKF4*Qc|y3mY|L>jaxxJMx9s_=kEvb3J*G>jp#*T{P$;t#+cyC9;&2vvL`tCqtr#w
tb6#|A`6@BQ|z~Gd5Te#2jF2&c<+s2ChFwP-$uMWV0{ZviZ`{FS}^}yN`}xr(ODv)5j0z=o#K$_u}wXEp0@?Q^ke0#0(VMBAr5tD
7nIJIys`BYUwyZsvek(opV|5GggeQ)<yX26>b7Q|H|pvs0>1>MwJiYZ6<w8wRT_s9n7%9|<^316e-zp!b8oZRhJKSS&6dK8?c3LP
zt-|cQCs;oy_NW$@PJYM3W641!ClnfPUHH?jDm3UAjGGv-}@_9lXWW7>^RQCk}fJrG5f`RP0I9PV=cg;k+xyCSd`3PWtdgcSmY&M
k5p+RybybF2<<1JoT>@-Pr~;}RwGa#sJ+xx0@je@p&=aq_HAK3ddoZV>A@DcZY~(2YcgDNLUWRMy;{O<4lmwapBx#8#GOi0Ikf<V
VB=XHzRniz*iK+Pm|TR%SzaIKc3l@&y5H*YEX*h(6<PXofxU<IjMg4;g{NvxEUN};sgE3}tUCck1gsI#5`k((S<Y1)euy=P(qkT8
v~&Ch=PfwF5>o%4wNbd8$iZ;A%L4$xAOuwT)3gRcX-^*!v~1?5;)8$my-v-t=dZ7TgD{-$sLDk=uI5^g=@Z`4^){r`jEP7oZZ-9)
=O#kG^&`nb<Qlg;OtXCsx#*dO-Ii?^W|IoL@>dF1E9AMxO>mS8h!PUu5smilI)zn+oE$+~M?739Y`eSk2h2OORcIY3>g*oNw4q@F
`+W}NtKxnNmXV%)ebw^L$I|5-DK|QjinkJ)=lww(t_{>L|ES&1TG;b=c#f1Opl0(a+rGAx5s`M^1REuw*SL&0I32)MflNI)O1oMF
Z_n!geYHA@=8~TEYC1EULBp;<TGX&C$WfE5T<L7<j{E%cz}uH5g8m(9N*!zTkOf^GS)9tPdULXK6Q6n$6^MaLFD~*R@Lit&6%wb%
g}oS&(&3Z?n-H%RhQQrykt4JTA$6Z47`ee_H^kX^mYh>ZQ_Al^CAOr>_!airlPVUAb=(lr{S9VBI<2k$&9RFF<*Em5(ranG)6$$b
stU>gAI_fldf+hpLNT$>#WgF3;NGizf+T{a=Tam+48<WmS~8h57vAMl;*oIU%yu#;5%*FHb4?OL^0VEg7>fVf8sj;0y6WCv5B5ZN
@nF%<`j(|B^=*;6Kt5lcFq8qHl?kmJJ1iHv)I~Z)P6iwKIfG0Lxl#xnk2TSH$l+BE0F^5<9<vl_5HphjXMH0KfM{3ii^Nf|&|CMP
LDbd-^%c*y&!CKuOr9%s4gY<gHV<kf5N1NbT&gfBwW=Mswo=5CuC6SdRKGS5Y^p5as34;4%C-q=w;;=z6E2kh^$V8|bW*Eyl#gMt
i@o?{S7|b1E?+J+*GR263Qm)+u8Ue|3zm)aSUjk2MD`l0tGXbF{^q1f43Dx^;ZiY)ci=|ijGDXT-q<d4kM|+Exsyy9d)h}t5)*3f
$#5Zx8p}6l0SiB=T7%H!mbf2li4WH0K-zbFQ4moJWv`Yby&l;u<OIZVwwH`D%WjiNavEP5%~?O*Qp4S5uWtwWj!Mq+&N>^vPQl!e
v$R4&2|3r0ser|jC_iMc#$1s1VTpNanElK?tcFsF3y<yGbMm}T5A?2LS*q<GWalzM^kYvIZt}qSY95(?;PAi~?Z7BqgebF=yBkIY
bHq4*qJD_OF&k7T5jWNqT!q#<>7C}X(*ontTwQf}mF*}H!?C%yEyh$tghDw@O<T1yJ|r7|{-}2&3)2xRp>zwYD-S*WG&FKm?Isc3
dKNpY@kxe*sW#mCIoSQC^P1pul5%y22mZg0L41mrP531<+S<Yn;1W$FoeoJ|<B*$p&2=jLm7r_V+4u3XJw}`&KRjER)M?FN40P9d
;04_*{T~Hbng4l+Vya}4&bOOS?{O*l7t}6QAi=XT=qRKC*O%ESTQ|Ead8+Fo48kX{y)f;l?VpY03KF3IY`Ge$L{Zc_XgEJG6q*Q+
>NqiMl?VT`APr+w;_8jz!`;jF-CsPSYjt2)uuY%pZ5Uv_KSuG{g}g(aCB5EXo2{+`NrLB@f%;cYK%=Yeof!<9CrIvC>@mV4QS)ph
Qlg5-O{}empLM~xM;Si5+&wI=QR(XiG&Xe81+3k9nN5vS!{_eY@`teA6R@sG28E9`HWU|+a}u;{@@S%5-s2jM(B?WIxL(KwQK|=8
czkGxXKD*1#NjkRlE{UL?%*>Xy?0>E4!oUUsHa_Et5};YoibsqybGc3YwYj*8J~=UZ)GozT&ktYNdOsoDo!v;@$={2fZyP^D)8o4
ly#UCSv-e2t8r<hU=A1|>3c$Eo}NpyHkj7y0&*a(ZDTQJ(Ez;mzU}x`Nt2|v1PXf^vM7AxXEaroOT^^>&0Z_UG;p)gc2I#EdWMm*
%ScllCB{zJvWbJUf5|B0j9vyOg9D?efP43REg8Gi>MliW6sP4yFf342Qqm-_^<d2e-^;$yN1d#r^Z{gGeOP~FfJWfZgzGMi`E#zM
qZ{%`q7gXziq$-Q7gIMEV`3w1)wE)leI_`=aht=yXa%IPH`cIH><{JYK0EL%`K=y9)&J2*iuZ<2V7t_h7sADk0+j4m_;=#XU^Nkq
!Gu(AMjXeGNT~2SL>2lu4+gP(V;PaewGZcm9`jSjAIWdUbHEnEj#{KdDs#KDOo4_hjc&o4CALABNocb1L3k8HMH<L_<iET(!;H2>
2qF)he#*o}fkXXvci$7W(z6LBG7rin1mHomzB$j%Kj_;bks}}V66^vnlI!_hhY8Tj5Y|`E#(5?n)-0d=zo&Z?73`&=R=G`Vk@J;*
r2Z`hHxu?EOVI*Yzy2QI3!>4-h`W-yLRKWDt9tM;A~GQFLxidt`q^0EZ+cNTYtgon&il6u0k<P37@<_&8fLeq<icLZ9r>0q@FgMG
dh%~f$e$QV?Dn;13n|`o$u%QFd^RnXTK9LyUQ%7Ko>$VobuXn2kMr+B<uB}WC`37Xw+#{4&=4_bGf}swqFe`Mx2<s6q)G{2HCNsq
c_usIvh;^a@`!+Ufi`{)6t0l5(eg<LEoW}7BeBro6c0J(rh8<;5y(lp_c@c*`G)UuXs{iZm$~$#+eF8*TB)JYeBk8zulffzrpzYC
JQb5kR3usZYWg0rtn`Y;+0ekQ=*`qO)&5oepD9k@&w@7bYgg2Wh}boSqF6obr?rHr*d@~Sl{6A^Uh?MbLhZFMDpMH?mG-GBM+o8B
woK3g1idWLfb278covIjka(`gUsubhR>bSV^FJ8(VU*eb1u{Q9*#WHR>0I}D0vI6=fH*q{0F^12ek$>T5=jZ8w&EzjR~G*Dwz-@h
Li5Mk@F{RrkptMNX5hvnV8&BD@i-jA-{IVFaB+$77gYj}*f>;+g|0E86`;$j1+Ww;r^c~~54f}H1oG^vyyk-fIH5tB>}rs+5Cm5f
f?V8+owTBxg3p9>glgOIP!!;-+KBQ14Ondw-OB}H<)aO*b-4f_zW=`GK<XFT2cLi@w6H%Tnz9eAjH>Vz^PYV%a#;rxf`~53Zg|~l
=w>l#Ad~8<6V88F1BBJFUxYnlbYl~*Ipv5+xkQ*br_s)Ahq@+tVPS~W6!VNB25?GQ)OCkev5?P%&?AM#q6-HslP4S9sQwNwHJHcY
nt)}|$l11}To35ZKE@zBs!`c^E$fvmb(|eB(iM4bwx~<kWXGMQj=ChHUXce>iauGdfYjjzmro0hz5u+abwxnw=y(nZ`0ITw_(AJI
xFlzZM=Jz~Odrr=)q1Us7OOjaMgRZ+C=zNg)&`?%00Hu{0sOrLhR$rGvBYQl0ssI200dcD
"""

def restore(destination='.'):
    raw=lzma.decompress(base64.b85decode(''.join(PAYLOAD.split())))
    assert len(raw)==COUNT and hashlib.sha256(raw).hexdigest()==SHA
    files=json.loads(raw);assert set(files)==set(FILES)
    destination=Path(destination);destination.mkdir(parents=True,exist_ok=True)
    for name,(count,sha) in FILES.items():
        data=files[name].encode()
        assert len(data)==count and hashlib.sha256(data).hexdigest()==sha,name
        (destination/name).write_bytes(data)
        print('N40_SOURCE_VERIFIED',name,count,sha)
    print('N40_SOURCE_CAPSULE_VERIFIED')
if __name__=='__main__':restore(sys.argv[1] if len(sys.argv)>1 else '.')
```

Архив читаемых исходников, всех точных отчётов, исходного пакета и фактических логов (`N40_handoff.zip`) — дополнительная копия. Встроенная капсула выше достаточна без этого архива.

**Незавершённая цель остаётся own110/weak000/E≤249. Проверенный новый результат — конечная отмена лишнего U с четырнадцатью сохранёнными own211-потомками, а не отмена последнего Q.**
