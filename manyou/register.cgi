#!/usr/local/bin/python
# -*- coding: utf-8; -*-

"""
register.cgi
"""

from templates     import REGISTER_TEMPLATE, FOOTER_TEMPLATE
from database      import database_open, database_close
from controller    import update_user
from mailer        import create_message, send_mail
from form          import get_form_value
from validator     import validate_mail_address
from error_handler import error_handler
import cgi
import cgitb

cgitb.enable( display = 0, logdir = 'log' )

def get_values( form ):
    'get values from form'
    return dict(
        submitted     = get_form_value( form, 'submitted', '' ),
        mail_address  = get_form_value( form, 'mail_address', '' ),
        mail_address2 = get_form_value( form, 'mail_address2', '' ),
        direction     = get_form_value( form, 'direction', 'vertical' ),
        column        = int( get_form_value( form, 'column', 7 ) ),
        row           = int( get_form_value( form, 'row', 11 ) ),
	day           = get_form_value( form, 'day', 'everyday' ),	
        hour          = int( get_form_value( form, 'hour', 8 ) ),
        )

def validate( values ):
    'true if all values are appropriate'
    return (
        validate_mail_address( values[ 'mail_address' ] ) and
        values[ 'mail_address' ] == values[ 'mail_address2' ] and
        ( 'vertical' == values[ 'direction' ] or
          'horizontal' == values[ 'direction' ] ) and
        ( 6 <= values[ 'column' ] and values[ 'column' ] <= 12 ) and
        ( 9 <= values[ 'row' ] and values[ 'row' ] <= 15 ) and
        ( 'everyday' == values[ 'day' ] or
          'weekday' == values [ 'day' ] or
          'holiday' == values[ 'day' ] ) and
        ( values[ 'hour' ] in range( 24 ) )
        )

def register( values ):
    'register the user'
    database = database_open()
    update_user( database, values[ 'mail_address' ], values[ 'direction' ],
                 values[ 'column' ], values[ 'row' ],
                 values[ 'day' ], values[ 'hour' ] )
    database_close( database )

DAYS    = dict(
    everyday = u'毎日',
    weekday  = u'平日（月〜金）',
    holiday  = u'土日',
    )
SUBJECT = u'本日の万葉集の登録'
BODY    = u"""本日の万葉集にご登録いただきまして誠にありがとうございます。
下記の通り受け付けました。
送る時期:%(day)s %(hour)d時

もし、このメールを受け取るお心当たりのない場合はこのメールにご返信下さい。
本日の万葉集 http://tmkc.pqg.jp/manyou/"""

def create_mail( values ):
    'create mail'
    subject = SUBJECT
    body    = BODY % dict( day = DAYS[ values[ 'day' ] ],
                           hour = values[ 'hour' ] )
    mail    = create_message( body, subject, values[ 'mail_address' ] )
    return mail

def process_mail( values ):
    'get uta, and send mail'
    mail = create_mail( values )
    send_mail( mail, values[ 'mail_address' ] )

MSG_VALIDATION = '<div class="message">メールアドレスを正しく入力してください</div>'
MSG_ERROR      = '<div class="message">申し訳ありません。エラーが発生しましたので再度お試しください</div>'
CHECKED  = 'checked = "checked" '

def render_html( values, message ):
    'create html to display'
    vertical, horizontal = CHECKED, ''
    if 'horizontal' == values[ 'direction' ]:
        vertical, horizontal = horizontal, vertical

    html = REGISTER_TEMPLATE % dict(
        message           = message,
        mail_address      = values[ 'mail_address' ],
        vertical          = vertical,
        horizontal        = horizontal,
        ) + FOOTER_TEMPLATE
    return html

def display_page( html ):
    'display html page'
    print 'Content-Type: text/html\n'
    print html

def preprocess():
    'prepare main process'
    form   = cgi.FieldStorage()
    values = get_values( form )
    return values, validate( values )

def process( values, validated ):
    'main process'
    registered = False
    message    = ''
    try:
        if 'submitted' == values[ 'submitted' ]:
            if validated:
                register( values )
                process_mail( values )
                registered = True
            else:
                message = MSG_VALIDATION
    except:
        message = MSG_ERROR
        error_handler()
    finally:
        if registered:
            print 'Location: http://tmkc.pgq.jp/manyou/registered.html\n'
        else:
            html = render_html( values, message )
            display_page( html )

def do_it():
    'do it'
    values, validated = preprocess()
    process( values, validated )

if '__main__' == __name__:
    do_it()
