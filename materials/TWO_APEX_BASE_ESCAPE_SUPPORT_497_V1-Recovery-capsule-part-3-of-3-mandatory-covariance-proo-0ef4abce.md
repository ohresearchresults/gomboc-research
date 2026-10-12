# material-0ef4abceed94

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# TWO_APEX_BASE_ESCAPE_SUPPORT_497_V1 — обязательное уточнение усреднения в разделе6

Эта короткая часть дополняет уже сохранённую капсулу. Полный принимаемый комплект теперь состоит из трёх материалов: source part1 **[internal-source-reference]**, proof part2 **[internal-source-reference]**, настоящая обязательная correction part3. Старые названия первых двух материалов «of2» остаются историческими; при передаче доказательства нужно передать все три. Исходник6390bytes и JSON4164bytes не меняются.

В разделе6 proof part2, SHA **c073bc05a95bcd63420877d8d748ce8b4e3251d52d5b8837ed4402ad8777570d**, после внешней covariance-оценки ошибочно дана фраза: «В первом неравенстве разность не меньше 2(b+s/2)² после замены суммы z_i² на s²/3». Эту фразу следует удалить и заменить следующим полным выводом.

Пусть ожидание E_cells взято с настоящими положительными объёмными весами fan-тетраэдров, и s=z1+z2+z3. Собственный центр даёт E_cells s=-b. Тогда

20 E_P(e.X)²
 =E_cells[b²+z1²+z2²+z3²+(b+s)²]
 >=E_cells[2b²+2bs+(4/3)s²]
 = (4/3)E_cells s²
 >= (4/3)b².

Первое неравенство использует сумму z_i²>=s²/3. Следующее равенство использует E_cells s=-b и поэтому законно именно ПОСЛЕ усреднения. Выражение 2b(b+s) не обязано быть неотрицательным в отдельном тетраэдре. Последнее неравенство — Jensen/Cauchy–Schwarz. При covarianceI получаем b²<=15, как и требовалось.

Само итоговое неравенство раздела6, полностью прочитанное из512/546-источников, верно. Ошибка находилась только в добавленном объяснении якобы потетраэдральной положительности. Она не касается нового двухквадратного тождества, истинной двухапексной массы, вывода b->x, поддержки q.b<=1, growth16, строгих оценок9459/19 и29160/59, обоих точных контролей или конечного кода. Ни новая численная граница C_min, ни иной census этой коррекцией не заявляются.

Таким образом, непрерывный proof читается как part2 с указанной локальной заменой, а не как два противоречащих доказательства. Сохраняются оба исходных immutable материала и настоящая явная поправка; это не молчаливое изменение родительского результата.
