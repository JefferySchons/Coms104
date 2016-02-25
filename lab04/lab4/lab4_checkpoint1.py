#function to print even/odd for string length
def even_or_odd(s):
	if len(s)%2!=0:
		return "Odd"
	else:
		return "Even"


a=raw_input("enter a string:")

b=even_or_odd(a)

print b
