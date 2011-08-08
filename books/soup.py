# -*- coding: utf-8; -*-

"""
soupfy library
"""

from urllib2       import build_opener
from BeautifulSoup import BeautifulSoup

USERAGENT = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)'

def get_opener():
    "custom URL opener"
    opener = build_opener()
    opener.addheaders = [ ( 'User-Agent', USERAGENT ) ]
    return opener

def read_url( url, removal = None ):
    "read contents from url"
    opener = get_opener()
    stream = opener.open( url )
    source = stream.read()
    stream.close()
    if removal:
        source = source.replace( removal, '' )
    return source

def soupfy( url, encoding = 'utf-8', removal = None ):
    "parse the HTML identified by url"
    source = read_url( url, removal )
    soup   = BeautifulSoup( source, fromEncoding = encoding )
    return soup
