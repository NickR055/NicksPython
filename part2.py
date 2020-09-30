from urllib.request import urlretrieve
import re

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
ERRORS = []
# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

# Use open() to get a filehandle that can access the file
fh = open(local_file)
things = {}
#Log Counts

lines = fh.readlines()
regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
# Loop through the file
mostreq = "index.html"
leastreq = ""
two = 0
three=0
four=0
total=0
##Finding filenames
for line in lines:
    parts = regex.split(line)
    # file title
    if not parts or len(parts) < 7:
        ERRORS.append(line)
    else:
        filename = parts[4]
        if filename in things:
            things[filename] += 1
        else:
            things[filename] = 1
        #finding codes
        code = parts[6]
        first = [w[0] for w in code]
        if first[0] == '2':
            two += 1
        if first[0] == '3':
            three +=1
        if first[0] == '4':
            four +=1
    total +=1
#code math
print("The percentage of requests that were redirected: ", three/total*100,"%")
print("The percentage of requests that were not successful: ",four/total*100,"%")
#finding the most/least
#most
#sorted(things, reverse = True)[:1]
#print("The most requested file was: ",things[0])
#least
#sorted(things, reverse = False)[:1]
#print("The least requested file was: ",things[0])
##Dates

