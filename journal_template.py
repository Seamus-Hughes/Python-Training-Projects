# Author: Seamus Hughes
# Date: 5th April 2025
# Purpose: Template for my weekly Lifestream posts.

#----Imported Module----
import datetime 

#----Variables----
# NOTE week number is dynamic and will change with each week. 
# NOTE day_title will be dynamic 
# NOTE week starts in Thursday for this project.
# NOTE full date to be added. 
page_title = "# Lifestream Week 2389"
author = "*by Seamus Hughes*"
day_title = "#### Thursday"

# markdown template of post 
# NOTE, number in [] is dynamic and changed for each day. 
post_template = """
> quote[1]
> -- attribute

[1]: note"""

# ----Date----
# create date objects 
todays_date = datetime.date.today()
delta_1_day = datetime.timedelta(days=1)

# Loop to create 7 days. 
# counting through the days of the week.
for i in range(7):
	# iterate through 7 days
	delta_day = datetime.timedelta(days=i)
	# create datetime object for eaxh of 7 days 
	# 1st day always today as i = 0
	day_of_week = todays_date + delta_day
	# Displays dates
	print(day_of_week)
print("")

# Loop to create 7 days. 
# counting through the days of the week.
for i in range(7):
	# iterate through 7 days (formatted)
	delta_day = datetime.timedelta(days=i)
	# create datetime object for eaxh of 7 days 
	# 1st day always today as i = 0
	day_of_week = todays_date + delta_day
	# Formatted date in a string
	# NOTE prefered format is 'Monday 7th April 2025'
	# please facilitate adding "st" "nd" and "th" as a future part of this tutorial. 
	formatted_day_of_week = day_of_week.strftime("%A, %B, %-d, %Y")
	# Displays dates
	print(formatted_day_of_week)
print("")

# ----Combine variables----
# NOTE f""" .... """ multi lines with {strings} doesn't work in this app
full_day_entry = f"{day_title}\n{post_template}"

# combine all.
print(f"{page_title}\n\n{author}\n\n{full_day_entry}")