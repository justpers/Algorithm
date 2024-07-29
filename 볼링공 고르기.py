n, m = map(int, input().split())
weight = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i+1, n):
        if weight[i] != weight[j]:
            count += 1
print(count)



# 조합하고 무게 같게 고를 경우 빼기

# 1 2 2 3 3
# 무게 같을 땐 패스하고 다르면 count+1