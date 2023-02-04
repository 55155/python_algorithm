num = int(input())
l = list(map(int, input().split()))
l.sort()
step = 0 # 몇칸씩 뛸 수 있는지.
count = 0
pre_step = 0
while step < num:
    step += l[step]
    if len(l[pre_step:step]) >= max(l[pre_step:step]):
        count += 1
        pre_step = step
print(count)

# 솔루션
count = 0
result = 0
for i in l:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(count)