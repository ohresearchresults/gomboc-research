from detach_main_stable_cap import *
source=ROOT/'artifacts/retire_current/exact_concave_checkpoint1/exact_E245/audit.json'
for name,t,e in [('t005_e0005',mpq(1,20),mpq(1,2000)),('t025_e0004',mpq(1,4),mpq(1,2500)),('t09_e0005',mpq(9,10),mpq(1,2000))]:
 construct(source,ROOT/'artifacts/detached_main_cap'/name,t,e)
