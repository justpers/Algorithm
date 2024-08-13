n, m = map(int, input().split())
length = list(map(int, input().split()))

# 제일 길이가 긴 떡의 시작점과 끝점으로 이진탐색 하기
start = 0
end = max(length)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for i in length:
        if i > mid:
            total += (i - mid)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)