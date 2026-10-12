# figure-0581

AI research report · 2026-09-27 UTC

---

# Keen Harbor 93 — независимые опоры C434, собственная масса и смена стабильного носителя

## 1. Результат

**Own strict110/additionalweak000 не получен.** Получены новые точно проверенные однородные own211 тела после конечного освобождения нормалей, изменения нормального веера и собственного центра. Масса не заменялась выбранной reference-точкой.

Основной практически удобный вход — **KH93_C434_R82_G6**, V160/E240/F82, C480, own211, additionalweak000, primitivezero000. Все 82 нормали целые на сетке 10^6. Его единственный положительный Q depth приблизительно **0.11600403115840405**, P-баров нет. Это уменьшение Q на **28.80788958568407%** относительно буквального округлённого C434. После удаления только двух точно избыточных опор осталось **три** свободных места до достаточного ограничения F≤85.

Отдельный более низкий по Q, но более дорогой по рёбрам endpoint — **KH93_C434_LOW_FREE_G10**, V166/E249/F85, C498, own211/weak000, Q≈**0.11589613196289336**. В нём весь стабильный треугольник поляра относительно настоящего центра физического тела лежит ниже оставшегося Q death. У него нет гарантированных дополнительных опорных мест, а достаточный запас по смещению центра меньше. Он не заменяет R82_G6 как безусловно лучший вход.

Также точно сохранены рождение третьей S, двухсторонний контроль с настоящим малым P-баром, последующий переход S3→S2 с заменой стабильного носителя7 на53 и конечные трёхопорные усечения уникальной U. Ни один положительный бар не назван нулевым.

**Публикационная замкнутость достигнута:** последняя секция содержит полную автономную recovery capsule со всеми необходимыми исходниками, точными входами и проверяемыми манифестами. Её холодное восстановление всех17 представлений завершилось успешно. Ссылки ниже — дополнительные копии, а не единственный источник новых тел.

## 2. Исходная идентичность и прочитанные зависимости

Использован **J91_REBALANCED_C434_G18**, а не J91_EXACT_CENTER_C434, старый RA40 или KH93_H_LIVE11_G12. Округлённый C434 и точно центрированный companion — разные рациональные тела: у второго центр буквально равен центру C390, у первого отличается на малую ненулевую величину. Выбранный вход имеет SHA-256 `a08ba7b333bd3b3cbf4f2179e8de4242f702f63dddc6f3b6fbec26942f424efe`. Он задан130 точными вершинами C390 и пятью апексами; V135/E217/F84, own211, Q≈0.16294506579914078.

Все шесть файлов нового пакета прочитаны полностью. Извлечены необходимые полные единицы J90/J91. Поставленная полная поправка C452 перезаписала ошибочную копию после извлечения; C434 она не меняет. Для начальных опор восстановлены нужные C390 и округлённый C434, не весь исторический архив. Свободный F84-бюджет уже обоснован в поставленном parent; новым результатом здесь является его фактическое конечное исполнение.

## 3. Точные конечные тела и все положительные бары

В таблице перечислены **все** положительные конечные P/Q depths каждого указанного входа. Десятичные числа — представления точных рациональных величин; полные birth/death/depth восстанавливаются без отсечения. Для всех новых строк additionalweak000 и primitivezero000 проверены точно.

| Точное имя | V/E/F | strict(S,U,H) | Все P depths | Все Q depths |
|---|---:|---:|---|---|
| J91_REBALANCED_C434_G18, parent |135/217/84|(2,1,1)|пусто|0.16294506579914078|
| KH93_C434_FREE11_G10 |162/243/83|(2,1,1)|пусто|0.15604223880313006|
| KH93_C434_FREE179_G8 |160/240/82|(2,1,1)|пусто|0.11621361783075182|
| KH93_C434_R82_G6 |160/240/82|(2,1,1)|пусто|0.11600403115840405|
| KH93_C434_THIRD_S_G10 |162/243/83|(3,1,2)|пусто|0.10302438693069516; 0.008665925998579392|
| KH93_C434_COUPLED_G10 |158/237/81|(2,2,2)|0.0000065944690318997465|0.11616334672494356|
| KH93_C434_TURNOVER_G8 |160/240/82|(2,1,1)|пусто|0.2791564059936442|
| KH93_C434_TURNOVER_DESC_G10 |160/240/82|(2,1,1)|пусто|0.15502076696495964|
| KH93_C434_THICK_LOW_G12 |166/249/85|(2,1,1)|пусто|0.11600403116132926|
| KH93_C434_LOW_FREE_G10 |166/249/85|(2,1,1)|пусто|0.11589613196289336|

Капсула содержит **17 H-входов и17 полных аудитируемых представлений**, включая арифметические companions и промежуточные усечения. Это не17 попарно различных тел: ROBUST_G6 и его очищенное H-представление R82_G6 задают буквально одно тело. В совокупности17 аудитов содержат один положительный P и18 положительных Q.

У R82_G6 стабильны грани7 и18, соответственно шести- и двадцатидвухугольная. Уникальная U — вершина7 точного порядка аудитора; H — ребро[64,104]. Индексы граней и вершин — разные системы. U лежит на опорах13/33/79; родительская U лежала на13/33/57. При сравнении нормальных конусов по исходным меткам опор общими с parent остались82 конуса,53 старых исчезли,78 новых появились. Это не число независимых flips и не сертификат всей численной гомотопии.

**Собственная заполненная масса изменилась:**

| Тело | Объём, приблизительно | Собственный центр, приблизительно |
|---|---:|---|
| R82_G6 |1.712677687303486|(0.02496294275060901, 0.0032163470075184217, −0.006782738122176878)|
| THICK_LOW_G12 |1.712677687294729|(0.02496294275521205, 0.0032163470108027784, −0.00678273812733382)|
| LOW_FREE_G10 |1.7132656359969396|(0.023386357524407427, 0.0020728789563843877, −0.00620781241811685)|
| TURNOVER_DESC_G10 |1.7473545650765254|(0.05083286085421619, 0.0038337100872908136, 0.0031425318168821484)|

Полные рациональные объёмы, первые моменты и центры каждого опубликованного входа вычисляет `diagnostics93.py` в `OWN_MASSES93.json`. Они полностью определены H-данными и точным кодом капсулы. У R82_G6 максимальная битовая длина знаменателя центра16125. Строгий рациональный интервал его Q — `(116004031158404,116004031158405)/10^15`.

## 4. Реально выполненные материальные переходы

### Свободные нормали с живой массой

Использовано H-описание `y_i·x≤1`. Текущие вершины вычисляются как `x_T=Y_T^(-1)·1`, затем заново строятся максимальные многоугольные грани и заполненный объём. Для согласованно ориентированных граничных треугольников:

`W=Σdet(a,b,c)`, `V=W/6`, `g=Σdet(a,b,c)(a+b+c)/(4W)`.

Физические и полярные точки — `p=x−g` и `q_i=y_i/(1−y_i·g)`. Производные проходят через вершины **и собственную массу**. После конечного шага веер перестраивается. Старые U-safe хорды не наследуются автоматически после движения опор.

Начальный generic release воспроизводится из25-го нормального массива PCG64(seed930191) с амплитудой10^-10; полное совпадение binary64 координат с сохранённым release проверено. Первая политика дала19 принятых шагов в22 записанных итерациях; запрошенные80 не объявляются выполненными. Последующий прогон завершил160/160 принятых шагов. FREE179 считает19+160 принятых шагов, включая восстановления запаса, а не179 строго монотонных спусков Q.

После FREE179_G8 выполнено80 итераций с margin=2·10^-5 и начальным радиусом0.005,69 принятых. G6/G8 freezes — разные точные тела. Из G6 удалены только исходные строки80/82, точно избыточные. Повторное исчерпывающее перечисление подтвердило равенство вершин, объёма, центра, максимальных граней, рёбер и рациональных значений баров.

### Рождение третьей S и смена носителя

В отдельном ответвлении разрешена третья S. После120 принятых шагов получен THIRD_S_G10: уменьшенный основной Q оплачивается вторым настоящим Q и третьей стабильной гранью53. Это не улучшенный own211.

Затем применён двухкорневой полярный лес, разрешающий текущий дальний корень и опору53, но уже не освобождающий прежнюю опору7 от выходящего свидетельства. Отрицательные промежуточные дуги разрешены только при номинации. Положительная хорда `q_i·(q_j−q_i)>0` строго увеличивает квадрат радиуса, исключая циклы.

За21 принятый шаг получен TURNOVER_G8 с настоящими S18/53 и одной U. Это подтверждённое уменьшение S3→S2 и смена носителя, **не отмена последнего бассейна**: Q вырос до0.2791564059936442. Последующий180-шаговый спуск дал TURNOVER_DESC_G10 с Q≈0.15502076696495964 и другим оставшимся седловым носителем — полярным ребром59–61 вместо43–55.

Двухстороннее разрешение двух P- и двух Q-корней с целью `ΣQ+10ΣP` дало COUPLED_G10. Его дополнительный P≈6.59·10^-6 реален. Это контроль данной политики, не исключение других двухсторонних путей.

## 5. Точный запас и низкий полярный носитель

### Достаточный куб на неизменной поверхности

Для положительной физической хорды числитель `w_ij(g)=(v_i−g)·(v_j−v_i)` аффинен по центру. Знак сохраняется при `|d|∞<w_ij/|v_j−v_i|₁`.

Для опор `n_i·x≤h_i` полярный числитель

`L_ij(g)=(n_i·n_j)(h_i−n_i·g)−|n_i|²(h_j−n_j·g)`

имеет коэффициент `B_ij=|n_i|²n_j−(n_i·n_j)n_i`. Положительные свидетели всех не-S граней, отрицательные исходящие знаки обеих S и положительные расстояния до опор дают точный достаточный куб. Численно выбирались лишь свидетели; каждый знак и каждая граница проверены рационально.

У R82_G6 достаточные открытые границы U1≈7.493732680351959·10^-6 и S2≈5.756078024930828·10^-6. **Весь замкнутый куб `|d|∞≤1/262144` сохраняет U1 без слабых U и S2 без слабых S.** Для того же типа сертификата у округлённого parent получен радиус1/549755813888. Отношение конкретных радиусов2^21 — не отношение максимальных камер и не материальная компенсационная ёмкость. При движении поверхности этот сертификат не наследуется. Полный endpoint census, включая H/weakH, проверен отдельно.

THICK_LOW_G12 сохраняет замкнутый радиус1/262144. LOW_FREE_G10 — только1/33554432. Поэтому дальнейшее уменьшение Q сопровождается потерей запаса.

### Три усечения уникальной U

У R82_G6 стабильный полярный треугольник соответствует физической U на опорах13/33/79. Его угловые квадраты радиусов≈2.67319023,3.25083912,2.96970239 превышают Q death≈2.488035025883449.

В `low_carrier93.py` последовательно заменены все три угла. При текущем **настоящем** центре g, физической U с центрированным вектором p и полярном угле c:

`f=p/|p|²`, `δ=1−|f|²`, `r=|c−f|²`, `λ=δ/[2(r+δ)]`,

`q_new=(1−λ)f+λc+βf`, `y_new=q_new/(1+q_new·g)`.

Использованы β=10^-8,10^-12,10^-16 и точное ties-to-even округление только новой нормали на10^22. Старые нормали сохраняются буквально. Каждый шаг использует новый интегрированный центр и проходит полный точный аудит. Получено LOW3_G22,166/249/85, со стабильным полярным треугольником82/83/84. Квадраты его угловых радиусов≈0.4683789696924993,0.46536351084197514,0.4667297005398785 строго ниже нового Q death. Выпуклость квадрата нормы даёт утверждение для **всего треугольника**.

Начальная попытка одинакового β=10^-8 на первых двух шагах и сетки10^12 не сохранила требуемый промежуточный носитель. Оба тела точно own211, но утверждение о последовательной замене углов не прошло. Они сохранены как LOW1_G12/LOW2_G12, а не объявлены правильным трёхшаговым носителем.

Три новые нормали затем умножены на10001/10000 и заморожены на10^12, старые82 строки неизменны. У THICK_LOW_G12 относительно R82 объём изменился на≈−8.757074926995141·10^-12, центр — на `(4.603039973644596·10^-12,3.2843567165205244·10^-12,−5.1569418536375585·10^-12)`. Это не нули. Own census211/weak000 и низкий полярный носитель сохранились.

Дальнейший свободный проход сохранён после110 наблюдённых итераций,109 принятых; запрошенные140 не объявляются завершёнными. Его точный LOW_FREE_G10 сохраняет низкий носитель и даёт Q≈0.11589613196289336.

## 6. Буквальный компактный геометрический вход

Полный файл `KH93_C434_R82_G6.txt`:1888 байт, SHA-256 `9765712b5ffaa464ed4d677974256294c6d867b77fe77b930d166853f66a92a7`. Каждая тройка задаёт `n·x≤1000000`.

```text
82 1000000
-725174 1362065 699290
-876644 1271151 690615
-1099310 1231174 294886
-817964 1365431 563226
-1081003 1264128 151488
-621649 1353152 816931
-910427 1348627 429305
-518139 1328018 931336
-1150535 1200456 6778
-1020626 1165129 671462
-1000361 1313225 295844
-1194316 1138885 290932
-1092629 1226455 -152925
-1154723 1038071 651530
-1018232 1244394 -303529
-826413 1255634 -573231
-413284 1274995 1033847
-712036 1248759 -690383
-565903 -2054257 -854847
-307427 1210004 1127958
-587643 1233564 -794247
-200527 1134456 1212109
-455233 1210233 -883762
-928979 1254154 -443961
-92885 1049729 1285004
-316806 1179053 -958168
-193819 -1291659 -912554
18238 952579 1348058
-174313 1140389 -1016977
-5177 -1016438 -923390
126983 847597 1397922
-11369 1085575 -1065309
231228 735671 1434828
330275 -1762331 162369
151779 1022336 -1093263
30004 1300793 -698627
219511 -659625 -911359
322219 610162 1464118
1094885 47914 75899
412797 485892 1476567
312873 951248 -1101019
394488 -437948 -877153
372181 573535 -1047196
751040 -363347 1338736
494318 358585 1477376
482341 -441422 -830169
502322 597143 -1020344
986434 79237 -460427
565401 225769 1467982
1050351 419486 112141
1083749 -76462 20200
570962 315730 -946952
315382 1317869 -337108
631111 96499 1445527
618364 -68927 -830846
685954 -34720 1413641
769199 -342229 -602838
779840 -1029259 1003128
816852 -402173 -515337
803000 -801799 1145327
813560 70446 -729507
796119 -578783 1253080
873889 -555249 -338841
940788 -543762 -95731
905170 -119352 -513537
748587 944500 20227
956411 -355836 -265735
889363 454940 -604392
917283 703683 114724
1033644 -185828 -146671
1044375 -230785 26003
1003015 537275 125496
1077079 104258 162986
1081632 235703 135814
1081426 316201 94169
570808 -432037 -763436
714032 -374886 -651118
654625 -473702 -663065
648347 -407882 -703531
589983 -1511107 549377
727139 -1270183 798804
579789 -1442685 583018
```

Полный аудит115507 байт, SHA-256 `e97d7d38f144ef72d22af89b43caa4069992851b771a7f7cc9125f581d1d9d44`.

Для THICK_LOW_G12 умножить эти82 тройки на10^6, заменить заголовок на `85 1000000000000` и добавить ровно:

```text
-480844644026 -160273790520 475858784753
-345759387308 -413844418278 432109208393
-316040533149 -402620500776 465219326806
```

Все остальные входы также целиком включены в следующую капсулу.

## 7. Проверка, исполненные границы и продолжение

Поставленный C++17/GMP движок исчерпывающе перечисляет пересечения опор, выдаёт конические сертификаты ограниченности для ±координатных направлений, проверяет настоящие максимальные грани/рёбра, замкнутую ориентированную границу и Euler. Затем интегрирует массу, повторяет положительное тетраэдральное интегрирование, считает все строгие и дополнительные слабые S/U/H, все положительные P/Q и сопоставляет локальные корни с глобальными знаками. Положительного bar-floor в точном движке нет. Это не новая независимая реализация всей физики.

Номинация: Python3.13.5, NumPy2.3.5, SciPy1.17.0, Torch2.10.0+cpu, float64, один поток. Её порог баров10^-14 не используется как доказательство отсутствия меньших баров. Все параметры, остановки, точные binary64 checkpoints и полные runnable units находятся в капсуле. Переносимость каждого пути плавающего оптимизатора не предполагается: прямой exact replay использует замороженные точные входы и оптимизатор не запускает.

Сохранить последний Python-блок как `RECOVER_KH93_C434_CORE.py`:

```bash
python -B -S RECOVER_KH93_C434_CORE.py KH93_C434_RECOVERED
cd KH93_C434_RECOVERED
python -B -S replay93.py
```

Нужны Python standard library, C++17, GMP/GMPXX. Assertions включены; `-DNDEBUG` недопустим. `replay_parent93.py` отдельно восстанавливает округлённый C434 и исходный центр. `nominate_chosen93.py` содержит producing commands выбранных линий.

**Наблюдённые конечные маркеры холодного восстановления:**

```text
KH93_C434_SOURCE_RECOVERY_PASS 47 168569 be552041df6afda1c54a45465859faab7baeaa1ad645753a135eff6ce3108d69
EXACT_COMPLETE_OWN_MASSES_AND_LOW_CARRIER_DIAGNOSTICS_PASS 17
KH93_C434_COMPLETE_EXACT_RECOVERY_PASS_NO_OWN110 17
```

Decoder57653 байт, SHA-256 `311b760aa0dc02141dd54a85ef45017f5d7c5b93ef2324f8ffb18fa199ab60da`. Декодированный canonical dictionary168569 байт, SHA-256 `be552041df6afda1c54a45465859faab7baeaa1ad645753a135eff6ce3108d69`,47 единиц вместе с манифестом. Внутри — полный byte/SHA manifest исходников, входов и ожидаемых аудитных выходов. Полные массы, все вершины, максимальные грани, рёбра и рациональные бары восстанавливаются из этих данных, а не оставлены только за ссылками.

Следующий механизм: конечная перестройка всего текущего Q-прохода43–55 либо альтернативного59–61 с повторным установлением собственной U1. R82 имеет три дополнительных опорных места и большой проверенный запас. THICK_LOW/LOW_FREE имеют физически отделённый низкий полярный носитель, но F85: там дополнительные произвольные опоры требуют предварительной действительной замены/удаления существующих. Ни остановка численной политики, ни смена одной метки, ни малый суррогатный штраф не являются исключением семейства или отменой бассейна.

Пример непосредственно исполнимой номинации:

```bash
python warmstart93.py KH93_C434_R82_G6.txt NEXT_H.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python free93.py NEXT_H.json NEXT_H_FLOW --steps 200 --margin 1e-6 --radius .005
```

Дополнительный полный handoff (`KH93_C434_RESULT.json`) · Архив исходников, входов, аудитных выходов и наблюдений (`KH93_C434_RESEARCH.zip`) · Отдельная копия decoder (`RECOVER_KH93_C434_CORE.py`).

## 8. Полная автономная recovery capsule

```python
"""Complete KH93 C434 exact and producing-source recovery. Standard library."""
import base64,lzma,json,hashlib,sys
from pathlib import Path
DATA = r'''
{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;*xl;j9madh=gRq8X-LBw<fPc2D+HM?3*byC(fz>o$fOuyGp6Za~S7_Kf7dmgzO=inoq5sq=o&uAlGJtrA!)G;a0Ol
1-j|N{~({Swv#8LppDt~S3WJ)s-$qOugt)5_YB|Q_dRlV4f<VE3A<9MC%V06v>AgF-zRTunaRB~HT(=;+@k06xeDX;u$v$0gSAtNF6y8yfqghe=AbVLbm{F)
@=0IZkp~cs@`~K*h5*tqsDvjDdhyV*J{lsik}nU6&>oUPYwPcz2?)kmo_*L&<;6<q%Q&ZfEAu%++VvLQ?0320^mSjiuno#5YLhNk2%uudluEc0)VcWQncW*S
SUgEL;}fYOBD|sL<j0U%F(@;kITs&y-}>dYXx^=H*-gt!nkPC`3lb_L*y<H>*u2kp`#JJF8*-W}?>pS-F-kc1iSsaxF;vA|SELIO(d!McF7BZ4FOlVFkr?+d
(F4Q}-6Wv$m-Ym{xf@AGz_`kr*483vt_*dk1mGBF24!714$0#Cq@Wp@<UgOx3VB$kv^r-Za>im%g$w;+?+14m@?Mvj&(Caz#rbK`P6E^W-q#xyFXJ<_H#Dd7
_(@NQjn2#~HKH*Ql%b|PA0fCOc)Ha*#Tidw5X!NA^EK%4R`R;0#Xzs+!;?n!p|tA|^lQd3nO7wJh=9yy<S}Sy_MQ9<)qMCyIEi3Ji^E2mm%+49Qov#bc9xl^
1)B-NWOC_xJ2}gk9%PX91;RhhQYF%*hVq<m35_#xPnO8Hv)O^k-pwmzlpRnwx|&vwHo|_3;ADZ%DQmBRYzUtAkyTPZ7&tP%tekaC(!s7?qK6=%!Kkz=xLE`R
Et1(JlNmjlyupwK7S?U93FO)C!U1ZVmd$(U4Ixz5us%hM)0NTw7mYPherl&<-ILO+F<db|oN1wn7`@0HWiFM=!Rq--0!O@NiKH^vYoc(?x3{JBppIz4j5Bgr
Yx$$AbKHyQksK)&&$w?d+$)%37iG%);o*?pg~)<*vjb|}O5Co;7@luP=`bEMG!ozFgAt@pqg-#a;)=UJu}`*Y{G&8}{_}vW4t=$hW8zv_Z(dHeX?SocHZSvm
kpG~wW~W9dHg^g-7`PaEgJALBvXL(K5xR8-Z{0>H#dIx^tnF>c5iUh8#|t=b8vy)ypH?`StjLCekz;75#;c6vIs!d@z+=6SzYW|0FEbMllQq?iGMnMhM~*A=
=sH3biSX+0w#L{)<s7i~Qd|w?MCHF6%Nf!hY0A4(i5+V%27$IpMwTCQK`nTNGqZe@(V5^55Stt4hb3j7k{}`R)7f-^RqY1MF>OjqXi~h#7#>;GuXZY&b$O)~
BBoD=)75a@HXzu}{B73gWyB=j6#(?R0deXAmcl(f4^bX>Sd>BjQzY5DIltxRz(hOS<A3E+OL|=6&3y@s?rgebVhhai@&>0h^ytTn?ATMEY`XqtckmzbRtDJy
bZyYu&*GQ=pzy~VrYfembwGJ#Pi1t_WS<Z7cn-f8hO6bOe-#+ReY}?`1Ax)As|#GrGFLKBUHk{=Q^@W=kk24h+~e2WS#wxJmtJrq9<Hd<L8n1ZQMOR33CT`)
h(y9IYob|c;Uw0b?8qL{`Sh+`<hY%CX7127?0B7>Ra}!^AR6AF2!Yyms);v%aU@)@Mnb^MS!NiHiKk~A?1OQ*8a`#tCFxyra;o{kz^ktzILf}?W>!0Au%szL
W6U=QCk-IGZ|+{MI7HH|y7AN>5P($;ijjdgo0;iJD}mG!aM`@f$vGLtiF>!J!rj>}xzP9d8_#oi95&bUECC?^tXXXb`y^o4u=v0uh@vkMG$+9JZQ!+>S(5P>
&Xji`=LNS&B>b<j4SK}aokJ{Bc(MVLqz*2Jf3cMs>SROnUy~6ijQF4;(vh^~TIjn)sd0Q6yyxUU-fB}u#6Yi&#x>pUq#^aD)&)CO3N67qwFSeptjTwW03C0-
6~2Rv_Hr}|RSaF<BR+%eBjs42&Kp1qd0Jj?sUpVQQ@j;B$O%{*x3kztfbeO`vW*NsHx83662YGrSA{TUk%~VdBKBhId#VslIwcy@__t$tf<qPCq8si+R2Y2}
xOwSRRWkP59bHUN5-;iCEXOgseM$Xs+I;c!vLq*ib<0|HkPrJRS{|(LTpgh8^^2b@b43E0BkrolvxBhPEYi628qXzjHzwjdwPEpIWG29;6#Gko52>jY4-UaX
`be9*1~*mb5h#W?Jpo)BKrS#sSHNNDJH^2B4N)QhWfEW<wV=Uxy^T<!`YL408gL`xepCd#q?LI!)57P10=?~n&TV4Cwh4uUKoSG4uLHETB@__U&)B&sbnePO
RttX-%pJALQD6=Kp6<%uWPzENnt$g$s+qfYjTv$NwUUjzS^#*vH_GK+KDnf;|9euby(e$P(43EhR^TNPkuLIj``jd->ECM{MGt_;=`z{yG+4Dho1!!n3?|7j
|19_-9<o}9;jp7i?}ua-#T6^MknDqfS7o)rI<1Hm!&tIIJMXj5y4>eg1TI4Vh*}YLQk{;QW8BFSB=yc9HG@Vx^u6y)v!S*Ri>Ues&kvoJBF|`an(}Bj+4vbC
&tUa|^t3#zeR`P~7Eo9*G4wy(GWDcZM}LmRgPNCxBikjK<a8o(!9~Dm>IV-LFJ7NhL!_ru0aORM4gR9FRJ;PEVfO4oRwoy0`+p$xG*w1$LDU`U%sQLZ5M#(y
1|gr5{^<m&V*93yyNwuQYihq2q@(#!yQRmUuIngvj5b<NQz5vm9<GIQ7|DS8_p7amff^R1x-d+(NMPXM+)p~%u`ZSFbL@!o3F!f6O${{DJ$IZC85)-d$LlNl
Ujg6c0Lc!~1*8!Xu2mvVnwu7NRTU62V3WKS%<7iAo~<(-k{DLE$Q4Cwh*W3JKlr6yngsXyFiGM<HWoUmU5NfscQX|$t3Bx`N?l{nWmb`u4^!*-7BTaL8XULM
zmk94uB>tYS0d}@S;_T->_0#*nZMW2sy9pry1JW(Bmt?dQmxwV+=fodJ4Uproz&q}PT{XSO)U*7lx0gGh$gpospv+Q)rq&l+veNm&!fitG0^KQeOQFDa#=tM
Io8Qm_*&cc$o#xn@E%g6pvYZIR)zUo$M7m00K#6GF1%dEY2lqm_YRo<af7K;*a20{f}yK#%K2N-0ZT@~!JA;fJ2}JUT0R6@dmQ%8peJCF05)Kqy@(V9@~A`a
jf4g4CoxP-%WXxNBP8#%&G^M&p7*F0gN4HqFL}xSEeLG<F3X8y2z&ZDzeQ);U?|<92noHTbEnjTn{`9+3qfH|1D?}-=Gt~kr`oL733E18th^=SwptUP#Z3`p
JU0zu{Ps(oCh$<ItEYH%Rsu!6aH*W;sYmleG7Ac}+;C_treLv33El{(a9Z7?9tW>%`;}(eO(a{agFbN-vmf(aBqqr?=rU`B;!eM8^!J!p<JXI#Bt=8XCDSn)
GP3%*N$&R+y~>8nx;T&l8cHjYs$$`bkBKf{-mELUY#!X5v0vB)KTbF#DZ$-nb0M$pfOKAa;j2H<a&DTP$Wd0OlZ^@7_}x*0Qqc?VZZtv6Tnpspb*~(sPU<E6
q$_;AH-sES<v9K5XM&n}6}Vbuqa}zk`kE-_^O3$PJvC(OX}^xLA|E;an9|gQYYV#Ss4)eQ0IQH!A$tJ$5>yu33hXvSrq#V3bx^-9+S&>9?N?Zc2T}B&Z&F37
G)XmLt-7XZFJ#J~znV2gnKk{u>f>MXSt!B&iwDHi{NAhLro9dqIN5%x){*?~rl4k54MO>UVJ<J}Tr|52%uNF_Cg{BK2zkD%nTm5y@<NlIC2Ff(N1xoHP$Gy2
IA>vT%2$>>G!g-W&u1c_974G@RdKz*GM3ZUqem1NiO?xx)=57GS0uYlO#|d!iM^u3{fS@FU=k$<u=%Vv5k?v30x5bs9CJG+Z(-ogRzt4}I}f0w$iyB|nRHq?
zB}991up{iX(YC<EyYgV^x!@r?98qP8f(jXKfdk+Cx|IjninL3@nf-Q-YQNA=41Kkot&W}R&Jj$NOUy8mzry;J%Z9+B50!$OR|yV*?aBGI=_$lqa$>yw@fX4
`IjYy6EnuHS)GEp;rUl&yVqY)L@ok~s<66Sgd*^>JYqBrr~!0X*CucCte`h250E!Iuk;S7sYHl_yZ<rM#?ZimB<DK3TopQS2lzf2kVPTgHv=_84M_3^Stz-L
aVgI*KL}QW>@O)K{0F?O9umgl=$x=?&#)Z;`w9jg)xsju9l?3Jy?X(ivv!W&hGRK1@k>sIw6oh@jeIjPY+yp><noE<^sm&jQ-0#8k9mU<pbuiB^pd0UFVA`&
3fiPvibu~EWWzc<{UQhi50+q~$@uPzEx=fK2U$8uE?*g{HSponU30NpoKaGr**L$i@NjTnj8ewmOo_LOgoIlN;Z1|TvanZ}r(-D0*qgw67|alb$@O^dGw^Or
1i`}!Nd-v+cV>*}&)KncGKSKb*`6sMkl2@z-VdMmcytg?CJfmk(pF~VK8r$xXi=;CjYf38q9HoQ%w~_=&OH6S!XS)e>SvrmZ3i?d^V2IAe75bEx>#k-!q2I@
;+C^NY)m;RBiY<WHRb-eh1~1%aC`aG6)V#GaQbX$_B^tqxf(Y=+vcVmvi{!b018K>yudq2X(diJT3CSZVtOs0?9aCQM<5)CYS6OU>n*qJv-IL}gIWn?gs%14
rY8q2kjV0V0;D&fG1;&s8&k4EH?7^L{wQHU+#VNSdSZ^&dnp@$2K2^8ySM~S@PAk8UYNb^<hxxZ+dZBLY|Z8N!)gdB8qW_1V8(xQU(52t+83Ay$Y#2N=AzQ2
m=GSuElI5_ZE0yM0Y`!AxkU`v-p!Uz`w8_bJq#pM=Gh)8<Y$lq!_U%(s+2284IJJrDx^}~jD<fJJHAqWd<VDhW)AS;w#1g?6F_y2(t$uJ$_{V4K1j3-VM!Ro
%|0i!prEFk4gxIeXDKLVP+H{cWSI{f5;YsxHB_f)m+(x-BB3h!@!dgKzpHATV0UOXD|T=Hl})cm2+$fxC;&1`Rs!Ri+c^!OdY;>8;BWn;O~SV@tO_v)%GBu}
6#4YLIU2H$IDK%A%J|qESO>?4*Udq92e##|_mYJ*?pe^uL(G@^c}s!2OPd)}z1i#Ck8s`VW*6Cr;P-Z%OM!}XXV|Opy9IbkZO*=fY|6Q5?(rtiDJJ9kPB%RD
8;O77d&l9^Ir@4a&7wgWSc)_?4T>%LtRLW!DCB20!mdKL7Z$?t704EznQDGN_GKif;)w7DSLJW+IHr<MvckUTsz4Yvoa2I{N4HPe=XU|c$GKzhhGJ^+Zcc?z
YP!4E3?^0O*&Whw$@%^BTK}o{Mf>TgJ?m?QUWL!I%Rhg?CFM@}R+G`g=1FeJhnY!_p8ao7Ky0a@j%=S6be<agYG(HR_~eeG3d(xf{1UFio*XHbZwkdYeFv&K
8EzC@lNGfiGQlGGR%kbemxO7!_wNgBpdq{}P%J{wx%XdaaWvS{^g4{=$S}g6<BfzP?erR=npJ$DZC?rQm5Bkd2Vj!h^Mn!9vFexaoSo>0@oYq>Wft5JSPS|<
C!^O=(DyZ2bS-wH7x+kV5535n`2JI7R(&oc?DNxG9VEDUddx)JNM;nzdNar7;JsISRmP>Z?7ZGcbL#5i=r@pD7<*P%Hq2_m8&ff)kSbX#JG9~TuY;^T<aKKM
1F$PLE%?(}F)%SO3;`;OY`1@!sD1<lka+PgINsj$GG&liDz=&33w9UFB%iZlZwIKzyFdO~M>i@J+g(cqroK5AY{iBa^G6!O<jahqAa$^HBK~JMOEjK|6m#hd
Md+TU6{J|*6B@g9OkxuG@HyBJO2U2p2-$cj-;~E{<)du=F4hUeFninEUl0BZ%LMlOk@Z(&;Rw_Pg*>G`5|dtC_CE(K^g72fFa4e?@V%>mmp-tyPh_W2^e>=`
oq<7#*-G@@rArzc*K)s|MJpC$6nh1dOPkh9tA8f01c;r>C$yPLyLUTEj0T2+H<f=^u4JK8%&Iw5n6*6Zy%10%IJFqLhr%qz|3drh7kGHxR`xI)%jXZtGQ~J0
tNiW#zuvdtHniqZ6ag7CM-8SG((3Mz`n*)a)bG%vCk$!TV$IK#M&Tjc<{c?(3CFq1EYv%2B=kwY`vpV@ll!WXD+gI8mss@#J-_UuL)Dlok#)8RK<MR|`qD#q
N91g)t|EhMixx?#?1`hWinN0dYRdv*Zdr$6sM+;HrAMdo^I;p?8W6T(X|Ph?8=97MFQLJe1o|5gy=NwX&EndApi)!bd5B*20ohtr8!Tc-)}Pt!#c8htqtvO;
0dLK#VP}4|6wN@UUaTf^5B>Qxz+_CytkZ{IMp@4CXJP_t*Liz5bExJI-?m8fmR+?mf$4coID_|lG1K@OjoP&ONVRB{!XjZEy-~*VEP6yR@strr0nl-mC<=Tl
Q&mU`VkGxpuXjXLD9COR&4p5LzDZ$>a8U`Mf%Gq$XRC}q#g{Ih#7>A_Wta$xO90N-Gv2lZ<5z$qV_{Yki8#V{Gm@A43o8%^<y$ys*R^n<x@JEeFeFL)*gl5F
sbmH#4Pa5=X014gdR2U*Aim<YB$e-a!-e1Q9$V;NHL$lTO4_lsCB9h!-o`c9ACR{;6;xI>Lxkr%s_^I@#s?}Gs^OCf7C!=Cr|jUSh9ilYQFeoq3r>2Xj(s}F
l;!c)XqYApEw=>aYSg7u`7u|p$;ztI($AQ4W+Z_gs-N<cEg2ufR*=p-a3-<O;rp|&jj~7sIrrZ^;7iDl$_YX|Y^-^;=v~!!15<M9b-LUm`YmDWo3bNW@0787
EK^*Kt$P^@g=aU6E=8_u*si1B$pT<<>O({~c&)oU<rtahhata*EO$=I=h$>2%?u9KJ-&0T*<=q*z(UdPvcruY*9$TDBK^o9%|W2Nr<E-o98qC~5<n~EE_3e?
!@qzk4pc1|!eJ%Op)@&9@Pi;HfRWdt-(4$scEG`4EmCobdYS<6;BBxF^rScX%kl~yR524%?x~Ne<|zih7DyMH)^1HY*&^v>?v|f;Q(q0FZWjXpPI!?YJm{9g
PS2qCbDr(z)q`*)AB%zGd`{l)wjw<isA192y^xrfgh4z4!$0cx6V<Os)xrUA#96oyCO!Cp{P!P)Kby<48*S5pdvdH&ai@H?JQYWlFBD7&jV!ME%LWfH`*zdd
m0nP=5l#=-%(V$^d$HG;-S1z)YCL^+hgH`wTsr{qKhn+vk&>`F<ngNkV?_wpt@<GFk|7xT=S)WB)9H-mX(f1~1nM`RAPkJH{m!UDzNjE@mioO^J2)b7CBi#R
&wk%sAs#8lf*;}IqK_!V3>)n4Nr3SD_3pP|GlnG%#@DMIhSFSEjGzRwF~F=yT2DADTi#eYzY3!_Q@`;n-g-?kZao+vX=!}qh?QUZ3jExSzKum5etH}((BCs}
TYK{=L8-RKvAgG_>+F&`ZK6;|<*somqy}jpX*>4~JR%SVGo>ZE^uzk(*rTXRu#uAqVHqyD)7B`g1rCR#YVH78#VhE-Ug|Y;LqNh8`<ed9Vz5bmIo^TySQagT
E_YJ6{=z>ZG9^kC>JyU#8h8N;N5*%&X<Ra;__5~}P?ZSy$^lL`#%N~MNK|od31>_+zr?*ePF;?rrcU$RM+|O#(Qv$zOnL3Z1iq2@4RgO+(hXkVGdg8sf0B_k
;W`K`9jNj;`*N(G(sL6CO$Z|{pJh=7l-d&NXaEV6HYSm18Cd8<=J&+-@iPHODbk6%m06$&^bY~oZVOf>bX#G6lMOZ%jkeCRS0r^-86GE$p-et1Q4J$43*y7@
r<P*cN_{w@#s&VbEBc>Tv_}L;Yl>i%`dg7X%?FIs&G<KEAB`WscsZhVoiinJqWgq|v%@V^F*(f^L;BDRHNhKnmyR302X*(Dv`@SMdM0T9d$&T468DS%kV2_~
>tF+jJY{8cl%K%;k=)I$9XH>ypq?+Gey5l*v^-?0(qIEhi>86$fZ8W>f93y2DuSaLn$?XH*{P;NQZ%j>f+RSqd<{xEIGI?on55u+SAUxbs?LJm-%KINdkKj<
vxn+H5U1)V4rE)I!}GmqS?*Pm{7DvY2o()xpQwgm$yO5m?V8rIc<mP+ohwNUpD59F20XhYEWkXVz6P6-P(F-KI9cUYHVI-=FY44i?vyT1K~#RK>L24QxR-Hu
TQD6)#taESv;#zJoM<&#gyeaTKToDdU7wTN3>edqT+R6w1t~ugY@M~R?eECTy^E}FAA)jZug|GI0Bq-Bo~A}SZT4F1@nx-1kix(r$M{T+TWIetPt%&o09AW|
#hp*6!i+RqBUVb`tuy<M*1*?$pw<jmjyVWdGnLtwQ)OT?EZOcPAfoaMZOD1SxXK$6#>)VUZS$BXmu88iw;J(<yh+4AsUi~mQm2VpZ2!k79$eUKYJ8yQfjWT{
j^8NUH_G~sfvBDYmMA6$X@c#9z%7s+aLwCoKg`~{EMZd4`!1G=kDZ4T+dCoMhx0r-pc-UNxIo^zTvq?$HGw~*Cf4h4GzhF8KLmPxqN7aa#%+UNW$M&#di5ZR
d(R0pk5B7PEh~~$ccwKuXH4<-*QHEFS+29G4DSlk=ZN0U@+;J6GRVWBB8u;l=}dJmSk+xFyEHpKcq)5DL&fn}xQH5hE|(fB4~!2)XxI@Ouxj;G5R5MC#?ZY`
KfcD2_&EakqvMFaLc+v7zDo4pEJhJw<F}{lo4Muxs5FR~WWpMXa0%maO0E{bgJ8_bTCMr9pAqQdF`7{X51@*iC{4=K<(r-i{^d6Leb)!jI2ZnTB|0JGs64I4
ZFZ3i_9!+7<C;B6Ty^oj)G7PUf9gRlZSpA<W{gB$)BsbtD&c#|1qV}D^8Yc0Krq@K%PID2);O4$-fLuUI*6@s2LEOomi}OTM5@uE>}DJ%z`T1jJmcNG8+nYp
<`sYFiD{;E`RYyD-QoIcFFZF0n)JpwyMbSHlT}`0kUB4H!Q1+indMz~3R{X9<gV+{&T3H%EZ`Q7)2q?ukhmBxxpNITS#>WqkEyhix0PMd5;R>ipEiN{WNc)L
+A(d`b<@`Gw#ItN!pD%7>dHN&7sT?#JlXA8V+`$nwcRd+4NmI_hH;Kd8w?hMl5TQP%rQT$PRr?55s=*ER>MOnA1}kWx8Shs@Lqn4FwNDPa}sd9iw*W6Y3Dhg
OBOSK8<B&J9GSh>S-!Hxl~A5jggT%Pp0TdfYB2rhU$#c$I^nQ_8@sU%f+f_1i#=}^%<Ba^)R!Y{ZRC7^H_9$u^u*w$K61CW@O?H3%oLXFMn+EaJJ)G}D_cNW
$0_29b1n%!qRVLn3u7l45MA&?-!0ACs`-#Lv*ssOkGtc#v1K5beu`h#S|P^8#Cls)e7}=&edne=>ROh$Fmfx|IW{Ajum4bt)nFL53Dr{L>nZ|O0V7<0<dwNr
hryjo`oy>yOk9-eu$QQ-C^2mBce!{HkFJZ^RZtSun4?<i^3uPF&LlqO?j*)m!GwxXRsTPs5Jw-`*}eI&s_ZI{=n>W!!N!UtBg#NmBFaz1zARd8cKQwrm8bM(
<scF#VWIv?{3yVtbC6xG>(|?zV8Pt!0R69C1GkP@RRL}tZA~W3x$tb4L62x?q<rxHsg7Un^442(TD8e|YtyE4xvbl?%P^7->HfU6&m;8HGGKcyn`!R<kc+$4
^4SA@U}Q~o<*o|9R_oas-C6JbP<i#tiOn$st`fXCkW!Xj3e!L=vdORiZD$;)7lzj<m3|QxFAY1iMUff{xy%j>8VEMm%@`YX8<>-h^Nbb(Fm>lbgqXZSfb$_k
#JMlAp(Z(iEpXPY$<{J1Qf7tTbTJW{I;L8aqvfo=rVRw{!d1KT%mN}oUpHPziy}Nz0KK|)Bq>B+M%6QNw4fh9H!OKz^e<Kxu1wOT?$&6~4t^1%vGo{gwopG{
onc(zx<eRcf_cghT(SJp52a4;IRKfRzu&4V-Z1+@uyY4uRvloSm94oK?O#a$``w?|)b+Q))NzeNU7%)SDp>r!wB`TK&tRQABXG!mFWaH1vG7!+v-up4(kITA
8#pM|w=Iu?<~c27N{ML_Q~Jv+&qZXQrbx58uV9_kbpCWf^QCzb%{Fi38gECVX~6;u^4I>TKD2{C`!B^6i9_~B;w)`M;Y>)}P>QMbXxt<$4V48dgv@H=CwmyG
ldLu5=wD7H5vA$l!+%l`JOwC~4T<coWQi^CY63i^2t7&H=~)`Pb}s)7s$!&!rPY!Rt$b(<;=~`&Cs@TT;qxo0iMdr-7b1N4kkBK!UIkC;Ihz&VXGxL+4f6D2
w3AnPLousnZpcE~8b*E9oJ)SRDiEyR<sXyMYb~cGpF5hVpD03@V3|xR$;`5Wp5`hXt#V3bREtdjcf-BV?%jQrK%W{E{uv{EAO04cRZi!Ak6<3?QN&V7zjf)Q
WeUfFL9hj^OZ0nA8aNvJJ480t^f~tu9sfw(h%kAY&=_Nsr`)F#0szev>BXL^(H1rQn8n5jVXLxXGT58H$(Nmcjm!Sa1{(c#6Xxi!S)+LvYS$jbPpv&JESvDc
48LTzAYiC76UnAp^>Fc7Tr<+N8Yym{zah@({wg<Fcb&?yMa?G3BB&q3y>rtnxbnx;D#QxmJ`NXVFcMnI=<2ndX~7Ldrf{6=B1q)~C01byDEdFfl!v@`x&3NW
91L^zHiW*9eD1923kKt_xD~;h_MFg+e;~r6Sl2ib@_as4w&sD-*GykX)#c*|n@OBNK!Gp|Uf4)p<9>VbGn3D9Ymk+uHT<4$i12qTOAqAk5MWncujl`il)YbS
4!3lJMeoHk;P&Uq==SZqo^4638zN%-YAe5SLK520p_-2Ic7fi!YR5$iJW*?Tyanup-b>(bV<Y;&yB!=GXNKh^N=W71TZz;0{^8~UJmlT-j=%$&!+@_UKR{z$
OvY++B1cq!vq`BDqYbh?3yp$Lzp^z}WKmFrZ0U41H}St$qU}t2(Cl^;Uh;xjR?Mr?{t&(IH>$cG07A`^`-<&<p;m7sy|+?cuII`%u#}5j%hLh!c4E2>9UTkN
&ZguK{mXZM2i*<wlhN4_BpN`1H-TdudAWq~{h*V8)U5~4^-ulGw^@?FX|0f1&m(ehvm$<rixe<tP$QQO>)k;;bbUyuAL|x<8wP19t$j9$GI-mOC+m|)*jAVg
Dco)u=X^3~n`u%`f6i3hA3$5|P!O*Vc$`CX_I!w{{r~uVfLq`RinyNhDJ<^b=!w(DmnFxgjR$y<9*<tRM^Cu_Gz^1av}Rx9qa+wF!nP*m9dm+aHQoill1M7L
(*A2YZhPf<Q@b*5tvi}^6UeGZAFx7E0kx~1g-jU+Q6Bv;UF>eS<UIm>Hm&@R5}X64s4NK@PhC`q8<$5No(a)u-Gh;i>Tiyon9-0Wofv68+cL5pH(TRI{Z0~5
cT3@O@w*gKd5ekbuQ41G9uKbBeNV4J3}Cj=@Q3>#CRkC-nSRv5OfyGb8mFb`i3NnaMBDD#l2`UgO5a_I5VdKm6evgJp3{m7m4xeASq;=ebKz|MAg=MUGl$Ns
XpvvcqI%YliO-=bSN-i7-wohgqweTy-&O6eYv!G%z&rE`B^lk4<~_86fIgCIB<jgKN~c{pq+5JCKNMxMKiSfBIBu-irg>M}tGe#cdCqQN+y$A6;(e3CwiMRO
mBPTKpR;UE*Pj75pu~YuS!j)%$MwHkC=&s2s!T1FiZq22qypBiyN#mJNAH<bEAy}EPdCPo2%P`*VhN-?GxS`<Qr5pkQts=dP`2zheZKmAkUk+Nv(Z(vEN@F(
Q}`))En8RhZ4)aNZ=Z-_n9zeXc+`I;3qfs?GBNc@hsur9CjyOY_H78S-Zz(_A^T@C0NQv_=i(J#xr;2BEs-`@0HEzBQG`vbcWX)5*At9-`4#2KR-q!Y`6vZ*
I*w!|MITG(yNaOZ%<t8UNk|8s;j=1}vz0y~?Tx_t+MF&td&xj-v3gOc2fn3Dxe#!FoXqJPYTtseYI4I4TY_ufbgbN-N0EDp#a_tF-nm-t%0?q6_`>C;3CHHy
0a|AS;43)~ka|5725Bs?i?^y4yF(BRQXp3{Cp_iU9Hz_3<9BeCmuZ3Hd>+Dvc(QPh-jmQ>46dJS3B%`gGAPiHz=#HQU}N?Tp=bWk7M%ojHt|yc4$NcA5c!J^
L|~rLZ=%5OP62n)YP~O<5k;>G&%zeF@1(yhKgRmFh-Lu(W0akqkRqGl^wJ5%uow!AQ;HGYzz`;#xre>{PE?%>`8juY&54#ztd-1<rz+Yd+TT9E*5LDp_OlNJ
%uYl$sUYzPWP-zo4zl9)J(Fg?Wnxq`UtdXIU0A`@-H?FTj+p&kERY9<)*Ls@A*Y=y_kPJ(=9R!~!f3s-hP}uxX|Bkd))&v#iki;-!g4`fq9$!GqK?NZ1(-n0
0=8ja$XU=-4HmKTeBAYdhIV&z+0vlJ%AkA8O8{g(-46dg^u7Z{R&kFfZX=AwT|A9}!L;2$B*>LP5%kpMr`Ad^wkzULnHy)6zF<dDyIt6`xM6<7F(Z98u!*Sd
resh;<b`F9@G%ojwC!mQu#1{u_M=9!eo1~QY7E+2&VdfWa<)veBEc_^T%0BLhfig{*enlaF`NM#2ID`8DTBdXn7?&bwyl=s&FsW}mLd-ET$N?gbfX-Eg;L`n
PzF`_J8~b{bcuf7m#LNjf)iR3H_q(bR@7QDe?jYccZRrj(lZ_4<bzzCoXzWWw3qT!ZpW;!Wo{^&uzN{T8vW%Q^JVcrQg@`*I0DN@fn^gOGPmok7<9eK1nl40
ske9xfI5bF*kCng6BrI=_BA-UTvl1IX(C)H{2br=;&?O+n5sAxK$PjDOfWYSJ8W+pdmdNb5Eq@LJTgjTlVns=M1<zhX8Cwa5=y=z+i~11x2e%yGLd|*ENI#3
cp{N6U>xV#(g?I;gzSaXtiRsirg@LA|5cS(yZ{SLefivi7O^MTazqRGn@C#jZ6K`?=x@1$o&&wu2EHRs>>LQ5o!qXH3rdj|8ZN2>|GwEUQT|=RPE}`J+BR}S
gidVKEBswC0sj)$x#b2q&G$a+&KF<s#eJo1rZRq$#;%&{@fICd;)v!OcD;(vjrbM0i>1zTqxA6n9{ZwK8CUufnmzOczw6nDbM27}2~NZJM88aB5!|BG%)?_Z
{s0Sr$|exZeCWf^2vT;Mq3E<zDEf|9F$AB2_$|WZ4d_KPu)J{${?bsJU+WVrzXCqlnu9x<g5=SC<$f0_|6&D4z<1eJb52lKxA&XHt9kQ~GQyM8|6m?aEcEQ9
44hPjVI_giE6Bf-O=+j`?L9y+mQ;KmPpm&@5NM`$iJ9!0kZ(*on{afcg>oTa{egG-Pwk4ew%IU8QAhjId~BJ}!F#CUd!<1ZA79fW`Y3dM(|}6nrMAm-4La9#
DeiEKCq=F?qpM9swsty^N}d{a+>SvgK0If1q#je@OOoMHvP$^8b)99WMxkD8->s4j#fU&~E?F|P{_g|^HSPTjZJaJ4k<Gi0Q;YBjWr<sxjjNH+&}LPeo0mxl
v7%NF{q4;cM*}Pcys6uAQ9_xf;d*))j1LWM*4*LqQt^uKcpkHW1!eZ1PbH2LZzc*#PtKuC|H-cQ+&uw>UU`yqj3J6oT|argsyFG>FGwPMO&O2g*zac%mA3>v
X9XqaR%bJm3R6X7On0^w3?n^BGGhC5si^u7zfR5CauBJ4Dq;0Sae!y7NeNxO?7B=>9K=e)r*R{`QD`<ah4y@DL7V#|CFk6!$Xo@94ZqCHxLyVR(2k}?N;|Tq
zyz2SLs|=J?>!v--9ffy456m`(fr}JQWZ4sxuZb{_wV`lBKv$X?+Gf+ennw402yW_dU|{_XU>-GrQ@@2vR3sc#=yU4)D=O23p`Uy;LV%h3t~K}!E7Mv4m^s3
B3tZyY7j3l)}eNT%bp{hOWGj1#ze^4W~i+?90hA+l$jBs=AjRei!ke5w14%=Zx}Dh;?k|Vmk}0(>;6=QN_&tJ9zfR?`^JT<zR?742Y%{ZUS&w_167&cIjYew
>ssW?Y~9)+^s0Q@zWXwO?2rt|E|@ThTW17D&)D_USD>0tBlnHZa5`p2TF+MppLYqdKgI>{(=6FB8|z<I5Yy_=N;P>jMU-u@Mn|mw@e*D5*9=RAbFU~X(NDyL
H(sBKxeA)MDaF=NVzf3r!{^l%3f<Qzq&}O|;Z@LrTFGp)^VThBW5P?ZaH74AD%NUDr*ZIFX6KgmC6}l^_o!&jownSP<myr1X}x6T-0+)1?ByL#S0|bU>(z0|
<#&GHwx{x%ZU$ick(bn?YCC|c%V&rhKcQ=<D`T&ja=jCrokM=0uiI;2-^DHZhO2a~RfwAAV2|demCWNxh1AixqU8A(w5c4Dpd9FVG4d+qZ6Fk*fm1|yT8*}v
W4mHMyC!AJ{l-ra?z^5^?pUlRVF1tr!-BjoYYT+F66BRi8CWAYk252_N4&W|=Lg#1-3sShryqhKyfV==zj&FXGMD*f(Dq(U7G_szla7Q7SXR(U7(CFHzn7uv
ms?!zpP7zUSDobqn=o&RLVH-OGbn7HfGKuxg-{;R03@~!*kjBe)}C%U4y{Yza^1qYWOIXjxgcLDA*28I{EZ=DAK3fa)XJzXYJH+Syw5#XDg<1zYuwM^s%@EY
S0Zfu?Ezt(fkKlklfo|3zXU4ufabYY&iG;y?POnD<4f#k#PwiVNU1yed5UzN1kDtq?^76-5ZxlJTTwc}$!m1FPKV=RcC+PhqVLhxD)ULFQU`!Tt_6r!5n<>)
JgHq7W4oJw$hAc1;_}xDoSp#BW;j+MR!xokF*N|6z2>mKOb-7mp~IQld*08<*LMPn5B$y?&@7KKaP4OQkMf<uli$ry-eV(fT#mLWo}{($1CNM5!Z!9Ze%7W}
OTTbN(|;#vk%a%GvMRX|(8JUU@~A;K24d=f$$v42uPMX`X#8;6hp+HNaZ{i?DuD!xp!~L3u(MLP3mBs6jdb~|HzcOSa4*hW=giK8nYy?RuBOF|C10Uzm&$v8
eVqwKT41aBp@L1DzsWnm=TV=b!B33>F9bOE-9TS;@fXhThPb5@&0Ex*>ih%$y}IX4ZD!4T7qXd})c1lFq_xQ!5ZgwVLL8)PR^3yb{j6k_3U72pVAoHHi`c<S
3<G#1t>w4PRduK8W?|8#R({ReNO9!Ps8cjRMMo{@Nzqlutv2uIJfHBU4apl>(sEj>X@q_Ia_%X6p2&xn@rdK(vv<%s(hA){@jYLdqfKXZB4H8IB{rO6rc+iY
FnMQ~#rQBf>npALi<O0s0k&)<RQZDN5@IJYgQ1&?*jsle*)1tX_sv*>*4?k7@#5<<yXfk<Y#gp<>loB@GPjY+JALb@9K3w9i*e<H@X;?a^sQlozO~H8PJ-$~
<XY@HyT8g@2Pzu==C5=xJ1Bf~!%=e8&kj4ef0crBwG<Dq5%pKmD_?`8Xn20`q0882JPiQ(<E=@&*&OJ%@386Usd3VyE#RU<(}x%*n_U7gM7yvp>UfRn6B4Ac
{HE_hxA^fjUvP_96394i#bPRHigECODBTs<Z1!Tgo@L}19wUmt^>^Bf9cfTGpH^pu^oG2`khhX@@HbFqne?KW$v}f^HNV;K4i1@L*U<UaR}3(4d(*O9q?dU`
F-nm=Y;O!B4Go3x{cw-rNk*(dI~f}BZ$)g_dB?~vDDpQ+DW=yU{2QBjD7znc@uK4!Ky`FkBl@+yUKaz=zCaVm<~-@%O$Zv1TJ(Kw57EA?Rm<m5ThQ$m=*Wsc
`%*o(xypdg(Dq2>`a#({*}n0XPe}_xEUR}$0O__lv~%`rB|xrtuY{Jr5-0DMZ0o)pe-o0=c^b(NvA;Q-YuB&dFK(`KQ0e5Yyyo;{wnuiMDZpfD?f><T);Wot
J<|enk5V1lxBr7tR{tqAt&MzmV5c|zt28P-{~C<wcE;df%$RW^fC|Qod#JN!$p&(1PRr|-?RgA>17Y&IS8y6SL+V3yv9w^a1B<>Y)AW$3oIRt19zGzn3qWXn
+j#{%IJvqtA^j@PXquW1r`Uo2aS0sstmx^^cyA-<R)GRtK}ipr05sa#-K9ERuJ#UpHu_MbyYPJl0l^!KnZ8Yh&xxsvNS8E-C&=xOCd^@~c2Fk)$=_8-t;#1L
O5imuH)2_aWFn$bMbb_PZzu6EHQFJKTO8Dj2z_JZOEW(_Dl%;#P`WNE<qRgl!35956qiUTf_&4DwH>&)O_Zbt=EW*0tt9vQoW2V>4eKaWTE$JTcP+l7hDZOQ
BQcmK<rp&(^Rg`RqNZ8|$J9%x#_iu_gWU*=LHC0D@azB}lv(=_AING0UGjZXmwU$x-yy;9tR_3`$>pBm*ZGWOJy;zZQh5enpqM?t)5RJN>?jUjI5u`<vFwUm
yL(SIMXB+XtqAPkbX+~QO}V12xc4tZWocWI-YJ!IP;up+XAL+Iod|>3VHQ2PjupiQz}??KwZc!z(E0#Cp>i1aBc~2wwopC#FJ!n;0b--5LrH-~6~F2cle(vi
;P=#{$G!^^kZ+h8q1qy0aZ2*7cVtm7^b`H;-$yWYUDYJ6@qN*{Ohix)&PEOb7iq;SET7GW!4={T&R#%hQb7j@HPCSSZJ7!qYtfpd@Y_E}cIe1Cfaax^ZhM@+
Z`{5V+s9P1mSTd9SQtfLYN0)QZbe4q$v|K&9GUeyF8okWV&+w;2pr!C?&F#hOES{55uPlaulLZcxOu=c^c~l0r-h(l4=?#1y!8{~@}@~!G0^q?aQ{3Fg>j|0
L60)Twj1cmldruqdvT)UY?nZj$J<{@aIPC`R3jd$k^}bgHOAphWX|$65LXI^fJL^<dDnB`s+YY;ivX|RJ*usmyEizLpQtfw*EQ;$T8(Uyc$bdEJSF^AP3@&7
cfGknkGKjfOAr#%FFS|#5X@4~q?H4SU<T?UqPj}zXxmvx$?XLmqDz%Ciy#kQrr_=_?YXDWxaG#X-x>7zu`%l--)h%$R0GcZA@L<aliNOT8mc_=IQdKCPT*4O
_+BjzCUZee)>N$v^Jm<hJ;iGm;pQlcoK3-PHv(&R`5OpRFYoB5qakK)T@RewG4MYAT#i*2%Ez1sY@-YVFBw^1=okW!FJThy<H5JpBTRkoO9SheEEz3S+>X+c
wC@GOyoc>4x9$FCE2o<&a*f=psXXGyIQWP6z0t)8*mS3x+Fk>=3p_e8+q-X{#nz@_6L7`X`CcladkGhKy}C`Y{+6y!J1X%#U)ogXVvv^)pDH;WLt}-lAPEs7
zAKc`-76(iQe`w!soo$6EjV{Zz29~gP@S6(C*hS}^0X5Qn%zI<kZT4QNV(@7z^|crJBIXP+NL<?Z%|0%%@w3-k-g)z{%p#29-7~--TK}o)`i4J73;X2KwMk&
!Y{YNfIZD%l}7YavLz;MB=p<?vIz~%GtW6BV(W%?1=JpKOJ;tzKdYX+LG&?>BK^xW>KsmlQl+`KvI~*?2opQ;p_3o2#9SM)g7?w6U>d%WPs(@+EfbBsu_Pue
+N5}o!as(GAl{$O`#xD<1;gc?87~nRqTzig?sb+-7U?w!iiPBN24t`A5I#di3j{N~(pV~uW0rvm&%`ngi-Rhj7l)T8KIH62MQWxIxSdt+2&Mz))Bk>-+!M;Y
K9~Qwf1>=)P^RT=DQ{G*lw^8}QQP?BlgZDw8fWQCW;lC{{yjBSzMnAdb*#6o&gBCeH+=m2EbX!hR1g;A{r^h5yuVXixJIBs#HsHnzKWz*onJmKGf)gl3@naQ
*PD^I;%j}b)udi3Tp;qN3b)w4hBDsQAp{(migiZKE1Zz5FvYVPXiW>50Veavixsjd$S`1-VwrE{#t*l?(AK>RxADgX0v&_@adyo>-q^?rV+S_Q4W?~>W)558
oELU~n1kX)pDcOtV~~jEYc0L}+zg;n#*8Xa((K?lPq$$MG!C$#<5)v}1&ng|QG9NezV??eqs)%L+~<s4iccCqk2ZuBRm@z`Tw+y77G(7$XP`9A^^6=|2`kiF
&?9rd!1o%RIi#XE-~sGcNT>dXoPrV17xA4)_5h<b8J6T}dB2S%70nSZv0GW1#u*)w>xDR1SyEL_hTpk^I1C?tI{_?~TKq+}hIi<*dyEyzA?6MI7l(_hG718z
S2VA;#975|W0QF^iTCpr<-s$4F9C4j^l=h8oqDF`xn}Qac26QTTJB?N5v^}iEm8`xrGj|uJWJ=-wZFCZP-2UQ4-IC*gM3nvi(O)5iE{0qHdzdbKa(Q3^S(w3
Hnlf<j1w`E|KkL~!)3%#HbU3$IAEzk2$Y?_KT2cQd1wSm_i}AcGs=&D>jGM-$VXNol?vu<!_QkPKdadZ(y=^GUZHh;z$<+$Y(qIpFYZ-`D<tl?Pc-OBe?ak4
y`rv#7BbXhAiU7UQhh5mQn>C_sGFELPE}2(iAE*`VC8g`r0Rnp2TL_81(l!%P}XG+FP(=OMyRFyK65HL;lcsjOIcnJXxYU;;{$(julL8aEe)=Ubrt{bdS^&&
K0|F&Mtm%UDchhIm>B|xN|pd3SR>4*yjrH~(;<{aCmCT_{#+<d-f#J%>dFx-Df`nKKck;?A0yY)XCE=k7S50=C-g#_D1tp~NLk|?Dugr*fNa0{9Q$tMS5lZW
Z)l`>q(5D}u60Gpmiv5ZWB34!wAmI%1H=&Kiw$zW&0Ak6X$V(&?%fZyDaM^f-BeS%OqHI*Mymeh3jB92WH^D2ezA9D$gfeNq?bLf*S!9h0IADl4F3N&xQ0oz
UD{(<t+M@U6fZ`O%k=%YoTQ9saL6r^!;Gq73IqtULsCJdVk6Ac8%?y$6K`Op6XH-v8u=1ie;Y~O>Y#ZhR9n0ZF4rplnYn<jv}A{hmuR{snlDXa3L*dodb=vL
7({m=+_RDhU++;@CGysv7d2&YTFUTP3|@2(mW8!mRFhdXA7dPw8iHiVn2ItF$Qu+tn8g&fG5-2{LU!7lPXgP_BW*s@E?qHaURAg<Z~@FdZ43X%`x^JbJ488K
f;$Xqam(>-$9gxlXicjO=N+*fYr5n?USZrz+ks)4`C^DKmUagY^NFbBb5cj@d73Qkgy7^=Yo%cGHH~kpRkVPtY}jlv&T8TZ4vWDIf-r$Gs;oFzizgkBHcfG}
%N;3T{N*OQYn2quL_FtJ9RkBa2s|+MZ)~-`rgS#_+!D<wU8vIT0CA~~k45=bryMU_^eO-H)2r;=cTy0uH@TM(?l?d?O`BP4*;dkufEJG5<!R_FUDnRN04()4
Nq3~w`1O(wlEG?Jh?mXX5Hx9kQ>ohzAw;^--fv9-Si;Ypwk9UZ?~g@aknd754=uvQd^PkAiUI`5c#q+%I{8hLm7k9!9MrW6Mcg=f%V(Xks{kh3N(8ujGIHQ5
DXVqhW`!~8NH*}u1Bd25H>H4)A+&!q=jTul@fR8d|EXqyFM@f`*~$-#Q!A(kLGy$h0>=cXb~|rp%K73Na5N)MoZ1?Cl#d)%h)W#sP9P(R^}<q9LpVPNHj6J2
40zx$3%jg6{wIqF8>6Te|9kEy5W=(XpNRXv+E9Z$XOb>fxMoWXTK~S)RAL6r>^Ib^N#3nk-p{yiXK?5D*flY!eAL=wlYgyteZc*TjdP&lxzynq#~cYexvu}H
jiq^w^DF!vV3=@L>%ST6JxQ5GXR>orU3WXhrccJPwSHch{GT%?O(6QWKz9Ikd+)O)?bN9<IcE)p&2qn5k5|iloo<U<lZ2XFrOvI!U0RExu9RV5wl%v7eTAJC
0}xzQjPllpe!hv1>Y>TP1+`Z*3o$qA%{?nTYjr)AD8{Y$T%(h;B(G_>(LGX;Fb)h8K-JN;ogo#8yq4#*MweGKuw}hIM~cYb0aZ>;*X~^Brt|K~d}A&3Mb)S}
IAU7dY{?A}`APzfB;8e8upz8uBq3e&pE6Ld9Bl)>CkI+FwBTx2-s(p}$}!;BQ|oEU<j}Nn21XD;qrqwNUS$C5@J$)5&L~kO!8sUGpexq{L+Cl_wNm->(KpoQ
)Q`tsULr+)8;c^8A{8Egiv}_IUf`alit*Y(WEOHISbPfqoI1;ip495hbEdXiyL2?fjpx-i#bDidNs?)+jSY=8adj3CrxK^ZLL(h4?i7F!0`2HINU?umm8oU}
Fghnw8JztA8?R(@a|)pLngbA5L@IA>H1*)r-vpEzKNkfxucJimpX#e6IH<B5&)+}%1u{O0!;cqePc7R7Ppk6^qy)zKJ9l9kd`L8Yv?!+*?%i!`;xdmHa)|8L
XUxdHM1d!ucp7Pmq2+xFq844b==Lin8>UCV-VUJ$?bjZODx!-lba1w8p~h*XPXquz?ahZgrcD4u`RMd1y8uQkN~x$dEw1_D9Fj}w%>ff#&-=8qj2p7^WxFVy
*O_^*jucyM;%Ne0+AD~dQgn6OgKyG^sKxMp@bc>vg#9%1;+S6pKUC*ovDs|PaxW^!mVIRd392=|Z=+OT5nFzNSRcrm{*ZrTX8)8RY_rq1J25yKRGZU_42ZAe
Z%(uqpQCy?9w_$XliOYnFd7-VssrH;YgwjgMcv!*{g1x!GZcn*ktDAPAb)jD8!NT9L5*bQ9RUTzS`c4?H=(O7*XzXVwr%D|r|43_R1k6Fy{(bRfdoDx!5Q9Q
YFnOqj=`gpQm#oKW*##2F<_UH9kF+CS&49*@vK_)8-#;$Ba%u$U35`0F1bPpcuY2-PTJpjc6IVXvc1to0K#f@{76FsJcmz7MK*=R#d3dl{I<k`cla^j|B%Ju
>rFGoRXmz{Z4;9<0^P&BhuY@2Hfij)S!VeiU+VVmppPC*2&rd>x))Ncqqqby9JK2KuvmCkNSV)sW#(_3ZY8TNzk@?;L3fx{rf!Zf84nyc)5KRv3$Dp63%N->
=Yfa|mBJrHK%?S^RZa?K62mmEXclF|&P^w#px@tC)=cA^?$?s*eU?0AZiZ}l{kyJ{{EF7*5;`H<Ud*Ut2R$J>?iL3tTG?nJa;%HJ1OPr=h)9(DDKF~t#wa52
R|LVC`I9*4Vsm|LO4Z_cq;E?#VRM=%g+F$``q*$g))Y+gaYx6ADJWVMKO}S|g$<zU!K;SK-XI^+b9ycuk>GJQcGsK49+4W9VxeuOs|psdNs#TauCg_BPKw>2
dr*9wgHd|EoDNfFgm=bLJdJgv5;%u<{Z|k!o&db$6CNB|RSi7uktEnnN?9Pr@852^q>^|=0Od4WrmU{wLwUL`=2gt8mM1LK`Um;1sDeBI6RVEFPMtL@{$Y`v
BmNW<{mDwMxwzAkm`+K;3?_8+!0(aicJGXz58M9<WP-e~K*?;{<~Lc8^EX7?<tpbR9KF2wG_s!({OZAfXR+;FjqrB~)D;4)B!gY8ke8&C-0>1wurkq=g)y^!
m|4BxhT)k849Y~;=A2}n%dOT07nWKl8ubcD)u#DAi8wzDODgEtQ_v5eaV9HdfvQ^1H?~j2ulfDq|5a<a)Qn-5Zo$^jWN}J2LP*I$=}C9z<i#KjaYVZQ2<toI
tvM|s+n#crS<{IT(x<?1Yd=DstIe>dI6wOGnlC};Rj<YO=R$84hMRz%ipvkQ{h<s?6liM?Q+#yU8)(w96^|A&Ed+aAMpGmMdUDjJpTXoo!w?zSJ5_^41`LTT
E{h-&jlnIslx4QcUeZ!VtQ9i4e=&JZ-IL!HZhJTL;5o|0SM9UCWs{d+B@hKWio?R_scqt{b3}HV=}@U%SYh_z?!f^pb~?{3L{eke0RrU_Fd^?o*p|Uri5*QF
06oS20C+y&yXtunTr<8a8(~M1q|L^Xut|;mjnDapl(|N;^M432e#H-9iMbZlRUb?LG=^(-X7~oY;nWi$)nH6IydV9?iKb#kFoud)EnSLMq#P*W9H#_}E6bIg
`-^xHZcYIj(7ps9Y>HuP7TkXjRFT2bytG73-_Oh;v*k!?G%(ZcXXjPMN<+8apw3WCaP`(L^DmaGY!`_uU1VNeWt2O)iA@O@K}y}@;r1Bb$n#O<lH>8Q>M_<a
FDh*ZP@cGK293S_f)?9`<+Zl+NlH&}Dmoo>>s5M;p*Gsd?VJA&6}p*>jKI}hu&;Y19Ymxc<AhhX^JxjiSkpU3(m>E`L;^HBt7e0uOJCR<08=hA?Iuqhy#C&I
5*!ua#xF4#XB{$XAx8YLeTHQqfz~2D%EfvJuzBNx%0PM1De(lt%)nag0f3NZC0z8KrS13p#s7>A!Sa@uj^sA^o@b)Vm!i!=`8nlOuhfaguL?|<pv8&Sgkl1M
+sc>YQ{|OE;{q0y0_K6Jh)#el6aV;nnRPUP?%dqn6D>+|l6nBNR4Xp#<!-pJF_XSUTyj!x<yA=$ge;$Qcf~|bx7%%5!`Kp?q~txvyYT0Wa~Dqo#M~b?!<7!}
l%y`MU#Pwh<Hzi4hzXFbj8NJ~p$%^9eN+%EuJQ-QqS!uveaFka1rub*(tsZwvtPggS)pVK$fth40u*>`%~NGFIgc%s9WF$!a!R7EsST7R^*(v7PNE|oOQ@b=
ub2XFL}>Gp6f?ndB=;9quOuF$Cjas9lZ2w$APemEZU_IuzT8+p%F;9LwHxhe77cz<+rJ(ZT`D|Jg<-)@V*%v92UMR5rN&+zG{69iR7-GKr1~Lrcce$Aok!SU
nCzXlouz_xcJFR{@7HF&;+?N}JEcp_smU+O$;ufFfryqlVK_hpzpq>0enmB~=4JH^^!Y%`*qx;M^^k<bKjtYpc@4nU6Q`$=)o|_ur8(f!Sy6_W<xTy=+$9h$
>UZtbh^@IUNqne&s;&$Rk3z;l!@;*<F(jj#kcj|YN;V`DfSa`$++&P4;ONH|dYh+;7QGtn)tV4+{!yn>?HS6*SCw(X>8!cOQ=hpJQIj5iT&B>MB7Q=_a*1j0
paV5>MHYDtkS9tS6|F=qC&s0b!{eiLokQYYr(({gC=BFBkRpx=i&(~;*IItxpWGv|m9Rt8`D-LVgo6*}lO%cR*R2+=4QwwyUpVdh9-4T+cdrHigL+U6Mso+-
J7aPu<pOx|b{wG~A|qc2-Dk%NzOs0U!4q7LW{ol(nPKiJL#kfMrA?@DcNmCK%t>2klNzDy`I&7GBik9N_%fI&M=V2;4<iqix|R^|@F_ZJi+S!pAH>==Lh+HP
A@>##7`o(x*u;g0x(RLP+ESDR)Ef(uzNg-1J|LYLO6V=-Vo|R^8|r;wk7JIVE~*NxuCQtK_zK)H8p)Fanc*H+$vj32obcFuG|FU}UR5hB&j5IJ@fCy;)cu}5
!Sjpv?@A-mEI4SLNW;O=iKdCN5Y2C?i{(or;QTUhS)!5=ZfUg6qv-x#{9Xo2cf7S<0?Dgt7ANpWJLJA(d{F3_Cp5|M#K24Rg=+T?-#bAsnxD`6HfK_SLDTG*
AC?uakP_QuO#J?$s#-hWSYQDdQ<G~&BH%{-H|V*B`QFgV#BiJhb{T_`o^3S2V1`sBJDz$0p=9PRwhHL0dP9W#Ikwf01q9~Wem=CCLcZHfgIz<H*UixdNI5F@
lL=C+9>#I?<o2jy+jaL$Zm4KDe$D$d%>E05SeF3FhL31yf?s(P!g@)U?>8%He`h{{M@<J>?vyYxa_F39Pu`NrMq)PD3w}wrJ9X+3?X+#SJ&k7j&N|03BSwb-
gGrBQ9Oh|w$Cdl~#w<>J=Z8F&inAz4c`q~9-NXM)5xbv6E4Z?mkEUlmpyQr^R>>1}@3Z!(y`Fwe&tm(VYS&3VeVd}q7)J|;PV)%<rL4HI#fD5Gi*C<JA9d9G
G_g)sD25#<C_AwqHxLJ-TBoJbX2;<!pvwh-@=om9MY^;D{G>t<)!hbN>s8Y^>;nLo2Fj^$RaVH*s<H9tM8g%c=nzIbPrzc)<|LUemTv}~`poDochQu`4yzEk
RZhQ3?e#v1A6VK2`cSx>i4u|&#+D*N7`~sM0wR}O|72ZVwW=*PoQKO>k1fSgM?WHwA&uI<q*k_uH`rP`#iy#GCooG{*<jmcIIOGXa?3G|>Urh4B5n&PFFwyx
NT4a5(dPr}6Vd<VfW>7(#B~YtJZ0@?wxhPxc6OcxB6yzHl(Tqao(@VWCsm@HIyZ3{Ms2K)%=H{MHNA_WY{1J`ol7<_1tTLqv1=GG<6B<I+>Fp~0BnmzWgNe}
YJBZ0xc#1BdShYLkQdhdE7r4by_SL!>loIArPL|{AqBfRcaU|5G08sxU{y@=L5jept=VYPi1&+WF8HC`xf9Y#&1!ff&tmT-=>2LBc|XPlEt3?|+Yxd$%l#1d
(q2$@p_YnBeFBlSHFOlkz-g%b);y#Zlw>b<tTv;ua1Y9BNAADfjzBac&aT`O;-pvJM727;!+-^}Y8gu-;fk}`RQGu3_R3O963dQe#V|5Fko`W)5E;C>!v3aj
($ytBhOIgA-j)`il9j@rPES~;Y*Cfj?NU$2FtQHh3_cU#3xTb@;W1bJ-DE7fZ@kU>loZbSUV+EF364zmlpL7)uyyf@({g;$M9yMXQK>x4(%^=uowiiaC<r>P
-5WE}?mc|u8<|~xWW+{<zMrvey(7{+<+|yd^AfU)Y(=&J|7)?yi7CT+?@UiO0R9GlffwLbQt{uJ#78XTU{rW`-JK`BYcJmmCd0I76u#$VY1tt|*th@>7#gNA
_hx9wdQyFKP2IiKXz{5<*<rvy{}|}*epcp=fxl%k=aSQTpI%0_e;)&_#~r!7ZvOt=PLY>QK{u$L5#Scc#*k+-#OC&YuH0LWF4?>ra0m&7ynWknL%3V1Tr;TN
92ec8<vkb}a8#T+QPZJpE`3}udy{#|T&J==!uBYKNbQ}i<hd$e-C2ha>+|In2N`Z<UK2@{F}*?nvy697(-BY{17=tUzzm8zn&hdsPHC+e|AhN0SPYNdPoimC
s%G$@-pO!C<?eWD@588h1!hP!ogn9So;%S_KGpx7ji}923b%Uf6os&rMUpqyU;tAVfAaucr$rLu#;{aFzTCC|F2XgvapmQH>)U{JCjjTYnDa@#4aedQw^BEw
LexU)z2l+wxOWBV)-Ix(4Kv}_04<`jZ6Y~FPL53tSaCJPYllafDxcBh`n}HX4khu&CNnA<_Mnq+3}X;`ps{t3$0b>bEi7Zirw~k>Vgv;eVPI*btIU{`lNCA<
VKvmi-Gol0m<cx9l{(;|A@}N_G&q9wpRg%jNsud^DjMt5f|kYa!(~c^Q7Wo+3RhX#gzuGPqCVw1@QmA;$ivxmu=)}&94@5(v`gAgn&;YbLaQN43I_`VsWUa*
PlM1+>AhXNC%GuQ4<;p5%SqWXP!y`M<U9^1)$!l*qNSkCVU{Lud4#0hP4Q@3*Y&}=-1duzV=E$ly0rfRoIVUD>NgzU&^T@lNO<7_FBdF(you;KPPrw+!=3%h
tNl1cYQXooD8IG~);AR$kSvXmYDOusX8y@S(SkS8!+yQUc<gLK=~eX=7j?zq|B_!w5<1Jn#D@0P(66koyE#LqwIZOaR3Ut!tup&8l)J%++Uei+;ufaAjM|lJ
IbP2Y32h=dMEdCli=Ea+LJX`>C89Krng*ky9Lk%DGdDy&=H?C)>u;(i&zd2I_J4M&akck`*;k$bcnTFo!<x@Yv^X{n*SWM;Lyfd-V2<2UdXIEGR^wN5=5qY}
tVHhhoM!O!y6p}34Hjn<<mI#(%XTu$Vbk336D5!QTsGCb5G<)iCatfDfllG<yo8U;#bspY&=5?6&QvtaQ^b2BpH1tVe=rnvhfZVLN#yfT)CkO3KGBJpT&%Br
eyfP{p6mGf0`G?Wf>KNe_zq4ostYO$LHO|0=1GEWajTyfS?g|OlKDT!#5l6PSs4*lu(D4+BSL~vy-sJr#-$Avk`=mpH%Zwsh_cxcpW*n|_l~e*`Qe$lR+4N>
HL~ux3mJrjUW04UCx|j?IpPgP{U&^ib&XOp6O?ei6I=P?@bIUvG8E9yAj}KRdMn()g>rt@L*W~sQ<P!(C?-N#GuuIHu&QiAypm;3;Qq9xS#j~BS(4fiNN8Cs
&dRoe_zUAO#D}OLS~dnL5mrk}{*fJCi10d=SzBBokn`w|6*<!DQ|Aj#k0slpUJPp@c%C3=vy-Q4;)Y{Cs=?HG0M-D!n}4bE2h>@(7pE8OYE+Bs3U~C&OAJ&W
Y7*c-T@g!~)&u@i8tMG~y1k37h;3^R<ICI=hbg#ebuj!=t+HHRk?gF~Q<pwTsRNf%FRIG}A(35oK)ZX<Uc*5i-F=*jhzpE_SKca!%2M8$BFXA|lmhSKwZilL
qLDiUwx+<g-$f_M+KyMp?aO2;#2y*VJFL<vP-tG%az8(lrUs{g3hCgMVlmQ_`wi-(7u)|roSpA-5?G)D(+mF026Bkh6i2aK@MhY9Esqf0j%D%5DrQ|U9~?U|
b3wk4?zy8>L$1YDD8D8p(FvcF>Rr|x)O<wx)hWmpm{BQj-c+Fds2&9za$uRKuLsm0#!2@SuwypB<OrFOdL_{~VM>s*^hT3`V@4%lbx~SJ7{tUv95}G`2h8=e
v3t!<Khw)*N1?IXUVD%y{qgD!Tb7+~kpB)CfWIYnQ#D>6tlDcmoY&ySubv27gB18u*PrC81EeQOPtZ!qxns6hyas(X<}I@bs7fOHHO+}*Sx>{t_55WHrH>rG
cJ~41;vAlH4ZyN6`UjTrpz*$EcRC>T8v&F!3Eozy<(uNfP;-{kQ)NU-9m7~)#w$fzXH_5clI3i+>zAbHNE%wd4t=>&6D9@MGmRwj;gEeaL+w?Tb`0BZ*%x8X
xc5#LSoXD{83s!%18W!XeXUm!rSb<R>DHgi*ypFdp;5-u$NUudD%1IsP{!H0ThT@!_FEr47Aw{i9|$lRWFWH_$u^|`EqY#p$81?P92i`zR;#k`ib*rx|8phS
4h~ZPQ*Yg7Y&e^7j?vt`k`|)iZ+dLyiqIxdOLXk(Q;-?hSpwepG8iOg4})_eb}S1D(FgppzXmOm(c#$?Ys901kYwqab<fRmk>?@3<&5pKL^x-mxzUgMF(+P&
rsp$xb`VA15Dz~2HQI~7vK20ow$e3f4J>&rJI2rJu@-gGdmrF%2l_xOalZG{#3&QQhgztJSKKQ~NSxf^EI1+Q_Ov8=&hF>^`ts#f1c^P^6u9ROP__8PD}-tX
l9UWpI5Fc*wl&7QK2+T_AcEc&Uh_(OG;mOMl<3-#R(yL>40;e(2^$vU=;Gcir-MK{gJB_Go|G2O`AFIX02W?3i(<ax04qJVJSwjkivbOh#~;E#*Xn){h^+8y
tdFJNpw06cRY$$+3X*H90u=_{=3Q)AiIE>oj2AJXt=mY3kqBWXR(BO7E*q^EZxx9?J>y{DUxL6MF!2k8YAApXZ9GPZheg?nJ|=5I@TwDw$5H{pIr$M}^<M-Y
@ohO63yt%H<1L<f;%il?jS~orlaZu88V#@})Ynq9Rg+u%B^a6A;Uld886d%afr9X$me=HhKl{2(lR?{5U38sh{mVoIQcE~#(3U%7mm2t2WJ=w0%nv!weF~z~
K>5=2#0-6cK;Uhx`e+`1yOo^hESjGRQ1P|t`jWYfjE>Wd4;1;HG5&d9zJ)${i@h)<R2KnApo}gXJ-=1pMX`cOr132hcrfD5xS6K(?HA|!J{IKXQ1?+s8lARM
9Eb<)ASj<DJE<&3dx6pxa_`x%w%|EvV<Yv83Myes=c*~UZV)G0(5Qvf$6%(qmWe_B`ZpX9nRg7EeK60gG+qJuDn<hlt$jh^>t9aX*O8Iw2I1v&QsL#z;1vwX
iK1MhA{!@LdbYL6sl%S=hp_dz$)>tnB1eolOlx<L^))9^Ghljdip}NeAGqFTi!Tn9o+9_GEe<$+nkBWChQ^b*L5MF?u-*}O99V<Y9+(#mk4h9u;;TkO?6FE;
kZH^+UWfSh%;yV3)wX0`O^~0*IFB4`N*(m_B*A0Vjf`ZyIQe)qbj<WWqE*Z-G<U&5R&K8fAjkUy1|ENXQPaXp*>d_`f}mLkyp<!Y=B;U~?e%Z;0%MNHNa+72
gr*AVW|EK4?R0C}>M1n@N-<{`KUI8o;)FuMgLgeiO?5616)9HHfZUW{lR_X~&+oC}d>gvH)Ixc7DA^3C?t@PfU)SMkR*K@0pyBrPuI*M1eGONXW1>RCdu+ja
C^K-Q5hh%I)%ynckMH^YRg1?lH#kW(GN0x-$Icg%_t1&-T~VuVijvX87HLI$+Mr9pC`5dfMR&R&@25k0#W|=%cY*K!+?`!BSG$=eAZ&HTvU7fl=!&)Q3SedY
VOn&mzcTclcqGi<bTt)Hz9wS~SZ`;bNNLJjc<S2}d1*B~sencSkZ%s2hs~(uQ&I9wkLLJw+On)sNPy4t+b|>pjB3LW=&Di2=)WjrtJ#_@Da5F~jKgrLzd}HJ
$McAI`XxmqB9115!cb)K$|6dfvTO2vll*#!sGI7gFakR<?MJi@>OHggXR6iGA<RSk3W}%nrXqjK;~)jJFmPMANtEZL)CG@D4v8OT<EVR!-1Yoi(&eXHS*xAG
RYIC}M{zzV#>*Ze?8<SjsHQgrvfAcygiY7R2M9fzRnf;;78{I!Bqw@F;91{N6d4?h!oAo5^?lVKh2@l$=-@@EG}59+8|NPKFWxklK2bXnSL=vIMPIdBF^Bp)
;fsapo}0tR;4H_m6u?G&FUgmXmoxNf%zaSr_pPknD>{sD9M%$kPOD9HCAF8#$|bfSL)f(3x+YOM_eJd*bY*=DrJSJ-4uD^BG_I9QldGv6>-FF&fCcIgSpUnW
lH>mIC1XE@lGx2A`XFo}(d4@cT!?54YN%nAfgy9_@1i_zBn6}^_c)ET(wqt#3)Tw=KmGXIf8X`53KGMBz{*Yqi0%MeVE1;Xn@wSl&Vp=zJ3C~f6+;!VlU0cX
2W#8iFH<_xrfWLFi4kX}ZbJDRyI5H3=crSL2v}*-;Th%~^Z1`>EtwV{-+%hNh`Cy%6(Dx?v{#sB<iJl{(JhWURAiPYgN=&#9xQs~<wNKE;Fx%-mc(mQV}|8Y
y2c~|&~z$7>lLD=K9BsM76ZI1ZcDh=?!TPsm{NeZia$?$Dtcsi0;;-p>!D=wlxLA%Z1!5h2Rz`UzN9ZLF5BdhTk-}C660|wCv7>1S?C^;lu@ZQ4Ggyyq!U!w
*}rY9U5hN+->lWW*rm@Da=tYe0q3LyXdtvW&dR|789$1j%Ur-A@6n7*$Vo6@HPX$Oy00t)P3C&6(3Y_M8Oki}<4(RI>v2WED(VaPmd=!pFUsi)e5;cVUU@;L
!!<C{+nK?*5@tL(MNFGS3Fo+y6+Qs&tRBDr3Mo$rk3U30h2CY_8H*juIA}X;W7=Gwp(#Fjmk0#cbags8DAFkE9zN08iWK-=Z2R^C`Ll|lrw3uiV>j_mw<!6A
zHB$rO?Tq6&j0SBH`qX9o?DKO(OJY;aX38-X|MKr%wsUTKk+`fD5>*Y)6{SmypS+Uj}F3^lO}@Pj)J}n1lz!CxyAt&ZD;&=#>LB7-V1)=7>X<WypDcBoeC(D
1e0Pa;WgX&<d-CS)L*Fj#T&CF>BwHhhcL2pM$g1Um0)=YsXGJAMGmSTtVTgbFf~MH#Q~Lhf}tARbEcIP?h~79<Gg+=y|x0?O<iTwu+WEv99v{}`DUXwh8A!x
g8}@%cPb?8J#UT59?#@%GW|ps?Ano^gST&X;<BUD5y(xShuRd8zbJd^<U;_+)3tB6?^dpXma=s5x%bjaK#9lYn7;Ph(}G#guAt14o|%2F4Z725{2g&<M&OY4
QTKX@4UHQ?HA&z5z>RcKB#w(x3K5isKD;Tys*#yUM?p=WYGTW7y-Q+91cgD7+k^kfVYMWyX=0yU(o~x^^+|H4f>^vH3H9guUy<-SG<~+Ghrh$su@ynC<S@4G
VcS&hH<*N~U;WrC%hV__5Esh6(aVw$IH9IaG%((lQ0|sJu>e_7V%*mS3iDdpt^XuGt97qGuJ#c37+#fv=D8<o^iOMTIb>0b-!Gn3J}^J}ry4qC-QyyNK^gD8
Fba*E5I$abW#eM{rNL*ru+B2Fx!ZOOo;^0RCaH*`W8~$H<sr^{9XVS(K1?qOV|leP-Fnw%l9LoqIGQw0Lf%F6j*DzA_2UOl$cg_PWTH;G=mvuvtb;a+)`*J5
0Q5SU%DA%LNS`n&>PktIDc)=a`>jRQq+$X1Yol^_Hi}6&a2W1}y$WS-XE$GGfkI8DN=B<i>1yg0SJ8mAUpD_-z~(ShyNW`#vOJUKk9}xx$I*26*8zh-@IEB}
ng`UNz0SH7^+zy~MCL~GZsyE@>)SEUoUhX`!Pn;y&w3js(b3R7g<GYn2=NoxkkMp{*`Ex@eU2jE4=W2!BTG@9mY5HHl*)<V_(+PBa3o>`cwYZRAt{O6pHG0d
*(P>c<t*6GQLOGaq&Hy4fyn<BfLBYmGHsw3Dkwx&%S7`I7?_{DrRYrU)azx!Jim1=E>l5X7oZO9AbHy%q=QmHD6l;=33}Jt(P9~$!CKdH>hbncefUGy9P|>f
`%Tt|)50~gXHT*hBt*^GOOo4(YjMoVk6%hL(9QiRoQTj%0=|_%KD6rT3Y(+0G-$_=$TDvuE?OJ?eJ7)?r@`4~o64my*=n0}tnT2*lEd$byGDLjd-?TQp!m@K
iNN(1F)tz3c!#5x-J$a6Cb!B&1rR7KZf-ziznL`lycCeI(czITHp=ScA_Im>jzZ6loX!1~6J(j(Ss`NQK1OtoS1LQch!f!yDjC}+SqLLKcC1CZtC&_sEuupr
M*P?_ulPU;2^$512PJgrzp=%LqJj*P&dwQC101qb<R#OwzI)sUqEKi2e0dH$&%`;V@#ei{(<>ZHiB(?+m{Rb7;`JB7h$)X)>lq15=gYT+Q(WD#H&ri`Ow<n2
s}3X9gNqjtAZ<hoeSMyPuIj^tQi7#ukm*mrQ=GSnd~%dI3qknun)Zp;6JbPDu-~g2wLK175o$#PgcOW7lP>=^jgeq@h<;0p7K&Y)W~&}9bN^mgLce<NLzq5O
(U1!Z<!xe4y#9ZYYcpx@o5ccIVm*n+y9)_TqUlb<>8Jj$aDihY1xcSP5NJD3cfOgd_iZUEC<|0r8-dh%YF1p^g7`sjr&*bM0n~at4O5KX-jw&Q!*rUD)x(K$
{$cBfwbZ%w!#l7TT<>pJ*^i%q!3?M1rRXc_xv1`3Y!5*;x|kIke_(K|e*re>NI!K^U5uONs&A*_Qd=`YCmfYQe@ApwnnFXLI!b1KWrsZCw%n6_5I6Ddcdj(A
frW38!wo)soHNgOIh(IQ5!-6!T}nm-SB5Hgj`0?b2pq4_4sMt9KIxlX<VeoTc@_5<q9iBb{Y2%`GBQu@XcgWbl4Z{#;_O1pILWuuZaS)nW;dnCD%cJYyCPei
_VI$jpW56&Be1mAbH829uD_?=={Vmya8^_DH#&V_)oHsI^_nd)K^U!q@?+TBwuV#4IbrMM!2f~>Cm!42f~>C)|5<9pgs1-oMcId!)}pSp=I#;O5P3EaN-7$G
{hkXnnp_Oh1cc7?gW?VHbcs5@y)gWS70dl!ie>-@ctTjy*Zf{ltC#s#-qPumJ*6xGREWoF-**4d-5%p0RRyLz_I4z41>QF79qNEK;%?Ko=m-6nC)3FPISb5T
hS5u_PC(xLyMdBwI`ae56Sjl7Y-{s=rl9%T6~JZ+rh}{*<UZNX-UKdcXVByl(BicUSBe2#)j+iNj%#ww_HsWF5s<3ATSNlEddW7`7m(L?pf1*wAlQr@)&_m5
I@pE(I|ieX3;hhCK+$iA<<IuQ?%>C)XGfA1k_sD*$EcDkOzD<sIHPI*^t7bm?9O$quAhE*d>dl~lhE4^D^gePS`pLW1UVVt-+Y%;yt8o^Pd$}<ABZgRkHyGn
5z^@8q%86)6UG&^?4L}rDmJ?@S79q^T31Mc8};^?Qu&H`;*0tiTw)S{oqDAYwnVl%3847h0!H4_bC?=LX#mD=UbZQjmV>oK2O2S5`^ZwD(m+vzA**Azu`Q@B
T}S6hPB7+C66N@`|5)<erjK>YP8{PNHG}DxFdKwH&#2o_6Oqzn!v94}YU+YqW&ioR*;5fL2$O1gDUX>ZHX58la(0_Peugp_a3b#OZ?wbttNPp12gR=Ra8^3q
3zrcVN}Ut+YI%==wXY$5-cZD_v`Xjvl{Ng6WM1hrmp1j;o|Jnd!(8+WR^Rb`#C@Dt!t7+KT%`;Ty=(5*i=45=0nFe0iNL^+xYZdh!qM_=@&rPlKR6aH1U+nM
uIDt*vgbiIR?SyhM{}wM*PZ6&+}q<yOPF2lgbElWTe0HiGnV@Mhh>mM&uaN1OgVg5$itrAr+XI#_l)1LnN~64q9*LMVE;Z)Fs@`GejV*+Vi8d`mB{Ec6CzBo
X6@nUQeD#!hZrT9e_Etcd{wbl&<go3<H_B%+X5ZE;8?OAE&Z#|x!y2YS`ki^n6NzAKxkop!n3P;zXJ)hI+0om3+@O%g60&~no6v3nJQu>GoL3Mj4YpIj;HQ3
)25ES>x*&y71pQnN0G)KxPWjyl2a<DRGG=YAn-MPlbUEO8)+)Xi3As8^s)TbpJIh8@5)MBULoWU=g!EF%*3wTj3<j?DBm21jl4wsCncA}4n|`b4;wZRZdD>b
{-IFuJ7%)r-1k=L&HA&QBBhu~`TnwS$Aq3?PFn|wgl(`rVCUm4WgneCynAWGliG`&lG)qeA}O8W@fzo1zBfdn@JAE3Vyn=t;JncQ8o(izxPl44PAPkgi0+wp
aN@%OBA^gz4dsf|rapXy{e3qAn}fwf(N!c(F6~(xYm$EHq~X-gd6@5w?iGOBUO(%Kp-N>gZ+Xz~dVM>`O2ZF-0~BG+3SZk3Dw86CKuJ%0z^Nne&f{S*R*{Y}
`+(?i0(pg6hocIzR)#?(?x7^NxFnN}gV8yW4v}Vrv=KMbxL;_esLr_&2s5y!u~UbmU7uagkgxW4fJ)yS;LT4wGEqt~?kDy1q{F>k8#!{7s(xUQg#gg_yn8P_
R%D?-|E7JJm7E9u8^k;VxVjCEtIaiAucGUel5#UexcU@?8#u9%4Tbu<FKkW`;oNMpF7efW+Q81(gVkD9uEOE+Oc*$n^&{X^o1Fp<kAX=khR;At(<b4iBPQHp
R;d&Q-rK?^+KUqI2HGVxH8bP==zm>9zdA|*ls7As46EXsym}9{Z3>a%H?VkbSm6N*1ZQH3O&t*250XF}q0h~q>bnSO3qc7!(u~hHRs+OZ%C7cvz$y7xNBD6X
F;iz$EW=IwPnFvC32fE#HrKJCFG?akBB7jY)zEr{J9j}Gd)3md7(8Ql2N#c`)J&y?Qh1Ky{JB$WZn_{rxCbn;sRJf*?CCbj%ZZjf>)!r<Kl<u8zMl62)2xC&
GZF9$DCdTT{5GsvlZt%#E116zww>26*6t({*MaQf6ZFamPpPzp<;Rhw`L`fOjhUVv=6<O!hv<=pPnv7a2tI`&ycCJ82^N8niN-+~P+4Gxke~ql+?m4!YX9_W
Az|r8E@r>3dwtCe9W0l#Si|rchtSDUq1Lc6GP<dP7YfxbGB)<dX3Bj|%k76}A@{4ha5L5@tak5K_ri2d7)gN1avs0ZcftC?fjRK*WS*s=H)4kcdFZueuK{cE
)e?e+N>v8?lpfV!$LIgD3t}Ft@Tr%p<#(^Jx+PSi`6v4NUni3UXf)C1H-&vfEYo0gzhkgq%g961wh+F|iF(j@6o9=aUnono%<$E&i=5l8wUZ)-8}2W(68bU%
1<tX19a_=wL@t)oRrH*2$W{RE1iOPXAWN)@`Tl+bS@4l!+BnV|>#iP3VSt>)(}gh8UhQJo#iSz4qM1`o2->9E07PkN_8O}7@HxzE{mE#mVb519K8*as)_*0C
etEYsg|RpEBJPoMXR@WQP9t0biEEx+Rgis2W^GC1uMnk}kX-&``Mr+V+!`S?G@fhwOZ#b8u@%WVWu#;jGgR8Zfe>$Z2vy=YRi{mc$KF~ye*Gk<`z47+h<Rwk
Upwz<D`J~UMga8s1rMzlV<+%DujIdE1T2M+dJau=0)Hq%sZ<ZdV7+Sg^$Vlb2(cBQr5kd1m9DUYDevjJt{PtswpLTQ7A3MFB`~ZcZ|}uoYNIZT06m*SEZP9J
A7R`}xJ#jiD&aw8he{?#dI+n{hCfd!&rq+Ct7cw*g^&-q4BJWWLE2c~+g3+Vxht>R*qE+aF4>}?-1AZys_VbX-Hr-t-n$kxf9nsOutX$Yw~wJV@2Ww;AwVW&
cN_bMiM)<QIj9%mZKKaO%DJb&)cbTQ1%MM@1j=d0Qv`0#LQLhvM^N6<uUW%a4B6hYtpnGYlivYh&L0y;`qD!mMEF6dCL0xZhFkiA=hw7}g^nZ+{55uCzhjbv
;vJ-kiITjJxU7-UFg20j?A08K#L!56OPeoAx6SR{PxF$R#N%OD<vk@1*Auaij2LQ7G<!S7-xI#SsU6Er_QNTA$GLyHxy#=kMHy@r=o}LFVGew{LU(o*YKQ%y
QWz~%<HpI!eED?2Ftu6h3x<$IyyA5FH@NCVWx0T&%;w?2o>Lh*(}(PPUHR2HH<v}}YY^LZ>#%_iH<cM&*VNRCr&lsFfmeY~Az<_tG7MDZC>CG|5{tB%T@Haz
mP;6%gvk9QjV>3}#P&9;N0`$KB+AL39R8b3FZgXjCL{OsJqbAMf^Q05<CUYq2V`5w&6fHdgY{#wOxG;1Am{%u?=xpXuUX(K4wm*Ae?g3K#M3W+=Q-Df9UorV
dtG&A1+ERD`@B{#u2uQVc0JopFTz9cE#qS_;o?KIf6{(LcNXi^%Wc_aDjNfRapWm0*f%$|8QS}UAMC~u9HGWN@)}#5J%1^-%-oOd&GRn<J|bb}k46c*L4SRQ
ExPud+8V@6{<^}A2Db))OuHn!lfb$!bUBtnR>!+!``<l2L~oOE(R282Id;%8Yh8N@beE#M)t4N;GW|x9ZI9D>mfs<xRqdi+Z!S%G*;6?b`JonkORHFCF#V=N
n?P%0+#_X;{@(evlZn{kKvFur7>|fc$@{4&=eMClgD7Y1epS&x;=@+2qz+Fky(tR-VXxg6rG779EF6U)#0$(cIdCLFxVOMjfTReqc`ccZ17I~U%p1Fcct=Dc
WgT;i8zP9`wkM*YEr~Os#eyOl1bIXp!&lVC4@~9Z^4bkof>`)WQH154b?ml=P@L8?NrwEc;YWH!@Q8W6hvtm!IIgTUpyz+*&%09YahS{$%Tx56-uT+<#56J!
r{k<tE~MCWR9ugJ!`>Y`A`h@wlH{$Z7v5>+Jq%c9GlUB|Up=Ct|BKc1k-?ePWHoeHOMl;Y5q~cySuYt{ab|esqv=sm<zl2}vH-x4MoQ${BPk63lpL%nH}31g
#+>Up0?dq;R_=<iZUnTS<eSBhF2uAvH&`lmh(j<E$vPz5E(M}ji-pMjDY2H9N+<37&R0ejolA9e>Wy8E>{ij5azv4?)ac$DK6m95PVl8!7#t*}D6SnVI0<qJ
VN3z3c9!0CCgXfJN5DYPJukfAb*ilNWdHZcG#KjV6~<<)NmlOcG}ZlHgTcxr)e!qW4U#p1b^jNBDXt#(_%Z{k@&vpt_2Ev74IkFeW{lM3vg5slLmLlUzQ17%
+ffxnB_WiEj(c!<Z(#2ghkdt_X(ObKXTOs-5teYz6u~g^O^a(TgTPHj`gy!RVQTMYmUBPNazqmRv6OzI-0m)3*qU?I=5hO10_h>}!K%0S1q+W6PlTxIUz{*j
u7z$uR5~9xD}LfLtT*(|(q*0N$NavR);JIJ8s2)Pzh-8BZrv_`?YnTi8dG4w43Is&9xQ<WriBaOw)wu=hI<*J5eW&E+!56$50+Q*{SC5IF3@CG1`OcS0|)LJ
IKT}+=}I5@#7e$W+oV?ff>>lc&P}vk7B**n-a$SowRk%x8Yrg^<QO3&-YrHw-f;U-ChDp;HY`O03d_J>9X)q5^F@M5)C?3*OwdK8%`q7*xRoQ;3PhCz&|Y>X
QAdbZjfhYTe-XIRRT-hc^t_=qwZ&+yJ;*OKK`t^i(etL6*WYWCqLh*Xi&l@15I=6e%dT7Cw!u7TKeOHd*X`L8E>lDf2EcqNm=rgmo?6zZB|cEVBXYn$g5~LJ
{6f8lvYyh#cym+>%`yVOTNj8~4TuE-fYzsVAf-2;8W;Sy`0Q0jVFMsaDGp*NJ#K0tmHu1f`5efIkWk*kVbOzAd3>JIs6~1BzR&Bxec%9$w!h``>)JTe-sAHw
GL1NJ@8m!r_m=XH`sP8+aXIJSlFXDs6lll9(tkLM|9KtS5vdONsGZ=g0>6;76{D6Ri3>oaoA@2$kR7Fcy>ezW))lWIFo}yD+_2HUp)y4ER~D;9SW`r9iXVOK
&F&J-%ytDN?-fngH*dwWDU(Pk%n<!fiMx$pw>MZ=&eSG{jf?UMM?6Br;S_U3-#>3AWY+xoR1D~Eu<`hRc)NxYLk*Ib;*csbCOKBQ(lg7rNEClUlY3R_{HQ*s
Q`|7GG0Uw<s<-5XcD%8`j4Mz7QE^&GB3dpOvhqARFx2zloC*>=l4T;%^*cHq>u8bu%2Si>1`|R~mkKELSgrk}IH=3zOZxr^%gIiI76sAr4r=Kmo34!`TWY^*
!IDCS<n~)8cQdh}cend-UK0k}eNiIqflUh!0cBTaRFJ6RKl2p*{m1l;H-|15iy>}A_uuijAtTU}L6jm8xkpibaij0rSXP;=-fZhd8l0b0FxDx&NnvliO-eYs
+7W_$EQ#t8fIiPENyJRre9EH){nn+@32_02-m=JNUJ1%(*SbD~kL7x29pd5h=^$-dB~Kw{TG)%3ivCM0!(Xsyk;aXJ`?(VRVo;<AEQ*nSC6cPaO_`HYIC8Zv
qXZ5i)t2oa*w}sby~&=iM5`<9h$dNzi1Q<NRvdsJ(`^~*+f8F;^GBL<zGX4nFft5g+wNrtQM>UZ*yxS;lTLv`cqpD}vAdp}BD_jaC@JGzN`j6jYGSi;TewVk
mZeq#prNW3Ycir=2eYQ?h$8K65fmcAUA*=LMR)cw+;Ng5b-_`KRoM`~=O?Xbe$3fk_mm~@1qkoPf}UlQzwi8eGVI7n6k~NhfV~?EU}%WqE7SyetDkI05?YNH
d>SX>4vCX1W<12?=($;$biU3>G~LpWKLrkB)QI?B=y$L&wZn#m+pXt|VP|dwxB8+Mc&my5Ug7m2)gRni;C};<qjMj3pA@1Ij6Mo%88mQrPsLq_@GEN0tqncs
tHrhPkE+veex;E)2F2v})8_XQ8WxkowP(h-J}#Oyw(AZTswyXs)v=&T^9JQPBn^jj8j^9C-n$wPG0K_A9JxEWc<Dv?jP^JY^7UW!=*_pGlat4@Agd)04UDy`
CdrK~GXv0e*I9xr1FP?U6<e&(VJV5+-_|9z9dE4$|Av+He51nY9R$tr6&tR2GahRSU#4<`SF59-EniTYc@bM)<FPY#1v);^Tlg*S2sjLwg%d2@f1_c?2><&P
z!z8oVn`4or=Fm0*`(%FA^U72Tok9G>k(%UQ@sj`N!!Ti6#ZKM&&wDdDwk2)f@}-&D*BBE7bUX&)VFS^uee*!`QVwEOhM#Pb7{MArYNBxG+-hZhFfL_oUkYx
AKIW<PF^b`_1hT9qlhQOOA0x2U){c#ud|+APc59%%usq61p#`>9M!g*IwmC=!)Wd$c>EZRO&43HB|iT*uD8b?gMK+-d#-US<-#L1=RMRBPVoOSy>7T+`jKpp
9k~5xVeZTwd5Ii!2;K~!pOvto$Y#M1l!mFcFX2k41to&tH=Vv~i4HV4TyF2&Mq<NI{dCviWG-(p{P$-2f32j%&wU(60SqV}>I)M}l9F!6B&k-oLT5X;EPs1T
Ka0!)<dvi+`3f%myoZovoG4K8I}S<Ow;+m_#Q1C|^|s&BuKl%K#c^Sr>U0wRC#i_XuoFr%mx1xQZMQT2@tWeL%LPA)qX>!=`Ykh;Z_+Bx1~I6?IMFIZ#b3l+
v;(Xu2U(32Ly;E87-bO<k_=Q-3Y1i=hbTKuXhu(Tg!956xT|3|ngo)p0VzlXS*gQnH)OeFGe=za`z@CE)bADYPLu#bmJ*O<Kp$Qk&Lr@fP*@k88v-zwA`o^!
SJL$5P;>}#RcVo5L($K{B9#~Bk{kUz*%_pT=+^;HsC@89Q%}h_+(;;*WrX$;h<KdaRCXE=E&%)XJ`Kd1fB?4~%p#2$<lsmTG$Hfv`q8M4<$5L>jCaoSD}MfO
^Ej%M)XX=TOQ`SkJu5y2Oe2+Yx0%65K<GNPxLyVRPXywps+3u~_X>j+&k?XKO*{(y`V#xsrya@JReW#gAd1s+$^vQWGn}{|*7fq{9mkJ5<Em<z<b2*aD8q2o
uPrC*Fo1AhKYtFB6vpsQrY+ozn6sao(yrowD6>I7q~H=_?n}g=_g0AgSqDf+B~r9}7$!E5q}s1x0lfP8xse;p!0tWUEH1I7eOfRV4;?sqQNb=4;=H48)=^Pa
^keM$L_a+P<HxafD<Ox;NAmB9%S2n0!S*jiSS-ZSI(XKcx0O9>QJ0Q@glUk&ywT`c1G<ADyH<%>nscla4F2!tQb4)wxsEb}m>Y$XJ?^kmLKb+5dIdA}AA+^z
{m1QRU0MkgPW9#D+>Q%qd52@m&z7aB0Y>TZU?)5`l9K;pyBSW1MB4nd4iTVlqlB~t5VBoFWZVz1<guo^)nh{gB8UW5Z}r05M)-rY1`>^^tG+j}sxz7fThWif
$n!_scp!po>dqA7>vSd4s!sxHe5=&<rtZ?7J-d?p>(DTBn;>rE0g=xN)ha}*iQF~OIuhP2=PQ>z6i}n5yIc((Wvn+aRA70Bb|!Q^$6#u`oni=|c@Thqh{g_I
^BA#)lPY(G7{VFLeG=^Qgi-=3;5{kJ%1jU(8D<m*?>^Y0Qh%+nLZB3k|8P_>7j~+lqglpAT<B_y^w<Y1Ck{B9%uEiFo)gIyq^gHgZruo#Z5yxgGdNj?vio2w
CI}V$`IEmrc{s%!jM~qnmjV-NT<&kT5FAAHve`zSYZ*z2>)RSk_+AofbUDUzkdaddw239t78rJqX)DvO&0Q<*d-=qgMiqK?uhgR1Z7GA|CqLFZ+L&5iNfYM6
bx8J{;c6kugGoX__D<@f%Ad3XhmkB+WoAN4SCEp|^62tBpgS$JPF{+beJ|yNU-ilM?0GTJC(yE6P*M2#Tb*jV`hH^py>{GE?znlR`*2RzKZe}X_sKC0&6jnF
?+61~0jzPZGNRvyE3m$6d$>S%b$p%;N0J<~HY1W1HY(z4snS1wJOb2GCxYm;j`d%W02Y4NU%pz$<meAPP!$8pef5>cY?u#Xu~`MW!_C;K<5SW*Y)qiuP#At5
c^T~u7kI~cRVIu!R;q?ONIW2E_$^4X$*cb(o&Q}lnV=slDC*(sCh!)W5BIZXdM^?-@L-5Ksv9s7`n8CWU0}!?{W)!b`=UeKwfSlQhACvVlZ@q%0PJp^753Zu
>>}nE#q8?8+upQXdHTP@KmfR@2RNa=ItX?6^F8Yb95cjZ8eaP!+EmA}sNMu-GZ64qScL|vVAgaj3OYcK)ncD2wxSHt8vF;pnv)Bt4iMy!a8bcv?2PNYn8l*t
CQ$fJ3q@tQGXK0NY^yR3zpgG7O9wC`1fRW$`#d9GBrDrm19JO$%e=`(E#r&(@ASyY+oIhLA|(pSxcJAFCouyK(1FK>EbR)hF}zB^&GHs+Y!fadcS?&3jN%$q
^+Eq9cnkA?zE+Gwp|9d^oZc9@ezpE13b~fwrVjNniq6^GZR?H?HT1EouP~J2OyDuOr{6uLFlhzW0mBLlDc&MEHUpI@%sN!nDjt*4b5<?PIH555H>8uXL`JzW
1N;Hk>nHH%W=ce&VZ|1r0k~34EqiiJ1Fz*yeR(w1ggA5!BB`FcbZ!xv!1V)MpVqgpQNKre4&A5I?r;R{))NkC=PAC9u0dBS@zhMT&M0f+?`W&o@-5jP42&0r
jE88q{Gi%&%{aAQ^`CC<onJVV$(#plFY+Y`q7I|SZPtCf(GtUXjRI6w{|&{H1UJ({nBKsOntl<$<EvjSzF~eiR<2OK!tQXB^8{TVzlTR@ie}aNgvHH0XkYOl
UZ!$lZA<Vhm`)IE3r;V08Yw~Nn?9WS2fm_op%j4KYki|}Ax>=q5hgAe%-P{L<N7<If`~%Bq@O+Y7H~Fns?kEFr%lACX|=UySbqT!gRTs#58*uwpE%9@(ufJB
jr8hh-*P_A%35}?WDi-q0x&yhFOCh?hNJ+<j;ro0moC&ede&YR4E%*=30s)zcRaQ8!%DY~rLQd8Dv<<AmtGHwFFfL&oMg^bnmj+>kIO)*)R#vY;@HbG)qanA
fps+VzEnVI8$z(uP?$_ZhJ#43Zox{a&NAnBF#JO;uUwW+vsx|{WvR(k@P6ZEebD+!`NM7ZlYp*!KrmyL`dTrPl|#N3DSVi~o83E=qZF5~%-egv*AKPJ#;g1O
t4SgI^r?$#;x3v%@uREf08hW1e+MUo!V0t@c%BYZ_iJiUMg{o~s_4Cgs4{g5r^ET{V=hje412&ugr`-1bNb+Nu(@>n1z9X5{IJ%&E_3pNSTj8$*Z2T)e05Tp
C@$_l_FTNrqZKwSW=!!I>SI^pl>}YT)%TXwknPD>0McwT0WGY8)1Wj6yeUKtTODC-^c9VSx-b@O$V9r?lnOaqa(4UK@G9le0W_jlZpSqbuOXC*RMaSHJbsq_
9`egm4zZ(09)35+P|{xEyqIXk(oJ>?tNm_~7thbR9h|W>1PAj*oIBmoUC{MxkZUBVAR>S?(st)W*;cpZ@Az2U5O1?(Q`3z>#^}h#nL9Z?7X|MuEbrHPk}1(<
xW~xxJ9H4O_}G&<&HNHBP9WeyH*Zn$@YI)ZKS5x|1ruVW`O5R}a{*+XiLTwN_|^#&o(jyG#Kq@t0Sh~O#Le6)Ko^N%kgDyof@k9G!Y)Q$C1$^b2cBVbJMfU(
ZTHnspQiqP@0;AMb3#9{GNvbo!dmm8UKQ38Q8QwknVk~FOs0B-<ii#Mj8y5SRKFjbycw~{{Vg8FKg!B3;_PQh0)b2ASe|=mBlarR)PKwBeLFUKZyqsl=-Iz{
=JAsxjcuW7!61DDNd4e}x9Rm?%+v#}W&>$R<OZLCA<&dUE#E$v@${Msn2}+V8>so_n56Fx6;|`bR$V@>WMfHF6wPhN{yF>)PEL>nDb#F6JkvdJW^!^NePYfG
_R5Mev(%Q);FoX^+m__EM5pd-fFH$FLd6gjD;*xLN(Pxw!L$Bq+1v^b0e`gMny7o}{b<5!75(Q^#-#6l^^XRk62&D$1jqNBuwV=?G&?Yk8v$Ww?jYvst);_O
nVvzjJMESnex=J=*!HJ(btjtx(xmTJ+8r<>s!b0k0#r0=yymO(YQouvcQ0X3_MS_ZvjRlGC_wMXef%91GV?kk<#}$@t`y%~oM|c%b;&7~*hxJ9tXQCrb<?BL
y=vL$VI~iT_Aoj_O`p^pOi^X;d}K);!wGT>RV8%6OQ84d`boJ1<Y?&YtAlv+V68rb95}tbP1Q-sr^8!tL+^0Hs%@L__h3ZtQ=6_kJasIJ?E|{p^CuW0i^(L7
pJ()G*l;!7tnb{nbt?>f$Kb*5`Cq!x=M27KNQHf7pxfF?3q@5Ll3tFa%a5iq;clbHf_jrAm7t;T60Sd8yDl*S&wNZwj7S!Gog26E4v=OnsL)^ZoE_cgZIXEj
gow+5Qn3RAgggJJ5yYr>BzH%NXW{zZ`t-4b2VwZzyY=O2ITeEd{H^QVcg(jYe@Gg;M~u?fqP)M|Mqt(ZDT*okKY}J0KN?Sd(^Q)9+!*ghV*8G!>(1dB@YqdQ
2c=@w6rT~|=>Me81$*;nFY5vmv*xGof3*6dvew#Bat$L2W~|?jz=aO&vQZw$_~cq91f;{Mqj~KX_L!7ghvWy<JCkl|3-zat$vMmIK+uJB2Y>fDsJgE%rs5RG
42^{4zRfbR_&!U3t4YE#_L<Gzpv|jcI0u&JcWdOI@%_I@HBI6NaaOL=%=4C$gJ@1^V13BV5+s@*>&ijLGuM%wo$;GMW2W<W;I^DCu;Vg%DAr>+ACvU>e#@T6
<lz5y<0R@<x3u8q7+n>wm76E(YFrO(xTRlUE{greU1`TDbdjR7^}T7c*eA(5*1q-0R%YYH>?6K`l}o!IGj-rxUBu*|Y@cZ2$y@9wmuIKL09uo~I2=&tn+4CI
f6<u9`t$&E===YbWbttqW6O)ANC>4DF5m114YKd0#X3{b5Ec*6G|v?Uq=Xg-CT0g#;%+)pUHrKJsgsVlG5M@-aYd8FM0<PQXN8pg8|k<i#=DNUaHjZP?@b6`
*}V32`DXXMj4#wg&yWFL;k`m5p=QWuy2B}d(A)oU)3MTVsT?TtQ7p04Ihw)!36{B-&9Q<13B)8S9EugELMXu6>GSAn3ft1N3bek)wXR5NiG24R(;2syZ}YCo
pnQc!sm)xm!&X;pT9?ZPw9Y)et+Tq<6^<*c!v!pxKBhC9^jJZUsHewW3=m%me+5F13cahZzCHoZNwA$4W8>(gsa0{#TVquvj-C=|=4;JuiP)FG6FCFodG$~b
dpjx3LSoNV<MoThvvf2?)M=jAOI9{*UvW{K7s9X|>NcoI6cKV(#FwHB1J)6ZWtLQ-=o=z>!&|Le%Kfj5W-Le9gWi3!{VwiS0!4!|Zbqd_XD|;^<OCF#1Ij?D
n{{^3oAfW#XRp`T;r96s=z#tR4~;~Ym5aJSF@0fvs-#=omHT8P;T`)?ORG|ugBp)~u}OaY&(K$X*5P5vjP22m+QmTbS5@I2J#vLzmJGg^cbDqwLj!6oeI7>W
iySE#6qW_FpC9AI1yr-Wk24jp;C)q7qPJ;BkI1_3ZL|u12u}peoo5W@r~8PTS$~yrGdYdE??83?+G5^hQ+)&#TgmsTd?}I}P1ANa<Uob>j}?IDv*`kq{>elk
oO&q@w@?4``uEm+f8?h&31l+CKd&T$7r<SN<;*gZDc_DMLaM{j`O0xVfi!(21K6F&g>~Z3g=uTuRIbbYeP8ClQhM107%FrgJG8FZ!hE(_@@U1y*&>ERZ+n|<
<8RJ5eXQ~NsMn~C#6mO6PxV~*taF`SO4B61tLGmunN9@q)>?gA+wvJf%IEBb<hyM5ZHY<$y;YsCg5z~B=18lwYs?Cc9aPXx-}56gIUgoY@JGb@xU&i9^&Iw=
(btwH#>V>EWd;n}HHBOBok?9bjMuBN5qo`M04g3Xa_I-#Aodg&ec=_;lVS=8!w&R<Jm|9<S{AElt`cD*Tbe#dlh4X<wlV=Jc*>YGJpy0#Ue8!$Rh}OLzQbZX
ob>;p;Q>j6hX+VTm4Bz1);!fC3>U%RK%J0ORDiXED#V3;07jAQe0;Dl|9OVfMtn{0_8(7B<tYKBpIBRf*+K(Gv{NYLslPn8Lu8A?Wx>IT&kkL}1Jt~UEXf+4
+@?}oL6;I+ME-YymkcI;caP_)fT;v!=OAfkQ*J3*3^fymh-B;dvPixup{(yJ-^)+r%8W|q#lbS!)JI8N?m)Ca_;hOlc4;V&z{$yIbPSBEW+{_6ghwHef3hRc
QCJ^%+q1F{AB<a84EL9o3|kVSE=Ja2Mt-=Yo8U~;K^Pfd_`lY$2SP^)Ea35?F4oz1FRFO7ZL7beSNUc!%n~8-U>lS`iG0@!jir=tcePz&7X*}=VRe~9#B>3n
ny8LQ9p_@f6b}y=@_T>%DnI;^E$t(hg9wkY%IzZdq#XN2X!5YE{1kxD0%qg_`8ABg5BDE@Z7q~Z98oQHo6UqUH5^YCQWXN*6gKD+dcY4?)3Hle$%pKFxlvI0
@Wo}2^<wWHgs7|VUsekIPP>IP$~UaR%9f^75tgUR=%i$!I>Ygmv3Z8hnR%$k;xKUbX*BI|bbEA$t$Um-A<NyqB5w5FR=8t|9p?#qV$M^_5ECv$qB7XUC`>QI
hqKz<T(?7P%|gnR+iM38o1FE!M5PbUX7AB51RoW$k$1uWs{#h$`x@6=nyG~UeTqt1qcYCl1ub5^j6xsF&gi^!`|)gMPa8$2feJH2080N)()<NYpf6z;$;Jg3
niT*=<-<bS`zR}ig*2zk=*dVWtbRW%HL<8$3e?uN%4IIiT-&;F8?TCdSTj}s4hr;1@3it|nKOM|^~<|1Y6J6T=@zE$qBPqt_#~DAii#Wu*CCyk?TvtiZL3Tn
gop4NP9Q2}ReE_UX#D?MfP}_TK_^7s)rPv9Tc?jgTZ)+{bQ^gdX5sU-I+^P{jj0q1)!M3`KzL$2;V9^#E)RW+w-_{E4O%{FbR)3d6MMfxOIq4d8Cl*yKfR4n
-~Zh`Z+tTyAat4IuXm(Oh7EQiK%hVpnf<rhnBYhuR#!bU)(TciTF&Wij<Um5f@51ia*1kIC6R^@_FSn)K7e1%1fkbM4gvjPKYh>9o*PN9N_b-uh2Yp};9@nh
YU5iZLN=NZ0b>y^`SgTFgxTTsvAM13Px=zC#l<K+(o11&hvq1b?VbeOHwdZgN-SW>Q=37y|CWG>jg``H9mWq&eNMFYmil0zFYd*?eTh<2{}&P4Mq(d^kmfh6
n-w(H@llsg%!CWRJ_0+Zt~1Ro)yVZwTP{+FQF?F(pJS;I03M*``59d2smZ!A$;G*8>zT=XjCPD#e=4v4XJL{uxlhM+Hy}^tLYiZ=Zm}a#78Fhp#nCHy-*Yii
I{r8+q@$Np>XTO_gyp^MW^X!oeDiK^Dd6#CN~(A4xiF~A(<Pk$p!TTnVQpYznrCTws6M@%EaqzWq;aekZBjqpLpxeXJ2Ej;Y#K>}(S;^<l^<6x6N&G8?b<Cq
q+$pbT`jn+WX-{v;5lj!U~N~|zVi|aPkv!@LrJIwlv;U@Z^r+~Y|ccKKAj0!t14Q64C@6OqaK~yZ12&+o$ldfYSm=`oc11Uk{*m0;dsCWXwuF&TwJlenq#3l
{9)$fD6n(=yLjz}eXsr;q`l#^_Hw@nt|iaP#!*1?vo2sNfr=K`JgLuoYZSMWp=lDbuih53%E2vSTxMLs1PY~U=na}%Y%gHM@I$vBCv;-Be`vyQ9h&qbwL;%)
CobKd0o89etcxsF_{f~6xdoIAN4C5$r|lyGi?F9sOu&JcdmcVnmEU1jtvJbi(E?+GmMBH$^gZ1l2;lC-9?8prjWen#u9*xyu84FV9b|pPectDCNh@~2I(8U5
0&mHiFoKX4BCS%AFi1yXTtSx~6{Sed3-XeBU(#mDJSLb<UV$hhaDvkmAV-??F3Uv28XVvu-;d<mO!yH#@J(0kIB7pw6zkhRkrL&J5O5y{_O=XV*V@M4>8(UA
9-R&U4xOv|XKPQzzM1C&-I+%eWP87}<KhD$WmZadfX562Qd(+-{bn67Xd-`cxfsI(YV7i}FB*K>EF2mgA0Fa49Euxi#D6<G;^t}zcoCsV40RO|Jml5%d&ET%
oj=h>)6L+KNdP{7ICs9S-4Xe*JT=vtxW*-yPZM8<e#;&*p!}mZgt>JB5}>yDuUrYqE^KAYkw!naloQ%_OjvxX&mBm!J9y8Xw{sKyr)}mW_3>f-2Z3a*M!T|#
VSg%`Li)`<{NCcz&wAqC!rWF8(&>sV#zYTckiXnT1@wkp`frm?c_X)gRNLw_#aa<;H2rO9Z<an%jnD?6W*s|(bONyA)pT#n-Ssdpb(IqA>o<pxp!@69kVkFA
*sS6rggDzwFb=&os8;3e+b`q4vxYf6I<gIqTn=(opZRiwrmK0bxty;PZ`q#fHgi{6G`*cDCJ3bar|C{(h+GW}kyur+gzn&80=rzrJm4czJ*_aYSO%C`dAE5p
CaMHZVyE)quT@LJpkeT)6bvNLo2pl4I3Vq#rp)>sq&33gZ52z423$SCnZSzItC-_ysVlq5xtb^nNFw<$(<Ca8G0qMOZu)Uh+A~FK4?(ozTsUdA<Y66q>WXf&
+Tg?s)J3QD030q$Y07Ih+<U1dG*X1D6qM^L{3qyvw78%86TokQO8gAF+2^}+aF&56<FbW^kSVKg?i-A^dF=x<IfB?i72`lu_=ZqhbuI#6*2s+9_F-a5Nb*^d
JW!?a&5VUFX$luQn|o7npe-prINSiXyaDHJJvifVFIh^uhqN92yx7M%Gc3BXp`W?GokjRCS#i8cIERP<<aB#-)fq6iS6AiC@`Z1Dq4A1tvLFA5x^c}41}&EL
E+v5UwMR4${E}1Zo5F}R*T3yhach?4KcZYRp&8`#V{Un%vGa@+voD{nbDd$7l0W7ZrOOS^6Iiby|2gH_wvNO7@mZkJ=MB`zZl7zyixzJG+rLOqR1&Ge%`;J7
!C%5+j^wF%wig3iVB<@mvCHCBb{UXd^Wu3$OEDc7R;^6aN#(7;|ImFZMuWrF9)q)-=v!#!myp@78W~4eBXKmt-KGN~4X4i?an2^3z+Vs|e1=6~fk{K6=~zz6
8pd=KISdf<;6b_t1op@h&0~m*in+#XU=LQ`2R{>6k(f6gaa`a;#GO@CPjo%fs7q}_MPBr4&X6Su11YCadu&uo8pe4QW|@N*T6pc9FIoXkWd_VCHEjw8Gbt~N
B`!Y&ciR{Mix)^fSahwe{yFE^=m=m75U#j9ksc=|w<wE0rFN$kQo<+eI~Ahw3vyHK`{!Q>wk5|YPO<W}zH~A$=q@F=Euu;&sjSrq0zP~km%KUq_$l^juBcbm
c@>yqhx7nN4OgaqME<al%x?!@_tJ0aGKHO~*EU2h^24c)4EzRDz}h|4O8^YWObryW2asbTZhE|V$QuMX89s6oz_006vPo=vrN+mPvhHJdOtii(XK-i9kESk}
QmJuAAD_yd85G%nq9FnQut>Hr?fa_i4(YYazA4dHTh)iXT_q!~W<8<z<z`Mv($an2mIh8TuBUa-w_mMc2Q-Dy%GQMz2VF;Yg};>lm}{d}D-^6xk8kUa&SM3q
5q)cZESlq=X(uA`KuYVO?+g)DEs53<ZKTamtOL{cQ~EarC)ndGijUi8Y^rha)DNo+!B+8_00C$voJTB$Q8}#q0h;JkVb+ii$^|tKrf*?sah1Y~mBk;N&H6MG
;cE0OTqYE7;<oha9Jlaebaf5UVYW0n(;vkTZ8OGi;szoPru<AvZJ-9Mg?%^xyhRAe){R9C{qPUhco83F0b+Gh-6NWWnmK~3-{JI<lC~R1{5mtV#DAU+?7>Ja
T2oh07(`}Df)i%Ai}d<00#UGeQjhUE3-5SVC6lrTXHygf!g^&+w*6_F-DFD&RudvPUx7msZ3%R-0y=eOo8vgjFx+_EE7xKv=cFP=R&3JRowny5XZ1&xU()>J
F{C?_6&BC~G_GW3m&KQVx^%UAeGz^JYG2A=CG(rXce&M$GoNQ`dJI%u+l_ygLJCXv2_sn$%hbR`SqNpe(rSY!ElrpW&lT7gU{?TmKtc6Dbc>xqQ=3ut3=sBd
^hu$YmN6^{OMZm4)YEgzX=4_1gln<V$NNm~3KRu`+y|tYY7h>JIw%_jS?@&F0<W^YeIQ5)MdWYkNZ)R6mShmYokqIYzg_+t)g@6H&H-|+<AK=Hd#BEmFy|S%
f$1N`)k_iy(;#gb$ao;2hEi!<B5$6WO!uf{ac?gdd^BNjL6+rpE3{a&iIPEe`8g19z7gXS>>sce`N~{ZJ^@l+ipS?fb-dS@ubG%1f(esRWgR?|W3}nciI@yB
|3&=b!jtqA3&ysfBuBDr6bC{`+0i!_9!^@8Bx8&7R9%?yilN%GDNdx97ngrw9ox%-97$w&lx;X!Fhbq~9Hb<Nro!LT?`L)-#=f?UnVJjrvmBpSdW-C+@amE}
jW=(-^;g1_CcH$f{hz<XP3gN(Hxv0wens$h_{-b*W1Q<9S;4S5Rs7u3>JW3V7T_z6lgL8wPUiD5y0&<d0xX-#1-qlVFJlD?5QYyPY6Y(#{l03HC8y!5Pe3w6
axsG>6iIcsbtA9-<An^!R8V%ldm7X(G?kY;B(nr49vi5QRr0VYFu77lD?Jyp-wgWo_8(rJ_K)9ByrcgGFWM`fw5xglwyBBpP|o$XzM;yM|EJ$Y*W~3-(0T|H
fphWk4KNrVXl+Mse~9NbiQ|fvdXTWG$H6{eLEL$Xo^kNlG2!4VHedlZB}A3ML>OSdAgASXHO`8Lj5b>bPE)H)k1Y1)eg^!FOTyrVH8>Pkn4{XorF6KCXGhM}
Cy$7eK4l#?^R#f%W4)T_!XFvad`OpzTb=>B;)5}UqM#N5cj#A{POj=qt)$8ZEGv>E=CcDyGK4Sw5bofGgF}f)<#X^`x+91y0FvydARc(LQ8JM^Ba8i-1XT-p
)7$d;%3L??#Gp4CL(f+6MGiTnulKC4kFZLXIP+%Y-eMWsiWP_&yhjjbb{9{8WxZmKG+wJPAzQ+Qa5*_9MH$Kruzk9aa||<eRGhg%#kv6{tq%&Lpng5sqY)^x
v88&MUJI~#&!#!q)Dzq}TW-XBDoN0X8)^VMT6DnSO05|d-P|C!8}e*UUp<qpw_;q}<ogk-2D{f@Fz%0o>^ullCoqgwmH-Gyp_=Hgh=g_twDdW_1i7=$Hud@Y
z5fDn)kia)d>0_(h$7=7o~3~ys#gM=BLXTGf|Ty-?r49XoA5;%#0C<leEu#zu{P5l8DuyNrw1b2XMYg$Ia_EC7?#RPV>E6j2hi=0e9YEJTH|T^sO>!`Zj^et
qiky;HS-`HMuF6eAW^fqNQdhitK-;WTy4>lTo@=LOAcvwW2l6s&I$mi8M;Aq0Nkelc~t|aMmX%W+FF7;AP5hQKgM4HetyoUG-IFnnKDM`AmV_O#|QTPVo>->
vf471Jp}Ueg(3<;d-t`OpWM}&kyLN~CBi?LVh9iYH3?EHs@D!@cKmc4Ox6GU5JV^@L2*=qiGv~b+E}C%I6c#8KM1jFnptuVP%<fC=VZKC-&f;vl8?Y}qboFY
A!~>LKmf+ersK#-HZyq!(EEmhUTu7SkF@4}$|KY`L7ij1$7lgqZs0)epY4r;(ZBH^0Ae`JX3oN*Ky4Cqs6_krAQt+>X+9*cwGtd>Cmoz}6dm7R=F)1=<f2xr
+;I76-HWuucXoGCzmiX{v#7x&T!PPEo}*y=dXyaF>qKYES&>nydfFo||BhIO-o>lLL0aHQbZIGk`68ssyxxec3k@Qp?-P=PSJ4Gc=gB*O#-w?yd)XM|!d%N!
AzC>E*0NM)f241JizqE$VDw%IkZja^MzPpL7TokifwcefZCmQqwm-h;Ht7R@m$9eKCM*V>iIP3LYl<`3`K%%T{-#f}MTGdcMo!f*J~ar8&t0~en>;-BL77@7
O9WxQvSALT@Ko+4&5jG6p`41YTP$6P=~C+vt%kPcyS2mZs#P`})vkWkap6k+XH!b^tEp92AA}nJcaVW{Q08qabP+?(pd=BVDqC;jGTgC9-J+?R+(H%QqD0x&
s?rUE?I_eGIpAC&Ole`&C!TqQ=55=H*>k7fPFw{b9u@-lwp~wNxC1dYp2UIf8ltF;XD3cdFy~xs9RNe;z>@wcrlli|nUD!;cFuomcXN=EO2t5T=;A=O1ZJ`7
#8Q413+uJbVW>dGv`4v0$U$+GS7-KbG*iX*NQ^Cv-A9k4SVgQRZamt$Lrs+}UyKXf7j1Zv>L}N#tW)F##=)FbW6zwMg+SMeK2)rIg{{eVfZKkdz`3l-dCcM%
gOI$9<Gp52A65fCO3sMe60S9`c$Wp?^kn=Rp`FJb;N4d?LM$>9Q1$gG&#oI~(A1S##iYzm0qGjsZit#Fi{3YlNr4eYBBa$e{G4#h;e^y}_P}B37eRAovD4r3
iEG|b0o?5R(*ThQqf=l0P*(5tQ0R!vJh<Al7%5qWERYMOMDWzWW1J|#eN=Mgu8fgRwMRHcTR!5@fwIa&K5GTWzdd>m4)V)@5~rbX3`;lkDGPcsRz7Ti9rQf4
jn=TuN^}-$eFjfqE9wJjOuF5K7#lq`Mkg!qFiwvpE@cazllP}NYpzXL<k?1fs~Wrr+Y$CKVfNcXI%fA*wFCCf_EB5q1X@k!@j){@RM663_d;HOj-q*xM@Yh+
Pj?G7$&*hILnSe4pMkLjJUG0t-CsYygyDm3G}7Pil=S)AUCkYPFI(OpMxU8nSNXcGwXUecRLe(Two8;@B+mGNy*3wB+s72|-CA_<Wv?8P;-~YNEdr!X0HP}_
xe#IJR;`&y!?c5#DQPX^98mk;I`oy>xO=cS<U;Tg5ua^vFd|qvDOZWeeOKVqrd+&Pnw8+|iGo%>s<_$(oZGyJQKsMjlnjwVpN2eSTw5t+0r3^Sm^q`SHL6Bp
fi{N{HegB+X|iP5%cce4rUJGoNJ2+`Ws(C6F-vh6!P1Fnt?_J~A4D3aiIg^xM4goP6BcO1TrE?Daf*#8(gIp$r^6}r&&)ap*;<Bg2sV{<gE>TY3z~3=KQvp%
tOrvWZvgB9+ALjlYyOD=UI1cX;o@??Va;!QoL}Y*q0xa|9|svg-FcT7G6;ZX_oHd7qo}rfHhQsxXN4sTcB0s0ViCX_IwQTqi+AOLgDK9ot&=Hf+$`-Z<zOOG
_h>(pY6KRXEy%|7A;GG)xaW6~z%5AuF3-ySZ^U40Fw2Nuzye>HV31R<r82)mjiAlyzJ7C<p6+JEvb;<SxoOSYjSDxm;MuTsL4YTZ70F9@92RUPAcsYcvcJ3l
|JO|s^(sBrZGAyzXEI-2kIN?X>V71}n&w1*JtxBt-#cMIE!y`%+-z@u(6H~3{q@qIBn<f~6=`_rsXi#Yk)&XeM(P~D%SV^MnU>ULkZ+&3f8HZL8wbw*IfvBp
l7pEA{;c{g1b7Ri?PkcwUy^4AQ|%PM$td@WMnps`eFwT>rNP(_zvZoMex`D~pi_l~@qdw`q7%te_Fh-Bh3aG)G=I71X<x>tvw7@n2zrDWZZBdA?0S5dI3G6a
G;DYtl!48AfhpTz^7l?kUuIJCU@6?G?G)nlytp?Q<<YttJpe6!yFzY<((J@4(RE#h&fzxxuLoKt$=;)WI1AXvN9Sm=I+Cqbg3%R+;AEoSG|TbHeMj8NstH(N
$qWlKFR)+kG^|QVF(Dyrqdz7QjddJsJYR!kCX#h5fkM;Ot+s`b-&IkG%KyR1egrP+(Aa8xUm}dBy6bt3%WuJ67o7}_{=Zr==4QxrMUvMmZn%=FOP#8CfiqcM
?+gzO<Bz)OY;6gB+>lERcqoXhuUoGC>(C;)q4-k+f97xLy_W>DR7s7_9*y+e!=ro(BKutL({j{6Q@P}pDh+3?)HVl108}U}n_XeYQxnFY(Yad0$D>rr?FFsS
L?A`Wr7#n@CvNn@?$;A&f&@I24zt9;rbEox#_tT&H(Py%AEavU%KX4aZ+t4)JnqHek7MT~(W8LO$W%=BUDhXiY_0G?)H@D6LHt0!ZaZW(>s$X;ONM>cdHMX1
`h%=1pJcN>3ON^ULV}B-MuB0jV49|UcII#1KI-FZiZ+5dg-<2a{9!X~Ka>4w3aGRXhCgyWzwqfXq@x1RbM>*|B24D`-80|3@bx#E>j*`r4PgAAKWiG|?HLKf
cMm*}mZ&^+Lae(aGZf)`3@~+!%Z9tN-vGiewf3bD=P$Bzx6-{;tL*Rd<+NN!eosJlu%0xo-IT83=IT4-MWB{s7}<|IY*5$HU+vw30vbui<D3xNo4RsisLc!L
u;5@Oc|*bAl9H#TSy#_u5Y$8hK!mSdF`C`IO8f({Yl7aL=tn?uq68#KPLT7fof^Z36J2~emuDr!Tvm#dpI<FuPWUt8BM?q~9oFm`em;J33BOnpl3VtArN9>}
ZOo2S!k@b%CMQqEZ~%I-$NqG)!=0NrVKnN|U-|`cQ#Ln}`;vfwVao^qHH|7S-?Hjv{-U6hiFk<y*1!+l4R7;RL7P>0??a?+N5h2(qc6L<xT3BzLA?Z6yxHMs
mm(#cdvO4ALnMYivWny&jpB|YZcfvTMVWfTi)u*#Re3uB_c4#8JQOQT1gY>>zE$5QbqvlM49!9B(>TpH=~T+jt>Lh*hs&*ER4i4txZ?xLodI9eq*u>8cZjCj
r|rwaX*RYc8`@}Nc(IBpN&o<+p3aVPgpQ*h3wMxNM3pmW4YqsP1m=%H)LI<_&<H8;xg-&?KL6b{h`G44{&~JkTvc|#G#+Q0pJ}X~=PnK=2OBWnlx~cd1wNf9
Q=*+SVvzHz8t7Gr*)pyma4g9>R))b4#|YUZ|9ZE8i7ry?21G|bA6*_HkGP@+%o=Wz)2gImlA+?4!&CCBl(b@1T7syZJ=N*bjBJ;Hs{I?G8O5`4nZ0|QAKs{h
beH?qUx$dU>Fam&^kxOlB+)R?&xgz%W5=Mf9X-3`%0W~+6^lCzyydpitDcA1jx+m<U_nW}(f<e|g%Hk--oaF?IcE9)0wd;*#R}=`B7==7AiTV~ranB|eoQq$
g6%a!g||>jN(#CzoRe5y*%qpDpoL$_W?5*g<0qs$IqPy24E29z$uX!B7E+4=5AK{A3H2cQ;TD29iaZhnjgAsf9+=75+{`S!q4D9~O{HB-$$61+RSre+^9LNd
Wd5yzJo*CsxBpAzwvll5Ra*V(sl@8S5^Dn@5Ix{m%|GaP`epS=WDW*BXa91X1Uh6B0U%0f%@9zd%B@7jZUG87BYF5(pk}V3Ti6n}j+_SNA=^;J4@Wp`+3Ufx
vWAN(P#l?yIF>3}n>TPu{B^0)nBl`R>iUi%tmc&BUSh{IceKhljn1k)196cTzz<D8=+YD=9@>ya7J`5Ax&FbL%zy8kjJ;`DZ!emXvg^RL222!{X!At@{$E}o
OUFq3A}XR#G5nDip)8ilBX9?_DB>p(wLq7i&g|1svL};n0C!y{*`n>1uTOT@071+@u9cf}{wm^t0<#K&+=swJ)T86d-;gl&@ZKaz5ZB^Qs;)GeoSt%Zo7NIu
&fvzf#w$unf<=8*fmyQwfHDJdf`^0dT<ITEgP$Thk_xUBa0!~c`%n!(qu^3e?3=vCvjsw{1t8v{)53SAo|DG)kXYtL5j&6zd&f+Xz`R|NYb^4J4$Ka~I=Z+W
E}bm47{l*FX5{Y|6-w*PTe9J${-J`SNn@7$`_a<fn{L~M3qXOaU&^OCut9Mmcm{N%ij@N-gJ$@a7h_8|oCbdja&Fbn6z@#9)yLC{@%qPvXn&61G<b}&h*NK>
>vVuGcAZ&Ifa16ZB=61Ef#@V>#>Kg>XiRmF_ux(Xya1iHOke!Xxo|*IONYNq0fB$b^a5{TKPvgkicT#*u2~JK^xm!5akfxi-Yw^4aqKix;|$y{Hgu2)bSq)H
%rM_*=n_XZ2m>pLIU4H(NKpr^5lQ0D2jOG>cp84x+4VW{l1c@YC3g0s)QP<$*Fn3)zeJb{&>>3jm%D)yBnU;El2lpcbFyr!=^c6)%#v!u{+f4Q#S_7vdDlhv
xesNcxIdeQ8aJEZhl%y*rW05@h@aFwLTSb~s0BM}K;%q$=#uw?8tB55#c+(t)^_APoeVyUjV$Yy|Ie^cEIG9;yC@{pXqew$hFeM4ina97e+;0Fc)fQ&(*Uvo
$^*}9A<B0IOzBBE)Wm(&zG>t-qWXY=4J(LmvRLs$)){!{nsz$(7~ZJ;vkwZ#)*Ii~fkl90U4gFc6xvNm#&6`b=@R@sijCD8zpn{O7lyR}HFgzwH?DOCyzz*>
BFY)?_K%kX`_%YnK^ZmV_YGZK6}e1fuop5)&?wZvDHWG(s@>~>!{!d3sv6gcx;j7vjh3~LY5%KMgv1V*(!YcfU_<XDSOl_4Uc1rp95_AF5?X3va4IMkW%U-)
J#*_ozdjc{SfApl8(s%5Ha%uYKE8EZrP$U`jS0RUpql6Pp6R;A<xpQ-#@XYatOm0-5dHQ5^TGfQ+5raMGkRrTfHUAAtW|OWovI<GH_ZUcnn$zXJM4um)Q_i>
@Y2A~U8d4lR`E?^#DwYuadZg%AjhR#!IbW72&lNbgV#eRG8K3T@Q*YAzhe<CO72tmhm=RUJ2D%=033-IXb)*zdjzYdJ265dphqL$+X+7C(<%=Ebtu)@f*qZ<
YE*tz7A1ksGuS1^X9!}7L3*2{o>6pqVpBvR!mfR{ZDhxRg6FrwJitWm``c=J%JN^dUzxDU*V`j$E;(DtVREZ8qLms`u6D%kF~vsYR!{zbr8a<61v2NS4^Pvm
_-oiyg=qpFlv-U2L`xQ%(59972BO{PY<`7Yha>HWousg?Aou(-oAFpLGbR9aVUCFvN|?H5r}^5qY8RE@G_`aqS7G&(A_-WsqSch(goEMc8;hjxwf^#7=|pg1
6R-a56887$ukUMicU0vPgltpts}IJ7l)mh^Y93o7tdK_{3%jN_eUtcNyqF{cgyCbM$d8t}@|rP>TL6XqXMzx<-xJx$xYH$@v0g7$;=kP=ruyg1IS&0KHKhH`
#^j+CV*trmDU1p0U}C5$q0%sNGQ-HCy}7ubTD0c@`a%ZvWbN#ousLf^vBJ6av?Op6q9$Bme!b{%U;Mh1nUp62eTAykr3~IJxU1M(IYa7j80gUZ9v^v{aR6@g
X!4bjw$=OlvyynYoZ(-wExvLV(j+Y={N;;}v=mn695kbMbw&kP-NL&<Kk8Zr3dTwITbvGe?3Z-oK%r-vV$>^8=4qK5uZSDgBICa3M1t7)+FFszzN=K&tsuK1
fau}%r%f5)0k@=c?G>FiQb?pc3E9c?BguUR?-Fr>{7&05wv2eN0!B;SMm!WzNqIMl5SO3c41X`m>BQOI^R7AmcE0if!VjIHb4HH*9Ls!6`-cx^=}o^A14<TE
L^npvezsFRv=%@XZg|6QFg2XiD*r`(oW}dg&;0n?kFw)gF`Tkqf_&sKDL_cx9Ky@HO>U_pfKrOvM!?u4Egc$CEby1@sb!oS8Igd1T&Q_Yc?k2#7zcDyd2hmZ
tn01zHz_YM7XXJzG*#b6Bau4wk`&v-h&*zg#sOKa|4ugzJZhXzv;KV@u>;bB!a31mCJ8jZmk!9YSRLzMQ+PG071%L3d{REJDVZWW$`8Gh;33>Bwc}VkN*#}d
Xw&H@pt^$lQRwU%I&o9Hj+*VVEl$lY)=`PAQab#+hXSZuo<e_-gSW{LP?@6s`}V`va6LYh&W(QcMXfz!AU}-9lHwtX?cWzkRwEnBH3LwZ70by2X@YY+pH-=7
%@yh;tb0jr+;vuV0=REKLy<p$e59iEGNX?#ORTu0P20I1khJf(T|p(RYTDfeoqwvKylNA>+)O+Y48wS4wOndNyRR`y*z~k%(l1%fb#zzOp?p_?h!I9b#D3sS
Rri^s^k1?2-&o>70ymEqi*m}Ut_gvgRi~4nr*@alvFKY6b^(wF*cw39ANRAePxLKt!>Ou#IUS6rhb=q}tot6=+!%|U&80XD5U|+rcxdKjQDNaA4@vZb#nLar
AJm?84SOlaAg-ct5s9%=SVf+wd}JkEScJErY3fgExi=BR1a&|S@zG+=9XS4OX#@Mb^U5u;Gt?fbNUo$6Os#MDpLgo0KL7V#uzgKd&#9|<FxAF)=+WZI!xX~~
{Q*h)GvRLoI*%e)nNLPEgTak1wu=Ssyjr(w`Sbf7=B?jQ<znH5n(YQ~xnC7|&i^eSic^tQj%pM!2tkX!hFY*HzxH%M7Aa}qj0}Dzo^&A}V=y^*t+%%X{i4Tx
=U)=zxrfekbH+f(a+Z=x^e+P2nyeLAJssoo0dnLIN9G!0P*6hOtzIehuP0k7eWF}e|3W}_oAMb6?s3fSM2iC4YMG09A%k5i>L#sLv6*s~!fvkuEnW*Eyl*Eh
+G1*)9`1+L_-3~yZ!|hRWHpcIRU1SF6VBw>yeo51*k>g40cG9_3X7&Z8@8X5rgwTxWkF!dC+0yv9oaxp7Y<FK=CGRQj-Zp5F!jX4tij@wF=Xmw9=YjMtQzzw
!-noFLi$<vr=&d6wcCjS7d`u}ggZX^r0RQ_e}~F2*UkPtzg3uVMm%6G1V7ydPw?9^2+{pUxGO0Db1s;ItZQiBqj6KV)0@c7sg|TAG)IOSfE!2101M>F^q9J3
q3->#8L>QBlaU6W9_@!+e&>M4=8%=b0aoDfPpdhDuC9%|;h#L7(H>9z(1)s|Qrvp-1_sCBr&8sR$Ob{424%uB@Sz~6KZ?n9g%Z`K1oYs3ShFr7u^y2Pbj#ia
QvbLFOJK!KKHm;~6WOF9s9ejec7G)6!y3Qo-zO-5>?WiuNJ9mVj${n5txrsBdg2U#aA}H_@+lLAG|Oiv<g{VEg?{A&-Q?Oc6{fvv@-%Qh$mT{h7jTWjcF$0Q
@q*M{(F3{l4y-5->jBHHHYKn;;^-8jbXkoS#{;ctM$G7CHK(zI;?O46#ipZ+b3pz@w~}717<$v3Re`e2T*=_hkpW3T@2(G8nkC&1+Q85MT;*w?cG6;D`~FI!
gYdUyYT*z}80GffbNJ?Ar3b{(M7IM1nC@+7$6IA$+*2R#gfOO&A1vx82xf;w@vNza<8#OKTwKgFp~~{s69`gP*1~Y?a_OZDP#LzSlYowJ1ydQ@oqcIF9@;LU
eDde#tQoLm*W6krYLq4j!_&tQuPEjXONO~v7bgNCOvgF?91=maLSnBwSaTZNw{BI>?Ja9QF6bA+ZYhr5by!z-A+%n5Z+vV$?qoB_6H;i;Y<-_3p8Z$}a`P40
q2pq|UwjSVAp3L2kpW1Ns$Rf%PpN5rjKl<TFOfT1V8P{|i=>c%xbY$5{oEQ6!%ytJ&<!P~oxDw2W0Baai5vW1><rbUd|Bz!0rIq{R5OI#qwSof`zfWd88Ia`
iPz%J-K|j#?Nlo+ns<l>40KDz!M4(n&uUEOtv~XNzNjQSDY+m>65Hp{zxKcV>ZGpa4)Ry%dhu%Ps3j5@nrZW#SqLh7T>d>!OB6?g0EpY4_QA)+g!bM6+*_It
5=Oiddg?pK$`c^`%aHmEILOw~r+YBF=4GmOpX=Od#cy}bX%DZ;-rj6hZ6V2nQP8!{;yKO&oFfNGp@EMDnk#Yu{`O4X?bO7v4w5{LD_x(K`LZl?!Ri+gM&lr$
JQkKdoSJ+^5)1WQEi9)nCy4XQ*)sj2dT1(ZG6D_H%*RA&-=<dg)A=hv3}IPVZ;xF*Lm!OX1;H%$wkReQxZgKOAhUuaM%LOP3Lme@{@M&#pA0U8KE2ORLM^MX
k*R@#bDn4Dqe%N_#P|0ZLL5IBqJtpZ2=Lq_fWq5(D`-h0bU|8m<++^)Tl&xUaO}?kd@=SC76+%kmj-<i{mXXa7AoU=^mftJ)Vb?eDE|mFFlCvk54OvaNu|{F
LIj!dktO$9{Lcs!B$cYq<(qzdPjS@SF{Mi*i;cVO+pxrZ`wmN6@vW_E;gq4aWC~}Z6lg<K`%a~F5<i|n6gocm?J`tS-mG|K4oUrElIT8kL~~QGJnI-R>{^~t
)zwPH(O_PA@DZ-r(KR08=?ks|9wR)m&92Cj=+GXTi%XX#Hlm1eC;`x{**GrsUTS3@K|nCH7^Q1fWMS8u791|>MzIDrT|g)&!G;x}&9?G|hMpP*U;>l#ER@W7
Szd%t$ra%vy>PV^!KD9{!;QizaeryGD%Nsc9IRi`C^)6x%_U`{`k=mT`wMpeiuGIDcBH@XCfgpB=6A*Ux(7saI#epx$N%k<U7&LIl#a6ZnaPmv22Y&6P4BQx
2<{=f?1gbv0|y6|n8pdxH^Ec{kX{W$$S4G#Uql1wU<7~2Ru3p{a(W!oa*P;}y`u`%0zjHad#6-uf}jldG16uJ)YujyNhM$t!k4p4O7s+myr=|mehJjNW|bQz
BXL9}f)QEkZ-4x~v41ZgcuCmw{}RJ=D<}o&T8cla=U*s?$5wMkQ72#EsLeq6Wv;Ih({#Bb0^>cFp%Vdx1gWJIr;|AYH^TOP`!&|pj@oi>L#RXSZHDEm(4_~1
C~H7(4+{gTYnuS$qVcLVt^(#JdA+e%RZD$94k0KM4hs<%a*w0SYjO7aqybABK8F{XkTA3S=BAbJZ3Pjp<7Y_aptp}Y$62E2|G+BqG69XT<kX`!sw|^v$xS!t
D%+{8*(ZO9F{I0Iq74?inbZ=}W9{xUky>fOHnOlMTvOJ+45$QcbeC?_W_`<nbS#3aOHSQ}qM2S;$p|`1`fh0gpx0C@6C;b_c-Nj+K+Zk{=fPXqx-Uq}U#EI9
p=-<8_jO)b&@tS<1tv{{r}VRBPO5CkFXq*u<aXgv$e`Xzk0RIgXYd@;Hj{?FLSr|mMs9ZuMz`3S5|coa*3!+q2Brq2@0$VRc>5(xt@S8>-*`nIMBVtToLw+U
D$aGcxOUPN7}d9p80RO${82f@K@w#Obx)S~y4G`*8l19nx(y}yW>9DVbiiV=P>tyt00F4q0{Ns0@xL7hvBYQl0ssI200dcD
'''
raw=lzma.decompress(base64.b85decode(''.join(DATA.split())))
assert len(raw)==168569
assert hashlib.sha256(raw).hexdigest()=='be552041df6afda1c54a45465859faab7baeaa1ad645753a135eff6ce3108d69'
files=json.loads(raw)
root=Path(sys.argv[1]if len(sys.argv)>1 else'KH93_C434_RECOVERED')
root.mkdir(parents=True,exist_ok=True)
for name,text in files.items():
 assert not Path(name).is_absolute()and'..'not in Path(name).parts
 p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(text.encode())
for name,item in json.loads(files['SOURCE93_MANIFEST.json']).items():
 b=(root/name).read_bytes();assert len(b)==item['bytes']and hashlib.sha256(b).hexdigest()==item['sha256']
print('KH93_C434_SOURCE_RECOVERY_PASS',len(files),len(raw),hashlib.sha256(raw).hexdigest())
```
