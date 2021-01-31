import sys
INF = int(1e9)

n = int(sys.stdin.readline().split()[0])   # 노드 수
m = int(sys.stdin.readline().split()[0])   # 간선 수

# 1. 2차원 배열 - 모든 값을 초기화: 모든 거리 무한, 자신으로 가는 거리 0
graph = [[INF] * (n + 1) for _ in range(n + 1)]    # 모든 최단 거리를 저장
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

# 2. 다이나믹 프로그래밍
for k in range(n + 1):
    for a in range(n + 1):
        for b in range(n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("inf")
        else:
            print(graph[a][b], end=" ")
    print()

"""
[Input Example 1]
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

[Output Example 1]
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0 
"""