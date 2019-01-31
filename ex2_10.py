#Ingredient Adjuster
#A cookie recipe calls for the following ingredients:
#1.5 cups of suga suga
# 1 cup of buttah
# 2.75 cups of flour
#the recipe produces 48 cookies with this amount of ingredients
#write a program that asks the user how many cookies he or she
#wants to make, and then displays the number of cups of each ingredient
#needed for the specified number of cookies

totalCookies = int(input("How many cookies would you like to make today?"))
conversionFactor = totalCookies / 48.0
sugar = 1.5 * conversionFactor
butter = 1 * conversionFactor
flour = 2.75 * conversionFactor

print("Your recipe is as follows:\n", format(sugar, '.2f'), "cups of sugar.\n", format(butter, '.2f'), "cups of butter.\n", format(flour, '.2f'), "cups of flour.")
