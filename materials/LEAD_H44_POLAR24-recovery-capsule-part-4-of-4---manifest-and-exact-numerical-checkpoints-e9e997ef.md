# material-e9e997ef9df9

AI research material · [Export notes](../catalog/coverage.md#text-records)

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

# LEAD_H44_POLAR24 — complete numerical recovery capsule, part 4/4

Status: numerical discovery and reusable search method, NOT an exact equilibrium certificate, NOT a target own110. Parts1–3 preserve literal runnable source units. This part preserves all21 endpoint parameter vectors: three baseline poles, six completed bar-objective endpoints, twelve completed direct-escape endpoints. No vector is abbreviated. Earlier coordinator progress claiming two own211 runs is corrected: the actual preserved twelve-run ledger has one own211 endpoint, witness0, S=[0,83],U=[15],H=[[7,28]],Q-depth .9137549406360692 in the numerical polar facet order. All other witness runs have additional extrema. This record is authoritative over any inconsistent prose summary.

## Recovery files, dependencies and environment
Save the complete literal material [internal-source-reference] as h44_lead_probe.py; 7141bytes SHA256 361c7ae721405b4df7f6cbb57aeacd01a3cc11fd9a665641dd2c60a752d94c96. This file embeds every literal H44_G6 input row; no sandbox checkpoint or external archive is needed.
Save [internal-source-reference] as h44_polar_orbit.py;6560bytes SHA256396dd247b01381e078cefa700a41b5d0cfc5c50b243e8937a4244453fed4e02d.
Save [internal-source-reference] as h44_polar_witness.py;3842bytes SHA256fc31d4ddabed8e62d181005650b2312cc8e5c163ba8951f7bdb082d1eddd2654.
Save the complete code block below as REPLAY_H44_POLAR24.py;7143bytes SHA256df41ee899e96f67f3b510b5d4bd185088d193770b434da0e1941d9186725f518. UTF-8 LF, including terminal newline for each file.
Verified execution environment CPython3.13.5, NumPy2.3.5,SciPy1.17.0, OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1. Binary64 endpoints are numerical objects; no cross-version optimizer-byte identity or exact no-weak proof is claimed.

## Commands and terminal checks
```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python h44_lead_probe.py --self-test --out H44_lead_baseline.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python REPLAY_H44_POLAR24.py
```
Expected markers NUMERICAL_H44_OWN121_CONTROL_PASS and H44_POLAR24_NUMERICAL_RECOVERY_PASS 21 98595 cb75c67fdddd9878b952ab084ca1f5d72c18d20444df84ae5d812e44a36e0011.
Replayed output H44_POLAR24_ENDPOINT_REPLAY.json98595bytes SHA256cb75c67fdddd9878b952ab084ca1f5d72c18d20444df84ae5d812e44a36e0011 contains every44-vertex numerical body, actual homogeneous centroid, exact stored parameter checkpoint, all numerical S/U/H/weak labels, full numerical P/Q bar records and environment. Same-environment replay executed and passed before storage. Floating audit tolerance1e-9, numerical positive bars>1e-13; these are discovery thresholds, not exact certification.

Producing searches, with every non-default parameter explicitly listed:
```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python h44_polar_orbit.py --baseline --out H44_polar_baseline.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python h44_polar_orbit.py --search --steps 6 --seed 20260924 --out H44_polar_search.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python h44_polar_witness.py --steps 12 --seed 24092026 --margin .0001 --power 1 --out H44_polar_witness.json
```
The search sources preserve all bounds, start generation, constraints, finite-difference step, tolerances and iteration limits. Elapsed wall times in producing search ledgers are intentionally not byte-replay targets. Complete terminal geometry is replayed from fixed literal vectors without rerunning optimization. The original search ledger optimization status/nit is not scientific certification.

## Complete REPLAY_H44_POLAR24.py
```python
"""LEAD_H44_POLAR24 numerical recovery, part4. NOT an exact certificate.
Requires the exact three source files listed in SOURCES. No optimizer is rerun.
Outputs every fixed endpoint of the executed 6 bar and 12 witness searches,
plus origin/primal-centroid/Santalo numerical controls. All coordinates use
literal binary64 checkpoint parameters; no source is obtained from the network.
Run OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python REPLAY_H44_POLAR24.py.
"""
import hashlib,json,platform
from pathlib import Path
import numpy as np
import scipy
from h44_polar_orbit import vertices,census
SOURCES={'h44_lead_probe.py': {'bytes': 7141, 'sha256': '361c7ae721405b4df7f6cbb57aeacd01a3cc11fd9a665641dd2c60a752d94c96'}, 'h44_polar_orbit.py': {'bytes': 6560, 'sha256': '396dd247b01381e078cefa700a41b5d0cfc5c50b243e8937a4244453fed4e02d'}, 'h44_polar_witness.py': {'bytes': 3842, 'sha256': 'fc31d4ddabed8e62d181005650b2312cc8e5c163ba8951f7bdb082d1eddd2654'}}
RECORDS=[{'name': 'origin', 'x': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'counts': [2, 9, 9]}, {'name': 'primal_centroid', 'x': [-0.4396350620277652, -0.2617600530831985, -0.05543678906278008, 0.0, 0.0, 0.0, 0.0, 0.0], 'counts': [10, 15, 23]}, {'name': 'santalo_numerical', 'x': [-0.45270851603684054, -0.27519232193358595, -0.06095950845168827, 0.0, 0.0, 0.0, 0.0, 0.0], 'counts': [5, 17, 20]}, {'name': 'bar0', 'x': [-0.46522755604982075, -0.25821732718991136, -0.10115115928942231, 0.003513471048758699, 0.014596938834953098, 0.033424127731894716, -0.018795417101501705, -0.016121739284903305], 'counts': [13, 19, 30], 'P': 18, 'Q': 12, 'loss': 0.7290341327869172}, {'name': 'bar1', 'x': [-0.4652270714052102, -0.25821716719256305, -0.10115187354874498, 0.003513653366448096, 0.014596551124778989, 0.03342293607957765, -0.01879455062313805, -0.016121010919867302], 'counts': [13, 19, 30], 'P': 18, 'Q': 12, 'loss': 0.729034132786963}, {'name': 'bar2', 'x': [-0.36939085870403815, 0.12053093858673443, -0.1831827703969929, -0.06732239658271072, -0.5263542150205847, 0.3139146582969297, 0.03001239622883326, -0.5447619937248497], 'counts': [19, 5, 22], 'P': 4, 'Q': 18, 'loss': 1.1299408517032714}, {'name': 'bar3', 'x': [-0.46522493413912136, -0.2582167321390969, -0.10115201147704378, 0.0035149045462244547, 0.014595675603397208, 0.03342171475464925, -0.01879297981422449, -0.016118676126583003], 'counts': [13, 19, 30], 'P': 18, 'Q': 12, 'loss': 0.7290341327571527}, {'name': 'bar4', 'x': [-0.4652262038529384, -0.2582170093837074, -0.10115164934960366, 0.0035137894726388285, 0.014596464438469809, 0.0334228461206733, -0.01879388453180183, -0.016120587551441527], 'counts': [13, 19, 30], 'P': 18, 'Q': 12, 'loss': 0.7290341327681064}, {'name': 'bar5', 'x': [-0.4720482430459319, -0.21691413663085118, -0.2963333876568626, -0.0883290306394173, 0.04690800418046453, -0.14623285836259586, -0.021090582083570644, 0.09376535694544734], 'counts': [12, 19, 29], 'P': 18, 'Q': 11, 'loss': 0.7708032961896673}, {'name': 'witness0', 'x': [-0.6742789459051414, -0.3996259231139179, 0.09221899292110754, -0.3442796018111812, 0.18916877557252165, 0.08773596644119193, -0.07485429234001127, -0.129737084654649], 'counts': [2, 1, 1], 'P': 0, 'Q': 1, 'loss': 0.06895224630601571}, {'name': 'witness1', 'x': [-0.4018318172681145, 0.07388399632841282, 0.2899062589740405, -0.42972264015698597, -1.1218908113833777, 0.1415942349474075, 0.976324820831826, -0.47782573227894964], 'counts': [3, 2, 3], 'P': 1, 'Q': 2, 'loss': 0.014585356258617635}, {'name': 'witness2', 'x': [-0.4093005217529799, -0.29084603998443564, -0.00437809301760564, 0.00174048524781341, 0.011772775132121927, 0.01632425520534803, 0.012575570912049978, 0.021203129024262732], 'counts': [2, 3, 3], 'P': 2, 'Q': 1, 'loss': 0.12588834015939304}, {'name': 'witness3', 'x': [0.47501611158045987, -0.07215375370280074, -0.47998517309289607, 0.03292540563533012, -0.9348614216336324, 0.8285596033612183, 0.6585509267722535, -0.2533405722338623], 'counts': [3, 3, 4], 'P': 2, 'Q': 2, 'loss': 0.017946325969379825}, {'name': 'witness4', 'x': [-0.30391495160019283, 0.031024900417726337, 0.18979562133547728, -0.5600447829971401, -0.8890458586383354, -0.5824477409984181, 1.998584376841551, -0.8973451778177235], 'counts': [3, 2, 3], 'P': 1, 'Q': 2, 'loss': 0.03363120460924667}, {'name': 'witness5', 'x': [-0.21203099551086066, 0.05097096374444076, 0.11065190171086467, -0.4443296158865744, -1.499999996709043, 0.16022165962290666, 1.0876595818955634, -0.7986461312295902], 'counts': [4, 2, 4], 'P': 1, 'Q': 3, 'loss': 0.0556659957387373}, {'name': 'witness6', 'x': [-0.05525793969205117, 0.23772012774446652, 0.03198596191361937, -0.8888599174260134, -0.43891119608587525, 0.06383887387507886, 0.8127990221648986, 0.18269224063549844], 'counts': [2, 3, 3], 'P': 2, 'Q': 1, 'loss': 0.14906660212830386}, {'name': 'witness7', 'x': [-0.29131703729146535, 0.04250341600165041, 0.21774596954313874, -0.7452535253605626, -0.8168158800662694, 0.19763454660361515, 1.0337026340148614, -0.43290962480149786], 'counts': [3, 2, 3], 'P': 1, 'Q': 2, 'loss': 0.03265059625136506}, {'name': 'witness8', 'x': [-0.40682675401103346, -0.387265473825372, 0.17722963155468544, -0.6074179730632588, -0.7039383681542873, 0.9347057733133594, 1.999999999992498, -0.26094099347067573], 'counts': [4, 3, 5], 'P': 2, 'Q': 3, 'loss': 0.11436600894188771}, {'name': 'witness9', 'x': [-0.5055708471451739, -0.05556997893507285, 0.21794350975178473, 0.13954141347338198, 1.1030861981497786, -1.250583983075979, -0.08503382533365962, -0.9348391265457323], 'counts': [5, 2, 5], 'P': 1, 'Q': 4, 'loss': 0.043563263929596335}, {'name': 'witness10', 'x': [-0.7959338555160762, -0.1402676771599122, -0.012880111808059688, -1.1164783977120425, -1.4999999999999998, 0.48907245643895575, 0.529382206045344, 0.10863611875915154], 'counts': [3, 3, 4], 'P': 2, 'Q': 2, 'loss': 0.09080863785045788}, {'name': 'witness11', 'x': [-0.2926738228686217, 0.02568459471343248, 0.33291897328820536, -0.6377651942399493, -1.2197595646721784, -0.3511337794362356, 1.016087780871245, -0.5511145652820818], 'counts': [2, 3, 3], 'P': 2, 'Q': 1, 'loss': 0.01623723632580178}]
def main():
    for name,expected in SOURCES.items():
        b=Path(name).read_bytes()
        assert len(b)==expected['bytes'] and hashlib.sha256(b).hexdigest()==expected['sha256'],name
    out={'status':'numerical_not_exact','environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'records':[]}
    for record in RECORDS:
        V=vertices(record['x']);r=census(V)
        counts=[len(r[n]) for n in ['S','U','H']]
        assert counts==record['counts'],(record['name'],counts)
        if 'P' in record:assert (len(r['P']),len(r['Q']))==(record['P'],record['Q'])
        assert not any(r['weak']),record['name']
        out['records'].append({'checkpoint':record,'vertices_binary64':V.tolist(),'audit':r})
    b=(json.dumps(out,sort_keys=True,separators=(',',':'))+'\n').encode()
    Path('H44_POLAR24_ENDPOINT_REPLAY.json').write_bytes(b)
    print('H44_POLAR24_NUMERICAL_RECOVERY_PASS',len(RECORDS),len(b),hashlib.sha256(b).hexdigest())
if __name__=='__main__':main()
```

## Interpretation boundaries
Every endpoint has the preserved combinatorics V44/E126/F84,C252, because the positive-pole projectivity and nonsingular lower-triangular metric map preserve the dual H44 hull. The code still numerically rebuilds the initial incidence and audits the final own centroid; no exact certificate is inferred from positive transport or a matching hash. The furthest radial vertex is chosen as the allowed terminal root in the escape objective, and all other vertices in the body and own-centred polar require an outgoing positive dot product. A small aggregate escape loss is not a small barcode: witness1 has a lower loss than witness0 but class323 and deep P/Q bars. Likewise the bar-depth sum can reduce while many small extrema appear. Eighteen local runs do not exclude any full orbit, changed metric/pole range, finite physical surgery or other architecture.
