
import datetime

mytime = datetime.time(13,20,1,20)
print(mytime)
print(mytime.hour)
print(mytime.minute)
print(mytime.microsecond)
print(type(mytime))
print("================")

today = datetime.date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.ctime())
print("================")
from datetime import datetime
mydatetime =datetime(2022,10,2,14,20,1)
print(mydatetime)
mydatetime =mydatetime.replace(month=12)
print(mydatetime)
mydatetime = datetime.now()
print(mydatetime)
print("================")

# Date 
from datetime import date

date1 = date(2021,11,3)
date2 = date(2022,11,3)
result = date2 -date1
print(result)
print(type(result))
print(result.days)

print("================")
datetime1 = datetime.now()
#print(datetime1)
#datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2020,11,3,12,0)
result =datetime1 -datetime2
print(result)
print(result.seconds)
print(result.total_seconds())




