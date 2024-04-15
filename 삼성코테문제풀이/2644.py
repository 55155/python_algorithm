N = int(input())
start, end = map(int,input().split())
case = int(input())
l = [[] for i in range(N+1)]
for i in range(case):
    parent, child = map(int,input().split())
    l[parent].append(child) # 인덱스가 가지고 있는 아이들 검사
    l[child].append(parent) # 인덱스가 가지고 있는 부모 검사
    # 아이들끼리는 2촌 

# 구현부
visited = [0 for i in range(N+1)] # 아직 방문하지 않음.
from collections import deque
def BFS(start):
    q = deque([start])
    visited[start] = 0
    while q:
        human = q.popleft() # 7
        for i in range(len(l[human])):
            if visited[l[human][i]] == 0:
                visited[l[human][i]] = visited[human] + 1
                q.append(l[human][i])

BFS(start)
if visited[end] == 0:
    print(-1)
else:
    print(visited[end])