import sys
from collections import deque

# 네 방향으로 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = 4, 3  # 세로, 가로
graph = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1],
    [1, 1, 0]
    ]

visited = [[False] * m for _ in range(n)]   # 방문 유무
count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            count += 1
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            print(x, y)
            for a in range(4):  # 인접한 위치 구하기 (현재위치에서 상하좌우)
                nx = x + dx[a]
                ny = y + dy[a]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 범위에서 벗어남
                    continue
                if graph[nx][ny] != 1 or visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                queue.append((nx, ny))
print(count)