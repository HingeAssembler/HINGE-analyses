#!/usr/bin/env python

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
        out_file_name = '/data/pacbio_assembly/pb_data/NCTC/'+nctcname+'/'+in_file_name

        if file_type == 'gff':
            cmd = 'python gff_to_fasta.py '+nctcname+' '+in_file_name
            print cmd
            os.system(cmd)
            pass
        elif file_type == 'embl':
            cmd = 'python embl_to_fasta.py '+nctcname+' '+in_file_name
            print cmd
            os.system(cmd)
        else:
            print nctcname
            raise NotImplementedError
        num_assemblies += 1
print num_assemblies
