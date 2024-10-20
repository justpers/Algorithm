# 플로이드 워셜 알고리즘 사용
INF = int(1e9)

n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)을 만들고, 모든 값을 무한으로 초기화ㅓ
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비요은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용이 1s
    a, b = map(int, input().split())
    graph[a][b] = 1
    
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
            
# 수행된 결과 출력
for a in range(1, n+1):
    count = 0
    for b in range(1, n+1):
        if graph[a][b] != INF or graph[b][a] != INF:
            count += 1
    if count == n:
        result += 1
print(result)