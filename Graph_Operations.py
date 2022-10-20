
def process_am(A, setting):
    if setting == 'Kruskal' or setting == 'Kruskals':
        # create nodes list
        nodes_list = []
        components_list = []
        for x in range(1,len(A[0])+1):
            nodes_list.append(f'a{x}')
            components_list.append({f'a{x}'})

    elif setting == 'Prim' or setting == 'Prims':
        nodes_list = []
        for x in range(1, len(A[0]) + 1):
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
    if setting == 'Kruskal' or setting == 'Kruskals':
        return nodes_list, components_list, arcs_list, weight_list
    else: return nodes_list, arcs_list, weight_list



def non_zero_vals(weight_list, arc_list):
    new_weight_list = []
    new_arc_list = []
    for ind, elem in enumerate(weight_list):
        if elem != 0:
            new_weight_list.append(weight_list[ind])
            new_arc_list.append(arc_list[ind])
    return new_weight_list, new_arc_list

# this will be insertion sort but will sort two simultaneously based on a's values
def simultaneous_sort(a, b):
    new_a = []
    new_b = []
    for ind, elem in enumerate(a):
        i = len(new_a) - 1
        while i >= 0 and new_a[i] > elem:
            i -= 1
        new_a.insert(i + 1, elem)
        new_b.insert(i + 1, b[ind])
    return new_a, new_b
