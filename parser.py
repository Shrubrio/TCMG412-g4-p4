from stat import filemode
import urllib.request
from urllib.request import urlretrieve
import os.path
from os import path

weburl = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
resultcode = print("result code: " + str(weburl.getcode()))
    
if path.isfile('logfile.txt') == False:
    print('downloading log file...')
    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve (url, 'logfile.txt')
    print('done')
else: print('this file is already present on your workstation')
    
file=open('logfile.txt', 'r')

Files = {}
filename = []
logfile = []
dates = []
NumDates = []
Num1Dates = []
yeartotal = []
NumMonth = {}
lineseg = []

code4 = 0
code3 = 0
requests = []



percent3xx = (code3 / len(dates)) * 100
percent3xx = "{:.2f}" .format(percent3xx)
percent4xx = (code4 / len(dates)) * 100
percent3xx = "{:.2f}" .format(percent4xx)

request_total = 0
    
for line in open(r"logfile.txt", 'r'):
    if "GET" in line:
        request_total += 1

print("Total number of requests:", request_total)

    
fp.close()
