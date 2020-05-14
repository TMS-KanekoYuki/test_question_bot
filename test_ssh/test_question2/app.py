# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:34:14 2020

@author: tms03002
"""

import os
import sys
import json

# flaskのライブラリをimport
from flask import Flask, request, abort
# linebotのライブラリをimport
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, PostbackEvent, TextMessage, TextSendMessage
)

# 自作のライブラリをimport
from template import button_event

app = Flask(__name__)

# 設定ファイルの読み込み
ABS_PATH = os.path.dirname(os.path.abspath(__file__))
with open(ABS_PATH+'/conf.json', 'r') as f:
    CONF_DATA = json.load(f)
CHANNEL_SECRET = CONF_DATA['CHANNEL_SECRET']
CHANNEL_ACCESS_TOKEN = CONF_DATA['CHANNEL_ACCESS_TOKEN']

# クライアントライブラリのインスタンスを作成
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# テスト用のコード
@app.route("/")
def test():
    app.logger.info("test")
    return('test OK')

# LINE APIのコード
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")
    try:
        handler.handle(body, signature)
    except InvalidSignatureError as e:
        print(e)
        abort(400)
    return 'OK'

# メッセージが来た時の反応
@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    message_text = event.message.text
    app.logger.info(message_text)

    if message_text == '執事診断':
        line_bot_api.reply_message(
            event.reply_token,
            button_event.SitujiSindan().question_a()
        )
    else:
        msg = '申し訳ありませんが、現在対応しておりません。'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=msg)
        )

# 値が帰ってきたときの反応
@handler.add(PostbackEvent)
def on_postback(event):
    reply_token = event.reply_token
    user_id = event.source.user_id

    # postback_msg : method名を文字列で
    postback_msg = event.postback.data
    # situji_sindan : classオブジェクト
    situji_sindan = button_event.SitujiSindan()
    # クラスオブジェクトと文字列で取得したメソッド名から、メソッドオブジェクトを作成
    question = getattr(situji_sindan, postback_msg)
    # 次の質問投げつける
    line_bot_api.reply_message(
        event.reply_token,
        question()
    )

if __name__ == "__main__":
    app.run(debug=True)
