#Male and Female Percentages
males = float(input('How many men are in your class?'))
females = float(input('How many women are in your class?'))
totalclass = males + females
percentm = males / totalclass
percentf = 1-percentm

print(format(percentm, '.1%'), "of students are male in your class, and", format(percentf, '.1%'), "are female.")

