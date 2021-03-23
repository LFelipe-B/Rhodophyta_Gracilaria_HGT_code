This repository contains codes and tables used to infer horizontal gene transfer (HGT) events and calculate stats derived from these data, using as query the red algae (Rhodophyta) genome from the species Gracilaria dominguensis. Analysis were run betwen September-January 2020-2021.

File list:

# g_domingensis_CDS.fasta_GC123_distrib.csv
Table containing the subset of CDSs from putative HGT events GC ratio of the third codon position (GC3)

# hgtCDS_felipe.fasta_GC123_distrib.csv
Table containing the full CDSs from putative HGT events GC ratio of the third codon position (GC3)

# gd_proteins_diamond_lineages_renamed.tsv_full_HGT_dist_raw.csv
Table containing the raw results from the script "Get_HGT_indexes_V5_rhodophyta.py"

# gd_proteins_diamond_lineages_renamed.tsv_HGT_index_raw.csv
Table containing the raw results from the script "Get_HGT_tax_distribution_rhodophyta_V1.py"

# Get_HGT_indexes_V5_rhodophyta.py
Script to calculate the Alien and HGT indexes from taxonomically annotated diamond outputs (for blast it would require some customization for the file format, as well if you use a blast output

# get_sequence_GC3.py
Script to calculate the GC3 in the third codon position using a CDSs list (in fasta format)

# HGT_list_per_scaffold_sorted.csv
Name and number of scaffolds where a HGT event was found

# Gracilaria_GC3_scaffold_dist_stats_2021.txt
Statistical tests run in R to test for GC3 differences in HGT candidates and for distribution of HGT events in scaffolds
