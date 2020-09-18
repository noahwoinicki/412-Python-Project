from urllib.request import urlretrieve

dates = []
year_amount = []
pure_num = []
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local = 'local_copy.txt'

url_ret = urlretrieve(url, local)

open_log = open('local_copy.txt', 'r')

for row in open_log: 
    split = row.split(' ')
    dates.append(split[3]) 

print(dates)
open_log.read(64) 
open_log.readline() 

for date in dates:
	pure_num.append(date[1:12])

if pure_num[8:12] == '1995':
    print(len(pure_num))
    
    

print("Total request made in last year:", len(dates))
