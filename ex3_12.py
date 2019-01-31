#Software Sales
#gives base price

base_price = 99

#gives discounts per unit based on the four levels of discount

disc1 = base_price * .1
disc2 = base_price * .2
disc3 = base_price * .3
disc4 = base_price * .4

#gives the price of the unit with discount

price1 = base_price * .9
price2 = base_price * .8 
price3 = base_price * .7
price4 = base_price * .6

#asks the user how many units they have purchased

units_bought = int(input('How many units are you going to purchase?'))

#gives the customer the quantity of discount and the total price

if units_bought < 10:
	print('You do not receive a discount')
	print('Your total due today is $', format((base_price * units_bought), '.2f'))
elif units_bought >= 10 and units_bought <= 19:
	print('Your discount today is $', format((disc1 * units_bought), '.2f'))
	print('Your total due today is $', format((price1 * units_bought), '.2f'))
elif units_bought >= 20 and units_bought <= 49:
	print('Your discount today is $', format((disc2 * units_bought), '.2f'))
	print('Your total due today is $', format((price2 * units_bought), '.2f'))
elif units_bought >= 50 and units_bought <= 99:
	print('Your discount today is $', format((disc3 * units_bought), '.2f'))
	print('Your total due today is $', format((price3 * units_bought), '.2f'))
else:
	print('Your discount today is $', format((disc4 * units_bought), '.2f'))
	print('Your total due today is $', format((price4 * units_bought), '.2f'))





