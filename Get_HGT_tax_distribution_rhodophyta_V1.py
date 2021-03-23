#!/usr/bin/python

# This script was writen in 17/09/2020 based in a previous script (HGT tax distribution V6) to calculate distribution of taxa in blast outputs based in non duplicated scientific names in a given category (here nontarget=everything which is not an eukaryote)

import pandas as pd
import numpy
import numpy as np
import sys
import csv

# import and load csv file
f = open(sys.argv[1])

data = pd.read_csv((f), delimiter='\t')

# remove taxa or group which is same from genome of interest
data = data[data.Lineage.str.contains(";Gracilariaceae;") == False]

# insert new column with category (nontarget and target) according to data in Lineage column and according with desired target group (Eukaryota or Bacteria etc.) and nontarget (Viruses or Bacteria etc.)
data.loc[data.Lineage.str.contains("Viruses;|;Bacteria|;Archaea;",na=False,case=True), 'category'] = 'nontarget'
data.loc[data.Lineage.str.contains(";Eukaryota;",na=False,case=True), 'category'] = 'target'

# String to be searched
search ="nontarget"

# remove duplicated scientific names
data = data.drop_duplicates(subset=['Query', 'Scientific_name'], keep='first')

# count occurrence distribution of string (word) and create new column (count_tax, search=nontarget) based on species name
data["count_tax"]= data["category"].str.count(search)

# create pivot dataframe (df) in this case "pivot" with 3 cols Query, count (number of lines (hits) of Query), and sum (number of times of searched word - string was found in this case "virus")
pivot = data.pivot_table(index= 'Query', values= "count_tax", aggfunc={'sum','count'})

# create new col in pivot df with name "next" and get results from number of lines of seq_tag divided by 2 (half of total of lines in Scientific_name #
pivot['next'] = pivot['count']/2

# create new col in pivot df with name "Taxon dist HGT" that compares sum(number of times that word string was found) and get true and false to keep and discard (keep if TRUE and discard if FALSE)
"""KEEP: n of nontarget - count tax is > (greater) than n of lines (of hits)
    DISCARD: n of target - count tax is > (smaller) than n of lines (of hits)"""
pivot['Taxon dist HGT'] = pivot['sum'] > pivot['next']

# change col names from 'count, sum, next, keep/discard' to 'n of hits', 'n of viruses','half n of hits', 'Taxon dist HGT'. This should be raw table#
pivot.columns = ['n of total hits', 'n of nontarget','half n of total hits', 'Taxon dist HGT']


# print this raw table
pivot.to_csv(sys.argv[1] + '_full_HGT_dist_raw.csv')

# drop columns from row table
drop_cols = pivot.drop(['n of total hits', 'n of nontarget','half n of total hits'], axis=1) # more than one value needs brackets

# print final files
drop_cols.to_csv(sys.argv[1] + '_full_HGT_dist_final.csv')
