import datetime

#today = datetime.datetime.today()

now = datetime.datetime.now()

#print(today)

print(now)

print("{}년".format(now.year))
print("{}월".format(now.month))
print("{}일".format(now.day))

print("{}시".format(now.hour))
print("{}분".format(now.minute))
print("{}초".format(now.second))

print(now.strftime("%Y.%m.%d %H:%M:%S")) # %Y=년 , %m=월 , %d=일 , %H=시 , %M=분 , %S=초

