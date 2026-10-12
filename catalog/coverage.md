# Release coverage

The archive contains 158,763 scientific files (2.81 GB before compression), 898 AI research reports, 1,101 source notes and proof drafts, and 174 research branches. Some files occur at multiple paths to preserve historical dependencies.

## Verification status

[C622](../C622/README.md) passes the supplied exact verification programs. The search for C<500 remains open. The Minimum study contains proposed computer-assisted proofs of V≥10 and F≥9, retained for a separate mathematical assessment. Together, these bounds would imply C(1,1)≥34. Historical reports include incomplete and superseded arguments; their labels describe the status at the time.

## Missing material

Seven submitted research tasks have no saved result. The J143 translation-mass-closure note lacks confirmed copies of four companion files: `input143.py`, `exact_translation143.py`, `quartic_census143.py` and `TRANSLATION143_EXACT_RECIPE.json`. The complete KL13C 100-file source bundle is also unavailable. C622 includes all inputs needed for its standalone check.

## Text records

Reports and source notes preserve their original language. Internal identifiers, private links and machine paths have been replaced where necessary. `[internal-source-reference]` stands for a reference to another record of the research system that has no public address. Markers left by the chat interface (citation tags and links to its temporary file storage) have been removed; where such a link named a file, the file name is kept in the text. Some encoded source blocks are omitted and marked in the text; those passages cannot be run as complete programs. The [report index](reports.json) and [material index](materials.json) record substitutions, omission counts and file hashes. Index titles are taken from each record's first heading; where that heading was a single word such as “Verdict”, the first sentence of the record is appended.

## Data formats and reproduction

[NumPy format notes](numpy-format.md) document array conversions and the replacement for a ragged object array. A symbolic pickle cache and binary payloads that could not be fully inspected are omitted.

Historical scripts require their stated dependencies, and many write outputs beside their inputs. Run them in a working copy. The [C622 check](../C622/README.md) uses only the Python standard library and writes to a new output directory.

The Python files in `C622/` have been reformatted for readability, and its source guide has been rewritten in English. The algorithms and exact construction data are unchanged; source-file checksums have been updated.
