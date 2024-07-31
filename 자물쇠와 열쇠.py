def rotation(key):
    m = len(key[0])
    rot_arr = [[0] * m] * m
    for i in range(m):
        for j in range(m):
            rot_arr[i][j] = key[m-j-1][i]
    return rot_arr
    
def solution(key, lock):
    
    m = len(key[0])
    n = len(lock[0])
    
    # 수월하게 탐색하기 위해 lock 크기 3배로 늘리고 0으로 채우기
    new_lock = [[0] * n * 3] * n * 3
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            new_lock[i][j] = lock[i-n][j-n]
            
    for _ in range(4):
        key = rotation(key) # 오른쪽으로 90도
        for col in range(n*3 - n +1):
            for row in range(n*3-n+1):
                for i in range(m):
                    for j in range(m):
                        new_lock[col + i][row + j] += key[i][j]
                
                for i in range(n, n*2):
                    for j in range(n, n*2):
                        if new_lock[i][j] == 1:
                            return True
                for i in range(m):
                    for j in range(m):
                        new_lock[col + i][row + j] -= key[i][j]

    return False

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0], [1,0,1]]
solution(key, lock)