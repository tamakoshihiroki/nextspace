# -*- coding: utf-8; -*-

"""
mail functions
"""

SMTP_SERVER      = 'smtp.gmail.com'
SMTP_SERVER_PORT = 587
SMTP_USER        = 'tmkc.igo@gmail.com'
SMTP_PASSWORD    = 'Pz/Fp}(5<pVN15?.'
HEADER_ENCODING  = 'iso-2022-jp'
BODY_ENCODING    = 'iso-2022-jp'

SUBJECT          = u'books error'
FROM             = 'tmkc.igo@gmail.com'

from email.MIMEText import MIMEText
from email.Header   import Header
from email.Utils    import formatdate
from time           import sleep
import smtplib

def create_message( body, to_address ):
    'create mail message'
    msg = MIMEText( body, 'plain', BODY_ENCODING )
    msg[ 'Subject' ] = Header( SUBJECT.encode( HEADER_ENCODING ),
                               HEADER_ENCODING ).encode()
    msg[ 'From']     = FROM
    msg[ 'To' ]      = to_address
    msg[ 'Date' ]    = formatdate( localtime = 9 )
    return msg

def get_smtpserver():
    'get smtpserver object'
    server = None
    i      = 0
    while ( None == server and i < 11 ):
        try:
            server = smtplib.SMTP( SMTP_SERVER, SMTP_SERVER_PORT )
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login( SMTP_USER, SMTP_PASSWORD )
        except:
            sleep( 5 )
        i = i + 1
    return server

def send_mail( message, to_address ):
    'Send mail'
    server = get_smtpserver()
    if server:
        server.sendmail( FROM, [ to_address ], message.as_string() )
