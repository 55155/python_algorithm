# 입력부
N, L = map(int, input().split())
board = []
for i in range(N): # 2차원
    temp = list(map(int,input().split()))
    board.append(temp)
l = [2, 2, 2, 3, 2, 3]
# 구현부 
def rule(x):
    if x < 0 and x >= N:
        return False
    return True

def line(l, L):
    point = 1
    while True:
        if point == N:
            return True
        if abs(l[point] - l[point - 1]) < 1:
            point += 1
        elif l[point] - l[point - 1] == 1:
            # 오르막길인 경우
            if rule(point-L) and rule(point-1):
                for i in range(point-L, point): # point ~ point + L 까지 1 생성
                    if rule(i) and l[point-1] == l[i]:
                        l[i] += 0.5
                    else:
                        return False
            else:
                return False
            point -= L
        elif l[point] - l[point - 1] == -1:
            # 내리막길인 경우
            if rule(point+L) and rule(point-1):
                for i in range(point, point+L+1): # point ~ point + L 까지 1 생성
                    if rule(i) and l[point+1] == l[i]:
                        l[i] += 0.5
                    else:
                        return False
            else:
                return False
            point -= 1
        else: # 2차이가 나는 경우
            return False

import copy 
for i in board:
    temp = copy.deepcopy(i)
    print(line(temp, L))
l = []
print()
for col in range(N):
    for row in range(N):
        
        l.append(board[row][col])
    print(line(l, L))
    print(l)
    l = [] 
# # 가로방향 탐색
# for row in range(N):
#     for col in range(N):
#         print(board[row][col])
# # 세로방향 탐색
# for col in range(N):
#     for row in range(N):
#         print(board[row][col])
