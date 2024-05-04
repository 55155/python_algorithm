N, K = map(int, input().split())
l = [[0,0] for i in range(K+1)]
from collections import deque
def rule(col):
    if col >= K+1 or col < 0:
        return False
    return True
print(l)
def BFS(start_col):
    global l
    q = deque([start_col])
    l[start_col][0] = 0
    while q:
        col = q.popleft()   
        if rule(col+1):
            if l[col+1][0] == 0:
                l[col+1][0] = l[col][0] + 1
                l[col+1][1] = 1
                q.append(col+1)
            else:
                if l[col+1][0] == l[col][0] + 1:
                    l[col+1][1] += 1
                    q.append(col+1)
        if rule(col-1):
            if l[col-1][0] == 0:
                l[col-1][0] = l[col][0] + 1
                l[col-1][1] = 1
                q.append(col-1)
            else:
                if l[col-1][0] == l[col][0] + 1:
                    l[col-1][1] += 1
                    q.append(col-1)
        if rule(col*2):
            if l[col*2][0] == 0: # 첫방문
                l[col*2][0] = l[col][0] + 1
                l[col*2][1] = 1
                q.append(col*2)
            else:
                print('in if')
                if l[col*2][0] == l[col][0] + 1:
                    l[col*2][1] += 1
                    q.append(col*2)
BFS(N)
print(l)