from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# Use open() to get a filehandle that can access the file
fh = open(local_file)

count = 0
yearcount = 0
date = "/1995:"
lines = fh.readlines()
# Loop through the file
for string in lines:
    if date in string:
        yearcount = yearcount + 1
    count = count + 1
print("The total amount of logs is: ", count)
print("The total amount of logs in 1995 was: ", yearcount)
