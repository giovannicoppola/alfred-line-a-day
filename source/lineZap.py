#! /usr/bin/env python3

## retooling the existing textZap script for the line-a-day workflow. 
### Wednesday, May 12, 2021, 2:28 PM


import re
import json
import sys
import time
import os
from datetime import datetime

today = datetime.now()
myUser = os.getlogin()



if myUser == 'root':
	myFile = os.path.expanduser(os.getenv('MYFILE_HOME'))
else:	
	myFile = os.path.expanduser(os.getenv('MYFILE'))

# dd/mm/YY
todayStandard = today.strftime("%Y-%m-%d %a %-I:%M%p")


myInput = sys.argv[1]

file_content = [ line for line in open(myFile)]


completeEntry='- **'+ todayStandard + '** ' + myInput




        
f = open(myFile,"w")
f.write(completeEntry)
f.write("\n")
for line in file_content:
	f.write(line)
    #f.write("\n")
    
  
f.close() 














    


    

