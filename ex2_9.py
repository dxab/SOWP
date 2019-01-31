#Write a program that converts Celsius temperatures to Fahrenheit temp. 
#The formula is as follows: f = 9 / 5 * C + 32
#This program should ask the user to enter a temp in Celsius and then
#display the temp converted to Fahrenheit

celsius = float(input('Please enter todays temperature (in celsius): '))
fahr = 9 / 5 * celsius + 32

print("Today's temperature in degrees fahrenheit is", format(fahr, '.0f'), 'degrees.')





