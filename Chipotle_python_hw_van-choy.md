##Part 1: Get Chipotle File from URL and Open in Python##

First, get file from URL using git clone

`git clone https://github.com/TheUpshot/chipotle.git`
<br> Read file in command line using `head` to see what type of data it contains, and check the delimiter used in the file. 

<br> Open spyder to import tsv file
`import csv`
<br> create object `file_nested_list = 'orders.tsv'`

Now the tsv file needs to be read as a csv. Using this code will open the tsv file with tab as a delimiter as a csv file.
<br> `with open(file_nested_list, 'r') as tsvfile:`
<br> `tsvreader = csv.reader(tsvfile, delimiter="\t")`

##Part 2: ART 2: Separate 'file_nested_list' into the 'header' and the 'data'##

`header = file_nested_list[0]`

`data = file_nested_list[1:]`




