# -*- coding: utf-8; -*-

"""
retrieve images
"""

from soup             import soupfy
from urlparse         import urlparse, urlunparse
from zipfile          import ZipFile
from upload           import upload_file
from mail             import create_message, send_mail
from xml.sax.saxutils import unescape
import os
import traceback
import mechanize

URL    = 'http://www.mangakan.net/new.html'
ERRORS = []
WGET   = u' '.join(
    [ u'cd "%(title)s";',
      u'/usr/local/bin/wget',
      u'--quiet',
      u'--no-clobber',
      u''.join( [ u'--user-agent="Mozilla/4.0 ('
                  u'compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)"' ] ),
      u'--referer=%(referrer)s',
      u'%(directory)s/image/%(image_file)s' ] )

def utf8( unicode_string ):
    'return utf-8 string of unicode string'
    return unicode_string.encode( 'utf-8' )

def clean_title( title ):
    'remove unusable character from title'
    return unescape( title, { '\n' : '', ':' : '', '!' : '' } )

def get_new_books( url = URL ):
    """
    get { booktitle : url }
    """
    soup   = soupfy( url, encoding = 'shift_jis' )
    rows   = soup.findAll( 'tr', attrs = { 'align' : 'center' } )
    result = {}
    for i, row in enumerate( rows ):
        if 2 == i % 3:
            columns = row.findAll( 'td' )
            for column in columns:
                link  = column.find( 'a' )
                url   = link[ 'href' ]
                title = link.contents[ 0 ]
                try:
                    result[ clean_title( title ) ] = url
                except TypeError:
                    title = title.string
                    result[ clean_title( title ) ] = url
    return result

def get_book_image_files( url ):
    """
    get page filenames for the title
    """
    try:
        soup   = soupfy( url, encoding = 'shift_jis' )
        hrs    = soup.findAll( 'hr' )
        table  = hrs[ 1 ].next.next
        images = table.findAll( 'a' )
        files  = [ image[ 'href' ] for image in images ]
        return files
    except AttributeError:
        number = 1
        files  = []
        while True:
            page = soup.find( lambda tag : ( 'a' == tag.name and
                                             tag.string and
                                             '%dpage' % number == tag.string ) )
            if not page:
                break
            page    = page[ 'href' ]
            scheme, netloc, path, _, _, _ = urlparse( url )
            dirname = os.path.dirname( path )
            path    = '%s/%s' % ( dirname, page )
            url     = urlunparse( ( scheme, netloc, path, '', '', '' ) )
            files.extend( get_book_image_files( url ) )
            number += 1
        return files
    except:
        stacktrace = traceback.format_exc()
        ERRORS.append( stacktrace )
        return []

def get_book_images( title, url ):
    """
    download image files into local filesystem
    """
    image_files = get_book_image_files( url )
    try:
        os.mkdir( utf8( u'%s' % title ) )
    except OSError:
        pass
    except:
        stacktrace = traceback.format_exc()
        ERRORS.append( stacktrace )
    scheme, netloc, path, _, _, _ = urlparse( url )
    dirname = os.path.dirname( path )
    url     = urlunparse( ( scheme, netloc, dirname, '', '', '' ) )
    for image_file in image_files:
        command = WGET % dict(
            title      = title,
            referrer   = u'%s/%s' % ( url, image_file ),
            directory  = url,
            image_file = image_file.replace( u'html', u'jpg' ) )
        os.system( utf8( command ) )
    return image_files

def zip_book( zip_filename, title, image_files ):
    """
    zip directory and delete directory
    """
    zfile = ZipFile( zip_filename, 'w' )
    for image_file in image_files:
        zfile.write(
            utf8( u'%s/%s' % ( title,
                               image_file.replace( u'html', u'jpg' ) ) ) )
    zfile.close()
    if 0 == os.path.getsize( zip_filename ):
        raise OSError
    return_value = os.system( utf8( u'rm -rf "%s"' % title ) )
    if 0 != return_value:
        raise OSError

def upload_to_dropbox( title ):
    """
    upload zip file to dropbox
    """
    filename = utf8( u'%s.zip' % title )
    try:
        upload_file( filename, '998 temporary', filename,
                     'tamakoshihiroki@gmail.com', '|+17=lx3Il8zMz9]' )
    except mechanize.HTTPError:
        pass

def do_it( url = URL ):
    """
    get books specified by url
    """
    books = get_new_books( url )
    os.chdir( 'books' )
    for title, url in books.iteritems():
        try:
            zip_filename = utf8( u'%s.zip' % title )
            if ( os.path.isfile( zip_filename ) and
                 0 < os.path.getsize( zip_filename ) ):
                continue
            image_files = get_book_images( title, url )
            zip_book( zip_filename, title, image_files )
            upload_to_dropbox( title )
        except:
            stacktrace = traceback.format_exc()
            ERRORS.append( stacktrace )
    os.chdir( '..' )

def postprocess():
    """
    send error mail if any error exist
    """
    if ERRORS:
        address = 'tamakoshihiroki@gmail.com'
        body    = '\n\n'.join( ERRORS )
        msg     = create_message( body, address )
        send_mail( msg, address )

URLS = [
    # 'http://219.94.152.133/mangakan/fate.html',
    # 'http://219.94.152.133/mangakan/toheart.html',
    # 'http://219.94.152.133/mangakan/touhou.html',
    # 'http://219.94.152.133/mangakan/haruhi.html',
    # 'http://219.94.152.133/mangakan/i-mas.html',
    # 'http://219.94.152.133/mangakan/k-on.html',
    # 'http://219.94.152.133/mangakan/snk.html',
    'http://219.94.152.133/mangakan/nanoha.html',
    'http://219.94.152.133/mangakan/oreimo.html',
    'http://219.94.152.133/mangakan/loveplus.html',
    'http://219.94.152.133/mangakan/toaru.html',
    'http://219.94.152.133/mangakan/gundam.html',
    # 'http://219.94.152.133/mangakan/macrossf.html',
    # 'http://219.94.152.133/mangakan/madoka-magica.html',
    # 'http://219.94.152.133/mangakan/sr.html',
    # 'http://219.94.152.133/mangakan/dq.html',
    # 'http://219.94.152.133/mangakan/ff.html',
    # 'http://219.94.152.133/mangakan/zero.html',
    # 'http://219.94.152.133/mangakan/rozen.html',
    # 'http://219.94.152.133/mangakan/dream.html',
    # 'http://219.94.152.133/mangakan/jump.html',
    # 'http://219.94.152.133/mangakan/toloveru.html',
    # 'http://219.94.152.133/mangakan/ichigo.html',
    # 'http://219.94.152.133/mangakan/onepi.html',
    # 'http://219.94.152.133/mangakan/negima.html',
    # 'http://219.94.152.133/mangakan/codegeass.html',
    # 'http://219.94.152.133/mangakan/s-witch.html',
    # 'http://219.94.152.133/mangakan/saki.html',
    # 'http://219.94.152.133/mangakan/eva.html',
    # 'http://219.94.152.133/mangakan/amagami.html',
    # 'http://219.94.152.133/mangakan/working.hml',
    # 'http://219.94.152.133/mangakan/precure.html',
    # 'http://219.94.152.133/mangakan/kannagi.html',
    # 'http://219.94.152.133/mangakan/ragnarok.html',
    # 'http://219.94.152.133/mangakan/kanon.html',
    # 'http://219.94.152.133/mangakan/tsukihime.html',
    # 'http://219.94.152.133/mangakan/bakemonogatari.html',
    # 'http://219.94.152.133/mangakan/sekaiju.html',
    # 'http://219.94.152.133/mangakan/sispri.html',
    # 'http://219.94.152.133/mangakan/seiken.html',
    # 'http://219.94.152.133/mangakan/hayate.html',
    # 'http://219.94.152.133/mangakan/doa.html',
    # 'http://219.94.152.133/mangakan/vocaloid.html',
    # 'http://219.94.152.133/mangakan/koihime.html',
    # 'http://219.94.152.133/mangakan/bakatest.html',
    # 'http://219.94.152.133/mangakan/yotuba.html',
    # 'http://219.94.152.133/mangakan/is.html',
    # 'http://219.94.152.133/mangakan/valkyria.html',
    # 'http://219.94.152.133/mangakan/hotd.html',
    # 'http://219.94.152.133/mangakan/sonota_01.html',
    ]

def hand_upload( titles ):
    "hand upload"
    for title in titles:
        upload_to_dropbox( title )

if '__main__' == __name__:
    # for url in URLS:
    #     do_it( url )
    do_it()
    postprocess()
