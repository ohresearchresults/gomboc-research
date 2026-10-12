# figure-0502

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# RA37 — конечная сборка обратного терминального ребра MORSE6 и точный контроль всей высотной полупрямой

## Итог

**Собственный строгий110/additionalweak000 не получен.** Получены десять новых точно восстановимых рациональных однородных многогранников с истинным E≤249. Девять имеют единственную строгую неустойчивую вершину, additionalweak000, primitivezero000 и пустой физический P-штрихкод. У восьми из этих девяти обе точные обратные терминальные точки MORSE6 являются экстремальными вершинами, соединёнными истинными положительными рёбрами с неизменённой U=(0,107/100,0). Девятый — отдельно проверенный арифметически простой спутник с округлённой терминальной парой.

Таким образом, положительный терминальный вход реализован внутри полноценной конечной собственно-массовой U1-геометрии. Он больше не является только изолированной точкой. Оставшаяся проблема — устойчивые грани: семь U1-тел имеют класс312, одно514, одно716. Контроль с поднятой вершиной имеет(3,13,14).

Главный новый конечный контроль: **для каждого из девяти различных фиксированных корпусов изменение только высоты осевой вершины не может дать110. При любой действительной высоте выше всех фиксированных точек сохраняется S≥3 при фактическом изменяющемся объёмном центре.** Доказательство проходит через все события видимости и изменения максимального комплекса. Это не выборка высот, не вычисление при свободном центре и не исключение общего класса C2-тел.

## Источники и область использования

Полностью прочитаны все четыре переданных материала и весь `research-journal(20260923-031251).md`, включая буквальный родитель `figure-0500`, SHA-256 `628f77cad0ad9de768f16dbaf232b8d0b68852fcd00e848696417f026f6d9f5b`. Необходимых отсутствующих зависимостей для новых тел нет. Другие тела, упомянутые только в историческом журнале, не реконструировались.

Использованы буквальные P/Q/B, λ и рациональная точка MORSE6, а не приближённые коэффициенты. Гладкий собственный центр0 не переносился на конечные оболочки.

Терминальный вход взят при γ=−3/5,t=1/20. Его положительность при c≤1/10 применялась только после нового вычисления фактического центра конечного тела; дополнительно сам знак проверен непосредственно. Родительский `critical_apex_atlas.py` не выдаётся за выполненный атлас: в родителе он был невыполненным исходником. Здесь выполнен другой точный контроль.

## Конструкция

Обозначим точную терминальную точку через T:

`t=1/20; x=2t/(1+t²); y=x²; ρ=(1−t²)B(y)/(1+t²); s=−3t/5; e1=(1−s²)/(1+s²); e2=2s/(1+s²); T=(λx,P(y)+ρe1,xQ(y)+ρe2)`.

Буквальный P/Q/B включён в восстанавливаемый `morse6_skew.py`. Верхняя вершина A=(0,107/100,0). Остальные точки могут выходить с поверхности MORSE6; утверждения о вписанности в гладкое тело или о сохранённой доле его объёма не делаются.

Численная номинация использовала направления d_i и обратную цепочку относительно вспомогательного c_ref:

`p_i=c_ref+(1−η)[d_i·(p_(i+1)−c_ref)]d_i`.

После рационального замораживания все массы и знаки пересчитываются заново. c_ref нигде не заменяет фактический центр. Восемь параметрических checkpoint-ов сохранены буквально в binary64-hex; повторный прогон воспроизвёл все восемь целочисленных замораживаний. Точное восстановление тел от этого численного повтора не зависит.

В обычных вариантах добавлены отражение R(X,Y,Z)=(−X,Y,−Z), четыре нижние точки на одной горизонтальной плоскости и A. В ветвящемся варианте имеются три цепочки по12 точек в каждой половине, общий T, его отражение и нижний шестиугольник.

## Проверка

**Окончательный холодный прогон перебирает все опорные тройки точно, без Qhull и без сохранённых номинаций граней.** Проверяются опорные неравенства, максимальные многоугольные грани, истинные рёбра и противоположные владельцы, связность и Эйлер. Масса сверяется интегрированием из двух начал и тремя координатными дивергентными тождествами.

S вычисляется по полярным знакам при том же физическом центре и сверяется с попаданием основания перпендикуляра в грань. U и слабые U используют максимум всех выходящих знаков. H и слабые H используют полный отрезок и конус двух нормалей. Основа аудитора — переданный `circle_family.py`. Это один полный аудитор с перекрёстными проверками, не два независимых механических аудитора.

Точные контрольные тела дали tetra446/weak000, cube(6,8,12)/weak000 и prism446/weak123. Для всех десяти новых тел получены additionalweak000 и primitivezero000. Положительные P/Q-бары не порогуются; равные уровни обрабатываются одновременно. Проверены равенства числа положительных баров U−1 и S−1.

## Десять сохранённых конечных тел

V/E/F означают вершины/истинные рёбра/максимальные грани. Vol — заполненный объём; центры равны(0,c_y,0). Десятичные значения здесь — ориентиры, не точные входы. Все точные дроби находятся в генерируемых полных отчётах.

| Точное имя | V/E/F | Строгий S/U/H | Vol≈ | c_y≈ |
|---|---:|---:|---:|---:|
| RA37_K12_G4_716 |29/80/53|(7,1,6)|0.829815279323|−0.251936879406|
| RA37_K16_G4_312 |37/104/69|(3,1,2)|2.117307856131|−0.411780514940|
| RA37_K20_G4_312 |45/128/85|(3,1,2)|2.415180129131|−0.343900823726|
| RA37_K24_G4_312 |53/152/101|(3,1,2)|8.254614051207|−0.941902065054|
| RA37_K28_G4_312 |61/176/117|(3,1,2)|1.861275650975|−0.152392700715|
| RA37_K40_G6_514 |85/248/165|(5,1,4)|1.664584328816|−0.023804809772|
| RA37_K40_G4_312 |85/248/165|(3,1,2)|2.885081016242|−0.234419893200|
| RA37_K39_COARSE_G4 |83/242/161|(3,1,2)|2.884814642373|−0.234351855835|
| RA37_BRANCH3_K37_G4_312 |81/234/155|(3,1,2)|6.175390191605|−0.700812004675|
| RA37_K16_H3_CONTROL |31/86/57|(3,13,14)|3.131786995876|−0.024164205857|

В первых девяти строках P-бары отсутствуют точно. Числа положительных Q-баров соответственно6,2,2,2,2,4,2,2,2. У последнего контроля12 P-баров и2 Q-бара. Ни малые положительные бары, ни нерекордные тела не отброшены.

Нумерация вершин сохраняет порядок входных точек после удаления неэкстремальных; `source_ids` возвращает исходные индексы. Грани отсортированы по примитивным ориентированным опорным плоскостям. Q-индексы — номера физических граней, не физических вершин.

### Компактный вход: RA37_K16_G4_312

Половина H состоит из следующих15 троек, делённых на10000, и затем T:

`[[4725,-12395,5036],[6035,-12279,4065],[7365,-11913,2898],[8593,-11317,1473],[9612,-10469,-162],[10351,-9338,-1884],[10790,-7904,-3529],[10956,-6166,-4921],[10897,-4146,-5911],[10648,-1894,-6391],[10196,520,-6311],[9464,3001,-5681],[8312,5424,-4581],[6584,7626,-3166],[4162,9413,-1662]]`.

Точная T равна

`(1029667/10025000, 12265947594454241918844975623387013050918943366026636052103/11599371720644870478518106382292673185905069178661721312500, -561412832806259746688158616716191699674851/17346327513553081001259755496425094202250000)`.

Положить B0=(1866,−12513,3346)/10000, B1=(3221,−12513,2074)/10000. Полный упорядоченный вход — `H, R(H), A, B0, B1, R(B1), R(B0)`. Это все37 точек.

E=104 оставляет145 рёбер до249. S=[0,34,68], U=[32], H=[[33,35],[34,36]]. BASE — грань34. Терминальные связи15→32 и31→32 являются истинными рёбрами с положительными собственно-центральными знаками. Все36 предписанных стрелок здесь истинно-рёберны.

`r/R∈[265405169837,265405169838)/10^12`; минимальный выбранный положительный истинно-рёберный косинус лежит в `[1422183295,1422183296)/10^12`. Общий знаменатель центрированных координат имеет435бит.

Малый Q-бар:34→0, компонент[34], разрез[[29,34],[32,34],[34,36],[34,39]], относительная глубина≈0.012103565545.

Большой Q-бар:68→0, относительная глубина≈0.783211433940. Полный компонент:

`[15,16,17,19,20,21,27,29,30,43,44,45,46,50,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68]`.

Полный разрез:

`[[1,65],[2,64],[3,63],[3,67],[4,66],[5,65],[6,43],[7,21],[8,17],[10,55],[11,19],[13,58],[14,20],[15,28],[16,36],[18,45],[23,50],[24,27],[25,62],[26,46],[28,30],[29,33],[29,34],[35,59],[37,56],[41,44],[42,44],[47,61],[48,54],[49,57],[51,60]]`.

Достигающий путь:

`[68,55,50,46,30,15,27,20,16,19,21,17,29,34,39,51,47,49,52,48,41,53,38,22,18,13,0]`.

BASE не является полярным старейшим корнем. Поэтому уничтожение только маленького бара с меткой BASE не соответствует требуемому единственному устойчивому положению.

### Арифметический вход: RA37_K39_COARSE_G4

Он получен из K40_G4 удалением нетерминальной C2-пары с половинным индексом1 и округлением T на сетку10^−4 с точным ties-to-even. Это отдельное тело, не точная поверхностная точка MORSE6 под новым именем.

`Vol=2884814642373/1000000000000`,

`M_y=−27042466607188669/40000000000000000`,

`c_y=−27042466607188669/115392585694920000`.

S=[35,80,125], U=[78], H=[[0,54],[15,39]]. Для обоих истинных терминальных рёбер38→78 и77→78 точный знак равен

`1050325977622620253/230785171389840000000 > 0`.

Общий центрированный знаменатель имеет57бит, максимальная битовая длина отдельного числителя/знаменателя58. `r/R∈[472765157935,472765157936)/10^12`; минимальный выбранный истинно-рёберный косинус в `[2024253199,2024253200)/10^12`. Остаточные Q-пакеты:80→35,37/32,глубина≈0.177014647197;125→35,62/64,глубина≈0.553665531393. Все82 предписанные стрелки — положительные истинные рёбра. Это арифметически простой контроль, но остаётся только7 рёбер бюджета.

### Ветвящийся вход и вариант с большим физическим запасом

`RA37_BRANCH3_K37_G4_312` сохраняет три трека на каждой половине и общий точный терминальный узел. S=[8,77,146], U=[74], H=[[0,61],[24,37]]. BASE — шестиугольная грань77. Все80 предписанных стрелок положительны и истинно-рёберны; терминальные рёбра36→74,73→74 положительны. Его Q-пакеты имеют размеры17/6 и25/27. Первый шестирёберный разрез целиком равен `[[24,34],[27,59],[49,74],[80,105],[95,127],[120,130]]`. Это другой полезный интерфейс, несмотря на максимальную относительную глубину≈0.725775944860 и лишь15 свободных рёбер.

`RA37_K40_G6_514` сохранён как вариант с большим физическим запасом: минимальный выбранный истинно-рёберный косинус≥0.008499912188; все84 предписанные стрелки положительны и истинно-рёберны. Но у него четыре положительных Q-бара, включая основной79/81, и E=248. У K40_G4 основной Q-бар меньше по глубине≈0.553577478063, но его63/65 интерфейс всё ещё велик. Два предписанных положительных хорда K40_G4 не являются истинными рёбрами; отдельно построенный полный положительный лес истинных рёбер и точный аудит подтверждают U1. Эти различия сохранены.

## Новый точный контроль всей высотной полупрямой

### Формула массы через все события оболочки

Зафиксируем W=conv(всех точек, кроме A), нижнюю грань Y=b и `h_min=max_W Y`. Рассмотрим `K(h)=conv(W,(0,h,0))` для всех действительных h>h_min.

Для каждой грани W с n_y>0 положим τ=β/n_y, где n·x=β. В силу C2 точка(0,h_min,0) принадлежит W, поэтому τ≥h_min. Разобьём такую грань на ориентированные треугольники a,b,c. Для каждого положим

`A_j=((b−a)×(c−a))_y/6>0`, `σ_j=a_y+b_y+c_y`.

Точные объём и момент:

`V(h)=V_W+Σ A_j(h−τ_j)_+`,

`M_y(h)=M_W+Σ A_j(h−τ_j)_+(h+σ_j)/4`,

где `(z)_+=max(z,0)`. Это разбиение добавленной области на пирамиды над видимыми гранями W. При пересечении порога τ_j соответствующее слагаемое включается автоматически. Старый максимальный комплекс K(h) не продолжается сквозь событие как неизменный.

Для каждого корпуса выполнена конечная точная проверка

`(τ_j+σ_j)/4 > c_W=M_W/V_W`

для всех треугольников. Значит, центр каждого добавленного тетраэдра выше c_W, и фактический `c(h)≥c_W≥c_L` на всей полупрямой. c_L — доказанная рациональная нижняя граница, не замена центра.

### Сохраняющийся устойчивый противосвидетель

Найдена наклонная грань W с n_y<0, сохраняющаяся максимальной при всех h>h_min. Для неё при c=c_L+s:

`G(c)=(c−b)^2(n·n)−(β−n_y c)^2=C0+C1 s+C2 s²`,

и C0,C1,C2>0 точно. Поэтому при каждом фактическом центре расстояние до этой грани строго меньше расстояния до BASE. BASE остаётся строгой S, но его полярная вершина не максимальна по норме.

Полярная вершина максимальной нормы всегда строго неустойчива. Она не BASE; C2 даёт отличного от неё партнёра. Единственная другая горизонтальная опорная плоскость содержит одну верхнюю вершину, а не грань. Следовательно, кроме BASE имеются как минимум две строгие S. Получаем **S≥3**, включая высоты геометрических слияний и без предположения об отсутствии примитивных нулей.

Сертификаты охватывают девять различных корпусов: K12,K16,K20,K24,K28,K40_G6,K40_G4,K39_COARSE,BRANCH3. H3 повторяет корпус K16; десять отчётов не объявляются десятью независимыми семействами. Точные c_L соответственно `−13/50,−21/50,−7/20,−19/20,−4/25,−3/100,−6/25,−6/25,−71/100`. Полные списки всех порогов и коэффициентов восстанавливаются кодом.

### Явный сертификат K39_COARSE

Для W:

`V_W=2883356330089/1000000000000`,

`M_W=−16245316266201343/24000000000000000`,

`c_W=−16245316266201343/69200551922136000 > −6/25=c_L`,

`h_min=423/400`, `b=−10717/10000`.

Минимум по всем80 треугольным слагаемым:

`min_j(τ_j+σ_j)/4=24950880589/118126550000 > c_W`.

Сохраняющаяся грань использует исходные индексы `[6,64,63]` и плоскость

`n=(−14869029,−4571938,5824081)`, `β=144455112499/10000`.

Для s=c+6/25:

`C0=1267852700294166461893/100000000`,

`C1=42111864753776488/125`,

`C2=255007942897402`.

Все три коэффициента положительны. Для компактного K16 сохраняющийся носитель использует исходные вершины `[0,24,23]`, n=(−6399010,−15517405,32043131), β=323472120441/10000 и c_L=−21/50; коэффициенты `[23706737684655183247653/100000000,6869425275774167913/5000,1067709573263261]` также строго положительны.

**Область запрета:** фиксирован W и евклидова метрика; высота произвольна в указанной полупрямой. Изменение нижних носителей, самой BASE, неосевое перемещение вершины, изменение метрики, добавление/удаление другого материала и общие C2-тела не исключены. Это завершённое препятствие110, но не полный высотный атлас всех S/U/H.

## Реальное событие геометрии: h=3

У `RA37_K16_H3_CONTROL` A поднята до3. После нового полного построения оболочки остаётся31 экстремальная вершина из37 входных точек. Исчезают исходные13,14,15,29,30,31, включая точную терминальную пару15,31. Комплекс становится31/86/57, класс(3,13,14), weak000.

`Vol=782946748969/250000000000`,

`c_y=−2270314370094973/93953609876280000`.

S=[1,28,55]; U=[0,1,2,3,4,5,13,14,15,16,17,18,26];

`H=[[0,1],[1,2],[2,3],[3,4],[4,5],[11,26],[13,14],[14,15],[15,16],[16,17],[17,18],[24,26],[27,29],[28,30]]`.

Хорды из прежних терминальных точек к новой вершине всё ещё имеют положительные знаки, но не являются рёбрами: точки поглощены оболочкой. Это непосредственно проверенный контроль того, почему терминальный знак нельзя продолжать как сертификат U1 через изменение комплекса.

## Полнота сохраняемых данных и статус исполнения

Капсула содержит шесть полных файлов: все целочисленные половинные массивы, основания, коэффициенты MORSE6, отражения, удаления, правила округления, высоты, предписанные леса и восемь параметрических checkpoint-ов. `replay_ra37.py` создаёт10 полных `*_audit.json`,10 полных `*_height_ray.json` и `SUMMARY.json`.

Каждый аудит содержит точные Vol,M,c; все экстремальные и центрированные вершины; максимальные плоскости/циклы; истинные рёбра/владельцев; полный строгий и дополнительный слабый S/U/H; примитивные нули; полярные вершины при том же c; положительный истинно-рёберный лес; каждый предписанный знак и фактический статус терминальных рёбер. Оба P/Q-ландшафта содержат все радиусы, все истинно-рёберные уровни CHORD-MIN и все положительные бары с полными компонентами, разрезами и достигающими путями. Ни12 P-баров H3, ни малые Q-бары K12/K40_G6 не сокращены до выбранной сводки.

Выполнены точное построение/сертификация и отдельное холодное восстановление шестиблочного словаря с повторным полным перебором опорных троек. Холодный прогон с `PYTHONHASHSEED=937` совпал со всеми21 ожидаемыми размерами и SHA-256. Это повторяемость одного алгоритма, не независимая вторая механика. Отдельно повторён параметрический генератор восьми замораживаний. Случайная оптимизационная история не заявляется как холодно воспроизведённая; её неудачи не используются как исключение.

Наблюдавшаяся среда: CPython3.13.5. Точное восстановление использует только стандартную библиотеку. Необязательный параметрический повтор использует NumPy2.3.5 и один BLAS-поток; он не нужен для получения или аудита рациональных тел.

## Полезнейшее продолжение

Предпочтительный геометрический вход — `RA37_K16_G4_312`, когда нужны145 рёбер свободы. Ветвящийся `RA37_BRANCH3_K37_G4_312` сохраняет другой терминальный стык и шестирёберный Q-разрез. K39_COARSE — дешёвый точный арифметический стенд, но почти исчерпывает бюджет.

Теперь требуется **менять оставшийся корпус и нижние носители вместе с фактической массой**, а не продолжать поднимать одну вершину. Для K16 противосвидетель `[0,24,23]` и полный29/31 Q-разрез дают конкретные носители. Изменение этой одной грани лишь разрушает данный сертификат, не доказывает отмену всего устойчивого пакета. BASE должна стать единственной устойчивой гранью; её исчезновение из списка младших баров недостаточно. Точная терминальная пара и полный собственно-центральный положительный физический лес дают сохранённый ресурс для совместного изменения геометрии.

## Восстановление и наблюдавшиеся квитанции

Сохранить следующий полный блок как `RECOVER_RA37.py`, UTF-8/LF, с заключительным переводом строки. Команды:

```text
python -B -S RECOVER_RA37.py RA37
python -B -S RA37/replay_ra37.py
OPENBLAS_NUM_THREADS=1 python -B RA37/nominate_ra37.py
```

Последняя команда необязательна. Наблюдались:

```text
RA37_SOURCE_ONLY_CAPSULE_RECOVERED 6
RA37_TETRA_AND_CUBE_EXACT_CONTROLS_PASS
RA37_WEAK_PRISM_446_ADDITIONAL_WEAK123_PASS
RA37_ALL_EXPECTED_BYTE_COUNTS_AND_SHA256_PASS 21
RA37_REVERSED_TERMINAL_FINITE_CONTROLS_AND_HEIGHT_RAYS_COMPLETE 10 21
RA37_NUMERICAL_PARAMETER_REPLAY_MATCHES_EIGHT_LITERAL_FREEZES_PASS
```

Для каждого тела также наблюдались `RA37_EXACT_BODY_PASS` с его V/E/F и классом и `RA37_ALL_HEIGHT_ACTUAL_MASS_S_GE_3_PASS`. Числа треугольных слагаемых высотного сертификата: K12=28,K16=42,K20=42,K24=48,K28=60,K40_G6=84,K40_G4=80,K39=80,BRANCH3=92; H3 использует те же42 слагаемых K16.

Словарь исходников:37100байт, SHA-256 `e5a87a0a414de552dc4f443b528114a10c92d0f31e4c17807d54b404829a3319`. XZ:13636байт, SHA-256 `c050e20ed4dcef4ffa0e3c53cfeb7eb72e0e24562e80ac70b1d5d28f5eb63756`. Декодер:19742байта, SHA-256 `e97c01cdd644bdb2d54596018d5de9505654398cb051fc606974d1810d68296d`.

| Файл | Байты | SHA-256 |
|---|---:|---|
|exact_ra37.py|10217|f7aeacc6368a010d30c914f9462beb563f3f8cab0fcb0982d3e557c76b8e542a|
|morse6_skew.py|2552|dde3d7cb908c28b1f4acb1e8a6a803c67e053aa0ed4c0be98974a2be8b93a40a|
|RA37_DEFINITIONS.json|5897|d11a96ac1c129b5329f4ef194ccc3e9057d066cbdb3b1ffd239b1ed5223c47d2|
|replay_ra37.py|9536|15d630684b3498f65fe8cec832a172cdcc47fd325324dd0c0297dbac70222260|
|nominate_ra37.py|5236|1047cc666d0290b6be2f5c7a18f3e4da24296848acb1ca2e7699d41beeed5b3a|
|EXPECTED.json|2617|617c5bb0a9093dc95c0307f3e1a9f0a39900b6d4c7ec12af5bfbb0539b9fb406|

Полные21 квитанции содержатся в восстанавливаемом `EXPECTED.json`. Основные наблюдавшиеся отчёты: K16 audit252033байта/SHA `d7a7ca6ebb7dd57d98c40701282c4c29b652b3e12099cf4d941a60c69e4330dd`; K39 audit132447байт/SHA `d58b66e1e0e2ffc3d9946ea62ad7526a0c1311a793cdcb74e98e6aa2e7ed7ef6`; BRANCH3 audit554935байт/SHA `140530236416913bd5a75f00173d13766ca094c0cca93e6c386c6dd4c60b4b51`; SUMMARY80937байт/SHA `1ebb996cdd6458217c9911f05cf2dad5aa078a437f8d9b55063d6b909cc27491`.

Дополнительная готовая копия исходников, всех отчётов и журналов исполнения: RA37_COMPLETE.zip. Она не является зависимостью следующего автономного блока.

## Полный автономный декодер исходников и точных входов

```python
"""Recover all six RA37 source/data units. CPython >=3.10 standard library.
Run: python -B -S RECOVER_RA37.py OUT
Then: python -B -S OUT/replay_ra37.py
"""
from pathlib import Path
import base64,hashlib,json,lzma,sys
DATA=(
 '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'
 'bgIhvQABnWrsoQIA+RUKx7HEZ/sCAAAAAARZWg=='
)
def main():
 raw=lzma.decompress(base64.b64decode(DATA,validate=True))
 assert len(raw)==37100
 assert hashlib.sha256(raw).hexdigest()=='e5a87a0a414de552dc4f443b528114a10c92d0f31e4c17807d54b404829a3319'
 files=json.loads(raw);out=Path(sys.argv[1] if len(sys.argv)>1 else 'RA37')
 out.mkdir(parents=True,exist_ok=True)
 for name,text in sorted(files.items()):
  assert Path(name).name==name
  b=text.encode();(out/name).write_bytes(b)
  print(name,len(b),hashlib.sha256(b).hexdigest())
 print('RA37_SOURCE_ONLY_CAPSULE_RECOVERED',len(files))
if __name__=='__main__':main()
```
