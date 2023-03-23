from dotenv import load_dotenv
import os
import base64
from requests import post
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
url = os.getenv("URL")

def get_token():
    auth_string = client_id + ":" +client_secret
    auth_byte  = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_byte),'utf-8')

    headers = {
        "Authorization":"Basic "+auth_base64,
        "Content-Type":"application/x-www-form-urlencoded"
    }
    data = {
        "grant_type":"client_credentials"
    }

    result = post(url,headers=headers,data=data)
    json_result = json.loads(result.content)
    return json_result


if __name__ == '__main__':
    token = get_token()
    print(token)