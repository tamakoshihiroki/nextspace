# -*- coding: utf-8; -*-

"""
error handler
"""

from mailer import create_message, send_mail
from logger import log
import traceback
import os

SUBJECT = u'本日の万葉集 エラー'
BODY    = u"""エラーが発生しました。

ブラウザ環境：
%(ip)s
%(user_agent)s

エラー内容：
%(error_message)s
"""

def create_body():
    'create mail body'
    return BODY % dict(
        ip            = os.getenv( 'REMOTE_ADDR', '' ),
        user_agent    = os.getenv( 'HTTP_USER_AGENT', '' ),
        error_message = traceback.format_exc(),
        )

def error_handler():
    'error handler'
    try:
        body = create_body()
        mail = create_message( body, SUBJECT, 'tmkc.igo@gmail.com' )
        send_mail( mail, 'tmkc.igo@gmail.com' )
    except:
        error_message = traceback.format_exc()
        log( error_message )
