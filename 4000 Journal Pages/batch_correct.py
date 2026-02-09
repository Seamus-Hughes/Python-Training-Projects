# Author: Seamus Hughes
# Date: 7th Feb 2026
# Purpose: Run through .md files in directory and correct numerical order if footnotes.

import os  # For file
import re  # for Regular Expressions search

def main():
	
	# Variables
	directory = "Lifestreams"
	# This patten finds [^Num]
	# \[. \^ and \] are escaped - recognised as is in text & not code.
	# \d+ = capture one or more digits. is its in ( )
	# (?!:) = is a "negative lookahead" matches [^7] but NOT if followed by :
	pattern_ref = r"\[\^(\d+)\](?!:)"
	pattern_foot = r"\[\^(\d+)\]:"
	replace_ref = ""
	replace_foot = ":"
	
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
				
				# Correct footnote ref numbers 
				file_content = renum_foot(file_content, pattern_ref, replace_ref)
				
				# Correct footnote numbers 
				file_content = renum_foot(file_content, pattern_foot, replace_foot)
		
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

def renum_foot(text, pattern, replace):
	'''Using regular expression search to find and log footnote numbers. Then relplace with consecutive numbers.'''
	
	counter = 1
	
	# check footnotes. 
	before = re.findall(pattern, text)
	
	# This will search for the [^1] regular expression in the text
	while re.search(pattern, text):
		text = re.sub(pattern,  f"[PLACE^{counter}]"+replace, text, count=1)
		
		counter += 1
		
	# replace placeholders
	for _ in range(1, counter):
		text = text.replace("PLACE", "")
	
	# check footnotes. 
	after = re.findall(pattern, text)

	if not before == after:
		print ("differnt")
	else:
		print ("Same")
	
	return text


main()