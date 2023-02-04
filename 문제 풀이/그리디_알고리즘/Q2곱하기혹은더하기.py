# 곱하기
import sys
input = sys.stdin.readline
data = list(map(int, input().strip()))

result = 1
for i in data: # 0 2 9 8 4
    if i != 0 and i != 1:
        result *= i
    else:
        result += i

print(result)
        
    