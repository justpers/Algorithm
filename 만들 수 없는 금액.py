n = int(input())
token = list(map(int, input().split()))
token.sort()

target = 1
for i in token:
    if target < i:
        break
    target += i
    
print(target)