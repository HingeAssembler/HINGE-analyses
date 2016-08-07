#!/usr/bin/env python

import os
import sys
from pbcore.io import FastaIO 
import commands

seq_list = []

base_dir = 'data/'

NCTCname = sys.argv[1]
assembly_name = sys.argv[2]

embl_fl = base_dir+NCTCname+'/'+assembly_name
out_file = base_dir+NCTCname+'/'+NCTCname+"_hgap.fasta"
writer = FastaIO.FastaWriter(out_file)

with open(embl_fl,'r') as f:
    f.seek(0, os.SEEK_END)
    num_lines = f.tell()
    print num_lines
    f.seek(0)
    while 1:
        if f.tell() >= num_lines:
            break
        line_raw = f.readline()
        line = line_raw.split()

        if line[0] == 'SQ':
            #print "in ses"
            seq = ''
            next_line = f.readline()
            #print f.tell(), num_lines
            while next_line.strip() != '//':

                seqlist = next_line.split()
                seq_str = "".join(seqlist[:-1])
                seq += seq_str
                next_line = f.readline()
                #print f.tell(), num_lines
            seq_list.append(seq)

assert len(seq_list) == 1
grep_cmd = 'grep "fasta_record" '+ embl_fl
meta_data = commands.getstatusoutput(grep_cmd)[1].split('\n')
print meta_data, len(meta_data), commands.getstatusoutput(grep_cmd)

if len(meta_data) > 1:
    meta_data1 = [x.split()[2] for x in meta_data]
    start_end_tup = [(int(x.split('..')[0])-1,int(x.split('..')[-1])) for x in meta_data1]

    new_seq_list = []

    for tup in start_end_tup:
        new_seq_list.append(seq_list[0][tup[0]:tup[1]])
else:
    new_seq_list= seq_list
print len(new_seq_list)

            
for index,seq in enumerate(new_seq_list):
    zmw = index + 1 
    ls = len(seq)
    new_header = "m000_000/{zmw}/{start}_{end}".format(zmw=zmw, start=0, end=ls)
    writer.writeRecord(new_header, seq)
    
