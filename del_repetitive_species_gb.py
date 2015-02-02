#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Script to refine the reference datasets
Deletes the repetitive species in a dataset and save the unique sequence records in a .gb file
Use it after extract_target_gene.py
Created on 23/07/2013
'''

from Bio import SeqIO
import sys

#help
if len(sys.argv) == 1:
    print ""
    print "Script to refine the reference datasets. Use it after extract_target_gene.py"
    print ""
    print "Usage: del_repetitive_species.gb amplicon_dataset.gb"
    print ""
    print ""
    sys.exit()

all_species = []
all_seqs = []
unique_species = []
unique_seqs = []
unique_records = []

input_dataset = str(sys.argv[1])

print""
print "cleaning dataset..."

# All species
for seq_record in SeqIO.parse(input_dataset, "genbank"):
    all_species.append(seq_record.annotations["organism"])

# All seqs
for seq_record in SeqIO.parse(input_dataset, "genbank"):
    all_seqs.append(seq_record.seq)


# Find the unique sequences
for seq_record in SeqIO.parse(input_dataset, "genbank"):
    query_seq = str(seq_record.seq)
    if query_seq not in unique_seqs:
        unique_seqs.append(query_seq)
        unique_species.append(seq_record.annotations["organism"])
        unique_records.append(seq_record)
        
# check if the redundant seq is from another species   
    else:
        if str(seq_record.annotations["organism"]) not in unique_species:
            unique_seqs.append(query_seq)
            unique_species.append(seq_record.annotations["organism"])
            unique_records.append(seq_record)

#print results
deleted_records = (len(all_species) - len(unique_records))
print ""

print ("number of deleted records is %i" %(deleted_records))
print ("%i species remained in the dataset" %(len(unique_records)))

# write to file
SeqIO.write(unique_records, "amplicon_dataset_unique_records.gb", "genbank")
print ""
print "Done!"
print "Proceed to gb_2_RDP.py"
print ""
