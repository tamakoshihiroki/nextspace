# -*- coding: utf-8; -*-

"""
CyberAgent FX
"""

from common   import soupfy
from common   import update_currency
from datetime import date

SERVICES = dict(
    cyberagent_fx = 'http://www.gaikaex.net/mark/swap_calendar_frame.html',
    )
TABLE_INDEX = dict(
    days = dict(
        USDJPY = 5,
        EURJPY = 7,
        AUDJPY = 11,
        NZDJPY = 13,
        GBPJPY = 15,
        CHFJPY = 17,
        CADJPY = 19,
        ZARJPY = 21,
        ),
    swapbuy = dict(
        USDJPY = 3,
        EURJPY = 5,
        AUDJPY = 9,
        NZDJPY = 11,
        GBPJPY = 13,
        CHFJPY = 15,
        CADJPY = 17,
        ZARJPY = 19,
        ),
    )

def process_url( service_name, url, database ):
    "process"
    soup  = soupfy( url )

    year  = str( date.today().year )

    trs   = soup.findAll( 'tr' )
    rows  = []
    i     = 0
    while True:
        try:
            rows.append( ( trs[ i ], trs[ i + 1 ], trs[ i + 2 ] ) )
            i += 3
        except:
            break

    data  = []
    for row in rows:
        for currency in [ 'USDJPY', 'EURJPY', 'AUDJPY', 'NZDJPY', 'GBPJPY',
                          'CHFJPY', 'CADJPY', 'ZARJPY', ]:
            try:
                days = int(
                    row[ 0 ].contents[
                        TABLE_INDEX[ 'days' ][ currency ] ].contents[ 0 ] )
                if days:
                    data.append( dict(
                            data_date    = '/'.join(
                                [ year,
                                  row[ 0 ].contents[ 1 ].contents[ 0 ].replace( '&nbsp;', '' ).replace( '\n', '' ) ] ),
                            service_name = service_name,
                            currency     = currency,
                            days         = days,
                            swapbuy      = int(
                                row[ 1 ].contents[
                                    TABLE_INDEX[ 'swapbuy' ][ currency ]
                                    ].contents[ 0 ] ),
                            ) )
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
