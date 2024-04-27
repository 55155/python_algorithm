case = int(input())
result_list = [1 for i in range(31)]
result = 1
for i in range(1, 31):
    result *= i
    result_list[i] = result 
for i in range(case):
    W,E = map(int,input().split())
    print(int(result_list[E] / (result_list[W] * result_list[E-W])))