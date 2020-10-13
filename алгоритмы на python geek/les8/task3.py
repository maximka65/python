# 3. Написать программу, которая обходит не взвешенный ориентированный
# граф без петель,
#  в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).


def dfs(graph, start, visited=None):
    graph2 = {}
    for i in range(len(graph)):
        graph2[i] = set(graph[i])
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    set2 = graph2[start] - visited
    for i in set2:
        dfs(graph2, i, visited)
        return visited


def graph_generator(n):
    graph = []
    for i in range(n):
        print(i)
        graph.append(
            input('с какими вершинами связана вершина, вводить через пробел ').split())
    for i in range(n):
        for j in range(len(graph[i])):
            graph[i][j] = int(graph[i][j])
    return graph


n = int(input('сколько вершин в вашем графе: '))
print(dfs(graph_generator(n), 0))
