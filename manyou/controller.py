# -*- coding: utf-8; -*-

"""
controller
"""

from datetime import datetime
from database import database_open, database_close
from database import database_fetch, database_execute

NUM_OF_UTA = 4566

# def get_uta_by_indices( database, indices )
# def get_uta_by_keyword( database, keyword )
# def get_user_by_mail( database, mail_address )
# def get_user_by_date( database, day, hour )
# def register_user( database, mail_address, direction, column, row, day, hour )
# def cancel_user( database, mail_address )
# def increment_send_index( database, mail_address )
# def num_of_registered()
# def transition_of_num_of_registered()

def dec( string ):
    'decode string from database into unicode'
    return string.decode( 'euc_jisx0213' )

def get_uta_by_indices( database, indices ):
    """
    Returns the unicode encoded uta corresponding to index,
    dictionary of number, subject, kundoku
    """
    indices = set( [ index % NUM_OF_UTA for index in indices ] )
    query   = ''.join( [ 'SELECT id, number, subject, kundoku FROM ',
                         'manyoushu_text WHERE ',
                         ' OR '.join( [ 'id = %d' % index
                                        for index in indices ] ) ] )
    fetched = database_fetch( database, query )
    return dict( [ [ int( uta[ 'id' ] ),
                     dict( number  = dec( uta[ 'number' ] ),
                           subject = dec( uta[ 'subject' ] ),
                           kundoku = dec( uta[ 'kundoku' ] ), ) ]
                   for uta in fetched ] )

SQL_UTA_BY_KEYWORD = """
SELECT
 id, number, subject, original, kundoku, kana, sachu, koui, jikou, kuni
FROM
 manyoushu_text
WHERE
"""
SAFTY_TABLE = [
    ( u'\u00a6', u'\u007c' ), #broken bar=>vertical bar
    ( u'\u2014', u'\u2015' ), #horizontal bar=>em dash
    ( u'\u2225', u'\u2016' ), #parallel to=>double vertical line
    ( u'\uff0d', u'\u2212' ), #minus sign=>fullwidth hyphen minus
    ( u'\uff5e', u'\u301c' ), #fullwidth tilde=>wave dash
    ( u'\uffe0', u'\u00a2' ), #fullwidth cent sign=>cent sign
    ( u'\uffe1', u'\u00a3' ), #fullwidth pound sign=>pound sign
    ( u'\uffe2', u'\u00ac' ), #fullwidth not sign=>not sign
    ]

def unsafe2safe(string):
    'convert unsafe character to safe one'
    for unsafe, safe in SAFTY_TABLE:
        string = string.replace( unsafe, safe )
    return string

def get_uta_by_keyword( database, keyword ):
    """
    Returns the unicode encoded uta corresponding to index,
    dictionary of number, subject, kundoku
    """
    keyword = unsafe2safe( keyword.decode( 'utf-8' ) )
    where   = ' OR '.join(
        [ '%(key)s LIKE \'%%%(target)s%%\'' % dict
          ( key    = key,
            target = '%'.join( [ char
                                 for char in keyword ] ) )
          for key in [ 'subject', 'original', 'kundoku', 'kana', 'sachu',
                       'koui', 'jikou', 'kuni' ] ] )
    query   = SQL_UTA_BY_KEYWORD + where
    fetched = database_fetch( database, query )
    return dict( [ [ int( uta[ 'id' ] ),
                     dict( number   = dec( uta[ 'number' ] ),
                           subject  = dec( uta[ 'subject' ] ),
                           original = dec( uta[ 'original' ] ),
                           kundoku  = dec( uta[ 'kundoku' ] ),
                           kana     = dec( uta[ 'kana' ] ),
                           sachu    = dec( uta[ 'sachu' ] ),
                           koui     = dec( uta[ 'koui' ] ),
                           jikou    = dec( uta[ 'jikou' ] ),
                           kuni     = dec( uta[ 'kuni' ] ), ) ]
                   for uta in fetched ] )

def get_user_by_mail( database, mail_address ):
    "get user id from user's mail address"
    query   = ''.join( [ 'SELECT id FROM manyoushu_personal_information WHERE ',
                         'mail_address = \'%s\'' % mail_address ] )
    fetched = database_fetch( database, query )
    if len( fetched ) < 1:
        return None
    else:
        return fetched[ 0 ]

SQL_USER_DATE = """SELECT
 id, mail_address, send_index, direction, `column`, row, day
FROM
 manyoushu_personal_information
WHERE
 is_canceled = FALSE AND
 ( day = 'everyday' OR day = '%(day)s' ) AND
 hour = %(hour)d
"""

def get_user_by_date( database, day, hour ):
    'get users corresponding to day and hour'
    query = SQL_USER_DATE % dict( day = day, hour = hour )
    return database_fetch( database, query )

SQL_REGISTER = """
INSERT INTO
 manyoushu_personal_information
 ( `mail_address`, `send_index`, `direction`, `column`, `row`, `day`, `hour`, `register_date`, `is_canceled` )
VALUES (
 '%(mail_address)s',
 1,
 '%(direction)s',
 %(column)d,
 %(row)d,
 '%(day)s',
 %(hour)d,
 '%(datetime)s',
 FALSE
 )
"""

SQL_UPDATE = """
UPDATE
 manyoushu_personal_information
SET
 `direction` = '%(direction)s',
 `column` = %(column)d,
 `row` = %(row)d,
 `day` = '%(day)s',
 `hour` = %(hour)d,
 `cancel_date` = '0000/00/00 00:00:00',
 `is_canceled` = FALSE
WHERE
 mail_address = '%(mail_address)s'
"""

def update_user( database,
                 mail_address, direction, column, row, day, hour ):
    'register or update user information'
    mail_address = mail_address.strip()
    if get_user_by_mail( database, mail_address ):
        query = SQL_UPDATE % dict(
            direction    = direction,
            column       = column,
            row          = row,
            day          = day,
            hour         = hour,
            mail_address = mail_address )
    else:
        query = SQL_REGISTER % dict(
            mail_address = mail_address,
            direction    = direction,
            column       = column,
            row          = row,
            day          = day,
            hour         = hour,
            datetime     = ( '%s' % datetime.now() )[ : 19 ] )
    database_execute( database, query )

SQL_CANCEL = """
UPDATE
 manyoushu_personal_information
SET
 cancel_date = \'%(datetime)s\',
 is_canceled = TRUE
WHERE
 mail_address = \'%(mail_address)s\'
"""

def cancel_user( database, mail_address ):
    'cencel the registration of the user'
    mail_address = mail_address.strip()
    query        = SQL_CANCEL % dict(
        datetime     = ( '%s' % datetime.now() )[ : 19 ],
        mail_address = mail_address )
    database_execute( database, query )

SQL_INCREMENT = """UPDATE
 manyoushu_personal_information
SET
 send_index = send_index + 1
WHERE
 mail_address = '%(mail_address)s'"""

def increment_send_index( database, mail_address ):
    'increment the uta index to send next of specified user'
    mail_address = mail_address.strip()
    query        = SQL_INCREMENT % dict( mail_address = mail_address )
    database_execute( database, query )

SQL_NUM_OF_REGISTERED = """
SELECT
 COUNT( * )
FROM
 manyoushu_personal_information
WHERE
 is_canceled = FALSE
"""

def num_of_registered():
    'the number of registerd users'
    database = database_open()
    fetched  = database_fetch( database, SQL_NUM_OF_REGISTERED )
    database_close( database )
    try:
        return fetched[ 0 ][ 'COUNT( * )' ]
    except:
        return 0

SQL_TRANSITION_USERS = """
SELECT
 t1.date        AS date,
 COUNT( t2.id ) AS number
FROM
 ( SELECT
    CAST( t1.register_date AS DATE ) AS date
   FROM
    manyoushu_personal_information AS t1
   GROUP BY
    date
   UNION
   SELECT
    CAST( t1.cancel_date AS DATE ) AS date
   FROM
    manyoushu_personal_information AS t1
   GROUP BY
    date ) AS t1,
 manyoushu_personal_information AS t2
WHERE
 CAST( t2.register_date AS DATE ) <= t1.date AND
 ( CAST( t2.cancel_date AS DATE ) = '0000/00/00' OR
   t1.date <= CAST( t2.cancel_date AS DATE ) )
GROUP BY
 date
"""

def transition_of_num_of_registered():
    'the transition of number of registered users'
    database = database_open()
    fetched  = database_fetch( database, SQL_TRANSITION_USERS )
    database_close( database )
    return fetched
