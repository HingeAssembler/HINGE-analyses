#!/usr/bin/env python


import numpy as np
import os
import sys

file_list = np.loadtxt('NCTC_names.txt',dtype='str')

cmd1 = 'rm ./data/'

path_to_licence = sys.argv[1]

try:
	
	for fl in file_list:
		cmdf = cmd1+fl+'/*'
		print cmdf
		cmd = 'python download_NCTC_pipeline.py '+fl+' '+ path_to_licence
		print cmd
		os.system(cmdf)
		os.system(cmd)

except: # file_list has a single name 

	fl = str(file_list)
	cmdf = cmd1+fl+'/*'
	print cmdf
	cmd = 'python download_NCTC_pipeline.py '+fl+' '+ path_to_licence
	print cmd
	os.system(cmdf)
	os.system(cmd)
