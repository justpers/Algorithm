t = int(input())
n, m = map(int, input().split()) # 금광 크기
gold_lst = list(map(int, input().split())) # 금 개수
gold_map = []
index = 0
for i in range(n):
    gold_map.append(gold_lst[index:index+m])
    index += m

# 왼쪽으로는 다시 돌아갈 수 없음 -> 1번째 행에서의 선택 먼저 고려
for i in range(1, m):
    for j in range(n):
        if i == n - 1:
            left_down = 0
        else:
            left_down = gold_map[i+1][j-1]
            
        left_str = gold_map[i][j-1]
        
        if j == 0:
            left_up = 0
        else:
            left_up = gold_map[i-1][j-1]

        gold_map[i][j] = gold_map[i][j] + max(left_down, left_str, left_up)

max_value = 0
for i in range(n):
    max_value = max(max_value, gold_map[i][m-1])
print(max_value)