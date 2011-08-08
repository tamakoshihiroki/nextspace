# -*- coding: utf-8; -*-

"""
database abstraction
"""

HOST     = 'mysql01.next-space.jp'
DATABASE = 'n030044102'
DBUSER   = 'n030044102'
DBPASSWD = 'qwertyuiop'

### manyoushu_text
## id       SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY
## number   VARCHAR(12)
## subject  VARCHAR(282)
## original VARCHAR(166)
## kundoku  VARCHAR(3104)
## kana     VARCHAR(1195)
## sachu    VARCHAR(313)
## koui     VARCHAR(446)
## jikou    VARCHAR(66)
## kuni     VARCHAR(2969)

### manyoushu_personal_information
## id            INT UNSIGNED AUTO_INCREMENT PRIMARY KEY
## mail_address  VARCHAR(240) UNIQUE
## send_index    SMALLINT UNSIGNED
## direction     VARCHAR(10)
## column        TINYINT UNSIGNED
## row           TINYINT UNSIGNED
## day           VARCHAR(8) INDEX
## hour          TINYINT UNSIGNED INDEX
## register_date TIMESTAMP
## cancel_date   TIMESTAMP
## is_canceled   BOOL INDEX

import MySQLdb
from MySQLdb.cursors import DictCursor
from time            import sleep

def database_open():
    """
    Returns database connection, wrapper function for MySQLdb
    """
    database = None
    i        = 0
    while ( None == database and i < 3 ):
        try:
            database = MySQLdb.connect( host = HOST, db = DATABASE,
                                        user = DBUSER, passwd = DBPASSWD,
                                        cursorclass = DictCursor )
            database.cursor().execute( 'SET AUTOCOMMIT = 1' )
        except:
            sleep( 5 )
        i = i + 1
    return database

def database_close( database ):
    """
    Close database connection
    """
    database.close()

def database_execute( database, sql ):
    'execute sql'
    cursor = database.cursor()
    cursor.execute( sql )
    cursor.close()

def database_fetch( database, sql ):
    'select rows by sql'
    cursor  = database.cursor()
    cursor.execute( sql )
    fetched = cursor.fetchall()
    cursor.close()
    return list( fetched )
