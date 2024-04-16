# 입력부
N = int(input())
board = [[0]*(N+1) for i in range(N+1)]
apple_num = int(input())
apple = []
for i in range(apple_num):
    apple_row, apple_col = map(int, input().split())
    apple.append([apple_row-1, apple_col-1])
    board[apple_row-1][apple_col-1] = 1 # 사과 위치 결정

move_num = int(input())
move = []
for i in range(move_num):
    move_sec, move_dir = map(str, input().split())
    move_sec = int(move_sec)
    move.append([move_sec, move_dir])

# 구현부
# 지렁이가 있는 공간을 -1로 두자.
def rule(row,col):
    if row >= N or row < 0:
        return False
    if col >= N or col < 0:
        return False 
    return True
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
from collections import deque
q = deque([[row,col]])
break_flag = False
count = 0

for i in range(0, move_num):
    sec = move[i][0] # 움직임 규칙 
    dir_str = move[i][1] # 
    for i in range(0, sec-pre_sec): # 0초부터 3초까지 이동
        count += 1
        nrow = row + drow[direction]
        ncol = col + dcol[direction]
        if rule(nrow,ncol) :
            row = nrow
            col = ncol

            if board[nrow][ncol] == 1:
                q.append([nrow,ncol])
                node = q[0]
                board[nrow][ncol] = -1
            elif board[nrow][ncol] == 0:
                q.append([nrow, ncol])
                board[nrow][ncol] = -1
                node = q.popleft()
                board[node[0]][node[1]] = 0
            else:
                break_flag = True

                break

        else:

            break_flag = True

            break

    # 다음방향으로 전환
    if dir_str == 'D':
        if direction + 1 < 4:
            direction += 1
        else:
            direction = 0
    elif dir_str == 'L':
        if direction - 1 > -1:
            direction -= 1
        else:
            direction = 3
    if break_flag:
        break
    pre_sec = sec

while not break_flag:

    nrow = row + drow[direction]
    ncol = col + dcol[direction]
    count += 1
    if rule(nrow,ncol) :
        row = nrow
        col = ncol

        if board[nrow][ncol] == 1:
            q.append([nrow,ncol])
            node = q[0]
            board[nrow][ncol] = -1
        elif board[nrow][ncol] == 0:
            q.append([nrow, ncol])
            board[nrow][ncol] = -1
            node = q.popleft()
            board[node[0]][node[1]] = 0
        else:
            break_flag = True
            break

    else:
        break_flag = True
        break


print(count)
# 마지막움직임은 for문 이후에 해결
