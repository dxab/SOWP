#MPG can be calculated as mpg = miles driven/gallons of gas used
#write a program that asks the user for the number of miles
#driven and the gallons of gas used. it should calc the car's MPG and 
#display the result

miles = float(input('How many miles have you driven?'))
gas = float(input('How much gas have you used (in gallons)?'))
mpg = miles / gas

print("Your car is currently achieving", format(mpg, '.2f'),'mpg.')

