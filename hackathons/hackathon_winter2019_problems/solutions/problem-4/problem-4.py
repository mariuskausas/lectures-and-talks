def fib_v1(f1, f2, count):
	""" Returns Fibonacci of x"""
	fib_sum = f1 + f2
	while count >= 2:
		count -= 1
		return fib_v1(f2, fib_sum, count)
	return fib_sum


def fib_v2(x):
	""" Assumes x an int >= 0 and returns Fibonacci of x"""
	if x == 0 or x == 1:
		return 1
	else:
		return fib_v2(x-1) + fib_v2(x-2)


def rabbits(f1, f2, months, mult):
	""" Recursive way to calculate rabbit growth."""
	if months < 2:
		return f2
	else:		
		months -= 1
		return rabbits(f2, f1*mult+f2, months, mult)
	return f2


print(rabbits(1, 1, 28, 2))


def rabbits2(months, mult):
	""" For loop way to calculate rabbit growth."""
	mature = 0
	young = 1

	total = mature + young

	if months < 2:
		return total
	else:
		while months > 2:

			next_mature = mature + young
			next_young = mature * mult

			mature = next_mature
			young = next_young

			months -= 1

		return young + mature


print(rabbits2(30, 2))


def rabbits_for(n, k):
	""" A cool solution to calculate rabbit growth."""
	a, b = 0,1
	for i in range(1,n):
    		a, b = b, k * a + b
	return b


print(rabbits_for(29, 2))

