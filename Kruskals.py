from Graph_Operations import process_am
from Graph_Operations import non_zero_vals

# takes node and returns component
def find_component(node, components_list):
    for component in components_list:
        if node in component:
            return component


# define a function kruskal which simply takes a single adjacency matrix as it's only argument
def kruskal(A):
    nodes_list, components_list, arcs_list, weight_list = process_am(A, 'Kruskal')
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
