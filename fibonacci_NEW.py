
#	empty list "fibo" will contain final sequence at end
fibo = []

#	> > > > > > 		SECTION 1	appends fibo (list) w/first pair of vars from user
def fibo_one():
	a = raw_input("what is your starting number?  ")
	z = raw_input("and your ending number?  ")
	a = int(a)
	z = int(z)

	x = a			# ex: 3
	y = x + (x - 1)	# ex: w/b 5
	fibo.append(x)	# ex: fibo = [3]
	fibo.append(y)	# ex: fibo = [3, 5]


#	> > > > > > 		SECTION 2	the math
	while (fibo[len(fibo)-2]) + (fibo[len(fibo)-1]) <= z:
		fibo.append((fibo[len(fibo)-2]) + (fibo[len(fibo)-1]))
	print fibo		# the answer

	print "\nFibonacci"
	print "Not just Fibonacci, but Fibonacci_NEW!"
		






if __name__=="__main__":
	fibo_one()


