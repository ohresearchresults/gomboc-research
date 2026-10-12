# figure-0504

AI research report · 2026-09-23 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# QF71 — точное массово-геометрическое препятствие для неаффинных C2-продолжений

## Результат и граница достижения

**Новая собственная strict110/additionalweak000 конструкция не получена. Новый результат — точное препятствие для большого класса действительно неаффинных изменений формы, а не повторное закрытие фиксированного аффинного семейства.**

Для C2_S3_PROJECT73_G6 найдены **68 старых опорных полупространств, образующих 34 C2-пары**, каждое из которых по отдельности запрещает S1 у любого однородного C2-потомка, сохраняющего высоты основания и верхней вершины и остающегося внутри этого полупространства. Остальная геометрия, число вершин, комбинаторика, объем и фактический центр масс могут меняться произвольно. Старой плоскости даже не обязательно оставаться максимальной гранью.

Следовательно, при сохранении этой осевой архитектуры всякий S1-потомок обязан выйти **за каждое** из этих 68 полупространств. Это не нижняя граница на число новых вершин или операций: одно геометрическое изменение может пересечь несколько ограничений.

Дополнительно для S3_G6 точно доказаны необходимые конечные перемещения:

- в исходной общей системе координат `d_H(K,P) > 3/20`;
- после вычитания собственного объемного центра каждого тела `d_H(K-c_K,P-c_P) > 1/6`.

Это условные нижние границы для будущего S1-тела указанной осевой архитектуры, **не** общая невозможность C2, не исключение измененного основания/высоты и не исключение произвольной измененной геометрии.

Новых численных оптимизационных кампаний или послеродительских геометрических checkpoint не заявляю. Выполнены полная точная реконструкция шести родителей, новый целочисленный расчет препятствий и отдельный холодный запуск самодостаточной капсулы ниже.

## Источники и точные родители

Основание вычислений — все четыре приложенных точных материала LEAD_C2 и полный приложенный журнал. Литеральные геометрические входы и правила C2-развертки взяты из recover_lead.py, а не из приблизительных координат журнала. :contentReference[oaicite:0]{index=0}

Наследуемый аудитор вычисляет максимальные грани, истинные ребра, собственную объемную массу, полный строгий/дополнительный слабый S/U/H и оба полных ландшафта при одном физическом центре. Это **один наследуемый полный аудитор с внутренними проверками**, не новая независимая механическая реализация. :contentReference[oaicite:1]{index=1}

Приложенное старое аффинное исключение касается шести фиксированных форм и сохраняющих ортогональную C2-симметрию аффинных преобразований. Настоящий результат имеет другую область действия: изменяемые тела при сохранении отдельных физических полупространств и осевых высот. :contentReference[oaicite:2]{index=2}

Точные исходные единицы:

| Единица | Байты | SHA-256 |
|---|---:|---|
| exact_lead.py | 11008 | 6b41211b97ddc5c026736d6a9e5670deb4739cd985fccab7dd40d681224d3923 |
| recover_lead.py | 9006 | 0cb0cd79115afb6adde8fbbdb2f08a3e03d6b56a7143b6947f2646d0086e77f8 |
| metrics_lead.py | 1992 | a2d991bdda7e43b28948e60b85b69083f0b6d7bd896b871fb9cc6aa54137b4ac |
| Полное приложенное аффинное доказательство | 23803 | 7d94b90d561a69dbdbe702388da05eda083a3da3368a25617a4a222056953cb8 |

Все требуемые зависимости нового доказательства включены в капсулу ниже. Старые численные производители [internal-source-reference] и [internal-source-reference] не приложены; они не требуются для этого результата, и их поиск здесь не воспроизводился.

## 1. Общая массовая граница

Пусть K — полноразмерный выпуклый многогранник однородной объемной плотности. Предположим, что он инвариантен относительно `R(x,y,z)=(-x,y,-z)`, нижняя максимальная грань лежит в `y=b` и имеет осевую точку во внутренности, а единственная верхняя точка есть `T=(0,t,0)`, `t>b`.

Собственный объемный центр имеет вид `c_K=(0,gamma,0)`. Обозначим `H=t-b` и `m=(t+3b)/4`.

**Лемма о фактической массе:**

`gamma >= m`, то есть `gamma-b >= H/4`.

Доказательство полностью конечное. Триангулируем границу и раскладываем K в тетраэдры с общей вершиной T. Ненулевые объемы неотрицательны и покрывают тело однократно. Если остальные вершины тетраэдра имеют высоты y1,y2,y3, его объемный центр имеет высоту `(t+y1+y2+y3)/4 >= (t+3b)/4`. Центр всего однородного тела — среднее этих центров с положительными объемными весами. Это не свободный выбор центра и не предположение о сохранении старой массы.

Основание неизбежно строго устойчиво. Если S1 достигнуто, именно оно является единственной ближайшей максимальной опорой; следовательно, собственный радиус вписанного шара удовлетворяет

`r_K = gamma-b >= H/4`.

Если одновременно U1 достигнуто, единственная верхняя осевая вершина является единственной наиболее удаленной вершиной, и

`R_K=t-gamma`, поэтому `r_K/R_K >= 1/3`.

Это **необходимые**, не достаточные условия. Они не заменяют проверку локальных корней и слабых равновесий.

## 2. Неаффинная теорема о сохраняемом полупространстве

Пусть дополнительно будущий K остается в физическом полупространстве

`n·x <= h`, где `n=(nx,ny,nz)` и `(nx,nz) != (0,0)`.

Если

`h-ny*m < ||n||*(m-b)`,

то такой K имеет не менее трех строгих устойчивых граней в указанной C2-архитектуре.

Действительно, разность расстояний до этой плоскости и основания, с точностью до положительного множителя, есть

`D(gamma)=h-ny*gamma-||n||*(gamma-b)`.

Она строго убывает по gamma, поскольку `ny+||n||>0`. Массовая лемма дает `gamma>=m`, откуда `D(gamma)<0`. Фактическая опора K в направлении n находится не дальше сохраняемой плоскости, поэтому некоторое опорное расстояние строго меньше расстояния до основания. Максимальная по норме вершина собственного полярного многогранника дает строгую устойчивую грань, отличную от основания. Ее C2-партнер также отличен: единственная инвариантная горизонтальная грань — основание, поскольку верхняя опора является вершиной. Получаем основание и еще пару, то есть `S>=3`.

**Существенная область действия:** объем и gamma могут меняться; разрешены добавления, удаления, многочисленные новые вершины, смена комбинаторики и временные дополнительные равновесия. Требуется только указанная осевая архитектура и сохранение одного запрещающего полупространства. Не требуется сохранять его старую грань или ее вершины.

### Целочисленная форма сертификата

Работаем в исходных целочисленных координатах с масштабом s. Для каждой негоризонтальной старой плоскости вычисляем

`A = 4h - ny*(t+3b)`,

`N = nx^2+ny^2+nz^2`,

`R0 = (t-b)^2*N`.

В проверенных родителях `A>0`. Условие запрета проверяется без квадратных корней:

`A^2 < R0`.

Каждая строка нового банка содержит всю плоскость, ее максимальный цикл, C2-партнера, A, R0 и положительную целочисленную разность `R0-A^2`.

## 3. Полный расчет на шести точных телах

Все шесть исходных тел реконструированы с совпадением прежних байтов и SHA-256. Их геометрия не переименована и не изменена.

| Точное тело | V/E/F | strict S/U/H | P/Q положительных баров | Запрещающие полупространства | C2-пары | Нижняя граница gamma в физических координатах |
|---|---|---|---|---:|---:|---|
| C2_CHAIN73_G5 | 73/212/141 | 5/1/4 | 0/4 | 54 | 27 | 31/100000 |
| C2_MASS_FREE75_G8_CONTROL | 75/218/145 | 25/1/24 | 0/24 | 0 | 0 | -14610883/80000000 |
| C2_PAIRDELETE71_G6 | 71/206/137 | 5/1/4 | 0/4 | 46 | 23 | 4909/4000000 |
| C2_S3_PROJECT73_G4_CONTROL | 73/212/141 | 3/5/6 | 4/2 | 68 | 34 | -29/10000 |
| C2_S3_PROJECT73_G6 | 73/212/141 | 3/1/2 | 0/2 | 68 | 34 | -5731/2000000 |
| C2_S3_PROJECT73_G8 | 73/212/141 | 3/1/2 | 0/2 | 68 | 34 | -1146227/400000000 |

У всех шести additionalweak000 и primitivezero000. Полные остаточные P/Q компоненты, разрезы, пути, уровни рождения/смерти, физические положительные леса и максимальные комплексы восстанавливаются внутри шести полных audit.json. В банке не заменены компоненты их размерами и не отброшены малые положительные бары.

**Ноль у MASS — только отсутствие препятствия данного теста.** Он не отменяет его прежнего фиксированного аффинного исключения и не доказывает возможность S1 или правильное замыкание массы после изменения формы. Но он точно отличает этот геометрический ресурс от S3: у MASS данный универсальный массовый минимум не делает ни одну старую боковую опору автоматически несовместимой с BASE-S1.

### Полный список запрещающих граней S3_G6

Индексы относятся исключительно к аудиту с SHA `8745e40d8eee2b1ee0c0172fa939f4c56b4ecf8a13727fb0310e819499c54cc9`:

`[0,6,7,8,10,11,13,15,16,17,18,20,22,24,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,54,58,59,64,65,66,67,70,71,72,73,74,75,76,77,78,82,84,85,86,87,88,94,95,96,97,99,102,111,112,113,114,115,116,124,134,139]`.

Важно, что запрещающие опоры не ограничиваются двумя текущими устойчивыми треугольниками 43/82. Например, достаточно сохранить неустойчивую в смысле S-классификации боковую опору 36 или ее партнера 71, чтобы S1 оставалось невозможным при любых остальных допустимых изменениях.

## 4. Две точные конечные границы для S3_G6

Точное исходное тело имеет

`Vol(P)=92365675306523659/375000000000000000`,

`c_P=(0,571191349078618212571747/2955701609808757088000000,0)`.

Его S — `[43,82,140]`, U — `[68]`, H — `[[69,70],[71,72]]`; положительных P-баров нет, Q-баров ровно два. Восстановление сохраняет оба целиком.

### 4.1 Общая исходная система координат: больше 3/20

Здесь `s=1000000`, `t=1000000`, `b=-337154`. Для грани 36:

`n=(1636688818,-2073990989,7566093087)`,

`h=1482641329441032`,

`N=64225953510568624814`,

`A=5906793233048210`.

Для `epsilon=3/20` положим `B=t-b-4*s*epsilon=737154`. Точная проверка дает

`B^2*N-A^2 = 9921202123722571271166628724 > 0`.

Следовательно, даже при минимально возможной фактической высоте центра масс необходимое увеличение нормированного опорного значения в этом направлении строго больше 3/20. Всякий будущий BASE-S1 потомок с теми же b,t обязан удовлетворять `d_H(K,P)>3/20`. Включение P в K не предполагается.

### 4.2 Каждый объект центрирован собственной массой: больше 1/6

Для любого BASE-S1 потомка той же осевой высоты

`r_K >= (t-b)/(4s)=668577/2000000`.

Для старой грани 43 используются

`n=(44232989951,14255580826,90476735280)`,

`h=19776687639808536`,

`N=10345818611619082503077`.

После подстановки точного старого собственного центра, для `epsilon=1/6` сертификат имеет

`A=25155661524882408027639689885190073/369462701226094636`,

`B=2011462/3`,

`B^2*N-A^2 = 18595973005947478950193990763816478866052628306463806312473859041287/1228524188375542237627162107851752464 > 0`.

Он доказывает, что старое собственное опорное расстояние в этом направлении меньше `H/4-1/6`. Новое собственно центрированное S1-тело содержит шар радиуса не меньше H/4. Поэтому `d_H(K-c_K,P-c_P)>1/6`. Свободным переносом центра эта граница не обходится: оба центра здесь именно объемные. Это утверждение также применимо при большей, а не меньшей, осевой высоте будущего тела.

## 5. Что это меняет в конструктивной задаче

Получено препятствие не для всей C2-геометрии, а для **сохранения слишком тесных боковых опор при фактической однородной массе**. Для S3_G6 изменение лишь двух именованных S-носителей, внутреннее перераспределение геометрии, обрезания или движение массы внутри хотя бы одного запрещающего полупространства не решают задачу. Требуется согласованное расширение всего указанного набора опор либо изменение осевой высоты/основания.

Наиболее полезное продолжение — действительно неаффинная переработка MASS_G8 с явным BASE-корнем, живым пересчетом массы и полными P/Q. Новый банк дает дешевый необходимый фильтр для каждого промежуточного точного тела: проверить `r_K>=H/4` как целевое условие S1 и проверять все сохраняемые опоры против массового минимума, прежде чем тратить усилия на локальные пары. Это не рекомендация повторять закрытый аффинный поиск MASS и не утверждение, что отсутствие блокеров достаточно. Конечный результат все равно требует собственной strict110/weak000 проверки и истинного E<=249.

## 6. Самодостаточная восстановительная капсула

Ниже полностью включена сжатая копия **всего** исполняемого исходника, всех четырех буквальных массивов половин цепей, точной развертки шести входов, полного наследуемого аудитора и нового проверяющего кода. Сжатие — только транспорт; никаких исходников, координат, библиотек или checkpoint извне не требуется.

Команда: `python -B -S RECOVER_QF71.py OUT`.

Наблюдаемая среда: CPython 3.13.5, стандартная библиотека, assertions включены. Никаких NumPy/SciPy, оптимизации, случайных чисел или допусков.

Наблюдаемые новые артефакты:

| Файл | Байты | SHA-256 |
|---|---:|---|
| qf71_recover.py | 21772 | de29fe2a20d974364e0694cc023e8bfd928d5dc999e7eb09c13443003f2ea4e5 |
| EXACT_DEFINITIONS.json | 12004 | 0266b7d8f6760abc17f19b82247fdd515d0d1ad0431b7a93c157c94b92d3ab9c |
| QF71_NONAFFINE_MASS_GATE.json | 188664 | 6bb0defd9cb6a902ef28be75fbac89890ff104d57f40b57373b1d38dee42f2d4 |

Все двенадцать прежних квитанций шести входов и шести полных аудитов проверяются внутри исходника. Полный первоначальный REPLAY также отдельно воспроизвел тринадцатую агрегатную квитанцию metrics; самостоятельной капсуле этот агрегат не требуется.

Наблюдаемые конечные маркеры:

`QF71_S3_G6_RAW_HAUSDORFF_GT_3_20_PASS`

`QF71_S3_G6_OWN_CENTRED_HAUSDORFF_GT_1_6_PASS`

`C2_NONAFFINE_RETAINED_HALFSPACE_MASS_FLOOR_BANK_PASS 6 188664 6bb0defd9cb6a902ef28be75fbac89890ff104d57f40b57373b1d38dee42f2d4`

`QF71_SELF_CONTAINED_SIX_PARENTS_TWELVE_RECEIPTS_AND_NEW_GATE_PASS`

`QF71_INLINE_CAPSULE_RECOVERY_PASS 21772 188664`

```python
"""Self-contained QF71 source recovery and exact replay; CPython 3.13.5 stdlib.
Run: python -B -S RECOVER_QF71.py OUT
"""
import base64,zlib,hashlib,sys,subprocess
from pathlib import Path
PAYLOAD = """
c-pmmYjfK;*5-Hr3Uz;x=ui&t7pajdCy|r9<4GLbNoPu{V)1IzmMBG%Z%O69?{f}7ijwWl>~3vl+M+<<063TDJODxc`RAXXk9@O}
-^b~?v&`3VS>;*(GM*NzMV#iHS-e{Hi|Ks6?5r>I`7)n%(tNoti!zPZ`N7^<J}vs`ypjz&Z%!W8m-DJ)ADH%m+gYvSDvOs{XIdu9
c=<5wKpZunSF6tKW<_1j(6W<PaWc)bgT2$6s<V(X`ma0vv(ERzH=|{q&TsSO!Q!Fw>C5@S-r-GFt}&!^z9`Xav7FE36ryP!XH@O%
{h{T0dtTz0mT4xTpJl0=8kXnVUgpJN?s~qF<%#3lVVZ@3Tcl~6pq67~USL|5li8tV5BIA1x)XP*{H{}0S-!~er&@Prd3qUFWxDE=
v&A%@p)96Z9dwS%b-s+JsJ*yZuXt#CYWTZ@Gt$IJGe0y<H!cz{&aylxk|ay4!U$qJH|)$yTrc)b$4<P^@e9jyyv#5HFZcZ-IN19*
?_8EEXad%lcB-3MF0azdJiT7bON<m+%I`6x3dO7W%@Q^(%4yyySJ3_Un{r87|MSm3>AyE~n#?-yEO{~{XkOjs_x;6u`f!<NOIRf)
)prW%4;`9Ocg5;?V|7wkyUgGhtAo9_7|Jbdlix3<Wm>MM4{bB07U`iEuh&tMdO>E#nUfiA?52t9=SgIkn%-g6S9@)}$I|cz9qDJ!
xY<ExbblGcy)Xh8Vx3>)%g*J^bgJ*o;`?%jiP4NM;Dvf;eK+qzffw*Xa(2CwK_>`?S$U7)H-<(<xLSXj-{#ZK$;;0NdmqTcgU<h)
efrq>S<>*z^@F~G{&Rgfzgzt}=zO|aqfUqHzsy#hcsf;)1|`LqTh>YD>r2vRzFI?RUsmx&KG+U`ZNFx>I=EWl_MC+uuu8aOuOt8c
L-Rhz>T*6^vCZMU^X0ljjrG;TN}t8+OZ_rlT|$w2Y_0`L@TH?_p5UvzQ7j>s<5=A~QUwU{&XKG`p|GB#v${??pCx6*&b87P%XxN_
u4UD9KAq;<0<*k`Z>H<4OxJn_SIzhKP}D(~^kO~H20*KuWz|{Vz-N2+FCN$_?{(5q=SR8VN*Xs=-6T&n>HkBM+0C?ft;ah}uJ`X{
6KW94n%R84C46-=>)r4FgXnZQU#;3rdhytt>?dPu(vR^6SLQ@lR|b_C@~*C~Oe!<wT{VWB$DpUpDCDSQS5z+R<yG3d*9Pn;WdRH*
D~g>I%FvHCGgvQC>&Z%FjHcdCs(7spNb0S|6Ta4OX~OphF#T-R(|$cErN`RTr+_Z4kv49LkwPZiSlzyt)>m=cJJHK*rB`Y$K&FL2
X!n+Jb&>aMO~1|`#5A5IS=_lA#L22xjjtw}HjMAZ_=@|uqCV>SG{mbv1j$joB7nsTZkT7i-pRO}jN^N#d!pCZCaz04+L9z;I8tTo
qsu(rF-WhmrMBNoYa43)USm%#uj{a=>0FE_!^;wX`8##C;9+BQgF4(hcb5d{)4b|U=h`b_F|hCurt@(henTH{sfG5JFb324!D7DX
X-#t!#0vu0-a^~y24J^bK?BsE_Ed+L<#vacC3i?4O^27|PKPMi?l65w#drx1=dPF3HHJKZh!>DVpOc{^4%{iKqgT6jEpm0~=oIHC
W87xz$Sc@P(>FJ)ts5FV=r3b{uLo+bYM9r8$|&>P_hzN+QX48$QtRu%<OO{Wt|!tlDZTV$f>oMojaZcn!Cw%psz4hqrg4?8#Lr)i
=F3<w6TM7H3vIkqzTFb1>2}K~>~2Ed8kg}zuP>9$WjYyFVxy}B0LQvXaj~%vbXp0~Gj#k<8&JY1E1+*<K0z9<&}6tm+7rewi8FB&
PgnWyM-Jh&yVf(h(%GAG<|kkW+iI%+-72vQt$(?71H-x9u1fz_!sI)zj82Z8JALy}72Ku)vUk$OA7VA2p`I^q@?ipZy?!i}CbZfr
Cg}s7SM9Y|TdIP@$2wBBCvke0b2hV?0#4G;O3=j>^Q-RO&RAa=gGx~D>6>uP;iYKl;zCe*KDbD;-ahVCLgu8~moG0iph=Bhz7!YA
vBs#XUuqM<6WDc2SqHJ?NX(1x8p!L_Kr3y<XbVgo59|qptAhLdf$mVpQdW)oTL64NPzjfSP3rCjs8aVu@ldij1QfNCz<jsCRvCS>
h4^_tkTpyFe%qx;pvpEUVqE+CWFvzrOoj#4H1N;yY_W9{9Za4W!DN_!7i0SV#69k7epdlCM2o8QIIA_$T<B=FJyae;%lRvje;*eU
QY{QFuk8l#z!`gWVEiR6H{h&-XxHU7^(j*UaxS;^xD}bejGCX&>=-#~U_(M0$mxxx`D)i-CZkR2Xy_HX<TfO9R2x;cM83_gpl+$$
i26DqBWxG3LN*yr4QjN}&|Ij2aNk?GV2&Be{4<Al(ddPk1OCSYgYw2kJK5DZZpNJOz{W{a04yuwF^fQ6s7qN8d{*8wckXdrZ8xS)
v_5@|v={UtZH*yvwN;*1;-~Rz2qu(X3pC%`q*E>%Yy&6LObnFo$t*e<?1JMJLkoEX#1H7t0deFjO?I<`TJ5ZaswyX)Xl<@_qEoc!
Ja|3-u8(x7e;s2%sZ4mZSON``mE;1d&Kb(NZ$0FOSzXxJR|Nz&Y^5);Nz%l#q(tqpK4cm+^_mIv&7DM&v?N_^Bn{Jc`3tjkCleb2
y`7W17b3$HNS`yEa5>X?{h`(%M69>edh5M1+L}D--FmvGaU<EAE`td-bZ7t8Yw_I~M6qUpq#2fxi@f(uAF0VD<#K%~#uVB2`n|SU
g?yU~c}+?j;&HU$?p<D9T&`Db4tcHjO8rXPhNV%PO9<`{00OPa%d5#S;SBu^rTRBw)5ALva|V2cPfo(A`kKnGN4<DI?I-)-886bl
wV!OXt438j=bffzae!=~(6o1_k0)AP<64Gnxxt+){aTZSSDV6;3b~g>ycC4RE#CA^BgTci|KyEXK1&G9$3M$o8_e9Q1Rcc7MwMi%
0vxedKH|pc97Fv>lmmGs=tEvkhNX~KO&jGbWn-W_3Gj@hQZKsVr%Ya2-A(6dJl)DaP~djdTr;0$DdW3c_|UJ!XnYMw)f1uSqVwmK
wu>|IA0ioWe~hFV!>Ih8$nUY%niB2nmDPoy^v<=k9UV1Qwue-d%hg&C>24}$!;9to2I-&gHSo#bCc~y0IQ(pWiv&yM+rxhnVjn?^
oXqoJ`xNN%$OioP8Q6V1z#ZM@(=1=|@|DH3snc@Mli^2RJ6-~_`sxY}n=b@^;r5fg-6<_wPQ-$>$Forqc3P`BE`?yxw1=ohG5Jf}
J!ZT0KP*=kH329$A*2Eey)Zl|WO;>{Pgm?7)J}UW?Pe{;9H_a(yPRnO$>`<C5zJ^-+8+Yn%=+8oi7XH~;^$)UabD%WhTm`Un_TdA
QV-L4+^h5yuEw+?U(}W+LC^Su;QHh<)4W*sv?puHrO<WDDiYANr-dpbD4;})z7lslqN}X|(H{VyDCN|iSflI^#C%b=9n$8W80U-0
Gg_egw2=QpECzJlEZeEi`sNcl<hsp*8W=IZrs&NFo5`p=l<(%CUyp=kIiy8-c0t5_i-Yb`Sn5{iVSxtnmX7TCY5pq2UBe_>eLU))
5Wk){11u+yg)XBuU+6M5*8!rlEO944qh&sgX&YM9aXjhYX)o_&qi60mq9`ulwbfeCl}-VH|9FamC)?Id>ss43$xVe-S;mp39pDRA
b^E<mP&Qy8Q9^qfNhHuw=2}i9E^O7S<w-CSvd>+{`BSBsXVU90uu-#3pIG13Jj3+9>2jJQsk)U^I2T4p7Ue7!%DZ&V(ey|0Dc&LP
(U!XkHQu8aWhD#8UH;w$p^<AUp&VuwFM6nig_pKjcF7jBA=aJ9xcLoR7VVuOZtzu4MVmcqLq(r!YDini3k3D1*Aq>bG+leVcc~4(
T6$`UCkVM#JNQ>2zRG1%Dnu$*Bgb+-VVch14)+IHUd?B;*+i?>nqAVm`;8hG>Fa*~SZm)MenU)xRTDKnhNAR0EmfUJ{Z#YiECxRv
f2Sob-~P^F|9vuC-7ILYA2*NpFZ*)cszlJnMO{tJf=EH#LQ_Qhb8RhR)R!$fT~+c+rQ{GosG;bM5IMrtdI?7pKf7n$!FZx~zsQgG
^zjP>8u9+jJ-Oe-Hx0gL@GUIy@>SZV+>bUazO`WgmenJ<J!zBJHAud;y$B@g$o-Ac(d307FS!-M*i4z^Z0$`Er{KcBjDegax2@r<
+*Hn|?dp&^plLr}dzEiztt;j)a+uqj@4d(K()(A$+{NQN&8~;CZqwl^-NIlMsHMJ+mlye3T<MS{Vj$+Ktnz5}{U%-l@@N4P>-C~(
pDtRxZS`C)<m9GJRc%{KInI+dgM+Et<BN&5U;Ea$nDp!0Rjc?yhQNhf1EW@B)wBNxtDbG_RQ%qmPuDKy(BT+MzK2vWiePX<nwljx
6Zt>dKO%{Z-L|&rzhTXQRb;F-=LtVrildHrxy`-HdbC+zX^-~1czd4u0U%(8y@L7GMk|d=Z7M<!P0dCh+CS_+Wnz2C!z^QsWO_ym
P_-<MC-ij*pAq$xvP{j9zQk0$r9b^bjBkm@HkRJn<$~(rhZmyuEz(NkX2V!U4^=6&VIr62)rC%rr8sHs;oDmg$NNdrkCXj4sg?1z
6<>#3o5oGDsOskXg+`5Di|vxQzttj6c8x;QeXCOiD4I7<P;f|<Sre~Gj5d@Z)F-`UFYxzJf8E5w`~Nl;U{o%AwTXrI8}A-Nm6P3g
sGDr!;prBio88QxTMY6^qvaE=y-N9|4NuO*_D;_5bGziT{(00qWR*u99(pvK0}Spar%m+1u3mZ9uI1Y=+691Wx%b%8L$md`yGwaC
?h-@d8jpmS%oM2j^K<pixL!T{T?wFZEP|%h<dMy6mIO4d`q1aFx<>-e!NnNaQ5)A1+`E&FUXcfWZ6VMOi9FGER#Uv?%FOqP{ebch
K|>ilw^S<IJFCNHXSLLZrNDUWEu3YXl{YJkGvE^&bf{f5Rp5I^z03VeeS@g7?xo5(grzkS)&Z|=?atD3a!!KvnG+#7Y5lc3k%v%(
Jc=R}8mR}`{4giKUoZ0+(xkivPF~Vu5vH+U)qb!(5^^6~KN6drZ2gU}_EkBRfVoM&xs2~3HS9<|(*zZ+DSMo*Z{lfmJD(z<imxwu
Wc&MeeIw23P)eCKkF>bLCdN`t=PG#?spC8maAaLBrX|*3$B%B#ivl(mZ}i3G!-`HsMd^IL%!u9QTP^pMjwAt;AGBFp%JWYVb3gi{
FP7!3q_tW^2nBgJ6(-MUwdtjaZgFy^FXq#D*(&->MJp*|y}ZeJtrp3%KLU=e*KQJ}<ubjQsV_B`X`JY#`qXFf@|rg+yQ6RK55Jt9
fA~6z{(boE!@m!YqxWBqkE4^rv$L*_+lOz?qw~K%MW0STy!-GGmCnxUn`h^zA8_~Y(c!<MBWiROeTm*TcR&35%klZ)$I+)RXVLNK
>j*-l&-LAtPiG&v*OT}EIs5Pi-JYL*8AYSF??%zlr_<5dxvV*<x3=rkM?Dp$X}qFkeXpC|Bzc!lg!I(8pdLK~H8p*iW5K-^Sm)?t
PY-m{n&@MGq=3BI>#p<lGVbc*9x79HeD>-8xT5yW6$?X4M|X5@O9GiUf_Yan5_7LV=s&df>76k>z+l0K5~@i=`aySlyMj&K((Q@1
q5f4olLx{OminE1u20i$^9!{^-HK{%CnMS9_JWULG=yeMahL%y*=vEK*As2C;oIwyfxdKUJwlrut8};Bj+_5Zz+Ec0)t9sm>>iH}
-$rk&=*^ecqv(8eetIZ9=;ZXn*}tPVpFW<SemYh@rtQ5xJR5aH=jUFRn!G>!@X@!UcP`dYra}Mo&UkEjmL2GwzHOU<jZeo3Cn&c9
&j_j53VlcKn6~dzv27Y2*G4l-@7ShibFuB278RS8VWQYFTrT#^fP`3K;G>o8s^Y*4NQf0!j;D7l&*oysv}}`#J=ew1OxNQs9XGID
Dz<#b*E_CfI$Z3zmQTgDVH)&lSOJ#@p2d9{9?#41OrDTycwEo)!+^y3j+EnCmPhqX*9=J>CTQ@ST-&2T_e~3vq)$6^c$}`|n^X{l
fx`kFUzWR$OOo;F@Bl(N0oV0?o`B)<Kpi*qxZFcmm}eN0G|P8GRox4r1~*_Swh@GeDs~{nG#nl-%w+_!+%$aBmO&qV+l4LUD0vuW
D79xps2n9MiT*4nV0GAm5la17p$WlO82TQUdx2Dg83Z2L&I(K}_oXMehELXV4BzB&29|HJ{zKb>e8;m~9*+;>bGh%*z@cT6<#>iA
?dUo*5ZCt{_8`ZWF6F>GP|>q(U;3fxOIHhB>d*@fpUodaE|)tNRrFn3nm>eDrN>(2CxKyyTu$}a!CjyHBY;}j?4jfHc+Aiu{e*_+
uv<93oR?|3<nf_vgrv8?_vle3<husz5#8dp2_vDH1CG)D=yWvl-RNCV2WJy}D*ha}spZgA`%YlMx5$jH8@Pd|yx($dHm&0$C`}iG
GaVbjVwqgQ_T118q^rA*2N|%UOJ3wTQep5ULw4X9juViZ+pdoZx{jKGYx?ZVC<%jr^y|PNfn)F(EZ>8=O<z{PaM)muhnV--wr1d1
jxWc6n+8S-3n6eIjGfoFEsF=%$G9<C6IDIe4}HU70ceIvIE*at%P=&gi7_<kJ$(~HK<G;shrV12H81o7-?7=AusF2mnk>Wg{m>=c
@&ZiFm7d?nbjS<Y{hYwHY;pkL7<|!{y}-2)oq=?$z@llBYX%S|b=61Ah8}!|Bi3LYky9JCZL5)@$n#AZ>NG3#2zA=7Ylk*_FrWv)
EiFR9Z#Wb%wi}pUAR(adBNm|^3JCHj-=_|tK|r;P)_!2wFqz9W0NlPwxNE^X9C)&<;Se$~{`vqcgRE-0j$z_jR)Ab+kE0#M4uy$n
Sg7KvJ`j=^w?}S`sJ6&25xt(N?$YFFj2IwvMXeFCt_&~SrjT%<;n0GsGHCgRZFp|oxoy}K!Y29y#53~4vdUvHe3&pKC7CcRdXlIF
xC&GUa1I-H2+J%7aKH{6B7eD-tYAW6Y)mTz8hM<!ATo5kTFc0Nb|}%!undE6*dsuZ5ZZ@%VQcEbflorqBmv>!S*Efi)D0LU1AAeh
a%1S(u&|sa90+bpfC5|shB2m_CQ@8rD0i_v4^TzQ#aLl5mvauVz_H{gTzHhlC<TA?Oq(rc+Q>(NFAW7%ksG0<k8}qevs>737hi$|
4D8x+CIQl#YjPl&@Fq0%8OLBG5B;-_$gMeCVVVGu7S@n<a`@r&?dW)PKJv}zowva<#UxyrgOIcsgkd00kqJ|xK0uN#KqnOTz(pNJ
C>-VpgcLQU;Jizmg49E#!d9#z<OFOHR&nSUlC)6LB6BjcAZbJ`Y{e}s?gyH;L(Z3;bTo>04m7Gj(f|mKtr&(cr9rpsesB?)gg`QU
OXhTlF&J7c$5A{(YJt4Z3YckFD)mB;;u^SPOR@n|sI+Wyf(2>@hNJj~R}&7zGBXY!rlK4&TY+o%o+KS^pjd}56Q4^dm8Wb3CZ|56
8qZS9gSAfh%vk4pfCa@eJcqp14;?lb+*c+dy2H^30^-<`ftbE(WCVn&rW5+UB}s^iQldmMh6CG>c|WWP3c`upja)sDR0PoEDK26W
zB3t->;lb9MMpx*kbK0lBq4#KYeqtRk|+riG2$drO&}%A?ueB%v_#QMguCT2F)=uU5i_wRWua*V%uQtI6FI5biO;4WdSbegp9HQU
^R2`57NHMGlA;8*^iQBgAW4e!5#&O*Cf3MVj^rt(<h8JIs2B-Ak12`CBQ%{rkt&mzfWxc=nVCF<l26S`TuDrTz2xvdQFs-{XEs(0
pZ;g`=A0G;!7e93B*P!14nZ%FG8ue99;_ywean;g5uOh7b(?5Hy-M)G$|Y}uyKqp#;{)Y?Hj<sBcZhBinZTwfMohrCD#9HDd0i^c
2g7m*8A9UlD$W5l%-hfg$V$lv00MM0RkUMB^<u(A7WO%Z0i#1{ShSIh$0CZsD<7a1;=5j3P^M#y!8k#&8BjyAnsk}~oXoT(CJ;UI
d`Yj6UZe*jN|4hy*g=e3UKY`s170ENJW>dJ$C4`#5HMCTE)e6cBI?8dEQJZ=Cla$k3>4gff`R2Rtp$*SR0I+mT;lc$9q^Ud1@M9V
%a#ZM%m~%uA#jKvNo<2zEV)3jh&(8ya4cs2<PkxjRw`hkw(5cOFS8e>?Avn5g1)>4HGstuH$V~;S2hTrZMA$sQgC>^XV6N|lnf6N
OgTg(bh*?6hQL)Extc*}gAghlfj`=YT+<+kB~bvs0!m6%L;uX?fhY8mp+Xcmi(4;o9LYY>u@C+bN?d_a6gV56?-;}u8Cz^eR=`ri
kYhk|coEqO2m`rn6B~m?LRBb(RVlAz2xlOQXW_C(nQ9q?DhxzE!L$q>hlZ{yz+n+A1T0`{hG9w6p>?`MM$pR;+>ME|1?I)696k-j
8!{@9e*$(W;E!WlF1s%n0@kyx!XPXvNia~zazeRCw~1THB{8j;fTX-^g54cYQdlf4VGjva4va~z46t&E7BXB>zHt>`fqn408Ou1-
G-wQjCJvJff=Dc@CFT>dI;02i6ry1SUcdH6-%bEqqqnrLvAwO)dL^$rKv!^KvSc?-04Gk7LDy!UV<cH&X9X<~Q!{q5Fa;WAE-_=*
iA_I_T`)*6A1?=O_Oq~yaqaX}_u=pgzMG|)>87b4TVd=KxfkXL_$>9!)K8r-@xnOFff$8@ew`5CoFYza-$>lpOJXOedw6=qxHB)1
2-#~KXO0<XaZ23QH{3M$oeZAgCq-s?kQ^kAm*jz+xv86_MUgu}nuE|=iC@61zv;D^qfeQo3#UtrEXXr2@w39T(hQSIle~z*nlj`*
Q0Y8~krhodw~`D_?8JEzBQo+dwDY>R9SXT?H24f9v~J=RKn^!8+yuc63hj|#ugF3tkC8{>B2U5IF{dzbiZC{eG)WR*1#$>2yPoT=
nUzVw*!5#SL6Bx3W(noy3?_Gsya3DuN#Pr548=i<Zk!_x*)b-Wf#X<Vk%XBYyLC6)3DtSVbOd$8&ASP_E`uKJB#R3y5$rU<JPI!{
oWxHO2u3gicw^+rB93!7j%~uwsp~`YN&LHR>kjRJpsGtdXK+e0fUyEI#u)Mhd^Pb+s4)kAS}B(De&SLt1lp&0T4a8aTTWcqZel#$
-6Pv!ZERC_Sd+WCL(Y=J6Da0V1AL)?FNB4Yx?bX-gCIt9S$>fKzl<EnjmSt{Cr!iWx@&A_5sB&|Z3Dye#4)op2odE);$>hBK@g^x
rWO0NEcQ}lgv>}$(+-NzE`UU)m1jx*bT`57tbh}gG2kkcu(QN+(<}ux*hQ9wVICWCo|y&GV_KL=3Nn;9iIE^j8;EseZNkRTu+!(d
+r$|Wo-XpJks&J-aC9sNk@FC6pjLsMLWg#ix<%|D(}KBsg#ob45a-Bl0O>F-QfaGtn^-=9`1gpOHJmj)g;qdxq#F>;apS`D+%!gF
3=rE+2Dq~QJVSTzNN{o+VBr)15HLE&$@7>3A6oEWr(g0l*mxcHHrwVp{fvRWj?1Zf+Hjxf4~hOG5mdH$&6BFV7?1n3_22(7srUYM
-ruL26WleFOt6h{EeDtV$Jc%Svbml-I??vj7XRkGao*;~)lHSr`RT6uNd+$GRC!F#i|A$aRewG2=eKz^>`a><9gy$3lY~xugLcbu
%_j`ItPJ_sil67vSM^qKb~9V_=E;@PQvJdzS?Pf8t>~ss55J@9{9(mM(DjmE$QPFOqWiz9u6B@D={%#?Ct2hL9h%ALsbGENPGrqF
yWxo#XZ4fbNFJrzdL0WlpMFGHAGurev(^P2`)wVO8z%gG^-=M9z7QwsWlq>}t?#_HBahpe6Cu{^cJ*1r>HJQN>(|b9-ef%CW2Ulk
GTA-uh?bDzY@LF`+#WwG?b3?{t6Wr=c71YMy5Hj?NYvpEAuy4?spC(wGZ}eC0o};wvrsLG=I8hGyLQbZeh9Sv0G6M{qv|vFEV?I8
j?7SJ{leZ)bVnPe56`ur*P6H9J4_#5iJAQAgTK;;zt&2{@`SK_{QE;2{6+`z3_voSr}6=4`<z{`y4R}*z4}3?0e^Fdi%wqL3sL=`
qacrtwI2#+|FT~_?8}L2!&A{)_Y-Y@-`Ynn`_=sm+^im6R6q8sACFEZ9k$Ncprgb6!@o{<56!6q%DuiEbe~7PeH^=<<<|K(wyh}X
2ODy6MF+0{A#IzN;HZy|Ws|Ro@kT!r{ZJh0r{YvS0FN%>g*feFr1}%bpjUaco=b<VA4*63Lm^STj_B}d#J>|mPtkivy;B`xnp1UU
1}ptg<LkB_pVqV6iXD1~5tV6j-HCd+o?WIX{6qYcu=)j{a@oAY-|Ad%q&(4-qpPX<S5sArOz2TPK~G)1ebn*C;D|>3Un`29it`H*
b=UmP6uqYKe8R}Kj(IE~x>`rf6Qbl{ov#?$33a#ctuABaNuhq(<3N7pdIy*JeO6vzUOjDNbd{3$R0pA_LQVdj%-8GrEP4<Lf88<s
Oxv7>*uC{~)#_sVNXP~|WC13(do<)Jc+qKa_)ll_q(7SuzEX>?s57FA5iXAC;)ssN$m1TZXXlU3d_47hd?WiL;xp#zLHgt49|*wu
*p&WxyYBX(kaoqrt%yhJkJt+%iXD3Wx+#{9&42X<0~?QIAEiGVfk3u&dPA?Ai|$$UZWP&cIwLy#_#fhCA3uFO{_t^hcpAMOoxK@-
e0%uuJUShnW0Cpc<2$bP`uNkEe~qZc+vxoLC_4Xi645jL=>6!!yZ7g3-N%01g(NHiKD>>Njz6KZGsrp~MJLCHAL+or*?IK#)94JH
pMxB}IsWo?)K%P}C@Xdzq;dt-^P9DxU!Li$9sq;Oi(7u*M;$v;McOM<bxc2Kh4H`n^mTOlpRP7U>x0>KRxW!oCKQ3m@5|LXnqSK|
>h_eL)ajJ^{l1m>NgVA(S8>)2!`zpr^t8<p4_QE9LaN#R1(Y2=DyYWzsSVIgCgTIbJxBN2uZp7|@wi#{1;y8e_M+Eqp6-%<E<iq%
Qo5V;l$E!_H1_v<LI0vviph@KbDfCIWU2avJ{~g%<&*XhqO}g&gT$%#NalA9Yu2ByPfAdjO20bL=9)B+U9!2#VLEy<VI_K99se72
wMWErhkOybfx^*ND(8;hfS(Xu!}4fPAt<oOH{t}#oB~Uaz_J`4ODxxPGb1zO%y4Wo@v(+XP1jFDCkZXAz>_eQzvj?`zr9pPuHKH0
5Jcx6K7CY+9_`=`j69cM&0|nlPh^na;3d4?`aKXfK-PL|j1<)T&cenw7J@pa+Cx$)lln{>E}rhOrL1w2Gk&8YaNK&+i#?_Fc71(-
N!#=tYeTRJbYHG7L3fLyyzh0}Yg)Sh|7UQJyFI?8-~~y{3zDJK_IN9oPQ+5_ez!c{Xqb;aZKvQ^=9pM!m{{hQpVtE#_V#Zg#hYx?
V1wRO$a>c0_j{Je1`0(fBXnugXy;aw0H{I%RKIKi*p|}dEUzb9GB@YDlsCz0q`tB1U_Ie@x);d*D^4bqUY^(q!MbH7HZM>O*J6c5
nA$Ow%O1M@)PiShd(C@26*@QR`EwA^iHyEw_;wf?VG!!R>v=|K8-cIW(<aa1U3$kfY)ideWXWUV`?sxEfB0ughQ!~iu|4Tm^lMo)
iO&}+ELLpYGPL1q0Y2Y%_E-BTZENsQ2sbo5pUx23^uWM07(`ybQlI;;_bclaC~l2m5&bNpXpwW<lkD6#bxFJ{9i5a@Bw<2pTx(3f
U-Q@3nmX*;ocF9Oo#;5<<lg#BsDGnX$DYX5Sp4j2OliPGX4zH%E3CKCSo)w1pI2{NUA0;cpH@$OJa<<`jxALbSpTFVx;)hWuk^Ic
S2t7DWiro75M=4^`Wd-zL@InA->kCvvM3_82*NTsUxMZ$b&1-rs{Z`0it5SyW4rc@H))P>QH}|~%y=!?3Mkm&5mLoS?t#BMJReDn
d=9?VDNJrGhjx1ScSMJP-+nqhI*Q(%gX397eg5+4CZGQP7%@v5z1?nVM&1)GB~?`8l>Cqz9v_{Z9KKOQmt^nt;m3ceGr}7vlCLoS
H(36}fJetiOl@SRXCJ;n{3*tM7M=e+I{r!ndNcZPg73spKaT!pCDyY57m6ZE2~mVRA2GR%qVAwgHTV8Ew|=bd
"""
raw=zlib.decompress(base64.b85decode(''.join(PAYLOAD.split())))
assert len(raw)==21772
assert hashlib.sha256(raw).hexdigest()=='de29fe2a20d974364e0694cc023e8bfd928d5dc999e7eb09c13443003f2ea4e5'
out=Path(sys.argv[1] if len(sys.argv)>1 else 'QF71');out.mkdir(parents=True,exist_ok=True)
p=out/'qf71_recover.py';p.write_bytes(raw)
subprocess.run([sys.executable,'-B','-S',str(p),str(out/'results')],check=True)
a=(out/'results'/'QF71_NONAFFINE_MASS_GATE.json').read_bytes()
assert len(a)==188664
assert hashlib.sha256(a).hexdigest()=='6bb0defd9cb6a902ef28be75fbac89890ff104d57f40b57373b1d38dee42f2d4'
print('QF71_INLINE_CAPSULE_RECOVERY_PASS',len(raw),len(a))
```

Дополнительные копии, не являющиеся единственным источником восстановления: [полный распакованный исходник](sandbox:/mnt/data/qf71/qf71_recover.py), [полный новый банк сертификатов](sandbox:/mnt/data/qf71/cold/QF71_NONAFFINE_MASS_GATE.json), [исходник и все восстановленные отчеты](sandbox:/mnt/data/qf71/QF71_SELF_CONTAINED_HANDOFF.zip).

**Итоговая научная граница:** получен новый строго ограниченный неаффинный запрет и количественная необходимость большой согласованной смены боковой геометрии S3. Никакой новый strict110 endpoint, общий C2-запрет или достаточность BASE-нормового условия не утверждаются.
