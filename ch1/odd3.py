from datetime import datetime
from time import sleep
from random import randint
#import time
#import random

odds = list(range(1,60,+2))

for i in range(5):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("This minute seems a little odd")
    else:
        print("Not an odd minute")
    sleeptime = randint(1,60)
    print(sleeptime)
    sleep(sleeptime)
