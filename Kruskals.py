adjacency_matrix = [
    [0,1,0,4,0,0,0],
    [1,0,2,6,4,0,0],
    [0,2,0,0,5,6,0],
    [4,6,0,0,3,0,4],
    [0,4,5,3,0,8,7],
    [0,0,6,0,8,0,3],
    [0,0,0,4,7,3,0],
]
# this function takes an adjacency matrix and returns a nodes_list, arcs_list, weights_list.
def process_am(A):
    # create nodes list
    nodes_list = []
    components_list = []
    for x in range(1,len(adjacency_matrix[0])+1):
        nodes_list.append(f'a{x}')
        components_list.append({f'a{x}'})
    # here we create the arc and weight lists simultaneously
    arcs_list = []
    weight_list = []
    num_nodes = len(adjacency_matrix[0])
    first_col_num = 0
    for row in range(num_nodes):
        first_col_num += 1
        for col in range(first_col_num,num_nodes):
            arcs_list.append([nodes_list[row], nodes_list[col]])
            weight_list.append(adjacency_matrix[row][col])
    return nodes_list, components_list, arcs_list, weight_list

# takes node and returns component
def find_component(node, components_list):
    for component in components_list:
        if node in component:
            return component
# takes weightlist and arclist and removes all arcs with a zero weight
def non_zero_vals(weight_list, arc_list):
    new_weight_list = []
    new_arc_list = []
    for ind, elem in enumerate(weight_list):
        if elem != 0:
            new_weight_list.append(weight_list[ind])
            new_arc_list.append(arc_list[ind])
    return new_weight_list, new_arc_list

# define a function kruskal which simply takes a single adjacency matrix as it's only argument
def kruskal(A):
    nodes_list, components_list, arcs_list, weight_list = process_am(A)
    T = set()
    n = len(nodes_list)
    weight_list, arcs_list = non_zero_vals(weight_list, arcs_list)
    total_weight = 0
    # we go until one less arc than node
    while len(T) != n-1:
        # find the shortest arc
        i = weight_list.index(min(weight_list))
        uv = arcs_list[i]
        # I write a find function to find the compenents the nodes are in
        u_component = find_component(uv[0], components_list)
        v_component = find_component(uv[1], components_list)
        if u_component != v_component:
            components_list.append(u_component|v_component)
            components_list.remove(u_component)
            components_list.remove(v_component)

            T.add(tuple(uv))
            total_weight += weight_list[i]
        # we want to now delete this arc so that we don't consider it again
        arcs_list.pop(i)
        weight_list.pop(i)

    return T, total_weight
print(kruskal(adjacency_matrix))