"""Own-centroid monounstable persistence annealing with exact strict checkpoints."""
import argparse,json
from pathlib import Path
from primal_log_thales import run as descent
from polish_211 import run as repair
from exact_audit_vertices import audit
from exact_barcode_report import report

def run(source,out,steps):
    out=Path(out);out.mkdir(parents=True,exist_ok=False);(out/'input.npy').write_bytes(Path(source).read_bytes());p=out/'input.npy';rows=[]
    for k,eta in enumerate([.001,.00001]):
        d=out/f'stage{k}';descent(p,d,steps,eta,True);p=d/'best.npy';repair(p,d/'strict211',500,1e-7)
        if(d/'strict211/success.npy').exists():
            a=audit(d/'strict211/success.npy',d/'exact_g12',10**12);report(d/'exact_g12');row=dict(stage=k,eta=eta,counts=a['counts'],weak=a['weak'],exact=str(d/'exact_g12'))
        else:row=dict(stage=k,eta=eta,result='finite strict211 correction failed')
        rows.append(row);(out/'results.json').write_text(json.dumps(rows,indent=2));print('THALES_ANNEAL_STAGE',row,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('source');p.add_argument('out');p.add_argument('--steps',type=int,default=650);a=p.parse_args();run(a.source,a.out,a.steps)
