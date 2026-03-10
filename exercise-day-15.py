# Exercise good morning sir based on current time we will greet you with good morning, good afternoon, good evening or good night we will use time module and use if else

import time
currenttime = time.localtime()
currenthour = currenttime.tm_hour
ctime = time.strftime("%H:%M:%S")
if (currenthour >=5 and currenthour <12):
    print("good morning sir")
elif (currenthour >=12 and currenthour <17):
    print("good afternoon sir")
elif (currenthour >=17 and currenthour <21):
    print("good evening sir")
else:
    print("good night sir")
print ("current time is ", ctime)
