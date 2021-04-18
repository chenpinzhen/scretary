# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:19:53 2021

@author: 陳品蓁
"""


text=event.message.text
#userId = event['source']['userId']
if(text.lower()=='me'):
    content = str(event.source.user_id)

    line_bot_api_8.reply_message(
        event.reply_token,
        extSendMessage(text=content)
    )
else:
    line_bot_api_8.reply_message(
        event.reply_token,
        TextSendMessage(text=text)
    )
from linebot import (
    LineBotApi, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

channel_secret = 'cd7e4d61a3958de0c7bb558581e3f17a'
channel_access_token = 'X4rJU4vOY5jM0hSQeAqKHl4u1hv79mqv/OxsvRABWEYaoIoxZuLeJ+ML8fxcdf0JxI+piqLs0ieESpJHJnLE8TDfrfC2Qbs9+77JzM7zdEAFhepflNMhEt3b6RUTElmeqEm2sjJZ9Rtplxp6K9dZWgdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(channel_access_token)
#push message to one user
user_id = '1655740641'
line_bot_api.push_message(user_id, 
    TextSendMessage(text='Hello World!'))   