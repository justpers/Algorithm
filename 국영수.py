n = int(input())
lst = []
for _ in range(n):
    data = input().split()
    lst.append((data[0], int(data[1]), int(data[2]), int(data[3])))

lst = sorted(lst, key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in lst:
    print(i[0])