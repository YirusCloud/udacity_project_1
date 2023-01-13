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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
number = []

for c in calls:
    if '140' in c[0] and c[0][0] == '1':
        number.append(c[0])

unique_number = set(number)

all_number = []

for c in calls:
    all_number.append(c[1])
    
for t in texts:
    all_number.append(t[0])

for t in texts:
    all_number.append(t[1])

telemarketers = []

for n in unique_number:
    if n not in all_number:
        telemarketers.append(n)

print("These numbers could be telemarketers: {} ".format(telemarketers))

