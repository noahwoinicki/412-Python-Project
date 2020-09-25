#preparing python
from urllib.request import urlretrieve
from os import path


#variables
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local = 'local_copy.txt'
dates = []
file_names = []
error_codes = []
n_dates = []
n1_dates = []
year_amount = []
n_month = {}
not_successful_request = []
redirected_request = []


#pull marketing info and make log 
if path.isfile('local_copy.txt') == "False":
    print('File downloading...')
    url_ret = urlretrieve(url, local)
    print('File Download Complete')
else: 
    print('File is already downloaded')
    

#open and get to work
open_log = open('local_copy.txt', 'r')

for row in open_log: 
    split = row.split(' ')
    if(len(split) > 8):
        error_codes.append(split[8])
        file_names.append(split[6])
    if(len(split[3]) > 14):
        dates.append(split[3]) 

for date in dates:
    n_dates.append(date[1:12])
    n1_dates.append(date[1:3])

for d in n1_dates:
	if(d in n_month):
	    n_month[d] += 1
	else:
	    n_month[d] = 1

for mistakes in code: 
    print(mistakes)
    if(mistakes[0] == '3'):
	redirected_request = redirected_request + 1
    if(mistakes[0] == '4'):
	not_successful_request = not_successful_request + 1
	
redirected_percent = (redirected_request / len(dates)) * 100
not_successful_percent = (not_successful_request / len(dates)) * 100




#print report
print("How many requests were made on each day?")
print("Day: Number of Requests")
for key, value in sorted(n_month.items()):
	print(f"{key} : {value}")
	

print("What percentage of the requests were not successful?")
print(not_successful_percent,'%')
print("What percentage of the requests were redirected elsewhere?")
print(redirected_percent,'%')
