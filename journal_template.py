# Author: Seamus Hughes
# Date: 5th April 2025
# Purpose: Template for my weekly Lifestream posts.

#----Imported Module----
import datetime

#----Variables----
# ... (previous variables are fine) ...
page_title = "# Lifestream Week 2389"
author = "*by Seamus Hughes*"
day_title = "#### Thursday" # We'll update this using the formatted date soon!

# markdown template of post
# NOTE, number in [] is dynamic and changed for each day.
post_template = """
> quote[1]
> -- attribute # (Minor typo: attribute)

[1]: note"""

# ----Date----
# get todays date object
todays_date = datetime.date.today()
print(todays_date) # Prints the original date object (e.g., 2025-04-07)

# formated date in a string
# NOTE prefered format is 'Monday 7th April 2025'
# please facilitate adding "st" "nd" and "th" as a future part of this tutorial.
formated_date = todays_date.strftime("%A, %B, %-d, %Y") # Correct use of strftime!
print(formated_date) # Prints the formatted string!
print("")
# ----Combine variables----
# NOTE f""" .... """ multi lines with {strings} doesn't work in this app # (Minor typos: strings, doesn't)
full_day_entry = f"{day_title}\n{post_template}"

# combine all.
print(f"{page_title}\n\n{author}\n\n{full_day_entry}")

