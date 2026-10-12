# material-df78f2d00bf0

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# C114_RETRACT20 Recovery capsule part 1/2

New non-record family, not the requested own110 body. Independently rounded G6/G5/G4 have V21/E57/F38,C114,ownstrict211,weak000,primitivezeros000,TP=0 and one remaining polar bar. G3 is a genuine control:own277,weak000,six P bars. Each grid is a separate rational body; face labels and complexes cannot be inherited.

Complete recovery dependencies: this part; part2 (complete numerical producer and seed); already immutable complete exact auditor [internal-source-reference], saved literally as exact_turnover.py:11252bytes SHA256c9ef4681d976faa810ea3e27631a5ad686ac904fb18ba2bd8a38e5435ad36f1d. Explicitly select this dependency for a fresh worker. No originating sandbox or unpreserved JSON is required to reconstruct endpoints.

Save the Python block exactly with final newline as replay_retract20.py:4056bytes SHA25615352ca7e883895bdae04b58ac77319464aa32302e7fa745156a8c0feb6dc117. Reconstruction and verification command: python replay_retract20.py. Standard-library Python only; executed under3.13.5. Each of all63 binary64 coordinates is independently rounded using exact Fraction, ties-to-even, to each grid10^6,10^5,10^4,10^3. Never cascade rounding. Input compact JSON has grid then points and final newline. Canonical exact output serializer is in auditor. All eight reproduced files matched the embedded byte counts/hashes in an actual execution. Expected markers: TURNOVER_EXACT_TETRA446_PRISM446_WEAK123_CONTROLS_PASS and RETRACT20_INDEPENDENT_GRIDS_AUDIT_PASS. A preliminary replay without input final newline failed the hash check; the corrected4056byte script below passed. This was serialization, not a coordinate change.

One complete exact mechanics auditor with independent filled-mass machinery is not two complete independent mechanical audits. No exact continuous path is claimed between numerical checkpoints or frozen grids.

```python
"""C114_RETRACT20 exact endpoint recovery; independently rounded grids.
Requires exact_turnover.py, complete durable material [internal-source-reference].
Run: python replay_retract20.py. All output audits are exact, stdlib only.
Numeric producer is separate; these pinned coordinates avoid optimizer dependence.
"""
from pathlib import Path
from fractions import Fraction
import hashlib,json
import exact_turnover as ex
FINAL_HEX=['-0x1.ef54dedcfda13p-2', '0x1.e922a2186b65cp-1', '-0x1.d6a55a3a4e390p-2', '0x1.43562d1e3eea1p-1', '-0x1.83b3652a229aap-6', '-0x1.10e8392aac0d3p-1', '0x1.af4bca25103c8p-1', '0x1.01bbda7eeeefbp-2', '-0x1.3d70ac5a0f6aap-2', '0x1.e202cb4240e48p-1', '0x1.3defd6a210e9fp-2', '-0x1.2af09e80dd8cap-5', '0x1.011de10d88299p+0', '0x1.8770b21bf6099p-3', '0x1.81056ea73a9b9p-3', '0x1.0c998fa740054p+0', '-0x1.c09de0b8930ccp-5', '0x1.e7e21552dbf55p-3', '0x1.090a3a89df3afp+0', '-0x1.2927b283dc65ap-2', '0x1.151fb1eb0a02dp-2', '0x1.ec6bc19b2152fp-1', '-0x1.ea14d7fbad4efp-2', '0x1.87650387ee0d2p-2', '0x1.b1def6cb5b662p-1', '-0x1.3f589125fd97dp-1', '0x1.055d47d553ac2p-1', '0x1.66bc634a51cd9p-1', '-0x1.6feef201960a7p-1', '0x1.4ee3494241d8bp-1', '0x1.09c45db6b95b7p-1', '-0x1.981a23052673ap-1', '0x1.8b4f2f196b891p-1', '0x1.3a923d3878586p-2', '-0x1.b72cc707c2b04p-1', '0x1.b6f1ab4d53994p-1', '0x1.2b2ebded5ba1bp-4', '-0x1.cb53c2f0a6571p-1', '0x1.cec7529ca7025p-1', '-0x1.60c1012b9f195p-3', '-0x1.d2e2d093e525ap-1', '0x1.d0ebfa0297850p-1', '-0x1.b401cbdbc62ffp-2', '-0x1.c8452198236dfp-1', '0x1.c1152e22510d4p-1', '-0x1.5affcacdbf4dbp-1', '-0x1.a7175e78d91d4p-1', '0x1.a0d82d5ce1f35p-1', '-0x1.d7dcdeef1c0c8p-1', '-0x1.6ce464e2f720ep-1', '0x1.6ec8ed0b88324p-1', '-0x1.229cd6e9d06d3p+0', '-0x1.1aad2733bc40fp-1', '0x1.2c645bb82d2e1p-1', '-0x1.52c4ffc3ad650p+0', '-0x1.4e58e12961881p-2', '0x1.a5874e87d3d85p-2', '-0x1.7463a49a6d9dep+0', '-0x1.a864e7d9413fcp-6', '0x1.7d7d5527a82ccp-3', '-0x1.7f8250156d90ap+0', '0x1.1f07bfc473828p-1', '-0x1.eb586a31ae724p-3']
EXPECTED={'C114_RETRACT20_G6.json': (543, 'dcc2aac57655f4a0153b769a5175a6fa23023de2f4f5ddd956dbfa8cc644653f'), 'C114_RETRACT20_G5.json': (479, '2359585f5e02520aa82b95222d4f5bd80fe8d65fb8c0e9bac7920dd4f227f12b'), 'C114_RETRACT20_G4.json': (415, '929d757e793f95b3f1dd2121c4e4969f9fb79d959e0cbe7973e817c71943f307'), 'C114_RETRACT20_G3.json': (351, '718be12bbd961c279847ce76901a7017e4f06ddcfff0da55383313a38f8332f6'), 'C114_RETRACT20_G6_EXACT.json': (69075, '7c4c61381a60fb38cb73dc315546dee949729f504cbbe58b7ef165b901f8d3e0'), 'C114_RETRACT20_G5_EXACT.json': (58178, '08ecdce26900f572a91dba8a69222da21100f77d8ec60249ec2619db83e736ec'), 'C114_RETRACT20_G4_EXACT.json': (48457, '9e7f3463a963e18f8e30691ddaeb499558b1a83c2e9468a826a314e23def139c'), 'C114_RETRACT20_G3_EXACT.json': (41122, '2a692539cb81886b74a629cf41cdf8bfc4b0a6414462f770e596be72314c476a')}
def check(path):
    b=Path(path).read_bytes();assert (len(b),hashlib.sha256(b).hexdigest())==tuple(EXPECTED[path]),path

def main():
    b=Path(ex.__file__).read_bytes()
    assert len(b)==11252 and hashlib.sha256(b).hexdigest()=='c9ef4681d976faa810ea3e27631a5ad686ac904fb18ba2bd8a38e5435ad36f1d'
    assert len(FINAL_HEX)==63
    ex.controls()
    for k in (6,5,4,3):
        g=10**k;rows=[round(Fraction(float.fromhex(h))*g) for h in FINAL_HEX]
        obj={'grid':g,'points':[rows[i:i+3] for i in range(0,63,3)]}
        name='C114_RETRACT20_G%d'%k;ip=name+'.json';op=name+'_EXACT.json'
        Path(ip).write_bytes((json.dumps(obj,separators=(',',':'))+'\n').encode());check(ip)
        o=ex.audit(obj);ex.write_json(op,o);check(op)
        assert (o['V'],o['E'],o['F'],o['C'])==(21,57,38,114)
        assert list(map(len,o['mechanics']['strict']))==([2,1,1] if k>3 else [2,7,7])
        assert list(map(len,o['mechanics']['weak']))==[0,0,0]
        assert o['mechanics']['primitive_zero_counts']==[0,0,0]
        assert len(o['physical']['bars'])==(0 if k>3 else 6)
        assert len(o['polar']['bars'])==1
        print(name,'PASS',o['TQ'])
    print('RETRACT20_INDEPENDENT_GRIDS_AUDIT_PASS')
if __name__=='__main__':main()
```
