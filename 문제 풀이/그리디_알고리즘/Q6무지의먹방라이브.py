import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    pre_time = 0
    sum_time = 0
    leave_food = len(food_times)

    while sum_time + ((q[0][0] - pre_time) * leave_food) <= k: # 해당 층이 삭제하면 안될 때
        now = heapq.heappop(q)[0]
        sum_time += (now - pre_time) * leave_food
        leave_food -= 1
        pre_time = now

    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_time)][1]

solution([3,1,2],5)

