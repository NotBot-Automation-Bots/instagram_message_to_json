from flask import Flask, request
import requests

app = Flask(__name__)



@app.route('/', methods=['GET'])
def home():
    
        PAGE_ACCESS_TOKEN='EAADEDzSrDWYBACnvv0Epv6FkutCDq4zgZBgdyRhL7atlSCfrWcP7yM3DLQXzs5xED2NXhqs5FpwrFDZA3wtD3zgAkq4ZCo1CJqouwrUkaSIoyyiDXa78FH222ZCKVKwtDCONaxeIeA1H9YQqn0vCZCyjVfJCfyF3QRhVrLgAiTnJ0gGco6fkpebpGDRPT9gnDOw6kofqpOLy2T2F3tStp'
        url = f'https://graph.facebook.com/v11.0/102863632088614/conversations?fields=messages&platform=instagram&access_token={PAGE_ACCESS_TOKEN}'
        r=requests.get(url)
        dj=r.json()
        for i in range(0,len(dj['data'])):
           thread=dj['data'][i]['id']
           url1=f"https://graph.facebook.com/v11.0/{thread}?&access_token={PAGE_ACCESS_TOKEN}&" + "fields=messages{from,message,created_time}"
           r=requests.get(url1)
           message=r.json()
           user=i+1
           user=f"\n\n{user} user\n"
           print(user)
           print(message)
        VERIFY_TOKEN='done'
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if (mode and token):
            if (mode == 'subscribe' and token == VERIFY_TOKEN):
                print("verified")
                
                return "processing" 
            else:
                pass
        return  "success", 200           


if __name__ == '__main__':
    app.run()
