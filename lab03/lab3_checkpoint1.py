#This script computes the total omount for an order of mousetraps
#costing 2.00 each for the first 50, and 1.50 each thereafter

num=input("How many mousetraps?")
res=raw_input("Are you an Iowa resident (y/n)?")

if num <=50:
    subtotal = num*2.00
else:
    first=50*2.00
    extra=(num-50)*1.50
    subtotal=first+extra

if res=="y":
    tax=.06
    total=subtotal+(subtotal*.06)
    print "Subtotal:", subtotal
    print "Tax:",(subtotal*.06)
else:
    total=subtotal
print "Total:",total
