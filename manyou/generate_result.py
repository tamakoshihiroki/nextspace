#!/usr/local/bin/python
# -*- coding: utf-8; -*-

"""
generate result.html
"""

from templates     import RESULT_TEMPLATE, FOOTER_TEMPLATE
from controller    import transition_of_num_of_registered
from error_handler import error_handler
from datetime      import datetime, timedelta

ROW = '[ new Date(%(year)d, %(month)d, %(day)d), %(number)d ]'

def render_html():
    'render html'
    transition = transition_of_num_of_registered()
    rows       = ',\n'.join( [ ROW % dict( year   = item[ 'date' ].year,
                                           month  = item[ 'date' ].month -1,
                                           day    = item[ 'date' ].day,
                                           number = item[ 'number' ], )
                               for item in transition ] )
    now        = datetime.now() - timedelta( days = 1 )
    html       = RESULT_TEMPLATE % dict(
        year   = now.year,
        month  = now.month,
        day    = now.day,
        number = transition[ -1 ][ 'number' ],
        rows   = rows
        ) + FOOTER_TEMPLATE
    return html

def display_html( html ):
    'display html page'
    print 'Content-Type: text/html\n'
    print html

def create_html( html ):
    'create result.html'
    result = open( 'result.html', 'w' )
    result.write( html )
    result.close()

def do_it():
    'do it'
    try:
        html = render_html()
        create_html( html )
    except:
        error_handler()

if '__main__' == __name__:
    do_it()
