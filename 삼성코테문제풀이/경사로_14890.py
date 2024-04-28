# 입력부
N, L = map(int, input().split())
board = []
for i in range(N): # 2차원
    temp = list(map(int,input().split()))
    board.append(temp)

# 가로방향 탐색
for row in range(N):
    for col in range(N):
        print(board[row][col])
# 세로방향 탐색
for col in range(N):
    for row in range(N):
        print(board[row][col])
