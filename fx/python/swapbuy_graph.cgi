#!/usr/local/bin/python

# -*- coding: utf-8; -*-

from common   import open_db_connection
from common   import get_swapbuy
from datetime import date
from types    import ListType
from urllib   import quote
import cgi
import cgitb
import re

cgitb.enable()

DATE_FORMAT = re.compile( '([0-9]+)/([0-9]+)/([0-9]+)' )
FORM        = """<form action="swapbuy_graph.cgi" method="GET">
 <input type="text" name="date_start" value="">
 <input type="text" name="date_end" value="">
 <select name="currency">
  <option value="USD/JPY">USD/JPY</option>
  <option value="EUR/JPY">EUR/JPY</option>
  <option value="GBP/JPY">GBP/JPY</option>
  <option value="AUD/JPY">AUD/JPY</option>
  <option value="NZD/JPY">NZD/JPY</option>
  <option value="ZAR/JPY">ZAR/JPY</option>
 </select>
 <ul style="list-style: none;">
  <li><input type="checkbox" name="services" id="central_tanshifx_direct" value="central_tanshifx_direct"><label for="central_tanshifx_direct">セントラル短資FX（ダイレクト）</label>
  <li><input type="checkbox" name="services" id="central_tanshifx_hyper" value="central_tanshifx_hyper"><label for="central_tanshifx_hyper">セントラル短資FX（ハイパー）</label>
  <li><input type="checkbox" name="services" id="forland" value="forland"><label for="forland">フォーランドフォレックス</label>
  <li><input type="checkbox" name="services" id="min_fx" value="min_fx"><label for="min_fx">みんなのFX</label>
  <li><input type="checkbox" name="services" id="mj" value="mj"><label for="mj">MJ</label>
  <li><input type="checkbox" name="services" id="cyberagent_fx" value="cyberagent_fx"><label for="cyberagent_fx">サイバーエージェントFX</label>
  <li><input type="checkbox" name="services" id="gaitame_dotcom_next" value="gaitame_dotcom_next"><label for="gaitame_dotcom_next">外為どっとコム（外貨NEXT）</label>
  <li><input type="checkbox" name="services" id="gaitame_dotcom_stage" value="gaitame_dotcom_stage"><label for="gaitame_dotcom_stage">外為どっとコム（ステージ）</label>
  <li><input type="checkbox" name="services" id="ntt_smart_trade" value="ntt_smart_trade"><label for="ntt_smart_trade">NTTスマートトレード</label>
  <li><input type="checkbox" name="services" id="himawari_fx" value="himawari_fx"><label for="himawari_fx">ひまわりFX</label>
 </ul>
 <input type="submit" value="描画">
</form>"""

def extract_input():
    form     = cgi.FieldStorage()
    result   = {}
    results  = [ 'date_start', 'date_end', 'currency', 'services' ]
    for item in results:
        try:
            field = form[ item ]
            if ListType == type( field ):
                result[ item ] = [ f.value for f in field ]
            else:
                if 'services' == item:
                    result[ item ] = [ field.value ]
                else:
                    result[ item ] = field.value
        except:
            return None
    return result

def extract_swapbuy( input ):
    database = open_db_connection()
    data     = get_swapbuy(
        database,
        input[ 'date_start' ], input[ 'date_end' ],
        input[ 'currency' ], input[ 'services' ] )
    database.close()

    return data

def date_from_str( str ):
    match = DATE_FORMAT.match( str )
    if match:
        try:
            year  = int( match.group( 1 ) )
            month = int( match.group( 2 ) )
            day   = int( match.group( 3 ) )
            return date( year, month, day )
        except:
            return None
    return None

def color():
    from random import random
    HEX = {  0 : '0',  1 : '1',  2 : '2', 3 : '3',  4 : '4',  5 : '5',  6 : '6',
             7 : '7',  8 : '7',  8 : '8', 9 : '9', 10 : 'a', 11 : 'b', 12 : 'c',
            13 : 'd', 14 : 'e', 15 : 'f', }
    return ''.join( [ HEX[ int( random() * 16 ) ] for item in range( 6 ) ] )

def construct_graph( input, data ):
    date_start = date_from_str( input[ 'date_start' ] )
    date_end   = date_from_str( input[ 'date_end' ] )
    period     = ( date_end - date_start ).days
    axes       = []
    for service_name, swap_buys in data.iteritems():
        swap_buys = sorted( swap_buys.items() )
        x         = [ float( ( data_date - date_start ).days ) * 100 / period
                      for data_date, swap_buy in swap_buys ]
        y         = [ swap_buy
                      for data_date, swap_buy in swap_buys ]
        axes.append( x )
        axes.append( y )
    chart_axes = '|'.join(
        [ ','.join( [ str( value ) for value in axis ] )
          for axis in axes ] )

    tag = ''.join(
        [ '<img src="http://chart.apis.google.com/chart?',
          '&'.join(
                [ 'chs=600x400',
                  'cht=lxy',
                  ''.join( [ 'chd=t:',
                             chart_axes,
                             ] ),
                  ''.join( [ 'chdl=',
                             '|'.join( [ quote( service_name )
                                         for service_name in data.keys() ] ),
                             ] ),
                  ''.join( [ 'chco=',
                             ','.join( [ color()
                                         for service_name in data.keys() ] ),
                             ] ),
                  ] ),
          '">',
          ] )

    return tag

print 'Content-Type: text/html\n'

print FORM

input = extract_input()
if input:
    data  = extract_swapbuy( input )
    graph = construct_graph( input, data )
    print graph
