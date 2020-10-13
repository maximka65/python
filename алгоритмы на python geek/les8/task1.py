# 1. На улице встретились N друзей.
# Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?

from collections import deque

n = int(input('сколько друзей: '))

graph = []
graph.append([1]*n)
for i in range(n-1):
    graph.append([1] + [0] * (n - 1))

#print(*graph, sep='\n')


def bfs(grp, start, finish):
    parent = [None for i in range(len(grp))]
    is_visited = [False for i in range(len(grp))]

    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:
        current = deq.pop()
        if current == finish:
            return parent
            break
        for i, vertex in enumerate(grp[current]):
            if vertex == 1 and not is_visited[i]:
                is_visited[i] = True
                parent[i] = current
                deq.appendleft(i)
    else:
        return 'невозможно!'


print(len(bfs(graph, 0, n-1)) - 1)
