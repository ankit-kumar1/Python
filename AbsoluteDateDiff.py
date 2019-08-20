import sys
stdin = sys.stdin

n = int(stdin.readline())
import datetime
for i in range(n):
	dt1 = datetime.datetime.strptime(stdin.readline().rstrip(), '%a %d %b %Y %H:%M:%S %z')
	dt2 = datetime.datetime.strptime(stdin.readline().rstrip(), '%a %d %b %Y %H:%M:%S %z')
	print(abs(int(((dt2-dt1).total_seconds()))))
