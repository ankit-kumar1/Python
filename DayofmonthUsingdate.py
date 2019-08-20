# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar,datetime

date = input()
born = datetime.datetime.strptime(date, '%m %d %Y').weekday() 
print((calendar.day_name[born]).upper(), end =" ") 
