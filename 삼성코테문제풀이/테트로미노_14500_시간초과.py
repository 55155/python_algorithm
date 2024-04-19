N, M = map(int,input().split())
board = []
for i in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)
Max_Board = [[0] * M for i in range(N)]
visited = [[False] * M for i in range(N)]
# 구현부
# 상하좌우
drow = [-1,1,0,0]
dcol = [0,0,-1,1]
def rule(row,col):
    if row >= N or row < 0:
        return False
    if col >= M or col < 0:
        return False
    return True
from collections import deque
max_value = 0

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
import copy
l = []
result = []
visited_l = [False for i in range(4)]
def back_tracking(pre_value, depth):
    if depth == 3:  
        result.append(copy.deepcopy(l))
        return 
    else:
        for i in range(pre_value, 4):
            if visited_l[i] == False:
                visited_l[i] = True
                l.append(i)
                back_tracking(i, depth + 1)
                l.pop()
                visited_l[i] = False

back_tracking(0,0)
def OH(start_row,start_col):
    global result
    count = board[start_row][start_col]
    # 1 2 3
    # 1 2 4
    # 1 3 4
    # 2 3 4
    max_value_OH = 0
    for case in result:
        for direction in case: 
            nrow = start_row + drow[direction]
            ncol = start_col + dcol[direction]
            if rule(nrow,ncol):
                count += board[nrow][ncol]
            else:
                count = board[start_row][start_col]
                # result = 0 if 하나라도 넘어가면
                break
        if max_value_OH < count:
            max_value_OH = count   
            count = board[start_row][start_col]
        else:
            count = 0

    return max_value_OH

max_OH = 0
for i in range(N):
    for j in range(M):
        # i, j 번쨰 board
        visited[i][j] = True
        DFS(i,j,board[i][j],0)
        value_OH = OH(i,j)
        if max_OH < value_OH:
            max_OH = value_OH
        Max_Board[i][j] = max_value
        max_value = 0
        visited = [[False] * M for i in range(N)]
max_value = 0
for i in Max_Board:
    if max_value < max(i):
        max_value = max(i)

print(max(max_value, max_OH))