import sys
import heapq
INF = int(1e9)


def dijkstra(start):
    """
    1. 시작 노드 최단 테이블 0 설정 & q에 삽입
    2. 방문하지 않은 노드 중 가장 짧은 노드를 선택 > heapq 사용
    3. 해당 노드를 거쳐가는 다른 노드를 계산하여 작은 경우는 갱신 & 큐에 넣기
    4. 2~3 반복
    :param start:
    :return:
    """
    q = []
    # 1. 최단 거리 테이블 초기화
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:   # 이미 방문함
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m = map(int, sys.stdin.readline().split())  # 노드, 간선
start = int(sys.stdin.readline().split()[0])
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)


for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())   # a -> b, c 비용
    graph[a].append((b, c))

dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


'''
[Input Example 1]
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
[Output Example 1]
0
2
3
7
INFINITY
'''