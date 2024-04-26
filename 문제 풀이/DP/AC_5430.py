def command_exert(l:list,command):
    if command == 'R':
        l.reverse()
    elif command == 'D':
        if l:
            l.pop(0)
        else:
            return "error"
    return l

case = int(input())
l = []
import copy
from collections import deque
for i in range(case):
    command = input()
    length = int(input())
    list_temp = input()
    l = []
    num_temp = ''
    flag = True
    for i in range(len(list_temp)):
        if list_temp[i] == '[':
            pass
        elif list_temp[i] == ',' or list_temp[i] == ']' and num_temp:
            l.append(int(num_temp))
            num_temp = ''
        else:
            num_temp += list_temp[i]
    q = deque(l)
    rev = 0
    l_copy = copy.deepcopy(l)
    for c in command:
        if c == 'R':
            rev += 1
        elif c == 'D':
            if q:
                if rev % 2 == 0:
                    q.popfront()
                else:
                    q.pop()
            else:
                flag = False
                print('error')
                break
        # l_copy = command_exert(l_copy, c)
        # if l_copy == "error":
        #     break
    if flag:
        print('[',end = '')
        if rev % 2 == 0:
            pass
        else:
            q.reverse()
        for i in range(len(q)):
            if i != len(q)-1:
                print(q[i], end = '')
                print(',',end = '')
            else:
                print(q[i], end='')
        print(']')