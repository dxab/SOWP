#Time Calculator

#constants
minute = 60
hour = 3600
day = 86400

#inputs

seconds = int(input('Please input the number of seconds: '))

#conversions without remainder

sec_to_min = seconds//minute
sec_to_hour = seconds//hour
sec_to_day = seconds//day


#calcs

if seconds >= 60 and seconds < 3600:
	print('Minutes:', sec_to_min)
	print('Seconds:', (seconds - (sec_to_min *60)))
elif seconds >=3600 and seconds < 86400:
	print('Hours:', sec_to_hour)	
	print('Minutes:', (sec_to_min - (sec_to_hour*60)))
	print('Seconds:', (seconds - (sec_to_min *60)))
elif seconds >= 86400:
	print('Days:', sec_to_day)
	print('Hours:', (sec_to_hour - (sec_to_day*24)))
	print('Minutes:', (sec_to_min - (sec_to_hour*60)))
	print('Seconds:', (seconds - (sec_to_min *60)))
else:
	print("Invalid input.")


