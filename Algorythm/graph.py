weight = {}
parent = {}
graph = {}
proccessed = []
infinity = float('inf')


def minim_node(weight):
    minim = infinity
    minim_node = None
    for node in weight:
        if weight[node] < minim and node not in proccessed:
            minim_node = node
            minim = weight[node]
    return minim_node


graph['s'] = {}
graph['s']['a'] = 6
graph['s']['b'] = 2
graph['a'] = {}
graph['a']['f'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['f'] = 5
graph['f'] = {}

weight['a'] = 6
weight['b'] = 2
weight['f'] = infinity

parent['a'] = 's'
parent['b'] = 's'
parent['f'] = None

node = minim_node(weight)
while node != None:
    weight1 = weight[node]
    neighbors = graph[node]
    for i in neighbors.keys():
        new_weight = weight1 + neighbors[i]
        if weight[i] > new_weight:
            weight[i] = new_weight
            parent[i] = node
    proccessed.append(node)
    node = minim_node(weight)

print('graph: ', graph)
print('weight: ', weight)
print('parent: ', parent)
