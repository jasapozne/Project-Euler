def ali_je_prastevilo(n):
    if n <= 2:
        return n == 2
    elif n % 2 == 0:
        return False
    else:
        d = 3
        while d ** 2 <= n:
            if n % d == 0:
                return False
            d += 2
        return True


def delitelji(n):
    sez_deliteljev = []
    for i in range(1, int(n ** (1 / 2) + 1)):
        if n % i == 0:
            sez_deliteljev.append(i)
            sez_deliteljev.append( n / i)
    return sez_deliteljev


def najvecje_prastevilo(n):
    delitelj = delitelji(n)
    sez = []
    for i in delitelj:
        if ali_je_prastevilo(i):
            sez.append(i)
    return max(sez)

print(najvecje_prastevilo(600851475143))