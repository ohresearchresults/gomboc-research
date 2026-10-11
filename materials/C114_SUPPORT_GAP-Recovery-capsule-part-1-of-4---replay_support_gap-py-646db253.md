# material-646db2539e5e

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Cold exact reconstruction of C114_SUPPORT_GAP affine/free endpoints.
Require preserved exact_turnover.py and metrics_support.py in this directory.
No optimizer or old filesystem is required. Fractions give independent grid freezes.
"""
import json,hashlib,os,sys,runpy
from pathlib import Path
from fractions import Fraction as F
from exact_turnover import audit,controls,write_json

SEED={'grid': 10000, 'points': [[-4837, 9553, -4596], [6315, -237, -5330], [8424, 2517, -3100], [9414, 3105, -365], [10044, 1911, 1880], [10492, -548, 2382], [10353, -2902, 2706], [9618, -4786, 3822], [8474, -6237, 5105], [7007, -7186, 6541], [5191, -7971, 7721], [3072, -8578, 8573], [730, -8971, 9039], [-1722, -9119, 9081], [-4258, -8912, 8771], [-6777, -8264, 8141], [-9216, -7127, 7164], [-11352, -5521, 5867], [-13233, -3265, 4116], [-14546, -259, 1863], [-14981, 5606, -2399]]}
ENDPOINTS={'AFFINE': ['-0x1.ef2ef38ea4c55p-2', '0x1.e8f210eff7d05p-1', '-0x1.d57a78a3ca757p-2', '0x1.433f034872991p-1', '-0x1.7d26f84ca4697p-6', '-0x1.1089863e9716cp-1', '0x1.af33196b3928bp-1', '0x1.0256b26467b49p-2', '-0x1.3bccf889df385p-2', '0x1.e1dff131429c8p-1', '0x1.3e9eccd2f3629p-2', '-0x1.1b3f0c2995a42p-5', '0x1.010fb19d75c49p+0', '0x1.88cc0a4dfedaep-3', '0x1.84c4a63156d1bp-3', '0x1.0c86f69b34ac9p+0', '-0x1.bafbe3c3d8503p-5', '0x1.eab90d40bef88p-3', '0x1.08f83e57e7ba6p+0', '-0x1.286f192c01521p-2', '0x1.160b7c1f2b37cp-2', '0x1.ec51224f350b4p-1', '-0x1.e968a97037000p-2', '0x1.87dc452a5b558p-2', '0x1.b1c24b1ab857fp-1', '-0x1.3f095d2690003p-1', '0x1.0567dce6ef20ep-1', '0x1.66aae6217bca8p-1', '-0x1.6fad775e069a3p-1', '0x1.4ebec2b1f4aa8p-1', '0x1.09b63ff3c25f1p-1', '-0x1.97ef22bf6edf8p-1', '0x1.8af75126029b0p-1', '0x1.3a7e3fc22b25bp-2', '-0x1.b716741af31bcp-1', '0x1.b662c9ca5c0a7p-1', '0x1.2aeeab453a588p-4', '-0x1.cb4ad52d87c37p-1', '0x1.ce0b2ca794051p-1', '-0x1.6093897aae5f4p-3', '-0x1.d2f4ec7ee116dp-1', '0x1.d00127e0f9effp-1', '-0x1.b3e8a80a4c237p-2', '-0x1.c872b0a3cdde4p-1', '0x1.bff80b642504cp-1', '-0x1.5ae50193cc57bp-1', '-0x1.a75bfd68ec614p-1', '0x1.9f9779a7c872bp-1', '-0x1.d7bd5fa340b88p-1', '-0x1.6d3b1a646d91bp-1', '0x1.6d7fe0404a950p-1', '-0x1.2289a1e6e0dc5p+0', '-0x1.1b1427b693d2ap-1', '0x1.2b16c699e6ec9p-1', '-0x1.52add54969d72p+0', '-0x1.4f465325ea92ep-2', '0x1.a3067f6a9b157p-2', '-0x1.7448880ece7e1p+0', '-0x1.b8d1f382ba8a3p-6', '0x1.7961557f82c17p-3', '-0x1.7f6aa0309e252p+0', '0x1.1e7fb83e4bfe7p-1', '-0x1.ed6999c00c4bap-3'], 'FREE': ['-0x1.00772283ab1bep-1', '0x1.01a13ec792723p+0', '-0x1.cce3c758f0132p-2', '0x1.47590a19886e7p-1', '0x1.5df25354bea0dp-6', '-0x1.122a05f383c7fp-1', '0x1.b1f21bed80f2fp-1', '0x1.896c57d149679p-3', '-0x1.3b855a7565d83p-2', '0x1.e38e06e387f74p-1', '0x1.26a5ac3730e98p-2', '-0x1.3972faf3648f2p-5', '0x1.fbde2d78d3142p-1', '0x1.cd27932bdbf25p-3', '0x1.d141808cf2c53p-3', '0x1.0c97beae31260p+0', '-0x1.4983eaffb4f55p-5', '0x1.f1cbd81dd7342p-3', '0x1.098b8406b1f1dp+0', '-0x1.271ab6dc7db48p-2', '0x1.049b92a96bfe0p-2', '0x1.eccbc55bd4119p-1', '-0x1.ef9e97447c9ccp-2', '0x1.730b837135738p-2', '0x1.b0f49d43e1c7ep-1', '-0x1.4412a3c458a0bp-1', '0x1.fb88b5c4c8117p-2', '0x1.68079d296c794p-1', '-0x1.69c57e490048bp-1', '0x1.54a79caa5722ep-1', '0x1.0a4e84b02fc63p-1', '-0x1.94b8113af6414p-1', '0x1.8f40997fe4cd3p-1', '0x1.3d6c269388b4cp-2', '-0x1.b7086661abe4dp-1', '0x1.b71b177e28d50p-1', '0x1.46260da902e56p-4', '-0x1.cba69ffe4dfbcp-1', '0x1.ce8752038f1eep-1', '-0x1.524e7af427604p-3', '-0x1.d0a6efc049010p-1', '0x1.d4c2acf63ff9ap-1', '-0x1.a98d2d989f285p-2', '-0x1.c7b1fe22fe90cp-1', '0x1.c52e84232af1fp-1', '-0x1.546d90b76f6bcp-1', '-0x1.a99def3337ff1p-1', '0x1.a4fb5071853e9p-1', '-0x1.d0403fa3cc865p-1', '-0x1.731f9c8422eb9p-1', '0x1.740593380c77bp-1', '-0x1.2215cc55bdee2p+0', '-0x1.2056e410e3d7fp-1', '0x1.2ff175ff76c9ep-1', '-0x1.51e749342bad6p+0', '-0x1.624ea9185e78ap-2', '0x1.b37fc348f8bc5p-2', '-0x1.761a123f58ecep+0', '-0x1.5dabae9c438abp-5', '0x1.9acaa6368662dp-3', '-0x1.85f70b31139c4p+0', '0x1.310f9ad3939f1p-1', '-0x1.01ed152ec9a45p-2']}
MANIFEST={'C114_RETRACT20_G4.json': [415, '929d757e793f95b3f1dd2121c4e4969f9fb79d959e0cbe7973e817c71943f307'], 'AFFINE_G4.json': [415, 'fff1195c3367844605deb414d289466ed1aa89346aa8e445b2cb82cf477a8a33'], 'AFFINE_G5.json': [479, '79cafe390a79d1170c747ef166e4c7a4ee1873b0813ac2438995303ce4e9ff80'], 'AFFINE_G6.json': [543, '1b5339ef07d1945fed9a0c7a748d594cd4499b9bd04de13d7aef1191ad89e16d'], 'AFFINE_G7.json': [607, '5cc0bd7898b5ef0d4955dffe6c79feaa8d48f9f2d727db4de7ab55ad384cf477'], 'FREE_G4.json': [414, 'b9286d8eada6f64d74f3baf25b97bbd94a7b3d7c89b88a0a957ecf08767cb134'], 'FREE_G5.json': [478, '88ab8b46712b0a206b3b6a6262d7e089148a45a55cd89d4ecdfebfeb53273c97'], 'FREE_G6.json': [542, '6e06d0576eb5fd9ae55161e4e0a14d21badeacf92c1794ca01b5e084ffcd64c4'], 'FREE_G7.json': [606, 'bc0b21df80ace28085a491f33fa2c1f0a364a0af1577ec0eeb6df6658c9111fd'], 'C114_RETRACT20_G4_EXACT.json': [48457, '9e7f3463a963e18f8e30691ddaeb499558b1a83c2e9468a826a314e23def139c'], 'AFFINE_G4_EXACT.json': [48752, 'c21be6ebfda361894a8b59b007940da64a31aff373880d4e70b2de8aeca082cb'], 'AFFINE_G5_EXACT.json': [59563, '5ed44ecdee145657647edf8cec6404359ba76f894656f1bb03499cc7bc7ed9f3'], 'AFFINE_G6_EXACT.json': [68905, 'e3b1a535879d32da7c39d98027d238423f0ff27765240c2a8af31809eb23a885'], 'AFFINE_G7_EXACT.json': [78849, 'd75e4860c03b62a0bf9ff9a07c60a73d4aed2c9c632eb17b001af80889acc6d0'], 'FREE_G4_EXACT.json': [53380, '0daa7be2860318b8ef97859588d5d80d084da6afcb6ccae7aecfa01a1d4caeb8'], 'FREE_G5_EXACT.json': [61917, '4e169b9fab072733125e134a8deece2ab883ea977fbb3d50eb2d07f9c76a1c06'], 'FREE_G6_EXACT.json': [71263, '236db7c9f100d70df271baccfd29c949e28c83c8b546467218efd9750239cced'], 'FREE_G7_EXACT.json': [81028, '8fda178a631b02ef5548525ad91d46cfd93d4c2921529e725981d92b70082d6d'], 'SUPPORT_GAP_METRICS.json': [27800, '124f0e43db9a7eb8172c6fbf35d7d4e5d5d1da08473aa85ac321757cd23cf6d9'], 'exact_turnover.py': [11252, 'c9ef4681d976faa810ea3e27631a5ad686ac904fb18ba2bd8a38e5435ad36f1d'], 'metrics_support.py': [2482, '8474a730ebdbc70df1bbaadfabc2f9239cce51833dbf26bbb3e901cf0817b6f4']}

def check(name):
    b=Path(name).read_bytes()
    assert [len(b),hashlib.sha256(b).hexdigest()]==MANIFEST[name],name

def main():
    here=Path(__file__).resolve().parent
    for name in ['exact_turnover.py','metrics_support.py']:
        b=(here/name).read_bytes()
        assert [len(b),hashlib.sha256(b).hexdigest()]==MANIFEST[name],name
    destination=Path(sys.argv[1] if len(sys.argv)>1 else 'cold_support_gap').resolve()
    destination.mkdir(parents=True,exist_ok=True);os.chdir(destination)
    names=['C114_RETRACT20_G4']
    write_json(names[0]+'.json',SEED)
    for label,hexes in ENDPOINTS.items():
        values=[F.from_float(float.fromhex(h)) for h in hexes]
        assert len(values)==63
        for k in [4,5,6,7]:
            g=10**k;pts=[[round(x*g) for x in values[i:i+3]] for i in range(0,63,3)]
            name=label+'_G'+str(k);names.append(name)
            write_json(name+'.json',dict(grid=g,points=pts))
    controls()
    for name in names:
        check(name+'.json')
        out=audit(json.loads(Path(name+'.json').read_text()))
        write_json(name+'_EXACT.json',out);check(name+'_EXACT.json')
        print(name,out['V'],out['E'],out['F'],list(map(len,out['mechanics']['strict'])),list(map(len,out['mechanics']['weak'])),flush=True)
    runpy.run_path(str(here/'metrics_support.py'),run_name='__main__')
    check('SUPPORT_GAP_METRICS.json')
    print('C114_SUPPORT_GAP_COLD_SOURCE_REPLAY_ALL_19_OUTPUT_HASHES_PASS',flush=True)
if __name__=='__main__':main()
