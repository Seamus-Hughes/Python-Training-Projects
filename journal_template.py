# Author: Seamus Hughes
# Date: 5th April 2025
# Purpose: Template for my weekly Lifestream posts.

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
> -- atribute

[1]: note"""

# ----Combine variables----
# NOTE f""" .... """ muti lines with {steings} dosn't work in this app
full_day_entry = f"{day_title}\n{post_template}"

# combine all.
print(f"{page_title}\n\n{author}\n\n{full_day_entry}")