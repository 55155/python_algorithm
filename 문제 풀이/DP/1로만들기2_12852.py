# 입력부
N = int(input())
DP = [[0, []] for i in range(N+1)]
DP[1][0] = 0
DP[1][1] = [1]
# 구현부
for i in range(2, N+1):
    DP[i][0] = DP[i-1][0] + 1
    DP[i][1] = DP[i-1][1] + [i]
print(DP[-1][0])
DP[-1][1].reverse()
for i in range(1, N+1)
    if i % 3 == 0 and DP[i][0] > (DP[i // 3][0] + 1):
        DP[i][0] = DP[i // 3][0] + 1
        DP[i][1] = DP[i // 3][1] + [i]
    if i % 2 == 0 and DP[i][0] > (DP[i // 2][0] + 1):
        DP[i][0] = DP[i // 2][0] + 1
        DP[i][1] = DP[i // 2][1] + [i]

for i in DP[-1][1]:
    print(i, end = ' ')