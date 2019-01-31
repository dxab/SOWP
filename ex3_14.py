#Body Mass Index

#asking user for necessary input

weight = float(input('What is your current weight, fatty?'))
height = float(input('What is your height (in inches)?'))

#formula for bmi

bmi = weight * 703 / height**2

#give display bmi

print('Your BMI is', format(bmi, '.1f'),'.')

#give the customer information on whether they are fat fucks or not
#threshold for being in the normal range is 18.5 - 25

if bmi >= 18.5 and bmi <= 25:
	print('You are within a healthy weight. Congrats!')
elif bmi > 25:
	print('You are overweight, ya fat fook.')
else:
	print('You are underweight, may I recommend some pizza?')


