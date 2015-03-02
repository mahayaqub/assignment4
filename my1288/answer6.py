first_name = raw_input('Enter your first name: ')
last_name  = raw_input('Enter your last name: ')

print 'Enter your date of birth:'

month = raw_input('Month?')

try:
	day = input('Day?')
except:
	print 'Enter day in numeric form.'
	day = input('Day?')

try:
	year = input('Year?')
except:
	print 'Enter year in numeric form.'
	year = input('Year?')

print first_name + ' ' + last_name + ' was born on ' + month.capitalize() + ' ' + str(day) + ', ' + str(year)+'.'

