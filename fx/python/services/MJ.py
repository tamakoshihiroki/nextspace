# -*- coding: utf-8; -*-

"""
MJ
"""

from common   import soupfy
from common   import update_currency
from datetime import date
import re

SERVICES = dict(
    mj = 'http://www.fx-today.net/swap/calendar8.php',
    )
DATE_MATCH = re.compile( u'([0-9]+)月([0-9]+)日' )
TABLE_INDEX = dict(
    USDJPY = dict( days =  3, swapbuy =  5, ),
    EURJPY = dict( days =  9, swapbuy = 11, ),
    GBPJPY = dict( days = 15, swapbuy = 17, ),
    AUDJPY = dict( days = 21, swapbuy = 23, ),
    NZDJPY = dict( days =  3, swapbuy =  5, ),
    CADJPY = dict( days =  9, swapbuy = 11, ),
    ZARJPY = dict( days = 15, swapbuy = 17, ),
    CHFJPY = dict( days = 21, swapbuy = 23, ),
    )

def process_url( service_name, url, database ):
    "process"
    soup  = soupfy( url )

    year  = str( date.today().year )

    tables = [ soup.find( 'div', attrs = { 'id' : 'div1' } ),
               soup.find( 'div', attrs = { 'id' : 'div2' } ) ]
    data   = []
    steps  = { 0 : [ 'USDJPY', 'EURJPY', 'GBPJPY', 'AUDJPY', ],
               1 : [ 'NZDJPY', 'CADJPY', 'CHFJPY', 'ZARJPY', ], }
    for index, currencies in steps.iteritems():
        for row in tables[ index ].findAll( 'tr' ):
            try:
                match = DATE_MATCH.match( row.contents[ 1 ].nobr.string )
                if match:
                    month = match.group( 1 )
                    day   = match.group( 2 )
                else:
                    raise
                for currency in currencies:
                    indices = TABLE_INDEX[ currency ]
                    try:
                        days = days         = int(
                            row.contents[ indices[ 'days' ] ].string )
                        if days:
                            data.append( dict(
                                    data_date    = '/'.join(
                                        [ year, month, day ] ),
                                    service_name = service_name,
                                    currency     = currency,
                                    days         = days,
                                    swapbuy      = int(
                                        row.contents[
                                            indices[ 'swapbuy' ] ].string ),
                                ) )
                    except:
                        pass
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
