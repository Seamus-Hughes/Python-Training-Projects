# Author: Seamus Hughes
# Date: 2nd April 2026
# Purpose: Add additional Markdown entry for my daily to do list

import os  # For dir list
from pathlib import Path # for file creation
from datetime import datetime, timedelta # for date conversion

def main():
	
	# Variables
	list_dir = "Lists"
	pre = "To do "
	post = ".md"
	
	try:
		
		# --- 1. First Run setup and error checking. 
		
		if first_run(list_dir, pre, post):
			return 
		
		# --- 2. Pull text from most recent to do list ---
		
		# Create list of files in output folder
		contents = os.listdir(list_dir)
		
		# Return just dates from files names
		file_dates = strip_filename(contents, pre, post)
		
		# Convert date strings into datetime
		dt_list = date_convert(file_dates)
		
		# error check for empty folder
		if not dt_list:
			print("No valid to-do files found. Create your first one.")
			return
		
		# Pull latest date from list
		current_dt = max(dt_list)
		
		# build file path to open 
		full_path = build_file_name(current_dt, pre, post, list_dir)
		
		# Text feom file to string
		text = read_md_file(full_path)
		
		# Test print
		print(text)
		
		# --- 3. create and save to new file
		
		# New file name = old + 1 day
		new_dt = current_dt + timedelta(days=1)
		
		# Create and Wlwrite to file
		new_file(new_dt, list_dir, pre, post)
		
		# Copy contebts of old file to new new file 
		# Remove checked to do's 
		# remove fiotnotes 
		# renumber list of to ds 
		# save to file 
		# end program
	
	# Allows errors to be printed on console
	except (FileNotFoundError, ValueError, IsADirectoryError) as error:
		print(f"Error: {error}")
		exit()
		
def first_run(directory, prefix, postfix):
	
	# Create file path
	list_dir = Path(directory)
		
	# Check path exists & is a dir
	if list_dir.is_dir():
		print("Folder exists")
		# Check contents of Dir 
		contents = os.listdir(directory)
		print(contents)
		if contents:
			print("Dir has contents")
			
		return False
	else:
		print("First Run: Creating folder and file.")
		# Creates Dir including any sub dir (parents = true)
		# still runs as eveb if dir exsists (exist_ok=True)
		list_dir.mkdir(parents=True, exist_ok=True)
		
		print("First run: creating Dir.")
		
		# Create first file
		new_dt = datetime.today().date()  # today's date
		new_file(new_dt, directory, prefix, postfix)
		
		return
		
def new_file(new_dt, dir, pre, post):
    date_str = new_dt.strftime("%Y.%m.%d")
    file_path = Path(dir) / f"{pre}{date_str}{post}"
    file_path.touch(exist_ok=True)
    print(file_path)
		
def strip_filename(names, pre, post):
	'''Strip prefix and post fix from a file name to obtain list of dates used as part of file name'''
	
	# create an empty list 
	file_list = []
	# obtain date from file name
	for file in names:
		# Removing the file type
		part_strip = file.removesuffix(post)
		# remove inital file name
		full_strip = part_strip.removeprefix(pre)
		# collect dates into a list.
		file_list.append(full_strip)
	# return list of dates 
	return file_list

def date_convert(string_list):
	'''converts a list of string dates into list of datetime dates'''
	# create an empty list 
	dt_list = []
	for i in string_list:
		# convert string into datetime format
		# adding .date() removes the time elemennt
		dt = datetime.strptime(i, "%Y.%m.%d").date()
		# collect datetimes into list
		dt_list.append(dt)
	return(dt_list)
	
def build_file_name(name, pre, post, dir):
	'''Build full path to file by combining all the above elements'''
	
	# convert datetime back to string 
	date_str = datetime.strftime(name, "%Y.%m.%d")
	# add directory using () /
	# combine file name elements inside ()
	full_path = Path(dir) / (pre + date_str + post)
	return(full_path)
	
def read_md_file(path):
	'''Opens markdown file and saves text contents to a string'''
	if not path.is_file():
		raise FileNotFoundError(f"File '{path}' does not exist.")	
	if  path.suffix != ".md":
		raise ValueError(f"File '{path}' is not a markdown file.")
	
	# NOTE encoding="utf-8" used to ensure Markup characters in markdown recognised
	text = path.read_text(encoding="utf-8")

	# Return the contents of markdown file as a string
	return text

def new_file(new_dt, dir, pre, post):
	file_path = Path(dir) /(f"{pre} test{post}")
	file_path.touch(exist_ok=True)
	print("test")

main()
