# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:07:31 2015

@author: Van
"""

# ##Part 1: Get Chipotle File from URL and Open in Python##
# First, get file from URL using git clone git clone https://github.com/TheUpshot/chipotle.git
# Read file in command line using `head` to see what type of data it contains, and check the delimiter used in the file.



import csv

f = open('orders.tsv')
csv_f = csv.reader(f, delimiter="\t")


# ##Part 2: Separate 'file_nested_list' into the 'header' and the 'data'##
#First, create an empty list

file_nested_list = []

#Then, bring in the data into the list.
#Why do I have to append 0:5 when there are only 5 columns??? Not 0:4?

for row in csv_f:     
    file_nested_list.append(row[0:5])

#And then assign first row as header, and the rest of the rows as data 

header = file_nested_list[0]
data = file_nested_list[1:]

#Check work
#Why does the 'choice description have [] around it??? Does it affect the data?

#print header
#print data [1:10]

# ##Part 3: PART 3: Calculate the average price of an order.##
# I was trying to append a new column to calculate total price per row to account for quantity*price
# Couldn't figure out how to do it, so I took a peek at the answers and realize the item_price is already the total price!

# I wasn't sure whether item_price is 4 or 5, so I used -1 (I tried 5, and it didnt work, so I guess it is 4)
total_price = [row [-1] for row in data]
#print total_price[0:10]

# The prices are in string, and need to be changed to numbers in order to execute the calculations
# But there is a $ sign that needs to be removed

total_price = [row [-1].replace('$',' ') for row in data]

# I tried to change string to float using total_price = [float[row[-1]] for row in data]
# I cheated here - I dont understand why we have to use [1:]? 
# What is the difference between [], (), {}??

total_price = [float(row[-1][1:]) for row in data]

#print total_price[0:10]

# Calculate avergae - is there an average function?
# Why can't I do this, since I have already converted my strings to float?
#total_price_sum = sum("total_price_average")

total_price_sum = sum(float(row[-1][1:]) for row in data)
#print total_price_sum = 34500.16

# find total number of orders. This will be the total number of rows in data

print len(data)



    

f.close() 
