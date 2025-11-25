# Author: Seamus Hughes
# Date: 25th November 2025
# Purpose: Add additional Markdown entry for my weekly Lifestream posts.

# ----Imported Modules----
import os # for files

# ----Functions-----

def last_mod_file(directory):
	'''Compare all files in defined directory. Compare date last modified, returning file last modified.'''
	
	# Check the directory exists
	if not os.path.exists(directory):
		raise FileNotFoundError(f"Directory {directory} not present")
	
	# Create list of files in Lifestreams folder
	output_contents = os.listdir(directory)
	
	# variables to check the most recent file
	most_recent_file = None
	# NOTE 'None' is used to create an empty variable
	most_recent_time = 0
	# NOTE files will have modification time greater that 0
	
	# Loop through log folder
	for item_name in output_contents:
		# Create full path to the file
		source_path = os.path.join(directory, item_name)
		
		# Check so only process files not Directories.
		if os.path.isfile(source_path):
			# get modification times for this file
			source_mod_time = os.path.getmtime(source_path)
			
			#If this file is newer that current most recent
			if source_mod_time > most_recent_time:
				most_recent_time = source_mod_time
				most_recent_file = source_path
	
	# Check for any files 
	if most_recent_file is None:
		raise FileNotFoundError(f"No files found in {directory}!")

	# Return the name of file last saved	
	return most_recent_file

def read_markdown_file(markdown_file):
	'''Opens markdown file and saves contents to a string'''
	
	# Check markdown file extension
	if not markdown_file.endswith(".md"):
		raise ValueError(f"File '{markdown_file}' is not a markdown file.")
	
	# open file file to edit
	# NOTE open() checks if file exists and open() checks if it’s actually a file (not a directory). 
	# Will return a error message automatically. 
	# NOTE encoding="utf-8" used to ensure Markup characters in markdown recognised
	with open (markdown_file, "r", encoding="utf-8") as file:
		file_contents = file.read()
		
	# Return the contents of markdown file as a string	
	return file_contents
	

# ----Variables----
log_folder = "Lifestreams"

# ----- 1. Setup-------


# ----- 2.Identify file-----

# Uses Try: / except to manage error if directory or file not present. 
try:
	# Find file to edit
	edit_file = last_mod_file(log_folder)
	
	# open markdown file to edit
	file_contents = read_markdown_file(edit_file)
	
# Allows errors to be printed on console	
except FileNotFoundError as error:
	print(f"Error: {error}")
	exit()
except ValueError as error:
	print(f"Error: {error}")
	exit()

# ----- 3.split file-----
		
# split contents of the file 
# NOTE add leading space at end to clear from list
parts = file_contents.split("#### ")

# This moves 1st section to separate list
# We can come back to it when rebuilding the page
intro_section = parts[0]
# Creates a seperate list of sections that i need to review and possible edit.
search_sections = parts[1:]

# Find  marker and replace is journal placeholder.
# NOTE: enumerate() returns place No. and object in list. allows me to directly edit the list 
for i, section in enumerate(search_sections):
	if "++++" in section:
		
		print (section)
		print ("-----------")
		
		# Modify actual list item in list
		search_sections[i] = section.replace("++++", "New stuff!!!!")
		
		print (search_sections[i])
		print ("-----------")
		
		

