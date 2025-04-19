# Author: Seamus Hughes
# Date: 5th April 2025
# Purpose: Template for my weekly Lifestream posts.

#----Imported Module----
import datetime # Correctly imported!

#----Variables----
# ... (previous variables are fine) ...
page_title = "# Lifestream Week 2389"
author = "*by Seamus Hughes*"
day_title = "#### Thursday" # We'll link this to the actual date later!

# markdown template of post
# NOTE, number in [] is dynamic and changed for each day.
post_template = """
> quote[1]
> -- attribute # (Minor typo: attribute)

[1]: note"""

# ----Date----
# get todays daye object l # (Minor typo: date)
todays_date = datetime.date.today() # Correctly gets the date object!
print(todays_date) # Correctly prints it!

# ----Combine variables----
# NOTE f""" .... """ multi lines with {strings} dosen't work in this app # (Minor typos: strings, doesn't)
full_day_entry = f"{day_title}\n{post_template}"

# combine all.
print(f"{page_title}\n\n{author}\n\n{full_day_entry}")
