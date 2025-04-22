# Author: Seamus Hughes
# Date: 8th April 2025
# Purpose: Template for my weekly Lifestream posts.

#----Imported Modules----
import datetime 

#----Functions-----

def create_formatted_date(date_object):
	'''Formatting date into a nice looking string'''
	# NOTE prefered format is 'Monday 7th April 2025'
	# please facilitate adding "st" "nd" and "th" as a future part of this tutorial.
	# NOTE %-d used to get rid of leading zero might not work in some instances.
	formatted_date = date_object.strftime("%A %-d %B %Y") # Output = Monday 7 April 2025
	return formatted_date

def create_daily_entry(entry_num):
	'''Using range number given, will create template for daily lifelog post'''
	# ----Date----
	# create todays date 
	todays_date = datetime.date.today()
	# create datetime object for each of 7 days
	# 1st day always today as entry_num = 0
	delta_day = datetime.timedelta(days=entry_num)
	day_of_week = todays_date + delta_day
	formatted_day_of_week = create_formatted_date(day_of_week)
	
	# -----markdown template ------
	# NOTE f""" .... """ multi lines with {strings} doesn't work in this app
	day_entry = f"#### {formatted_day_of_week}\n\n> quote[^{entry_num+1}]\n> --attribute\n\n[^{entry_num+1}]: note"
	return day_entry

def weeks_alive(birthday):
	'''Calculating how mamy weeks someone has been alive. NOTE birhday format need to be dd/mm/yyyy'''
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
birthday = "28/06/1979"
page_title = f"Lifestream Week {weeks_alive(birthday)}"
author = "*by Seamus Hughes*"

format_code = "%d/%m/%Y" # MUST match string format!
birth_date = datetime.datetime.strptime(birthday,format_code).date()
# Get the day of the week. (0 = Mon to 6 = Sun)
day_number =  birth_date.weekday()
print(f"Weekday number (0 = Mon to 6 = Sun): {day_number}")
# NOTE week starts in Thursday for this project.
# Will print number. use logic later to convert to Mon, Tues....

#-----Main Loop------

# Create page header
print(f"{page_title}\n\n{author}\n\n")
# Create template post for each 7 days. 
for i in range(7):
	print(create_daily_entry(i))
	print("")