def vsota_vrste():
    k = 0
    l = 1
    while l < 1001:
        k += l ** l
        l += 1
    return k and k % 10 ** 10

print(vsota_vrste())