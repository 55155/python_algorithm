N = int(input())
l = list(map(int, input().split()))
s, ss = map(int, input().split())
count = 0
for i in range(N):
    l[i] -= s
    count += 1
    if l[i] > 0:
        if l[i] % ss == 0: # 나누어 떨어지면 
            count += l[i] // ss
        else:
            count += l[i] // ss + 1

print(count)