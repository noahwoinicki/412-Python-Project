from urllib.request import urlretrieve
from os import path

dates = []
year_amount = []
pure_num = []
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
local = 'local_copy.txt'


if path.isfile('local_copy.txt') == False"
    print('File downloading...')
    url_ret = urlretrieve(url, local)
    print('File Download Complete')
else: 
    print('File is already downloaded')
    

open_log = open('local_copy.txt', 'r')

for row in open_log: 
    split = row.split(' ')
    dates.append(split[3]) 

print(dates)
open_log.read(64) 
open_log.readline() 
    
    
print("Total request made in last year:", len(dates))
