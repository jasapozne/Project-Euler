#izkaže se, da obstaja že vgrajena funkcija, ki to reši
from itertools import permutations
def seznam_permutacij():
	return list(permutations(range(10)))[999999]

print(seznam_permutacij())