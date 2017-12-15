
from datetime import date, timedelta

def allsundays(year1,year2):
   count=0
   lis=[]
   for year in range(year1,year2,1):
	   d = date(year, 1, 1)    
	   # print(d)                # January 1st
	   d += timedelta(days = (3- d.weekday())%7)
	  # First Sunday
	   # print(d)
	   temp=d
	   lis.append(d)
	   while d.year == year:
	      yield d
	      d += timedelta(days = 7)
	      lis.append(d)
	      # print(d)
   new=list(set(lis))     
   print(len(new))      
count=0
for d in allsundays(1990,2000):
   count=count
