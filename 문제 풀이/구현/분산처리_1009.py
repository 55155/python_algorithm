N = int(input())
for i in range(N):
    a, b = map(int,input().split())
    result = a%10
    for i in range(1, b):
        result *= a
        result%=10
    print(result if result != 0 else 10)