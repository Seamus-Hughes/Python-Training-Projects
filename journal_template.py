# Author: Seamus Hughes
# Date: 29th April 2025
# Purpose: Template for my weekly Lifestream posts.

#----Imported Modules----
import datetime # For date management
import  math # For rounding

#----Functions-----

def create_formatted_date(date_object):
	'''Formatting date into a nice looking string'''
	# add .day to get just the day number 
	day_object = date_object.day # output - 1-31 as int
	# use strftime to format date object
	# use f string to allow date_ordinal to work. 
	formatted_date = date_object.strftime(f"%A %-d{date_ordinal(day_object)} %B %Y") # Output = Monday 7th April 2025
	# NOTE %-d used to get rid of leading zero might not work in some instances.
	return formatted_date

def date_ordinal(day_no):
	'''Add the corrct ordinal suffix to dates st, nd, rd, th'''
	# Rounds UP to to nearest 10ths
	rounded = math.ceil(day_no / 10) * 10
	# Obtains remander after removing 10ths
	remainder = day_no - (rounded - 10)
	# If 20 then date is 11-19. 
	if rounded == 20:
		ordinal = "th"
	# Checks if 1, 2 and 3 irespctive of the 10ths
	elif remainder == 1:
		ordinal = "st"
	elif remainder == 2:
		ordinal = "nd"
	elif remainder == 3:
		ordinal = "rd"
	# Mops up the remainder. 
	else:
		ordinal = "th"
	return ordinal

def offset_to_thurs (given_date):
	'''Offset any date given to the previous Thurseday. 
	
	Uses Modulo (%). Produces the remainder after multiples of 7 removed. The remainder is alao the number of days you have to go back to get to Thirsday. '''
	# Given_weekday No as int Mon = 0, Tues 1.... 
	given_weekday = given_date.weekday()
	
	# given_weekday - 3 gives Thursday week value of 0
	days_from_thurs = (given_weekday - 3) % 7
	# NOTE If the % No. is positive it gives a positve result even if i is negative. 
	
	# Days to take off to get to nearest Thursday. 
	offset_days = datetime.timedelta(days=days_from_thurs)
	
	# create offset day. 
	offset_date = given_date - offset_days
	return offset_date

def create_daily_entry(entry_num):
	'''Using range number given, will create template for daily lifelog post'''
	# ----Date----
	# create todays date 
	todays_date = datetime.date.today()
	offset_date = offset_to_thurs(todays_date)
	# create datetime object for each of 7 days
	# 1st day always today as entry_num = 0
	delta_day = datetime.timedelta(days=entry_num)
	day_of_week = offset_date + delta_day
	formatted_day_of_week = create_formatted_date(day_of_week)
	
	# -----markdown template ------
	# NOTE f""" .... """ multi lines with {strings} doesn't work in this app
	day_entry = f"#### {formatted_day_of_week}\n\n> quote[^{entry_num+1}]\ \n> -- *attribute*\n\n[^{entry_num+1}]: note"
	return day_entry

def weeks_alive(birthday):
	'''Calculating how mamy weeks someone has been alive. NOTE birthday format need to be dd/mm/yyyy'''
	format_code = "%d/%m/%Y" # MUST match string format!
	today = datetime.datetime.today().date()
	# parse the string into a datetime object. 
	birth_date = datetime.datetime.strptime(birthday,format_code).date()
	# Date Maths
	date_difference = today - birth_date
	days = date_difference.days
	weeks = days // 7
	return weeks
	
#----Variables----
# Fixed. birth date as personal project.
todays_date = datetime.datetime.today()
birthday = "28/06/1979"
page_title = f"# Lifestream Week {weeks_alive(birthday)}"
author = "*by Seamus Hughes*"

format_code = "%d/%m/%Y" # MUST match string format!
birth_date = datetime.datetime.strptime(birthday,format_code).date()

# Get the day of the week. (0 = Mon to 6 = Sun)
day_number = birth_date.weekday()
print(f"Weekday number (0 = Mon to 6 = Sun): {day_number}")
# NOTE week starts in Thursday for this project. (as i was born on a Thursday)
# Will print number. use logic later to convert to Mon, Tues....

#----Test Bed-----

# Test Run to work out how Modulo works in this section. 

for i in range(7):
	# i - 3 gives Thursday week value of 0
	i = i - 3 + 7 
	# If the % No. is positive it gives a positve result even if i is negative. 
	# Produces the remainder after multiples of 7 removed
	# Add 7 to i above and it produces same result. infact it makes it easier to understand.
	# The trick here is the remainder is alao the number of days you have to go back to get to Thirsday. 
	modulo = i % 7
	print(f"i = {i}")
	print(f"mod = {modulo}")
	
# Debug code to assess new offset_to_thurs function

# Create test date
start_date = datetime.date(2025, 1, 6)
print(start_date)

for i in range(7):
	# create a datetime object out of i into respective No of days.
	days_offset = datetime.timedelta(days=i)
	# create 7 consecutive days 
	test_date = start_date + days_offset
	weekday = test_date.weekday()
	print("")
	print(f"Test run No. {i+1}")
	print (days_offset)
	print(test_date)
	print(f"{weekday} - weekday")
	print(offset_to_thurs(test_date))

#-----Main Loop------

# Create page header
print(f"{page_title}\n\n{author}\n\n")
# Create template post for each 7 days. 
for i in range(7):
	print(create_daily_entry(i))
	print("")
