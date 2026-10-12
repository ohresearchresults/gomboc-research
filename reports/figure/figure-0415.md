# figure-0415

AI research report · 2026-09-19 UTC · [Export notes](../../catalog/coverage.md#text-records)

---

# Clear Maple 17 — закрытие исполнения без нового геометрического потомка

## Результат

**Новый конечный многогранник не получен.** В этом исполнении не построены ни lower-C own110/weak000 endpoint, ни новый точно проверенный нерекордный endpoint, ни реализованная новая контактная архитектура. Нового геометрического препятствия или исключения также нет. Конструктивная цель назначения осталась невыполненной; это состояние исполнения, а не отрицательный математический результат.

Не запускались оптимизационная кампания, удаление опор, перестройка изменённой оболочки, новый расчёт объёмного центра или полный census нового тела. Поэтому здесь нет численного кандидата, который можно было бы принять за почти готовый точный результат. В исходном рабочем каталоге находился только приложенный журнал; сохранённого геометрического checkpoint от прерванного ответа не было.

Завершённая работа ограничена полным чтением входного пакета и проверенным восстановлением **неизменённых** исходников канонического родителя. Это не новый replay его геометрических аудиторов и не продвижение рекорда.

## Прочитанные источники и фактически выполненная проверка

Прочитан весь приложенный `research-journal(20260919-090500).md`, включая общую память, память ветки и буквальный родительский payload, а затем все 16 декодированных файлов целиком. Обязательный parent — `figure-0411`, объявленный SHA-256 `8fcc52aa7ec1d0556b774912061d81594425ea912bf5bfee8caada67a4026e0b`. Этот SHA является идентификатором предоставленного immutable payload; его исходная envelope-сериализация заново не создавалась. Сам родитель прямо сообщает лишь прежний canonical replay, а не новый геометрический результат.

Фактическая цепочка восстановления в этом исполнении: извлечение единственного полного родительского Python decoder из журнала; проверка его байтов; base64 → XZ → JSON source map; проверка полного покрытия manifest, длины и SHA каждого из 15 перечисленных файлов и отдельного SHA manifest; запись всех 16 файлов в новую директорию с побайтовым чтением обратно. Родительский decoder не исполнялся через `exec`; извлекались только данные его литерала.

Измеренные и проверенные идентичности:

| Объект | UTF-8 байты | SHA-256 |
|---|---:|---|
| Текущий приложенный журнал | 278595 | `8663233c76a48ca6fec3693d3ec1c9675dd339ecd46751808e9a1880189c80f0` |
| Извлечённый родительский decoder | 29915 | `df80654b5f796c788027090ec6cfd7f39f5aee2ad8079fc99458202ce9c57019` |
| Декодированный source-map JSON | 68603 | `63b9a7de970fa8fb01f43ce10bec573441e5afeebe4ef2d3b7031ea6fb64c9ca` |
| Неизменённый `GENERATOR.json` | 11841 | `3cbd90d799189108f26b941800c8fa79a6f1c5abb17b2db614f0e54f57fffee7` |
| `MANIFEST.json` | 1673 | `0ba857a7d98fa85ad04ac1800886a9c450a5dc4c25e02177832adf9e0275d6af` |
| Новый source-integrity helper ниже | 3274 | `5c8a01662cbc7989a65bd8c93b93444ca2d062ad3ee337262fa3503801e75854` |

Полный перечень восстановленного closure: `COMPACT_INPUT.json`, `GENERATOR.json`, `MANIFEST.json`, `README.md`, `REPLAY_SCOPED.py`, `SMOKE_NUMERIC.py`, `core/RECONSTRUCT.py`, `core/centred_mass.py`, `core/check_A.py`, `core/check_B.py`, `methods/G_FREE_CODEC.py`, `methods/SVD_CORRECT.py`, `methods/contact.py`, `methods/flexible.py`, `methods/minnorm_qp.py`, `methods/scope.py`.

Выполненный terminal:

```text
CM17_CANONICAL_SOURCE_INTEGRITY_PASS 16 68603 63b9a7de970fa8fb01f43ce10bec573441e5afeebe4ef2d3b7031ea6fb64c9ca
```

Это проверка целостности и доступности исходников, **не математическая проверка тела**. В этом исполнении не запускались `REPLAY_SCOPED.py`, `SMOKE_NUMERIC.py`, `check_A.py`, `check_B.py` или `centred_mass.py`. Для канонического closure отсутствующей зависимости нет; старую проблему отсутствия FULL76 повторять не нужно. Другие исторические конструкции, упомянутые только по ID, не были восстановлены или использованы как скрытые исходные данные.

## Геометрическое состояние, передаваемое без повышения статуса

Последний источник с полным восстановлением остаётся **VQ20_C622_ROUTE88_118_G12**: V176/E311/F137, C622, собственный строгий census110, дополнительные слабые000; все137 опор активны. Его прежний A/B replay и отдельная интеграция348 положительных центрированных тетраэдров сообщены буквальным родителем. Это унаследованные результаты, а не результаты нынешнего запуска.

Унаследованный контрольный A=B имеет 311825 байт и SHA-256 `142ddb5d88fdc8b1721dbb62f52d9b71b78ac4c36e8600131235c6c4289698a0`; прежний `RECEIPT.json` — 681 байт, SHA-256 `6ca0671aace64125886235d1060235f93290915c512bd7e9ac1e0789d7ec3f8a`. Эти выходные файлы в нынешнем исполнении не производились.

Ограничения входной реализации сохраняют указанную в родителе область действия: старая owner/triangle-карта не даёт автоматически настоящую массу после изменения exposed boundary; `scope.quotient` не реализует исчезновение максимальной опоры; внутренний SVD repair пропускает два root scores; rerouting не означает turnover защищённых stable3/apex. Никакой из этих программных ограничителей не превращён здесь в запрет на допустимую геометрию.

Унаследованный необходимый бюджет также не усиливался: D=94, и при потере k максимальных граней E'=405−3k−D'; для E'≤310 нужно D'≥95−3k, то есть потеря degree excess не более3k−1. Это только бухгалтерия настоящего комплекса, не существование подходящего перехода.

## Полный runnable source выполненной проверки целостности

Зависимости: фактически использован CPython3.13.5, только стандартная библиотека; сторонних пакетов, случайных чисел и оптимизационных параметров нет. Точный вход — приложенный журнал указанной выше длины и SHA. Следующий код зависит от **буквальных байтов этого входа**, а не от возможности найти документ по его ID. При передаче свежему исполнителю журнал или полный исходный parent capsule должен оставаться приложенным. Этот helper не является автономной капсулой нового многогранника: нового многогранника нет.

Сохранить как `CM17_RECOVER_CHECK.py`, UTF-8/LF, с одним завершающим LF:

```python
"""Recover the supplied unchanged C622 source closure; no geometry is audited."""
import base64
import hashlib
import json
import lzma
import re
import sys
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    require(len(sys.argv) == 3, 'usage: CM17_RECOVER_CHECK.py JOURNAL NEW_DIRECTORY')
    journal = Path(sys.argv[1]).read_bytes()
    require(len(journal) == 278595 and digest(journal) ==
            '8663233c76a48ca6fec3693d3ec1c9675dd339ecd46751808e9a1880189c80f0',
            'wrong journal bytes')
    text = journal.decode('utf-8')
    blocks = re.findall(r'^```python\n(.*?)^```\s*$', text, re.M | re.S)
    blocks = [x for x in blocks if x.startswith('"""Recover the unchanged canonical C622 parent;')]
    require(len(blocks) == 1, 'parent decoder not unique')
    decoder = blocks[0].rstrip('\n') + '\n'
    require(len(decoder.encode()) == 29915 and digest(decoder.encode()) ==
            'df80654b5f796c788027090ec6cfd7f39f5aee2ad8079fc99458202ce9c57019',
            'wrong decoder bytes')
    match = re.search(r'PAYLOAD = """\n(.*?)\n"""', decoder, re.S)
    require(match is not None, 'payload missing')
    b64 = ''.join(match.group(1).split()).encode('ascii')
    require(len(b64) == 27864 and digest(b64) ==
            '6a7d42eeabc1365c9dc122a9e62e6127e779db025765c6cbb37107cb31788638',
            'wrong base64 bytes')
    packed = base64.b64decode(b64, validate=True)
    require(len(packed) == 20896 and digest(packed) ==
            '74dfffa9c2c4972bf1d4b99c269e3c3df99eaa01549548b858c542b431fa3597',
            'wrong XZ bytes')
    raw = lzma.decompress(packed)
    require(len(raw) == 68603 and digest(raw) ==
            '63b9a7de970fa8fb01f43ce10bec573441e5afeebe4ef2d3b7031ea6fb64c9ca',
            'wrong source map bytes')
    files = json.loads(raw)
    require(len(files) == 16, 'wrong source count')
    manifest = json.loads(files['MANIFEST.json'])
    require(len(manifest) == 15 and set(files) == set(manifest) | {'MANIFEST.json'},
            'manifest coverage mismatch')
    require(digest(files['MANIFEST.json'].encode('utf-8')) ==
            '0ba857a7d98fa85ad04ac1800886a9c450a5dc4c25e02177832adf9e0275d6af',
            'manifest hash mismatch')
    for name, content in files.items():
        relative = Path(name)
        require(not relative.is_absolute() and '..' not in relative.parts,
                'unsafe source path')
        data = content.encode('utf-8')
        if name in manifest:
            record = manifest[name]
            require(len(data) == record['bytes'] and digest(data) == record['sha256'],
                    'source identity mismatch: ' + name)
    out = Path(sys.argv[2])
    require(not out.exists(), 'destination must be absent')
    out.mkdir(parents=True)
    for name, content in files.items():
        path = out / name
        path.parent.mkdir(parents=True, exist_ok=True)
        data = content.encode('utf-8')
        path.write_bytes(data)
        require(path.read_bytes() == data, 'write/readback mismatch: ' + name)
    print('CM17_CANONICAL_SOURCE_INTEGRITY_PASS', len(files), len(raw), digest(raw))


if __name__ == '__main__':
    main()
```

Воспроизведение выполненной проверки, с ещё не существующей выходной директорией:

```sh
python -B -S CM17_RECOVER_CHECK.py 'research-journal(20260919-090500).md' CM17_SOURCE_FRESH
```

Ожидается ровно приведённый выше `CM17_CANONICAL_SOURCE_INTEGRITY_PASS` с 16 файлами и SHA source map. Несовпадение любого hash, manifest или байтов при чтении обратно является ошибкой, а не разрешением подменить источник.

Для отдельного восстановления неизменённой геометрической базы родитель предоставляет следующие команды. **Они здесь не выполнялись** и не являются конструктивным продолжением:

```sh
python -B -S CM17_SOURCE_FRESH/REPLAY_SCOPED.py CM17_PROOF_FRESH
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B CM17_SOURCE_FRESH/SMOKE_NUMERIC.py CM17_PROOF_FRESH
```

Унаследованный точный aggregate marker: `COORD_C622_SCOPED_CANONICAL_AB_MASS_CONTROLS_PASS 6ca0671aace64125886235d1060235f93290915c512bd7e9ac1e0789d7ec3f8a`; численный marker: `COORD_C622_SCOPED_NUMERIC_ENTRY_PASS`. Их смысл и команды заданы буквальным родителем.

Дополнительные фактически существующие копии: source-integrity helper (`CM17_RECOVER_CHECK.py`) и полный неизменённый родительский decoder со встроенным16-source capsule (`CM17_PARENT_SOURCE.py`). Они не обозначают новый endpoint.

## Наиболее полезное продолжение

Возобновлять следует именно конструктивный поиск от точного канонического `GENERATOR.json`, а не ещё один отчёт о его воспроизведении. После фактического удаления или перестройки опоры новый halfspace intersection должен заново определять extreme vertices, максимальные грани, настоящие рёбра и обычную объёмную массу. Только из этого комплекса следует строить следующую контактную карту. Номинальный quotient, старая триангуляция или локальный residual не являются промежуточным геометрическим результатом.

Приоритет, оставшийся от назначения: связанная потеря максимального интерфейса, сохраняющая достаточный degree excess, с физическим перераспределением массы и возможной явной сменой корней. Здесь нет выполненной кампании, которая сузила бы эту область, нет выбранной перспективной опоры и нет нового точного checkpoint для продолжения. Любой полученный далее endpoint требует собственного полного S/U/H и отдельного weak census, A/B проверки действительного комплекса и третьей интеграции.

**Итог передаваемого состояния:** полный canonical source closure доступен и проверен побайтово; научный frontier не изменён; задача E≤310 own110/weak000 остаётся конструктивно открытой в рамках этого назначения.
