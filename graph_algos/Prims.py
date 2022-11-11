
from graph_algos.Graph_Operations import process_am
from graph_algos.Graph_Operations import non_zero_vals
from graph_algos.Graph_Operations import simultaneous_sort


def find_mincost_prim(nodes_list, arcs_list, weight_list, b):
    # I sort the list of arcs based off their weight, returning weight will allow us to return total weight later
    weight_list, arcs_list = simultaneous_sort(weight_list, arcs_list)
    for arc in arcs_list:
        u = arc[1]
        v = arc[0]
        if v not in b and u in b:
            b.add(v)
            return arc, b
        elif u not in b and v in b:
            b.add(u)
            return arc, b

def prim(A):
    # perform imported functions
    nodes_list, arcs_list, weight_list = process_am(A, 'Prims')
    weight_list, arcs_list = non_zero_vals(weight_list, arcs_list)
    nodes_list = set(nodes_list)
    # T will be the answer and B will start with a random node
    T = set()
    b = {'a1'}
    while b != nodes_list:
        arc, b = find_mincost_prim(nodes_list, arcs_list, weight_list, b)
        T.add(tuple(arc))
    return T
