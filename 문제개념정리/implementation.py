'''
a = int(input())
l = list(input().split())

row = col = 1

def WAY(w):
    global row, col
    if w == 'U' and row > 1:
        row -= 1
    elif w == 'D' and row < a:
        row += 1
    elif w == 'L' and col > 1:
        col -= 1
    elif w == 'R' and col < a:
        col += 1

for i in l:
    WAY(i)

print(row, col)
'''

# 3 의 개수를 출력하는 문제

# 5 면 5시까지 모든 3이 들어가는 시간을 count++
'''
time = int(input())
min = 60
sec = 60
# 1분에 몇개의 경우의 수가 있는가
count = 0

for i in range(time):
    if '3' in str(i):
        count += min * sec
    for w in range(min):
        if '3' in str(w):
            count += 60
            continue
        for j in range(sec):
            if '3' in  str(j):
               count += 1 

print(count)
'''
'''
string_board = input()
step = [(-2, 1),(-2, -1),(2,-1), (2, 1), (1,2), (1,-2), (-1, 2), (-1, -2)]

# 조건 a ~ h # 7만큼 차이
# ord('a') < string_board[0] + nx < ord('h')
row = string_board[1]
col = string_board[0]
count = 0

for i, j in step:
    if ord('a') <= ord(col) + i and ord(col)+i <= ord('h') and 1 <= int(row) + j and int(row) + j <= 8:
        count +=1

print(count)
'''

# 4 4
# 1 1 0
# 1은 바다 0은 육지

row,col = map(int, input().split())
x,y,direction = list(map(int, input().split()))
turn_time = 0

board1 = [[0] * col for i in range(row)]
board = [list(map(int, input().split())) for i in range(row)]

board1[x][y] = 1

drow = [-1,0,1,0] # 북 동 남 서
dcol = [0,1,0,-1] # 북 동 남 서

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
result = 0 # 정답
while True:
    turn_left()
    # direction 이 의미하는 바 --> drow[direction], dcol[direction]
    nx = x + drow[direction]
    ny = y + dcol[direction]
    if board1[nx][ny] == 0 and board[nx][ny] == 0: # 가보지 않았고, 육지라면,
        board1[x][y] = 1
        x = nx
        y = ny
        result += 1
        turn_time = 0
    else:
        turn_time += 1
    if turn_time == 3:
        nx = x - drow[direction]
        ny = x - dcol[direction]
        if board[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(result)