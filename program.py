def fact(n):
	if n<0:
		return 0
	if n==0:
		return 1

	else:
		return n*fact(n-1)

def pow(n, a):
	return n**a

def simple_check(n):
	c = 0
	for i in range (1,n):
		if n%i==0:
			c+=1
		else:
			continue
	return c==1

n = int(input("Введите число: "))
print(fact(n))
print(pow(n, 5))
print(simple_check(n))

