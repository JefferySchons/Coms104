#the function
def area_of_circle(radius):
	area=3.14*radius*radius
	return area
	
#the script
radius=input("radius of cylinder:")
height=input("height of cylinder:")
circle_area=area_of_circle(radius)*height
print circle_area

