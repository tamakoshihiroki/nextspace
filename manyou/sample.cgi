#!/usr/local/bin/python
# -*- coding: utf-8; -*-

"""
sample.cgi
"""

from templates     import SAMPLE_TEMPLATE, FOOTER_TEMPLATE
from database      import database_open, database_close
from controller    import get_uta_by_indices
from mailer        import create_subject, create_body, create_message, send_mail
from form          import get_form_value
from validator     import validate_mail_address
from error_handler import error_handler
import random
import cgi
import cgitb

cgitb.enable( display = 0, logdir = 'log' )

def get_values( form ):
    'get values from form'
    result = dict(
        submitted    = get_form_value( form, 'submitted', '' ),
        mail_address = get_form_value( form, 'mail_address', '' ),
        direction    = get_form_value( form, 'direction', 'vertical' ),
        column       = int( get_form_value( form, 'column', 7 ) ),
        row          = int( get_form_value( form, 'row', 11 ) ),
        choice       = get_form_value( form, 'choice', 'random' ),
        )
    if 'random' == result[ 'choice' ]:
        result[ 'number' ] = 1
        result[ 'send_number' ] = int( random.random() * 4565 + 1 )
    else:
        result[ 'number' ] = int( get_form_value( form, 'number', 1 ) )
        result[ 'send_number' ] = result[ 'number' ]
    return result

def validate( values ):
    'true if all values are appropriate'
    return (
        validate_mail_address( values[ 'mail_address' ] ) and
        ( 'vertical' == values[ 'direction' ] or
          'horizontal' == values[ 'direction' ] ) and
        ( 6 <= values[ 'column' ] and values[ 'column' ] <= 12 ) and
        ( 9 <= values[ 'row' ] and values[ 'row' ] <= 15 ) and
        ( 'random' == values[ 'choice' ] or 'index' == values[ 'choice' ] ) and
        ( 1 <= values[ 'number' ] ) )

def get_uta( values ):
    'get uta'
    database = database_open()
    uta      = get_uta_by_indices( database, [ values[ 'send_number' ] ] )
    database_close( database )
    return uta[ values[ 'send_number' ] ]

def create_mail( uta, values ):
    'create mail'
    subject = create_subject( uta )
    body    = create_body( values[ 'direction' ], uta,
                           values[ 'column' ], values[ 'row' ] )
    mail    = create_message( body, subject, values[ 'mail_address' ] )
    return mail

def process_mail( values ):
    'get uta, and send mail'
    uta  = get_uta( values )
    mail = create_mail( uta, values )
    send_mail( mail, values[ 'mail_address' ] )

MSG_RIGHT      = '<div class="message">%(mail_address)sに送信しました</div>'
MSG_VALIDATION = '<div class="message">メールアドレスを正しく入力してください</div>'
MSG_ERROR      = '<div class="message">申し訳ありません。エラーが発生しましたので再度お試しください</div>'
CHECKED  = 'checked = "checked" '
SELECTED = 'selected = "selected"'

def create_html( values, message ):
    'create html to display'
    vertical, horizontal = CHECKED, ''
    if 'horizontal' == values[ 'direction' ]:
        vertical, horizontal = horizontal, vertical

    rand, index = CHECKED, ''
    if 'index' == values[ 'choice' ]:
        rand, index = index, rand
        
    html = SAMPLE_TEMPLATE % dict(
        message           = message,
        mail_address      = values[ 'mail_address' ],
        vertical          = vertical,
        horizontal        = horizontal,
        random            = rand,
        index             = index,
        number            = values[ 'number' ], ) + FOOTER_TEMPLATE
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
    try:
        if '' == values[ 'submitted' ]:
            message = ''
        if 'submitted' == values[ 'submitted' ]:
            if validated:
                message = MSG_RIGHT % dict(
                    mail_address = values[ 'mail_address' ] )
                process_mail( values )
            else:
                message = MSG_VALIDATION
    except:
        message = MSG_ERROR
        error_handler()
    finally:
        html = create_html( values, message )
        try:
            display_page( html )
        except IOError:
            pass

def do_it():
    'do it'
    values, validated = preprocess()
    process( values, validated )

if '__main__' == __name__:
    do_it()
