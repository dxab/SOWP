#Mass and Weight
mass = float(input('What is the mass of the object (in kilograms)?'))
weight = mass * 9.8
if weight > 500:
	print('The object is too heavy')
elif weight < 100:
	print('The object is too light')
else:
	print('The object qualifies')
