#stara funkcija napisana že v problemu 3
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

def prastevilo(n):
    i = 1
    kandidat = 2
    while i < n:
        kandidat += 1
        if ali_je_prastevilo(kandidat):
            i += 1
    return kandidat


print(prastevilo(10001))