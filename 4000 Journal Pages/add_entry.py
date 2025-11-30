# Author: Seamus Hughes
# Date: 30th November 2025
# Purpose: Add additional Markdown entry for my weekly Lifestream posts.

# ----Imported Modules----
import os # for files

# ----Functions-----

def main():
	
	# ----Variables----
	log_folder = "Lifestreams"
	split_at = "#### "
	marker = "++++"
	template = "\n\n> quote[^1]\\\n> -- *attribute*\n\n[^1]: note...."
	
	# Uses Try: / except to manage error if directory or file not present. 
	try:
		# Find file to edit
		edit_file = last_mod_file(log_folder)
	
		# open markdown file to edit
		file_contents = read_markdown_file(edit_file)
		
		# Split string to allow edit by of specific section
		first_section, search_sections = splice(file_contents, split_at)
		
		edited_sections = find_replace(search_sections, marker, template)
	
	# Allows errors to be printed on console	
	except FileNotFoundError as error:
		print(f"Error: {error}")
		exit()
	except ValueError as error:
		print(f"Error: {error}")
		exit()
	
	return first_section, edited_sections

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

def splice(contents, separator):
	'''Spliting the string but keeping the character/s that make the split in the resulting parts.'''
	
	# split contents of the file 
	# NOTE add leading space at end to clear from list
	parts = contents.split(separator)
	
	# This moves 1st section to separate list
	# We can come back to it when rebuilding the page
	first_section = parts[0]
	# Creates a seperate list of sections that i need to review and possible edit.
	following_sections = parts[1:]
	
	# replace the #### that was removed during the split 

	# NOTE: enumerate() returns place No. and object in list. allows me to directly edit the list
	for i, section in enumerate(following_sections):
		following_sections[i] = separator + section
	
	return first_section, following_sections
	
def find_replace(edit_list, find, replace):
	# Find  marker and replace is journal placeholder.
	for i, section in enumerate(edit_list):
		if find in section:
			# split section into each line
			parts = edit_list[i].split("\n")
			
			# replace marker item in section
			# parts[0] returns 1st line of sections
			edit_list[i] = section.replace(find, (parts[0]) + replace)
			
			print (edit_list[i])
			print ("-----------")
	return edit_list

# ----- 2.Identify file-----
first_section, edited_sections = main()
# ----- 3.split file-----