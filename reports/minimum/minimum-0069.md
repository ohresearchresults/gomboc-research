# minimum-0069

Historical AI scientific report · saved 2026-09-16 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced; unreviewed-encoded-blocks-omitted.

---

# TREE253: отделение корневой грани от терминального ребра и полное инцидентностное покрытие

## 1. Итог и точная область действия

**Получено новое полное исключение непрерывного физического подкласса:** в настоящей реализации буквальной TREE253 корневая грань F0 не может встречать терминальное родительское ребро F5∩F6. Более того, доказано равномерное отделение этого ребра от F0, выраженное настоящими аффинными зазорами. На срезе (10,17,9) это исключает 124116 из 326693 полностью перечисленных гранно-размеченных дерево/инцидентность-доменов. Закрыты четыре полных класса точного набора общевершинных окон. В K=2 остаётся 55 из 142 доменов.

**Вся TREE253, весь K=2 и весь совместный joint110-срез пока не исключены.** Ни существование в остатке, ни оптимальность новой константы не утверждаются. Глобальные V≥10, F≥9, C≥34 и принятый реестр 632 типов / 52585 совместных корней не меняются. Новые числа имеют другие единицы счёта и из этого реестра не вычитаются. :contentReference[oaicite:0]{index=0}

Новый результат имеет идентичность **TREE253_TRUE_TERMINAL_RIDGE_FULL_INCIDENCE_COVER_V1**. Он относится к принятому буквальному OJ253-домену: полному графу неотрицательных теней, состоящему ровно из стрелок i→p_i при p=(0,0,1,2,3,4,5,0,7), выбранных на настоящих соседних гранях. Произвольный граф, лишь содержащий такой остов и дополнительные положительные тени, здесь не объявляется исключённым. В доказательстве все используемые знаки ослаблены до нестрогих, поэтому соответствующие слабые стенки также покрыты. Именно такой объём OJ-посылки зафиксирован буквальным родителем. :contentReference[oaicite:1]{index=1}

Прочитаны актуальная сводка, релевантные доказательства и оба буквальных родителя целиком, включая их исходные капсулы:

- minimum-0061: 49087 байт, SHA-256 5bd7dc9ed75e5dcbd403d23bf0c22fdaaf06d0d60f54066507505173dc3ee910.
- minimum-0029: 36226 байт, SHA-256 07da26de37a7076fae43373e6ecd0c85ba0b45ffbe359ed38b707c462083dd8c.

Эти два SHA действительно воспроизведены: буквальный Markdown с одним конечным LF обёрнут в JSON с порядком ключей version,result_markdown, ensure_ascii=False, separators=(',',':'), без конечного LF у JSON. Конфликта массивов или идентичностей не обнаружено. Исторические C32 и 633/52635-сводки родителей не заменяют более позднюю сводку. Условные объёмные зазоры второго родителя сохраняются; опровергнутые им индивидуальные трёхцикловые product≤1 и P0 для I+Λ нигде не используются. :contentReference[oaicite:2]{index=2}

## 2. Одно настоящее тело и новые неравенства

Пусть P={x:q_iᵀx≤1} — ограниченное полноразмерное однородное тело с девятью настоящими максимальными гранями, перенесённое к собственному объёмному центроиду. Q имеет строки q_iᵀ. Всюду используются только его

V=Vol(P), Σ=E_P xxᵀ, Y_i(x)=1−q_iᵀx,
d_i=A_i/(V‖q_i‖), Λ[:,i]=d_i E_Fi Y,
H=E_P YYᵀ=J+QΣQᵀ, K_i=d_i E_Fi YYᵀ.

Механическая пара одна: N=M⁻¹≻0, G=QNQᵀ, n_i=G_ii. В частности Λ1=3·1, ΛQ=−Q, Λ²+Λ=4·1dᵀ, d_i=(Λ²)_ii/4, rank Q=3, rank Λ=rank H=4, rank K_i=3. Свободные положительные массы или независимо подогнанные моменты этим определением не допускаются.

**Новая теорема о терминальной концентрации:**

(1)  Λ_05+Λ_06 > 51/25.

Из настоящего cap Λ_ij<10/9 следуют

(2)  Λ_05>209/225, Λ_06>209/225;
     Σ_{j∉{0,5,6}}Λ_0j<24/25.

Это гранный результат без U1, без V=10 и без ограничения обусловленности M. Точный сертификат (1) и полное покрытие его замкнутого отрицания приведены ниже.

**Физическая лемма о контакте.** Для любого такого тела 0≤Y_j(x)≤4 на всём P. Действительно, выберем вершину v, минимизирующую q_jᵀx=m, и настоящий тетраэдральный fan из v. На остальных вершинах значение не больше 1; среднее в каждом тетраэдре не больше (m+3)/4. Усреднение с настоящими положительными объёмами и собственный центроид дают 0≤(m+3)/4, то есть m≥−3. Нулевые тетраэдры не несут массы.

Для любой строки r положим w=e_r+Λ[r,:]ᵀ. Тогда w≥0, Σw=4 и Qᵀw=0. Если грани с индексами I имеют общую настоящую вершину v, то

0=Σ_j w_j q_jᵀv ≥ Σ_{j∈I}w_j−3Σ_{j∉I}w_j=4Σ_{j∈I}w_j−12.

Следовательно Σ_{j∈I}w_j≤3; при r∈I получаем

(3)  Σ_{j∈I∖{r}}Λ_rj≤2.

Общая точка граней также достаточна: их непустое пересечение является гранью тела и содержит вершину. Простая попарная смежность без общего контакта с F_r недостаточна; ниже дан настоящий девятигранный контрконтроль.

Для t=Λ_05+Λ_06 тождество wᵀY(x)=4 даёт более сильную геометрию. На настоящем родительском ребре E56=F5∩F6 имеем Y5=Y6=0, поэтому

(4)  Y0(x)≥4−4(3−t)=4t−8>4/25,  x∈E56.

На всей F0, наоборот,

Λ_05Y5(x)+Λ_06Y6(x)≥4t−8>4/25,

и cap 10/9 даёт

(5)  Y5(x)+Y6(x)>18/125,  x∈F0.

В частности **F0∩F5∩F6=∅**. В метрике M расстояние x до плоскости F0 равно Y0(x)/√n0, а расстояние собственного центра до неё — 1/√n0. Таким образом (4) — отделение более чем на 4/25 этой собственной высоты, а не лишь отсутствие контакта в открытом комбинаторном образце. Оно действует вдоль всего ребра, включая оба конца, при любой разрешённой SPD-паре.

## 3. Точный сертификат концентрации и покрытие слабых стенок

Наследуются именно доказанные на одном настоящем теле посылки родителя:

Λ_01<1/32;
2Λ_01+Λ_07<1/10;
Λ_01+Λ_02+Λ_07+Λ_08<1;
α=n1/n0>1/2, β=n7/n0<3/4;
0<Λ_ij<10/9, i≠j;
19·1ᵀG1−75 trG≤0;
20G_aa+3·1ᵀG1−15 trG≤0, a=0,…,8.

Последние десять форм — унаследованные настоящие scatter-следствия; они не постулируются для произвольной независимой Λ. Новых предположений о ранге общей моментной системы, аффинной изотропности или массах не вводится. Три старых строковых сектора сохраняются без изменения. :contentReference[oaicite:3]{index=3}

Замкнутое отрицание (1) лежит в следующем компактном многограннике:

w0=1, Σ_{j=1}^8 wj=3, 0≤wj≤10/9,
w1≤1/32, 2w1+w7≤1/10, w1+w2+w7+w8≤1,
w5+w6≤51/25.

Его **208** вершин перечислены точно. Для стрелки i→j форма L_ij=2e_ie_iᵀ−e_ie_jᵀ−e_je_iᵀ имеет tr(GL_ij)≤0. Взяты восемь таких форм дерева, 40 форм противоположного знака для обязательных отрицательных нетеревянных не-предковых пар, четыре формы 1/2≤α≤1 и 0≤β≤3/4, десять scatter-форм. Все 62 формы и их порядок буквально определяются восстановленным исходником. Формы для общих point-pair теней не объявляются дополнительными инцидентностями.

Для каждой вершины v найдены целые μ_vk≥0 и **один общий** целый вектор

γ=(8838714,4974758,9839555,3278146,−10827487,−871630,−998913,194430,−243512)

такие, что при D=7200

B_v=D(γvᵀ+vγᵀ+Σ_k μ_vk L_k)−I ≻0.

Все 208 блоков и 1872 ведущих минора проверены целочисленным Bareiss и независимо Fraction LDL. Коэффициенты μ полностью восстанавливаются капсулой из исходника, без внешнего файла.

Для настоящего w берём выпуклое разложение w=Σθ_v v. Общность γ существенна: tr[GΣθ_v B_v]=DΣθ_vΣ_k μ_vk tr(GL_k)−trG<0, поскольку Gw=0 и G≽0 ненулевая. Но Σθ_vB_v≻0, поэтому тот же след положителен. Противоречие доказывает (1).

Численный построитель перечисляет вершины последовательным точным отсечением. **Независимый verifier не импортирует построитель**: он перечисляет все независимые активные базисы. Верхний bound w1=1/32 включён в ящик. При r активных оставшихся линейных отсечениях выбираются r+1 свободных координат; остальные фиксируются в нижних/верхних границах. Решаются сумма и r равенств, затем проверяются все неравенства. Любая вершина допускает такой независимый активный базис; совпадения удаляются рационально. Это покрывает вырожденные вершины, равенство t=51/25, нулевые механические стрелки и все прочие слабые стенки. Отсутствует допущение о положительном минимальном размере площади.

Сохранены также семь материальных предшествующих сертификатов. Их точные гипотезы в порядке case0…7:

0: w1+w5+w6≤2;
1: w5+w6+w7≤2;
2: w2+w3+w7≤2 и w5+w6≤2;
3: w4+w5+w7≤2 и w5+w6≤2;
4: w5+w6≤2;
5: w5+w6≤101/50;
6: w5+w6≤81/40;
7: w5+w6≤51/25.

Все восемь проверены: **1640 блоков / 14760 положительных ведущих миноров**. Случаи 0–6 логически поглощены случаем 7; их исключения не прибавляются повторно. Они сохранены как воспроизводимая последовательность точных объектов, а не потерянные менее сильные результаты.

## 4. Полное физическое инцидентностное покрытие (10,17,9)

Семь окон пути z=(6,5,4,3,2,1,0,7,8) имеют номера

0:(6,5,4), 1:(5,4,3), 2:(4,3,2), 3:(3,2,1),
4:(2,1,0), 5:(1,0,7), 6:(0,7,8).

Пусть W — **точный** набор окон с настоящей общей вершиной, K=|W|. Унаследованные K≥2 и K≥(o−2)/2, где o — число вершин нечётной степени, проверяются для каждого нового инцидентностного домена. Они охватывают также более сильные степени, требующие K≥3 или K≥4. При K=2 дополнение двойственного остова — прямой гамильтонов путь, степени тела равны 3 шесть раз и 4 четыре раза. Это используется как структура, не как автоматически допустимое вершинное механическое дерево. :contentReference[oaicite:4]{index=4}

Для настоящей тройки {a,b,c} по-прежнему законен исходный Gate. При s_i=(Λ²)_ii=4d_i и p_a=Λ_baΛ_ca, p_b=Λ_abΛ_cb, p_c=Λ_acΛ_bc это

9p_ap_b≤s_as_b, 9p_ap_c≤s_as_c, 9p_bp_c≤s_bs_c,
3(p_as_bs_c+p_bs_as_c+p_cs_as_b)≤2s_as_bs_c+27p_ap_bp_c.

Новая работа заменяет грубую перекрывающуюся 21-ветвевую дизъюнкцию выбора двух окон полным покрытием **104 точных оконных паттернов и всех их настоящих инцидентностей**. Получены 9 паттернов K2, 31 паттерн K3, 35 паттернов K4, 21 паттерн K5, 7 паттернов K6 и один K7. Тем самым ни одна из 21 возможных пар выбранных обязательных окон и ни один более сильный случай не теряется. Основной новый запрет выведен из настоящего контакта и объёмного центра, а не из объявленной независимой системы Gate.

### Полнота перечисления

Полярность используется только комбинаторно. Двойственная карта имеет 9 вершин, 17 рёбер и 10 граней. Каждая такая карта дополняется диагоналями её настоящих гранных дисков до триангуляции на тех же девяти вершинах.

У сферической триангуляции с 4≤n≤9 средняя степень меньше 5, поэтому есть вершина степени 3 или 4. Удаление степени 3 обращает вставку в треугольник. Для степени 4 хотя бы одна противоположная диагональ четырёхугольного звена отсутствует снаружи: обе пересеклись бы в дополнительном диске. Удаление вершины и вставка отсутствующей диагонали обращает подразделение ребра. Индукция от тетраэдра даёт полный генератор и числа 1,1,2,5,14,50. Последующее удаление диагоналей с проверкой простых циклов и 3-связности даёт по E=21,20,19,18,17 ровно **50,219,558,768,633** карты. Путь от любого дополнения к требуемой карте сохраняет все её рёбра, поэтому эта процедура полна. Канонизация перебирает все ориентированные корневые рёбра и обе ориентации сферы. Это исходная полная каталожная конструкция, не новая неподтверждённая выборка. :contentReference[oaicite:5]{index=5}

Полностью прочитанный исходный c34_catalogue.py, 8955 байт / SHA6728985c7b85aa629dd854cf4e725f4dcc26ad0419bcc2740dd67b3a5ba765f7, также холодно воспроизвёл прежний c34_catalogue.json, 1111066 байт / SHA1c434afbe8a867931501722ac475fc4fe76460ba3eeac6b3d6dc083d83e6cb77. Новый tree253_cover.py содержит все нужные функции сам и от этого внешнего файла не зависит.

В каждой из 633 карт перечислены все гамильтоновы пути: **356940 ориентированных путей**. Позиции пути переименованы в z; двойственные грани становятся множествами граней при вершинах P. После точного удаления совпадающих размеченных инцидентностей остаются **326693** домена. Их каноническая запись — лексикографически отсортированный список десяти отсортированных наборов incident-facet labels. Для каждого из восьми родительских рёбер проверяются ровно два настоящих конца. Домен исключён тогда и только тогда, когда хотя бы один из десяти наборов содержит {0,5,6}.

| K | Полное покрытие | Исключено новым контактом | Остаток |
|---:|---:|---:|---:|
| 2 | 142 | 87 | 55 |
| 3 | 5209 | 2902 | 2307 |
| 4 | 45231 | 22654 | 22577 |
| 5 | 127613 | 52882 | 74731 |
| 6 | 119375 | 38354 | 81021 |
| 7 | 29123 | 7237 | 21886 |
| Всего | 326693 | 124116 | 202577 |

Каждый исключённый домен закрыт **для всего своего пространства настоящих реализаций**, всех объёмов/площадей и всех разрешённых взаимно обратных SPD-пар. Новые числа не содержат выбранного неустойчивого корня и не являются совместными корневыми орбитами принятого глобального реестра.

### Полностью закрытые оконные классы

Полностью исключены следующие **точные** W:

W={2,3}: все 3 домена;
W={2,5}: все 15 доменов;
W={3,4}: все 3 домена;
W={3,4,6}: все 13 доменов.

Это не утверждение, что само включение, например {2,3}⊂W исключает все более крупные W. Существенный механически выделенный вывод: **K=2 вместе с F1∩F2∩F3≠∅ исключён полностью**. В K2 исключён также весь класс с шестиугольной корневой гранью. Последние два утверждения следуют из полного перечисления, а не из проверки одного представителя.

Полная таблица K2, в формате W: все/остаток:

{0,5}:15/14; {0,6}:20/20; {1,4}:15/2;
{1,5}:30/8; {1,6}:15/9; {2,3}:3/0;
{2,4}:26/2; {2,5}:15/0; {3,4}:3/0.

Другие двенадцать точных K2-наборов топологически невозможны:
{0,1},{0,2},{0,3},{0,4},{1,2},{1,3},{2,6},{3,5},{3,6},{4,5},{4,6},{5,6}.
Четыре невозможных точных K3-набора: {0,1,2},{0,1,3},{3,5,6},{4,5,6}.

K2 независимо восстановлен вторым способом. Прямой гамильтонов путь разрезается в диск; четыре его внутренние вершины степени 4 выбираются 70 способами, стороны четырёх оставшихся одноштриховых внутренних вершин — 16 способами. Вдоль границы получается 16 концов восьми дополнительных рёбер. Восемь явно заданных вариантов двух вложенных rainbow-блоков дают 8960 предложений; после точных проверок простоты, гранных циклов, 3-связности и двойственного пути остаются 284 ориентированные карты. Их 142 канонических инцидентности **побуквенно равны всему K2-подмножеству независимого полного каталога**. Полнота результата обеспечивается первым генератором; второй служит структурно и алгоритмически отдельной сверкой.

## 5. Настоящие контрконтроли: что нельзя усиливать без доказательства

Получены и сохранены **два новых точных однородных девятигранных тела** (14,21,9), а также полная моментная реконструкция унаследованного E17-контроля. Они не являются TREE253 или joint110-свидетелями.

### Два усечённых тетраэдра

В обоих случаях δ=1/10000. Вариант small имеет (a,b,c)=(1/10,1/5,3/10); вариант large — (1/2,4/5,4/5). Обозначим u=1/a−1/b, v=1/a−1/c, w=1/a, h=1/a−1. Девять исходных полупространств n·x≤b заданы буквально:

((1,1,1),1), ((−1,0,0),0), ((0,−1,0),0), ((0,0,−1),0),
((u,v,w),h), ((1,0,0),1−δ), ((0,1,0),1−δ),
((1+u,v,1+w),1+h−δ), ((u,1+v,1+w),1+h−δ).

Полная геометрия восстанавливается пересечениями всех 84 троек плоскостей. Центр вычисляется из настоящих положительных тетраэдров; затем q_i=n_i/(b_i−n_iᵀc). Независимое интегрирование исходного тетраэдра минус пять неперекрывающихся удалённых тетраэдров даёт точно те же объём, первые и вторые моменты, что граничный fan. Все девять площадей, центры площадей, Λ,H,девять K_i, ранги и общая M=N=I реконструированы и проверены. Площади точно восстанавливаются как A_i=Vd_i‖q_i‖ из этих же данных.

В обоих телах F1 и F2 имеют настоящее общее ребро, но F0∩F1∩F2=∅. При этом

small: Λ_01+Λ_02−2 = 5199999994002941063343971431/993403599997501251500000000625 >0;

large: Λ_01+Λ_02−2 = 14999999997773285000007378893/178499999999054923500000000405 >2/25.

В large сумма тем самым больше 52/25, даже сильнее нового порога 51/25. Перестановка new→old=(0,3,4,5,6,1,2,7,8) превращает эту пару в настоящие F5,F6, сохраняя корень 0. Она даёт настоящий F9-контроль Λ_05+Λ_06>52/25 и отсутствие контакта 056. Но стрелка 6→5 при M=N=I нарушена: старые q1 и q2 ортогональны, G65=0<n6. Поэтому это **точный барьер замене common vertex простой смежностью**, не осуществимость всей механической системы и не контрпример к исключению E17.

### Настоящий K2-контроль в остатке

Для e=1/10 взять D=((1,−1,0),(1,0,−1),(0,1,−1),(−1,1,0),(−1,0,1),(0,−1,1)), h=(0,0,0,1,1,0), первые шесть старых полюсов q_i=(1,1,1)+eD_i+e²h_i(1,1,1), затем (1,−1,−1),(−1,1,−1),(−1,−1,1). Использовать new→old=(4,0,6,7,3,1,2,8,5) и полупространства q_i·x≤1. Это ровно буквальное семейство родителя, не новая rank9-теорема.

Код доказывает (10,17,9), все восемь настоящих родительских рёбер, точный W={0,6} и отсутствие контакта 056. Два разных внутренних апекса дают одинаковые точные объём/первые/вторые моменты. После собственного центрирования вычислены все настоящие гранные моменты; Gate проверен на всех настоящих общевершинных тройках. При M=N=I хотя бы одна требуемая TREE253-стрелка строго отрицательна. Этот контроль сохраняет реальную геометрию наиболее большого K2-остатка; он **не** доказывает ни его механическую реализуемость, ни невозможность.

## 6. Проверка, восстановление и открытое дополнение

В новом чистом каталоге выполнены регенерация всех восьми целочисленных сертификатов из четырёх полных исходников, независимая рациональная проверка, полный инцидентностный перебор и все три настоящих телесных контроля. Все размеры/SHA совпали. Затем выполнены отдельные холодные запуски run и check полного lossless-восстановителя ниже. Оба завершились TREE253_TERMINAL_RIDGE_COMPLETE_COLD_REPLAY_PASS. Это не только сохранённый лог локатора.

Построитель проверен при **CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, threadpoolctl 3.6.0, OpenBLAS 0.3.30, SkylakeX, один поток**. Версии и архитектура буквально проверяются. При несовпадении регенерированных байтов построитель отвергает результат. Независимый verifier, генератор покрытия и телесные реконструкторы требуют только стандартную библиотеку; проверены тем же CPython. Assertions включены. Случайности и входных геометрических файлов нет.

Полный восстановитель содержит без потерь **все четыре исполняемых исходных единицы**, а не ссылки на них. Их совокупный JSON: 35415 байт, SHA209d3668e11d486da3c9e03e76e4c76eb269a00d39a58ac27be45c8676e62929; zlib-представление 12823 байта; буквальный base85 payload 16029 символов. После декодирования каждая единица проверяется по собственному pin, затем самостоятельно строит и проверяет все свои результаты.

| Полный исходник | Байты | SHA-256 |
|---|---:|---|
| tree253_contact_build.py | 8538 | 9c2794d409ae76843471a0f8db971abe4037d113397ebe3e04fb84c94f601b7f |
| tree253_contact_verify.py | 6134 | 1f0bc693b1168909675c8d81e4b7e4b90d82d173d458810791cde93cd774d959 |
| tree253_cover.py | 10420 | 64c7ab014aad323b878666a91594c461049bfd4693761539faeda981651373c4 |
| contact_barrier_body.py | 9444 | 71c6376841b5be6068fbb3f2906cfe67d3a9f4b1d09347b2e54785379cc8292e |

Все шестнадцать выходных pins, включая восемь полных μ-массивов, находятся непосредственно в OUTPUTS восстановителя. В частности основной contact_07.json имеет 88507 байт / SHA7a1bb86e7d5410d1a4df4ba3e4261775408ca6d3956b8f7d409f49dcda91e061; полный реестр инцидентностей — 29402372 байта / SHAa40bd001daf35925cbaad0997ae2ea1f63f58a38afc6a165a28042ad85c5f7d2; полный остаток — 18231932 байта / SHAbe8637b655bdf223e76654479a1e72fbb949f6dc9806a0178f0c44be57f7a9ec. Никакие продолжение-критичные строки не остаются только в sandbox.

Сохранить следующий блок как **recover_tree253_terminal.py**, ASCII/UTF-8, LF, с конечным LF: **20855 байт**, SHA-256 **804efb2bfda43123f22ca5380d63083e8d0ecdf2403245b3cc2712db5265a20f**.

Команды:

```text
python3.13 -m pip install numpy==2.3.5 scipy==1.17.0 threadpoolctl==3.6.0
python3.13 -S recover_tree253_terminal.py recover
python3.13 recover_tree253_terminal.py run
python3.13 -S recover_tree253_terminal.py check
```

recover требует только stdlib и пишет четыре полных исходника в tree253_terminal_recovered. run заново строит сертификаты и выполняет все проверки. check не запускает численный построитель: проверяет уже построенные коэффициенты независимой рациональной программой, вновь строит весь комбинаторный реестр и три тела, затем проверяет каждый выходной pin. Любой непрошедший assert/дочерний процесс останавливает запуск.

Ожидаемые терминальные маркеры:


[An encoded source block is omitted from this text export pending a complete content review. This passage is not a complete executable package.]


Пробовались также более сильные пороги 41/20, 21/10, дополнительные контактные комбинации и совместные двух-/трёхстрочные локаторы. Новых принятых сертификатов сверх восьми указанных они не дали. Эти численные неудачи имеют статус UNKNOWN, не доказывают ни осуществимость релаксации, ни оптимальность 51/25, ни невозможность тела. Предлагаемые числа не используются в принятом результате.

**Полное открытое дополнение определено алгоритмически:** 202577 доменов без настоящего контакта 056, каждый со всем своим ещё не закрытым пространством реализаций. В K2 — 55, включая все 20 с W={0,6}. Наиболее полезное продолжение — связать теперь обязательный равномерный зазор (4) с реальными площадями, центрами площадей и объёмом вдоль терминального ребра в этих полных остатках. Общая Λ, все K_i, собственный центр и взаимная обратность M,N должны сохраняться; независимые коэффициентные строки не становятся телом от прохождения Gate. Ни приписывание дополнительных общих вершин, ни возврат к ложным цикловым/P0-посылкам не допустимы.

Дополнительная удобная копия всех исходников, точных результатов и двух журналов холодного исполнения: [TREE253_TERMINAL_RIDGE_bundle.zip](sandbox:/mnt/data/TREE253_TERMINAL_RIDGE_bundle.zip). Полная капсула ниже не требует этого архива.

## 7. Полная исполняемая recovery-капсула

```python
"""TREE253 terminal-ridge exclusion: complete source-only recovery.
CPython3.13.5. recover/check require only stdlib.
run additionally needs numpy2.3.5 scipy1.17.0 threadpoolctl3.6.0,
OpenBLAS0.3.30 SkylakeX, one thread, as asserted by the recovered builder.
No attachment or data-file input. Assertions must remain enabled.
"""
import base64,hashlib,json,subprocess,sys,zlib
from pathlib import Path
PARENTS=[['minimum-0061',49087,'5bd7dc9ed75e5dcbd403d23bf0c22fdaaf06d0d60f54066507505173dc3ee910'],['minimum-0029',36226,'07da26de37a7076fae43373e6ecd0c85ba0b45ffbe359ed38b707c462083dd8c']]
SOURCES={'tree253_contact_build.py': [8538, '9c2794d409ae76843471a0f8db971abe4037d113397ebe3e04fb84c94f601b7f'], 'tree253_contact_verify.py': [6134, '1f0bc693b1168909675c8d81e4b7e4b90d82d173d458810791cde93cd774d959'], 'tree253_cover.py': [10420, '64c7ab014aad323b878666a91594c461049bfd4693761539faeda981651373c4'], 'contact_barrier_body.py': [9444, '71c6376841b5be6068fbb3f2906cfe67d3a9f4b1d09347b2e54785379cc8292e']}
OUTPUTS={'contact_00.json': [85463, '6a7235f7be05e20254547550e6c20a9be72d9503739d62323da2658e2d07826e'], 'contact_01.json': [85581, '3ecb5e0752e7d7bcc30fee33c289ee60f56616a13909c03f63972181470af181'], 'contact_02.json': [92612, '94b5abc4c902417363ba339058d413b875bf5c5ead4c5f2132cd438f2f30a7b2'], 'contact_03.json': [88795, '2580c7a4a8c06539edc63dfbac31c61db2366d56d40bccfc8857046869d4bb48'], 'contact_04.json': [82172, '8d1b77b14f5c51b93cff686f09e6984d92404469c00c29877c67a7e8288bec59'], 'contact_05.json': [88125, '4d41bd6f1dd981168ca75dce6d210472adb911356b96876ecf923ec22c296f61'], 'contact_06.json': [88245, '2f96d780353b5e7ce4b4a36e766408e9ec1c4d45c99ec38142880a89a4c12917'], 'contact_07.json': [88507, '7a1bb86e7d5410d1a4df4ba3e4261775408ca6d3956b8f7d409f49dcda91e061'], 'tree253_contacts_verified.json': [3976, '4ec252a64551ae950f984eddd90f9eda06e0a8eaf2fc55e4844305ee30983206'], 'tree253_domains.json': [29402372, 'a40bd001daf35925cbaad0997ae2ea1f63f58a38afc6a165a28042ad85c5f7d2'], 'tree253_remainder.json': [18231932, 'be8637b655bdf223e76654479a1e72fbb949f6dc9806a0178f0c44be57f7a9ec'], 'tree253_k2_domains.json': [12782, 'd8587c64d96cfdd751f8da0d82e785f26563e94a2c9cb6a03fde91b69cbbfb11'], 'tree253_domain_report.json': [3225, '6bebead6c3e5a6fe355fa82a930cd59041fbdde81ab290a826231e8aa8fb308e'], 'contact_barrier_body_small.json': [58919, 'e01fb35a965e37c8cc017f210cbf8399056dd4156e0161ece907a041ace13dc3'], 'contact_barrier_body_large.json': [52375, '957b2365f38f143c8e5ba728ffebe0ee33a344397e09298d371dcd94785ce801'], 'contact_barrier_body_epsilon.json': [68757, 'cb8d451b11473c1689f9c43faec48b83d67aee34fe0df9e7e0a81c841d4b7740']}
PAYLOAD_PIN=[35415, '209d3668e11d486da3c9e03e76e4c76eb269a00d39a58ac27be45c8676e62929']
COMPRESSED_BYTES=12823
DATA=(
 'c-rlKYkT9i(dhT{E0p$WMM{uOQg>;wPrY7kb{ogLv7NL%3ST|E$)+Wd3Q5U!HhX^inHd1QNp?2xdwM=K+gc<pgTY{CFc=KL&wujb'
 'D094Q;W|kY2Fb#W{il=d)1M}P`kDTHjDiN_@0@kxF5bkqK@`Nhv=N0-&{;ZOkTtw`7iB?$fRcFK$l`|M-$PF1J$2$}{nU_6G(2aU'
 'p8Oo0e|pO9;;4~kPUJg@-&luk;v`QEEPT?qj2kysvzgWJHsYjlABRz9nnuH0JK+Xu3#@*QmPx#6EE9km#!=b`H`_SL8t-I6!$}+O'
 'WT6m{%i?&Q7xLnb8%7RQlx4O~b_Zyv5})Ap=SaTXr*XvYoD>VN^a-l`9Qnbr;m4WgFjt=>LAFbvKf8_g*m`O#0qsZj)Ci--ui=)8'
 '=%Pltb1OBn-F6*lkDZt5cuAb5m0FrJH|>@?x9pAsf8fcqnS3%Z%@DavKAD(iid+fQ4+wSU<v>MeL}Qq)Fpk&zK(zid6yjL1<v?a5'
 'TsEROYxoMlWgG>NT<IB=*2J?rU)fmcp7XE~tW)4BNSWW;)c1SrdE!L3f!5V^N?KKt^i!Ww!%C_^5?)uDLl`=Iz7Eq&+c;b89ZMvr'
 '1S>iAbj1xQQ)_P>L>f{`CjgC*N5NyJX<@y&6{C^>5_;jxL&RNY*lnHaEwOM)beJH=htUoRLfvFop5q^euhT7;ouA?_pFf^%1q%?O'
 'kYr=cIs$D|p+J~6wp^k?Z-BsdLhZ~SJKH0Cs9M*l{Ho1OiT8?g0e9jifwL+`afPhzq$$WxW3li9cXzv3G(c(_SRO>-#7S=VI_DN8'
 'ssvy*Y*cHe8)v<4vgR661NaTLX}FG~CJ<~B`vEUifOe1{x%N&onQ7<@fBX2;#aALa)!`DV;2|n*VX>YljX%T|>&)Q-7W@Y(KneCM'
 'H&308dFnFp>*4S8PNe=EZP!i|q<pSnHD>DgKTYeH%wT|!fiDKb*Zc)v=>=$}Y1D+y?l4bQGCPEcC~a0!sEXOfN@g3XneDrx@FTn)'
 'qyv$*PU36=P-rQa0t{*@r;MU6vPU3$uTQD+B8eZM4kU>V5Q2z2;YAM}Q(!21EV3|7*Qa+uczc&|>M@qba?r*vTRs=kZMK8fBm6&T'
 '-4%=sO-lKTAK0DZ!vY;9!0L8;F7PVQP*2o8^6NH8HXKIRU;{Q}z!S`3BN*#xK4`yek-<&95F4z6bypnG3r@RJ*IDy9(q*8ZYTXt{'
 'ly0{M?fI&B>!KDBEWZgO4QlAG4Z+@^-|>}mliq;~HB8G|zbG}9v0qd-p(Oidt3zqyn1(|Dq#gn7!36bkqdc|&(@Xp)Xe@MEq$8WV'
 'QnN+OrJhnr=<6QvPWk6AFs&gK{1kJ`^PMJ880)M{T4c|Kik}M*s80;LAR$1oSt-w~<;j^~e@yeGYsXvhx!b|HC1U&I7?WTFp{ca~'
 'ni~`9!+dXZ(QT=SS%%euXtxOxCkteGH4SBe$WPFfBny0v0O(V+1oi=+D|iHFk5GQHr_r8+QE@0bLams+T<@W#`w2!d+UJt?O-a&Z'
 'DdYvALpkqKLk_8OLIH4_!6@P^DzXF#jton**Fl>hTBKlcmL>>u$JYN^dUb7NEX%H7IfEq496sAA%hdDoig#%s1Hvl6M}$HB5bcDv'
 'UY~^kMF4}AA8@8E_-w^se4%rd0TLrjOa`37=V~0CYB5P7nup{xUFs9m1fC$7^zZrSa3Y8JzK|(m@};ymWVRNvdtKK>k18Ddr4Vm5'
 'W?}-%nFAU+**oi9kZRb|hWF(0IdUlC!ten~<OyOneYgwP0U->f^;Zh>3A~*++iei}8d()3v=Ino&pW0q?4oZty;?T4DsjXl!#*gV'
 'Pr<+v*rFUYY*R>-5IJGaq1E{l)rG1|JQ+6FE=7h_$<Xyz#)P^pQ`-1DF(w_Hr_1C!-i&q+n)EM<8ae3uqRp(FrlW#AVw6$GgjywW'
 'dGctSN#4=C5cS!S7KwtyqKf*M{B!i@#_aLV*`>&FjVuX)V*nCr+(0fPwrg11WOo59J;GZMPFT(aS>oIUege<1=J^E{LSYsLP&A1V'
 '3Y2wW0ptgM<8HTJ!wMyqiVNjyuVx0Jcl6U}e`GeOh^3%utiN&(^(B<t$7>KBnA~AzUxrDV;e=-3#5ILp#F5YEDuL=R$}QQ`r4to$'
 'OC*()LOBJJq-sY03536p98GWnE72TCZp-m0^+uSeNN$+IMRRHl5V|hyZ+ON!m_)Yh1_&S)7sN+<=zl>rC<XTaK<Nc6`x*`T#vW$M'
 'nCWdOFa^X93BFJDLvq_wLBlpjNJk9quC%X-yg&v~u!R%gX;0+TVNL|?g*h(EYghqlL4v>x-VV^yPc7r<!~*U7x$yz`3TYQaStAW^'
 'qrmS}`7sM_6PiILM>rOi!Jwvqp_j<-ewfl?S}nsH!r(5f4oGsH6edg!`G@6yz!C$Ksh%KAbd`WqDOEE&XvMnf#Z@)H;O=;&F_T~e'
 ';^U*SU2YAGO@>I!ySDi4$=|+Ev=Lg2ZVV>UXLADPsKt6PV@}A31^d4@0S4^iQ-7ja@YK`4NRA@`VmoD?iGl00F`2>u2G<QV?6B77'
 '(%_*Vdzyt?PDt$RDG(1NB;3*(N;0I7SV+`g-<6UJVczSngjsyg_SM-B!Rk`|?{vkB#9Db*p;^I?V1O4*b?#tEOm8SKkRs>=Yf@ba'
 'it#FYMQc19@>~jq&!L^Qw5QIaUSB0v0O?11BT2JDI}tm^iv+X8+R$Qs6_3QGY5p5ghoDP7sA30|sqMYRg|R+eTEcF(dP37#q~##X'
 'Adn&F_rl1bMUQ116Z=Ckw<T}v$xN206#B?<Q?0C%_9?mv%HlgWCrGB#0oF-3e?$dYo!?bI7HEu))IFOQm5(J9Pe&=94QZau*Qg#f'
 'zS`bmON*rzT9HCQGE#s{s5Tf6B=AHHi=hU^D38c<^G>1mQ!(R2Lhm1&3rdp#YW}+7pB|?(7ClbrLeD=(X+i4tA*o-Wb^GgSE#|L3'
 'NNg`acWUTMW8(2t6f0KOR2~XmhqoICh+m$8WZ{kif;i>R$6Rj5h2sZh3_PA{Y8j`%$f=)DiH<MrE^?L_*I8l=Bl8{DAyXg!ygM%~'
 'B@~YoN)ow+MhY4z)XnscAK)}~lE6XxW=hLLVd)%YGAzjJ<}2i)FBN|bX{+M1l_$Y4YF0~BiwZ@Hz=TCY?JH%5FS^7;rOoFiA^i&z'
 'I;BQVav%Iq<sDjNpK)X^0<TZ~6+dg;$w8jx%F|zA$#>^fWlHs0#|7q8u2q>N5BUkP4H^aL?OEqVwjnLOak3W&T8@BIaz#=Tf-ph^'
 'rS+D?52_t_#Ntl}LM<TH`E@Ks`2q!C1=8uST8=Q;v~KH6Kc+dM4&biDnJUz5HpB<skD&#eU|It3cZ%Qu4c^}aHB74h1HyLf7Ktc4'
 'z`DKl13-e`!bhNJNh$83AH3T2!+rxbzJ(UmZbSj*hf*Uy6s`jDmj3{XhaSEqhXt-D>GeXTzlVoj?&hMTRqorMN&UNG*@AubF;}{s'
 '>cb+7(b$AGdc>4J4U<I0M$I!J2NLL2>=LZXfT3FF2Qhd@msCeayJXIko49zkiS~tP0BF(jrK7zBU{z{f(uDJV>%E+ft!LVM|3a5~'
 'o%hP8e~>*nq|$c?ipmpyQl9T?KxM;+yrWkk%5t3hh^8hq71Ef!JI9R!{V0S#H@*cejUK=N{U-42(^g(1j?~Vf7jHIk)Im>N@F-W_'
 'xCW8lFh<Kz>AU%ym3%Se94h$$$}Y1#>*`;KD8ZWCx@hjhV7er87jqAPPks2q@;o7fl;>ieTg~%qQQyNn&#rkp9$QbZxLLNCEBF8w'
 '%qo)<2M7|uMz-4Ui@S07V~QX2-W^}}sV1W*?K7CXUtV!?{pkmOMG_-)hfq;m1HDkV0E{d2xl=EIc66mV6illuy#|{2ZThwB*Ov6%'
 '3Rk1p;+Z^C_MO(ZnAI=Yka6M%3D*X!4@<8uEWmKjVaP`M6c(f~<%qooT$y!oZHAfpA^U$0nJ5lC`h3rodoL`zDJsk_X3DH!G*N0O'
 '_WFRh2$@ixXOpbmwRO?hUa#{iiW{IlC;=}GP@fIHJX^Cm^53E?=AE-U-wNgV%6O(LA7~E7h0s^8eUbq8x49pBnHHjtA<Uk5^XBTu'
 '+2ZoU<!tfp?0j~!ID7kd_`N*;*W&Wy&Eovy<;~eS{GNTH=c|twi=WIUlY1572i*ZE>mfRce`2D43yKziRTaH4`9{7c7WlVNa>k@{'
 'OIpOa39KFvt{3l}By_+&<}|GeKnqnQ<?qhfHU{;=e_%fM*@d%leTQGL_xwHkj(^9#=O5T5{2yS6Ji}a|+ixM?EMDVY7CZuuX+61P'
 'A&B(O@#BYuxya&$!M}xk+=HiIuq0(5!-9er0-wKgfc=?@X{aVYyOSq|Y2H*r)U<gMhTzAui^a?wF21uC#$fU3>}qy-lMl&1KHR)t'
 'oLyWjzW?|=q+jD0l|U)*0LeTxjpkHk2!>k#ABMNl1|G49lin`O|GhMlPrIAV#ZOnAJMW)QpJs1=`Db!bhAIizuaI*95Qt)ZNx6Yt'
 's*)u^u#hwqPIo9ie}?yualWlW08j@zprgfx!xE;WFv18E4^}ViT@j>_B~a!_5e?%87%2ihFFnuUmgV))K2jg0D6jW<HL2HJ3D?i#'
 'NtgwjR3pEXEd2<g=sa)@15Hl+-DZp1L9(_W6s$$y?_w1^rTiw@1+Yv+zg>ooFs;ep-=qoFO7rKRqo#fmL>_RFrcW`9MQa|5@L4q5'
 '$Z7572{sCK9umN7;XY*nHvWLSj|p(8rZ}yv5K3(I?b*!?c<=hU$)Y_IyHGGHdF@YUAFdX&f1b~<M9zIAPffdA?CR|M+0E<<N+DjX'
 '@JbeiO3eQLU)LYb0jm#}=O5mJZkjFLoLyagm|c;Ml2X@vb|<V^=(O{*ORRD=`*Z;*AV1%K|M7D1)9mVI_D||q1!95B#~*J#{dm))'
 'E+f5EfY1prv(+C^+R0t;=!c-$GTKRUIgQ6+u?*M2VxgbFD#({4hiOm1z5e*))%i@obq}Drb(nu*e?k!=9ixVM7q0zs1lM)EOT0jY'
 'VyVcg449~s$7P|aUWOi8aY+CQHb|bpID3PD8p;9f;hqPGWMdmfQQ%K$=OZlnr=b=A36cij40B!-l!CQnBvqVZ{1mGMR6RIJ6h^l%'
 '24ejWV!gIW?C-ox!PrG!C3~Ih7M|nX1wTh|3WBo_6Oh5()<?g?$4|4%Hy3Buz!g`sn}2<p@#gjFY3;0ne>Pd3dHLh_i<|dXv$MC?'
 'piLp;`%edH-+y;ePlLhxblk`hs+`YX*1N3Pcm1L7jRSw!5Bk36`aPrTTU~c)c$T&F9cO6_e8V3Y%YM%o4En~fZ}iP!*Y~<XFb1s;'
 'YV7>%dUnm{=$2rOK5GnYn>CtNQ)dlG!vxkCR?;li=wcdc%n!=<2*&Ze=MzlBJnb9x)RB4GJ4o!Cr&hm-O8?V`OTc?R>h}hKPIKT4'
 't!{rgbOWOwSccW_^?Sp9-v|btWjJFu7+U_gZ*+&<u|Kf7R@Zl|L4OojzA+qGgP@5xkNW))kfGTPJhvYJxvXI54_(je8p|N)c0Fq}'
 '4g#d-U|<d$vpY7%p3z+ny5pf`j?CWBaF*~(z{b|V1X?x6J-6?;Ue6mFRu8B@=(<i9YW7Ed&+NLRVc%W$y*{Xdp4VSmX4mrkUU#&#'
 'mR-Xcx|YCfG#vMlcKwmz4V|7d@{B>h3uEsMy8hC2ysqgDOy9M-gMr^404o66OK&vl4~^bnG#L9m*X@l2Fv}bwW+UHpheOxwVf&^#'
 '?t0556kQtQU@#u_{IS(Ddc6U35g2Mb8V<d|&>03JYcz5LuRoTUnHFN!gWkCQU}^gPcx0M`k>?D7DT9G;nMQADIlenK&2E3-jt8UR'
 'An=xB3+QZF0D7<-m=c)Pqi!z81AjO&y8SK;#Lx?RZqMlsg5hA$Ge*HU@JtUH?0aK)>;mBdCBqqwot|e}V{<5h0mlQdp<}x42rB#i'
 'o@w}|)AN@-7=xe(BQzX>YyhqUzdHupM#~|PZoKS`eb0BsW?&#@(#8POJQNm&3dAf;*pL6M8Cn3|Vw_Q7b9{~Jw@Z<aXJqo6k^TQz'
 '^2#Q55&U@eLh$2R5&Y=L;76zKo)W>2XCe;o442CF;78|Z@Z%W<KVo@~e;B?__xwx-Kc30p$9;kHSvmO8IShV0Q^AjWF40iIkNXL='
 'Gk@&t4}%}`)}IT0JUbrzNW&AaVF8#quw2y{?e+6_nkDeS?Z9`MX^_p+pcuQkJx%UPp63#^M*?>&R`t<#aPBYGZeh8Kt|L5Ep0-<$'
 '1NmwgxV?reG!ZCPcS9*80}L$)4`Gqz`wd^^qvVDeIqc<BOOcK`8he40@u3{92enl+nr@s_@S=3$id_TRl!Z1Kg3~AHcjbU+%cb(a'
 'ar4zH&1!{hSGaN?kafBpbOJo+iUo{UnEVQ=P4=nWx_HoS+^NBVrEuyswi7>K=ris1f>{)M&Kjs8sVX;IFnDq5!QguOGzuO7D@1|J'
 'J)k@_2@4h=;eH}K?2ppR{h0R#TG{J*$1Cr;eId5P7>s>6nHU(r&G)dvx2N$gd!fW@gJ=&}Ve6aUG=X2K1iDzs(v=&bd$ti!)as+$'
 '9ybW7zvZ@&mdiC#4A<rwQZUz0_;LabE-3O}(_iyJ;X%ewPQ5j<+w(*YZ&KaOA@Y%F4q#rt4*zPRqiI-?`A}{T7S3#>h}^6r{(<pz'
 '?7zZaS114kSi)4KH8M_}bnH`2K6L2UwRKQKzq1uiLHIcKNKj%zLFc;k5vP>J3t*?9NFPu?AiIfR;NqVMZte<Sp(tUM@=aC3G)g5X'
 '=r%85%3uj8z9fIBq9#<hqz@=VKk75WFjCZJWk(oE!BLK>JJ0vhZQoE~mU7(l7zU;#AY|3Cmtv7JAeU0)K7USrg!HIQHvg4W8W`RN'
 '3_cMJ=c7;#RuCrwl=p8`DD}ArWzpLu*-}xXDb5W-<)cc#5JpDGJ|MzWf3bAJ^)3mdBWH<=RIX_Qj6%_d@^4?4(?p6BM!F5WEOFMd'
 '3Jy}nJ214^`wjIS1A9TSU^~cgOFnMpdZyj$x3v7NW9n0%N6R+OUe0<QKLkGitc7fQEL0Om`O9zUZ6ri#m=g~JibaJ=uyn<x^33kq'
 '@g0>s00VL<@REF*0=bGY0CV=eP~H?SxhJKu|AvQ?J>P<m<uf^lq)J6ZTMaZef$`zkoyZZ<s*tTuKk#UK5<DSZ(+hn5HAv!A(;|nB'
 'rMp)Kt0Dw+aMiezz)UXYD;6@CeXJIinTq#&^kS``9%OVdT@i_`MQFPiaU#gCrN*h{>92DTTbnP}v6E?Qe5V#Vra%<>iu@KK650j('
 'b&d*HL@_=OtRtY^<<Nc~m?YPQ^nWSVB&3hk)y#1VQlY+Tyff^#aw_X(JZtuv;*DQ<w+_NAfdJec=Gbj+8Gi`-zn7@8VZIpPX}nwt'
 'yGsU8lgzv}Cok+5*H}7aDx={Z5Z;|5AAsoyPsj-P1WhW&bQOms^%!Tuqlk9_L9gb6;Lj6VHk`HVN?|@pFskbT5pt5md4dZ1>B9p|'
 'XUC#ipa*}SXKdU`+Q1b^{9P6#+6R>Q2fdvqJTOekji)-n8pX^~tQC|NQWGrHOE^za^b=u7%MucWiXKZRb;XwAk&B{RKuo=*nK@K4'
 'VLB!a_<RCF4_yBNUY?4f@%8Bw#zb>ctkWIlEO+ZQvPI<R%sh?gxEgBpjguweqxST~cDvk|K~@BF11R3y_~AYCJFhq4eUts2LAiLF'
 'g`4o#fR=Pby1eX)t-^a*cDG{}wX)FU8?G8;JH;AA`I5S|1SK<P$4`uY>%<(jT2yAbbUY5pr<<I4qo`bUXvjhE?&3A}dX2%Kw<q`-'
 'q^l?GjXu39rH9cTlBmWxzXEEKVEygy)3>F!3(CKJ;vJ|6s=*7ibLKpTsmU$+wRl%Qq4^qKxS>yPiTWLGo&v(6_O4X>?LqC1dAg%='
 '@1JNGE5zRf_hIL?A2iuH{5zm1RN7T5t+0}hl{PEC$=*I!Yj;>{Eo!Z?*4t-l0bz(a#mNU?r^*{DfYV*8Mf>~>T=dly7@*5??S~AB'
 'r>WR2!j&Y~i7?y}O{SHh6en{44KkOeH+WQsYEFE68su+2E~)dEwkedtbxD0eB4(fpD@jh<6phaKdFOySE0hBtnfoofIYyo9`NT&='
 'UKqm}{Ci1)d}t;RMQ=_^G^xEk*EqD@Ie-V?nhePv)ap&I=K^0@m);RXK>RG=x^vkh!M(E=dH<QlZ$Rhl>W#Z|fV&qh;S0!2yCgH$'
 'T)S>xpWNuDf|pWarSz91)8Kal4Q`+&GM}5`j~_a>+BL9}8Fada^awPrBYu6Frb?Re5g*vZp1KitPh}8fmOM?;EZEAEU)K?HBL;>u'
 '%ti}`H`Aw0lff#`TP>Dh1lGUYo>bLw_hy?lX7q!R=LD<Z+I5<xzeuPF9Y_Eq&7M9tYz4x9;#diZJ@r9d?CYdN=35~t{kjhB1TCuS'
 '3oiGA6nB1c8@Z+3KK;#qYHPQ<mcJ7trQ_*GF9~oblXqm{d=a5?8n5UC8lX93pmJL$hG7=&Ah15y+dGF-krQ?@9=C+$g(CxLo!#8u'
 '!J_@tmk+w|lHq7YPZ}oa@>JOgfs5BZ?+CR?Xj^Cwt>arYu(a=oYFu)kDY*~Ui=tC)Sw8QiB*i*&@;L_x=kJQBH`nn>E}ns!I~t&a'
 'pW4*Fmj5&bHMvu7yXl)Z{Ed1e*rE!ukDUFzyQ342oMy;D0zLixuKsREt37Q<@`kBkP+Z%KSQvPC#eu$UoJ<w!H0Y(_R2*EOei24z'
 '>)Tn9#K~l<Vui)9xA;k4u)Pdi!E@JQtM1L&`FA&0@Mm#-^YK%YQ9s#oy-V*(s!FXqwWm3rpJF>vj##9+s1!^h&(XusK+!jxj1~5V'
 'Xs@;iZ_eIa%oZPRW>-x{#sVYT;5Y)%45hyY_8uvtr;1ClJpN-yina2_0U;oMx?RVvvj(~{(ky6)i(NJ_bhl5qO@~=txP4;T9d3SZ'
 '<9O|5YqX7UcaE~;n5e1>($Q1scz%2zBq?a2MHnsP`J`)ejwi<P3`i;58isnYP$d@vhe}EXpK=a{^E9oK?n%GNn&yc)JTc&*doqAu'
 'Y(Z^bo-D&PjD&jCny^HSlc1?jtDuXw#TwLFmTIQ54av{-Y-#LY)eGa!n?TrwD1&hm@?0{c)1fvX<HFg7n9+=3h2pNAv{|aJK|$Hi'
 'rp@35*1vZkP9BVR(6p)N2K2m(J<c~i^?c#0dAm$FI%?}^+EkRcDJ-j31-uq0hUyR>Iwx?Y0|>L?HUK<SQE>n~aB{+9gJq{x0}r!F'
 'U(F|m2U6zqxlqpKjga!u-v=Aa3*4X4bcQag{Qdwm%(S68hlC-4x-8i-=>mb`Bn)mrr_=+K0}&(}r5NXiGRCy#kC)$Fe*DK}lZ908'
 '7UXFIJqsfa<)*3UtOL-~j~dSAw>r-6fDOLv<cmBS;~mCkiFhK4(aJ-yW>+^K-hDX7Pz(yi5&?8#8<}Bv0RO~1JlPd84;{-$Mq#R>'
 '`X;4vdrDZfOrzBr=_gK_J#7OG`DoB<>L*!Dw`%BYv&*aOzOIT=LNsdM@TS!SCFISU^bWj9ztmmlfy*s6D4?q0KCg-@#C<Z1tKb|{'
 'aXG6suV&xQE@xL~Hy=J;E+BdF{fF!C&u-4&1M!)vK)|ZOFn=*DU&OxrB|H}Wl55){;O+A5hqp-MtJ(R-pJrFHx7b8WwNcZ%vbGv9'
 '1x42V7Y3Sqx|kufA1@alF5k{R&EU`F4The;V1jBdK~X^=)YuC_B)W(pTPz|6Y`F!<{bGUYd9i3tgql7YF+!0Wl}mrh=MIBMj1f`M'
 '9TVXD28Ed5Vw7|=YbX;fVdw}TJrH_D<j7O$(x2{$X|@lp{yAx!(GXL3$7Yv;a)X&Ba@=*`ABK_CV@Uo@p(EwsURI4G0VC@!4<Ye3'
 '{|V*zPbkNKLOK2u%JDx5<q(VUGkMci#6{Jqa~ReUKiF+Z+w1v>BoSIlaSl-bNZ>&vtg+Q|cU#@F==p1{R(WJc^{Ou@eJ^g5;_{BG'
 'dvUYXy}a4#{_tk2`=d8oMWv0TZ}`1hW>v1Y`r7-g?rq(!-$RDyw>oC!02exi1>seoI$D=$J-%bN-QqC?xnIllwkD%JnBE%Z5g!_s'
 'ukYZBoyO{>EexE%=$%HR;~lv_VJwf?(3u#-iMoRkC8evebYcNv3ESjU$C5e*4$$!eeM)=tdB{(4#EsuJi#-W-1mx(gG<gl3C32*a'
 'gsZJovDXjTm4jFUpgnb6I+=s`LLZJ5$$b<{FiW1nU<56<^IeB!_=q<LJQtgy))olQCIKp)-@DIq%G{771(T^O@9?;ehOO#HBb&Y='
 '_66xixa#?S35^Qw8}0LW7?~sX%=1tfswZP%@Z2URPQ-IwuB-rr^*Y6&$>Pkh=pwb7D+n*&R8N=-Dq_0h#npZl4D#)FBof=n)*lPU'
 '3p%wh?UjMX9zMNRxE;nj={1_==V@LHnR)FULA(eXsDT8YKXH6tQ(OB&!swbJr3T~{Ka|uN4S^DVXhsD$;HwjPP>}{Jmn2$$iVf>Y'
 'W6wX$_Y|K)P44AFjT(W(@(%l_mv`8)T%*k!bG4s+xQ%zX-!6NsD2d9FmY*82Jl&W14gW;30F`An_Um4^t4F|SyPNYKav=6Lk65Ga'
 'ajFI-WL%&);9H#T{bZM)#cUu>cUrA<Diybw3uwn&kW8M7E_?{<nB9pBW`1Wau74FCQ@qF#{>RtxRN>Px58D2EIGwvN2XqLh^iJ1N'
 'jB$Hh#Nd79*<JlG{%)M}Um126x6K9Uwq=MX&R2h=ozl>wAaFjg3JD?R6*A#ENf6?lqv}S@WInMg_h_zRu`kF`FwJ2P<RzD@{6eqo'
 'YokoUt^Uj<m(T3Ym$Mp=eA|*-)^X&y+WbyU(cI%-2v2V0?D%+kib)88vbIP2zxLO%@4s__0o`5T2N_0y>Q!nSMjBu#$w_*rd>XiA'
 'wS09rw?xFSxLzO=cMBAkr0CO&oF}3E7SHk^sUSOnC3n2R2{cZ4m1)tL03~$&NH9-WqV9zhTMbdZFQa@f4@?WxpTS!{&5jb5HkCl#'
 ';ZeOO5k6a(T$G5_oCp4rtETMl5Ro1)x`+@WC*yt{JAUrnQE_6GQ*~eGU#rv>zBa5Ymii(NQk-kURPup+(p55g;V?PO6Mz7ifWIZc'
 'C$}*3NEaEyWj4?KWH2Q{-4G9`q`Ydo=C0A{1(y@s^p-;_w@rJx+2PY>*R0I~w*Y&bAM__5-lI-8aAbwyeyitK&TV$`vN@vTTfX)-'
 'T1$H@b6v^XT5`hbtfk>f=Aa}6%Uo29^XeU<6s&y5YpW=^hMUjDk-q2Ly?SM_g)w&rko2j0n3l&u=2u2NFz9>P0gqJJksf`9ewh0B'
 'T3!H3xb5=k=WR>76=vJYZr`Fb?bWRlS!*o>O@<4t6$U$Y0n*jcNb?_RUHh4<GD?T0>jS{$dG_OkSGc0ys4qb))#}YS0)Nh*x#M|!'
 '1bb=?(86VQF$GPFyI3)U3*}5j@6<Uh$qAwe207Go9KGU_Ez9=B$LrbK#oLeHpMAJo%>IdK;y7c-1e41kCU|&TbMdO1v(ZIgbFV9<'
 'Mt>Qg;_%#0oF9yqU|lB-(?v<Bi%0U(i%Sz0f-m|0j+KY+Epyi~UUVaYZR0eg!`6~sIr2Gi6(AsANiLY!HddMLUG1D<eXFm&9hWbK'
 'm5!Gy+fW$r^}V5keIevSHElk>CnU7_SL}&g%b^s`^mDO0@a*1*+-!*xKjpN{kTj(W-RDj5*0d}9pB~a$7Oy2A)YIi8r}jG3G2NP1'
 'K3zzcyZ`(V-TE#=l?3Ho1+hVLb|INNDSCy^2Pl_dU(G&!yt-)?8yyEnRsWywN<hcUn-S;n1{QQ#kRM*96aSqs@{kF<pg}cg5n;me'
 'dx+i{TKLd8`%V(a@*4%|@9slPC1a<JIGW;4M;L8)Fb{^}x{`Ac<aK<z3t&NsXKE*n^KNf(^N){<>x&QPGeQ4%bdLD!=Ir9*w?CrA'
 '0Q@x?_xlYZ2WwovKLZhK42ITdJnDNxchq;Bfi?F1QNQOcd%@7^FMGb{Sp&y6dgj=L$6?R#{lU=fI(^p}4*JVs{Zj~Dyj};@U5<0{'
 'VTS+4{>Dq6Lr@2Ikt+{xhyOXc<l~<s9IE46A|J2b&aRGK{PF*Hx8&dI1x}qk1_*8fCaxoJdES%|cFd~^v<qUzzs_GQ<&WUEw&h7_'
 'D*LgO_V$yv4z#6OGO5!$AaToiII-Ky`Q-3Y1#(*Hh0X_suyNMmuK*~mL8@H2EE*F@OSvpvk|!!HfaNk<0v3o<Xb3ij71ZZ1^`+LO'
 'ZWj)>6<gLWhsyy`%uZpME%D;$+-zM+tCdbe=p{#r@Osq(wwGm?!r8VgT{66cL1=i8bl;KDmW>($;wmobeF>^Xf;nW`e08*<rz!z4'
 'RD5^-pGcc~HkVGolF6mH%+ZV6yyYF^DhR3Y0ms>KawR#rkVFZPi+(FtVaxyaVjBS!3KZ0*4Ooc4pCE_|kD2&S9rVbfJ%VULf2H?q'
 'x`#!{-abHRkI~=7CD%bDM=#MU{l4sAVxXU%T5TGaR9;zB@MyrG$N2)(iQ*{qKoASA5lZwXd1?fB?*W)|U<%+BRy1$mkunif6K8jg'
 'bbA*hbT>2@5khf_kiN!QBvYXx*e>WX_VM}(5H?70pBm^V227|DZeVA@W=c&!_M3OtSRu#mq>Pyq66^-Ah>tv_fX6h^IX$JvWy<pa'
 'G7-NY-bP|-WTmiu;lWR0Ix~nx(Eg&xuK8zo;*>ck$uBIaFp*uAAjNJqu~|EAfM+C~iScFH_+=OD0uCHJMTg`an6HrGewnIsv(>t}'
 ')kM{5fCU>0DDy{~Kpa3&P!_e#53Hf<M<7bKYR<0${bvdm{loKt2w1%7Q$kqzT!6_Xn)||yUi%M_SH*LPBpZlnMLtS3YNvnILitdo'
 'lu+aRvRVYDx8l5OTC0yyJHS(F`vVPhDE|u6j?jcS5%Q0W0dOU7>;bRITen2>D19l+BS+?rV=V#5VrCK`B<UVY2KTZIE0-Cm8eBSU'
 'Ot6%Kz*xEfE%1nRfEMIxA__u|J3^O*XepjgCzuOtO^1}-d?N|>IUdXBWM6elSEdGGZgx<7wS>D{uek<bF7=Li(A1Hgu}l15L|LQD'
 'LxBkBzYvh4(+}7ejV$(KE(`p%BOj#VHtI?n3)e<@&oS|@9sDbx{g+bwzwv#wEav{kkuG~80Wje$7(UP|`>zUx|ARG)YRDdt@Qp(8'
 '2zg`*8aw${xB^@oEY{8w%trCrF9z%(H!O$;Xh#DI<TF~ScVL$<j%n8#{iUfBq;=(iqy5^gZ%iow?3ORnd63e)Z!_@>)3sgKcwkX1'
 'Pw-BiM|41wfmXcN3g7bE`K`=!vGDDDQoJ9xN|tle=G>(T?UtUMYPmc7s*nz#ENUGV-3R?dZE~l7lN(cahZ}N=r~#P+K&{SavWFPi'
 'C|?dh(g$4Xk{3J&)&utROTs_Tqz#uH7>0DQdj7o#IRH!&AGf6M?3#L6fql8;g`Gf+i9_J4mCcvS3LnxLZ>c%(PP$uICW1Y`2qP8D'
 'mUEemjh5=;lFR$0L0<wtlo~Aci!Qad=rc@R`WzEpZIAD`pfcoFF64QF&j4t$OuvY2f0#_olFb~I?_f8LGV_+D<f|k_U>_;v^fdyM'
 '4_X3xranjS4`IpE<KpvHFB$uF;Q4;p^4X<=ynp^4KRJaB?1?Eo`t_ItzjcoI8u9;K6+i{pJ+HCgk*)~S`mr>H;f=%y{V````E|g0'
 'UH@3!`>(6}M@g8&!}H#Pn0pv4rtN9ekf?j+)4Kz|b)o_X9a5QaplMDbbA-x(&{1I#aw-KC<g}=X(gCSbFmf{sH$m6FUR_T};Q{F('
 'w*?4GkM#|^a_VDtF~h6x&aVEom~|JkUJ=QA{_)4lo9m_sFi4+02m;M2rLnT;QcRf3<4m|!BXN0oc_~#pSgqu@xGkC%g?Rv#Sb3_&'
 'R)rn$aP)M?z;0%4=^Vbc!*6qymuLdte4R!G^l5(3d8ZSUJ+4W>I-P6cS57`VT`iMEvYwyoCph15fgzw@T91qQWSJ)~!C0z?n>EVc'
 'l2Lw!!Vgbj`C@*;`{Hp|>)@;k5WJXT06mtj!Y$F0Nd8%@YY##;jA~#JRr)ebGyJ|8?eNhOHUAD2Wz;TA08&u$$u{0<dNEx0Wx~_M'
 'd|z&6k`KbYE*ex6xG#0Rv`RJ&S`!nBrCygV>J#ex&y6$k@-=+CpE--^IzL>d_-W%d+~Zw;Sz{A}^`AY&FioViBzD5cjUO7qcYGr5'
 'eouMXj)%duTB{Cz0OsHdCtbznXi%i>FtdN8)TpyM`~c`k+))D3A%feS4A!JuXxf-M9v<cbi&urZiFlGDrZVntv!0NiH7*y!W3f4v'
 'k-iJ_aK#j+w&z2=Bv=@Ur3f3k3-#YVt52S#Y6B0NWdw+t0Zk*W-f1NCdBs0a&lL6K`kF3;Xus4ST+9M$P-x7?$BK@`=OFXagi#Tj'
 '2jh&XINVY@s3E{$wjlp%l=}XfT#Gq2lTR)ki!4p10Lrc`mE4Z=%Bn7`Dp~?w^;e_X1iN*@g!~J6GqpCp{Px+M<k-|R1&}qEK+^>O'
 'td#dC-#{)1S-SFIujn~h<EoyJz&ICmtr*xtkw4~hmBHjg+q9|B@kZnj)Z3wvm?Y0ML_SlPuSAxinu3O4l;?XqXROT;OS?c^dU|ZV'
 'J>R#fKvF4?<OPn=0pX79Hug~2m?^K!Wcjcz(`P~_<A(@8b6H-Wg)caEOQS}SiHw#exI8j#eIkIJ0FQvOb9U=YtMVe5JUWB!<Z&=+'
 '+V}5)c%{g%Wm+<u1G&1FNB|fvnwn!+secdrR9yW*39elYGn4V8goe7$1IpoaCrymfKf6XFDHf=S4yP@Uhg9jwboHFVGtfCuUq>m0'
 'iGqtW0G}V9^~U)wEq0AQ(_pG~W%0d3grL6~Pw=<$slyUHtdIHmw+?gtO0`Qa>Mhxnn98Wa1W%(DYybv~Fo%mzyeb<y4R3j6*efrz'
 '>6BMI;IyTl^S*LF?JLuNZZeYz0<$qRS3X~=lp#~ZWy%b}Q<S6ez+l#>2j-+zHCPTe*3n#jb}cz2FGni&iO_si;b!QjCbP4^+Jfn6'
 'kn0l!d*CUN;EvkF`RO-l++Ljh3y&M;4KY=^X6GuOqd=6;`_OZ9%=-Ni8xBTn(Cs45evCa<vw7k?EO5Bfd=7`zY-z!jdv!q3!1Ek('
 '?djo)b9x}o2Oo?nTy}N&Rkz*k!!*nUR|~ewF9^)BEMJ&I1;Nx*8)K>r3Re=WMXUnqEaGWmL&Zyy2E<O!b1neM=dCh-=I&9o=~s=I'
 'tcctsS19*o!J8C)ZEN>T*N<P5Buc?Tj|$`?C(x6xWm(8+KrEsPpd57jgK^JbU28BHcd<$qXU>|-ZE9qM01KBA9>8wJy@67Zhe~<8'
 'qtc#&iHbk#;MVb;h>67GBE?S(%*D62`)r^y@geR$eneWmpf_bmUKT7N(r~-FlxCN&*^@o02ZE(!eCHpwQR<$0-W6Zc!JXGqy7;cG'
 'xRp}Gd}zfD^6H}#*^w_z2<M8rsPdVwRw$4{^~tYR=wRXGv3rf!7kBT8kKq2rDz~8Gu2!$<q_V{{DBZDetBvaZxiOR5W$6}$-EWA{'
 '8nVc6)_3xcza$|j4JJQ>(Qpzs%rMrXv8C_~D(@t?1yTzllOOoNP=ey~9#uNL@MRCdT=Xd@Q}NOK!7eU-MG9jx1?@}UnJFE?DY241'
 '5ibRhh+<0w0L3lxgbeYrY(IGrO%ul|rIYH#6|~j_c({_0vlj6*9}arGagj`Vg?b1y_-svJW?|h)-!jImH|h1QF7W%rw1xw-%LWtE'
 '9CwGn(GzQITHP--FalEnr{4!KR@WE;7|ZGphX7{S8v?k&WMmqai9pQJXz-;PMT-5x(J-)1zH_UDzf&q=T0PSols=M!O#To<PJNk5'
 'S6{{{9`zA%qz|PzL5^tt0dS&lDYRAA1mOq5kk7Oaf4g)=BZi|4%BLaJ7g~_x3<@EwGTESX6&h`bElI|ej8;VK7@HnSDAJ08tWcMd'
 '8H`W!CNN~v<`h4Y2ZX7Kg2KR9N#lwtV)*<ZIjETD$f`5~dA*f&Pyt4u+87Q@{<V%51MhBTSKoiY0JEzPZ@--_-u-w{{yGC4dVeke'
 '58+S@-YyD3T{lH|7p>XWpjWWWX%Xxt5oC>rFuRL)q*HeI84edLQrfepsWJ)BF(|g%=`$-$Cc^&7E)hQrr>Z+=6Rxv30+UM`A;koy'
 'Cc82(<JVx;J0EyUa558A4x?M1bGc|r=#6E(OY)QUR2MJYK$w`#zFUaR@A--;g_S>aavj3*r-OKVi;Z-f8WbX-;61QH=`kT4&kB*v'
 'gt#o|tp7p+qRCTa5PXdPO4AVNy!g(l$mEf=$54I9{y~`>vN8JrR`)Albzg#2C=EiaY;N0(Bn<zE&+aV5MhwWtZJ2@;vGDG&jp7?T'
 'jbp;M5E78f5q*>8F#hr=*9&t8KZ0`c<J;NWg<zY-)r>-pg~k+NnMWX&V>rLF7SN-`&BsN*zc{;myLk8U$E(FZ-haH9E&c%oKmKEJ'
 'egSZ1*9EwL$2UiQH<t6u|N6hacsEP'
)
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def main():
 assert __debug__ and len(sys.argv)==2 and sys.argv[1] in ('recover','run','check')
 compressed=base64.b85decode(DATA);assert len(compressed)==COMPRESSED_BYTES
 raw=zlib.decompress(compressed);assert pin(raw)==PAYLOAD_PIN
 sources=json.loads(raw);assert set(sources)==set(SOURCES)
 root=Path('tree253_terminal_recovered');root.mkdir(exist_ok=True)
 for name,text in sources.items():
  b=text.encode();assert pin(b)==SOURCES[name]
  target=root/name
  assert not target.exists() or target.read_bytes()==b,('EXISTING_SOURCE_MISMATCH',name)
  target.write_bytes(b)
 print('TREE253_ALL_FOUR_COMPLETE_SOURCE_UNITS_RECOVERED',flush=True)
 if sys.argv[1]!='recover':
  if sys.argv[1]=='run':subprocess.run([sys.executable,'tree253_contact_build.py'],cwd=root,check=True)
  for name,args in [('tree253_contact_verify.py',[]),('tree253_cover.py',[]),('contact_barrier_body.py',['small']),('contact_barrier_body.py',['large']),('contact_barrier_body.py',['epsilon'])]:
   subprocess.run([sys.executable,'-S',name]+args,cwd=root,check=True)
  for name,expected in OUTPUTS.items():assert pin((root/name).read_bytes())==expected,('OUTPUT_PIN_MISMATCH',name)
  print('TREE253_TERMINAL_RIDGE_COMPLETE_COLD_REPLAY_PASS',flush=True)
 print('RECOVERY_SOURCE',*pin(Path(__file__).read_bytes()))
if __name__=='__main__':main()
```
