# n, m = map(int, input().split())
# weight = list(map(int, input().split()))

# count = 0

# for i in range(n):
#     for j in range(i+1, n):
#         if weight[i] != weight[j]:
#             count += 1
# print(count)


n, m = map(int, input().split())
weight = list(map(int, input().split()))

lst = [0] * 11
for i in weight:
    lst[i] += 1
result = 0
for i in range(1, m+1):
    n -= lst[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += lst[i] * n # B가 선택하는 경우의 수와 곱하기