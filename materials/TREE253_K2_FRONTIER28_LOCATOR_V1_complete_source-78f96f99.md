# material-78f96f9966bb

AI research material · [Export notes](../catalog/coverage.md#text-records)

---

"""TREE253_K2_FRONTIER28_LOCATOR_V1: complete new direction wrapper.

Dependency source units, unchanged and exact: shared code from
[internal-source-reference], and literal native55/transport source from
[internal-source-reference]. Save the latter as
primal_path_transport_recovery.txt beside this file and extract shared_code/
from the former. Exact source bytes are pinned below. The complete locators,
all sparse-pencil builders, all exact checkers, and all nondefault numeric
parameters belong to that shared dependency. The present wrapper supplies
only the new literal indices[private-runtime-path] input and exact rounding.

Usage: python frontier_locate.py NATIVE_INDEX ROOT standard
    or python frontier_locate.py NATIVE_INDEX ROOT alternative
Valid native indices are the28 open representatives of the accepted214
ledger [internal-source-reference]; roots are1,...,8. Alternative means
exactly facet-cycle shifts[0,1], all ten apices, duplicate complete fans removed.
The output directory name records every command input. Running in a fresh
working directory is recommended; no previous numerical proposal is an input.
The start vector is zero and there is no random input. Each complete exact
record retains every integer coefficient and the chosen rounding power.

Exact verification (from the resulting f28_iI_rR_KIND/ directory):
  python -S ../shared_code/verify_catalogue.py certificates.json exact_report.json
or, for alternative,
  python -S ../shared_code/verify_variants.py certificates.json exact_report.json
The exact checkers use only standard-library integer and Fraction arithmetic.
A success marker in this wrapper states EPHEMERAL_NOT_IMMUTABLY_PERSISTED:
the complete exact source/data capsule still MUST be stored before promotion.
Failure to produce an exact record means UNKNOWN, never geometric feasibility
or impossibility. All returned numerical candidates are preserved even when
rounding fails, to distinguish that observation from a proved exclusion.

Observed numeric environment: Python3.13.5 NumPy2.3.5 SciPy1.17.0,
OpenBLAS0.3.30 x86_64 Linux; both thread counts1. Ordered rounding powers
12,14,16,18,20,24; np.rint with integer64 output (bounded coefficients ensure
no overflow). Every candidate is independently checked by the pinned exact
checker before success is reported. Complete reconstruction of an accepted
result will use its frozen coefficients, not demand floating bitwise replay.
"""
from pathlib import Path
import hashlib,json,os,runpy,subprocess,sys
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
HERE=Path(__file__).resolve().parent
assert __debug__
PINS={'primal_path_transport_recovery.txt':[13252,'4a4c26be277540ea88a012c66cf7a8373bd65d0f4c935ae717a99b4acf8c3c1a'],
      'shared_code/grouped_search.py':[5142,'bd4afc0a07d93cf66836a16d9ae1e41a17c78617177c2981d10b82617afa0373'],
      'shared_code/verify_catalogue.py':[8229,'459eb1de9cf3d876f9937832ca13c12b9ee0b1faa0c0a13ab9966d3ad2c55cac'],
      'shared_code/verify_variants.py':[9034,'dbdfbb3cee97fffcd0a19e6d2dc3d372d58f6822247850f18d45c2f0bf8241a0'],
      'shared_code/variant_search.py':[2055,'55424fd54559d7ae0325feaf9fb8caffd5bb4015b2a55c9b4f8511a3388c0216']}
REPRESENTATIVES=(10,13,15,17,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,43,44,48,51,52,53,54)
POWERS=(12,14,16,18,20,24)
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
def enc(x):return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def main():
    assert len(sys.argv)==4
    index,root=map(int,sys.argv[1:3]);kind=sys.argv[3]
    assert index in REPRESENTATIVES and 1<=root<=8 and kind in ('standard','alternative')
    for name,p in PINS.items():assert pin((HERE/name).read_bytes())==p,(name,pin((HERE/name).read_bytes()),p)
    ns=runpy.run_path(str(HERE/'primal_path_transport_recovery.txt'),run_name='_literal_native55')
    table={int(line.split(':')[0]):line.split(':')[1].split() for line in ns['NATIVE55'].splitlines()}
    incidence=table[index]
    sys.path.insert(0,str(HERE/'shared_code'))
    import grouped_search as g
    import numpy as np
    if kind=='standard':
        import verify_catalogue as exact
        g.INCIDENCE=tuple(incidence)
        d=g.pencil(root,list(range(10)),True)
        extra={}
    else:
        import verify_variants as exact
        from variant_search import variant_geometry
        shifts=[0,1]
        path,faces,fans,labels=variant_geometry(incidence,shifts)
        g.geometry=lambda:(path,faces,fans)
        d=g.pencil(root,list(range(len(fans))),True)
        extra={'shifts':shifts,'fan_labels':labels}
    work=HERE/f'f28_i{index}_r{root}_{kind}';work.mkdir(exist_ok=True);os.chdir(work)
    x,l=g.locate(d)
    out={k:v for k,v in d.items() if k not in ('A','bounds')}
    out.update(native_index=index,incidence=incidence,coefficients=x.tolist(),numerical_minimum=l,
               proof_status='NUMERICAL_ONLY',**extra)
    Path('candidate.json').write_bytes(enc(out))
    accepted=None;trials=[]
    for power in POWERS:
        scaled=np.rint(np.asarray(x)*2**power)
        assert np.isfinite(scaled).all() and np.abs(scaled).max()<2**62
        rec=dict(native_index=index,root=root,apices=d['apices'],rounding_power=power,
                 coefficients=scaled.astype(np.int64).tolist(),**extra)
        try:report=exact.check_case(rec,incidence)
        except (AssertionError,ZeroDivisionError) as e:
            trials.append({'power':power,'status':'NOT_EXACTLY_ACCEPTED','exception_type':type(e).__name__})
            continue
        accepted=rec;trials.append({'power':power,'status':'EXACTLY_ACCEPTED'});break
    status={'native_index':index,'root':root,'kind':kind,'numerical_minimum':l,'rounding_trials':trials,
            'candidate_pin':pin(Path('candidate.json').read_bytes())}
    if accepted is not None:
        ident='TREE253_K2_SHARED_ACTUAL_MOMENTS_CATALOGUE_V2' if kind=='standard' else 'TREE253_K2_ALTERNATIVE_FAN_SHARED_MOMENTS_V1'
        cb=enc({'identity':ident,'incidences':{str(index):incidence},'records':[accepted]})
        Path('certificates.json').write_bytes(cb)
        script=HERE/'shared_code'/('verify_catalogue.py' if kind=='standard' else 'verify_variants.py')
        p=subprocess.run([sys.executable,'-S',str(script),'certificates.json','exact_report.json'],check=True,stdout=subprocess.PIPE)
        Path('exact.log').write_bytes(p.stdout)
        status.update(status='EXACT_CHECK_PASS_EPHEMERAL_NOT_IMMUTABLY_PERSISTED',cells=report['cells'],
                      certificate_pin=pin(cb),report_pin=pin(Path('exact_report.json').read_bytes()),stdout_pin=pin(p.stdout))
    else:status['status']='UNKNOWN_NO_EXACT_CERTIFICATE'
    Path('status.json').write_bytes(enc(status));print('FRONTIER_RESULT',json.dumps(status,sort_keys=True),flush=True)
if __name__=='__main__':main()
