#!/usr/bin/python

import sys
import os
import subprocess


if len(sys.argv) >= 2:
	bact_id = sys.argv[1]
fasta_name = bact_id+'.fasta'
st_point = 0
if len(sys.argv) >= 3:
	st_point = int(sys.argv[2])

base_path='data/'+bact_id+"/"


if len(sys.argv) >= 4:
	base_path = sys.argv[3]



#fasta_names = [x for x in os.listdir(base_path) if x.endswith('.fasta')]
#assert len(fasta_names)==1

#fasta_name = fasta_names[0]
bact_name = fasta_name.split('.fasta')[0]

print bact_name


if st_point <= 1:
        subprocess.call("rm -f *.db",shell=True,cwd=base_path)
	fasta2DB_cmd = "fasta2DB "+bact_name+' '+fasta_name
	print fasta2DB_cmd
	subprocess.check_output(fasta2DB_cmd.split(),cwd=base_path)

if st_point <= 2:
	DBsplit_cmd = "DBsplit "+bact_name
	print DBsplit_cmd
	subprocess.check_output(DBsplit_cmd.split(),cwd=base_path)

if st_point <= 3:
        subprocess.call("rm -f *.las",shell=True,cwd=base_path)
	daligner_cmd = "HPCdaligner -M500 "+bact_name
	#daligner_cmd = "HPCdaligner -t5 "+bact_name
        daligner_shell_cmd = "csh -v daligner_cmd.sh"
	print daligner_cmd
	p = subprocess.call(daligner_cmd.split(),stdout=open(base_path+'daligner_cmd.sh','w') , cwd=base_path)
        p2 = subprocess.check_output(daligner_shell_cmd.split(), cwd=base_path)
if st_point <= 4:
	remove_cmd = "rm "+base_path+bact_name+".[0-9]."+bact_name+".*"
	print remove_cmd
	os.system(remove_cmd)

if st_point <= 5:
	LAmerge_cmd = "LAmerge "+bact_name+".las "+bact_name+".[0-9].las"
	print LAmerge_cmd
	subprocess.check_output(LAmerge_cmd,cwd=base_path,shell=True)

if st_point <= 6:
	remove_cmd2 = "rm "+base_path+bact_name+".[0-9].las"
	os.system(remove_cmd2)

if st_point <= 7:
	os.system("mkdir -p "+base_path+"log")

if st_point <= 8:
	DASqv_cmd = "DASqv -c100 "+bact_name+" "+bact_name+".las"
	subprocess.check_output(DASqv_cmd.split(),cwd=base_path)

