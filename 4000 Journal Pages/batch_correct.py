# Author: Seamus Hughes
# Date: 31st January 2026
# Purpose: Run through .md files in directory and correct numerical order if footnotes.

import os  # For file
import re  # for Regular Expressions search

def main():
	
	# Variables
	directory = "Lifestreams"
	# This patten finds [^Num]
	# \[. \^ and \] are escaped - recognised as is in text & not code.
	# \d+ = capture one or more digits.
	# (?!:) = is a “negative lookahead” matches [^7] but NOT if followed by :
	pattern_ref = r"\[\^(\d+)\](?!:)"
	pattern_foot = r"\[\^(\d+)\]:"
	
	# Uses Try: / except to manage error if directory or file not present.
	try:
		# Create list of files in output folder
		contents = os.listdir(directory)
		# Test print
		for file in contents:
			# Create full path to the file
			source_path = os.path.join(directory, file)
			# check is file
			if os.path.isfile(source_path):	
				# read file contents
				file_content = read_markdown_file(source_path)
				print(source_path)
				
				# check footnotes. 
				footnotes = re.findall(pattern_ref, file_content)
				print(f"Inital footnote ref No.: {footnotes}")
				
				#replace_footnote_numbers(file_content)
		
	# Allows errors to be printed on console
	except (FileNotFoundError, ValueError, IsADirectoryError) as error:
		print(f"Error: {error}")
		exit()
		
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

def replace_footnote_numbers(text):
	'''Using regular expression search to find and log footnote numbers. Then relplace with consecutive numbers. Sepeeste approach for footnoate and reference .'''
	# This patten finds [^Num]
	# \[. \^ and \] are escaped - recognised as is in text & not code.
	# \d+ = capture one or more digits.
	# (?!:) = is a “negative lookahead” matches [^7] but NOT if followed by :
	pattern_ref = r"\[\^(\d+)\](?!:)"
	pattern_foot = r"\[\^(\d+)\]:"
	# replace numbers in numerical order.
	counter_ref = 1
	counter_foot = 1
	new_text = text

	# This will search for the [^1] regular expression in the text
	while re.search(pattern_ref, new_text):

		# Searches through the text fot a match to regx expression
		# Count=1 makes it stop once its found the 1st instance
		# FOOTNOTE is a place holder, if not there it would continue an endless loop of finding the regex match.
		# Placehoder can be removed later.
		new_text = re.sub(pattern_ref, f"[^REF{counter_ref}]", new_text, count=1)
		# increases counter by 1 each loop.
		counter_ref += 1
		# replace placeholders
		for i in range(1, counter_ref):
			new_text = new_text.replace("REF", "")

		# This will search for the [^1]: regular expression in the text
		while re.search(pattern_foot, new_text):
			new_text = re.sub(patten_foot, f"[^FOOT{counter_foot}]:", new_text, count=1)
			# increases counter by 1 each loop.
			counter_foot += 1

	# replace placeholders
	for i in range(1, counter_foot):
		new_text = new_text.replace("FOOT", "")
	return new_text


main()
