from urllib.request import urlretrieve
from os import path

dates = []
n_dates = []
n1_dates = []
year_amount = []
n_month = {}

url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local = 'local_copy.txt'


if path.isfile('local_copy.txt') == "False":
    print('File downloading...')
    url_ret = urlretrieve(url, local)
    print('File Download Complete')
else: 
    print('File is already downloaded')
    

open_log = open('local_copy.txt', 'r')

for date in dates:
    n_dates.append(date[1:12])
    n1_dates.append(date[1:3])

for d in n1_dates:
	if(day in n_month):
		n_month[day] += 1
	else:
		n_month[day] = 1

print("Day: Number of Requests")
for key, value in sorted(DaysOfMonth.items()):
	print(f"{key} : {value}")
#####print()
#####for row in open_log: 
#####    split = row.split(' ')
#####    dates.append(split[3]) 

#####print(dates)
#####open_log.read(64) 
#####open_log.readline() 
    
    
#####print("Total request made in last year:", len(dates))
