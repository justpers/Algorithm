n, m = map(int, input().split())
length = list(map(int, input().split()))
length.sort()

# 이진탐색하면서, 중간점을 절단기 높이로 설정했을 때
# 손님 요청보다 떡이 부족하면 중간점을 왼쪽으로, 반대면 오른족으로 옮기기

# 10 15 17 19
def length_binary_search(array, target, start, end):
    result = 0
    mid = (start + end) // 2
    for i in range(mid, end):
        result += (array[i] - array[mid])
    
    if result == target:
        return mid
    elif result < target:
        return length_binary_search(array, target, start, mid - 1)
    else:
        return length_binary_search(array, target, mid + 1, end)
        

length_binary_search(length, m, 0, n - 1)