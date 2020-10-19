"""
 dfs(재귀) - '1' 노드 방문 & 독립된 노드 수 확인
"""
n, m = 4, 3  # 세로, 가로
graph = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1],
    [1, 1, 0]
    ]

visited = [[False] * m for _ in range(n)]   # 방문 유무

def dfs(x, y):
    """
    dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
    :return: 처음 방문하고 범위에 맞는 노드인지 유무
    """
    if x < 0 or x >= n or y < 0 or y >= m or graph[x][y] != 1 or visited[x][y]:
        return False
    graph[x][y] = 0  # 방문 표시
    print(x, y)
    dfs(x - 1, y)  # 북
    dfs(x + 1, y)  # 남
    dfs(x, y + 1)  # 동
    dfs(x, y - 1)  # 서
    return True

count = 0   # 독립된 노드 수
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1
print(count)