"""Lossless exact-proof compression: repeated subtrees and dual basis indices."""
import hashlib,json,sys
from pathlib import Path


def main():
    source=Path(sys.argv[1]).read_bytes();report=json.loads(source)
    assert report['complete'];nodes=[];index={}
    def intern(i):
        row=report['nodes'][i]
        if 'dual'in row:
            item=['L',sorted(j for j,w in row['dual'])]
        else:
            item=['B',row['facet'],[intern(j)for j in row['children']]]
        key=json.dumps(item,separators=(',',':'))
        if key not in index:index[key]=len(nodes);nodes.append(item)
        return index[key]
    roots=[intern(i)for i in report['roots']]
    result=dict(format='dag_row_basis_v1',complete=True,input_sha256=report['input_sha256'],
                coordinate_scale=report['coordinate_scale'],roots=roots,nodes=nodes,
                source_tree_sha256=hashlib.sha256(source).hexdigest())
    data=json.dumps(result,sort_keys=True,separators=(',',':')).encode()
    Path(sys.argv[2]).write_bytes(data)
    print('COMPACT_LOADING_PROOF',len(nodes),len(data),hashlib.sha256(data).hexdigest())


if __name__=='__main__':main()
