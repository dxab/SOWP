#Hot Dog Cookout Calculator
#hotdogs come in packs of 10
#buns come in packs of 8
attending = int(input('How many people are attending?'))
per_person = int(input('How many hot dogs will each attendee have?'))
total_dogs = per_person * attending
bag_dogs = 10
bag_buns = 8


#the remaining buns alone the parentheses portion are not enough to later down calculate the inverse of the hot dogs to display.
remainder_dogs = total_dogs % bag_dogs
remainder_buns = total_dogs % bag_buns
total_bags_dogs = total_dogs // bag_dogs
total_bags_buns = total_dogs // bag_buns
inverse_remainder_dogs = 10 - remainder_dogs
inverse_remainder_buns = 8 - remainder_buns


#this function is used to calculate the amount of hot dog bags we will require
if remainder_dogs == 0:
	print('You will need', total_bags_dogs, 'bags of hot dogs.')
else:
	total_bags_dogs = total_bags_dogs + 1
	print('You will need', total_bags_dogs, 'bags of hot dogs.')
#this function is used to calculate the amount of bun bags we will require
if remainder_buns == 0:
	print('You will need', total_bags_buns, 'bags of buns.')
else:
	total_bags_buns = total_bags_buns + 1
	print('You will need', total_bags_buns, 'bags of buns.')
#this function is used to calculate the remainder of dogs
if remainder_dogs > 0:
	print('You will have', inverse_remainder_dogs,'remaining hot dogs.')
else:
	print('You will have 0 remaining hot dogs.')
#this function is used to calculate the remainder of buns
if remainder_buns > 0:
	print('You will have', inverse_remainder_buns,'remaining buns.')
else:
	print('You will have 0 remaining hot buns.')


