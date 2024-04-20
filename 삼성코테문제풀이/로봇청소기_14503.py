# 입력부
N, M = map(int, input().split())
# 1. 현재 칸이 아직 청소되지 않은 경우 현재칸을 청소한다.
# 2. 현재 칸의 주변 4칸 중 청소되징 않은 빈칸이 있는 경우
    # 2-1. 바라보는 방향을 유지한 채로 한칸 후진할 수 있다면 한 칸 후진후 1번으로 돌아간다. 
    # 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우, 
    # 3-1. 반시계 방향으로 90도 회전한다.
    # 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청되지 않은 빈 칸인 경우 한 칸 전진한다.
    # 3-3. 1번으로 돌아간다. 
row,col,direction = map(int,input().split())
board = []
for i in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)
# 북동남서
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
def rule(row, col):
    if row >= N or row < 0:
        return False
    if col >= M or col < 0:
        return False
    return True

break_flag = False
clean = 0
while True:
    # 1번 조건
    if board[row][col] == 0:
        clean += 1
        board[row][col] = -1 # 청소함
    # 2번 조건
    count = 0 # 4면이 모두 청소되었는가?
    for i in range(1, 5): # 
        pre_dir = (direction - i) % 4 
        nrow = row + drow[pre_dir] 
        ncol = col + dcol[pre_dir]
        if rule(nrow, ncol):
            # 3-1
            if board[nrow][ncol] == 0:
                row = nrow
                col = ncol
                direction = pre_dir
                count = 0
                break 
            elif board[nrow][ncol] == 1: # 벽인경우
                count += 1
            elif board[nrow][ncol] == -1: # 이미 청소한 구역
                count += 1

    direction = pre_dir
    if count == 4: # 2-1 번 조건
        nrow = row - drow[direction]
        ncol = col - dcol[direction]
        if rule(nrow, ncol):
            if board[nrow][ncol] == 1: # 뒷방향이 벽이면, 
                break_flag = True
            else:
                row = nrow
                col = ncol
    if break_flag:
        break

print(clean)