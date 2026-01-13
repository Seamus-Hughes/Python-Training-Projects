# Author: Seamus Hughes
# Date: 13th January 2026 
# Purpose: Add additional Markdown entry for my weekly Lifestream posts.

# ----Imported Modules----
import os # for files
import re # for Regular Expressions search

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
	
		# obtain markdown contents to edit
		file_contents = read_markdown_file(edit_file)
		
		# Split string to allow edit by of specific section
		first_section, search_sections = splice(file_contents, split_at)
		
		edited_sections = find_replace(search_sections, marker, template)
		
		# reconstruct file 
		file_reconstruct = first_section + "".join(edited_sections)
		
		#re order footnote numbers. 
		new_text = replace_footnote_numbers(file_reconstruct)
		
		# write changes to file
		with open(edit_file, 'w', encoding = "utf-8") as file:
			file.write(new_text)
		
		print("file saved")
		
	
	# Allows errors to be printed on console	
	except FileNotFoundError as error:
		print(f"Error: {error}")
		exit()
	except ValueError as error:
		print(f"Error: {error}")
		exit()
	
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
	''' Finds the marker and replaces it with journal entery placeholder'''
	
	# Find  marker and replace is journal placeholder.
	for i, section in enumerate(edit_list):
		if find in section:
			# split section into each line
			parts = edit_list[i].split("\n")
			
			# replace marker item in section
			# parts[0] returns 1st line of sections
			edit_list[i] = section.replace(find, (parts[0]) + replace)
			
	return edit_list
	
def replace_footnote_numbers(text):
	'''Using regular expression search to find and log footnote numbers. Then relplace with consecutive numbers. Sepeeste approach for footnoate and reference .'''
	# This patten finds [^Num]
	# \[. \^ and \] are escaped - recognised as is in text & not code.
	# \d+ = capture one or more digits.
	# (?!:) = is a "negative lookahead" matches [^7] but NOT if followed by :
	patten_ref = r"\[\^(\d+)\](?!:)"
	patten_foot = r"\[\^(\d+)\]:"
	# replace numbers in numerical order.
	counter_ref = 1
	counter_foot = 1
	new_text = text
	
	# This will search for the [^1] regular expression in the text
	while re.search(patten_ref,new_text):
		# Searches through the text fot a match to regx expression
		# Count=1 makes it stop once its found the 1st instance
		# FOOTNOTE is a place holder, if not there it would continue an endless loop of finding the regex match. 
		# Placehoder can be removed later.
		new_text = re.sub(patten_ref, f"[^REF{counter_ref}]", new_text, count=1)
		# increases counter by 1 each loop.
		counter_ref += 1
	# replace placeholders
	for i in range (1, counter_ref):
		new_text = new_text.replace("REF", "")
	
	# This will search for the [^1]: regular expression in the text
	while re.search(patten_foot,new_text):
		new_text = re.sub(patten_foot, f"[^FOOT{counter_foot}]:", new_text, count=1)
		# increases counter by 1 each loop.
		counter_foot += 1
		
	# replace placeholders
	for i in range (1, counter_foot):
		new_text = new_text.replace("FOOT", "")
	return new_text

main()