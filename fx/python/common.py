"""
FX swap retriever
"""

from urllib2       import build_opener
from BeautifulSoup import BeautifulSoup
from datetime      import date
import calendar

USERAGENT = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)'

def get_opener():
    "custom URL opener"
    opener = build_opener()
    opener.addheaders = [ ( 'User-Agent', USERAGENT ) ]
    return opener

def soupfy( url ):
    "parse the HTML identified by url"
    opener = get_opener()
    stream = opener.open( url )
    source = stream.read()
    soup   = BeautifulSoup( source )
    stream.close()
    return soup

def get_weekday():
    "today's weekday"
    today    = date.today()
    return calendar.weekday( today.year, today.month, today.day )

CURRENCY_MAP = dict(
    USDJPY = 1,
    EURJPY = 2,
    GBPJPY = 3,
    CADJPY = 4,
    AUDJPY = 5,
    NZDJPY = 6,
    CHFJPY = 7,
    ZARJPY = 8,
    HKDJPY = 9,
    SGDJPY = 10,
    NOKJPY = 11,
    SEKJPY = 12,
    )
SERVICE_MAP = dict(
    central_tanshifx_direct = 1,
    central_tanshifx_hyper  = 2,
    forland                 = 3,
    min_fx                  = 4,
    mj                      = 5,
    cyberagent_fx           = 6,
    gaitame_dotcom_next     = 7,
    gaitame_dotcom_stage    = 8,
    ntt_smart_trade         = 9,
    himawari_fx             = 10,
    )

HOST     = 'mysql01.next-space.jp'
DATABASE = 'n030044102'
DBUSER   = 'n030044102'
DBPASSWD = 'qwertyuiop'

import MySQLdb
from MySQLdb.cursors import DictCursor

def open_db_connection():
    """
    Returns database connection, wrapper function for MySQLdb
    """
    database = MySQLdb.connect( host = HOST, db = DATABASE,
                                user = DBUSER, passwd = DBPASSWD,
                                cursorclass = DictCursor )
    database.cursor().execute( 'SET AUTOCOMMIT = 1' )
    database.cursor().execute( "SET NAMES 'utf8'" )
    return database

def close_db_connection( database ):
    """
    Close database connection
    """
    database.close()

def update_currency( database, data ):
    """
    insert swap data into database
    """
    if not data:
        return

    query = ''.join( [
            'INSERT IGNORE INTO fx_swap ',
            '( `data_date`, `service_id`, `currency_id`, `days`, `swapbuy` ) ',
            'VALUES ',
            ',\n'.join( [ ''.join( [
                            '(',
                            '\'%s\', ' % datum[ 'data_date' ],
                            '\'%d\', ' % SERVICE_MAP[ datum[ 'service_name' ] ],
                            '\'%d\', ' % CURRENCY_MAP[ datum[ 'currency' ] ],
                            '\'%d\', ' % datum[ 'days' ],
                            '\'%d\' '  % datum[ 'swapbuy' ],
                            ')' ] )
                        for datum in data  ] ),
            ] )
#     print query
    cursor = database.cursor()
    cursor.execute( query )
    cursor.close()

from email.MIMEText      import MIMEText
from email.Header        import Header
from email.Utils         import formatdate
SMTP_SERVER      = '118.82.87.14'
SMTP_SERVER_PORT = 587
SMTP_USER        = 'webantenna@bebit.co.jp'
SMTP_PASSWORD    = 'gizx7ix4'
HEADER_ENCODING  = 'iso-2022-jp'
BODY_ENCODING    = 'iso-2022-jp'

def get_mail( traceback ):
    """
    create mail header and body
    """
    msg              = MIMEText( traceback )
    msg[ 'Subject' ] = Header( 'FX daily cron error' )
    msg[ 'From' ]    = 'FX daily cron'
    msg[ 'To' ]      = 'tamakoshihiroki@gmail.com'
    msg[ 'Date' ]    = formatdate( localtime = 9 )
    msg[ 'Content-Type' ] = ''.join(
        [ 'text/plain; charset="', BODY_ENCODING, '"', ] )
    return msg

def send_mail( message, to ):
    """
    Send mail
    """
    import smtplib
    server = None
    for i in range( 3 ):
        try:
            server = smtplib.SMTP( SMTP_SERVER, SMTP_SERVER_PORT )
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login( SMTP_USER, SMTP_PASSWORD )
        except:
            pass
    if server:
        server.sendmail( 'webantenna@bebit.co.jp',
                         [ to ], message.as_string() )

import string
# API
# /api/swapbuy_graph?date=...&date=...&currency=NZDJPY&service=...&service=...

QUERY_SWAPBUYS = """SELECT
 fx_service.service_name,
 fx_swap.data_date,
 fx_swap.swapbuy,
 fx_swap.days
FROM
 fx_swap,
 fx_currency,
 fx_service
WHERE
 fx_swap.data_date BETWEEN '${date_start}' AND '${date_end}'
 AND fx_currency.currency_name = '${currency}'
 AND fx_service.service_mnemonic IN ( ${services} )
 AND fx_swap.currency_id = fx_currency.currency_id
 AND fx_swap.service_id = fx_service.service_id"""

def get_swapbuy( database, date_start, date_end, currency, services ):
    """
    get swapbuy data for currency of services from date_start to date_end
    """
    query = string.Template( QUERY_SWAPBUYS ).substitute( dict(
            date_start = date_start,
            date_end   = date_end,
            currency   = currency,
            services   = ','.join( [ ''.join( [ '\'', service, '\'' ] )
                                     for service in services ] ) ) )
    cursor = database.cursor()
    cursor.execute( query )
    fetched = cursor.fetchall()
    cursor.close()

    result = {}
    for row in fetched:
        result.setdefault(
            row[ 'service_name' ], {} )[
#             row[ 'data_date' ] ] = row[ 'swapbuy' ]
            row[ 'data_date' ] ] = float( row[ 'swapbuy' ] ) / row[ 'days' ]

    return result
