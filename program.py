def fact(n):
	if n==0:
		return 1

	else:
		return n*fact(n-1)

isActive = True
while isActive:
	n = int(input("Введите число: "))
	if n<0:
		isActive = False
	else:
		print(fact(n))

