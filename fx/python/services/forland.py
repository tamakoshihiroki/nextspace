# -*- coding: utf-8; -*-

"""
Forland Forex
"""

from common import soupfy
from common import update_currency
import re

SERVICES = dict(
    forland = 'http://www.foreland.co.jp/service/swap/index.html',
    )
DATE_MATCH = re.compile( u'([0-9]+)年([0-9]+)月([0-9]+)日' )
TABLE_INDEX = dict(
    USDJPY = dict( date =  2, days =  3, swapbuy =  4, ),
    EURJPY = dict( date =  7, days =  8, swapbuy =  9, ),
    GBPJPY = dict( date = 12, days = 13, swapbuy = 14, ),
    AUDJPY = dict( date = 17, days = 18, swapbuy = 19, ),
    NZDJPY = dict( date =  2, days =  3, swapbuy =  4, ),
    CADJPY = dict( date =  7, days =  8, swapbuy =  9, ),
    ZARJPY = dict( date = 12, days = 13, swapbuy = 14, ),
    CHFJPY = dict( date = 17, days = 18, swapbuy = 19, ),
    )

def process_url( service_name, url, database ):
    "process"
    soup  = soupfy( url )

    date  = soup.find( 'p', attrs = { 'class' : 'tableDate' } ).contents[ 0 ]
    match = DATE_MATCH.match( date )
    year  = match.group( 1 )

    tables = soup.findAll( 'table' )
    data   = []
    steps  = { 0 : [ 'USDJPY', 'EURJPY', 'GBPJPY', 'AUDJPY', ],
               1 : [ 'NZDJPY', 'CADJPY', 'ZARJPY', 'CHFJPY', ], }
    for index, currencies in steps.iteritems():
        for row in tables[ index ].findAll(
            lambda tag:
                'tr' == tag.name and tag.find(
                'th', attrs = { 'class' : 'alignR' } ) ):
            for currency in currencies:
                indices = TABLE_INDEX[ currency ]
                try:
                    days         = int(
                        row.contents[ indices[ 'days' ] ].string )
                    if days:
                        data.append( dict(
                                data_date    = '/'.join(
                                    [ year,
                                      row.contents[ indices[ 'date' ] ].string ] ),
                                service_name = service_name,
                                currency     = currency,
                                days         = days,
                                swapbuy      = int(
                                    row.contents[
                                        indices[ 'swapbuy' ] ].span.string ),
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
