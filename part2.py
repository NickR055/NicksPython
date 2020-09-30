from urllib.request import urlretrieve
import re
from datetime import datetime

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
two = 0
three=0
four=0
total=0
dates={}
mon =0
tue =0
wed =0
thu =0
fri =0
sat =0
sun =0
weeks={}
jan5=0
feb5=0
mar5=0
apr5=0
may5=0
jun5=0
jul5=0
aug5=0
sep5=0
oct5=0
oct4=0
nov4=0
dec4=0

##Finding filenames
for line in lines:
    parts = regex.split(line)
    # file title
    if not parts or len(parts) < 7:
        ERRORS.append(line)
    else:
        #dates
        date = datetime.strptime(parts[1], "%d/%b/%Y")
        weekday = date.weekday()
        if weekday == 0:
            mon +=1
        if weekday == 1:
            tue +=1
        if weekday == 2:
            wed +=1
        if weekday == 3:
            thu +=1
        if weekday == 4:
            fri +=1
        if weekday == 5:
            sat +=1
        if weekday == 6:
            sun +=1
        year=date.year
        if year == 1995:
            month=date.month
            if month==1:
                jan5+=1
            if month==2:
                feb5+=1
            if month==3:
                mar5+=1
            if month==4:
                apr5+=1
            if month==5:
                may5+=1
            if month==6:
                jun5+=1
            if month==7:
                jul5+=1
            if month==8:
                aug5+=1
            if month==9:
                sep5+=1
            if month==10:
                oct5+=1
        else:
            month = date.month
            if month == 10:
                oct4 += 1
            if month == 11:
                nov4 += 1
            if month == 12:
                dec4 += 1


        #Filecounter
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





#date print
print("Monday had a total of: ", mon," requests")
print("Tuesday had a total of: ", tue," requests")
print("Wednesday had a total of: ", wed," requests")
print("Thursday had a total of: ", thu," requests")
print("Friday had a total of: ", fri," requests")
print("Saturday had a total of: ", sat," requests")
print("Sunday had a total of: ", sun," requests")

print("The month of October of 1994 had: ",oct4," requests")
print("The month of November of 1994 had: ",nov4," requests")
print("The month of December of 1994 had: ",dec4," requests")

print("The month of January of 1995 had: ",jan5," requests")
print("The month of February of 1995 had: ",feb5," requests")
print("The month of March of 1995 had: ",mar5," requests")
print("The month of April of 1995 had: ",apr5," requests")
print("The month of May of 1995 had: ",may5," requests")
print("The month of June of 1995 had: ",jun5," requests")
print("The month of July of 1995 had: ",jul5," requests")
print("The month of August of 1995 had: ",aug5," requests")
print("The month of September of 1995 had: ",sep5," requests")
print("The month of October of 1995 had: ",oct5," requests")


#code math
print("The percentage of requests that were redirected: ", three/total*100,"%")
print("The percentage of requests that were not successful: ",four/total*100,"%")
#finding the most/least
#most
mostreq = sorted(things,key=things.get, reverse = True)[:1]
print("The most requested file was: ",mostreq)
#least
leastreq = sorted(things, key=things.get,reverse = False)[:1]
print("The least requested file was: ",leastreq)

