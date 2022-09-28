import plyer as plr
import requests
import time
import random as rnd

maso = True

while(maso):
    timer = rnd.randint(1800,7200)
    r = requests.get('https://insult.mattbas.org/api/insult')
    plr.notification.notify(
        title='Cirno says:',
        message=r.text,
        app_icon='C:/Users/Barusu/Pictures/fumo.ico',
        timeout=10,
    )
    time.sleep(timer)
