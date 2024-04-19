# BFS 로 네개의 블록을 먹으면 종료 
N, M = map(int, input().split())
board = []
for i in range(N):
    temp = list(map(int,input().split()))
    board.append(temp)

# 구현부
# 상하좌우
drow = [-1,1,0,0]
dcol = [0,0,-1,1]
max_value = 0
OH = [[0,1,2], [0,1,3], [0,2,3], [1,2,3]]
visited = [[False] * M for i in range(N)]
def rule(row,col):
    if row >= N or row < 0:
        return False
    if col >= M or col < 0:
        return False
    return True

DP = [[0] * M for i in range(N)]
def T_shape(center_row, center_col):
    global OH
    max_result = 0
    result = board[center_row][center_col]
    for i in OH:
        for direction in i:
            nrow = center_row + drow[direction]
            ncol = center_col + dcol[direction]
            if rule(nrow,ncol):
                result += board[nrow][ncol]
            else:
                result = 0
                break
        if max_result < result:
            max_result = result
        result = board[center_row][center_col]
    return max_result

def DFS(row,col,value,depth): # start_depth == 1, end_depth == 4
    # 백트래킹 방식
    global max_value,visited
    if depth == 3:
        max_value = max_value if max_value > value else value
    else:
        for i in range(4): # 방향
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if rule(nrow, ncol):
                if visited[nrow][ncol] == False:
                    visited[nrow][ncol] = True
                    DFS(nrow, ncol, value + board[nrow][ncol], depth + 1)
                    visited[nrow][ncol] = False       

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i,j,board[i][j],0)
        visited[i][j] = False
        max_value = max(max_value, T_shape(i,j))

print(max_value)
