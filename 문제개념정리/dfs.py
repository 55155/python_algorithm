from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()

print(queue)

# 인접 행렬 방식 : 연결성이 없는 것들도 모두 추가, 특정값만 봐야할 때는 더 효율적이다.

'''
INF = 99999999
graph = [
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
print(graph)
'''
# 인접 리스트 방식 : 연결성이 있는 것들만 리스트에 추가 , 모든 경우를 순회해야할 때는 더 효율적이다.
'''
graph = [[] for i in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))
'''
# DFS 는 관행적으로 번호가 낮은 순서부터 처리한다.

def dfs(graph, v, visited): # 한번할때 해당 노드 끝까지 체크
    
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
graph = [
    [], 
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9
dfs(graph, 1, visited)

# BFS : 너비우선탐색, 재귀 없음, 한번에 인접노드 다탐색, 다 방문처리
from collections import deque

def bfs(graph, start, visited):
    
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

graph = [
    [], 
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * 9
bfs(graph, 1, visited)
print()


# 음료수 얼려먹기
# 인접한 노드를 다 방문하고 만약 루프가 끝나게 되면 result += 1
# 인접 노드를 파악하는 방법
'''
row, col = map(int, input().split())
board = [input() for i in range(row)]
print(board)
visited = [[False]*col for  i in range(row)]

drow = [-1,0,1,0] # 북 동 남 서
dcol = [0,1,0,-1]
count = 0 
flag = False
def dfs(x,y):
    # x,y 좌표를 주었을 때 인접한 좌표가 있는지 검사해야함
    visited[x][y] = True
    for i in range(4):
        nx = x + drow[i]
        ny = y + dcol[i]
        if (0 <= nx and nx < row ) and (0 <= ny and ny < col): # 좌표 내이고
            print(nx, ny)
            if visited[nx][ny] == False and board[nx][ny] == '0': # 방문한적 없으며, 해당칸이 얼릴칸이라면
                visited[nx][ny] = True
                x = nx
                y = ny
                dfs(x,y)

for j in range(row):
    for w in range(col):
        print(j, w)
        if board[j][w] == '0' and visited[j][w] == False:
            dfs(j,w)
            count += 1 
print(count)
'''
'''
4 5
00110
00011
11111
00000
'''

# 미로 탈출
# 초기 위치 1,1
# 괴물 O --> 0
# 괴물 X --> 1
# 반드시 탈출 , 시작칸, 마지막칸 포함 count
# test_case
'''
5 6
101010
111111
000001
111111
111111
'''   

# BFS 이용 이유 : 미로 특성상 쭉 직진하더라도 중간에 막히면 꽝임 따라서 모두 탐색한 후 제시

'''
from collections import deque
y, x = map(int, input().split())
board = []
for i in range(y):
    board.append(list(map(int, input()))) # split() 안쓰면 그냥 된다.


visited = [[False] * x for i in range(y)]

dx = [0, 1, 0 ,-1] # 북 동 남 서
dy = [-1, 0, 1, 0]
# 출구 ( row - 1, col - 1)
count = 0 
def BFS(a, b): # 재귀 사용안함, a = x, b = y
    # popleft 사용해야하는 경우 : 더 이상 탐색할 경로가 없을 때
    global x,y
    global count
    graph = deque([(a,b)])
    visited[a][b] = True

    while graph: # 새로 갱신된 좌표에서 
        a,b = graph.popleft()
        for i in range(4): # 4 방향 탐색 
            nx = a + dx[i] # 북 동 남 서 탐색 
            ny = b + dy[i]
            if 0 <= nx and nx < x and 0 <= ny and ny < y:
                if visited[ny][nx] == False and board[ny][nx] == 1: # 괴물이 없으면서 방문한 적이 없다.
                    print(f'append! {nx} {ny}')
                    visited[ny][nx] = True
                    board[ny][nx] += board[b][a]
                    graph.append((nx,ny))
                    # result += 1 # 새로운 경로를 발견할 때마다 1씩
    return board[ny-1][nx-1]
# 모두 탐색 아이디어 : append를 시키고 pop이 되었다 ==> 해당 경로로 이동
# append 된 좌표중 허수가 있음 --> 다음 경로가 없음

print(BFS(0,0))
'''
