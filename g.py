__author__ = 'student'

n, m = [int(x) for x in input().split()]
def reading(n, m):
    graph = [[] for i in range(n)]
    for j in range(m):
        a, b = [int(x) for x in input().split()]
        c = min(a, b)
        d = max(a, b)
        graph[c].append(d)
        graph[d].append(c)
    return graph

def dfs(start, n, used = None):
    if used == None:
        used = set()
    used.add(start)
    for i in n[start]:
        if i not in used:
            dfs(i, n, used)

A = reading(n, m)
dfs(0, A)
