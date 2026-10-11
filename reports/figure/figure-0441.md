# figure-0441

Historical AI scientific report · saved 2026-09-20 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# Nimble Comet 21 — точные локальные препятствия для двух NC22-фронтиров

Branch `[internal-source-reference]`. Завершение по команде `finish`.

## Результат и граница выполненного

**Нового own110/weak000 тела нет. Новых физических тел в этом результате — 0.** В доступном рабочем каталоге не обнаружено post-NC22 checkpoint или журнала конечной деформации из прерванного хода. Поэтому не заявляю выполненный численный поиск, новые принятые шаги, плато или неудачу какого-либо геометрического семейства.

В этом завершении получен другой математический результат: **два точных, не зависящих от сохранения инцидентности локальных препятствия для отмены оставшегося полярного бассейна**. Для каждого исходного тела заново вычислены максимальный комплекс, настоящая заполненная масса, полный физический strict/weak census, оба полных положительных леса и все положительные elder-бары с путями и разрезами. Из единственного Q-бара выведена нижняя граница необходимого изменения ФИЗИЧЕСКОЙ опорной функции.

Это новая сертификация локального препятствия на неизменённых родителях, **не конечное продвижение формы**. Прежнее уменьшение TQ более чем на90.7% принадлежит literal parent `figure-0435`, а не настоящему завершению. :contentReference[oaicite:0]{index=0}

## Точный результат

Для родителя P и любого предлагаемого однородного полноразмерного выпуклого многогранника L положим K=P−c_P, K_L=L−c_L, где оба центра — собственные заполненные объёмные центры. Тогда:

| Точный родитель | Исключённый ЗАМКНУТЫЙ шар | Следствие для каждого L внутри шара |
|---|---|---|
| NC22_ROBUST_G5 | d_H(K,K_L)≤2847/100000=.02847 | Не менее двух строгих стабильных граней |
| NC22_MACRO_G8 | d_H(K,K_L)≤1397/50000=.02794 | Не менее двух строгих стабильных граней |

Следовательно, в каждом таком шаре нет own110. **На L не наложены ограничения на число вершин, граней или рёбер, прежние контакты, корни или сохранение старых владельцев.** Допустимо произвольное изменение однородной заполненной выпуклой формы внутри указанного расстояния. В частности, утверждение охватывает E≤310, но не ограничено этим бюджетом. Дополнительные слабые равновесия не нужны для препятствия: сохраняются именно два строгих S.

Радиусы выражены в единицах буквальных координат соответствующего входа. Они не предполагают независимой перенормировки размера каждого тела. При общем масштабировании координат радиус масштабируется тем же множителем.

Более точная необходимая граница задаётся формулой η=(1/√d−1/√b)/2, где b и d — точные squared-radius birth и merge единственного положительного Q-бара. Для любого L с единственной строгой стабильной гранью необходимо d_H(K,K_L)≥η. Вычислены включения:

- ROBUST: .028472297692 < η ≤ .028472297693.
- MACRO: .027948095454 < η ≤ .027948095455.

Ничего не утверждается о достижимости η, оптимальности этого препятствия или существовании own110 за его границей.

## Доказательство через физическую опорную функцию

Пусть h_K(u)=max_{x∈K}u·x для |u|=1, Q=K°. Так как0 лежит внутри K, h_K(u)>0 и ρ_Q(u)=1/h_K(u). Значит, сверхуровни ρ_Q² совпадают с подуровнями h_K после монотонной замены уровня r↦r^(−1/2). Поляр не заполняется заново и не центрируется по своему собственному объёмному центру.

Пусть положительный elder-бар Q имеет birth b, merge d, b>d>0. Между уровнями α=b^(−1/2) и β=d^(−1/2) у h_K существуют две разные подуровневые компоненты, каждая содержит точку со значением не больше α. У более старого максимума Q радиус не меньше радиуса младшего. Для многогранника связность радиальных сверхуровней восстанавливается по максимальным граням и истинным рёбрам: вне диска в плоскости выпуклой грани компоненты определяются внешними граничными дугами; на каждом ребре используется его точный минимум squared radius. Именно эти уровни проверены полными достигающими путями и разрезами, а не локальным знаком одной стрелки. Соответствующая истинно-рёберная постановка ранее зафиксирована в общем журнале. :contentReference[oaicite:1]{index=1}

Предположим ||h_K−h_{K_L}||∞≤ε и 2ε<β−α. Выберем t с α+2ε<t<β и две разные компоненты {h_K<t}, содержащие указанные точки. На границе замыкания каждой компоненты h_{K_L}≥t−ε; в её внутренней отмеченной точке h_{K_L}≤α+ε<t−ε. Поэтому минимум h_{K_L} на каждом компактном замыкании достигается внутри компоненты. Это два разных локальных минимума опорной функции.

Для полноразмерного выпуклого многогранника, содержащего0 внутри, каждый локальный минимум h на сфере соответствует строгой стабильной максимальной грани. Действительно, пусть F — грань контакта при нормали u, h=h(u)>0. Если hu не находится в относительной внутренности двумерной F, существует ненулевой касательный вектор v⊥u с max_{x∈F}v·x≤0. Для достаточно малого θ>0 вершины вне F ещё не могут максимизировать опору, и

h(cosθ·u+sinθ·v/|v|)=h cosθ+(sinθ/|v|)max_{x∈F}v·x<h.

Это противоречит локальному минимуму. Следовательно, F двумерна и её перпендикулярная проекция центра лежит строго внутри — строгий S. Наконец, для компактных выпуклых тел d_H(K,K_L)=||h_K−h_{K_L}||∞, что даёт утверждение.

**Рациональная проверка без округления радикалов.** Обозначим D=1/d, B=1/b. Для ε≥0 неравенство 2ε<√D−√B в точности эквивалентно двум рациональным строгим неравенствам:

q=D−B−4ε²>0; q²−16ε²B>0.

Оба положительных рациональных остатка сохранены полностью. Двоичный поиск целого числителя при знаменателе10^12 даёт указанные включения η. Случай точного равенства контролируется отдельно: D=4,B=1,ε=1/2 отвергается строгим тестом.

## Заново вычисленные комплексы, масса и равновесия

Оба входа — физические выпуклые оболочки59 буквальных целочисленных точек. Оба имеют58 экстремальных вершин,168 истинных рёбер,112 максимальных треугольных граней,C336. В каждом случае direct strict(S,U,H)=(2,1,1), additional weak(S,U,H)=(0,0,0), физический положительный лес имеет единственный корень и0положительных баров; полярный — два корня и1положительный бар.

**NC22_ROBUST_G5:** literal grid5900000, вход1612байт, SHA256 `e8736443506f04989db43d9cdad1e0706a3db208b3022e0a898a87f0f2dc5028`.

Vol(P)=540394962091699/1500000000000000.

c_P=(992129883877388603783,−5518424798984073502563,397844053588075844696)/51013284421456385600000.

**NC22_MACRO_G8:** literal grid5900000000, вход2146байт, SHA256 `4a8ac835b46f65cd536af7fed823e802ca8a80828b126f3d72b8ab8fd8971479`.

Vol(P)=1084503873361089164405039/3000000000000000000000000.

c_P=(1020077240696948820547218381364962,−5554386479712855750213659246030963,383213401729561131735746761128419)/51188582822643408559917840800000000.

СуффиксыG5/G8 не заменяют literal grid в определяющем JSON. Исторические raw-lex индексы и номера A-граней также не заменяют маркировку текущего проверяющего кода.

**Маркировка ниже:** физические вершины имеют индексы строк исходного V-входа; полярные вершины — индексы отсортированных примитивных целочисленных поддерживающих плоскостей в NC22_INDEPENDENT_V.py. Это другая маркировка того же тела, а не смена его корня.

| Родитель | Стабильные физические циклы | U input | H input | Q-корни | Q death-edge | Максимальные глубины лесов P/Q |
|---|---|---|---|---|---|---|
| ROBUST | [2,56,13]; [41,37,52] | 57 | [8,34] | 59,111 | [7,52] | 33/23 |
| MACRO | [2,56,13]; [41,37,53] | 57 | [8,34] | 61,111 | [20,62] | 33/23 |

Относительный полный Q-бар Δ_Q/R_Q² заново заключён в [149254512746,149254512747]/10^12 для ROBUST и [147822667952,147822667953]/10^12 для MACRO. Эти глубины остаются положительными. Различие η и относительной глубины отражает другую метрику, не новое уменьшение бассейна.

## Полное свидетельство главного ROBUST-бассейна

Бар peak59→older111, смерть на7–52. Достигающий путь:

[59,43,3,30,49,31,15,24,5,25,17,1,6,19,7,52,57,33,36,71,98,96,103,90,95,111].

Вся33-вершинная компонента строгого сверхуровня смерти:

[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,24,25,27,28,29,30,31,42,43,49,55,59,62].

Все33пересекающих истинных Q-ребра:

[[0,63],[1,21],[2,106],[3,108],[4,86],[5,77],[6,82],[7,40],[7,52],[8,23],[8,38],[9,107],[10,73],[11,74],[12,101],[13,102],[14,88],[15,72],[17,69],[18,34],[19,44],[20,41],[24,64],[25,82],[27,76],[28,81],[29,97],[31,78],[34,59],[42,80],[43,88],[55,105],[62,73]].

На каждом пересекающем ребре минимум squared radius≤d; минимум вдоль указанного пути в точности d. Старший корень вне компоненты. Все эти сравнения рациональные. Для MACRO также выданы полный33-вершинный компонент, все33ребра разреза и достигающий путь; их полный детерминированный producer включён ниже. Оба выхода содержат ВСЕ физические и полярные точки, радиусы, минимумы рёбер, родителей, конечные корни, глубины и положительные бары — не только перечисленные здесь пути.

## Проверка, воспроизводимость и пределы

Использован один полный точный механический проверяющий код из родительской независимой V-реализации: перебор всех поддерживающих троек, максимальные плоские оболочки, двусторонняя инцидентность истинных рёбер, links/Euler, положительная заполненная интеграция от внутреннего якоря, прямые S/U и все условия смешанного нормального конуса H, включая дополнительные слабые случаи. Каждый родитель имеет112положительных якорных тетраэдров.

В этом результате добавлена независимо записанная трёхосевая граничная интеграция объёма и первых моментов. Для каждой из трёх осей она в точности совпала с якорной массой и настоящим центром. Это независимая проверка интегрирования, **не второй свежий полный механический аудитор**. Полярные корни дополнительно сопоставлены с физическими стабильными гранями по точным инцидентностям.

Контроли исполнены: тетраэдр strict446/weak000; призма strict446/weak123; строгий радикальный тест по обе стороны и на точной границе. Два родителя и оба сертификата затем полностью восстановлены в новом пустом каталоге, и все3ожидаемых выходных файла совпали по байтам и SHA256. Исторический95-выходный NC22 replay и его численные кампании в этом завершении не повторялись.

Новый журнал1426строк, включая literal parent, прочитан через EOF. Его родительский envelope99998байт с SHA256 `1aab00a915c988e42a312b576321e13404c59c98641d45136219d92186660865` воспроизводится как compact JSON version2/result_markdown с конечным переводом строки внутри result_markdown. Это не тот же файл, что более крупный дополнительный NC22_RESULT.json207878байт. Конфликта определяющих тел не установлено.

**Область незнания:** нет нового результата о существовании110; нет исключения всего нелинейного или аффинного семейства; нет оценки достижимого бюджетаE при конкретной новой операции; нет сертификата непрерывного пути. Полученное препятствие не превращает прерванный запуск в доказательство невозможности.

## Следующий содержательный вопрос

Следующий конечный опыт должен изменять собственно центрированную физическую опорную функцию достаточно, чтобы выйти из доказанного шара, и одновременно контролировать весь33-вершинный Q-бассейн и все физические максимумы. Не обязательно двигать старые стабильные владельцы или только death-edge; большая перестройка массы, новый контакт и замена корня остаются разрешены. Необходимое sup-изменение не задаёт достаточную операцию и не указывает, где именно следует переместить материал.

Точными стартами остаются NC22_ROBUST_G5 и отличное NC22_MACRO_G8. Оба полностью входят в новую малую капсулу. Для ROBUST явное удаление неэкстремального input46 сохраняет исходное тело и оставляет58-вершинное описание; ещё47входных точек укладываются в достаточный V≤105⇒E≤309 бюджет. Это известный запас архитектуры, не новый конструктивный результат. :contentReference[oaicite:2]{index=2}

## Самодостаточная капсула нового результата

Код ниже восстанавливает6текстовых файлов: два полных V-входа, NC22_INDEPENDENT_V.py, новый NC23_SUPPORT_GATE.py, EXPECTED.json и MANIFEST.json. Он не требует старого sandbox, исходного большого NC22 recovery, NumPy, SciPy, сети или внешнего родителя. Все новые вычисления — целые числа/Fraction; RNG отсутствует. Исполненная среда CPython3.13.5; assertions включены.

Сохранить код как RECOVER_NC23_SUPPORT_GATES.py и выполнить:

    python -B -S RECOVER_NC23_SUPPORT_GATES.py nc23_replay

Наблюдённые terminal markers:

    NC23_SUPPORT_GATE_SOURCE_RECOVERY_PASS 6
    NC23_TWO_PARENT_EXACT_SUPPORT_BARRIER_GATES_PASS 3493 bbad3b97cdacf314936f52dcfdb2b1464d59c09f9ef841c19d87c94956e97243
    NC23_SOURCE_ONLY_TWO_SUPPORT_GATES_COLD_PASS 3

Точные выходы:

| Файл | Байты | SHA256 |
|---|---:|---|
| NC22_ROBUST_G5_SUPPORT_GATE.json | 101034 | 3a9bddc36c05f419dd02b0ae53a7ef5c5f305ee8ea874b503548891b3b2deead |
| NC22_MACRO_G8_SUPPORT_GATE.json | 153642 | 2063d9cc6f80faeaf67eb8321d130e425d9c4fcde6d2f27f417e677c6043c090 |
| NC23_SUPPORT_GATES_RECEIPT.json | 3493 | bbad3b97cdacf314936f52dcfdb2b1464d59c09f9ef841c19d87c94956e97243 |

Новый NC23_SUPPORT_GATE.py8264байта SHA256 `18cce762dba2ab6c8b72ecdbd6b67889f650f16f07212c8cd0d9abceaa164b64`. Полный recovery11149байт SHA256 `ba243894559ba4dd4ce2c71b5e4d549375faa6501eaff799fe6985e174967bf9`. Дополнительные удобные копии: [recovery](sandbox:/mnt/data/RECOVER_NC23_SUPPORT_GATES.py), [полные исходники ZIP](sandbox:/mnt/data/NC23_SUPPORT_GATE_SOURCE.zip). ZIP9363байта SHA256 `e1c7707789d6968e3a67eb295acb2e09020bd163fb6686aaf4aa39ba5054426e`.

```python
# Self-contained exact NC23 support-gate replay. CPython standard library only.
import base64,hashlib,json,lzma,pathlib,subprocess,sys
S=r"""{Wp48S^xk9=GL@E0stWa8~^|S5YJf5;7N2IPF(;!h=iqrocag;lg9zQDdLTm8Uv={r_qpY^vT(b-g)Oys<M<YeggnYUuE)@n`pw1
sp-h}u9T}nw_`&qQopL_PF9Nsu*KP`BqDH>y9B>|lnTi&a8){rCTFl=WxoDGqSv>A3sJ_{^<NmPdkp$k+eRJZ&N}58+v&=;*}DkW
rFv`U>Iq565bV4r+$Ap+mI5nalW3pz0TaC4;*fqr7YE`YoE{xq+5~$Svd6Iz)ULZ$+C`71&-tStZJxmfH17|TX7V75b0c}o`=KZ`
+cyV$htCUOsPW963hLrnIWjLqG^Bg$4ZTD-?H+{rEd(Vg?nkX)wwdV7MOf@0Gnf$rK)G;C7{+@_0!8oOu}xp&<G3d24@tPOKq+Jt
-KzPUsK7Mx7hZT~m{W6o&G?dzg-s_89}<1$aPZxrk$0YI%FE*-U$Zd%jm24|^1VHovcP&f<*o~Wy?JLR{Fz^n9s$6@JX}?ILV6`T
jKp{?N>trouo&gx8}-J&lH8~C@6s%+_b|pEatfe|ZN4sXDC1tpR2c#DKrp16uBcU@A`?lfzWIE1*@=d`oVm*-iwZ^=*5L&o%S^Vn
h@EiQN>^e35bZ2cYdu-<6Sco34+62?*%A<MAx|hH;I<<!HR}y<c+^vxF*Z(?2sXMbQvY_6@_svFbYH&kVs>7+gZT)7J<S%SXC@c+
YhGA=1=ga!iiUL;llH#{lid;!ns+vGJ)7y96CH|ogDnTuMQo9rAbyEMXi>vtWyq#s`f4n$wSm>9pfmGd_~D>qq<*WJ$)$Os+(1t9
E`80F>RiYc=Xc^#vw^F##xo3CeIB^iMtSk)av2#eC4`>YC5<{p5^(4kU)iE(Hy;rbXezgG2gmC??M*<1-yN{0(yCCUMg!4ViP!ka
>mN*fz+TOAl)9WXiL<E2OAenM%tm(ni-41pvE3Bj97<62wwUgtkl^xXXBF3V{y4|ao)a;Y3ISZnJCd0u2G?7i95d1a|I{UB_mnn%
&4vTHh+|OUpS$HVBXcFb?VB6hwmz%RUDKY4Y{t+`_zYo_P`tG0lMEX&U{N7uW@za@pmD9onT<#9N&4arjrWpmOfzclGB#}nXkQeZ
1}cr_B%za&{e8RLr55&a4~{LLwE#MPa`$*F7tHMD{%M5@(%YRku@S&XAVbPg01;ILN~ElJJ3>?+!nRM`OOK*C<!7g<Z6ptYU$WG9
xuA>O6mHq}XIOFYgoPvmq8oxjd7|svw*`@)hNv-ira4Ljo$%8^(hbEaPumKqnkUMupAy;Q2Jrl+H~WI9@p#VMaUYYRu;Z%mLz$4*
2;F^Gzg{0-GhCDqo7QpsD|N!kT4}FGfck8<6-#WTN<0*)-@y3q{7)|kTVKT82ujalcIfqXyrj>JgJDhXT=@L2j{_2JUJCNqbw+db
ps#q{jld7!;PE-nlv<>@L=cdg^@Azbx+IEFy7uL7R%ZyR1)H<S9LDH8K8rEW<cj+;#f~02^EYeX3p~PwIzw%#f}^*tsIN>pwHzU1
5dmAs+k+r-y}DbyEaf(HY!w0x9%3qgQ$}zq6NHpq^6*TT?qE@GsVjQ=FU#hyRv*tZdO|bNK-6c_!lrEI1PBUfEbY`)ic?a467Kmm
>q`2Wo1A&<kfFNF8ePFGa%MWRDwq9uJ$Fr9gAOSWu$jtLM$**2M<!>mssh-i7VbYU?Sy>!*{%%|w0G}`(|R9nZ2|zP_jGb8b(&0s
aVETkqzSVFkOwvHOUcpja~23y!q-Q}`I0VWE+^3;9Zd~<0Jn-IL@YlEhE;Oa{I~;rwl@n4;y}ZY%PDt9d`bHZ3hB^3qp_lkZb7tu
hdYE<@8Bdy*8PGBcG6Ffqyni?6KI#IORpOS=*BT2vK$Ux*Du8{H~oZZG9!L5$3xe;m(AM_UP-}x<vwCLK4CUG7Rg}uoWj!7+78E4
=tE^lW1G({2$M$g0H0ukMhkF!A}84lk7F%W8psBMKd479dL!lc;#0l;I_3|m)#+tCyhermBv-YZ8HGmC5d{>r@AqA{yf7h1P|3b*
wdkmDP0t1_?x7eR%t)2_<CbRjam%Isb$gN0I~802;?qQ74`cvc$iwz552TzIGP+$~+zqoI*`X9VTTxeA@v}v1iWuxn0^fC~lK(?N
^4g_ju2BgSVQ#b=7k{TeA}h6kpTSMIFsR6W&SW;j1~1m}_s|(Vhg&2HkEF&ZqP4^*f~S;@UeMwkdp;Pe<UTdAM+1q?Z!!sJ6Kks-
T&x`sw;q&)aA?TlZs>d+Qz%5Uc8!n})G7%My{5SkcD!Upoe$n>NF&U7X(|qqN*a9vb!xC+K(4`|-L)QphNf!Y5<FI!tmL*}EczI~
gPR<Tcg8V_F*>P>Nkr`QdA~#=9J}bWK^@qIbl+$gM`~j2$Fge(xjMM>d`tNtlw;Qi&3G7#9<ZTqNl>8N^eG0bUtidvGC)N&vFQP=
3qK;2Neyj-A~lGH2FpX-0GroyJPMWR;k_=9W7<5f#GWy<;Xwp;@)Jrsy}`w8?s`OmBpUbzNViN4Uf7Pb-eX&gARTgOm1S>J2+w8L
j(mVE8#lNzLJ1z{$VtPd6*-cs3rGZ^4_D!6*uJ{@@T{(NjJy9{?l|y5{=$qIWTPwk{#3J&%4`J-HBW`!iuiLhP7lwohDYB*6z6?Y
u%~SYN*y+J52Gae?g*9eA@O3wco2Md-}YhdnM-BT@P`WuNA3Z0jkO8K*prpHtBW4w$IqAKTzOjitrerk6eL^efnQ=$&u<WX$<hm(
CazvOip!`KiiPQ%om+*w{kv=2{%uhab(ONn1rQti1XI@yNGR6=m10O}TxBpI^@yPJ$YsG;VcS)2qYWd(E$vf@?=t9fsX@t+b&~1&
3pL#F3nr2P1y9{)jbdE{a|A+HoPVzi87t}uT;#JY!<ed!Z*!pFhFfkhB#n;n(<;XIycnrG0-r<1RG>i*7L@cGyJyvec(UAD{JV?L
8k8)q!dNBlQd||p%+mjvjovx=4o1W}dyj^2sN1BXCs-`4bLfd`BUe0mae`D@bxBrO<CyV1%uk93h{@O$a$>}`>!5;Sn`iZSI7#tr
0KBCoHs6i!ijaC}tJ29Qm;`)*-Ck4Xp(;430sI@Gf%KAv91sqI*+yo017pg^$Ok$!i-;HcsAeJ2!3rM>)_>%Qx~BI{1vw8PfPYzk
j^!UCc3^o5;x58KuF!g2zNc9%U5mq3R8$#Vq{CVF<B7mB`$y31*!nUEZHlVI0d)?WU#<12zPE04i%G&+`*lXU7!v1!{?p6sSpXMg
HAuVFPRVh*NG0QH_H<a7mLgd$%7AobnrwO$^ztIea)>oLw~F>T9x93;x|2ykqxC|41uco$Nj%}4$b9$baHp|+63^!66mwBnNi&g&
ol7<T(see0B`GlQK;4~Te8G@g<W*F|&o~93KkFhGcp1tv3+*0Y53!Le5r?~!kE0h5jX7e_hT1~gVLCHKuvjL%uiiN*za>5(TMn=a
GkjDbgEX;Ij#T<Dwh^EI^M*rX=>DjRs(%SixoBe$@XYPp|BE597~+!#t?H2C(<zYH%XI;TrzvJ@<mPm-+lU~Q#=-e&Zx2vNR^AsO
u2Xg;&{S?icg4Zu8@Zd{ZxaLQ<qupsi&EG#>UGk4NG|F^<-A!u@Y?WEe1h4Q2L<L@%yc+x$6gQ)7LNrLZ;iXK7UDg$HF1r4erzFs
Z1VA1M-=z5I@Yxt$2-^L!8$6Xq)caYqt1VH0t{}v+?WC?57*&z&47rf4?IF6OJ+EfaL?kHr(%zFCxW;l7@uOFYBW`FftDGH3(F>{
DZ{h1=enT*;#qxJAJ%<`lUNdZlM0SlNT3U*y41`&UieB1_!XiiW>x34M1!+?;&DId^N1S;b|m>H5&b@1-@YiiVHHP4riei0kkO^*
d&C|Aw)SLra@n?40kWeWQMWUR)>BoZ3cZsjpc%T<-3Wzt5j6<m=SX}^`JJC;?lscZzZmDx&6M*Li3&U_oeB)c8jB3%`&md94uTjl
<-4j}w+7R*g3JJ-$Op+qGn&G;oEP_vh=S8PCaYG~!lr)bv2DC?`!4_+_sZYSozpeP$^D`A(Wj~f-P~O#Z+5GqCS_f<UNXZ)&GSSg
=&XQOXw`rGdKfb0Y34&XJ7S}3qA7OHg|&MQR+{Rv1<w(&r&tRpdw-WpIK0C6u7?+zAT|4K;6xhFM$gUqD>|wa`jN)$L^tZ<!Gc1n
o=LELaqWS%1gavqNO@y>ynCcBkS@?)i*T7q0(Zz8H_22@st!;P=?2y7PWKgnvRVL!oI5<jz@TCJy^VH=zy`Jr$A8;3<FSo=0GBgv
|EnKjivGD|A0yW0?<K(5t*(dvub9SK2fBV}7j(HKSJ+b{9U0QZ7l`|WP>Y~gC@r^coUI<i6rM-aberB!U4$8xv2NxVod4kZKC#I)
9^C0P2t@SyW#p#;nD1>t=u7YDY3js=*_vi!1JK}4fyo<I%@wZLyO8U9-Fw2O4rLe1(adRkNcha>6kt|{>qu?|A6cj?p4CD6dnuJ^
!2)MQM27}A`Eb!K?Q>t0^iF7-UqCNgqZ2+rF7Iwm`yB_x-;A1E>W*Wb2S23H%^EBmi>!M#_|k+uwUL^YLe+e^GW42!7Arjy!vi!A
B}P3H2r%wZJISqo2QC{X(phJ%>)pgXrzOhu0(Q@B$7Sr!?{Ym8;5^DHzw$Go7iHe#?`lV^<(rleVWEPmu?xSgCmyYLE@-<2+`snt
tlX}KYqCiSliVrH&TR&mdf_l0gGDyb$WUBD<gCuKn$5pPjRi&|8-pPSrwfmeX#wLxmGqC0wh*N5nc*Z=U{Tyr8iof>ZD(#b_c=#n
hLf{ma5fbe`^^KC-7fK8pRVYS38AB5IeRWp%oE}N4uM#o!PY3>ld=ti{OQ00hcG5a<qfoc>X&m<aY-Pp)&1lPcv+|)b}$~vYgb_r
Zqrxez2%XcIGI1fx1u~z57)7GEfJ|~C{c9&_7(K(Y8%G3Mw6WZrgI&MVQCD3^Qt0ajhDkK>sk&(4)1zX^kq}8L9j4r`04JvXQ@VO
o3?DuhP8XnM>G|u#NgTe;t+-!q3MN*;ap2u@e7xsr#?TnNJnEFIEb6#U_5l1@jOvBM?efz)Z~Q~3JA^^x8_1>UFovCGTC~Uq~tnS
bsk7?^^DE8XUrNpdJFx_1V1!|CcFJ!q>FYzZSw=MAFk}X^W`sDAcjV7zW%IVLY*nx;~BvATbg|drOd3hMSmTY8426-8ql!dd=&pm
?^PBFL%j>3UsiO!8$~GB5LAV7w)0W3n%FT26l*{N^)y4FBr)xkdoh)H;dTD~O+-(shmzS->V_oFU7|x+UX0!FR$z;x6A>i5*k*>p
OanKM#%x!sh&ykAvbm-ScOs?`b^yta)Fpu%Q54v1CPZe9B2)idi}sYdZa1%k9#2oiZw{xn^l0FHz$0Frff6zJi$oLtAU3D*tPW*f
07l#V4z~Xo31y!)1u4PgwPqc#V@Y)w4=^ftYdelSQ0E~y#b#(4n)SJ;+4#$X)p(#r;XIz+&b9X${8qY`&?z?$lT^ZGZlb%$T~nm%
D6KvrzEYj-+Nl=-Y)F=VBSNlP9SBIL!RbxY1{a6q@u2SIaa~P_|MLjE$zh43t>WQD#{dSTiR}jwgr)eyl{W4^Vl;iGa-MPvn0DMV
4CXelCTjuyPL#VpbqH?Y6I6qu`jPTL5O7){aOl^Nb?)D|pE%<Eq9%kxnd=bwBj#+)6&O=`xo|GRt}nwwmjOg{9d7y*!B4BSBe|Qv
C?9j3N&~2wTp%EhLx_Fz0)i)W(Cnnz?%LoQCNgOaH}D-v=B`i3X^d;lDQ70EgPve1?$OmuN5PWpnkEDTq3BTUB`TP4?~&J@Api-0
f->tnU_eZk1d#k&eK1^dL4G@0kJx|k>fIVD1Y;9QQk_PZC5lw#t-C9{_!&Eg0uVP$;X#zI=J+&{D*qG2i6zKYeFImAGgyU-xVqLc
PN<5DA&Dq+PEm*i3~FrMP5$$-su-9l_J4~CDBjz?<BX(1MyT91dRJDFu0g91rjFZZ8DL{11jg9L49zSni<#mhnn?fzjIpwIyQ|=x
y{s?b5ZkIKl^gZCD}W(bmBE&`A7uh+ZGk|8?Q7I0;G*<TcB`LdK)H@C@~qwL$|{k&p>H%%l#$;N_5ydy@l#rh{{66&o2sOlr%Q1$
>MH(EGBZB8#Ftz{Eu?CdlM=>EvQTOusJ(&g*g5CDu9+;o<`fKS=qrmH8^+seL!$Mujf(Xx<U&fN7^SDkmarfxrvmW#jVBY04p7wq
?18$Qo38}k4ITF`OJ1iuN_rw|zdKNuNy?)(eL%^-5UnC0f!l)%NGS9KImX9f>iEaJ2^0i8-l5(&l*zjygrLq^IR+p0nfKAnlzy>`
fwQDhQ*b*<XAk!k60{KTYy4>u`n{uoYu-__U4=4nc~x7qK|xUBaMAUmS0rOtDw0Zhi>fx=i0$JpRbUN{ZtSxrNNAsl4aP(ff1Qc{
LVeXV_4VoMoFNaT#z_=^c*I_xdZgqVMdvR6?jK5gF`Ci*x4N9qzIggorwd}(!wf`zV5f($WLR%7M)h+I`fBTJ;BcL8udZ7$@n60&
4G)g4#m24yGEbk!^LTRAGoYPjSZxV_I8otj;C0Y!DP4>A(8_T4cN}O^1c~Y`RX0m~2+~^k`!lGsE~Tqp-ncY9NBNs|kWX=0L#E{r
Vl&Jx`jg-g0zV_X5&5%%sd}j{2$h<+0v*N8VGYpFN3ioOfT6=Q5#`zj1qB8~B?6<8p$L~CQ4oeAXO}fH1#>bj_izvMz-XhIW=6tp
FlzS|y)ijC_mf8pvH@}R^;-1~E6y!hwrf*&tBG&>$<R#kL&IHWJdJ~-%g#1BaL(ZN@F@QK3%J@?x{m+%i%dZ-PmyI;Y@Bp$HBdxm
6!~=p*}NpG_t^5qhKRyi_3uF<zj@-jnDPmD$kuw$6N-66f5P+kHoGzXU!=wTJ}o_+90F`@Vd|uqBB!swBM?L4nT62vIxW8=Dv>Z4
q8&RuxhvIbKOGP%X%-)D4k~@UlF38Nq5wN`C=Pgb6cSUX%Nxy=9tynP?@RpR<pu;IVva)<N*_)|>po+)^3^N+h&+lP%V|0{cP!~<
l|>IemzORsi1^CK#h0*GX(YPK_LV>Vohw;RQh;(m6vS{YcShKs_0Q2cU2MBqU2{}D#BM{*(?XZkBJ}2(?$&XTh@_0&Skf!R2$#$#
*J2M7*>;vy487+eYy)JHzeEov6)Fy_d}+uw&wiZL)YK#{ey-)ESz(k@b-&2_S(4I#@56-NW}4o63)vcI<I41S>{<OfKf6%{O~ofW
`kO0%QkRG-VQ(}tC%YSa9Z}%dg-s+VY{Qces~O5E=_yGX-NW&&HT+>1&`bl?8B7@)Z{*x8+yf?yfNQL2g(caiez3bbqy6D|_w3AC
sn^~QJL{oWZkS^seKn3i*x*h{os)g9`dKcIMLi-`XNvA3k$B5J9>w+VQOHuc?7`4H08DxQ@R^1NnlvStS(WOV>WVe6IFQ^wEe*@r
pq3#bCI_x1FZ<A>6H2+Y5m9_%2h&G%ZO{PLvWhsB1#_c{vF5i@kp9?u;b>G`o6w=uR&iX>-)5mZiMH>;d~Whx$|`NZq(K{qFuh>F
TX(fO#x$$uDIr(Kgq~^Q{>7qj;3uf|QprklEdjru$qWffn&@l9HYL>Kue_%r2W7(7q_ZR#b%P6Ax#DW$uCGo1sr;UKH68gZ%CkbL
3KrSA1mn29J3%%cV9yMbHr}r7pTEN&8+-$#=G03D7=66Gx2UGvPX(#~aC@=;HlUV9BhPYC+~`mac8LT^nFII7HbB>ch!jqIDn&RB
3uzts78&~n2Yw01<?-}<uBe*jca=8t5|DqO-pA+5E=c8cniLsNiPEpBIOgAQ8T)@sdU4y|pTNd{o!JmlLd1{J@t(-C+sEyf9yJMp
J4V-n=7oeS%=FKfBll4>)boXNL$?v(V($>=j~zO6AR}#0MU}l)EOyEKf9@Zt@dW&%dfbD4e7W(YXD&$#01FNTWZ8yTu!{7TrdI<C
rQ(7|dHR4aYxEwBPCEi$+zmEHe;X>8zR>9M#!sSmi-w@W$owBIXWc1cjRb5>p6oHQHG_c09V6-pD^QvPn7*<ky$_z4<FeyUOP`-^
cQ0w9kp{5Ipq4W`&Q69tmPyhmEAp~etuuyGYRd0;li+a%{K4T!c_jmxh~fa^E>+1VctYq?u91b;QNJ`#gm^}uC5X*gtu07g2~ADQ
Fhq=YL~kb&_YX;*HdZU_KYRWY(ZH?-oh6#Or%0sZ3Wwp%Gt@k^g4)EtftBlFQH&V4u(2%948JpA08C@7qZh?a8Pt>hvS7^^^#*Kd
vf@Z7*6vtN>4F6N5@_0Sq5)P0W9~%9kW7s#G)Q9t(N_%feTrG^ef1ioV8XQGk*(`MvvRC|(V}3WP`+wNh;sD7O;_B$KlwZ`kDduH
My%2DQSM>F>n*fP3J>ZHEkE0ty<iVd$_WB7CP$vhhS<GPsrlt6YfwrxQGXZ32$Y2OLV5?I{>PH@rZGviHPs+UM&Z}!t-hXzVwng<
AvR_i2$CRBl@vyxxS*LRqRLo6P@t@<P2`)QKIu;N6be}#q4PE1v_I_}Fe78SD))<x7qGLc*&fti^$<{ACyS*xes=QtFC?XoAOfs5
8P9lE6T#xN0m-~>8r3^`@E4Z9444-j=iXdHKH|#&u#)uof9Ny>&Q6jL+JEMKSQ1==vT!b8dq0B0?VSz;^zX^Q>B!0;H6jN)jo<{`
r6<YQO%GmQGKRHTr!dCRi@nUeBEBV(dBE<#68h!`D;R;KWkU}k3W~9rZcg%Ipiy!(>E7aIv(Lk9I+Sicjlvv#xDb(L&?HvJ5}5v?
&Y=7elAfQz=2);=-dViT9+kp5J>gLg3rl3><zrb3TCG5W;3FxCaCRaL$e7#6z97ngpEwjg4fp8=rdy{&hK%F*p>703nBb<?3pr!7
e?aE-{vhrDl1aB6fSPKXIRdcU(xlV~V1$hT*qF^5nKb>N?<5GWGm0rmF{oTP7*Tk{Z|<ebe$6@NHTNy1fx8n|Uf9W!{peQPz!!wR
4=>E{h6I<vhm+d1(VqV~cFyqwbEV%-yTsBE7e@R*ISGIhsR?p|SYB|8hS?VS=WTJjw@yL~Gj;egi34~)yKo?=$-;G%DFb`iB;TI1
^XX&OpB-|pVUd5`$LIP*uqm(9gF^f~{k6VqKBU*=Ojj>q9-LzO-m9mhBV+m(k_dOCwR&F72%_Vo=Mk{?A6MQA6Xzp%m1QAGO|MxP
>H7Vi&Mxxca*lcTLcY<emcb_mWwG$E!K{2kZq^M{^iu?B^R`fbC31f4^GVpIsjdU$7NT5L^m`KAtH~I2k<}QQE?6i^(#XzBD?+e_
C>uW57mKj=hh+ZZf8z!&=~2((UxwFD+bqhE_|Bkfb6}kg3qDqx&ekquJ0}8MX%wx%;JWC~9W7;R@UR8n#KL|iG94C5Wun9NZBT)w
P<FFTf_n<?#yg;umgBe5!1hGXlAjleEn2Pwahj1dm~v*n$-#G6^`FLTaM6IIi`xHP+0Pfq7-4!^lxsu!<3wpw4EC7G9+^b>Pq1YV
RN)f)LY5?+Tx904r|oaS@Q%Q`Z5ZQ$EV<uB1Tg*A9Gk_k1v!sDDfR{>#!!rF4MU7<A)FY=_+(}&C6CR?_fr%H9mQu4?&-JvA@Ew%
`eiSbanWsU7?<lSa1d*}kzKHN%B=cAFe)`~1K?)h>`?fZu;Z``JH<6=<~TVbpW52-zT-RhH(RGUs3-^$_9*U{Q0qVlgZKk7-PiIe
U2=WSFZLN4?a_>`8crrHNOUGcLV&AS+Uh^FV~KFCte*Zbb<~X8kH=i>A@0XbXj~3msovr9JXJ#D{spZ~D4WLJdUc|;_gSZWTXG0}
|DLVQX^}~e8z*E4bC*$Yn{{bPxzRIXOSPaV%5THj)9h>H-X1x|R(ICeDBL9I6d7wSbx~IFfe{->j5IO$K{J8XJH2XWK>`R7FIqwt
;Y^qZ&{#YrEvj=W0|)8hU0rmjC@11AGa~8Tw*UYDT!_oG2y8Iz00HVe^^ySq^a5{2vBYQl0ssI200dcD"""
def sha(b): return hashlib.sha256(b).hexdigest()
s=''.join(S.split())
assert len(s)==9780 and sha(s.encode())=='3aa1eda27b6ec52ff477c6f064e25c81014fd27f345322aebb1de3983c36db4f'
z=base64.b85decode(s)
assert len(z)==7824 and sha(z)=='9ba83d25bdf27bf9936f0516a1d2dcb4864b91695e1f45dbea1809bb3961860d'
b=lzma.decompress(z)
assert len(b)==18805 and sha(b)=='88bf80ae7516194f340c98f758cb6188fd3ac17606bb7ddbf279da74165642c4'
f=json.loads(b);assert len(f)==6
p=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'nc23_support_replay')
p.mkdir(parents=True,exist_ok=True)
for n,t in f.items():
 assert pathlib.Path(n).name==n
 (p/n).write_bytes(t.encode())
for n,m in json.loads(f['MANIFEST.json']).items():
 x=(p/n).read_bytes()
 assert len(x)==m['bytes'] and sha(x)==m['sha256'],n
print('NC23_SUPPORT_GATE_SOURCE_RECOVERY_PASS',len(f),flush=True)
subprocess.run([sys.executable,'-B','-S',str((p/'NC23_SUPPORT_GATE.py').resolve())],check=True)
e=json.loads(f['EXPECTED.json'])
for n,m in e.items():
 x=(p/n).read_bytes()
 assert len(x)==m['bytes'] and sha(x)==m['sha256'],n
print('NC23_SOURCE_ONLY_TWO_SUPPORT_GATES_COLD_PASS',len(e))
```
