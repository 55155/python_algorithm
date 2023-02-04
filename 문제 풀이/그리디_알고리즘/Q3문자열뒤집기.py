# 구간 뒤집기
import sys
input = sys.stdin.readline
data = list(map(int, input().strip()))
pre = data[0]

num_0 = 0
num_1 = 0

for i in data:
    if pre == 0 and i ==1:
        num_0 += 1
    elif pre == 1 and i ==0:
        num_1 += 1
    pre = i

if data[0] == data[-1]: # 양 옆이 같을 때는 그냥 출력 
    print(min(num_0, num_1))
else: # 양옆이 다를 때에는 패널티를 준다. 
    print(min(num_0, num_1) + 1)




# 솔루션

data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))
