# material-5528a3fd59b0

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# Обязательная поправка к POLAR_GLOBAL_RADIUS_TRANSFER_V1

Нормативное аналитическое доказательство состоит из [internal-source-reference], SHA4263be15863102ce16c91f17c336c702da53bf1c1c8dce3f8372b64c79c7d0ff, СОВМЕСТНО с этой поправкой. Поправка имеет приоритет над одной ошибочной координатной формулой того материала.

В разделе 4 фраза «Точка p=u/(u^T M u) в исходной системе» должна быть заменена точной формулой

p=M u/(u^T M u).

Здесь p — точка в исходном ПРОСТРАНСТВЕ ПОЛЮСОВ q, а u — исходная ПРЯМАЯ вершина. Равенство p=u/(u^T M u) вообще неверно при M!=I. В физических координатах x'=M^{1/2}x, q'=M^{-1/2}q по-прежнему верно p'=u'/||u'||^2, как и записано в основном доказательстве. Обратное преобразование q=M^{1/2}q' как раз даёт p=M u/(u^T M u).

Обоснование внутреннего положения p: строгая неустойчивость означает, что M u находится внутри нормального конуса P при u. Этот конус порождён настоящими incident-полюсами. Поэтому M u=sum_i lambda_i q_i с положительными lambda_i; скалярное умножение на u даёт sum_i lambda_i=u^T M u. После деления p есть строгая выпуклая комбинация всех вершин настоящего полярного гранного многоугольника, то есть лежит в его относительной внутренности. В физических координатах вычитание p' оставляет тангенты y_i, использованные в остальных формулах.

Все матричные, угловые и реберные выводы основного материала сформулированы через правильные G=QNQ^T, N=M^{-1}, sigma=(u^T M u)^{-1} и через физические y_i. Они не меняются. Рациональный контроль и полный исполняемый источник [internal-source-reference] используют M=N=I и также не меняются: source5616/SHA8c37a3a6e845383642c34137dd4c912986588ac2dec9edc6d4894cd8ac702318, output4266/SHA59d049dadbf78c72c5df164427d1d46b40461a0affa3f8650866ef30eaa7fe84.

Основной материал без этой поправки нельзя цитировать как безошибочную координатную формулировку для произвольной SPD-метрики. Никакой новый C-барьер или целый инцидентностный подкласс данной поправкой не объявляется доказанным.
