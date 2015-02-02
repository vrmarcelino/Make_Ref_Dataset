#!/bin/bash
#PBS -V
#PBS -N Ref_dataset
#PBS -k eo
#PBS -l nodes=3:ppn=3

# 02 - Fev - 2015

echo "Launching....."

echo "extracting genes"
extract_target_gene.py Ulvophceae_GenBank.gb tufA

echo "cleaning dataset - del repetitive entries"
del_repetitive_species_gb.py amplicon_dataset.gb

echo "GenBank to RDP"
gb_2_RDP.py amplicon_dataset.gb

echo "End! Now add the fasta Ostreobium Seqs that we have (Thomas Sauvage) to these files"