# material-896981ab8ded

AI research material

---

"""Exact central-root forced-facet certificates. Python 3.8+, stdlib only.
Run: python -S central_root.py (without -O). All rational inputs are literal.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations

if not __debug__:
    raise RuntimeError('Run without -O')

EPS = F(13127,5250000)
SPECS = (
    ('34',(3,4),F(73,128),
     (F(135,128),F(15,8),F(10,3),F(21,8)),
     (F(135,128),F(25,24),F(2,3),F(21,512),F(5,10752))),
    ('35',(3,5),F(5,8),
     (F(28,25),F(28,15),F(28,9),F(5,2),F(5,2)),
     (F(28,25),F(49,45),F(8,9),F(95,128),F(15,38),F(7,600))),
    ('45',(4,5),F(3,4),
     (F(271377,250000),F(3933,2500),F(57,25),F(76,23),F(21,10)),
     (F(271377,250000),F(627,625),F(1083,1100),
      F(844,1587),F(9093,337600),EPS)),
)
DEPTH = {1:F(0),2:F(1,8),3:F(1,4),4:F(7,20),5:F(27,64)}
FACETS = (
    (0,1,2,6,7),(0,7,8),(0,1,9,8),(1,2,3,9),
    (9,3,4),(8,9,4,5),(7,6,5,8),(2,6,5,3),(3,4,5),
)
ROWS = (
    (0,1,2),(0,1,6),(0,2,3),(0,3,7),(0,6,7),
    (1,2,5,6),(2,3,4,5),(3,4,7,8),(4,5,8),(5,6,7,8),
)
PATH = (0,2,3,7,8,9,4,1,5,6)
DUAL_PATH = (6,5,4,3,2,1,0,7,8)


def ldl(a):
    n = len(a)
    assert all(len(row) == n for row in a)
    assert all(a[i][j] == a[j][i] for i in range(n) for j in range(n))
    lower = [[F(i == j) for j in range(n)] for i in range(n)]
    diagonal = []
    for j in range(n):
        pivot = a[j][j] - sum((lower[j][k]**2*diagonal[k]
                               for k in range(j)),F(0))
        assert pivot > 0
        diagonal.append(pivot)
        for i in range(j+1,n):
            lower[i][j] = (a[i][j] - sum(
                (lower[i][k]*lower[j][k]*diagonal[k] for k in range(j)),
                F(0)))/pivot
    assert all(a[i][j] == sum(
        (lower[i][k]*diagonal[k]*lower[j][k] for k in range(n)),F(0))
        for i in range(n) for j in range(n))
    return tuple(diagonal)


def verify_pairs():
    bounds = {}
    for name,terms,bound,multipliers,expected in SPECS:
        n = len(multipliers)+1
        q = [[F(0) for _ in range(n)] for _ in range(n)]
        q[0][0] = bound
        for j in terms:
            q[0][j] += F(1,2)
            q[j][0] += F(1,2)
        for i,multiplier in enumerate(multipliers,1):
            assert multiplier > 0
            q[i][i] += multiplier
            q[i][i-1] -= multiplier/2
            q[i-1][i] -= multiplier/2
        order = tuple(range(1,n))+(0,)
        diagonal = ldl([[q[i][j] for j in order] for i in order])
        assert diagonal == expected
        bounds[name] = bound-diagonal[-1]
    assert bounds == {'34':F(6127,10752),'35':F(46,75),'45':F(3,4)-EPS}
    return bounds


def exception(root):
    assert root in (4,5)
    direction = 1 if root == 4 else -1
    return frozenset((root-4*direction,root+4*direction,root+5*direction))


def margin(root,triangle,bounds):
    tri = frozenset(triangle)
    assert len(tri) == 3 and root not in tri
    assert tri <= set(range(10))
    if tri == exception(root):
        return None,'exception'
    bound = sum((DEPTH[abs(v-root)] for v in tri),F(0))
    if bound < 1:
        gap,kind = 1-bound,'depth'
    else:
        direction = 1 if root == 4 else -1
        a3,a4 = root-3*direction,root-4*direction
        x3,x4,x5 = (root+d*direction for d in (3,4,5))
        assert sorted(abs(v-root) for v in tri) == [3,4,5]
        assert x5 in tri
        if x4 in tri:
            gap,kind = 1-bounds['45']-DEPTH[3],'pair45'
        elif {a3,a4} <= tri:
            gap,kind = 1-bounds['34']-DEPTH[5],'pair34'
        elif {a4,x3} <= tri:
            gap,kind = 1-bounds['35']-DEPTH[4],'pair35'
        else:
            raise AssertionError('Missing triangle certificate')
    assert gap >= EPS > 0
    return gap,kind


def fan(face,anchor):
    k = face.index(anchor)
    cycle = face[k:]+face[:k]
    return [(cycle[0],cycle[j],cycle[j+1]) for j in range(1,len(cycle)-1)]
