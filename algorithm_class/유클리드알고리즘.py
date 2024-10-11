def gcd(m, n):
    if n == 0:
        result = m
    else:
        result = gcd(n, m % n)
    return result

t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    
    print(gcd(m, n))