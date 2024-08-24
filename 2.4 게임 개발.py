n, m = map(int, input().split())
a, b, d = map(int, input().split())
# d - 0:북, 1: 동, 2: 남, 3:서

board = []
# 0: 육지, 1: 바다

for i in range(n):
    board.append(list(map(int, input().split())))
    
v = [[0] * m for _ in range(n)] # 방문 위치 저장할 맵
v[a][b] = 1

da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

count = 1
turn_time = 0
while True:
    turn_left()
    na = a + da[d]
    nb = b + db[d]
    
    if v[na][nb] == 0 and board[na][nb] == 0:
        v[na][nb] = 1
        a = na
        b = nb
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
        
    if turn_time == 4:
        na = a - da[d]
        nb = b - db[d]
        if board[na][nb] == 0:
            a = na
            b = nb
            turn_time = 0
        else:
            break
print(count)