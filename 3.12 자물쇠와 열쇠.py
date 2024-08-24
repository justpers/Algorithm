def rotation(key):
    m = len(key[0])
    rot_arr = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            rot_arr[i][j] = key[m-j-1][i]
    return rot_arr

def check(new_lock, n):
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if new_lock[i][j] != 1:
                return False
    return True
 
def solution(key, lock):
    
    m = len(key[0])
    n = len(lock[0])
    
    # 수월하게 탐색하기 위해 lock 크기 3배로 늘리고 0으로 채우기
    new_lock = [[0] * (n * 3) for _ in range(n*3)]
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            new_lock[i][j] = lock[i-n][j-n]
            
    for _ in range(4):
        key = rotation(key) # 오른쪽으로 90도
        for row in range(n*3 - n +1):
            for col in range(n*3-n+1):
                for i in range(m):
                    for j in range(m):
                        new_lock[row + i][col + j] += key[i][j]
                
                if check(new_lock, n):
                    return True
                
                for i in range(m):
                    for j in range(m):
                        new_lock[row + i][col + j] -= key[i][j]

    return False