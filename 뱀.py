n = int(input()) # 보드 크기
k = int(input()) # 사과 개수

board = [[0] * n for _ in range(n)]

# 사과 위치 보드에 표시
for i in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1   # 인덱스로 변환 위해 1씩 뺌

l = int(input())  # 뱀의 방향 변환 횟수
direct = []
for i in range(l):
    direct.append(list(input().split()))

row = 0
col = 0
time = 1 #뱀이 (0, 0) 위치에 있을 때는 이미 1초가 지난 시점

# 동남서북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
look = 0 # 뱀이 초기에 바라보고 있는 방향: 동쪽

while True:
    time += 1
    if int(direct[0][0]) == time:
        if direct[0][1] == 'D':
            look = (look + 1) % 4
        else:
            look = (look - 1) % 4
            
    row += dx[look]
    col += dy[look]
    if row < 0 or row >= n or col < 0 or col >= n:
        break          

print(time)