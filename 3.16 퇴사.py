n = int(input())
t_lst = []
p_lst = []
for _ in range(n):
    t, p = map(int, input().split())
    t_lst.append(t)
    p_lst.append(p)

total_pay = [0] * (n + 1)
max_value = 0

for i in range(n - 1, -1, -1):
    time = i + t_lst[i]
    if time <= n:
        total_pay[i] = max(p_lst[i] + total_pay[time], max_value)
        max_value = total_pay[i]
    
    else:
        total_pay[i] = max_value
print(max_value)