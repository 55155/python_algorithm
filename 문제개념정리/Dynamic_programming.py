# 큰 문제를 작은 문제로 나눌 수 있다. 
# 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다
# 정리 : 작은 문제를 구하는데 썼던 프로세스를 그대로 사용한다. 

# Memoization

d = [0] * 100

def fibo(x): # O(N) : 훨씬 짧다 , Top down
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo[x-1] + fibo[x-2]
    return d[x]

a = [1,1]
count  =0 
def pibo_dp(x):
    global count
    if x == 0 or x == 1:
        return 1
    else:
        for i in range(2, x):
            count += 1
            a.append(a[i-1] + a[i-2])
        return a[x-1] 
print(pibo_dp(30))

# 1. 점화식 정의
# 2. 해당 점화식을 재귀형식이 아닌 반복문 형식으로 사용

# 1로 만들기
'''
num = int(input())
d = [0] * 30001

for i in range(2, num+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1) # 1로 빼는 것이 더 나은 프로세스인가, 2로 나누는 프로세스가 더 나은 프로세스인가를 비교
        # ex) 26 == > d[25] + 1 = 3
        #     26 == > d[26//2] + 1 = d[13]
    if i % 3 == 0: # elif 가 아닌 이유는 공배수일 때 더 작은 프로세스를 구해야하기 위함이다.
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[num]) # 하위 횟수에서 plus하는 식으로 연산
'''

# 제일 큰 수로 나누어야 효율적이다.
# 하위 문제로 나눌 수 있는가 ?
# Tree 문제로 나눌 수 있음
# 아이디어 : 횟수자체를 구하는 문제 
# 해를 구하는 문제가 아니라 횟수를 구하는 문제
# if N % x == 0: 일 때 해당값으로 가는데, 

# 개미 전사

# 가장 높은 해를 구해야한다 
# 브루스포스로 할 수 있나 ?
# step = 4. X
# step = 3. O
# step = 2. O
'''
length = int(input()) # 초기 설정 미스
food = list(map(int, input().split()))
l = [food[0], max(food[0], food[1])] + [0] * 97
# 1 4 1

def iter(length): # 3 1 1 4
    for i in range(2,length):
        l[i] = max(l[i-1], l[i-2] + food[i])
    return l[length-1]

print(iter(length))
'''

# 세가지 경우의 수에 대해서 구할 수 있음
# 점화식을 구성

# 이전 step에서의 경우의 수 
# N = 0 --> 0
# N = 1 --> 1
# N = 2 --> 3
# N = 3 --> 5
# N = 4 --> 9
# 이전 step에서 1 x 2 를 왼쪽 혹은 오른쪽에 넣음에 따라 이전 스텝의 경우의수 x 2 가 된다. 여기서 -1을 해주어야하는 이유는 모두 2x1일때의 경우는 중복되기 떄문
'''
integer = int(input())
N = [0] * (integer +1)
N[1] = 1
N[2] = 3
for i in range(3, integer+1):
    N[i] = ( N[i-1] * 2 ) - 1

print(N[integer])


n = int(input())
d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2 * d[i-2])

print(d[n])
'''
# 효율적인 화폐구성
# 최소한의 화폐를 사용하여 출력하기
'''
효율적으로 뺄셈을 해야한다.
'''
# N = 0 --> 0
# N = 1 --> -1
# N = 2 --> -1
# N = 3 --> 1
# N = 4 --> -1
# N = 5 --> 1
# N = 6 --> 2
# N - 3,5,7 를 했을 때 음수이거나, result[N - 3] 을 했을 때 해당 수가 -1:
# result[i] = -1
# 아니라면 min으로 가야한다.

# 점화식 
# 2 3 5
# 2부터 출발
# bottom , dynamic programming ( 점화식 )
N, M = map(int, input().split())
l = []

for i in range(N):
    l.append(int(input()))

result = [10001] * (M+1) # 필요한 지폐의 개수 , index가 의미하는 바 : 얼마 ? 
result[0] = 0

# 점화식 a{n} = min(a{n-k} + 1, a{n}). # 1이 의미하는 바는 k원 지폐한장
# ex) 2 3 5 --> min(a{n-A} + 1, a{n-B} + 1, a{n-C} + 1)
#           --> 모두 10001이다 --> a[n] = 10001

for i in l: # 2 3 5
    for j in range(i, len(result)): # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
        if result[j-i] != 10001:  # result[0-7]
            result[j] = min(result[j], result[j-i]+1)

print(result)
if result[M] != 10001:
    print(result[M])
else:
    print(-1)
