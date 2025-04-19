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

# Date Maths
yesterdays_date = todays_date - delta_1_day
tomorrows_date = todays_date + delta_1_day

# Display dates

print(f"Yesterday's' date: {yesterdays_date}")
print(f"Todays date: {todays_date}")
print(f"Tomorrows date: {tomorrows_date}")
print("")
# Formatted date in a string
# NOTE prefered format is 'Monday 7th April 2025'
# please facilitate adding "st" "nd" and "th" as a future part of this tutorial. 
formatted_yesterday = yesterdays_date.strftime("%A, %B, %-d, %Y")
formatted_today = todays_date.strftime("%A, %B, %-d, %Y")
formatted_tomorrow = tomorrows_date.strftime("%A, %B, %-d, %Y")
print(formatted_yesterday)
print(formatted_today)
print(formatted_tomorrow)
print("")

# counting through the days of the week.
for i in range(7):
	print(i)
print("")

# ----Combine variables----
# NOTE f""" .... """ multi lines with {strings} doesn't work in this app
full_day_entry = f"{day_title}\n{post_template}"

# combine all.
print(f"{page_title}\n\n{author}\n\n{full_day_entry}")