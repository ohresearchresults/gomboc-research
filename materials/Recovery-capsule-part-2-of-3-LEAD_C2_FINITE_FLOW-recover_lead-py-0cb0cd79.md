# material-0cb0cd79115a

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Complete literal geometry recovery for six finite C2 nonrecords.
Save with exact_lead.py and metrics_lead.py, Python3.13.5 standard library.
Run python -B -S recover_lead.py OUT, then python -B -S OUT/REPLAY.py.
All integers are literal exact inputs. C2_S3 G4/G6 are EXACT rational
roundings of G8, verified against all original input rows and receipts.
"""
import json,sys,hashlib,shutil
from pathlib import Path
from fractions import Fraction
BASE = {
'C2_CHAIN73_G5':[100000, [[26238, -33183, -449], [28609, -32974, 1377], [31068, -32622, 3163], [33612, -31201, 3205], [36189, -29878, 3505], [38688, -28246, 2635], [41231, -26550, 1567], [45835, -22747, 5614], [46527, -23010, -2028], [48629, -20638, -4619], [50610, -17985, -7414], [52269, -15197, -10603], [53678, -12163, -13945], [54713, -8984, -17475], [55455, -5544, -20967], [55775, -2050, -24596], [56060, 1993, -27597], [55691, 5844, -30890], [55645, 10469, -33108], [55107, 15007, -35336], [54544, 19835, -36915], [53773, 24810, -38099], [52919, 29976, -38683], [51886, 35281, -38777], [50731, 40714, -38272], [49323, 46257, -37298], [47569, 51911, -36024], [45410, 57642, -34363], [42821, 63379, -32173], [39514, 69077, -29756], [34279, 75329, -29269], [31227, 80399, -23427], [25738, 85647, -19474], [19273, 90649, -14772], [11522, 95090, -8761]], [3500, -33292, 1645]],
'C2_MASS_FREE75_G8_CONTROL':[100000000, [[46382421, -48054707, 558586], [45825307, -47286153, 14341221], [43659388, -46546805, 25556964], [39844021, -46044897, 35706454], [35051784, -45498814, 45768406], [27669017, -45425310, 54661278], [18424788, -43100472, 61219880], [7322805, -41293818, 65797048], [-4359348, -38109904, 69035098], [-16695617, -35242555, 69787437], [-29054518, -31779574, 68517515], [-40647561, -34852338, 62236058], [-51445987, -29826690, 57895754], [-60696564, -27076840, 51033398], [-68467150, -23593756, 43553933], [-74584021, -19930423, 35816897], [-79195792, -16457764, 28023899], [-82378452, -11837101, 21534194], [-84510789, -7713014, 15401130], [-85777436, -3401427, 10254059], [-86423556, 169322, 5591161], [-86593792, 4578267, 1821527], [-86332958, 9222169, -703065], [-85730377, 14055831, -2524880], [-84795921, 19059376, -3880987], [-83503059, 24249074, -4944952], [-81802987, 29625668, -5929467], [-79623396, 35202003, -6975636], [-76865659, 40998378, -8146213], [-73417316, 46981068, -9637455], [-69095673, 53232144, -11265808], [-63662692, 59870785, -12480426], [-56842647, 66961336, -13139879], [-47993045, 74613062, -13023721], [-34535659, 83675117, -13894797]], [22268708, -57684805, 40585559]],
'C2_PAIRDELETE71_G6':[1000000, [[262507, -330829, -5036], [286111, -329211, 13754], [310748, -326478, 33228], [336163, -312092, 32053], [361913, -298813, 35049], [386896, -282478, 26353], [412248, -265397, 15680], [459892, -224813, 62243], [465796, -230476, -20073], [486725, -206800, -46244], [506507, -180228, -74215], [523069, -152283, -106117], [537181, -121804, -139465], [547451, -89970, -174774], [554765, -55584, -209769], [557648, -20819, -246362], [560748, 19887, -276011], [556643, 57941, -309586], [556621, 104643, -331171], [550861, 149772, -353987], [545521, 198301, -369336], [537808, 248080, -381136], [529255, 299764, -386931], [518920, 352822, -387802], [507346, 407155, -382774], [493197, 462557, -372967], [475626, 519088, -360238], [453988, 576378, -343663], [427970, 633715, -321850], [394688, 690602, -297839], [341789, 753507, -293577], [311774, 803917, -234779], [192098, 906188, -148298], [114344, 950454, -88467]], [35050, -331697, 17377]],
'C2_S3_PROJECT73_G8':[100000000, [[26201155, -33655616, -304426], [28617265, -33120450, 1376697], [31070109, -32464896, 2838362], [33582821, -31157333, 3228189], [36140437, -29775004, 3395061], [38625047, -28153267, 2649611], [41245031, -26513597, 1696989], [45532784, -23509183, 3302004], [46555913, -22825512, -1935077], [48530136, -20530767, -4605926], [50468319, -17885201, -7416900], [52133372, -15105116, -10589955], [53579221, -12135777, -13957049], [54656999, -8944588, -17454810], [55417423, -5517743, -20947698], [55841751, -2003352, -24528451], [56042281, 2011883, -27572830], [55815392, 5904673, -30817766], [55668241, 10482600, -33082473], [55132940, 15058351, -35217718], [54496527, 19857345, -36827695], [53728630, 24819086, -38021747], [52852649, 29968124, -38661153], [51849348, 35274959, -38751117], [50674038, 40715349, -38342095], [49309121, 46261199, -37347087], [47629379, 51900385, -35935071], [45476226, 57636209, -34285271], [42783118, 63400025, -32286031], [39395404, 69229508, -30210407], [35238221, 75343256, -27214715], [31110825, 80324988, -23490703], [25739318, 85815461, -19691682], [19429416, 90655782, -14560758], [11675984, 95194106, -8617459]], [3489864, -33715409, 1386565]],
}
EXPECTED = {'C2_CHAIN73_G5.audit.json': [145159, 'ab6144fd3501ee075df3df2926c1a4d9c358d5540154a17aa59524056e7137d9'], 'C2_CHAIN73_G5.json': [4060, 'dcd15cc7a29a6fe69e520dc71c7c49b69a9e853f43df499a94fab370b5a6ba48'], 'C2_MASS_FREE75_G8_CONTROL.audit.json': [230060, 'aad41adac2566705ce74d0007bfd26a6b8b46be83d5c5dcffe48ce3552b7f234'], 'C2_MASS_FREE75_G8_CONTROL.json': [4754, '340b0d8ed6b7df12cda9ecbefa813d850233e8a97011e2bd6364aeba930ec93e'], 'C2_PAIRDELETE71_G6.audit.json': [157844, 'b6f6685cf5b368567670116fd94ea836afec623fe49b4f9a00cbbb4498182359'], 'C2_PAIRDELETE71_G6.json': [4179, '7a7b470d306b1789d71340ef3458bf70cadcf46b5ae7503a233d77229fb9d3a5'], 'C2_S3_PROJECT73_G4_CONTROL.audit.json': [132962, 'bd9cdb7d3bdaf9093cb49bf6b04b7bb3a5939422a582faae43d31ac2c5712cba'], 'C2_S3_PROJECT73_G4_CONTROL.json': [3849, '274769e18fa881a962eb624b71afee3722c1277b55091281cecfd7fe24af35b0'], 'C2_S3_PROJECT73_G6.audit.json': [160639, '8745e40d8eee2b1ee0c0172fa939f4c56b4ecf8a13727fb0310e819499c54cc9'], 'C2_S3_PROJECT73_G6.json': [4289, '918661eb41dc89ab6fb6d437889c8812a737106c086d0c61e38f93f75812edbe'], 'C2_S3_PROJECT73_G8.audit.json': [192624, '7a3337db25cdc6e73fdd99ea0aed1f201cf1bc204b4b0b7040f495771682903c'], 'C2_S3_PROJECT73_G8.json': [4737, '5900d507f94e7859856b737683c1723dc5fa44678876f0898db8b6499079cfc0'], 'LEAD_C2_EXACT_METRICS.json': [92801, '865555af165ca6818d6b4db6937ed3c19bf38137f24f5dc01044eeada9eb2569']}
def data(name,scale,half,tail):
    xb,yb,zb=tail
    rows=half+[[-x,y,-z] for x,y,z in half]+[[0,scale,0],[xb,yb,zb],[-xb,yb,zb],[-xb,yb,-zb],[xb,yb,-zb]]
    return dict(identity=name,scale=scale,rows=rows,rounding='Python round nearest ties-to-even; literal integer rows authoritative',half_count=len(half))
def main():
    out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
    defs={name+'.json':data(name,*values) for name,values in BASE.items()}
    scale,half,tail=BASE['C2_S3_PROJECT73_G8']
    for g in (4,6):
        name='C2_S3_PROJECT73_G'+str(g)+('_CONTROL' if g==4 else '')
        div=10**(8-g)
        defs[name+'.json']=data(name,10**g,[[round(Fraction(v,div)) for v in row] for row in half],[round(Fraction(v,div)) for v in tail])
    raw=(json.dumps(defs,sort_keys=True,separators=(',',':'))+'\n').encode()
    assert len(raw)==12004 and hashlib.sha256(raw).hexdigest()=='0266b7d8f6760abc17f19b82247fdd515d0d1ad0431b7a93c157c94b92d3ab9c'
    (out/'EXACT_DEFINITIONS.json').write_bytes(raw)
    (out/'EXPECTED_RECEIPTS.json').write_text(json.dumps(EXPECTED,sort_keys=True,indent=2)+'\n')
    here=Path(__file__).resolve().parent
    for name in ('exact_lead.py','metrics_lead.py'):
        if (here/name).resolve()!=(out/name).resolve():shutil.copyfile(here/name,out/name)
    (out/'REPLAY.py').write_text(REPLAY)
    print('LEAD_C2_LITERAL_HALF_ROW_RECOVERY_PASS',len(defs))
REPLAY = '"""Cold recovery of six exact C2 nonrecords. Python3.13.5 standard library.\nRun: python -B -S REPLAY.py. No historical numerical checkpoint is required.\n"""\nimport json,sys,subprocess,hashlib\nfrom pathlib import Path\n\ndef receipt(p):\n    b=p.read_bytes();return [len(b),hashlib.sha256(b).hexdigest()]\ndef main():\n    root=Path(__file__).resolve().parent;out=root/\'exact\';out.mkdir(exist_ok=True)\n    expected=json.loads((root/\'EXPECTED_RECEIPTS.json\').read_text());defs=json.loads((root/\'EXACT_DEFINITIONS.json\').read_text())\n    assert len(defs)==6\n    subprocess.run([sys.executable,\'-B\',\'-S\',str(root/\'exact_lead.py\'),\'--controls\'],check=True)\n    for name,data in sorted(defs.items()):\n        p=out/name;raw=(json.dumps(data,sort_keys=True,indent=2)+\'\\n\').encode();p.write_bytes(raw)\n        assert receipt(p)==expected[name]\n        audit=p.with_suffix(\'.audit.json\')\n        subprocess.run([sys.executable,\'-B\',\'-S\',str(root/\'exact_lead.py\'),str(p),str(audit)],check=True)\n        assert receipt(audit)==expected[audit.name]\n    subprocess.run([sys.executable,\'-B\',\'-S\',str(root/\'metrics_lead.py\'),str(out)],check=True)\n    for name,rr in expected.items():assert receipt(out/name)==rr,name\n    print(\'LEAD_C2_SIX_EXACT_NONRECORDS_THIRTEEN_COLD_RECEIPTS_PASS\',len(defs),len(expected))\nif __name__==\'__main__\':main()\n'
if __name__=="__main__":main()
