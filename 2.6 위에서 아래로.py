n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
    
array = sorted(lst, reverse=True)
for i in array:
    print(i, end=' ')