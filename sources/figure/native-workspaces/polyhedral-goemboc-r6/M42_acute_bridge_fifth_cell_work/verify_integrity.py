#!/usr/bin/env python3
from __future__ import annotations
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "SHA256SUMS.txt"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()

def main() -> None:
    expected: dict[str, str] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, rel = line.split("  ", 1)
        if rel in expected:
            raise SystemExit(f"FAIL duplicate manifest path: {rel}")
        expected[rel] = digest
    actual_paths = {
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*")
        if p.is_file() and p.name != MANIFEST.name
    }
    missing = sorted(set(expected) - actual_paths)
    extra = sorted(actual_paths - set(expected))
    bad: list[tuple[str, str, str]] = []
    for rel, digest in sorted(expected.items()):
        p = ROOT / rel
        if p.is_file():
            got = sha256(p)
            if got != digest:
                bad.append((rel, digest, got))
    if missing or extra or bad:
        if missing:
            print("MISSING", *missing, sep="\n  ")
        if extra:
            print("EXTRA", *extra, sep="\n  ")
        for rel, want, got in bad:
            print(f"BAD {rel}\n  expected {want}\n  actual   {got}")
        raise SystemExit(1)
    print(f"PASS SHA-256 integrity for {len(expected)} files")

if __name__ == "__main__":
    main()
