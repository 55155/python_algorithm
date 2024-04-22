N, S = map(int,input().split())
l = list(map(int,input().split()))
count = 0
visited = [False for i in range(N)]

def DFS(index, depth, sum, limit):
    global S, count 
    if depth == limit:
        # print(sum)
        if sum == S:
            count += 1
    else: 
        for i in range(index, N):
            if visited[i] == False:
                visited[i] = True
                DFS(i,depth + 1, sum + l[i], limit)
                visited[i] = False

for limit in range(1, N+1): # 5개 모두 더하는 경우
    DFS(0, 0, 0,limit)

print(count)