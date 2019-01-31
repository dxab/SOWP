#Color Mixer
color1 = input('Please enter your first color: ')
color2 = input('Please enter your second color: ')
if not(color1 == 'yellow' or color1 == 'blue' or color1 == 'red'):
	print('Color 1 is not a primary color. Please try again.')
else:
	if not(color2 == 'yellow' or color2 == 'blue' or color2 == 'red'):
		print('Color 2 is not a primary color. Please try again.')
	else: 
		if color1 == 'red' and color2 == 'blue':
			print('You have made purple.')
		elif color1 == 'red' and color2 == 'yellow':
			print('You have made orange.')
		elif color1 == 'blue' and color2 == 'yellow':
			print('You have made green.')
		elif color2 == 'red' and color1 == 'blue':
			print('You have made purple.')
		elif color2 == 'red' and color1 == 'yellow':
			print('You have made orange.')
		elif color2 == 'blue' and color1 == 'yellow':
			print('You have made green.')
		else: 
			print('You have not made a secondary color.')

	
