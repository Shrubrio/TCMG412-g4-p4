from urllib.request import urlretrieve
import urllib.request
import os.path
from os import path
import re
from collections import Counter

#variables
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local = 'logfile.txt'
dates = []
Files = {}
filenames = []
errorcodes = []
numdate = []
num1dates = []
yeartotal = []
NumMonth = {}
code4 = 0
code3 = 0


#check if file is present
if path.isfile('logfile.txt') == False:
    print('downloading log file...')
    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve (url, 'logfile.txt')
    print('done')
else: print('this file is already present on your workstation')
    

#open file
open_log = open('logfile.txt', 'r')
#seperating needed data
for row in open_log: 
    split = row.split(' ')
    if(len(split) > 8):
        errorcodes.append(split[8])
        filenames.append(split[6])
    if(len(split[3]) > 14):
        dates.append(split[3]) 
#counting result code instances
for issues in errorcodes: 
    if(issues[0] == '3'):
        code3 = code3 + 1
    if(issues[0] == '4'):
        code4 = code4 + 1
 #getting code instances in percent format
code3percent = (code3 / len(dates)) * 100
code3percent = "{:.2f}".format(code3percent)
code4percent = (code4 / len(dates)) * 100
code4percent = "{:.2f}".format(code4percent)
#individualising dates
for date in dates:
    numdate.append(date[1:12])
    num1dates.append(date[1:3])

for d in num1dates:
    if(d in NumMonth):
        NumMonth[d] += 1
    else:
        NumMonth[d] = 1
        
for file in filenames:
    if(file in Files):
        Files[file] += 1
    else:
        Files[file] = 1      
        
most_requested = max(Files, key=Files.get)
least_requested = min(Files, key=Files.get)

print("How many requests were made on each day?")
for a, b in sorted(NumMonth.items()):
	print("{} : {}".format(a,b))
print('----------------------------------------')

print("How many requests were made on a week-by-week basis?")
print()

print("How many requests were made per month?")
print()

print("What percentage of requests resulted in a 4xx error code")
print("{}%".format(code4percent))
print('--------------------------------------------------------')

print("What percentage of the requests resulted in a 3xx error code")
print("{}%".format(code3percent))
print('----------------------------------------------------------')

print("What was the most-requested file?")
print(most_requested)
print('---------------------------------')

print("What was the lease-requested file?")
print(least_requested)
print('---------------------------------')
