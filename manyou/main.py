#!/usr/local/bin/python
# -*- coding: utf-8; -*-

"""
main routine
"""

from database      import database_open, database_close
from datetime      import date
from controller    import get_user_by_date, get_uta_by_indices
from controller    import increment_send_index
from mailer        import create_subject, create_body, create_message
from mailer        import get_smtpserver, send_mail
from error_handler import error_handler
import sys
import calendar

def get_day():
    'get now as holiday or weekday'
    today = date.today()
    cal   = calendar.monthcalendar( today.year, today.month )
    for week in cal:
        if today.day in week:
            index = week.index( today.day )
            break
    if 5 == index or 6 == index:
        return 'holiday'
    else:
        return 'weekday'

def process_user( user, utas, database, smtpserver ):
    'process one user'
    try:
        uta          = utas[ user[ 'send_index' ] ]
        mail_address = user[ 'mail_address' ]
        subject      = create_subject( uta )
        body         = create_body( user[ 'direction' ], uta,
                                    user[ 'column' ], user[ 'row' ] )
        mail         = create_message( body, subject, mail_address )
        if send_mail( mail, mail_address, smtpserver ):
            increment_send_index( database, mail_address )
    except:
        error_handler()

def do_it():
    'do it'
    try:
        database   = database_open()
        day, hour  = get_day(), int( sys.argv[ 1 ] )
        users      = get_user_by_date( database, day, hour )
        if not users:
            database_close( database )
            return
        utas       = get_uta_by_indices(
            database, [ user[ 'send_index' ] for user in users ] )
        smtpserver = get_smtpserver()
        for user in users:
            process_user( user, utas, database, smtpserver )
        database_close( database )
        smtpserver.close()
    except:
        error_handler()

if '__main__' == __name__:
    do_it()
