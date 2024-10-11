def Hanoi(n, a, c, b, rod, result, last_top):
    """
    n개의 디스크를 a 기둥에서 c 기둥으로 옮기는 함수 (재귀 호출).
    b 기둥은 보조 기둥으로 사용됨.
    
    매번 3번 기둥에 있는 디스크의 상태가 변할 때마다 그 위에 있는 디스크 번호를 출력함.
    
    매개변수:
    n: 옮겨야 할 디스크의 수
    a: 출발 기둥 번호 (1, 2, 3 중 하나)
    c: 도착 기둥 번호 (1, 2, 3 중 하나)
    b: 보조 기둥 번호 (1, 2, 3 중 하나)
    rod: 각 기둥에 있는 디스크를 나타내는 딕셔너리 {1: 기둥1 디스크 리스트, 2: 기둥2, 3: 기둥3}
    result: 출력해야 할 디스크 번호가 저장될 리스트
    last_top: 이전에 출력한 3번 기둥의 최상위 디스크 번호 (중복 방지용)
    
    반환값:
    last_top: 현재 3번 기둥의 최상위 디스크 번호 (재귀 호출 간 상태 유지)
    """
    if n == 1:
        # 기본 경우: 가장 작은 디스크 하나를 출발지(a)에서 도착지(c)로 옮김
        rod[c].append(rod[a].pop())  # a 기둥에서 디스크를 빼서 c 기둥에 넣음
        
        # 출발지(a)나 도착지(c)가 3번 기둥이면 상태 변화를 출력
        if a == 3 or c == 3:
            last_top = print_top_of_rod(rod[3], result, last_top)
        return last_top

    # n-1개의 디스크를 a 기둥에서 b 기둥으로 옮김 (c 기둥을 보조로 사용)
    last_top = Hanoi(n - 1, a, b, c, rod, result, last_top)

    # 남은 1개의 디스크를 a에서 c로 옮김
    rod[c].append(rod[a].pop())
    
    # 출발지(a)나 도착지(c)가 3번 기둥이면 상태 변화를 출력
    if a == 3 or c == 3:
        last_top = print_top_of_rod(rod[3], result, last_top)

    # n-1개의 디스크를 b 기둥에서 c 기둥으로 옮김 (a 기둥을 보조로 사용)
    last_top = Hanoi(n - 1, b, c, a, rod, result, last_top)
    
    return last_top

def print_top_of_rod(rod, result, last_top):
    """
    3번 기둥의 최상위 디스크를 출력함.
    이전에 출력된 디스크와 다를 경우에만 출력.
    
    매개변수:
    rod: 3번 기둥의 디스크 리스트
    result: 출력해야 할 디스크 번호가 저장될 리스트
    last_top: 이전에 출력된 3번 기둥의 최상위 디스크 번호
    
    반환값:
    last_top: 현재 3번 기둥의 최상위 디스크 번호 (변경된 경우)
    """
    if rod:  # 3번 기둥에 디스크가 있으면 최상위 디스크 번호 저장
        current_top = rod[-1]
    else:  # 3번 기둥에 디스크가 없으면 0을 저장
        current_top = 0
    
    # 현재 최상위 디스크가 이전과 다를 경우에만 출력
    if current_top != last_top:
        result.append(current_top)  # 변경된 최상위 디스크를 출력 리스트에 추가
        last_top = current_top  # 새로운 최상위 디스크로 갱신
    
    return last_top

# 테스트 케이스 입력 처리
t = int(input())  # 테스트 케이스 수 입력
for _ in range(t):
    n = int(input())  # 디스크 개수 입력
    
    # rod는 각 기둥의 상태를 저장하는 딕셔너리. 1번 기둥에 n개의 디스크가 쌓여있음.
    rod = {1: list(range(n, 0, -1)), 2: [], 3: []}
    
    result = []  # 최상위 디스크 번호를 저장할 리스트

    last_top = -1  # 3번 기둥의 직전 최상위 디스크 번호 (초기값 -1)
    
    # 하노이 함수 호출
    last_top = Hanoi(n, 1, 3, 2, rod, result, last_top)

    # 결과 출력 (결과값 사이에 공백을 추가)
    print(' '.join(map(str, result)))

