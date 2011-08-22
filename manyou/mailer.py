# -*- coding: utf-8; -*-

"""
mail functions
"""

SMTP_SERVER      = 'smtp.gmail.com'
SMTP_SERVER_PORT = 587
SMTP_USER        = 'tmkc.igo@gmail.com'
SMTP_PASSWORD    = 'Pz/Fp}(5<pVN15?.'
HEADER_ENCODING  = 'iso-2022-jp'

SUBJECT          = u'本日の万葉集%s'
FROM             = 'tmkc.igo@gmail.com'

from email.MIMEText import MIMEText
from email.Header   import Header
from email.Utils    import formatdate
from smtplib        import SMTPServerDisconnected
from time           import sleep
from tategaki       import tategaki
from error_handler  import error_handler
import smtplib

def body_encoding( to_address ):
    'body text encoding'
    if ( to_address.endswith( '@docomo.ne.jp' ) or
         to_address.endswith( '@ezweb.ne.jp' ) or
         to_address.endswith( '@softbank.ne.jp' ) or
         to_address.endswith( 'vodafone.ne.jp' ) ):
        return 'shift-jis'
    return 'iso-2022-jp'

def create_body( direction, uta, col, row ):
    'create mail body'
    name     = uta[ 'subject' ]
    uta_body = uta[ 'kundoku' ].replace( u'  ', ' ' )
    if 'vertical' == direction:
        return tategaki( name, uta_body, col, row )
    elif 'horizontal' == direction:
        return u'\n'.join( [ name, uta_body ] )
    else:
        return u''

def create_subject( uta ):
    'create mail subject'
    return SUBJECT % uta[ 'number' ]

def create_message( body, subject, to_address ):
    'create mail message'
    encoding = body_encoding( to_address )
    msg              = MIMEText( body.encode( encoding ), 'plain', encoding )
    msg[ 'Subject' ] = Header( subject.encode( HEADER_ENCODING ),
                               HEADER_ENCODING ).encode()
    msg[ 'From' ]    = ''.join(
        [ '"',
          Header( u'本日の万葉集', HEADER_ENCODING ).encode(),
          '" <', FROM, '>' ] )
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

def send_mail( message, to_address, server = None, retry = True ):
    'send mail'
    server_close = False
    if not server:
        server       = get_smtpserver()
        server_close = True
    if server:
        try:
            server.sendmail( FROM, [ to_address ], message.as_string() )
            if server_close:
                server.close()
        except SMTPServerDisconnected:
            server = get_smtpserver()
        except:
            server = None
        finally:
            error_handler()
            if retry:
                send_mail( message, to_address, server, False )
