from graph_algos import Kruskals, Prims, Depthfirst
import adjacency_matrix

# we get the adjacency matrix from the file of the same name and the algorithm from it's same name out of Kruskal or Prim
def main(A, algo):
    if algo.lower() == 'kruskal':
        res = Kruskals.kruskal(A)
        return f'you have run {algo}\'s algorithm and it has returned (arcs, weight): {res}'
    elif algo.lower() == 'prim':
        res = Prims.prim(A)
        return f'you have run {algo}\'s algorithm and it has returned (arcs, weight): {res}'
    elif algo.lower() == 'depthfirstsearch':
        tree = Depthfirst.search(A)
        return f'you have run {algo}\'s algorithm and it produces a tree composed of the following nodes: {tree}'
    else: res = 'please state valid algorithm'


inpt = input('please input the algo you want to perform on the graph: ')
print(main(adjacency_matrix.adjacency_matrix, inpt))