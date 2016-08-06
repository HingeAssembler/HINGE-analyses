
correct_head.py $1_reads.fasta $1_reads.pb.fasta map.txt

fasta2DB $1 $1_reads.pb.fasta

DBsplit $1

HPCdaligner $1 | bash -v

rm $1.*.$1.*.las

LAmerge $1.las $1.[0-9].las

DASqv -c100 $1 $1.las
