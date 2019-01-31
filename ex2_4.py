#Total Purchase

item1 = float(input('Please enter the price of your first item: '))
item2 = float(input('Please enter the price of your second item: '))
item3 = float(input('Please enter the price of your third item: '))
item4 = float(input('Please enter the price of your fourth item: '))
item5 = float(input('Please enter the price of your fifth item: '))
subtotal = item1 + item2 + item3 + item4 + item5
salesTax = 0.07
total = subtotal * (1 + salesTax)

print('Subtotal: $', format(subtotal, '12,.2f'),'\nSales Tax:', format(salesTax, '13'),'\nTotal Due: $', format(total, '11,.2f')) 


