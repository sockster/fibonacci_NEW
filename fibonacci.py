"""
def nacci:
	for num in range(0,10000)
"""

num1 = 0
num2 = (num1 + 1)  # 1
num3 = (num1 + num2)  # 1

	

# print num1, -> 0, 
# print num2, -> 1, 
# add num1 + num2 (save as num1)


def nacci():
	for num3 in range(0,100):
		print num3
		num3 = (num2 + num3)
		print num3
	
print num1
print num2
print num3

nacci()



0   1
1	2
1	3 (1 + 2)
2	4 (2 + 3)
3	
5
