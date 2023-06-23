import requests
import json
from credentials import chat_id, api_key, username, password

def send_telegram_message(message: str, chat_id: str, api_key: str,
                          proxy_username: str = None, proxy_password: str = None, proxy_url: str = None):
    responses = {}

    proxies = None
    if proxy_url is not None:
        proxies = {
            'https': f'http://{username}:{password}@{proxy_url}',
            'http': f'http://{username}:{password}@{proxy_url}'
        }
    headers = {'Content-Type': 'application/json',
                'Proxy-Authorization': 'Basic base64'}
    data_dict = {'chat_id': chat_id,
                    'text': message,
                    'parse_mode': 'HTML',
                    'disable_notification': True}
    data = json.dumps(data_dict)
    url = f'https://api.telegram.org/bot{api_key}/sendMessage'
    response = requests.post(url, data=data, headers=headers, proxies=proxies,verify=False)

    return response
    
if __name__ == "__main__":
    text_to_send = "✅ Print is done!"
    send_telegram_message(text_to_send, chat_id=chat_id, api_key=api_key)
