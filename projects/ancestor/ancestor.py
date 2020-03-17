from graph import Graph
from util import Queue

# take in a list of ancestors
# create graph with list of ancestors
# start with starting_node and go up as high as possible
# then return highest number

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1), (22, 2), (24, 22)]


def earliest_ancestor(ancestors, starting_node):
    # 1: Create graph
    graph = Graph()
    # takes list and grabs the tuple pairs
    for item in ancestors:
        for num in item:
            # takes all the numbers and adds them to the vertices (a set)
            if num not in graph.vertices:
                graph.add_vertex(num)
        v1 = item[0]
        v2 = item[1]
        # Adds edges to the vertices
        graph.add_edge(v1, v2)

    # 2: Get paths of node
    path_list = []
    for num in graph.vertices:
        # gets a path to starting_node from every vertex
        if graph.bfs(num, starting_node) is not None and len(graph.bfs(num, starting_node)) > 1:
            # adds paths if it is a path greater then 1
            path_list.append(graph.bfs(num, starting_node))

    if len(path_list) == 0:
        return -1

    # Gets the biggest path and returns the top number
    return max(path_list, key=len)[0]


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(earliest_ancestor(test_ancestors, 6))

