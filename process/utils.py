import requests
import json

def sendTextMessage(message,contactno):
    url = "https://www.fast2sms.com/dev/bulk"
    querystring = {
        "authorization":"kVgiNBJ6UOHpTxIEP1Z4MfdyQ0RcqCDzLluwjn2vGr3SsAWtaK1o9YM7WIbdmqTe3lsgcZkH0X4JNOD2",
        "sender_id":"FSTSMS",
        "message":message,
        "language":"english",
        "route":"p",
        "numbers":contactno
        }
    headers = {
    'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = response.text
    d1 = json.loads(json_data)
    return d1['return']