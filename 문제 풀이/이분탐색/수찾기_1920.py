N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))

def binary_search(num):
    global A
    start = 0 
    end = len(A)-1

    while end >= start:
        mid = (start + end) // 2
        if A[mid] > num:
            end = mid - 1
        elif A[mid] < num:
            start = mid + 1
        elif A[mid] == num:
            return 1
    return 0
for search_num in B:
    print(binary_search(search_num))