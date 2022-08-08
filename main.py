import pdb
import requests
import json
import os

room_id = 256189130

url = f"https://api.chatwork.com/v2/rooms/{room_id}/messages?force=1"

headers = {
    "Accept": "application/json",
    "X-ChatWorkToken": os.environ.get('ChatWorkToken')
}

response = requests.get(url, headers=headers)
#import pdb; pdb.set_trace()

json = json.loads(response.text)
# import pdb; pdb.set_trace()

for m in json:
    if m["account"]["name"] == 'zen-bot':
        message_id = m["message_id"]
        url = f"https://api.chatwork.com/v2/rooms/{room_id}/messages/{message_id}"
        response = requests.get(url, headers=headers)
