# 입력부
N = int(input())
board = [[0]*N for i in range(N)]
apple_num = int(input())
apple = []
for i in range(apple_num):
    apple_row, apple_col = map(int, input().split())
    apple.append([apple_row-1, apple_col])
    board[apple_row-1][apple_col] = 1 # 사과 위치 결정

move_num = int(input())
move = []
for i in range(move_num):
    move_sec, move_dir = map(str, input().split())
    move_sec = int(move_sec)
    move.append([move_sec, move_dir])

for i in board:
    print(i)
'''
# 구현부
# 지렁이가 있는 공간을 2로 두자.
def rule(row,col):
    if row >= N or row < 0:
        return False
    if col >= N or col < 0:
        return False 
    return False
# 시계방향 정렬
# 우하좌상
drow = [0,1,0,-1]
dcol = [1,0,-1,0]
pre_sec = 0
pre_dir = 0
direction = 0
row = 0
col = 0
length = 1
for i in range(0, len(move_num)):
    sec = move[i][0]
    dir_str = move[i][1]
    for i in range(0, sec-pre_sec+1): # 0초부터 3초까지 이동
        nrow = row + drow[i]
        ncol = col + dcol[i]
        if rule(nrow,ncol) :
            row = nrow
            col = ncol
            length += board[row][col]

    if dir_str == 'D':
        direction += 1
    elif dir_str == 'R':
        direction -= 1
    if board[row][col] == 1:

    pre_sec = sec


# 마지막움직임은 for문 이후에 해결
'''