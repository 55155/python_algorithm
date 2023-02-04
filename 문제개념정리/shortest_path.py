# 최단 경로 알고리즘
# 말그래도 가장 짧은 경로를 찾는 알고리즘
# 다양한 종류가 있는데, 상황에 맞는 효율적인 알고리즘이 이미 정립되어 있다.

# 한지점에서 다른 특정 지점까지의 최단 경로를 구해야 하는 경우, 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야하는 경우등의 다양한 사례가 존재한다. 
# 이런 사례에 맞는 알고리즘을 알고 있다면 문제를 좀 더 쉽게 풀 수 있다.

# 실제 코딩 테스트에서는 최단 경로를 모두 출력하는 문제보다는 단순히 최단 거리를 출력하도록 요구하는 문제가 많이 출제된다.

# 다익스트라 최단 경로 알고리즘, 플로이드 워셜, 벨만 포드

# 다익스트라 최단 경로 알고리즘과 플로이드 워셜 알고리즘은 그리디 알고리즘과 다이나믹 프로그래밍의 결합 
# 음의 간선이 없으므로 효율적일 수 있음.

# 가장 비용이 적은 노드를 선택해서 임의의 과정을 반복한다.

# 1. 추출발 노드를 설정한다.
# 2. 최단 거리 테이블을 초기화한다.
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
# 5. 3번 ~ 4번을 반복한다.

# 다익스트라 알고리즘 
# 1. 가보지 않은 노드들까지의 간선의 거리를 int(1e9)로 초기화 해놓는다. 
# 1-1 출발 노드를 선정한다. ex) 출발 노드 1번
# 2. 모두 방문하여, 간선이 없을 경우 그대로, 간선이 있을 경우 해당 비용을 int(1e9)에서 간선의 길이로 바꾼다. ex) 1 -> 2 간선의 길이 1이라면, 
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선정한다. 같다면 일반적으로 더 작은 번호의 노드를 선택한다. ex) 1번 노드와 4번 노드가 가장 가깝다면 4번노드 먼저 방문
# 4. 해당 노드에서 다른 노드로 갈 수 있는 더 단거리가 생기면 해당 비용으로 초기화한다.
# 5. 

# 핵심 : 한단계당 하나의 노드에 대한 최단 거리를 확실하게 구한다. 이미 지나간 노드에 대한 초기화는 다시 이루어지지 않기 떄문이다.

# 쉬운 다익스트라 구현 
# 노드의 번호가 index
'''
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(input().split()) # 노드의 개수

start = int(input())

graph = [[] for i in range(n+1)]

visited = [False] * (n + 1)
distance = [INF] * (n + 1) # 처음 distance를 모두 무한으로 정의 : 다익스트라 1

for _ in range(m):
    a,b,c = map(int, input().split())

    graph[a].append((b,c))

def get_smallest_node(): # 방문하지 않은 노드중 가장 최단 거리가 짧은 노드의 번호를 반환
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]: # 만약 distance[i]
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1] # 입력양식이 graph[Node].append((도착지, cost))
        # distance[도착지] = 비용
    for i in range(n-1): # n 은 노드의 개수
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]: # j = graph[now]의 
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost # 경유값으로 바꿔줌

dijkstra(start)

for i in range(1, n+1):
    if distance == INF:
        print('INFINITY')
    else:
        print(distance[i])

'''
# 개선된 방법의 다익스트라 알고리즘

# 단지 최단 거리가 가장 짧은 노드를 선택하는 과정이 좋다

'''
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for i in range(n):
    _,b,c = map(int, input().split())
    graph[i].append((b,c))

def dijkstra(start):
    q = []    
    heapq.heappush(q,(0, start)) # 객체 선언이 아닌 이런식으로 만든다.
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 더 작은 것으로 교체 되었기 때문에 진행하지 않아도 되는 프로세스
            continue
        for i in graph[now]: # 1 2 3 : 1번노드에서 2번노드로 이동할 때 
            cost = dist + i[1] # dist는 현재 노드까지의 거리 + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost # min(1-2 직진, 경유해서 가는 길이 더 빠른지)
                heapq.heappush(q, (cost, i[0]))

q = []
heapq.heappush(q, (0, start)) # 1 2 3 
distance[start] = 0

while q:
    dist, now = heapq.heappop()# 현재 비용, 현재노드
    if distance[now] < dist: # 의미가 없는 정보
        continue
    for i in graph[now]:
        cost = dist + i[1] # (2,2), (3,5), (4,1)
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
'''
# 플로이드 워셜 알고리즘 : 해당 노드를 경유해서 가는 최단거리 cost[출발지][도착지] = min(cost[출발지][도착지], cost[출발지][경유지] + cost[경유지][출발지])
'''
INF = int(1e9)

n = int(input()) # node 의 개수
m = int(input()) # case

graph = [[INF]*(n+1) for i in range(n+1)]

for a in range(1, n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

for i in range(n+1): # 출발지
    for j in range(n+1): # 도착지 
        for k in range(n+1): # 경유지
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
'''

# 미래도시 
# 다익스트라, 그러나 비용은 모두 1로 고정

'''
4 2
1 3
2 4
3 4
'''
# 플로이드 워셜 : 모든 노드에 대한 최단 거리 d[출발지][목적지] = min(d[출발지][목적지], d[출발지][경유지] + d[경유지][도착지])
'''
import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split()) # 노드 개수, m 케이스 개수
INF = 1e9
graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(1, n+1): # 처음에 대각행렬은 모두 0으로 초기화
    graph[i][i] = 0

for _ in range(m): # 입력을 받아야함
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())
# 해당 점화식대로 진행 : min(d[출발지][목적지], d[출발지][경유지] + d[경유지][도착지])

for i in range(1, n+1): # 출발지
    for j in range(1, n+1): # 도착지
        for k in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

distance = graph[1][K] + graph[K][X]

if distance == INF:
    print(-1)
else:
    print(distance)
'''
# 전보
import heapq
import sys


N,M,C = map(int ,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

INF = 1e9
distance = [INF] * (N+1)
def dijkstra(start):
    q = []    
    heapq.heappush(q,(0, start)) # 객체 선언이 아닌 이런식으로 만든다.
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 더 작은 것으로 교체 되었기 때문에 진행하지 않아도 되는 프로세스
            continue
        for i in graph[now]: # 1 2 3 : 1번노드에서 2번노드로 이동할 때 
            cost = dist + i[1] # dist는 현재 노드까지의 거리 + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost # min(1-2 직진, 경유해서 가는 길이 더 빠른지)
                heapq.heappush(q, (cost, i[0]))
dijkstra(C)
# 전달할 수 있는 도시 + 최대 비용

count = 0
for i in distance:
    if i != INF and i != 0:
        count +=1
        max_distance = max(max_distance, i)
print(count, max_distance)