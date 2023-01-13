"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
time = []
for i in calls:
    time.append(int(i[3]))

longer_time = max(time)

print(longer_time)
total_call = {}

for i in range(len(calls)):
    total_call[calls[i][3]] = calls[i][0]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(total_call[str(longer_time)], longer_time))

