# 순차탐색

def sequential_search(n, target, array): # 배열이 이미 정렬 되어있는 경우에 사용가능
    for i in range(n):
        if array[i] == target:
            return i+1

def binary_search(array, target, start, end):
    if start> end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:      
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)

def binary_search(array, target, start, end):
    while True:
        mid = (start + end) // 2
        if array[mid] == array[target]:
            return mid
        elif array[mid] < target:
            end = mid - 1
        elif array[mid] > array[target]:
            start = mid + 1
    return None

import sys

# test case

'''
5
8 3 7 9 2
3
5 7 9
'''

def sequential_search(array:list, target):
    for i in array:
        if i == target:
            return 'yes'
    return 'no'

N = int(input())
N_list = list(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

for i in M_list:
    print(sequential_search(N_list,i), end = ' ')

# binary_search

def binary_search(array, target, start, end):

    while True:
        mid = (start + end) // 2
        if start > end:
            return 'no'
        if array[mid] == target:
            return 'yes'
        elif array[mid] < target:
            start = mid+1
        else:
            end = mid - 1

def quick_sort(array):

    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(N_list)
A = quick_sort(N_list)
print(A)
for i in M_list:
    print(binary_search(A, i, 0, len(A) - 1), end = ' ')

# 떡볶이 만들기


# 순차탐색으로는 굉장히 오랜시간이 걸린다. 
# 이진 탐색을 사용하고 싶다
# 해당 높이로 절단했을 때 나올 수 있는 리스트를 정리
# (4,0,0,2)
# (10, 15, 17, 19)
# 
def binary_cut(array,target, start, end):
    mid = (start + end) // 2 # 인덱스 
    # l = [(i - array[mid]) for i in array if (i - array[mid]) > 0 else]
    l = []
    for i in array:
        if (i - array[mid]) < 0:
            l.append(0)
        else:
            l.append(i - array[mid])
    # 어떤 이진분류를 해야할까
    # 기준점이 있어야한다.    (sum(list)- M) // N = mid(1) --> 다 자른 것의 합 sum_
    # 이 기준점으로 잘랐을 때 sum_ < target: # mid 를 줄여야해
    # end = mid
    # index를 자르는게 아니라 value를 잘라야해
# 1 5 
# 20 
# 15
def binary_cut(array, target, start, end):
    mid = (start - end) // N
    if mid <= 0:
        return mid
    result = 0
    for i in array:
        if (i - mid) <= 0:
            pass
        else:
            result += ( i - mid )
    
    if result == target:
        return mid
    elif result < target: # 많이 짤라야함 mid 줄여야해
        return binary_cut(array, target, start, mid-1)
    else:
        return binary_cut(array, target, mid+1, end)

N, M = map(int, input().split())
l = list(map(int, input().split()))

start = 0
end = max(l)

while start <= end:
    result = 0
    mid = (start + end) // 2
    for i in range(len(l)):
        if i > mid:
            result += (i - mid)
    if result == M:
        break 
    elif result < M: # 더 잘라야하는 경우
        start = mid + 1
    else: # 덜 잘라야하는 경우
        height = mid
        end = mid - 1
print(height)
        

result = 0
while start <= end:
    result = 0
    mid = (start + end) // 2 # mid 정의
    for i in l:
        if i > mid:
            result += (i - mid)
    
    if result == M:
        break
    elif result < M: # 너무 많이 자른 경우
        end = mid - 1
    else:
        start = mid + 1

