def vsota_kvadratov(n):
    sestevek = 0    
    for i in range(1, n + 1):
        sestevek += i ** 2
    return sestevek

def kvadrat_vsote(n): 
    sestevek = 0
    for i in range(1, n + 1):
        sestevek += i
    return sestevek ** 2

def razlika(n):
    return kvadrat_vsote(n) - vsota_kvadratov(n)


print(razlika(100))