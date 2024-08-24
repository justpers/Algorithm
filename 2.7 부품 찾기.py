def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n = int(input())
num_list = list(map(int, input().split()))
# 이진 탐색 하기 위해 미리 정렬
num_list.sort()

m = int(input())
request = list(map(int, input().split()))

for i in request:
    result = binary_search(num_list, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')