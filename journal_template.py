# Author: Seamus Hughes
# Date: 15th October 2025
# Purpose: Template in Markdown for my weekly Lifestream posts.

# ----Imported Modules----
import datetime  # For date management
import math  # For rounding
import os  # For file handling
import shutil  # For file moving

# ----Functions-----


def create_formatted_date(date_object):
	'''Create date into a preferred looking formatted string'''
	# add .day to get just the day number
	day_object = date_object.day  # output - 1-31 as int
	# use strftime to format date object
	# use f string to allow date_ordinal to work.
	formatted_date = date_object.strftime(
	 f"%A %-d{date_ordinal(day_object)} %B %Y")  # Output = Monday 7th April 2025
	# NOTE %-d used to get rid of leading zero might not work in some instances.
	return formatted_date


def date_ordinal(day_no):
	'''Add the correct ordinal suffix to dates st, nd, rd, th'''
	# Rounds UP to to nearest 10ths
	rounded = math.ceil(day_no / 10) * 10
	# Obtains remainder after removing 10ths
	remainder = day_no - (rounded - 10)
	# If 20 then date is 11-19.
	if rounded == 20:
		ordinal = "th"
	# Checks if 1, 2 and 3 irrespective of the 10ths
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


def offset_to_day(given_date, day_number):
	'''Offset any date given to the previous day defined by the given day number.
	
	Uses Modulo (%). Produces the remainder after multiples of 7 removed. The remainder is also the number of days you have to go back to get to Thursday. '''
	# Given_weekday No as int Mon = 0, Tues 1....
	given_weekday = given_date.weekday()

	# given_weekday - day_number gives day week value of 0
	days_from_day_num = (given_weekday - day_number) % 7
	# NOTE If the % No. is positive it gives a positve result even if it is negative.

	# Days to take off to get to nearest day defined by day_number.
	offset_days = datetime.timedelta(days=days_from_day_num)

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
	'''Calculating how many weeks someone has been alive. NOTE birthday format need to be dd/mm/yyyy'''
	format_code = "%d/%m/%Y"  # MUST match string format! 
	today = datetime.datetime.today().date()
	# Creating a datetime object out of the  string with set date format..
	birth_date = datetime.datetime.strptime(birthday, format_code).date()
	# Date Maths
	date_difference = today - birth_date
	days = date_difference.days
	# Weeks + 1 as first week is week 1 not 0
	weeks = days // 7 + 1
	return weeks


# ----Variables----
set_birthday = ''  # to be filled later
val_birthday = ''  # to be filled later
favorite_color = ''  # to be filled later
todays_date = datetime.datetime.today()
author = "*by Seamus Hughes*"
# folder variables
output_folder = "Lifestreams"
archive_folder = "Archive"
# Profile file names
profile_file = "profile.txt"

# -----Main Loop------

# ----- 1. Setup-------

# If protife.txt exists then birthday has already been saved to file during previous run.
if os.path.exists("profile.txt"):
	print("Welcome back to my Lifestream daily Journal Template")
	# Safely opens the file and reads entire contents
	with open(profile_file, 'r') as file:
		# strip removes not needed white spaces, tabs or new lines
		val_birthday = file.read().strip()
		print(f"Your birthday is {val_birthday}")
# If profile.txt not there then it's the program's 1st run and needs to ask for birthday.
else:
	print("Welcome to my Lifestream daily Journal template.")
	# create a loop, only broken when a valid date is entered.
	while True:
		try:
			set_birthday = input("What is your birthday (dd/mm/yyyy)? ")
			# validate the string and create datetime object.
			val_birthday = datetime.datetime.strptime(set_birthday, "%d/%m/%Y")
			# Creates new file. WARNING will over write if already exists.
			with open(profile_file, 'w') as file:
				# Save date string rather than datetime to text file.
				file.write(set_birthday)
			break
		except ValueError:
			print("there was an error in your date input")
			print("Please try again")

# ----- 2. Dynamic variables -----

# Now we have a valid birthday we can create dynamic variables based on the date
current_weeks_alive = weeks_alive(val_birthday)
page_title = f"# Lifestream Week {current_weeks_alive}"

## Feom the bithday, work out  day if the week they were born.

# Convert birthday string into datetime date object. 
birthday = datetime.datetime.strptime(val_birthday, "%d/%m/%Y").date()
# Find day number of birth date. 
birth_day_number = birthday.weekday()

# ----- 3. Create Markdown Text -------

# calculate week start date
week_start_date = offset_to_day(todays_date.date(), birth_day_number)
# Starts string for saving to file
print_to_file = f"{page_title}\n\n{author}\n\n"
# Create template post for each 7 days.
for i in range(7):
	# Creates markdown for each day
	daily_entry = create_daily_entry(week_start_date, i)
	# Adds daily_entry to string for file creation.
	print_to_file += daily_entry + "\n\n"
	# NOTE += includes to contents of called variable + anytring else addes.
	# All new lines need to be added to the string

# ---- 4. Print to File-----

# Create dynamic title
# Remeber to add file type (.md)
dynamic_title = f"Lifestream Week {current_weeks_alive}.md"
# point file to directory
full_path = os.path.join(output_folder, dynamic_title)
# Make sure the folder exists
if not os.path.exists(output_folder):
	# creates to folder if needed.
	os.mkdir(output_folder)

# Creates a new file, gives file name, writes to file.
# NOTE: adeed encoding= "utf-8" for better future compatability
try:
	# 'x' mode stands for exclusive creation
	# creates and opens file for writing
	# will fail if file exsists.
	with open(full_path, "x", encoding="utf-8") as my_file:
		# Write a string to file.
		my_file.write(print_to_file)
		print(f"Successfully created file '{dynamic_title}'")
except FileExistsError:
	print(f"ERROR: File '{dynamic_title}' already exists. can not create.")

# ---- 5. Archiving Material-----

print(f"Archiving updated files to {archive_folder} folder.")

# Identify or create archive folder
if not os.path.exists(archive_folder):
	print(f"creating {archive_folder} folder.")
	os.mkdir(archive_folder)

# Create list of files in output folder
output_contents = os.listdir(output_folder)
# Loop through output_contents
for item_name in output_contents:
	# Create full path the file
	source_path = os.path.join(output_folder, item_name)
	# Returns only is file.
	if os.path.isfile(source_path):
		# seperate file name from file extension
		filename_root, file_extension = os.path.splitext(item_name)
		# Returns only markdown files
		if file_extension == ".md":
			# Build path to archive folder so you can check current file against archived file
			destination_path = os.path.join(archive_folder, item_name)
			# check if file dose not exist in archive folder.
			if not os.path.exists(destination_path):
				# File not in archive so copy over
				shutil.copy(source_path, destination_path)
				print(f"{item_name}: saved.")
			else:
				# Compare archive and source files to see if any changes have been made.
				# get modification times for each file
				source_mod_time = os.path.getmtime(source_path)
				dest_mod_time = os.path.getmtime(destination_path)
				# If source is newer the archive needs updating
				if source_mod_time > dest_mod_time:
					shutil.copy(source_path, destination_path)
					print(f"{item_name}: updated.")
print("Archiving process complete")
