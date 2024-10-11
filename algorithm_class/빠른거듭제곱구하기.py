# 분할 정복법 사용

def Exponentiation(a, n):
    if n == 0:
        return 1
    half = Exponentiation(a, n//2) % 1000  # a^(n//2)
    
    if n % 2 == 0:
        return (half * half) % 1000  # a^n = (a^(n//2))^2
    else:
        return (half * half * a) % 1000  # a^n = (a^(n//2))^2 * a

t = int(input())
for _ in range(t):
    a, n = map(int, input().split())
    print(Exponentiation(a, n))
    
# 재귀함수는 n을 절반으로 나눠서 계산하므로 O(log n)시간 복잡도를 가짐
# n이 짝수인 경우엔 a^(n//2)의 제곱
# n이 홀수인 경우엔 위에 추가로 a를 곱함