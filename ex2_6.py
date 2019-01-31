#Sales Tax
statetax = 0.05
countytax = 0.025
amount = float(input('Please enter the total amount of your purchase: '))
statetaxd = amount * statetax
countytaxd = amount * countytax
totaldue = amount*(1+statetax+countytax)

print('Subtotal: $', format(amount, '17,.2f'), '\nState Sales Tax: $', format(statetaxd, '10,.2f'), '\nCounty Sales Tax: $', format(countytaxd, '9,.2f'), '\nTotal Due: $', format(totaldue, '16,.2f'))


