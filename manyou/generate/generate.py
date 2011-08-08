# -*- coding: utf-8; -*-

"""
generate uta pages
"""

from xml.sax.saxutils import escape
import csv
import re

HEADER_PAGE = u"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <link rel="SHORTCUT ICON" href="images/favicon.ico" />
    <link rel="stylesheet" href="styles/style.css" type="text/css" />
    <title>本日の万葉集 / %(kundoku)s</title>
</head>

<body>
<div id="page">

 <div id="header">
   <a id="logo" name="logo" href="index.html">
     本日の<br />万葉集
   </a>

   <div id="menu">
     <ul>
       <li><a class="calibrate" href="result.html">利用実績</a></li>
       <li><a class="calibrate" href="sample.cgi">サンプル</a></li>
       <li><a href="register.cgi">登録/設定変更<br />（無料）</a></li>
       <li><a class="calibrate" href="cancel.html">利用解除</a></li>
     </ul>
   </div>
 </div>

 <div id="content">

 <h1>%(kundoku)s</h1>

"""

FOOTER_PAGE = u"""
 <div class="register">
  <p>毎日一首、万葉集をメールで読みませんか？無料です。</p>
  <a href="sample.cgi">&gt;&gt; サンプルを見る</a>
 </div>

 </div>

 <div id="submenu">
   <ul>
     <li><a href="faq.html">よくあるご質問</a></li>
     <li><a href="contact.html">お問合せ</a></li>
   </ul>
 </div>

 <div id="footer">
   <p>
   本日の万葉集 Copyright &copy; 2011
   </p>
   <div id="footer_link">
    <ul>
      <li><a href="search.cgi">万葉集検索</a></li>
      <li><a href="all.html">万葉集全首</a></li>
      <li><a href="about.html">運営</a></li>
      <li><a href="privacy.html">個人情報保護方針</a></li>
    </ul>
   </div>
 </div>

</div>

<!-- ClickTale Top part -->
<script type="text/javascript">
var WRInitTime=(new Date()).getTime();
</script>
<!-- ClickTale end of Top part -->

<!-- ClickTale Bottom part -->
<div id="ClickTale" style="display: none;"></div>
<script src="http://s.clicktale.net/WRa.js" type="text/javascript"></script>
<script type="text/javascript">
if(typeof ClickTale=='function') ClickTale(12997,1);
</script>
<!-- ClickTale end of Bottom part -->
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-968446-2");
pageTracker._initData();
pageTracker._trackPageview();
</script>
 
</body>
</html>"""

HEADER_CGI = u"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <link rel="SHORTCUT ICON" href="images/favicon.ico" />
    <link rel="stylesheet" href="styles/style.css" type="text/css" />
    <title>本日の万葉集 / 万葉集全首（第%(kan)s巻）</title>
</head>

<body>
<div id="page">

 <div id="header">
   <a id="logo" name="logo" href="index.html">
     本日の<br />万葉集
   </a>

   <div id="menu">
     <ul>
       <li><a class="calibrate" href="result.html">利用実績</a></li>
       <li><a class="calibrate" href="sample.cgi">サンプル</a></li>
       <li><a href="register.cgi">登録/設定変更<br />（無料）</a></li>
       <li><a class="calibrate" href="cancel.html">利用解除</a></li>
     </ul>
   </div>
 </div>

 <div id="content">

 <div>
   <form action="search.cgi" method="post">
     <table summary="万葉集検索" class="search">
       <tr>
         <td>万葉集検索</td>
         <td><input type="text" name="keyword" value="%(keyword)s" accesskey="k" tabindex="1" /></td>
         <td><input name="submitted" type="hidden" value="submitted" />
             <input type="submit" value="&nbsp;&nbsp;検索&nbsp;&nbsp;" accesskey="s" tabindex="2" /></td>
       </tr>
     </table>
   </form>
 </div>

 <h1>万葉集全首（第%(kan)s巻）</h1>

 %(utas)s
"""

FOOTER = u""" <div class="register">
 <a href="register.cgi">&gt;&gt; 登録/設定変更（無料）</a>
 </div>

 </div>

 <div id="submenu">
   <ul>
     <li><a href="faq.html">よくあるご質問</a></li>
     <li><a href="contact.html">お問合せ</a></li>
   </ul>
 </div>

 <div id="footer">
   <p>
   本日の万葉集 Copyright &copy; 2011
   </p>
 <div id="footer_link">
   <ul>
     <li><a href="search.cgi">万葉集検索</a></li>
     <li><a href="all.html">万葉集全首</a></li>
     <li><a href="about.html">運営</a></li>
     <li><a href="privacy.html">個人情報保護方針</a></li>
   </ul>
 </div>
 </div>
 
</div>

<!-- ClickTale Top part -->
<script type="text/javascript">
var WRInitTime=(new Date()).getTime();
</script>
<!-- ClickTale end of Top part -->

<!-- ClickTale Bottom part -->
<div id="ClickTale" style="display: none;"></div>
<script src="http://s.clicktale.net/WRa.js" type="text/javascript"></script>
<script type="text/javascript">
if(typeof ClickTale=='function') ClickTale(12997,1);
</script>
<!-- ClickTale end of Bottom part -->
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-968446-2");
pageTracker._initData();
pageTracker._trackPageview();
</script>
 
</body>
</html>"""

PYTHON = u"""#!/usr/local/bin/python
# -*- coding: utf-8; -*-

HEADER = \"\"\"%(header)s\"\"\"
FOOTER = \"\"\"%(footer)s\"\"\"

from keyword import extract_keyword
import os

def get_keyword():
    'extract keyword'
    referrer = os.getenv( 'HTTP_REFERER', '' )
    keyword  = extract_keyword( referrer )
    return keyword.replace( '"', '' )

def render_html( keyword ):
    'render html'
    return HEADER %% dict( keyword = keyword ) + FOOTER

def display_html( html ):
    'display html'
    print 'Content-Type: text/html\\n'
    print html

def do_it():
    'do it'
    html = render_html( get_keyword() )
    display_html( html )

if '__main__' == __name__:
    do_it()
"""

TABLE_TEMPLATE = u"""<table class="searched" cellspacing="0" summary="歌の詳細">
  <tbody>
    <tr>
      <td class="label">番号</td><td>%(number)s</td>
    </tr>
    <tr>
      <td class="label">題詞</td><td>%(subject)s</td>
    </tr>
    <tr>
      <td class="label">原文</td><td>%(original)s</td>
    </tr>
    <tr>
      <td class="label">訓読</td><td>%(kundoku)s</td>
    </tr>
    <tr>
      <td class="label">仮名</td><td>%(kana)s</td>
    </tr>
    <tr>
      <td class="label">左注</td><td>%(sachu)s</td>
    </tr>
    <tr>
      <td class="label">校異</td><td>%(koui)s</td>
    </tr>
    <tr>
      <td class="label">事項</td><td>%(jikou)s</td>
    </tr>
    <tr>
      <td class="label tdbottom">訓異</td><td class="tdbottom">%(kuni)s</td>
    </tr>
  </tbody>
</table>
"""

KAN = { 1 : u'一',
        2 : u'二',
        3 : u'三',
        4 : u'四',
        5 : u'五',
        6 : u'六',
        7 : u'七',
        8 : u'八',
        9 : u'九',
        10 : u'十',
        11 : u'十一',
        12 : u'十二',
        13 : u'十三',
        14 : u'十四',
        15 : u'十五',
        16 : u'十六',
        17 : u'十七',
        18 : u'十八',
        19 : u'十九',
        20 : u'二十',
        }

def generate_uta_page( index, number, subject, kundoku, row ):
    'generate html page per uta'
    html     = HEADER_PAGE % dict(
        kundoku  = escape( kundoku )
        ) + TABLE_TEMPLATE % dict(
        number   = index,
        subject  = escape( subject ),
        original = escape( row[ 2 ] ),
        kundoku  = escape( kundoku ),
        kana     = escape( row[ 4 ] ),
        sachu    = escape( row[ 5 ] ),
        koui     = escape( row[ 6 ] ),
        jikou    = escape( row[ 7 ] ),
        kuni     = row[ 8 ].replace( '<br>', '<br />' ),
        ) + FOOTER_PAGE
    html_file = open( number + '.html', 'w' )
    html_file.write( html.encode( 'utf-8' ) )
    html_file.close()

ONE_LINE = u"""<h2>%(subject)s</h2>
<p><a href="%(number)s.html">%(kundoku)s</a></p>
"""

def generate_one( number, subject, kundoku ):
    'generate one line per uta'
    return ONE_LINE % dict( number = number,
                            subject = escape( subject ),
                            kundoku = kundoku )

def generate_cgi( manyoushu, kan ):
    'generate cgi per kan'
    utas = []
    for row in manyoushu:
        index = re.sub( r'.*\[.*\]', '', row[ 0 ] )
        name  = re.sub( r'^[^\]]*?\[.*?\]', '', row[ 1 ] )
        uta   = re.sub( r'^[^\]]*?\[.*?\]', '', row[ 3 ] ).replace( u'  ', ' ' )
        if index[ : 2 ] == '%02d' % kan:
            number = index.split( '/' )[ 1 ]
            utas.append( generate_one( number, name, uta ) )
            generate_uta_page( index, number, name, uta, row )
    cgi = PYTHON % dict( header = HEADER_CGI % dict( kan = KAN[ kan ],
                                                     utas = ''.join( utas ),
                                                     keyword = '%(keyword)s',
                                                     ),
                         footer   = FOOTER )
    cgi_file = open( 'all%02d.cgi' % kan, 'w' )
    cgi_file.write( cgi.encode( 'utf-8' ) )
    cgi_file.close()

def read_manyoushu():
    'read manyoushu'
    reader = csv.reader( open( 'manyou_utf8.csv', 'r' ) )
    return [ [ column.decode( 'utf-8' ) for column in row ]
             for row in reader ]

def do_it():
    'do it'
    manyoushu = read_manyoushu()
    for index in range( 1, 21 ):
        generate_cgi( manyoushu, index )

if '__main__' == __name__:
    do_it()
