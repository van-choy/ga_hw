# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:07:31 2015

@author: Van
"""

import csv

file_nested_list = 'orders.tsv'

with open(file_nested_list, 'r') as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    

header = file_nested_list[0]
data = file_nested_list[1:]
    
print len(header)

print len(data)

