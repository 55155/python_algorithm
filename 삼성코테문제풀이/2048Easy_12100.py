# 입력부
N = int(input())
board_origin = []
for i in range(N):
    temp = list(map(int,input().split()))
    board_origin.append(temp)
# 구현부
import copy
max_value = 0
# 상하좌우
drow = [-1,1,0,0]
dcol = [0,0,-1,1]
def rule(row, col):
    if row >= N or row < 0:
        return False
    elif col >= N or col < 0:
        return False
    return True
def move(command_num, board):
    if command_num == 1: # 상
        for row in range(N): # 0
            for col in range(N): # 0
                for i in range(row, 0, -1): # 2 1 0
                    if board[row][col] == 0:    
                        break
                    elif rule(row-1, col) and board[row][col] != 0 and board[row-1][col] == 0:
                    # 현재 board[row][i] 값이 0이 아니고, 다음칸이 빈칸이면, 
                        board[row-1][col] = board[row][col]
                        board[row][col] = 0
                    elif rule(i-1, col) and board[i][col] != 0 and board[i][col] == board[i-1][col]:
                        board[i-1][col] += board[i][col]
                        board[i][col] = 0
    elif command_num == 2: # 하
        for row in range(N, -1, -1): # 0
            for col in range(N): # 0
                for i in range(row, N-1): # 2 1 0
                    if board[i][col] == 0:
                        break
                    elif rule(i+1, col) and board[i][col] != 0 and board[i+1][col] == 0:
                    # 현재 board[row][i] 값이 0이 아니고, 다음칸이 빈칸이면, 
                        board[i+1][col] = board[i][col]
                        board[i][col] = 0
                    elif rule(i+1, col) and board[i][col] != 0 and board[i][col] == board[i+1][col]:
                        board[i+1][col] += board[i][col]
                        board[i][col] = 0
    elif command_num == 3:
        for row in range(N): # 0
            for col in range(N): # 0
                for i in range(col, 0, -1): # 2 1 0
                    if board[row][i] == 0:
                        break
                    elif rule(row, i-1) and board[row][i] != 0 and board[row][i-1] == 0:
                    # 현재 board[row][i] 값이 0이 아니고, 다음칸이 빈칸이면, 
                        board[row][i-1] = board[row][i]
                        board[row][i] = 0
                    elif rule(row, i-1) and board[row][i] != 0 and board[row][i] == board[row][i-1]:
                        board[row][i-1] += board[row][i]
                        board[row][i] = 0
    elif command_num == 4: # 우
        for row in range(N): # 0
            for col in range(N, -1, -1): # 0
                for i in range(col, N-1): # 2 1 0
                    if board[row][i] == 0:
                        break
                    elif rule(row, i+1) and board[row][i] != 0 and board[row][i+1] == 0:
                    # 현재 board[row][i] 값이 0이 아니고, 다음칸이 빈칸이면, 
                        board[row][i+1] = board[row][i]
                        board[row][i] = 0
                    elif rule(row, i+1) and board[row][i] != 0 and board[row][i] == board[row][i+1]:
                        board[row][i+1] += board[row][i]
                        board[row][i] = 0
    return board
move(4, board_origin)
move(3, board_origin)
move(1, board_origin)
for i in board_origin:
    print(i)
def backtracking(board_local, depth):
    global max_value
    if depth == 5:
        for i in board_local:
            max_value = max(max_value, max(i))
    else:
        for i in range(1, 5):
            copy_board = copy.deepcopy(board_local)
            backtracking(move(i, copy_board), depth + 1)

# backtracking(board_origin, 0)
# print(max_value)