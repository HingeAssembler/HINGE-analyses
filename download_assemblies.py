import json
import os
import numpy as np

database = json.load(file('NCTC.json'))
file_list = np.loadtxt('NCTC_names.txt',dtype='str')


num_assemblies = 0
for nctcname in file_list:
    assembly_file = database[nctcname][u'Manual Assembly'][1]
    if assembly_file != None:
        file_type = assembly_file.split(".")[-1]
        in_file_name = assembly_file.split("/")[-1]
        out_file_name = 'data/'+nctcname+'/'+in_file_name
        cmd = 'wget '+assembly_file+' -O '+out_file_name
        num_assemblies += 1
        os.system(cmd)

print num_assemblies
