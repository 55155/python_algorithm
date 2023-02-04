'''
a = int(input())
count = 0
money_list =  [500,100,50,10]

for i in money_list:
    count += a // i
    a %= i

print(count)
'''
'''
# 큰 수의 법칙
N, M ,K = map(int, input().split())
l = list(map(int, input().split()))

l = sorted(l, reverse = True)

Max = l[0]
Min = l[1]

k = 0
result = 0
# rule 연속해서 k 번 더할 수 없음
# 총 M 번 연산할 수 있음
for i in range(M):
    if k < K:
        result += Max
        k += 1
    else:
        result += Min
        k = 0

print(result)

# 큰 수의 법칙2
count = (M // (K+1))*K
count += M %(K+1)

result = count * Max
result += (M - count) * Min
'''
'''
# 행마다 제일 작은 수 중 결국 제일 큰 수를 뽑는 것
row, col = map(int, input().split())
l = [list(map(int, input().split())) for i in range(row)]
print(l)
r = []

for i in range(row):
    r.append(min(l[i]))

print(max(r))
'''

# 1이 될 떄까지
# 그리디 알고리즘 : 당장에 할 수 있는 최적의 선택을 하는 알고리즘,
# 선택의 결과가 미래에 어떻게 다가올지는 전혀 생각하지 않는다.

# 제곱근

N, K = map(int, input().split())
count = 0
# 먼저 5를 반복적으로 제곱 --> ex) 126 5 세번 곱하면 125가되고 1이 남는다 해당 1을 +해주면 된다.

result  = 0
# 최대한 많이 나눠야함
while True: # 25 3 case 최대한 많이 나눠야 유리 
    target = (N // K) * K #  24 
    count += N - target
    N -= (N - target)

    if N < K:
        break
    
    N //= K
    count += 1

count+= (N-1) 

print(count)