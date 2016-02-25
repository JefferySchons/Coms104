import math
print "Quadratic Equations: ax^2+bx+c=0"

a=input("Enter a:")
b=input("Enter b:")
c=input("Enter c:")

decrament=(b*b)-(4*a*c)
string_eq=str(a)+"x^2+"+str(b)+"x+"+str(c)+"=0"

if decrament>0:
	#2 solutions
	print "Equation:", string_eq, "has two solution."
	
	solution_one=(-b+(decrament**0.5))/(2*a)
	solution_two=(-b-(decrament**0.5))/(2*a)
	
	print "Solution1:", int(solution_one)
	print "Solution2:", int(solution_two)

elif decrament==0:
	#1 solution
	print "Equation:", string_eq, "has one solution."
	solution_one=(-b+(decrament**0.5))/(2*a)
	print "Solution1:", int(solution_one)
else:
	#no solutions
	print "Equation:", string_eq, "has no solution."
