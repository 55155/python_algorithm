# 입력부
N = int(input())
board = []
for i in range(N):
    temp = list(map(int,input().split()))
    board.append(temp)
# 구현부
max_value = 0
# 상하좌우
drow = [-1,1,0,0]
dcol = [0,0,-1,1]
def rule(row, col):
    if row >= N or row < 0:
        return False
    elif col >= N or col < 0:
        return False
    return True

def move(command_num):
    # 좌측으로 가는 경우
    if command_num == 3:
        for col in range(1, N):
            for row in range(N):
                if board[row][col] == 0: 
                    continue
                nrow = row + drow[command_num]
                ncol = col + dcol[command_num] # 좌측으로 한칸 이동
                for r in range(1, row):
                    


move(3) 
for _ in board:
    print(_)

def backtracking(l, depth):
    if depth == 5:
        for i in l:
            max_value = max(max_value, max(i))
    else:
        pass
