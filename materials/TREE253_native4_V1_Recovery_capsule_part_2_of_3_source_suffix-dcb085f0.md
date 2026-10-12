# material-dcb085f0f1ef

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
>
> This public text omits encoded source blocks; code in the affected passages is incomplete.
<!-- historical-status:end -->

---


[Encoded source block omitted; the code in this passage is incomplete.]

RAW_PIN=[27887, 'd1eab0e4e3ba4b5289f71042de4814ddf63b01c017629357e01b2d54953ac75d']
MANIFEST={'verify_grouped.py': [7956, 'c1a8bb624a41a04573b56a83ed859288ec005f351c0120fc90a969b8e0b3d04c'], 'certificates.json': [11403, '96cf99bdf9ce8c095b1e0484c7cc7ca04fa5a2fd85148ab0a9c083be869eb841'], 'grouped_search.py': [5136, 'cc27c361c7dea443e9af83621383e6c2516bb6f724ceea21846d1a0a685a4bbe'], 'quantize.py': [1147, '6ac24f7a00d798f15938fa70cd7dc589257060de8acd0de1d9cbde83755192b2'], 'exact_report.json': [1378, '72707b48e737fdf86f787cb9796a224bbd341db41a6de26c1d132557f84f48d3'], 'exact_check.log': [245, 'c4923e175b86802fcce54fda29cf453a8b621c0f1a5839226ac1529c93a59a64']}
raw=lzma.decompress(base64.b64decode(''.join(DATA.split()),validate=True))
assert pin(raw)==RAW_PIN
files=json.loads(raw)
assert set(files)==set(MANIFEST)
root=Path(__file__).resolve().with_name('native4_recovered')
root.mkdir(exist_ok=True)
for name,text in sorted(files.items()):
    p=Path(name);assert p.name==name and not p.is_absolute()
    b=text.encode();assert pin(b)==MANIFEST[name]
    target=root/name
    if target.exists():assert target.read_bytes()==b,('SOURCE_MISMATCH',name)
    target.write_bytes(b)
result=subprocess.run([sys.executable,'-S','verify_grouped.py','certificates.json'],cwd=root,check=True,stdout=subprocess.PIPE)
assert result.stdout==(root/'exact_check.log').read_bytes()
assert pin((root/'exact_report.json').read_bytes())==MANIFEST['exact_report.json']
sys.stdout.buffer.write(result.stdout)
print('TREE253_K2_NATIVE4_SHARED_ACTUAL_MOMENTS_COLD_REPLAY_PASS')
