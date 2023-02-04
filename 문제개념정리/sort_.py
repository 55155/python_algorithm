# 선택 정렬

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_idx = i
    for j in range(i, len(array)): # i ~ 끝까지 돌려야댐
        if array[min_idx] > array[j]:
            min_idx = j
    # 뒤에 있는 것중 제일 작은 수 발견
    array[min_idx], array[i] = array[i], array[min_idx]

print(array) # O(N^2)


# 삽입 정렬

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(array)): # 0번 idx
    for j in range(i,0,-1): # 왼쪽 index는 이미 정렬되어 있는 상태이다.
        if array[j] < array[j-1]: # swap 이 아니라 insertion
            # 만약 현재 있는게 더 작다면
           array[j], array[j-1] = array[j-1], array[j]
        else: # 만약 왼쪽에 있는 것보다 자기가 크면 굳이 정렬하지 않아도 된다. 왜냐하면 
            # 왼쪽 배열은 이미 정렬이되어있는 상태이기 때문
            break

# 퀵 정렬

# 5 7 9 0 3 1 6 2 4 8
# pivot = 5
# split = len(array) // 2
# 0, split --> 자신보다 큰수
# split, len(array) --> 자신보다 작은수
# swap
# 5 4 9 0 3 1 6 2 7 8
# 5 4 9 0 3 1 6 2 7 8
# 5 4 2 0 3 1 6 9 7 8 
# 1 4 2 0 3 5 6 9 7 8
# 엇갈렸을 때 자기 자신과 바꾸면 자신이 중심이 된다.
# 만약 9 7 8 인 경우 range를 넘어간다 엇갈리게 설계 ## swap(pivot, right)
# 만약 5 6 7 인 경우 right = 1 , left = 1 어짜피 스왑이 안된다.

# --> ()


# 자신보다 작은 것이 엇갈릴 때 l[pivot] > l[right] and right < split : swap
# 핵심 아이디어 : 자신보다 작은 수를 왼쪽에 둔다 
#              자신보다 큰 수를 오른쪽에 둔다
array = [5,7,9,0,3,1,6,2,4,8]
# 첫번째 
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right: # 피봇을 기준으로 엇갈리기 전까지
        # left == right 인 경우는 pivot이 minimum 인 경우
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]: # 첫번째는 제한 조건, 두번째는 멈출 조건
            right -= 1
        
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]
    # 분할 끝
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
quick_sort(array,0, len(array)-1)
print(array)

def quick_sort2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] # 피봇보다 작은 수 담기
    right_side = [x for x in tail if x > pivot] # 피봇보다 큰 수 담기

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# 계수 정렬
# 특정 경우에만 성립 
# 인덱스로 저장하는 경우
# 인덱스로 저장을 하는데 해당 인덱스가 value
# list1 = input, list2[list1[i]]

array = [7,6,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * ( max(array) + 1 )

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')


# 위에서 아래로

case = int(input())
l = []

for i in range(case):
    l.append(int(input()))

# 선택정렬

for i in range(len(l)):
    max_idx = i
    for j in range(i, len(l)):
        if l[i] < l[j]:
            max_idx = j
    l[i], l[max_idx] = l[max_idx], l[i]

for i in l:
    print(i)

# 삽입 정렬

for i in range(1, len(l)):
    for j in range(i, 0, -1):
        if l[j] > l[j-1]: # 앞에 있는 값이 더 작으면 
            l[j], l[j-1] = l[j-1], l[j]
        else:
            break
print(l)

# 성적이 낮은 순서로 학생 출력하기
def rule(l:map):
    return str(l[0]), int(l[1])

score = []
case = int(input())
for i in range(case):
    score.append([rule(input().split())])

a = sorted(score, key = lambda score: score[1])
print(a)