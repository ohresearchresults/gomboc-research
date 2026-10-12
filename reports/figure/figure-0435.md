# figure-0435

AI research report · 2026-09-20 UTC · [Export notes](../../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI report.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../../C622/README.md) passes the supplied exact checks; the search for C<500 remains open. See [verification status and source gaps](../../catalog/coverage.md).
<!-- historical-status:end -->

---

# Nimble Comet 21 — конечное продолжение C222 own211

Branch `[internal-source-reference]`. NC22 обозначает следующий вычислительный этап той же копии.

## Итог

**own110/weak000 не получен.** Получены13 новых точных рациональных тел. Вместе с родителем14тел прошли полный cold replay; совпали95ожидаемых научных выходных файлов. Сохранены полезные невыигрышные тела и неудачно округлённые варианты, а не только лучший endpoint.

**Основное продвижение при единственном физическом максимуме:** `NC22_MACRO_G8`, V58/E168/F112/C336, strict211/weak000. Весь полярный бар, нормированный как Δ_Q·Vol(P)^(2/3), уменьшен с11.269446242675… у точного родителя до1.042729166392…: строго более90.74729%. Относительный бар Δ_Q/R_Q² уменьшен с.729722610441… до.147822667952…, более79.74262%. Положительных физических баров по-прежнему0. Это изменение полного бара с достигающим путём и разрезом, не уменьшение одной почти нулевой стрелки.

**Весь лишний полярный бассейн действительно устранён** в отдельном `NC22_POLAR_CANCEL_G8`: V46/E132/F88/C264, strict121/weak000. Однако для этого пришлось разрешить второй физический максимум. Затем `NC22_SOLE_S_G8`, V44/E126/F84/C252, сохранил S1 и уменьшил весь оставшийся физический бар более57.36202% относительно POLAR_CANCEL. Это новая S1-сторона, **не110**.

Предпочтительные точные старты для продолжения: `NC22_ROBUST_G5` — U1/S2, C336,76-битный знаменатель объёмного центра; `NC22_SOLE_S_ROBUST_G5` — S1/U2, C252,73-битный знаменатель. Они отличаются от прежнего NC21_ROBUST_G5 и друг от друга.

## Источник, определения и полный census

Прочитан весь журнал-update через EOF, включая literal parent `figure-0431`, предоставленный SHA256 `29c8ca382debc04dbf9e38e40c8357e2a0180bb71ada189399a84cd105294b12`. Конфликта определяющих данных с назначением не обнаружено. Родительский вход `NC21_PHYS1_ROBUST_G5.json`:963байта, SHA256 `6e5377f36feed6c502403df6880cf59cccb30b840cce4d3b38738c320fcf191e`.

H-вход задаёт P={x:n_i·x≤grid}; V-вход — P=conv{p_i/grid}. Всегда используется настоящий центр однородного заполненного объёма c=∫_P x dV/Vol(P). Физические точки x=p−c, полярные Q_f=n_f/(h_f−n_f·c). **Полярное тело не центрируется по своему собственному заполнению.** V/E/F — истинный максимальный комплекс, C=V+E+F−2=2E.

Пусть T_P=ΣΔ_P/Vol(P)^(2/3), T_Q=ΣΔ_Q·Vol(P)^(2/3). В таблице целое L обозначает точное включение в [L,L+1)/10^12. При числе баров0 значение0точно. Последний столбец — битовая длина общего знаменателя самого объёмного центра, не всех центрированных координат. **У всех14строк additional weak(S,U,H)=000 и физические vertex/face zero-counters=[0,0].**

|Тело|V/E/F/C|strict S/U/H|Бары P/Q|L_P|L_Q|Биты центра|
|---|---|---|---|---|---|---|
|NC21_PHYS1_ROBUST_G5|74/111/39/222|2/1/1|0/1|0|11269446242675|6505|
|NC22_BALANCED_G8|55/159/106/318|2/2/2|1/1|258850927923|249532927684|116|
|NC22_FLOW_BRIDGE_G8|108/162/56/324|2/1/1|0/1|0|1898152489940|16386|
|NC22_FLOW_B_G8|68/102/36/204|2/1/1|0/1|0|3217662424893|10319|
|NC22_FRAGMENTED_G8|68/102/36/204|14/1/13|0/13|0|2547959410867|10224|
|NC22_FREEV_A_G8|62/180/120/360|2/1/1|0/1|0|1189326858077|114|
|NC22_MACRO_G5|58/168/112/336|15/17/30|16/14|36606|1042703619377|76|
|NC22_MACRO_G8|58/168/112/336|2/1/1|0/1|0|1042729166392|116|
|NC22_POLAR_CANCEL_G8|46/132/88/264|1/2/1|1/0|1058522987158|0|113|
|NC22_ROBUST_G4|58/168/112/336|3/2/3|1/2|26715|1064128764264|63|
|NC22_ROBUST_G5|58/168/112/336|2/1/1|0/1|0|1063091091910|76|
|NC22_SMALL211_G8|27/75/50/150|2/1/1|0/1|0|25634246899423|116|
|NC22_SOLE_S_G8|44/126/84/252|1/2/1|1/0|451332780751|0|115|
|NC22_SOLE_S_ROBUST_G5|44/126/84/252|1/2/1|1/0|464654515374|0|73|

Полярный census при физическом c отдельно проверен: strict=(U,S,H), weak000. Положительных физических баров U−1, полярных S−1, без отбрасывания малых положительных значений. Полные рациональные массы/центры всех14тел, максимальные комплексы, оба witness-forest и все elder-bars/paths/cuts регенерируются встроенным кодом.

FRAGMENTED показывает S2→S14 при уменьшении суммы баров. Прямой MACRO_G5 —15/17/30, НЕ211. Лишь отдельное восстановление запасов перед округлением даёт ROBUST_G5. ROBUST_G4 —323, НЕ211. BALANCED уменьшает оба энергетических дефекта, но остаётся222. SMALL211 — более малый C150, но возвращает большой полярный бар; он не заменяет лучший U1-старт.

## Два предпочтительных точных старта

### NC22_ROBUST_G5 — сохранён U1

Вход1612байт, SHA256 `e8736443506f04989db43d9cdad1e0706a3db208b3022e0a898a87f0f2dc5028`. V58/E168/F112/C336, strict211/weak000. В A raw-lex labels: S_inputs=[48,111], U=[57], H_edges=[[12,33]]. Стабильные треугольники[7,55,10] и[50,41,51].

Vol(P)=540394962091699/1500000000000000.

c=(992129883877388603783,−5518424798984073502563,397844053588075844696)/51013284421456385600000.

Полный физический лес:57положительных истинных стрелок, корень57, глубина33; положительных физических баров0. Минимальный квадрат выбранного положительного косинуса в[761796289553,761796289554)/10^18. Полярный лес имеет корни48/111, глубину23; минимальный выбранный квадрат в[851433706017,851433706018)/10^18. Это запасы выбранного леса, не объявленные оптимумы.

Единственный полярный бар peak48→111, merge edge19–42. T_Q∈[1063091091910,1063091091911)/10^12; Δ_Q/R_Q²∈[149254512746,149254512747)/10^12.

Достигающий путь:
[48,21,23,37,33,36,22,28,8,20,14,3,9,41,19,42,44,15,49,70,100,98,107,91,97,111].

Вся строгая верхняя компонента:
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,19,20,21,22,23,28,31,33,36,37,38,40,41,43,48,52,62,68].

Все33пересекающих полярных ребра:
[[0,53],[1,105],[2,18],[2,32],[3,17],[4,71],[5,75],[6,102],[7,93],[8,80],[9,86],[10,16],[11,35],[12,78],[13,81],[14,69],[16,48],[19,42],[19,46],[20,86],[21,84],[22,74],[23,109],[28,67],[31,106],[36,82],[38,84],[40,108],[41,55],[43,83],[52,89],[62,99],[68,71]].

### NC22_SOLE_S_ROBUST_G5 — полярная пара уже отменена

Вход1469байт, SHA256 `2299ae147858f39710f762e8c72dee6fdbe9208dd434cdcdb4f4d11dde12ace5`. V44/E126/F84/C252, strict121/weak000. S_input83,U=[6,43],H=[[18,23]].

Vol(P)=813833199550531/2000000000000000.

c=(712054504203447506964,24769193568684787723,−152866258546992757060)/8789398555145734800000.

Полярных положительных баров0; полный положительный лес83стрелки, корень83, глубина51. Минимальный выбранный квадрат положительного косинуса в[585523960670,585523960671)/10^18. Физические корни6/43, глубина7, минимальный выбранный квадрат в[889438830549,889438830550)/10^18.

Единственный физический бар peak6→43 через18–23: T_P∈[464654515374,464654515375)/10^12; Δ_P/R_P²∈[223581160479,223581160480)/10^12.

Достигающий путь:
[6,0,14,18,23,25,26,29,31,33,36,43].

Строгая верхняя компонента:
[0,1,2,3,6,7,11,12,14,15,16,18,20,30].

Все36пересекающих физических рёбер:
[[1,4],[1,5],[1,17],[1,21],[1,27],[1,32],[1,34],[1,35],[1,39],[1,42],[2,5],[2,8],[2,9],[2,10],[2,13],[2,17],[3,32],[6,32],[7,32],[8,18],[11,32],[13,18],[15,32],[15,39],[16,39],[16,41],[16,42],[18,19],[18,23],[20,41],[20,43],[23,30],[25,30],[26,30],[30,37],[30,43]].

Стабильная грань83 —[43,20,30]; вершины20/30 принадлежат компоненте,20–43 и30–43 пересекают её границу. Это конкретное сцепление физического бассейна со стабильным интерфейсом, а не универсальная обязанность двигать именно эту грань.

## Выполненный поиск и ограничения

H-продолжение меняло нормали и контакты при заново интегрированной заполненной массе. FLOW_B дал C204own211. Снятие ограничения на число полярных корней привело к FRAGMENTED, S14/U1; восстановление возвращалоS2. Полярные bridges, в том числе64-link long-way с twist+.5 и физической projective mass closure, дали отдельный C324own211, но не отмену.

Затем изменена параметризация: свободные физические вершины с настоящим перестроением hull, живым объёмным центром, полярным ландшафтом и суммой ПОЛНЫХ баров. V_A выполнил150шагов; VM_C закончил3внешних предложения,2приняты; VM_D закончил2предложения с70внутренними шагами, их второй endpoint определяет MACRO_G8. Отдельное восстановление с eps=.001 даёт ROBUST_G5.

Совместная физико-полярная функция с разрешёнными дополнительными корнями дала BALANCED. Возврат жёсткого U1 действительно породил SMALL211, но резко ухудшил полярный бар. Другая ветвь разрешила U2, сменила полярные контакты и в PM_A завершила3конечных macro-предложения: полярная сумма последовательно уменьшилась примерно до.03796546,.02575995 и0; последний rational endpoint — POLAR_CANCEL_G8. Продолжение с одним полярным корнем породило SOLE_S_G8; восстановление запасов — SOLE_S_ROBUST_G5.

Незавершённые запуски не названы полными: FLOW_D107/300; FLOW_BRIDGE199/300; PAIR_POLAR307/350; SOLE_S_A239/300. VM_B имел2законченных внешних предложения и checkpoint26следующего; SM_A — одно законченное непринятое предложение и checkpoint58следующего, определяющий SOLE_S_G8. Полные параметры и границы завершения в FINITE_PARAMETERS.json.

Исправлены две ошибки вспомогательного кода. Старый VPAIR stop-text говорил numerical own11 при фактических counts S1/U2; теперь stop_target=both требует S=U=1, а polar означает только полярную отмену. Старый SAFE_CAP менял view полярного вектора при нормировании; добавлен copy(), старый receipt отозван. Исправленные478тестов повторены из полного cold-пакета: trace совпал,0ошибок и0own11. Старые stop-text не использовались как свидетельства110.

**Не доказана непрерывная no-birth гомотопия.** Восстановительные промежуточные точки могли иметь дополнительные корни. Не доказано глобальное, affine- или topology-family исключение. Доказаны названные точные тела, массы, census и оба полных ландшафта.

## Уровень проверки

На H-входах точные all-triples и pair-plane clipping перечисления совпадают; проверены максимальные грани, истинные двухинцидентные рёбра, links и Euler. Они разделяют основной census-код: это НЕ два независимых полных H-аудитора. Положительная fan-интеграция массы независимо сверена трёхосевыми граничными интегралами.

На всех10V-входах NC22_INDEPENDENT_V.py не импортирует основной auditor. Он самостоятельно перечисляет ВСЕ поддерживающие тройки, строит максимальные плоские hulls, проверяет истинные рёбра/links, интегрирует заполненный объём положительными тетраэдрами от внутреннего якоря, проверяет S, U и смешанные edge-cone/weak случаи. Совпали точные объём/центр, V/E/F/C, strict/weak и сами S-плоскости, U-координаты и H-рёбра. Имеется также отдельная трёхосевая массовая сверка.

Для обоих истинно-рёберных графов сохранены все родители, корни, глубины и компоненты положительных witness-forest. Это не утверждение об уникальном непрерывном gradient-flow разбиении. Elder-анализ использует точные минимумы squared radius на всех истинных рёбрах, достигающие пути и полный cut для каждого положительного бара. Нормировки Vol^(2/3) удостоверены рациональными кубическими сравнениями. Тетраэдрstrict446/weak000 и призмаstrict446/weak123 проверены и отвергаются как110.

Встроенный пакет ниже восстановлен в НОВЫЙ каталог: все7частей exact replay, оба контроля и collect выполнены; все95выходов совпали. Отдельно выполнено точное воспроизведение пяти главных rational inputs из пяти literal binary64-checkpoints.

## Продолжение

Для U1 предпочтителен новый NC22_ROBUST_G5: отменять всю33-вершинную полярную компоненту, не только19–42. В его59строчном V-входе единственный неэкстремальный индекс46. После явного удаления остаётся58точек того же hull; ещё47точек сохраняют достаточный предел V≤105⇒E≤309⇒C≤618. Это бюджет, не доказательство осуществимости отмены.

У SOLE_S_ROBUST_G5 из54строк экстремальны ровно
[2,3,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,23,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,49,50,52,53].
После явного перехода к этим44точкам остаётся61новаяточка под тем же достаточным бюджетом. Его последнюю физическую пару и стабильный интерфейс следует изменять совместно. Простое восстановление U1 из двухкорневой ветви уже испытано и вернуло большой полярный бассейн.

## Самодостаточное восстановление

**Встроенный exact/continuation-core:** все14полных literal rational inputs; все исходники используемых методов с helper closure; exact auditors, масса, forests, paths/cuts;5полных главных binary64-checkpoints; сохранённые parameter objects/границы завершения;95ожидаемых hashes. Старые sandbox-файлы или исходный родитель для тел, проверок и двух команд продолжения не нужны.

Это не побитовый replay всей исторической numerical-кампании: ещё34промежуточных binary64-checkpoints и развёрнутые receipts находятся в дополнительном полном97-source пакете. Из одного встроенного core не следует заявлять восстановление этих34состояний. Они не являются единственным источником НИ ОДНОГО нового рационального тела: все тела заданы буквально; пять главных также воспроизводятся freezer-ом из встроенных terminal checkpoints. Полная историческая капсула дополнительно содержится без усечения в полном JSON-handoff (`NC22_RESULT.json`),207878байт SHA256 `b019e955e4cab6cb3c0f49c441f4bee861c8f524c7987f4ac2bdde9ddadf8f3a`, и source ZIP (`NC22_COMPLETE_SOURCE.zip`),288089байт SHA256 `28f7a5de9bc11f6408ec5e2481862b791ada6aba52c06624a64776321b524f32`.

Среда: CPython3.13.5; numerical NumPy2.3.5/SciPy1.17.0, OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1. Exact replay — только стандартная библиотека, assertions включены. Межплатформенная побитовая идентичность optimizer trajectory не утверждается.

Сохранить следующий код как RECOVER_NC22_COMPACT.py:

    python -B -S RECOVER_NC22_COMPACT.py nc22_replay
    cd nc22_replay
    python -B -S VERIFY_TERMINAL_FREEZE.py
    python -B -S NC22_AUDIT.py --part 0
    python -B -S NC22_AUDIT.py --part 1
    python -B -S NC22_AUDIT.py --part 2
    python -B -S NC22_AUDIT.py --part 3
    python -B -S NC22_AUDIT.py --part 4
    python -B -S NC22_AUDIT.py --part 5
    python -B -S NC22_AUDIT.py --part 6
    python -B -S NC22_CONTROLS.py
    python -B -S NC22_AUDIT.py --collect

Наблюдённые markers: `NC22_COMPACT_SOURCE_RECOVERY_PASS 57`; `NC22_COMPACT_FIVE_TERMINAL_FREEZES_PASS`; `NC22_COLD_PART_PASS` для0–6; `NC22_TET446_PRISM446_WEAK123_CONTROLS_PASS`; `NC22_SOURCE_ONLY_COLD_EXACT_14_BODIES_PASS 95`.

Полностью снабжённые входами команды для НОВОГО продолжения — не заявленные уже выполненные150шагов:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python NC22_VSEARCH.py --source V_ROBUST_FEASIBLE.json --jitter 0 --eps .001 --proots 2 --radius .2 --repairs 60 --steps 150 --out NEXT_U
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python NC22_VPAIR.py --source SS_ROBUST_FEASIBLE.json --jitter 0 --eps .001 --proots 1 --weight 1 --stop-target both --radius .2 --repairs 50 --steps 150 --out NEXT_S

Капсула:58файлов, включая manifest для57остальных. Base85безwhitespace75775символов SHA256 `ddc8357e9c6dcd15158487c0f5d7b8465c82390e8b135bb49067e225378cee28`; XZ60620байт SHA256 `44251f26d457d138e4739a26901b6754414b7afe4507efe042ddfd209d7fdc0a`; decoded JSON233789байт SHA256 `47cdc954a51819a417683c3528b1189fdedf6398bffeee6243cc21b6e6fb545f`. Файловая копия RECOVER_NC22_COMPACT.py,77414байт SHA256 `0955407c3c4508da5eca208c57c122174b1e850eacdeabee3b73736325a2a202`.

```python
# CPython 3.13.5; exact recovery and audits need only the standard library.
import base64,hashlib,json,lzma,pathlib,sys
S = r"""{Wp48S^xk9=GL@E0stWa8~^|S5YJf5<B>e<j9madh=gPkz)OB1JNP^0()NMTbvlFPV3KvS8`}Jdxb~Q2D_`WMM!>cH@W`y6?dc73G7L#uDhULyR+D5dkj@N#
Y}6yR^U0c+-eE^rs4fRD{?s~$zHcMOKC(Tht#dL~k>13WOT|xCi6qF`y;a2!VpQ<Vh@N}i8)@&it}t=Ki>&VA-`|)fkdmP3kuH0P%G@yo%30h)(4MtUt=Ud=
12_NR@!B0n%Sa@<+iLi7q|n~6j>r8q55@Mtyuk#yz>NrX$f1$%Xlz^$T||=Zsal2|+96h8g+Xq<J{q%$I#BC=@&v{dA@YjV<Q+T#*|;@%unxBl9znj45n^s5
uV%rf4jDMS28t1qS<xZk=K5trsk6ta%==U-=fBp1V_SeKRGcXL_nEKq|1koS+x)woueO1!Eh9~i*PKl5r>*S84_B3W75lVqI~J9xm5vPW754>4gSq`Xtq@>%
DlSjm%h<u?x|lVnK$Pr(JF%iOl&ON4_rF?1*_jp;V=~F}(Gmxm4zgl0oKnI8l{aaW(-Q8N`Ma=pwo^Yjs}6ws%=`jg*Y7`HE4&nS3LQ0j#rz3c2WJvlfwtAm
_#i_aj_auUWseH!@Jy|HyBqSr0zo2d(o<6|D7G(7`>8?XpeGKl?D`2kGd7RE!L{a)d3RoQB$#vY2?V$3QHrCoxrWcGdv8ZKZp*nW<a};L)xn97d66a;zN6S|
X`EVWj}eM>h=yW&)X>_|hc!j7@$q&(KS}z4t25VJrN;5#rDRDz6aePTAU#}w(Xr`b!nVZ&H*@>FuTqG3|NY(-s$Q(xtd{Z1!qitP>H!DT%}WM^%VthT={kVI
;JJJ%S){eRNdG~D|KH2Kx5PKXQaN$5vH(}$4sSDxACgsUgs4=Uf#(@4fW63K`z@ydLN563mi>^dL5%!DYC`Pu<_|B107jzgkx}>$`0ef)@(`w0^))Da1OFaa
1gb<OIsrD_Xkr5^Me&tm_rqxJl%vr2DXab#Z}S1R<cb;rJ(yvAoEdoblCr9VkP6~^i#7v^NQqgg%nCwmVUg%^0gt$5fEE~Mn30bM)}v;|aI;z(gX$>^EtmgG
)y<<(+p7JI6z*cL*=pEAW}AayIiIw444g!AxoZN?$n}jUo#naBn@-tonzx(C*;Lcjh%(hU&{YU7i>;z5H6z_*W%8;vM?n-KnENo)e(y*X{9>CqeF!EX)h%Ar
oge--n>7}W!7Pq=X4o*0)*3>(uI?s?bQt$w!-KGIR<$*Kcv-3kK%0OKPYp2aYn{cTlF<i%-B1&F3sVE1^(3>h^ASylE`kG%CVl6z5xS#fcq2J!we;D>+a7Sd
zKs37$-9e<gl7$?=982{r}^qZBVx6S{=s}Mm~{ETE@l*CCy1sTxp)M&F>MeaOfKZZm4pRm$D2?$qj7cgp-rKp+_2yC)@2KA5u4}9v)X|`PH$_|MBH$?eA~m1
QOQ(umMy^G16*i?uun>a{-hb=D+rt&CQ!LgZ(0LO30z+2pTr7!ZLFJv-#Dr--&ibG#m`P@nEdWbNpEZu43VPi(R1pWrxp~B_L-EyZ9j{D?#Glq=3Mi%b(jmT
pGhmTw`0MAL=XR0{XE(=RY`f;+bWAfmtWPu#*J-&eCt$hWT*$%AO|2tB-HUtux8{L&u4erZORK`Il@@)mYzNMULf0!`Sb6iCPbuUb|&GO5leG*YiqIPqcE_n
FKmcmwbVXHN035H%+p1~Y0n)8JP4h~no^G)TmD53+uHql1Rtj}JBSs2zD3igL4UslBM{SE|1|b!jZs53C6UQ?qp-T^tLW6J)#6FG%Bj_>VxY*)E&gaMDMf_a
BdkT^8}nVp{>las%Z6gLhMb4jZjU^m3<lHx`3nchWKRrVrvvCYTq|~jY*uv@qfN9?K1lBRGAhLbP-;doXay6q_Mx5flNVBDB#vzsCrCG2z={83++-0X%nayq
s&Xy2mfKJ!_j=?K<mtE$ApkMg5jx%2#^a=S)#M1dyZ!fy(r{Zr58^k7u_u7A;VW}0{46W32@b%b#fZKbjoC&jTzB_op)})rP^b=W`+k`s!rgmTw-SL$rbEru
;|D!Id|}Z2@_p>1+(xd%n>Ngnv;IyjAz<a)^4?36uQnTxDAwhDdPZNaiX@3-j9WPI1YGa3akT|pjg}IyE%^tK8+}i;H8FWZ=92(-pW3ZNbso@TmWMVFvU<5p
IOTXbiRbSq(LA;)k7?V5=HR^`mP`td89^#HWmJ!=x~q)Iek@qUjcy7T@fj*ew6TnO=D(A@ywA5xg97J3lGHX<PIGpu4d}_cJxs#)$R>64+&L7-=zNW)>6v)I
50on-LF8HYk;nwqc+(x6`=aG&mi=cAK1@#r_cBLDYg55GfI7tu(Mj*0p7fgfK=F6u)6|n|>lYspN|4Dn;|y2cZr?D@qhWu8H`K_PhI%sZlSsEDnUKUKtW1rM
o<%&y7M5eGQFkS$44z~+A@-$(qJB>g@P<{>ps=y;45$kQ8_wFAtauGnmGh{g*&S`7?=R%-u;z*Z)H3oJHQfVcsJOp7MQkF;o(2ZjO+uHKZACWtKOvkaOu7%w
M(Y<mg!X-{*|;#~C4WkRc!V?IdHzle2i-Pm=Xm}65PA&s<lX|T^{mfw@;VB!-<P@c$FEbKW5Rs(EUoqDnt)hG%}d#|e+^DkfQx!ia^Ciqtfp0YPtrGRmti_@
tBuTM3N8Tm3cw*Y_3VchRGPv&@tGgi93lxBix0b0nl)B~$v&@fezk_%8D|>mB#{8<sAgLlm}8SrbRejF*<Dv_GdWXfG_p)z9i=CvW+4S83d6a4eR5eKQmCER
z4Wgnu3GQN=zXkrok9po4oU_92XOpUY~mNOk=X-U>Vxh58xsr>!-z`1%tBK)O@tlFdMLVXkG>na*ww{8k>L)l&Y*Ov=b*{`;Xv#c(Y`wHY|$%6Rq>b6=wtX2
L#p;6!cjzh7Xtb8#-iRG4@;TL{cb_-(X;34;&W&$;y}^q@9B(<Zb_f^2(igm*X61BXaLygLIMfSkq(!_xa6kJJA$Ku$UPY~lD0s{Nnxmy<7y|F$MKZj{xkgF
_7sm+QC<Am-vb+5ZT9d?n5jgPBPzcCmY(+xl=}1E38<~Fm58Lp)M0g+zaKawy}{Z;?VW7A%(6<O`7J@fVvDWFOm-kJ+lNyzQ?cK?_wZ{>s~5n}M}SZznCJg&
htkLI@l-*bFvm&hj&ff)OK_TBkcNU7maYY2%{AZFT@o4%c@7_vp{TT~zf(YCp05b`$YhZhE#IetYoETk_kI>~U5ELI*H|`gCmKfl5=S1k?Qpv8W%lb=3wN}*
0~N~;1%5-cW_#m~y^#3MD8S<)W6gidZv*`KTV7mp0<6=LRQ@xcn8_m_QTKFL#{mm(yuI4uE9vutctFTkSCdhpOGmO(<PG4j+J-jku@gZgpg5jyax>AMiwT9L
#=yP<HZwaOA<lTcOgqPz9{fyQNs3CV8X}S$(VLz1$^ZcwL-rl0t-$IcVr)?esW6yGuB)16@*q22B<6$k{3Jl}c@6Z0CiU$O{UA@Q!g?CY-5x|LUI<HTZ0^qi
+^Z#KM2x=JS$*{NBK0kXLvhtn9kV0k)GL^rYAhT6CrVVTdl_+4n#DL}_EeuJlV=>#9T64W@gV<I?zU~5e0$na59wuZfn4TLqW9;Z&qIjcI#~2akWstj2Of=Q
=a`=vu1#xh{%oT<^aJhs@`V#QeDlakPyo<=R_KTU;+OW~@a~TzlV@kL15wMjVJM<0_8Y2?F=uhkLYzby-ghtBetL9n%~$3J3_g@ic(U&Uo?g&vDHiYmPZB73
q`6V^9p6^OM9f+7^O98rC^g_$wJXiO7ouw=Lmp}BDD!0-c1x%B_P!TXm)Ml%`l2JwG|<WuLQmjk3INk2N~F}?lW2H=i5v~s6>*_vxYG16oa^7UV-VIZAzJ?I
6KagjEYMutF?Wi2J`o0Vf%W8&TUwk#Z{@vWnLsRs;!QA_IZ*wvz^$)?eJ8jJ)<g^tL>hB^y4n-w$%~@nx=98uaC1({VK=9Auvw(IUErPqDd#p}_W-x}AU1k1
*c5YWDl9JI3rq8n|3bi(m^0AX>0U%~!WW->uSQ_T{dKIhgMv)V5Ns2JcpQ^4!4xitw|BN4q}v*3v*&uadbYRDYjlnZQAw=jC^QRo`kDpCnJy(tX1tdN3`<+D
7AI=>_d08b=<>l#1azeIzpgqC-BebRth%{_9(UyQQD4L-!lYHP`TuhC6Ha+Yq`%hxYJyts(^7--6&rNJix-@~VZLtQUV8~tXkZ6WsalLDm{}I2Zg9iiT>bpE
5#%tSW~m+w*)59E8K+_19*if@B%+Vp@A?c%)DKhaEv(#53)af;`g%phaD7toRZgRAo^vGY8}oyM<SuCO8ygVAa9#PRW*UM)KhP!_qskWQps8W9Dibx>zIahN
@#y{7a`cTG+g~JQJOwW*a8aD+Bh&uuYm0h~RUF;du!qk<DG&QxN5}vNF)gD5yj!@+GP8o4V}DcoX|g;{oCdpyLF1qL5OK}%@wmlRNJoJVU01Y1__lS2qpYI~
$c^~79*{Y^3<1~<Raz1G;qd(5Hi9`EwMkmyDvdj=RF&fs24n6mPc?$@@ye_RlKn3+7%hTMOqy%PzV7#Td>VAig#YOG#ny6i9Iw|i$9lxV{m9+(PL(`P7&z2h
p7yg#{)2+&r@)>kr2IX>ij1Yb`QmU1YbicD<P($@k+D_!1Awb1Wqy8jmn@8wfrcBe5UHPglhrV3h<REvW9TWwk&PFqDD#5~&`7<C{=n{uWDu8%Y1#AQMlKlg
;vB3IDadAF0LB?YjA+8SyNGsmZ8o*#H4p#W$uZV<v`?&!h|1au>Xl%fO@Iex>yRxJQSDHTK%w+cnNME>R_Ge|+nR%4|5K1ozIlNt`Ht{X9eNsb94fbC+F~<2
44A34k0XMV`}(tPIBIKi)`b`~#}x)OKEv(yc%XMjpB?=pJ8)T4MvGstmW;;oO7*c?=MLWr-p{^-*4<vMLYf34rD_W}rU86Uk>IO;C(n3rLO@-fr;=l+z7Mty
GFk&8fiuZ5epUAo_O@v2a2F-(20%@_*Z4HLlnQtMFUH}pCU-ENP2kPF;`)WzNMh<Js*;L+>YZQ5=j4+5C`8sVdB2ioY6GT_v*FcV_v^6&rA@~6C&M$OYn*b{
W2D#TKBp0j4pGoea37G7kHP@YC7S!hkbVww%J~!uofTiqJD4L`G!LFl!PMt;5?ppcY#sqnp`{}&19Tk*=#CwY1M~~SRbNpa&=U<*Obn>utM+4!?khlQIQj&4
xc*6?6XPBdZ814RKFs8eUy}w-iUrz}6p{9<o|`I@=WY+sm9u;tsV35FcLNPQ!*rvSbCeRGs>!%qf3VHZ&S{e74Kz}Anl%Nw&`DPh#Co^>N|`r%0CC66<XFxy
GWnX&n|vO@Dbb3__}%$bZ3^3i{&@N@wLiZnNo~FXt8cQ@ZkcbiR!`{L8=r)`HG3FzYgQD>vYPbLcsSHkn<jt5T`@fa+j?byfAeSrM;7WWn-p>^#A$cSrib($
M5bt<-avz3m+FPKzlaEIJK`MPuL&pxb!j>3COLr*2#l!lx|tn3!xi0FrCCZEmM=gl=i_^B3n!eFRdwp|G6K$k>{@tV?zR9AUkvj&Gg>bSdxgXb09C}30EuI!
`Op6>kR<P?XlkYE0_GPdmVmehIE73%jf9O_aOk)F^QLM;zurwjC?X{@GDxir9>#htZzJv)&GA;n`)6Uqszy#X|3HHzmgU|q#Z0}xU>B@3F{jH$=>NhwtipOd
4^xiEn?O>x7hskP5I1>yH0WjQc=}WYEZUZ3|FaDD96Kv8%W$wFN}1BDpmZNr1e{M~EUy48apm#j!<F(d$@j6JHx1+y!7lENHX8wR?r?(wzz)Q{_m_p@cxO+q
i|zuVmeybBgFz{SOJBr4=9}G}u&aaulTDLACZ+qFJ!GJ41&ZNb&mP>o5TPWVLYw;R6zRw|z8A-ji_qXV-W6EvzGDf{LM(nAN9n@x4TM0upVp!dY3rK1_~#jF
18B_9-07|U6v)OKJ94F-)E^FZd;6^sT|v^>gbsciLAQ~rT%T0CPysCo;Y+F;FuWLoq<ptR#T2Ix10<M`kbrK9$LkXs99^P6>3ghIDDmj`9(Q>SL6YMSf$RI#
dN@->xaxU3=`+j&3dVzXJftEwLfz~Y&@&9Z%<0F|;XqWgaJMd@LywqqPm$wXAj*NI!THd!V2|qCn0z*AlYU5<@A|(fDc7sB7eY6>=IU$)OSXy8L#-H13X|BG
1g{vEZN0V2!V=xLw*?53t_9V@dYIP9Sd3oTKX;|fP>{$_K3Y<;fVwB!waEn}CqHrRo0V2b!&Ly}v$`F7F;FLQqpGrA2vj8actX9tDGTjZNqzWSLH2LVn^Ig*
QP_HQr^`(#Ey6`-%62Xa@-o(WiWeRLUTX&&!6XN@{q`AQaV`w!DxcHZrrq*OfDduUqGjsubTS=1{(rx$GVjyXt=D0#Ey%`PZzs1sJQuWf=OJd}&57iMcEv<@
iJmXwnBnhacz|cwD=cz>8Yx{@vll6Wk$ozsbH%r4fN(u9yY_0ACj-XES4ueGkUvX3d<MUX7TEu0(LjkS0&neok8bfUeyxv*+HV-D-%6HxGCqOvi=*orAG5G+
ufYlOG35*YbA|ZTz8n(^fVu&2n58(|<)J`*q;ne}&RM%pqqaPt!rB<SJYs1+`s6kUfbJNL&Y_t6K9=~iaEh8%s#bIZ`ee=N6-Q6J`-Nw^X-IT&P5_Z{b0tXq
H7SFBT;T9S(>X#S+X?{69%1Ui@t$$(fOuMhEsr$*0Ogm43J!?|(Bo85RaLyAwN|0jcN+qv={|I<1*joF>}E3VH-|lny)~aVYwLx!N0@H<iLX~d{U(>4D+McU
5C&%CA#|RN`6Xl}zUOy$vTr!6AwXQab%e?GHT60nbMyUE4Hs8c_pg?Vj|EBm89lO&3~(|@n#ess*egt6=!`87<57XV5IqTR;GvAI7&s$^n;@S?n>>D%l5MdE
6+dBepX5m@jtPlWK*1+sLmp}oWbMpwH|bUS;=N7S5qPEl_&{^V%un0tH48(Cwjj3@CpV3&_*Hi5nBpCkrxKufbBDLPE$baz6AZigKvW-tJ|lNp&*l5J`@2=<
B$mE>>DxYzTkZ)C8X68+cokDEn>_XPYMiSBgLR&F$<??Z+g3Uu+h>QirWAb8hBC#Rk#l!-`d|SPvR#urMmSv@O}?hnoG<eE^hL5(C4tcUv#PMSdN_&U6mXi4
vm`k5d#BhiP;B&d(J6D3NjGYO$2YLoqbJ@zbRRbxoJL3XfWZzdvz~Ns_>8YxrXEjB>|F5|%woxKmRPcs;3@kzo-=B0oZ2y1m(w~)I`2cPL8Uq}S*Vl{qv1Ir
agBjpE%g)CzjB6joJwLzth(B{CKO1^1NN1&EmJ@dAsFsq2#h`F%w*3E;7Yfc+KZoC2!8Vz#(am`(OUSP3f+KxEWM!#xp>wy3vikZ5GVF-?boti?lL>%yFO)7
kFyzFRcAL_^oOO9umYrNHSr@NkVzCX+Q`b(w~@wEYe#C|xc&^7;prcy?@pO<!~~vwD<b4Q79_8_gx_dr5DGZFXw3HkQVk>_+os4V2#2hv?#v*<`FtGNkvrb!
1tGMmEe9S;6iIKA2$#1a9#3GlA_+mlzdeDc6))tybW%h{k{O+e*uMEj81MUjZ0dB^WyoLqY9C79(U97Ts$6GXt}Fi(7?mT?pUZ8e&gmG;2qgs4E`WViGus}_
{jZLP%mG%O=ssjSQAe)UDgPqXh<~x^nY-rafMJ;KcR0Iw|BkN{1SiTf%s4)!qZ6F~mE$HFD)?mP7Hp+$<3@b{pO|hM<aVW+?raMTR0I8mV6sD+II2WSy|KYF
#nE=?c}n(*0ML%z`hv66)!p0QA@^HPG16bPK6yI13SKKkNY~dz!tIMoXR`jc+cz^NbR7*6d<6~Z`1y4W1ASSg`Ff#<URvj95K0Njfc^tzv>~B9$x10IbDsu!
BRf@L6F4&MT+D1Q0q_c%&7Rs2ajJk-OfA$#jpUrVw=$&@t1pgZPpFT`k>($ae7r<XNWc`y2C)Bo9EJPj+q(7D>OB=6Ft2#EsJvjzMRx@|f1)_dO=C`QF>CaL
A1~L`UF7L&IJsxPT|%l@Li3yE@XENOw}h3}k{-%gEGb*;k`G5WTfC<F08M57A(LQ~#$50`tt0~=zku)2zE0IZXG8Fi*#%bJ1<I}rr6auii8qp2Ud_u`6#j#`
fE=v-)!k{n#<CC@hA`Q5?G!6j3TR8P__2Kr{e3^zjvte!*$DnGdT&|Ti|mlj6WNTQd;%q-FL^lWBs^pY#5?nYqqt%2vwN3g9je+@1(l+|&e($+BJ(-OyHftO
UFu6z{VKGNrRa!X-!@V!F<?WrtFIvHXTbBQhm9$v;yRA|G3^V`s=foTm7X-*^VB6e$WM;?2}q_!HnER+Q3%ltHsbe(F<}T<vD{3|`vx`xBdCn(?Dqa4;+Z{(
z&Bdfzc5@*fV2!sKO-+P(e{8=NKu|$q2?F4Ok%o>&PR$G;nZ**T(q>@G=*!T`19Vvk*bXFYv_5T^k#BAsn*;AV?AhAsIyO7)Rk|-pyI7uzz*~u-Nim?H#EdC
@noXlkRMMe51Y*Fh#U&_7n(oIl-!x=xUNt7VC*9ezXj50!4YGoTc3wXM;qs=nU#AM7h()9`Q!V<ZRI7eF{&%3pz*e4<DZ1r?(yup6pn(d@kADa!E}}mE>`d8
Ge&Nt_}H&1>$YlqwXiO603CwbZdFf+nE_}PB%BZx0#JhbxeL-rjMGHuBR|<rD9I=$@IoX@1+j(=A<MF-E0iD2c7HO#EmlJGd&A}S@A7D-)))ZuRqYr*+|bA!
Bw(2ei_&-RTFdXLL1@h$c@Ag`K}J#1`S5U-CU@dZETMFp##aX&#Rw&eVbfK+z&j&R_e^e<Gkj=RKq`RLS`c8RSE1!YF?37M)cU3sfs#ZCdUa`3^L^Loe3aB2
f9JH^2_^b{ZvefD5AC~elNd)OFu92ic}=IyC7d_+-p8L8pnu8CPz(z~1(o*ChWptsa;v4Ror$qepxJ~Z9X^!vEZN`ll3k0HifZy2dvo%gikEb-*~9#poC9M-
E%J8Ld>0cjAo_qE1F`6rV`1Ekw1F-5$3HfKMP#z`&xHs3+;i>EH)E{T8E><(KxlyGQeUMrfgF1SPhc;o67xwYkEH(r=lGK8`7Z2HV3q?e2e-VEyHl$egFQ6D
$f;&76UcBjJla@Gyo*#4pK`MEu``P}zF^(0Q+BKl$AkV9PiMgQH3I6HBk#fx4h_}n2Ko>Y_es3ldxm?+aojF_?cRWJ_*5UeY7p3AnsQ{mglZh`+eoeQ$X~jd
6LR0F+YkC!vY%vx2ba~g1(<mgVv1}0x=YaWm_2gA6uWk6BM^Nu=f(m956LIeDvOwTb|5P379lD%`NfL(3vkU~Yl1Rrw6eoYOdViXcN0BU4iV(tmhn@w;{{C%
vx^5HvVZf6G1zP47T)uNwTiW7y}dq}nu1lCU`S(d*jq?G9RS7P_?u1`J9O<k-B$w&GIa2@3d*|vCJNj@#V%?^hDTD9NR|D%Vz**bZAzKi6AGn%N+o@d1g$d4
0J;AVC$e8+!t{hx9XWyybBG(^-nt`(D{9Kj&tS(Gh3#EQ_Iu{wQ9b)*TLg1<tYlLx>^Jj#aBG~4<RQtOZbF#xDN!Xh&F?@K7z;FnJ?h-S9#QQFQu}uPKp(r8
!l6K`ZT-=*pGOD9&Q=Nk{t55MbD@P&Qi^Db<n}GKe=#7sA#%BJsfr2C0N6A38T~_1=QR&#c;pGqgkni;Nlv6<Ffn^F%sBE%dg$Z~ah4Dy4H61i9M*oSmx2L3
qyLBwaATOiAJi^qw%{kkLSV^(=1a<qXjF7c$+k>w{pQn$A#FfW)lwCTHg4+hbzHEcTO3pv<5cOC&G-fo&mZb(5}+EFCi$v6$?zOjnH*B7m3Hk9qe~L4p|lRD
eK;#~D?R3ax00xK9-XL|uyd@ZplvQGrjc;qkZH_TSLb9-?Zd%Q63@UB6<=o%WE)$sr?<Z{{wK7zsL(`}J9UKyV87rP8p{MLxYch@53G9~9H56ios$KjGQgfl
*a!@#3lRV{kg~2@tv(0&v2(O)+ojPIWy_U)shw+_b1Lw=7pw(cKSbk7&8!Q9jeGD=q(~_opSA%y#?#4|9~$rFS*wIA%gx3H!i9?O-B;WsQSSg%iO|ktxDu=2
B8Z9Z<c99>TFgqLp$ol{_!C~I0hGkTA(9#M3U(rl^yqR51q7z+aaZP<!$PMGCcjVHt5O-TiVc3xY3-z&GfdwXt6AmpjXw|kOKMn0<n7{11{w{}b6)*`<>nEm
vTyF`8;x^iAgT2I+A~)mt&F?7U%{@;wp7zIwEurUZ(QanQW<45C8R8jDK_&S=OpLn@>^gmd}k!@LpPj@cHDl&7`2V|2ZWGhC5Eo4wZo@KE+bWvpZ=<e0}eg<
93xP7oFRDb2kXZ6FJyefa+2`X`pY+d+G=}eW*sQYNs9K3rEwD5$~_Hu^T?|Z;E{5RIZpeWv9Aml<4Gi8e8pR$sQeNp$_Cg@<a=sd>HvV!6A5p>47m;A0>eE+
+8^&v-J{5zP`bYvSY3rs&Gw}~Vg_}(b)$o;u!T%KFMt)ZSCVfVUT_gjzHx?oUXZXA!;31Ja(#{e#DhbocRvn)GKnf6*010kt@|jL&b-+wf7M{F<&qqh8eyZz
2!&6}6Nhl^WBfBe?`?IsE;zY(*uQ`oCF{f^CZP6C@yiZyY&^f&q-t~Dg<>yXPz=ij(o|4lVH`9BKm8w{^!Wf8>(+QRt9ilnKJ|w--Gyu3@QSLnlJQ;qOP!^z
>E+Y)mfy4-F6`~yl>{_Xo{h!KV_;r=D@ByzRCr98^=EdpV2B-mZyIDcuskWaH3=?P?~iGIu*`xA_(SwK!3J$djU|3pD|UJXq(4LP%&Kt$Y=;Qmb5B^|rGe|v
EhPUTaj@_;hwi6y`z?snmI|(@r>MFXR4d-C<|T*!J)$?Mu3vunaq=6VM?cTV-qB?ULSJ?18A)wd=jZ{LU0$l2<GoaHf+hnDl??w;{m#iTmdnYZ#9#|=qU@oJ
b4T%W(wF<CGTZK+PxMg;F4O2P>HzVTuKo|N@_o$znBpyq@Pq5B!6}}AI^`>nXdj$EbQ!Wyt6lIhbp8NauA*-FzQY&#n|$5xw_edmS&jgj-1DE8xye(7d*~7o
rGz=vmNvfcY_!+(!kq^w6B+1Db`Gvd;91@@O2(+)OVpC*X40d#|1=Ifub)1Eb}&0fQB++I``d>4|3j_a>iA7b<<8kuvJ3lTckDV-29V%34NI6A7Q~U{ZyLH+
Y5P$>*WG@!iU5N#SO*^`bWiZDB0=niK@i2AJ`<VMb<teft=@4S*0OFfzn}<V=4y_p{H>BEly9EBdu01*g&B*s{9N}M;@V0tcX)K`tZlbQFipnPmU<J`zH?X3
8^=bx2CETb4e^NR?)+B@)u{kp%WKASl!E}I*t~gNfBAD!X|jkY2;J$r@`4=1!0<FxR@s-vKk+>aH*ua{FtX8r+Nf%hO&-cJWs%3%yBb&KRGw_tZt!bqsPmbY
yr|C_+&O8ZWv0k`2y+^Ag>5qo<7v<KJ6Ck+PC_bHn(rw~aP}1#3PF)Sf<_l$7wTnZ;S%@+G1iL!c&FFGXT%8fJVwW(nL*y(6z-)20o*?-<m!3~nV*>de}cxT
@Scn8Rl%qQ^k~wE9`{&Gm8ZJaH@Rc-1Hn>?nk=Xr6E71}jJ~kQJ3!KVqzWVADCc)l3<6&p6eH2kJb(6|k@7kQgZ?|PX6|eB;(^!39&bNacIT&{jU#vxu_;jv
HZY_@3+RE&uP>0$!o%F%1lWmcFx@f8ETY?1>Z*eFrA-vi3%DH7(vE)<IBj&*Ic7O5a&#1B(^#9CaF;pGa{kanBoQa`qC+Y;BAEYKIl!t?Ca9Ee3Qy<))t3un
a0XI;W*%rp?~Fw9mI-}wkD|XS7-?~9?0^J1PqdI-VLX8V7o|OsuV?0Gx5X0QYvrN>p%KK3G_bL(L3G6)+8^!plD2l7yq#8^dQ4?)B1R$v0(xqh*XcTEat*j}
*Efg?kLe7(;<@VU<J(vQU$YfS`7UJwK}M=hrt)m8Q(Rh~6BLw?Up7-kGB@eoLgTybj{CbN63$1e=vX%aaAW~}InnFNtuhU15g-`dmbxV>fpj|W5@D4k(ooU9
>3Oe(E_KbmtLoW&4*7li>ihN*(j58)X$s!vK4FmXo934i&0B_HPBNv`&!r}`KR^#@ua^EO@WIoXIY^?}K<Jm}FR8ZFFRR$3-WeHgASV;?mDYNkST-aLTwaV=
cn+b)qiWWKCl|z}s-LZT_Bb}yCZu=`GIc|-gH(?6aAGx-0pbEO{{plSE(NwuGb?uf10MC+_v_O;dXO3zEW9jCYGp*HvH<hOV;2<H$m0Ibxa@SrUJSh(r)=pF
Tw1mc-f^&NGaZXI(b*8{<Hemy%Go#B76Ccx148tZHkEP385G#1um2@`)RpsCy!7^G_QztLU)Kqyp4y*c^wkX!ct|jFlUQtu?fP;nV<wnpvqv2^-lhW{rLExK
VYxWf@?z{_xfdrtS<V>n|Kdq$&=&EJBxnG>(<<+Wy0yf|eR1{shOM<J8kA)S&pduuT0G#2GUSAn&43}@-^Il=zKs26|2)pjO;|;0H$T;y<%!Zj%>x*O?-$HW
5cI#I?Ym084FAAnM}TSuyMrsU?)cr>Q+v}ye5hrj_BDYCw@aO4M@pYaTquo;ITUs3p@w>;_<E^`XwC(P|B^zvSmb0q2D%g!dR(m$AOFT_&p!H@hK*Q!tM1_@
!1f8~#6<T8lQ}$bEUj-ijWdDyY!=-3zmc`DSj$Hy$|F(XF3#r5;?wzRv~>Z<{HOFh!;NGsx#=jB_<iF!5dpQT#W;hbpc`Y`kWEVIrt6!UH^t}5uj{NfWVpe?
u4YSIQ(6xl9{JCDi+<Cto=(+0F^%ZcVu*rF+)uI?ynVYy#y8(*FwLjSEwJp$8R5S_bO!uBv0cm)MhShmY5sGeckm3UuYk}6<vq2#%8UMuyX!~>NX`zQd;*Jt
&n^pksV_t@jjwPE8!<}w0K6e-OwHB6z&A3sy0I#NN$!S4y1P?w0GJyvW(IWp!XPWJwYiJq#OQNLS#ItRG&A5FFB`IcdJx^Uh#IUC>6+aXr9f03Ox&4faNptz
aa<olMR*;ZG)S^Hk0JU;$w}y8*=C7USExTV9<q$VThd_Z1t-T^t-&JD6DAVED6}8_#1)^wi5sWLmb58QBlr`J=6(h@iFZS%#t<kah+b3cSGI#a0j6z|!~)7|
2VhHqw*BF|;K_UGgc<CUCV5Z=6fCX?bdPrp7gTCrB;Osw3)>v)O;Z7L`inTeQaX4?Uch|$VC#`g`(L5Y@W+q=F0HLPp{Z|aaPxk6v-RNlx+`~)a^J~SEq*pM
HXeomk%_{N5Vl7}z5Z^$yd4sa`3<N77upZzYf=8hb_KHkgXPH*J8!$5db~3l*d$$7!<b#uWmyNt%DJ~aa)GOWLTz)#nLn#8JFxnOSd2~iC1Wkq5a*22c`5wz
n3C2bIh<9X$J20zAk$kjU1rALq`spJJ3pxPFMXKEzWceH51h%VQ;uGN7x>bPT}^KOX+78TEW()1mNnY=(q}v$bWtYKXltv$f0+<LUXJ(PD7;z}PTV@(KY@K2
WsPeazSgcD0#l5$HzMbj{lghHd3KJ{=7~;mHv@(3pzcsnEQdQ%<hH`YGzuPQCjm?kQ@#+?=FYm!Nhgr0M_)fVy_}GfAAykvY5#Kg{*3L7o}q$UaY7nEbQ16n
zvm-=&%-b7E3IR=Q0JDt0{l_#(a^FP<-Evi5i&!0LNKutWzQb<57|D@mZ)KVdTclx&2qFXbRKw5Z#^p|!P-hsc?^_`I(Nh5fQ4DW$%dg_Iu)LK7N_e<s%M16
=yg~XR?u^rrB1XvQDQ7Hk|oz-?PZFMk%@3XEOHEOuzKwjLcj7#Y3mZy+!=fQwz>#!7NOWuUOSF^Lvz#p%AyNB@6DU*P)2wjc@_TBS`nY98>jYS3zWn(S5z}L
-6m15r}zN$4h;HtD1E^M|G2tfc-1WS)GoJ)-Q(rKDw2X7y$0&0ClvA+;r8ghmlDxgiyy|ICZ)(icO|hPg?<21`?a^ni^_{SV@u>WIOuv42Xq$KhdDt-tAF{4
%KlFu?GqzQ+GdRilL+BEcA&r+Pnt=CIpvnXYK`GcuV+hULfy<<v1!3<bDfh+#$|C(ASo0>L4*5KaUFedIK33<pS4;NNl)NDs&!RtH1Dawjl%U8JfkNOm~AtB
4m}24bXu<<)!>MW2}ndE++WW)cP~7n>cNy$y=dOiVQ|`?O*Y9nW4=J{UmCd4e&-?ec1elaS2}=X)UyN6&Ie?1NtHsbN5M+}oOmx_+46ndj8fSGTWC*>3j2Bo
z*Ks+0mF~h?BzgcD-@KQ$O;k{u_xxu+3n`7dFOT?KyqM$1l2GZZNFn8O9^nnDNp&qP<Z^F^JalJiHNjJB_5&8s`3aWyBGmMojl6zTxSzCN0~L+RZM<5C|2yy
MdXv65J=DM6)Qd^m|cyFV5M&X69G?uTygfixGC~!g<R#7sa^4kZu-|ySHLl8eI}~^Ky{?Il)9kjI4y3`OkhLP99ha^Olv$Ekw2Mzs{u6GMgwPLn-xbE%yx&M
tWVLp)HzH)r-2al;Jew0Ameib1=1c->}Yp<yUp6xIkZJjDpNKJZLd<&jvmp+_^XER7L`c}%7+4lxLA7a>4~$eprUs4Pw+RnbrBp!yV*ByewL4Xa8A1<&SD8o
joyGh)5k=;zVpfON*xqmhJ6<mYRG8INzi<e7V%15Ax}mSYjqHuFN29ulb<NG!IWli>HE!YA*jRThG6!K^HC_F(G1%Js9@=_8qq<s0QR8EP-^W}3k+C)tP5&I
yt|wgv7(M;bsGN6yNw}#u^w{M@Vj#T_X&W7eVkpL&1><^5Tw8d1pDl%Ru`qxx&Y-epmJ)|r|{^+^gl@wShG+H#%{B9w^B@PV$px{rPCSk7J-~~ge8H^AG0W9
xs3SJ3t7iMeIYV|5RiPc;VPJin~7Qp_r}AnBO>UTC!dM^!3HcIt}?~Ts&qklOnj%VzwErOy6Y{nKyc72H8qyFtYlBXM{9zjkqB~@CPTr3uV(dx72u;7W@DFq
$j0pWZju>s8rQisIghx3LsZZe_8nd&>JAhHraNoH|GE(6F`QlG#)YoH9V21JQPl9uCwhKU>JUh!2OTT6Y+_6PAiaQ2puy7d320hevRS!Jw4)N?w=AoM-flS`
W}cogc{{}*^{@l<3<6_8iH7V$I=K3!%E4IPV~z*-x>)|hLs3>9x%jG4vYFp<)^|_Yi2=0YeuS%w7jPYZE2V+2mBzKk6K!`Zh%h<Te=XLI;GJCrLAK}dqB<0(
#iqX*ga6D1oNjHnf-L_rK$DU?NvPI+d;8np?$eTIVeOmlnI=cE4}kFdI*0g}Z4A;8NZ|FLvn<-=ms~N*tPi^k7A!$!kBz(*l_s46BPg*k@`aR#v+#$MhzI}~
CUXc^Q@#7qsFx*67kJZI!&#B$Ddz+nD?A5|y7`#H+SMg}UE3dSd;m}^e<naGfsTerPE$L3M)(urD0~2|(P?x+e%)|!DOD6bo!xs|A+Dhc{k2FfXPiV|R`1qF
$pWb9h4F1}2xS0Q?{nD6`_naeTD(n?ZXASB75SFPB8x5544usQ#=2qE8<j4z7_Zc!%j&<%e*$$Uz$F$~>&gkh?hLWHFE!0jiIizFRNU2DotU&{u}9R!mP0~I
X+5LsHv99$&W^8f30ZxahnXqkJ}DfW76U5S$O<?uk^>b^xiMM=qDbGyjU97ud$rZa0I)@N@T)`zXB+gcON#7?hI&_TwW=OCd7nL{68pjw9M{!QVW|Q!do3EQ
>4CY5SrEGG3HzA(3KVEoHm77~3mF&p78X&cotaNoKAB;}vM!qA4z}JIsOCjeDdCiDnTb+LN=_oosow()vErlkr}a-Uo3ap7a2+iIRFHJfJ34<Iw!c=-iXTIm
{`|s4%sB^Cs`#Kujr|sL@S!A7A?u4~o7)q;VC1F4xGSPtba!@#QwXi9q<n6Q!)dDFLOk79_{>H~7o-#)&h;;S;zvt=;n%-{zEuN?me|lh^_Ne5iTU~-Fzz?9
Z@QGHJ^5Byintm=@)wu_*q9^eugwo{rjZw=ChCv#A#apnohrC4ipL+W%3JZEBN5^2dB+<SN%fQ=6>7=ozon|=u%|pPvtfZqLmlTp`(cR^ep;Ie*b|nS_Q0|$
u)O^G%*Jy6rci6aVDYF;a#n)vq68#DX4@h|3@Emsw;p`<Z4tRO8HlsG89Wf7tv2*vN!i4HX5P5wz-J$llwjrbTlJ3{+1SamK_Be=lmWRh*7HYR;lj8~yZ1AZ
2ofu>2*_#o{}u2#o?XisH~~s-)tgKi5iQD{9Q+mXg`&FVrG#)7pH~T}p4p)v&d4Xov%){`WQmAdIV|<Y>szc$H5h=o=rC1@Y#PHr7pS;i5NXHJ0tq;JUV>Wq
&mz63`n^rvaoAaz#bBTiHlu{-)T~%Vp<PYM5c(8yf{II3S5!Zn@{;q3_EGqORc}y7ygU|zWgH~)Ai_Z&6%eRv?vO66w07s%ew3RG5rWOTqa2<h9QEi_-Yt#%
rODr>M+u{Rq!X<r=$Hs)XiwK3%A+E`RFL8dy+}5iDgWF~Ylj_h4W;k*3vy{&F@O|U39IZ!#Z6=fDo4oRYR<B(n)EyCk#dM~v*0=R@(E9&V5XsKT&pZYjD9JV
uzRYa1PX@Rw7wM~Y%H&q1TQ>L9^koG8m5c!C9tp~q(9W3XU>p*Ar%284jTnU+j$1@@n{6YXdd43h}2LgSXeqG)`^IdHZMs3R-6Mz^yEXLl+W2CRO@aX5|f|t
%|3RXk{!$d-Ku6u1Ov7oY$w`HJ>Emm!>FFw6!b{ADcH+<kh0d>W>gXh(wcwOa)4qEt!I7yf-eKc3qoo)rr&3*=FD<OHDD7K5y&z~tZ8Pw&5?4Lnp4`V!Su-_
D%rusd|Dx<Zs|0aAA|@z=R5xlHKNhRDK?aCpT?~`_ZRqKQ2CZA5L&5=!^y+7!Oc3llj;GzxxjYGRX-`p;9KA2{Y>Sw)!9A~SZDLC9EamKd#C20tYAgb%J2OK
YEv_+kohx142ULmk_$>T`Gyh3H$c`r*@c!L<!iSFdTgpPGn~L(QH|9P0=Dzm{c4ky7H|Jc`<VRKW=!3<O3L9scIVvtRuLM^?U_$*YoTHdyUAvwneZ}|ZFblu
^Q8*jd|~NHG{|{=f-?+l&(yT&+GpFNxXQ0h_c`sw@JCC}q*BAluH^5?SHb#7q1(K~y;^jVyq`|M+1jn#fixy~DoDuD;>`ray^vxRDATfs=ESviP%49Xv5ehD
`70oLYDJBz?Vz*hbfv${$U`x=I=>fBS`=T1<Xw6}6MwFD5yK-<kh0)>;=6<_x%xCVO)9o8HS)ts?I&wI2S;++x9)y#>eLDXS+5D&>>UHqwqR>8M!~LH;UDJN
R*-GHaj~pnIE=s{>5dGg9ubaUUuk*jpVu{1L2Hf%{~6&_(ldZi<alUY#T1<(=*7qe_jOROnbb(JjPRKrloN#q1gh40K)_aN1RuQ}+N*xP#K+KSp-q@)xn#UW
A$fW1#&!9iPFV+7PK=zN2%?*^KFEIM_{BJtYc?JT;<@om%B|5UEy1hm*UhHvDX@62e|l;KDVtiK)qx7q(pF$}o5DWtj}x5_JoE7{_V(@**i}>Eg9lZfdq_{m
qyVpzY6t+INy4*UtWva2hW}!kd)nRTe-SEP=}3(ug+;iNF;XK#(Yn|8%Kq34U*+MxD4mtQXX=YnL4U%cSn@$0W)oKncaMm;zM4&BhWq3=Er~7n#E$5&-JN5&
PF)Jyb=h@;^Pm(#c`8f6xDsB2Nzrm}m}mkM<vuQJLTcV`Tlh0uuO)Gsd<IxeajV@Yk)}Q?=62ZpjprBe7es0`3Nxz1!6FAb%`zZwEcixFTPtFGujvElluLZE
uI38=KF*oZrC*;4JoZi)vpBy1+vwC3TUFKLfx8HVI!J@>mbtDS2UdO%_0*O-Ziym)1vTpb^6>C<z=(C`07OxmUbz*?uY)Q?C-x(&5OVlKCcg_aj(dJh7Cn5h
*z8x~CeUckTo&I+7Df}z!Agz%+8$<0VtyJQchAV2?FYJ>sC#c}^YKaJGgUMP3@nkow;KeIr`LmuJWUVDa{;~<p>t~N6tHd&0Jx|d49y;rmkDQLs&<}~m+uer
x?x^>Cks3o7aDn47Rm!Cz(e`FuWS@RUUV!DmJWT&#)A4lG6SA)d$O@)@CFPN<}ryBwhM7yE!P*7um}@|DRGh&-aa<{9~%Lxo7qRdHV)rJ47QyNW~2wcex?XV
(|24D+$PI`xVh0${8rW6bb@a3bEfueX&LI0ow<Xk+H6Uw#0<*~ewU*lT=F3F*OEeg$~l-mvt}bWR>MtAYp=_${^r3KPc-m}TzElPb*QHvcBAa$<gO#BYnNeu
005?esms7hRNYmmo*zqFlZ6VZb<luusD%vF7X}@6%mF+$cMfzs{h_|i2?6NV5z05t)Ca}<(!3DMWx`z#SNHD1h3M3>xuODDJbzCF)?RC3vNvNc?1iL%0J+74
(#OS5N$EH2ouMcwKVa~wLLn-TSRVBKM~b7_5uWOiWu=(wkrDn^In`dWTP!O9yg$zIDG?!E&KlXD9qR^X<hIm6P8>X#pht<6weDyPx@=`n5wK8T>6kH<f^9j`
UXl1Nmh4sc2$7q@KO>77r%xAKIP#u_RdEmKoqOI;#|)GAXpjK)$BKu_)YL-5Upl$d@s+wCB#~hf1u;h8rNXsAwpZb|$yNi<PQyuwVB+R*Tt^uP2+>NVHp$6Y
Tu@3;!eeaqlEo$miCfgz-kyXCU+t>gh+j%*`7v%zym%`f)EezinE5Tkqn7551GY0dF8=-x$oGU=@{3T57Fr+)UGs&PpQ}(C{w8Sp7xnd=9z(lqU1fX*Qjw@B
MHOzoBmD(f|94W-Hm9}%WRSOZ1=ReJc_8gBBq5!Hv|P|yg;oe)R^k3#HGB*Zl%BR7th90G<Z`OTWl@8x=CK6VIuTS`oFz5D&=}9mOzR(P!>^G)>uiV&GpX8c
Z725$s%QwHz<4W!sAjomm2!oaHj18)PiR_xA_Xsyjgj}kxYHkao297CZc|7#h9|gDeLR0z-e4Oz`W_{`j?ngOmAqn0xAR8s{%_CsqM7M}u$q7#3s7tIwM<13
%5C91ewUaeDlBhmboe)NXY9a4MvhJinpQso+i-{%sdFV4r{2;#Ca-g<ot7EXG2sK@D<!J-L(*9j+&Hbvs{WlTa%xNN`y?N2oblaWg^A@4_=E;b=$$>+!)$#Z
s88HE#q7CN^>|)?bgE|!A(ho-SiCwzYfta?o>EH-K5!xWJ)Thl0?KszoZ3Ib=4LUP5p%>-xvB>6N|Zv48g+Lh`!0^JEee<*?Oo{c#qCVZH@Z_XBd(Y0BOxnP
;GOT&rP-2;=)-W>09G9<Xw9L+N1g&esM?SzhRNxKBc-iYaFq8!LkZtHiB~K7QV6-)>&Z*B4Qe>_gEHNsK%5N+L(gKVMtfi$i9bk_UpRVwJw^-q#J{7eW1SJ-
<>eo)38I7a6*9X4Q;-b62Vl<o-HTaIG-4@#MXQB?)`rV#LF)E($BG9FMpGPI0-6w&MkP=`k(6MrI3n}u^kGt_fC{zuMFrNgMGC~@5s%W`?yLPm{<&v8U(zf|
PX|6Q$LZ+<gd8Ok9jJ6mm48>~wB)uA^A-CRG)ZC1#IKp)!nL+PgY(e(rr@%*c5hA2bR<($gpt=rqL>ejRT$?hwG_8{Pgt+6V@27;D+~(ustX;p4TI|I6dib%
%OtEI+3B*D?=|w-h&|P!yYvavFS8*ZU8MdtKVwR*s^33Hb*!cEt;i1yE@-Y6pYV!`Ykiy}M=#TBS8(!2T&z~5`y?~99I>q@IxI>21H~HinW$yQ9#(!zA$67o
(Ss#4C$6P^5cvb_U!<FAe>Wtv_dlIfhmD9eq>0jGUP&v!$HgcVM@hY*eRet{#v<x7avd$T6SMj@*)|{IZ1z{<Q7Oo_pHVobryK*2G#Zc6IO8yTUb;x3$J5lZ
J~yMpaVCG2v9%JdKfiSE(r!b+)$t6Zkfc&5>{&Bck0oi7PL$#2FX+R}3w%4Wqs2_o>|IzIO=H*Bl)45~#ZIhR)G&>+N*hwmVYh{$!yE+&E_Q`0UmqqMH)nxS
UfM?NjHomHj4lEfD~_q&Q;xLJ5|oO)`cgOGwV+kpRH;w$N=bzRF9R1=<{ph@Dk>q5<4G9uAGgscd&gtPu>MsR{j`tSli$nD`@6MAWS8!wAI@P7xMM!D^QA$m
x+uW2-5a692YsXnvEDd7?QV!f9$|w@bMt(n);PT^9A5`lBK1p{HQhv=!^p(NRw72b5lE#?P&_35mWzHqT7r*%G}^#?MJXk}!b=V`b$YlImlbKS%aRwLzSM0}
cQe?2<ghBjEABi;ZanHM#EAkpCi^9PD^at9OTb^D#@T1^?mj3H+va`?gDCQ`lJKc`aJs;(>Tl|B8#UjbY}`GAqAiw#r`SOFJwxSbIf~LB=EUnD1r-%E<j;iH
Jel|X^ecjImg-lH?f8RqwvW=hG*winnCeg=-W_fXse&0bqzNHfmvwEyZy98+491y1UDHi(##NE6Q_^`ZQF`_PA}#3|QuApr$fEy)pwcO47c`%|!oW-vjX4Mg
i|?30MH5qRJ241!-ij(PZ`f8O%%K5VuVSQZ>@rt*-1b~2UQ4Ajnxh{mQ<|3SI^y7KzsaDt^HH@=sZ2<ja!O0*trUo2SNCW#eo&U6q*I;-l?hrt%!YC(aTfOA
(kr4D2Q%s<`??nEqZu?VPs$+4kZyJmS(A#8dC^Qbg$YHsO9DjPSW7vvlLSaU1Fp-;tItv599`8|(R#Jr-NVpIaKj~M@GlV;J-71uhs8nc54K;KIO=%36@bPl
HV-D#2o53?y%Yk_qWBVmYIWoMquL`4#p-+pW^n*CgT(F9+dioeFGUsvZv&*xam%hMfM%*O^Z}xI0ZON!zd)o9uHVh*(H%vZ)>kD<DfO_XD^-leYW#@=Z5cD{
<&|QWf5;`~TClrVbVO0(%BzueAw&xp_&yf7Rsd|kUnt|Y$J%VWs5rj<fUd>Fnclrg>26r6d)iz6d1IhZWj0@I_txQWU*~?2;#8MgyItE9TDK8O^?a}Q$gEF)
-zwe$WsfG!pOF`f+hXoAyiT}sVgf||57cNM3fo8a&-rSODZ`S-iH&(5aJdAlLNdyoJox8uOGai4nPw-Y@*N#e6}Ck%#>_8=llKb%AGIuY%K}&}jTX4nyFP)$
cY!a9r=}K)47X(v`m7zQB0z+|@3lx`6?~0lA;NNSrXHNXE4->Gs?9XR{_9$=D<eC2l2H&m`H<(znWlhTfVSiw3hkOT#T~rRalmLME^*A7Oq`&;J<h3$X0f{w
z@rs=clk|KeR(qdw%B!U^4RBv1<rjH9cs)D3-LW*X_+36l3&Y3LT%;Z=f!B%Y;i<zRy8*C?Z0C`mBl1cDOfFoptiJTpVu`D5Bo9xsSRARHu~u&LfF70)BNt{
{>RjKEtwLnS4#~{2IQZRi&#8|VEbz$FVgj~1`%|YlTi268XaZ$7*!4-FKc3=G;ge%(A4w;;Ksl2w|}O%vj+(BB;kDdZ5*nudakWczY+vSiwr!AGs(XkW^(xd
=_<(opRg)KniVsQ+9CBw=CEMpZSBzQ$s+<2@Ut0UX(aAYHwQuy{BVi>swV!vI-igSm`{iwO?6d^76$-+qmRX3VnA>K6AH(pQMp-sExZd1<1Uu;;w*gY^IlHb
BI^P}x#UM^-M%-3rmOd3?L!;?qX_j~UCefy!0b;sgnvWQ^~}$OP>r3`WIqi&Wb=SlXEz^GMq2t%1kDD<cKKjmJUSaHeiT9Y<T$vp7qVUNdGi>YWo#BhST3s<
oY}J!A&p^EoM0~DYGrkK_WDZCK_-*qA^VW5BKrxz095f*1Do`Q05J8u2in^dHl6?f#LSQa;NjrE1=c<vg9JWdIaA2dnl_l*ZvA$-(PICqEP7ynxS_nG%Zrm8
_JQzIH4NWcA6;;#pCcXQgnLg7bs(NgOu6z;hl;|`TcDXwpY;w5EUWNY_IhQ!UR+AZj8y3{q{{5<=$rF$!^(xVhO+THE+6Y8SyI7^4|(jq2Px#YlYi%mX>>I#
8JNf<{#@3)EIT^JqP6QtAj2v3CAU`&A8TNSekmkNCE+AUJM1AC`G8D}5@3kl;g*>QB*Ht)6+d>9Q9)#Ak0=d(m(G<*$CUH#<Ht|>{7b^DI-YXPtv+tJe)YY{
qI%$6oc7~*M`273q6&0xH0&G}X)B{-8;Zl3$!2D+y4JuS+!;u-3E{LE%4S#KRQ%3gM-c`-OfTp91b!B^FM4qOR*)jNMHdZ;Db<BFzUjk1_I2MWTyYj`kO8t6
Rrh2ey)30WL~%LanAptT)-LHBk%81kTym8>+>o?TrLFh1_0~!BTq%z(*xgH^ixx1^dVKm71!|Y5e{vajZss9-mqYIsj(Hf8dDD^@>{SpRnO4>0%U}KV8o6hc
q_%@u3fEyL!=S__Up0u?^b$|Y6`Z|9CUSIfBb1sGO^U25Y68w2X=wCbC$;YvbAZpm3N!&U6w8H3c9|G9yQyKxnUxEJkpRR<^MqW#fGT)EjVPr*usF6Q0T<MT
e+l+LjUvbX3Eg;qt;IEEMSc<9zD{YFS*O`lK!**5#qTXk2MDh$>EbUCuC0EYG}wxvG8caO1ZQ}pcnvu@OmwABO1$)%Fev%hgQHg0<>%3$Z#o_nwJMiF`MiFW
<;&r2D2b;IV$w4)yFl%{lHv;K6HafAi~8j<OQy>naQaJY^@(G&mBN6)z&S{CwvZGK#jj)h8RII>!;6FS8JLRfsuGf#=Du;xBdTLl6kGc&8=e)0m5AFhNPkFT
0?V*SkXcY`zdHt0G@F#&Tc~!$CwKP>lwnyogHEmyj|Zcas04)Y9M#fZlAPFjq%xA%)UQp)!L8@>7-Z8w+|#f&Gs1S`??vdbhP3yHruQfHO87Z(Ae(TSSI<fp
S3^-t0Y4C*%wG$;I8lj!FVTu86N<&&#Q#Z%7r%yeANlcSHC{=IuduymiVm$$Rr2%%KeutBWhwZh*u|+Z%c;DKx-xZE7RGFlaDe*y)<%TRD6Y17oQDo4gI{Nm
iXq>shkvdp3rYLh$@}sD;c+yii`PjwyY!R#^;9YY6`5axrHr7Cfl<Mqyt`59w|KXlM+q3U03A+9J_)>Eg5vkvI-ZiC!5e%tKU=s3L`a!F_VJ$M^)KW_WB3m1
gQS2Dqv8(aG~lp8UH69(GQ$$LGGyV9ugHv>b#^K;w8^0rV!d0HzkTBL9(*RUrN_Dth@>jSr@=<fAK&aSWRR;d9XB7+dbkraHVWXaHk*;aC4aGw*1ABEsS_cA
pTSc4a)+5oqQ@lyk_c}D*soIwT03Qu@8%JXMkt23Wjci+K)T9I5Dr!oD=L30)O=;)9MR0=uXzA7NcB$A5&|v7Q7eD7H)!@9g3!s4`4l?oF6youUM$!MZjZ@+
f+W-wPvK|C&M3`ce^=g!XZWOo#vXEg>Y=Tlb@}1WTAdQ?TtLibw(Tu#BO-Wgc;1WmNR8O~oCH*|3tPOLBi1iTmGZ>m!mR6v^dBww;J2?vJh7;251E}|eER*-
;4wPCB~FCUcxP<TTqVAx!EKRNl9vXE0vGH0Umd;r;DvQPzh8JBukYP*o0iJ<0^=qai<APO&}LqlOKRxX)+THr9gjC^MR4j1`G2sc?(d=vQfa~n+6ce_Tp-#d
tR1mm|K?K2*mPsyMpYDEV1>AdlO6kdB;4JDpkxMwIfH{7=!yL<v`j}jdypIl)s<2YJN^d%+}=tw)$LXAbjq-Xq^X_=ZQ1EBvjSxXvi#oESxst0?G5KA#*9Pk
Ktp&6{Cy#)s=ZKrh7tMzPO6jaKpNBF0_~Ft1F|8xjc9N-@BfrK4q*+b@x6x5RWkN7_|*w*RgZL9Xt1*#32j^RP?4&c!<U~_Mcnz>0XJb@8}*VJQ!67zyQK1c
yJdMC|Di6jK4rlI$)GlIAZSqt=ZP*OOdkwX5n>}ZqHf-P1*TE(Edla`axH$(2*T!!xXpF-A1N0(cz9oTpxYb_5pe3U9hsxqDDKnb=0t&Kt8evRXg8?;Easf|
7-E?nO2hP}$=;NbE@*!Biy02e`6eo%6OU*_NA)&LZe3Bg?)*UNe3@Lo^m&-#x<(-$xdCAgVT}>n47>2Co2A6XRx@#Id~R)<6Sqjz&}eVc7|WZt7`j{!l*b2-
2t8h>-+B^J3NKvdh*cSy4R)1c)f|~B97pd}_E)y33TtrCqcg6=hy(z2-Y}*>v6HWN=r7pdp@yVLD$(}2gCxmgB0>AU;Y;rd`3x&e71Y~3ZAQCZR4hMiDgy10
2m%T+zUN+NN6YBgEh;i!cA0#h>Ak|1ZBsg~MN>Zk;o_3sXlF+Uedy7tGqfDAZ944!Nx<w+<h4b+qAW7AC?MA;4^$69JZ3uZQF#ZlFy9N`e)^TZ%Vy=n-oa=s
%R$+MY$1Y@{?8iv%XUmFHc@p&3E+*o4<SF_hf0D?_pzf)anq_OoSW1hD}MZE6R@-5n@WrB<Y>d|zzi^i-K5{S#+tzLllYUen!nM)e4a~>JL07{*jzj#eO`>A
^(`3LV(?y!$xpn(K)grh2L|_eydJ2wq*knZ0DZB{;7KnoMzbDiyG96UT)putKabll^iZ1X(f`3+zDm8wtFO@)q1(?r4NBBGa1jG5%46JwqAXsH6*QHjl@Gt%
X;_B$_0`wuyP@a?@OB=n(YQWnYMMU(n_&&M1vEk@t+AK2{w;6aeUt!icAN^ya|x0_e2|cZWyt36>en66W+E@xjuF)+Yh(ph(Z_~t#z_ROPlAXut1l19ef`dm
_^5gjZ9)DCBj=+_=#(gO6K0~sJ^3sEcCY2DVttrN`_QE0Tw5?@wX@0;X;y*lj>6aGz_*45$%Vgi+}_8Q<~N0Gjml+t*?n=GNSX8{B5My)J1n?qNz0@);cc}z
sjOP+v>`w(uTO{KEP<v;N19#`Z?5;^BM=eTM)<kEg@q)A_?}-jk|$OY;JLb!Pfqwz8AKqP8{L=+tY$Vgt~nohz_*D(4LJEeBus>W?35-JXQGemh<jTpri=e)
UC{F;Hl+XmII;&%_;xOv*Mh*BE0ldU+0KXDKK@xzd4Tc~PcFcUI9uiXvAGQ_tcSftm_M}tEx9DV0TO4ke=>2r10vo24>3@j;H^2T1m<Lq<PC!z6LPy2A1BPT
ES)AHMObeSQz(`~WyFh`$Mi;Mv1wr}8j-cv=V!#Oy2!8!7zy`ux|_n_fb@&Y1JcbXzNuwdT+pFfve>j}$Q>))W#%2!UQlu~)iRXt$$O!>1fi4N35RpRTy(lv
%|a3wj>wnMgy7qnI~HJ<D=Xh8<Pzd+qbxf*vE8;VqB+=JT$w}3YrvYzV=cs$x_~$=MK-{-KJNs?X-HL8a?w5$`@c6B`zjKPgVgNcCXl85Wi>YE5o~+9VP!{V
(av%y&ZHo%B8DRk()shkW@FpI(1>}T^x|E0Ky+v_L5j3}HPyNaJ?bGVIEzgwEj|(Ja8jX#1hRrB!a*r6b$5==8VF5Q<v%OOLU|sSbUaiemw3C2;#)tadF|w;
MI2#Lc5ndpe2NCaKO8g(rRsoGhfQ`_O8wm{^MtSED~t*DvK1CbmEd_cI|!TMLjA&5^xMnk9#<|SCSKckGG-qy^_po_VEpCWs-?l@&vvtH$Yp~MNZL@gzRTu6
ZQ1<(`t@T1u4JXCdcKuEXuE2~&-ckJ_)h*xWN%#BZi!r@r@s6HQJ-B+rzkIp4!InJQ%YrHwED9feealRr{pQ>dRvqnBA=q#X_7ddq|-tIgh2dGtZDY8EUxX2
2^80C`gnUlM^_rCH62Nxw(LzLK)|X7AC8UV0fG|dA4og8J0G6n-noXs1_`X-*#1LWU0=N2qzk^=a5@#NqD)?FyQhQ)y6cloRqWbS{WOJMmw<^YvPB#_n3r7T
;$1ta)z68HxF=9s+eGS9PO!6t=5;#!w=|By@hOh5A)`<237&Zt?WRpYat<(w-7ZzK0C&~^htT%(^#7e<{hy50dWz~VvGzrN)Z2vTb>b`SrIW*dO%n53t+#u{
$1pi2S_d4_;1bULlxW(|KjPA~7xHs0#vd#>*P$)%l?Re`5ta(<$79F-)i}npCd|^`A_S!-PrTBB##1Q04Y~R2vesahvF`N)_vM=)Go$9!%*xDnx@SRSf#Lc2
#4j$<N^tZKWRm!#MlQ6AML~4u%w6fX0nl!OV!ZaS|D!v4z~m}}CNRne_s#%$1TcBI8S}&|@HNc)<GfsbNWd^4Yum|aKC>@?F*Xo>@GmHZx?Ek#_>~B*c`bO&
%;_TDW;}vvkNmYWz-q027{4FxanUc+Lw*}L)Uy-#H`N^`;Wkj`ChL#&@V3)kv6^B~Glj)w+UA>xtU)^CPw;!^&hz=26h!PD+hD+hUVB^d2bOF(N_{lC3;{aM
k6yx*6yfzEQUupW8AO7|uc{r4w`!)>8@7NB9F=_WdwGs6&BKL@1;1>kxOwW6j+f6v+Cm3Vmn-uwY}V$lwymNxt$>IO;U<97E8ymc)-Kypx4MT{FQj6=h9jFf
M@R$W1jKJ~$pe7n-;1@}gjREli6z58^9?1A*@!LU?!uF|1aA8B>pXq<6(Utz-8I2wtm8;GVu`hc!51?IM2JE^u-ptyodV)|PBf=lNB|xu%)bZw0;f4afskEx
&UA}zNX6Ggm=}}~4Nd6{e}aov0ty(DnYcCG#sqlhF?}Txk_A_-$G-Fvog2fUdpT$f%5VQlY9o;NQeP*;d`X9LEHo{<rFmri1yRs%LOs9Y=*FBo1ZG=d9S_-)
i5u^-X73C|TeX($t_nVQ9?dBfosoj6zBB`3L+||9MPDtJD|hn7%BKEldl)e7WJiW8PkKo|ZYWhh5-q&D6Zntx!R<XLR5#q3C6~}7y$?QsI@dG#zyErt(kD_%
7~}SB;i{_g6Y}0LomGE7&_E>9_$zLj6D0ASW+?KsX}ghi$_W63INrio-p5CZ>%B>EGHts&)Ju|u9W*<VHS~|nj_JbYn@ix>;7va^PfX@|BP`i2(Fft@x_Lb<
WefXv^=L>_T)I#fn<9IF%cSRsHXtKe1K+*1k~oMo?orG7EHHSEL2WC!rk?-ndsn`-!%5jOo7VL8I|or86{TS<Sj)&zOF)&4=LwNHIsFIsmu0pksrQnRyz0aQ
=c8&#zQ|oaG`zgh^^yC)0`5PN?8I|Qi`^iP&ipZam$N`XZcEZ3GcDUdD6PB)8!;Rl`mmR~B88gsm^h~idxn?Mlqb?%bSXLw)hE;Nt|<@CZ+|KTr%$fdY6BAE
1TY8-a#YY-;;#fulE#*dV*EMT1iZ`|Cb<n>Om+KjMacz|MA*RMG_B#q4%G31v_2rmfn(~qD$H9^HX*kySq=l~kQ}Hb1rU@<X+VgrEmvmv{ecIIzfa_u(^YNn
4m*0D`%4WQdxp>Q`AE=vOeap714G#Drf$~=VW8)sKMAX6#&50<vFlgn1o{J7zk+fA0;%Kt{Amw3_yAt_L~(g;8i=2aiOEXrZEH#LUvV+gb)yv~0<(dU`9|IH
=yqd1Z>AVu`P|g#+Mt7T8ObnEw>lw92!t>N0cfY%N`sXCa9kI75y<|B1DPM9%kG)6KnyiA>bN4uaKI~htK_}NN*#eSNd+;v2mcPwYx%Q4bs^N%p_vi;I-END
*SE)lWLmtLA@v*(eP*BR#Y{vKi18*K1GKNBN~7W5WP72(RN@Qq1*JJXAGau&<=qBn(}CcmmuRya%R0vSeQS@`Bk<ROpNs<UDFL1*Hezn5=u*K!^uv~rK9jHb
LNc4_DMaVOQly@|LP;VoW~81!bhAHv6c*@bPb9*2nE71r4od6fvp=Khl7)9!gVDa(pN#Ozb;KrIHq<FVBXYD1|6N59XZVOz1v8ZgwP3~osS+lEVW>S$TYJ>M
Og?4*WOX%7+$TOHPljCC&%a8$LE4^-HJslJa?9lS&R!&VV$1Zabr-_`4?NkLFmp~vMQU9Ao<6`UCupqmf*PA9nK_?7u7u6~C|6BU?j74-TAozjU49HiM7(l;
m$&KN4nz~KHD|0<Yj)g}zdWGGRR$n7ALi_C684n2dHGlvT~$eUglS^|V{y60-x3xfk4%?SbZvNeQ|}R+k#2HTe+H86AS^q?+At$_Ql6alp%LU;LPo5aXt#yg
RMe0!6UO`7)670~-epQ*^KBiQ{1Vl|0@-xD*?LVNf%rUv5jyuPM_Q$cIM8l9x{$DD3Z%z6Bu$EzRn&rFe%E~*^>0(?DaG|Vm3M=@ASN~bIvwSY8M5;6jR@l_
^BWLy@?j8}wi(8Gr$|AyR;`<Txm=~9Bf=c47mV9IBeT8xM_E&B#oZ1oYYxe}VLkAUx(VaRI*s!C`085~0y%vp9hr;H@g@?V6$;l;v)>n@^AB^SJ!P6#e1vP{
ZRC-Ze3&vP@~(@Y2R;EJ1(r_4MplSC=zn4a5CIYNAIoM{X$JXB>a}76PkJcr1Xf&U88p2bO&5%6h=hS%ivJ}omN7eo;6Xc^EHq-}@gTHBIRQ5v|MLI1kw=Yz
wl7<>d6T*^DBVeS$k~_jOE$eF_N9*Er_0n=)q$X+Or+?wR7)y}<rCi_Dd>!+cNH-<c`p!utb$WNjP;&b7zS2Vr+ID~7tf!?GDC*TK?pgyjSfR=RZsLmqB<lB
QNGt;C<0}cL&Ew10I6kgug!y{mk^vSGe8uJi)Mf!TiCt(36T~zC0m+N{Yrej{!Zrg<Gy~&?qM4&j;=7(JG<cZ`0Vx5glBbWUJsz=M6m7Jp96Zj0=pQ@(m!Os
;|EoejjUCJu95?qsg&2Z#^M|UTixEJxd$5{cPW&=+Qj#p)_R!|Eu`Sv<oc3X_LcY%>wb%(0;!IBw6$89h4e)j<dg0-LkdRLl0qSMTIk`kaZ_uMZEdMxgPU&b
FhlAG=;V4?O?#pN0t7$#7z~@|+w8V5n&t7sj)It7B{Krw6SEhB#fT+ay*e1(JfP3RbNx=(eRKek{2;sR$mbv4W+5<CZvr@-k4b#;zNzvOp$9Q2CU2{uzh-@#
G+k7hoRq4KFjKsgvEq|@iK0$vg#Sg70)_lu;033U9-6D`DQb*a9|+0acXIcla0@nKyI<>D96lov?cH8}`SgJd8YjoLjrZR+hTUsaR@d`M-(J|f(b7a740uI?
I8$u!IH?~dyoN%fWMYc93D`3YwG_2>D@$NYz*W`ENb)tdQ|Tlyi<{~u=}2LHvDH3fF-=)mhC@tgx`tDz7{Bk+rEaSSUY3G8TWY1}*4?4}9Ay!PIlAxSzI2@D
zrjRfH`BJGX$=I1UWcUVS?+7^32C`o9CXDVvt1>+KbbE?PLyVwX!{#+qxn+HEOt+^J8e#lGR253d-w9KOHKq3dNMEjNDK}Yt9C#@>wuxyD3X6S@G<t-)YMl&
7!=B`leym8aTy)53-9j)7QB-d)anU&AElSheDi$>6y_H}u2>b$!i%2A8|F3fmB{8r)$V)39T`}D5*{g_cvLb2Qll#DofM%b2WJ8cXnp9~Edss6q>i|S&!N7<
!=q*~s*)4^3S{ajlNXk17YMCbq^<$cU>47HN0?yFg7Fssv2@)c>w}8+&1JQ1j4`T1Ntf|T$Z!@=ZvGkRGuaV^KZEm=IRZacuw8f{CQRZp)RuYW>pNALu2R*(
Aq#36SQ)e1s8?{>y$jrk_gaOv6F5!{>`N|dR6TzQOnz`^KbK7ruYsN|>g0)*rEZj@jVH{tE9di)Yik&HV4Hxs0)0@It;4z6ziO_ng|ZD&TXadPYd<w)=lI$!
nU4;x0}uP{wW+-N!<`!D$P%0&3^NE%4D^MSCAGYdDu-qXM4G#@@i|Z+`scpBqu-m&?6@jbPTDfN0dfA-UWEg85w9~pU9S9;{IRG;#H%;gC-*-mP|?PTQ`e`~
07JC0D<xAPYh{TTZ}oD=tn!I|6-eohR^%i<Sh8(ID^OFVi(4~NZuvpABk<F%IPJ>sRyxH5F#D9x#Cn<l7B5>dPgL0JJcl3ozGHD0jfuUVoRAl>rnA{UOBk-+
n5`ngN<$Z8oY@@ZH;HCy%8>}Kuzr1M=3e!{@!~tN<X6OvRS_K61WhChH>>nh04o(F>e>w^%K#BV%gj+&Kzl=xNC}DA(*$Uy7**FQJ~u84Sn725^LS#qyyU-*
so1^w5Jr3^y=(JZ&8ontp(jkUO>#gI<<P^&!13eZTD+AIA}5(jF}%E$(VnlSArXo7(mUsg|DLW0jtjtBLb^_rRBU`JTElb<ca@+H0?3Ah1LoQ+%s4}3<q2bf
Xx*P>@((g!`O)j4Em|>Ouoc(>WXt4pizXf%r@BGrrr0S21E6f;O|n&K(t3vaLKyF1yR?<}l<CsOorZoV`5pt`IC&kija&<Q%YdR5qO-~hEd^v=@wLt4){S8N
0rb<D@bp<9A%t#vViu`Iy~F%0YJoCD3jX;^i$%c<e{}!PB|if3*W_Uhi>psQ8S{;V8=VRQP_7ZQW*eZI9@mSTa|)nLw)NgCO`lF@WKQW4kV_@_PCwGUmnDzG
c~HYIyDK5e6AOhf+grZ=c;EqkqG@rpkh0?(aB%sB7G_bmUM!j!(JG@{j48(`5Vqht!4ohbCbvAYYn~<xBoNUQqqxQ$l%+YiS^*;Y0UzAmi{==L%|Xw327;pW
NLP;ekgrK+RFk08ERQ}dkw-}RPRk!b)0ELyDAWHyo=yqH+==9tROZ-0mjE>_1fsIFG!&ayHnD!OSWIkhaLyRoN1^6S`RFa4Es2VC9Xg3Q>emB&BaQ`F_p1hl
@$DfoIU5$I9S{yueZIDhvwO@{O1@mw`>myH@E$XYz)Vd7whgEJEhWba*sqy2$r2uQJkI$pO8Tz70geGMMUbu0$YVC*PEr`FE5lzNb!qIv^gnEmp-Vvfw~1E<
qt0X_lH}k(%OjaN%ZL-U526=TxRWqgaOuYvBY~_V_g1TWkBG?!4sE;$Or>U@GdTEXT1gKMFcKuO*)DJx;D1ZJPUE({*I}zZ!GBKjLtUh~10MS1$M{9lB6Bcy
$9C(RL@{Q~MXiQZk`7qdBQ?Q}dU3ri3$08vTc2mRn3g(xc#$4W%Y_JIb{@8I@JcDM%?53xG)rTqa9w!8kgLMl+b8vg-N+ih4D0Nad5(0qESnnDc)Y$oo68yZ
N7Nx|pW$aP=>_z*M#S%k97J0+X?2~i<^*wBEqNxuk)Whg<e1_8?T+yDTEMV3uU12_Er9bU@-yDL01p|ugik1!H_R`B><Zy0qcFuhjc&(VNiM7?=W_+Wy(GuV
%^f~8E48MrhCBtM)LQah^-vBVVfce7cVHhqSm49!d-4HN-)=XO!_9_o4dj3!_QvnHA(yEuJq5x2?`#^&!`98h(c*pVIsq-R$)mdanXaRx^DJ;fp4#?4rD&q6
+L+{am&S<KcH=W*H^z`8((uIrMcivc0`4|S?>Y~U|5xpW(*)5(i<ZD;(3OwY!!BQ+%i;E6#8?zKP0Mh+O+_CK6J`hIlnI#SK;8_>&FQ{0lDIap4Zf4>jdG9d
#p6Oy2Dn*ah_7w64aZKN(qtSuJ`ck{hI`9vM8MgsOe5H7RE7~)K_fZgB(_-t6NsCP{j_9Gy8$#t-19fnRuS@<;mohHwP>>Bj%zd-r{t9z-K+i>Rlb7EBvd3X
U47vBy@6R=kfuZT)smeoq)0cmBBv~f(G~!lSW?sGtyHSW;AY;(b1$oPpp<nIjjh--`6@7}4CIOV=_i#<V9c4KE}{c5$zz1iFpS-2F85I==y3*zsZqo_+d{ky
0$%j_if&fiJJvW41?rzrNpdQ2wghLRE!Jf~GUb847Tx=%4{t;{F~fE*gFJL+&zcE`$0NdVob4bv9eTo3Tsa%u7B$R(;MI|l2uh$lNd-!H0DMQ-I<UvW#;mW@
Q3^esX9;sH`X2ls#xU_P@AUkATIxB?qe94gqfxg$NfXZq{{$v=$!=u~#*CV-u4>J}=N!Vk!SGiO4)evHo8_r}7yCP&qD(wj{%&h=h@CVDT7X?*x~ja!K@)0L
E|6AkqMnBNSp^wpD|noB3Rds?oKwwgYqY^7XncrX<kk)$6@pXMn1Jscny1A?k;Nl%!f6=B><eF;=HxpK{%>+iF;>6qQv#bdACWS!1E;!u?GFzd7^tY3jLmYC
bvQ5J3|CmC+rnm|sYn86)BkBghIhLpl=FOsN=kgPYYJjDp}NseE!^SnrkaUv0$DywYz&u^hCjuMn7SFlTQCnYAdhW9{(m>8|6d>mtnCC(T0i{Tcv>5Qf9V<}
S0T)?*@{U!@X7Oh%#fsN^JA%e$W=i57nMt<Hlc!}L2Qslc?SN=j*>GOYS>NhSM7dMkpJf`aRbweNJ8~KTafD8QJ2Tkftepm&2eo<GKY!XA#L&3^rWGFvdP25
hGZ!g&xN8czVLMvj$zj_#LP<vtYSu>-M*^LO+(k&1)^-LX)}0+>c0XM3OWlF%|i#KIg42OJWV!GjDh|gu_~Fx1F-_Wz!A@OqgO-J-vygRr1NwJEZ~?-D1qVq
7r-lvtP&!?Won#ND^qB(&@QvUKm^)66)1ikV;gSSPu}W!aM(*RS&_ulSAnD1i)PE%Cf-Twy`b6<LE(*blk=GrtW-m((6Tmq!kO_Ck+HE5es&pyCVrt};zC5=
*`?|?m$s{)oh<CpRBDD?RNT0uF;*e3ALEd=zr4|&%dP`~T}uHbuX@o0JEuHkK}+0LFN)pXJn`0SCn-sV3_%^Knm|2-_+pea7V!5$WA%t=L*E*WjTN$TSrZ2I
HY|St6@?DkmD<t~F9=Pbd}OeOsRpAD`PWKseMVT2&@(W;nM_idk^pZ#L518jM7JkaqZ)6b1yFC{1bD3NyQ<`Vy~sTAEb!H?vhS(0k}a0(V(M1DY$mdbcrs4P
krVR{_pJ-YaIwj985di6tLn+ODnLZ4jQyFK4#T1J(c7<ZEtuD~Q+d4`Z&lMnJHDte1aH6<2eW0q<KsuNnTYWH0~bQy)(c9mS8$2G+E?}Tx3?YgDKsnVRsEn*
<hH=}WyH&}Jvh-U#1r%7`{?N5+_3}gj?=4Xs%L~)D&i*n(}a>(He>m)8BVk{%*H%|c=e8M{?v2t*&saOo@*;xk<|0}9Gac2-BKg5+3l_3eHc>{+Yl$Ztd_R<
Ygn9PT3LZ>dzJrYg_LioJHmQf?;`xPIraAh@aqq^C6m%Pe6!|`R*b|gcH9*3+!TaD0bPG^xsA{<bW<tx^Atm(o3qQd>S3)|9m5wl?rAK|{k8_nf1!2Ed-0bS
POuu$aoH;m+Mj>us1irzL<DxUl;iP90I=9?l!ZEUP>HSjf`}Jq;*5xOQj6k=y3wE(VFMZFd|n7|9CEbdOaf%ySlG5XzO%gm8Ww@?xK^AwJVEaupGT-Fpcd&n
?8|4j{l3~lMNfR8luCt$%bPQYbJCEwG}oU2v_u%fuT0;>QIGw(e%pnC$48$7Y>YQ!;hk_q-lYrFZM-GmS-Vk?P_go(3;4-ncMbgHMU;_qm5wgvB0va$mP~a{
K`pntMl_|?vI)R`_YT{}jN{|paQwd`Jg_VX_DSfkM#jukKu+ro-&Ou&{)pj6a4lcxM3BDk9seY`Y{nnEinn>Wa7&qV9HkL-0fJTEvHQ!X5!I4I8=qyBvNb#y
j+qu~vW)f^mOuAqIL9A26RLkcMyA#{2RJn84|@HnDZDyuWAuYX-nMETB68c+e-tMzs7grwJXQl-2z-yO7C?W!EO<;sLcaZ_hc1D|As3no0U(HHVHc6u7Mcox
+w=hik~RcpuzDy2%F9~drK`B*Ij+#W-SFSWo%d6B^J_~50_LcP4lSAFJA7LUvICd3Q{=e_=Kl!MacnfI`12Z1jiZ|>-~lq1y&!8IQz=4`=%4f&ub%ymebDo!
8l5;Ua+Q5n@v+eQxpU<PW*vG}K{+?;xXyOnCjo8Kq>@l_EVLA#nG(-l8I><ZaF1wn@)x)6wvB73mJ^2K>+VO4gPq52@we$2B=gEFQ2unO+a(WKo*d&C0fb-=
9gd)nqLk1#hx(%@%|nu7`viDY)l<ZoHN#uiJh%MWHcyQv<}{sJosr3HbtfZ=s=#p8HzRy%q>buXS_$t(aTxau+gK?(lBjk@UNWs$yB5ZjX%+!GnC|RPwzY3|
MOIHE6xk#<^tU6Cf3K3u*cn!su>eQ<eeh*f%1<9C>B8}u=n*Tl;yXp0@hc4Id3H7lf*#R`WQ|XtY0Ilgz}qm*_o#m`9oYit%2CQDxuhyv28UMJuK<CxN@7b_
R<xY0D6}^}_{RAr>N@VTs2<|DRBp6#DapX{_y6~%V1Hs3ak?v-<x$%Hp&q=5bF7g$ZHU5(s>A*N)M$?U(-TY_(JQ#Jm|DZ`m;jV3IwlC6yhd|}S6QkB?WAS&
qEjOcJ<lM7*_pq-bT-pqMtCgx6Zj8v9;5FCAtpD~BXD@_dt*7y1^7|SB6`3!_Q@t70RUF<Bl6?M1J#B6q`00>3S_zDAk`*k=t9<M-a&Vl+yznm=(BLNcT(9D
ZmYb(BwGNQbb;52e)Q*{v=j5iL>G?nOA=K%RGdrEL#^UU#ua%zalK^{bKWUxf9NR>^Wt8lL>m}zLGsPP0s_c0`{WbW;j0ikViNQMr#zPiGpjv3qO%fq1!9w~
8{bKq%uLc%G6iUo*yjLst%Wh-3Ieb4-F@iC*bd&%b1o+sjck(~q(8I}$B!fP;|K{|jK&ftyYJ?+-FQ@2`6@2=05U*H(FZ=nkfjV5Ug9x=9qQPv-Q*bNvOA@j
*PyOHf>2WY^NWbpn?<cKrha%v`PSA_`eZ?5Dnvv$AW`{@K3wL_V&l5os{BIxF$zLcEMoaC>IzDz0RjF9T(=tbL@qe??4@`T1q;2oGxMt|9@X7Ozt-HLMfH0=
@Ibpk8sV^jQ~pjKgk{aBA;h0TJ%Ldcvs_w>ydA^T9qZ6?*VkWHly&Zb10)JuC!`;|B`IfOxGkb+S~3c@5wxO4t23%|pZqCgbE(UMWqOI$`msHdP*6<FQ>}?9
KV}*;*SRA|U`qOD<G$XDdDh$pHfz87Qo@!IjAA0Jf)j))=oMfc6kjqKIL07`@Y%+QNMCwUzG+~}k-?Lrr!~vy&rEZEU?X_?emTN+tSxOtPo~50uF=e$*3|X^
kesg}HTsm|&&kQo=!r{Nhrb&ARt=JUi<D;r=!|{r_oW4FawAj(K~OLFO`?tqN}76Fos=x?|3uY3wG~Ef2HjxB%?ZEBNBfQw)*Bay7>uP|!z4@o_uMJg1UCnf
;+zBGFf(*4Fwka@n}lRL$55tj*D!qaX|c~#E04Ny<WW2UBk+@~cPol$bC1}1rqyI;z>UBEPdY2CKIXf!HtKm5msn9-oGyMK;XBq&8_O_-H?;oTi_MHobmaP_
f`FW&yHV0w{YPB)FrqJ9>S!P9GnjSVLa@O`p9U9*q>(cl%x4LS=yV0l(=WS)L$J7bn3{t+j+DEOUBB#PAAnVm49fSWPB+xNjaWY$nJe1&o3US~9|TQK8zgGm
TN<N9!zR8xnBV^-DCMrt-^`#!NjyA%Eu*`>`tsK0-dW!=0n4*;zJwQT8+Qd>W^G=DV!rFifi&N>z2S&|?hgE7II@M?pcJ%2*&n@mt!D}Fd8hU6g`d*u-lLbI
CgSXu3A#&TtWZ<3rtFTsp#E8DD(i;-z=taA-s8-WoFl->Yu`&e?i2+1NaQ8iU>>r__OWzT0eol$1y4r{T+YRNrwlX44kINf6<hH8owZh2p#0gKWCM+>f#^)D
XUFTUu6(H$Am5{QLPW&9TzriALbTV@v0Y(f9zpE)e}c(8EJ%G1KkB_A^Pc(O=>_xg@N<@YN^|7`9%Y>LYIyIjBtq#i;Z{GTZ~TAA%(XK0wma#+5s=rPUzk2o
BoMPcsLrX)NMr*74Hz~q43}%p5|Xi^1+X^_hA1iGI32Oo?gvb*=#L~A9I$8mV_n!<e;D=P|J~a8S<bn7hviNa(5b^uo{BD|Ac@iob^o2aO-Eq_V}&v!<|%t;
I>OpgOifIDYxn22SLMUjEEk3QpVT&(63qDEtKF2i+A5a4s;{zy!4zRa1CeZAIti23y0avj9jIFQWgplca~A-T%eUjTPJ7a1Ch}h&-{5C^x=&x(e04+dbZX<$
-J4ZoEDMGzzMn%3FBia=Y7V^I;Z`D}ou#?+!mRL8<^i7J(d|oDfFqHn_;9unV&&`4j~WvI4ZlEsdRaWjOMEU~k%!IX>U;6Qx6|~0<r-(<iycQ~_+uMLODrTt
rfA(i4g41xu(qc@%cXUk@RN|g2bi#z(XfMP@_1F&D`ud;6Ri=3<^A_><}_GZKeJsSWun$J_&Pa#z`}x=@h1B7a)QFex7(>D=)L>n!o{5})Tx@Q(_MuB>x%kj
lKBe%#xx;KN7>5q#Tt!@Va+X7b-iYhRbX0a|HO<JI%R@hH0lU$<?s6p9JRr8l9Q4omkE3aXr8++zFI%weAsIfiN1(+D~2z?!s#dL>dN%7YAr@f%VS*3X%9J6
u!!Fjj;Halv2027G>$D2n3<FrcgFxge`J2WP7v&THOxXOymxp%O$7WjcG#X6(9Kg#^n1+6l=R8;076PXy?ecG2_MSVdjYt9dYFDYfR>~Q6}79?QX(D@b$FyO
%Q(ySqm3eVC5U}Rw$wXAK1Xk<-31$YCTq7upC4<5a1RN9p2jyIL{YLVf~pS<i2B7l7Ywj9x_v+v>(@JS=V35*!magmx6ryJhSa2B^<OV|_iEVjso;JDGXz;c
BgweR-^sZ-O7DFEQ)5g588(~MuN)ojHjwcz4HQ^GyC!1t<y7e{;OagPK8LDejsVpqF9$Mdp<>3;4+3mF@ly<Y(=zp%1^CSBRF`t2V3looE`Rj{Qj$lJXH#Zu
?z*oz<PG8od#-?Ydf1M18;8`C@2>S3?W(=Dn93{d;;<oxQO$}DosX7fq(R%4>o^O(rGQ{oW`T#lj@rhs5u4)-krHfakp)xGljSpOy)I_kH8q+z&=*g%iy&!p
W)cdSLz3<*w3$;Q!?3!EN>gT2O8MCA6Sb&ora6XjDJRmiFiYNeDST2^z};N(7yK>!EZZj#2m3gny5Xx}Pi`G!QLjYDk<VEj$!bpGuh3gH%F%5kC7-mi^1`GC
-}>arkyzXq;6*gK=M2mq)0|5?r!wYGt5mI@;{J9L<wT&A@#iO=e|*NIW|pg<txwq&0QPuROQwEDPH_aJoKOM9*@@skY|s8~-*=}2Sx`U+xPXCy8)W5$yvw_-
@tE54vtS2t|LGs7*rQ6aqnY<+5;{#*W*=aAk&EZLls8?IVJVL$H(S%&A2|HBs)Tw93|uVY(=sKTy@a*~suU8;Mv+B2ZpY4R@c1g3Q229|V7}k@ecJs&Qpb&_
ul3IDkgHq2WE@<vQ1}=i=oRu^sn^)uMo@hBSZ;#Sx9#b_>DeZh4mt>gi%UkyQgcTfSE!n97q(=J<_(G1+1`fDFc%d{`j}e6#G1fIU3Ykz0R)+dJjPGGV~4fi
oNMU+QOuWM-m+{~h(Xay*w}K7_>QTj>D|zilFVirC~apS0Q1I|%HRc*L^OC3%n?JFp*aB!6Qzi20rSYh^m9)27jRRF{2<q+S4yj<8PsOlY1fD8?$AU!yaO|`
<0m<{r0XSS2eWI-6K!v&g~g2@1z%#v=F~KlbhkD^m@<{is)8D5Nnm6y{muRXQV{=4jp1js#ZG8lc^Ym<m6r&H4vEb(j`5d6?|wuMRV>m>u9`opFHxHas`nNv
FnriR>khW`@aUD_B;QE*yr|J~Ou;wO%)QGH)^ldKc4?iRXA-Vq?>~f%XvgnrRA|yB3z{oaf_uzN__&L1s?H3>i3V?NoO(mPPKWWyUaR{0$9F`6^eXa16s-31
>%JjT0h~beqI7FPkr7sfehdPsd2BeJB}YMd7n&9mHGk;LO|K+M;bf2Z0ZG3!I#-0~GeX&W1PTevvGNo+{W{;ke?`8ONV<%b&3uV_5i`y0=%!@-mxqk1C!URH
ek#&G3CMDY6$KKvQj|p)tqRONbp=2RAS?^vVwMna;;)Lv;7WcpbK#Io5r6WFiu_zX>;YlcJpv;$Ff~Ti540*HA1X$}SD46-6U-qkj^qfKBuW%MpEw>5o&r0-
EsV=vq&uUY_yL#xGts+hGwmcuPi<lhUf_mTZH8oG$eM2ai@V?BujEi0tl{j|nR>`tSLXr|$DT^c0n|^BFz(S=c4pZ%V)MpS_jt|G)jsIEyq1u^AbY@S8Jo~l
^3bB-W8<JAhC1}Fx1^yKiI?fos%XGMZih!$<Wka~bEL36g1hVzJ$$aHx|+625FhC3B%sFl07G~6Z>}Bg)zez9uCbL5qLZ<HyG8s1$#)`{#BiALI2f1{x?3oA
BH2t!U7X~K6#&oB5H^cG1W!1vZm#6`nigbsF8vAN;D0Y6I#4NdP0ZiRw@@!i>!?{-^FRTI^L&d0C+`4XG3g*a?DCPdoAW)Js6*}O+nXt2Q^sFk2RI!R5Z+WO
w92GveH<{DRH|O(pCr7C4_zppt7xdxDyK84lo^cUZ2?9N6^3Is#jB;`5sIGnPJu+0f8B4J`cSY{pJ+QS{0t}ljERu%y5$SSD)m1Ln8otq#v;vhJfl`S>H|@L
`jb+SBS&a2r!`6yYB&{7<;ln1uV!;<ps;%3eVz4^<yrpZz58S1SbAa>EO>1X<^3zZ>v)XMFW0)u>OAmXx~zGV@?4f&TtheKcX^tU+Y_f?I(I(B3to(VrBXE_
eT0kA4^~7aK2HPT>91qek*Xu`YI-4I5be^OJ^MeJWh+YY#!}UUq?^I{wDYMnuH$kTN@K4HwVBwrkB*%xh00GF=>5Yj?V561hxFvhetJyeQro@;&;wSvn(o#q
c;DKAvv4q1O%s5mTAVX1UV#Iv=Yp~A#3FfCIhGLpEf5{6ygA&`*^&sl0$RJ(n?V&^K&VwU<*_mKDH+6~2(SrD^Ja5)gaesA$Jv#eK;LS(9e%~`{xgKj$J~0q
AIM#RCdq_yHxYvh<&*Yr=+>$ouPoQakZlHQ!zTFS=V*eI!x=YB^0C-X>^W!opVZnHul9aHe+1Gk<D1WY2^pY4FI@^LHx@6gG6;3idfy}Y#!vPlLh%aQ0c6D5
SW%x<2lZW?513iT{l_%H6sLtMl&HUm!C6~(5q4CK?#siWXR5Lwmmwd6GXa7GXAG<D2UMBc8_g^=IEiRyfb!Kogzm(b-Idkg0mPrWmO@$;>sxrpcSwiZgOcQN
3YYrgx`O!LrVY)Tk2R+>2``GnsERudR;xVExNb(Gy3imV4M$WNKHuPW9Q(2Uaz~y=5s0T)qDC8#5wM<!BanHdn1f*b*1!u=_9w=`SiH!yfEvf(i7sNRYA46I
cIkYI5Wv=)cML2AcKo^uM8<M}y#03=Otd2A9bnHV{Yv&oA@r4ISeY<ZCytAG{0Ip08|+yYUHBWy_WQ(N9bP;}?Oq}YcNmPvnt{9w*T3*NM#tJCgnegD0#rI-
lqiO4NinF@n~ht?k1Ryzq$h)`vJXDNB5|wxckaHWgTzo<7zg9Y<?*g7ZBEWL0?O`FR`6po>sWL@;hT#uIk&5fn-5GUzXLlNT<Y`qoWzB$g+h(*si<L-v4j_^
3@>nF<1=*05L;3)vn<*VTo7ZcMeQ+8*0Qy@OpOi%EtNy?OZKyQJoj^F7=|p-WfFVXeD_(ye<SJ^{>~4tueJ<e7cMZ^^h|pMU8WxmC64koVD;WOa5=wHh0V~C
eMDJmT2myL`<r=+3?FY&y%S)ua2csZ=VmTx<Ou<)X71yDsD6$qDn!=4=}jBbbW?MDpQ$mw=Trg+&3y=%WnuN*a%%^#AaUL<YTk;1`ypP!cT=r8A?8~n1&VV?
n}1Mh_&wlbtqzDWT@x{=gPICy9gYYsPL^)%F#(x~2p<^KKFccV_%cX)>q8C}#(fn(UrDTHtRtWW;S29e{n>!rmK0LE>?JB(VbG*G<_=PcopayH?5J)}c=ZcW
ahR$jRa#-C=-0%f0j(yH*{v#LHpC;=@zy1naZNWM47Cs;VXG!r>fxs(mOcUlq|^7<Yv_F?uX=Y_S#wZ+v8)8Zv)%PVmGG$mDQjkYan0@_fsnPP!PNA)?ECYV
{G!2#*C^UDM*Wy@V%q6V(wsux@R3HjZsv3mxbhA=>^!tr2RPB0O<dZV1oo9QZU?<>(s~A;Ld@b`YYlE|4U793m~PH91e)fSTI7Fs@9lKaRaWl)5hVrwjWnRl
dp@a)cwBKZB_u-uSyAdDf0iKi#O2uax0=P!MB>Yr5-s`A`E$_~nX^YMU)^=p>v}_|P|=yuCs@O{at^{#`^(xgo-`hHvLhoS=V<>!OShX?gv?T!;MKF@Zllm#
Z|a_N%pFXQI}WVPt+PH^W?Novhct*N*ONg6RxU4k{{Jdy3FISGtwih1ki2R6|5y{b02={Ct;~_YY#k&s*zcTV9Ba>2A6xZ)oSV+f?*G0^dL`?@ucyB|H)sZe
T{5>-SEAxm@f|!D?3fS?Q+QmOq0Klr1O57<!{d^d={ZR8d$Xc>(n)NWjuwT4T02_U{}|qHtfta%ho(p4ePcowIF<Pqk;8`AFltq63%Vbb_<xYjYP}N!BOB1`
8PVz(BeX4XAZAwBfqG#_6n1;;i6A|Nf|ZwfJH)-GN;l<;LeIGWW<BX|elfc;llLdY-wZnHjTW1_?A;Zq&iP_*jnO$*AbkG)fmmSPGax7S?%59oQliFNO^p9u
lo_Zzg8u=~#i@XlF(5?K?!TulQkX$D|6sd=)2>a#g&Z)c;T<KedV2fwQU3NQkFI@}0T|4PA_&|Rik6<n{!#<Lf>*c0zQ;2N|AWb@%kZpH401Y{iEY@^7~UME
CBARBJmKj%Y&T|j&mx6yJw1|ExK8HAvx1zAJt(zgNUMW|e=H%AHs=Qio|y+Xul&j1$QB)xgM*Cs(~4B7PCE8kOJaQ+@?Cvui9hDt9;Y-?Tf2b!k#vS`mi=^*
PJ&QY0|R9lmLe##>Dy9fTVNVdf*u|}AHYn7ZM67H%FC~`^yz;)Ou-ORMl>*S@xchm!E(Yj??6QAI+=_~V`}UyYbqfGhz3TTMA8X|??)1SVsyGTDMVm<<#?%1
u*q>SMt$*ZrHGJ_x|m*!6zz8v_C7$hd(SV9xN)=jrt%e|ig(M|nu?9t1WiG-W~A8;`lUcKSjv>&j49IW6pY!GR3z5_)S8ZqYOoHHL0`g49L%$ShZm1f9AOni
PsP9VCopa~ThK<aEnR#~lD+uVl9|~PCo1R(U-j|$?kUVK9TZ!+m!h#7d$uDMke#=|i9LqceXOP=JPKntb<TcaxxZ)Lg%P`}2#FR!Ddc=!##OF=iJTe_qEe@?
;`6(a+=c4+iwG`xoV~0HxWO6BwTnh2wyp-(f>N}<spX{zK;Rqh6-11HY^d{Rf1$S^JK86Di)~?_xAh*NdC7tcNXn)zIV}N&Sx3UR^Dlob;$pdG>F05%@k<__
r|UWt|M668WHIGS-wcah1ala1B(ul>bC!=MMG##Pgaf(orRYWJ0W|LDaZ(xYWRdfdWVemi5<PUV!CpR*j#mo5ulxtW6}4kHgU7&f<_>A1rp}V{MWz<=2ainn
O}mn>@n(Yjmf~4X62ix_P=(x5>qY9S)km$&PQzuzOn9IlcKF>tM<BNv+JP>ct}U@lj}6?wOg7gqTBXP-k}BY6i)?bKZiH_57-07@PeROM*0G&Mxq)hX7<)D)
jnV>Vg;6Yj4}G4e8>)<SBC(eA*l3(JsV&=$Ne^EKEB3HW%x~xwy5d}aHc`zg3i)c--BxazFlry<qNu$J7f-bYe|0q<!4ub8<G$G>q~M!o90Q)-VXw;QPzN`c
vm?JH5ykUh-zG#r>!5+}7aaK~^uG~j`yukL^3BaA052pUh0kxJATK5w$$Gx_S)$2~vK9o_Eg^Q!<~aWNeuHRt#2BkG;Z%q#Xn0CZHNE@XyUZplisQ<a&q3#;
@YfMFx-WJ?0UBBZg5-OtQBRCtWWooin~;{XyJe~NKyilbFl3P+4&YpoOAY;3UEKoJbU@81eEv^sG6qXi(3{yPILZj$UKB)S7O*@yT^Q6&qh#E)tqh<_Q`prv
ZGKVdS}XJSY8qQ|JsBshsXm4d+rP8-8ia$k{Wlpbxv0)24AnS~2U8(?kubo~AlFiefHV~Ql9!3WgAmyHIoDxbVVfdtU?y+jIFXn~j-LLN%>|{6V<D`^VE-&Q
r4ns47pcEEyu^1rtZz+#yree+IVAe?zK<nOJBvbgH{F;f*y=KcA4|20gR;0&lzdr>@51XqVL4UK-ATRlfnN|QL_%9qj;sY^5?4nL+Qq4PrEoQo<cDez;t_~G
bJ|9d5ul9icqT?O1N62jV-8%f)RS>}C0bU~`)$X<e!*kpyc5l85wy3P`>X9B0DEsA&H=Zz|HyxWo?*TNkqRKgstG{denHtoq6lj&n*5iGQk%?=udYW~U1YZb
J<giYUcz@wy7Rx}c2NZFdH*EwQ7!yiFx|3EZP(T~i>9aU{%+r<sjUn=8Z3qXWGEc+pDI~mCaj9zM3As(LA_sdh4RfrmiD}cuSda%v*9<sB!8RPl1epxKUJAf
Y7V^OFql*c2W}jcY+BFo0aRwCfr<J1t?U}*LglHc=DJiTk1{lzV~IeAc<SR4xzO!!6*_;A$Nqw=3wLjMKEHbhh08MuTLnVdMX62s;imM$<d^ooj~Vf>VrR|~
c3vg5C#TVC<bH$?{GLrop*)L3r8ci4uMF{?_(A>|)2JgG`GMm8J_5Z_Y_N;&q!Y5kDv-5K7(89uQY(@Fj5bd+_n;XT7#Fo8hG{R`r`Ll6^oQj1j*=!)A$Rk@
e50-l5Fy)S{anCxIRAL*8ZKfpU9u=5XV_6_mjXQ+$B{7l^svf4qbsWTn}4s;x(sv)yPR>Ag<A)kC5jOqiW0qR&L@bEW-9-NN76J6hGvfPc>%eIJ%7%MZ#rpy
=IQ3&8%3kME{20spRqD&%)vsxEGgewg3AJEg18xK!o>#{Dk<lq7l17pxu*Sym1}7Sj7s278?Tb2EvftFiN{UF9hS%48Dnn^Ox(%J`v$Z)lzN^P781Aq3s1ER
K~OO|MC}1E!PRx!gW{w+`xgVVa5^kX%SHS1gLuDxYp$16#(#!Gw0-1bMx1@g(NVpi%t|t7KL*>&<$b)w#+cr{&PFF9Vd0`mO&y@XsTAff7J4R*3X+o7Z2nUG
!4?f=HOJ<2H{Rd5f*MnrSa!495kyU_MwNHft@A%b@zf5zCHT@`3`@zbg4;O3Z(BV5`!_(a!T=#OMJI)Lsp=3>Y})GGiBmZpdgN^8)`;zNvezfsN5%;E=~B{P
ZL{9mcsCZ;A~PiH9DXMaeZXKGng}LVa0u}GIs-^iIR4`hR)|azet&Qf1fJ|}$f99Q%$QtOP^%rW0dl&Z6MaIdsav%VjJds!oVM+vcO}T=<*qf-kzI5qt3)Ac
j6LhTE79vR)3*S4vd4mbLU2pvE?Ys}+IhC6pdbPsfgbiV&U!5R%$0El%`p1^M1akV?wt^RA-BfRB+Ks6PY};A`Z#M?71k!Jp>xWhc*wTv420SkL($p?J&z#o
fJ8_98n&^E=C=%M<P+=!M|Sr+cVe64kKtf=Q>GuLcnQWXsm25qj@72LEq_3`R(owDh?pA3r2|ca7U~5AbY{Q%I~Q4IsvREJ)z{Bi!CVQLm%wU?Oni2)mAL$y
Tt)6kE<$OeL5Lmd2E<=w?;B!Os|s}EuB>SmIDg>^BDcI0Ok!FhMQ}=#oVBb~@d}jFBG@tO|B1c?b9I;_Yf`%rOOs;&&fAMA%dh!49k*o1G3Ii1#wScr$o#qd
bts-0j0!`h%aNwZ0}OUh*4$N<Y64HXh(BTl>yV(W3>r769x?^J@~`msa@W_OzAL!R9>b$C)J+D)X{sLI!aY$NGl=FhUPVGRKAbZy$8f#KPld=HEmKkt1&&Zm
zhLC*U>=yH2L=D7Ei4|jdq7&&J%g1`KxdOdug~Pe%y%)3vB%|>h_0yoHUqkZ+}D^SV1otE@?H3{uDy{GHYkNWZP5wo&9JJEtedt(CuCpw$l0pr5*XpSECLf=
pTq|@OQMnVs?p)64=e}~I0w1nb_~DwAkq|m02@5&eex4^u8moN3|Mz{Q1Q*c*v~ZA>XhMG5@OBWSl%KtGKa%w&9$kT#0FOX4f+_?L%$kp=kk~Cau&QGIW~nU
w{ISzeL3*O_s!ruPxy3I8kvp1{wIBX{;^tgaDF?4oUK{fn7i3&NBJNET}ppKtrNHE^V?uJ^RzjFDcFNIDh$=i@+6ME9{lIZo2AFgxDXk0SX+I?<9bo*>+r5x
5h_3De`by;2u2xt{hHo4RyrqC#l?#VKQXK&7lVw*9*{mF@a3B?z%hulZoDbQFDA(&*A4cn46<j~9M@aMY?g-le(l5uu@c_=uGB(@<s12;OT$4IDtp#J-^jZ#
nvZ6?(|0CCVoG}hGJG)k2R3UhR6oJ#oD+3!tc`<G)Gm|c(-pHP812EO!N+tRf@NWpxzWY`D3=MAVm%Z49Zyj+>)W}kV@m%fZQG&)w!Dp~Nd<qu=t0V#^Rgmz
OJrJpG~Y%c71B|>yd5@=v(h3osag86f@wm)_Ee<zK(1}8(OJzV7ZFuf0s-NDLO|I6!$k%zm5ZC*{B1f_Ps*q-LZ?(pV-*4a^-Z(iqC<=a!BTE8F1*Y5n6|}-
$ulb*`RSo;@ez8mUs7xM6ee{hBYgK95`t}A+e)!mTIXy24lzWoRpHwoL@h=Y;FvSTrc$N*hrxw}J_W1{uhL{<x^g4jWqX3NjCoKaRH|u_eA?_SI;eJ5+ajm)
NqfDEW=0yi@1xynFK_!u!cpazT<h1e^v8b4>(`)q`$l(q5?PE5=*Xvw#_$Yd;W_dNO!(9X#FRJG=Ozf(;7vv+0!Flf-SZv>2l-=u_}*bazlQ~idfY!a(mBxV
Y}&IBSJ|3Fv3gKd4v7memS8gl1eZ^MR+U8k<f{o2dVMI!u-vsAC9+iHUb<jFPPtkWAsA7|B4*?o;4caFJ@&54Cak<G36RsJ5lGOcn;x@BQ>eb7gNQ}x-kmRx
jkx30!T2U~=>%*Jo{>ErnCob#+Aj_mYjbdQBD`I?eOJH7#~4BLW>8*Kmf>w?RGT<JE7&nhJ;Aw^NB^`-nTf|lgS_qbrguKHekN^Ta!h9dDj02ZHy)9OeKHWv
{&aG4h2TF!)h5~7(rCcBj^;f>OjfzIPXX>XDtz?Wp3aTtv3*P=C<ISONj8!`+EeRK$9}i09Yuz%sF*DnV!9*8!_<iQK7`5=crBu`+X6%BBnG7P5%sTCG7~5=
*s&*R27?8(q79oCxr9v-;TZpm#L2#gvBegdbYY+|S7Je=!89DquTqJPEM0``LCs(NTET`judLyiw7R>978ejk6bf=MTO8mXHkel*&jEy~Q)Xg`woV&RuI&3u
xY1?;)Xnb`z&`iN$WJCa?kH)~o&83@o*Lj|CV3vwoMTJLwIp4ss5ycD5mITb%o_Mq3;fC>nQ7aj^Lh%2@INFSf;1bMQrgN)<h_B*5lhE_!EoSdx%`-%X~mqj
Y<JYeDW0QvS+)JqCut7!a$q6RwGQMJAF7Nknsd1|yE&GBg35hOMf_heiZ-%)5-1MMb9<yYk5g*=vZTJN>qbQE6Q-GzWViguTK0LhlKd!)uqgkA@|vW8Jfy;!
k_T&2yyW;u^YF9$vRg;UUEaHECa6vZ6iGbs23iM}gyBVZj)Qu*Bys^v8!O7f*j8zeUW&Wu5GEDTq0&$F$&_iGqUH^YdJkpQo#TCK@Yx^}556K1*W8_oC#Bit
5J;`*3-ivKCDANbxLX)0M?f!D{`g0<(4-I~MrmkLo?eZG#Mk~Eybmstl87(stx>lHvQK9(Zh53qY%cp;0D%g>-8MN?9f`DhrasU~<BDz;8ugZ%VJqlBe2nU!
_ld@2?P|D^Obm+INANj`s6ScOXFI=dAfbxoaASWFWl=KTu%%42v1Gio#LYL7=hzRa!S!={YGe5dIz3Px!r$yTm^|H|QGYOq!c1c!OQxN$y~V=dAb$nxz^9(9
BBT)`$%@|m%x#$%+a47Uj0F@&&X7C)8ULQhQ+1hVQ|4G(W$hMB{Hgr646lI0`>ETaK4()F!^hhI34H*-EKdWvQe|gDf+sjI|Df?oCDh`kvLgIaHH77EV7Y{)
!X;tgZCDTncBe13%w3^tsKPg;QTk)-9IhBXZNLoIA!RL)tdg;BlnMj6Ecb{NEDL;%XL%;B31ZwZwwzonhlAybR6!gZr^)V1VK2_RW$585d%U{REbbPk^t;Ln
2cWGlul%xHvY}gxfxsv_)=!%pkt_SO+!Id~{KA?bP;4m+T{`PDPtucjhPMqYPJ28fZ^coLM8{FH)DX-Hu-6G;Port9N&;J+U|5hSzV>2-hXUEJ({`i*4TIxl
tF8IY2p9ED@pb_~{zQt6mLc!v!bZ5~K6W@P=QW(VmB}vORbJ@c8yda{jWMf+0tx)#Myc#Vb?_~o4tybN@FXB5qGDcjuZlAJ_DFV#%$ww+E5IoE-(DmF=x|hb
+niWKr~gg9p+z#&p=}pS5fF4e*DoTI43Axg>$O0EZ{%@Z+Y%RO!-4V)Hvq`d8i<QOaRd|lvF&a(0+*HG6MuQL@w(t3u^P6bk+E_kHOo~wqS@_0eo0Oi8lX-@
U;m{_EZE2nwpG<#LwlU$%f&Dbt?>DeQwRmX#Fvm(0QP|AsCV!r<z*0a;4Ig&CLF<>8tyGUqu-ax53@B%tgN&NcENwL%b>TugtKXi6rWlvIe1qg6!_ka#IhfL
$KeX1<-tV)(yaV~0h#R$=}S%)SZcrq*QnofztG`IsM7@Y`j)HLPtyqg7au*<(yyS2FIfptB<N3&A8x@Vud(IE-}_|FZ?F?ui(L9QviIjDm*Z6+loMtx&aj2=
w8I$PJkI4py-T=nyT_;%OgqHuZZ-<<;5jgkb@K}erMs|75%Y%6b=KV7<b>M4IlD?tH}HU9Y>*ac1kp}dvk_|{f6HksE<z6|s2B8VhI|^yZ-nfBO8RRSE*~@k
A{}f5o=~8eC~O&X#Qp&Yu%O2}f)+(DlO~tY5@U@|Sqo<8#`%9cDvR@J4g}FR_4LOspQ^TK{M+Goz5;QJ>d&<0671%e47uT}%DAcA$>9m#+wsA)xu10Z8^$q}
JN~(=TfR})!_fO!;_O6EE)z-UHfeD8jK#D@uMm{!O3BZyML+yt`(hWBCWh+f3?4UkC13-aXH%-;Q+tDa?P18vboM;0ekl6xYEmzCy*M4&58RXAvI2{L_}mvU
ZXypFs*iDnr){(_i|_#ShWvdu2o>!hN~%w_*pr4?&9;N>KKLq<_&3ldK0YE)+(2QSD|ygji21fxNgq#3W#EV-v-CtY=judnSSHgE^R#e>Pt-abklP{939P~7
KF4j=O><3lkWhxEE@9)42XC4N$KO^h4R5D8`o9y|hcal%GhN^=k!qM)#&R)J8bixJY=;vuV8BsSOiv<Cp~hwnnF;=R?Rjh4KfWC{jDp$0QLD^JfHTMGAaOm&
1bjnMy_$@o`DS^$zB<*h=R1_^4LmY_YBl0pt=M$Y-5i#i7R~IBDhjP~Qfl)3w6<bxvUM;W3J}Vu!vRItE|I$5N4l{@1RE|=qi6$a5)J80tc$e-eBMe8s}u}$
kt-qW9rP$_?DV5gEq1rj0HL}(ysgEN$0N+d2v7oRZE6PNPEVBZPR9|K3uvnR$n-)WiVHT&;WmbHn8v9Xj|LcCP>Js|NL@4Ni8@uRN1r)(hzO7YkRSK@p5l)(
j{81<Qap*&Pdny>CAPKqR{1&DV6ivC$hQIfIYN_0ahUD>HOL2Io1}6zGB}rc)k1+)z%KP<tudLgpw9Y^jm16hwV<aa!#ysi-Q8w`q=y@>hU(71<q1*d6B~Ju
hC<S0M0SD;f42GzUfvIApP}q(wh<Au|2ML)@eSDpM#U>3V7WbjmrWP8qL@V!OB4?Vja@1s`JpKvS@tb{U13b6yXk~=QSO|kN~5=t>!t{&eb=!)kS&-)!BZ{k
k2JB)#O{{cq3ffTn4e2{;+Bm;ZKS@%rbc|PxsOtU@Jk&I8D#{RbCjpzNQ*L(`JC!e+~zom-E>r`;^$=N&P3&8xT(#s*1iw{(-^xj3#YcA{FL2_jP$);GFkez
3G<{Dd%q9a|A9jx&p-|Y(vN`0BeBTi9BD56dn9TYRC(PPuym?3SUcsczGB#RFcV+++;fb#7{su==tIVNm|<gtC(o~%Z9|z&*aj{9!lbzZ+DlVM;gW)H(&|vV
W_S5ctzXkAT%HEEoUjn}j5C8}({h6U(i<zgG=5Bj2V!0iovcHHq&49lN1`Q_F|2z|*JEoB*LS(r315O)DZ4aQLX)g5%H|dBVGVssJe{8}sP5|_Bfx9qAbN?N
`hrus+Ygl^uSW8SF%-U%t~;lHK8V~%@QUv7`_5Ahm+B=~3Pp@ON(X1owQgDHhXdNti6Ys%e%ajT;D$6m%Aw5vItl+-an+R{S4Xy*EKH2;W*c^hAm7;K+n)RW
gN1m@>&xdVsKo^#x^pFkbcMsI==CSo3^9pZKp3gs)yqr~-i0qAVFKNHyJ!~#MD31sblw}tVK<3)wSO9n7}N-bcfKcY?pvCQS7JImE&mLKNa;uyEOz(q+1{<N
;<x-#bdliyC*2y;s8{(XmQd<!99`wZay#7eggLg9KN@sGdqEzZrfeQ&^9*FdLz-cpA&cUZ4(wI2E#%WDYU7(BL+WB>7d!j2b>H`IXB{#BQ{Ll;$?x!CzdV%S
NO^^-mEC1^R+*OkaZ<n@oK4$ryOsEqeDSu4CpGQ{k0@CCB61I7=UqHx5S!UyuMF9sS{fMEVV=sURC_<F5JN@ldZ0-SdITSWsf9D&PEjUByerw2vz^fP5~G_8
`!TR1&Y+|5rJ*$(_S9<QB+t{{HqJ43<~6(8_SKK!I2Z-KL9>v8glHh^bv=Ym4kV|BPVs|xN;}d+hZ5dg(&g%SAvS}yLW6aNkAp>i=e>BSD#b_v891b5xKaVe
a2kd@5lPGlIZ+qb>kQ(7I};#*EAKjOnY9oeuc%J?D|05bcD`-#dzBc4lX!*PWVYsen@YBNvRG!(N`d`}@a`YE@f-&IFLHWxT;o-9uoXk}(NX9;gGF$NOSY%j
^{ALW<nSrojO#{W?U6EAegysEbz%lO|NXA=@J}_hKPBtWFl8sR>vmdG`4glz#rVMQRIPe!)y{#0;RWTsv(jLC0)Ogeo!nV+zp%bzgs`D5_Nf0gA@A!BwS<U$
7~#~ll?Ykdn_&4c48LawP3W33-f|l+_h%Mb55m#-V~aI>C8D2z5Z|6^05uhXm{Bls-IBNtq#V%H1##R6a$+$o8t3$}sw=s_Pt}n$^CzPKm${kLS5={q9+I%}
JET1doYzpmz*%SSW%%kVq7kY}VO$2!9=HVKmYoDV9P@+zvU6?0_s^4XT5O1u*ZK_itSP52PL00F<!R@8U?S+~xj?PG!K!;^5DGt46B^jZR!2$u7oQ9*6sRAf
yY|2XvvLPsJcg&0QqU%e{wpAZUXCMUpI6DW8(Pv?-MNSly-kV^eTLe%4)P{;U)O{iV;@s;cD$hf_+8v}vShxQv;mu%lPS{Uo^q#()%1bM>2lu@QzzPGvcYX4
@t<~+Ce4&xV;)+pdcK(`+!3tq*%AqInj0Fj7|o)gc|Ne@Pn4xxN@)D355tVhRW`ua4sUsxD?fCu$A&ae6j>Q@`hzL8>HXIE(qw(2jBTA3YurKTODt#FqCD@}
SWw1u`9=989BAw&o+ZR8LVYjX#&Tmf^5vQ{fLEm#PK|t1eGCH>1v8)Kbbf2P%t+8Ll@g?cP={wJJy`r%Dm3n>gesDox1E7&e?j_qoY&XtM1eJ!dr=t&(Gb2e
D4tdCX3X(3m!Uk*kx%CC{;su}>jA)?$0YJqk!tP!6R0pP4Kf?hdL1bBpIyoNrC(?LF)P+|huj$|qU9sf?B-!k#_hY(!<?@fF=OrtGR?JRu#_>ffJD=YZzA>Q
RsWJGV=f&1n*Wi(xzMwhOSg#1+;+Dd*!2_5cB+cYuX;VwtF{iM*mY{luiB7!x(_IsR2;}-p9-Jf1hK6$5_|Jyz|eEB&riNVW}j0c#{IfM(A>reJ?#Aa^?NDr
DH{4@-wZ@Oa?*nuA4&)5R3+{q!iD+Fpj}evbNL?^ZJ`dr7@}_S1P3VgG{qt|bi9>`%*W=Bkx{S)KLt92g4&Uo{n~zx?l|V80~qi``r~mdJ`c)Nen~cB8LM}D
!N(!_b`8T^1q}yGwbM`$o2+uI!nmag0J{SsRRNzH#OmiU-wOAM5sZurh}L(RC8Df-3Gl%i-#7A`fGPv(^(W5pA=}+exIe23l_{ou-YnhEI=X3hiWlrPgRqq^
_Jer7VSzK*)k*o_4-Yq>*Gt1BXBbmViET|d5n}Sy!A=)9zb`U>F&dGMUk4;4uy)R!UpnaFZcP2}eXJtlMH8MyAw)K<gLlbR#R|Tl4>!kkFJ@O7U^pFFtj>4F
+^=^=IBm=BjvG!LP6Tc{6}sigU6j(4IOEYFQSb{MyWp{uewBW$&z#E6@SFJ~c4$tFWokPxk3KJl`36RcMU_F?zey?ab|0j#M}5hvm(b@t8n8akf8~wh9sIMk
@z7Gc4;YMhcZd?oKsZWtJG~qwv4sl2k+gXW_NU!+`N({Fj%)c()x2BRlW@iHh?8#Bq%7q$jxptcSw9*A218O67Wbb1+$)f4%(>C|zMNOHdgOo#etqT%z|T#B
uO*^jpSz#ho8>k&?4kOY4s*bnd$?@?cnm$g87)E@B6z~p%hD**%1mDd_xsaFt%*=?7gY&4Az?&u4AvQ5?*pb7Q^SlwT=hU$r^Rb;o|Wi%Z*(O07S^<^)^5(q
Z28c#*|>B9Aq}abkoO&jCg)#N^tb4MGP{jQv%2eg*bZYf7{&?8g6aFzL4y|33_Lz=+gh#TUuF7nhN5#yP0OS@zVY%?PH`eJj0~lU;9GCLKvD7&q}ymN8vhUM
FS%QEXs@LL<w^A{$rJIQS96uriUlTs*bDaed)Re}i(8d`+KkW$5e~Sp#!M5db9BWYa(2j%Oq~`+h=`b823UH5S>#>t{X8xFNqT)Ksm@#!llBru06?V#H@mcK
0sEp%j`)#`ae^>k1ugqXNGyw6ud4hF=JqN8DrGz#^TzZ#*Wo_u%ib`Wnn3P-u^%wJDQ4B|-O4F--^B?d*8|$v0WeMky^Ak<=~FUIAh%O%1S-D`56Ec&${)H*
7A%F?Bh<`2E<$rR5T?|rrg8&d8YE?gQ><DCA)~v7!Q@fAc)X19BwpWAlFti&9l^PBGD~K`yo)Q%@`Tfr-7$1DalZWg@xqnYVUEP_=!m^tuh2psd(Wt}!zHL)
O9qN0YO;p%EBfmRUtzxerSH}EuPH^KjlDo#$_mInU&f?osXqnH?s-X)^Pk=xSo&}s%z=TBqe7;376TXUPAyFY-03yWLS=YBIt4c(Z$bgu&o#e%AXR10W=Hw(
i5TTprJjZ#YvlMF)F@wSi8o1lR4DG-FSK_=VHNFm1ws&6zROQF)~YcWJ7*-gfsiK&sp~{<wGwiUuQgytvHR7z_+{WAX_Nw~qerd>QYoYP<zPmf!O)DoO$E(~
Vm>mu*0!u89F0irH|cKld>w-qF`Q$5IOuVbl%p%PLgyQ9Do;H59jnG8*Wp49(`#llr!|v;*d43DX6D2-##^WxV=lvnB$@>f$W^vGCUEt8cK>{A&>BF^A+nkE
pdi<I22c-7y7cEET`jVIx+ILaK^MFivbEZH{SKmwYll4C^63Z&$3cJe{qIYyC`AjHX9O%iX^<U&@CJR;uZ&36OplRBarKBm5hACUI3$>gq*eZ4VfQS>a$qIN
;<YKP;)dYd<G7_>i0G<&PY4;(g%Ej-4V3cewtLP%lnFF{PC)eZVfZ7kD<`pi1=ixa3)%vd29eG8z3P3#%wcR5j}GQ&Xz;|Ql#j0Iesj&G0?1K`7f&h&^Xa*T
uK0~Fp<yL~Nb4Ow8c+gy_UD{iy8j*+@5%k`6@^aL`&!fH4kNOMRxL4+v+aYf#{$7i*PU%pZzpF$QrW}-Orj^pcF61d+4itSwM4ljvrdryfsri9Kb#mBkA9^-
-a6sCl=GNH+FQ05NXK|2l+z<$X2#N58pBphQC=4mk`DI>r53|BzE~mP?J0B}y2DXJM#6It!39)!sVyiE4p%mzZb)wLDFGG0&FdBOEsCDA0*4)~IO@7g-a97F
0sY7Gz<Mr{Pk54m@H+(r^ngf&B99epq!r_C@YzPWN||?k)x-;beqzL;X7lU^ySreT6UzyYH|u~P6OF<yJ)S{l4(WH6u$*uT#;W7xrhHI^p_Jmno6BG~7YW)=
m)6e{R~6+sA`_vi(z}6H9Q^WY_CGDuOMSGRV9FSEv~r^_?qR?6MaM5ND`QHRF=m6YlWC~kWT}ntt}68E+VJGIgp^)!N{XPFrvA4UA5=K*P_AtPz9+<Aze&ov
F17-C@820)nCp@`Nq+dc=#w}dovw!r{M&MdOM?6JY)ZL3w>>gVM*cuny<r~sPm;{!S{HY_l041{*GWAo8qlq&Un77<H<77D>%HD;O86{_4d{F!QWK>Vz{7SQ
8oZI5o+6Kj&v(iOeUdw_)eA6dtPm7fXRmYc26wGX6Gm1BKxLc&WG!e62eGFt7R1bB?>Jlw#&ZOjfQ7v(<<|7KwGdrb!C25Mv+~aO=A~Z9V#q5naUW(z;7fD-
Nk3<FJqS}Bx&&~2M!?b_I#Tsi{$MRWR{m?DKj%ditr#`@#JY{tne)T(9xo|_VU@9w0S&YYQZZ_G6Vn&ppZgl)!Ym!<$^1(o>v|R~RaPp{7g&f#om}!oCHoKa
Alj|JR$*}u_<_tIh(9D5{v{`}(6}4J;M7CTDR5TZ==qo6M-J?agm|UmfnPmeZ@|hu45I@$mjIJmGZ9aBtsa@+ZLcdkgw0D@+Tgl_kKrDs8vP3_+EW0iTrZ|s
CM%2-hju(?HH!741r?AbwQ&n)vl<)1?i*K_IxLC24!8&VQ^9!)NDv<yZar-=2_3=f<UDP}2?Y1`hs<s4%fwwCxvnp?oiVup2P)nt!@YOXP&%AbuH1RE_ZV<%
gtB4kHw*`RZU}WxuLVBvoCoU`qx!E^6l84XOia}fOC$?5kF$1VNu!mUJl|svMmxWMHH^w7^!qQEuGy{~Gh_l)Y*Hhd**Scq-Ybbhb$J$W(#DAub>m1@O;aru
;3#3KTDn1hpcrZM4V_2cP9dkRvZWE0G8>ScJCz)SY&MNR{=8J*rcuB_Ky9@3NGpgtApTHEB10B9iL?+EjbPL?VjVgk37#toG^E_H#VPZou62Ci)0P>)xHVwX
otH4BzKFc@Me~ifV*d2y$jf**uM*QGz}UPC9XKLoPRKhU63qEYBn~6@?$z#;uXDdJoevQ$f2Bx9I}K_jq1Uw~<i9oyG=8te4aq`Dd-c11Z>DZ+rA^)O$LSDQ
qEX7Bd5nepc+}X*Kk8hm<K<R?pv`OCsIi@Ig>v!LmKg>YZLI+3W)bHs3mpkQLN}Y1!U{=GG`Z(k6QM5wM(5uyq9+#?1Hn~#npangG;<V(nMp?mTn^EN!05(e
6g^>hXcg#^2kO6X*OtjG+(o+{q6*@GyoU$NR%5f5uUR9G&Va@iTnrCHM1ihgr^MQ>15SKY7PoT_+fz+6R>@W^A@1!_J5VZVR)N@wyKzX0rO?uIm)SHirstX|
kE#00;KYpcvjjvk{5d1b35qUy4gW73_wrGffi_Q{*bL`|UW1Ob7mmT{(PqdC9Qs^ZmacaOe5P2OeWdzuj+g_yld5{SB5_~vw{hlmOk5HS$qR*wU0!^(MdPfM
^76duhyRrPi+EFxBX8_qZd*JKl_b%nD>PCd1q4hF4Y@^<lyUQGLpqe^WpM5z?o@FX?#HlJR>_;`>M}G;8U7`1)YUTBJKmJjetpl@`U_05BO-#s1T|l1XL)p5
?l+YxSx=P&T)R{pfI1`PIg@tyg&P)r+?tKJXcIv`*25tA+UyC5L`AgR=d8)%E$n1UTYC6l^k3?jkVdZpoCcZKg!D84&}eWtI(|F$A!UP{odID>lvW=Pn6a>B
y^qN?!gj@kcwgzcPFlxZ@$=R8xRVG6<(pQrIdM|Ta*QcuF15Gj=r>~h-qqo!MSiUHtBc{@hgY1$wotjf+)sqO0JX6<EjSFSEUVZKJ|mS?pO|$!=(0J26a(VX
Ias5#0Re_~0_=;<JusL>u4|Sd)|M(nF~GFCS>B8a=;y?|i35~f+anjBBcOrsds?-0_C(79cm=t!cR1><Q$a<_qdW+b)gXyBr$EN}Zr7TVdQ++U7tt(0#Fy}@
SW|y(g-3`(h}=G`qtrvwkBYv*%mC%gi#;_SmE3U2l?#y2mcfBa+(90#_s=vgTXs<yZ;{D)Z~F|(a_p}h_#-DI9rzu^wrX9>KGbq)exV`;W{(MEqasOn<P5s5
zhX#jHE0jLz)I(<`R5s>D_V^GdD1zG=;yqGzKB_!>l0V+y&Iq_2Wg!5@tY^{tlIdIf}taZRtj$RM#b+g3tb(3IE|f5Q^3Z4G87*yAT7e=I?H~#*||?2J@c;<
#}QZE5N4^vs58wct-EdLA(_ybXU{QItXmN&EWA=5_y)W@Cr@={uwGQcxxpd>%K_4Puv0h2DI`Jxk8vXvFy5EY`dV|;n#91(A3YMZYGLj5S_3rVPYU)y$`!vQ
j~T5V{F01&!J0Pz(j+24wF!}k*AhLJgk~98A(Hv+k>7$bkXNN~zW6`UfbIvn4=roeq*PAEZyoLC;pOWocmcX3!?2*cI><4*;Qb`O3DYqs7J5*KdRP+(9L1wY
AQxm>NsTl*g^M|ga<>C?MGPx=RXlpplRc)C#LUN3k?_eA3evMyJh}{Ww<p%*4~~}(RWR2GV>YnQGc@xfD-px|hY6;dG?|&lvPeYm=NfwNt$%W9ku)T<1qGgi
#OuIOxhR#Hmh#~IUzpJ#tnCOOu18sck<XxWz;he7{i;?7N)lf3zo4(k<;_I5^+5SE_`O_paH%fx{48B}b$Xy%u0yg69(tAHBMerz1+ys*wA=&|AFw?uY%gV;
!CnOGY57d`G!Q=Z$b~68%IFs?^zq|}Zwr1|UYiaW%Sd!?Ufa}G7=f%6VvwsQOBrr-zxP-%>_xzKRk#z4%%IgH<rH+P*v~;|K0g29ycHt4DHGu&+z|7sSof0M
^1zO%o;fFgC8SDp6v6qcU)Z75Gy~7$-K3g62^1jj@Gpoy)__D6`rE4|J`yS66)l_<_^hKVowj6Qa4R1r)*J?FE1TuY;DM8ZNKaG8CRCOqw|kjcglY(EMY&y6
9qk~w`cVnwQ28}0wIM6c0^z*=_kEz85&dAN(He1tJAz8uy)c(x)fD0U4`XmTdQ?4<bMt$O0tuqlj2?&4T>TzoQ$?gz_LR#lxOmb&J0^P4mVJ$q3Yq+CYdlK5
EP`mN#CRH19yN-twGkLYmE=Bns^K7ydGGnhQIrUrJ`i$lDfzX*4pPQ$0;~!hs$glAe8v^E9%B_VNWT6Dg>F&JM{}&@2qB>aDocV)W9|bL2;1CnMhtSrTveNC
exu10I(>ygLQh8;Xyz@VIZmVE#0hQz)+aFxZW4=#31I^pOT;n54;TbfMiFE+O3W=9*|5v$U>@W<C)B}JB(R}xgwdxzKxkKY-TBMW^zP}^ak%N#qSjPet_yir
c<1DZ^T#BpUb7~(WdhDKK&14ABe(UW(idI%Oi=pd2nc_o-UUe_tn)TEMDy-GagH#@6RCnyInn(HCBH}h8}A5Rf>sL{Yu4Me(wgWWJ;`(t;AuB|)u|Q+%+)wk
`BeL(AS%J{pVGS#s@mG1NV3f*Z+yS_HK{Au%oYm{(j9|%*|rT;0^@`&=FbH_|H!K<t>d()_?hsw|Mz%90~4FJpp&6RNVm1iJIepsNdXMdjv<s3%yGLm5*Zde
&E(blDb}0+cfy`#t$Bbtz88b>QAfaTfEr0XZ;u+Yh(K<nsbtiUib;9r@d5;*6HK4#<WI@%ceD0*_;GcdA5z*9hEcT*USJ427>IoqEq6lp{m+1>C*%@olvzU4
5JqY+Fixw3M5iIEt8l6NuO@I%w5An`8==-#diT?cq1aXjBaPhG^}&q9TQ}*lvr_)LX36DYa&H6Z51}O38u<y${jYH0%hdM0Ag`{6JV(bNRI7ar>{W?0f{a<3
_Ke3B)u}@erUv}Tp^6P2Lxbm>QQ5$}5ow~u`k!u`ZTtK9nIyoI6=CfXlz9Zv-n+QU@~^91qUn!mAb3;xM9(=`fbzeQf6|H@+gBAk(|Xya*FPQ$=L&}Ug(GsZ
7d|DWqB@;&*G18Vxr1YojS~k^7bA(|Sn3<oGNFzft&z3~4R^mha`ns}!59B;$DNf`oW=IH9qg;#&q>nJ!^a-+UL8}vephL~)cV3>rdc#@lo;Wj{T#=O^G=#d
zO!~!VQo`k;r0df3B?bYDbKk4tF1ba-F8y^>sCXQXxX?Gj~n@g&}5#wh+dpkG9LVwt4nAuQ~j6RsL4G`)NarFL=VdkyFj&j&;i&|q5O&Y=Vs7|o}RtqD|P6D
ZMrOA!}Ff$`5x-{TWQ2dfLiPw**$AFgzB}5W6}1`uU%*+y>ORpX#FfU8zCa#+DBIA*l05$Mz-kB;$TgKf13a&B2MZSk@hG_zoQwZ@4MiE&8CBYfbs)e6s561
6Cb{#4kU#L?62SK??ARy1pl=-2z<poi;{Rc_&p8kC|Xu>geBGD81~>Nlg2N^XMObN|3Q!#oaQki*9)<BW2|7!WuhGJa2Uc*XPA%6k5DEKE+Neo!pjAplP744
VwuDJ+GDKkco|+jR{v<S6&2%n4xPak`EiidiI?aEJnr4w+GVW95X3Tmhw<j25-uW}J3vM>r|WL%GHg61$MkH_2SRi*V{le+H%dql7)X&n39yVc)*|O*8lbqO
TYZF$gnw){3#AaFvp2)<6Kt@X$%cvM7u_J3atby2T`0^QwZ&C};^|4+%V%e_>y9RQk6iWbr3bBxrSpxb#ci2G4>=i5$b`ff5Hz)oEoaVa*7A7z%sh;xVdE@2
J)G_<k!ub)yw+46k=zet58Zs>V+yWNth%Qcd+Y&U7Jp{?c`HcviU-i{n9QGO^GCT`9(Dc^E-FF{GOOqez(?pcHwiSqyEFV$ronzz;o3CvnTTO>&{Oa0f)!P-
su~@3*Ta!i?x)HjOh8~ICA1r6@L8|e&ump@U*lJ+hj0IU;g(bu8fJ6Ev_mccT~D_7TP_eZzpu!TZhL%VSFXtKZA-zFU@$5eLvou4{LWwg>TOX7J}83cdIUX9
hXt=<sB`K*(6>^O+41!ybTFf`rwk!7Bu4=5xIzjA@rMDwcP+?y6EYaUqWmk$CHMcZCATFdwns))xv1NshO6EDK4O*aeAhD|w+P9ihoN*Sm0|(o=;y($;iFB=
hscS1o~xmi*f@}*G(M=GDXptK{FYv9a*fP4@RL|<cL1FOD{BTKM1!|=sS^LWD2UrvCJV67r*9JpWyVT-maB`bCFVkRWvko3TvO29?b!Tz;#gvDP0D894K2~N
2oH&E&|^o%XCkXEO)-Y4s7W(VZZ+NV?`89YEyk+MdDH==<}Qqg%UVkfbDVFwM|zH`V^SoMKT1o5rl#`xi(_9vF|3Zq9wbg4ZxwSlK}C70=iN#Yn-FpsxB^MH
bm85GnjbTc8eVT1=?uOL*QWw!2C4o`M?kBpT2#&h&E~2zhN~-iExpeK9inI$4sGq?ohD}jx1N4XN`Yf{@_0UZFV7rgb7(X3q%RtHoRu_iGH~hN5t6?E_pQeG
OL}1Hw*4*KD0i$JV=2JXCO4G4mkw}htt0Gc9TWU&rinF}vq3&wE_wz#!~qV#ZCf|wp^B`~Z;CVep82jhKow?{f|VRfnUj&~g<(U#6rcu%luXT;f9)iz9dUb4
DZ{)hNWM-FX$c3TuUG~>xn*8rTcF$EHJi`oozSlSmplsAoP49|==n9TA%D!}(mywo*Be1WA5uTRA)ioOt#w#+Xt0Kg!f0a&689*R79HeyEzyagijM7ZypmWy
1+CB?@rI8SHadOcO}q89dK<4Hy4<D;g2D8~I1?7II%D;v5{w5g@+-Mz5PM;1*r3Rq2BpKkvyOaVjjdbFUPS)5s{yHooy8U~@>=ecK!8h^uEeua7>xEbx$0da
G07f&DR(caOVEMCCEGVAqZTboVfOsvp!UI6RGT-1CTLr0cZ*_!?`>zQ)8M&fqfrR>_v;#zVO!SBS6Ah}JZ2s=nKNg6&Y(_Hv{^0pm27v8$=Puap#5pRGXw8v
-mc!$cv84WYU)YzcN@j5#aW{urQk3Mw<5B8*#KwOXUkG%`(eu>SYeIMx7ExkaA}bb$RCM!70JIrs`6B)3ReF#izqU~+py-yHu@9q6fDMq%KXz<J$Z5VJ_lf-
Qv3a#Ye_iD9Sh_moyzu1ZmDfU!q9P7v?|~liWra*#EeBOb*ZRTyve^zz5fp_HpnDzVGGa7|5!z%EJ8tb%MkwXoE{4$VEzaqF?y)ZNX{qwn>aCaSW^b4ZhDrb
LJ_{!%!EMd8H{%ttx@ek=&Ns>m5zO`S|LjK&`$j7=QnR@m?FB}8_M8ngL<|FMS=|K)H*=(9M!&3EK!V~^PG=+<6c}zn{t)$E@ygjZDFCN{h7;AS->uUwx8L4
8eKq;2=J9o5Pw+U2SpHHRb(n2q|NnS)y=zoR(-T!$fj{sqJ2|hEyE{-tN>sBjV03d;6qo*DIXtuS?P$@z85YUfALQv{MG&lC4;gJ<$M9WPyG@*qlycpaz@T$
Zlh|5YQ^y4a9b3~ET%&)z)mL<xHRN!D+_U9M)8pb!7bgwBaVbrc#9%!A_DdG7@+^u@{csZ^|^oI19w$eWR8!DGlP!t0W2AgqeNCLaFiaZPSoivr$f$~=Sxfi
dl?T05qbFepz6gYLGZl(59uq<WsK4fw>Kgodz{z#>$c9aCqLk(A(QYSzR-7!X`OCQZbz4feMSu&)tq{&yS$*K)SpcnakAT8Z#+sGl7M}REo8n-%611XA*Ej5
`QHpMK}akAZMKrAwro8<8e?hR31%VyF@ItWov3|*Of4SIAn4XUlI0in#)B5?4$jp9l-H{_eA5BS8B@GQUl@&oT0sgQP)V$KB3L`YCqD>cZ+(V4JlzTt8_{$V
FWI3a5HX$rzMEf#+QBT?rr(<6o~Gf>KWt0nR%t4N_ZA!5b-Li50XGKUsLY&HqWq?^)}Qr<v~q*#Pv%Gnh>|YhTxajg&IsHOBL4l-)0ia%dBAyaf9!u?>Tpfp
<i=7IELX1toS{K@7sYzY8dy7n1ZWCU8i3!A0c--wCz5?AftLxeZBk~12~F`I)9Lh(<7wG8qNx4IO?dcKB)rj6={C-AUo9{9VzYH!<v}Fuoizm|+3DH1lM5s!
#21JB6iV?`9OLe9Stb4S?2avJs*#*)o57ol+|~LiklF}=c`CX=W0C{k#*W?Vx{of%qw6Wk*#iZ^a`u_Nt%aL`NbS_m*!SoTT*q_E=>bo@`V<=^<M!CzQzj~s
!?ljK-{L`f(8d5YG=vm__~IhW3sd|7_N9zdj~=g*@glBBr10Y-D43v1v7bZ?zp2KsGXwo!@=q%r7#Kr6#Xg3O9wmAhFt`#yAv}26&e|j7pPf4*<S_7(^nn`n
`J4ncUZeKBZGD#s`@MomLt&>P5Pj~HhuzD|_TjI_o>0gW0m;Ras$ERA4P!<AMZGS&F0d#zf*9Ojp<-k+h=U7pRC2s@EKkOjkN)Z#$41!_R5iDCoPtT|Pw&8C
ANk%hWG-%+3aWrE{q?ls_KsS@1J$G4&`2ddsVtQ;kaO0V9s#Yv$pmvuifi$ALG2k@HFIg^T!l_|5=1MGLlpN!!xMK83|5cY#LCW|niMsQtTvaSk#oo1fDgJ^
_%Kmlz5?4dN!1^JLjPkWd0LCWBRbwML0nm<a0YiRTka-xasA%Cqmv|(qH<O7EMqeS`DnwfI=<)lTtZ}r!pG_#CJi=8C{M&ad#tp5ObDRfs2I_!O_R#H>pDw!
KafuZesyjm;yJr6_GspSOISZU4;GUC(y$*li~l6caIy5{|0n>{YcwAr(i`Kd^K*Pbu&;yAmqLU2d8566PO+NZ&$o|DZ+pB;z)(Mqut_AbUI1Tz?b>1+@TNa_
0%VRGn3v2sGh27YJ6l0p0Aqjja=PCTTm^eXwl>HV1%?t&vzW|Q=6*a7s&*8O#g0c2ysWS`w?3s6FVM`v%0~+2LZT<(Oh`gWr~#!a<@c!G*-93`JgGH_AnMd>
ic-e2#XY6fjgrC?eJ^AxPVd)l0jG~$XKP@y`kjiqQbUukOiCJbU4D^)J$2nbICl#ci~kx4pD9_NqagLgXqe-Y(LT}XC*52qr11zZh1XL{|9z%&0OIg}m&ola
cA-dzokg(w@zEb}ekvNP4#+t?57zYeBMa5dap|>hrjfp%lrFY3-`W*i$8qbkhJDOZ2|DRn8y`4jU0M;Pb9`1TtI+dOD>OSJ2uh8j_0_N;k=kRMnhS-?!rfT*
^LNbvso5TBz~>A5hMmXYCm$$hLOhMIjhg6v&Y!_$BbkBStjD!F5~OOp8^E9A019c;khv@luYN;MQ&&CjYZ)~7@dAbW3T3|HjHNDE!Z225-zS$EjHnRgN+VAV
v`eOnpp;zvY8{x7mxQzC+Bb#)LG|F}O)Faf$5zq5{FypTL)F=qOc4_8dAzDmuPY%JI<bCu{58;0Upk4=b_$Dn!FXbC3)lwU3Z*Cn2afr%0TO7538grQP)qRy
FhB|;6F0_KRg)zmmIPdloN}A~S6$Jod=r!!lLRCA5+qrYOx+X=cEyK$VEcKvx9%DLiYPjr^Aq7^4*LXg@g>6Am#Z1>W&z81jH;@&GKv_sqve5D%0HNDmnMg^
P$dKnv<1kU*y%)P?_@Q%+nV2@oi@a0q>GLD0z`CP2y3Pn^Fi(eofK8Connnwlw(CD#~DVmOL!zq#&>B()GOSrs=f2|{ZeZ7c!3*Q2y?$Kzf{^&Jts{3CjKj}
o3b8B38`P5n48uQ>e7|656jZ23^Bd>V~n`hC|*1~vfG|0RVXMe$}|7u;>TA^lAX~D@$3BAlnH5dy3VQ8G+>40%e44urn@F<PnVuP;9YIcoPx)VB1*v%raKxF
x!8E%sr*2(-o8G5elBYd4g#n#roTfvv4Wt?buvB42tCt9q;!aaH}t>iyamI5BposL-3nN=r~FB*Nh;jc!wi)34W@Twh*`R^RJ=c_NHyQKU-M7Z8yEyZ5SQ_p
Xz7G{ietWS-)8z)m$Tq&U@(fni_Lmik!ZK=(y(DF10c1X0k;MAq+o^M4=t!s2O}yfLm!qhd-q?}nZqYz_vDp<*uAKZPW?<jP@}wGn;;#^Hw1v5mQ*1`Ua^q6
yq7xLibvB9>{x<RjxIKQ^<Z>PDJPB*_MOkL!~@xhCvIh&FY_z+GU<BTvC(=gw3dJrh9w1MfNX_1dV$P<usjUD_ZMmb<hl0aiTJ+#bmMFU0%Bl$ka~v~!~;V~
&gN;(7V3`_{~x$nBp#*Ggp9W&4|ooV^a=dB0287|!qO!gcJ`CFmAvP07}zbQQ2054fsC4JkO0Lv#D$mp@Z4S_2xdbyD~a4sPU#Cm#slwvt#)ZX34yv@N?~xB
SYE1))|U8aS0uG(%)qxwQj;9M395fY7|WUjH{ULChej9!H|UyEG(ko{`3;7=`dCX$vWJ?6jC^OrvCz(XfF)Sgvz>bL9BoYTY#4m4X4rCe)@cK__<xss=_2V1
^ecU?#NxR^($G^lrn!tJfPdr5k-x8L(bW#vqTiJ(yr@Drg6}2Q+mS$zjr&qGC94{~fChq(%dydhx=u#RM`s65!vvSnn@43D_w@CPLwz8gtF_8ntLD6&P#^&!
DSV|t@4(UtCyKxzWW`|JFTNl2zIUK~-y6czwpd0Vt8V}2x#7!2dH*a+st5eQ>wcxd7gLuwxW%%9p~$0OE%_sfT&F51YZ%?^V&C4~#xRM==!jp}lz^qVpKpw;
d)WZ-TKuU(m;_7KATih}YMn7{9imJLV;D=Tg<{#0L<Y}ZwpfP{9E7dW*M7&@eq`dr{JlhI_s3?QDO}!Rbsn?u3+M+`L4=7mk$53ZG)=$NH`8s$kgmUqFHCHR
P|LCe>kC|Wt#JsNZC%VO_eUWV80*c3(;ph_08+-};16?Eo!g`8+zHunvQdjl&WnB_vLXA(UQMkfKo+~~u>^yGcg2Uj=V8zcsguH&4yqq?IC2ncc3Gxqh5$x?
#vANV`>DMz`wU4qrO)Q}$B+4)SCH<F?OLIi)njcoq^EW=K@{=ul>+b5gL8eXf%Ab$n4Q`7`dHI4m-P}Nrj}3nuOgkKQHfiN(ZUjt={VPME^;MuQbqHMY>OrH
C%C!|LTP<Ft&CERQ2yGmH5>zB^|&DWGIa*6j;F<T;Qe$>VPA4dZ7RLw`E|EjDz)kVlOh@K<jo%nVqE3YYiMsup=`MLZLgI-VeN~ZsxKUI>IdTlSf&}gYDV4M
nhG#92>a;)6@>B(T9c~^awDJC7K;a|8c@!n3%&@MOLdG+ORFJr0E3}xBE%I>ptonD%KlY<b~|#qhR5@!$&PmQymr0>gzXuv<Kb13sfz%TG=00&+{dKS(H~E8
{(&U?Gm4!yy<5hL(_LGAF3Xk=x+ZFzt=ScqLOdXa!WB%*_7IWw3;VVW@|^&S^o|raXimXFdpq%EJ$GcoBDLOU%o^2E8=YfiiRz>i+AJvWkBwoLG;&qpn*fKg
0jkqHMsQO{!c4?_j0qI9Jk>IfGo7(;b)7p`)IB*}lTDiM{uPfK0k$eu4xSSppso3$ReA?d=R<^A#<Wy3S?KefIwm0XgA;flRp-B3)5szpm6W%nVUYPU;~fJD
v_~WHXYiQ{R1QjiV^&5EB;Q2uXJpZ%b9xQq1m)$Vx(PI>S0?NBw<_P{AV7q?;_68&4Wi*qb)vmtJ+n!pJrSR2b&XPgHdcXe=AWwulC$b0J^&bpln)^&lfQz!
F|uSl+1n;0FEM`g@eLbpN&&xqq-QqJf0OIY%+Hf{4&&&g*D86+@AYl*ko6-{!f*~?8fAsZkl?;;1bS4-1%uG0sF+Y*d$g8Ln(AELgdG{+R^cP&tBx#bYGb<Y
`!j{aa2d>Y(k||*cqx7tm^K%`ZWss6j}UJqjve#aNz16=kE`Q_eVrpIB7oi?g)*(b3$kzThN^NbpIYt%PWPp)ZU{cWbzyTc^+zZ6<Q<I;2!KtR-2MMLj!adN
$0Y5wTQ8Ip3Tu!Fu0A|0z(TqXrJpO}Vq<<r3_27~7!QTF%DSbX%7TJjybF3+U_o%3%Jm+$z8f6|<dCesT0cX#jDdeI0fp3NxyGu~$V;FW`UIF3v-s7wk(S_r
$sGz?t@VkE4TfcB%augM^sTKHv)*hr@>FhV1K9Um@39ocu!>irDL^x=q=I<XV%9R@x=8Ls8i_zmwG&S1|KkNf+#T5(H&aF_a7Jhn-vl_16lc6kzP~g^R^8qA
DG&AD7pn)_89|rsUCG5z%utI0YKVj;P+rYgF105fmzPvWu*$(_A8-2Gil%gCCs5x@w*`~dz{>9#y6d4&p9UA&)X=9JO<M+?S>zaI;1q9%oHCFuohd+BGEkhu
l1=VeDXqlNKS^XCfhfD7-78ni+s?Qke-nM0ccs-YtRWIcH_uxIQJ+f*Q}ExJSkE;|*4j$8Ju-z|IFv_GP={T-x!0u)M>I$>e9}HqJ8VFH?xj+84DeGeO*ia%
n22}U_(lqveZ?g$tOEO4gS**djRj7~J#3sR)d)xOHrf(N>=*>N6mTMGSJq+$ov16|G$>>mGpQf}^n{H+F+l3NP(3@~;qXhaEwK89x!wH%giM9~C+vV$Um0By
cdD43gKjy_Kqpiyv`0rDy3(CeAzC|61^I~8;s0H^)KUVKH!x(vn>9?UyeRSq0up3>0N65V`~P(<riw4P_MfQ)akF6;0QlA$UA3$&)tRidb6|^P*k-1P-#uEd
QYa@$?ygSh@U%eaZ2X<ac807LPo#Ud22paFDLpVcv9;Bc1|)2qTox7)3XR%8U$KXBlg)6;;S}bQf~Skm;%nqFXGlP~s)2ltk7XNP{S)30UD?NwhLe501&|B9
J(%7Hp76@4`onWffk!#p|J`hC0FKke6@mTLUCe@F1%e*z)<N_u3-hiT<a@k1*X*&`qNzAd;ETc>MO<%W)4X?W=BRATkdV^Ylp=}cdVO>jWueBOmP*B*M>UQw
Qx$%~yg@&^PA+(ZC87TOp(CI}c-8BQ-SK;5$N;o`&uNY3z;DZIXIKYktuzmadR36$pT`VkSG7AwvR`R2ajHZG+uYI{@7c6-npBITROiJZxDLyK9oiWstDSTc
fM2f^Hhn4mNxOa&@PDW=^6IRY<mQEZypWhD((-3<Czi69z9L{WMD|KrUHzM%r%=3Gb2R&py@F1slHsDqGhlrCN?BtBn7K-U%0jnsrnt-NWro5k+iAdga`MoH
Qt<|YwAh@}Er|j-6tSTrac)Ut^N3BpIrrZ9jvpH%yVg^~T{C|CGj25)acBr4`9&7SCHQriTgtq4oZd>Z12h<}pBMjgYjYfXvTa0VDn>KwU)goXKg75ENS`a2
Y5Xo&Q9mlnBY+w6y9}+XsT>OpKbi-xy-<%hKRI{0pZ5!1EOdp&u;>pk*brX<&UI*s1V~Z^AP^m*llFUFW;ykiEI!=*6LF{uC<Y53%#=agNWkL<gA~n5QI)+Z
kv@AV=jY8LB8=~q0@5knaHqefqr`tJSAh_b4BC4E(=$<f@4$iwT|i{e0dmQ&Rcpt;0_<A+a)J<C<PNs!X&t_&37<p-qEwB12jG$C$=HGdj0UF#2Un$6Vo>KT
k+7IX8wTiu;_S41-kURqOE|a*aZU_&`9(t-A&fKs-O5KZm6T%EU<^6so6z+0!w)TwevRO7vNGJuXOlD`v;&#2q2tiGSyTUka;OW2frI7qF_3z7g&EhUrS91;
<@x8k?i+{W{9OhC!@t@*B%;VN{o0rUxRirt?wj`eACS2ncBl}$P~%zY*^_EtTT0_M6O-MKtKGX7!J~hj6sEp#%krC`qE4`kWHZr`bN`(EZ6=vWtIRl1hv&(-
RStZJY=d38ZT61D+8p!q1S;Yezhf>3?Ywk^KXH1ksf*7iLE?TjhvLphXxd=~G~QWXlW=I5tmVy=8!Z~(?7KJ1q{=cGB1F!dSOqfm#RK;iUu`>QTtw0Lu7s(*
6A5n|LAG>X4o(lLIy%hK&uiIOmV(1N^2mm_MiwK%!0pDrpkev;3Wsl64CJeSl2ePl%z@QOkMj4|+BMe~?YV(O*ERhp?+FFAiD<~uv=sYu#_&??qV@9(ig2ql
o$1v#)O<vma_1UP=ADHrV`6W>#v*CBtKl9jP??3tcbot;e`K5;UrKI!izIm^J3^6jQxCD4x<WPd%@l8)oms_k^G9ZndjlTM%i;3{-wI?>*iF08k-3zT3-MRf
(C9L7B!#HzHPl@eyMz&h)fD3i88SZJ`V|IZr!?vrSJy!{Uqv$<Aky3v_y;^g?bB7^bs3X(CQrOS-8U9+Rp(bTk5e3RHQqusL0PL5y->v#CAgBYh0RabTNe6y
IhPB^<?xutphw2@fckzx1<_NV=~E0rWMfiUDnT<k#jKh~Eb~_DkhiJMe9MhXn!HIx8gzj9r;^|&8T8a|%ACl}Jr&<pyYr&yFpK-BA~lLUT+UsT!zn+SOFfG_
70n7t<z-7TqHxjhcUb1jX?EHx4FqS1DMb&4(Yr_&3Ii4V@2OU?ag3DDrLx0;Cb;_7E)`0!4nM6=L`F8WD>YE%`r~HEY6ddpZJw09=(poAS8iVh35zj6i)qyR
_Rz^m4OPG)JGB3W7SZo1?g5X6teyY;s2B6|220u;OqZr$)yX-4`qkeli#V+3+MV`aG30cz73#33s*o!sdBeZfT;evee?(S}uBWI-_a=KT7d(`ulI(SluaO=>
AOxm%_<|!P!S=4x?-x{~gaNRGgQ~$z0@*C=i84KR+o&GOhA>d@I&62z+6;(&IG2KJ*LZbuu?9kL+2ht2Zn7RvT2#a{TVdqSyf;f@;x^(R!leSA`#yLl$0~j@
8!JXqZ@$;T-K#%Oj|wHUA5peoCG-=AJIIAJ?V7cOLp;Yr<`^*@or)`nlfGNwBZs{JW}gMT7HA-aanA4KU6!@`b48s0ja?#E+mGrm03=yCp8~ANv~3Dt6P{i~
U_~dg3{OJL7e31QLU$EVkRbbrPsRK2R@V1jXNeOC)}yj+wH2nna^0gwjyAUsM_8iQny<7f@E8%(zW=EPh`L=%d)9(Cc36OvA~D-gztagQ39zhM*N`={EF9%N
)e14h#Xi;kHRE1f1xzhm{I!=J6z;J3Uw-0P!4tXsR%F1`>XUMTbi%&46|)A7>c|FD6F`2G#k_tNepBWve1MSetu}POkA)sIX4|+GQ0mR&1c)^uA}(7E^qy(R
RU}qJ$Yu<bAY3*@W(07+)GesE(XDJC$Zn10wBJYfkHE;5A`l*)^OH#ep>1MOfKo^D`nILfj`orc)2rYUP~|jVPT{+~l?zn@?}}Df&eOLcDpi*tqr+**;@n(>
3EhI@Aj@LspgGBG<*MqFwTB9)-0p(oe|!kp?TG9|vD5ovCRP93$BI3SL+vZ$J<?EO-P<2cX|EM5kJX%QB20T1Q|UN{neIUXz8%6CIjF<<O6-~!71i~GV8TQ#
fLf7V)2o3KKLu1j%2%0_hz!-1>bldC-f)6hQ2cK$iGi5q_lG_cw85pkZoRN%90dK0+4@*?{glUH(GQ_T{~X^pn1~-{yR^1P1z8jC&M7ztu*@yg$5+>pE8ndz
>CRi}aGe7fu7yyB&>s#IJqU4~PA=oJy+6gz@=gZT-ua$k6=NnY%$G(YE+z?J;w*$PD12&ayva-A9J`q7e6ZHx`l<=F+#q;qgc+1iBY{Ka6KgDzP%TA_`m!zW
VIBFXaj@V)ReF^{1kl~#YV1JGmxedb!Gx3I`L$Y|0dBl;)n>YYoUx-woTJS)Qmn`oKI$WGy0l^m^b>#&;@E5sivZLSdKMF!gYOO=q@6%4{K;4?fL10fi#?!B
n-CoWK)PmXH8j@_dP42*G~0c^wLPPFYp6THUkf26AQapl$JJ?Dcaj!Uz<A!@?97vZ#Td@I^p!=lYE)!>=53nY2?kCh^#4v;2?vbA6{UQ~|L?8EX{6%*493{Q
;KDU<UIgG%flH*S`|!Y|s;P_C(Q+aN+c+b_HwEKE)h4xzWo8ojSXi7jEPdsk$mHObZ4l8FMtM?hy3h2k=q?8kudM_;C=)(<E%r9)+2e?1L7p)<uM$FDi6o)@
dAG5d(_Zo4K%9Kh#ELqc(x+Iy29xw2AZZCQ<P=4;BgArjya5G??eGj!KLXZ&UwGIz9(Og^-mn8z;_NH_h)Rzce#T|hP$i|4(mCj=0UQBEJ@I-|1_N>2Y}{sA
ijlHZx(s?xpqT=h7}0YJ^i&6~0#IemUcY(557teAS>QI0X8xwl!e_l+sIl+*8)EWMK=Oy4n7zAo&B75W3&}dFNLRs2)A!XiyX!AOmGQYOsQfiircYTQJ}hbQ
IUuz>R^9|b8ebaP#p#(8qLSs2g3KVy))<^&y8v2^&PbNXR%(RMq>zWiw5p%wtDD?4#)0HmTG8RffaS3WD^w<hPLUMNd@B{dRKh2_1-zaIpO=tdLd6r<ALz%%
A=*ApLzPEOfc7Sr>XLrDswRz-o1-T};Gima7k&1f%gcZ3b+RZ}c8<1Ed(N6>KR{jGW&O3tnS#}WaOTdDoLWK1BYl0AelA#KhLZcZV3A&!m3n1uNNsd2-tw#8
_xj=L(pLz#KC6!X;pv%>0l&TVQg9LdHLz?6MS<3^Nv*4c5#(^tm2H~la9m+@)1ZU9Ola5`ATubq*)C7kDr%%pUsZ@W5!rbT`Lj|{kDnpaG_6n?%@7hN5|fwn
1;SzP|0ndMmzt**IuR}TlrBQOi2dR{Nm@yMQdEY`K$-g5OdLHI3jK1h;<-(bDn0iO#$OKjV@NMma|uKeefVx4*AV)!<_>{<==x6-+R!o8J*+-=yYWr}#!$RM
+QHXtBaZwLh5FM`9I|sVZ4{1OAF`IT$(3T-?2tcQBFSpE@Y#zIlf5Kv`7~zI6T<u}*L?i50o6y%BWZr#tgh4cfP1!gt^I+W!XOU-hW2x_MN1+yz_83vmjk`u
=M4iB_F$|)Rzz~yyDmoB@@%fN@aJ3?{scyj%ZS6WSzy#MyQ0KD*U;zu!QM`cHfT_b@E$KyyvBQW-lpciy1w=9U)>YWhdfqOh6?7gv5oTAk=Uor-R+PB*<Ic^
#8)xWdatL=?GY?1+H@2#GOXtD(76hgq>c7!h*##wCTRF8EHsN$K%?}kwj`IyIYZ1_H(s1il!8NEA9yM9+W$m9qi@P`mK+(Gn|M<3)nM@?H5~<|?L@$z*zBzD
4>nVHU-;pvf0>P4(3M4Zm6xQd$ZWHvDZk357#x<U%5%~CiijKA2dUkZZ*Ya1yzC>{0I8tP5GHl^(48hy6S8YQGK@@fI>UlB^`(gW`Ab(pK<p#{cwp)KE7vCx
BOy;B<fldViDpDS2Je-s7<n~P4LelupeetFs}_+tSr=9<6oRTHY)AISKj~X1{)o_dd97huPX=fJ#jwb{OJZuCnY|=IDUrAa9f)L~`D90rGz(c(kL!(ju?eM3
kG}Qzf{?>5aC^hjVhnD8d)-*TMZ<}=Q-}-^2Tn+Fb$9d@(!?$DJa{s}5-=@2!-on*645L0oY#0ez$?pXq8nnzb7<Im&%h>(YM_xkG?Fgg^rB$psEHAzU(w|6
;!pi6zh=hEPl{AE-g`Ku;$)6N&FE(i_796IeHlzCI&xgjHGy-r4~7?gLUUbWKcqHxHJztdqbWqiV+)*$^6t@mDh!`}${pk2J(%cGk6P7@M67sS@va)JVqVh2
T=H-o>2gNy_I^7AEC+J?Ub!M!@8sU146?7DZ0BAfL(b$dFu31g{g6TGVR8I=nd*ymd%vZiFLvrF5WLNoxrHNh53Es%AZ@nvz~Xdfv-eLA0rW4mZ|~C06+*;K
=)y=?_=nydu_!;#{1n1g#$=5b`uEY}ebR~XL}dePVZTg1Z1w1Y?OZ>M-k12)9w69beWG6J&dmuZ)adVIz!HSRm4*IY)7>k9W`2&c&65}o#bt6OlWHhX^ob^i
hd3UnK$fSU8^<jl#R!g$;6YVADOW&iv8#z<a$_t`-F;#r-G9hNjt%{`z523rrVFECOu7MU@^CEZbVtu=juLTu*T<rlR>=~Vp~(Pvq<OXa6dz7kV@I2hGH)Mu
eYOKRzF<rm4wJ^-dcjI?o9&?LKFzA%8th$(jMIatsH@dHtGKM!Gl{Rk`$SvVCZ&T^KLG}B_z{s6a<ejic*YP14a%~<_b`lJ-QmVYFEO8WSUqn&u5DEVD&!l&
0lHq<8oXEDtfumJj;Xt-O)S=*AIEWu@dPTeKXDaB;DjaLx-qpJg5jh3yP3S%fm~qj$?F1og0D+CZD58<QVJyE0Qg*4#)^+C&BfA!P^Mt5nT+=fs;F6Ea<>i_
>7jwRR*HL!GsWESm}h<OTYNj!LMlySAhIe@Z$=I1;177u8E)1{Z?5TCs{*vj<mfQzv~p?OG+T@p|MYac$(4opv&8BA&uQJVssdLdgIbF*f;LbShBXG<CMi`1
^!Ij&xNu}4CU^2Wm6umRQr_6Cy8gzP+3txMYU?fboBz4{zSl60H&^Xld+~Sh_G`NHLOBG7yQ@6_8Y@hjiEfn4d{sOFuo?KHxkY`P+kCTEnF3o1a>GNiS;_@e
Bd^ODMCgPGFRCn0x4SANGB2tfljSTzGc$A2Jhi7Z&{*2+XHEHuA)@PHlPzkE0WteSI9l{}u`&c>Y+&pTIUZ^uAV>bI$5Rfq>JUYRV^b7M?(DJoDo@bvAJY7i
w+LelYBAC-^!0K*%I7+%d!xlZUBCi>#*9x8w5xMs(8L{50xq~|cf<-UIHyqjqst>tX4zVw?)whDjyALDT8PTPcwJ7>cgTby;m~hGIQ?fC>icb>Z6Kh%5-$#2
f*X52Hw(}&JES<~fcRwTf5U=S1WPL3K#>sT(NhtvkRtu(!L8|R#Z4Hq9cRl$=L0YP9-Q1AAP~DF{`3*MoN8)w;ak}QX3#C}cno`<rJH#Pt?dn~BOD-4k5E&~
)$g~KS4k7ZYtj8XRve0>cY&na%Ae}2X479~{ulEUgPbs2!8*q!@8Q=Vf(lz_5ax5lpxT2kgQ6A{C%3-*Q9r{KLZ<d|dsa%frkKDgLnQ#kFD!;gL#RDr^E^l|
^;gJy{IcEk;Nvs~#<c-LB17jisQY~Jso~pU3W4Bhe?XJuiPEA(8oF_w+(<~Ok$zR7xOB+ZGml*+YMs|iQ;=*@+~bNO9`%CT^(0oxHM@*(LdJXH;cq+Ooce9G
?7UI77}gena3o1KZfX-1hUtrgHSjzL;xCayO39TLz|9yZKfT|P#4ZQkYm6{)%QoLKqDPAB_fa81P~6rZ7;QjWWNA|2LK-Za*Smotz6@Wkk9%{dk$=cywIjQZ
o>I4Y76!FyB8K~@j4FC3Zix#?K(~OrP8ZXpbOs0qj27?2H|@ZNc8<OBWeJLa9+B{;4`4(Cl0sGCr*$yyxvUk?22Pbl?ppq;c+AYR+jYrS(}WnvEnM;cy1C0A
v=x5_`hKMvYYCZI^pH6w%Jzz<9B%s4b}gV5<(+Zt{39z~gtQErd71fo%JongUGJAEe}F9K794lf>Zbum4JnyMhu4dBUog8`wE3DS&`DwZg;eNfo6XrWBuCd)
#~Gs+!THz$vzqM(fNUZk!v|nHK1(i7eeq(4Tyzl75#P}Z&{bcmD0rdfA96?A-%IorI<Gp@Mx%yiwf5GeQSc7}o@RF1z-0V0n@eLB7pAW+Btp8pQ+wyKn0o^o
B4#wMZuGGGyEFf%-O0phN-R*xYm$?DPt%mZd`_kMgAn6m%1xEZsfl~4e~i^KaBMMYs6s#n(BaJL^hK;G3S4`=!PHp^odKUf(IfmmV~LKQW$#!%kDcC?yMbAJ
96G`#3N@4)FgE9P8j5(-ymf(OHf|5E9AG(4L;tNq{|jGDxXiGiBL|2*V({wVKoI9C`Ck=Ha(ffUsqHqxvjJ@NZfriZNYY&?sj^U>EpRCXuVwk7<^k#@YyD&i
oeu*hp)<7loi$p_7_~1AQa+<zT2KZ~ZfX7?C(s>#ukqG*6jloLyZ&6Jx?h1eJFO@d4B_l{8OXtrASLk5ZDCQ5BNzX(^Y<M_@u*uY1tx%hj%<eZ%sr^vH7yPB
qFMD&4QFu^l|#v{ptIDwJs2}k!YY*wj9+o|%nyip?O@DJDLivKx&<(dHkO0>Vjz;WjbgIb#JbRm=P;YmF7=+mnp3vXq9#Ztrezu1mMPH<_lUnT#fm)OBqCFh
nOAV-3Qt{gC^TJQSn~(5rc6A77td#AFlnwaz)N72yx0l+P6KOFsKa*6!d+q*%|`w2^Mb>>7=qSl=lZI}wYl0~BcP}XoMDWhLuI@*fRKbzUoxGGdQ`nixF?hm
>koP$ig?xjN&e>9Z;uQN9!a7rWw2_+x+RwX>Kl(P5sSBU8BxZ~I7RE1t)*AeRY0CJrK=YF1xSP|JgF0NM<7J*nT;txV{(t#9pUoKQO!6Y!Fy0Nta7-4lFf6J
bHFc19_WXZ9z9pfv@#L;E}4^?UZe-mkZ=F+js*5<fcPxnUXy`7Lj!%BmQawTTbh9De3%siW49!w`Re7K6O(&Nc4)MsNR?>DGzE8lfMjVJB<go0#<8Qed~jn>
gP2$|2bvg6WE8ZpIIGzpY{3RJyM*J6hCaO5jzH5<!MRg-Q6x7`KfJiD!G3Fll6v=kF$QrSL_MiXx^hYzGUo~R1W8)|C?k7=pg5;FoQ~mbl%I(PigqL@dy!I>
U|BO*4^u|3y|{=OaNHVe|2NqA9tm5?Y^ur&+D-@oHj^aMs#zJPNVgT2NJNU*xH3p08|J=!oZyAazU-kSY%>tcay-ad49l{()?Pd{c*5g^(g6ye@aTXeg7*+)
*ytQ*z+ZT@F&}uVSrvXnxH_Sr%&C0foq1J%L5TdlB8r@d9XR>A&3b{_XVY}qVTyxuBuHKxu3gtKd{DNDQLTxsY6@db+ul~;Q2)*<lJ-}_#bg2KN~9?8fv^aN
QGqiV*GH5^5~8mn%(7wT$Hm%S{XxA~QtWxWljJl${>QR;pyhx<HrQ!-Dp7LqXrsGB)P!r7l^LLggZ3jqQ|bPw<7@shBwvZ(-(P!im}I$ozo&_3^KRNtB-vM$
N9mTzORO+?M$UN5s8T{AO=!ph+VE;9qELaJ^ko%p6UBGx<`{PjuK)H>J2s_hr+A4U<9ae`VH}(A;udT@7759FUEiVJVntN&CSG*X?57SMaXQTZdlw{-A}jhc
$V<mdkuNA$3FHyb<WVzRV~56<$HGq0=mqoAFzUY(r)*1aiHPH=-UNsxV{z+&dje)k5(-*Abi09K`ot+B(Z*MQP8G&P9k^6Y(-kSM{L-rGJd~WPA_BFxXXGnq
@j17-EWIjC-R$4@#<%}7T)Z|R=g!_gt7FXnM=;k_yN6|L^tXuC*tM;Lw7M;kp|x>o{tHsGGe1VABvb`*>8}J{EKLDa8R{u7+sS_v|MMxw^K$n`-I~|hTa*qV
n=%%cJT7nEzeV2TXdW`swN3cL3_HrTYQP2B<Ex2QM)m!`pz7H7BE(z*BxWXDI*F6GazI~Hf>61>)^rcKfJq++)v-n~ym<A??N<QttaamvOzV=7(A4(Q{3R~3
)DrX<IYEk>O+0Q&B%<$#0^{IBrNXUSH9%>VkOQ147b@3T8GXp)JO~dAya7M_LQFoNLK^8+_kyR^RhshEF5k@QvzYL&o9-s&1bE#yluKs(z?xhuXh*K19!(=G
eL@beF>PknTr6{O^%Vm5kWN!++yTW}a0<<+g@>=$MQ`f6?4m|d2`76|szk;OttN=K%Dd?AXu1Yxi5#If3s{F(6##0Djadr-{aK6FG>Z9fS3AcMLuNctbx$A6
8|9Sh4KVhB6*zB+<wDdIFt9et?NZC=wK&JA@={;lE1m-~JuHXp8KSgz(UI9FodshL-b%Ny!Y4{iFSw8O8ee(H1N^GBJ#~UU-SzX<=V{ctFVF$zoHf?LByT~;
Syuq0Mf&|@r2!|bu1}`EsMF!2T!b8g;clC~38U@$;Y-DN8V&8CriGp<l7&MbY@cQ9ZrL7bwAZ|OEOWS}rj3qpr1W>7P}y_p<7p-b?Yaf=LExO=dZ6ddi#>xc
+G;9Wr`*~Ra<xqGwY57FVMSS-|9i~8n6wd;<@P|4H<XjLC#U01o+c=rx`+nZfbd;-Uu20n##j1M*)*l<>vEBpEbe&aqVKU_aMKFnGRMZdA{gBLEjBZpD<|xk
2%sCmY9LMXW1&nyeYJqdaV6-}1^TWkCLZ<0m*b&)Nqup(yNHQQK1g)2kUl}3tf`5gfWDOMu>IZt2M%JdE93)|$ikMrk3;&{mP$l7oDHyG<)bE}f2&+?-(x^Z
>TBfrp3GiQ&yLH7)NDaKuJQ$?_sT9k<YD@uvSsB=2Y5$4esmcrF4H|h0la<o^Xs#zSIq6-GDx;^5<=9+n?s7NU%FV8UKQ!XWG&O@TW*-<E8b41Meq(wiY~?i
)bZk(v^I#i86{s?WF!lM0eKa4j(ROb44zqH%fcbfuw{dAEWFzat9S|xs>LN@Pj~7rMTZ3Na8<J*V^9q!IDaU);m%HJ-lCR4o4dX_BJc1t<t@?DVOn45LXJRt
Vz!Al{8b4*>hn4roc&RM@ITG&2M+4V3xk9vB<@@bxl6_Rz@FekVo|TCqUK0xzDNPubYi3MzAdR#98=^^C{cIna1YYOhlVYx#u%ZXZTuRZTryiM&~Sa27-?Vv
t5PmcYR9GQOA33I3RvFT{bU5`(Y&G6g(=orp}L)Ef=Y4b{C)-%_q#MS(Lm3uT=Ef^<jt?oQ{C5A6{e(W#s*ozdsyD&Qlu($j62JluNA)Sp@b=y1o|hLh`MDu
>ELK@Dz9b~Bpsgvgzfo|%$@c+L!bU5O!cms&S>g1+lW3t%=fiIn)ug<k+&;esS@7UXp<s%A;}-I6J@TKVRJa43x-QWAy8TI!<PuQ*9v8}czT&HPhW#Tx}f!j
Ue@YpC+0P?%DevJlVzSVDG66PMSPO#rsIUKUXx<i3!U-(&F68KyV}SP6a>{;N(sxI636|_p~?62cn}UtU8Cw4BykCe*3`xXFwTm9p3T<Ds8YW5dU)tWY;m$Z
Q$J&v0*8;)2%OS^v0~P7#Ed`~9OB9Uo*ZJ0qygP=S%CluiNWDtbDDH`kBmSllu<Y&I}{B;>4C*=96LL^dZgmdpTLR8i~xh$Ylst@4Jki@zp#31t(qg+D6O~l
JE*~7t3BFO=*)*<sV<pwE6S)e=CQ2w9Z5oN;ZZCbD>mZ7!rUXjEGd4fPb`BvU}$zNNFX)@XtUCMoMTn5rER&G8JjquuuG`Myn(nNxR8tn2B}o|^FNZ0fJJmk
-#Ft|P=(Y_PZkET54~2?ffCPZmZp7BUoYG`j0<8hpB5_yDI;>D5a`@)V2(c~;BIVZ!clGcxUYLR_xAs7jeXVklSC@LPpP;m^_${$ndZk-n?KW~-j<ebJU~`<
k`EIn003mPd8+ZA@2aVPE;r?FEMBk^9QpxF;u9m*7=mzM-}k9UBQh#m@5Ir-vuGL)p$%pnpw7m_Z$lHyf({K^zy=xAvvC1edtCaJ4?u3InqeX$CKxIrZ51qu
G=vW*M}s3zc*(NSTr@Pbl+)`<@WsL?jD92A62-n9%B_`VPPH8)x9haiD1a8YO>RIi_REK_5+-LXdC?BOtY?3Pb3K|~0jy{qU|3DoP+RuP!>2WdcIN)bj?{X;
NHZ`|sZI0j^I7Vod<hIIb?tgiXL=&G5_`VqP|L%SZO_iic1|}~v>KWrCOMDH;g5ljJMQ(>bOUdBHgP=TI0j5k27+pccs?<FqQNt8*X@p9A^u>u@6p1>v&vfN
QUT63sk3rCIi~Q&E_v9!BB;JH@EVa)pF--fWHg!y{ISE1ZjOI2>kh0XJ7jC!tt<ayBog9;^+uoBdC-^aOpvWRt3fm~1JO;);!WgEPs3S^K7^O_=Nyp-exhAh
3WS(bXl>xF(fe?+KgdVM@MF1QXZ!CtB=&=vGYt%mGo+-yM(B^cZ*6?}z`<3x4-QlFHhderuHLyi2YI)*V3dQoCRDSKMx}PsQiN3CHAW2`sO}ZSd5H0cV`^SK
0})0Fbs&?$d!P7JmLusc1%pJw56<z(HU!4N<`ZVBKs_)kxV0LbbM%EMicflbTwHG<F~6D58W|jLsBenau~X1vBSN^!B1^BT;qLG&pYoVF9395FeT+lhrl}}q
oC)`Z78*&bm5Qy6MDB{?>~VVp2`7zFgK&T}r<!a)IS?)0u@8qM3m@C?ncJy)Og#~oIdmd61w_N3-61j}N&>1$$7gXN62^Iwu*37)!?&-Ua%v-6Q6u@I-C+E!
oQrV~ZzYdRUWY;7dDvhKS+Jw*O8v6emG~&CjM2U#RDP;Y{X1ElM995!GM;PlET3xnPh(^Nx1w=Iv5Sy2+5@<E<%C;@WKYgECKrF+d?%|sv>Y@&gBS2iH0W@w
3|-gqwk~RCLJ)nS5}n&MSv(5{fbbNQes+9sr){(q_os3Tpc-$@oQqQT*q3Comp!Gj7)ZQNsRlNSaa*zYpRX3<DZ9vmzV~-UTnWmpxN{-Cy-{@;F&>xWo3QfU
%E>dLW$!#vmxZV>y}WIX^qIa~VEOAS?50NqW9_0NcpX+}85W^8tTaR<2X|w&opaF+Y??S#(k}du&4Y!cN4o;&X3nKSj%H|L{oNDlG<$V}oG6x!UdAfUmu<C*
m<35YJ4ok@eo@f0ddDWbx>$7=0_}t4M4yKoS@y+5g*!iw!0H)vURxzAk8XZFch&~A*l_z(_R+w4_F8_=UJn(u5w`$BhU-P(P3n*vJ9!{{<D3Y5m?|5DkIa0|
7t`8-qqn*h#pdW~(u!yDno$u~eT|?GVtE_IV|1tJImw^vHc5a5)eBemIUYhU_~t4@sGhv$syEx9`LRJ;mn6QX7-w_w(U(rIGZK^G#=e%b@ogZ4RMPz%b#f*w
U?>DEj?rG@fvVsT0DVg_UpSIJcR?c5!msu?W-iY|zI^igG9UWjGti?+PS4c=ybAAA?^^>7aM!{z4baUm^KdNJ7B4?B1NQ6zFo2RXV%}eXm_rJ9S+0w`chRJC
IhlT^)?u9t?K36K{hfJ|HjLNY?!qi8BO^hqA*BK#`o^r^2^cUVzX>AGx(zbOPrjziILSu$Tn@QPb%+r_kD|S?*I>mf&8Vn%Lpb58lWS4v%~x~_g8`n_#TUfy
r9Rpi1{4oUkS3o(BcFV8myD%SPNDQ5&2a~z0K2<xkBY|=y+4>Tg{!3fxMM=4zFe;2uV_S2$ke1tRWo<&)S`0p2H5iGL?Qo4JG3-TV1wYTixN?|_Y9?LIOIMT
sL9a6u=(+mC^-OK2t7l4f9tSVFAXkx#5s3o8L%FuIW|_!5!M2#tHRNw$rM#)FP6(PQjKb^-WV^elXv}3)E})fG{7LaSZ${MYpa~(OeK`a+2h<Yt4!tHHI=#z
*dDmM3?4&}1pI@`{oCkcQ56{)VCUIS#h-T;N6$IFg5ceyUW+5Y{M~Hv-9iIska2O&GRR0^C=Y0>B=gj2_r)rUn2#oCL#YO<Oa0m6R9wu(P`l3;`J2G;jOlOY
g_**Ciu_{w8y}Q#8^vQ(+(HCaJE)R@VwNyzq838=%?G9Vd&e9>3e2Ze=$Z`xfB6CyiV_CS1N@v53j~`bHbN$BvVN3!T+WVutPV)f^dL2@>j=};rs%=5(7Wp;
Jci#Kr=LZi8G&c<YmE2<J9k}CAjY>7@Tu2>I!8G}GCap7Vs$`2w1?li-g_P`*|?<69-P&u!^d~?gr26`ab->=e}*?6l3RhaZZwV45}FUu)E(W(D896+mlEmY
)Kd0Tk&7sj1-S)KImud~DHRK@Rj+`*=YI~EOu^y^%k9=EA1d2kfGQ^2#aN=hViww}o0ONMs1_4T997M!JIjnrT0q0lSy&?SJk`VFaL|C20_s5JHa1u@)?{L_
_#inJN9*UGB(HK~gbd@4$|V*$%$?=1WzbgS9|GZhPuf&Sdu@SoO;fP&W?&yt@npVuCA|THhoYF7b9ea#OVb%qfL4f-F*2dM$2$}gFQ<hmEh<UJxMvW!9W^%o
QxdNJbl7LWPEWn%#OkDEKcz~HZ<tu+=}n(DH2sV_PM&{6*!Ms36_poH0pL&!34@%blq_p4z4TI!0$@7GQ`rWO#42Ie7=9D3{!_9->0c}ROPyF!(`3F;aCfMh
iyI+hn!q-cp)@Zf%t6!>3o6%y=%M45!CjKjU9~b(l4Z8`2=P3v<u2vEmj{E*4XA7R;3vY9X!d%I5t%2n(_YBaBHkA=X9lVlv!zrpO-JW&$?6aBqfn1YukeV@
um78S`ScE(zLBTrVc1<-j{B`37GACDjl!ZwLYNi>MDl2Jgi}9x<T0E*T2a<Hq|JGS3gwh^`2}GdIV42iJ(77@Bpq)N&PhhIFZPT=5_I_{`q4pKuBEmuqyinP
b{Z2zxx4DZZR{Yu*ESWQ)O&^9Q``GTvXO2>8e>QdM&O?hHz$9WH@(KD)!GE0&{5>q3Y!*vm%!n%Dc!5Jo~!w(dc^^4znAR12>)BsMDB7^8~*VXw2_+oW_)-f
^o?3fr5tm*(iEd_2bBKN0b*}Cyx0yf=N(54H<)^J6CZLo)|BUN|Es}qx)#1GB(K9%-E_`}Wklgs;U3p0es$}(@sJ2>2G14Q!L@m@Jnvmi1OoUk<~CS;pV*8z
;paOSKEb@MCOT+fn#QNJhpC~)>vUia(dz!EiEGT7;x~p?b5KICdH;69gb&)nN2>e@)&(8CeuLS1cW6XRolYscJyUnjWg|-ztzifsNHo=!p!Ym96I+6t{b_$3
t_{!Tf3fwfG$e%pX4V203Ogxx00F4k1HGaSw`)ZfvBYQl0ssI200dcD"""
def sha(x): return hashlib.sha256(x).hexdigest()
s=''.join(S.split())
assert len(s)==75775 and sha(s.encode())=='ddc8357e9c6dcd15158487c0f5d7b8465c82390e8b135bb49067e225378cee28'
z=base64.b85decode(s)
assert len(z)==60620 and sha(z)=='44251f26d457d138e4739a26901b6754414b7afe4507efe042ddfd209d7fdc0a'
b=lzma.decompress(z)
assert len(b)==233789 and sha(b)=='47cdc954a51819a417683c3528b1189fdedf6398bffeee6243cc21b6e6fb545f'
f=json.loads(b)
assert len(f)==58
p=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'nc22_compact')
p.mkdir(parents=True,exist_ok=True)
for name,text in f.items():
 assert pathlib.Path(name).name==name
 (p/name).write_bytes(text.encode('utf-8'))
m=json.loads(f['COMPACT_MANIFEST.json'])
for name,r in m.items():
 data=(p/name).read_bytes()
 assert len(data)==r['bytes'] and sha(data)==r['sha256'],name
print('NC22_COMPACT_SOURCE_RECOVERY_PASS',len(m))
```
