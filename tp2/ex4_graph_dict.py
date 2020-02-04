def arc_to_adj(l_arcs):
    """Create dictionary-formed (adjacent) graph from a list"""
    gr = {}
    for orig, extr in l_arcs:
        if orig in gr:
            gr[orig].append(extr)
        else:
            gr[orig] = [extr]
        if extr not in gr:
            gr[extr] = []
    return gr


def nodes(gr):
    """Return the set of the nodes"""
    return set(gr.keys())


def successors(gr, n):
    """Return the successors of node n"""
    return set(gr[n])


def predecessors(gr, n):
    """Return the predecessors of node n"""
    return set([orig for orig in gr if n in gr[orig]])


def wall(gr):
    """Return the sinks of a graph"""
    return set([orig for orig in gr if gr[orig] == []])


def sources(gr):
    """Return the sources of a graph"""

    s = set(gr.keys())
    for orig in gr:
        for extr in gr[orig]:
            if extr in s:
                s.remove(extr)
    return s


if __name__ == '__main__':
    l_arcs = [('a', 'b'), ('b', 'a'), ('c', 'a'), ('c', 'd'),
              ('b', 'c'), ('b', 'd'), ('b', 'e'), ('d', 'e') ]
    dict_adj = arc_to_adj(l_arcs)
    print(1, nodes(l_adj) == set(['a', 'b', 'c', 'd', 'e']))
    print(2, predecessor(l_adj, 'e') == set(['b', 'd']))
    print(3, successors(l_adj, 'b') == set(['a', 'c', 'd', 'e']))
    print(4, sinks(l_adj) == set(['e']))
    print(5, sources(l_adj) == set([]))
    l_arcs = [ ('a', 'b'), ('a', 'c'), ('d', 'e'), ('f', 'e') ]
    l_adj = arc_to_adj(l_arcs)
    print(6, nodes(l_adj) == set(['a', 'b', 'c', 'd', 'e', 'f']))
    print(7, predecessor(l_adj, 'e') == set(['d', 'f']))
    print(8, successors(l_adj, 'a') == set(['b', 'c']))
    print(9, sinks(l_adj) == set(['b', 'c', 'e']))
    print(10, sources(l_adj) == set(['a', 'd', 'f']))
