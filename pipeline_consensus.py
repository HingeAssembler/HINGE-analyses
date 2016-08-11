#!/usr/bin/python

import sys
import os
import subprocess


if len(sys.argv) >= 2:
	bact_id = sys.argv[1]

path_to_hinge = sys.argv[2]
st_point = 0
if len(sys.argv) >= 4:
	st_point = int(sys.argv[3])

base_path='data/'+bact_id+"/"
#base_path='/data/pacbio_assembly/pb_data/NCTC/timing/'+bact_id+"/"




if st_point <= 1:
    draft_path_cmd = 'python '+path_to_hinge+'scripts/get_draft_path.py '+base_path[:-1]+ ' '+ bact_id+ ' '+base_path+bact_id+'A.G2.graphml'
    print draft_path_cmd
    subprocess.check_output(draft_path_cmd, shell=True)

if st_point <= 2:
    draft_assembly_cmd = 'draft_assembly --db '+bact_id+' --las '+bact_id+'.las --prefix '+bact_id+' --config '+path_to_hinge+'utils/nominal.ini --out '+bact_id+'.draft'
    print draft_assembly_cmd
    subprocess.check_output(draft_assembly_cmd,cwd=base_path, shell=True)
    
if st_point <= 3:
    corr_head_cmd = 'python '+path_to_hinge+'scripts/correct_head.py '+bact_id+'.draft.fasta '+bact_id+'.draft.pb.fasta draft_map.txt'
    print corr_head_cmd
    subprocess.check_output(corr_head_cmd,cwd=base_path, shell=True)

if st_point <= 4:
    subprocess.call("rm -f draft.db",shell=True,cwd=base_path)
    fasta2DB_cmd = "fasta2DB draft "+bact_id+'.draft.pb.fasta'
    print fasta2DB_cmd
    subprocess.check_output(fasta2DB_cmd.split(),cwd=base_path)


if st_point <= 5:
    subprocess.call("rm -f draft.*.las",shell=True,cwd=base_path)
    mapper_cmd = "HPCmapper draft "+bact_id
    mapper_shell_cmd = "bash -v draft_consensus.sh"
    p = subprocess.call(mapper_cmd.split(),stdout=open(base_path+'draft_consensus.sh','w') , cwd=base_path)
    p2 = subprocess.check_output(mapper_shell_cmd.split(), cwd=base_path)


if st_point <=6:
    remove_cmd = 'rm -f draft.*.'+bact_id+'.*.las'
    subprocess.call(remove_cmd,shell=True,cwd=base_path)
    LAmerge_cmd = "LAmerge draft."+bact_id+".las "+'draft.'+bact_id+'.[0-9].las'
    print LAmerge_cmd
    subprocess.check_output(LAmerge_cmd,cwd=base_path,shell=True)
    
if st_point <= 7:
    consensus_cmd = 'consensus draft '+bact_id+' draft.'+bact_id+'.las '+bact_id+'.consensus.fasta '+path_to_hinge+'utils/nominal.ini'
    print consensus_cmd
    subprocess.check_output(consensus_cmd,cwd=base_path,shell=True)
    
if st_point <= 8:
    gfa_cmd =  'python '+path_to_hinge+'scripts/get_consensus_gfa.py '+base_path[:-1]+ ' '+ bact_id+ ' '+base_path+bact_id+'.consensus.fasta' 
    print gfa_cmd
    subprocess.check_output(gfa_cmd,shell=True)
