# 그리디 알고리즘
# 에라토테네스의 체
'''
import numpy as np
# 리무브 리스트에 지워야하는 리스트를 담는다
# sosu_list에 지워야하는 수들의 약수인 소수를 담는다. range(1,10000)
# 

# def sosu(list):
    
case = int(input())
for i in range(case):
    num = int(input())
    num_list = [i for i in range(2,num+1)]
    sosu_list = []
    remove_list = []
    for i in range(2, int(num**0.5) + 1):
        for j in range(4,num):
            if i%j != 0:
                remove_list.append(i)
    remove_list = set(remove_list)

    for i in remove_list:
        num_list.remove(i)
print(num_list)
'''
'''
case, won = map(int, input().split())
change_list = []
for i in range(case):
    change_list.append(int(input()))

count = 0
count2 = 0

for i in change_list[::-1]:
    count = 0
    if won >= i:
        count += won // i
        won -= count * i
        count2 += count
    if won == 0:    
        break
print(count2)
'''

'''
def draw_star(n):
    if n == 1:
        return ['*']
    
    star = draw_star(n//3)
    next_star = []

    for i in star:
        next_star.append(i*3)
    for i in star:
        next_star.append(i + ' '*(n//3) + i)
    for i in star:
        next_star.append(i*3)
    return next_star
n = int(input())
star = draw_star(n)
for i in star:
    print(i)
'''
'''
def recur(string, start, end):
    global count
    count += 1
    if start >= end:
        return 1
    elif string[end] != string[start]:
        return 0
    else:
        return recur(string, start+1, end -1)

def isPalindrome(string):
    return recur(string,0,len(string)-1)

count = 0
case = int(input())
for i in range(case):
    count = 0
    string = input()
    print(isPalindrome(string),count)
'''

# 핵심 : 
# i 는 해당 숫자 
# visit[i] 는 검사해야하는 숫자 

# backtracking

'259가 입력되었을 때 입력될 수 있는 모든 경우의 수'

'decision space'

# Dynamic programming 

# 피보나치 수열
'''
def fib_naive(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        fib = fib_naive(n-1) + fib_naive(n-2)
        return fib

fib_array = [0, 1]
def fib_recur_dp(n):
    if n < len(fib_array):
        return fib_array[n]
    else:
        fib = fib_recur_dp(n-1) + fib_recur_dp(n-2)
        fib_array.append(fib)
        return fib
# call stack overflow

# bottom up
def fib_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib_array = [0,1]
    for  i in range(2,n+1):
        num = fib_array[i - 1] + fib_array[ i - 2 ]
    return fib_array[n]

'''
'''
n,m = map(int, input().split())
answer = []

visited = [False] *(n+1)
def plus(depth, n,m):
    if depth == m: # 1 2
        print(' '.join(map(str, answer)))

    for i in range(1, n+1): # 1 2 3 4
        
        if visited[i] == False:
            visited[i] = True
            answer.append(i)
            plus(depth+1,n,m) 
            visited[i] = False
            answer.pop()
plus(0,n,m)
'''
'''
n,m = map(int,input().split())
# n은 최대 숫자, m은 수열의 길이
visited = [False] * (n+1)
plus(0,n,m)
'''
'''q = int(input())
list_queen = []

def rule(list_queen):
    if list_queen[n] == n:
        
def n_queen(n):
    if n == q:
        return 
    else:
        for i in range(q):
            if list_queen[i] == 
n_queen(0)
'''
'''
list_a = []
n,m = map(int, input().split())
visited = [False] * (n+1)

def issort(l)->bool:
    if l == sorted(l):
        return True
    else:
        return False

def recur(depth):
    global n,m
    if depth == m:
        print(' '.join(map(str, list_a)))
    else:
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                list_a.append(i)
                if issort(list_a):
                    recur(depth+1)
                visited[i] = False
                list_a.pop()
recur(0)
'''
'''
n,m = map(int, input().split())
list_a= []
def recur(depth):
    if depth == m:
        print(' '.join(map(str, list_a)))
    else:
        for i in range(1,n+1):
            list_a.append(i)
            recur(depth+1)
            list_a.pop()
recur(0)
'''
'''
import sys

n,m = map(int, sys.stdin.readline().rstrip().split())
list_a = []

def issort(l:list)->bool:
    if l == sorted(l):
        return True
    else:
        return False

def recur(depth):
    if depth == m:
        print(' '.join(map(str, list_a)))
    else:
        for i in range(1,n+1):
            list_a.append(i)
            if issort(list_a): 
                recur(depth + 1)
            list_a.pop()
recur(0)
'''
import sys
'''
N = int(sys.stdin.readline())
l =[0] * N 
count = 0

def rule(col):
    for c in range(col):
        if l[col] == l[c] or (col-c) == abs(l[col] - l[c]):
            return False 
    return True 
'''
'''
import sys

N = int(sys.stdin.readline())
l =[0] * N 
count = 0

def rule(col):
    for c in range(col):
        if l[col] == l[c] or (col-c) == abs(l[col] - l[c]):
            return False 
    return True 

def n_queen(col):
    global count,N
    if col == N:
        count+=1
    else:
        for row in range(0,N):
            l[col] = row
            if rule(col):
                n_queen(col+1)
n_queen(0)
print(count)
'''
'''
import sys
l = [list(map(int, sys.stdin.readline().split())) for i in range(9)]

board = []
for i in range(9):
    for j in range(9):
        if l[i][j] == 0:
            board.append((i,j))
            
def rule(board):

    row = board[0]
    col = board[1]
    check1 = (row//3) * 3 
    check2 = (col//3) * 3
    
    for i in range(9):
        if (l[row][col] == l[row][i] and col != i) or (l[row][col] == l[i][col] and row != i):
            return False

    for i in range(check1, check1+3):
        for j in range(check2, check2+3):
            if l[row][col] == l[i][j] and (row != i and col != j ):
                return False

    return True

def sdoku(depth): 
    
    if depth == len(board):
        for i in l:
            print(' '.join(map(str, i)))
        exit(0)

    else:
        for i in range(1,10):
            l[board[depth][0]][board[depth][1]] = i
            if rule(board[depth]):
                sdoku(depth + 1)
            l[board[depth][0]][board[depth][1]] = 0


sdoku(0)
'''

'''
for i in range(n):
    if visited[i] == False:
        visitedp[i] = True
        list_a.append(i)
        recur()
        visited[i] = False
        list_a.pop(0)
'''
'''
import sys
case = int(input())

l = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
c = c[0] * '+' + c[1] * '-' + c[2] * '*' + c[3] * '/'
visited = [False] * (len(c))
result = []
def plus(pre, i, depth):
    if depth == 0:
        pre = l[0]
    if i == -3:
        pass
    elif c[i] == "+":
        pre = pre + l[depth]
    elif c[i] == '-':
        pre = pre - l[depth]
    elif c[i] == '/':
        pre = int(pre / l[depth])
    elif c[i] == '*':
        pre = int(pre * l[depth])
    
    if depth == len(l) -1:
        result.append(pre)
    else:
        for i in range(len(c)):
            if visited[i] == False:
                visited[i]=True
                plus(pre, i, depth+1)
                visited[i] = False
plus(0,-3, 0)
print(max(result))
print(min(result))
'''

# 모든 팀이 될 수 있는 경우의 수를 탐색해야한다.
# ex 4명 2 ; 2 --> 13 24 / 12 34 / 14 23
# l[i][j] - l[][]
# [(), ()]
'''
import sys

num = int(input())
l = [list(map(int, sys.stdin.readline().split())) for i in range(num)]
visited = [False] * (num)
k = [0]
team = []
team1 = set()

def issort(n):
    if n == sorted(n):
        return True
    else:
        return False

def recur(depth):

    if depth == num//2 - 1:
        team2 = set([i for i in range(num)])
        team1 = set(k)
        team2 = team2 - team1

        team_1 = sum(l[i][j] for i in team1 for j in team1)
        team_2 = sum(l[i][j] for i in team2 for j in team2)

        team.append(abs(team_1 -  team_2))
        return
   
         
    # 종료 조건    
    else:
        for i in range(1,num): # i = 0 1 2 
            if visited[i] == False:
                visited[i] = True
                k.append(i)
                if issort(k):
                    recur(depth+1)
                visited[i] = False 
                k.pop()

recur(0)      
print(min(team))
'''
'''
count = 0
l = [1,1]
def fib_naive(n):
    if len(l) > n:
        return 1
    else:
        for i in range(2,n):
            l.append(l[i-2] + l[i-1])
    return l[n-1]
a = int(input())
print(fib_naive(a), a-2)
'''

def w(a,b,c):
    if a<= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or  b > 20 or c > 20:
        return w(20,20,20)
    elif a < b and b < c:
        return w(a,b, c-1) + w(a, b -1, c- 1) - w(a,b-1,c)
    else:
        w(a-1, b, c) + w(a-1, b-1,c) + w(a-1, b , c-1) - w(a-1, b-1 ,c-1)

n,m = map(int, input().split())
answer = []

visited = [False] *(n+1)
def plus(depth, n,m):
    if depth == m: # 1 2
        print(' '.join(map(str, answer)))
        
    for i in range(1, n+1): # 1 2 3 4
        
        if len(answer) == 0 or answer[-1] < i:
            answer.append(i)
            plus(depth+1,n,m)
            answer.pop()
            
plus(0,n,m)