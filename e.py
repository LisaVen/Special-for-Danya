__author__ = 'student'


def reading():
    n, m = map(int, input().split())
    graph = [[0]*n for i in range(n)]
    for j in range(m):
        a, b = [int(x) for x in input().split()]
        c = min(a, b)
        d = max(a, b)
        graph[c][d] = 1
        graph[d][c] = 1
    return graph


def read_as_matrix():
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]
    return a

def mvr():
    used = set()
    a = read_as_matrix()
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 1 and j not in used:
                print(i, ' ', j)
            used.add(i)

g = mvr()
print(g)
