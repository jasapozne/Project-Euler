abeceda = {'A' : 1,'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}

def sez_imen(dat1):
    with open(dat1, "r", encoding="utf-8") as dat:
        imena = dat.read().replace("'","")
        imena1 = imena.split(",")
    imena1.sort()
    return imena1

print(sez_imen("names.txt"))
print(len(sez_imen("names.txt"))) 

def prestejmo_vse(dat):
    sez_zmnozkov = []
    for ime in sez_imen(dat):
        k = 0
        for crka in ime:
            if crka == "'" or crka == '"':
                pass
            else:
                k += abeceda[crka]
        sez_zmnozkov.append(k * (sez_imen(dat).index(ime) + 1))
    return sum(sez_zmnozkov)

print(prestejmo_vse("names.txt"))
            
         