from graph_algos import Kruskals, Prims
import adjacency_matrix

# we get the adjacency matrix from the file of the same name and the algorithm from it's same name out of Kruskal or Prim
def min_span_tree(A, algo):
    if algo.lower() == 'kruskal':
        res = Kruskals.kruskal(A)
    elif algo.lower() == 'prim':
        res = Prims.prim(A)
    else: res = 'please state valid algorithm'
    return f'you have run {algo}\'s algorithm and it has returned (arcs, weight): {res}'

algo = input("chose an algorithm (current options are 'Kruskal' or 'Prim'): ")
print(min_span_tree(adjacency_matrix.adjacency_matrix, algo))