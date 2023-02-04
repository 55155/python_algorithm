# 다이나믹 프로그래밍 이용
# 점화식 이전 스텝에서 더하여 만들 수 있는가를 보면 된다.
# ex) 3 2 1 1 9 
# l[금액] += 지폐
# 바텀 업

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x: 
        # 만들어야하는 금액보다 지폐가 더 크면 
        break
    target += x

print(target)