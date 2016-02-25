num=input("How many mega mousetraps:")

if num%50!=0:
	numbox=(num/50)+1
else:
	numbox=(num/50)

shippingTax=numbox*5.00
mouseCost=num*2.00

print "Shipping:",shippingTax

total=mouseCost+shippingTax

print "Total:",total
