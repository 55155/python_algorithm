# 투포인터 알고리즘
# 예제 문제 : 특정한 합을 가지는 부분 연속 수열 찾기

# 시작점과 끝점이 첫번째 원소의 인덱스를 가리키도록한다. 
# 현재 부분 합이 M과 같다면 카운트한다. 
# 현재 부분 합이 M과 작다면 end를 1증가시킨다.
# 현재 부분합이 M보다 크거나 같다면 start를 1 증가 시킨다. 
# 모든 경우를 확인할 때까지 2-4 번 과정을 반복한다. 
# O(N) 이다. 
n = 5 # 데이터의 개수 N
m = 5 # 찾고자하는 부분합 M
 
count = 0
interval_sum = 0
end = 0
data = [] # rand 로 설정 
# start를 차례대로 증가시키며 반복
for start in range(n):
    # end만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]
 
print(count)