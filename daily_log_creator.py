# Author: Seamus Hughes
# Date: 9th September  2025
# Purpose: Creating a daily log using the append file function. with added log file check

#----Imported Modules----

# Interacting with operating system including file managment
import os

# for fomating date and time. 
import datetime 

#----Functions-----


#----Variables----

# Store file_path
file_path = 'daily_log.txt' 

#-----Main Logic------
print("\n")
print(f"----Log File Inspector----")
print(f"Analyzing file: {file_path}")
print("\n")

# Check if file exists
if os.path.exists(file_path):
	# print file path 
	print (f"File path: {file_path}")
	# Get file size
	file_size = os.path.getsize(file_path)
	print(f"size: {file_size} bytes")
	mod_timestamp = os.path.getmtime(file_path)
	# convert time stamp into datetime object. 
	mod_datetime = datetime.datetime.fromtimestamp(mod_timestamp)
	# Format timestamp into readable time. 
	format_timestamp = mod_datetime.strftime("%d.%m.%y %H:%M:%S")
	print(f"modified: {format_timestamp}")
	# get file type
	filename_root, file_extention = os.path.splitext(file_path)
	print(f"Extention: {file_extention}")
	print("\n")
# Returns error message if file does not exist. 
else:
	print(f"Error {file_path} not found")

print("---Adding a note to your daily log.----")
print("\n")

# Requesting note input from user. 
daily_note = input("What would you like to add? ")
 
try:
	# Opening a file to append 'a'.
	# If no file, file will be created. 
	with open(file_path, 'a') as file:
		# Write the new note to the file
		file.write(daily_note)
		file.write("\n")
	
	print(f"Successfully added your note to {file_path}.")

except IOError:
    print(f"Error: Could not append to the file '{file_path}'.")

# Display the entire contents of the note. 
try:
	with open(file_path, 'r') as file:
		# Get contents of file.
		content = file.read()		
		
		# Print out the contents of the file.
		print("Displaying your personal log")
		print("-----------------")
		print(content)
		print("-----------------")

#Error message if no file. 		
except FileNotFoundError:
	print(f"\nError: The file '{file_path}' was not found.")
	
print("\nProgram finished.")
