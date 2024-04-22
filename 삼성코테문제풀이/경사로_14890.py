N, L = map(int,input().split())
# height, row, col
import copy
board = [[copy.deepcopy([0])*11]*N for i in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    for i in range(N): # 3 3 3 3 3 3 [1][i][j] [2][i][j] [3][i][j]
        
for i in board:
    print(i)

