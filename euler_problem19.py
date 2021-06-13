def prestopno_leto(leto):
    if leto % 4 == 0: #to bo zadostovalo, saj 1900 ne bo na tem intervalu, 2000 pa je prestopno leto
        return True
    else:
        return False

dnevi = ["pon","tor","sre","cet","pet","sob","ned"]
vsi_dnevi = dnevi * 5218
vsi_dnevi_v_letu = vsi_dnevi[:len(vsi_dnevi)-1]
#1901 se začne v torek

def stevilo_dni_v_stoletju():
    leto= 1901
    k = 365
    dnevi = 0
    while leto < 2001:
        if prestopno_leto(leto):
            dnevi += k + 1
            leto += 1
        else:
            dnevi += k
            leto += 1
    return dnevi
        
print(stevilo_dni_v_stoletju())
36525

def dnevi_v_letih():
    sep = april = junij = nov = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    jan = mar = maj = julij = avg = okt = dec = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    feb1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
    feb2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    #še bolkše bi to bilo zapisati z zanko in range!
    leto = 1901
    sez = []
    while leto < 2001:
        sez.extend(jan)
        if prestopno_leto(leto):
            sez.extend(feb2)
        else:
            sez.extend(feb1)
        sez.extend(mar)
        sez.extend(april)
        sez.extend(maj)
        sez.extend(junij)
        sez.extend(julij)
        sez.extend(avg)
        sez.extend(sep)
        sez.extend(okt)
        sez.extend(nov)
        sez.extend(dec)
        leto += 1
    return sez


def koliko():
    kolicina = 0
    for dan in zip(dnevi_v_letih(),vsi_dnevi_v_letu):
        if dan == (1,"pon"):
            kolicina += 1
    return kolicina

print(koliko())