import plyer as plr
import requests
import time
import random as rnd
import os.path
from os import path
import shutil

maso = True

p = os.path.dirname(__file__)
pn = p.replace("\\", "/" )

print(pn)
userp = os.path.expanduser('~')
startup = rf'{userp}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'

if pn == 'C:/Users/Barusu/stuff/Scripts/NotifBoi':
    print('cheese')
    f = open(rf"{userp}\Downloads\demo.txt", "a")
    file = rf"{userp}\Downloads\demo.txt"
    time.sleep(1)
    try:
        shutil.move(file,startup)
    except WindowsError:
        pass
    f.write("Now the file has more content!")
    f.close()

