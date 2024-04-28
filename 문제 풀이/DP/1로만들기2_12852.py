# 입력부
X = int(input())
# 구현부
# 세가지 방법 : x3, x2, +1
count = 0
N = X
DP = [99 for i in range(1000000)]
DP[1] = 0
for i in range(1 , N):
    DP[i*3] = min(DP[i] + 1, DP[i*3])
    DP[i*2] = min(DP[i] + 1, DP[i*2])
    DP[i+1] = min(DP[i] + 1, DP[i+1])
print(DP[])