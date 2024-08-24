def first(array, target, start, end):
    if start > end:
        return None
    mid  = (start + end) // 2
    # 첫 번째로 나오는 x일 때만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)

def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 가장 마지막으로 나오는 x일 때만 인덱스 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)

def count_value(array, x):
    n = len(array)
    a = first(array, x, 0, n - 1)
    if a == None:
        return 0
    
    b = last(array, x, 0, n - 1)
    return b - a + 1

n, x = map(int, input().split())
array = list(map(int, input().split()))
# 이진 탐색 2개 써서 인덱스 차이로 계산하기

start = 0
end = n -1

count = count_value(array, x)
if count == 0:
    print(-1)
else:
    print(count)