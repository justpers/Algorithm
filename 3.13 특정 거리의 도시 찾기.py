from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    row, col = map(int, input().split())
    graph[row].append(col)
    
distance = [-1] * (n+1)
distance[x] = 0

q = deque()
q.append(x)

while q:
    pos = q.popleft()
    for i in graph[pos]:  # 현재 노드에서 갈 수 있는 노드가 i로..
        if distance[i] == -1:
            distance[i] = distance[pos] + 1
            q.append(i)
            
minimum = 0
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        minimum = 1
        
if minimum == 0:
    print(-1)