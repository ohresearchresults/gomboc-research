# A discontinuity in the selected-tree penalty

This is an objective-function calculation, not a polyhedron candidate or a low-complexity search.

Let the target root be R(s)=(1-s/10,sqrt(99)*s/10,0), a=(1,0,0), b=(11/10,1/10,0), and W(x,y)=x.(y-x)/(|x||y-x|). For s near the positive root sigma of

(9800-2200sqrt(99))*s^2+(26156-2156sqrt(99))*s+14156=0,

R has the largest norm. W(a,R)=-1/10, W(a,b)=1/sqrt(2), W(b,a)=-6/sqrt(61), and W(b,R) crosses -1/10 upwards at sigma. The widest-path rooted tree has direct edges a->R,b->R just below sigma. Just above sigma it has a->b,b->R. Hence sum_nonroot max(-W(node,parent),0) jumps from limit1/5 to limit1/10. This is a realizable angular escape matrix, not an arbitrary unrelated graph weight example.

In contrast c_i=max_paths_to_root min_edges W(edge) is a finite maximum/minimum of continuous edge weights for fixed distinct vectors/root. Its nonroot deficit sum has limit1/5 from both sides. `bottleneck_capacity.py` computes these capacities and active edge derivative witnesses; the literal numerical control is `artifacts/forest-merit-counterexample.json`.

Scope: this identifies an algorithmic discontinuity in the direct-edge L1 merit. It does not imply convexity, smoothness, descent at all tied policies, absence of local minima, or continuity across changing vertex sets/root selection. Exact physical audits remain necessary. On peer2's fixed C498 contact chart, continuous-capacity correction advanced from merit19.34 to13.60 before another finite stall; it did not yield110.
