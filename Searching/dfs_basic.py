"""
 dfs(스택) - '1' 노드 방문 & 독립된 노드 수 확인
"""
n, m = 4, 3  # 세로, 가로
graph = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1],
    [1, 1, 0]
    ]

# 네 방향으로 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]
count = 0        # 독립된 노드 수

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            count += 1
            stack = list()
            stack.append((i, j))
            visited[i][j] = True
            while stack:
                x, y = stack.pop()
                print(x, y)
                for a in range(4):  # 4개 방향 위치 확인
                    # 인접한 위치 구하기 (현재위치에서 상하좌우)
                    nx = x + dx[a]
                    ny = y + dy[a]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 범위에서 벗어남
                        continue
                    if graph[nx][ny] != 1 or visited[nx][ny]:
                        continue
                    visited[nx][ny] = True  # 방문 표시
                    stack.append((nx, ny))
print(count)