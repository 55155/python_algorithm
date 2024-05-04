# https://blog.encrypted.gg/1062
# 좋은 아이디어. 
# 입력부
R, C = map(int, input().split())
visited = [False for i in range(27)]
board = []
for i in range(R):
    temp = input()
    board.append(temp)
# 상하좌우
drow = [-1,1,0,0]
dcol = [0,0,-1,1]
def rule(row,col):
    if row < 0 or row >= R:
        return False
    if col < 0 or col >= C:
        return False
    return True
result_list = []
break_flag = False
count = 0 
l=[]
def DFS(row,col,depth):
    global result_list, break_flag, count, visited
    if break_flag: # 종료
        
        result_list.append(depth)
        count = 0
        return
    else:
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            
            if rule(nrow, ncol):
                alpha = ord(board[nrow][ncol]) - 65
                if visited[alpha] == False:
                    count = 0
                    visited[alpha] = True
                    DFS(nrow, ncol, depth + 1)
                    visited[alpha] = False
                else:
                    count += 1
                    if count == 4:
                        break_flag = True
                        # backtracking 시에 항상 제자리로 돌려놓기
                        DFS(row, col, depth)
                        break_flag = False

            else:
                count += 1
                if count == 4:
                    break_flag = True
                    DFS(row, col, depth)
                    break_flag = False

init_alpha = ord(board[0][0]) - 65
visited[init_alpha] = True
DFS(0,0,1)
print(max(result_list))