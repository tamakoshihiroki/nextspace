# -*- coding: utf-8; -*-

"""
search engine keyword extractor
"""

from urllib   import unquote_plus
from urlparse import urlparse
import re

ENGINES = {
    'www.google.'             : 'q',
    'search.yahoo.'           : 'p',
    '.msn.'                   : 'q',
    '.aol.'                   : 'query',
    '.lycos.'                 : 'query',
    '.ask.'                   : 'q',
    '.altavista.'             : 'q',
    '.netscape.'              : 'query',
    '.earthlink.net'          : 'q',
    '.cnn.'                   : 'query',
    'looksmart'               : 'key',
    'about.'                  : 'terms',
    'www.excite.co.jp'        : 'search',
    '.excite.'                : 'qkw',
    '.mamma.com'              : 'query',
    '.alltheweb.com'          : 'q',
    '.gigablast.'             : 'q',
    '.alice.it'               : 'qs',
    'mixi.jp'                 : 'keyword',
    '.hatena.ne.jp'           : 'word',
    '.nifty.com'              : 'Text',
    'so-net.search.goo.ne.jp' : 'keyword',
    'search.goo.ne.jp'        : 'MT',
    '.biglobe.ne.jp'          : 'q',
    '.infoseek.co.jp'         : 'qt',
    '.fresheye.com'           : 'kw',
    '.livedoor.com'           : 'q',
    '.baidu.'                 : 'wd',
    '.marsflag.com'           : 'phrase',
    'ocnsearch.goo.ne.jp'     : 'MT',
    'hi-ho.search.goo.ne.jp'  : 'MT',
    'allabout.'               : 'qs',
    '.mooter.'                : 'keywords',
    '.nikkei.co.jp'           : 'q',
    '.asahi.com'              : 'Query_Key',
    'odn.excite.co.jp'        : 'search',
    'auone.jp'                : 'q',
    }
    
RM_OPS  = re.compile(
    r'(' +
    '|'.join( [ 'cache:', 'link:', 'related:', 'site:', 'daterange:', 'ip:',
                'domain:', 'info:', 'stocks:', 'filetype:', 'file:', 'host:',
                'type:' ] ) +
    ')\S*' )
CUT_OPS = re.compile( r'|'.join(
        [ 'intitle:', 'allintitle:', 'inurl:', 'allinurl:', 'inanchor:',
          'allinanchor:', 'anchor:', 'allintext:', 'title:', 'image:',
          'applet:', 'url:', 'define:', '\+', '---', '~' ] ) )
U_OPS   = re.compile( r'AND|OR' )
DSPACE  = re.compile( ' +' )
DQUEST  = re.compile( '\?+' )
URLENC  = re.compile( r'(%[0-9A-Fa-f]{2})+' )
UNICODE = re.compile( r'(%u[0-9A-Fa-f]{4})+' )

HEXADECIMAL = { '0' : 0,  '1' : 1,  '2' : 2,  '3' : 3,  '4' : 4,
                '5' : 5,  '6' : 6,  '7' : 7,  '8' : 8,  '9' : 9,
                'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15,
                'a' : 10, 'b' : 11, 'c' : 12, 'd' : 13, 'e' : 14, 'f' : 15,
                }

def decode_encoded_unicode( encoded ):
    """
    Returns unicode string
    Input: encoded: example: %u5916%u70BA%u30C9%u30C3%u30C8
    """
    try:
        return ''.join(
            [ unichr( HEXADECIMAL[ letter[ 2 ] ] * 4096 +
                      HEXADECIMAL[ letter[ 3 ] ] * 256 +
                      HEXADECIMAL[ letter[ 4 ] ] * 16 +
                      HEXADECIMAL[ letter[ 5 ] ] )
              for letter in re.split( '(%u[0-9A-Fa-f]{4})', encoded )
              if letter ] )
    except IndexError:
        return ''

def clean_keyword( keyword ):
    """
    Returns cleaned keyword
    Input:  keyword is url encoded
    Output: utf8 string
    """
    keyphrase = unquote_plus( keyword )
    for codec in [ 'utf-8', 'euc_jisx0213', 'euc-jp', 'shift-jis',
                   'cp932', 'shift_jisx0213' ]:
        try:
            keyphrase = keyphrase.decode( codec, 'strict' )
            keyphrase = keyphrase.replace( u'　', u' ' )
            keyphrase = RM_OPS.sub(  '', keyphrase )
            keyphrase = CUT_OPS.sub( '', keyphrase )
            keyphrase = U_OPS.sub(   '', keyphrase )
            keyphrase = DSPACE.sub( ' ', keyphrase )
            keyphrase = DQUEST.sub( '?', keyphrase )
            if keyphrase and '' == URLENC.sub( '', keyphrase ):
                keyphrase = clean_keyword( keyphrase ).decode( 'utf-8' )
            if keyphrase and '' == UNICODE.sub( '', keyphrase ):
                keyphrase = decode_encoded_unicode( keyphrase )
            keyphrase = keyphrase[ : 250 ]
            keyphrase = keyphrase.strip().strip( '?' ).strip()
            return keyphrase.encode( 'utf-8' )[ : 750 ]
        except UnicodeDecodeError:
            pass
        except UnicodeEncodeError:
            pass
    return ''

def extract_keyword( referrer ):
    'extract keyword as utf8 string from referrer'
    domains = '|'.join( [ domain.replace( '.', '\.' )
                          for domain in ENGINES.keys() ] )
    match_domains = re.findall( domains, referrer )
    if not match_domains:
        return ''
    domain = match_domains[ 0 ]
    _, _, _, _, query, _ = urlparse( referrer )
    query_dict = dict( [ pair.split( '=' )[ 0 : 2 ]
                         for pair in query.split( '&' )
                         if pair.count( '=' ) ] )
    try:
        keyword = query_dict[ ENGINES[ domain ] ]
        return clean_keyword( keyword )
    except KeyError:
        return ''
