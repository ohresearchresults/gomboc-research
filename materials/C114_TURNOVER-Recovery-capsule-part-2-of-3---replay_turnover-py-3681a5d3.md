# material-3681a5d34289

AI research material

---

"""C114_TURNOVER Recovery capsule part 2/3: exact inputs and replay.
Use with exact_turnover.py from part 1. Part 3 preserves producing methods.
python -B -S replay_turnover.py OUTPUT_DIRECTORY
No numerical optimizer or non-standard package is needed for this exact replay.
"""
from exact_turnover import *
import os
BASE=[[-13513, 10001, -9032], [7585, 971, -5336], [9215, 2535, -2766], [9859, 3065, -261], [10414, 1455, 1511], [10533, -561, 2627], [10245, -2747, 3309], [9489, -4870, 3884], [8292, -6612, 4622], [6777, -7643, 5870], [4984, -8225, 7187], [2841, -8790, 8032], [556, -8903, 8725], [-1868, -8784, 9006], [-4342, -8346, 8933], [-6808, -7570, 8472], [-9197, -6461, 7561], [-11427, -4979, 6139], [-13362, -2964, 4209], [-14798, -281, 1613], [-15515, 3415, -2186]]
POINT_HEX=['-0x1.f5caa768fe9f4p-2', '0x1.dff9a2fb9acbcp-1', '-0x1.e158f680fa3e7p-2', '0x1.48bed884f992dp-1', '-0x1.0b947d36682e9p-7', '-0x1.0f2b986fd9cd5p-1', '0x1.b04c82af132e3p-1', '0x1.03946c1d2e4e3p-2', '-0x1.376cd57b59330p-2', '0x1.e1e8c3998bd71p-1', '0x1.3e53956b7a401p-2', '-0x1.10bfc7682d45fp-5', '0x1.01d6759ab795cp+0', '0x1.720530ef60638p-3', '0x1.66823a9ae3ec9p-3', '0x1.0c3422b7f5f9bp+0', '-0x1.cc0df11db22a8p-5', '0x1.ee4b84b474b7ap-3', '0x1.08fa0287be72dp+0', '-0x1.2b0a08c29c433p-2', '0x1.1565aebb4dc86p-2', '0x1.ec73974c70e1ap-1', '-0x1.eb9cc8d9ce42dp-2', '0x1.8920674c6d82ep-2', '0x1.b1d825283dee7p-1', '-0x1.432e5258fa1d8p-1', '0x1.02787096afceep-1', '0x1.6776b1cbb3095p-1', '-0x1.71f933a251080p-1', '0x1.4d77ae8ceb48bp-1', '0x1.0a7c4d9e7d14bp-1', '-0x1.98e2dc58a23d6p-1', '0x1.8bb1f2332ff6bp-1', '0x1.3a9ac9e854a3cp-2', '-0x1.badb76f44778fp-1', '0x1.b4c12cd3ce79fp-1', '0x1.28073f8d2cb09p-4', '-0x1.cd0a504df5f15p-1', '0x1.ce97e1ae75841p-1', '-0x1.641b183de0c86p-3', '-0x1.d21bf69148bf5p-1', '0x1.d2ef8be7abe16p-1', '-0x1.b62966ae2fc9cp-2', '-0x1.c688e950b3ce8p-1', '0x1.c37ca761ed415p-1', '-0x1.5be7ad0252320p-1', '-0x1.a4c141adc95b6p-1', '0x1.a3340108fc502p-1', '-0x1.d7f49f6a00bfbp-1', '-0x1.6b3da808494cdp-1', '0x1.7050449926a97p-1', '-0x1.245f159ab70d7p+0', '-0x1.1756862f32209p-1', '0x1.2b00be18a02f3p-1', '-0x1.52f817d0db504p+0', '-0x1.496a93e009611p-2', '0x1.a607b6e7f6f5dp-2', '-0x1.743faaa44636ap+0', '-0x1.64ebea528ea5fp-6', '0x1.78aca8960fd46p-3', '-0x1.7ea079d4f590dp+0', '0x1.169f6d7047b7cp-1', '-0x1.e2463fc71170dp-3']
EXPECTED={'PARENT_C114_G4.json': {'bytes': 415, 'sha256': 'df0a606ee746a5546f046a4800f1eed5c833bf27e0fbe31d28da4984a482a6f2'}, 'PARENT_C114_G4_EXACT.json': {'bytes': 48699, 'sha256': 'ac065bc291fbab74f40fa1e2973749543e728c7cf85030915f84caaa1aa018e3'}, 'TURNOVER_C114_G4.json': {'bytes': 413, 'sha256': 'f25bc23f5a3195f5769859866978326cb2ab58123a615c6a8263811ea0845619'}, 'TURNOVER_C114_G4_EXACT.json': {'bytes': 48240, 'sha256': 'a1627a4730c3890b0b48906ac19fbb5e9468ef143375a7f59577ffd394420691'}, 'TURNOVER_C114_G5.json': {'bytes': 477, 'sha256': 'c94486e307ca34fa99da41bf2c196a3e02ae296a3558c4bf8b05ca52571ef389'}, 'TURNOVER_C114_G5_EXACT.json': {'bytes': 58670, 'sha256': 'd96cc104e8904e709e594bdad8413296554cba0d35f8e81c2f8a80ed73180de0'}, 'TURNOVER_C114_G6.json': {'bytes': 541, 'sha256': '810eb562f2a68f32f7e83dde67164d00306ac6128446fcfede0e6d4979e128cc'}, 'TURNOVER_C114_G6_EXACT.json': {'bytes': 68998, 'sha256': '647b86cb35c8870e56ec47f6f3652bbac2ddbd501ac5d0d462543003544ec4e9'}}

def replay(out):
    out=Path(out).resolve();out.mkdir(parents=True,exist_ok=True)
    controls();results={};receipt={}
    for label,g in [('PARENT_C114_G4',10000),('TURNOVER_C114_G4',10000),('TURNOVER_C114_G5',100000),('TURNOVER_C114_G6',1000000)]:
        if label.startswith('PARENT'): points=BASE
        else:
            v=[F(float.fromhex(h)) for h in POINT_HEX]
            points=[[round(z*g) for z in v[i:i+3]] for i in range(0,63,3)]
        data={'grid':g,'points':points};raw=json.dumps(data,separators=(',',':')).encode()
        name=label+'.json';(out/name).write_bytes(raw)
        rr={'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()};assert rr==EXPECTED[name];receipt[name]=rr
        a=audit(data);results[label]=a
        assert (a['V'],a['E'],a['F'])==(21,57,38)
        assert list(map(len,a['mechanics']['strict']))==[2,1,1]
        assert list(map(len,a['mechanics']['weak']))==[0,0,0]
        assert a['mechanics']['primitive_zero_counts']==[0,0,0]
        assert len(a['physical']['bars'])==0 and len(a['polar']['bars'])==1
        name=label+'_EXACT.json';rr=write_json(out/name,a);assert rr==EXPECTED[name];receipt[name]=rr
    p=results['PARENT_C114_G4'];den=p['polar']['delta_sum']**3*p['volume']**2
    summary={}
    for name,a in results.items():
        ratio=interval_power(a['polar']['delta_sum']**3*a['volume']**2/den,3)
        summary[name]={'census':[2,1,1],'weak':[0,0,0],'cost':a['C'],'denominator_bits':a['centered_denominator_bits'],'TQ':a['TQ'],'TQ_ratio_to_parent':ratio,
            'min_edge_over_R':a['min_edge_over_R'],'inradius_over_R':a['inradius_over_R'],'volume_over_R3':a['volume_over_R3'],'physical_arrow_cos':a['min_physical_arrow_cos'],
            'physical_root_input':a['physical']['roots'],'stable_face_cycles':[a['faces'][i] for i in a['mechanics']['strict'][0]],
            'polar_component_size':len(a['polar']['bars'][0]['component']),'polar_boundary_size':len(a['polar']['bars'][0]['boundary'])}
        if name.startswith('TURNOVER'):assert ratio[1]<420000000000
    write_json(out/'TURNOVER_COMPARISON.json',summary);write_json(out/'TURNOVER_RECEIPT.json',receipt)
    print('C114_TURNOVER_THREE_EXACT_OWN211_NO_WEAK_FREEZES_PASS',flush=True)
    print('C114_TURNOVER_EIGHT_SOURCE_ONLY_OUTPUT_HASHES_PASS',flush=True)
    print('C114_TURNOVER_GLOBAL_POLAR_TQ_RATIO_BELOW_0_42_PASS',flush=True)
if __name__=='__main__':replay(sys.argv[1] if len(sys.argv)>1 else 'TURNOVER_REPLAY')
