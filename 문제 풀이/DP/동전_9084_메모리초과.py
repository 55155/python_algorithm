T = int(input())
l = []
DP = [] # 개수를 담는 리스트
for i in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    M = int(input())
    DP = [[0] * (l[-1] + 1) for i in range(10001)] # 
    for coin in l:
        DP[coin][coin] = 1
    for money in range(1, M+1):
        for coin in l:
            # 30 = 20 + 10, 30 = 10 + 20
            # 이전 경우의 수에 현재 동전으로 만들 수 있는 경우의 수를 더한다.
            for coin2 in l:
                if money - coin >= 0 and coin >= coin2:
                    DP[money][coin] += DP[money - coin][coin2]

    print(sum(DP[M]))