def ali_je_palindorm(niz):
	return str(niz) == str(niz)[::-1]

def najde_palindrom(n, m):
	najvecji = 0
	for i in range(n, m):
		for j in range(n, m):
			k = i * j
			if ali_je_palindorm(k) == True and k > najvecji:
				najvecji = k
	return(najvecji) 

print(najde_palindrom(100,1000))
