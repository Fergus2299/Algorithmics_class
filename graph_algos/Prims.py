from graph_algos.Graph_Operations import process_am
from graph_algos.Graph_Operations import non_zero_vals
from graph_algos.Graph_Operations import simultaneous_sort

def find_mincost_prim(nodes_list, arcs_list, weight_list, b):
    # I sort the list of arcs based off their weight, returning weight will allow us to return total weight later
    weight_list, arcs_list = simultaneous_sort(weight_list, arcs_list)
    # look through the sorted list of arcs in weight order
    # if there's an arc where one of the nodes isn't in b but the other is then we can
    # add this arc to the solution
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
    # we want to throw out the arcs which have a zero val since this notation means the arcs aren't connected in this case.
    weight_list, arcs_list = non_zero_vals(weight_list, arcs_list)
    nodes_list = set(nodes_list)
    # T will be the answer and B will start with a random node
    T = set()
    # we'd usually pick a random node but for now I'm starting with a1 each time
    # TODO: make node selection random
    b = {'a1'}
    # we add arcs to the tree until b contains all the nodes
    while b != nodes_list:
        arc, b = find_mincost_prim(nodes_list, arcs_list, weight_list, b)
        T.add(tuple(arc))
    return T
