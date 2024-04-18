# 입력부
N, M, row, col, command_num = map(int,input().split())
board = list()
for i in range(N):
    temp = list(map(int,input().split()))
    board.append(temp)

command = list(map(int, input().split()))

# 구현부
# 동서북남
def change_dice(dir_num):
    global dice
    # initial position 기준 dice정의 -> 
    # index로 정의
    if dir_num == 0: # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif dir_num == 1: # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif dir_num == 2: # 북 
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    elif dir_num == 3: # 남 
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

drow = [0,0,-1,1]
dcol = [1,-1,0,0]
dice = [0,0,0,0,0,0] # 1 2 3 4 5 6 
# 인덱스-1가 전개도를 의미  
def rule(row, col):
    if row >= N or row < 0:
        return False
    if col >= M or col < 0:
        return False
    return True

for i in range(command_num):
    direction = command[i] - 1
    nrow = row + drow[direction]
    ncol = col + dcol[direction]
    if rule(nrow, ncol):
        row = nrow
        col = ncol
        change_dice(direction)
        if board[nrow][ncol] == 0:
            board[nrow][ncol] = dice[5]
        else:
            dice[5] = board[nrow][ncol]
            board[nrow][ncol] = 0
        # 1기준 : 동쪽; + 2, 서쪽; +3, 북쪽; +1, 남쪽; +4
        # 2기준 : 동쪽; + 1, 서쪽; +2, 남쪽; -1
        print(dice[0])
    else:
        pass
