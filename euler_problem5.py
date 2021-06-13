def deljivo(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True


#zacnemo z 2520, saj je to najmanjše število da, deli 1:10
n = 2520
while True:
    if deljivo(n):
        break
    n += 1

print(n)