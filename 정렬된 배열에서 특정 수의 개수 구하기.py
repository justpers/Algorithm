n, x = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = n -1
result = -1

while start <= end:
    mid =  (start + end) // 2
    
    if array[mid] == x:
        result = mid
        break
    elif array[mid] > x:
        end = mid - 1
    else:
        start = mid + 1
    
if result == -1:
    print(-1)
else:
    
    count = 1 
    i = result
    while True:
        i += 1
        if array[i] == x:
            count += 1
        else:
            break
    i = result
    while True:
        i -= 1
        if array[i] == x:
            count += 1
        else:
            break

    print(count)