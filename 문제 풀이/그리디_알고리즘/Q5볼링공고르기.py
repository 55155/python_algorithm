N, M = map(int, input().split())
l = list(map(int, input().split()))

count =0 
# 백테스팅 안해도된다
for i in range(N):
    for j in range(i, N):
        if l[i] != l[j]:
            count += 1
print(count)

# solution

array = [0 for i in range(N+1)] # 해당 무게의 공이 몇개인지
for i in l:
    array[i] += 1
result = 0
for i in range(len(array)):
    N -= array[i] # 두번째로 뽑을 수 있는 공의 경우의 수를 줄인다.
    result += array[i] * N # 두 경우의 수를 곱하여ㅓ result를 구한다.
    
