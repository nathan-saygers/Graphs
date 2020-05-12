
from util import *


def build_graph(ancestors):
    anc_graph = Graph()

    for pair in ancestors:
        if pair[0] not in anc_graph.vertices:
            anc_graph.add_vertex(pair[0])
        if pair[1] not in anc_graph.vertices:
            anc_graph.add_vertex(pair[1])

    for edge in ancestors:
        anc_graph.add_edge(edge[1], edge[0])

    return anc_graph


def earliest_ancestor(ancestors, starting_node):
    ancestor_graph = build_graph(ancestors)

    if ancestor_graph.get_parents(starting_node) == set():
        return -1

    result = ancestor_graph.dft(starting_node)

    if ancestor_graph.get_parents(result[-2]) == set():
        return result[-2]

    return result[-1]


print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                         (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 2))
