"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_number = []
for c in calls:
    unique_number.append(c[0])
    
for c in calls:
    unique_number.append(c[1])
    
for t in texts:
    unique_number.append(t[0])

for t in texts:
    unique_number.append(t[1])   

print("There are {} different telephone numbers in the records.".format(len(set(unique_number))))