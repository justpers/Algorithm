# 실패율: 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
def solution(N, stages):
    answer = []
    
    for i in range(1, N+1):
        not_clear = stages.count(i)
        clear = len(list(filter(lambda x: x >= i, stages)))
        
        if clear == 0:
            per = 0
        else:
            per = not_clear / clear
        
        answer.append((i, per))
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    for i in range(N):
        answer[i] = answer[i][0]
    
    return answer

