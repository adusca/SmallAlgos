segtree = [0] * 16

# filhos do no x sao 2*x+1 e 2*x+2
#
#         [0, 8)
#   [0, 4)        [4, 8)
#[0, 2) [2, 4) [4, 6) [6, 8)

# Chamada para consultar [a, b): query(a, b, 0, 0, 8)


def query(a, b, node, l, r):
    """
    Retorna a soma de [a, b) intersectado com [l, r),
    onde [l, r) eh o intervalo correspondente ao no node.
    """
    # Se [l, r) estiver contido em [a, b), a resposta eh a soma
    # do intervalo [l, r), que ja temos
    if a <= l and b >= r:
        return segtree[node]

    # Se [l, r) for disjunto de [a, b), a resposta eh a identidade
    if r <= a or l >= b:
        return 0

    mid = (l+r)/2
    return query(a, b, 2*node + 1, l, mid) + \
        query(a, b, 2*node + 2, mid, r)


def update(pos, val, node, l, r):
    """Atualiza a subarvore enraizada em node, de modo que o
    array subjacente satisfaca arr[pos] = val"""
    mid = (l+r)/2
    if mid == l:
        segtree[node] = val
        return
    if pos < mid:
        update(pos, val, 2*node + 1, l, mid)
    else:
        update(pos, val, 2*node + 2, mid, r)
    segtree[node] = segtree[2*node + 1] + segtree[2*node + 2]
