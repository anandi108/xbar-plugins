#!/usr/bin/python
# coding=utf-8
#
# <xbar.title>Dogecoin coin Ticker ($1USD)</xbar.title>
# <xbar.version>v1.1</xbar.version>
# <xbar.author>impshum</xbar.author>
# <xbar.author.github>impshum</xbar.author.github>
# <xbar.desc>Displays current Dogecoin price for $1 from Coinmarketcap.com</xbar.desc>
# <xbar.image>http://i.imgur.com/FBUh3fk.jpg</xbar.image>
#
# by impshum

from urllib import urlopen
url = urlopen('https://api.coinmarketcap.com/v1/ticker/dogecoin/').read()

import json
result = json.loads(url)

def flow():

    if result[0]['percent_change_24h'] > '0':
        print (' $%.4f | image=iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QAyQACAALwzISXAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AQHACkSBTjB+AAAALNJREFUOMvVk70NAjEMhb87WYiGBZAQU7ABNSVSWpZgEEagsJDoKBELUCEKFuBuCKTw0xyQC0lICe5i+/k9/wT+3opUUJQhcAUqa8I5ZQT4tANwioGTCkQZA9vmOQE2oUJFhL0DXBz33RpKUfCLfLTQJMx9IlEWuQr6QB3prGtNS1lwiMvEYo7ekNsKRBkB+y+rH1hDFVOwy7ids+gbVzrsM6CXeYDTF85xroB1ZoHb73ymB5RhJkpZTihGAAAAAElFTkSuQmCC color=#000000'% float(result[0]['price_usd']))
    else:
        print (' $%.4f | image=iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABmJLR0QABACnAADQ9FZaAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AQHACQ1FZwK3gAAAMRJREFUOMvNkjEKAjEQRZ+jKNjYKh5AbzCdjVcQj+BFPIKlp7EMeAJrUbASQVCEr80uG9cNbqe/Cgn/5WUI/DqNfBHM+kCzbs+lPUAr2pwBq5qABbB+M8gszkDvS/kOdAG5VBgEM4ApsP0CGLukjxlEoA0wSZR3Lo0qhxhZDIBDAmDA0wsBLD51CZeOwLKivHbprZx6AkAHuEXbD5fawYwywMqAzOKeDTTPvKqcTGZBMLsGs0utn5gADYEHcKp9e9ni//MCDtNCE3qjsIwAAAAASUVORK5CYII= color=#000000'% float(result[0]['price_usd']))

flow()
