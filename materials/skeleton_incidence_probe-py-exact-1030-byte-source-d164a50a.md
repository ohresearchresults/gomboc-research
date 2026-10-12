# material-d164a50a0950

AI research material

---

from itertools import product


def main():
    rows = []
    # AC,AD,BC,BD pair facets; ACD,BCD triple facets.
    for ac, ad, bc, bd, ta, tb in product(range(2), repeat=6):
        for cd in range(3):
            if (ac + ta > 1 or ad + ta > 1 or bc + tb > 1
                    or bd + tb > 1 or cd + ta + tb > 2):
                continue
            extra = ac + ad + bc + bd + cd + ta + tb
            s = 3 + extra
            ri = [2 + ac + ad + ta, 2 + bc + bd + tb,
                  1 + ac + bc + cd + ta + tb,
                  1 + ad + bd + cd + ta + tb]
            delta = sum(max(x - 3, 0) for x in ri)
            correction = sum(x - 1 for x in ri if x >= 3)
            one_facet = sum(x == 1 for x in ri)
            edges = 3 * s - 6 - delta
            coarse_bound = 2 * edges - correction + one_facet + 2
            rows.append(coarse_bound)
    assert len(rows) == 65
    assert max(rows) == 18
    print('SKELETON_INCIDENCE_PROBE_OK patterns=65 coarse_bound=18')


if __name__ == '__main__':
    main()
