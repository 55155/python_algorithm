# 입력부
N, M, col, row, command_num = map(int,input().split())
board = list()
for i in range(N):
    temp = list(map(int,input().split()))
    board.append(temp)
command = list(map(int, input().split()))

# 구현부
# X동서북남
drow = [0,0,0,-1,1]
dcol = [0,-1,1,0,0]
dice_garo = [0,0,0,0] # 4 1 3 6
dice_sero = [0,0,0,0] # 
def rule(row, col):
    if row >= N or row < 0:
        return False
    if col >= M or col < 0:
        return False
    return True
for i in range(command_num):
    