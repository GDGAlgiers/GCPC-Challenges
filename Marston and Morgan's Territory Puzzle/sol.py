from collections import defaultdict

def dfs(src, par):
    global isVisited, graph, isValid, even, odd
    
    if isVisited[par] & 1:
        isVisited[src] = 2
        odd.append(src)
    else:
        isVisited[src] = 1
        even.append(src)

    for it in graph[src]:
        if not isVisited[it]:
            dfs(it, src)
        elif isVisited[it] & 1 == isVisited[src] & 1:
            isValid = False

def solve():
    global n, m, graph, isVisited, isValid, even, odd
    
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    isVisited = [0] * (n + 1)
    for i in range(1, n + 1):
        if not isVisited[i] and graph[i]:
            dfs(i, i)

    if not isValid:
        print(-1)
        return

    print(len(odd))
    print(*odd)
    print(len(even))
    print(*even)

if __name__ == "__main__":
    tt = 1
    while tt > 0:
        n, m = 0, 0
        graph = defaultdict(list)
        isVisited, even, odd = [], [], []
        isValid = True
        solve()
        print()
        tt -= 1
