n = int(input())
lst = list(map(int, input().split()))

lst.sort()
count = 0
result = 0

for i in lst:
    count += 1
    if count >= i:
        result += 1
        count = 0
  
print(result)
