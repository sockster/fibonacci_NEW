"""
starting #, ending #
state range(a, b)
state list w/    x = a, n = b
y = x - 1
append.list[x, y]
	for each number in the range,
		append.list[x += y]
		print "Fibonacci!"
		
WHAT DIDN'T WORK:
	Lfibo = len(fibo) - > > did not capture length of fibo

"""

#	list fibo will be the sequence
fibo = []

a = raw_input("what is your starting number?  ")
z = raw_input("and your ending number?  ")
a = int(a)
z = int(z) + 1

#	x and y are the initial #s in the sequence
x = a
y = x + (x - 1)
fibo.append(x)
fibo.append(y)



print """	> > > > > 	SECTION 1	this section works, returning:
	print range, 
	then 1st #, 
	then 2nd #, 
	then fibo, 
	then len(fibo)"
"""

print range(a, z)
print x
print y
print fibo
print len(fibo)


print "\n	> > > > > 	SECTION 2"
print "print fibo; append fibo w/5 numbers, print again"
print fibo
"""
fibo.append(23)
fibo.append(24)
fibo.append(25)
fibo.append(27)
fibo.append(28)
print ""
print ""
print fibo
"""

print "\n	> > > > > 	SECTION 3		this section works returning last and penult #s in list"
print "Print length of fibo"
print len(fibo)

print fibo

print "\nPrint (fibo[len(fibo)])"
print (fibo[len(fibo)-1])

print "\nPrint (fibo[len(fibo)-2])"
print (fibo[len(fibo)-2])

print "\nNow save those to vars"
last_num = (fibo[len(fibo)-1])
penult_num = (fibo[len(fibo)-2])

print "\nPrint (fibo[len(fibo)])"
print last_num

print "\nPrint (fibo[len(fibo)-2])"
print penult_num
print "  	> > > > > 	SECTION 3 - END"


print "\n	> > > > > 	SECTION 4		the actual math"

"""		returns endless loop
fibo = []
while y <= z:
	print fibo
	y = penult_num + last_num
	fibo.append(y)
print fibo
"""




print "\nFibonacci!"

print "Not just fibonacci, but Fibonacci_NEW!"
		




