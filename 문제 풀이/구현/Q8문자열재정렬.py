# 알파벳 0 ~ 9로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

string = list(map(str, input().strip()))
string1 = []
result = 0

for i in range(len(string)):
    try:
        result += int(string[i])
    except:
        string1 += string[i]
print(string1+str(result))