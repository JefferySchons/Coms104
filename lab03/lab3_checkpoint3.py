from math import ceil

weight = input("Please enter the weight of the letter in ounce: ")

if weight>3.5:
    cost=.88+ceil(weight-1)*.17
else:
	if weight >1.0:
		cost=.44+ceil(weight-1)*.17
	else:
		cost=.44
print "Cost:", cost
