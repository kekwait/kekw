def fact(n):
	if n<0:
		return 0
	if n==0:
		return 1

	else:
		return n*fact(n-1)

def pow(n, a):
	return n**a

n = int(input("Введите число: "))
print(fact(n))
print(pow(n, 5))

