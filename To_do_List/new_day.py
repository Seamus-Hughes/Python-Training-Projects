# Author: Seamus Hughes
# Date: 16th April 2026
# Purpose: Add additional Markdown entry for my daily to do list

import os  # For dir list
from pathlib import Path # for file creation
from datetime import datetime, timedelta # for date conversion
import re # ror string spliting

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
		
		print(f"Old path: {full_path}")
		
		# Text feom file to string
		text = read_md_file(full_path)
		
		# Test print
		print(text)
		
		# --- 3. create and save to new file
		
		# New file name = old + 1 day
		new_dt = current_dt + timedelta(days=1)
		
		# Create next to do list file write to file
		# Retuns full path name
		new_path = new_file(new_dt, list_dir, pre, post)
		
		# Test print
		print(f"new path: {new_path}")
		
		# Split old file contents
		new_todo = split_todo(text)
		
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
	'''Check is Dir and file are present. if not creates Dir and File to alow program to run.'''
	
	# Create file path
	list_dir = Path(directory)
	# Creates Dir including any sub dir (parents = true)
	# still runs as eveb if dir exsists (exist_ok=True)
	list_dir.mkdir(parents=True, exist_ok=True)
	# Check contents of Dir
	contents = os.listdir(directory)
	
	# Adds file to dir if empty
	if not contents:
		new_dt = datetime.today().date()
		new_file(new_dt, directory, prefix, postfix)
		return True
	# *** TO DO ***
	# Build initial file / template
	return False
		
def new_file(new_dt, dir, pre, post):
	'''Build and creates new file. converts datetime into date stting with correct format.'''
	date_str = new_dt.strftime("%Y.%m.%d")
	file_path = Path(dir) / f"{pre}{date_str}{post}"
	file_path.touch(exist_ok=True)
	
	return (file_path)
		
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
	
def split_todo(contents):
	# Split file sections
	split_text = contents.split("\n\n")
	
	# Create empty list 
	result = []
	# check each part of split text to find todo list section.
	for part in split_text:
		if "[ ]" in part or "[x]" in part:
			result.append(part)
	print(result)

main()