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
z = int(z)

#	> > > > > > 		SECTION 1	vars from user #s
print "\n	> > > > > 	SECTION 1"

#	The Setup: x and y are the initial #s in the sequence
print fibo	#empty list
x = a			# if 3
y = x + (x - 1)	# 	w/b 5
fibo.append(x)	# fibo = [3]
fibo.append(y)	# fibo = [3, 5]


#	New Vars: return last and 2nd-to-last nums in list "fibo"
last_num = (fibo[len(fibo)-1])		# return [5]
penult_num = (fibo[len(fibo)-2])	# return [3]

print len(fibo)			# return 2
y = penult_num + last_num	#new version of y, using previous fibonacci seq result


#	> > > > > > 		SECTION 2		the actual math
print "\n	> > > > > 	SECTION 2		the actual math"

#		initial nums from user's low num
print fibo

# 		while high num in fibo list is less than user's high num (z)
while (fibo[len(fibo)-1]) + (fibo[len(fibo)-2]) <= z:
	fibo.append((fibo[len(fibo)-2]) + (fibo[len(fibo)-1]))
	print fibo				# just checking - not necessary after every go 'round
print (fibo[len(fibo)-1])	# just checking - not necessary	
print z						# just checking - not necessary
print fibo		# the answer

print "is z greater than last #?"
print z > (fibo[len(fibo)-1])
print type (fibo[len(fibo)-1])


print "\nFibonacci!"
print "Not just Fibonacci, but Fibonacci_NEW!"
		




