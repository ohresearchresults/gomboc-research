# material-a2d991bdda7e

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Summarize exact reports without deleting any small positive bar.
Python3.13.5 standard library. Run python -B -S metrics_lead.py exact.
"""
import json,sys,math,hashlib
from pathlib import Path
from fractions import Fraction as F

def main():
    root=Path(sys.argv[1]) if len(sys.argv)>1 else Path('exact');out={}
    for p in sorted(root.glob('*.audit.json')):
        d=json.loads(p.read_text());row={k:d[k] for k in ('V','E','F','C','actual_volume','actual_centroid','strict','additional_weak','primitive_zero_counts','inradius_circumradius_squared','extreme_source_indices')}
        row['centred_coordinate_denominator_bits']=int(d['physical_coordinate_multiplier']).bit_length()
        row['r_over_R']=math.sqrt(float(F(d['inradius_circumradius_squared'])))
        row['P_bars']=len(d['physical_landscape']['bars'])
        row['Q_bars']=d['polar_landscape']['bars']
        row['Q_metrics']=[{'peak':b['peak'],'elder':b['elder'],'component_size':len(b['component']),'cut_size':len(b['cut']),'death_relative':float(F(b['death_relative'])),'birth_relative':float(F(b['birth_relative']))} for b in d['polar_landscape']['bars']]
        row['minimum_positive_true_edge_cosine_squared']=str(min(F(e['cosine_squared']) for e in d['positive_true_edge_forest']))
        row['minimum_positive_true_edge_cosine']=math.sqrt(float(F(row['minimum_positive_true_edge_cosine_squared'])))
        out[d['identity']]=row
        print(d['identity'],[d[k] for k in ('V','E','F','C')],{k:len(v) for k,v in d['strict'].items()},'c',list(map(lambda x:float(F(x)),d['actual_centroid'])),'r/R',row['r_over_R'],'Db',row['centred_coordinate_denominator_bits'],'cos',row['minimum_positive_true_edge_cosine'])
        print('Q',row['Q_metrics'])
    target=root/'LEAD_C2_EXACT_METRICS.json';raw=(json.dumps(out,sort_keys=True,indent=2)+'\n').encode();target.write_bytes(raw);print(target.name,len(raw),hashlib.sha256(raw).hexdigest());print('LEAD_C2_COMPLETE_METRICS_PASS')
if __name__=='__main__':main()
