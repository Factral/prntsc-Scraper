
# prntsc-Scraper

This is a [prnt.sc](https://prnt.sc/) scrapper, it generates random urls, checks if it is not a [Crypto Scam](#crypto-scam) image, and if it is not it sends it to a discord webhook,threading is used to increase the speed of image verification.

## how to use
1. have installed python 3
2. install the requirements `pip install -r requirements.txt`
3. [connect to your webhook on discord ](#connect-to-discord)
4. execute it, `python3 main.py`

## Connect to discord

when it verifies the image, it sends it to a discord webhook on a server, if you don't know how to create one you can check here [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) copy your webhook url and put it in:

```python
WEBHOOK_URL = 'YOUR WEBHOOK URL HERE'
```

## Crypto scam 
prnt.sc is a website that has a reputation for spreading fake crypto wallet credentials that somehow scam the user, are all over the web site and they all follow the same general methodology

### how to know if an image is a scam?

when finding an image in prnt.sc , it converts the image to base64 and compares it with the values of data.json , if any value is equal, it classifies that image as fake image and does not send it.
 *sometimes it gives some false positives*

## Contribute
 Any [contribution](link) about the code is very helpful, or for any bug, open a [topic](link)
