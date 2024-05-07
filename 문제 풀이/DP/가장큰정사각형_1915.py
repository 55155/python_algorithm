# 입력부
import copy
N, M = map(int, input().split())
board = [[] for i in range(N)]

for row in range(N):
    temp = input()
    for col in range(M):
        board[row].append(int(temp[col]))
    
direction = []
DP = copy.deepcopy(board)
# 구현부
for row in range(1,N):
    for col in range(1,M):
        if DP[row][col] != 0:
            DP[row][col] = min(DP[row-1][col], DP[row][col-1], DP[row-1][col-1]) + 1
max_value = 0
for i in DP:
    max_line = max(i)
    if max_line > max_value:
        max_value = max_line
print(max_value ** 2)