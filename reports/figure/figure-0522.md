# figure-0522

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Внутреннее V-укрупнение канонического C622: десять точных тел и ограничения сохраняемой геометрии

## Итог

**Собственное однородное strict110-тело с E≤249 не найдено.** Получены и полностью сохранены **десять новых точных рациональных внутренних тел**, все с E≤249, additionalweak000 и тремя нулевыми счётчиками вырождения аудитора. Для каждого заново вычислены максимальные грани, истинные рёбра, объём, первый момент, собственный объёмный центр, строгая и дополнительная слабая механика, включая смешанные условия на рёбрах, и обе полные радиальные структуры P/Q. Во всех двадцати структурах вместе имеется **360 строго положительных баров**; ни один не отброшен по численному порогу.

Завершён чистый запуск с восстановлением исходного канонического тела и всех десяти потомков: **50 проверенных побайтовых совпадений raw/A/B/MASS/RADIAL**, затем полный пересчёт всех 360 интерфейсов. Наблюдались завершающие маркеры:

```text
INNER_C622_TEN_BODIES_FIFTY_PHYSICS_RECEIPTS_PASS 10 50
INNER_TEN_BODIES_ALL_POSITIVE_INTERFACES_EXACT_BRACKETS_PASS 360
INNER_ALL_360_INTERFACES_AND_MECHANISM_RECEIPTS_PASS
```

Главный механизм оказался не просто потерей старых коротких рёбер. **Неизменённая устойчивая пластина и близкий к исходному центр масс сами вынуждают множество новых U**, причём это доказано для произвольной внутренней геометрии в явно заданной области центроидов. Одновременно доказано, что сохранение канонической вершины A=(0,0,1) делает её строгой U для любого внутреннего выпуклого тела и любого его внутреннего центра. Поэтому физическая смена корня внутри исходного тела требует действительно удалить A, а не только сменить дерево свидетелей.

Все новые точные определения, производящие программы, исходный канонический генератор, два полных аудитора, третий массовый контроль, полные структуры и рецепты воспроизведения входят в **самодостаточную 29-файловую капсулу ниже**. Ей не нужны старые sandbox-файлы, ранее не приложенные материалы или повторный численный поиск.

## 1. Прочитанные источники и идентичность родителя

Полностью прочитаны новое research-journal.md, его память ветви и буквальный неизменяемый результат родителя, обе части восстановления [internal-source-reference] / [internal-source-reference] и все шестнадцать восстановленных исходных единиц. Эта работа относится к новой внутренней ветви [internal-source-reference], а не к продолжению RESERVE31.

Авторитетный родитель:

```text
figure-0373
SHA-256 8a9f5de8374e75eb2e09766c3546f750afd74102ae1fc3bddef86c4da45dc68d
VQ20_C622_ROUTE88_118_G12
V176 / E311 / F137 / C622
own strict110 / additionalweak000
```

Есть ограниченное расхождение метаданных: один новый абзац общей памяти связывает тот же ID с SHA fbf2665c837f63248614a08d388110749d793ecef0b2e332cd3a18a5d7f9e5faa. Это не совпадает с заданием, буквальным заголовком родителя и двумя точными частями восстановления. Использован указанный выше буквальный родитель; происхождение другого SHA не угадывалось. Геометрического расхождения не обнаружено: следующие внутренние идентичности точно воспроизведены.

```text
GENERATOR.json: 11841 bytes
3cbd90d799189108f26b941800c8fa79a6f1c5abb17b2db614f0e54f57fffee7

raw.json: 15437 bytes
ac01d1625274b64f336a715e1f5462f40686f647f0b7d1a4d90a5ee21765adb5

A.json = B.json: 311825 bytes each
142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0
```

Историческое предупреждение буквального родителя о невключённой 76-файловой капсуле не является недостающей зависимостью этой работы: приложенное позднейшее scoped16-восстановление замыкает канонический генератор и необходимые аудиторы. Его исходный точный replay также был выполнен до новых опытов.

## 2. Какие именно двадцать вершин сохраняются

В исходной лексикографической нумерации канонического отчёта максимальная устойчивая грань input3 имеет цикл:

```text
[62,100,154,156,159,162,164,167,169,171,
 166,165,152,151,150,128,123,119,92,64]
```

Её точная исходная опорная плоскость n·x=h задаётся целыми числами:

```text
n = (338323724862940134101156250000000,
     3196203549675762044509500000000000,
     931749019282765151505218750000000)
h = 1056438414677423594768348559795247
```

Каноническая U — вершина94, A=(0,0,1), степени44. Нумерация поддержки3 и физической вершины94 относится только к исходному родителю; новые отчёты имеют собственную явную нумерацию. Цикл исходной двадцатиугольной грани согласуется с буквальным родительским результатом.

Если выбрать подмножество старых вершин, сохранив эти двадцать, их выпуклая оболочка в указанной плоскости остаётся той же максимальной гранью: все остальные точки находятся в исходном полупространстве, а каждая из двадцати остаётся экстремальной. **Устойчивость относительно нового собственного центра из этого не следует** и проверяется отдельно.

Для максимального комплекса

```text
D_F = Σ_f (|f|−3),
E = 3V−6−D_F.
```

Сохранённый максимальный20-угольник даёт D_F≥17 и E≤3V−23; при V≤90 получаем E≤247. Это достаточный бюджет, не механическая теорема и не необходимость V≤90. Во всех принятых телах ниже E вычислено по истинным рёбрам; диагонали интегрирования не подсчитывались.

## 3. Десять точных внутренних тел

Глубина здесь означает **1−death/birth для квадратов радиусов**. Десятичные числа в таблице служат отображением; точные рациональные уровни и интервалы ширины10⁻¹² воспроизводятся программой METRICS.py. Все строки имеют additionalweak000 и primitivezero000 в терминологии сохранённых аудиторов.

| Точное имя | V/E/F; C | strict S/U/H | Число P/Q баров | Максимальная глубина P / Q | Максимальная пластина | Биты общего центрированного знаменателя |
|---|---|---|---|---|---|---:|
| INNER_FAR90 | 90/217/129;434 | 38/55/91 | 54/37 | .006114590256 / .008180865165 | исходный20-угольник | 27071 |
| INNER_COVER85 | 85/185/102;370 | 13/20/31 | 19/12 | .191879137728 / .404321756077 | исходный20-угольник | 31940 |
| INNER_ROUTES54 | 54/112/60;224 | 2/12/12 | 11/1 | .319012452207 / .981857988652 | исходный20-угольник | 19696 |
| INNER_ROUTES53_ROOT_TURNOVER | 53/109/58;218 | 2/5/5 | 4/1 | .345124513831 / .984101922901 | исходный20-угольник | 19695 |
| INNER_PLATE_PYRAMID21 | 21/40/21;80 | 2/3/3 | 2/1 | .596932521534 / .999990307700 | исходный20-угольник | 6805 |
| INNER_PLATE_CONSOL_G4 | 85/229/146;458 | 19/11/28 | 10/18 | .172489353721 / .079422085027 | **23-угольник** | 15575 |
| INNER_PLATE_CONSOL_G6 | 85/229/146;458 | 20/8/26 | 7/19 | .172480683332 / .079367414197 | **23-угольник** | 16332 |
| INNER_PLATE_CONSOL_G6_STRICT | 86/235/151;470 | 20/9/27 | 8/19 | .172480639713 / .079367377872 | перемещённый20-угольник | 16364 |
| INNER_PLATE_FLAT_G6 | 89/243/156;486 | 67/53/118 | 52/66 | .003288448878 / .001335991305 | перемещённый20-угольник | 17808 |
| INNER_PLATE_QUOTA_G6_STRICT | 86/235/151;470 | 14/7/19 | 6/13 | .227744677970 / .079751128813 | перемещённый20-угольник | 16153 |

Каждая указанная максимальная пластина действительно является строгой S при собственном центре соответствующего тела.

INNER_FAR90 сохраняет более99.6% исходного объёма, но имеет93 строгих S+U вместо двух. Следовательно, хорошее покрытие поверхности и малая потеря объёма не сохраняют механику. INNER_PLATE_FLAT_G6 уменьшает обе максимальные глубины относительно FAR90, но увеличивает число S+U до120. Это конечный пример сглаживания множества баров без их отмены.

INNER_PLATE_QUOTA_G6_STRICT уменьшает число S+U относительно FAR90 с93 до21, однако оставшиеся главные P/Q-ямы значительно глубже. Это полезная консолидация, **не доказательство исчезновения конкретных72 исходных линий рождения и не близость к110**.

INNER_ROUTES53_ROOT_TURNOVER — отдельная геометрически полезная альтернатива. Она получается удалением только старой A из ROUTES54. Старые двадцать вершин грани остаются неизменными, E=109 оставляет140 рёбер запаса, а глобальный физический elder имеет исходный индекс100 и является одной из пяти U. Это настоящая смена физической вершины-корня, а не перенумерация старой A.

### Действительная однородная масса

Все приведённые ниже значения относятся к **исходной мировой системе координат канонического родителя**, до окончательного переноса на собственный центр:

| Тело | Объём, приблизительно | Собственный центроид, приблизительно |
|---|---:|---|
| FAR90 | .48735585793823044 | (−.013245980458174341,.005886063678235456,−.009161563196120513) |
| COVER85 | .35863115941787027 | (.04412989560766899,.03577894502597321,−.017537259513951103) |
| ROUTES54 | .03716496853344448 | (.07159576647851017,.2718843530180934,.06241149761089624) |
| ROUTES53_ROOT_TURNOVER | .02912984152526427 | (.08297446737077713,.29874202989772214,−.0268268637236628) |
| PLATE_PYRAMID21 | .0007429883760175832 | (.23966867908868833,.2871115833457584,.05914018761632267) |
| PLATE_CONSOL_G4 | .4541103111285427 | (−.021608543922332416,.0019499423152794329,.004148722405052847) |
| PLATE_CONSOL_G6 | .4541186524408326 | (−.021610431463382505,.0019502660259380399,.004152616701971485) |
| PLATE_CONSOL_G6_STRICT | .4541186201401741 | (−.02161045506241508,.0019502514315877905,.004152629206704921) |
| PLATE_FLAT_G6 | .48204109209665547 | (−.013895504070806261,.007106067530355499,−.006937621764870328) |
| PLATE_QUOTA_G6_STRICT | .4483212509284774 | (−.024501623281520984,.00027447427626110067,.006714026894266132) |

Эти десятичные отображения **не определяют** тела. Полные сокращённые рациональные V, M и g находятся в восстанавливаемом GEOMETRY.json каждого тела; исходные данные и точный алгоритм входят в капсулу. Для ориентированных граничных треугольников (a,b,c) и проверенной внутренней точки интегрирования r используются

```text
D = det(a−r,b−r,c−r),
V = ΣD/6,
M = ΣD(r+a+b+c)/24,
g = M/V.
```

Вспомогательное начало r получается округлением среднего входных точек на10⁻⁶ и никогда не подставляется вместо механического центра. A и B независимо реинтегрируют действительную заполненную массу. После переноса на g третий целочисленный тетраэдральный расчёт проверяет строго положительные объёмы и точно нулевые первые моменты.

## 4. Точные ограничения внутренней геометрии

### 4.1 Сохранённая каноническая A не может перестать быть U

**Теорема.** Для любого полного трёхмерного выпуклого K⊆P, содержащего A=(0,0,1), и любого g∈int K вершина A является строгой U относительно g. В частности, это верно для собственного однородного центроида K. Ограничений на число добавляемых внутренних точек, граней или изменение связности нет.

Точный сертификат проверяет15225 неравенств для всех различных пар175 неапикальных старых вершин:

```text
(v_i−A)·(v_j−A)>0.
```

Диагональные произведения являются положительными квадратами норм. Любые ненулевые направления в P−A — неотрицательные комбинации этих образующих. Поэтому для g внутри K и x∈K\{A}

```text
(A−g)·(x−A)<0.
```

Это полная геометрическая, а не локальная массовая преграда смене A. **Она не исключает110**, не касается внутренних тел без A и не переносится на материал вне P.

Наблюдавшийся маркер:

`ACUTE_APEX_ALL_INNER_BODIES_PASS 15225`.

### 4.2 Неизменённая пластина при близком центре вынуждает U≥17

Положим

```text
b = (−13245980,5886064,−9161563)/10^9,
delta = 1/10^6.
```

**Теорема.** Любое полное трёхмерное выпуклое K⊆P, содержащее A и все двадцать исходных вершин пластины, собственный объёмный центроид которого принадлежит закрытому кубу b+[−delta,delta]^3, имеет как минимум17 строгих U.

Шестнадцать вынужденных вершин пластины имеют исходные индексы:

```text
[154,156,159,162,164,167,169,171,
 166,165,152,151,150,128,123,119]
```

Для каждой i из этого списка и каждой другой исходной вершины j точно проверено

```text
(v_i−b)·(v_j−v_i)+delta*||v_j−v_i||_1 < 0.
```

Это верхняя граница соответствующей производной радиуса для **всего** закрытого куба центров. Линейность по цели и выпуклость продолжают знак на любые новые внутренние точки, так что изменённая внутренняя связность не обходит сертификат. Семнадцатая U — A по предыдущей теореме. Точно проверено, что собственный центроид FAR90 лежит строго внутри этого куба.

Область вывода существенна: это **не** исключение всех внутренних тел с исходной пластиной. Значительное изменение массы и выход центроида из куба, изменение самой пластины или удаление A не закрыты.

Наблюдавшийся маркер:

`INNER_RETAINED_PLATE_COM_CUBE_MANY_U_PASS 17`.

### 4.3 Принудительный54-точечный каркас и важная оговорка о внешнем центре

При фиксированном исходном каноническом центроиде c0 вычислены все точные положительные цели каждого старого v_i:

`(v_i−c0)·(v_j−v_i)>0`.

Начав с исходной пластины и A, последовательно добавляем единственную положительную старую цель выбранной вершины, когда такая цель единственна. Получены33 принудительных добавления и замыкание:

```text
[62,64,74,75,80,82,84,86,90,92,93,94,96,99,100,103,106,
110,113,116,119,123,128,133,145,146,147,149,150,151,152,
153,154,155,156,157,158,159,160,161,162,163,164,165,166,
167,168,169,170,171,172,173,174,175]
```

Любое подмножество старых вершин с полной старой пластиной и A, допускающее единственную U без дополнительной слабой U при этом **фиксированном** центре, должно содержать это замыкание. Сам54-точечный каркас имеет53 положительных **истинных рёберных** выхода к A и нулевую положительную P-структуру графа относительно c0.

**Но c0 находится вне conv(эти54точки).** Это обнаружено точным опорным неравенством и включено в сертификат. Поэтому достижение54 относится к системе положительных выходов, а не к допустимому интерьерному механическому110 или даже интерьерномуU1-телу. Его внешний графовый barcode не называется радиальной структурой границы относительно внутреннего центра. При собственном центре ROUTES54 имеет2/12/12.

Для сравнения, **COVER85 действительно строго содержит c0 внутри**, имеет при нём физическуюU1/P0, но при собственном однородном центре — U20/P19. Это полноценный внутренний reference-versus-own контроль на одной и той же изменённой геометрии.

Оба завершённых маркера сохранены:

```text
INNER_SHARP_REFERENCE_SKELETON54_EXTERNAL_CENTRE_PASS
INNER_INTERIOR_REFERENCE_U1_OWN_U20_MASS_TURNOVER_PASS
```

## 5. Конечная изменённая семья: пластина, внутренний материал и новая связность

Численные номинации переводились в точные тела следующим образом. Каждый binary64-компонент восстанавливается из своего HEX-представления как точная Fraction и независимо округляется ties-to-even на10⁻⁴ либо10⁻⁶. Округлённая свободная точка y переводится внутрь **всех точных канонических полупространств**:

```text
p = y / max(1,max_j(n_j·y/h_j)).
```

A фиксируется там, где она сохранена. Это конечное изменение заполненного материала, не изменение выбранного механического центра.

Для освобождения пластины её плоскость остаётся исходной. Внутренняя опорная точка f выбирается с x,z, полученными ties-to-even округлением среднего исходных двадцати координат на10⁻⁶; y решается точно из n3·f=h3. Положим

```text
b1=(1,−n_x/n_y,0), b2=(0,−n_z/n_y,1),
d_i=s(v_i−f)+a*b1+b*b2,
k=max(1,max_{i,j≠3} n_j·d_i/(h_j−n_j·f)),
p_i=f+d_i/k.
```

Параметры s>0,a,b — буквальные рациональные входы капсулы. Все знаменатели и все включения проверяются точно. Таким образом, двадцать номинированных точек остаются в старой плоскости и внутри старой грани, но являются **новыми положениями**, а не сохранёнными старыми вершинами.

### Реальное событие23→20, а не предположение о максимальной грани

У CONSOL_G4/G6 максимальная пластина оказалась23-угольником. Перемещённый слот92 не экстремален; свободные слоты113,146,157,173 входят в опорную плоскость. Её полный цикл в исходных именах слотов:

```text
[62,100,154,156,159,162,164,167,169,171,
173,166,165,157,152,151,150,146,128,123,119,113,64]
```

Эти два точных тела сохранены как самостоятельные полезные нерекорды; их не переименовывали в20-угольные.

Для STRICT-вариантов добавлено точное условие зазора для каждой свободной точки:

`n3·p ≤ (1−1/1000000)h3`.

После новой реконструкции все двадцать перемещённых точек действительно составляют **всю** максимальную20-гранную пластину, а слот92 снова экстремален. У CONSOL_G6 это меняет V/E/F с85/229/146 на86/235/151 и собственную механику с20/8/26 на20/9/27. Шесть добавленных рёбер — истинные, не ошибка триангуляции. Все массы и обе структуры пересчитаны после этого события.

## 6. Точный интерфейс сменившего корень малого тела

Для INNER_ROUTES53_ROOT_TURNOVER новая лексикографическая нумерация даёт:

```text
S=[3,30]
U=[0,4,13,20,23]
исходные слоты этих U=[62,80,100,123,145]
H=[[0,2],[0,13],[19,20],[20,21],[23,24]]
```

Исходная20-угольная пластина теперь имеет номер30 и остаётся строгой S. Всего P имеет четыре положительных бара. Его главный бар, peak4→elder13, имеет:

```text
component=[0,1,2,3,4,5,6,7,8,10,11,12,14,15,16,17,18,19,20]
boundary=[[0,13],[1,9],[4,13],[4,31],[4,33],[4,35],[4,36],[4,37],
[4,39],[4,50],[5,23],[5,25],[5,26],[5,30],[5,32],[5,35],[6,23],
[9,15],[9,16],[9,17],[9,19],[20,21],[20,23]]
attaining_path=[4,2,10,11,18,20,21,22,23,25,26,30,32,35,37,50,39,36,33,31,13]
death_edges=[[20,21]]
depth in [345124513830,345124513831)/10^12
```

Полярная структура имеет ровно один положительный бар, peak3→elder30:

```text
component=[1,2,3,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53]
boundary=[[0,2],[1,30],[2,30],[3,30],[11,38],[11,42],[12,40],[13,41],
[15,49],[16,43],[17,35],[17,39],[18,49],[26,50],[27,43],[29,51],
[30,34],[30,36],[30,37],[30,44],[30,45],[33,53],[35,48],[42,54]]
attaining_path=[3,2,30]
death_edges=[[2,30]]
depth in [984101922901,984101922902)/10^12
```

Остальные три P-бара этого тела и все остальные355 интерфейсов не теряются: полные рациональные уровни, компоненты, срезы и пути восстанавливаются из буквальных определений капсулы. В частности, для QUOTA_G6_STRICT остаются шестьP и тринадцатьQ баров; главные имеют компоненты33/32 и18/16 соответственно. Их меньший локальный счёт не заменяет задачи отмены всех девятнадцати положительных особенностей.

## 7. Что именно было исследовано численно

Численные результаты используются только для номинации. Полные исходные программы, входные поля, параметры, действительные числа итераций/вычислений и три полных HEX-конечных состояния, использованные для принятых деформаций, включены в капсулу.

Три независимых жадных отбора176→90 с сохранением исходной пластины и A использовали критерии общего числа корней, приоритетаU и вогнутой функции полных баров. Каждый выполнил9675 вычислений оболочки/массы/структур, всего29025 вызовов, **не29025 различных тел**. Все86 удалений каждой последовательности завершены. Лучшие конечные численные классы не были110.

Восемь MILP-номинаций связного покрытия использовали eps=.002,.005,.01,.02,.04,.08,.16,.3, пятисекундный предел каждого решения и mip_rel_gap=.001. Первые пять численных статусов infeasible не считаются точными геометрическими исключениями. Последние три дали85,80,75 точек; COVER85 принят после независимой точной проверки.

Четыре радиальных внутренних L-BFGS-опыта завершились после19/20,26/364,6/147,13/231 итераций/вычислений; три имели abnormal line-search termination. Это конечные отрицательные опыты, не стационарность и не отсутствие массового управления.

Четыре опыта полного persistence при фиксированной пластине выполнили по700 итераций; четыре с освобождённой пластиной — по1200. Затем два режима quota выполнили по1600 итераций,2536 и2457 вычислений. Quota сознательно допускает один крупнейший остаточный бар на одной стороне; её малый целевой функционал не является критерием110.

Шесть дополнительных аффинных согласований пластины с проекцией центроида проверили по201 масштабу. Улучшенные по числу корней образцы выходили за исходный P; их включение проверено, и **ни один не принят как внутреннее тело**. Семь опытов удаления A и два прореживания53→21 по560 вызовов каждый сохранены отдельно. Последние дали простой контроль: исходная полная пластина плюс старая вершина157, точный INNER_PLATE_PYRAMID21.

Существование этих конечных неудач не исключает все старые подмножества и тем более произвольные внутренние деформации.

## 8. Проверки, файлы и границы независимости

Каждая номинированная рациональная опорная плоскость проверяется на **всех** входных точках. АудиторA заново перечисляет допустимые пересечения троек полупространств и проверяет ограниченность; независимыйB строит пересечения пар плоскостей и обрезает их всеми полупространствами. Каждый полученный H-экстремум должен оказаться одной из предлагаемых V-точек. Эти два включения доказывают равенство номинированного V-тела и полностью восстановленного H-тела; QHull не используется как доказательство.

A/B независимо строят максимальные многоугольники, истинные рёбра, заполненную массу и полные строгие/слабые S/U/H. Их канонические отчёты совпадают побайтово. Третий массовый расчёт проверяет центрированную целочисленную тетраэдральную сумму. **Полный barcode-алгоритм один дополнительный, не два независимых barcode-аудитора.** Он обрабатывает равные уровни одновременно, сохраняет компоненты до слияния, проверяет максимум весов каждого полного среза равным death и минимум на достигающем пути равным death. Куб даёт семь положительных баров на одном общем рёберном уровне.

Отдельно проверено: среди360 положительных баров нет глубины меньше10⁻¹². Это результат точного сравнения, не порог удаления.

Выбранные наблюдавшиеся идентичности новых отчётов:

| Файл | Байты | SHA-256 |
|---|---:|---|
| INNER_FAR90/A.json = B.json | 194499 | dad8a911d0441767799149c61ec9d376a95233679350cbabc1bdd10f908b474f |
| INNER_COVER85/A.json = B.json | 202004 | 0874713be2e7db9e8528b3a06191f47453d9ebdd5f3faca5a6146dcedb9d9328 |
| INNER_ROUTES54/A.json = B.json | 120323 | 00148acbec2b247cde782fad02189ccb531d7104236a4992f8d8a0aea8fce668 |
| INNER_PLATE_CONSOL_G4/A.json = B.json | 144340 | 0f28398588a29c3b2a9ac817666e8fa3b50d143e8c0e8773904a758f82eb8af6 |
| INNER_PLATE_QUOTA_G6_STRICT/A.json = B.json | 152514 | a4847be215c28db4e3ce8e1d2b91d649c4074fdcc5434cca8eab4a0e6e04c04e |
| INNER_ROUTES53_ROOT_TURNOVER/RADIAL.json | 11213284 | 9491dae24d09cfa6d6e841d3be879f4072f16c0818b485a0246cbe53c053f35b |
| INNER_PLATE_QUOTA_G6_STRICT/RADIAL.json | 20031895 | c68334a77535ba5804f0d19f44fa93e7d65cbce2ff3b504044aa3841e173085c |
| INNER_MECHANISM_CERTIFICATE.json | 39810834 | 0452c33a5f87ed78d31d952d5d3fea8ac0cbaae3de0d93a8ddd7a8cfb037deb |
| ALL_INTERFACE_METRICS.json | 98524 | 8b833ab570942f06e511436ed779dfc3e8b93b20c563dbaac48916d629b8f18d |
| ALL_EXACT_SUMMARIES.json | 10294 | e25c41a777b2401dfb7308915bb95bd8f6b8f8200a09691eb05426507bfd0aac |

Полные50 индивидуальных физических receipts и три дополнительных receipts находятся в EXPECTED.json и EXTRA_EXPECTED.json внутри капсулы. Исправление метаданных GEOMETRY/SUMMARY после выявления23-угольной пластины не меняло raw/A/B/MASS/RADIAL геометрию и не скрывается за утверждением о совпадении всех вспомогательных файлов.

## 9. Самодостаточное восстановление

Точная среда: **CPython3.13.5, standard library, assertions enabled**, UTF-8/LF. Численные производители: **NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu**, CPUfloat64, один BLAS/OMP/Torch-поток. Побитовая переносимость траектории оптимизатора не утверждается: каждое принятое точное тело определяется буквальным рациональным входом, независимо от повторения оптимизации.

Сохранить следующий полный декодер как RECOVER_INNER_C622.py и выполнить:

```sh
python -B -S RECOVER_INNER_C622.py NEW_SOURCE
cd NEW_SOURCE
python -B -S REPLAY_INNER.py 3
python -B -S VERIFY_EXTRAS.py
```

NEW_SOURCE должен отсутствовать. Для необязательного повторения численных методов сначала:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B PREPARE_NUMERIC.py
```

Затем использовать полные команды из восстановленного README.md. START_QUOTA_MIN.json содержит все реально потреблявшиеся поля исходного большого history-bearing checkpoint: ids/free/HEX-координаты. Удалена только неиспользуемая история; её исходный SHA сохранён. Это меняет печатаемый hash файла происхождения, но не входные координаты и не алгоритмические параметры.

Капсула содержит29полныхединиц: канонический GENERATOR; четыре точных core-модуля; exact_inner, mechanism, freeze_flow; все использованные программы выбора, внутреннего движения, движения пластины, quota, аффинного контроля и удалениякорня; полные DEFINITION/EXPECTED; NUMERIC_CHECKPOINTS/NUMERIC_TERMINALS; REPLAY, METRICS, VERIFY_EXTRAS, PREPARE_NUMERIC, README и manifest.

```text
Декодер: 63800 bytes
SHA-256 07b73ce1dcf06ccbfa8485e4ce3a22b5644635bfd4f8ea5ab53b6647034e76ae

Нормализованный base64: 62140 characters
XZ: 46604 bytes
SHA-256 56cbbceacc4f4d9d5bc8c66e27939d6ada6cdfc47d47ab31716b77f531e972e8

Исходный JSON-словарь: 176424 bytes; 29 units
SHA-256 9ce25007b880e2f98903ff6edc652b0c92c6e9b9ef1048ae5dcc6648955a2a8e
```

Декодирование этой окончательной капсулы в новый каталог выполнено с проверкой всех исходных receipts. Полный точный расчёт выполнен в другом чистом каталоге с теми же точными исходными единицами; не утверждается второй полный математический прогон только из факта повторного декодирования.

```python
"""Standalone canonical C622 inner V-space recovery, ten exact nonwinners."""
from pathlib import Path
import base64,lzma,json,hashlib,sys
assert __debug__
DATA="""/Td6WFoAAATm1rRGAgAhARwAAAAQz1jM4rEntcpdAD2IhIRSSrMvei2aaw2KRhb7shx7KREQuhxzpDyOMpwLTbMZEX7PfccdKdHB
VpAogyIGFgIqDBpwDXBTQanOuR9uHq9w3bJ4FbPX4f2S1bhkBPButEpwwH3HrLi8F3Vh2LFvpsxND08qFSCC8BbdpNdMAeO83mx/
mDPdexR9JRYEX0uctddmVsv7YiceXRzNGRVT6dhJlAxaUS3LKVXMS6PdCe9qvARbzb+bPriVsq5+cuR5hw/8EEATr1pVRtfYsfEx
RO+w3t+o5bx+uWwv882NBB+YGm/Af0XzYyMeJSk3igToxMOkOOSHicq+5vdNEUFlSHN4vwNtSLtDLfzjFWreDEQxL71X/XovKcnO
cLL1utVYJA6fv6BvsqFU4YlVfj93jfiYGXR4jnDWiAttuy4htYnCJ24ndhRBi9QvCd1fMVOWtJiSA1Abk/oGfL0OiLCUwzoHluKW
SxwgAnrlsDLRFG6YypH2Rx1KnLMjAizNnNsPzdwCuR/N6sK4W6XydqMOP2Dic10YYh/4GfOnAJrF+3ZWkqtxmvcSnnj1LCdIaib7
nzSdgjI0ooWqEZEfQsqhxzfuzZ7ZxTu/snHNdN9onWAcmNCblOVcDZgTYY6zOVfa5QblYWEQFDjOCO3ZnhEGm5ee3f4KbyPubXqe
2mC+ROCthht+pOrDou3UUiF/nKUk4orQsLlJY5Qd8dGx6L66PRqb+SJWWxlUAJg6ym77AgbvKjEzPvYB9IJwRzHK64CobodXstIr
CvbmNAmGAViDt3x6TAhohseABRcHXVPvKm8ZcsSHdPGgweMFlG6novJQe3UaN8gfOGCTrM/G91H0D3nQg/FUxLF3rZo2l9qXD5NJ
RDM2frleDguBRo3/C3gG+oVoFWBl0pXUKVt9RK0PYeZjjvQWAEqbI9rftgYwb8MuqQpc6zTFHXrPCB0LZd9BvmluLTZCbihOd9Sn
bMbD9idyfqhvp5St3fOM3+uZS3N19e8cNd77pu6/otXzF1iG/2VaUQ0bJuIw53kNZsigbr4sc+0COAhu3DgZbLSC4plqHFCV2BLX
GULz7g38QTXn0MF5a3BaXHjqOskwGR0CeXoCbroooyT4npj/clDOik/dP3MI8tKKBJkLZ+uAe8ND2tf/Mi8S3g86eMlBd3UxZUC+
QoEiO4rSzUg8JaPU5yzPtf1bCT56CERbUx7MEFuHQWIcjFiLsxP8+Shce5rD4xsVBjyxquzrOSEz7pbZNgkMYr/E4KDUGZeb8ko3
D3+ijLZLEbo7yJ7/sXrqSh5H4QmTwlSZ03fFd2FnVc7LDwFKsxz5QVwpWIrzJ4UnXlhTbdnv9bnaD0rEvDaIKGhULEneRnse2syu
1HdR8DfUdcVr+x6z4DSFpaRQ28hz3oPQ65R/6Tt2MOC7fNAnNfPNY+6cqRYppQVXR2tB0ZW0HrkOUJQfMZ2ncOxD/ZelOXG6WOQe
HLVYfRID81MZGKMwGzB3L1T/OL8aunqHvgMMb+JsmMVDN5Eai1gKZF3+fTSO2kmzt/8HwlKNAdXVDiiq46mDUeyVhe+jfbrgpDzW
ECN4jQ57qfliSbBTr5IyUsIjB8jGP7lN2V8rc762C7mx3Ml/DJQL7yYUrGkPcWUe9f3lwDWetg/qFw9Yuo7frE/Evq8O7bpNxCJS
rs0wd5PcoSHDY0aYmKX2A3FZK6ybvP3r1pFwewnMwDf1fpEnnp04QBy0itfoWeerjy2x2iPTqv8mQWFNNs2JoxMCY/LKhwJD/23v
WyGdbApBP01Ixha2qRSQ7Oeo/s/oWxU49atO4uJYmv9XTZGnxtKyMAYJNKYEAHtIazRkTncKuNqW9jNuJX3y15MfqPhjPNNK1gaX
Zqb/zu9cez9doAAigpEYG8KTEEq8YhAqCBYJ1a60imuPZSc5yNymrcUKE8wpJdKXj443RB1HrbOh+Htycgdqt2xatuGJ3yGJe13Y
YBuwqzphI+YnzAVwxPhyfhkJU46ulvr4+QDXUO8ujnbL9QRHWFTNKXB4cJamKP81MBoCr82sxzFG/Q+dAPZj6CZVOYYhdBjgQ6+g
zSEKvmrDXOK8cjXu/xOnpZrQCE5aImT/ki5l9l6Ly7guhv6TcCFMni16eHa6SFFlZLH/Kj09CiVlyFnusYjFPY6IefeYq8ZtqbYn
MokybsTgiHdz/G89/MAEusQrXxyPmRjQZKy2ye0FOC0s59dgsXARcvpeG8J51nFt4jgcFLkFqfiRtYfYL1kp6qyDto9Dts0ghNPi
hQy1pDWwYswOdWFKHNtJ7UhesvJqXI90R2W/eos7UdE7DPP+oyVMj7dmsCPjzcIVrNxgR7CnisNK91Y+0aJvz+LReITdc0h5Bbr+
bjuwNL9IwMpKSUvxoDxtB/JJONQgue5DTPaRfbOpxwGLKkfht2KiTiR1RC7uARsrT96rJbAZOttHAdPM/8tWy08QGsnh2I5+rETS
6B3kumt9YZuu6vBPy8JjjBrv9pKzh73zmylaUFDHAl1LTgclZbZimD4+q1wkza8Nf9aUr6nPUAVN/WHe7ofrSdInjCrdo4deIool
u5BlpKBIPO5IEjqTKYIuFTaaa+skP16JmzEjImMF9GumLdbrK98d1Pk7n0vDJsSzo7wSUHqGhENfFUxjFynOMdp+Prlq+kr3TM3t
7k6/EmKCG9W6qsGZ+JdKQ99Q6p+5lVBKNrOwXlh5n9FOYqK9ckzWwXXjPtgKEzike8Bz2Vf4R40xjL7WTMlzZx6S87FBYePCaoIa
epL1E/JO5nRXJgxq7pmbsJSysaOpapJ7GMpc0/PHvVFSuGqgFs+bu3onbvhvwfSWjyg3JyBk7Q6e+mjKmuPLFSrrYGPIGTBbZRWe
Od5POZ+F1j3mjGuess+K037mC3IoQO1P44arHxTGiH6urhUcLruSFpdBhhtHoxZskP4OcXarrbQzSG714/tyWLGffwILgSfbZLl8
E/Qpav+5fNB5RuSmbILrX6apyL8XEE2bxLA3VS9ldPS+KY5v0SzseNajxSsdgiX924a8/65Q5Q3BTmaZvkx3MnsD5eNLuiruDrH5
W801cYbdLrmcjitQfeebZ/2KFnZ2NINR13CMYQk8A7WIFKkvwdGBZa/nQm6+J5wtFlyFD2PAeYVbc1z/hiCw/wwsz7Xppb7/lCwm
190mpa3QjZajUum2cVoFKo5lwjRTSjmpiLYlKft0RBrWocGR9663oZxiHha7VHLghEeST716LGF1K0qjrTE4JbTMN3Hl+9rSVa4D
ORV2N0GVfpVaDGmz8fGzHG0oGLSh/elyjgn+cWoALIA9AI4km21lkU7PAfCFipnb/dBXAV4ke2q2s8VHARvcAxj+RjAUOy907/Vl
RzMonx4sKk//1+MQJzKpoql2a9xfseUPU5njfXw6XiOTyIqq1sqcEIhM30a2D0f3GnfStZy7lVUPYmDt4Lc30IRzrGUTPqfVskav
QVgqJ20tXkai+4yEDx4f5CUd8f77y8urS6nuQ62mj+JB+Qm8861WUtaGyLmbOLkFye1ccY2PxknWkS6sHSE9fHZrsRiUNqvt2guT
NMvRymHLyQw4XUh1vpYWbbUlZFjj9ilXae+CLT3WxlWzPGpNluomEEB5h66tg9O6AOzPFemArpH9yK7r74hoazi8+PBTmSMpyt6E
r+B/6sKN0Me8T8t0fpcrG0HBG8QRWJUw9wk0EhYn4GVbnBE7i+VpKgrjswxYYXStNBuygfyWQICwECM4dOjNH15aKNMTVH7X2E+5
TV2bgBvWRzQbJv18y3YTYO6gPrkipS1zrP3C8WlUiMYTyhyUjePqXtpFMJwg0kcJwUSNBW3TcQBcCHVmoUbCuXSnBlNd9e2ChDKf
WTTK+3Y1AFfHgeDdGcAmDhCLCKdBuVSOQv0w3CVEKQxwmJFIejbv6j83/DrKPMmAIJbvIz++LsCZchWElEWaGj17k4ocu9VrCCnl
PO11XghN6rOXH5Psd/EC4EfU5AwJZ5oAe2jnF/pio29Pn1br+3f8u4/6MX8bukp4iwiJdx39xvjafcTJegr1w3k0+KJtW0N0Cf8Y
C1RWfzVNwbNKLx0HZB3nAk8O0QcyeqJ5dQuYJM7psyGWyZGtX2N1LjxngDSbjVthILWPpDgz5Oazkdf5LcXERixIerRaG7KW7hd8
AVwIq2hNI9P1qkketVwR3o/CEaG/yr6lbiTBGx5uHSNQ/s6hKj9xWLTUdbZ5OEyrFT/sHkdkL2rSvXItOmqeKss+y505y5zk7X6g
lnLdqY1iV60iwaMU3Y8N/6s8j5PUT3y14ATifwQPgQ7bWhWRkGZd9a1zOH35iSLyyyAFZ+FGXCVsMQVsKXsFMuliG3xBRDpXXart
2GpMn8CR/NPc4vYQUCh334XyjS85LB9NvphBS+gnIae+XJH2QLMFkTvWaYC1ALTBbPNmyQMChSYz2SDenaBrCasmxoyJhzZ8yjip
QWZAMnxmvQl0FeHAzK04QP40WCMewZ0496sm6dy2a/D1SnAWBY2T8qi/4xXF9SLWDbRPY5kxs3bNdu9kyQQb45E9zLVdPD+p5SHG
DsW6JFnkaMpx/x1b3r8DNRM2nmuveHPRIcA+aqFEReazlGwqah/XySP7Nq4mZSIUi/BI6nPBzWxF77HqAPh1veENRlFoAKP5aLbV
DHRZq921RTx7pMEh0Vfh8zgWJvW0o93X87MGlr9nshzyVGBf0MXK+TzreVA4MCt6EQS5eMP+JPs8kU7nSq+XbxE6c6OwtN5dgY9z
RqkrGbyB6tr15l5whX6eHCKsopz5Hqxa5IOFXvNoHz3XwW99XvQoAH/9KE2o+XLgjSibA9egKifxse7bcrX7M6skrwfabhNFBCMc
51b7qscpQVcZf4TXck05tRJWtzjRLMkg0+CcgZPNqQJa52fdzTyPlHOPrZyMa57rStCO9guDBA9ed70lgln4pn3AxF6slmZNZGuT
RVaHZZFmwqOpTVLWlEFDKpy81Cu/b5EYCAUlFiQLMsAB7sO5KoqPnVJO2FHHQH6RaY2Ay8KAcgYL77MXfrWuN6JA8p0R48AvU6Kz
p6KqE2lltZjPi3AuayFlxBtO99iINITurkPIAgkMknqpVK62RXDiV7v+ErV4GRlOWNF3dBVUaYvhA7fOF7dAtJVVzkyE4f6v3l9g
BvdAPRHScdeBCVCO7wt7Z2/Z9NMgx+fyWWrwoBAg/8+GgO2LfQQ006XLjTVOyr+tCrFx1/8Ta5ywcbE2ssQevqs4B9sR2een6BMh
BiesKRhrNmPePnqClnyoCwdwnTtmSVW/RZUv3yRfjhrOX4Fxfq2JwpiqMuA9PHUQtsF7nJkV3ks27Nau7YkyC81gD6S1yGoOmEQS
YALant/dKuc/6o42HUvMShMa4qYyTMYcsiZeEnwYxXWVLUtPW1RBUtBA7BimsEL1gffGdpJBmO3yl6PiXiHYCASBgECkoTrOp2U9
OEqko9L5TOn4NVMJZzTjuJWKCvRRLa3LL9Ab6U0kn8brTGagZhtKxJnBfxNnMvKqEStqnb6l3I8nneHfPjMNuKoE9mJPY8RH+4xU
b3sgm9BloFBwD0yuBuqDCEz1idYmycBlvYKhbErqKvQ8ht8JUEt88uFBeNcnuJHNs296qyK4/2JssPx8GnvzuApeCuqmXiSBqgnF
bfcPZD5piMx7hR2sxBB0Zt1ADODdP/Yioeqjdfu92dZFjc/iRzudGDoEbJgztONJ+hvtQNwpgVpjeDHQB+ZT/7EAyw4jRWM7RyVy
HInV6KIjyCHUXfIYV7B9w2wqU/SZlaT7osY8oijtjmURX7fto+YFUY8cDEmCIEjBcE1YGoTyibSzkaX4FVd00lt1S06kxFi0bYYc
YIVRGQz9eV9+9LIcqNm0jD1pGzXDLAeCr7EFvi+YNPWFch2Iy2Csx6ks1EFAv46GsdqKUyOphpmF5LW3lCDmR2YZ98pI5tPMNSQi
6GsVMJJtLGzgG6FjPjyCy4WrbcBBj5kv4cz4tRXK74m55i3AlQxPLJaJTP/sszFcOrIhxZAwym9hBKx1Go09WRaREys2iGpmVq94
By18xKYGBPkarraED7fjm/zlocsTvDyA7mSzB4JhXwgbhi9Qdt0FosCHwEQxJp6z0byGJK7xuIaLrp3XivIgLEDjhcxN3cwtN9XX
h3XjliXx+UoN8ppJiqYFqBegd1+PCsCnbnM7rp7DMcVp/5+cuhYVBvS+gc1+f4YOL/Ae0J3T+NWUQ8faKbBED6q5AhbHw4tQTaqI
ygEBry/SzYprJLQTP8rNmi3fZWqQRUpsdUl9tcrlrkxM1YaSIPnyhKbORUw9Fxbzlni+xz9PWWbvd3OqpKMbCfm7W9TRKLJEg8sA
PudahFwB921geAaXkZPXOjlVBPXuW1eRUMiqDY3YMY4QlKhByhlwvQ/J9Rn7x+p9q1IgdIdz4+k0VGb1Y6dOtZHIQ+wYaG6cvwxj
t8tOoIgWzYgOIfy142rhjSaRKK/JMMRM7gNOiPbjbMDl4M5j1l9ZYr7snL1Li+IyjlufLlviftheNegsmVZjz3J5F5XndUQC5OF4
Wrpp0kvU2V0nZ4pmj/8d0VIurwu2LKfLrfeUkLwKajj4Egy/FPYv0367dp7n1TlobJEBccTUoLEBgI8g4VyeLU6oVxElflcNeaII
fefHoiAh3Nu15unJBp/agQsq5Y9rU9z0MZxjC4mmdYxWH46DRYDPukM5lywatVv7gGoOV/BeP2kvE58meUqTc0rIFNSd4xlX1BPK
9NkPsFm3Iyq4bmIjIkoQ2g8OO2lRtJKNzUCxdDIUBJopCvemB1p7D3iqobPCI5JiIZyG75caC83dpmrVENbnxp/EZTMJ+3oyss9o
0/1h+SFHfGPUA9U5g2XNVdRMnhkGNb8X3cp7FKLEfQGHJy6pu4EF7DyZR1PmoMKyZ1A21msFBH8Mf7Q9ByyV0l94tvVbrWznHl0z
y8qS0KNkgib/vkPK8Q367iJFWrmAVKn60+Zjh1JVhDSCzb7MoygWyyCTbQTIMgECo/zPO48BMkAhtf02+Bs7CaRI6NJ14YyiDd/A
fB3d/YrplcZEaU/gozRXNWwACwjXYWLA2zguCzODLc7Bs72g+1foYWVpfFajQQMaTDZqXR0BaciYliywJTirGqUREah8bf32tJgG
QlvQJTYjkFTWE6RMI1cr+Q41kArFVwcLIAoiXWm9TnplPpdcJ2WL1SqT/lnKPMOPT0Bx9EqI7qWbY7xFVHqbFrg/is37NEm0IzeE
M/Alk7I1WrXFpkzmCwmeeD1NtUfBUg5OLXKL0nRUtcBrkFqD9OwMVRH1kbw5n7aN4CttRvoDLu6dy//i2XoXRwPiNYe+rsUqK739
28X2VO2K2qgXaAs1ZHZpMpWUwmonfqy06YQXjxKE3oRaMtAEw9cZFSjn94L8lM+Tgd74eTyEQfnuUEhpPYj19qaNH8QY3ttqNeUT
FeRz3Peo9YBzAAFzA8B1Mh7RwMEXolWQA2TzfGHk2p+QGNLDMbteDv4K9nlq/yytsE59j9BsZ1bkw9act0fDZ4mUbsrQYl1yNfX8
68Qd/Fn6b2W91+vedwTJXpMGN9DYNCtoveBeTrqwcD7aX3H3IqscvvLphA1wp25S9ObFF8fIV0mw9oJCXmQ4tJfDCld5dO57K/vL
Kwox9Rg2AHei2HbBvH+irrjbtEEqSuo5WXj9knBCxpSmwsQ0AYGsz5NmTTU/8RTypUtO8C9lm2trbbbdH6pJwn2RAN7vXZDo4ZKI
hXodDu4G2U4ALtVIGGUrlUIJ+RGbByxWm7g/odCpm7I1o76HrONzN82ngTd6jM7jOnvH2i/X8QzLhuJuthzKENWWWUbi4mIIUmoB
fdHAB9nVtNwOApJDSsfcsSoVM6va8ISQDKvhVrqfvS+O0XvAP9mee9CaK3G3heht5EEKNE/7UWeJF3NUupngJ5c0oV4IcLYq988W
/4RvIoNSzbaKybijQRkSJfRaUAYDdVOepjZoKXwa83w8iSySNxln5JlllBMQgegG3ymUsUVwWgju8CZ86KUa9OXhpXLyidwrMSvT
6dSzBm6zmrTRs7g8kQsKo7ODgalN7Iv2mnVJlqb+eTW8+iF428Mfj1oB51J0dfrXyWsxM+9jMeTX7Q4jCNhU/pIpU61t+Dz2MZe6
cdCPeyJZy27nxtggYzIUG4b6fGQ07UjJeZgZaNc+4IgaGIKrFHMQuHuDN2yH65CHPb90JbMHZHs1Oy3jmXlg/b+pJZFI7Nkp7gs0
XIsOU4Ht25m+gfcrv5TXBxeVzaECZh8x8DYMJx/xzCMew5QR0lW95+1AdlTFO8w+nA8rGlUtYizux/SvWBJJQMIHlRD8+nrEu60t
YISJDRSJYiYbfvLBW5E0J1IBpe0L9wZW0x8mTnFCA0nvs3vKjKUHCo3EzWaKFLbRqFsFk7mH7REC4cHuzbpxSXuH4++NHTEZTcFu
1K5NjD9cn9rsk3YClxCo1lKy5r1CWMnWen+ocsjj9PYp8iNYU9SvIDU4SDQcCU+Wdmk3Sa5Wvi3C9dkcJDj7A/EXAodab8+XqpxY
SNem/MwIgAFYdoR/dE4pEbX5beGx2XRZyakg+UJAcl7IwSoZVwaFtsG8b30QUG0kSbYEz3cdJeD2TeJLW8Fqa5Ad/8UN6K9GsOBj
xrEEFpXk/vDKhmbehH8wa/scuZugW65iNYXTPKQwAj0kUj0s8dSXwaucZS6WgEO0ZPngqq75isUu5EBmdvf3D7BmU2q9xRAG1j6j
kwOTGXVJ1xiJThf7heX7LXt+lY9HsKuMjop1tNi69+sBJH94Zyf2no/IBZ4OBnbQPSHhJl34SqJhGLlPc6ZrBukOcQpKBdE9pFPz
FEqSoaUnL+zlm+rbb1m1cTm1rCoAoglaryPQZt588t5vbDO0PhE9CTe8bsCwbXuF02W6kQjVe1bRyUuNvG3O6swA8D3dlXsD7djN
DK4rWxGi/SoEvsBUd3ZSL4Zp6pVc56GwXLRiPjCBFCbCU4ZMtx+qkU4khdHycBNrtdfpp01j1FN+kFXkyidfvSFBzynRtcLLpYnv
HPEeRsujipP0xcxc/Rxm85R3kMXSxxA94MTbSd05s03g8zGw1AP5gQLDFUdi2BCk2c87+l2xRTAR6OOzyoyXSyvE5yFBnotp8YcP
/thlPfTCa6ARp2TRz1CNaxnCYu/UonNuaRuQPRvzxt8m4nl4YvIAXCmpkcpjGo8wByWNVEc80FC70FnT6JK9Kp5Uz/AFvnV1asT+
fFDKz/dddFot1LyAwIjEwXj60eSWlMCrPM96UaHWF12UfICH23WDVGDDLAMAyxzEOO48vsSBwObVuebnFpoHvYbO/8GC3Sjcp+SA
Y1pWHn0xfw8JeZyRjT6czC/ky4LQ9/DJKBB90AQ0dK0cqHLhvevwUqtMqNg/pi52FVVI9WbXOuo8rAO8IvulcBscPcIB3HI6OSaM
9s1Vf0MroHkx+ddyrXjNQ0igjHs94ukK+N1SbCPOVNilp7QLx44DzyJYf0766HPv8gTEBEWPqEwKgdVEV4w9TDhSyMuTwR39pcBF
aSew4W7RXHlkuXE9hSEdpu3HMfBJSH63h1Mgpin/PW8zjoQ0MgK4EzigwZFuWyDdokExxhS03ObZHGzwqOkD23c/DqXnoBk7Y4T/
vapOA4Nboo1769W2PlhgWXZlyAgRlGwXFJToXs+DBA/bru6QuA8E/Erwz/pctBbu2d9BitU3J8cK50eFLVsjbXEMMHhPkLNXr1/r
fyTcFc0qAptLErmLlXpW7DnYk3Rm0EtDiHUDN9mCcBvAr01YHxeMunpSbPz/aIpS/NdTKx/gZd1bmYDt9/0f2hVEcAAnXsu38+vC
1aw1FwX6LJVW254cn6O4DAskc1B4UXlCdoALplO2LApCzknBRLFBCr4o+XjPLeWHU4gLmFTL2ds+URvwTyRc308PthH6z3xQbOmL
1xKvI2HWFwwNzeybC9nuF8pRWkmcmoH8jQswYlVIqqlempC09nOK2ricFJemMFR2xrZC0pVgLogVic6YSU3HhvXmN+k651i5A02R
EH20JCeiDDPVIFiY0ZGGhTdpAw+IPPq3Q+bK6GOFeCG3f4Tg7yQLL/r2uYceG8OaN1RRulKJNTBz+C4gIaIyN8MznvHjZE1yA6rU
eLru+lKkoXT6xEZsNM4VCIU8BhtsbpuHQrzYnq9mRbBeFuTbuzw9V8yEIX2nGoYpgcpw0ShmcKoN/MlpcMRnsAonDtp7CoCiOlca
+2VRGbKqInr/nS0wa7x1CteqWoTHvjTPMt+ts8D3WQ47baeIayK8Yh9KUCehh1HKKDsFZM8lSyg+8ujvD6rb4S8M4CX/s2HcXXNA
Djy61nokQC5rHuK/brXW2VJDo7XRL55NJnhsIbTmvU55SDCrDaHX0TAT4w4poBxRYygytFIPTty4ty1U73hwrkggu+8gaebHwGZY
Yeuh6FwPXlqzgFQqQuerX6z+SEdkh4l8hDunCDnUFscvrZAP4b7bPGnvI6onkkC6a4Vor2ppsHuFolC3pw7JPrYyqO8NUewYtroF
yDW7jCJQ8JyzbxTQ3mZPyV46X66ooKfwJTtlJu/IGAlQXOPuvPW98tkSBOsVE7dtYV+y5onf9JM1bAK+xSYIHVCRxUBh9LEfskld
d4bJ9MRb+4LdMfMw1sk84xEqmwByzsbW2Usx4vMHwKWZXhvVvaTvymAzr7dxp6grWmSxbzdG3/UiYfRddJGyqoCUiigcuQIWW27w
jGBKcrQpKBFRyN/0i14WJtxu6S1dgvGNJnNgdwVSW9gr4Vju0nz6rxrIQZqIRjAh4w/RGSFofv8TR874iAXdnwz1dR0NA1JQYEhq
dRkuEpDEqojLz5kXy47KRts8pYnNgPoRxyRBdooIXLyt0DWJVcuhKsFff5F9ZHHl07Pvfpo+Mnnx+ueikXoW3DIzk9GPgO5SXwN9
kwA6dsBnR54ppg9Ma+m2fKWXWO4B7f9WSf48G1zwSkSsIGg1oL7qwn6eQrp481hqbAvU3xc6sDMyAzK+Rtwo03vnAXQ3L9b9BaL1
0ulHqcVXVCA1yUf0i9RagLe+84P+oW42v57zeMj+nemLjoxYXZg3ZtgE9AvdJqctD2IWeqfmf/aSgdhuEKQ64+I3b+xCOHCk1IAE
VUvM5YkOHH90QExQH9y5/gt85eXKhAApsG39F08jCwtywAUXFFc2x8E9Kb6xI9cOn4/Cfw6nUf/FfIIYkcBUA1aHaLQ+th/5WLQc
ru9RYntVvxy9dPes3gQ4nNBKsKP7UMmKs3pIWWVyZq8MUoO9VLrgED8uPRl1TAf6sdpwTF1dRW9FXdBaKFMPkqLLFVlABQ0txyUF
R23rMsTZX3meD1dobSKPMe7fIV5YJMUwktQ0Mr1wqOO8HgTq9wK8I6+iF+em7v1cwuJk9uDTSL+N1nwpaz7D/O4XoxUAE8UfkUb8
Dav+F9FYJihSeCRsu4sX3p0llY7eDWh1cVPE+AFfzovEQjxoc/AgCJS65523oT3D7UaejqH9aIe5eQEb/IcYWTuALULHvnIytrm0
cvWdoPAY5GnMvlVutrc0Xr5UDZbMrng8KchB8C39VZunotXA28ItFFpIoVsW4zH+G9aoJzYjscxkLUXFS8xjYghWNu1NtEipa6Ai
/vSoMpbCDX80JBHzRc8KoALMXx+3fvAz6noURDXcu3+RLmRV7sA0a04BMYQP2P8bknlc5iO6GsqPr0Mj9uRoeS4iPY42hyBEglZ4
FDlFQfd3MhMC/5gouO5uaEnCXUUgX9pb7wsOdLTjevn6MeQT+z1jQmvL6p2pQv+R4n19JwOLV/Fx4xDduyKX+0GShAGqgAS45RRv
kHtp4rjiYLBNmloRR44KaQpFMe8rksxIBjk/cX2YpN3YZNPVeK4dBkoDY0QyEJ1wn8ZoPRYVxHdUnoETX1HYjcm6Ls3bjnxCi2Y8
THtiNeEPaRO8HYMzXk2dCQxBZdPc3sGcOjOwd1XE0fh4TwjcNb7EvLMCNAuYgM+jAbPBpJdFVZteTZYdYpyXAmwXCqLVHG+ramUs
2rquJpKebiuKIlkT7lmCJD0wdfK9dOy+OVN4QyPOCaWYw3+tFDnkGSiWO0YXtQ9emWqU0QXZv2Y3HGAQsy7gcPXDd3xrT1l/kvkN
Q9gtwBbHLJChbt5jgqX6m24G3G6QfKbDUf+cYImcAWus1YY4Xa/lCO4JqnI+nm2MdaL/tVN3LHOP4ZYw/VPhuplK2Dcf8Z/xpk4g
xXTJWomYWKTzQR/qcrKoBdCv+0zGKUAIrTGuhdQVihQHK0pXaiBV2B9ZaKmlKGGdsqt3cShyU4zMwgnDQ4kj/RlTBRGS8cMmgniN
2SBER2hvwp7AMzpinm1/XzkBKSOjGL9gQl8nJ0MIfTsIlIftY3T0tUF0QnYAB3hDyerYO3Id53FZnAcqPdPbkZRDuhJbh0tMyaG/
o59SjLpe3BgiZPR+7We+ZEVCzSpxKMFhjalBsIs3N6mjTCT/r0r4nKcSrcIubkPVkpbj6uHivnvUbeT5Uz1nFLDMY4SHuN8/WzFo
lwFvQjAM9YHX2LUV0wEaBX3fvqLI2Zb7xh55mSKDtfMzmD9xzsfewUx/uAT7cv3jwUeUlokgqJSFQMKt1vCJZ7JOm6ITxasbPvTu
QrkGWkgElIYZ3T76pdbi+ZDOihXY5Ag3o8PhytJx3fyFNVgqgTQLj8/WMVFyP9ZPVJUqJ5qV9uoJrXpH4eMkUrYdmd1lidAG4JeY
WetIOVkwUVEOcs3qrV9HUyuFutrAVX7ZKjzz9LJcf3OT3f8Q7bLTzLDHoLhkJFYcl787+nrxu2votIDs03GAIsw50TAOs7nAa6yt
K4rcmPdVvcNjZ1tDW1H9x8kZMwnQSQwOXdEIF9ki022HGFGpdjb66W/KJo/rpI6BQFB9DAnvHWLjbgwBdJr/bHaCGnaGjC/B8OxE
27EV5/M+o3Kl5z5jCUa//c2WG5DQZf/c1NZw6FTGMSrEMMsZkpM0brrGt97NRT7ADm5tElUaXV7zbltrD+nhZHr2rNZXoucBQ0Z/
TdWz/02odKTVwoluUH0Yh04ZvGPrbSsyzu32LE9QOY9cgYgSpl0WJzw3WBExNy0J35T3AYadJNugGidhsCtv5DFKGZ0OLbjJvpnu
qwpzzgTRt6+qeMeBijnjc+SAY0CdjobjJ8OnYq3aMD3Y3Irr27MPKP2hOecLam3pKBVNzpfplEjbgzLygmvd0jAgFVp9rzhFoO9o
pNWEpL1ZUsSpqJT2MGjw/Ww0WCMXuCJsiqqXiMT81lyfcUpfpz/hAOQR4EeFUNVwI9KrvKTHkv+4+ZJw4PcFGgiPes9ZfY/nuqlr
xxQ1tSl5FR6aHZQ8mMXWIr1aPRh2jdaEIzRwc73AuRrtu7bY7HOmn/wNwpluIazslWshlu53bQuGMD0VARFo27HfcAjEHG3Y7fp5
MBhBTzWbcNhlHvIKuVotuWYVcy3wMYaqkZD6P2Twetnm9l2nFKpx3J+7FzBaVCMqeKmCvo70RM0V08JKkKVJ+bvBhlCjKNayGZ/r
yKdmf2Kw48PCi3aesVAP+avsleMERTOrz+SzpiAuhNU2I966DW+MjV94/xR9tf6pA3vyp41Qa/kar6bjxQJQLUggiVVlxWYawg17
Eqk2mUv4r3/Q2udczHHr4F3tMbuT/iX5jvq5d5s4UU44EudYZOmDIDqd7+fHyBZBZE4hMQpAQGiSaPJ7WAoEJmRn+JQ/PLQeIdjX
TO2/LW2W2VdOlDnibTa31LMFkg6tsV4xilcUsogxJo287GGfa/rFWTO1dekdulRNGqSzD+Sd7bn550TMcDBfBXpSO4a9amR9t7No
8itFGczfspUV5B27AC18JEhehrF2EYdNuN9a39SIVAL9nzM/fBCSis4VkatrV8moH68y34P0TL0thvmG36KVpZfXSnYFrUX5G+yL
audAWVkbCZngjnsg99BBNIRcveXQ7T4DR9WCoftw6idZi+4NSfFK84YoH9/dnsBzbDhooX4UFRJQy9GyRh4yzNln7YRsYG5TxdjT
AYeHfe6pK260mYkgYlL6f2o8SGrKzU3ceYLCQN0S8p8RBDq0x0DyI07faZnDnSuVNGwfIXtT7rb9IZk/Yp8nFczKxZs3ZYBpeDbD
IzT5q2Jf+TFT9g5y9noUH60MtLnjBhmPkgEl57zzEYCftV4pxJLFdcq/nhxWJUn0ammREAfd9ntvjA7KQpzS0AtQwvfEJx3zf9eZ
oreL7qm/951jxmHbRrVq550L/MU2QJmwsHVGzcbK08X9aFAlRqw7OfY/ZshmEBkjJCoip1ZuuVpEyQlJRjmG8+HNvxIKt6KH8NhL
axANe9WDGU2u3slpl4+UPC3Khpf9CjmnwUS2KEj+p68I8gZxo1QSJSQRCHAHgm4NC2mJTXrjKGi9QUUREiJdvMnlJ7djI47D7z5M
1wwUOXpXVeun+igwu+P6k0zpLJDw9r3fkt2VSewQ1HhDTBVn5GRxwIxlshWoQYJf8fLWW2K848ggxtGpf5ot9pDzhg6b3rEfTofz
N/16/V3ZqL+5HY+Xinr5gPJifoQOPuMyvVN1A7H4YiuzJdeg4Nx0y4oGCt1jaaGSoZxzPecA9aeiQ6csFcaDenj4Re94KSZEqrhm
GiLjqjo60JJCbRCTIeiy+dxIVY+TIjuposxF4rwWdCmONmNrRvpynQJSfjnxIsy+6vuTDRe81/MkCPCKKlcImpLkjKbwf1LwMeWy
8C7mSpUEx0wKrelSsDbHeOZRcIocqPZrrxamezKUhcqqmUq1CHmIO0qdHS4eZ6AOyRaEYRmSTT9yITXq+T+wSVJhC/RBAxnw5xRi
+s8GDSv0AcqHhxhdUPuIy4pDg6FWeuE8Zulm9ga4tEIrhcJ0APgbKVk/KAVojhuXGXpkasn7WQf0vv9bRpHJGXOiawB9eOqebDiF
F03KuOoTDRp5kvDZm9oW9NHVCJI/t0Zt5P+3sbAe8kpIsClfWfeVF1cgbmSbuPXBU1uU9g1Hzst8fGvLxdJohOtW/jjdQxBraO5E
nTyQGwg3ZfFzrEPhsBtmo8QxBwN6XgoUwwVmOb8JweqIRNsIwK8aCB5VmHhAC64kWD1xZh9ChbaHNX1etps+dZ7p8emKQHJRGM8Q
MCHQbjjVqcnJurspLdl1C4AExCySflZiZAo9WO/flh8h4ESYRa8HRZ9oRCZCPgaVcmw/DXIsjL5d6Al0OK+20i5dzWYCP6XSSpQh
rFWChK1hUwE4ATPa9E8VIiqjgPIk3g28S71Eg1Yt1IIhPQT0sZXWb/5hEQcVAOW2N2AcCcxzJc9L0oegFeZfV2KCB9iXTvREuh1L
4W7YTFSTT6FZcxoPUtkExPWoOGaE2gHzQTC/45TqEk3AROn8tPNIwO69NzH7TJZ5aQ+sSoX+7HZgTd1pr8v0ggzex0e2QBYdPRoE
O9K6onB3ugVZOAXXXVAg6Uh71NyBrgBnbrPLm5+25aSdoqJoz8e/2W5Sx/jHRmdePC5nkq/NTdyeJwOlJhyHCrs/7GRRIoM/DbVl
Skc3egK5afAEFHmNC9kcW20miltuPpjoRTa0RdFtbMX8zhpWJq974tFurWq5M1zt8xSY36gjuMqddt2OpRx0W4KoPHdjR1Spur/2
+lKt88Fhq6LSEaLe2q3/PHtrfoEA5bqZjtcN44ixjz8F99NmPVnfqhjkgXdrUCWVQsyb23/1YeqT4IJDCI+Up3JvcT44kzVktvPD
2lpPRVRLBRCuULFsLBgNV6X2kdOGt+EWXIz06v5GPVloBh4guWPin50c+5ul3i71QDacfmkDNQpaFoQNlbHemphAGHFul5lo1BIH
sRmh+226m4dGdIwHxMcLcQCeRgGoY02Ge3VFs36NdiuarCIYajHfpC0PMTCeJcNM0tMfMVpSvUgRIu6fAEYSO8MKXjrLyi7GbsID
Uqx/LKwczOsXR7WmL5GX8mgktVoWjiSjNv7HRPs8Q2NtS+72NBzkR7w7Do4YAj8ph6GRFoW5P6rW92IwD2aVlaUFOZsANvnWO8R0
f1PGbXGSi1a8I2n3mYzJD5654mNHOkU8yC5BluI1GMJbRM/u7fLPSFHLs9EBzBzKIsL1G4JdNBBRjAqqoA0eUcC6M2cZO5f0W3Fp
Oi75oz8ijbuzBtu2hk9cLeWi9rkChPsXJQe7PJhMc/dmoMxxUDIZB+WEvoGz2CmcV3O4U46LEK7rA4qyfLz3/9GQh5h8WZlT1Q+G
prN6ZYh8w6j31DGRVR97MqqzXE5R5SodVxMUodyvYPBSb4/kQuimQE2BPDqIyP6lpsG9I+/5tVTDc6ONrEWGmUCXLXKwJjYYG4i3
HNNZs2wy4eadXGAsrUqvrWcCRz/fuwASmoI50QN4UKPy4Hr8zbaiaLUD2pczhP/FoTRJx8Q2UZ0udZps2594nrSqeeHIKcWhsFuW
BgIFL+AlxrjptTauKZurUV+MM00qofKmD0PUlgJz/3E96SV7OB0+433s0jXk3HDjiJnj3BrnDucFtW7FMQ8mYEgvpElFDIFCEYsL
rpUQXpUktEbzlvhUbYYsWH4JpPJ2uaxK7PaMbMFc927baFXHD7Eh4fYn7o5Rq6EWchMS31orFBT4Z9+7agjrWlOmLZXLFWBTWozJ
iVpb7HU/LegxzT44qWJ6navnarJhsft3xjdhi57u4mCb6CrJ5a8yoV7dNT5e4ExK2JNv3g/TpCggl1A37Adm5VJHXK5GdL9BfEzm
OE+XPBa6skmM+I07KXDEQHkNzxn+3DEB+O4/lnpm6KDvRaSdLn6WnS6YxGbz+E/zrp3AssbKG5BboliKOIJY6pTPxUXYmvVGKVI5
kCXRKTIMQgw8cI7H7G0dtfPNLfPgvXfpr5XBedzMH+zORp2cadQNTJ0MKQV3pEWQHTGXTkTmQ4vtHA9mvHMwC0B3opbhntUTy8+n
yE2Yx4vX1NN/mzM38aB954+LmSM6q67vnxu+J2zKkWV26+O0jQy5POjUWAQ38SK+xoXVTF45Dw/Cw1vlZ7ygFssaKOj0UP0fRxwv
INCT4gYBoYrXIO91aT4F4bRCNzNyWlzueT2htGCm6e/gYMIPGGF/W/ZDj3q4P40twnii455jI0EsqI1P60p7zfacXMpaHXZjOxei
3oCkpYfo2q0czzPgVSYrqG4ZVNgQJxvn8a5vNt2+4oQJtrgHHp0BzyaRfpRs4RASOJtM0xHk7UMw5fjf/sxItCJICHCEkMJ1JmP0
g8T7M0jpeAN8/tNwvQsAGRd3STIULMVgyfTof2i4idPIK3/gV04ZAHOamEApuxlUr1FXxJQqyXrVKZWMRX3Mbru8+GRxPNMmvFva
2MSHgTOD/aMBQkFukXqKa908xn+S3taRibt6hP2xRBEfn8zKGK1b7mdpqez29n/L5WOxf4OZ5MbNlian3s9BFQGJGp9AJ/fTSQKU
xry0l1dnOgUWU0sTPk3Yy7fdEEzq7qpKgMBXbvqK+42/cFPFKIIsD1qoJAmqBosdmCJ/GYwvCj2IEj7+4eYnoAAPM/CBopE57q82
lxrCp5KxzJkZM3sfdJi7Lv35wpWMc8xhReupnHJ6aooRnD1ym3M+C+DUeT5Np9Bx543Vu7L+2groSUWp0YA8JWi00kvE/VIR34Mf
p1kOXUoPQizPgUBuD/XhIfCbWyhnNFapg1PJ+kP9USZWSFTQ3zMtrKpM5VprKiQqwroqUqAw7l2o5o+CJbtJrawdPRlci7ghssFA
3YjR+vh+YbTXhVGEQatKwZW0qjr9bq8pLgVJGw78ZMF4eRcCtCx5F4UsttRupq6yabapsIKzAdLPIwDO4mPwuo2uhefzQ0vTL+k3
smU94J/HTzufTLz1TdYXKk1nXc+c5M66WQtfwvU3VY1DrMA1wSC91TuvxP8CLb2FPIqCQqY7r0W/qK256quY2BTJooMH6dtVhndC
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
+sCz+MBGGepffSL5irznfWLwZ3MzyjOIUG2Mz+irwz0CCbW8Uk0DHdRBEtK8uT/Ul2U7TivIFk/f1a4sytCMo5wcd6O1hZRI6IF2
YJ8nxNtx40O3QmaDxqKy5E74KMqv0oJtVtnyRUvHuLhQjpfqMbXWpFsLzznkXvHcgCdbyp+VRTQ/UPv5ellDwO2mRipMDpimoauM
lCVwtoS/o5V2HO/uwbdzihglfjXiwb6zD6pCpvzZYNjU1Mt0IS5nYK53xq1oJE5sMl9burdDYUWbyUUouzcnGqrZzTCF3nPRve1k
IlgER9aL3JIgSP9gRgv8SGmzUh5B4fI1rJ+F7uQccHiAX1v5y6sWOmXpjKxsAiffpod9yH3c4cIM3913s1wkik9Y/edqjQ3YiKBw
Mu60ysQPdg5Mw/zjh6e0Z+4eoSLNmqQMa9l/LyKyA4KNokP9X9KIV3PVeeuc8gZZm4WvEz12IsluRtSAt/wJ0Q0zX3jiLn04kfAs
ujx02qjkbtJQ8euQQw80zVhW5mB0aDi8hmX7hl50WfIeTrCQHi80MRL+xYmFQvttWQaLx1Jgh+5xdeIS/9y4ow1R7IXEIraXKEnv
1rRzb4n1npYXArdqXjkSLdiPoTfVbFBWt1eZH6KOfYHYETVpTGDrlrEJWRxEEdcAerW5qpxDFgNydbjDbFL92atpB2j/rq7S3oHb
qiWdmj8IE6QSGSoaAm523y30CR43ro5jqwoZdfmnSC/sS/KK0t3wkv/n9OQ+U76v/BHuoDD431hkDeDALAlKUxYkHJcPpc1l2h5j
Fb1HVRkYp+f0I6eImmbdnfBpzhE/ar0u9VE/55/bFe5xOkp1Xgj2Idc8rFQXYNcWnBBnIP9PcuQdz2b2H4KpsZnOe1hsaYVoavSr
0lVx2pFTYlBF1hr6PyAQpbt3q+85VAhg51ldSmvHpOTwt+IrAqfODOj3GU8DtcfC0H3Ch09c0ZR8hL5MY2uWPqo2DgNe3twYD3P6
Knt78T4xi7OumRdjddM+T11kx2LEKc8K9yeCT4Kqk2TfZJI/P3gmsMjVC0CVHM7+nfZxjoa28v38573irP3+XlMF+oxrJNpyoOzi
1N9yNopx4LZdLzTT2zN+9sMkdAFDfpYA49QWMS3RKGGx5ffd+nOb/oG6Apnlq+7/s5Nc50jSXjhDsfbv1rqHJLyEOVH8E5eps1C/
uPv23n+dNCEiSWpCk9WoqKqksW6cTb4Hm4PCdL6snK8B7BqklbZfIodgv+WUaUVXqWToy9RtwxQ9jGTK61S2oDRVXolM3ZkBtLV/
+eYDEP5VBY4R1Lr+HUYpdoF+wlLhP97e9Slo28uqpQ/1JqRUct4Wu/syYmNsUl9DaCRcllXQDuz0vSuAGGCJ0lPjsDBdUaBGces+
C7CUyJaAG8c6WAHy1c0OkpCD7ImeiU1gbN/ymuUL8P0swvpZUoEJ6R6D0Zyw6FrRihqoo4KvodusUpaMroSjQixWAGreKaVr7qgT
a1PsB15FVFEth3cbS40p7UteRPkPVNX65c9L0gwiMB6800oRjhpEtRuV5Yo20OZaa8yg8Vxim+bg+mitGhAqgJAD3QcVa8CK6qLE
h+kKRbyvMogtSzXibBUi0/C5Xh0089lOw+4e1bEGeDUo6etkNR15tXoA6kpu48ka5VVweXRAyDdNkRCX8vjuBEHQMbokzjnB1mTC
XygAAUEuiO+37rzTiRvM+HbE9Jd/F+XZcwg/S8cDq8E4ZXieewxFZFi+tLBhMQ79ub9WcmKVAkJuf74BxoiYyby8RQuSsNxioE4N
JpgzCta5t2vOmxOnlp1IvZSVR+iFwDc3+ivYIi/tZkEtb+75yM+ppYBzR31VJnoLlPhaEmEKAks5hXm6EGGjXFhavOdniiS0NHvQ
jPT+ORlekcOPk196RT3ZiDcbNgzg7yIvwhfSMFAwf/TLN+Ie0i+6EIzrVB45hHgWqQBmtE3AITwfxbl3C8XqVT9NQBmdVIHCSLgx
WHLP59eEn3K8NM3HKfxaSeoHDBvPW3Dwc373rr+nQsav4DhGTttHc6JfMe5SV1ZZNr4IlFkiDppgnWw0G+B+yFp7zLJ8ZvaGYsdL
byYCgA9VsU1+C3NcSGSiqNz3OKXaUT5vWy6uMxuCAxiZ1Q70Da5oyWhpnzfbBAbYrfaf71TBMIxK+1XGbxVnlRHgondhMXDkyCod
KNR1/0T6EwQx57Xsw25t4rPqtyU8wNC659Txx36Ps+JDMw7kapqI1BaBpzxpalUaa2JN4BZI0arAQnAoxxQxGGxOVU2v1lP/U7rL
0woTUcleKNJBfV4vSmobdEWJU+mY7ZpJcyoTfXErM5kTM9MUNRyJcrfr76MohqY9jPe4qQSrmIl7RM0Vp13Ul+9B0Ab3RCpyoizr
l2NRsbdEAn+YkQsHDOi1sy7p28tXRXI11lbxVIGTMl1EUwXEGma+yxr4QFyKsc/d2E90FXRyVjwObLHJCzrRa0RmG7KXZmeWdcjP
OPqJAmqq75KMMKvrwO/qgOxhREFo725QNu9zWcwHKAD57qK9SZxiuk2heC3b3blyRPi2fELZTNYYRcL6e25Czvar56itxNfCmuPV
YEPNs0TTh1hFGvNT04KEn2t+C7ajIbax1q8gRJXI1RntxpH78Jkd87Ktt10YRLLT2jEgg4lM/lKVT9x/xwJnOCMgi6U0ro78vMtr
capGZztkow17jp/+7XCBx7OJp8JlJRHpc9sikm14pZQftqx4i69zfglQoNge53ACUKmY3J8BtIGNbPdUVc1rqhlLcpnIqNSzpQL7
UjC/rwdH3IZLi03evJU43QomMarwIiRawEWYfmxk9tshdI7kBBc1k8gwtKHrObBfORG8esLh9ZMLJxFe/Y7opktF2+XrySG9HVfz
oJ13KmsaqMPLaDYJvrERPuUQocYYQUDue27RgNtaB8JrXmerdm2PTVtC9ZVCTvgRfzVaAjxR2JtGQVy2t9fBJvW6H4o6h1hzvqZ3
utTuRNB80cktX8C3IJHAypeDKWpFjo79hReUyzUaD4urJd97endJvXsxH3O0NStg35MJE49H7ghfCRb/nRequnruL4H8ltjATEbd
HvTAzfFLHr07BMxaby4oA7hfscaggi6CbFe9JyqobkkAD8uleGPKuWy3LAqm64NckFy6bUnuQRHTrSO7aPSl67my/jDiymi2l4tZ
51Qjdu47AnaZiF/T1KYH5GZ8LKmkI6T+AY3vDflq6QRjmJJGZsFpy02hy5ejXvosd+zb/tnNLJnEUdSO/RVzuuG+fBbNWAeADZC1
LJN4JBkZkTrxjF5uuRJosyfuTL0i3qtCRsIJlgqg1gJdtoYSXLW6tiF0CR2md6sSeK4l7xBuhlZrTcwaQjhwTsDkzMOtWJE9nY2D
vVetIV17MojCchpf0vV4WvKHX7iOIlPSEt1sv4iJ90CL4+FAt5SIlD5hR6YcqorRFRC/D47DeRgxNREIjIEqrNkMt7ij1Llyia5o
4GWlVr3zTYaNiJ+OMTSl6dRhLSgJe0lGoh1xrVZtijwbz6s3mhLaL0k10MJwp0r9FBcIshXR5f1hv3UeC3WsO/vpJr06H440wTt0
95aYZkN4Cy4kWmGqvywgHSVsdRt9STrHeRXVQyUmWRFMgKgo5Bm/qeqQDG0P++A7cLwr2ftaBur3z/dteaqDXc5GJkqNqhyjAlsG
soPxGrcl3QWO79LvLwST3ndYJL925zQb7WdTZpOG4kE6m4faejE9joa21v8qmsGMpU+b7OJ6L+pgJ7dxgeMtFru8NK1Mhq9GNLqg
9nu5J8rFipzBuWkxaM2zn2opS24MH+szx/tgbFQTldcgPLYVoEXIhRdLvCUv94HE0oZrToajMG3RRQSb3OJeY2yoeZ7iE+isO89t
j9Wr1me+Xr4Rj5M+xom4a/IMWQ0iRxG7lC7FdrbSsUV3KIkhQBBoU//cCluaHYFTFMnXXwt5K/Jlr5zn8zM8HNQv8WYo5UZzjrgp
CK3Pg1nsacYCdVp4NItX7QMGlDrENs8iObZxKtKP3Z0h1BZ/41IHNhnT+3O1ZBsJzN3QdPoe/8JBCpJNxMjGHCZfTpfy/CEcbozp
SewDBaybbRfcI+indQxxkGvjnQpBBVz+IzvwkQ3HgVrWnB3SQVjC6mApknuFuWf6MCgnDT/dAfVE27jJUIhZHgl15Ik3RALiSo+d
yDxKsXmWXyxXCflExav3CT5JxMjOm/9BroTJuJC+JoMLs83zaQg6zgtivaAkzuur028TISYiz3qRMHMkCTu15lw2QAKg9+r+scz0
lRhDm/kgxGCj4X20pcAcI27jXupQkmy/LtF7e5Q8RV0i9YndVTQs88I26FqtMpIgvGcjPDyr+Zcd04dcq4GZMNuyYD9AADkIQo+M
FOiX+yi9qUWvxGBZJCavYRJVNolLXq712EtXq9y/L4EoHMHgD6+PwjwRZD88MKhgycIY6fVhNCaVyDAIHL7xVAzpI1ZZEMV6rQnl
AnS61UV2YlpboSOiSgkoJcPz+Y2LXnjonHE67pwdb5AF3EjrZ5MYea2caUGeeCfR52YNzgK+/mahNhSy3Xl5ixsqcuAm7nGYMHLW
n2wE6eYQOcJxgDisOMWbw+fw5l5hm74Ft0LnHlZBIkmEX1XEFPBZuH2hoWf0V/CGLAGns0j5gEyBx4eod7bVBFmf8/Vy9Morqwpm
vfD6qFCQDd7U8+Bi4h+VDdabcr2VhxSfdNLYHBNs1aDzaX0DCN6uLi3foA9GWjBWLeFilQY3adqzeD4oeGhCAjnRYgIEsp1qBB0u
2ArgVscxbnweTEjTxEkvGlFyTbIe8u4HbGkr6YVi+6uWHWFi6HFy6zUXIauQh549ljYw/j69zhhIVGlZgvOPcF+SLXyK0WBm5yq6
bEYD7HwqLU3sjqGTDEEysOLPG4tupUdcvQk3rUshbi0JoMiswsWmg91gApo36Yq5vL8NIGZLrvJaIC5zpfWMmpyN61Fhco2dpNu7
E5YY26kpOQVGN+nXRrEfsyNFbDV8zEv32M1IQQrVCVtHVXSdSEvlB1Lz4WuQogy6PsK51gfPPqZAvMhm+gZY+Oa6ItDq/ALykcWX
1EJaEsWWVpI/SGXpFvLDrAMEJe56AyehFtnxDJav8oCh4gj4e228d+gvhEFvaRkXALnV0PJi44SZ06FbLqBp3pmb+2YjeBD7CNBH
o5qzZzomTsyy6jvPmQWftkbBIbARt39dhbf6jZDE/QNkPTAABkIKl5W3j9Btk6jGYeryQLeXpDMa+PyGDOd1IKIfOuwUTFe5JdYr
sHAk1g9KXI2Yh9NTd4vMLvAzHaDLxCMwnO/J3SRqWANgtvphHNvNLwsn5T5W3j5wiauZBvDzFQ3l1B6Pz6KcJz0IHRGmgLRqF5yM
eHrr3vs3LDPlfvsFC0ji4tKVHUWZS6orBTLhwXhug5HcHUMM/gpg5GFYB/ybisL4lTm97o1igcrCKJWCwfEI+gdlelpwPelsYmjo
mIj1ev6iOn8ZURMAM7Fy3PfCuOx6K2r/4nkpUnzqI292mPQjDwyjSbj9SDMCcZ2ZPVQVs3V8e+c8JpDyz/R0FgpJSJHti8/0/BS4
jUPIwcI0dPLAv5umczKSCQEElDLiuIkVLa913l2iuKYdua1RRMfjiDONett1ajRQJv2cQ8J/kJAQHYnHrXybJ+iGD6I8eHjYNFHT
3ze3bJDZp2VRH65U3OL3jAMsREfQ+IqCxYfDGV/udaJQ5W4hJEF255kQBCy/ZsTthUXkz/dpRLY7M6pCjr1ejKCj2c/vCb5uS7GY
MHKvq2Tr16+8cfWlyubMqfnQ6LQ4k7WUjj39QJBGrU+qTAY1xiywSMWUMfPe+UEAg9oVmjQ9Pf4nufXCjGyhfAErlB4i9uNVkqtL
cZC9PdLeSe7gyMw8IgQ69gZ5uahi64BnSTp1WI5rewSUTVLY+i20Nu7GN3ba4Achm8WOidAuaXy2Ax2bTkzEqu4mCpvIHIUigu/x
us+WhL7FZC0+tDiV6t/XMN5XJW+UUpmMr9EIKDtUrmKMsEf8kIyunENGNsd8Qs+5koKk47+UITVTxJ5HIv1DcZ1l3Bn1ivgSJhG8
KS8KBV3baXTpJwoO2zQ7H36J1d1UuVrjSccFJSXX9Sz7lRk+p27lqgdEnuhQoVddkY4oZLsHDtY0gPzXwqU0OXrbp/QfB/mpjHOj
Yp0QNsWs9KLnrqffnH11x6wMC9r2l2V15Q05C4i/ZmYvJF9Mp4B2BqGg85RJov295KTn3bdrnyhprpm4xhDERcpyn2Z3MtujokYe
Rr8v0ILsFxLHzWpBlqwg6l9walRQqr7OEpajaF5ObxL8LMry6GBw4Pthqd7PEKTc+j+lJRWVMTnDqZCxUgiRk9LZ8eBAi45BQdGZ
uTLPApv6CMLa6rch2dZmOWDZ5uSA28nLRuv7BeQGyf5xtyhk0MOKo9OpdL9b4jn5mgWKHrD70odE/VS9QyQjChNcWhf+ZRsFsVaf
EzI2Y9MTpjRGsctYnCOP0tuTN6/3SHisyi4/Hd0mlLyXqNLo/EzhokuDpVP9nibxeU8dlCCT4b7I8yvZQBeQNISR03b6rKrmCnAm
q5CDJ5q0Pot5yHOcOEBUk0uiSe77D5RTCH/TXWUfZ/bLlf75FwZXgzQfYcplomty2v/eTwjbplCTyujNP/blRcGQEXIcphtgCAON
m7k9e+mKrVlNXwkMKgr8RPM4ESPHCMylB56QOM2u1sb1x8X7TsCEZS9egeK/Z4XWYFfG95iIeQRlcoi38dTLY3fOL+0CEEjMfj5F
ZdqBHjaKkQbvNEL5iBgvBWWSUL5CupK2ISmGcMxbwgXtbnVj612Tv2AeCAQTZHUXqBQBBqMP0iY1xmR2DMNvgBh788Og3jbJWW5R
RZxZE373zLa11V5I+SB7tAV41cJHpPc3wsJ8XUUe8rcNYv+zAsPFD1ywvPBNPOaVEKV2GhFltqiWPJUKt4mFAGWm01qVYlIvJpEe
knYvu2tg5psVrK+Xh9gs2rI6HQgkRESb/THulWklZiFo/N4M0cCuJm+QC3drSA2bL5hwu6pWRrJtVaghJWpGqVmBo5aW1/5O+egl
KmT5GR1FHDutheR+61f3v3N1DiTGVUujymzTZwqjBhE9BET1Xt618TjDlzvF1l+AeM5P/h97LQVfotsJei74W/QJafGr051FzuZ5
nu1bNbz+jDEa+9BZg5Fh5Ws7U91VQo1LOgpCxZm/o35gxGdZnc0LTFD+XCcTgiTu49+EmOssSWzgVz7WYq+N9XaeHLTBbQms85av
ywvt/KXXifKccEfhvx8Bf8rVGH9WNNnTD65xltGweHIQS/UTZ4UEMabEX/mKkkL7Tr5JsfAPDVXZwLy7Cn2rjM6fFX0zmuVe3RoJ
3BuyAKyvYR+rZe+CNUsrd4VGI6enMvbxHYrTejbKCM1XdVwjAFT4Iln5iMS6RnkST+MXmxmPPrtghNr+/kUQVM+hbPZTIYcZLu50
mhQ07QkNcl3lBMEoQdBGWs1gdu7hKZb4W35jutJSACJ6WONLiha4Wo/hGestQNYoFoIFLp0aJFgYI9qFjbLQSF9BLO6CD7LMy7vE
6yrz/f6hwC6I+ljGPCH3XgZUrBsH0agLBUrpme+3BaxsA0H1eRWuIYGZoQWzFy0EcKE7paZWX5pIYW3b5O3MriYvCjKXIX37w1MJ
ygHM6VDfefe+U6nz8VlgHY90ocJfpW78jspFQ5q2zbuxXZB4Zju1qiCTChAz0QaIQikAe0hxbQcqsdoKFQmryIvX9QSoYg2gAvd4
Ux7WMJNu8GW67lI9rlSNVeZbtZ5jIcXjxgbvyLWTRG8gHrBajTaGT13LAbHGAsc9Xx1OOEgQG2TtwYSSbyw5PF7UMXv8tANCXscg
V2XSH4gDWKFBaSu7l50GVxWYPwA7xcn/v9b6lGKdunFU3MleR3jzKAer71RPCKM2Ywcpd62abFTebcHStzlHPyNV+rVd4iMkF+6n
PUOVNjceV8oYqD86fGw9L+NWFq9NFQjfXZxrmOaCG6KyKWoMOjM7GTD3nesXufIEUjD/wkK4Dz0WIwt6sfJ0ZiZH3Oq7sqMrJfRZ
s+V1CGzfR50bcTdGNMDxXYV88n+UFJN9TWgRyr3+XJBg3cJ7ycf8s3B4RhmqbXObpZaxh6oOhkGvZlvuUTzx+24aUfJ3YbOpnfAR
9iWLYPgzFzcdeGSkDWQvTRwo1xLAY5m2BHtzoICtdoyd6U1dZYcSouMFbdIT5fZi3uzt7bvevAeZ9jCJVs8MLJUrMHcGy/oz22Ox
+f4B/oBGK4/mGSlcMYx97iIUhzE8lPb2FoeTQGC5mmIEvqeuQtXT1O0k67j62QWHpFLBnQ5jc6Ojv+XH68YGvscr1ma+uP/ZB/in
6mSsVneFJCDRzzLvHYpQklgw+1zWXG4meEPsWGqc5U3jRQF+NmhmG+bmeXejevMyxOhlAAdMdr4bsazffnOf6CMYWbbbBgS036Jf
LhOsfkNGZZvGX0gmX4i2y56FdwIInpDKq6wUsWE3EvZaumjzOE+H2M/1ZM/yTBd6I9k2dpunV7NlroE3QXiUcjshC7c9Tou3b3HL
NS0INlV8Kubwq99z2OSxlIw3qow2zn8gzn7o1ioHmz8aoa+xxI+lQ+zUoCo5JnwAiBtYU5SidqqQ8nfTIQ5lUep1ThENY2N98USx
H6T9vkZBQrTbDGLmljbOmfzISR2t9h83nsDC7QwcDmcMf3tN3N4NIdFZkiu9amASxk7ol6vUUpL0aBrT9zWFLXjZV007Ae/g9OFo
SXN0vidSS+XiltWN94K9/TPdGwwu6Vyu6U8cOLiZmGKjFAUUkWQ27sC+GouFFo7Y43C8RuZQFs3hTPRiwSzxpVOCvqnIZ7q+zpMb
DK/zDbYrktqvnEcm6A+f2Uj4dKBpBXzdXaPpxddbWBu4hM2UUI6gYUbNEzW50EH3F0jcrmnEXMHWii0Fgw2+wbM9dHPzgxiFKA7N
m3OKAm+nOdSDx0XRP0MQsNZBR7zALs3+HvYVSW9bxLkYHvB4WNIuKvdLPgoo24NOBaQyUmDAdU+hysA3YyzU8NVOnX8PYRhNy5zP
935F6haLaGzpi4HbL0hfQrHq5c2/Ss27SOHhN/mR9Mw74UCfFeDljLLuhUZr0PCA+rHCn1HG2JuRVjxnCZoLBpmsQRht0vIpXUm9
mizYAkxva7Mg4Mtd6dTU5pDirCBdT/rA5NCzdHWaZZUOJkdD/kFqw2FUymfoz3PShoaScEPTnjOB4avL2P8ZV2IXJhSz8l4uI7SH
WGtLmSd2poVNN9ey2W5y4szhuVK1Zw4nVVKJTMEzowGgTM01AW3R+gUR95W1NVx19aDEdYoZ42N14pIS8QWY7OAtZzlW3lWlcfg8
jE9hna57pcpX1FU/vhOCGj57Mze29nNePmGDUVLv1cEtzl6iWcwShLjPBEYMEDFuBcCoySPP02mfWp0JWUNCowczli/9ycIpbtKb
Lp9Bl9IHlFXrro40Q6uoegEFb1hkk0IvckNOIlcgVQAQZjLQPJLlwWWSYkjBZQzANvxyeO41nUAQAkwxBxKRbLd+8QYAXuJ70ZLM
cNcY7XW4uEAO2P6LFA0+Iui1OMKrg+i5Zhuspq0uyw9+GFv7fPDRbuaFJ8kmye9TMGy8FiGcdxssNWacbhE97NTqQjAygl3xLXft
4SUUMkwNf30+VqOFVSPtE2YO5pPhczrTOvVbV/evg3aoxX/Zuy0WcFvP56HB2R+DtluO4X8I+MerhkDWMk97S6lLgwa3RxE3yT/x
pnxHwFVDIzSjET49m5syuBvQJzE/f5RJyfVwSJquwV8yZ+RUTF4k5Xf+//edVrqvALpCQDQ/auCkEBtf0wa/cue3HuNHXyV7gbhO
lHucxSBwv6Uh8X63kNJ9mqQwEU+i8mDEsymt8wkRiboEgOHuyZ5U/kQ+Y3OcZF0CBB3IiT0mC0X6jCNPk76dR3cikOcJg9iYBZSd
mpS5VoQ1tLEbgvevEhiofqdxwqf/0NpDms1Xob0YsNaOD2Z0+6wsNSCd9Ohl4bPUmSiOdv+2erHa+eXXUx6wkM/yL0KmBbtJ3jMY
OjpdPEy/zmIFX161mAJ5wN9/IDb+i9WEFk3Epzwr7HZUsrEqNRyF6UirziJD37sEy3vTgsafYbDFmoCmx+ZQjFQ2hEW7bhwp4l6T
GKGkmSs4V2qpIJt8v5X8BlOlQP2XshFKj0OWkZhznF7T3TDm8BcsbkTthXl/JQ1/JigWvjpM9YvKU6D9ItOSLsX8lCmK0jEIQbIg
sqbXMxLUGYp/csshukxh5ViNwqvUUZBbbTCCEuURwljQqLhz4LF9jTm4sOQDjnHSC5EupLIjudMvcMCxMwHs6Slk+QFUbEWcrU3e
uBAXLW3Rs+iWv6s0oRz2H+55oKPLlQD54EzRqF60e+eqmw3mONKexqL23TXR6Z0r3gB/faFZJuf/RVp7hn0xXokLL9X1WgiHw7D5
0iTfzDHbycFBY8JpOsyzT1X4gIxu4RRXNdbB5l0SKBLm+CxxBGaFZh6WZo7bQR5fj33TZjXF0nGshuFW1i4gxmAEUfQLEwOuEagn
VD4N5R5X591UtG5OK9pQRQs4vz4UZ98I8RtlBaEd0EZMuFWiTbQ8hgCbwKeTv5itBz6fnmngMxyy963ydZt00XZUV02N79o8veVy
Bx1bIx7D15uWX4bnuVvuTPixCXaInpXcgVieunxM0P4TZJHJ3VGlHWVJuwRb5OIqgoAtIwMfYlxiTW1jbRXg9xitH1ebOQZGn7uh
xI8zs7MJh4nGAZF7wE4Ogl+UD/9a+Pf3hpFQJSR6xhorpdy+FOmkhTjho8XZ+cVxfZnMms6Dqycpl1Px25LRBVhHiYU98RFNvhtz
GkUmczbE/Ba9E5SnILuxI6B/4PaM07sduBcHeVXOi8DU74qUKSnui4eujmX36I/nkcy0jHtSFBIl6czBjiJpi5/pLTndIi4gHEEm
7/Xt8D9xsIFaCdKxgcXHqJq8VGCsCxCj3CjApxRgHqKRiAd4kBhkQqFbqr3+ZbYr6sQLSu4Hu+jrok5+shjxrthQtftb0QRdX8zz
PA8L6Wwl87hdJLeHp3B/HwPaANylQJxy3zpueu8pZQfqcGafwrg8Y3FDahfeIIK6Wvkm7hg6YCAJFwSh7bzq15f7v5o5IqopKpXR
CwrSCI/2RcopeZU/0GjjNlmYtMH4W4zp6yj9FZfFGFETlwZY9pFmA5GLXdlsdG2rIZeUUmJ5c70rtOUFMETyGqDxQ5NMnuvg8/M9
40w0VeYvW0xz/bvIQbGFksJRKmbe96M8NLGnvQ4SjdZ3pDAN1tWarCtBJcmXLhCF6qW0d4aKngBoWXlO9XgR/lQedXDde3FRtVG8
BDCdnhGsPbWnv4OFZxYjCE9Tqy+gUVUQd5gqxAALnuM04CI1q/Gyqz8gGLXjFiHZuKGmmHdVFc5/SV/rKz8DJLuIn5ZvMLkDkjgb
Mvl2fjjYjzEWCRPrvaS8iDaquAjsgEtlo8xcmYeSXMjl+WOJFeUTvb23jGRzzviuyhy+TAPGxSYnvKdgWlEjZ2+EWleCYwJg7SBc
Akrcoh76mrNaczfAHn33wXcooNatpVFBm3UgaXLLLfouNjiKqERqE+TL5NV7DdivezvdfH+0DbvG0KM/Py4OmHTrwvoEUxYkjQki
NDXk3KYxnBoEZ2jP1NPBY3An8gbO8niQU2UnNIxI/1ge2I0G8B4zcjQgboUrrGr04VI8ySjFe6rqBp5S7RHnKXd1ntOh5DlJHpj4
vJNM25J8nxkg3szWB3xcnm91c1c0a1Bi0jau5HvfYrLOAyO+5H1ehqRj3GnG6B+b8Zer4wzDsLz5Upfy5g4ml8QtW3zgNwzPsI1u
L+Bn35aoQAlES97QyY15iPu3gSi0GM2Tm1EyDCG2iKrFmTLzNiJLpsO44PPjgMRLgCzEzl7kWRyrxHk3bRdRGgjkt9x0YrA/d1SV
sEZIYBTREkyArITxY/5uCCpgMnMFL1RHF+yYc2CPVwwFxkJ2mbocz4EU/DsrBGYi5UczQIM+W1wKa4+K9MmkdGxQNT1mBQGzOmzd
lN4nZ2Pz1aYS/L9SqoUIFGlcH/WFvR2/G/fAp7xCyrGjn6U5eBXJfTRJlE+GunOAGCJ8HEjBsM7Hm6eYCxc26/KNMRAWBYRTESyd
f1tTXEE69l4AX1vmwNZ5i4dKJZ6y82Wxy4U5BiU7AZGxq+GDKBNUPBqRpFYddDUWfo6GlOp4SyVOsK1YkB7tYZLDBNs2K0wGHINH
EPPEjhI54X6yX0cTy0tszinivbm5SrlH4Lcm8gRm0Ehkr0qruHadnDxhEYvc3NVqgxRTv/3BWT1OfK1jlayoMtzNlrTVldjROKNt
4JKvwaNPKG6xV3vRsSLsfWs3s+phvZfDlTUpCR1t8P+Afqkx47gvIKL0WKg6c1b/dOQjerXFM2G3fAil1tf7+ZR105z/fvzzJa/i
dB7Rvwlx1Pz6W8O6OJ3MBitp2p9GXzAKF6cOVc47e9B/NNf471iOwWculV3WzCsGbbNboveiWf7/ySR2eFiWYx2eqpbC06kd1A1I
cojSJo3WHyRxXeyX6aekTc5WUxgwUS5yYkm4HMmmqNldIJqXWaFzVOergVCmSE9u5AeJD2dNkXt2x7LX9ZRhTs3I7pP0idGzsA+1
7x/sGz7Avov9LZfBtMty+et6tEWGP+cqS87QqEPVHO1NiO2TyOymsDQxEnbRJeem54vw/CMU3ndrCVAUV0hk0eIJ6zl2zRP1JEW8
4G+OOAX8SFAD3WrGvKabC/W29RWXUEW6DUWfJqOuXNOkNOSiupInrb1XvnCbLk8oF5fXf1cUUAzMH+sCC72oPed6Sk7oCmgRJJiR
p/ZncyYzAYQ4pWmsYn2pd6kPh1+z559X0YEd4x2NorKrRmH6RZGyZ+tBj/5R920v2PFowXOY/ha3aEBGFC1rGQlptZfw5khaEHrj
IGHTVP+PauVvwfeW9nOQdtxJXva34l7noTWfAx8rL+2jiutenKCafRQLKuXrS5A+3UpyF5UnpRuaAI99eHBpxPFVIVlewy3V9w3R
sRckeNwUPVHPvP+5r85FyK+fJ/Mwlf6egBQ/agCXJqx7FtaDYeMZlBWRY2RfwCIyxwB+a4/TwFUpNIxZWs+0ItxCCqN4eblcQT3U
L8wSMjk2k7GNE/QBJkgQtbz8ICb8ULez25y9Z397BfR6EwEoMq6HQOuRL2BuR7dl17Cx9RNh7Up/HHBqzQm9nOl18pQuwxsnq9vr
IiMospNKXktWdbh1qwZwxB6gkOGMxIlDT7Mf/KQcAUZqsV6KIjupWa73KCrY0CROyY4fnpMix4UbAweAuWmv0YVsOtsJ6w/xXgBC
ZpSfrhgyKAUQW8VbZAeTYtM2aqCoqlm8rzWGQDxnKqSMy5LlVW4xqcwzGaaBE8f89UFOxdUgw8H7SbK1QHg4dMrxphVFyttPeuLv
YivJbxxe38afYFUc03zqMmMrYuptpBdLmryL3OOSW6QdVB6BnHVh+kURM5sZNbPk/RQudCGvdXdJ9d8wk54fFSVRQiiDrH7oihxY
yDP5j2nmNg88CdfKFahlLu4sm8a6jXOulprcXJmaWQmSsUtySEvjCcQ1qGCerWrpPdiNtNZGWbBDZqq9F/BCKW4BdTX5mkesndra
F561DBgZ4b0LNL5M1I6eECqIG0+EzKa/GLuOFaLZb750xzIGBUdL8ausjx5c/iXAYlp81wJ5HKI+ZTlUA4RsQO70IFE1jVrHJo0T
FtsHeFslFbmx/TvD9rOjsG39WaU7n7YYvnoP/jU3C+cprh2wJlEn3uAxEvdkWDepXxUYZ949NR/YR7CncIz2OlBIUutgDDKhY0sb
pAlohhI5JjruCadKwn2JVfiQ+SAdZ9oQ1IO9rQ09c2Dw/NxXqG7JrFmrc6WL+xVZPxdbw+fxRmubXk25wYaW9BOZj0fwPJ9EaJxn
BhTXXltta9Ru+6J5dXamJhsSnNYUI0J8CoaiQ40wCTOu9H3pX/fPhgfUg6cQThHYCldOnV5ud41DffTw9YvJ3yxob4XXHDKdp8zj
+KrwiaFmk9h1ZHJ9aOpjQJmaxxQQcReM+gPjKS8T//MuPYN/QTPQJJoBpZW6oTX61hzbE04BwapFSVLwCT2VhdjqclGv5Cim/tf/
npdJM/1BxdT1cArPU0bQQQjJOzzZoSxRI/Vz8QjTnGJXzqrsjgA/9EA5+7owcs99wM6LHxcscdi5FiZGVLJe1woVCaO8zq0dxngm
MjzYBnWFHs3HlxUq9spBk0lvXt5vHSr+vPTA6T5zPMudcyfrUUOaJ6LTPIVE1O3nmIlXbgieZhsZ24tJOMVzHbm3o+69WJXAgsA4
IMERURnJCO5/hS27QM08+VueRPwTpMzXjK5BnMbOS5DN5B8Wtu2mdLMjx04FGJy8iWYbxxcTgZUjR/bOGWxxYq0BGGFA50U7tumQ
H/BDJyOLA11SJb6fT+W0PxPKYET3ZcxKrNGsacVvFRNW9nS2iRUCJnd0+41PpUAQw34UYNEAW+9c+NaOkgMD4VKTaN0ichEJJDRV
ZzsUAgfb9rXtU++L8LtmLLG4CsbdKr2OA/OVjiW0ZHpOY0POBXYhjHC+icPCAC9Re1DYgL7oBFCFl869H1OtaDEVMffMRV797lVm
COjyUcxGv5s3D7AeuAv5wdxwCG47OWBVnhIy0tfDBH6YKX4mLFC7aSYdO42r9Lxkbu6zUXz82377O6rTJ9JvLCBCnKuXES0zo0iC
6tnvfe3hGzN69zxMf/Hb4qMQiFDuSad97mrcqjlCaT/orsJI2CYF6YC1ZXXq4bTh1WdlwcJtpYed+HSOj1GJd3KX/9nBX3AhTOVX
WptCjZ9awxp8VFsBqFLmRjuqXL0R/CTLcEkls9YKvKgr8+Up/Vxr97NIDPyE02rvEv2bjxIabjCiHNFyztlS1TaSusXg/OEbNh8b
DHD+rCTWB/l5iQFfLA+QmxyXaoQKA0Aw/9X2/JXWiaxthPHOMEt/U1XjCzxGiYsHfNqELq0IXbUZLFMSfK1Rjd5aMV0NRPfMwQnS
g874D+ecT7zqX4EhNTPaOC1uWKKONmwpyM+sDSh4kCV1uBMwnOv5b6KD9053y1sSpVS/gff/Z1013H2dM2MJoOzfvpb03/X0g17I
RphncZZulcTIjbAvlw5cJ+H5kK+cUm3vJ+rXUj84hWfPonOUKcGGL7sbCm3W/l8clrlBb89gFEflkJ7uRNyHjIdM53WSGNF6p7N7
QMjmCigxtTZy7QkD8A2f8vVUrkUv3kp1KWg0/I/hc+eH0MRmR/k9PdNan8gV+YnqRyBWluLQSi35porvcf0ULqCthJ8n6OHXCBv1
ydeWIC18/c4aKfY4xK8Js48DM4V3y/7Xs0HyBpD/6Pt86IiAahSZcRhpkrbtQpIDTbrl00DErX/STU6/oQPdA8+5uDFtcAXjDmCr
U3jt6XJJKfRXcdB3NTPvTnSlAxTX2wMnb/f4Uv7oB83MCySJX7MEimbrKDBcGSXRvrmjU35Hlgl1ygZbE6ta0fkdMqIJvlp3J86L
tH+lbRxKUTRkl4qYDJSfUqVSkN4vecO51FnbEdBJbkYuowHXDi7CLA7pcDu8u2neljIbkKr3qV1DEL9s4j8HbOXWUoL5ZU4fviqW
0vNXI5Lo7o0em9Y+RBCRVL4iq14ZnKlIqTTKQMhX/8pNnoeKamjWDdFqZjF3p6feoSUU7NzooCFbZbdTUfaXL8X53AO+R97yFr13
oMJTp+afZzEp2vgLCFRklnfLG/ZvTgdqJxqWZLNapXcg3jW5dj368U4F07e54AnzlxvQdDurzRr0uZ8/CK1seB7z8xZpyvwGibes
0EHSwbvsfznTxPsght8Ssl0G8IgW9Hb07cihsbVYY2bPqauQhznxep7xh2ZVfRnVv7iMweXHKtukivSoAy3F7w54PEg75H+Wtu8S
iyOuI9zNHn84rQCsRuA4JmD3OvFazjUY/OtC5/ffyQo71fRwfp87DU79V+HVYD26Jr1YdxdSEtXxu055j6mKJUmvhHza4R7Oh7V8
I4QXjjlQUgsF5RYj0e3t3hRdO3jfjoOVhK7aUgXVk5273o9/Lv8lN646m75Awutg3pR6Iegcz72HCtDqNd5/kLcQ7gLhUnrGmTak
qwxyhQdMF/8cnAKKq3lRcSvq3pk/nF5uTnlnZ0CNWVt8NuoUhwK88Emf0Q0m3bPBMEV925bkx7+KVAxo3PU9k0Dw/4Z7hoTA5qdl
ChyfXs4FSeOjyHfWtrIEBH0Lk6Rt6hKQzGZEWfk7IcZKZb96ONGGdcULhEMa54T6A+s1CjHlig1QvTyaJkjLB0FVz8EGntJGtBzz
Hp8JceWALr5/Hmvp8DPbBWK97jRUq2NyNuWABtiqE3tZw61e8IINLOlgIU68hJ8LhC0GUTYRlXaEh7PLRVlyA1eyGWrBMNZvzcDo
kZLp7IaMKhetmTsDYxbdGazfCL+MVaUSgGVKi0lYKNNBCyLhi8PVCLeuwkXBbNK9UjtfsWm+5RehFK+0onHvqiSV94d08IySptK9
EvCYQx2Fz8NTjddgoMoeecwYK5R4Jvw19Y0fa/vIbVsPuKbJ9v92+Xv17rS5etcI0M1SPhqUJs2wrMve/BJFHCRnG9H8YpMvZ8RE
VgSmIlDj8VLd7tXp5DkhfkVSpc/HAWJZO7FyVIMQlbetGrRaNR8hunayJbvRd4mVvu5IS5c3WiYpVXcvztJiUxetopcjEjqrzjEd
/HoHnjjeIcTgm76XurxLzqLnKV6pJlo/Os4V8ugQbmDvKryLWRqlAkC5q6TcVfFYP0kEoUe6SI0CUoJ50vFZiZowpp8SwOdwElTO
MPWalIAlNV9HI1irWXkmGBKLfmPXdysnMwAB/0F5ZNTXwWIa8brnYeETveAG+VCOHLGuDJPiqcil1VxVwluY1do21GCpby2opNg6
JpgDUODwJ3SoSRL6r6tlzFh/yRPAfhf9fwSjZfn+JRvRX24GV/qgGF472AoFRAEUaN4b2unGdZDNAC3HQ2MPQ4i5mFRQqfgDfyKL
9VCTBJZdqgLcH/b8svwmWhyXzE2TcT9Ow6dRNL9fx8DTzm7+g/BxVPB9BSM82zqDQqh0CwfkfJYAtjiFYGN/HYiOIlj9a3hbrhTR
W/Aw/7bzDffq+niJlUJFB/KFlmctTer016BxbMebeUBQfXJaRfoMiJwbdLJmzJj9VcY3qLWAGiOQxIz6zJRDRqM08L9H5z7UcHgZ
uAS222YMqCZnrCcFeUqi6glZX8WkagsRJohOPYKULSY7UjeGFO4gfsdjObhVxCF4lv8g+hDuHDWcEXKsl3qWa/TtV5Ptzru3aUsW
qRH6lIy/jpJLoTlw/zIzAVEQOdzqw4kmiJcp+Id7XtKFpfNpxFSFOnwf7hjfG0LuB8rFHXPVLoONAn2bfwwVBH4n7EryRuhfELNx
D4/jvPUMiIf8yHmPs4EM91dHUNhqOXA+FSfluaANyIZ2mWlRAAXCfWrMB50j1dB4W8akVAl2arg8WrP8ioIbVvdUaHIC2jLuiPfU
jpz8+N9Z1nrFnTpvyHJzSfFnLIQb58MmQn1qlDZrMqe0fC7gCeY7ya2MA3EX9Mi8A+ODOHTxqQ7uyh91k0atcqhRHLP+09A2Fhn9
Pmta6x8OrTkDMjRhbIMv/qmgSW38+MglBEE065jsGLwpvGnUHg2Y52j8i9DF3XTQdGorYhhM2LC6Y3kPxBI3rgRFcn6VQfp8AGsC
WLgxVbjfGP4g0OQP39+VgLEAegJrJ6xkcluvpRiQWaUfDlkuqY9tWqjuPMI4sS0U86gIQ9979VImudMsPZCHSVH3Xp2ki3KUPZnZ
6I8dy5kW/+sSvOkcoe0Gu1q4E+RNwzJUYzOgl02iL6XfesMEcaxM3MWA5ra7ommyzhinuAUBs+7yA3tHmAl0Ubcv6KwykBpCDH0k
ioEK5Alv/RSoyfCUQYyMlRlgUSPlcQo3g8RGJF5g8Ogn+faWwTuDSxwpYquiGKpNjZKuRgi2f83w2aIAGslkVxjQkXGl6+qlhJ0s
dREPLzi4aXXayDgcJUbJoHNc89MjEmUlSy/dVsmdwohZRUuWD2IXsA+gn15L9Cd+SPfrd/+iUi9N1FNDz3xTb/kudWQRwpEgPB/B
NHf0/rN3/emQarkSiJbyzgX4/jjMw859WNRwQr8Gs7b3BsSmyhzUgqD1shldFbj0GI9BDRsiDAGNWjVJbo38mdAke89mknQVI1zb
34B+LLGIaPPh+kJbGtdCXiqJluqwu15eWxEzJq9a/RmtF+nWgcYUn3bs87Vgx0uRlupUAItPcuu/DllRsHFewC/Axe+kPsltWxmT
2wvwpq3krFE796NFOuI3gKLYor7gzIhIHd8iCnMcAcchZhp/VoJVpluk9Jyv8GFOk6pORs2N/K4l4yi2xQ7w+GTRwAcKl9laiN7Z
tKbulr71Ft6+6B3rgYu5XWK1QxrK5g52aAq3Xq7nU9ewXTSqkoDhBSbYkdO0j5DNmoHaYMErCwxQCkfbl7ZeLy4cti/d6ImqnW5I
fLZt9WRgavEGDkWGpWg/OqFLJYw11R5m7QVdbrE2wOhqrPoUWS98IhoQIFxUZRaOClQf5cFeDraTNNmFDP+6JV9/n7f/dAcAI+PS
gl7GJvLyKLrtgFbuBc7PJ3SOIuDrCoYLksc/6eaBYWsTPzpUEcCZOVHbfFEhLgrDf2peF0p3XeFjO0hmTFM0uAKbbauKkw8yKCJO
2caNqQhwRx3RBHZCJB/7hOl62oErmJJD2M+xisLuOjN86EL79blNHCsKy3MqBUvH72KXy28p5EWY7O9QY96r8qh3Xhx+xa9mP459
lgQ0Avy3i8YeMc5SXSX/i/NdbnU+G+pYxRPW3sK6l1/lQMzsRincwyXpXOt6nHKOA4w1DgbwGsbiGoTCP66A1Lf1JHjsUpjD/8O2
1ckH0uUxHOInx4sQfGRfiXwGlT+hg8qvgwcBevAwHj+QB3G+hwjwwrNjXDFyxLYkbXlWB88KZZFWA+4tUqJP7A6xSqMxeNTv1RlU
Z74FvFkvstMN16SrLfrrkogPS1Gr0PCDqSPzZrVxAbYZn15rcLPtY/QZz4q6MzPQI5PuwHTC20yauor+pzmwKDE2WRdYEQcRbzEY
DBcgzQBRHTUfLqx7FIoVCUm59KyLim4qiqd+8ycrfJxOkr+gij58nou9wNVs1n5VpFKatEVJZwwazBdec0iUjvwrC99UDu74mKMM
nkIeYx2TU57BiIu8dRTpIbhReNatVCcfAtX/tixbZY/YCGALXTRGN7L+nIqy+U3kLFf76qb0xLm7o64h9CHKrHuOFEpa/J2t11k0
xiLhKysb3HECxC6CH8xYJwBae94MVIUlGXSvjWteNlbH9wJI6uQIFDU+QsSqrUxnkkFJ6gGHD9lmZSgprAMHsDk/fur08TMg+whY
ApdZfHPMApowa9fIx9L51QKP346+qgiO/jVQSo/ggpwNBIZLtK53EoYnRkEASA7zUriR2BUDdLqCiQnVN4TjdKdyOY7QyLNIeF/H
bb7Jk4KMfQGh2LmtWMek3FA3HlUthI5gax8JJXBKZq1EWoX9yzT2l1oyHz/g7lModAA2aLRYydBTbCqHxeco2cn+9IM6tCMAkTrd
nYcLazaKYaIoXr3jCEOLS2Tzr4+SO0OOv2Dho1W2HiZ2jVouaLOrfMs0MljvgHejPM9T66a5AM9k2HUSZlau/A5+gbeLyz7c5AYD
gM+i6vcOOofE8YKuhBqVKOr7PqubWDT0Rxgdg00QHBCexUW+kLQKTN5CoAB/shHdF2Cm42bzeLPe5clQaW0xAM/0Lq9yiWpx66Zc
gxOX1+Yhz6Jvb4LYXU0tbYM1Zhz6D70F9zOgQbZT4moPKOUnQMEVVAT6Os1BBqg3+ONCYBviJvQEZXL6Quwwm1aGNwIP4L77e/3m
1/5TLnuenvnEc3iIP4U8gWaRYaA/Y+tS6H/dwtCwVM8E4MYcGxA3ZmonK85Bwo790tgpYeOuXojx2QEb92tJE8QEUZ4oHF9Yuek9
Pz/kYTRFuFCpSNychJS6D+JMri9d7jR2Lf3dPW6MwzVbcrXzz8HksYIqVZpM1beA3kY7eKhXru1Y2XrT1PancmHoVPOK81r79kXP
0MqyxPfjd5rzMEMGc612GIM2gH/ZHkCT0IqWZoYpwKlBs/hXrKtmQ3h4mLn1jl/WTPyJNowv/1ruilaiEp+leClvBwQfJFZe8j2y
FNvqs3H70yF4/nj0OLyUB+kHubqlUEIvem0+bbMIwnZwNRLjFp0XjzyTNvlkxxZEuV2a0mL6lwgehm4pIVreWLp64wIpRonTXJka
i1DVTWvZxVGVLXe0baUTNV2/RaHEvNQ+fo7nS/EfTtc51vLP+yG4s5vBuIDRDnQoFeIK2Hq+Z8z9IFbbbF+VZtYTKUgmuqhRCC14
PZuiqI+L1EBWuuSVcqFd5gkAEhY1bUos2pA9p7XaGqEkshoilKjf3qtr2HT2c7DExLI7oXYCL0fiEiy8T2hTUm52kTQ303Jlub/c
PtEPPUVhuJuy1v+PMDQHR0Cs/Vr4v0ME8Jlm+qwrqrUMKp/WFzwB302Iim24U75Y18LcU9vpxf6n6XfD+qVl5nvneEDuDx5Wxrda
9ica8ADSunCmoudcADuqGwvf1/bsQ5dkyjifdGB4ADXJ0YeGIIr5Ybc2EzznoGFGqC7RbNsj+/hVOoguVq2EPQwYAtRsj4fo7r9V
Ec7Tg0Q2JnMe7BpS3SsjTeVqypQ1cZrqIIoArKxeyu1FfOFvFb3XsZq6fJPADxL9PzflGhoU4gSL4amNAETO1futCHidR8p7JvOk
jXTUdHPdmsCZjoYKXeL1g9yI1ahQDaP4dExnZT3ULfX/+fx7o4Dzww2JiPXJhTyR5qqXVnFxfFp9iiUUFzJx9y14z5dkB0jDZVo7
BU2+u7G+2nxKv7sWdQBjTxYFyhUEBa5IvuEHt1g9L/5hSC1L3YrUUO27T2Nyubze5QnPpkaB0eEn0ku0MYcNdDH7wIYz4IUsaEGM
sg3pNaeXoguUuPWfdOx6i4CXWS0cVaS01nFXNLfD70CU8Daapw5vSRr9R1289F+YJ86DgPfdTgb4z9ZmJoVd7H7A3ZLxEgeXkExY
cnAfO2XlJ85phsmnQFIrUAsPrxvqLd6JWpSByIqIFLsSFyKA5gGuYoaKzuZp5b4FBGLTw8u9QjuN4U5woncqck8j750gsdmNlKLi
/kAjosOOrzesld7dHYiIecpvIov4JQKeIMsS5uiMyzt7h29tXhuOiivLLtUBHDycOKlj4hinr5EqCi+0oir8dgcNIgFz7iP3w2jc
v31Jg7aVu5kPxOa79moR5XfEGB9a3DNubDXERYREOl1kP/Jl+KrjuAzL5P2WhFegrtNf4Po5Fr6K4DeSIYDuP8+1YxTGhsy9r6VQ
woPPNX/URtoCyKVgmUuyiklR8iXqi8MvpPqMaKhtmzNKmqcCAfF64EZBgCUgUATbNsSmqdfMUmFmsK/QgOZmbMAeRay6DtoIjcSw
FCNMOUQZ2nSUsMtj1gzGZXzbR7rFRDOamjcXBZmBxUefb2mBHCRvlHCfJA18BzOpJ2QIvmDFoHQqwvxSrpUsJtUPLz58orRVzVW8
kNtUN6/VTui/g0Xc8MFeUKUyFAibw+6HBda6bJtZfzq8ut1369RTVIH0trdH7p4X+FnfMO0/YTX8Fn4nAi7SOhjrKQSYLEUlprJK
hUztMmsskNLu19j6XdPt7E1ukQK7HaHhfvuweZErSptjkYkuZy7kWzaKGkB492GiIaBvB0sLpROodlDQm4TKBUcIO5oN80GSvXjD
QRiGNSVXmYnlg0j6a2dPwqY1q02I7bt4IjmB+9dYYiWpUImnzNImn3BcjgJCniTFZW5QUwrWsjbRRvxmIGKEDQHAvZp+Ezsi2Tn7
LFdFOKz4c048SdLNjXhgUO5nQNPv+jbMnooMxnJRNHRp1oqdb8Y45QWsGoLO9C0XdC6H7nvtTzH07wpKh0e45XFbIeC/7+gf3v7L
/23QMKnrv5poWh8q03jKKylV8LLp3Y37gJs1XnNOmLUwDMtjwAPsSuZoj7vbEltkFUfER6028/lRsDq+EN18thRbNmZTO9axW4qY
Wosl7tANvQl14ckrVfVZyO7b/TxOTDyIGYxg2RFnxBwgW9dVzdst7Fja8Gz34YdlcyKvOTpBXY/Iqdf5j06jqXcsWIavMePX4ooe
KsYCwGedG1rYd/YCQzwZ3RBdVidlTaTjOjcr6qmUUqWi03yuWgb0aTdY0TETp+Ya37BklOSvBixP2k4Q305dBepz1BCVo5mra70R
JiRVUzyBKCXYdOXjsfGkWVGWHyGK6N8G+aanO6pRCKfVIgCazJeEZAJUr4oyR/9DrWfLGtZjukfU4y5Sy3L7g25jfNGCkt57VgXO
CrE3AXVmCsx2l9LRYNOc7vLe5XDzUXkONZPHVjwibGK6KxZoSHzTIx2TiM2DXzMeIICG15LofqCMooDnhEINbw7Gpp9yLWPFzdnA
QxPeTE8OqVTE4k3oN0V9+JUOQn1A/GQt+xxKesB3cNj4gx2Zvtz3FHU4GWocp3+MSWp/MrUZngQwMG2fo9NFvXTEFeUwVOwdSgT6
QmEaumOS1NyNwZNgwMQQ7eZ3qJ6FLzIm4W85ZTZqDFBOKBdNlzoDeoyzxp8cXnO89sqNeAOaOCz1fVUB4BjfuKMMN5ulzShnfmSH
IhJ0lO4HVF1d1U34zA8kQ9p33QLN6QnMZtGdGSfai6HwrCu2aGgEhXE0ZEz1D+cMGihLw+d9pwhHHXLQ80xYAIPSrreyI5sUpsHW
Qnye0bN1mDup0gsah4Rk7L9AlesD+cOncdMqgNpQEfZOmcIcHr+j4ZoSHHXLQt9SnIkSnTjPZZ7LkUonGQ8/Op85uSlgzsUR7YK5
81WjVc+To6/LPbjO5kmfXiy7J7TzxZhcyLvcc2bo/WqkR6ZURguxuNoyNsj3Xz2/1RezQAoJraybQNNOHgEf3jlJ8l7RI7S7GfnJ
+P9VbPkHyW9DMZ532MeHbL+naWOwngjtqBck+H0He3me6RbNioziHPN0Q6ltwnxlx7rIsw7ZeI7qLQDNWFkG9jrLgiX3mUtwpdXf
J4beGhLs4vHsYZck2sLeTw7dY6soxrrRSvSgxHWXxPohClF1KG+VrOpNUmuLI73iKZYJ8Lc4FZSA6h2doVWsWuM25rHWzTZW5AMr
WO02KkmqACbkg04oIshrGuJsXc0KjtLkccvtbXfNp4jWFJxXPIiQanKPXfipvimtMUotGvrAExvvbzvZTAYYOhDIXy9iYRB1WCtg
zJ2ykVfTKLtgCDnpAeqlJBMCiTeSNoUMIR8TlPaDS8f6IWqWKrlFA81UsUhjIOJSQLsrciCyZirl4QvwmBN5lugItKYCsLFo51XN
IwOpxInBED9kscpKuyJA8gQq62bdIONIOk0EL/kgmQMxgEgOuS+Il3bWanIG7AvJRFQVxmyuWSxURTONaObQu+CgfDArZxF60SzK
YXbuqJZUFP6d8xmPBdQVsMPwxaU0vSv3eWcedxXuqtPwP7cKnN76hK+Whrrqumb+KgBqhkP2X/DDWkMyPJhKfgUqQVm9Rglw9W60
xqTYQK/9i4xl4yBubWwJxEXjnn2kZX9ooADLaq5OkWbJLIiynhT32/Ha935S2YUXilyg2HvopU1z1cke8EN/jr7yoBRxLjFsfyq8
+c1wcjqa/batHUNFIK5hx9k7gWl92m4S9n/Xmsq2fs4KQT1FeFu3sMYv6Y4Sh3thvRgoA3nmOZyBAEQuOm8aPG5/NXfbe1Z4qKrw
TiLfTL5FTuIocfvo2lk5bX2xZcJxhC0eeXsczb+0SZobfkbI7y56x0Pv/nkT+lKbOx/HTLxKAGPviiyLzgGN9hXNDODWbqo8lx8/
Ho6frbr2Vyko/VhhlkVklRylbViCMlPQNo7w85pDNohfSH3BWuKRMHjzyq1tVtngcTKaweP556y0hAVLrYqcJaQX704J/m0YlsEJ
d8a9uP9lyE/FHp/O7s0RK+0KuAVYCdmzraaV+YvN6/HZSc4yW1DVxB67+cWwa6abE0LJK3sARrl4mn70u6J8cVmrmVvjBL1dQUqc
ym5XHaPEmI0ZyiZ1yjT83iuLxJymWP89bIuKP/MzeCNo+nYoENBpypDvQfAOvWa50kydr/uWFRQFOpqIc4QNu9qvPePYMLNqt8YA
2Go9KMUG2I+I6tpdiZD8CDL+Bx9BYEL74Wf3Fm9sxqINmvahMjvINknZguz9mJOysYeVPYLYwDUcmCnWwZDbdipHNlhiqtKdfCWV
pxr+QqJoNQdL8PoJihIcJjJUnSDt2grwwiudPnfa2uCvoo4Ttebb9xx35YuPtuCSlZZqCXO6EuSD04D8c7E90H5sB+3ZAWQ9D71C
EsLJFtLDe1UZsCYeyGa8IMiUU/DMiXNT9muHJWejQobeS6nOdV4yYUA4M3XiYqXiaCFZGVd4096CKrQTu08ePvrojKbAf2pdxcZI
4HOHuLMp5ZmgB82mdOhZ9D0VdhnW5gQB9XYgO9UsBfWlheE70Y3zWTZqIFwMDD62dQr+EotEMMd6FYrLKArV/YCpxwZRzG8CC5lq
Bzm79b1oEC61y3AXuMP5hvH+PBAJQgX3IY3nY6hBUkWP2/WtpHqCxi6XRg0fB+Nna1M4dBZZOBiy6x43+8/NRV+h2JwbGg6wvXLB
Y8g0T2i/XSScBgh/nTJXqHjk4abiWZQ/lyo8Xf6JwhyLeTuTPu//Hvq3TDMY0/vGz/VPCgl15qS9IBvrFCLYIYlPsn/eQrKZFiYh
oovjL1uOLXt74Hlcd2ofAs44vsYeskX19zA3gXgVTMb3osS93ypOZ3MIKo96Dte6/+hpHq5Ynw1Jjijb4kUhAnwgO2CHpMMKLulp
vGUobALF9PEkyAT4Z/6agmE+fvZ/tKeyURmRZ/+eNtbt9SWEvm7Tn6ok2YBEIIuM/9dbFnJ1btWTcR9Lh5fei/i4Zmb4qnYkGhdN
TPTiXdfKBwgUdHyVhLV9cy5VHX8DBvo3Z+LWCN8NUHFFWntw+yGtskB2OoGV8GDV3SHSirYMcGaHzzp/6I0fLseXQ6tNCxkscJsj
RBfU3UZnt1jvJBBWr6ZagqdHuqW46So2sqwsgiMUY54/m4+HEBL+aVdGQ4QAUcDH/ny1+kCAsUJTppnLYDdELpyL0LggoQscv+ZW
nNuKj2lBvGpz8tpjeKUWfgWtidUW/ia0VyA9eS1ux8NzNGqAPCZN6iSHDmu6+qH08z5grLGNkTT21aKNoSAU5GFMOEAwVnSjQTfS
BmzjQqfY6dfIbRBEWjfm25sl13k/cEREL/d0L6jP6NUT8+h9BeiAmNAdpTg//JnwoKO6rjoWRAzzf8whW1nX5F6HIGsfkB+HxY92
6tBCmSwp8ZkcKQoFKuKW+c8OvFl+sSHff05bK1yCNIBGTz85IUSeTuSq3OcJXBJS9GCEvXbaDlHH7m2qh7VgeUnmO0WdzqyTIBC4
BSTci3gFiBqCXjR3K6PrspHAg36csufDD2vrv8EAeGVN5GdcjRsu4YoCs5HdphE+Z9hhF+p3dZ2VJjIrcpvM8ZfUXYUYAdHm6jac
DqJyUItRpV4cgQEDe4lqtlYit5vbi/d0eCWGJ3c2zS9HNAhXxoUPauYKYlocOW2rETK6A8mUKEBMvVs9NRik8iNLXPMd/eYx8BvK
m49GkKz+UpYX0d5/JVE4veJ/0Nkulp5rje+lLPgr7JVD7WDxiaNpK2bsGuP3N7wTBJ4mmQ/yLaocNCxOMsJdcLEpvHHxF0R0Clv8
AUgRlHYqPgzyIQipUqia0ZmKAq2s53GhYkxwOiUGhfV9zeIBR9K4Cq5VixH3qnS3UsgZ8/0safM6nzJgQF27MmioOli5uOnOosX0
h7kfAzYoC5PkQ7ShQQy3D0LL8gf+U73+DeszuVYSfjbcC9g/jM0q+uUZtlIPujDRCW4tfoe4LW8U2wcZHtDTzOl+LMNZsC/vHb+Z
qt/y+XBz2Uh2B++NZ3gw1oNoo/pB3MfNlfKml6YdDqmtU2KOH3pwS5NcmdHwcxWnq5lTb3I9tvKkwSy7ounL3ArhrS0UKDdwAWWd
fw1/KjIYwzgQjmKwBb6Poc9/PwQDkTMxQCNXS5N6/tl0+VPa5yEqTjZTlsFFIe8D9qVk9Uw3qCnr9QJpwJJad5MjTEz3AbCJo2tn
cejA6nbNg3Irdpjg3cHtxo9xspZoboCQHp/0Ia7+lIcieLVu1aj8fRNFJ/1sMEddd7+T6rcKcZIb0iAHcOPOrnH0CQqY8OENoLdH
SKfJmQd1X8TjsPvTwEAFJiJ3EwKLXPGtSMeB8U1YmnMlDPDGrML0tl4Kya+mVif+caUxRjQcQfEIq+SBiN2TDpCVPJPjqD6XuSbz
ntwN4nFBUvTyQLFzcIy8GSTIsfFNw+krzCfJML6mB9jXy0p4Oq81lH/1rsbdHgb2iD/TuwvzfbJwiT/Im/Z9tg3AMUUQ32dFIod4
kwg/XyBZr6FdEdNwe1wzGUHXfjyR3RGkWmw7ZLX+gnXL7w3YxKZKbApZMBI6/HvhMUADzuC5inj/7RE9v5mN92/Z9vcG9JM9pEJx
9pMGchYP3uqM6vvP+zjtmblz+Nrjk6ltbLFqzZm/5cvIbq3DJ2zhNmRrN/kWXxAYXMrSyLRxobiws5GJg9VodCScxW1ia09aMHMd
UIjEk5gzWLN65T60xt5S8c93rUVUmDsvSYrWoWO10mFKxm1Ut07C1ogpqNjIllWwJsZOpv7aQNcFZJc0xnhbqJQVcEVgiEIBCIG6
HvtxBJPRb5wQSBauKFWkH1EpAyPedHFJormZHUMIN36HwwUWaG5TQ45Ra2hhJhSrVXv0dYzE7ogGRXnXj5I7dFgS3CrnaV+SC49v
bfUoQkflG4/LjcNVymZQjv4nTVr0XO2MzlB1SST4pwmy9ABwPCvELaeWBcVARHy10j5cpMP9f0aA3G+9z4vqxF9N1LJz/WwgBh78
3JgHvmwoSVDdApi+FFSb3xGPEpjFeF1ZqncsVKjCs2iXYA2R1SG4Tu5cpd+r+0ccragz+8YHMjtTn/Fkpv+W1MGEYZcbld5ylb2x
/pV7zJ1LHdhe2t6io/OSNL1NF+88VuFWDuMXDs9rfSJi710ILTwmqRk9Mb3jJpmEyeHljAgV6d8OABuPi29IwtNxJqT/zBfSnwcu
x6coSHPgRpbhtfvZbcGQMf4mmlCBM5SNYeWg3jHiElR5ndpxFx9YpOeUgogQyynPt785RQSMeS96f9i51iNK/I8AFCtgnc7tiVdJ
sWSCy4xE3eZP90PKpCUJJ3tGnewweoxgLbZkhLzSvAvoOfJOoz1+VSC3bOJBe6izhsF/2/mSzWDSkQk8WnhT5sO7UPHhQPv4Njp4
mn6lbvJ/E6HKEtma7cMQByRLlFnW6U6uVT9g2W7ynz/NBLcgavnB4pnPxKckHKdIgvG0tz4bi0NYF0BW+b+80ImXOKPBvGnIgaLT
1MxmGzLcv89PGkOk3JlUWFbJDVZ+56i51OdpDb38gJE8b1bCZhJg6qZ2eHc2js+5tg/rDZ14v6KU6beKvoF2PJioVQV4Ppl7MpR1
g2cBgTGJN8fKSoEAnPmCUBSROmmN7S73sXnnfJqthVyFdvvxf4OuByKMIBWfZMKX+piFuc2T4Q4V1MyBYmPqxm3QQDji/KHJshbt
Ukad99i8rvAH59LZXAVaqEj3OWxZ2h04jWYGiv/c2GYnSK7VKjsn0g4GdBw0BWW7lXxfMFgDAlNrpEpehKPcSwZN5EEfxNWJhJqd
ha/8j7BJdSi5DeumhFpCFJLai8PjfWerXaYX5CfSPJdIJ2Bp5htfH5kJ5B4ArVlcblCvRtdz32gvd4ZtenlNYKYfYpuIE5zv59Mr
9vdrvmURSgxnKyfidYkbs1VKgyy+1v7OxWsTvGd0/B3UKMGACLccduOb8ve93hBhdu/OMxCqiSEaMzbXHA5fw+5KCAXu1g06SYJa
X/LWJyW3PDRAU6iAbVMCqt6qVBvLNm3PanS+0rhKUNiqgu/XtmiRNrr1iC0D8guBbt4mUZ/D+lT/v8oeBreDD1JdiXPVKgX4WGVy
Z3oMcx+nVq2jmODCT6RDaKp5fWuX+or7t8EMvWKeSlThII3i+IvkSxCGAe1+tpWWydQaefbcKefreLRpKbkx5ByST9LpaYpYhwL/
wWpYV/F6pTdRqgUKuUJjdeluEq+45oyTqxRLd5SDA6hulzdT/00SFOSDxe4r8c6rdfyAvOaaPXMuvGkDOPQDoly7WMCyIx0PKYpd
5+lOlpECErkEOznUCFDRcKtrRVilo+u9w9FezNa3oLTID2w7Fg2Hv/YY/nFqwe3ybB69UGxm9im/QYpcrsPXQg10gMWPEsqYTjXH
EdKitsRhgg5pex6LRSeldKqv9fYuZ3VrDpFN4FYsRajsIZhGOAgsGR+W0AYfp2woZmCmhyi/Zcjscm/1dBNaUV03d2GC7SI32gy/
oR/QyGoWfOSO43p+QR7ihUzeG119ERNOmNgCMBy9VIPUcQLrWk7fkW1kXFt265FB+IH7rPIcIANesnyJDlPmJzH4zvgvveQKtzF6
CVZVjTjX2Ri7QFVuwY2sDAqbo5LKD+WhPBLYmeuhtodkVE76NYQjJzNdwEabHDWmGqMMdS+nbiFZfRXyQr0dIeUrGOLFPf3laOtf
nYBRl665qR7G63iNcYQjGIcHa/RiTQmBrmZwuadAP4MSKERnStbG0/DrJdkDP0by0swScR6N3pfGV10F0e3q+3ual5WcgvBChX85
FwVoI8IturcGXaqXq6Na9vOr9FVDb6Ldk7tvloW5D6/24NwKzuwgVRRENHVBXe4O0Jhr0iwGwZMmsaQBWEwHHaFOJC4sh6dv+/QX
J773Q0gizRU3h3LHm0IvAgT5ESmrGP50GI3/MSF91Uz6Lpyr2lYXIQI6iZbk8Y4+crEbGqSBUCUndb737Ffkk7Y8l9Yh/FqM/bcR
D5HEdjeyBj6uVMmE6Cw/hIpceBAY1nGftfoWOvKshUTWwFUr2UCyUs6yagNe6sTiA0BeON0iF7H5ANrzXe7b9l0Psu+01Wj1fa4Y
56w6rem8z0t/c75T1QjJhPB9N3gkeENIbzZnhCxpULsK7TXJv76IRJjTLgMqraZBR3BN/TD2IBX4qUG95P5Ek/+9geJUPRS9gTy0
o8LB7pwyNicdE/CjNITymCKoXLeNR7WNomyP6ybs7VrTRE7uHEONOXy6YPISA7lMzQ6ni6baO+CdJhuMzscaip1PybMigB//nXyG
p2N+Z1QymoCWdAJqUJQFw4DlSEEUh7I+pDrupQtuMQUSShFm4tJNYwvIiigETvti2DUwJ63x3KGppZreVtSVXUUQ601BZW8sB2oQ
5uSyvu3f34BVQWcaQVNalu1aysa9d4PMFNkJPxYer2Ln9h2dmeu434IJ3mGooeLwA8fZZ4QIzqmlBIWvWr6bis+MERJK2CKKlgmy
QaOgwk+Wz44gNxBecBGjJ95XzAg07mGRszW2wpIwkNVL5OYdFFM+463POiMgDhiPNKcgPtiKHx2TXE5Cafua0EDcgY+hQ9594fvK
A89JOc8RO38mjkSBu83ZzCbgsdQB3tLlTx+XoqWBwCNpsljpAJxvUU4d6sIStWWoDMONTktBOA0jp+53VUFJYAEtghPF6WnyGBgg
vkwH3+uE38Atw0ypikB2est8DxbHSTLZ1TOaB0JWJdk+mO62H1mmpjJwGNN/jw2IljO7B0UBqOpSBR9n/yvSGmGxFIjLx2gU92ik
gjlxe+GQKDQHx8FW19jXWH3Y5ALKhf1ay7BxfwPs2X2Avn4WXmp24bGyfZFYbeEaFCIbeXHqi3bzuAbnLPK+8As6eQelSRYNq+du
A+w8RgbzGICPzRkI7ozSdvsNFgA0BHnhGQ+U7QVpsOSaYuVTXs60c5L/xffvuDl7FegslKijdfb8huKOzZ7BZoRe8Y+giarcoYm1
TZxX7gglyXktJ8MMW/7RITZAi+bYcrruKkBw9buwYealBY4Q5fl36b46W5kLytTlma3L2gzTPWNX0dkwUfIFIHsPrlvKE1DtdQgL
JaVlkQzhQj3YkAxsWrMyCZs5Og+Gxzvk+sMyFesUlVYTh2rdURPGKnjZkcMZdt+oT5WQmP6rNf8vTDv7rEvB7EpfKoEUuBaNS76g
6mnD+oKlKYtyneIqcblSStturlhrHNcZRAMC033B+36PbWVN8OKH90TRoNgFcWGDoPWzOoOytnClp3XZMWGFgryIxvzW6LnClzVY
s9OcO7t2JlOGupesWl61kIU9Pc5TnXKo5KqTjXYvt4dffOv8ks7eAgP8wWrT0dvdEBHrUX2CK9FKVuB+24QatZM7M27cCk/nWY//
CuEqY718oGvxr5jXXOZehWOUqHOObO2YyWtEUe+r5bm5tfYJ8NbN8tAmkPphKNgbXS1xvybJoH3cuWA5YOkt9B8zEGQVtGBOfHd2
xKQ0o2GlzC5GTT5dDPtcvD+crEH39BWvsMRI8MoyToN2/LvsS6vNmoJaUHAJnOvOGiY3V8IPM0ablnx71B6GwyUUleezIIj2SnFW
8Ya2kcK8sDZQAJ6stLpwGFgDEC/HybP1ouWjbIKNw/eYa6NgFWp3/dljbyvIeTC/NB2O0Kw8PK/4/c8d9eBicr8WSHFa0abJeKFx
Cj4DWbp9OhtRKxFmFiZoq/0PAQo/ba/dThDOu453vmaJQ+zzzB2Z4XV268V1b82V6x9cU6gsq0WrxyyzqcbHBkwHB2YlndQRu6U8
SJzqjyAyTga8QVmg+otrvAAKyzwO8sJv8r9omng4lqsemzNtkUCKBrKqZpVrB/y2dafig9JRQhzsTTNeuau1RRufJrUYSSZqydjr
dOWBR/+NG1KdCHZ85iMhzC6GJxY7UPV3Qw7JGaMvPezTtWg5IEiJ2DWpy322VSM8WWpVZ3LIVGgz/7CrNW1bYYuzLZ8P21ghegxj
gVOzOEGqeCogLwsja31ncvoExulIMsTTTykXsyCbnlJNeLqLgEgOqvHOwBY2Ddf7sIj5t7MYjkEqnJaAUWuupG2PTgdP2vT/vB1c
idC2e5g3xse1Mh1ZAV0yEUi6LLAB4Uo5an1tElR9cIQ33+ErRkueRnHyAU+cGpU92bDTsTRyEQp2dtJwU1FkyXQDFeAnfsfyz7we
9qSdFKAVHYfBengFQs8cH3EhKz5Iirl5kiXCSDB+fZgLEbFhgiLty0m7T+kN1TyxG/S50M2/M3UFAn93PB8YRMAA9f5Tx4RhD6jC
ob+duDy0q/gGYeadOlo2LUZy4+tmhDafwaTgTyy1yEKguQtZ/4IZg+cwz67FGvg6Kb1q7AlfRQQBQbeEik+jPxoj0kugaPK9kGYt
1jTZmK+BrhcZAgAQCy18ERbe9W7IzgKeWWphDzn0bHN3JKAxSKyFtnhow2CiRiBDVZHIntnq3ZMHTonDBxGVVEqsQPSfplktJ91k
OOECbUl3PNK8a9rGDiYWjrGh2GclkYYVTopJSeDfS0AkTWCAFD/gWGFsz2HQBheba9yfuRjoFBjHE9LhFy+ReabjbcnyY+YvOwOX
VPC8GHriWLd7Yo5CrjczsB6mQNHCpVKeDwcG3uJe40c32tou8TFpgm7JXkW+4l+7k5zdEa6I4n1Y6f5r9zpWXxUvNLK0x/9+7OKt
EBCwWwsKGC2uf3jhE+KKGLxTu2q+mvfbv/uznAUtLPJX/Yov7mYieGnJWMAZ56dt4xqR9ovEu5E951D+VKlUCgOzXi56LrnnNxyL
Y8qyo0YgS7YvOS4KvwfvFzGEJsmcXY3qtoHQ6auoJ2i6kpBTc/QMBuPt320g5sTPg2k8xK1LCE+gWvFCR7M25TEoje+pxu59hYA/
vVH7JjMCnQZgoHNOM3NuY8twf7K0k45d4nhSOVq5HNBiFvJnKHZ6ttG4VQ1oEqwYeHnqdgWNMw6LW54czliAIjIc6/UbAAAA27tx
jO4AtyoAAebrAqjiCq9ms62xxGf7AgAAAAAEWVo="""
z=base64.b64decode(''.join(DATA.split()),validate=True)
assert len(z)==46604 and hashlib.sha256(z).hexdigest()=="56cbbceacc4f4d9d5bc8c66e27939d6ada6cdfc47d47ab31716b77f531e972e8"
b=lzma.decompress(z)
assert len(b)==176424 and hashlib.sha256(b).hexdigest()=="9ce25007b880e2f98903ff6edc652b0c92c6e9b9ef1048ae5dcc6648955a2a8e"
d=json.loads(b);assert len(d)==29
out=Path(sys.argv[1] if len(sys.argv)>1 else 'INNER_C622')
assert not out.exists()
for name in d:
 p=Path(name);assert not p.is_absolute() and '..' not in p.parts
out.mkdir(parents=True)
for name,text in d.items():
 p=out/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode())
for name,(size,digest) in json.loads(d['SOURCE_MANIFEST.json']).items():
 b=(out/name).read_bytes();assert len(b)==size and hashlib.sha256(b).hexdigest()==digest
print('INNER_C622_STANDALONE_RECOVERY_PASS',len(d))
```

Для удобства также сохранены самостоятельный декодер (`RECOVER_INNER_C622.py`) и полные исходники, протоколы и receipts (`INNER_C622_COMPLETE_SOURCE_AND_RECEIPTS.zip`). Последний архив149234байта, SHA-2561455cdba1b61bc4f3752b0007bc7591fd7a4bb02d97afb83034af42485a6da06. Они дополняют, а не заменяют буквальную капсулу.

## Наиболее полезное продолжение

Предпочтительным новым малым входом считаю **INNER_ROUTES53_ROOT_TURNOVER**: исходная устойчивая20-гранная пластина сохранена, старый неизбежный апикальный корень действительно удалён, собственная масса и полный комплекс точны, остаются четыреP и одинQ бар при E109. Следующая содержательная задача — совместно перестроить эти полные физические и полярный интерфейсы с действительным изменением массы, а не восстанавливать прежнюю A или оптимизировать один death-выход. Альтернативная консолидация пластины уже показала, что уменьшение числа корней может углубить остаточные ямы; поэтому её дальнейшее использование требует одновременного контроля всех баров и точного зазора свободного материала от максимальной грани. Ни конечная кампания, ни две доказанные условные преграды не исключают более общую внутреннюю конструкцию C<500.
