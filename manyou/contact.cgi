#!/usr/local/bin/python
# -*- coding: utf-8; -*-

"""
cancel.cgi
"""

from templates     import CONTACT_TEMPLATE, FOOTER_TEMPLATE
from mailer        import create_message, send_mail
from form          import get_form_value
from error_handler import error_handler
import cgi
import cgitb

cgitb.enable( display = 0, logdir = 'log' )

def get_values( form ):
    'get values from form'
    return dict( 
        mail_address = get_form_value( form, 'mail_address', '' ),
        content      = get_form_value( form, 'content', '' )
        )

SUBJECT = u'本日の万葉集問い合わせ'
BODY    = u"""
%(mail_address)s

%(content)s
"""

def create_mail( values ):
    'create mail'
    subject = SUBJECT
    body    = BODY % dict(
        mail_address = values[ 'mail_address' ].decode( 'utf-8' ),
        content      = values[ 'content' ].decode( 'utf-8' ), )
    mail    = create_message( body, subject, 'tmkc.igo@gmail.com' )
    return mail

def process_mail( values ):
    'send mail'
    mail = create_mail( values )
    send_mail( mail, 'tmkc.igo@gmail.com' )

MSG_RIGHT = """<h1>お問い合わせの完了</h1>

 <p>
 下記の内容で運営者に連絡しました。ご対応致しますので、しばらくお待ち下さい。
 </p>

 <p>
 メールアドレス: %(mail_address)s
 </p>

 <pre>
 %(content)s
 </pre>
"""
MSG_ERROR = '<div class="message">申し訳ありません。エラーが発生しましたので再度お試しください</div>'

def render_html( message ):
    'render html to display'
    return CONTACT_TEMPLATE % dict( message = message ) + FOOTER_TEMPLATE

def display_html( html ):
    'display html page'
    print 'Content-Type: text/html\n'
    print html

def do_it():
    'do it'
    try:
        values  = get_values( cgi.FieldStorage() )
        process_mail( values )
        message = MSG_RIGHT % values
    except:
        message = MSG_ERROR
        error_handler()
    finally:
        html    = render_html( message )
        display_html( html )

if '__main__' == __name__:
    do_it()
