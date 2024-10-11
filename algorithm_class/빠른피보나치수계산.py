# 행렬의 거듭제곱을 사용해 피보나치 수열의 n번째 항을 효율적으로 계산하기
# 분할 정복과 행렬 곱셈 이용

def matrix_mult(A, B, mod):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]
    ]

def matrix_pow(M, n, mod):
    result = [[1, 0], [0, 1]] 
    base = M
    
    while n > 0:
        if n % 2 == 1:
            result = matrix_mult(result, base, mod)
        base = matrix_mult(base, base, mod)
        n //= 2
    
    return result

# 주어진 행렬 M을 n번 거듭제곱하여 반환
# n이 홀수면, 현재 result에 base를 곱해 업데이트
# base는 계속해서 자기 자신을 곱해 나가고, n을 2로 나누어 감소시킴

def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, n - 1, 1000)
    
    return result[0][0]

t = int(input())
for _ in range(t):
    n = int(input())
    print(Fibonacci(n))
