#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script to extract the target gene from a genbank dataset that has complete genomes
Download dataset from genebank
ex: tufA [Gene]
save as genbank format (full)
@author: VanessaRM
2 - Feb - 2015
"""

from Bio import SeqIO
import sys

#help
if len(sys.argv) == 1:
    print ""
    print "Script to extract the target gene from a genbank dataset containing complete genomes and etc"
    print ""
    print "Usage: extract_target_gene.py raw_downloaded_dataset.gb 23S"
    print ""
    print ""
    sys.exit()

input_reference_data = str(sys.argv[1])
gene_name = str(sys.argv[2])

store_records = []

for seq_record in SeqIO.parse(input_reference_data , "genbank"):
    for gene in seq_record.features:
        if gene.type == 'gene':
            if gene_name in gene.qualifiers['gene']:
                trimmed_record = gene.extract(seq_record.seq)
                seq_record.seq = trimmed_record
                store_records.append (seq_record)
    
counter = SeqIO.write(store_records, "amplicon_dataset.gb", "genbank")

print "Done! %i records saved in your dataset - 'amplicon_dataset.gb'" %(counter)
print "proceed to del_repetitive_species_gb.py"
