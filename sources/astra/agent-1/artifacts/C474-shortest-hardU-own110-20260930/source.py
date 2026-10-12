"""Actual-mass shortest escape correction across explicitly rebuilt hulls."""
import pathlib,json,time,contextlib
import numpy as np
from contact_forest import ContactModel,correct
from merge_contact_vertices import run as merge_vertices
from merge_contact_facets import run as merge_facets

def run(source,input,out,events=60,steps=1200,epsilon=2e-8,hard_side=None):
    source=pathlib.Path(source);input=pathlib.Path(input);out=pathlib.Path(out);out.mkdir(parents=True,exist_ok=False);hist=[];start=time.time()
    (out/'source.py').write_bytes(pathlib.Path(__file__).read_bytes());(out/'definition.json').write_text(json.dumps(dict(source=str(source.resolve()),input=str(input.resolve()),events=events,steps=steps,epsilon=epsilon,hard_side=hard_side,scope='Continuous shortest-path escape correction with explicit physical topology reconstruction; only own110 nominates exact audit'),indent=2))
    for k in range(events):
        p=out/f'stage{k:03d}';p.mkdir();c=ContactModel(source,1,1,'shortest',escape_floor=epsilon);z=np.load(input)['z']
        if not 17<=c.meta['E']<=249:raise ValueError('Input contact complex is outside goal budget')
        with (p/'calculation.log').open('w') as log,contextlib.redirect_stdout(log):
            z,e,ok=correct(c,z,p/'flow',steps=steps,eps=epsilon,trust=.012,physical_retraction=True,acceptance='armijo',geometry_event_tolerance=2e-7,hard_side=hard_side)
        np.savez(p/'final.npz',z=z,X=e['X'],Q=e['Y']);row=dict(stage=k,E=c.meta['E'],S=e['S'],U=e['U'],Pmax=max([b['relative'] for b in e['bars'][0]],default=0),Qmax=max([b['relative'] for b in e['bars'][1]],default=0),seconds=time.time()-start)
        if e['S']==e['U']==1:
            np.savez(out/'POTENTIAL_OWN110.npz',z=z,X=e['X'],Q=e['Y']);(out/'POTENTIAL_OWN110.json').write_text(json.dumps(dict(chart=str(source.resolve()),input=str((out/'POTENTIAL_OWN110.npz').resolve()),**row),indent=2));return
        ev=p/'flow/EDGE_EVENT.json'
        if not ev.exists():
            row['event']=False;hist.append(row);(out/'history.json').write_text(json.dumps(hist,indent=2));(out/'FINITE_END.json').write_text(json.dumps(dict(**row,scope='Finite correction ended without own110 or an admitted edge event'),indent=2));return
        event=json.loads(ev.read_text());side=event['side'];i,j=event['edge'];A=e['X'] if side==0 else e['Y'];scale=np.sqrt(np.mean((e['P'] if side==0 else A)**2));tol=1.05*np.linalg.norm(A[j]-A[i])/scale+1e-13
        try:
            producer=merge_vertices if side==0 else merge_facets
            with (p/'merge.log').open('w') as log,contextlib.redirect_stdout(log):summary=producer(source,p/'final.npz',p/'body',tol,1,1,'balanced')
            if summary['E']>=c.meta['E']:raise ValueError('Explicit topology event did not reduce true graph edges')
            source=p/'body/chart';input=p/'body/realization.npz';child=ContactModel(source,1,1,'shortest',escape_floor=epsilon);ce=child.evaluate(np.load(input)['z'],False)
            row.update(event=event,newE=child.meta['E'],newS=ce['S'],newU=ce['U'],source=str(source.resolve()),input=str(input.resolve()),admitted=True)
        except (ValueError,RuntimeError,AssertionError,np.linalg.LinAlgError) as error:
            row.update(event=event,admitted=False,error=str(error));(out/'UNADMITTED_EVENT.json').write_text(json.dumps(row,indent=2));hist.append(row);(out/'history.json').write_text(json.dumps(hist,indent=2));print('SHORTEST_EVENT_UNADMITTED',json.dumps(row),flush=True);return
        hist.append(row);(out/'history.json').write_text(json.dumps(hist,indent=2));(out/'latest.json').write_text(json.dumps(row,indent=2));print('SHORTEST_PHYSICAL_EVENT',json.dumps(row),flush=True)
    (out/'FINITE_END.json').write_text(json.dumps(dict(events=events,seconds=time.time()-start,scope='Finite event sequence exhausted without a qualifying body'),indent=2))

if __name__=='__main__':
    import sys
    run(sys.argv[1],sys.argv[2],sys.argv[3])
