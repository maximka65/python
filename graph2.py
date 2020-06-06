graph = {}
weight = {}
parent = {}
infinity = float('inf')
proccessed = []


def minimal_weight_node(weight):
    minimal_node_w = infinity
    minimal_node = None
    for node in weight:
        if weight[node] < minimal_node_w and node not in proccessed:
            minimal_node_w = weight[node]
            minimal_node = node
    return minimal_node


graph['s'] = {'a': 5, 'd': 2}
graph['a'] = {'b': 4, 'c': 2}
graph['d'] = {'a': 8, 'c': 7}
graph['b'] = {'f': 3, 'c': 6}
graph['c'] = {'f': 1}
graph['f'] = {}

weight = {'a': 5, 'd': 2, 'b': infinity, 'c': infinity, 'f': infinity}

parent = {'a': 's', 'd': 's'}


node = minimal_weight_node(weight)
while node != None:
    w = weight[node]
    neighbors = graph[node]
    for i in neighbors.keys():
        new_weight = w + neighbors[i]
        if new_weight < weight[i]:
            weight[i] = new_weight
            parent[i] = node
    proccessed.append(node)
    node = minimal_weight_node(weight)

print('graph: ', graph)
print('weight: ', weight)
print('parent: ', parent)

print('Minimal weigth to finish is: ', weight['f'])
