'''from time import localtime

tm = localtime()
print(f"{tm.tm_year}-{tm.tm_mon}-{tm.tm_mday}")
'''
import datetime

d = datetime.datetime.now()
print (d.strftime("%Y-%m-%d"))