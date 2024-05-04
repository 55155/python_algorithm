# 9465번
# 1 3 5 7 9
# 2 4 6 8 10 ... 
T = int(input())

def rule(row,col):
    if row < 0 or row >= 2:
        return False
    if col < 0 or col >= N:
        return False
    return True
    
for i in range(T):
    N = int(input())
    board = [] # board 초기화 
    DP = [[0] * N for i in range(2)] # row = 2 col = N
    for i in range(2):
        temp = list(map(int,input().split()))
        board.append(temp)
    DP[0][0] = board[0][0]
    DP[1][0] = board[1][0]
    
    for col in range(1, N):
        DP[0][col] = max(DP[0][col-1], DP[1][col-1] + board[0][col])
        DP[1][col] = max(DP[1][col-1], DP[0][col-1] + board[1][col])

    print(max(DP[0][N-1], DP[1][N-1]))