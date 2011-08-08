# -*- coding: utf-8; -*-

HOST             = 'mysql01.next-space.jp'
DATABASE         = 'n030044102'
DBUSER           = 'n030044102'
DBPASSWD         = 'qwertyuiop'

NUM_OF_UTA       = 4566

SMTP_SERVER      = 'smtp.gmail.com'
SMTP_SERVER_PORT = 587
SMTP_USER        = 'tmkc.igo@gmail.com'
SMTP_PASSWORD    = 'Pz/Fp}(5<pVN15?.'
HEADER_ENCODING  = 'iso-2022-jp'
#BODY_ENCODING    = 'shift-jis'

SUBJECT          = u'本日の万葉集%s'
FROM             = 'tmkc.igo@gmail.com'

### manyoushu_text
## id       SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY
## number   VARCHAR(12)
## subject  VARCHAR(282)
## original VARCHAR(166)
## kundoku  VARCHAR(3104)
## kana     VARCHAR(1195)
## sachu    VARCHAR(313)
## koui     VARCHAR(446)
## jikou    VARCHAR(66)
## kuni     VARCHAR(2969)

### manyoushu_personal_information
## id            INT UNSIGNED AUTO_INCREMENT PRIMARY KEY
## mail_address  VARCHAR(240) UNIQUE
## send_index    SMALLINT UNSIGNED
## direction     VARCHAR(10)
## column        TINYINT UNSIGNED
## row           TINYINT UNSIGNED
## day           VARCHAR(8) INDEX
## hour          TINYINT UNSIGNED INDEX
## register_date TIMESTAMP
## cancel_date   TIMESTAMP
## is_canceled   BOOL INDEX

import MySQLdb
import re
from datetime        import datetime
from MySQLdb.cursors import DictCursor
from time            import sleep

def open_db_connection():
    """
    Returns database connection, wrapper function for MySQLdb
    """
    database = None
    i        = 0
    while ( None == database and i < 3 ):
       try:
          database = MySQLdb.connect( host = HOST, db = DATABASE,
                                      user = DBUSER, passwd = DBPASSWD,
                                      cursorclass = DictCursor )
          database.cursor().execute( 'SET AUTOCOMMIT = 1' )
       except:
          sleep( 5 )
       i = i + 1
    return database

def close_db_connection( database ):
    """
    Close database connection
    """
    database.close()

def get_uta( indices, database ):
    """
    Returns the unicode encoded uta corresponding to index,
    dictionary of number, subject, kundoku
    """
    indices = set( [ index % NUM_OF_UTA for index in indices ] )
    query   = ''.join( [ 'SELECT id, number, subject, kundoku FROM ',
                         'manyoushu_text WHERE ',
                         ' OR '.join( [ 'id = %d' % index
                                        for index in indices ] ) ] )
    cursor  = database.cursor()
    cursor.execute( query )
    fetched = cursor.fetchall()
    cursor.close()
    result = {}
    for uta in fetched:
        result[ int( uta[ 'id' ] ) ] = {
            'number'  : uta[ 'number' ].decode( 'euc_jisx0213' ),
            'subject' : uta[ 'subject' ].decode( 'euc_jisx0213' ),
            'kundoku' : uta[ 'kundoku' ].decode( 'euc_jisx0213' ),
            }
    return result

def get_uta_by_keyword( keyword, database ):
    """
    Returns the unicode encoded uta corresponding to index,
    dictionary of number, subject, kundoku
    """
    query   = ''.join(
        [ 'SELECT id, number, subject, original, kundoku, kana, sachu, koui,',
          'jikou, kuni FROM manyoushu_text WHERE ',
          ' OR '.join(
                [ '%s LIKE \'%%%s%%\'' % ( key, '%'.join( [ char for char in keyword.decode( 'utf-8' ) ] ) )
                  for key in [ 'subject', 'original', 'kundoku', 'kana',
                               'sachu', 'koui', 'jikou', 'kuni' ] ] ) ] )
    cursor  = database.cursor()
    cursor.execute( query )
    fetched = cursor.fetchall()
    cursor.close()
    result = {}
    for uta in fetched:
        result[ int( uta[ 'id' ] ) ] = {
            'number'   : uta[ 'number'   ].decode( 'euc_jisx0213' ),
            'subject'  : uta[ 'subject'  ].decode( 'euc_jisx0213' ),
            'original' : uta[ 'original' ].decode( 'euc_jisx0213' ),
            'kundoku'  : uta[ 'kundoku'  ].decode( 'euc_jisx0213' ),
            'kana'     : uta[ 'kana'     ].decode( 'euc_jisx0213' ),
            'sachu'    : uta[ 'sachu'    ].decode( 'euc_jisx0213' ),
            'koui'     : uta[ 'koui'     ].decode( 'euc_jisx0213' ),
            'jikou'    : uta[ 'jikou'    ].decode( 'euc_jisx0213' ),
            'kuni'     : uta[ 'kuni'     ].decode( 'euc_jisx0213' ),
            }
    return result

def tategaki_replace( string ):
    """
    Replace horizontal letters to vertical letters
    """
    string = string.replace( u'[', u'∧' )
    string = string.replace( u']', u'∨' )
    string = string.replace( u'(', u'∧' )
    string = string.replace( u')', u'∨' )
    string = string.replace( u'（', u'∧' )
    string = string.replace( u'）', u'∨' )
    string = string.replace( u'/', u'／' )
    string = string.replace( u'<', u'∧' )
    string = string.replace( u'>', u'∨' )
    return string

def tategaki( name, uta, column, row ):
    """
    Returns tategaki text from uta
    """
    name = tategaki_replace( name )
    uta  = tategaki_replace( uta )
    name_splitted = []
    i = 0
    while True:
        splitted = name[ i : i + row ]
        if splitted:
            splitted = splitted.replace( u' ', u'　' )
            line = []
            for char in range( row ):
                try:
                    line.append( splitted[ char ] )
                except IndexError:
                    line.append( u'　' )
            name_splitted.append( line )
            i += row
        else:
            break
    uta_splitted = []
    i = 0
    while True:
        splitted = uta[ i : i + row ]
        if splitted:
            if ' ' == splitted[ 0 ]:
                i += 1
                splitted = uta[ i : i + row ]
            splitted = splitted.replace( u' ', u'　' )
            line = []
            for char in range( row ):
                try:
                    line.append( splitted[ char ] )
                except IndexError:
                    line.append( u'　' )
            uta_splitted.append( line )
            i += row
        else:
            break
    name_splitted.extend( uta_splitted )
    while True:
        if 0 == len( name_splitted ) % column:
            break
        else:
            name_splitted.append( [ u'　' for _ in range( row ) ] )
    body_splitted = []
    i = 0
    while True:
        splitted = name_splitted[ i : i + column ]
        if splitted:
            splitted.reverse()
            splitted = apply( zip, splitted )
            body_splitted.append( splitted )
            i += column
        else:
            break
    body = '\n\n'.join( [ '\n'.join( [ ' '.join( letters )
                                     for letters in page ] )
                        for page in body_splitted ] )
    return body

from email.MIMEText      import MIMEText
from email.Header        import Header
from email.Utils         import formatdate

def get_mail( direction, uta, to, col, row ):
    """
    Arrange a mail
    """
    number   = uta[ 'number' ]
    name     = uta[ 'subject' ]
    uta_body = uta[ 'kundoku' ].replace( u'  ', ' ' )
    body_encoding = 'iso-2022-jp'
    if ( to.endswith( '@docomo.ne.jp' ) or
         to.endswith( '@ezweb.ne.jp' ) or
         to.endswith( '@softbank.ne.jp' ) or
         to.endswith( 'vodafone.ne.jp' ) ):
        body_encoding = 'shift-jis'
    if 'vertical' == direction:
        body = tategaki( name, uta_body, col, row ).encode( body_encoding )
    elif 'horizontal' == direction:
        body = '\n'.join( [ name.encode( body_encoding ),
                            uta_body.encode( body_encoding ) ] )
    else:
        body = ''
    msg              = MIMEText( body, 'plain', body_encoding )
    msg[ 'Subject' ] = Header( ( SUBJECT % number ).encode(
        HEADER_ENCODING ), HEADER_ENCODING ).encode()
    msg[ 'From' ]    = ''.join(
        [ '"',
          Header( u'本日の万葉集', HEADER_ENCODING ).encode(),
          '" <', FROM, '>' ] )
    msg[ 'To' ]      = to
    msg[ 'Date' ]    = formatdate( localtime = 9 )
    #msg[ 'Content-Type' ] = ''.join( [ 'text/plain; charset="',
    #                                   body_encoding,
    #                                   '"' ] )
    return msg

def get_smtpserver():
    """
    """
    import smtplib
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

def send_mail( message, to ):
    """
    Send mail
    """
    import smtplib
    server = None
    i      = 0
    while ( None == server and i < 3 ):
        try:
            server = smtplib.SMTP( SMTP_SERVER, SMTP_SERVER_PORT )
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login( SMTP_USER, SMTP_PASSWORD )
        except:
            sleep( 5 )
        i = i + 1
    if server:
        server.sendmail( FROM, [ to ], message.as_string() )

def get_form_value( form, name, default_value ):
    try:
        return form[ name ].value
    except KeyError:
        return default_value

usernameRE = re.compile(r"^[^ \t\n\r@<>()]+$", re.I )
domainRE   = re.compile(r"^[a-z0-9][a-z0-9\.\-_]*\.[a-z]+$", re.I )

def validate_mail_address( mail_address ):
    if not mail_address:
        return False
    mail_address = mail_address.strip()
    splitted     = mail_address.split( '@', 1 )
    try:
        username, domain = splitted
    except ValueError:
        return False
    if not usernameRE.search( username ):
        return False
    if not domainRE.search( domain ):
        return False
    return True

def get_user_by_mail( database, mail_address ):
    query  = ''.join( [ 'SELECT id FROM manyoushu_personal_information WHERE ',
                        'mail_address = \'%s\'' % mail_address ] )
    cursor = database.cursor()
    cursor.execute( query )
    fetched = cursor.fetchall()
    cursor.close()
    if len( fetched ) < 1:
        return None
    else:
        return fetched[ 0 ]

def update_user( database,
                 mail_address, direction, column, row, day, hour ):
    mail_address = mail_address.strip()
    if get_user_by_mail( database, mail_address ):
        query = ''.join( [ 'UPDATE manyoushu_personal_information SET ',
                           '`direction` = \'%s\', ' % direction,
                           '`column` = %d, ' % column,
                           '`row` = %d, ' % row,
                           '`day` = \'%s\', ' % day,
                           '`hour` = %d, ' % hour,
                           '`is_canceled` = FALSE ',
                           'WHERE mail_address = \'%s\'' % mail_address ] )
    else:
        query = ''.join( [ 'INSERT INTO manyoushu_personal_information ',
                           '( `mail_address`, `send_index`, `direction`, `column`, `row`, `day`, `hour`, `register_date`, `is_canceled` ) ',
                           'VALUES ( ',
                           '\'%s\', ' % mail_address,
                           '1, \'%s\', ' % direction,
                           '%d, %d, ' % ( column, row ),
                           '\'%s\', %d, ' % ( day, hour ),
                           '\'%s\', ' % ( '%s' % datetime.now() )[ : 19 ],
                           'FALSE ',
                           ')' ] )
    cursor = database.cursor()
    cursor.execute( query )
    cursor.close()

def cancel_user( database, mail_address ):
    mail_address = mail_address.strip()
    query = ''.join( [ 'UPDATE manyoushu_personal_information SET ',
                       'cancel_date = \'%s\', ' % ( '%s' % datetime.now() )[ : 19 ],
                       'is_canceled = TRUE ',
                       'WHERE mail_address = \'%s\'' % mail_address ] )
    cursor = database.cursor()
    cursor.execute( query )
    cursor.close()

def num_of_registered():
    query  = 'SELECT COUNT( * ) FROM manyoushu_personal_information WHERE is_canceled = FALSE'
    database = open_db_connection()
    cursor = database.cursor()
    cursor.execute( query )
    fetched = cursor.fetchall()
    cursor.close()
    database.close()
    try:
        return fetched[ 0 ][ 'COUNT( * )' ]
    except:
        return 0

def increment_send_index( database, mail_address ):
    mail_address = mail_address.strip()
    query = ''.join( [ 'UPDATE manyoushu_personal_information SET ',
                       'send_index = send_index + 1 ',
                       'WHERE mail_address = \'%s\'' % mail_address ] )
    cursor = database.cursor()
    cursor.execute( query )
    cursor.close()

ENGINES = {
    'www.google.'             : 'q',
    'search.yahoo.'           : 'p',
    '.msn.'                   : 'q',
    '.aol.'                   : 'query',
    '.lycos.'                 : 'query',
    '.ask.'                   : 'q',
    '.altavista.'             : 'q',
    '.netscape.'              : 'query',
    '.earthlink.net'          : 'q',
    '.cnn.'                   : 'query',
    'looksmart'               : 'key',
    'about.'                  : 'terms',
    'www.excite.co.jp'        : 'search',
    '.excite.'                : 'qkw',
    '.mamma.com'              : 'query',
    '.alltheweb.com'          : 'q',
    '.gigablast.'             : 'q',
    '.alice.it'               : 'qs',
    'mixi.jp'                 : 'keyword',
    '.hatena.ne.jp'           : 'word',
    '.nifty.com'              : 'Text',
    'so-net.search.goo.ne.jp' : 'keyword',
    'search.goo.ne.jp'        : 'MT',
    '.biglobe.ne.jp'          : 'q',
    '.infoseek.co.jp'         : 'qt',
    '.fresheye.com'           : 'kw',
    '.livedoor.com'           : 'q',
    '.baidu.'                 : 'wd',
    '.marsflag.com'           : 'phrase',
    'ocnsearch.goo.ne.jp'     : 'MT',
    'hi-ho.search.goo.ne.jp'  : 'MT',
    'allabout.'               : 'qs',
    '.mooter.'                : 'keywords',
    '.nikkei.co.jp'           : 'q',
    '.asahi.com'              : 'Query_Key',
    'odn.excite.co.jp'        : 'search',
    'auone.jp'                : 'q',
    }
    
RM_OPS  = re.compile( r'(cache:|link:|related:|site:|daterange:|ip:|domain:|info:|stocks:|filetype:|file:|host:|type:)\S*' )
CUT_OPS = re.compile( r'intitle:|allintitle:|inurl:|allinurl:|inanchor:|allinanchor:|anchor:|allintext:|title:|image:|applet:|url:|define:|\+|---|~' )
U_OPS   = re.compile( r'AND|OR' )
DSPACE  = re.compile( ' +' )
DQUEST  = re.compile( '\?+' )
URLENC  = re.compile( r'(%[0-9A-Fa-f]{2})+' )
UNICODE = re.compile( r'(%u[0-9A-Fa-f]{4})+' )

HEXADECIMAL = { '0' : 0,  '1' : 1,  '2' : 2,  '3' : 3,  '4' : 4,
                '5' : 5,  '6' : 6,  '7' : 7,  '8' : 8,  '9' : 9,
                'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15,
                'a' : 10, 'b' : 11, 'c' : 12, 'd' : 13, 'e' : 14, 'f' : 15,
                }

def decode_encoded_unicode( encoded ):
    """
    Returns unicode string
    Input: encoded: example: %u5916%u70BA%u30C9%u30C3%u30C8
    """
    try:
        return ''.join(
            [ unichr( HEXADECIMAL[ letter[ 2 ] ] * 4096 +
                      HEXADECIMAL[ letter[ 3 ] ] * 256 +
                      HEXADECIMAL[ letter[ 4 ] ] * 16 +
                      HEXADECIMAL[ letter[ 5 ] ] )
              for letter in re.split( '(%u[0-9A-Fa-f]{4})', encoded )
              if letter ] )
    except IndexError:
        return ''

def clean_keyword( keyword ):
    """
    Returns cleaned keyword
    Input:  keyword is url encoded
    Output: utf8 string
    """
    from urllib import unquote_plus
    keyphrase = unquote_plus( keyword )
    for codec in [ 'utf-8', 'euc_jisx0213', 'euc-jp', 'shift-jis',
                   'cp932', 'shift_jisx0213' ]:
        try:
            keyphrase = keyphrase.decode( codec, 'strict' )
            keyphrase = keyphrase.replace( u'　', u' ' )
            keyphrase = RM_OPS.sub(  '', keyphrase )
            keyphrase = CUT_OPS.sub( '', keyphrase )
            keyphrase = U_OPS.sub(   '', keyphrase )
            keyphrase = DSPACE.sub( ' ', keyphrase )
            keyphrase = DQUEST.sub( '?', keyphrase )
            if keyphrase and '' == URLENC.sub( '', keyphrase ):
                keyphrase = clean_keyword( keyphrase ).decode( 'utf-8' )
            if keyphrase and '' == UNICODE.sub( '', keyphrase ):
                keyphrase = decode_encoded_unicode( keyphrase )
            keyphrase = keyphrase[ : 250 ]
            keyphrase = keyphrase.strip().strip( '?' ).strip()
            return keyphrase.encode( 'utf-8' )[ : 750 ]
        except UnicodeDecodeError:
            pass
        except UnicodeEncodeError:
            pass
    return ''

def extract_keyword( referrer ):
    from urlparse import urlparse
    domains = '|'.join( [ domain.replace( '.', '\.' )
                          for domain in ENGINES.keys() ] )
    match_domains = re.findall( domains, referrer )
    if not match_domains:
        return ''
    domain = match_domains[ 0 ]
    _, _, _, _, query, _ = urlparse( referrer )
    query_dict = dict( [ pair.split( '=' )[ 0 : 2 ]
                         for pair in query.split( '&' )
                         if pair.count( '=' ) ] )
    try:
        keyword = query_dict[ ENGINES[ domain ] ]
        return clean_keyword( keyword )
    except KeyError:
        return ''

def print_uta():
    database = open_db_connection()
    uta      = get_uta( [ 1 ], database )
    to       = 'tmkc@wm.pdx.ne.jp'
    for codec in [ 'utf-8', 'euc_jisx0213', 'euc-jp', 'shift-jis',
                   'cp932', 'shift_jisx0213' ]:
        try:
            uta[ 1 ][ 'subject' ].decode( codec, 'strict' )
            print codec
        except:
            pass
    mail     = get_mail( 'vertical', uta[ 1 ], to, 7, 11 )
    send_mail( mail, to )
    close_db_connection( database )
