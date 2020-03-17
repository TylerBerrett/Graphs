from graph import Graph
from util import Queue

# take in a list of ancestors
# create graph with list of ancestors
# start with starting_node and go up as high as possible

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for item in ancestors:
        for num in item:
            if num not in graph.vertices:
                graph.add_vertex(num)
        v1 = item[0]
        v2 = item[1]
        graph.add_edge(v1, v2)

    path_list = []
    for num in graph.vertices:
        if graph.bfs(num, starting_node) is not None and len(graph.bfs(num, starting_node)) > 1:
            path_list.append(graph.bfs(num, starting_node))

    if len(path_list) == 0:
        return -1

    return max(path_list, key=len)[0]


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
earliest_ancestor(test_ancestors, 5)

