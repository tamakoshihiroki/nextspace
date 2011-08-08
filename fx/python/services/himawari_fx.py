# -*- coding: utf-8; -*-

"""
ひまわりFX
"""

from common   import soupfy
from common   import update_currency
from datetime import date
import re

SERVICES = dict(
    himawari_fx = 'https://sec.himawari-group.co.jp/fx/outline/trade/swap/index.do',
    )
YEN_MATCH = re.compile( u'([0-9---]+)円' )

def process_url( service_name, url, database ):
    "process"
    year  = str( date.today().year )

    soup  = soupfy( url )

    currencies = {
        'USD/JPY' : 'USDJPY', 'EUR/JPY' : 'EURJPY', 'GBP/JPY' : 'GBPJPY',
        'AUD/JPY' : 'AUDJPY', 'NZD/JPY' : 'NZDJPY', 'CAD/JPY' : 'CADJPY',
        'CHF/JPY' : 'CHFJPY', 'SGD/JPY' : 'SGDJPY', 'NOK/JPY' : 'NOKJPY',
        'SEK/JPY' : 'SEKJPY', 'HKD/JPY' : 'HKDJPY', 'ZAR/JPY' : 'ZARJPY', }

    data = []
    for abbr, currency in currencies.iteritems():
        row = soup.find(
            lambda tag:
                ( 'tr' == tag.name and
                  tag.find( 'th',  attrs = { 'scope' : 'row' } ) and
                  abbr == tag.findAll(
                    'th',  attrs = { 'scope' : 'row' } )[ 1 ].string
                  ) )
        try:
            data_date = row.findAll(
                'td', attrs = { 'class' : 'date' } )[ 1 ].string
            days      = row.find(
                'td', attrs = { 'class' : 'swapDay' } ).string
            swapbuy   = row.contents[ 13 ].span.string
            match     = YEN_MATCH.match( swapbuy.string )
            swapbuy   = int( match.group( 1 ) )
            data.append( dict(
                    data_date    = '/'.join( [ year, data_date ] ),
                    service_name = service_name,
                    currency     = currency,
                    days         = int( days ),
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
