# 입력부
N, M = map(int, input().split())
board = []
for i in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)

# 구현부
def square()