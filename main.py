FILE_NAME = '/home/vagrant/NicksPython/local_copy.log'

# Use open() to get a filehandle that can access the file
fh = open(FILE_NAME)

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
