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

lastsixmonths = ["May/1995:", "Jun/1995:" , "Jul/1995:", "Aug/1995:", "Sep/1995:", "Oct/1995:"]  
lastsix = 0
request_total = 0

with open(r"logfile.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total number of lines in file between Oct 1994 and Oct 1995:', lines)
    
for line in open(r"logfile.txt", 'r'):
    if "GET" in line:
        request_total += 1
        
        for month in lastsixmonths:
            if month in line:
                lastsix +=1

print("Total number of requests:", request_total)

print("The number of logs in the last six months is", lastsix)
    
fp.close()
