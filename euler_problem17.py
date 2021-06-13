enice = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
desetice = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"] #prvi "" 0:9, drugi pa 10:19

def stevila_v_seznam(n):
	if 0 <= n < 20:
		return enice[n]
	elif 20 <= n < 100:
		return desetice[n // 10] + (enice[n % 10] if (n % 10 != 0) else "")
	elif 100 <= n < 1000:
		return enice[n // 100] + "hundred" + (("and" + stevila_v_seznam(n % 100)) if (n % 100 != 0) else "")
	elif 1000 <= n < 1000000:
		return stevila_v_seznam(n // 1000) + "thousand" + (stevila_v_seznam(n % 1000) if (n % 1000 != 0) else "")
	else:
		pass



def stevilo_crk(sez):
    return sum(len(stevila_v_seznam(i)) for i in range(1, 1001))

print(stevilo_crk())