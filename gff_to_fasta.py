from BCBio import GFF
from pbcore.io import FastaIO
import sys

base_dir = 'data/'

NCTCname = sys.argv[1]
assembly_name = sys.argv[2]

in_file = base_dir+NCTCname+'/'+assembly_name
out_file = base_dir+NCTCname+'/'+NCTCname+"_hgap.fasta"

in_handle = open(in_file)
writer = FastaIO.FastaWriter(out_file)
for index,rec in enumerate(GFF.parse(in_handle)):
    #print index
    zmw = index + 1 
    ls = len(rec.seq)
    print len(str(rec.seq))
    new_header = "m000_000/{zmw}/{start}_{end}".format(zmw=zmw, start=0, end=ls)
    #print new_header
    writer.writeRecord(new_header, str(rec.seq))
in_handle.close()
