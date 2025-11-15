# Author: Seamus Hughes
# Date: 15th November 2025
# Purpose: Add additional Markdown entry for my weekly Lifestream posts.

# ----Imported Modules----
import os # for files

from datetime import datetime  # For date management

# ----Functions-----


# ----Variables----
log_folder = "Lifestreams"

# ----- 1. Setup-------


# ----- 2.Identify file-----


# Create list of files in Lifestreams folder
output_contents = os.listdir(log_folder)

# variables to check the most recent file
most_recent_file = None
# NOTE 'None' is used to create an empty variable
most_recent_time = 0
# NOTE files will have modification time greater that 0

# Loop through log folder
for item_name in output_contents:
	# Create full path to the file
	source_path = os.path.join(log_folder, item_name)
	
	# Check so only process files not Directories.
	if os.path.isfile(source_path):
		# get modification times for this file
		source_mod_time = os.path.getmtime(source_path)
		
		#If this file is newer that current most recent
		if source_mod_time > most_recent_time:
			most_recent_time = source_mod_time
			most_recent_file = source_path