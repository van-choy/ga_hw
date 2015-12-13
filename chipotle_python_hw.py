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

'''
Copied from answer: the csv.reader has a delimeter parameter, which we set to '\t' to indicate that the file is tab-separated
with open('chipotle.tsv', mode='rU') as f:   # We temporarily refer to the file by the variable name f for file
    file_nested_list = [row for row in csv.reader(f, delimiter='\t')]   # Create a list by looping through each line in f
    
    ''' #Why mode = rU?

# ##Part 2: Separate 'file_nested_list' into the 'header' and the 'data'##
#First, create an empty list

file_nested_list = []

#Then, bring in the data into the list.

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
# I was trying to append a new column to calculate total price per row to account for quantity*price, I couldn't figure it out. Then I realized the item_price already took into account quantity

total_price = [row [-1] for row in data]
#print total_price[0:10]

# The prices are in string, and need to be changed to numbers in order to execute the calculations
# But there is a $ sign that needs to be removed

# total_price = [row [-1].replace('$',' ') for row in data]

# I tried to change string to float using total_price = [float[row[-1]] for row in data]
# [1:] alternative way to remove the $   

total_price = [float(row[-1][1:]) for row in data]

#print total_price[0:10]

# Calculate average - is there an average function?


total_price_sum = sum(float(row[-1][1:]) for row in data)
#print total_price_sum = 34500.16

# find total number of orders. This will be the total number of unique values in the first column.
print (row[0])# = 4 Why is this showing 4? Its counting the digits in 1834. Why is it not counting the number of rows in the first column?
#print len(data) = 4622. Are there 4622 rows in the data?

#sorted [data[0][0])
#sorted (data, key=lambda row: row[0]) #why is it that whatever column I sort returns the same results?
#print data [-1]
#looks like there are 1834 orders? But I am not sure if every number from 1-1834 are used in the list.

#print header
#csv.DictReader(file_nested_list, fieldnames='order_id')
#I am trying to print the first column, but cannot get it to work

#wWhy is it that when I interchange data with header, I get the first character of each header column?
#for column in file_nested_list:
    #print column[0]

#Why cant I split the data?
#for column in data.split(" "):
    #print column[0]

#Calculate average rounded to 2 dc = 18.81
Average_price_order = round(sum(float(row[-1][1:]) for row in data) / 1834, 2)
print Average_price_order

#unique = range [0:1834]
#len(unique)

order_ids = [column [0] for column in data]
#print order_ids

#count unique IDs (I cheated)

unique_order_ids = set(order_ids)
num_orders = len(unique_order_ids)
sorted(unique_order_ids) #why is it not sorting?
#print unique_order_ids
    
#PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
sodas = []
for row in data:
    if 'Canned' in row[2]:
        sodas.append(row[3][1:-1])

unique_sodas = set(sodas)
print unique_sodas

#set(['Sprite', 'Coke', 'Lemonade', 'Coca Cola', 'Diet Dr. Pepper', 'Diet Coke', 'Dr. Pepper', 'Nestea', 'Mountain Dew'])


#PART 5: Calculate the average number of toppings per burrito.
#First step will be to create a list of burrito orders and count the total number of orders(rows)
#Second step will be to count the number of words in the description column per row where Burrito appears and total it up
#Lastly, calculate the average 

burrito_orders = []
for row in data:
    if 'Burrito' in row[2]:
        burrito_orders.append(row[3])

print len(burrito_orders)    #1172 Burrito orders

number_of_toppings = 0 
for row in data:
    if 'Burrito' in row[2]:
        number_of_toppings += (row[3].count(',') + 1) #6323. 

print number_of_toppings

#Average number of toppings
Average_toppings = round(float(number_of_toppings)/len(burrito_orders),2)
print Average_toppings #5.4

#PPART 6: Create a dictionary in which the keys represent chip orders and the values represent the total number of orders.

#First, explore the types of chips existing in orders
#


'''
Working

#To return a unique set of chips order (Option 1)
types_of_chips = []
for row in data:
    if 'Chip' in row[2]:
        types_of_chips.append(row[2])

unique_chips = set(types_of_chips)
print unique_chips
print len(unique_chips)

#To return a unique set of chips order (Option 2)              
unique_chips = set([row[2] for row in data if 'Chip' in row [2]])   
print unique_chips
print len('unique_chips')


#'Chips and Roasted Chili-Corn Salsa', 'Chips and Tomatillo-Red Chili Salsa', 'Chips and Mild Fresh Tomato Salsa', 'Chips and Guacamole', 'Chips and Fresh Tomato Salsa', 'Chips and Tomatillo Red Chili Salsa', 'Chips and Tomatillo-Green Chili Salsa', 'Side of Chips', 'Chips and Roasted Chili Corn Salsa', 'Chips', 'Chips and Tomatillo Green Chili Salsa'])
#Looks like there are 12 unique chip types, but some are just duplicated because of the '-' in the middle. They need to be replaced.


unique_chips = set([row[2].replace('-', ' ') for row in data if 'Chip' in row [2]])  
print unique_chips
print len (unique_chips)

## chips = ['Chips and Mild Fresh Tomato Salsa', 'Chips and Guacamole', 'Chips and Fresh Tomato Salsa', 'Chips and Tomatillo Red Chili Salsa', 'Side of Chips', 'Chips and Roasted Chili Corn Salsa', 'Chips', 'Chips and Tomatillo Green Chili Salsa']   


#Create dictionary 

'''
chips = {}

for row in data:
    if 'Chips' in row[2]:
        if row[2] not in chips:
            chips[row[2].replace('-', ' ')] = int(row[1])
        else:
            chips[row[2].replace('-', ' ')] += int(row[1]) 

print chips

'''

#Couldn't figure it out, so I copied this over from answers, and added replace '-' to get rid of the duplicated items.



from collections import defaultdict
dchips = defaultdict(int)

for row in data:
    if 'Chips' in row[2]:
        dchips[row[2].replace('-', ' ')] += int(row[1])
        
dict(dchips)
print dchips

#Here's the dictionary: {'Chips and Mild Fresh Tomato Salsa': 1, 'Chips and Guacamole': 506, 'Chips and Fresh Tomato Salsa': 130, 'Chips and Tomatillo Red Chili Salsa': 75, 'Side of Chips': 110, 'Chips and Roasted Chili Corn Salsa': 41, 'Chips': 230, 'Chips and Tomatillo Green Chili Salsa': 78})
'''

f.close() 
