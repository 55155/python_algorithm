S = int(input())
sum_value = 0
count = 0
num = 0
while True:
    num += 1
    sum_value += num
    if sum_value > S:
        break
    count += 1
print(count)