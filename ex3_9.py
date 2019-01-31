#Roulette Wheel Colors
num = int(input('Please enter the number for which the color you would like to identify: '))
numid = num % 2
if num == 0:
	print("The roulette is green.")
if num > 0 and num <= 10:
	if numid > 0:
		print('Your number is red')
	else:
		print('Your number is black')
elif num >= 11 and num <= 18:
	if numid > 0:
		print('Your number is black')
	else:
		print('Your number is red')
elif num >= 19 and num <= 28:
	if numid > 0:
		print('Your number is red')
	else:
		print('Your number is black')
elif num >= 29 and num <= 36:
	if numid > 0:
		print('Your number is black')
	else:
		print('Your number is red')
