#Money Counting Game

#These are the set values for USD currencies and coins.
qtr = 0.25
dime = 0.10
nickels = 0.05
penny = 0.01
dollar = 1.00

# This part asks the users to input the quantities of each coin they have.
qty_qtr = float(input('How many quarters do you have?'))
qty_dime = float(input('How many dimes do you have?'))
qty_nickels = float(input('How many nickels do you have?'))
qty_penny = float(input('How many pennies do you have?'))

#This sets the total value of the coins.

value = (qty_qtr * qtr) + (qty_dime * dime) + (qty_nickels * nickels) + (qty_penny * penny)

#This algorithm determines whether someone has won the game. 

if value > 1:
	print("You have lost the game. You have gone over.")
elif value < 1 and value >= 0:
	print("You have lost the game. You are short some change.")
elif value < 0:
	print("You have negative money, WHAT DID YOU DOOO?")
else:
	print("You have won the game! You have exactly one dollar!")


