# material-d32187b109f6

AI research material

<!-- historical-status:start -->
> **Historical AI material.** The title and claims below reflect the AI’s assessment at the time. Claims of proof, certification or completion are not a current verification verdict.
>
> [C622](../C622/README.md) passes the supplied exact checks; C<500 remains open; Minimum’s C≥34 remains a working lower bound requiring a consolidated proof. See [verification status and source gaps](../catalog/coverage.md).
<!-- historical-status:end -->

---

"""Self-contained deterministic replay of the 27 CF82 selective-refinement nominations.
Numerical only: no direct strict H/weak audit and no nonexistence conclusion.
Derived by exact complete-function extraction from the recovered CF82 source pack.
Pin: CPython3.13.5 NumPy2.3.5 SciPy1.17.0 Torch2.10.0+cpu, float64,
one BLAS/OMP/Torch thread. No random numbers or external files.
Run from empty directory: OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python SELECTIVE_REPLAY.py
The pinned full source checkpoint is embedded as literal JSON; inactive input81 retained.
"""
import itertools,json,sys,hashlib
from pathlib import Path
import numpy as np
import scipy,torch
from scipy.spatial import ConvexHull
from scipy.optimize import minimize
torch.set_num_threads(1);torch.set_default_dtype(torch.float64)
DATA='{"points":[[-1.3865717075746062,1.203142883761701,-0.5528460714378198],[0.5427834932831748,-0.2874792181788413,-0.6477865165054382],[0.9367420274774121,0.20231573308712195,-0.30444099243351536],[0.9671125372055763,0.40836412728676863,0.19291711155125876],[0.7736703605165144,0.3660347258673285,0.5652373819936709],[1.0469994573467694,-0.014983241795287669,0.3170683168748958],[1.0229961244596464,-0.27542429835485904,0.29273046305050543],[0.9368350478669333,-0.4701185974981127,0.3783830351205955],[0.8195427835795688,-0.6041844068595167,0.5001777057491521],[0.6779482103256776,-0.6833797509625594,0.6445668761539458],[0.5034945985300523,-0.7447021870836911,0.7731220152720012],[0.3003228726534137,-0.7842744964006372,0.8780432126363832],[0.069605768860905,-0.8135141369377777,0.9405933439963376],[-0.17702944283319993,-0.8315392231861332,0.9510967019749123],[-0.42826589915866503,-0.8348927592226237,0.9062030464430363],[-0.6785180524487701,-0.791722267309843,0.8301217418148304],[-0.9196786032757784,-0.69870473415248,0.7184479669787729],[-1.1426333201174337,-0.5489742173528618,0.5695470900265687],[-1.3309959306763142,-0.32663459612706347,0.3852835709401246],[-1.4580374802803089,-0.02461511159550732,0.16668691787191292],[-1.505428991371038,0.3888681676515076,-0.15043403859052645],[0.043920080192217395,-0.4709798144221673,-0.5507704023632636],[0.8245126706068967,0.01923407152984415,-0.4981853380269574],[0.9734031623306422,0.32294001538154454,-0.1198111634114277],[1.0382906841910982,0.2592850620265991,0.153939777588622],[1.0433284436338923,0.1452389693069436,0.2798043860270974],[1.0472470469489858,-0.15166929005252483,0.2800201983612987],[0.9854078174797661,-0.38472902165062745,0.3211173031705106],[0.8810799245706813,-0.545137603038614,0.4355175334769805],[0.7521543542374555,-0.6496617861274733,0.5703291802501368],[0.5948753050116047,-0.7155147444981274,0.7121930609289774],[0.4058495765864244,-0.7663481883919075,0.8295296065558433],[0.18781049056854796,-0.799814056400865,0.9156981150801776],[-0.05252640055949097,-0.8241930313817073,0.9525868276248382],[-0.300713088258705,-0.8426297647083589,0.9289917185349017],[-0.5550127211559822,-0.814917952827898,0.8762038459298267],[-0.799215741022275,-0.7476961437407903,0.7845735110366705],[-1.0343515135183263,-0.6312056126972645,0.6490233068878949],[-1.2429499186763184,-0.44697218151593154,0.4809321252478351],[-1.4049232159029095,-0.18314552006883067,0.27824649034358034],[-1.4910442177246384,0.19386429438395067,0.025666286602515236],[-1.4104670886554227,0.8490695218150517,-0.48731088460900257],[0.7004438247969643,-0.12535696757385054,-0.5939621108047002],[0.9611128482488404,0.2668857824208942,-0.21226761482459422],[1.0228833963044348,0.3271450089393057,0.10437409108746343],[0.950695459678378,0.28762653963648127,0.4121839686103017],[1.0493775213916148,-0.08414923210857343,0.2979637848299553],[1.005426462036419,-0.3309663261875478,0.30736004306824777],[0.9098813446262797,-0.5087328077582025,0.406869129757564],[0.786452563243289,-0.6290181261297264,0.5342934123474442],[0.6374843948954984,-0.6995948927831159,0.6793954541149192],[0.4553103264341591,-0.7570816777087337,0.8014012029295633],[0.2447811089919373,-0.7922398051053828,0.8984585878026148],[0.008887721522668514,-0.8191824141835025,0.9483180112894904],[-0.23974822240818078,-0.8335727800333149,0.9454456484972561],[-0.4923860287030496,-0.8295877768114531,0.8887987577141213],[-0.7405617794147733,-0.7733417621159385,0.8053413928825464],[-0.978035001470788,-0.6674977539028507,0.6830824971985914],[-1.1947164778361394,-0.499786036960693,0.525979266745604],[-1.3704001638889336,-0.2570955850015811,0.33190846892788217],[-1.4832655175888247,0.07867496849183449,0.08716883118555491],[-1.5168109149478781,0.8415495329034577,-0.2740562848252703],[0.30182883303482844,-0.4116390636924844,-0.6370593419378434],[0.8915126409778519,0.12041231469439549,-0.4018839686262054],[0.9994452242735644,0.36392287032755155,-0.02166530890835178],[1.043796736498868,0.20311902588925593,0.21628891735643915],[1.049002182372587,0.06395060807578722,0.294404890284373],[1.036423397474488,-0.21478507779082662,0.2875956430416435],[0.9621420238976607,-0.4282546339089779,0.35035522111307293],[0.8510506227580079,-0.5763337725069101,0.4671819860771044],[0.7162504467719766,-0.6665053912500599,0.6083543860403591],[0.5503723469208428,-0.7294980735268133,0.7444489726966241],[0.3530165509460098,-0.7797194393165903,0.8516066689235873],[0.12922270281571044,-0.8069605273844734,0.9297959353532058],[-0.11461018000699882,-0.8282696285280914,0.9535868948135788],[-0.36444468625272664,-0.8415084109717812,0.917301822537433],[-0.6172884080397173,-0.8062678716415606,0.8526171258578794],[-0.8603475947094106,-0.7259890319037118,0.7513807035421681],[-1.0896702572497123,-0.5924363389386024,0.6101769009749308],[-1.288829908657273,-0.38930188175169883,0.43243536433596774],[-1.4346425653048342,-0.1062390924737907,0.2236441468864222],[-1.4937576958601726,0.29947930880193313,-0.05055694744911774],[-1.4089393050751717,1.0232217469702432,-0.5431397322758326]]}'
assert len(DATA.encode())==5053 and hashlib.sha256(DATA.encode()).hexdigest()=='ff07c078fdfbcb672dadb156dc59cc8cfe6078130645c34758f70c4f98afd4b2'
def hull_data(Y):
    H = ConvexHull(Y)
    T = H.simplices.copy()
    a, b, c = (Y[T[:, 0]], Y[T[:, 1]], Y[T[:, 2]])
    flip = np.einsum('ij,ij->i', np.cross(b - a, c - a), H.equations[:, :3]) < 0
    T[flip] = T[flip][:, [0, 2, 1]]
    anchor = Y[H.vertices].mean(0)
    a, b, c = (Y[T[:, 0]], Y[T[:, 1]], Y[T[:, 2]])
    v = np.einsum('ij,ij->i', a - anchor, np.cross(b - anchor, c - anchor)) / 6
    V = v.sum()
    g = (v[:, None] * (a + b + c + anchor)).sum(0) / (4 * V)
    groups = {}
    labels = []
    for eq in H.equations:
        key = tuple(np.round(eq, 10))
        labels.append(groups.setdefault(key, len(groups)))
    eq = np.array(list(groups))
    faces = [set() for _ in eq]
    own = {}
    for f, tri in zip(labels, T):
        faces[f].update((int(i) for i in tri))
        for i, j in itertools.combinations(tri, 2):
            own.setdefault(tuple(sorted((int(i), int(j)))), set()).add(f)
    own = {e: sorted(fs) for e, fs in own.items() if len(fs) > 1}
    assert all((len(fs) == 2 for fs in own.values()))
    ids = H.vertices
    lookup = {int(i): k for k, i in enumerate(ids)}
    E = np.array([[lookup[i], lookup[j]] for i, j in own], dtype=int)
    QE = np.array(list(own.values()), dtype=int)
    eq = np.array([H.equations[labels.index(i)] for i in range(len(groups))])
    Q = eq[:, :3] / (-eq[:, 3] - eq[:, :3] @ g)[:, None]
    return dict(Y=Y, ids=ids, T=T, edges=E, qedges=QE, X=Y[ids] - g, Q=Q, V=float(V), g=g, faces=[sorted(f) for f in faces], equations=eq)

def roots(X, edges):
    adj = [[] for _ in X]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    score = np.array([max(((X[j] - X[i]) @ X[i] / (np.linalg.norm(X[i]) * np.linalg.norm(X[j] - X[i])) for j in ns)) for i, ns in enumerate(adj)])
    return (np.where(score < -1e-10)[0], score)

def graph_bars(X, edges):
    R = (X * X).sum(1)
    d = X[edges[:, 1]] - X[edges[:, 0]]
    t = np.clip(-np.einsum('ij,ij->i', X[edges[:, 0]], d) / (d * d).sum(1), 0, 1)
    h = ((X[edges[:, 0]] + t[:, None] * d) ** 2).sum(1)
    pa = list(range(len(X)))
    out = []

    def find(i):
        while pa[i] != i:
            pa[i] = pa[pa[i]]
            i = pa[i]
        return i
    for k in sorted(range(len(h)), key=lambda k: (h[k], *edges[k]), reverse=True):
        a, b = map(find, edges[k])
        if a == b:
            continue
        if (R[a], -a) < (R[b], -b):
            a, b = (b, a)
        if R[b] - h[k] > 1e-12 * max(R):
            out.append(dict(peak=int(b), elder=int(a), edge=edges[k].tolist(), birth=float(R[b]), death=float(h[k]), depth=float(R[b] - h[k])))
        pa[b] = a
    return out

def report(Y, full=True):
    ch = hull_data(np.asarray(Y))
    pr, ps = roots(ch['X'], ch['edges'])
    qr, qs = roots(ch['Q'], ch['qedges'])
    V = ch['V']
    g = dict(V=len(ch['X']), E=len(ch['edges']), F=len(ch['Q']), volume=V, centroid=ch['g'].tolist(), S=len(qr), U=len(pr), unstable_inputs=ch['ids'][pr].tolist(), stable_faces=[ch['faces'][i] for i in qr], physical_guard=float(np.min(np.delete(ps, np.argmax((ch['X'] ** 2).sum(1))))), polar_guard=float(np.min(np.delete(qs, np.argmax((ch['Q'] ** 2).sum(1))))), edge_floor=float(np.min(np.linalg.norm(ch['X'][ch['edges'][:, 0]] - ch['X'][ch['edges'][:, 1]], axis=1)) / max(np.linalg.norm(ch['X'], axis=1))))
    if full:
        pb = graph_bars(ch['X'], ch['edges'])
        qb = graph_bars(ch['Q'], ch['qedges'])
        etas = [(b['death'] ** (-0.5) - b['birth'] ** (-0.5)) / 2 for b in qb]
        g.update(Pbars=pb, Qbars=qb, TP=sum((b['depth'] for b in pb)) / V ** (2 / 3), TQ=sum((b['depth'] for b in qb)) * V ** (2 / 3), eta=max(etas, default=0), eta_normalized=max(etas, default=0) / V ** (1 / 3), sum_eta_normalized=sum(etas) / V ** (1 / 3))
    return g
def root_scores(X):
    diff = X[None, :, :] - X[:, None, :]
    lengths = np.linalg.norm(diff, axis=2)
    radii = np.linalg.norm(X, axis=1)
    scores = np.einsum('ij,ikj->ik', X, diff) / (radii[:, None] * np.where(lengths > 0, lengths, 1))
    np.fill_diagonal(scores, -np.inf)
    return np.max(scores, axis=1)

def caps_bars(X, edges):
    r2 = np.einsum('ij,ij->i', X, X)
    pa = list(range(len(X)))

    def find(a):
        while pa[a] != a:
            pa[a] = pa[pa[a]]
            a = pa[a]
        return a
    events = []
    for i, j in edges:
        d = X[j] - X[i]
        dd = d @ d
        if dd <= 1e-28:
            raise ValueError('zero edge')
        t = np.clip(-X[i] @ d / dd, 0.0, 1.0)
        z = X[i] + t * d
        events.append((float(z @ z), int(i), int(j)))
    out = []
    for death, i, j in sorted(events, reverse=True):
        a, b = (find(i), find(j))
        if a == b:
            continue
        if (r2[a], -a) < (r2[b], -b):
            a, b = (b, a)
        delta = float(r2[b] - death)
        if delta > 1e-11 * max(r2):
            out.append(dict(peak=b, elder=a, edge=[i, j], birth=float(r2[b]), death=death, depth=delta))
        pa[b] = a
    return out

def geometry(Y, with_bars=False):
    H = ConvexHull(Y)
    T = H.simplices.copy()
    a, b, c = (Y[T[:, 0]], Y[T[:, 1]], Y[T[:, 2]])
    signs = np.einsum('ij,ij->i', np.cross(b - a, c - a), H.equations[:, :3])
    T[signs < 0] = T[signs < 0][:, [0, 2, 1]]
    anchor = Y[H.vertices].mean(axis=0)
    a, b, c = (Y[T[:, 0]], Y[T[:, 1]], Y[T[:, 2]])
    vol = np.einsum('ij,ij->i', a - anchor, np.cross(b - anchor, c - anchor)) / 6
    V = float(vol.sum())
    g = (vol[:, None] * (a + b + c + anchor)).sum(axis=0) / (4 * V)
    X = Y[H.vertices] - g
    Q = H.equations[:, :3] / (-H.equations[:, 3] - H.equations[:, :3] @ g)[:, None]
    dQ = Q[:, None, :] - Q[None, :, :]
    d2 = np.einsum('ijk,ijk->ij', dQ, dQ)
    np.fill_diagonal(d2, np.inf)
    if d2.min() < 1e-18:
        raise ValueError('numerically coplanar triangulation')
    vi = {int(i): k for k, i in enumerate(H.vertices)}
    owners = {}
    for f, tri in enumerate(T):
        for i, j in itertools.combinations(tri, 2):
            owners.setdefault(tuple(sorted((int(i), int(j)))), []).append(f)
    if any((len(o) != 2 for o in owners.values())):
        raise ValueError('not a paired triangular hull')
    edges = np.array([[vi[i], vi[j]] for i, j in owners])
    qedges = np.array(list(owners.values()))
    ps, qs = (root_scores(X), root_scores(Q))
    pr = int(np.argmax(np.einsum('ij,ij->i', X, X)))
    qr = int(np.argmax(np.einsum('ij,ij->i', Q, Q)))
    pnon = np.delete(ps, pr)
    qnon = np.delete(qs, qr)
    loss = float(np.minimum(pnon, 0) @ np.minimum(pnon, 0) + np.minimum(qnon, 0) @ np.minimum(qnon, 0))
    result = dict(V=len(X), E=len(edges), F=len(Q), volume=V, centroid=g.tolist(), S=int((qs < -1e-10).sum()), U=int((ps < -1e-10).sum()), loss=loss, min_edge_relative=float(np.min(np.linalg.norm(X[edges[:, 1]] - X[edges[:, 0]], axis=1)) / np.linalg.norm(X, axis=1).max()), physical_nonroot_min=float(pnon.min()), polar_nonroot_min=float(qnon.min()), active_inputs=H.vertices.tolist(), stable_triangles=T[qs < -1e-10].tolist(), unstable_inputs=H.vertices[ps < -1e-10].tolist())
    if with_bars:
        pb, qb = (caps_bars(X, edges), caps_bars(Q, qedges))
        result.update(Pbars=pb, Qbars=qb, TP=sum((z['depth'] for z in pb)) / V ** (2 / 3), TQ=sum((z['depth'] for z in qb)) * V ** (2 / 3), relative_P=sum((z['depth'] for z in pb)) / np.max(np.sum(X * X, axis=1)), relative_Q=sum((z['depth'] for z in qb)) / np.max(np.sum(Q * Q, axis=1)))
    return result
def chart(Y):
    h = ConvexHull(Y)
    t = h.simplices.copy()
    a, b, c = (Y[t[:, 0]], Y[t[:, 1]], Y[t[:, 2]])
    bad = np.einsum('ij,ij->i', np.cross(b - a, c - a), h.equations[:, :3]) < 0
    t[bad] = t[bad][:, [0, 2, 1]]
    owners = {}
    for f, tri in enumerate(t):
        for i, j in [(tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0])]:
            owners.setdefault(tuple(sorted((int(i), int(j)))), []).append(f)
    assert all((len(v) == 2 for v in owners.values()))
    return (t, h.vertices.copy(), np.array(list(owners)), np.array(list(owners.values())))

def tensors(Y, ch):
    t, ids, edges, qe = ch
    a, b, c = (Y[t[:, 0]], Y[t[:, 1]], Y[t[:, 2]])
    vol = (a * torch.linalg.cross(b, c)).sum(1) / 6
    V = vol.sum()
    g = (vol[:, None] * (a + b + c)).sum(0) / (4 * V)
    X = Y[ids] - g
    n = torch.linalg.cross(b - a, c - a)
    q = n / ((a - g) * n).sum(1)[:, None]
    d = X[None, :, :] - X[:, None, :]
    length = torch.linalg.vector_norm(d, dim=2)
    length = length + torch.eye(len(X))
    w = (X[:, None, :] * d).sum(2) / (torch.linalg.vector_norm(X, dim=1)[:, None] * length) - 10 * torch.eye(len(X))
    return (X, q, V, g, w)
def restoration(trial, guard, maxcor=8):
    start = trial.copy()
    steps = []
    for it in range(maxcor + 1):
        geom = geometry(trial, True)
        if geom['U'] == 1 and geom['physical_nonroot_min'] >= guard:
            return (trial, steps, geom)
        if it == maxcor:
            break
        ch = chart(trial)
        v = torch.tensor(trial, requires_grad=True)
        x, q, V, g, w = tensors(v, ch)
        root = int((x * x).sum(1).argmax())
        sources = np.array([i for i in range(len(x)) if i != root])
        targets = w.detach().numpy().argmax(1)[sources]

        def cons(z):
            return tensors(z, ch)[4][sources, targets]
        vals = cons(v).detach().numpy()
        J = torch.autograd.functional.jacobian(cons, v, vectorize=True).detach().numpy().reshape(len(vals), -1)
        sol = minimize(lambda d: (0.5 * d @ d, d), np.zeros(trial.size), method='SLSQP', jac=True, constraints={'type': 'ineq', 'fun': lambda d: vals + J @ d - (guard + 1e-09), 'jac': lambda d: J}, options={'maxiter': 120, 'ftol': 1e-18})
        step = sol.x.reshape(trial.shape)
        if not sol.success or np.linalg.norm(step) > 0.025:
            return (None, steps, None)
        trial = trial + step
        steps.append(float(np.linalg.norm(step)))
    return (None, steps, None)
root = Path(__file__).resolve().parent
Y = np.array(json.loads(DATA)['points'])
ch = hull_data(Y)
X = ch['X']
pr, _ = roots(X, ch['edges'])
adj = [[] for _ in X]
for i, j in ch['edges']:
    adj[i].append(j)
    adj[j].append(i)
edges = []
for i in range(len(X)):
    if i in pr:
        continue
    j = max(adj[i], key=lambda j: (float(X[i] @ (X[j] - X[i]) / np.linalg.norm(X[j] - X[i])), -j))
    x, y = (X[i], X[j])
    rx, ry = map(np.linalg.norm, [x, y])
    ang = np.arccos(np.clip(x @ y / rx / ry, -1, 1))
    u = x / rx + y / ry
    u /= np.linalg.norm(u)
    arc = np.sqrt(rx * ry) * u
    mid = (x + y) / 2
    score = x @ (y - x) / rx / np.linalg.norm(y - x)
    edges.append(dict(i=int(ch['ids'][i]), j=int(ch['ids'][j]), angle=float(ang), guard=float(score), bulge=float(np.linalg.norm(arc - mid)), arc=arc, mid=mid))
records = []
for mode in ['angle', 'tight', 'bulge']:
    order = sorted(edges, key=lambda e: (-e['angle'] if mode == 'angle' else e['guard'] / e['angle'] if mode == 'tight' else -e['bulge'], e['i']))
    for count in [8, 16, 23]:
        for factor in [0.5, 1.0, 1.5]:
            selected = order[:count]
            P = np.vstack([Y, [ch['g'] + e['mid'] + factor * (e['arc'] - e['mid']) for e in selected]])
            before = report(P)
            try:
                Z, corr, after = restoration(P, 1e-05, maxcor=12)
            except Exception as ex:
                Z = None
                corr = []
                after = {'error': str(ex)}
            r = report(Z) if Z is not None else None
            rec = dict(mode=mode, count=count, factor=factor, edges=[[e['i'], e['j']] for e in selected], before=before, corrections=corr, report=r)
            records.append(rec)
            print('SELECTIVE', mode, count, factor, None if r is None else (r['V'], r['E'], r['S'], r['U'], r['eta_normalized']), flush=True)
            if r is not None:
                (root / f'SELECTIVE_{mode}_{count}_{factor}.json').write_text(json.dumps(dict(points=Z.tolist(), settings=rec), separators=(',', ':')))
            (root / 'SELECTIVE_LEDGER.json').write_text(json.dumps(records, separators=(',', ':')))
print('SELECTIVE_REFINEMENT_SCOUT_DONE', len(records), flush=True)
raw=(root/'SELECTIVE_LEDGER.json').read_bytes()
assert len(raw)==68893 and hashlib.sha256(raw).hexdigest()=='233185aa5e5fa0f39f019272fc2fb49a65ba3949ae313b9e47af8c82a838366d'
print('CF82_SELECTIVE27_LEDGER_BYTE_REPLAY_PASS',len(raw),hashlib.sha256(raw).hexdigest(),flush=True)
