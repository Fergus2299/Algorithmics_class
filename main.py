import Kruskals
import Prims
import adjacency_matrix

# we get the adjacency matrix from the file of the same name and the algorithm from it's same name out of Kruskal or Prim
def min_span_tree(A, algo):
    if algo == 'Kruskal':
        res = Kruskals.kruskal(A)
    elif algo == 'Prim':
        res = Prims.prim(A)
    else: res = 'please state valid algorithm'
    return res

algo = input('chose an algorithm: ')
print(min_span_tree(adjacency_matrix.adjacency_matrix, algo))