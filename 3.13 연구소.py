# 해설 참고

# 벽을 3개 설치하는 모든 경우의 수를 다 계산해야함
# 전체 맵 크기가 8*8이므로 벽을 설치할 수 있는 모든 조합의 수는 최대 64 combination 3이다.

n, m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)
                
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
                
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        result = max(result, get_score())
        return result

    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
dfs(0)
print(result)