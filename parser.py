from urllib.request import urlretrieve
import urllib.request
import os.path
from os import path
import re
import datetime
import collections

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
months = {}
requesttotal = 0

Jan = 0
Feb = 0
Mar = 0 
Apr = 0
May = 0 
Jun = 0 
Jul = 0
Aug = 0
Sep = 0 
Oct95 = 0
Oct94 = 0
Nov = 0
Dec = 0
code4 = 0
code3 = 0

months['January'] = Jan
months['February'] = Feb
months['March'] = Mar
months['April'] = Apr
months['May'] = May
months['June'] = Jun
months['July'] = Jul
months['August'] = Aug
months['September'] = Sep
months['October'] = Oct95 + Oct94
months['November'] = Nov
months['December'] = Dec

if path.isfile('logfile.txt') == False:
    print('downloading log file...')
    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve (url, 'logfile.txt')
    print('done')
else: print('this file is already present on your workstation')
    
open_log = open('logfile.txt', 'r')

for line in open(r"logfile.txt", 'r'):
    if "GET" in line:
        requesttotal += 1
    if "POST" in line:
        requesttotal += 1
        
weeklybasis = requesttotal / 50
    

openOct94 = open("Oct94.txt", "w")
openNov94 = open("Nov94.txt", "w")
openDec94 = open("Dec94.txt", "w")
openJan = open("Jan.txt", "w")
openFeb = open("Feb.txt", "w")
openMar = open("Mar.txt", "w")
openApr = open("Apr.txt", "w")
openMay = open("May.txt", "w")
openJun = open("Jun.txt", "w")
openJul = open("Jul.txt", "w")
openAug = open("Aug.txt", "w")
openSep = open("Sep.txt", "w")
openOct95 = open("Oct95.txt", "w")

for row in open_log: 
    split = row.split(' ')
    if(len(split) > 8):
        errorcodes.append(split[8])
        filenames.append(split[6])
    if(len(split[3]) > 14):
        dates.append(split[3]) 
    if(split[3][4:7] == "Oct" and split[3][8:12] == '1994'):
        openOct94.write(row)
        Oct94 += 1
    if(split[3][4:7] == "Nov" and split[3][8:12] == '1994'):
        openNov94.write(row)
        Nov += 1
    if(split[3][4:7] == "Dec" and split[3][8:12] == '1994'):
        openDec94.write(row)
        Dec += 1
    if(split[3][4:7] == "Jan" and split[3][8:12] == '1995'):
        openJan.write(row)
        Jan += 1
    if(split[3][4:7] == "Feb" and split[3][8:12] == '1995'):
        openFeb.write(row)
        Feb += 1
    if(split[3][4:7] == "Mar" and split[3][8:12] == '1995'):
        openMar.write(row)
        Mar += 1
    if(split[3][4:7] == "Apr" and split[3][8:12] == '1995'):
        openApr.write(row)
        Apr += 1
    if(split[3][4:7] == "May" and split[3][8:12] == '1995'):
        openMay.write(row)
        May += 1
    if(split[3][4:7] == "Jun" and split[3][8:12] == '1995'):
        openJun.write(row)
        Jun += 1
    if(split[3][4:7] == "Jul" and split[3][8:12] == '1995'):
        openJul.write(row)
        Jul += 1
    if(split[3][4:7] == "Aug" and split[3][8:12] == '1995'):
        openAug.write(row)
        Aug += 1
    if(split[3][4:7] == "Sep" and split[3][8:12] == '1995'):
        openSep.write(row)
        Sep += 1
    if(split[3][4:7] == "Oct" and split[3][8:12] == '1995'):
        openOct95.write(row)
        Oct95 += 1

for date in dates:
    numdate.append(date[1:12])
    num1dates.append(date[1:3])

for d in num1dates:
    if(d in NumMonth):
        NumMonth[d] += 1
    else:
        NumMonth[d] = 1
        
for issues in errorcodes: 
    if(issues[0] == '3'):
        code3 = code3 + 1
    if(issues[0] == '4'):
        code4 = code4 + 1
    
code3percent = (code3 / len(dates)) * 100
code3percent = "{:.2f}".format(code3percent)
code4percent = (code4 / len(dates)) * 100
code4percent = "{:.2f}".format(code4percent)

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
print('This is the average # of requests per week')
print('---', weeklybasis, '---')
print('----------------------------------------------------')

print("How many requests were made per month?")

print(f"Oct 94 had {Oct94} requests.")
print(f"Nov 94 had {Nov} requests.")
print(f"Dec 94 had {Dec} requests.")
print(f"Jan 95 had {Jan} requests.")
print(f"Feb 95 had {Feb} requests.")
print(f"Mar 95 had {Mar} requests.")
print(f"Apr 95 had {Apr} requests.")
print(f"May 95 had {May} requests.")
print(f"Jun 95 had {Jun} requests.")
print(f"Jul 95 had {Jul} requests.")
print(f"Aug 95 had {Aug} requests.")
print(f"Sep 95 had {Sep} requests.")
print(f"Oct 95 had {Oct95} requests.")
print('--------------------------------------')

print("What percentage of requests resulted in a 4xx error code")
print('---', "{}%".format(code4percent), '---')
print('--------------------------------------------------------')

print("What percentage of the requests resulted in a 3xx error code")
print('---', "{}%".format(code3percent), '---')
print('----------------------------------------------------------')

print("What was the most-requested file?")
print('---', most_requested, '---')
print('---------------------------------')

print("What was the least-requested file?")
print('---', least_requested, '---')
print('---------------------------------')
