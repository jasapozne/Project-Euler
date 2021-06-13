def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1   
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_1000_stevk():
    k = 11
    while True:
        k += 1
        fib = fibonacci(k)
        if len(str(fib)) > 999:
            break
    return k 

print(fibonacci_1000_stevk())