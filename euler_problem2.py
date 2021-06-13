def fibbonaci_soda(n):
	vsota = 0  
	x1 = 1  
	x2 = 2   
	while x1 <= n:
		if x1 % 2 == 0:
			vsota += x1
		x1, x2 = x2, x1 + x2
	return vsota
print(fibbonaci_soda(4000000))
