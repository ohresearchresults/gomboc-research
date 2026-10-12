"""Extract exact literal FILE blocks from a readable research capsule.
Usage: python extract_capsule.py CAPSULE.md DESTINATION
Uses only the standard library. Refuses unsafe paths or conflicting files.
"""
from pathlib import Path
import hashlib,re,sys

def main():
    if len(sys.argv)!=3:
        raise SystemExit('Usage: python extract_capsule.py CAPSULE.md DESTINATION')
    capsule=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
    text=capsule.read_text(encoding='utf-8')
    pattern=re.compile(r'^### FILE: ([^\n]+)\nBytes: (\d+)\nSHA-256: ([0-9a-f]{64})\n~~~~~~~~~~text\n(.*?)^~~~~~~~~~~\n',re.M|re.S)
    found=list(pattern.finditer(text))
    if not found:raise ValueError('No complete literal FILE blocks found')
    seen=set()
    for m in found:
        name,number,wanted,body=m.groups();rel=Path(name)
        if rel.is_absolute()or'..'in rel.parts or name in seen:raise ValueError('Unsafe or duplicate path')
        seen.add(name);encoded=body.encode('utf-8');size=int(number);raw=encoded[:size]
        if encoded[size:]not in(b'',b'\n'):raise ValueError('Unexpected trailing data')
        if len(raw)!=size or hashlib.sha256(raw).hexdigest()!=wanted:raise ValueError('Literal hash mismatch: '+name)
        dest=out/rel;dest.parent.mkdir(parents=True,exist_ok=True)
        if dest.exists()and dest.read_bytes()!=raw:raise ValueError('Conflicting existing file: '+name)
        dest.write_bytes(raw)
        print('EXTRACTED',name,size,wanted)
    print('LITERAL_CAPSULE_EXTRACTION_PASS',len(found))

if __name__=='__main__':
    main()
