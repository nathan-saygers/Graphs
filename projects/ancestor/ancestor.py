
from util import *


def earliest_ancestor(ancestors, starting_node):
    pass


test_input = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
              (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def build_graph(ancestors):
    anc_graph = Graph()

    for pair in ancestors:
        if pair[0] not in anc_graph.vertices:
            anc_graph.add_vertex(pair[0])
        if pair[1] not in anc_graph.vertices:
            anc_graph.add_vertex(pair[1])

    for edge in ancestors:
        anc_graph.add_edge(edge[0], edge[1])

    return anc_graph


print(build_graph(test_input).vertices)
