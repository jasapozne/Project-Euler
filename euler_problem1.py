def vsota_vec_3_in_5(n):
    vsota = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            vsota += i
    return vsota

print(vsota_vec_3_in_5(1000))