# material-ea7ad1333aa9

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---

# Recovery capsule part 1/3: SOC_C420_G8_G10_G12_OWN121
# All three parts are required; expanded source dictionary 115177 bytes.

[Encoded source block omitted; the code in this passage is incomplete.]


import base64,hashlib,json,lzma,runpy,sys
from pathlib import Path
if __name__=='__main__':
 home=Path(__file__).resolve().parent
 chunks=[''.join(PART.split())]
 for name in ['SOC_PAYLOAD_PART2.py','SOC_PAYLOAD_PART3.py']:
  chunks.append(''.join(runpy.run_path(str(home/name))['PART'].split()))
 expected_parts=['019d1855482b972dc6ada5074e60838595a05a12aefd9693e31aef9da7f211d1', '5f14d442b3b7d3b1e870c3c3a3f632a75b850f76f24e03ad93f6794393a692e8', 'c0d8a34d5ae83ef0cf4245c5f02441536d35533362c88f39d01dfb101efa1e11']
 for chunk,expected in zip(chunks,expected_parts):assert hashlib.sha256(chunk.encode()).hexdigest()==expected
 encoded=''.join(chunks);assert len(encoded)==40530 and hashlib.sha256(encoded.encode()).hexdigest()=='385f3254258d4fd6617138569cae040cd6ba3b057e71ffa6cbe4cbaf432ac8f6'
 blob=base64.b85decode(encoded);payload=lzma.decompress(blob)
 assert len(payload)==115177 and hashlib.sha256(payload).hexdigest()=='c628cd09a3331c4d9f00266655591d3b05b7a0bbb98a483c3faf95e399561f3d'
 files=json.loads(payload);out=Path(sys.argv[1] if len(sys.argv)>1 else 'soc_replay');out.mkdir(parents=True,exist_ok=True)
 for name,text in files.items():
  assert Path(name).name==name;data=text.encode();(out/name).write_bytes(data)
  print('SOURCE',name,len(data),hashlib.sha256(data).hexdigest())
 print('SOC_SOURCE_RECOVERY_19_FILES_PASS')
