#**Create New Homework File**#
Code: _touch Chipotle_ComLine_hw_van-choy.md_

#** Explore Chipotle File**#
Code: _cd data_
<br>
Code: _cat chipotle.tsv_
<br>Code: _head chipotle.tsv_ 
<br>
Code: _tail chipotle.tsv_
<br>
Code: _wc -l chipotle.tsv_
###Observations:###
<br> 1. Looking through the top 10 rows with the head code,  there seem to be 5 columns in the file, describing the quantity of each order, item name, description, price. Pulling the entire file using the Cat code, I noticed that the file is very long. 

<br> 2. Using the tail code to pull the last 10 rows: The file appears to be sorted by 'order id' from 1 through 1834. There seem to be duplicate IDs. There are 1834 orders.

<br> 3. With the wc -l command, I can see that there are 4623 rows (lines) in the file. There are multiple rows for each order ID because each order can have multiple items.

#**Chicken or Steak?**#
Code: ``cat chipotle.tsv | grep Burrito | wc -w``

This command shows 'Burrito' appeared 17669 times in the file, 'Steak' appeared 10726, and 'Chicken '23204' times. However, it doesn't take into account the quantity of each occurance in column 2.

<br> Then i realized the question was asking for Chicken Burrito and Steak Burrito. So I used ``grep -c "Chicken Burrito" chipotle.tsv`` and counted 553 Chicken Burrito, and 368 Steak Burrito. So Chicken seem to occur more times. But I still dont know the quantity ordered of each occurance.

<br> I have no idea! After searching resources on the web (for a long time!) I found this code: ``cat chipotle.tsv | grep "Chicken Burrito" | awk '{ sum+=$2} END {print sum}'``. 

<br> 4. Not sure if it is correct, but Chicken Burrito counted 591 orders, and Steak Burrito counted 386. Sounds correct? So Chicken Burrito is more popular.

#**Pinto or Black?**#
So assuming my code for Q4 is correct, I continue on the same train of thought, using the following code.

Code: ``cat chipotle.tsv | grep "Chicken Burrito" | grep -c Pinto``

<br> 5. The number of times Pinto appears in Chicken Burrito is 105, while Black appears 282 times. So Chicken Burrito more often have Black Beans.

grep -r dictionary . | wc

``find . -name *.csv -or -name *.tsv``
<br>
<br> 6. There are 13 files with .csv/.tsv in the directory
<br>
./data/airlines.csv
./data/bank-additional.csv
./data/bikeshare.csv
./data/chipotle.tsv
./data/drinks.csv
./data/hitters.csv
./data/imdb_1000.csv
./data/sms.tsv
./data/titanic.csv
./data/ufo.csv
./data/vehicles_test.csv
./data/vehicles_train.csv
./data/yelp.csv


#**Find Number of Occurances for 'dictionary'**#

``grep -r 'dictionary' * | wc -l``

Resulted in 88 counts, but I think this only count the number of lines with 'dictionary'.

`cat * | grep -r 'dictionary' * | wc -w`

<br> 7. This resulted in 1447 counts. Not sure if it is right.

#**Interesting things**#

`uniq chipotle.tsv | wc -l`

There are 4589 unique lines in the file out of a total of 4623

``sort -k 5 chipotle.tsv | head``

Looks like the cheapest item on th menu is Chips for $1.99, but they also sell the same item 'chips' for $2.15? Price increased?
<br>
1793	1	Chips	NULL	$1.99 
1005	1	Chips	NULL	$2.15 
1006	1	Chips	NULL	$2.15 
1008	1	Chips	NULL	$2.15 
1015	1	Chips	NULL	$2.15 
1034	1	Chips	NULL	$2.15 
1045	1	Chips	NULL	$2.15 
1074	1	Chips	NULL	$2.15 
1074	1	Chips	NULL	$2.15 
1076	1	Chips	NULL	$2.15 
