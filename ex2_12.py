#Stock Transaction Program
totalShares = 2000
initialPrice = 40.00
initialCommission = .03 * totalShares * initialPrice
totalInitialInvestment = initialCommission + (totalShares * initialPrice)
salePrice = 42.75
saleCommission = .03 * totalShares * salePrice
totalReceivedSale = salePrice * totalShares
totalProfit = totalReceivedSale - totalInitialInvestment - saleCommission
print('Total initial investment:$',totalInitialInvestment,'\nInitial Commission:$',initialCommission,'\nTotal sale of stock revenue:$',totalReceivedSale,'\nTotal Profit:$',totalProfit)

