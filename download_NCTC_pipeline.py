import json
import os
import sys
import subprocess



base_dir = './'

bact_dict = json.load(open(base_dir+'NCTC.json'))

#bacterium_of_interest='NCTC7972'

bacterium_of_interest=sys.argv[1]
path_to_asperaweb_licence = sys.argv[2]
if len(sys.argv) > 3:
	bact_dict=sys.argv[3]

bact_name="_".join(bact_dict[bacterium_of_interest]['Species'][0].split())

cmd_base = 'ascp -QT -l 1000m -i '+path_to_asperaweb_licence+' era-fasp@fasp.ega.ebi.ac.uk:vol1/'
dest_dir = base_dir+'data/'+bacterium_of_interest+'/'


os.system('mkdir -p '+dest_dir)
print 'mkdir -p '+dest_dir

for run, file_list in bact_dict[bacterium_of_interest]['file_paths'].items():
    for file_path in  file_list:
        cmd = cmd_base+file_path+' '+dest_dir
        print cmd
        os.system(cmd)

dest_fasta_name = dest_dir+bacterium_of_interest

dextract_cmd = 'dextract -o'+dest_fasta_name

bax_files = [x for x in os.listdir(dest_dir) if x.endswith('.bax.h5')]

for bax_file in bax_files:
	dextract_cmd +=  " " + dest_dir+bax_file

print dextract_cmd

try:
    subprocess.check_output(dextract_cmd.split())
    print 'dextract done. deleting .bax.h5 files'
    os.system('rm '+dest_dir+'*.bax.h5')
    print 'removing .quiva files'
    os.system('rm '+dest_dir+'*.quiva')
except:
    print 'error'



