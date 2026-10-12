# figure-0416

AI research report · 2026-09-19 UTC

---

# Quiet Atlas 74 — точный физический cut C366 и граница завершения

## 1. Статус результата

**Нового own110/weak000 тела не получено. Конечная деформация C366 в этом выполнении не была построена.** Результат не заменяет C622 и не является новым геометрическим nonwinner. Получен воспроизводимый точный результат на неизменённом C366: полный повторный аудит исходного тела, точный максиминный true-edge bottleneck, реализующее дерево, полный отделяющий cut и карта его взаимодействия с единственной устойчивой гранью.

Все четыре предоставленных файла доступны и прочитаны целиком: research-journal, буквальный C366, независимые аудиторы и H/global numerical methods. Для выполненной работы отсутствующих зависимостей нет. Упомянутый исторический 16-body bank не использовался и не восстанавливался. Численный оптимизатор, height continuation, новая операция над опорами или поиск нового тела здесь не выполнялись; их результатов этому closeout не приписываю.

Буквальный исходник действительно задаёт пересечение 63 полупространств row·x≤10^10, а не физическую оболочку нормалей. Его исходный статус own121 и предупреждение о ложном впечатлении близости из-за короткого ребра согласуются с новым исполнением.

## 2. Что действительно исполнено

Из предоставленного источника извлечены неизменённые check_A.py, check_B.py и centred_mass.py. Затем выполнен RECONSTRUCT_C366_HEIGHT100.py, включая независимое полное восстановление H-полиэдра двумя способами, максимальные грани, настоящие рёбра, собственный объёмный центр и полный strict/weak census. Эти аудиторы предоставлены как полные исходники, а не как ссылка на недоступный архив.

Повторно получено:

- V/E/F = 122/183/63; C=366; strict(S,U,H)=(1,2,1), weak000, primitive-zero000.
- S — максимальная грань 3; U — raw-lex вершины 2 и 38; H — настоящее ребро 90–118.
- 240 положительных центрированных тетраэдров, точно нулевые первые моменты; общий центрированный знаменатель 22026 бит.

Ненулевой собственный центр не заменялся нулём. Для ориентира, его десятичное отображение приблизительно равно (−7.309661343635336e−12, 8.702322205634483e−11, 1.439044076161052e−10); объём приблизительно 2.080788355863554. В доказательных вычислениях использованы точные рациональные значения из полного аудита.

После построения нового графового сертификата весь восьмифайловый source-only пакет восстановлен в отдельной чистой директории и исполнен повторно до терминала QA74_C366_PARENT_AND_TRUE_EDGE_CUT_COLD_PASS. Таким образом, это действительно исполненный cold replay, а не только сохранённый wrapper.

## 3. Точный true-edge результат

Пусть X_i=p_i−g, где g — собственный центр заполненного C366. Для ориентированного настоящего ребра определим

W(i,j)=X_i·(X_j−X_i)/(|X_i| |X_j−X_i|).

Корень — точная наиболее удалённая вершина r=2. Исследовалась величина

beta = min_{i≠r} max_{true-edge paths i→r} min_{arrows on path} W.

Это **не all-pair score**, не локальный максимум escape и не peak-to-merge радиальная энергия. Использованы исключительно 183 настоящих ребра, то есть 366 ориентированных стрелок.

Получено точное равенство beta=W(49,64) и строгое рациональное заключение

**−826010086/10^9 < beta < −826010085/10^9.**

Сертификат содержит дерево из 121 стрелки к корню 2, каждая из которых имеет W≥W(49,64), и следующий непустой связный cut K, не содержащий корень:

K=[21,28,29,30,31,32,33,35,37,38,39,42,43,44,46,48,49,50,52,53].

Его полный список 14 ориентированных выходов:

[[29,1],[28,5],[35,6],[21,8],[38,10],[42,15],[46,18],[21,20],[37,34],[52,45],[46,47],[49,64],[52,57],[53,62]].

На каждом выходе W≤W(49,64)<0. Равенство среди выходов достигается только на 49→64. Любой путь из K к корню пересекает один из этих выходов, что даёт верхнюю оценку; возвращённое дерево даёт совпадающую нижнюю. Поэтому критическая стрелка установлена точно, а не выбрана по округлённым численным весам.

Все сравнения производились целочисленно. Для веса n/√d сначала сравнивается знак n; внутри одинакового знака сравниваются квадраты с правильным обращением порядка для отрицательных весов. Отдельный VERIFY_QA74.py не импортирует алгоритм BASIN.py: он использует другую общую целочисленную центрированную реализацию и непосредственно проверяет каждую стрелку дерева, отсутствие циклов, полноту всех выходов cut и обе оценки относительно критического веса.

### Геометрическая карта cut

K содержит нежелательную строгую U38, имеет 23 внутренних настоящих ребра и связен. Инцидентные ему максимальные грани:

[0,1,2,3,4,6,7,8,9,10,12,15,16,20,22,23,30,41].

Грани, все вершины которых лежат в K:

[8,15,20,22].

Для каждого выхода ниже указаны i,j и две инцидентные максимальные грани:

[[29,1,0,1],[28,5,0,2],[35,6,2,4],[21,8,1,3],[38,10,4,6],[42,15,6,10],[46,18,10,12],[21,20,3,7],[37,34,7,9],[52,45,9,16],[46,47,12,23],[49,64,23,41],[52,57,16,30],[53,62,30,41]].

Все индексы нулевые. Вершины — raw-lex из A.json. Грани — максимальные грани A.json; связь с опорами задаётся active_input_indices. Здесь все 63 опоры активны, поэтому эти индексы совпадают с индексами строк отсортированного RAW.H, **но не следует автоматически считать их номерами исходных строк POLAR_POINTS.json**.

**Единственная устойчивая грань 3 имеет цикл [8,20,21]. Она касается K в вершине 21, а выходы 21→8 и 21→20 лежат на её границе.** Поэтому найденная физическая область не отделена от устойчивой стороны независимым неизменяемым интерфейсом. Полная конечная операция над ней должна явно сохранять либо восстанавливать собственную S1, даже когда текущая основная цель — устранение U.

## 4. Что сертификат доказывает для продолжения — и чего не доказывает

Полезна следующая элементарная лемма. Пусть у выпуклого полиэдра при его текущем собственном центре имеется непустое множество вершин K и все настоящие рёбра, выходящие из K, удовлетворяют X_i·(X_j−X_i)<0. Выберем вершину i максимального радиуса внутри K. Для любого другого внутреннего соседа j:

2X_i·(X_j−X_i)=|X_j|²−|X_i|²−|X_j−X_i|²<0.

Для внешних соседей отрицательность дана условием cut. Поэтому радиальное направление строго убывает по всем инцидентным направлениям рёбер, а значит i является строгой U. Если вне K сохраняется другая строгая U, всего U≥2.

Таким образом, исчезновение конкретной U38 не решает задачу, пока остаётся непустой замкнутый по положительным escape-стрелкам потомок K. Его максимум может перейти на другую вершину. Эта лемма допускает изменение собственных масс и координат, **но её cut-предикаты должны заново проверяться на фактическом новом комплексе и при новом собственном центре**. Она не переносит старый centroid или старую триангуляцию на изменённое тело.

Это не глобальное исключение деформаций C366 и не доказательство минимальной величины геометрического перемещения. В частности, отрицательная cosine-beta сама по себе не является расстоянием до own110. Найденный K — точный графовый bottleneck-cut, а не утверждение о тождестве с полной областью притяжения непрерывного радиального потока. Ранее упомянутый в журнале радиальный Hausdorff-сертификат здесь не воспроизводился.

Следующая содержательная конструктивная задача теперь конкретна: конечным изменением нормалей, высот и связанной физической области разрушить замкнутость этого cut, не создать новый замкнутый cut и одновременно восстановить собственную S1 на затронутой устойчивой стороне. Начальный перечень 18 инцидентных опор и 14 выходов приведён полностью. Он задаёт вход для связанной операции, но не доказанную достаточную размерность управляющего набора. Открытие одной стрелки 49→64 само по себе также не гарантирует U1: после изменения нужны заново построенные true-edge escape-системы для всех вершин и полный аудит.

Ни такая конечная операция, ни её успешность в этом результате не заявлены. Результат завершает точное описание препятствия и источников, а не выполнение основной конструктивной цели.

## 5. Самодостаточное восстановление

Ни один исходный attachment, sandbox-файл, численный пакет или внешний helper для следующего replay не требуется. В капсуле ниже буквально находятся восемь полных файлов: POLAR_POINTS.json со всеми 63 строками, исходный C366 wrapper, независимые check_A.py/check_B.py/centred_mass.py, новый BASIN.py, отдельный VERIFY_QA74.py и общий REPLAY_QA74.py.

Среда фактического исполнения: CPython 3.13.5, только стандартная библиотека, assertions включены. Случайности и seeds нет. Масштаб интервала beta — точно 10^9. Все остальные правила сортировки, tie-breaking, центрирования и построения сертификата заданы полными исходниками внутри капсулы.

Сохранить следующий код как RECOVER_QA74.py и выполнить `python -B -S RECOVER_QA74.py` в директории без QA74_RECOVERED. Он восстановит исходники и запустит полный replay.

Ожидаемые заключительные маркеры:

C366_HEIGHT100_G10_EXACT_OWN121_AB_MASS_NONWINNER_PASS
QA74_C366_TRUE_EDGE_BOTTLENECK_EXACT_PASS 1404 b6dc0abd9c7337d7d38235e4f2c0decff9e8c9d970f81bbc90d1460d52983c31
QA74_C366_TREE_CUT_INDEPENDENT_INTEGER_CHECK_PASS 121 20 14
QA74_C366_PARENT_AND_TRUE_EDGE_CUT_COLD_PASS

Основные выходные идентичности, JSON без завершающего перевода строки:

POLAR_POINTS.json: 2365 bytes, SHA256 207426c620eacfcaba4a3d60d9fc13fdaed16d41236ddd458ac3829ac5ea0973.
RAW.json: 3084 bytes, SHA256 2a803e23c50ef6c92e2281e57b6b83eea7e79c5c9c61c98889f7490a8caad699.
A.json и B.json: каждый 120665 bytes, SHA256 2d646e02deaed82244ff7cc00870b341dca148ce86b553acbc29cb4ef8aaca4b.
MASS.json: 223 bytes, SHA256 483df377a3860e3c848346695c7767f24dcde7300444122455ad609ac7c8a231.
BASIN.json: 1404 bytes, SHA256 b6dc0abd9c7337d7d38235e4f2c0decff9e8c9d970f81bbc90d1460d52983c31.

Новые исходники: BASIN.py 5211 bytes/SHA256 43e83bbec5668b152201bad325b30dbc026fa3beff4a353fba1c772de5770f74; VERIFY_QA74.py 2017 bytes/SHA256 5a8bdd2f84a1ffcc2025e3bc2806bd292d105a059fa1aaa1cb445de35628e11a; REPLAY_QA74.py 563 bytes/SHA256 c1df492f765ea0f3662aae8a14c8e2a2a32f849aab6f1ce458609307faf00019.

```python
import base64, hashlib, json, subprocess, sys, zlib
from pathlib import Path
assert __debug__
PAYLOAD = '''
c-rlJi<8<&(&xXz_=`9YF4}tYvO2<#_Imc)>G5l9pD{rQNi^yPff3Mj`~1J(FSDwIMB}z+cK2@M;`{(n%F4>h%FN2lO6lu^r%&Gg
dVaFJdC+_Cng5>c!f0JvuQo|5i7%4cJlv)8G^?!^i}iK5ifhp#PqU;JC98EhNuzL`)D~GS#J^3Pu9LX-vb9{yZq|!sa`HJlU(_bE
MYu+{`7&Ik`6A0jE&s9!R|(_HYl~IwVihi@wPhGxg%?R)i<5P-n$sxjX=NlJlvIAs()n_+TG#TMTwDUFn1}1Bm?q)!i<pM_be4`k
XOq=pUYo2ip%lZ`RF@a3p%&(~*BWS(MeD_4Rscow<!HSaT_raPVhQ{}s_(zT&(9e~KgpBzD9zR*Flv;qSED$+NY{D8G(Km44`$(f
9EY`Ck7zuJH}hrQ*ohn%2z4I31D{2nfHUEGvC4x+UEpu8ZWt#?7A@kW0W|SqT_6%Sy?irogw1hn0>*^`6lJyBbP2RK27vR6{h*EA
scEztyT?Qf@FbJkYLhiWqxU(h;m@mJu-+_ZNn;)^8?VL6Fc|5IP=<s0D!d+TiTP2I*M~#d=OQR~QBYBmtyhaQt`7~P|16-jIGIKB
MzgU!iIZ%BwWRqm_AOz*AW{k4Zweha*m&058f6d(G0ua*j}a~v?MwRcO3@mIdV++0TtUB-*JH8N3>@d;m7#im(jA{Q*R64L&ai7S
*RV_Rn{f<57-|fwRWQK9HEzYN1iU4%Ps9FsFiWz=D>XY(0q|?rScTa|(l|E+<U+4t+I!tttp@2(jB|W8o3>^fEoHb`Ev_4>xYWx@
e-gz{*<stl_vNs;VG1^4t4R$*!ivw!p+?EnB<sy8s}WK`#D5~F#1KqGlUfq|R2{-qgr!l_CH&~6B!?^qM5ad|C&_M|WN~A#r&q|!
OOYDG(uAamNLZ3fQ_7(*H$i^U*bVHVA#ia+7khwo0+?Td{HCYq2S~na<u_HBYyoqz(=g_pS?9Z^8U&1P-VB^!>qh<9;fF%DSjEXI
APr7pwP>`SG*d$^-rjUH^g4>mo}L^5GVke|xUU5v%&vlgIcyf#`m<!4%z~EHU(Dj*e32!4R$mdLnUr2-j)1JCd5wU{u2u%UQiB3!
X!IEQ!@w%B0Tciz;5$6#mAsk45<%fEg27<OqmRl;#^eYVnUNS7bSud=^8^-64s7%^0?hX$TrNo(0Dq;YK2Gv=FlbrB=6RpU%?^Hz
fJL?JI}Av36tNF21*sb8v%g-%i(t@b?STb-YW=*PrZem>04i}XOD@D^z`Mu^eJ&Tv27y!ssRgiK0>*ne#KLClG}|P55UC5iM5URR
hM_;(aJEST+-oRALh;|I!eKlHJ!P=;5KY03bQmz4<^+CUmiR}%ukLm&O?8t`d9I?-Vnk3*t>}4<U7)6EHBJLlufsYVvEUZ-NTr0N
G<j{(Xb$NwyebOgRgl3dG_DS0nE<sE1_g4XPqLMXI8b7&HlkG;2bS4vcKd6&<D~hQ)w<Ehnsm#6-adL1SEsOUuAA}W62#-i`k_S^
%~%4?7GjzPjkTb5wi>5qEt%y>t<hSyEYVt*4c2`5g+yFH-UYU$venv(m<b-(y<tD!iu?<iur1p!fFGEzEzH-KviaJ!@-Iis*Y+Os
wI%blZEl;Og#NcMOq2e{nhXC`JHvi{15_C;Mh%WqEv!i)VFw5Lz%CankaXy3;cO=F!7yE{r}@cV?YHGsE?ev*$pZLA4WoY@Z1?R_
=dPtF90;;np=+Ke&=QV5eVl}G+_*N5LhA*{2PH|r9u5VTk(c<?toFMOlzLnbHA~(kVKfcL=`3B})Hd*KFXYae*Wk^i(Ry}M3&)GC
^hFc)j>n7j8r(>ts~X!M#gY|aO5)%vP4AmBKx}#LF*)0S8cxX47*!K;ePBYihq}MlmeWF6;E2b2CMt@0>RYjrDbt2nb2i$n^{z%M
r&rZzslG-Z5V*tZic7s6qT8TxC3c3|2zEy{0HSn<y^U^3EKKHZU=1~;vUyn1R<to3%W4IVn=y0+9D>?V{CFHx8Nzb1gJw&qcx;x5
T@;gvRw<m_aE6VJ$Q4B3@Bs9<jT-8m5`jw=&PMD21%re;CsnVA6&_4XjK@J`+N?HT(S)(J_{d*>O@KDyS_)8^sJk+>34(1^Y>1Fv
N%xKlObNra#;`e#VN=DhsTyUTw&H}mv0iLgkp`*SOD6|HHK<QQ4oVEo%!%<oD!fdyJdKk-hv8s37S~y_s(QGiLJUf5oa8?{jMjn4
Ui|6TaF0u|gnYnBZUlk7za`1hJlqSYXijqNG^nj0hS_RdrCA)**<g(*oaf~q$>@Eww_tVg{_I6C0HyEiLyG6l<kt&Ce4=F1*%k)4
5iK^^8Z#2tNq9vK^j(+E6&v<aFV>F*2p+Kz!mk)9-cYbR;LUa@ihHHVE+9oMVOp<}WTc!!`6b9=;lIFYP-0>v<B>zn-7i^rI$G05
mCm|VY_fbEj%P^`{(}C|frZ4(?|@;Ql^7bO!Qyn4MCdk>`$|xF_=0DpTF>EKpzkP8ZxaR~BU_%_h&j)<$YhmggKls`Gag0e6e>zz
>RB}ghe)v3Kx?p%lGKjUI1iL63VB!cE$&J!D<LV9%L2==c_4+iB2UaX#uVK|GqRS0RO}T7o@B|DM0>dh#;%H|ZUv2TvJ2{*wF+n4
o)dy6{n|WSVh>*}HW$+xWq`Kmku7;%F)bcBKXQF*Z=QTOd0FSA3DkBp%EEav8U;apG@6GHg;Bj%F=516$_0h1i!HR)QSNa-S)$?w
MAA6HZW@oqH|r#CRIMOKkz+$AuTJu5XnQ_d;GOT{6pICS3b-4VZTh|^>UQkAeq!2j5+-rSwq18JX-AQ1cG~9HajiHCEw>XT9e?b3
P8f|NyBm$&WYP)4D0IhlJ$}Hsso5foa}3v~9bIOL`r~o%cb2t&bs~tqPp+XWiJHlHtZ*$?lxV5He$sYF&m7+$y?gV=+34)~-_Ax)
e}DJxA7|%h&;EOK_VLNHccWKN-oC91p7oJwSLZDzGlVBB*_Dw>Sv6LP3fKej;MMQ{c=BfS>i1vI-@QE{;0L`2Uq3$}+w%EA&oYZY
;`4*$0vK~N4-jg0O}}fqzTbt%Z<(%x2CHLw!u1@>wA!8r8v`)kZ+A@7?Y05d?X=yF<2aTp@ZasYj%_*w)o#08*R|RmAGmD4ZF}vm
3sl{92P1gxHUYV9%kQ{0aEq32c6`rt+omI0cE@x4w(E6V9?)%ffxPS4qUHJBj%k}VjqO@p%Q8C{9#B@tL)Ui4X$y~N^DN&IUWX|2
yp9hD&vJab?RPxUH9MYdTaE+T+9qb_pd$^1LHxGYZTlF>^1ZH)xmsP}TOPj6w%H*V6H{=2-ZK@K+Ge+7cZKKBbY0&eE?IsXGU?l$
t^j1ai^)4ShI35Ea@?-P6j@!{b4^UgXP{2o2jw0Ojmd!bw$0=D?Y8e)t}Q$e0XcWDB(1jVbS<aT?N~ImHmK?N4(8VK9S3wfUAu#8
p!IC4V_7^ozw25ah87^&w8104ONcOKs8`zq3_xttBbI?w$22_<2adMdwq*fN*Owe{oQ~z0kO~2@#U!xGw9H_Q@7NyJouC}cbHEd<
faEgP4EWH)^V%M`!KfS)eY*}8LqNP7Q0O_P00Cfx>AR8v;5a7hLrNfdm{O+$NorxKz<JMMQL=2BM7Jx~A3t0G*)(w1!&<ew9mxUH
>$EW%rsQ;d7fi$g3SzNMvdb_w))7=e+8|%P({+gI7Rd5!;(3>VFof%ZJR8CaJA=hFJ0!O@L<79BXtcJ8Z_~C-k`o7nKuTParmojD
yO=SnfbDuv0Zg_dNRVLN94tLhLFj=Ep9JOmBugfifFz~swJ}PEgtYBi(9$-q3#1W(()Eea0wh9zx}7d@q2mEFluAOmSQDsMyA9dI
Fr*T|0jB$w1p--pf!L!CJ~-X!g4zxUumlFfmu+_~2I^u28{CDsxNXO?A$3kifGdzvQa7F;Eu#mfbip7f0;I<82$%`KOGcq1Vcf3M
1~O7>NGQYx=H3=AX|(USE;GTwm2dH~S{M{egG`yi?*OMwGS9-&Zet{?)3ycV*M+`7k)SzP;tu#J1<Jt+U~tP4j_-CXaMmKVGXVjq
#?&PgiL%v(9f6&4JgAb{WtH#3LO??0c$h477jh*a)?J9Q(<TD3_z*Q0D$P)?M>6A+kbucpBJi9nt82Gy2p$VMdV_e#5Yd9!xgPqr
A<xh%uZ_-3JOr@|6(B@VJqJjk6A&tl=K_R<3X^gmRUOA=C@|EAH8MpTvxZDL(nLc;VS611`a}a#XWs@d1e6#=pbN`7NVh<lgBv!?
U<X14$-!#4q}(16)rD1q5}8=OE(8+<+g%LZAz5rg16Um(U04_}1X6^x#@g8?iv)P+k{A&SI^clgKyn3)n`t^kD;YJ<g%CiJ2ot0W
Miv4IdBiG^VY0~b0f5Md-C=_O+Y1JPN&zF=0Z5zeCQxCMbEQGBpk$aJ$i(Vl`7Bs=FayF$I^uL0lLa||cmWhU0VdRT$!N4XSSyIK
X-YXD(*=$|*hq)5L0|$fQY7bKeOp>!*d?qVR*cLm%oT|b7-e_uE;N!A2JQ<i1QwnM!D?ai>9|BWCWCc!JD%LAJQvDqVmMeG2R6u~
oegq_3Bj0|o-|VsX$ZK_($Xf|j$MYO%fxnOw-pqY1%{Az3=1|3Yv+^E#!|!3po=u;UDzVb9k`$+9V`a#pKSX<j46SzgZUn8izggX
X&66Zl@G6?18K9^R73YYvb!*OE~MA@tTsCU0Kq;3n;<6$gY41vNUj0xLbQEiO<^KUy`cdo07*w&2m4XS=@Mf-l4Z+P(hJiL`vjv8
(KNwZ^di>*T=IaGwbLcz)x~B2fpTFHAqBL--~t-}B*+^MzrnA1bN1}_^S5yB;K#9__wwx5zrB2i{Yf4rA0Eys?~V^?|B3Tdy1nE~
Z$>_I!xR8$ux~mVO;SV$Bl58G#cZ22j1w6rK2kAozSyjyq)tg~ea1UQ{5yI==fF>d{PC22JQaMNiGXbm=bT!8`<I>NDsO*;Sa-a+
7>zg+a1cHq=wHgvp?=4Ktye>cemQzr-f^RsccKT|;n=}!L*63aHj^-#MBzAeLnrplxI2j~XA&c#u>2UJ;rMYJ!v=+s17!#!FA2#7
sT=)ha#0Q(mPY?2r%H;vFaQR1=~UM_bGZt(4+q>z{x{;cek}9$7g5}3u7F^l+<5dT=HQQG_Z6i#R^fH<wf?f+Qz7_E<6A!ro}5sq
f_n&7f~Wf*iY<Rf6cZqZL0B^nemjw2O|b~alO91p7E?g-Vf}}^KBcS&-4(c7+>qH1G@Al{hZW=;l_FA^ryOnGCaZ-E#pP&}HAr?W
=!dsBYCqod$XLgsV?gbxKa!}xefR~P0wfRPcqWrX^6r2fA-He*VdjJSI$5v6X%eqOf`M`6?zjQ%n?YeF=_-fnF6N2mmLye!MT_}-
k&U!|l@dOqaVmRYleGQMS+ZNobjH^@MdK{{y#_3$3-JxHw<Wd{d1f;4qpqD`i?b51J@&^PCrQF~((XoH)Qx;A>UOYCPv9e&VJ8a1
*zb1hhNwT$DF1cww5UJ*cOd-@fwIO+Zgw5UKAynY58-c_i4(DVLt9S-54JtA-8hPqHu-!AJ29r`Vb&(Jw;gpt+p+4#x6c`c`FGM2
6#Speui|vokj7J4wPcrKSr=Eqi*S}xY)!gJNfE(Eg`}i|#(tdy>7Zz69*dBEDBg%M{n*b*%nh~<oNHigRipOf<N!2W3(J6L8VdUC
Q%2wsT^-3)s60h=>l*#dGF5Kk_YddT7DrE>j)>6F`S0f+emy@wd!v#ThiQg4XRrS8<bRGR?Qv)STO4eG`DVOaEuez=eH-E7HUaw=
{9vE!FY=RUN=vs=3lz;`UKwzAP``J}#y<7?AMfg%Q5)2CO_*$bq*sxD$a~zNpx>Xp`SnFH`5*P+wchi9P4a+5Fxe&1hK-b{x1OSB
3yf}J3PZUyYj&%o+9Be@%vvciH-><~2Xfg4-J4zug8JBxBQqSw-3WnYJ8s9=_Z%;ACw64UNi>;slTOr)yKQsQvBu-5YsM5y$DWOV
JA!T%!nIF=y?XNI?EKy6$@%kAKJ3{aScl*L@%%d?Rpn|?o%d@NC$vS<fi0zDFOn6N2c&Vx6>W=&Jig^)fF$OuxjX<{%$Kudolutd
<a73Xk>v8IMhcx?ajF^F<k07JUb{}xi|JY(%+sOhBUPmr&Mp?vr|JBM#dtqohWFy1a0)B=%kLyy*Hmp_kdN?PSo;9>b5^O2d-0>{
xPG}X?!~dfII#Wx$~alORxVK!_ZQH8DwnrC2W%@+L~cd2FIBrZtc}Z~a2Bq#L%S4TxTbL1yjFd$_kF)`O(B<S=D|RAyi?OAOADpI
lnc^yG1|6urvQyB%RZIL&vX@o96=YJsgbGrOx>XZw9lC=qWfg@`P69)X5+g)?DH8-vTmRSm*6^;z|j5D`B5G8%JbQ;lDxz?c1-)N
ug`6QuRN)8jT^&!`(IzVhVAZ+!u~LM_tf|8=O_LClGy^WXgg>1#kDGJ;uE%Gr{b`T@DJl~b#sJVJrl0PQ5_h`WeLNc>H-t<k_4I=
CBVn>c^L_H5x?j@Y;5<KunxzL+N6i+c7^YfgPBDljshh>+*&vRS@c*snQ=tL9I`$KXzx8*gd}iz5a5m-F4p%x?QHRQnyL|IizfbI
oGfbMA7S8+(`nkozc`ZHYI>yVh4?Dh=Aa(zl1?kJyoFE0OH*1B2}adTCH>LRv94dy%s359ve8*H138ZaNoZUuACOfy+aN7h3~cXI
+$en8<JC4>!a#IyNmU@Cvm&%p0;PhmV$pl|P9swcmSmq+$)?gKZVz;OkB2ORL0}s0cXUZkS$O_LG*^z8{&Yn56LFN&DYWs(QP`Q>
^?yBoe)j4NALn%a?(A>yE1$ijgE8p}&_Qr<{##M4J6=LLv+<~$v?%)w@22T0mfpgO-GpA@I_$%_+BnQ%AHp>|5R368gtMNjdM6p&
)%0d|^1W?;ogyOm3)?>Jiuyh_$A7{ZpnZtSltY9WML8Yzwq5f^<`cwCQ34GR)gxLh^1RZg5yE+Bj^P!wLaG5CQ=x^rGO5j!cZIsL
sLhghjl)X&<$)uyxYn-3;`*;T6a8uMJvTyOU6xApFyaqfiQ31qFERa&F9Ae_H=&22>Xr9?VD^8rU9B^Hm|`vx<uK$%O;Vlgv#p43
g6M{7BOl_cXLAV*0blNotI~oSqh%@kg4GkZ!Qf-1$`lY(@qy1v`S}oTALW)v4t7GWE&3T{tJ;6>KMZ0bQ<p#&m8f!X$LL``gR3FH
nvES@+|b9Zs?b%aXwG{>QTq_QXuS7@-<&p^PBGqx0L_>`Txsxrbu-#7X4tCgj7SOGSIXe5H+j8Rmm%mgn1?rK&kGCj?(E&0Coj*Q
zj>m}L^&7JqXN_)CRcjX6MT<k9cRP1(?MB<QM8bhB4#EPlYPmD3CB71h6<9hD11DSxZ_Eoo?@4%OE!$c3;1UF=o&G_=*b9Xbo8{|
BOCYa-s+3xk@Q8*l?&yxWW}e4H+Wb!kpENy_n5Vn$zy3~f8Nxk@J6Z+8ZG8y;x%<VVh%5&Sg=Vvu(dz5gr9;2^I2IV+SbbkPU`yZ
;eBQiVfwK?t^4}SH#6`wJm`}*cl&g1_@8B`<Ali&QGrwvCI_Q-&5raUYwY$zmmjX8`zp!5V`D`QVV;t^kVW)F%ZvRq*DJsr0Z~r&
EX~(O0X<My%a1PYhDUl+&0o>$>s7DX?@C5qyA#OYJa13}P+Ojzel(1p+Phd}jgKOYb0J;ZaF^z#@WrWwFPA+s2<IHc^})hmaCvCM
9j<%4{3Ren!#>rFDc6z4sDwfdGV6nIDENC!IA;s^oqhQGT!Tq862<(e$<=-xK7s)BYpMQ56D?PSp`|gkBuuGA!IXNb%_>j62(I#_
j3&`ITNr{a2EASjvNcU*x^ln&poiR@q_3^Z^G+@H2$^8~9<(5Y{0$_j@i;Jhlxy8r?b0vh@ut**4RW>^(3lUWDSyjFS9{`Pr;reJ
gQWIcNiAva#{o7&Ye@X$9g-fM(#>|c*)SfPz32v(5*|p-r&P5o?9L}#OV^-BJ1`(ZZ8;u#U8!xG%AWVm4kdkw6EDl|4y;o(a{{PA
{U!N0rC9f+aT>_{92Id>3&p;&Wi@byr{*5POQYPA;+>b20+whn{CO}~4SLS7)MMCxPK^g`+TT(!6MNYR_W75R29`8-=}T6+^wbwd
7LIgI*n|Y<l(!&_z{l0FzX|qM1R<6D5y3q6uY<iY>&Mbr35BeTRu6l`aV3`guiD#m2Zww)OQVz`|13)`LOLD-by))Spd{ZSPvssY
pPId?scB`DY}Im0%2;uA3J-{zA)^R~_K_{EN#0x!ScjW&OhG6=56SM=Mr;Kf+MXJS1IPw}id^P)mH}@*_)nX|bK=m(5b_#~+8X-D
)sPS=4#Y8}av9Jakh5eawc=Ra4YQjDu`I)#(<x|Tf-*7HyT-YA4w}mRySNDWpm8bU*eDjC$(7=|e)Q<#Vn4B^@vsrc)FzCQ$5#Yo
Nerp;*>hGVO`>_xSc@e+FIYlF@>t5j>A@?K{E>8k#^KUbGJLXhmi3#uPEvvSP7j{2+fSBR6PJq74<5z%XlOH$i5+O44*M`NRjZ#F
+Q#4)2y*1JPqGFcccPn~q)*$bNoq(sbwk8YU1p2bJe+}+^NO!7`wshy$pmVK+s}{QR@u34{q-uXGC;->`#JH@N&)rL1Z$!p2)_Q9
4U)*g1QJOMQB=|IZ-t4M`3~Z8bVK2VrEDME%^uT9P8dvJxS6e$1SoOf6bOWSFf@v%9x(-OCG<2o{c!BjAm+Y+=s+Sr8ZG*gMcohi
@d4&c5ZD#7x-D9^7>_0s1mrr?mE7U>Zibv4AIaqnIbeJVtQn+cz*chqFzCnO-eMMgdj&jJnH7yvLPgu9Y~$Uol)IA8y>K{n@VrZU
@T3bTGmk!SlBx$z6nD#Xv<T>cd)y?qkdJgr1||sFOrtNumf+LjjzFu&RBZ$DAjypo<YfqQER09KR_!f<O^NSeu+`Yu81f~XzU?Dd
Xd77|G9)Huyo}J;7+Q}cHX-{LCWQ9(GD-;~JJSA06L_X_2D>|n0M-!=+%G?rziU1-?tt{^q5ONF$KM&HULUd9S02URHpgXuR)Ox{
W$;mqbHwns2=;kin9wsiMW%~!@#uZ&<p*KNJ(QP7?j@Z<6oG|AG0yi7y$jWF$qlJIhIspe%<kI{^!dko{^aYkm;A}s^t2Cr2mWO1
+@IVAW<R+t@*Ve^sV$quL-Qk@f!kX?_K20`_@MzB_VWvHh~koRd_Y4Gq1x)?7qHQ{4}<*Tgp-~eAF}$8Z-=|5X7BBbl0~Px$*goA
-s;;ARe*y`xYQjv#moFiB%lCPIFJtem%(KYHShD&-~6V8%IviPW@Q5;rY$`Z%<d5U3Njnbm-GO1lh>3V`ld_uU|!14>Yj4$yg`tG
Oh{jyLP{=!D@g>p6Et|rEahjNvC>5%`cmW<L(RJU0{+P#?<+pLWE%Q|Uw?e4+@h(-cONXnbX7{BODn6wGReOrP)z72NuXc4(7#Q}
(>D4`7)&MDNg}veO7$(jqoJRPc`(p2wjxh|@BI=D!+w?p(i_NN=H`4o7jyKSt9D$+$!r}4S=OA-TiLvs&5I-&-H^u<QlwkAiDbTb
)=ZLz#V<m&%!H<OKF4rOXGVize>?!lXj~1D0pMOK-#Z?3P9U1JLQuy0h5hX1;o-tvc|ZGb2d4C#sdg38Ve?r_GV3=(MJcJss@ks>
!6>EsRCLY{>b+MRk2nkVd$@QJ?00c->~W<)Hi~lUIQS@})5xDf`cY*;Glcfc)VI*CnEDn6Ny<QNBs5ATj~A%Trkt1#<n~aMPgXm8
D%uNpH1R16HWN(t?F)I{@yC1lefH8&PZ`SFAJlF2ef9yj59;26w=eEKychiOUX;t*g0q*5Ry~{c_JjPj2UiUW_yhBFL;?uL=Au-#
m*i2n)VH>h;p!LI|K0MxU~(&t7XJl$e&4PC3zFNzo3h<)mV~Et*fWBo0s}lNKLkj=3p*C~q*uRx1VbVGpQyRe&y#Uo=J%c>W8mu3
TtAzb)eoILsdIjX&j9)2Okcdv7saEi{7XHzdjFZ4tP1|wEbr^TnC1Oz8Q!xuzgLsIOHAc3J!%dgQnFJ}+Vf$N9(_2Luh8L?Eh6M2
-C9MrR?)3h>PCls)Ga^E4>$9>x!yF(l2v64m5>E_Dj{ppl`Ye?vJ+P6pwqu5-OKM53$w$tuclEBTTc95l+wNyKgg|L3eu84AFH3{
Ph^5$|L13d%h^1BHu+B{^r+XpIXy(0<)j|NALjMAQN?9^T}~_<<oM|Rus`J+I*Kjbkag%P!knd9qPE6Tu1`f1-^uhzT7)e<H1e&q
YZVUlo;n!Qv7;0p={&`O6slOn_hj~#0V}RlDA|3E4q{5k4N-27$$6UQIz4{PuZ8MQ(~GIRO6JS;jjYnu4mA9!X^|GwyZ%%~BbaV7
nJ6j&85{i-m^h`BTB~SX8if~4;P9Z-dm4h*4S)-7H6$7Qf(*JUzlUo5m|Iv!=!(0u$HiSAe+MB=knzpvfU$(`lo}WtF80XK6{sW+
$e{Pf*om$*?FtDk03+gZP(^5^5rC(3<0vK|;^u?g?31jv$y8nt0q2rTIaN)Ptktd;n^{~N6ZR4miQuDEcym(9Ui}P>1ilNTRIuPI
m59V*Mx_Pfb;F_@r_sMT4n+vdU{X0aak8uYy3s-lyu5<FLUl@cQ=RVO7Z9pi0@WsQ-A!}$<zxC^mpz@NTOKCqzV#_c8C44Pio_cA
9_;AN5p;1g)WNbkHY}+8R^(9oMOw9-O=WFRF7T1OYDrs;q*s^6@`_4lB;sX}RMh!XomqYCROBb$L{adyNID)fMU<UY)~Ckr4a1Ut
gdGqc$w*M7D2L`)Q6}wzuW7GBkF+6)(7jXDTc;ZMZ80&pM*e0oQPo<!iHxEiM7S`js|A$_5qSVsqu;^3M?zSOc$`A55(0WB58&vi
vD|u^B-MgC)l(9(PfnhyfS&r_xo7r>zaS<U?`_2~$j2JXkr5s%EaPDimP|RdRVXa)VYtURbizqn4L8W5O1j)5?_={`t@$l#4AbXV
Vj$?H=3##v@X+!X4I&ex<6i=9>gi(3qL`C<OB_0g9UB_Ucz8f2!>MgnQK-fAFttyB{W}K$v@Nen$%gM_{DZ+X|6#hHLlvp8@#Xi^
%=hQm{*8%yBCDFsuH><6#T3e!eLC~KKeewD`*u08&o7DMfG!C3#<2f$Y5#sHTk+3l{<rWj*ZOd@|7DYGl1h%ATU3&sua9Tx6`G#<
*13AwW1p<2G`#{j$kglBQnG$EU9jT3ZcK$`n$3pwkSa;YR}IHGXON7;)4{S~?^ESt0Jmcy>?VCW^l6m&r;Ml|NaOMJUTmL&fi!_T
30}#9tDMSfI#`%3qHv~97ZA$r-B4L?S4h(Sl%WV*K9Se?iLC#pLG=C8hVl^X1C$y>*)^b#0;eI7itQt}eE7gXG$qxuj7uL%7{z&s
gi-k*b+f;Jkt9%6$fyF+afRf_v*6xShNCAI)z=9B^od2~4Z?R$ERMcBczN{1LQYSI$Ir9_{~OgY{pj2Rrl5RsQ9(uL7V<^F8l`-T
?>N_wQT(4czsLgEdOEY{Pa|?}=(71t#|q*%gVM_SS5~a~G$P65$ZhyjCYpEZWl-iore1?QjWh#fGCYHhGwveeu7+3sj^---F?p^a
Gjs!fALl*CCIqEUPU!MzKAB<eKR=Nmf9?on7Ov=#G%mf8v(d*LYA&T6L>f%^3^VXrz9=2O6TNLzVbKIv0ls&9ae(ITQHFe9FNd3#
#pRLu-ST|+*e3|msxv3wfqQ&@x)+U5j{Ud~A1%<G;c1|cdM<}OeTuWulwFn!11{u=P7qXQSUKS#2%#Z|f92pt(SP8O-yTd8VOB-7
Rdb>RI}x}0GaTsKwm84p?$2*3xdt`MeZJvm&SoUE#ImGgm)NMZQRt7hVgEjjxpM?Vu=*6{hl+FmSxlijM~-9ubB<D0^YSsuzw-zM
yW){k6mI?h2Pywo4pO9#_W#IfimH#VKmC`SrF{F}G#a#X
'''
b85 = ''.join(PAYLOAD.split()).encode('ascii')
assert len(b85) == 11745
assert hashlib.sha256(b85).hexdigest() == '9954e26992eeabf5ad10623e5ac8491eab00c35b963f8c79336105114612cc96'
packed = base64.b85decode(b85)
assert len(packed) == 9396
assert hashlib.sha256(packed).hexdigest() == '75355fe5f276e13889c096b96f02bfe41a87483db6d2663623f971133e01a0c4'
raw = zlib.decompress(packed)
assert len(raw) == 25695
assert hashlib.sha256(raw).hexdigest() == '77c7d697f8dd274c5e98d1e9a382b2c97eb700457f21ef1f805eba6703ccfc3d'
files = json.loads(raw)
assert len(files) == 8
root = Path('QA74_RECOVERED')
root.mkdir(exist_ok=False)
for name, text in files.items():
    rel = Path(name)
    assert not rel.is_absolute() and '..' not in rel.parts
    dest = root / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(text.encode('utf-8'))
print('QA74_SOURCE_RECOVERED_8', flush=True)
subprocess.run([sys.executable, '-B', '-S', str(root / 'REPLAY_QA74.py')], check=True)
```

Дополнительная удобная копия исходников, полного исходного аудита и нового сертификата: QA74_C366_exact_cut_bundle.zip. Она не является единственным носителем: все восемь необходимых исходных файлов полностью восстанавливаются из текста выше.

**Граница передачи:** единственное физическое тело этого результата — исходный точный C366 own121. Новая сохранённая сущность — исполненный точный true-edge tree/cut-сертификат и карта связанного интерфейса. Не объявлять их конечной деформацией, устранением U-бассейна, новым own110 или глобальным запретом на продолжение.
