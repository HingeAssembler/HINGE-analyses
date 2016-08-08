#!/usr/bin/env python


import sys
import os
import subprocess

bact_id = sys.argv[1]
path_to_hinge = sys.argv[2]

base_path='data/'+bact_id+"/"

st_point = 0
if len(sys.argv) > 3:
    st_point = int(sys.argv[3])
    
old_fasta_name = bact_id+'_hgap.fasta'
hgap_db_name = bact_id+'_hgap'
db_name = bact_id
fasta_name = bact_id+'_hgap_pb.fasta'
laname = hgap_db_name + "." +  db_name + '.las'

if st_point <= 1:
    subprocess.call("python "+path_to_hinge+"scripts/correct_head.py  "+ old_fasta_name+" "+ fasta_name+ " hgapgt.txt",shell=True,cwd=base_path)
    subprocess.call("rm -f *_hgap.db",shell=True,cwd=base_path)
    fasta2DB_cmd = "fasta2DB "+hgap_db_name+' '+fasta_name
    print fasta2DB_cmd
    subprocess.check_output(fasta2DB_cmd.split(),cwd=base_path)
    
if st_point <= 2:
    subprocess.call("rm -f *_hgap.*.las",shell=True,cwd=base_path)
    mapper_cmd = "HPCmapper "+hgap_db_name+" "+db_name
    print mapper_cmd
    mapper_shell_cmd = "bash -v mapper_cmdf.sh"
    p = subprocess.call(mapper_cmd.split(),stdout=open(base_path+'mapper_cmdf.sh','w') , cwd=base_path)
    p2 = subprocess.check_output(mapper_shell_cmd.split(), cwd=base_path)
    
if st_point <= 3:
    rename = hgap_db_name + "*." +  db_name + '*.las'
    LAmerge_cmd = "LAmerge "+laname+" "+rename
    print LAmerge_cmd
    subprocess.check_output(LAmerge_cmd,cwd=base_path,shell=True)
    
if st_point <= 4:
    mp_cmd = "python "+path_to_hinge+"scripts/run_mapping2.py "+hgap_db_name+" "+db_name+" "+laname+' 1-$ 4'
    print mp_cmd
    subprocess.check_output(mp_cmd, cwd=base_path, shell=True)
    
