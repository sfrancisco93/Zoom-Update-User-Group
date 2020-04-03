from User import checkUser
from Group import checkGroup, updateUserGroup
import csv 

csvFile = 'sampleTemplate.csv' ## Change csvFile to your actual file.
checkEmails = {}
##
# 1. Read CSV list of Users
##
def import_text(filename, separator):
    for line in csv.reader(open(filename), delimiter=separator, 
                           skipinitialspace=True):
        if line:
            yield line

##
# 2. Check if Users exist
##
for data in import_text(csvFile, ','):
	if(checkUser(str(data[0]))): 
		if str(data[1]) in checkEmails.keys():
			checkEmails[str(data[1])].append(str(data[0]))
		else:
			checkEmails[str(data[1])] = [str(data[0])]
	else: print("Error: " + str(data[0]) + " does not belong to this account. ")

##
# 3. Check if Group exists
##
for item in checkEmails.keys():
	if not checkGroup(item):
		print("Error: " + item + " is not an existing group in this account.")
		del[checkEmails[item]]

##
# 4. Confirm the change
##
for item in checkEmails.keys():
	print(str(checkEmails[item]) + " will be moved to " + item)

updateUserGroup(checkEmails)