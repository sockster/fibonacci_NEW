"""
starting #, ending #
state range(a, b)
state list w/    x = a, n = b
y = x - 1
append.list[x, y]
	for each number in the range,
		append.list[x += y]
		print "Fibonacci!"
"""


fibo = []
z = len(fibo)+1

a = raw_input("what is your starting number?  ")
b = raw_input("and your ending number?  ")
a = int(a)
b = int(b)
x = a
y = x + (x - 1)
fibo.append(x)
fibo.append(y)

# when below is "live" looks like it returns [3, for each ... int?
#for n in range(a, b):
#	y = fibo[:z] + fibo[:z:-1]
fibo.append(y)
# print fibo

print range(a, b)
print x
print y
print fibo[:z]
print fibo[:z:-1]

print "Fibonacci!"

print "Not just fibonacci, but Fibonacci_NEW!"
		




