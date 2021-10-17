import time
try:
    f = open("screentime", "w")
    f.write(str(time.time()))
except:
    print(-1)
