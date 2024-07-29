n = int(input())
token = list(map(int, input().split()))
token.sort()

int_lst = []

for i in range(n):
    if int_lst[token[i]-1] != token[i]:
        int_lst.insert(token[i]-1, token[i])
    for j in range(i+1, n):
        num = token[i] + token[j]
        if int_lst[num-1] != num:
            int_lst.insert(num-1, num)

# 이렇게 생각해봤지만, 그러면 int_lst 크기를 어느 정도로 설정해야할 지 알 수 없었음