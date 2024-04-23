# 입력부
N, L = map(int, input().split())
board = []
for i in range(N): # 2차원
    temp = list(map(int,input().split()))
    board.append(temp)

for row in range(N):
    print(board[row])
print()
print(board[0:6][0])