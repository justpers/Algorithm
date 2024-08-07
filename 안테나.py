# 안테나 길이가 최소가 되려면 중간 위치에 설치하는 것이 중요함
# 집이 짝수라 중간이 없다면 중간보다 왼쪽에 있는거 고르기

n = int(input())
position = list(map(int, input().split()))

position.sort()
if n % 2 == 0:
    minimum = position[n//2 - 1]
else:
    minimum = position[n//2]
    
print(minimum)
