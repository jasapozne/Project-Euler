def stevke(n):
    sez = []
    for stevka in str(n):
        sez.append(int(stevka))
    return sez


def stevila_na_peto_potenco(l):
    sez_ustreznih_stevil = []
    k = 2
    while k < 10 ** l:
        sez = []
        for i in range(len(str(k))):
            sez.append(stevke(k)[i] ** 5)
        if sum(sez) == k:
            sez_ustreznih_stevil.append(k)
        k += 1
    return sum(sez_ustreznih_stevil)

print(stevila_na_peto_potenco(5))
print(stevila_na_peto_potenco(6))
print(stevila_na_peto_potenco(7))
print(stevila_na_peto_potenco(8))
#vidimo, da je za int(l) > 5 vsota vseh števil enaka, kar pomeni da je to tudi končna skupna vsota teh števil