# Author: Seamus Hughes
# Date: 27th May 2025
# Purpose: Creating a daily log using the apend file fuction.
#----Imported Modules----


#----Functions-----


#----Variables----

# Store file_path
file_path = 'daily_log.txt' 

#-----Main Loop------
print("---Adding a note to your daily log.----")

# Requesting note imput feom user. 
daily_note = input("What would you like to add? ")
 
try:
	# Opening a file to append 'a'.
	# If no file, file will be created. 
	with open(file_path, 'a') as file:
		# Get contents of the file
		file.write(daily_note)
		file.write("\n")
	
	print(f"Successfully added your note to {file_path}.")

except IOError:
    print(f"Error: Could not append to the file '{file_path}'.")

# Display the entire contents of the note. 
try:
	with open(file_path, 'r') as file:
		content = file.read()		
		
		# Print out the contents of the file.
		print("Displaying your pesonal log")
		print("-----------------")
		print(content)
		print("-----------------")

#Error message if no file. 		
except FileNotFoundError:
	print(f"\nError: The file '{file_path}' was not found.")
	
print("\nProgram finished.")
