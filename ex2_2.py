percentSales = float(0.23)
totalSales = float(input('Please enter the total projected sales: '))
profit = percentSales * totalSales

print('$', format(profit, ',.2f'), sep='')
