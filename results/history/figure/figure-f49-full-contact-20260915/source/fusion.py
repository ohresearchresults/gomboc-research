"""Specific S8 face fusion, original supports49 and50. No optimization needed.
Source: exact S8 generator plus its maximal oriented face cycles.
Only q49 is redefined through auxiliary points144,148,154; q50 disappears.
Original auxiliary147 now constrains q0,q131 only, not a physical vertex.
"""
import json,copy,sys
from pathlib import Path

def make(d,faces):
    assert d['n_supports']==137
    assert next(t for t in d['plan'] if t[0]==49)==[49,[147,148,154],[0,1,2]]
    z=copy.deepcopy(d)
    remap=lambda i:i-(i>50)
    z['n_supports']=136
    del z['controls'][50]
    plan=[]
    for i,deps,axes in d['plan']:
        if i==50:continue
        if i==49:deps=[144,148,154]
        assert 50 not in deps
        plan.append([remap(i),[remap(j) for j in deps],axes])
    z['plan']=plan
    z['groups']=[[remap(k) for k in g if k!=50 and not (gi==10 and k==49)] for gi,g in enumerate(d['groups'])]
    z['groups'][7]=sorted(z['groups'][7]+[49])
    # cancel the two directed occurrences of shared edge31--38.
    edges=[]
    for f in [49,50]:
        cy=faces[f]
        edges.extend(zip(cy,cy[1:]+cy[:1]))
    boundary=[(a,b) for a,b in edges if (b,a) not in edges]
    follow=dict(boundary);assert len(follow)==len(boundary)
    start=min(follow);cy=[start]
    while follow[cy[-1]]!=start:
        cy.append(follow[cy[-1]]);assert len(cy)<=len(boundary)
    assert len(cy)==len(boundary)
    nf=copy.deepcopy(faces);nf[49]=cy;del nf[50]
    return z,nf

if __name__=='__main__':
    src=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(exist_ok=False)
    d=json.loads((src/'GENERATOR.json').read_text());a=json.loads((src/'A.json').read_text())
    z,fs=make(d,a['faces'])
    (out/'GENERATOR.json').write_text(json.dumps(z,sort_keys=True,separators=(',',':')))
    (out/'faces.json').write_text(json.dumps(fs,separators=(',',':')))
    print('S8_F49_50_CONTACT_SWITCH_DEFINED')
