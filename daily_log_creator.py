# Author: Seamus Hughes
# Date: 27th September  2025
# Purpose: Creating a daily log using the append file function. with added log file check and path finder element

#----Imported Modules----

# Interacting with operating system including file managment
import os

# for fomating date and time. 
import datetime 

#----Functions-----


#----Variables----

# Store file_path
file_name = 'daily_log.txt'
log_folder = 'logs'
# Creating relative path for the file 
# use os.path.join() to correctly build the file path
relative_path = os.path.join(log_folder, file_name)

#-----Main Logic------
print("\n")
print(f"----Listing files is {log_folder} directory----")
# check if target directory exisits
if not os.path.exists(log_folder):
	print (f"'{log_folder}' directory does not found.")
	print (f"Please create {log_folder} before running this script.")
else:	
	try:
		# string created of all the names in directory
		items_in_Dir = os.listdir(log_folder)
		# If empty string then directory is empty
		if not items_in_Dir:
			print("The directory is empty.")
		else:
			for item_name in items_in_Dir:
				# build path to item to enqble file check 
				full_item_path = os.path.join(log_folder, item_name)
				#print out just the files, not subfolders
				if os.path.isfile(full_item_path):
					print (f"FILE:    {item_name}")
			print("\n")
			print("----scan complete----")
	except Exception as e:
		print("an error has occured")
	

# Check if file exsists at this location. 
if os.path.exists(relative_path):
	print("\n")
	print(f"Is the file {file_name} in {log_folder} present? Yes")
	print(f"The files relative path is: {relative_path}")
	absolute_path = os.path.abspath(relative_path)
	print(f"Absolute Path = {absolute_path}")
	
	print("\n")
	print(f"----Log File Inspector----")
	print(f"Analyzing file: {file_name}")
	print("\n")
	# print file path 
	print (f"File Name: {file_name}")
	# Get file size
	file_size = os.path.getsize(relative_path)
	print(f"Size: {file_size} bytes")
	mod_timestamp = os.path.getmtime(relative_path)
	# convert time stamp into datetime object. 
	mod_datetime = datetime.datetime.fromtimestamp(mod_timestamp)
	# Format timestamp into readable time. 
	format_timestamp = mod_datetime.strftime("%d.%m.%y %H:%M:%S")
	print(f"Modified: {format_timestamp}")
	# get file type
	filename_root, file_extension = os.path.splitext(relative_path)
	print(f"Extension: {file_extension}")
	print("\n")
# Returns error message if file does not exist. 
else:
	print(f"Error '{file_name}' not found. Please add an entry first to create it.")

print("---Adding a note to your daily log.----")
print("\n")

# Requesting note input from user. 
daily_note = input("What would you like to add? ")
 
try:
	# Opening a file to append 'a'.
	# If no file, file will be created. 
	with open(relative_path, 'a') as file:
		# Write the new note to the file
		file.write(daily_note)
		file.write("\n")
	
	print(f"Successfully added your note to {file_name}.")

except IOError:
    print(f"Error: Could not append to the file '{file_name}'.")

# Display the entire contents of the note. 
try:
	with open(relative_path, 'r') as file:
		# Get contents of file.
		content = file.read()		
		
		# Print out the contents of the file.
		print("Displaying your personal log")
		print("-----------------")
		print(content)
		print("-----------------")

#Error message if no file. 		
except FileNotFoundError:
	print(f"\nError: The file '{file_name}' was not found.")
	
print("\nProgram finished.")