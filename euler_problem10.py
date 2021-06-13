#stara funkcija
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

def vsota_prastevil_manjsih_od_n(n):   
    sestevek = 0
    for i in range(1, n + 1): 
        if ali_je_prastevilo(i):  
            sestevek += i        
    return sestevek

print(vsota_prastevil_manjsih_od_n(2000000))