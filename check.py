# coding: utf-8
import requests
import time
import slackweb
import settings


Target_URL = settings.Target
Webhook_URL = settings.Webhook

def webstatus(url, slack):
    try:
        req = requests.get(url)
        if req.status_code == 200:
            return('OK')
        else:
            req = str(req)
            slack.notify(text=req)
    except requests.exceptions.RequestException as e:
        e = str(e)
        slack.notify(text=e)

if __name__ == '__main__':
    while(True):
        url = Target_URL
        slack = slackweb.Slack(url=Webhook_URL)
        print(webstatus(url, slack))
        time.sleep(5)