#Areas of Rectangles
length1 = float(input("Please enter the length of rectangle 1: ")) 
width1 = float(input("Please enter the width of ractangle 1: "))
length2 = float(input("Please enter the length of rectangle 2: ")) 
width2 = float(input("Please enter the width of ractangle 2: "))
area1 = length1 * width1
area2 = length2 * width2
if area1 > area2:
	print('Rectangle 1 has a greater area')
elif area1 == area2:
	print('Both rectangles have the same area')
else:
	print('Rectangle 2 has a greater area')



