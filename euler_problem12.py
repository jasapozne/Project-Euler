def trikotniska_stevila(n):
    return sum ([ i for i in range(1, n + 1) ])

j = 0
n = 0
stevilo_deliteljev = 0
while stevilo_deliteljev <= 500:
    stevilo_deliteljev = 0
    j += 1
    n = trikotniska_stevila(j)
    i = 1
    while i <= n ** 0.5:
        if n % i == 0:
            stevilo_deliteljev += 1
        i += 1
    stevilo_deliteljev *= 2
    
print(n)