#Book Club Points

#this asks the customer how many books they bought in the month
books_bought = int(input('How many books did you buy this month?'))

#this sets the points which the customer has earned to the books they have bought
nobooks = 0
twobooks = 5
fourbooks = 15
sixbooks = 30
eightbooks = 60

#This is the equation which dictates which reward the customer receives
if books_bought >= 2 and books_bought < 4:
	print("You have earned", twobooks, "this month!") 
elif books_bought >= 4 and books_bought < 6:
	print("You have earned", fourbooks, "this month!")
elif books_bought >= 6 and books_bought < 8:
	print("You have earned", sixbooks, "this month!")
elif books_bought >= 8:
	print("You have earned", eightbooks, "this month!")
else:
	print('Sorry, you have not bought enough books for rewards points this month. Fuck off')


