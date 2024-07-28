n = int(input())
lst = list(map(int, input().split()))

lst.sort(reverse=True)
count = 0
while True:
    if lst == []:
        break
    elif lst[0] < len(lst):
        del lst[0]
    else:
        num = lst[0]
        del lst[0:num]
        count += 1
  
print(count)