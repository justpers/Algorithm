from collections import deque

n, k = map(int, input().split())

graph = []
virus = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0: # 바이러스가 있으면?
            virus.append((graph[i][j], 0, i, j))

virus.sort()

s, x, y = map(int, input().split()) # s초 뒤에 (x, y)에 존재하는 바이러스 종류 출력
# 위치라 인덱스로 바꾸려면 1씩 빼줘야 함 

# 퍼져나갈 수 있는 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
q = deque(virus)

while q:
    now_virus, time, now_x, now_y = q.popleft()
    if time == s:
        break
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = now_virus
                q.append((virus, time + 1, nx, ny))
                
print(graph[x-1][y-1])  