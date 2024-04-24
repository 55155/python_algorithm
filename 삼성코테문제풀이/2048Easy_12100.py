# 참고 
# https://bio-info.tistory.com/230

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

def rule(row, col):
    if row >= N or row < 0:
        return False
    elif col >= N or col < 0:
        return False
    return True
def move(command_num, board):
    already_sum = []
    if command_num == 1: # 상
        for col in range(N): # 0
            point = 0
            for row in range(1, N): # 0
                # point 까지 밀어야함
                if board[row][col]:
                    temp = board[row][col]
                    board[row][col] = 0
                    if temp == board[point][col]:
                        board[point][col] *= 2
                        point += 1
                    elif board[point][col] == 0:
                        board[point][col] = temp
                    else: # 둘이 다른 경우 point += 1
                        point += 1
                        board[point][col] = temp

    elif command_num == 2: # 하
       for col in range(N): # 0
            point = N-1
            for row in range(N-2, -1, -1): # 0
                # point 까지 밀어야함
                if board[row][col]:
                    temp = board[row][col]
                    board[row][col] = 0
                    if temp == board[point][col]:
                        board[point][col] += temp
                        point -= 1
                    elif board[point][col] == 0:
                        board[point][col] = temp
                    else: # 둘이 다른 경우 point += 1
                        point -= 1
                        board[point][col] = temp
    elif command_num == 3:
        for row in range(N): # 0
            point = 0
            for col in range(1, N): # 0
                # point 까지 밀어야함
                if board[row][col]:
                    temp = board[row][col]
                    board[row][col] = 0
                    if temp == board[row][point]:
                        board[row][point] += temp
                        point += 1
                    elif board[row][point] == 0:
                        board[row][point] = temp
                    else: # 둘이 다른 경우 point += 1
                        point += 1
                        board[row][point] = temp
    elif command_num == 4: # 우
        for row in range(N): # 0
            point = N-1
            for col in range(N-2, -1, -1): # 0
                # point 까지 밀어야함
                if board[row][col]:
                    temp = board[row][col]
                    board[row][col] = 0
                    if temp == board[row][point]:
                        board[row][point] += temp
                        point -= 1
                    elif board[row][point] == 0:
                        board[row][point] = temp
                    else: # 둘이 다른 경우 point += 1
                        point -= 1
                        board[row][point] = temp
    return board

# def backtracking(board_local, depth):
#     global max_value
#     if depth == 5:
#         for i in board_local:
#             max_value = max(max_value, max(i))
            
#     else:
#         for i in range(1, 5):
#             copy_board = copy.deepcopy(board_local)
#             backtracking(move(i, copy_board), depth + 1)
# # move(3, board_origin)
# # for _ in board_origin:
# #     print(_)
# backtracking(board_origin, 0)
# print(max_value)
ans = 0
def dfs(n, arr):
    global ans
    if n == 5:
        for i in range(N):
            for j in range(N):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return

    for i in range(1, 5):
        copy_arr = copy.deepcopy(arr)
        if i == 1:
            dfs(n + 1, move(i, copy_arr))
        elif i == 2:
            dfs(n + 1, move(i, copy_arr))
        elif i == 3:
            dfs(n + 1, move(i, copy_arr))
        else:
            dfs(n + 1, move(i, copy_arr))

dfs(0, board_origin)
print(ans)