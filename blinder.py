# blinder.py
# for use in autobiographical memory scoring procedures (semi-auto) 
# where files and IDs need to be blinded (ie for PPI, session #, experimental condition,etc.)
# also sets up scoring for 2 scorers per memory, organized by weekly "sets" (assignments) 
# Takes in:
#   1. Source filepath, containing a folder with edited files labeled with old names
#   2. Destination filepath, will contain files with new names, organized by set and RA
#   3. Key.xlsx, containing mapped IDs to coded names, sets for each mem, and RA names
    


import os
import pandas as pd
import shutil

# define paths to source and destination folders
src_folder = "ADD SOURCE FILEPATH"
dest_folder = "ADD DEST FILEPATH"

# read in the spreadsheet with keys and new filenames

df = pd.read_excel("KEY.xlsx", sheet_name="all")

# iterate over each row in the spreadsheet
for index, row in df.iterrows():

    # get the old filename from the first column of the row
    old_filename = str(row[3]) + ".docx"

    # get the new filename from the second column of the row
    new_filename = str(row[4]) + ".docx"

    filename_parts = new_filename.split(".")
    new_filename = filename_parts[0] + "." + filename_parts[-1]

    # get the Researcher's name from the third column of the row
    RA_name1 = str(row[7])
    RA_name2 = str(row[8])

    setno = str(row[6]).split('.')[0]

    setname = "Set "+ setno

    # construct the full path to the source file
    src_path = os.path.join(src_folder, old_filename)

    dest_folder1 = os.path.join(dest_folder, RA_name1, setname)


    # make the destination folder if it doesn't already exist
    if not os.path.exists(dest_folder1):
        os.makedirs(dest_folder1)


    dest_path1 = os.path.join(dest_folder1, new_filename)
    try:
    # rename the file and move it to the new folder
        shutil.copy(src_path, dest_path1)

    except FileNotFoundError:
        print(f"File '{old_filename}' not found in source folder. Skipping...")
        continue

    dest_folder2 = os.path.join(dest_folder, RA_name2,setname)

    # make the destination folder if it doesn't already exist

    if not os.path.exists(dest_folder2):
        os.makedirs(dest_folder2)


    dest_path2 = os.path.join(dest_folder2, new_filename)
    try:
    # rename the file and move it to the new folder
        shutil.copy(src_path, dest_path2)

    except FileNotFoundError:
        print(f"File '{old_filename}' not found in source folder. Skipping...")
        continue
