n, k = map(int, input().split())
DP = [99999 for i in range(100001)]
coin_list = []
for i in range(n):
    coin = int(input())
    coin_list.append(coin)
    DP[coin] = 1

for i in range(1, len(DP)):
    for j in coin_list:
        try:
            DP[i+j] = min(DP[i+j], DP[i] + 1)
        except IndexError:
            pass

if DP[k] == 99999:
    print(-1)
else:
    print(DP[k])
