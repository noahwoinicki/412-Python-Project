from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True))

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)
