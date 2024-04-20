case = int(input())
l = []
for i in range(case):
    l.append(int(input()))
l.sort()
max_weight = 0
for i in range(case):
    weight = ( case - i ) * l[i]
    max_weight = max(max_weight, weight)

print(max_weight)