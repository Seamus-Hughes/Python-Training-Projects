# Author: Seamus Hughes
# Date: 27th May 2025
# Purpose: Open a file and read the contents.
#----Imported Modules----


#----Functions-----


#----Variables----

# Store file_path
file_path = 'my_story.txt' 

#-----Main Loop------
print(f"Attempting to open and read the file: {file_path}\n\n")
 
try:
	# Opening a file to read 'r'.
	with open(file_path, 'r') as file:
		# Get contents of the file
		content = file.read()
		
		#Print out the cobtebts of the file.
		print("Displaying your story")
		print("-----------------")
		print(content)
		print("-----------------")

#Error messege if no file. 		
except FileNotFoundError:
	print(f"\nError: The file '{file_path}' was not found.")
	print("Please make sure you have created 'my_story.txt' in the same directory as this script.")

print("\nProgram finished.")
		
		
