# Author: Seamus Hughes
# Date: 10th March 2026
# Purpose: correct a markdown numbered list. Make numbers concurrent. 

# ----Imported Modules----
import os  # for files
import re # for search and replace 
from itertools import count # for coubter in find and replace

def main():
	
	# ----Variables----
	log_folder = "Lists"
	
	# Uses Try: / except to manage error if directory or file not present.
	try:
		# Find file to edit
		edit_file = last_mod_file(log_folder)
		print(edit_file)
		
		# Get contents of file 
		text = read_markdown_file(edit_file)
	
		print(text)
		
		# creates a numeric counter starting from 1 and inc by 1 every time called.  (from itertools)
		counter = count(1)
		
		# using re.sub for complex search and replace ie patten matching
		# \n at front of both text to acoid swaping out No. in title date
		# lambda is a minimal function definition that can be used inside an expression.
		text = re.sub(r"\n\d+\.", lambda m: f"\n{next(counter)}.", text)
		
		print(text)
		ref = ordered_footnotes(text)
		print(ref)
		
		# write changes to file
		with open(edit_file, 'w', encoding="utf-8") as file:
			file.write(text)
		
	# Allows errors to be printed on console
	except FileNotFoundError as error:
		print(f"Error: {error}")
		exit()
	except ValueError as error:
		print(f"Error: {error}")
		exit()
		

# ----Functions-----

def val_dir(directory):
	'''Checks if directory exists and raises an error if not.'''
	if not os.path.exists(directory):
		raise FileNotFoundError(f"Directory {directory} not present")


def last_mod_file(directory):
	'''Compare all files in defined directory. Compare date last modified, returning file last modified.'''
	# check for directory
	val_dir(directory)
	
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

			# If this file is newer that current most recent
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
	with open(markdown_file, "r", encoding="utf-8") as file:
		file_contents = file.read()

	# Return the contents of markdown file as a string
	return file_contents

def ordered_footnotes(text):
	
	# This patten finds [^Num]
	# \[. \^ and \] are escaped - recognised as is in text & not code.
	# \d+ = capture one or more digits.
	# (?!:) = is a “negative lookahead” matches [^7] but NOT if followed by :
	patten_ref = r"\[\^(\d+)\](?!:)"
	patten_foot = r"\[\^(\d+)\]:"
	
	inline_ref = re.findall(patten_ref,text)

	return inline_ref
def replace_footnote_numbers(text):
	'''Using regular expression search to find and log footnote numbers. Then relplace with consecutive numbers. Sepeeste approach for footnoate and reference .'''
	# This patten finds [^Num]
	# \[. \^ and \] are escaped - recognised as is in text & not code.
	# \d+ = capture one or more digits.
	# (?!:) = is a “negative lookahead” matches [^7] but NOT if followed by :
	patten_ref = r"\[\^(\d+)\](?!:)"
	patten_foot = r"\[\^(\d+)\]:"
	# replace numbers in numerical order.
	counter_ref = 1
	counter_foot = 1
	new_text = text

	# This will search for the [^1] regular expression in the text
	while re.search(patten_ref, new_text):

		# Searches through the text fot a match to regx expression
		# Count=1 makes it stop once its found the 1st instance
		# FOOTNOTE is a place holder, if not there it would continue an endless loop of finding the regex match.
		# Placehoder can be removed later.
		new_text = re.sub(patten_ref, f"[^REF{counter_ref}]", new_text, count=1)
		# increases counter by 1 each loop.
		counter_ref += 1
	# replace placeholders
	for i in range(1, counter_ref):
		new_text = new_text.replace("REF", "")

	# This will search for the [^1]: regular expression in the text
	while re.search(patten_foot, new_text):
		new_text = re.sub(patten_foot, f"[^FOOT{counter_foot}]:", new_text, count=1)
		# increases counter by 1 each loop.
		counter_foot += 1

	# replace placeholders
	for i in range(1, counter_foot):
		new_text = new_text.replace("FOOT", "")
	return new_text
	
main()
