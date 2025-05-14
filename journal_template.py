# Author: Seamus Hughes
# Date: 4th May 2025
# Purpose: Templatem in Markdown for my weekly Lifestream posts.

#----Imported Modules----
import datetime # For date management
import  math # For rounding

#----Functions-----

def create_formatted_date(date_object):
	'''Create date into a prefered looking formatted string'''
	# add .day to get just the day pnumber 
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
	'''Offset any date given to the previous Thursday. 
	
	Uses Modulo (%). Produces the remainder after multiples of 7 removed. The remainder is alao the number of days you have to go back to get to Thursday. '''
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

def create_daily_entry(date_for_entry, entry_num):
	'''Using range number given, will create template for daily lifelog post'''
	# create datetime object for each of 7 days
	# 1st day always today as entry_num = 0
	delta_day = datetime.timedelta(days=entry_num)
	day_of_week = date_for_entry + delta_day
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
	# Weeks + 1 as first week is week 1 not 0
	weeks = days // 7 + 1
	return weeks
	
#----Variables----
# Fixed. birth date as personal project.
todays_date = datetime.datetime.today()
birthday = "28/06/1979"
page_title = f"# Lifestream Week {weeks_alive(birthday)}"
author = "*by Seamus Hughes*"

#-----Main Loop------

# calculate week start date
week_start_date = offset_to_thurs(todays_date.date())
# Starts string for saving to file
print_to_file = f"{page_title}\n\n{author}\n\n"
# Create template post for each 7 days. 
for i in range(7):
	# Creates markdown for each day
	daily_entry = create_daily_entry(week_start_date,i)
	# Adds daily_entry to string for file creation.
	print_to_file += daily_entry + "\n\n"
	# NOTE += includes to contents of called variable + anytring else addes. 
	# All new lines need to be added to the string 

#----Print to File-----

# Create dynamic title
# Remeber to add file type (.md)
dynamic_title = f"Lifestream Week {weeks_alive(birthday)}.md"

# Creates a new file, gives file name, writes to file.
# NOTE: adeed encoding= "utf-8" for better future compatability
with open(dynamic_title, "w", encoding= "utf-8") as my_file:
	# Write a string to file.
	my_file.write(print_to_file)

#NOTE: # Replaces all contents if file already exsists.

print("Message saved. ")