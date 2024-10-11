import sys
sys.setrecursionlimit(10**7)

def Factorial(n):
    if n == 0:
        return 1
    result = n * Factorial(n-1)
    while result % 10 == 0:
        result //= 10
    
    return result % 100000
    
t = int(input())
for _ in range(t):
    n = int(input())
    fac = Factorial(n)
    
    print(fac % 1000)