N,S = map(int, input().split())
l = list(map(int, input().split()))

start = 0
end = 0 # 
result = l[end] # 구간합
count = 1e6 # 결과
while start <= end:
    if result >= S:
        # 그 시점에서의 end와 start를 기록 
        count = min(count, end - start + 1)
        result -= l[start]
        start += 1
    else:
        if end+1 < N:
            end += 1
        else:
            break
        result += l[end]

print(count if count != 1e6 else 0)