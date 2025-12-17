#raw_sorter.py

# companion script to blinder.py, for autobiographical memory scoring
# takes in:
# 1. Edited_renamed folder (blinded files)
# 2. Personal Folders folder (parent folder to RA-specific folders, for each set/weekly assignment batch)
# 3. A set number (integer)

# The idea is that you run this script once per week at the beginning of each set (weekly assignment period) 
# to create that week's assignments for each RA

# (this is really just a file moving script... )

import os
import pandas as pd
import shutil
from os.path import isfile, join
from os import listdir

#takes files from Edited_named and puts them into Personal Folders > Raw for the Set you want
set = input("What set are you on? (p,1-5): \n")

src_folder = "PATH TO FOLDER WITH BLINDED DOCUMENTS"
personalIn = "PATH TO FOLDER THAT CONTAINS RA FOLDERS" 

RAs= os.listdir(src_folder)
RAs = [file for file in RAs if not (file.startswith('.') and not file.startswith('~')) and not file.startswith('nan')]

print(RAs)
for RA in RAs:
    print(RA)
    RApathset = src_folder + "/" + RA + "/Set %s" %(set)
    #make directory here?
    if not os.path.exists(RApathset):
        os.mkdir(RApathset)
        print("Dummy Directory", RApathset, "created")
    personalRApath = personalIn + "/" + RA + "/Raw" + "/Set %s" %(set)
    if not os.path.exists(personalRApath):
        os.mkdir(personalRApath)
        print("Directory", personalRApath, "created")

    personalRApath_scored = personalIn + "/" + RA + "/Scored" + "/Set %s" %(set)
    if not os.path.exists(personalRApath_scored):
        os.mkdir(personalRApath_scored)
        print("Directory", personalRApath_scored, "created")

    docs = [f for f in listdir(RApathset) if isfile(join(RApathset, f)) if not f.startswith('.') and not f.startswith('~')]
    for doc in docs:
        if doc.endswith('.docx'):
            docpath = RApathset + "/" + doc
            shutil.copy(docpath, personalRApath)
            print("copied")

print("Done Copying!")
