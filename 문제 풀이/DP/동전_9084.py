T = int(input())
l = []
DP = [] # 개수를 담는 리스트
for i in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    M = int(input())
    DP = [0 for i in range(10001)]

    DP[0] = 1
    for coin in l:
        for money in range(M+1):
            if money - coin >= 0:
                DP[money] += DP[money - coin]
    print(DP[M])