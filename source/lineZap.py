#! /usr/bin/env python3

## retooling the existing textZap script for the line-a-day workflow. 
### Wednesday, May 12, 2021, 2:28 PM


import sys
import os
import re
from datetime import datetime, timedelta

myFile = os.path.expanduser(os.getenv('MYFILE'))

myInput = sys.argv[1]

# check if input starts with a negative day offset like -1, -2, etc.
match = re.match(r'^(-\d+)\s+(.*)', myInput)
if match:
    offset = int(match.group(1))
    myInput = match.group(2)
    day = datetime.now() + timedelta(days=offset)
    todayStandard = day.strftime("%Y-%m-%d %a") + " 11:59PM"
else:
    todayStandard = datetime.now().strftime("%Y-%m-%d %a %-I:%M%p")

file_content = [line for line in open(myFile)]

completeEntry = '- **' + todayStandard + '** ' + myInput + '\n'

# parse the date from the new entry to find the right insertion point
entryDate = datetime.strptime(todayStandard.split(' ')[0], "%Y-%m-%d")

# find the correct position (file is newest-first)
insertPos = 0
for i, line in enumerate(file_content):
    lineMatch = re.match(r'^- \*\*(\d{4}-\d{2}-\d{2})\s', line)
    if lineMatch:
        lineDate = datetime.strptime(lineMatch.group(1), "%Y-%m-%d")
        if lineDate <= entryDate:
            insertPos = i
            break
    insertPos = i + 1  # if no dated line found yet, insert after this line

file_content.insert(insertPos, completeEntry)

f = open(myFile, "w")
for line in file_content:
    f.write(line)
f.close()














    


    

