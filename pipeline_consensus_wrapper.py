import numpy as np
import os
import multiprocessing as mp
import subprocess
import sys

base_path = 'data/'

file_list = np.loadtxt('NCTC_names.txt',dtype='str')

path_to_hinge = sys.argv[1]

num_proc = 1
if len(sys.argv) > 2:
    num_proc = int(sys.argv[2])

def run_pipeline(flname):
    base_dir = base_path + flname + '/'
    base_cmd = 'python pipeline_consensus.py '+ flname+ ' '+path_to_hinge
    print base_cmd
    subprocess.call(base_cmd, shell=True)
    
#run_pipeline(file_list[0])

pool = mp.Pool(processes=num_proc)
pool.map(run_pipeline,file_list)
