# Scientific datasets

Clone the repository for code, reports and C622. The archives below add the large numerical collections. GitHub’s automatic “Source code” ZIP does not include these separately attached datasets.

```sh
python3 tools/fetch_data.py all
```

Or choose a collection ID from the table. The downloader checks the archive checksum and every file, refuses conflicting local files, and runs no experiments.

| Collection ID | Files | Download | SHA-256 |
| --- | ---: | --- | --- |
| `astra-aristotle` | 15,566 | [122.7 MiB](https://github.com/ohresearchresults/gomboc-research/releases/download/research-2026-10-12/astra-aristotle.tar.gz) | `9ae3ee48add20d5946ecaf672fb60c8b3d82fa6367485a9623003ec987674455` |
| `astra-herschel` | 119,628 | [273.3 MiB](https://github.com/ohresearchresults/gomboc-research/releases/download/research-2026-10-12/astra-herschel.tar.gz) | `4ea9236d7442016f90c02cf381fde75e0f988daa15dae570401b3438d0e9d9aa` |
| `astra-peirce` | 16,979 | [156.3 MiB](https://github.com/ohresearchresults/gomboc-research/releases/download/research-2026-10-12/astra-peirce.tar.gz) | `8c90b589d6f3235e7019d9e1dd113a3092ad9cb26942dea5846e96a57762cad8` |
| `astra-shared` | 49 | [0.3 MiB](https://github.com/ohresearchresults/gomboc-research/releases/download/research-2026-10-12/astra-shared.tar.gz) | `a566b41b3d4562d9a0b676bf02bee727ae0438f4220f9e38b65011e8656ee465` |
| `figure-workspaces` | 3,004 | [151.6 MiB](https://github.com/ohresearchresults/gomboc-research/releases/download/research-2026-10-12/figure-workspaces.tar.gz) | `b189173843a4caa371fb7d77c54f87ef72cb1ff15f666a1aa70d0cdcbc7c4994` |
| `historical-constructions` | 3,422 | [188.5 MiB](https://github.com/ohresearchresults/gomboc-research/releases/download/research-2026-10-12/historical-constructions.tar.gz) | `9cd24a8be0a9a385a08e9c22617b29467a46dfbc4b1dfb2c1935481bf96e8904` |
| `minimum` | 79 | [0.2 MiB](https://github.com/ohresearchresults/gomboc-research/releases/download/research-2026-10-12/minimum.tar.gz) | `2f925a51cc2659afb287a7cc41e60ded2e1730955a559abb5b94122ef38ef874` |
| `recovered-science` | 36 | [0.8 MiB](https://github.com/ohresearchresults/gomboc-research/releases/download/research-2026-10-12/recovered-science.tar.gz) | `8dfcb9e78cecc3a52a3116064ad29e514f70bb5781f9764f1e31430fd77f1a66` |

Ordinary tar.gz archives can also be unpacked at the repository root. Their relative paths match [files.jsonl](files.jsonl). Numeric histories and unsuccessful candidates are included; inclusion is not a claim that a target was reached.

Some historical copies replace private machine prefixes with `/RESEARCH` or `/REDACTED_HOME`. These are declared path placeholders, not working locations. Adapt those paths before replaying a historical script. The standalone C622 check needs no such adaptation. Scientific input/output hashes distinguish these public derivatives from preserved originals.
