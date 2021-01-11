"""
시작 (0,0) 위치에서 (n, m) 출구까지 이동한 거리
"""

import sys
from collections import deque
n, m = 5, 6
graph = [[1, 0, 1, 0, 1, 0],
         [1, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1]]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = 0
queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    result += 1
    for a in range(4):
        nx = dx[a] + x
        ny = dy[a] + y
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:    # 처음 방문하는 경우
            queue.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1

print(graph[n - 1][m - 1])   # 이동한 거리