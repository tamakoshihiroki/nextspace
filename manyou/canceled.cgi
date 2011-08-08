#!/usr/local/bin/python
# -*- coding: utf-8; -*-

"""
cancel.cgi
"""

from templates     import CANCEL_TEMPLATE, FOOTER_TEMPLATE
from database      import database_open, database_close
from controller    import cancel_user
from form          import get_form_value
from error_handler import error_handler
import cgi
import cgitb

cgitb.enable( display = 0, logdir = 'log' )

def get_values( form ):
    'get values from form'
    return dict( 
        mail_address = get_form_value( form, 'mail_address', '' ),
        )

def cancel( values ):
    'cancel user'
    database     = database_open()
    cancel_user( database, values[ 'mail_address' ] )
    database_close( database )

MSG_RIGHT = """<h1>利用解除の完了</h1>

 <p>
 利用を解除致しました。ご利用、ありがとうございました。
 </p>
"""
MSG_ERROR = '<div class="message">申し訳ありません。エラーが発生しましたので再度お試しください</div>'

def render_html( message ):
    'render html to display'
    return CANCEL_TEMPLATE % dict( message = message ) + FOOTER_TEMPLATE

def display_html( html ):
    'display html page'
    print 'Content-Type: text/html\n'
    print html

def do_it():
    'do it'
    try:
        values = get_values( cgi.FieldStorage() )
        cancel( values )
        message = MSG_RIGHT
    except:
        message = MSG_ERROR
        error_handler()
    finally:
        html   = render_html( message )
        display_html( html )

if '__main__' == __name__:
    do_it()
