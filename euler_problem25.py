def fibonacci(n):
    a = 0
    b = 1
    while a <= n:
        a, b = b, a + b
    return a

def fibonacci_1000_stevk():
    k = 11
    while True:
        k += 1
        fib = fibonacci(k)
        if len(str(fib)) > 999:
            break
    return k 

print(fibonacci_1000_stevk())