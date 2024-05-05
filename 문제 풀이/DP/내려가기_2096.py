N = int(input())
board = []
for i in range(N):
    temp = list(map(int,input().split()))
    board.append(temp)
import copy
def rule(row,col):
    if row >= N or row < 0:
        return False
    if col >= N or col <0:
        return False
    return True
DP = [[0]*N for i in range(N)]
DP2 = [[0]*N for i in range(N)]
DP[0] = copy.deepcopy(board[0])
DP2[0] = copy.deepcopy(board[0])
for i in range(1, N):
    DP[i] = [0]*N
    DP2[i] = [1e7]*N

DP = copy.deepcopy(board)
# [row][col] => [row+1][col-1], [row+1][col], [row+1][col+1]
for row in range(N):
    for col in range(N):
        for i in range(3):
            if i == 0 and rule(row+1, col-1):
                DP[row+1][col-1] = max(DP[row+1][col-1], DP[row][col]+board[row+1][col-1])
                DP2[row+1][col-1] = min(DP[row+1][col-1], DP[row][col]+board[row+1][col-1])
            elif i == 1 and rule(row+1, col):
                DP[row+1][col] = max(DP[row+1][col], DP[row][col]+ board[row+1][col])
                DP2[row+1][col] = min(DP[row+1][col], DP[row][col]+ board[row+1][col])
            elif i == 2 and rule(row+1, col+1):
                DP[row+1][col+1] = max(DP[row+1][col+1], DP[row][col] + board[row+1][col+1])
                DP2[row+1][col+1] = min(DP[row+1][col+1], DP[row][col]+ board[row+1][col+1])
print(DP)
print(DP2)