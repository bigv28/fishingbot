import requests
import time

URL = 'https://discord.com/api/v9/channels/1025871229950902352/messages'
AUTH = {'authorization': 'NDU5NDI0MDI1MTEwOTA0ODU0.G3QHRK.bgECq4xV3gZdY76z07EdR1ShUAHaAbKtLRiRt4'}


def approve():
    r = requests.get(
        "https://discord.com/api/v9/channels/1025871229950902352/messages?limit=1",
        headers=AUTH
    ).json()

    message_id = r[0]['id']
    requests.put(
        f'https://discord.com/api/v9/channels/1025871229950902352/messages/{message_id}/reactions/check%3A502235451592278016/%40me?',
        headers=AUTH
    )


def send(command):
    requests.post(URL, headers=AUTH, data={'content': f'?{command}'})


while True:
    send('wd 50')
    send('buy f')
    approve()
    time.sleep(2.25)

    send('fish')
    send('sell all')
    time.sleep(2.25)
    approve()

    send('dep all')
    time.sleep(0.5)
