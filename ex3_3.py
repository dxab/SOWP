#Age Classifier
age = float(input('Please enter your age: '))
if age > 0 and age < 1:
	print('You are an infant.')
elif age >= 1 and age < 13:
	print('You are a child.')
elif age >= 13 and age < 20:
	print('You are a teenager.')
elif age >= 20 and age < 120:
	print('You are a adult.')
else:
	print('Invalid age, please try again.')
