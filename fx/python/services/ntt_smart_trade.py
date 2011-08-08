# -*- coding: utf-8; -*-

"""
NTTスマートトレード
"""

from common import soupfy
from common import update_currency
from common import get_weekday

SERVICES = dict(
    ntt_smart_trade = 'http://web.nttsmarttrade.co.jp/swap/SWAP21.xml',
    )
CURRENCIES = [ 'USDJPY', 'EURJPY', 'GBPJPY', 'CADJPY', 'AUDJPY', 'NZDJPY',
               'CHFJPY', 'ZARJPY', 'HKDJPY', 'SGDJPY', ]

def process_url( service_name, url, database ):
    "process"
    soup = soupfy( url )
    weekday = get_weekday()
    if 0 == weekday:
        days = 3
    else:
        days = 1

    data = []
    for currency in soup.findAll( 'swapdata' ):
        if currency.currencypairname.string in CURRENCIES:
            data.append( dict(
                    data_date    = currency.rollto.string,
                    service_name = service_name,
                    currency     = currency.currencypairname.string,
                    days         = days,
                    swapbuy      = int(
                        float( currency.swapbuy.string ) * 10000 + 0.1),
                    ) )

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
