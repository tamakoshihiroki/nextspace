# -*- coding: utf-8; -*-

"""
みんなのFX
"""

from common   import soupfy
from common   import update_currency
from datetime import datetime
import re

SERVICES = dict(
    min_fx = 'http://min-fx.jp/service/calendar/swapcalendar.php?col=8&pair=USDJPY,EURJPY,GBPJPY,AUDJPY,NZDJPY,CADJPY,CHFJPY,ZARJPY',
    )
CURRENCIES = [
    'USDJPY',
    'EURJPY',
    'GBPJPY',
    'AUDJPY',
    'NZDJPY',
    'CADJPY',
    'CHFJPY',
    'ZARJPY',
    ]
DATE_MATCH = re.compile( u'([0-9]+)/([0-9]+)' )

def process_url( service_name, url, database ):
    "process"
    soup  = soupfy( url )

    rows = soup.findAll( lambda tag : 'tr' == tag.name and tag.find( 'td' ) )

    date  = rows[ 0 ].td.string
    match = DATE_MATCH.match( date )
    year  = str( datetime.now().year )
    month = match.group( 1 )
    day   = match.group( 2 )
    data_date = '/'.join( [ year, month, day ] )

    rows_days  = rows[ 0 ].findAll( 'td' )[ 2 : ]

    swaps      = rows[ 1 ].findAll( 'td', attrs = { 'class' : 'plus' } )
    currencies = zip( CURRENCIES, zip( rows_days, swaps ) )

    data = []
    for currency, tags in currencies:
        days = int( tags[ 0 ].string )
        if days:
            if 'ZARJPY' == currency:
                swapbuy = int( tags[ 1 ].string ) / 10
            else:
                swapbuy = int( tags[ 1 ].string )
            data.append( dict(
                    data_date    = data_date,
                    service_name = service_name,
                    currency     = currency,
                    days         = days,
                    swapbuy      = swapbuy, ) )
    update_currency( database, data )

def do_it( database ):
    "just do it"
    for service_name, url in SERVICES.iteritems():
        process_url( service_name, url, database )

if '__main__' == __name__:
#     database = open_db_connection()
    database = None
    do_it( database )
#     database.close()
