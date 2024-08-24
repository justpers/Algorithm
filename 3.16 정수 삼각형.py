n = int(input()) # 삼각형 크기
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            left_up = 0
        else:
            left_up = tri[i-1][j-1]
        
        if j == i:
            right_up = 0
        else:
            right_up = tri[i-1][j]
        
        tri[i][j] += max(left_up, right_up)

print(max(tri[n-1]))