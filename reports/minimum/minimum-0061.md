# minimum-0061

Historical AI scientific report · saved 2026-09-11 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

Получены три новых точных результата для буквальной TREE253=(0,0,1,2,3,4,5,0,7): три исключённых замкнутых коэффициентных сектора; универсальная оценка направления корневого полюса относительно собственного вектора метрики; обязательная конечная дизъюнкция общевершинных Λ-ограничений. **Полное универсальное исключение TREE253 и полное исключение её совместных реализаций V10/E17/F9 пока не доказаны.** Границы V≥10, F≥9, C≥34, а также исходные 633 типа / 52635 совместных корневых орбит не изменяются. Существование при C=34 не утверждается.

**Источник и область действия.** Прочитаны предоставленный контекст, актуальные доказательства журнала и буквальные результаты minimum-0058, объявленный SHA-256 159513b19201b45a7b7495a919e077021333865f6f160c989e63debf72597df3, и minimum-0056, объявленный SHA-256 947dfff6c30be5287d6e8427635bde5dafac1ad9cb7fe5b1f5f15f1ecec31954. Математического конфликта с буквальными массивами не обнаружено. Непосредственно извлечённые recovery-исходники родителей совпали с их внутренними pin: LL7 — 33812 байт, b24a6e59e69d2073861ba9a0c924b6be14afbd39b7a10f66d1364ef5bd97f9d0; 7pj — 28361 байт, ebf05fef861e25571f7654e7df6f4c7121142691d81873b31404515a276bcf6a. Это проверка байтов recovery, а не заявление о воспроизведении не предоставленной транспортной сериализации immutable payload. Универсальный девятивершинный результат 7pj сохраняется отдельно и не переносится на грани посредством полярности.

Везде P={x:q_iᵀx≤1} — одно настоящее однородное полноразмерное тело, перенесённое к своему объёмному центроиду; Q имеет строки q_iᵀ. Используются его V=Vol(P), Σ=E_P xxᵀ, Y_i=1−q_iᵀx, d_i=A_i/(V‖q_i‖), Λ[:,i]=d_i E_Fi Y, H=E_P YYᵀ и K_i=d_i E_Fi YYᵀ. Одна пара SPD-матриц удовлетворяет N=M⁻¹; G=QNQᵀ, n_i=G_ii. Сохраняются настоящие тождества Λ1=3·1, ΛQ=−Q, Λ²+Λ=4·1dᵀ, d_i=(Λ²)_ii/4, H=J+QΣQᵀ, rank Q=3, rank Λ=rank H=4, rank K_i=3. Это необходимые тождества настоящего тела; они не объявляются достаточным критерием реализации.

Принятый буквальный OJ-результат для 253 означает, что полный граф неотрицательных теней между различными гранями состоит ровно из восьми стрелок i→p_i. В физическом применении выбирается дерево настоящих соседних граней. Уже доказаны α=n_1/n_0>1/2 и β=n_7/n_0<3/4. Никакого дополнительного результата отказавшего сеанса не предполагается.

**A. Новые замкнутые коэффициентные сектора исключены полностью.** Для всякой настоящей S1-реализации TREE253 обязательно

Λ_01<1/32,
2Λ_01+Λ_07<1/10,
Λ_01+Λ_02+Λ_07+Λ_08<1.

Следовательно, Λ_07<1/10 и Λ_03+Λ_04+Λ_05+Λ_06>2. Это универсальный девятигранный результат на указанном OJ-домене, без предположения V=10, без U1 и без ограничения обусловленности M. Неравенства ≥ на всех трёх противоположных границах входят в исключение.

| Исключённая замкнутая гипотеза | Вершин точного строкового многогранника | PD-блоков | Положительных ведущих миноров | Общий знаменатель |
|---|---:|---:|---:|---:|
| Λ_01≥1/32 | 168 | 168 | 1512 | 288 |
| 2Λ_01+Λ_07≥1/10 | 228 | 228 | 2052 | 180 |
| Λ_01+Λ_02+Λ_07+Λ_08≥1 | 180 | 180 | 1620 | 36 |

Всего проверены 576 целочисленных блоков и 5184 ведущих минора двумя точными алгоритмами: Bareiss и Fraction LDL. Независимый аудит проверил знаки всех форм, общую γ, покрытие и слабые стенки. Чистая численная регенерация воспроизвела все три файла коэффициентов побайтно; затем отдельно выполнена проверка только стандартной библиотекой.

Доказательство использует следующие точные физические следствия LL7: 0<Λ_ij<10/9 при i≠j; строковую сумму 3; и формы

19·1ᵀG1−75 tr G≤0,
20G_aa+3·1ᵀG1−15 tr G≤0, a=0,…,8.

Последние являются следствиями настоящей общей строковой энергии и ранга три. В частности, при s=Σq_i и S=Σq_iq_iᵀ родитель доказывает 20q_aq_aᵀ+3ssᵀ≼15S и sᵀS⁻¹s<75/19; сокращения до произвольных независимых строк здесь нет. Родительский физический коэффициентный cap имеет точное значение c_3=max_{r≥0}3(1+2r+3r²)/[(1+r+r²)(3+2r+r²)]<10/9. В сертификате используется безопасный замкнутый cap 10/9.

Положим w=e_0+Λ[0,:]ᵀ. Тогда Gw=0, w_0=1, 0≤w_i≤10/9, Σ_{i>0}w_i=3. Каждая исключаемая гипотеза отсекает этот компактный многогранник одной замкнутой линейной полуплоскостью. Если отсечение неактивно, в вершине свободна не более чем одна координата. Если оно активно, свободны не более двух, причём сумма и отсечение должны быть независимы на этих координатах. Именно эти два случая полностью перечисляет функция clipped в капсуле; вырожденные совпадения удаляются как точные рациональные дубликаты.

Для стрелки i→j используется L_ij=2e_ie_iᵀ−e_ie_jᵀ−e_je_iᵀ с ⟨L_ij,G⟩≤0; для обязательной отрицательной тени — −L_ij. Код выбирает 40 таких отрицательных пар вне дерева; он не нуждается во всех 64. Ещё четыре формы задают замкнутый безопасный бокс 1/2≤α≤1, 0≤β≤3/4, и десять форм — приведённые физические scatter-ограничения. Итого 62 формы L_k. Все их буквальные элементы и порядок детерминированно заданы в исходнике.

Для каждой вершины w одного отсечённого многогранника восстановлены одна общая целая γ∈Z⁹ и целые μ_wk≥0 такие, что

B_w=D[γwᵀ+wγᵀ+Σ_k μ_wk L_k]−I ≻0.

Для настоящей строки берётся её выпуклое разложение по этим вершинам. Общая γ сохраняется; след с G её члена равен нулю, остальные следы неположительны. Одновременно среднее PD-матриц плюс I имеет положительный след с ненулевой G≽0. Противоречие. Нулевая механическая стрелка, равенство в cap или секторе и произвольно малая положительная площадь не обходят этот аргумент.

Эти сертификаты не используют новое incident-pair LMI; их сила и область действия указаны без такого приписывания. Новое LMI остаётся дополнительным разрешённым условием на всех восьми настоящих родительских парах.

**Следствие A: корневое incident-pair LMI уже имеет равномерный запас.** Сам точный cap из LL7 удовлетворяет c_3<111/100. Полное рациональное удостоверение:

111(1+r+r²)(3+2r+r²)−300(1+2r+3r²)
=111r⁴+333r³−234r²−45r+33
=(r−117/250)²(111r²+54612r/125+9413937/62500)
 +2284461r/7812500+38866407/3906250000>0, r≥0.

Все коэффициенты последнего выражения положительны. Вместе с новым Λ_01<1/32 это даёт на каждом настоящем теле рассматриваемого домена

[[9−8Λ_01,1],[1,9−8Λ_10]] ≻ [[35/4,1],[1,3/25]] ≻0,
(9−8Λ_01)(9−8Λ_10)−1>1/20.

Поэтому после сохранения настоящего cap 111/100 целое incident-pair LMI на паре 0,1 избыточно относительно новых скалярных ограничений. Это точный барьер для такого усиления метода, не вывод из неудачи локатора. Он также даёт явный равномерный запас на этой конкретной родительской паре, без утверждения подобного запаса для всех пар всех E17-тел.

На паре 0,7 то же LMI уже следует из Λ_07≤1/12 и Λ_70<111/100: произведение диагоналей строго больше (25/3)(3/25)=1. Возможный дополнительный эффект этого LMI в коэффициентной релаксации локализован в узком секторе 1/12<Λ_07<1/10, а новый weighted-cut тогда вынуждает Λ_01<1/120. Здесь не утверждается, что прохождение LMI обеспечивает физическую реализацию. Для остальных шести родительских пар избыточность не доказана. Точное полиномиальное удостоверение и арифметика запаса включены в отдельный 884-байтный исходник ниже.

**B. Новый универсальный барьер направления корня и метрики.** Следующий результат сильнее своей частной численной секторной формулировки и использует лишь голые восемь слабых стрелок TREE253. OJ, α/β, U1 и дополнительные инцидентности ему не нужны.

Пусть ненулевые q_i удовлетворяют rB_3⊂conv{q_0,…,q_8}⊂RB_3, R/r≤3, и для SPD N выполнено q_iᵀNq_{p_i}≥q_iᵀNq_i. Пусть a_1≥a_2≥a_3>0 — собственные значения N, e — единичный верхний собственный вектор и η=|eᵀq_0|/r. Тогда при 0≤η<1

a_1/a_2 ≤ 27(9−η²)/[(1−η)(η+8)²].                                      (B1)

В частности, весь замкнутый сектор η≤1/16 удовлетворяет

a_1/a_2 ≤36848/9245<4;                                                   (B2)

следовательно η≤1/16 совместно с a_1/a_2≥4 полностью исключён. При η=0 получается 243/64. Это исключение сектора, а не всей формы.

Полное доказательство. Пусть w_i=N^{1/2}q_i, ρ=‖w_0‖, A=√a_1 r, c=A/ρ и θ=arccos(|eᵀw_0|/ρ)∈[0,π/2]. Внутренний шар даёт два настоящих полюса с противоположными e-проекциями преобразованных векторов не менее A по модулю. Слабая стрелка y→z даёт ‖y‖≤‖z‖cos γ, где γ — угол между ними; все такие углы строго меньше π/2 и все нормы ≤ρ.

Утверждается c≤cos³(θ/3). Для пути от одного выбранного экстремума к корню добавим начальный угол от его знаковой оси ±e. Тогда c не превосходит произведения косинусов всех этих углов. Их сумму снизу ограничивает длина соответствующего сферического маршрута. Дополнение нулевыми углами и вогнутость log cos дают верхнюю оценку cos^L(T/L), если угловых множителей не более L, а сумма не менее T.

Если экстремум находится в корне, то c≤cos θ≤cos³(θ/3). Если хотя бы один экстремум находится на коротком плече {7,8}, его глубина ≤2, множителей ≤3, а сумма ≥θ. Это доказывает утверждение в этих случаях. Если оба находятся на длинном плече {1,…,6}, один лежит на пути от другого к корню. Маршрут от знаковой оси более глубокого экстремума через противоположный экстремум к корню имеет длину ≥θ+2arcsin c и не более семи косинусных множителей. Действительно, противоположный вектор, имеющий норму ≤ρ, отстоит от начальной знаковой оси на угол ≥π/2+arcsin c; треугольное неравенство до корня добавляет необходимый остаток. При знаке глубокого экстремума, совпадающем со знаком корня, получается даже π−θ+2arcsin c. Поэтому

c≤cos⁷[(θ+2arcsin c)/7].

Это несовместимо с c≥s=cos³(θ/3). Для u=θ/3∈[0,π/6] имеем cos³u≥cos(√3u): производная log cos(√3u)−3log cos u неположительна по возрастанию tan t/t. Отсюда θ+2arcsin s≥π+(3−2√3)u>7π/8, поскольку √3<15/8. Значит c<cos⁷(π/8)<3√3/8≤s. Последнее сравнение точно: cos¹⁴(π/8)=((2+√2)/4)^7<(7/8)^7<27/64, так как 7^7=823543<884736=27·8^7/64. Противоречие завершает доказательство c≤cos³(θ/3).

Теперь t=cos(θ/3) и cos θ=ηc=4t³−3t. Так как c≤t³ и η≥0, получаем (4−η)t²≤3. При η≤3 это даёт c²≤27/(4−η)³, то есть

ρ²≥a_1r²(4−η)³/27.

С другой стороны, настоящее внешнее ограничение даёт ρ²≤r²[a_1η²+a_2(9−η²)]. После вычитания используется буквальное тождество (4−η)³−27η²=(1−η)(η+8)², что доказывает (B1). Если η≤η_0<1, можно непосредственно заменить 4−η снизу на 4−η_0, а 9+(a_1/a_2−1)η² сверху на 9+(a_1/a_2−1)η_0²; получается тот же bound при η_0. Подстановка η_0=1/16 даёт 36848/9245, с точной разностью до 4, равной 132/9245.

Для настоящего тела применяем эту теорему в калибровке собственной ковариации:

x'=Σ⁻¹/²x, q_i'=Σ¹/²q_i,
M'=Σ¹/²MΣ¹/², N'=Σ⁻¹/²NΣ⁻¹/²=(M')⁻¹.

Гранный механический Gram сохраняется. Принятый настоящий инерционный sandwich даёт (1/√15)B_3⊂P'^*⊂√(3/5)B_3, поэтому r=1/√15, R/r=3. Его физическое содержание: неотрицательная аффинная функция h−u·x при ‖u‖=1 и Σ=I удовлетворяет E f²≤(8/5)(Ef)² и тем самым h²≥5/3; настоящий тетраэдральный fan от любой вершины даёт vᵀΣ⁻¹v≤15. Полярность этих двух включений применяется только к геометрии; однородность полярного тела не предполагается.

Итак, |eᵀq_0'|≤1/(16√15) вынуждает a_1(N')/a_2(N')≤36848/9245. Результат остаётся гранным, без U1. Только при дополнительном настоящем вершинном дереве можно умножить его на принятую вершинную оценку m_1(M')/m_2(M')≤9 и получить condition(M')<36 на этом секторе; более точный уже принятый множитель 9cos²⁰(π/20) также допустим в совместном срезе. Он не вставляется в универсальную S1-часть доказательства. Аналитическое доказательство независимо проверено; вычисление не производило этот результат и отдельный исполняемый объект для него не требуется.

**C. Обязательные общевершинные Λ-gate без полного каталога инцидентностей.** Неориентированное настоящее дерево 253 — гамильтонов путь

z=(6,5,4,3,2,1,0,7,8).

Пусть K — число его семи последовательных троек, имеющих одну настоящую общую вершину. Всегда K≥2. На V10/E17/F9 дополнительно K≥(o−2)/2, где o — число настоящих вершин нечётной степени.

Доказательство полностью топологическое. Дополнение выбранного двойственного остова в прямом графе — остовное дерево T: оно имеет V−1 ребро по Эйлеру, а его цикл разъединил бы двойственный остов. У листа v дерева T с настоящей степенью m≥3 выбраны m−1 из m рёбер циклического двойственного звена; они дают m−2 последовательных общевершинных окна. Есть как минимум два листа, и три различные настоящие максимальные грани не могут иметь две общие вершины. Следовательно K≥2. Никакого механического matching здесь не предполагается.

В общем звене вершины положим c_v=deg_T(v), а r_v — число непустых серий выбранных двойственных рёбер. Тогда k_v=m_v−c_v−r_v≥max(0,m_v−2c_v)≥ceil(m_v/2)−c_v; случай пустого набора использует r_v=0. Суммирование при Σm_v=34, Σc_v=18 даёт K≥(o−2)/2. Полное покрытие степенных случаев следует из Σ(m_v−3)=4:

| Положительные части избытка m_v−3 | Обязательное K |
|---|---:|
| (4) | ≥4 |
| (3,1) | ≥3 |
| (2,2) | ≥4 |
| (2,1,1) | ≥3 |
| (1,1,1,1) | ≥2 |

Если K=2, T сам является гамильтоновым путём; оба его листа имеют настоящую степень 3. Всего имеется шесть вершин степени 3 и четыре степени 4. В каждой из четырёх последних два выбранных двойственных ребра в циклическом звене противоположны, иначе возникло бы третье окно. Это точная структура минимального остатка, а не утверждение механической пригодности T.

Теперь положим S_i=(Λ²)_ii=4d_i. Для W={a,b,c} обозначим P_a=Λ_baΛ_ca, P_b=Λ_abΛ_cb, P_c=Λ_acΛ_bc. Определим Gate(W) четырьмя одновременными полиномиальными неравенствами

9P_aP_b≤S_aS_b, 9P_aP_c≤S_aS_c, 9P_bP_c≤S_bS_c,
3(P_aS_bS_c+P_bS_aS_c+P_cS_aS_b)≤2S_aS_bS_c+27P_aP_bP_c.

Для настоящей общевершинной тройки эти неравенства следуют из polygon-corner и three-roof: K_i[j,k]≥3Λ_jiΛ_ki/(4d_i); нижняя тройка ℓ_i удовлетворяет ℓ_iℓ_j≤1 и Σℓ_i≤2+ℓ_aℓ_bℓ_c. Монотонность последнего выражения на прямоугольнике до настоящей тройки законна, поскольку её частные производные равны 1−ℓ_jℓ_k≥0. Подстановка S_i=4d_i даёт ровно выписанные полиномы на общей настоящей Λ.

Таким образом, как минимум два из семи Gate для

(6,5,4), (5,4,3), (4,3,2), (3,2,1), (2,1,0), (1,0,7), (0,7,8)

должны выполняться. Это конечная дизъюнкция из всех 21 пар окон; в соответствующих степенных случаях необходимо как минимум три или четыре Gate. Равенство считается прохождением, а не нарушением. Gate сам не доказывает инцидентность; произвольно выбранное окно не объявляется общевершинным. Покрытие действует для всех настоящих реализаций среза и всех слабых механических стенок.

Число 2 нельзя повысить, используя только настоящую E17-инцидентность и наличие такого двойственного пути. Полный точный перебор на буквальном LL7-теле при ε=1/10 дал 392 пути с точностью до обращения и histogram {2:2,3:38,4:72,5:114,6:118,7:48}. Два минимальных пути — (2,1,3,7,6,0,4,8,5) и (2,7,3,1,6,8,4,0,5), оба с окнами 0 и 6. Первый переходит в путь 253 перестановкой new→old=(4,0,6,7,3,1,2,8,5). Капсула ниже сама восстанавливает точное настоящее тело, все 84 тройки опорных плоскостей, 10 вершин, 9 максимальных граней, 17 рёбер и полный перебор. Это барьер инцидентностного счёта; тело и пути не объявляются механической S1-реализацией. Перенос к собственному объёмному центроиду сохраняет проверенную инцидентность.

**Что было испробовано и что продолжать.** Проверялись общие строковые разделители, замкнутые полосы α/β и коэффициентные отсечения корневой строки. Принятые вычислительные исключения из этих поисков — три сектора A. Предшествующий трёхстрочный поиск использовал промежуточные границы Λ_01≤1/8 и 2Λ_01+Λ_07≤1/3; его неудачу нельзя переносить на более узкую окончательную область V2. Последний ограниченный трёхстрочный опыт уже использовал окончательные границы V2, общие компенсирующие матрицы и incident-cuts на настоящих парах 0–1 и 1–2; положительного кандидата не получено. Он завершён как UNKNOWN, без принятого точного объекта. Совместная окончательная область V2 не исчерпана. Неудачные численные предложения не являются ни осуществимостью, ни невозможностью, ни доказанным отсутствием сертификата. В отличие от этого, раздел C содержит точный реализованный барьер именно для повышения инцидентностного счёта.

Полезнейшее продолжение теперь имеет конкретные общие входы: α>1/2, β<3/4, три новые строгие строковые границы A, восемь настоящих incident-pair LMI [[9−8Λ_ab,1],[1,9−8Λ_ba]]≽0, конечную 21-ветвевую дизъюнкцию C и аналитическое ограничение B в собственной ковариационной калибровке. В совместном случае можно добавить настоящую реконструкцию инцидентности и отдельный вершинный фронт. Все ограничения должны проверяться на одной Λ,H,K, одних настоящих площадях/объёмах и одной взаимно обратной SPD-паре. Полный класс не закрыт, и никакое число типов или корневых орбит по этим частичным результатам не вычитается.

Для следующего совместного строкового шага остаточный корневой многогранник задаётся w_0=1, Σ_{j>0}w_j=3, 0≤w_j≤10/9, w_1≤1/32, 2w_1+w_7≤1/10, w_1+w_2+w_7+w_8≤1. Его полное внешнее покрытие можно детерминированно получить перебором r=0,1,2,3 активных последних плоскостей и r+1 свободных координат; остальные координаты фиксируются в 0 или 10/9, после точного решения суммы и r равенств проверяются все ограничения. Зависимые системы новых вершин не дают, вырожденные вершины попадают в независимый поднабор активных ограничений. Это рецепт следующего покрытия, а не объявление нового принятого сертификата.

**Полная recovery A: один исходник, никаких входных файлов.** Сохранить следующий блок как tree253_sectors_v2.py, UTF-8/LF с последним LF, assert включены. Для build: CPython 3.12.14, NumPy 2.3.5, SciPy 1.17.0, threadpoolctl 3.6.0; проверенный BLAS OpenBLAS 0.3.30, SkylakeX, один поток. Все параметры, начальные значения, порядок случаев, barrier/Newton-итерации, шаги и округление 10^8 буквально заданы. Случайных данных нет. Для check нужна только стандартная библиотека.

Команды в чистом каталоге:

python -m pip install numpy==2.3.5 scipy==1.17.0 threadpoolctl==3.6.0
python tree253_sectors_v2.py build
python -S tree253_sectors_v2.py check

Build регенерирует и точно проверяет коэффициенты; любое несовпадение численной регенерации с pin отвергается. Check повторяет точную проверку сохранённых результатов. Ожидаемые финальные маркеры: TREE253_LAMBDA01_LT_1_OVER_32_2LAMBDA01_PLUS_LAMBDA07_LT_1_OVER_10_SHALLOW_SUM_LT_ONE_PASS и TREE253_EXACT_576_BLOCKS_5184_MINORS_PASS.

| Объект | Байты | SHA-256 |
|---|---:|---|
| tree253_sectors_v2.py | 10242 | 433f3e57d33706eca423b3efaa62528c1a8a0bd431eedaab13e93caeef11025c |
| lambda_32.json | 74396 | 0c3ef862ecfee1045239a1eaa2e92bfa549e87f9f0195800489ac96cd99bfe3d |
| weighted_tenth.json | 99994 | 3df1fa8a122c93262a0430b3e65890c06a4bf40c510faf4be065cbf2402ddd69 |
| shallow_one.json | 80517 | a5eab22640ac1affbdd01a4f4ea8a902e504ea80086b4cadb36b6be9c8458f12 |
| tree253_sectors_v2_report.json | 1291 | 6cf61b2b97c760ffbf1e603b6e16e595e4eec269e387d86422b48e0d6e71c0f2 |

Исходник следует полностью; его build не зависит от родительских файлов или скачивания коэффициентов.

```python
"""TREE253 V2 three closed root-coefficient sectors; complete source-only recovery.
Dependencies for build: CPython3.12.14 NumPy2.3.5 SciPy1.17.0 threadpoolctl3.6.0.
Check needs only CPython standard library. No files are inputs to build.
"""
import os,sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from math import lcm
os.environ.update(OPENBLAS_CORETYPE='SkylakeX',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONHASHSEED='0')
P=(0,0,1,2,3,4,5,0,7)
FRAME=()
PARENTS=[['minimum-0058','159513b19201b45a7b7495a919e077021333865f6f160c989e63debf72597df3'],['minimum-0056','947dfff6c30be5287d6e8427635bde5dafac1ad9cb7fe5b1f5f15f1ecec31954']]
PLANS=[["lambda_32",[0,1,0,0,0,0,0,0,0],"1/32",[74396,"0c3ef862ecfee1045239a1eaa2e92bfa549e87f9f0195800489ac96cd99bfe3d"]],["weighted_tenth",[0,2,0,0,0,0,0,1,0],"1/10",[99994,"3df1fa8a122c93262a0430b3e65890c06a4bf40c510faf4be065cbf2402ddd69"]],["shallow_one",[0,1,1,0,0,0,0,1,1],"1",[80517,"a5eab22640ac1affbdd01a4f4ea8a902e504ea80086b4cadb36b6be9c8458f12"]]]
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def weights(lower):
 lo=[F(0)]*9
 for i,v in lower:lo[i]=F(v)
 cap=F(10,9);vs=set()
 for k in range(1,9):
  rest=[i for i in range(1,9) if i!=k]
  for bits in product((0,1),repeat=7):
   w=[F(0)]*9;w[0]=1
   for i,b in zip(rest,bits):w[i]=cap if b else lo[i]
   w[k]=3-sum(w[i] for i in rest)
   if lo[k]<=w[k]<=cap:vs.add(tuple(w))
 return sorted(vs)
def clipped(coeff,cut):
 cap=F(10,9);coeff=list(map(F,coeff));cut=F(cut)
 ans={w for w in weights([]) if sum(coeff[i]*w[i] for i in range(9))>=cut}
 for a,b in combinations(range(1,9),2):
  if coeff[a]==coeff[b]:continue
  rest=[i for i in range(1,9) if i not in (a,b)]
  for bits in product((0,1),repeat=6):
   w=[F(0)]*9;w[0]=F(1)
   for i,t in zip(rest,bits):w[i]=cap*t
   s=3-sum(w[i] for i in rest);t=cut-sum(coeff[i]*w[i] for i in rest)
   w[a]=(t-coeff[b]*s)/(coeff[a]-coeff[b]);w[b]=s-w[a]
   if 0<=w[a]<=cap and 0<=w[b]<=cap:ans.add(tuple(w))
 return sorted(ans)
def forms(negative,bounds,spectral):
 arcs=[(i,P[i],1) for i in range(1,9)]
 if negative:
  allowed={(i,P[i]) for i in range(1,9)}|set(FRAME)
  for i in range(9):
   for j in range(9):
    if i==j or (i,j) in allowed:continue
    v=j
    while v and v!=i:v=P[v]
    if v==i:continue
    arcs.append((i,j,-1))
 out=[]
 for i,j,sgn in arcs:
  z=[[F(0)]*9 for _ in range(9)];z[i][i]=2*sgn;z[i][j]=z[j][i]=-sgn;out.append(z)
 for i,l,h in bounds:
  z=[[F(0)]*9 for _ in range(9)];z[0][0]=F(l);z[i][i]=-1;out.append(z)
  z=[[F(0)]*9 for _ in range(9)];z[0][0]=-F(h);z[i][i]=1;out.append(z)
 if spectral==10:out.append([[F(19-75*(i==j)) for j in range(9)] for i in range(9)])
 if spectral:
  for a in range(9):out.append([[F(3-15*(i==j)+20*(i==a and j==a)) for j in range(9)] for i in range(9)])
 return out
def bareiss(A):
 A=[r[:] for r in A];last=1;v=[]
 for k in range(9):
  pivot=A[k][k];assert pivot>0;v.append(pivot)
  for i in range(k+1,9):
   for j in range(i,9):
    x=A[i][j]*pivot-A[i][k]*A[k][j];assert x%last==0;A[i][j]=A[j][i]=x//last
  last=pivot
 return v
def ldl(A):
 L=[[F(0)]*9 for _ in range(9)];D=[];out=[];det=F(1)
 for i in range(9):
  L[i][i]=1;v=F(A[i][i])-sum(L[i][k]**2*D[k] for k in range(i));assert v>0;D.append(v);det*=v;assert det.denominator==1;out.append(int(det))
  for j in range(i+1,9):L[j][i]=(A[j][i]-sum(L[j][k]*L[i][k]*D[k] for k in range(i)))/v
 return out
def serial(x):return(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def verify(rec):
 vv=clipped(rec['linear'],rec['cut']);ll=forms(rec['negative'],rec['bounds'],rec['spectral']);g=rec['g'];mu=rec['mu']
 assert len(g)==9 and all(type(x)is int for x in g);assert len(mu)==len(vv)
 den=lcm(*(x.denominator for w in vv for x in w),*(x.denominator for L in ll for w in L for x in w))
 stream=hashlib.sha256();matstream=hashlib.sha256()
 for w,u in zip(vv,mu):
  assert len(u)==len(ll) and all(type(x)is int and x>=0 for x in u)
  A=[[den*(g[i]*w[j]+w[i]*g[j]+sum(m*L[i][j] for m,L in zip(u,ll)))-(i==j) for j in range(9)] for i in range(9)]
  assert all(x.denominator==1 for r in A for x in r);A=[[int(x) for x in r] for r in A]
  a=bareiss(A);assert a==ldl(A);stream.update(serial(a));matstream.update(serial(A))
 return [len(vv),len(ll),9*len(vv),den,stream.hexdigest(),matstream.hexdigest()]
def locate(p,rows,wws,return_failure=False,frame=((6,4),(7,4),(7,5)),bounds=(),spectral=False,start=-10):
 m=sum(map(len,wws));nf=9*len(rows)+45*(len(rows)-1);d=nf+1
 allowed={(i,p[i]) for i in range(1,9)}|set(frame)
 arcs=[(i,p[i],1) for i in range(1,9)]
 for i in range(9):
  for j in range(9):
   if i==j or (i,j) in allowed:continue
   v=j
   while v and v!=i:v=p[v]
   if v==i:continue
   arcs.append((i,j,-1))
 na=len(arcs);I=np.eye(9);L=np.zeros((na,9,9))
 for k,(i,j,sign) in enumerate(arcs):L[k,i,i]=2*sign;L[k,i,j]=L[k,j,i]=-sign
 for i,l,h in bounds:
  z=np.zeros((9,9));z[0,0]=float(l);z[i,i]=-1;L=np.concatenate((L,z[None]))
  z=np.zeros((9,9));z[0,0]=-float(h);z[i,i]=1;L=np.concatenate((L,z[None]))
 na=len(L)
 if spectral:
  L=np.concatenate((L,(19*np.ones((9,9))-75*np.eye(9))[None]))
  for a in range(9):
   z=3*np.ones((9,9))-15*np.eye(9);z[a,a]+=20;L=np.concatenate((L,z[None]))
 na=len(L)
 J=np.zeros((m,d,9,9));off=[]
 if len(rows)>1:
  for i in range(9):
   for j in range(i,9):
    b=np.zeros((9,9));b[i,j]+=1;b[j,i]+=1;off.append(b)
 for r,a in enumerate(rows):
  for t,ww in enumerate(wws[r]):
   t+=sum(map(len,wws[:r]));w=np.array(ww)/ww[a]
   for i in range(9):J[t,9*r+i]=np.outer(I[i],w)+np.outer(w,I[i])
   if len(rows)>1:
    for s in range(len(rows)-1):
     if r==s or r==len(rows)-1:J[t,9*len(rows)+45*s:9*len(rows)+45*(s+1)]=np.array(off)*(1 if r==s else -1)
 J[:,-1]=-I
 y=np.zeros(d);y[-1]=start;u=np.full((m,na),1/na)
 def matrix(yy,uu):return np.einsum('mdij,d->mij',J,yy,optimize=True)+np.einsum('mk,kij->mij',uu,L,optimize=True)
 B=matrix(y,u)
 for outer in range(12):
  tau=.05*.18**outer;fac=tau/m
  for inner in range(70):
   chol=np.linalg.cholesky(B);R=np.linalg.inv(B)
   C=R[:,None]@J;D=R[:,None]@L
   gy=-np.trace(C,axis1=2,axis2=3).sum(axis=0);gy[-1]-=1/fac
   gu=-np.trace(D,axis1=2,axis2=3)-1/u
   Hyy=np.einsum('mdij,meji->de',C,C,optimize=True)
   Huy=np.einsum('mkij,mdji->mkd',D,C,optimize=True)
   Huu=np.einsum('mkij,mlji->mkl',D,D,optimize=True)
   Huu[:,np.arange(na),np.arange(na)]+=1/u**2
   rhs=np.concatenate((Huy,np.ones((m,na,1)),gu[:,:,None]),axis=2)
   sol=np.linalg.solve(Huu,rhs);T=sol[:,:,:d];e=sol[:,:,d];v=sol[:,:,d+1]
   S=np.zeros((d+1,d+1));b=np.zeros(d+1)
   E=C-np.einsum('mkij,mkd->mdij',D,T,optimize=True)
   S[:d,:d]=np.einsum('mdij,meji->de',E,E,optimize=True)+np.einsum('mkd,mke->de',T/u[:,:,None],T/u[:,:,None],optimize=True)
   S[:d,d]=-np.einsum('mkd,mk->d',Huy,e,optimize=True);S[d,:d]=S[:d,d];S[d,d]=-e.sum()
   b[:d]=np.trace(E,axis1=2,axis2=3).sum(axis=0)-np.einsum('mkd,mk->d',T,1/u,optimize=True);b[d]=v.sum();b[d-1]+=1/fac
   S=(S+S.T)/2
   ss=np.sqrt(np.maximum(np.abs(np.diag(S)),1e-300))
   Sn=S/ss[:,None]/ss[None,:];bn=b/ss
   try:step=solve(Sn,bn,assume_a='sym',check_finite=False)/ss
   except Exception:step=np.linalg.lstsq(Sn,bn,rcond=1e-14)[0]/ss
   dy=step[:d];du=-v-np.einsum('mkd,d->mk',T,dy,optimize=True)-e*step[d]
   descent=fac*(gy@dy+(gu*du).sum());decrement=-descent
   if decrement < min(1e-7,tau*.001):break
   alpha=min(1.,.99*float(np.min(-u[du<0]/du[du<0]))) if np.any(du<0) else 1.
   old=-y[-1]-fac*(2*np.log(np.diagonal(chol,axis1=1,axis2=2)).sum()+np.log(u).sum())
   deltaB=matrix(dy,du)
   for back in range(60):
    yy=y+alpha*dy;uu=u+alpha*du;BB=B+alpha*deltaB
    try:
     ch=np.linalg.cholesky(BB)
     val=-yy[-1]-fac*(2*np.log(np.diagonal(ch,axis1=1,axis2=2)).sum()+np.log(uu).sum())
     if np.isfinite(val) and val<=old+.05*alpha*descent:break
    except np.linalg.LinAlgError:pass
    alpha*=.5
   else:
    print('BACKTRACK_STOP',y[-1],flush=True)
    return (y[:-1],u,y[-1]) if return_failure else None
   y,u,B=yy,uu,BB
  print('STABLE_ITER',outer,inner,y[-1],flush=True)
  if y[-1]>1e-8:return y[:-1],u,y[-1]
 return (y[:-1],u,y[-1]) if return_failure else None
def main():
 assert __debug__ and len(sys.argv)==2 and sys.argv[1] in ('build','check')
 mode=sys.argv[1]
 if mode=='build':
  global np,solve
  import numpy as np,scipy,threadpoolctl,warnings
  from scipy.linalg import solve
  threadpoolctl.threadpool_limits(limits=1);warnings.filterwarnings('ignore')
  assert sys.version_info[:3]==(3,12,14)
  assert (np.__version__,scipy.__version__,threadpoolctl.__version__)==('2.3.5','1.17.0','3.6.0')
 reports=[]
 for name,linear,cut,expected in PLANS:
  spec=dict(name=name,linear=list(map(str,linear)),cut=cut,lower=[],negative=True,bounds=[[1,'1/2','1'],[7,'0','3/4']],spectral=10)
  if mode=='build':
   vv=clipped(linear,cut);ww=[[[float(x) for x in w]for w in vv]]
   bb=[(1,F(1,2),F(1)),(7,F(0),F(3,4))]
   ans=locate(P,[0],ww,True,(),bb,True,-100)
   assert ans is not None and ans[2]>1e-8,('LOCATOR_UNKNOWN',name)
   g,u,margin=ans;scale=max(abs(g).max(),abs(u).max())
   rec=dict(spec,g=np.rint(g/scale*10**8).astype('int64').tolist(),mu=np.rint(u/scale*10**8).astype('int64').tolist())
   verify(rec);raw=serial(rec);assert pin(raw)==expected,('PIN_MISMATCH',name,pin(raw))
   Path(name+'.json').write_bytes(raw)
  raw=Path(name+'.json').read_bytes();assert pin(raw)==expected
  rec=json.loads(raw);assert all(rec[k]==v for k,v in spec.items())
  reports.append(dict(name=name,data=expected,verification=verify(rec)))
  print('TREE253_CLOSED_SECTOR_EXACT_PASS',name,flush=True)
 raw=serial(dict(identity='TREE253_THREE_ROOT_COEFFICIENT_SECTORS_V2',parents=PARENTS,tree=list(P),assumptions=['one actual centroidal nine-facet body','one reciprocal SPD pair','genuine TREE253 arborescence','OJ exact nonnegative graph','alpha>=1/2','beta<=3/4'],records=reports))
 Path('tree253_sectors_v2_report.json').write_bytes(raw)
 print('TREE253_LAMBDA01_LT_1_OVER_32_2LAMBDA01_PLUS_LAMBDA07_LT_1_OVER_10_SHALLOW_SUM_LT_ONE_PASS')
 print('TREE253_EXACT_576_BLOCKS_5184_MINORS_PASS')
 print('REPORT',*pin(raw));print('SOURCE',*pin(Path(__file__).read_bytes()))
if __name__=='__main__':main()
```

**Полная recovery C.** Сохранить следующий блок как incidence253_corner_gate.py, UTF-8/LF с последним LF. Только стандартная библиотека; проверено CPython 3.12.14, assert включены. Команда: python -S incidence253_corner_gate.py. Все геометрические и комбинаторные входы буквальны; никаких внешних файлов или каталогов нет. Исходник: 4902 байта, SHA-256 65f3c60d21df963ea4c4eda4afe4a225b7c51dc25d562b200adba585459eef0c. Выход incidence253_corner_gate.json: 1097 байт, SHA-256 8001cc52d66d7451e41988bcdb59e13381ef8e6004fcade8747523c90dfadc87. Ожидаются маркеры ACTUAL_E17_84_TRIPLES_10_VERTICES_9_MAXIMAL_FACETS_PASS и TREE253_CORNER_GATE_CONTROL_392_PATHS_2_SHARP_CONTROLS_PASS. Код повторно исполнен независимо, оба pin совпали.

```python
"""TREE253 genuine-incidence corner gate; CPython standard library only.
Parent minimum-0058,
declared SHA256 159513b19201b45a7b7495a919e077021333865f6f160c989e63debf72597df3.
The control is that parent's actual E17 incidence, not a mechanical witness.
"""
from collections import Counter
from itertools import combinations
from fractions import Fraction as F
from pathlib import Path
import hashlib,json,sys
A=((0,1,3,4),(0,1,6),(0,4,5),(0,5,6,8),(1,2,3),
   (1,2,6,7),(2,3,7),(3,4,7,8),(4,5,8),(6,7,8))
S=tuple(map(set,A))
e=F(1,10)
DELTA=((1,-1,0),(1,0,-1),(0,1,-1),(-1,1,0),(-1,0,1),(0,-1,1))
HEIGHT=(0,0,0,1,1,0)
Q=tuple(tuple(1+e*x+e*e*h for x in d) for d,h in zip(DELTA,HEIGHT))+((1,-1,-1),(-1,1,-1),(-1,-1,1))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def det(a):return dot(a[0],cross(a[1],a[2]))
def solve(a):
 d=det(a)
 if not d:return None
 return tuple(F(det(tuple(tuple(1 if k==j else row[k] for k in range(3)) for row in a)),d) for j in range(3))
# Positive balance and rank prove boundedness with zero in the strict interior.
k=1+e*e/3;bal=(F(1,6)/(3*k+1),)*6+(k/(3*k+1),)*3
assert sum(bal)==1 and min(bal)>0 and det(Q[6:])
assert all(sum(b*q[j] for b,q in zip(bal,Q))==0 for j in range(3))
verts={};triple_count=0
for ids in combinations(range(9),3):
 triple_count+=1;v=solve(tuple(Q[i] for i in ids))
 if v is None:continue
 sl=tuple(1-dot(q,v) for q in Q)
 if min(sl)>=0:verts[v]=tuple(i for i,x in enumerate(sl) if x==0)
assert triple_count==84 and len(verts)==10 and tuple(sorted(verts.values()))==A
V=tuple(next(v for v,a in verts.items() if a==ids) for ids in A)
for i in range(9):
 vs=[v for v,a in verts.items() if i in a]
 assert any(any(cross(tuple(y-x for x,y in zip(a,b)),tuple(z-x for x,z in zip(a,c)))) for a,b,c in combinations(vs,3))
assert all(sum(set(p)<=a for a in S)<=2 for p in combinations(range(9),2))
D=tuple(e for e in combinations(range(9),2) if sum(set(e)<=a for a in S)==2)
P=tuple(e for e in combinations(range(10),2) if len(S[e[0]]&S[e[1]])==2)
assert len(D)==len(P)==17
DUAL={e:tuple(sorted(S[e[0]]&S[e[1]])) for e in P}
assert set(DUAL.values())==set(D)
adj={i:tuple(j for j in range(9) if tuple(sorted((i,j))) in D) for i in range(9)}
def is_tree(es,n):
 if len(es)!=n-1:return False
 seen={0}
 while True:
  old=len(seen)
  for u,v in es:
   if u in seen or v in seen:seen.update((u,v))
  if len(seen)==old:return len(seen)==n
hist=Counter();controls=[]
def audit(path):
 chosen={tuple(sorted(e)) for e in zip(path,path[1:])}
 comp=tuple(e for e in P if DUAL[e] not in chosen)
 assert is_tree(comp,10)
 c=tuple(sum(i in e for e in comp) for i in range(10))
 wins=tuple(t for t in range(7) if any(set(path[t:t+3])<=a for a in S))
 for t in wins:assert sum(set(path[t:t+3])<=a for a in S)==1
 local=tuple(sum(set(path[t:t+3])<=a for t in range(7)) for a in S)
 assert sum(local)==len(wins)
 for m,cv,kv in zip(map(len,A),c,local):
  assert kv>=max(0,m-2*cv)>=(m+1)//2-cv
 odd=sum(len(a)%2 for a in A)
 assert len(wins)>=max(2,(odd-2)//2)
 if len(wins)==2:
  assert max(c)==2
  assert all(len(A[i])==3 for i in range(10) if c[i]==1)
  controls.append((path,wins,comp))
 hist[len(wins)]+=1

def visit(path):
 if len(path)==9:
  if path[0]<path[-1]:audit(path)
  return
 for j in adj[path[-1]]:
  if j not in path:visit(path+(j,))
for i in range(9):visit((i,))
assert dict(hist)=={2:2,3:38,4:72,5:114,6:118,7:48}
controls.sort()
assert controls[0][0]==(2,1,3,7,6,0,4,8,5)
assert all(r[1]==(0,6) for r in controls)
order=(6,5,4,3,2,1,0,7,8)
new_to_old=dict(zip(order,controls[0][0]))
old_to_new={v:k for k,v in new_to_old.items()}
relabel=tuple(tuple(sorted(old_to_new[x] for x in a)) for a in A)
p=(0,0,1,2,3,4,5,0,7)
assert all(tuple(sorted((i,p[i]))) in {tuple(sorted((old_to_new[a],old_to_new[b]))) for a,b in D} for i in range(1,9))
out={'parent_assignment':'minimum-0058',
'parent_declared_sha256':'159513b19201b45a7b7495a919e077021333865f6f160c989e63debf72597df3',
'epsilon':'1/10','geometric_triples_checked':triple_count,
'active_facets':A,'dual_edges':D,'primal_edges':P,
'hamiltonian_paths_up_to_reversal':sum(hist.values()),'corner_histogram':dict(sorted(hist.items())),
'two_corner_controls':controls,'tree253_parent':p,'tree253_path':order,
'new_label_to_old':tuple(new_to_old[i] for i in range(9)),
'relabelled_active_facets':relabel,'mechanical_realization_claimed':False}
raw=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode()
Path('incidence253_corner_gate.json').write_bytes(raw)
print('ACTUAL_E17_84_TRIPLES_10_VERTICES_9_MAXIMAL_FACETS_PASS')
print('TREE253_CORNER_GATE_CONTROL_392_PATHS_2_SHARP_CONTROLS_PASS')
print('OUTPUT',len(raw),hashlib.sha256(raw).hexdigest())
src=Path(__file__).read_bytes();print('SOURCE',len(src),hashlib.sha256(src).hexdigest())
print('PYTHON',sys.version.split()[0])
```

**Recovery следствия A.** Следующий полный исходник root_pair253_barrier.py проверяет рациональное тождество cap и запас 1/20. CPython 3.12.14, только стандартная библиотека, assert включены; команда python -S root_pair253_barrier.py. Исходник 884 байта, SHA-256 6e56c8a3866bbeadfa6fa3cd62861f66d8854158da9f93fe80e47511bba5cc11. Маркер CAP_111_OVER_100_AND_TREE253_ROOT_PAIR_GAP_1_OVER_20_PASS. Входы полностью буквальны; выходных файлов нет.

```python
"""Exact cap and TREE253 root-pair consequence; standard library only."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):c[i]+=x
 for i,x in enumerate(b):c[i]+=x
 return c
def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
a=F(117,250)
q=[F(9413937,62500),F(54612,125),F(111)]
d=F(2284461,7812500);e=F(38866407,3906250000)
lhs=add([111*x for x in mul([1,1,1],[3,2,1])],[-300,-600,-900])
rhs=add(mul([a*a,-2*a,1],q),[e,d])
assert lhs==rhs==[33,-45,-234,333,111]
assert min(q+[d,e])>0
lo0=9-8*F(1,32);lo1=9-8*F(111,100)
assert (lo0,lo1,lo0*lo1-1)==(F(35,4),F(3,25),F(1,20))
print('CAP_111_OVER_100_AND_TREE253_ROOT_PAIR_GAP_1_OVER_20_PASS')
b=Path(__file__).read_bytes();print('SOURCE',len(b),hashlib.sha256(b).hexdigest())
```
