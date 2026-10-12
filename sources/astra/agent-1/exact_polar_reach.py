"""Exact own-centred positive polar reachability on already audited H-bodies.
For centroid G/D and support n_i.x<=h_i, let s_i=h_i D-n_i.G>0.
The sign of q_i.(q_j-q_i), q_i=D n_i/s_i, is the integer sign
n_i.(s_i n_j-s_j n_i). All cancelled denominators are positive.
This supplements an exact body audit; it never replaces one.
"""
import json,pathlib,math,hashlib,sys
import gmpy2
sys.set_int_max_str_digits(0)

def compute(folder,elder=18):
    folder=pathlib.Path(folder);p=folder/'audit.json';a=json.loads(p.read_text());g=[gmpy2.mpq(s) for s in a['centroid']];D=gmpy2.mpz(math.lcm(*(int(x.denominator) for x in g)));G=[gmpy2.mpz(x*D) for x in g]
    H=[[gmpy2.mpz(v) for v in h] for h in a['raw_halfspaces']];N=[h[:3] for h in H];s=[h[3]*D-sum(n*t for n,t in zip(h[:3],G)) for h in H];assert min(s)>0
    adj=[];zeros=[]
    for i,n in enumerate(N):
        row=[]
        for j,m in enumerate(N):
            if i==j:continue
            sign=sum(n[k]*(s[i]*m[k]-s[j]*n[k]) for k in range(3))
            if sign>0:row.append(j)
            elif sign==0:zeros.append([i,j])
        adj.append(row)
    reach={elder}
    while True:
        new=reach|{i for i,row in enumerate(adj) if reach.intersection(row)}
        if new==reach:break
        reach=new
    active=set(a['active']);roots=[i for i,row in enumerate(adj) if not row]
    return dict(source=str(p.resolve()),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),V=a['V'],E=a['E'],F=a['F'],C=a['C'],counts=a['counts'],weak=a['weak'],elder=elder,all_input_supports=len(H),positive_polar_adjacency=adj,exact_zero_chords=zeros,polar_roots=roots,elder_reachable=sorted(reach),elder_reachable_count=len(reach),active_reachable_count=len(reach&active),unreachable_active=sorted(active-reach))

if __name__=='__main__':
    rows=[compute(path) for path in sys.argv[2:]];pathlib.Path(sys.argv[1]).write_text(json.dumps(rows,indent=2)+'\n')
    print([{k:r[k] for k in ['C','counts','polar_roots','elder_reachable_count','active_reachable_count']} for r in rows])
