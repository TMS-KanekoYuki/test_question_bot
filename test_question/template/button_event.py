# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:43:02 2020

@author: tms03002
"""

from linebot.models import (
    PostbackEvent, TextSendMessage, TemplateSendMessage,
    ButtonsTemplate, PostbackTemplateAction
)

class SitujiSindan:
    def question_a(self):
        button_template = TemplateSendMessage(
            alt_text="執事診断",
            template=ButtonsTemplate(
                title="質問1",
                text="あなたがピンチに陥った時",
                actions=[
                  PostbackTemplateAction(
                    label='頭脳であなたを助けてくれる',
                    data='question_b'
                  ),
                  PostbackTemplateAction(
                    label='体を張ってあなたを助けてくれる',
                    data='question_c'
                  )
                ]
            )
        )
        return button_template

    def question_b(self):
        button_template = TemplateSendMessage(
            alt_text="執事診断",
            template=ButtonsTemplate(
                title="質問２",
                text="あなたが大変なことをやらかした時には…",
                actions=[
                  PostbackTemplateAction(
                    label='優しくフォローしてほしい',
                    data='answer_d'
                  ),
                  PostbackTemplateAction(
                    label='ちゃんと叱ってほしい',
                    data='answer_e'
                  )
                ]
            )
        )
        return button_template

    def question_c(self):
        button_template = TemplateSendMessage(
            alt_text="執事診断",
            template=ButtonsTemplate(
                title="質問2",
                text="どちらの方がタイプ？",
                actions=[
                  PostbackTemplateAction(
                    label='無愛想',
                    data='answer_f'
                  ),
                  PostbackTemplateAction(
                    label='フレンドリー',
                    data='answer_g'
                  )
                ]
            )
        )
        return button_template

    def answer_d(self):
        msg = '診断結果は「正統派執事」です。とにかく、お嬢様の為に尽くしています'
        return TextSendMessage(text=msg)

    def answer_e(self):
        msg = '診断結果は「お兄様系執事」です。お嬢様のことが大好きで、いつもお嬢様のことを気にしています。'
        return TextSendMessage(text=msg)

    def answer_f(self):
        msg = '診断結果は「あくまで執事」です。少し無愛想ですが、全力でお嬢様を守っています。口癖は、「あくまで執事ですから」です。'
        return TextSendMessage(text=msg)

    def answer_g(self):
        msg = '診断結果は「弟系執事」です。お嬢様のことが大好きで、弟のように接してきます。普段は頼りないですが、ピンチの時は全力で守ります。'
        return TextSendMessage(text=msg)
