def pitagora(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False 

def najdi_vsoto():
    a = 3 
    b = 4
    c = 5
    for c in range(1000):
        for b in range(c):
            for a in range(b):
                if a + b + c == 1000:
                    if pitagora(a, b, c):
                        print(a * b * c)
najdi_vsoto()
