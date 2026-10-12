"""Native HiGHS with an explicitly feasible rooted-tree incumbent.
The current actual body's checked minimum tree defines binary edges and exact
integer flows. A continuous LP refines the physical local-model variables with
that assignment fixed; the independently checked result seeds the SAME MIP.
There is no alternate acceptance test and no substitution for actual geometry.
HiGHS discards coefficients <=1e-12. We make that operation explicit and
conservative: bound each removed term over the finite variable trust box and
tighten BOTH sides of each affected row by the sum of those absolute bounds.
Thus the solver's ideal feasible region is a subset of the original scaled
floating model's. Physical validation still uses the original unscaled rows.
"""
from types import SimpleNamespace
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix,csr_matrix,vstack
import highspy

def solve(c,A,lo,hi,lower,upper,integer,scale,seed,binary_start,edge_count,time_limit=8.):
    nv=len(c);fixed=seed.copy();bounds=list(zip(lower,upper))
    for i in range(binary_start,nv):bounds[i]=(float(fixed[i]),float(fixed[i]))
    M=csr_matrix(A*scale[:,None]);coo=M.tocoo();small=abs(coo.data)<=1e-12;columns=coo.col[small];radii=np.maximum(abs(lower[columns]),abs(upper[columns]))
    if not np.isfinite(radii).all():raise ValueError('a discarded coefficient has no finite rigorous trust-box bound')
    counts=np.bincount(coo.row[small],minlength=len(lo));terms=np.nextafter(abs(coo.data[small])*radii,np.inf);total=np.bincount(coo.row[small],weights=terms,minlength=len(lo));factor=np.nextafter(1/(1-counts*(np.finfo(float).eps/2)),np.inf);enclosure=np.where(counts>0,np.nextafter(total*factor,np.inf),0.)
    M.data[abs(M.data)<=1e-12]=0;M.eliminate_zeros();solver_lo=lo*scale+enclosure;solver_hi=hi*scale-enclosure;affected=counts>0;solver_lo[affected]=np.nextafter(solver_lo[affected],np.inf);solver_hi[affected]=np.nextafter(solver_hi[affected],-np.inf)
    if np.any(solver_lo>solver_hi):raise ValueError('conservative coefficient enclosure exhausted an equality row')
    a=np.isfinite(solver_hi);b=np.isfinite(solver_lo)
    initial=linprog(c,A_ub=vstack([M[a],-M[b]],format='csr'),b_ub=np.r_[solver_hi[a],-solver_lo[b]],bounds=bounds,method='highs-ipm',options=dict(primal_feasibility_tolerance=1e-10,dual_feasibility_tolerance=1e-9,time_limit=6.))
    if not initial.success:raise ValueError('fixed rooted-tree local incumbent LP failed: '+initial.message)
    x=initial.x
    violation=max(float(np.maximum(lo-A@x,0).max()),float(np.maximum(A@x-hi,0).max()),float(np.maximum(lower-x,0).max()),float(np.maximum(x-upper,0).max()))
    integral_error=float(abs(x[binary_start:binary_start+edge_count]-np.round(x[binary_start:binary_start+edge_count])).max())
    if violation>1e-7 or integral_error>1e-8:raise ValueError('declared rooted-tree incumbent failed its complete local-model check')
    solver=highspy.Highs()
    for name,value in dict(output_flag=False,threads=1,time_limit=time_limit,mip_rel_gap=.01,mip_feasibility_tolerance=1e-9,primal_feasibility_tolerance=1e-9,small_matrix_value=1e-12).items():
        if solver.setOptionValue(name,value)!=highspy.HighsStatus.kOk:raise ValueError('native solver rejected explicit option '+name)
    matrix=csc_matrix(M);model=highspy.HighsLp();model.num_col_=nv;model.num_row_=len(lo);model.col_cost_=c;model.col_lower_=lower;model.col_upper_=upper;model.row_lower_=solver_lo;model.row_upper_=solver_hi;model.integrality_=[highspy.HighsVarType.kInteger if i else highspy.HighsVarType.kContinuous for i in integer];model.a_matrix_.format_=highspy.MatrixFormat.kColwise;model.a_matrix_.start_=matrix.indptr.astype(np.int32);model.a_matrix_.index_=matrix.indices.astype(np.int32);model.a_matrix_.value_=matrix.data
    submitted=solver.passModel(model)
    if submitted!=highspy.HighsStatus.kOk:
        solver.setOptionValue('output_flag',True);diagnostic_status=solver.passModel(model)
        print('NATIVE_MODEL_DIAGNOSTIC',submitted,diagnostic_status,'supplied_nonzeros',matrix.nnz,'retained_nonzeros',len(solver.getLp().a_matrix_.value_),flush=True)
        raise ValueError('native model submission requires investigation: '+str(submitted))
    initial_solution=highspy.HighsSolution();initial_solution.col_value=x;initial_solution.row_value=np.asarray(M@x);initial_solution.value_valid=True
    if solver.setSolution(initial_solution)!=highspy.HighsStatus.kOk:raise ValueError('native solver rejected the independently checked incumbent')
    status=solver.run()
    if status==highspy.HighsStatus.kError:raise ValueError('native seeded MIP failed')
    solution=solver.getSolution();info=solver.getInfo();model_status=solver.getModelStatus()
    if not solution.value_valid:raise ValueError('native MIP lost an explicitly supplied feasible incumbent')
    return SimpleNamespace(x=np.asarray(solution.col_value),status=int(model_status),message=solver.modelStatusToString(model_status),seed_objective=float(c@x),seed_violation=violation,mip_gap=float(info.mip_gap),solver_version=solver.version(),enclosed_coefficients=int(small.sum()),maximum_coefficient_enclosure=float(enclosure.max()))
