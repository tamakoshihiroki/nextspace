#!/usr/local/bin/python
# -*- coding: utf-8; -*-

"""
search.cgi
"""

from templates     import SEARCH_TEMPLATE, SEARCHED_TABLE_TEMPLATE
from templates     import RECOMMEND_FOOTER, FOOTER_TEMPLATE
from form          import get_form_value
from database      import database_open, database_close
from controller    import get_uta_by_keyword
from error_handler import error_handler
import cgi
import cgitb

cgitb.enable( display = 0, logdir = 'log' )

def get_values( form ):
    'get values from form'
    return dict(
        submitted = get_form_value( form, 'submitted', '' ),
        keyword   = get_form_value( form, 'keyword', '' ),
        )

def get_uta( values ):
    'get uta'
    if values[ 'keyword' ]:
        database = database_open()
        uta      = get_uta_by_keyword( database, values[ 'keyword' ] )
        database_close( database )
    else:
        uta = {}
    return uta

MSG_FOUND     = """<div class="normal-message">
<p>%(number)d件見つかりました</p>
</div>"""
MSG_NOT_FOUND = """<div class="message">
<p>「%(keyword)s」に関する歌が見つかりませんでした</p>
<p>文字数を減らしてもう一度検索してみてください</p>
</div>"""
MSG_ERROR     = '<div class="message">申し訳ありません。エラーが発生しましたので再度お試しください</div>'

def render_message( values, uta, message = '' ):
    'render message html'
    if message:
        return message
    if values[ 'submitted' ] and values[ 'keyword' ]:
        if uta:
            message = MSG_FOUND % dict( number = len( uta ) )
        else:
            message = MSG_NOT_FOUND % dict( keyword = values[ 'keyword' ] )
    return message

def utf8( string ):
    'ecode string to utf8'
    return string.encode( 'utf-8' )

def render_table( uta ):
    'render table html'
    return ''.join( [ SEARCHED_TABLE_TEMPLATE % dict(
                number   = utf8( item[ 'number' ] ),
                subject  = utf8( item[ 'subject' ] ),
                original = utf8( item[ 'original' ] ),
                kundoku  = utf8( item[ 'kundoku' ] ),
                kana     = utf8( item[ 'kana' ] ),
                sachu    = utf8( item[ 'sachu' ] ),
                koui     = utf8( item[ 'koui' ] ),
                jikou    = utf8( item[ 'jikou' ] ),
                kuni     = utf8( item[ 'kuni' ] ),
                )
                      for item in uta.itervalues() ] )

def render_recommendation( values, uta ):
    'render recommendation html'
    if values[ 'submitted' ] and ( not values[ 'keyword' ] or
                                   values[ 'keyword' ] and not uta ):
        return RECOMMEND_FOOTER
    else:
        return ''

def render_html( values, uta, message ):
    'render html'
    return SEARCH_TEMPLATE % dict(
        keyword        = values[ 'keyword' ],
        message        = render_message( values, uta, message ),
        table          = render_table( uta ),
        recommendation = render_recommendation( values, uta )
        ) + FOOTER_TEMPLATE 

def display_html( html ):
    'display html'
    print 'Content-Type: text/html\n'
    print html    

def preprocess():
    'prepare main process'
    form   = cgi.FieldStorage()
    values = get_values( form )
    return values

def process( values ):
    'main process'
    message = ''
    try:
        uta = get_uta( values )
    except:
        message = MSG_ERROR
        error_handler()
    finally:
        try:
            html = render_html( values, uta, message )
        except:
            html = render_html( values, {}, message )
            error_handler()
        finally:
            try:
                display_html( html )
            except IOError:
                pass

def do_it():
    'do it'
    values = preprocess()
    process( values )

if '__main__' == __name__:
    do_it()
