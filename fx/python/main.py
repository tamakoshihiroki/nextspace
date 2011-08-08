SERVICES = [ 'central_tanshifx',
             'forland',
             'min_fx',
             'MJ',
             'cyberagent_fx',
             'gaitame_dotcom',
             'ntt_smart_trade',
             'himawari_fx',
             ]

from common import open_db_connection
from common import get_mail, send_mail

if '__main__' == __name__:
    database = open_db_connection()
#     database = None
    for service in SERVICES:
        try:
            s = __import__( ''.join( [ 'services/', service ] ) )
            s.do_it( database )
        except:
            import traceback
            stacktrace = traceback.format_exc()
            message    = get_mail( stacktrace )
            send_mail( message, 'tamakoshihiroki@gmail.com' )
            print stacktrace
    database.close()
