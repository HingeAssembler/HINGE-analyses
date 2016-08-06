#!/usr/bin/python

import sys
import os
import subprocess


bact_id = sys.argv[1]
path_to_hinge = sys.argv[2]
st_point = 0
if len(sys.argv) >= 4:
	st_point = int(sys.argv[3])

base_path='data/'+bact_id+"/"


if len(sys.argv) >= 5:
	base_path = sys.argv[4]




bact_name = bact_id

print bact_name

cmd = 'mkdir -p '+base_path+'log/'
os.system(cmd)

if st_point <= 1:
	Reads_filter_cmd = "Reads_filter --db "+bact_name+" --las "+bact_name+".las -x "+bact_name+" --config ~/AwesomeAssembler/utils/nominal.ini"
	print Reads_filter_cmd
	subprocess.check_output(Reads_filter_cmd,cwd=base_path, shell=True)

if st_point <= 2:
	hinging_cmd = "hinging --db "+bact_name+" --las "+bact_name+".las -x "+bact_name+" --config ~/AwesomeAssembler/utils/nominal.ini -o "+bact_name
	print hinging_cmd
	subprocess.check_output(hinging_cmd, cwd=base_path, shell=True)

if st_point <= 3:

    json_flname = base_path+bact_id+'.mapping.4.json'
    print json_flname
    if os.path.isfile(json_flname) and os.stat(json_flname).st_size > 0:
        pruning_cmd = "python "+path_to_hinge+"scripts/pruning_and_clipping.py "+bact_name+".edges.hinges "+bact_name+".hinge.list falcon "+ json_flname
    else:
        pruning_cmd = "python "+path_to_hinge+"scripts/pruning_and_clipping.py "+bact_name+".edges.hinges "+bact_name+".hinge.list A"
    print pruning_cmd
    subprocess.check_output(pruning_cmd, cwd=base_path, shell=True)
#    json_flname = base_path+bact_id+'.mapping.5.json'
#    print json_flname
#    if os.path.isfile(json_flname) and os.stat(json_flname).st_size > 0:
#        pruning_cmd = "python ~/AwesomeAssembler/scripts/pruning_and_clipping.py "+bact_name+".edges.hinges "+bact_name+".hinge.list E "+ json_flname
#    else:
#        pruning_cmd = "python ~/AwesomeAssembler/scripts/pruning_and_clipping.py "+bact_name+".edges.hinges "+bact_name+".hinge.list A"
#    print pruning_cmd
#    subprocess.check_output(pruning_cmd, cwd=base_path, shell=true)


