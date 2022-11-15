
def process_am(A):
    # create nodes list
    nodes_list = []
    for x in range(0, len(A[0])):
        nodes_list.append(f'a{x}')

    # here we create the arc and weight lists simultaneously
    arcs_list = []
    weight_list = []
    num_nodes = len(A[0])
    first_col_num = 0
    for row in range(num_nodes):
        first_col_num += 1
        for col in range(first_col_num,num_nodes):
            arcs_list.append([nodes_list[row], nodes_list[col]])
            weight_list.append(A[row][col])
    return nodes_list, arcs_list, weight_list

def non_zero_vals(weight_list, arc_list):
    new_weight_list = []
    new_arc_list = []
    for ind, elem in enumerate(weight_list):
        if elem != 0:
            new_weight_list.append(weight_list[ind])
            new_arc_list.append(arc_list[ind])
    return new_weight_list, new_arc_list

def search(A):
    # take the adjacency matrix and process it:
    Nodes, Arcs, Weights = process_am(A)
    Weights, Arcs =  non_zero_vals(Weights, Arcs)
    Visited = []
    for i in Nodes:
        # all nodes start out as not visited
        Visited.append(False)
    spanning_tree = []
    for node_num in range(len(Nodes)):
        if Visited[node_num] != True:
            spanning_tree = DepthFirstSearch(node_num, Nodes, Arcs, Visited, spanning_tree)
    return spanning_tree
def DepthFirstSearch(node_num, Nodes, Arcs, Visited, spanning_tree):
    Visited[node_num] = True
    # find adjacent nodes
    adj_list = []
    for arc in Arcs:
        if f'a{node_num}' in arc:
            # TODO: see if there's a better way than this
            arc = arc[:]
            arc_copy = arc[:]
            arc.remove('a'+str(node_num))
            i = Nodes.index(arc[0])
            if Visited[i] != True:
                spanning_tree.append(arc_copy)
                spanning_tree = DepthFirstSearch(i, Nodes, Arcs, Visited, spanning_tree)
    return spanning_tree
if __name__ == '__main__':
    """this matrix is meant to represent a non-directed graph since Kruskal and Prim's algos aren't suitable for directed graphs"""
    adjacency_matrix = [
        [0, 1, 0, 4, 0, 0, 0],
        [1, 0, 2, 6, 4, 0, 0],
        [0, 2, 0, 0, 5, 6, 0],
        [4, 6, 0, 0, 3, 0, 4],
        [0, 4, 5, 3, 0, 8, 7],
        [0, 0, 6, 0, 8, 0, 3],
        [0, 0, 0, 4, 7, 3, 0],
    ]
    print(search(adjacency_matrix))
