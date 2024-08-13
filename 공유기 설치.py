def binary_search(array, count, start, end):
    result = []
    while start <= end:
        mid = (start + end) // 2
        if count >= 1:
            result.append(array[mid])
            count -= 1
            
            if array[end] - array[mid] > array[mid] - array[start]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            return result
    return result

n, c = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

array.sort()
if c == 2:
    print(array[-1] - array[0])
else:
    result_lst = binary_search(array, c-2, 0, n - 1)
    result_lst.append(array[0])
    result_lst.append(array[-1])
    
    result_lst.sort()

    min_value = result_lst[1] - result_lst[0]
    for i in range(len(result_lst) - 1):
        for j in range(i+1, len(result_lst) - 1):
            if result_lst[j] - result_lst[i] < min_value:
                min_value = result_lst[j] - result_lst[i]
    
    print(min_value)