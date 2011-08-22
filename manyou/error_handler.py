# -*- coding: utf-8; -*-

"""
error handler
"""

from mailer    import create_message, send_mail
from logger    import log
from pprint    import pformat
# from threading import Thread
import traceback
import os
import inspect

SUBJECT = u'本日の万葉集 エラー'
BODY    = u"""エラーが発生しました。

ブラウザ環境：
%(ip)s
%(user_agent)s

エラー内容：
%(error_message)s

スタック：
%(stack)s
"""

def create_body():
    'create mail body'
    return BODY % dict(
        ip            = os.getenv( 'REMOTE_ADDR', '' ),
        user_agent    = os.getenv( 'HTTP_USER_AGENT', '' ),
        error_message = traceback.format_exc(),
        stack         = u'\n\n'.join(
            [ pformat( inspect.getargvalues( frame[ 0 ] ) )
              for frame in inspect.stack() ] ),
        )

def error_handler():
    'main error handler function'
    try:
        body = create_body()
        mail = create_message( body, SUBJECT, 'tmkc.igo@gmail.com' )
        send_mail( mail, 'tmkc.igo@gmail.com' )
    except:
        error_message = traceback.format_exc()
        log( error_message )

# def error_handler():
#     'error handler'
#     thread = Thread( target = main_handler )
#     thread.daemon = True
#     thread.start()
