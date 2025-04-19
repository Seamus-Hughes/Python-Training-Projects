Here is my code 

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
	
#----Variables----
# NOTE page_title is dynamic as week num will change. 
# NOTE week starts in Thursday for this project.
page_title = "# Lifestream Week 2389"
author = "*by Seamus Hughes*"

#-----Calculate approx age
birth_year = input("what year were you born? ")
year_number = int(birth_year)
# Obtain current year
current_year = datetime.date.today().year
print(current_year)
# calculate approx age 
appro_age = current_year - year_number
print(f"You are approximately {appro_age} years old?")

'''Parsing Date Strings (strptime)'''
# Variables
date_string_from_user = "28/06/1979"
format_code = "%d/%m/%Y" # MUST match string format!
# parse the string into a datetime object. 
datetime_object = datetime.datetime.strptime(date_string_from_user,format_code)

# Check code 
print(f"String was: {date_string_from_user}")
print(f"Parse object is: {datetime_object}")
print(f"Type is: {type(datetime_object)}")

# Get just the date part 
date_object = datetime_object.date()
print(f"Extracting Date part: {date_object}")
print(f"Type is: {type(date_object)}")

# Finding the day of the week. 
day_number = date_object.weekday()
print(f"Day number = {day_number}")
# Will print number. use logic later to convert to Mon, Tues....

'''
#-----Main Loop------

# Create page header
print(f"{page_title}\n\n{author}\n\n")
# Create template post for each 7 days. 
for i in range(7):
	print(create_daily_entry(i))
	print("")
'''