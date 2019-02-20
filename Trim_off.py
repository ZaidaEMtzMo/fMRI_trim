#!/usr/bin/python

import glob
import os
import sys
import subprocess

path='/Path_to_your_functionalMRIscans'

bold_files=glob.glob('%s/Run[1-2].nii'%(path)) #Look for the name of your runs.

print("List of files:",bold_files)
print()
print()

for cur_bold in list(bold_files):
    print("RUNNING:",cur_bold)
    #Store directory name
    cur_dir=os.path.dirname(cur_bold)
    os.system("fslroi %s %s_trimmed 1 90" %(cur_bold, cur_bold))
    print("FINISHED")

#In the fslroi function, the second %s is the output name of the file, then the number of volumes that you want to cut (1 in this case) and then the total number of your volumes minus one (they are 91 in this case, so 90 in the function).

print("FINISHED TRIMMING OFF UNWANTED VOLUMES")
