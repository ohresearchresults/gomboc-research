# figure-0566

AI research report · 2026-09-26 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Rapid Raven 22 — конечный masslift, точный первый контакт и новый рациональный L18-потомок

## Итог

**Собственный strict110/E≤249/weak000 в этой работе не получен.** Получены три воспроизводимых результата, выходящих за первый малый совместный спуск:

1. Буквальный `masslift57` исполнен, а затем **точно доказано, что на всей его первой допустимой компоненте параметра сохраняются оба исходных U и оба исходных S**. Следовательно, на этом луче до первого контакта не может уничтожиться ни последний P, ни последний Q, несмотря на отрицательные производные обеих глубин.
2. Первый контакт локализован точным полиномом и пройден до рационального `t=1/32`: действительно исчезает вершина27, меняются максимальные грани и E204→201. После пересборки фактического hull выполнено **новое конечное физическое компенсирование момента**, с непересекающимися фиксированными ободами контроллеров. Получено точное однородное тело V74/E201/F129, strict525, weak000, с прежним физическим центром. Это не110 и не улучшение census; это исполненный переход между комплексами, включая точное измерение и устранение ошибки старой формальной массы.
3. Получен отдельный рациональный потомок **R22-B7: V75/E204/F131, собственный222, weak000**, с P=0.0977248047665494 и Q=0.062093728967811124. Обе глубины меньше буквального L18; произошла настоящая смена ребра `(1,10)→(2,11)`. Его координатный файл имеет всего4392 байта. Полные75 исходных строк входят в капсулу ниже. Сохранён также соседний, невыигрывающий R22-B6 с собственным334 и двумя дополнительными строго положительными барами порядка10^-12.

Это не утверждение глобального рекорда относительно всех тел журнала. Центральное уничтожение исходных P/Q остаётся нерешённой частью направления; ограничение ниже относится к конкретному исполненному родительскому лучу, а не ко всем L18-деформациям, всем массо-компенсированным картам или классу E≤249.

## Прочитанные входы и идентичность родителя

Оба поставленных файла прочитаны полностью, включая конец журнала и весь буквальный код родителя:

- `research-journal(20260926-135740).md`: 360800 байт,1550 физических строк, SHA-256 `63760151d6149b50c8421728c9166bb71808ca30ac77edce17177fd414667417`.
- `J69_frontier_and_exact_L18_overhang(1).md`:11541 байт,82 физических строки, SHA-256 `9f5f451571aa23c4af2ec615b31b693b6bd2786c87f8b8f2a0c41a99ef1fb423`.

Идентичность родителя `figure-0564` дополнительно проверена побайтно: взять его Markdown от `# Clear Harbor 55`, нормировать окончание к одному LF и сериализовать как `json.dumps({'version':2,'result_markdown':markdown},ensure_ascii=False,separators=(',',':'))`. Получается35634 байта и именно SHA-256 `43bfbd73da649bfd2b1e41bbec8082606ae7b95b4fbeab380c1d5c6a7672bd34`. Кажущееся отличие хеша извлечённого Markdown от хеша payload было различием сериализации, не конфликтом научных данных.

Извлечённый без изменений `masslift57.py`:19060 байт, SHA-256 `d831cd40f09c3a2751f24ab8a1f5c137dedd79d27353d2b1926123098b0d45fe`. Старый архив не использовался и для воспроизведения результатов ниже не нужен. Ссылки на отсутствующие старые источники не подменялись догадками.

## Что действительно исполнено

Родительский код выбрал контроллеры `[10,10,23]`, то есть две касательные моды звезды10 и одну звезды23. Матрица физических моментов имеет ненулевой точный определитель; ранг равен3. Получены одинаковые отрицательные производные P и Q, приблизительно `-0.0010568737272552166`. Родительский dyadic-поиск действительно завершился на `t=1/512`, а не только содержал соответствующий `print`.

Наблюдались `L18_PARENT_EXACT_PASS` и `EXACT_FINITE_MASSLIFT_PASS [2,2,2] 204 1/512`. Маркер `OWN110_WEAK000_E249_CERTIFIED` **не наблюдался**.

Ниже перечислены **все** положительные бары каждого принятого точного объекта, а не только максимумы. Десятичные числа в таблице — приближения; капсула вычисляет и записывает их полные рациональные значения, birth/death, компоненты, cuts и attaining paths без числового порога. Все строки таблицы имеют additional-weak000 и primitive-zero000.

| Объект | V/E/F | strict(S,U,H) | Все P-глубины | Все Q-глубины |
|---|---:|---:|---|---|
| Буквальный L18 |75/204/131|222|0.10018756794854827|0.06712194454711798|
| Родительский `t=1/512` |75/204/131|222|0.10018550373576929|0.06711988035201905|
| Луч `t=1/256` |75/204/131|323|0.10018343951042938|0.06711781617971942; 4.864951784904043e-7|
| Луч `t=1/64` |75/204/131|525|0.1001710538946078|0.06710543162471673; 9.561550080879551e-5; 9.335270903365442e-5; 3.674221923328029e-5|
| Реальный hull при `t=1/32`, до нового компенсирования |74/201/129|525|0.10015402811854976|0.06708895595130665; 0.0010635851924042435; 0.0003893584410182596; 0.00020730515772700417|
| R22-C32: после нового компенсирования |74/201/129|525|0.10015453903674626|0.06708892016154654; 0.0014565004637337373; 0.0007287935245716879; 0.0003372794006384447|
| Реальный hull при `t=1/16` |74/201/129|637|0.10011370271080326; 5.897031801203603e-6|0.06705521053617301; 0.00366785022045359; 0.0011085445654188512; 0.0010988728394931587; 6.571936172727823e-6|
| R22-B7 |75/204/131|222|0.0977248047665494|0.062093728967811124|
| R22-B6 |75/204/131|334|0.09772476502584719; 1.5173237799879522e-12|0.06209362424195052; 2.7862480931226466e-12|

Таким образом, продолжение исходного луча сперва рождает новые Q-дефекты, затем меняет hull, а при `t=1/16` рождает ещё и дополнительный P. Уменьшение двух первоначальных максимальных глубин не было превращено в ложное заявление об уничтожении дефектов.

## Точный запрет на завершение первой компоненты родительского луча

Положим `x_i=p_i-c_L18`, а `y_i(t)` — буквальная функция `construct` выбранной карты. Общая конструкция родителя допускает степень4, однако **на исполненном направлении фактический полином первого контакта имеет степень2**.

Обозначим

`s(t)=det(y28(t)-y27(t), y46(t)-y27(t), y27(t)-y23(t))`.

Первое геометрическое событие имеет единственный корень r в интервале

`3323829/125000000 < r < 26590633/1000000000`,

то есть `0.026590632 < r < 0.026590633`. Численная разведка дала примерно0.02659063222155; доказательным результатом является рациональный интервал и знаковый сертификат, а не эта последняя десятичная запись.

Проверены все9417 off-facet опорных неравенств старого комплекса, все условия `h_f>0`, точная планарность и все внутригранные условия строгой выпуклости. Полиномы переводятся в целочисленную форму; положительность на интервале доказывается положительными коэффициентами Бернштейна. При верхнем конце интервала не проходят ровно три опорных неравенства:

`(face57=[23,28,27], outside46)`, `(face60=[23,27,46], outside28)`, `(face70=[27,28,46], outside23)`.

Их полиномы совпадают с одним и тем же s, а `-s'` имеет положительный сертификат на всём рассматриваемом интервале. Все остальные условия остаются строгими. Поэтому старая геометрия допустима на всей компоненте `0≤t<r`; сразу после r её нельзя использовать как поверхность фактического выпуклого тела.

На более длинном замкнутом интервале `0≤t≤26590633/10^9` отдельно сертифицированы строгие механические неравенства исходных U6, U62 и исходных S — большой18-грани и `[14,16,24]`. У U62 все семь соседей `[49,58,59,64,65,68,70]` неподвижны. У U6 меняется только относящийся к соседу14 guard; он линейный и остаётся строго положительным на всём интервале. Все остальные U6-guards постоянны.

**Следствие:** пока именно этот луч остаётся в первом старом комплексе, S≥2 и U≥2. Ни последний P, ни последний Q здесь уничтожиться не может. Это полиномиальный сертификат конечного препятствия, а не вывод из неуспеха line search. Он не запрещает другую карту, другие первичные вершины, другой центр или продолжение после пересборки hull.

Уже существенно раньше контакта подтверждён переход стабильности контроллерной грани `[2,10,15]` через ребро10–15. Единственный меняющий знак гранный guard имеет корень в точном интервале

`4965746572967/2251799813685248 < t_Qbirth < 39725972583737/18014398509481984`,

приблизительно0.002205234471904599. Его производная положительна, остальные два гранных guard положительны на всём `[0,1/256]`. Полные endpoint-аудиты показывают переход222→323 и новый Q-бар. Это локализованное рождение, не требуемое уничтожение исходного Q.

## Реальный контакт и физическое компенсирование после него

В точном рациональном endpoint `t=1/32` вершина27 больше не экстремальна. Три старые грани вокруг неё заменяются настоящей максимальной гранью `[23,28,46]`; V75/E204/F131 превращается в V74/E201/F129.

В системе `x=p-c_L18` старая формальная поверхность всё ещё даёт момент0, но фактический hull имеет центр

`(1.8441605293471082e-8, 4.28987533694031e-7, 8.274337502896833e-7)` приблизительно.

Его объём приблизительно1.2893762579548966, тогда как объём старой формальной поверхности приблизительно1.2893741407210089. Это не ошибка округления. Проверены точные тождества

`ΔV = -s(1/32)/6 > 0`,

`M_actual-M_formal = ΔV·(y23+y27+y28+y46)/4`.

Иными словами, расхождение целиком равно ориентированному тетраэдру, который старая формальная поверхность ошибочно вычитает после контакта.

Затем звёзды10 и23 вычислены **заново из настоящих новых максимальных граней**. Их фиксированные ободы попарно не пересекаются. Обод10 — `[1,2,11,15]`; новый обод23 — `[17,28,36,39,46]` в исходных материальных индексах. Для касательной моды d звезды используется `a·d=0` и точный оператор момента `D=B+(a·z)I/4`. Поэтому конечное касательное смещение меняет момент линейно и не меняет объём; между выбранными звёздами нет смешанных треугольников.

Три коэффициента нового компенсирования приблизительно равны

`(-0.02184767419225221, -0.02577583699475376, 0.00023395252950956017)`.

Это не бесконечно малый шаг. После него повторно проверены допустимость нового комплекса и полный фактический hull. Объём остался **точно** равным фактическому объёму до компенсирования, момент стал **точно0**, собственный центр — **точно0** в текущей системе координат. В исходной системе это тот же

`c_L18=(-598940702957066767579993/3094491948123633165600000, -41409701646081099765787543/309449194812363316560000000, -221127997915179023250323/1547245974061816582800000)`.

При компенсировании действительно сменился механический носитель: стабильная `[2,10,15]` уступила место `[10,11,15]`, а седловое10–15 — седловому11–15. Исходные P/Q при этом не уничтожены.

Полный strict-census R22-C32 в исходных материальных индексах:

- S: `[10,11,15]`, `[17,23,36]`, `[14,16,24]`, большая18-грань, `[23,28,46]`.
- U:6 и62.
- H:`[6,63]`, `[11,15]`, `[13,22]`, `[17,36]`, `[23,46]`.

Восстановление старых материальных индексов после удаления27 предусмотрено полем `source_material`; нельзя читать перенумерованную вершину61 как старую61 — здесь это старая62.

## Рациональный R22-B7 и сохранённый невыигрывающий R22-B6

Для отдельного конечного поиска освобождались все75 вершин:18 вершин большой грани перемещались в её плоскости, остальные — в трёх координатах. На каждом принимаемом состоянии перестраивался фактический hull и заново интегрировался его собственный центр. Численный поиск служил только выбором координат; точное доказательное воспроизведение начинается с полных строк `RAW7`, а не с предположения о воспроизводимости плавающего оптимизатора.

У R22-B7 объём равен

`1546682134640604290783573/1200000000000000000000000`,

а собственный центр равен

`(-59811157862551149789520322869587/309336426928120858156714600000000, -41302790594030898129739564248957291/309336426928120858156714600000000000, -11068344277099413455444999619371/77334106732030214539178650000000)`.

Это центр объёма всего реального тела, не среднее вершин и не прежний центр L18. Уменьшения максимальных глубин относительно буквального L18 составляют приблизительно2.45815% для P и7.49116% для Q.

Остаются S: большая18-грань и `[14,16,24]`; U:6,62; H:`[6,63]`,`[13,22]`. P имеет пик62, elder6 и attaining-edge13–22. Q имеет пик `[14,16,24]`, elder большую грань и attaining primal edge6–63. Размеры соответствующих cuts равны17 и27. Изменение истинной геометрии состоит в удалении ребра1–10 и добавлении2–11; заменены две настоящие треугольные грани. Число E при этом не изменилось.

Полные точные глубины R22-B7:

`P=9455596573630192984977503480054710235883650451167542216470686481729920061922462278807/96757385151275175591985121284952471744652807908115472151256742974300144623245003716307`.

`Q=126458628827419362968986220981586492999430950141245927295497909137369744117043435996341495457290689513394436334799/2036576493786908364234704699590726815570215979326152657261470310750233049096670604903765577189676980412127961562500`.

Соседняя более грубая рационализация R22-B6 не является222: у неё появляется U51 и S `[6,59,64]`, а также H51–56 и6–59. Два малых бара **строго положительны**. Их полные рациональные значения тоже восстанавливаются и записываются кодом. R22-B6 оставлен в капсуле как полезный пример чувствительности и как материальный невыигрывающий объект; он не замаскирован порогом1e-10.

## Надёжность аудита и границы результата

В новом ускоренном hull-аудиторе SciPy используется только для предложения троек. Каждая принятая плоскость проверяется на всех рациональных точках точными целочисленными знаками; все лежащие на ней точки собираются заново, а максимальный выпуклый многоугольник строится точным двумерным hull. Затем проверяются два противоположно ориентированных владельца каждого истинного ребра, связность граней и Euler2. Это сертификат полноты: принятые многоугольники являются настоящими максимальными гранями `conv(points)`, а непустая замкнутая по соседству связная совокупность таких граней не может быть собственной частью связной границы выпуклого3-тела. При неполной численной номинации код останавливается, а не объявляет неполный набор hull.

Масса независимо вычисляется двумя разбиениями на тетраэдры, со второй внутренней точкой и строго положительными объёмами всех её тетраэдров. Механика проверяется на максимальных гранях и настоящих рёбрах; диагонали интеграционного веера рёбрами не считаются. P/Q вычисляются точными grouped-level merge-алгоритмами, без удаления малых баров. Все конечные объекты из таблицы и все знаковые сертификаты повторно воспроизведены единым драйвером ниже.

Не доказана невозможность продолжения после первого контакта, невозможность других двухзвёздных карт или невозможность110/E≤249. Не заявлено, что компенсирование момента сохраняет желаемые S/U: R22-C32 как раз показывает обратное. Не заявлена точная траектория уничтожения исходных P/Q.

Наиболее полезное продолжение — брать компактный R22-B7 как геометрический checkpoint, включать в следующую конечную карту движение звезды62/её соседей либо существенное изменение стороны корня6, а контроллеры выбирать отдельно с проверенной вместимостью и фиксированными непересекающимися ободами. Старый луч нельзя просто экстраполировать: сохранение двух U и двух S до его первого контакта теперь доказано. При контакте уже имеется исполненный образец обязательной последовательности «новый максимальный hull → новая физическая масса → новые звёзды → конечное точное компенсирование → новый полный census».

## Автономная капсула

Ниже находятся **два полных исходных файла**, включая все75 родительских строк, все75 строк R22-B7, точную реконструкцию R22-B6, все вспомогательные функции, генераторы и аудиторы. Никакие данные из sandbox не необходимы для восстановления.

Исполненная среда: CPython3.13.5, NumPy2.3.5, SciPy1.17.0. Для доказательной части не нужны Torch, SymPy или GMP. Не добавлять `-S` к объединённой команде, поскольку драйвер импортирует NumPy/SciPy.

```sh
python -B raven22.py --out raven22_output > run.log
```

Наблюдаемые конечные маркеры включают:

```text
FIRST_HULL_EVENT_CERTIFIED 3323829/125000000 26590633/1000000000 degree 2 guardcount 9417 failed_at_upper [[57, 46], [60, 28], [70, 23]]
ORIGINAL_2U_2S_PERSIST_THROUGH_FIRST_VALID_COMPONENT
CONTROLLER_Q_BIRTH_BRACKET 4965746572967/2251799813685248 39725972583737/18014398509481984
R22_HULL_VOLUME_AND_MOMENT_TETRA_IDENTITY_PASS
R22_POST_CONTACT_RECOMPENSATION_EXACT_PASS
R22_BALANCED_GRID7_EXACT_PASS
R22_COARSE_GRID6_NOT222_EXACT_PASS
R22_COMPLETE_EXACT_HANDOFF_PASS_NO_110
```

У первых трёх диагностик в stdout имеются дополнительные поля; приведены значимые префиксы/поля. Последний маркер явно не является заявлением110.

Контрольные суммы исходников:

`masslift57.py` —19060 байт, `d831cd40f09c3a2751f24ab8a1f5c137dedd79d27353d2b1926123098b0d45fe`.

`raven22.py` —15100 байт, `93b85a6ad5319809104a7c4559bc5289676865da68391edc1338d02a707584af`.

Ключевые фактически воспроизведённые выходы:

| Файл относительно каталога результата | Байты | SHA-256 |
|---|---:|---|
|`parent/parent_audit.json`|52519|`9a0e3a6fe9d53f0746bc68e769566e95e81bb8078c08ec32f080de6e24d279e3`|
|`parent/chart.json`|12275|`5708e9d574d0b478994def44c644f8ef4d384adc17943c6a5e10b037a4b99f4c`|
|`parent/body.json`|18859|`b49763c8c0003bfb021d78aa6bbfd13c57efe4468f2dcc5f910560227ff09a30`|
|`parent/audit.json`|158885|`a7af444f62e5bde35947cb34556635d57251cb138b9112926c6cfb896bbc2548`|
|`polynomial/certificate.json`|9141|`2ba99b9ad5d933b393d3276ad053a1e7c36863b9b73d5f12cb8394d1b2baaa73`|
|`finite/ray_32_body.json`|27882|`9b5b958d6cacec524a6fa53a32f3cf2cd0c7007f36e341b19b3a9eacd2e5df69`|
|`finite/reclosed_body.json`|37793|`7af53c926c3028d213822e57318215c4c363336888ace6e29139ec45b82747aa`|
|`finite/reclosed_audit.json`|290155|`3164c23747185829ab923d230443123d4c7f7ebb4e0c71faed739cf00d28eab4`|
|`balanced/body.json`|4392|`bd11ca3c0700bccd1a99a4cc2171a725c8a5d8acae5f22992b265f1c2797fb59`|
|`balanced/audit.json`|67300|`12423b8058b8e5740aeb74d8eca0817ffc5c8cd4a312cc83f05822a7a84212c1`|
|`coarse6/body.json`|3954|`9a850522da40fd76121dbc309c2db0236915975ae304640b622db4673d665895`|
|`coarse6/audit.json`|61122|`c36837da846e49b42da2b54d46e1bbcc370aa94c4b77e75f3942f7aec25cc6f7`|

Полный `manifest.json` имеет3282 байта и SHA-256 `cb2a6c08abea0dd8f35041bb505219edf339433553b81b1e5562e8e1323a795a`. Все прочие лучевые тела из таблицы также генерируются, полностью аудируются и включаются в manifest.

Архив исходников, полного stdout и всех точных отчётов (`raven22_handoff.zip`) — дополнительная удобная копия, не замена следующему полному коду.

### Файл1: `masslift57.py`

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

### Файл2: `raven22.py`

```python
"""Floating nomination only; all supporting planes, face polygons and closure exact."""
from fractions import Fraction as F
from functools import reduce
from math import gcd,lcm
from collections import deque
import numpy as np
from scipy.spatial import ConvexHull
import masslift57 as m

def certified_hull(points, nominations=None):
 p=list(dict.fromkeys(tuple(F(x) for x in q) for q in points))
 assert len(p)>=4
 D=lcm(*(x.denominator for q in p for x in q));z=[tuple(int(x*D) for x in q) for q in p]
 if nominations is None:nominations=ConvexHull(np.array(p,dtype=float)).simplices
 planes=set()
 for i,j,k in nominations:
  i,j,k=int(i),int(j),int(k);n=m.cross(m.sub(z[j],z[i]),m.sub(z[k],z[i]))
  if not any(n):continue
  h=m.dot(n,z[i]);ss=[m.dot(n,q)-h for q in z]
  if min(ss)<0<max(ss):continue
  if min(ss)==max(ss):continue
  a=tuple(n)+(h,)
  if max(ss)>0:a=tuple(-x for x in a)
  g=reduce(gcd,(abs(x) for x in a),0);planes.add(tuple(x//g for x in a))
 assert len(planes)>=4
 faces=[]
 for a in sorted(planes):
  assert all(m.dot(a[:3],q)<=a[3] for q in z)
  ids=[i for i,q in enumerate(z) if m.dot(a[:3],q)==a[3]]
  faces.append(m.polygon(ids,z,a[:3]))
 keep=sorted({i for f in faces for i in f});remap={i:j for j,i in enumerate(keep)};faces=[[remap[i] for i in f] for f in faces]
 owners={};directions={}
 for fi,f in enumerate(faces):
  for i,j in zip(f,f[1:]+f[:1]):
   e=tuple(sorted((i,j)));owners.setdefault(e,[]).append(fi);directions.setdefault(e,[]).append(i<j)
 edges=sorted(owners)
 assert all(len(owners[e])==2 and directions[e][0]!=directions[e][1] for e in edges),'Nomination not a closed exact hull; no certificate'
 adj=[[] for f in faces]
 for e in edges:
  a,b=owners[e];adj[a].append(b);adj[b].append(a)
 reached={0};todo=[0]
 while todo:
  a=todo.pop()
  for b in adj[a]:
   if b not in reached:reached.add(b);todo.append(b)
 assert len(reached)==len(faces)
 assert len(keep)-len(edges)+len(faces)==2
 return dict(points=[p[i] for i in keep],material=keep,faces=faces,edges=edges,edge_faces=[owners[e] for e in edges])

def certified_audit(points,nominations=None):return m.report(certified_hull(points,nominations))

from fractions import Fraction as F
from math import lcm,factorial
from pathlib import Path
import json,hashlib
import masslift57 as m

def conv(x):
 if isinstance(x,str):
  try:return F(x)
  except ValueError:return x
 if isinstance(x,list):return [conv(t) for t in x]
 if isinstance(x,dict):return {k:conv(t) for k,t in x.items()}
 return x

def trim(a):
 a=list(a)
 while len(a)>1 and a[-1]==0:a.pop()
 return a

def add(a,b):
 c=[0]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return trim(c)

def neg(a):return [-x for x in a]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)

def scale(a,s):return trim([x*s for x in a])
def dot(a,b):
 c=[0]
 for x,y in zip(a,b):c=add(c,mul(x,y))
 return c

def cross(a,b):return [sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0]))]
def vs(a,b):return [sub(x,y) for x,y in zip(a,b)]
def vn(a):return [neg(x) for x in a]
def det(a,b,c):return dot(a,cross(b,c))
def ev(a,t):
 v=0
 for x in a[::-1]:v=v*t+x
 return v

def bern(a,b):
 # Positive common multiplier b.denominator^n*n!; interval [0,b].
 a=trim(a);n=len(a)-1;L=b.numerator;K=b.denominator
 return [sum(a[j]*L**j*K**(n-j)*factorial(k)//factorial(k-j)*factorial(n-j) for j in range(k+1)) for k in range(n+1)]

def build(R,ch):
 yy=[m.construct(R['P_vectors'],R['faces'],ch,F(i)) for i in range(5)]
 bases=[]
 for i in range(5):
  v=[F(1)]
  for j in range(5):
   if j!=i:v=scale(mul(v,[-j,1]),F(1,i-j))
  bases.append(v)
 c=[[[sum(bases[i][k]*yy[i][j][r] for i in range(5)) for k in range(5)] for r in range(3)] for j in range(len(yy[0]))]
 c=[[trim(a) for a in row] for row in c]
 D=lcm(*(a.denominator for row in c for p in row for a in p))
 Y=[[[int(a*D) for a in p] for p in row] for row in c]
 test=m.construct(R['P_vectors'],R['faces'],ch,F(7,11))
 assert [[ev(a,F(7,11))/D for a in row] for row in Y]==[list(p) for p in test]
 return Y,D

def prove(R,ch,out):
 Y,D=build(R,ch);faces=R['faces'];x=R['P_vectors']
 L=F(26590632,10**9);B=F(26590633,10**9)
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 normals=[cross(vs(Y[f[1]],Y[f[0]]),vs(Y[f[2]],Y[f[0]])) for f in faces]
 heights=[dot(n,Y[f[0]]) for n,f in zip(normals,faces)]
 s=dot(normals[70],vs(Y[27],Y[23]));assert faces[70]==[27,28,46]
 assert ev(s,L)>0>ev(s,B)
 assert min(bern(neg([i*s[i] for i in range(1,len(s))]),B))>0
 fails=[];geocount=0
 for fi,f in enumerate(faces):
  assert min(bern(heights[fi],B))>0
  for i in range(len(Y)):
   gap=sub(heights[fi],dot(normals[fi],Y[i]))
   if i in f:assert gap==[0]
   else:
    geocount+=1
    if min(bern(gap,B))<=0:
     assert gap==s,(fi,i,'unexpected polynomial',gap==s)
     fails.append([fi,i]);assert min(bern(gap,L))>0
  for i,j in zip(f,f[1:]+f[:1]):
   nn=cross(normals[fi],vs(Y[j],Y[i]))
   for k in f:
    if k not in (i,j):
     val=dot(nn,vs(Y[k],Y[i]));assert min(bern(val,B))>0
 print('FIRST_HULL_EVENT_CERTIFIED',str(L),str(B),'degree',len(s)-1,'guardcount',geocount,'failed_at_upper',fails,flush=True)
 # Both original U roots and both original S roots remain strict until the first hull event.
 frozen=[]
 for i in [6,62]:
  nb=sorted({b if a==i else a for a,b in R['edges'] if i in (a,b)})
  guards=[]
  for j in nb:
   g=neg(dot(Y[i],vs(Y[j],Y[i])));assert min(bern(g,B))>0
   guards.append((j,len(g)-1))
  frozen.append([i,guards])
 for fi in R['S']:
  f=faces[fi]
  for i,j in zip(f,f[1:]+f[:1]):
   g=dot(cross(normals[fi],vs(Y[j],Y[i])),vn(Y[i]));assert min(bern(g,B))>0
 print('ORIGINAL_2U_2S_PERSIST_THROUGH_FIRST_VALID_COMPONENT',frozen,flush=True)
 # Locate an explicit S/H birth at facet [2,10,15].
 fi=14;assert faces[fi]==[2,10,15];f=faces[fi];GG=[dot(cross(normals[fi],vs(Y[j],Y[i])),vn(Y[i])) for i,j in zip(f,f[1:]+f[:1])]
 lo=F(1,512);hi=F(1,256);changed=[k for k,g in enumerate(GG) if ev(g,lo)<0<ev(g,hi)]
 assert len(changed)==1;k=changed[0];g=GG[k]
 for _ in range(45):
  mid=(lo+hi)/2
  if ev(g,mid)>0:hi=mid
  else:lo=mid
 assert min(bern([j*g[j] for j in range(1,len(g))],F(1,256)))>0
 for j,gg in enumerate(GG):
  if j!=k:assert min(bern(gg,F(1,256)))>0
 print('CONTROLLER_Q_BIRTH_BRACKET',str(lo),str(hi),'decimal',float((lo+hi)/2),'edge',list(zip(f,f[1:]+f[:1]))[k],flush=True)
 # Primitive integer event polynomials are included in the certificate JSON and generated from exact parent.
 from math import gcd
 from functools import reduce
 def primitive(a):
  g=reduce(gcd,(abs(t) for t in a),0);return [t//g for t in a]
 cert={'parent_points_source_sha256':'d831cd40f09c3a2751f24ab8a1f5c137dedd79d27353d2b1926123098b0d45fe','hull_bracket':[L,B],'hull_polynomial_ascending':primitive(s),'Q_birth_bracket':[lo,hi],'Q_birth_polynomial_ascending':primitive(g),'hull_failed_guards':fails,'support_count':geocount,'frozen_U_guards_degrees':frozen,'protected_S_faces':[faces[i] for i in R['S']]}
 m.dump(out/'certificate.json',cert)


RAW7 = r"""
-11439418,-3850063,266376;-11436586,-2891673,-2078758;-11012478,-2268283,-3884988;-10198402,-1802514,-5565178;-9510348,-6927925,6508810
-9366848,-1548293,-6739759;-8478663,-8202318,8938576;-8378931,-1404158,-7749168;-7644821,-1356105,-8354867;-6450171,-1391943,-9061728
-6145891,2597816,-1494981;-6241984,2345593,36135;-5623246,2386234,828841;-5235324,-1521597,-9552644;-5121264,2359319,1410928
-5260944,3446660,-1971281;-4273979,2164859,2318946;-4290349,293681,4244065;-4147867,1843405,2773686;-4141030,1258405,3392028
-4113528,4422686,-2267736;-3937485,4202473,-812284;-3481009,-1810034,-10014104;-3329731,549552,4149437;-3408971,4159659,315756
-3278652,4707395,-3115791;-2748873,-1958542,-10137900;-2607660,636130,4067037;-2939567,-310459,4675082;-2370803,4875226,-3611610
-2016463,-2134865,-10193873;-2280378,4424803,718191;-1977909,3912817,1432905;-1542658,3702017,1773344;-1264265,-2344367,-10181882
-1187049,4712991,-4311133;-993382,3683080,1885113;-516110,-2582496,-10097209;-443297,4592143,-4372164;-65807,3904189,1768343
-29868,788154,3545525;245829,-2761621,-9946813;160797,561054,3564566;752453,723937,3323126;997862,-2929127,-9726299
876498,1627910,2986509;1262262,4204445,1562564;2405332,4462279,-3190451;1733591,-3083920,-9436565;3076914,-1717501,-8776968
2446935,-3226134,-9078737;3863116,4048136,-959866;3132038,-3356539,-8654079;2958214,4725441,1046972;3302520,-4439629,-8096073
3771261,-3499268,-8165843;3688981,4039304,1282536;4185393,3471690,1378209;4366444,-3628525,-7620150;4155985,-5179565,-6854522
4469579,3135309,1334821;4735947,2790900,1274870;4910575,-3748103,-7021958;4981252,2443667,1199756;5287381,-4753653,-5513321
5388246,-833841,-5916406;5506849,1716087,863424;5948514,952468,446780;5881216,-4223874,-4499633;6297887,159744,-53863
6294597,-3598061,-3572441;6529699,-611856,-601691;6656697,-1384755,-1223312;6554121,-2893685,-2704614;6669225,-2149699,-1922826
"""
GRID6_PATCH = [(4,1,-692793),(18,1,184341),(19,1,125841),(21,0,-393749),
 (25,1,470739),(34,0,-126427),(46,1,420445),(48,2,-943657),
 (50,0,244693),(59,0,415599),(59,1,-517957),(62,0,491057),
 (72,1,-138475),(74,0,666923)]

def body_from_rows(rows,D):
 points=[tuple(F(x,D) for x in row) for row in rows]
 for i in m.PATCH:
  x,_,z=points[i]
  points[i]=(x,(-F(68526367,100000)-272*x-409*z)/1000,z)
 return points

def summary(R):
 mapping=R.get('source_material',list(range(75)))
 material=[mapping[i] for i in R['material']]
 ff=lambda i:[material[v] for v in R['faces'][i]]
 return dict(VEF=[R[k] for k in ['V','E','F']],strict=R['strict'],
  weak=R['additional_weak'],zeros=R['primitive_zero'],
  centroid=[str(v) for v in R['centroid']],
  S=[ff(i) for i in R['S']],U=[material[i] for i in R['U']],
  H=[[material[i] for i in edge] for edge in R['H']],
  P=[dict(peak=material[b['peak']],elder=material[b['elder']],
     depth=str(b['depth']),decimal=float(b['depth'])) for b in R['P_bars']],
  Q=[dict(peak=ff(b['peak']),elder=ff(b['elder']),
     depth=str(b['depth']),decimal=float(b['depth'])) for b in R['Q_bars']])

def run(out):
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 m.audit=certified_audit
 # This executes the literal parent's chart and its finite dyadic search.
 m.main(str(out/'parent'),128)
 R=conv(json.loads((out/'parent/parent_audit.json').read_text()))
 ch=conv(json.loads((out/'parent/chart.json').read_text()))
 assert ch['control_material']==[10,10,23]
 rim=lambda faces,i:{j for f in faces if i in f for j in f}-{i}
 assert rim(R['faces'],10).isdisjoint(rim(R['faces'],23))
 assert ch['derivative_P']==ch['derivative_Q']<0
 assert conv(json.loads((out/'parent/audit.json').read_text()))['parameter']==F(1,512)
 prove(R,ch,out/'polynomial')
 dest=out/'finite';dest.mkdir(exist_ok=True)
 for t in [F(1,256),F(1,64),F(1,32),F(1,16)]:
  y=m.construct(R['P_vectors'],R['faces'],ch,t)
  Vformal,Mformal=m.mass(y,R['faces']);assert Mformal==m.ZERO
  valid=m.valid_complex(y,R['faces']);assert valid==(t<=F(1,64))
  A=m.audit(y)
  expected={256:([75,204,131],[3,2,3]),64:([75,204,131],[5,2,5]),
            32:([74,201,129],[5,2,5]),16:([74,201,129],[6,3,7])}[t.denominator]
  assert [A[k] for k in ['V','E','F']]==expected[0] and A['strict']==expected[1]
  assert A['additional_weak']==A['primitive_zero']==[0,0,0]
  name='ray_'+str(t.denominator)
  m.dump(dest/(name+'_body.json'),dict(points=y,density=1))
  m.dump(dest/(name+'_audit.json'),A)
  m.dump(dest/(name+'_summary.json'),summary(A))
  if t==F(1,32):
   assert A['material']==[i for i in range(75) if i!=27]
   # The omitted tetrahedron is exactly the formal/physical discrepancy.
   s=m.det(m.sub(y[28],y[27]),m.sub(y[46],y[27]),m.sub(y[27],y[23]))
   dv=-s/6
   tetra_center=m.mul(m.add(m.add(y[23],y[27]),m.add(y[28],y[46])),F(1,4))
   assert A['volume']-Vformal==dv>0
   assert A['moment']==m.mul(tetra_center,dv)
   print('R22_HULL_VOLUME_AND_MOMENT_TETRA_IDENTITY_PASS',flush=True)
   # Reconstruct both controllers from actual new maximal faces.
   pts=A['points'];faces=A['faces'];ids={v:i for i,v in enumerate(A['material'])}
   controls=[];images=[]
   for material in [10,23]:
    i=ids[material];basis,im=m.star(pts,faces,i)
    controls.extend((i,v) for v in basis);images.extend(im)
   assert not any(ids[10] in f and ids[23] in f for f in faces)
   assert rim(faces,ids[10]).isdisjoint(rim(faces,ids[23]))
   for sel in m.combinations(range(4),3):
    C=[images[j] for j in sel]
    if m.det(*C)!=0:break
   else:raise AssertionError('No rank-three actual-hull controller')
   V,M=m.mass(pts,faces);coeff=m.solve_columns(C,m.mul(M,-1));z=list(pts)
   for a,j in zip(coeff,sel):
    i,d=controls[j];z[i]=m.add(z[i],m.mul(d,a))
   assert m.mass(z,faces)==(V,m.ZERO)
   assert m.valid_complex(z,faces)
   B=m.audit(z);assert B['centroid']==m.ZERO
   assert [B[k] for k in ['V','E','F']]==[74,201,129]
   assert B['strict']==[5,2,5] and B['additional_weak']==B['primitive_zero']==[0,0,0]
   assert B['volume']==A['volume']
   B['source_material']=A['material']
   B['reclose_controls']=[(A['material'][controls[j][0]],controls[j][1]) for j in sel]
   B['reclose_coefficients']=coeff
   m.dump(dest/'reclosed_body.json',dict(points=z,density=1))
   m.dump(dest/'reclosed_audit.json',B)
   m.dump(dest/'reclosed_summary.json',summary(B))
   print('R22_POST_CONTACT_RECOMPENSATION_EXACT_PASS',flush=True)
 # Literal rational checkpoints, not a claim about floating solver reproducibility.
 rows7=[list(map(int,row.split(','))) for row in RAW7.replace('\n',';').split(';') if row.strip()]
 assert len(rows7)==75
 rows6=[[round(F(x,10)) for x in row] for row in rows7]
 for i,j,v in GRID6_PATCH:rows6[i][j]=v
 for k,rows in [(7,rows7),(6,rows6)]:
  D=10**k;points=body_from_rows(rows,D);A=m.audit(points)
  assert [A[a] for a in ['V','E','F']]==[75,204,131]
  assert A['strict']==([2,2,2] if k==7 else [3,3,4])
  assert A['additional_weak']==A['primitive_zero']==[0,0,0]
  if k==7:
   assert A['P_bars'][0]['depth']<R['P_bars'][0]['depth']
   assert A['Q_bars'][0]['depth']<R['Q_bars'][0]['depth']
   assert set(map(tuple,R['edges']))-set(map(tuple,A['edges']))=={(1,10)}
   assert set(map(tuple,A['edges']))-set(map(tuple,R['edges']))=={(2,11)}
  dest=out/('balanced' if k==7 else 'coarse6');dest.mkdir(exist_ok=True)
  m.dump(dest/'body.json',dict(points=points,density=1))
  m.dump(dest/'audit.json',A)
  m.dump(dest/'raw.json',dict(D=D,rows=rows,patch=m.PATCH))
  m.dump(dest/'summary.json',summary(A))
  print('R22_BALANCED_GRID7_EXACT_PASS' if k==7 else 'R22_COARSE_GRID6_NOT222_EXACT_PASS',flush=True)
 files={str(p.relative_to(out)):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
        for p in sorted(out.rglob('*.json')) if p.name!='manifest.json'}
 m.dump(out/'manifest.json',files)
 print('R22_COMPLETE_EXACT_HANDOFF_PASS_NO_110',flush=True)

if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser()
 parser.add_argument('--out',default='raven22_output')
 run(parser.parse_args().out)
```
