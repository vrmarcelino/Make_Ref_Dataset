#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Clean Reference dataset after the ref_sequences.fna 
and id_to_taxonomy_map.txt files have been produced

23 - Feb - 2015
"""

from Bio import SeqIO
import sys

help
if len(sys.argv) == 1:
    print ""
    print "Clean Reference dataset after the ref_sequences.fna and id_to_taxonomy_map.txt files have been produced"
    print ""
    print "Usage: clean_reference_data.py reference_seqs.fna id_to_taxonomy_map.txt"
    print ""
    print ""
    sys.exit()

input_reference_seqs = str(sys.argv[1])
input_id_to_taxonomy_map = str(sys.argv[2])

store_seqs = []
store_ids = []

# delete seqs smaller than 100 bp:
for seq_record in SeqIO.parse(input_reference_seqs , "fasta"):
    if len(seq_record.seq) >= 100:
        store_seqs.append(seq_record)
        store_ids.append(seq_record.id)


# clean the id_to_taxonomy_map
id_map = open(input_id_to_taxonomy_map, "r")
store_clean_ids = []

counter = 0
for line in id_map:
    identifier = line.split('\t')
    if identifier[0] in store_ids:
        store_clean_ids.append(line)
    else:
        counter += 1

#Save:
SeqIO.write(store_seqs, "clean_reference_sequences.fna", "fasta")

savefile = open("clean_id_to_taxonomy_map.txt", "w")
for lines in store_clean_ids:
    savefile.write("%s\n" % lines)

print "%i records smaller than 100bp were deleted from your dataset" %(counter)
