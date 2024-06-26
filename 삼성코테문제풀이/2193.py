N = int(input())
# 1자리에 1로 끝나는 경우 [1][1]
# 1자리에 0으로 끝나는 경우 [1][0]
DP = [[0,0] for i in range(N+1)]
DP[1][1] = 1
DP[1][0] = 0
# 0으로 끝나는 경우는 0이 나올 수 있음, 1로 끝나는 경우 1만 나올 수 있음 
for i in range(2, N+1):
    DP[i][0] = DP[i-1][0] + DP[i-1][1]
    DP[i][1] = DP[i-1][0]
print(sum(DP[-1]))