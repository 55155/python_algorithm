import sys
input = sys.stdin.readline

l = list(map(int, input().strip()))

if sum(l[:len(l)//2]) == sum(l[len(l)//2:]):
    print("LUCKY")
else:
    print("READY")
# 길이가 6일 때 0 1 2