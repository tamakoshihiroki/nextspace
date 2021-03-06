# -*- coding: utf-8; -*-

"""
外為どっとコム
"""

from common import soupfy
from common import update_currency
import re

SERVICES = dict(
    gaitame_dotcom = 'http://www.gaitame.com/market/swap.html',
    )
YEN_MATCH = re.compile( u'([---0-9]+)円' )

def process_url( service_name, url, database ):
    "process"
    soup  = soupfy( url )

    data_date = soup.find( 'h2' ).string[ : 10 ]

    currencies = { 'US' : 'USDJPY', 'EU' : 'EURJPY', 'AU' : 'AUDJPY',
                   'UK' : 'GBPJPY', 'NZ' : 'NZDJPY', 'CA' : 'CADJPY',
                   'SW' : 'CHFJPY', 'HK' : 'HKDJPY', 'SA' : 'ZARJPY', }

    data = []
    for alt, currency in currencies.iteritems():
        row = soup.find(
            lambda tag:
                ( 'tr' == tag.name and tag.find( 'td' ) and
                  tag.find( 'img', attrs = { 'alt' : alt } ) and
                  tag.find( 'img', attrs = { 'src' : '../img/icon_kokki08.gif' } ) ) )
        for index, service_name in [ ( 3, 'gaitame_dotcom_next' ), ]:
            match = YEN_MATCH.match( row.contents[ index ].string )
            try:
                swapbuy = int( match.group( 1 ) )
                data.append( dict(
                        data_date    = data_date,
                        service_name = service_name,
                        currency     = currency,
                        days         = 1,
                        swapbuy      = swapbuy ) )
            except:
                pass

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
