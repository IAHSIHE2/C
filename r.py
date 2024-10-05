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



def get_public_ip():
    try:
        # Fetch public IP from an API
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # Raise an error for bad responses
        ip_info = response.json()
        return ip_info['ip']
    except requests.RequestException as e:
        return f"Error fetching IP: {e}"


public_ip = get_public_ip()
print(f"Your public IP address is: {public_ip}")


