#Write a program that calculates the total amount of a meal purchased
#at a restaurant. The program should ask the user to enter the charge
#for the food, and then calculate the amount of a 18 percent tip and
#7percent sales tax. Display each of these amounts and the total

total = float(input('What is the total amount due for your food today?'))
tipTax = 0.18
salesTax = 0.07
tipTaxd = total * tipTax
salesTaxd = total * salesTax
totalbill = total * (1 + salesTax + tipTax)

print("Subtotal:$", format(total, ',.2f'), "\nGratuity:$", format(tipTaxd, ',.2f'), "\nSales Tax Due:$", format(salesTaxd, ',.2f'), "\nTotal Due Today:$", format(totalbill, ',.2f'), "\nTHANK YOU!")


