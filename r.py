import requests

API_TOKEN = '7692460124:AAF0972xIGq6V5JpguD_B9nBh35u0QdALao'  # Replace with your bot's API token
CHAT_ID = -4581487424 # Replace with your negative chat ID

def send_message(message):
    url = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
    }
    response = requests.post(url, json=payload)
    return response.json()

def save(message):
    response= send_message(message)
    x = response["ok"]
    return x

###################################################################################
print(save("h"))



from urllib.request import urlopen
import re as r

def getIP():
    d = str(urlopen('http://checkip.dyndns.com/')
            .read())

    return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').
             search(d).group(1)

print(getIP())
