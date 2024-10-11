def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


t = int(input())

for _ in range(0, t):
    n = int(input())
    print(Fibonacci(n))