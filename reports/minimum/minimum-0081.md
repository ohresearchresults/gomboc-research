# minimum-0081

AI research report · 2026-09-18 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# NIMBLE_WILLOW_98_UPPER_RECOVERY_AND_PRIMARY_SOURCES_V1

**Исполнитель:** Nimble Willow 98. **Назначение:** `minimum-0081`. **Дата проверки:** 18 сентября 2026 года.

## 1. Результат и граница утверждения

**Заново восстановлен и действительно проверен точный однородный выпуклый многогранник `FUSION258_PN03_C1374`: `(V,E,F)=(258,687,431)`, `(S,U,H)=(1,1,0)`, `C=1374`. Число C650 не аутентифицировано и не принимается как проверенная верхняя граница.** Это восстановление доступного принятого примера, а не новый рекорд сложности и не доказательство минимума.

Унаследованная нижняя сторона `C>=34` относится к текущему внутреннему синтезу; её доказательства в этом назначении не переисполнялись. Поэтому интервал `34<=C_min<=1374` можно использовать с явным разделением: нижний конец — принятая внутренняя посылка, верхний — новое точное исполнение описанной ниже проверки. Первый открытый срез нижней ветви остаётся `(10,17,9)`; здесь он не закрыт.

### Что прошло свежую проверку

| Проверяемая величина | Полученный точный результат |
|---|---|
| Полноразмерное конечное выпуклое тело | Выпуклая оболочка 258 рациональных точек; все 258 действительно вершины |
| Максимальные грани | 431: 361 треугольник, 64 четырёхугольника, 2 пятиугольника, 3 шестиугольника, 1 семиугольник |
| Настоящие рёбра | 687; в интеграционной триангуляции дополнительно 81 плоская диагональ, не включённая в E |
| Объёмная плотность | Постоянная, равная 1; не массы в вершинах |
| Собственный объёмный центр масс | После точного переноса три первых момента в точности нулевые |
| Устойчивое равновесие | Единственная максимальная грань с ориентированным циклом `[158,163,161]` |
| Неустойчивое равновесие | Единственная вершина `138` |
| Седловые и вырожденные равновесия | Пустые списки; нулевых обычных рёберных примитивов также 0 |

Индексы начинаются с нуля. В порядке первых встреч максимальных плоскостей устойчивая грань имеет индекс 132. Использованы 512 ориентированных треугольников. Равенство `258-687+431=2` проверено, но не подменяет проверку геометрии и полноты комплекса.

## 2. Точная цепочка источников; почему это не C650

Доступен источник библиотеки **`material:[internal-source-reference]`**, название `source-research-journal.md`, 1 737 149 байт, SHA-256 `1e54e3291077a0f4f0fe4588bb6793b823c7f904caab1c1ac8712bde2c014722`. Правильный идентификатор для чтения включает префикс `material:`. После первого чтения последующие диапазоны закреплялись этим SHA-256.

Полностью прочитаны и декодированы именно две необходимые исходные единицы: запись **2026-09-06T13:56:32.877Z**, `Accepted exact record: FUSION258_PN03_C1374`, и запись **2026-09-06T14:17:23.665Z**, содержащая полный четырёхфайловый проверяющий пакет. Их охватили чтения UTF-16 `[1463500,1492500)` и `[1492500,1503500)`. Заголовок первой записи находится на позиции 1465863. Необходимые блоки прочитаны полностью, а не восстановлены из поисковых отрывков.

Прочитан также конец файла `[1703778,1733778)`, до EOF. Последняя запись датирована **2026-09-07T04:12:47.886Z** и прямо сохраняет принятый рекорд PN03/C1374. Поиски точных строк `C650` и `=650` в этом источнике не дали совпадений. Это **граница данного сохранённого снимка**, не опровержение более поздней параллельной конструкции. Поиск не объявляется исчерпывающим аудитом всех возможных названий во всех источниках библиотеки.

Поздняя запись 6 сентября 14:32 отзывает принятие другой напечатанной таблицы RA04; она не отзывает PN03/C1374. Не следует переносить эту коррекцию на наш объект. Старый C1386 не нужен как внешний родитель: конечный PN03 содержит весь исходный целочисленный ряд, операции и сертификаты для восстановления C1374.

## 3. Математическое содержание выполненной проверки

### Координаты и настоящая объёмная масса

В PN03 записаны `D0=10^18`, 258 исходных целочисленных троек и 81 упорядоченная операция точного решения уравнения плоскости по указанной зависимой координате. Это **координатные решения, не ортогональные проекции**. Все окончательные условия компланарности проверяются после выполнения всей последовательности. Получаются рациональные точки `I_i/D` с положительным общим знаменателем D, имеющим 2274 десятичные цифры.

Для сохранённых ориентированных треугольников `(a,b,c)` вычисляются целыми числами:

`W = sum det(I_a,I_b,I_c)`;

`M = sum det(I_a,I_b,I_c)*(I_a+I_b+I_c)`;

`g = gcd(4W,M_x,M_y,M_z)`, `A=4W/g`, `B=M/g`, `Q=A*D`, `P_i=A*I_i-B`.

**Точное определение тела:** `conv{P_i/Q : 0<=i<258}`, заполненное равномерно с плотностью 1. Объём равен `W/(6D^3)>0`; исходный объёмный центр — `M/(4WD)`. Повторное интегрирование центрированных координат даёт ровно `(0,0,0)`, а не малый остаток. Q имеет 4583 цифры. Полные целые W, M, A, B, D, Q и все координаты автоматически восстанавливаются программой; никакие десятичные приближения не служат входом геометрического решения.

Для ориентира только: объём приблизительно `2.2136653964304474`; исходный центр приблизительно `(1.2809199210142977e-17,7.78728121310209e-19,3.832292863913185e-18)`. Он **не объявлен точным нулём**: выполнен именно рациональный перенос.

### Выпуклость, полный комплекс и все типы равновесий

Первый аудит проверяет каждую поддерживающую плоскость против всех точек; объединяет треугольники по одинаковой примитивной ориентированной плоскости; отменяет внутренние диагонали; проверяет замкнутые циклы, противоположную двойную инцидентность рёбер, полные контактные множества, все полуплоскости каждого многоугольника, ранг 3 в каждой вершине, связность и связные циклические звенья вершин.

Второй аудит получает максимальные многоугольники, заново проверяет все поддержки/контакты/полуплоскости, независимо восстанавливает настоящие рёбра как двухвершинные пересечения контактных множеств граней и заново интегрирует массу через внутреннюю вершину разбиения. Среднее вершин используется **только как внутренний апекс интегрирования**, не как физический центр масс.

Для S второй аудит проверяет перпендикулярную проекцию собственного центра против всех сторон максимальной грани. Для U применяет глобальное условие `max_{j!=i} P_i·(P_j-P_i)<0`, не только заранее выбранных соседей. Для настоящего ребра с концами a,b и внешними нормалями n,m положены `e=b-a`, `L=e·e`, `t=-a·e`, `z=L*a+t*e`. Седло существует строго тогда, когда положительны `t`, `L-t`, `(z·n)(m·m)-(z·m)(n·m)` и `(z·m)(n·n)-(z·n)(n·m)`; положительность определителя Грама также проверяется. Проверяются и граничные случаи. Первый аудит использует другую, векторно-произведённую форму рёберных предикатов.

Дополнительно проверены все сохранённые положительные primal/polar escape-свидетели и достижимость единственного корня по каждой цепочке. Корни 138/132; `K=3467702`. Для каждого ненулевого шага `(n,e)` выполнены `a=n·e>0` и `K^2*a^2>(n·n)(e·e)`. Поляра берётся относительно **того же физического центра**, не её собственного объёмного центра. Эти свидетели дополняют, а не заменяют полный аудит S/U/H. Их дуги не считались рёбрами комплекса: точка-свидетель может быть несоседней, тогда как E и седла проверяются только на настоящих рёбрах.

### Что здесь действительно исполнено

Обе реализации геометрии и механики унаследованы из полностью прочитанного четырёхфайлового источника; их нельзя выдавать за две новые программы этого исполнителя. У них общий точный декодер, но различаются интегрирование и механические предикаты. Здесь они **заново запущены**. Новый полный `speed_patch.py` лишь делит целочисленные нормали и вспомогательную центрированную таблицу второго аудитора на положительные общие делители. Он не меняет определение тела и знаки предикатов. Это точное ускорение, не округление.

Холодный запуск из новой директории завершил все три стадии: первая — около 25.96 с, вторая — 26.02 с, последняя — 3.20 с в данном контейнере. Проверены также точная трансляционная ковариантность объёма/моментов при переносе `(17,-11,23)` и геометрическое отклонение двух испорченных границ: перевёрнутого треугольника и отсутствующего треугольника. Ранний монолитный запуск упирался в локальное ограничение времени; завершён именно приведённый стадийный запуск. Исторические времена из «Фигуры» не выдаются за новые исполнения.

Доверенная вычислительная основа — приведённый код, точная арифметика Python и стандартная библиотека; формализации в proof assistant здесь нет. Допуск изготовления и сохранение класса после округления OBJ/STL не сертифицированы.

## 4. Первичные внешние источники и научный статус

**Проверка внешних источников выполнена 18 сентября 2026 года.** Ниже разделены опубликованные теоремы, препринты и наша внутренняя проверка.

**Существование уже опубликовано.** Zsolt Lángi, [A solution to some problems of Conway and Guy on monostable polyhedra](https://doi.org/10.1112/blms.12579), *Bulletin of the London Mathematical Society* 54(2), 501–516 (2022), впервые опубликовано издателем 17 марта 2022; [arXiv:2008.02090](https://arxiv.org/abs/2008.02090), первая версия 5 августа 2020. Теорема об аппроксимации и её следствие устанавливают существование однородного выпуклого многогранника с единственными S и U. Это не конечная таблица малого оптимального примера. Поэтому восстановление PN03 — не первое доказательство существования.

**Опубликованный дискретный пример с 21 вершиной относится к другой массе.** Gábor Domokos, Flórián Kovács, [Conway’s Spiral and a Discrete Gömböc with 21 Point Masses](https://doi.org/10.1080/00029890.2023.2241336), *American Mathematical Monthly* 130(9), 795–807 (2023), опубликован онлайн 14 августа 2023; препринт появился 25 марта 2021. В нём равные точечные массы на 0-скелете, не постоянная объёмная плотность. Такой пример не даёт верхнюю границу нашей задачи.

**Внешняя нижняя сторона, действительно найденная в первичном источнике.** Sándor Bozóki, Gábor Domokos, Dávid Papp, Krisztina Regős, [The smallest mono-unstable, homogeneous convex polyhedron has at least 7 vertices](https://arxiv.org/abs/2401.17906), первая версия 31 января 2024, v2 — 5 июня 2024. Утверждение относится к собственному объёмному центру и U=1; используются 5943 системы квадратичных неравенств и проверяемые сертификаты. Оно не тождественно внутренним V>=10/F>=9/C>=34. Подтверждение журнального принятия этой работы в просмотренных первичных метаданных не найдено; её сертификаты здесь не переисполнялись. Это не заявление, что V>=7 — последняя возможная мировая граница.

**Целочисленные моностатические примеры не следует переименовывать в 110.** Krisztina Regős, [Homogeneous, Monostatic Lattice Polyhedra, or the Magic Pyramid with 17 Sides](https://doi.org/10.1556/096.2025.00142), *Építés–Építészettudomány* 53(3–4), 203–217 (2025). Опубликованный PDF указывает принятие 10 июня и первую онлайн-публикацию 8 июля 2025. Он даёт целочисленные реализации отдельно mono-unstable P2/P3 и monostable PC/PB. Эти свойства по отдельности не означают S=U=1. [Опубликованная версия в академическом репозитории](https://real.mtak.hu/229740/1/096-article-p203.pdf) доступна.

**Есть свежий внешний препринт с явным объёмно-однородным 110-примером.** Tancredi Schettini Gherardini, [An explicit mono-monostatic polyhedron](https://arxiv.org/abs/2609.07827), arXiv:2609.07827v1, отправлен **7 сентября 2026 в 18:00:10 UTC**. Теорема 1.1 заявляет рациональное тело с `F=56946,E=170832,V=113888`, собственным точным центром и `(S,H,U)=(1,0,1)`; в наших обозначениях это SUH110 и, по вычислению `2E`, C341664. Это препринт; журнальное принятие не подтверждено. Его численные данные и сертификатор **здесь не переисполнялись**, поэтому это внешний заявленный сертифицированный результат, не второй наш PASS.

Авторский [репозиторий certified_gomboc](https://github.com/Tancredi-Schettini-Gherardini/certified_gomboc) доступен, содержит данные, сертификаты и исходники. Его существование не заменяет повторного выполнения. Независимый внешний replay полезен, но не нужен для приведённой самодостаточной проверки PN03. Нельзя без проверки переносить ограничения чужого сертификатора для простых вершин на комплекс PN03.

**Историческая новизна не установлена.** Дата внутренней записи PN03 6 сентября сама по себе не является удостоверенной датой публичного раскрытия. Внешняя публикация существования, публичный препринт с координатами, внутренний найденный пример и международный рекорд — разные утверждения. Здесь установлены точные свойства конкретного тела; публикационный приоритет, полнота мировой рекордной таблицы и опубликованность внутренней нижней границы остаются отдельно не доказанными.

### Точные опубликованные конкурсные условия

Первичный источник — G. Domokos, F. Kovács, Z. Lángi, K. Regős, P. T. Varga, [Balancing polyhedra](https://doi.org/10.26493/1855-3974.2120.085), *Ars Mathematica Contemporanea* 19 (2020), 95–124; онлайн 10 ноября 2020. В §4.4, печатная с.118, формула приза именно **`p=10^6/C(1,1)` долларов США**, а не `10^4/C`. Предмет — установление минимальной механической сложности класса, не произвольная конструкция или число граней. По сноске на с.95 решение направляется соответствующему автору (Zsolt Lángi) как принятая публикация в математическом журнале мирового уровня; требуется также общее признание математическим сообществом через два года. Финансирование приписано Otto Albrecht. Формула и сноска проверены непосредственно на изображениях страниц PDF.

Это установленная **опубликованная формулировка 2020 года**, не подтверждение актуального финансирования или индивидуальной правомочности заявки в 2026 году. Свежего официального изменения условий либо подтверждения выплаты не найдено. Сам по себе C1374 не является решением конкурсной задачи минимума.

Граница внешнего доступа: отдельные издательские страницы возвращали 403; для соответствующих текстов использованы первичные авторские версии arXiv и опубликованный PDF академического репозитория. Это не означает отсутствия публикаций. Переписка с авторами или организаторами не велась.

## 5. Что остаётся недостающим для C650 и полезное продолжение

Недостаёт конкретной более поздней исходной единицы «Фигуры», связывающей **число 650** с полной рациональной/алгебраической геометрией, окончательными максимальными гранями и настоящими рёбрами, точными объёмом/первыми моментами и полным S/U/H-аудитом. Для C650 должно получиться `E=325`; подставлять 325 без восстановления настоящего комплекса нельзя. Не получены ни такая буквальная капсула, ни соответствующий ей свежий точный receipt. Недостающее не заполняется чужим OBJ, названием файла или одним hash.

Следующий полезный шаг — при появлении доступного продолжения «Фигуры» после 7 сентября 04:12:47.886Z извлечь именно окончательную капсулу C650 либо её действительного преемника, применить тот же геометрический/объёмный/всерёберный gate и сопоставить исправления. До этого сохранять **C1374 как проверенную здесь верхнюю границу**, а C650 как неподтверждённое сообщение. Нового нижнего исключения, нового рекордного тела и материала невыигравшей поисковой конструкции этим назначением не создано; сохранённый полезный метод — компактный холодный replay со строго эквивалентным целочисленным ускорением.

## 6. Полная восстанавливаемая капсула

Ниже весь `recover_c1374.py`; он содержит полный PN03 и полный JSON с четырьмя исходниками, а не ссылки на них. Внешний архив не требуется. Среда фактического запуска: **CPython 3.13.5, GCC 14.2.0, стандартная библиотека; assertions включены, без `-O`, без случайности и сетевых запросов**. NumPy/SciPy для приведённых команд не нужны.

Сохранить код в пустой каталог и выполнить последовательно:

```sh
python -S recover_c1374.py
python -S speed_patch.py
python -S -u verify_stages.py first
python -S -u verify_stages.py second
python -S -u verify_stages.py last
```

Ожидаемые терминальные маркеры: `PINNED_BODY_AND_COMPLETE_SOURCES_RECOVERED`, `EXACT_POSITIVE_RESCALING_PATCH_PASS`, `FIRST_COMPLETE_EXACT_PASS`, `SECOND_COMPLETE_EXACT_PASS`, `ROOTED_PRIMAL_POLAR_WITNESSES_PASS`, `TRANSLATION_MOMENT_COVARIANCE_PASS`, затем статус `NIMBLE_WILLOW_98_PN03_C1374_EXACT_RECOVERY_PASS`.

| Байт-объект | Размер | SHA-256 |
|---|---:|---|
| `recover_c1374.py` | 27409 | `a9dbaeecb8a0c0dda42c3d437c3ccfdd834e9e39d9bf5fe27a16a1a530195cad` |
| Декодированный `capsule.pn03` | 10525 | `0470008c42fd61ca27045b001cddee34ab68a954dc6e8ec0198a63e9715409c8` |
| Декодированный четырёхфайловый `sources.json` | 18924 | `dbda2d8354f20195aba93630dcf10c4ffa0fdfa8282a1979603275310e583f2c` |
| `speed_patch.py` | 1111 | `ab7454f70d2a3c1c200f0e0e240e82619ea8e91e02659b167111f1fd35a91359` |
| `verify_stages.py` | 3951 | `8544890f4782d66d0801c05fe1bbb37fd4ff273121dd904e3aaf16cf1b6e9c2d` |
| Свежий `NIMBLE_RECEIPT.json` | 1013 | `c64fd8f0cc6069399ef057862bfef070a7f234aa8e805712d2cd533ea9bec0b5` |
| `verified/exact_report.json` | 115081 | `71caedb4ed3781a6f3589b77fba3d784dde934566266eba9382740ae5983a440` |
| `verified/independent_report.json` | 498 | `fb793bea34d849a031add9935e643622e4d2619618259df403dd1394abc6a338` |

Повторные исполнения дали одинаковые три JSON-отчёта. Координатные CSV восстанавливаются в `verified`; их gzip-обёртки имеют временные метки, поэтому hash сжатой обёртки не используется как математический идентификатор.

Дополнительные удобные копии: recovery-программа (`recover_c1374.py`) и программа с точными отчётами (`C1374_verified_recovery.zip`). ZIP имеет 58325 байт, SHA-256 `d747c0d8828834c4eed8407a06f8e65beb083b961ed380945e2aea8895dad920`. Полная буквальная капсула следует далее и не зависит от этих ссылок.

```python
"""Nimble Willow 98: portable recovery of FUSION258_PN03_C1374.
CPython 3.13.5, standard library, assertions enabled; no network, no randomness.
Parent: Figure archive SHA256
1e54e3291077a0f4f0fe4588bb6793b823c7f904caab1c1ac8712bde2c014722,
entries 2026-09-06T13:56:32.877Z and 2026-09-06T14:17:23.665Z.
This restores C1374, NOT C650, and makes no minimum or priority claim.
Run this file in an empty directory, then:
python -S speed_patch.py
python -S -u verify_stages.py first
python -S -u verify_stages.py second
python -S -u verify_stages.py last
"""
from pathlib import Path
import base64, zlib, json, hashlib, sys
assert __debug__, 'Assertions must be enabled; never use -O'
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parent
BODY = """
c-l302V7&<l|JXbC&5sr_detC*pA0-Y$qEhahzgrHpyn!j_pliJ1#RGkIOhN<8h6BQ2`+&kf;Iy0z_{DL=ja2L=jC?(S#&=2hqFk|B~H5{6N
yXPxqbko$q|-yZ`;C$DhPlR#s}scKYxT?$~Ub=}Xx5R5{|4TFqOj3>i_#i%ON@he%qyBELeoeA>QM%L_9GWP9M{!NrO;N&R6wt#XzP*>cVr6
iteJy)(-j2MF7{My#9riA(9X)6h9^fehqrisDlPI3zH?LYBl|xQIuBLYySEmob#8V<YYMx`PIVHBn@!%s7B&JImJwS^`g!7>TZ8Y9@m*gy(e
E*k=6?lgWlco6IITMtb6`xf|unM{rC)p{90d32^SJJk@Hmo;0}9W;cQpEi4fa#7rdS$QZKO(p~01?hmr;Ueeps+QwpSW4vlNYz}a5bbaggSg
MbC(`q(rOsyVz>v$Y5sCD@`ncA&N^)KjgC%W3{0;kaAp$`uwDRGh23~t?8Dp1>tSsXG@9+0B)WpSIyKA1dK2YSDR`Ss@fp3{n^o#qhN*3bbm
<&Xpxr}iHt&7$Cjpxz`DIknJSIH*qIU`chYB;56TLwA4Yz@l6SdS$mbAt1+yaD2;zpUnR;GH<Gxlvh@AWr5An7L{&+gA=WT#>iSFkf_w1-TX
!YlUp1$u!Tdq-SJ9xa<nE{$6$jvyJR?|hQ&PrRVikR%Nu8ow+xr{+AiQ;>$X&6(<1%cjKe?2Z*xCRp5t$1?{4fX$Q+3?Ru^RKGfeafYr0dyj
*#wAvnXDv_madG_x34teH^mh-WtfyyGr7wHm62XUnkj9$(t*2{(xOMNwSTsV|Z~UFI*gSz>w0yPgcd`c$4LY;Ka?PxiciYE3vRL@?A2S7bRC
`)p-&B#=yAo@|k_OD6F6@ggCfZ8@W@IZnS!lp@y*L*tB?-G>Zj^3(=#ea7XTNP+r?Qi$_DW^)=-#)(~cCTO7$2ATlWF$PaCQk;J4-^LO%Zk%
SoA^5E{Hq^G%HeqphfA+6;J%T-DJjJ|83zDZV94%nG!5LXG_#fgd*en;FZIIFxmZBBYcpQ-Lwt>>G)Wc^`bZA3VFfJnrat>xMcFGF%NkJp!I
ITWm};VDIdi|%-8r@th<NqvAQ(k0rV-SGps%34zFv}-&`huD(bRI=)WgL76Qn<K&?%H-NCF5FE8ytdS(kW}0xRiR_sqq%{c<lyPC@Y#YCM8X
rI!<!wu2ulYC{kzjUJoOVxrrih;K7>mQitO4Trxz(MDpLiG-6DC`x-LcWbEKn)KPc9nA*l=DwmAO}h#A|{>jIu7<<0S8z4;`mj18VB?{5KOk
IzgNM}0sx3Nt4Jk=Mwod^&o(V#^)(n&!e*R*MdkMShQRTo>hq*9v<Z^`dAliOS8&mIQ|%!HTlh730FRCrJ?J=~vtCk@eA$jS}IHh<v)D+tGW
RXqw_f*Yp{O@nBC@{N$p2KVIo^bn<(PE|S!;*r}eVG;m1$Q!AU}WgJrI%u4AfRXswKX_bTN1)(0qzOHGoM&|>rj+O2ThWQT}((EQ#$H?O0`0
)P1(hBjw8Pd&P6FH*7xrEeYjn?c8xs$xg@`<X>Ho&@q&bii%d-{!mj>g`#8BbE%+dL#1nLkK+7L9U?$nQL<ij{Uu<Ug<PD47+v=s&{_&Fao{
a>{+A-O@5UFd7bq^botrG5$NE$<H=4lxF}gT2fmBgN|a~rIblitr|#VY>!RZcM6N5TT<3~PU6i4b(y6%28dFqP&W%NU=rCAW-JKzAgit^M}B
+gQLK|%wls^qh)iy`=EmSS220g_E9P}4BCGn9RdwePY#UwARQDA#xLMn>J?A=%!}1idwF@hNmF9xDEuNSqmHl$d$b^7HHfz^3Lp2RR!n88`y
ez{5w-t+rCel~9*xId|Z7%a616xB|%9<E3=y$Ux{IU{(Y@2X_q~<3WTch$s&DHlA{9`PR4n@fc(pNTA6|2QwIB3v3Hz|CR_-pL~h3E}^efxS
*rREAwjG1hiE(k)TO5UD3WY0q+JEnP!rx$^q*A~%K>|b*PPxn_QtHyIdUs;jE&o3T0VbFG#8QZI(Jh3Z{7b}(pb8*vDbcD6h{|xS3jc6j$kB
CyDYiaj;nuL*JRh8o`?j5Kg;pVT&)YPcHwfQ$hBuy8&{LkUt`l6ie`WvK5tk<rt{)}t|33j3e&tS{sU~1Ov2Si;Up7ZPcEfFn63actFVSy$g
W3=TC*)6Tn4DSAkG>qjX=pruQv<-_hn_mE=W_imuv@#gTW`C}za^zVeFIgTmmj532O1n1#rhb8wc4TE5;aSqNF`VX#sPMA8=5uR8C94N;)^u
gYN@9vP)((zT85e)%h$(I0)z<kPBhB$08LG0zeZ<}*>!~tf4t5s!M)w+@#{tH0n^XL%VNKN}DzQls5lWK%#|peiPS|=5?z&&U8k<o$SVZ-+t
4JKw=yb<HGa0H9+fi)j50;Z<`AL=3=D-0h`NuSt`E}QfxYd)Sr~_rG&9(!ExSl{`75Q`SYINvu@T}iKoH;g`RU$Hj$}d1N!&??{$ynB4+2U$
4kX_lTaH&j>2yaf(X|!s&I29N9lF;k=ipUgWqPl@0fvz-pU4)at3suc=<>a<OT_&zmmnHcSOa3s=KfVa*m*$pst?MNxi9I#jxjXne*)eCAx0
Js@cxA?2RpfnS#}-y@N}TqN?<#OPR~Ir4>vamTdfDOh(s%S|8bq1_<mfE!3(rnp^~R$)p%z1e1sPg9{rdZ6(t!k46*YA?{|6Q=mxT?bJ&3o9
>SXyj_$aZG61j7@?6^T+;up44X7DBxs>IRI<hcWcr|fF!TpvJ&@h;oO_CVE9eRyd@ULz54NbG8tbkf+y;H3z%(oIFkkew?JU2b0YAeqU^h-y
IwmzXWH*2<#LGr{83DTOXx?}fK@*{h?{HV(FR8`IX7R?f&edU4QvO)}uxMH4S3=_;8>PEQZnxsC&;24y*ZWgcXEZ8&9yZ{reSc1Lc-jPr~+S
*Z=`&eZwf)gDKcg&)nuaYb9BMvLD$r=TRtw5lcyDebLx=`>0YGOGy54OEw(ceK@pribxnxHxD!ba6XS3V0Rw?=(68L58Mg`b7)XM;)f_vEG4
X>rrBwu4oFa-t{6Dt+76`BbkZsi*k04uetW&FxSMCFm;02$ju9w7wdL?usI7WE%Md_Sf8A_;%99+UtG7eZCOd7&D|c^HWf1WAfC{*w)iHV!3
p`xw$&xdNsB76dBJ|1q!%?8WX*UPX7cm5i#2!1REX0zRx$5RLg&@HQ`m4`)4G~ADe?afH`&qyX8S#GP=8)WtkTCE?yFX<Zby1ybJMPsH&ux6
wlH@tVS|6s(46ZlG>L~jh&482XvCUv5Z8-ytCJhLJ@wWB(N6kgC>JMGq;zK+a}JY`g{GykaJiRZ&OSUpG|<oD$&T4wTUibwv-X^JWz8Fg^}6
_x?s#hH9EQNMQPm$vLytaI6?}yRXKXFw;7xD6e`H#yHcfkgthANZR2SBqB&+L!E&lWj7)tfVwlc|A*jCY&W~dH3i;cW^V{++LJX#f-CY}ue!
dJy;rbYLWifNg`E`L%VFrw{<=0!4kS@U#XeGuOh7j*LcQit9)qz4JhiuozjphWf$Z?4<-;WhtU%Sc|wJ`yt~F6oI9p2DrWnQ5h(YKDY%XqK&
GT?{TC=jRzGCl6vljW|1ft(L)I{?+aA9kJl3=y&Yuq-wz9rp5Kd*++4TxFUSmHg`Club7HAy7E1UZ<x(DAzSzWj%eXIx*Z7zNlS=hMxJi~92
8R9KbDt&jLa|ik%4gIAsjL6vM()FBN8m@lqR~Gj$ye}D=Zyc*pHW|W@_8h5&<t|jwCha#GfE@{-dTs$6s(|UaN6ecGD2kv#~K~zD82BOmY+1
*iRNEeE<B)fqjOawE9gyak4j-y80q~MWHN?$*@uXZ9Pc3c0ycf>4JTDr(s->nYjW)YnmS#8v7g7<E+)df`8MuDsAd&jg~qLoqm0*K9NiO24W
l2(oJU!z7<L45x#C8w(Y2v;+i_Rcx#}kMbSTT#=kLXE=A|t?n(OEmvrsAQfgV6T!W$G^0T6-jDXs%U8@If>@`&O+XCEiUv5Z>D5v2piAwYzU
!4;Io-ECZiJ!lW*JDaH=cZ2Mko5V0_5mS>kj?PIX<qRetX1Wvx;Cp>tdthF;?+DKoLQ-gXzAs7+K1aS!uzAfyh%WcvOFt5e-QgGNY=BWb{Lg
0cBnX_+<F*y_)Chd@`Zy$V;grknhQC(DnY$|XK~{YQ7&~k7OWO;(&1Y!oT_Yswya21fUGmn2d_;iD)LP>4?JNJ67^uZr(P{7%@gm=dSHpuDR
YFsOy-^2rlhHV>Q{BnHoxAd_0`$qik;cM1I3bomf(h&RZnc{R0sBlSM4`62rC7?f+B9JaVc!DsWg}+6|KANH9hT@aZ$(O3Q^|nQ*D+to2b-#
;F7j6VUBCugGl-Pexvr6h?=B~wrqT_*N|{tyWwfPX3Qv1S_;|8TBE&y@T}hb0h-1L6)%8GhC(a1B)bpR`v!+7szP;Wb0TU~DXmg~ejsFcbS^
#dyh@?U85keb_&6Ma>JnE}=21L5Q=XgPm%@_%-p+*WL^bt-Y1Y|@DE)bT#%5)HioF8i+2PfVnZc99T)46&A@|Ev(TPQZ;UOS>60Lf5lRC7*m
PM)ZG%0Qm2#yr_0d8yvR2GcwBkj?7wF_N73q9op%jF{jfQ<&<kYxLLg2VEImZnd~hv}X3nTwf}n9{UFMbKp&V_t}`v<Sc;Z?y!C<otjeTT;v
T73c75b0%*~anxQp)HpbvQsR!Qb1Di0a<uN);dE(6dD?UF{dq;<oe???Sy)dAD`}W^C)?u9x%Q~ua}$DsjNRT<I~O;*#xln{rrdFdV|k)LB0
E1Bn$vC4v{^Z1u*f`<kx$%7Iu^`r^u?aHk4M|B0^ul-p`DHPhRx$-DWN`ev+uNH&0s3l%<%ymVvH_Vr57IS+cLMheDpJAc})Ytj^hs9bd125
sy;&^i^VayNt+z33#m|xvX&W5W#jCMUq%k~;oV}1yu{9s{KlA-T4OPo2f_l>zUyCNV^MG~;fsL8`7ha3-4S39u@@BTQhtk9CSw*0B)&kF17<
`u>z&A;PtB>@2n+(;Uq7)@UetuJrM)OA&vZy+S_^CMa5;ep%_J(^bON`fPPS~9WkP*T^q_0YLQiHyA7Wh_p%!|mO53v18U&8~ogh<r_%;{M)
=jO7x+*W@VST_(M%<y`5p%S*qHz^4Rc~2r<P~Dx9Ug2;{E4|&;fPt;nc<RzkmU~B)Z|5jVzFvFTC6*OJGUdWYco;Dh<rt2s}C|E0~x7oj@$h
ji>B)|wSfo8kiNwkt6)gsf~neASmud0XQMX4c1Ho{8>@q56>%5wh+JSuHkG)OMuD$-TeHl;vzjv7Mn<ALX$VuxrGp8G^cg$brsm67T-gvE*J
Z7sb31ybe6s&{Sep|V7t}vVJ+#nL5oHqto*kbID;1x{#zCjPVSU_-B<cjbkjzOBqL`UUwQhe;)PY*Zg6vr=*SJKgu!Ce#CCw&AYQIym63YZ@
X+9(%qpRE$+IopJ)J_a7H<hxuS?*_<PbuO!1~j&Ygu$YdBxHMBYZlRy%wV8$C1n0wd_-)ps!}!KNwkqU*208ek**+BFkkmA76wUMO4VmccT%
upI?V(GrwejJ(u|(O64N9~s;R$#af%)<XVJ~VV(Qu!R@SJ;SasIT^M)=M);6;xR%NaynJE?6GG^v45m#rST@g@yM!#I#WGxf~0$yoQuT48gI
5;S^b2M;%;W&x2?6x(v<^aj=u9%3{E`Ua0Y;;HrN-q-GmAT%u7|mc;^@4nkHwESxnR<C%6pV1LPPAj&SqB`KTN0q!)&S0EEw8SqR8t*RIci9
2FLDH=6b9Rt*AC*kqU5TMNR>CKE7xdE8~G65BiPNT?RB~nZF^612DMCNyS8-KvU8bKO-X9#!Q353EBd>8CPENNOsHv(HkX1UtUi6iFXI*&=*
qX}#l!%%^>o&09Rm-=2L%_cWXJh)_1UWSqJ#<aeo{2h)gfs}@-`Rm&WyKJ40#!f(*njsDHC4AWFANhj5RQA%gc_e$yKQjsci{1PXsnz#9Di$
ydrt$Ajyh~NzI+-vxfL2fqZ<b{0Pys)+ZDt{Sl9EECr?(mqYyUbh>qS?G>`Pq_3aqjyOd0BV<_WzjidfIK5@avfAZMW~_<)wd_CQM9uK(L><
oy&o<N<gKGKIQ_QVuHQj9>TiBU1rK$f)hGqqMkqs~6=8(kAy!uUdr>17y)Z0bRn$^+-Q+`y|Ig%v{Q^(E+ay5R1Yi9opDMKXja-6cc#>Ls?M
Y^uRtIk||ShhAUk%Qyx8(~``ae$LeNg?b0zMvnQ4vrxaoh&KI_g`wrKctTmES3%rZX6`-^Rs4sR_q~M8W0|$TvXhrZ!#~oCk8co;o+V*tuCt
)sdD<|^%hIfaU#tWl;e0A;B8G^*g#~Ndwh;-*eFP8IELqE+a1-dKOw0rbuAf-!-)8H&W5;J7u<0~MY?G;;4zXq6j&iGp5l__<k0Mv!Nn7#Wj
<6X$Y?{(`MjdEh6&Yvyb&YONrE@dV>~~$sOs`usIi6jC#L3dNhr^i5N5ZYzyap@aqWtU9%s8tRuZN+PvPzqu_$fRc?5ThqlS{@&l6!=fo!+9
o=bMx=7O`8RTqe|aJ^PuX+T((TAeH=R3VyUlQU`}lotu!aoHo&|4MpVYH^X{1=6?NG%V}zA=Y9kuP`SIh;_*rx3pyiys@J&&hf6|@VRnlRNa
5#u=x~)u<9P^^0RH1bX~x+jqClLRZ%Qyt5Ze>4qAXHI<5J-G}CFE6eJgS<0UF*^#l2FViy-XCv}1(h2a#QNZO1s#Qu(0mK{~n^>Pkzlq&{jL
+ehFT$#GCHq95XJhDO3niPuKG)-w;zA=8@xHD|IvtFR&VBSunGoh}6lRM5|9v(Iidh3PhC9yFr*@(<n4_B3?XLt}njMeII>ppKNpU<sKEh4m
Av#bTh`j2pHpQ@oL?k{+*Ei7?HAibzxie0kQ+tZIY=6dUSOQE#~NJrC*U#vv9-_V;pQJa*j^RP$w>4wV0N*^4!?r6+hj_@HdgB{@k!b~qmlD
RHzmhbSw5xe{}oBTP<8`dY-wN>DliQ^mfU2l-W^tyVpe}j)BIaSrQ;mq{VJH#`|uGwC1vKCmI))yCb&|Xm*G@VheK8*`I$F_JpGeeeSYs+>g
2JBZ=pcF5jA=SYh={t6JeWp#v3u*rZCrWdhc`GZ(ASIfmzP>q6y)i`T3e?Vf;YNN=u52-us~^lMuAK6>d*hsBGT-O4c#yKu_VDreI(OVN9xP
1hRRbwCWQNDoQOGlf@?!#vpCxMrb*i>OcOnX{8!0cUWpP$;`cUCk!3ENsUO5pZjim#;$ebFt;DZGV0!dHbGGNI{WuIny*8>l=l=sI^(IZ1<f
3eeGFJ<CuoB@@>5Tz#$U)$^oZBAmyddo_3;g}Gq2KxB1(xQSRIAMG!&0wP%U!Rt>X)KsSSXG{sJuu$64@XyLTMZd1gy;Feetsd5jL67qnTb-
=>?7hG{<Nl|-CMt1Rg#gnlYe}pv1VQ>Hy95R;UGVMoZP3^rqvWS2L{u5InDDgaTzaSXTsKQgZ9V7+L0XFm`??xp>)x)5OJ9djOLeG4HA0TX<
l0iaq?I)Rz9gUN8Q48ZGAyuQ&-4BSi#O_Q$FBa-^PNem`jGlnCgzqc%cs|oC-Hi$x9K*Fn3#8r7n)XDRV2ln(8T;sax)ABi4O*l)vaoZz}Y_
c2!5@nnH<ipQ1f$tfG;{sm6+i%%$CvIA=^ewo}=ONS9H*o`XlZWIQ>6h?@&f5<_y5NLEYBw9=l|zmWMjkqT-u1aZfRQy<yI^PAd-<2uZ|tZu
6JW|6$EuZJq%>P$yXcvvBjvdVsiSXYX0R<C7jrgaUGp$$<{e9_amb7Irn?*Bb;lxfU(<$lcXkxOMZH6oiUy1cdgNe0i_wC4W8J9x9MuhTj98
gcN-bc)G$u`52%zF6vwWy3>5gX+KI^%7luP)RtI;u+pFuVM8h;p=;KeO{zZCoLIY+~AN1ep23`b>t+TSqk>EkGw-lB(<Bqu{W@`MYn7kKY``
t!3nbim58kB^d&uGlYpa^%>DJrr-@!tm}^e70akP>1BS+;fhZFLf>zXrh)YZ|$D>}x>gsK4g^Zp^H<yRw=(&}HN7o8dr!%RiuuKX{TbqUZaJ
wwAG<b^7eX$DQmLEg_ss``_15^RJ3f}uKq5I*|m8<9=Jo@H1xMcwxIQS+i2S9#M4JaDm;G;@Fe+TaaS%6{y{;mX!P%c0;C?N(=EYSaJd)HKZ
?_wbrP#n-#6~qHd1So-0Xa;l~e*c3Q+#ZALI(h*m06dns_vRdUUwRRFf!n$NLcajcmtUh<fQO6e*H8_B7y`ixZtVbV&;gx*o`+jsrULpUaGr
Y}r2wQtI$c7)h2K2y2S^RT#KQuhci~V9v;sN}ZeIR?JoeHl2jm3UTV4Zn22P&4g#HNbKhVoBf%l6ykR6~F>geOp6u=`Em<Ct`*njl_^z(nMK
Ly;Ue}b9-M(75cfd2A-fPV9@)h+-t^Z@;;1|SFWKnLgzxca~%pqJr%9Sj261=s<y2bGDY_;1C48Uf%b6S#f%uPwR(-b;l{K>vg<zoJRrhDUn
$qIe(PzD+-d{r?L74F2$i0MLW~yZacxC=GN8&?z|W4*`H&07dk(FM^-KGrys*T!SP3PB)MN1VJ#p7fAtL|JR$daOT{9qhoONcXa(%@Z7JTN0
9*G5Vf~>89XoDhn@w_FMf&shqB~;^f$Pl!jS~veWMRh^8dY_fIq!T>GWrK@uj;+0`Sml^?+{v@7iDC)xXd+%=S~(U7CRyM4$n2nHk{G4NxmQ
@z^Km$qx8~5M?nnh!s=((9duGjdCXz#ZXRt`yEWc$KR}i0)-=pgKyqJ&rTss!L$JjnJ5hew4yeEA76b=!`%GHOzF@9kb<h<_zTRZ_kMNX6}S
&wj-nvlIDzhd{uT4$%ZOotx%i2E4-z?qfJYA{dJv?dBt+qpPz)J%k9kM{{vZNAyuSsUWmtiK_QQks1u|LahfK&oNQ=-YGscWFnas~v+A_~P!
~XcE1}LM!(7uR)r``VTX`s#2f}ZK3<h^}^VH?rc->~cG(L<NdGAH`s%_CnipJ$*v2t{?w`C8^CI`-@5zPQKv$Ez13K>-(L0ij<#2fuiM^Q+%
I4=<qO2>BfKIdS*^aJ?fDCB7Nhn|46MFhq&VjYV1L&MTiVA6CPQJ}m3*!TFFqPqV+og#+Jw$%MdtcRpr6{S2LDX*rooSJ3@e?~}rhpZUipJW
!+SOTcoG+jkF`Q3v`Tx4*pN_UhHIUwBFgufiB=MfHfoZKc>Yps&BW{zwyQM&O3fHFgip$F4I26e$e;h*mHX-D2|5Y1SWD^yO#tE^Z)t>Vn(F
bAGgmN*Dv$=jO?<3V8mFd`kBcRD{@k*ze`$?ao1nRyB&j$RFH9@Vi>X(y!CZ&`YndaE+z(4FVJlA78wH&L27Y)Qf+5%<XZuhSrdg?p0HTg6I
uO^v%&S+V4kFp^^%i$KIZ9=%sG>ZZBdE1%?Y>pexsq4dy5<zi_+v(GUy+<HlZQ5XA%@My#FU2|^|d`hj!pfj|85K|L)60oq&WlRE_F(La0yz
^=l_s1|O%RRczvzCRrPY>|R+NC{tk{>I-}hDZ7Ig-0SvM``HRG84q4A~!BNcRCT3p_2&ietPQWy)SOQ4d`wgaG{L3{q9W}LUI&>I7)O-g7}O
BKHf$=#Pvrj=+jR>;ka=b166Jg7d`YKO$6@0g1ip0C)lHZeVu)m`__%89xI`@Q<dq3A3bz!FI_(3Qcj~N`1G^e1AzMB?J)2W(zL0Lp{ozG4?
c`&0j^wvi>wqrK(BpsA&OS$Z|O`ky=ND`+JHwMWtqLGg3#w~cOMC7jLbS+x(hW-2l}iD*n3}o^#$_{6^`gV2%!&t9YK|_7rtBt8-2Whb`(3u
yv{?uD2NFJKJr71FTIRjMVI}N2wmzypN+%QKZb79i=O`QqwBG>&o9fFx4!Cwci!x!B$}arZa2|;w{Ao;=wv9cU;TjIx#0(lFO`uW;Cl}t+&m
r0++;ai=Em(kLheHr8bb&QrirgmL3f*`ak=#avxuhA1Ol|z-{(81bV%UNN4L;>x4#>q62biG!9C2P7zOj1+v^W3ARcr4*hzSe>II8JnGl94p
;<<Pn*u^%kE|jP0<Z%3`BRX|_%W2j`v6_P5dv%^gi&z;8L)K2F<?Lb^s^5+TmzWE1335YxYJ1AL7oUPl~gdeENw0Z<<sHe!y@1^9Ig(&{_fN
bn&wTaa-)Du==L7E{uFxJ9OrMp|G|6Eibkkd?La%Yb-?$V=to9WgFfnoLW=$?z92vk_t3F<eHZn@9k-9+!;i{A%XpxDo;U9x?xnME>h$qr-@
o_5|MJ%tviC;!-rSA`JyrQw;BZUPZ|D$LLlQhOh9VHvsW8+-g@|JO>zgnCCk;9op<D0Wu7pAg>3f$hdpz_b&nKUHECwN3jLQ%2-T0syjHrH3
$x#Cw(Lw>8jw4Wx640sBE-DrZ#44%Q-|9i099p_BKly3`CV~0#?w>DQ{A>u)kRIN<{q#Ky9(!v1^1i*D;nbttC!cy^03CMU=gIv1s2?3!dxb
f?_dp&9Q7KKOhv{V^fs+MZdr8qOxD0J#?#uT-@+ci9qkFS+93B?}^7Qh4xe(>RbvrnKDw!3&ee<nrfs`9`OAPzIxCg&I2tND2UxqCN>u3Yr-
;VA%C}Az=%F~|Q0|&3PGsi`+N8B4f4MKhJ<WuMN{hfXL9nPO0M^9X5JU)1rW_F5p-`?iz7|rj8_ilfnfXA=C@+vnR_EOp}rvNj1%^!&VdY85
<ydBNFuR*y8<)M7!OSwU9S2FzEi87fiMv6G^u<zb7f{NkZ`tYM0?j9%}MF1z5QtpHnb-)*|z5dHHXW#nvJ7y8sTa+$$EtDvf$Jro4UlD|vW#
r{Oi9WmspWkIysX2N#fEq3btfE^PD43Bk=q9Bqml>q4h<Y)ET4>R}*z-tl-`yK7xiq2EXU;-0(}o`1MJ_54LW)m2HDzhEFEwZ{b@b#@AMC-B
hP2Gb<Ist^sLv_t?4(Z;01rK5L40`Ts2vVnpN4wm#a?v#X$-~hv!em<)Qwqq?+Yu~fqVOnTX)<pF^{9$;dHLPd-kOm+7G|JNev<T%mnYe-2r
zJsbTo)?2#`K{b7$Cec|!<-@7FM_m5iO+Y=(V@$9t-^wSo2-vM8~+X^S`@C4$<0pr1gm)4OV!<~b7zhfCOY*TQg;1NXK++%m&{OH^7IS>EHb
A~#;dt-3V?Y`GUur~zuO7%@Q+~%<0`Qc~ockX&H*B?OKy-`+({x(cweE9u;iXfZL<5k$AhH4Vv-_Ko?Kp?fZkB2f66i&x`IIY+mb&hAhv%@E
D9^JGF{pj$@KzdY;-pZz4ub9bTet4P7F#rDD13lC^2EY?{uX7%HKMv5tPuvWklKdEY>e7kd9zDRRU~;Id8ilJ~#~$Re!Bnf*Q|FHz)G#TO5D
BP~Gs2!f`70kDht3`$gUUI_+u3j`PDxP5R&nl6gJ!f1^$>;{7(2(KlvB*9geUlr&zayn$MK_ni(ARzUW(=X=zal*u($sT470)RGBS`t8}r9q
PB}M|5ujKmg}oTd*wLT3pSykYi8trYIMx0fs6#^b;x<H}e5Q)!`a&y5&+q~L@cRfVVV+z{0#EjP#1YYv+|9VXzd}t{7`w@tr1lAAQu=sa>qL
ylAFL>V{wAVk=KMNS%7!xulxk|o0wuErr_R&LqZ~%VaD5IJ?-_8e9EMpF!+Lp&XaqHMiedQHz?3nx$)tND0KJ!lp7j3yhd_#v``JT5P>pJtI
>yAbG4%|6l7!u+3Xp|PCj+gxlv>^#R>*j`eRTAnX>|Ujpr?E3F$f{=VdOSO1C_D*z0Z+U&VHa;WkIRjE`}?nLqbXi-a*Eb@yKIx8EznTEE9A
RF;^e>uh*#^4y4`q^JMr&Mh(f4d~_lTK4*UL0}qB<gQ}Ttz1``|^hMk}R>GtK^+P>-OX<K(0i>kTHpaTmvM>Dyl2gk3!|jWC_)te}i946wf3
1p@u?8rHZ$Fb$_GD2u{PWUYi*OTRifKgLKGcu6Pc~Cy#c&ZSL0jmj>#$Cz)bVSN409fQ(Wi-H<<xVUIa>CI$KJaA_uq7}8qN~S-DdikGR`ok
hfQOTt2rX5X3MBE$mDoJC8w5Sp`JJh+^3+Iqd|ixhWSe)lyJH@B}^iC9zR_Q=}ZuMzluiO!10Cu2WE1nHv
"""
SOURCES = """
c-qBWjdR;Jvj10@cJ4?jko?u_-H1VEoZ7y)sU6pL;@&VE4Mjo{Wr<`-O0t~G|NeFt00~O6llI=dH@&lnuf+mbEOvib<nwper&qrm|Erg;zw3
YZiT=B(!ZZ$xxI0URMOdt@D4XXqQ3*>tgi&P`BA<opo^`!Qt$bZgvefF{ST!BXNySnWR`<QzlLSAdqavGId00(=q?OF`tf;IjNUD-KeCq6R6
sz3PB8{pno0Yn#5b+`ssx-=GGZ9rume%F57=?>j6(>=}te>()T8To_D#CW%GnMfvRT<^FWYaQB+4wQZSyV3BBrK6%RwZ-6hG8jw{DD0}#-|k
O_DWF=lC&Dk!-qjx6@xe#Cspa}yET8Yh#Jl#=({Qwz*!y^rC?Q-XR~a)W^q=raxr94k(DKjMWx!)To1xUoK%_$B~)>e#v&K+C*7!2z^a6$S^
fzI2~$%qqjS!#-TtT4iq_Fgl>FMaVGzkYoDF1-9e7C^abr52SyEOoGHa9-)`&%Gpl^wEF&9M$1Z6X#X{DS-;=q`kb3a=92SLE-V?PL7R%aiY
*{(O?FcD7LWFf7vECmed^F8%@&+>M+=Wa5xWV77meDZ~JSQX%g8e@}?4Y3KVDC9C^rXRe7pZ-B0xrNddh`QoARqPFswGi1-9E7u(gB{7*s@A
=(^?G0Ohh5>+jNmiPU`0{~7yv3Tn|`%`$#+UvA`v?>-wk?Uj*H}skYl5-nMj=n7}6mTen7%Nqqhua3sE|*UWp|Z6k$3R)Z*NggPJAjeQWh#R
_ZB{YbRGsO~FVKiq<l1-ScSOLjihlmM{fu2x<Smdl29ZI`=OR+`nLVFwcR9eZeI3!Z>z@u1pSPGBno^3oOtpPYn;toAG(25GgID>s48taX%F
gF#WKh9jpmchqPCdWF{=EAUS{F_}$C1+;R2L9@J7;NV1QAh`9$zxCdl$0f_I1po`@u+r$SkLft~ib#IZ!B=l-K4Pa|mxL2W8$#08=VB=Xfgx
v%?d_B%mtgsXhNwt=xkW4{yiI}!q5)F{FYB>rc&?{x~C_tfr!bpY-)KZ+5QK>X%9_BcOOl><C<w0)oRZ^t_I4_+dT(NU@%dXiK3B@~>7c9@%
ij)4qa@YT%A9$e4p^2i!PFXeLS~r2BxOKf_4r<N;B@uxxDY7IU%t5Y_e3pp94qWdIm!geaK}}}XgpE?6qP1y@Pq=^F$!Gpi(8bLJU;U$iy>U
?p@)@p?WF}~DhKbr=6Ra_r)SD8eXa%|g1PMQ{T#_%Dd!TbAMPqvbdkav-;czDGfO9`Dg1Q})=@MvuK>4`#M!xJ%su`RyKhFZa9YGwU2`e%wZ
;hUEXzJDGT&?)Zr<#Et$ZF+dBjBd1`drMNDW#C?6sfIN$dTT}37fXNfZ}>HC!8a>KFVd1E(GPPuJ&K?=_{I|m7K2R1)u7M#1-fJ{ghw%N#F^
Nitfsv1`N}3ONm)2pn{xN$i+2;no<T-?lb`9*qKbAxSOiaX;AA(sj-e+NibBJUo_el794qd*Ll|oJK<|tp1K|U5KxiY87gAQ6UvhMVEIChUr
}3{3V`S?U-Nyh)&xsz4@<B_u`5KiC{l~I+dGb%hR#K#$7vO3VWCnPq{^g9mVz>1JFCjFQoR*vW7j)$9>S?WYo*v53}P`{j0Xc|pJc@9q7=1V
_1^Z%ilYV6!#^-qG(<SsPR?L3g5eGZZm$q!Hd{hz4>mXKJr8y_cd+K39ff(hn2BDV?jPA$HH-(tb%koy138<6fydGA>CLh*E*;hC=EKFs@%6
uYSfX21sDe>9PeQJ2qaJ)8{_RK7CcTMx03%40m1Ar-lr=1cJtI5wZAeNEY`OE0Ub|FMwGBOhc2^G!D$uzw*wT^aSa0}`zhP!99NX?qGnm?qQ
A33``@Iqr7Y@S(mY^@_;+&m;q8xC;NF$a#(4CxYD^!F~Nj&7Fx4Cn`4%j|SMa!gWxb?3==(V^z_D7r9r||zX+eM9|hx$~Nh7L*t=$=@NMGE^
oO6oa-+(%Jl0}+n}$sGw|i5hJm+GmT3%ZUI>JQ*b-wmrz}&F|x+aNsN|t3h_JC6iQ28iJKuWGgfsE#IMafW}o4iLwXgaBuu*vvZd@_Ezo{=E
7M8+j?eX-@1X+cnMhdXjS(zFm@c^V~;wsSC!3Dv4Z1IaNBmlY8~~l@v5MMe&nhzV9LQi$SO6rrEv_72$)k^Myak`Ws>K3G0#iqnk8fe^FvrJ
m?${P?6dRho7=%p?=P-?IlVm{oc?zF)9v8u_~yoDquHXI)bsL&8)h{2T&t)z&&<E>=H~RL_m?N%(hr^qJ5O#X``$VwuM5u6w48-#4S*%T3~{
<6VP#;vWivPi_U73fxGa0tWoBgscq3^yNy{V_C`~XI*s=!%%Ske-K!pF^Ibq#{1NeJ*)H!jz^K-6@)Eq?fB~>$Iw9(phTw~68;N4X)-iwO+`
wadIlq`YC$Rez9O9DV<9T=prkI-Od=hDIkQy<KSyXqyU3i@nob=JQ?9#oBvY>yd4LVZN|fm3y-EtNa8OD?wUk_+3g>49~AN1F-w=l%s!`=N8
!d2-+Zt;UG}RYZsG3@vG3EQzflSZ3fd!~V2D0mCUWB}HKk*Vb6Tx>UuQ(QeLCXobqNM~989#(g9`3}b%Vi?V!8T0RC#19dq5!vC21I;_7AXv
{#luXPj@uoKJ_50S_#>zD=#%YIrES<%<sX{W<3&`&Sn;L>~7rp9={7hwXYP@8~bM_ExUNRX^B!Y)9sY%+1{_t8`MBYe!0vP{zPf6Ru|2hvss
d#zfO+&;TLy?Hyhxjnu-Ilev_{Br*08qT$5Q%cxE?aGg*XZ#u6&3@vC9T1~aJ76~--lF3i%|Mz4kbo>{B67o6WZKf?Evu82V0S3bTYW;Nspa
{W)@Nu_ivku)?Q^c}>?R9q$#YMgpd5Z!V~DI)%!Ca_i`h(K2PHpbhJI1>2927L&WT>QL9+lQ*O{!u<1;QzW2IYGsNe@fG0Rp5`}_M~6@l+l@
UswBm(;mDrPM0G&-?4!=M}nK<ZZ3~OqI5_1w(f*zyoM7;M^Vz&>|ZQ?7p<jKBeEW?+CjwA+ZxU<BNHc!nv75*45?y5kWezePCZJRE(w$#^u3
Ax5zM0qHqRQC&E-&QMSRbCjlu0Z_ak(Vr&-8zX=<A8fkkTHQNHiz6y1rNsCrF;u(EqJfrvW&{<30o~<<iLy(7Tfo_G_LMrNq?sIJ<LSwXYLQ
sL7A!x*I2!G%U)Q<Yv$Gm-6%GB2Z<{ijV&AA}XSyXc($0GZ}d{wdWnGMSwl79aOIPr%zN`&nt6(_?53&6ET`NqZzY42N)yd>jHxhW`)edPfu
bi?%?|IMB7uLp;JcVE3KwO<y#Iyn4?=I~KEKQH;;75Or$=|fMRuC}*#h;8xEdHl;EsZ*=#V7A*uKk{UsU19@<jX;alXSnyXJdeoFY|g(+*~#
_^jcw_SMn<s8&swp|WyNxG^|HKdC=VJMz<{J(v3boA>V;ApB#^P&44F1Lb2sonxA9hsR=Mi|2bwphB1jhz*POTmO+hnJqD6DNlhL$Nd=`l;-
!&U$C1=8eTDr5D1W&Eo_RK&H>RMqldh9g*RkD+XLxu2##Aax)G2NI@tfDvxYd%87$f{;7)aQ3Cg1gULI35x()W=pFR-tVi?l)DIpI1VvzkUv
Tqj94_#(rin>0r&)_*0@i;Z1j||LKVa24dx1bKgI6rtD<jSl?_#2R8g-@@GA5#tLITkd+c#2*LeiQ@)Q7Oinab0Br&f)UPqYwNXn{<<2$1?r
St^uMrStG8w5POzEUlAO~f1Q9}|ga_v`vX=);G65W8l^%D81Sp_+J=>tWH$IJ=kLLuHEk8=eI{Vo;EbW>37*&Ig=eM!j1#UUfEjX%E!T>dbb
=`FeZz;F4*{fE6}gW<|dnlNi?_bF@{x|_b>_bO#cn$w!*6lr#s+oy*tRIIqo=3^l^vu!L4C!<d@i)Df48m!W<2*&mzD@~8*#IsARl9gU@>4l
$gIIx|LQ}n<P$-sOFE4)5wMD<!Gln{fU)GioWG!NjF)pLvGW=jLClK6$wY?vBsY5}=8MueA3{`renjX<)!EPDEu2b5Fe!O^sE|J+Z4dfPySz
%w_%kcDz0BKT--bVAn~kGZr@9JFGbPRb@|w<%ryu(vlJH&UdF)!a{B)0sKq#5>v|ieo2dDEgEQ)vHnKGR1^RQGS41FmV&Q0K#9o0fO;w+{-`
<^IpaoG0H*rEN)E|{&78Y|BXY9u2Fz!eUZ^OZ$N<AC0=?EcSx5n!4&bvY&vC00*Qkf5l%Qy67o%_oKFd$g^e?M!N>h!?2iIi2R`-Sa~$B7Nh
BjR*Fc+%*qHcMmwYvkqxPMVnm%H5$ceaDa*$QL&573BFLC1!{nEH_S-#-q7P=a(p}OXPFx8=iRL${6YX!>_ab!%lke7B!qEQYNXZm7-2FR)r
iuO|$JP=U!E9ioJjh1wpGYfqYq#dp#Zi*&tSd4MLH}KFl(kk~AD9$3>!Uln!LV1)Q04^w#cX0G`D}SJcbK<(pR?d;lOz)`LfPvaqF?z%s*D-
epl{y5b5SAh@E2F?|120JLg0RM2bvsTCq-Y#P!6+M4c7h<k@id1SEW)+p`=ePFR?eC804{$^U72U{IUFsK(MmU(GelfeL%h_sE}-T|{#!Rfl
PvF*;Zi&{D+bp5Z~Qm*k$+^j{8r6WLs!jQT&;7#vmrXBunt*tZ`ARl_0~NoZZ0LBuaAOudt<3To}RT9nN~=Cs;f9wUwzpuVzxx)5bcx0y<<O
iPC6YhUYYfTNJt0NxcoQWP>BQrFJdeT3$GU^A}+wm)F9JdR>W}36zi_$V=tV|x+4+7z7jHkp!X>~PxA%PDM7>3)IM5-PDr#i%I5P7ZH?yGqP
yD^kwpX|Vk??urHDVJ60})J<e+DrqE8GCUQYWEx`3U9)#a7wZ0%Vp)_~5UO5<h2MKVLqE;EZJ3oOlUo&j$ZwXmop?g``;rG(Wa+~h)&mRtRm
sE~G0$e#&2K?ko@3j7Umim=Pte{KbmJm-}Ezk1Nt|EUXIBy&ePP%Ueq!PLiIdoW-YG*&^S$k1f~P9;&=xLUw`W*3$1T6CG9==p6Rm`p9x48u
DIJO}8`A<&Cr-2Cu^=I-Y*ONEI7keWvg>#C#eymdj1Mc6Tjz@tbZ1v*^UBqe<oqdm6M5>r;%9YX9JSKvsU;rC2gXN}Q&>uwrq)}OJ|8l#JWc
VNriPQq<tpJZ9xi#4a!)RtPxA&c&TC-ikh$G*O}kUL+i1POzO7HDP2tRo{puUNlM7ND!DYz8C3s}0l~J;Q*|K{y!g^NLTb<{rW&W`S^5_0lj
qN@9K%n`R?$NGkg*Zd;8>{J&{8CNWxg>|S1S$Gq7mdXD4Q``+D49`A7A@!kXMIw<VG7KM)?{)ym^amjc`hOx96I9W_EBJWu<)k{S(o@|8%d8
mq$G)f3B-4Qs1><Ly|x1a;(PZ_t&fr@Tz;<Edek;`V^V&-x%bIsrdU0a))WTnbxM%Fm+{*Y}fCj)9z6u?xcr!t+?!aySCL$jc7&Xb=9IughS
dcjUxo6+*LcdCj=X<6LHEDqh*{0Mv_!vxO*NDtwsF~Rc}oZ{sAW^hNo(-zNNqxEiEe9QaY6)=aXLzOy&O`ye?B6(m)6wG7B{^=+>9rGs*P#5
Fnm;<{t?V@ch=0abet-)xLv3t9G1BAzyf~y@zi&gI>)UvW%1?RMa;_!NUk)q`w%{Nt3nQ|M!3aYT%7<exY15dhdwPux-^;CrEnv87~1rt(i3
{$CLD-}`7ZO^)CN;oZ9O9FO8!+>$!+l+*h;$J>X4nPvV$Ur$#1UiasBR;OyGE&l;Sh=8%9h&ZrmYb?*Ikg~Dck}#%{-iLe>4WlP4z|75I_v#
o)<FaRcyEu7y*J#S>oZ>2{@#@aK#n^(Y{l*y__M7YUCX?K{*@nhPTC=3JHyOW7?~MqMz_X?c)lLC4%l7b$JO?k+EVLxhfgc>!>?=eL(cCy$K
V{uD``m93~A72x!7SN=(|K8;qNj2U|<5C&oC@y_=7Gnw35<*q?J&>X^@+-UZ68@^6(oYvkKmo$tfkHLRk}3j=8S4;I%3!Q4LFVfIvXkC>YlT
hC0e$7F^cS(Op|$&xrZptt<Ik$Rn#&VQf}F{9!?=z1D${p4MsE`w(wFoo>#$1zW(WRnOc@^09}UONpTvVyx_{6N+>*reE*()%@3BEglq9Pt4
4k7*+@CQ&+=FWnJ|KSM7s&Y|v3FhiD$Qir^Cay=k-~#UYM1dR=aJd1kY^avijo$j+9Ft)4;*|9!RJ|DY)(Mh{fD)x$>^6j4?;Pf*x5^u&$Sr
5~hrRWqk_Y9UHkMtOPvQ5n+glpB8b88<y`io6*v;BUnbJ4UtoN}l_&PbT|hW}o$K{Y`U6uTB=IsrQunZC}kpg6)d^;aYkahE5r-GnXh3yQ7a
gmt9CLjcx(tunW-aJ7R08_OVf<gK68X-{{sN-s<$%rbtH(w0k~;#_iaDt}v9UScrkN8|A#pMb&N)y5hLN=nd%=mMhqbiQuw7-O7OYWMy{sZF
pX}##^O)8^817Q7d{e-?Kp>Bxyou#IESYb1q%Ty`2$mu6J9PZ$-3iMg$@#6pv)cqA~RpWP}9%qbN0_^z(fmgHoE?9p4B`VYaaoAl1x1({U)Q
i9KO;zzJ&yn6M|}*}fQ@5j3^+@WceD&YQv-Sdy<(6yVZ8Kg!0F{$QMx_@>Beru<X-p%gVhRV1i}!9tYc46Y&U1c`kmj}jZgQ}driIPZdZfFh
%#4gE`^^^Nb4{@9zMuRuY&A*Njb5hL+dc*+(K6v8>y8McfMBY>J>iosDTcfdi|vioey{}v=f!7^dG1r6;2hU9kJ3FmwRmZOoJT{sR=U!=|`n
?WA+pj3#;`KmIw-c&BTwscFqJoBdNM29DC>kIEvLr0~$6vLHY>ZMyslw-#-Vz7p6aM{7?-E#MG8)VSRkcxfVm{e%OPSEN3XJ2i{5?t8&QH6S
vrThcs;O)ezA_9>bs7lH;fmQOehO1g&Rr-QE6uRQ7U{e^tq>FWyt#O-=x$p@<Q-*C?56%+PG-?J+_2|76SU$~bGiJ9iZCj#WXN%d)Qcr*ypi
AmIpoih3)ua%lq)HJjP~pON0V=ud{pkm6a-xhUY$iZJ2%3JxrfYulGd83o1w<Qs=`O@<n@^IqZ@y@Ssk@zsM(r131ha*JAYNF&@j00bjKag+
DjtkefmxUDZ>?;VT0gzN=<NuHI8awLZudY<o)W{KTVg0*AmSkI<=>YFL4dcQ+loz#)KX%3%Uz)lHJG>D<^Fwd8D}Pl1YU&1mU>dw1p$*2QR-
s}cNJcV;I#?bXmTs#XjL2TE2-SP<O&D~8{n}tQ2YGzmwIoHw*ZI+LecNcn2J7<w?kZY2+qV`_2)QH&I2{0YG~fe$<~jAlnAKedJct#9yZyOj
W;rV5pV}_Jn52@!t^r~=~su1e~pu}Nkd^pwS6mL&LoX$*LWAyxr-8T1H?W*g4`gHNA+Oy3oY<<nBJ?c9>Or`f(#~W0s2D9uxHgz0?}iFirs3
J(UVA8*)X0yg~}@ZApLl#XFSEkl=%|V#JJ)quzM+mMt0nKY)OIq8{pA$<839q8r68CrqZv!^wTQyktK4p47zol4X&De$=k*YR~>*j;{NFQ1F
3n?YGR%WovU|njnXv;U4zcKFVy+)1UNTh>iOEUZ*3{oVl<NCAFX-qeS80nC${w~RnFy1fBSn|r1IyU+)j5qx%~==Xg;}}e#?_v4Uuv4eMjfA
(>Y?c;f|<>Fm@XXbV&Kq!wyurogX>|k(%O#9jMZ~&gBlkvE7lrWw+|vevIPOmKf3?TkPU%w%E^sM<{9Mvd!~5d{;RQI?q15<@~tgJX@o4F6n
ePYc<buanSB|sPB#$FmWpH?FQUv!XW$K_|F8?NTHXeWYMMCw0o!j4S<apFtDlcZLOk*JeSs_lX@~v!Ad)6&$<;Q&0%eMksl~c9uUg{tTbs|N
!d5zJD)XSo;J1KAtZ_m1}E7F*c(u`I_iKs*ty*_?a-2jQXImz2`@R(mQZb<HN;#Kca*g^5Wo%SPgdDN=g>Mu2(ZEawzTW_)<5NSEryNg0E{#
yIE7iQJupIzDz6fTS+S>{nOM;zBOj`<#bc7^?djSSvP&|p@j-H6LXc>4KZinM`PNY7!K%?nvIE8Xt4BNPNvMOG(vuN-_%AmYF?yJM_WCm9I5
rHGZAJ^8$}b?-OGKC}-bE*PiI?Wh2AK029XB?^d=6i8Hix=%%7d?Q5zaY?(|q1d=bdz3$4)@L+$4`m^nU4t{_nxd3RKbWQtW<ji(NR&Cn3;%
#Fy1T55MLv(j1CP7GN^%sw(NcUQ(xGzjP}`6d2ZaH?@F7&>uB|{@C)e8Zjj~ep`p9BUT9O<Zg-cjupm5v{~K6yi2)!_VVsYJo+u2kiaeUvjs
?BK8Hm=3pu~t2{wPILFTuA0A4oI>`(vu6GT`yYIzsxnHSir1F~0ZMC6bB!xiP%|FH_|ImEdAs?NOOZO75vxXONSXPf_qLw$gJ;O!T9Pg8ySG
*$gluOX|hIPe`?zGqqp-vs(92>kh%Y@1bD@cGlwIl^8hPW~zV?#urGJZoCN
"""
PATCH = r'''"""Exact positive rescaling only; keep original four-source capsule intact."""
from pathlib import Path
import hashlib
p=Path(__file__).resolve().parent
s=(p/'independent_audit.py').read_text()
assert hashlib.sha256(s.encode()).hexdigest()=='f8c7d55d100d0d2320be41d99262c3bee49f667234d61e71f8e0dd49ab5be5c7'
a='  vals=[h-d(n,v) for v in I];assert all(v>=0 for v in vals)'
b='  gn=gcd(*n);assert gn>0;n=tuple(x//gn for x in n);h=d(n,a)\n'+a
assert s.count(a)==1;s=s.replace(a,b)
a=' S=[];U=[];H=[];deg=[];zero_primitives=0'
b=' common=0\n for row in K:\n  for x in row:common=gcd(common,x)\n assert common>0\n K=[tuple(x//common for x in row) for row in K]\n'+a
assert s.count(a)==1;s=s.replace(a,b)
(p/'independent_reduced.py').write_text(s)
r=(p/'REPLAY.py').read_text()
assert hashlib.sha256(r.encode()).hexdigest()=='76319a92605c0f157adc6abe86e93f343765cca7ec46ffc0419d5daf5b0f1087'
a='from independent_audit import run as independent'
assert r.count(a)==1;r=r.replace(a,'from independent_reduced import run as independent')
(p/'REPLAY_REDUCED.py').write_text(r)
print('EXACT_POSITIVE_RESCALING_PATCH_PASS')
'''
STAGES = r'''"""Three finite exact stages, CPython 3.13.5 standard library, never -O.
Input: canonical PN03 and the four pinned source files; speed_patch.py applied.
"""
from pathlib import Path
from fractions import Fraction
import sys,json,gzip,csv,hashlib,time,base64,zlib
sys.set_int_max_str_digits(0)
from codec import reconstruct,parse,topology,dot,sub,cross,det
from exact_audit import audit,rows
from independent_reduced import run as independent
from REPLAY import complete,witnesses
BASE=Path(__file__).resolve().parent
SHA='0470008c42fd61ca27045b001cddee34ab68a954dc6e8ec0198a63e9715409c8'

def inputs():
 raw=(BASE/'capsule.pn03').read_bytes()
 assert len(raw)==10525 and hashlib.sha256(raw).hexdigest()==SHA
 assert zlib.decompress(base64.b85decode(''.join((BASE/'capsule.b85').read_text().split())))==raw
 I,D,T,extra=reconstruct(raw)
 assert len(I)==258 and len(T)==512 and len(str(D))==2274
 D0,J,ops,TT,K,pr,po,wi=parse(raw)
 assert D0==10**18 and len(ops)==81 and all(len(dep)==1 for t,b,dep in ops)
 assert (K,pr,po)==(3467702,138,132)
 return raw,I,D,T

def main():
 assert __debug__
 step=sys.argv[1];out=BASE/'verified';out.mkdir(exist_ok=True);start=time.monotonic()
 if step=='first':
  raw,I,D,T=inputs();R,P=audit(I,T,D,expected=(1,1,0));complete(I,R)
  assert (R['V'],R['E'],R['F'])==(258,687,431)
  assert not R['degeneracies'] and R['zero_edge_primitives']==0
  for name,array in [('raw_vertices.csv.gz',I),('vertices.csv.gz',P),('triangles.csv.gz',T)]:
   with gzip.open(out/name,'wt',newline='')as f:csv.writer(f).writerows(array)
  (out/'exact_report.json').write_text(json.dumps(R,indent=2))
  print('FIRST_COMPLETE_EXACT_PASS',flush=True)
 elif step=='second':
  B=independent(out);assert B['zero_edge_primitives']==0
  print('SECOND_COMPLETE_EXACT_PASS',flush=True)
 elif step=='last':
  raw,I,D,T=inputs();R=json.loads((out/'exact_report.json').read_text())
  assert I==rows(out/'raw_vertices.csv.gz') and T==rows(out/'triangles.csv.gz')
  assert D==int(R['raw_denominator'])
  A=int(R['centroid_multiplier']);B=tuple(map(int,R['centroid_subtract']))
  P=[tuple(A*p[k]-B[k]for k in range(3))for p in I]
  assert P==rows(out/'vertices.csv.gz')
  ww=witnesses(raw,I,T,R,P);print('ROOTED_PRIMAL_POLAR_WITNESSES_PASS',flush=True)
  shift=(17*D,-11*D,23*D);II=[tuple(p[k]+shift[k]for k in range(3))for p in I]
  Wt=0;Mt=[0]*3
  for a,b,c in T:
   v=det(II[a],II[b],II[c]);Wt+=v
   for k in range(3):Mt[k]+=v*(II[a][k]+II[b][k]+II[c][k])
  W=int(R['W']);M=tuple(map(int,R['M']))
  assert Wt==W and Mt==[M[k]+4*W*shift[k]for k in range(3)]
  print('TRANSLATION_MOMENT_COVARIANCE_PASS',flush=True)
  rejected=[];bad=T.copy();bad[0]=(bad[0][0],bad[0][2],bad[0][1])
  for name,triangles in [('reversed_triangle',bad),('missing_triangle',T[:-1])]:
   try:audit(I,triangles,D)
   except AssertionError:rejected.append(name)
   else:raise AssertionError('corruption accepted')
  R2=json.loads((out/'independent_report.json').read_text())
  assert R2['class_SUH']==[1,1,0] and R2['zero_edge_primitives']==0
  receipt=dict(status='NIMBLE_WILLOW_98_PN03_C1374_EXACT_RECOVERY_PASS',
   capsule_sha256=SHA,VEF=[258,687,431],C=1374,SUH=[1,1,0],
   stable=R['stable'],unstable=R['unstable'],saddles=R['saddles'],
   degeneracies=R['degeneracies'],zero_edge_primitives=0,
   centred_moments=R['centred_moments'],witnesses=ww,
   raw_denominator_digits=len(str(D)),centred_denominator_digits=len(R['centred_denominator']),
   volume_approx=float(Fraction(W,6*D**3)),
   raw_centroid_approx=[float(Fraction(m,4*W*D))for m in M],
   translation_moment_covariance=True,rejected_corruptions=rejected,
   constant_volume_density=1,external_publication_claim=False)
  (BASE/'NIMBLE_RECEIPT.json').write_text(json.dumps(receipt,sort_keys=True,indent=2)+'\n')
  print(json.dumps(receipt,indent=2),flush=True)
 else:raise ValueError('use first, second, or last')
 print('STAGE',step,'SECONDS',time.monotonic()-start,flush=True)
if __name__=='__main__':main()
'''
def decode(text, size, sha):
    raw=zlib.decompress(base64.b85decode(''.join(text.split())))
    assert len(raw)==size and hashlib.sha256(raw).hexdigest()==sha
    return raw
body=decode(BODY,10525,'0470008c42fd61ca27045b001cddee34ab68a954dc6e8ec0198a63e9715409c8')
src=decode(SOURCES,18924,'dbda2d8354f20195aba93630dcf10c4ffa0fdfa8282a1979603275310e583f2c')
files=json.loads(src)
assert set(files)=={'REPLAY.py','codec.py','exact_audit.py','independent_audit.py'}
for name,text in files.items():
    (BASE/name).write_bytes(text.encode('utf-8'))
(BASE/'capsule.pn03').write_bytes(body)
(BASE/'capsule.b85').write_text(BODY,encoding='ascii')
(BASE/'sources.json').write_bytes(src)
(BASE/'speed_patch.py').write_bytes(PATCH.encode('utf-8'))
(BASE/'verify_stages.py').write_bytes(STAGES.encode('utf-8'))
(BASE/'SUMMARY.json').write_text(json.dumps(dict(V=258,E=687,F=431,raw_bytes=10525,
    raw_sha256=hashlib.sha256(body).hexdigest())),encoding='ascii')
print('PINNED_BODY_AND_COMPLETE_SOURCES_RECOVERED')
```
