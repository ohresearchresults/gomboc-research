# material-8474a730ebdb

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

---

"""Certified support-bar intervals; exact auditor outputs are the inputs."""
import json
from fractions import Fraction as F
from pathlib import Path
from exact_turnover import interval_power,write_json

SCALE=10**12

def root_interval(a,k):
    lo,hi,s=interval_power(a,k,10**24)
    return F(lo,s),F(hi,s)

def outward(lo,hi):
    lo*=SCALE;hi*=SCALE
    return [lo.numerator//lo.denominator,-(-hi.numerator//hi.denominator),SCALE]

def metrics(report,base):
    vol=F(report['volume']);vl,vu=root_interval(vol,3)
    intervals=[]
    for bar in report['polar']['bars']:
        b,d=F(bar['birth']),F(bar['death'])
        al,au=root_interval(1/b,2);bl,bu=root_interval(1/d,2)
        intervals.append(((bl-au)/vu,(bu-al)/vl))
    total=outward(sum((a for a,b in intervals),F(0)),sum((b for a,b in intervals),F(0)))
    largest=outward(max((a for a,b in intervals),default=F(0)),max((b for a,b in intervals),default=F(0)))
    pts=[[F(t) for t in z] for z in report['physical']['points']]
    bp=[[F(t) for t in z] for z in base['physical']['points']]
    dd=[sum(((x-y)**2 for x,y in zip(a,b)),F(0)) for a,b in zip(pts,bp)]
    dist=root_interval(max(dd),2)
    return dict(V=report['V'],E=report['E'],F=report['F'],C=report['C'],strict=list(map(len,report['mechanics']['strict'])),weak=list(map(len,report['mechanics']['weak'])),zeros=report['mechanics']['primitive_zero_counts'],Pbars=len(report['physical']['bars']),Qbars=len(intervals),TQ=report['TQ'],support_sum=total,support_max=largest,matched_centered_Hausdorff_upper=outward(*dist),matched_argmax=dd.index(max(dd)),matched_squared=dd,volume=vol)

if __name__=='__main__':
    base=json.loads(Path('C114_RETRACT20_G4_EXACT.json').read_text())
    names=['C114_RETRACT20_G4']+[f'{n}_G{k}' for n in ['AFFINE','FREE'] for k in [4,5,6,7]]
    out={n:metrics(json.loads(Path(n+'_EXACT.json').read_text()),base) for n in names}
    base_eta=(root_interval(1/F(base['polar']['bars'][0]['death']),2)[0]-root_interval(1/F(base['polar']['bars'][0]['birth']),2)[1])/2
    for n,z in out.items():
        assert F(z['matched_centered_Hausdorff_upper'][1],SCALE)<base_eta
        print(n,z['strict'],z['support_sum'],z['support_max'],z['matched_centered_Hausdorff_upper'])
    assert out['FREE_G6']['support_sum'][1]<out['C114_RETRACT20_G4']['support_sum'][0]
    assert out['FREE_G6']['strict']==[4,1,3]
    receipt=write_json('SUPPORT_GAP_METRICS.json',out)
    print('SUPPORT_GAP_EXACT_METRICS_AND_PROTECTED_REGION_PASS',receipt)
