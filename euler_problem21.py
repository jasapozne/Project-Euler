def delitelji(n):
    sez = []
    k = 1
    while k < n:
        if n % k == 0:
            sez.append(k)
        k += 1
    return sez

 

def vsota_deljiteljev(n):
    return sum(delitelji(n))

def ali_je_prijateljsko_stevilo(n):
    vsota_n = vsota_deljiteljev(n)
    if vsota_deljiteljev(vsota_n) == n and vsota_deljiteljev(n) == vsota_n and vsota_n != n:
        return True
    else:
        return False
    
def vsota_prijateljskih_stevil_do_10000():
    sestevek = 0
    k = 0
    while k < 10000:
        k += 1
        if ali_je_prijateljsko_stevilo(k):
            sestevek += k
    return sestevek

print(vsota_prijateljskih_stevil_do_10000())
