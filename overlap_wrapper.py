import numpy as np
import os
import multiprocessing as mp
import subprocess
import sys

base_path = 'data/'

file_list = np.loadtxt('NCTC_names.txt',dtype='str')

num_proc = 1
if len(sys.argv) > 1:
    num_proc = sys.argv[1]


def run_pipeline(flname):
    base_dir = base_path + flname + '/'
    base_cmd = 'python pipeline_overlap.py '+ flname
    print base_cmd
    subprocess.call(base_cmd, shell=True)
    
#run_pipeline(file_list[0])

pool = mp.Pool(processes=num_proc)
pool.map(run_pipeline,file_list)
