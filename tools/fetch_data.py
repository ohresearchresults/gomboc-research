#!/usr/bin/env python3
"""Download a named scientific collection and verify every extracted file."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import tarfile
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def sha_file(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def destination(name):
    p = PurePosixPath(name)
    if '\\' in name or ':' in name or '\x00' in name or str(p) != name or p.is_absolute() or not p.parts or any(x in {'', '.', '..'} for x in p.parts):
        raise ValueError('Unsafe archive path')
    target = ROOT.joinpath(*p.parts)
    if not target.resolve().is_relative_to(ROOT.resolve()):
        raise ValueError('Archive path leaves the repository')
    for node in [target, *target.parents]:
        if node == ROOT:
            break
        if node.is_symlink():
            raise ValueError('Refusing to write through a symbolic link: ' + name)
    return target


def install(dataset, expected, verify_only):
    if verify_only:
        for name, row in expected.items():
            target = destination(name)
            if not target.is_file() or sha_file(target) != row['sha256']:
                raise ValueError('Missing or changed scientific file: ' + name)
        print(dataset['id'], ':', len(expected), 'files verified')
        return
    with tempfile.TemporaryDirectory(prefix='gomboc-data-') as temp:
        archive = Path(temp) / dataset['file']
        print('Downloading', dataset['id'], f"({dataset['bytes'] / 1024**2:.1f} MiB)", flush=True)
        with urllib.request.urlopen(dataset['url'], timeout=90) as response, archive.open('wb') as output:
            received = 0
            for block in iter(lambda: response.read(1024 * 1024), b''):
                received += len(block)
                if received > dataset['bytes']:
                    raise ValueError('Download exceeds its declared size; nothing was extracted')
                output.write(block)
        if archive.stat().st_size != dataset['bytes'] or sha_file(archive) != dataset['sha256']:
            raise ValueError('Download size/hash mismatch; nothing was extracted')
        # Validate every member and all existing destinations before installing
        # any file. This avoids a partial install from a malformed archive.
        seen = set()
        with tarfile.open(archive, mode='r|gz') as tf:
            for member in tf:
                if not member.isfile() or member.name in seen or member.name not in expected:
                    raise ValueError('Unexpected archive member: ' + member.name)
                row = expected[member.name]
                if member.size != row['bytes']:
                    raise ValueError('Archive member size mismatch: ' + member.name)
                seen.add(member.name)
                target = destination(member.name)
                source = tf.extractfile(member)
                if source is None:
                    raise ValueError('Missing archive member data')
                data = source.read()
                if hashlib.sha256(data).hexdigest() != row['sha256']:
                    raise ValueError('Archive member hash mismatch: ' + member.name)
                if target.exists():
                    if not target.is_file() or sha_file(target) != row['sha256']:
                        raise ValueError('Existing file differs; refusing to overwrite: ' + member.name)
        if seen != set(expected):
            raise ValueError('Archive did not contain every expected file')
        with tarfile.open(archive, mode='r|gz') as tf:
            for member in tf:
                target = destination(member.name)
                if target.exists():
                    if sha_file(target) != expected[member.name]['sha256']:
                        raise ValueError('Local file changed during validation: ' + member.name)
                    continue
                source = tf.extractfile(member)
                if source is None:
                    raise ValueError('Missing validated archive member')
                target.parent.mkdir(parents=True, exist_ok=True)
                # Exclusive creation also refuses a concurrent replacement.
                with target.open('xb') as output:
                    for block in iter(lambda: source.read(1024 * 1024), b''):
                        output.write(block)
        print(dataset['id'], ':', len(seen), 'files installed and verified', flush=True)


def main():
    config = json.loads((ROOT / 'catalog/downloads.json').read_text())
    choices = {r['id']: r for r in config['datasets']}
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('collection', choices=['all', *choices])
    parser.add_argument('--verify-only', action='store_true', help='check files already installed, without downloading')
    parser.add_argument('--source', choices=['zenodo', 'github'], default='zenodo',
                        help='download host (default: zenodo); both copies have the same hashes')
    args = parser.parse_args()
    names = list(choices) if args.collection == 'all' else [args.collection]
    files = {name: {} for name in names}
    with (ROOT / 'catalog/files.jsonl').open() as stream:
        for line in stream:
            row = json.loads(line)
            if row['collection'] in files:
                files[row['collection']][row['path']] = row
    for name in names:
        dataset = dict(choices[name])
        if not args.verify_only and args.source == 'zenodo':
            if not dataset.get('archive_url'):
                raise ValueError('No Zenodo archive URL recorded for ' + name)
            dataset['url'] = dataset['archive_url']
        install(dataset, files[name], args.verify_only)


if __name__ == '__main__':
    main()
