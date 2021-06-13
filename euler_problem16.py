def vsota_stevk(n):
    if n == 0:
        return 0
    else: 
        return n % 10 + vsota_stevk(n // 10)  
print(vsota_stevk(2 ** 1000))