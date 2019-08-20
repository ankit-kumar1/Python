import datetime


input = """
01-01-2019
02-02-2019
05-04-2019
02-03-2019
02-04-2019
01-02-2019
05-03-2019
05-02-2019
05-01-2019
05-05-2019
"""

list_of_dates = [x for x in input.split('\n') if x!='']
list_of_dates.sort()
#print(list_of_dates)

maxcount = 0
for i in range(len(list_of_dates)):
    for j in range(i+1,(len(list_of_dates))):
        if (datetime.datetime.strptime(list_of_dates[j],"%m-%d-%Y")-datetime.datetime.strptime(list_of_dates[i],"%m-%d-%Y")).days == (j-i):
            if maxcount < (j-i):
                maxcount=j-i

maxcount=maxcount+1
print("max counsecutive days: " +  str(maxcount))
