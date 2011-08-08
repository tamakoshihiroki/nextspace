#!/usr/local/bin/python
# -*- coding: utf-8; -*-

RECOMMEND_FOOTER = """
 <div class="register">
  <a href="sample.cgi">&gt;&gt; 万葉集を毎日一首ずつメールで読むことができます。まずはサンプルをどうぞ</a>
 </div>"""

FOOTER_TEMPLATE = """
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

RESULT_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <link rel="SHORTCUT ICON" href="images/favicon.ico" />
    <link rel="stylesheet" href="styles/style.css" type="text/css" />
    <script type="text/javascript" src="javascript/common.js"></script>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["annotatedtimeline"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('date', 'Date');
        data.addColumn('number', 'ご登録いただいている方の数');
        data.addRows( [
        %(rows)s
        ] );
        
        var chart = new google.visualization.AnnotatedTimeLine(document.getElementById('chart'));
        chart.draw( data, { displayRangeSelector : false, displayZoomButtons : false } );
        var tds = document.getElementsByTagName( 'td' );
        for ( var i = 0 ; i < tds.length ; i++ ) {
          tds[ i ].style.border  = 'none';
          tds[ i ].style.padding = '0px';
        }
      }
    </script>
    <title>本日の万葉集 / 利用実績</title>
</head>

<body>
<div id="page">

 <div id="header">
   <a id="logo" name="logo" href="index.html">
     本日の<br />万葉集
   </a>

   <div id="menu">
     <ul>
       <li><a class="calibrate-selected" href="result.html">利用実績</a></li>
       <li><a class="calibrate" href="sample.cgi">サンプル</a></li>
       <li><a href="register.cgi">登録/設定変更<br />（無料）</a></li>
       <li><a class="calibrate" href="cancel.html">利用解除</a></li>
     </ul>
   </div>
 </div>

 <div id="content">

 <h1>利用実績</h1>

 <p>
  %(year)d年%(month)d月%(day)d日現在、%(number)d名の方にご利用いただいております。
 </p>

 <div id="chart" style="width: 700px; height: 350px; margin: auto;">
 </div>

 <div class="register">
   <a href="sample.cgi">&gt;&gt; サンプル</a>
 </div>

 </div>

"""

SAMPLE_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <link rel="SHORTCUT ICON" href="images/favicon.ico" />
    <link rel="stylesheet" href="styles/style.css" type="text/css" />
    <script type="text/javascript" src="javascript/common.js"></script>
    <title>本日の万葉集 / サンプル</title>
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
       <li><a class="calibrate-selected" href="sample.cgi">サンプル</a></li>
       <li><a href="register.cgi">登録/設定変更<br />（無料）</a></li>
       <li><a class="calibrate" href="cancel.html">利用解除</a></li>
     </ul>
   </div>
 </div>

 <div id="content">

 %(message)s

 <h1>サンプル</h1>

 <p class="vspace10">
 縦書きで整形、または横書きのメールをお送りします。
 </p>

 <table summary="sample" cellspacing="0">
   <thead>
     <tr>
       <td class="label">縦書き</td>
       <td class="label"></td>
       <td class="label">横書き</td>
     </tr>
   </thead>
   <tbody>
     <tr>
       <td><img alt="縦書きの例。熟田津に船乗りせむと月待てば潮もかなひぬ今は漕ぎ出でな" src="images/tategaki.png" width="188" height="188" /></td>
       <td></td>
       <td><img alt="横書きの例。熟田津に船乗りせむと月待てば潮もかなひぬ今は漕ぎ出でな" src="images/yokogaki.png" width="188" height="188" /></td>
     </tr>
   </tbody>
 </table>

 <h2>試しに利用する</h2>

 <p>
 ご入力いただいたメールアドレスに一首配信します。
 </p>

 <p class="vspace10">
 登録はせず、配信のみ行います。
 </p>

 <form method="post" action="sample.cgi">
   <table summary="trial" class="form" cellspacing="0">
     <tbody>
       <tr>
         <td class="label">メールアドレス</td>
         <td><input name="mail_address" type="text" value="%(mail_address)s" accesskey="m" size="30" tabindex="1" /><br />
             携帯電話のアドレスをおすすめします。<br />
携帯電話で拒否設定をされている方は、「tmkc.igo@gmail.com」からのメールは受信するよう設定をお願い致します。
         </td>
       </tr>
       <tr>
         <td class="label">文字の方向</td>
         <td><input type="radio" name="direction" value="vertical" accesskey="v" id="vertical" onclick="set_width( false );" onkeypress="set_width( false );" %(vertical)s tabindex="2" /><label for="vertical">縦書き</label>
             <span class="space30"></span>
             <input type="radio" name="direction" value="horizontal" accesskey="h" id="horizontal" onclick="set_width( true );" onkeypress="set_width( true );" %(horizontal)s tabindex="2" /><label for="horizontal">横書き</label>
         </td>
       </tr>
       <tr>
         <td class="label">横幅（縦書きのみ）</td>
         <td><select name="column" tabindex="3">
             <option value="6">６文字</option>
             <option value="7" selected="selected">７文字</option>
             <option value="8">８文字</option>
             <option value="9">９文字</option>
             <option value="10">１０文字</option>
             <option value="11">１１文字</option>
             <option value="12">１２文字</option>
             </select>
         </td>
       </tr>
       <tr>
         <td class="label">縦幅（縦書きのみ）</td>
         <td><select name="row" tabindex="4">
             <option value="9">９文字</option>
             <option value="10">１０文字</option>
             <option value="11" selected="selected">１１文字</option>
             <option value="12">１２文字</option>
             <option value="13">１３文字</option>
             <option value="14">１４文字</option>
             <option value="15">１５文字</option>
             </select>
         </td>
       </tr>
       <tr>
         <td class="label">配信する歌</td>
         <td><input type="radio" name="choice" value="random" accesskey="r" id="random" %(random)s tabindex="5" /><label for="random">ランダム</label><br />
             <input type="radio" name="choice" value="index" accesskey="i" id="index" tabindex="5" %(index)s/><label for="index">歌の番号</label>
             <input type="text" name="number" value="%(number)d" accesskey="n" size="5" tabindex="6" />(1 から 4565 まで)</td>
       </tr>
       <tr>
         <td><input name="submitted" type="hidden" value="submitted" /></td>
         <td><input type="submit" value="&nbsp;&nbsp;送信&nbsp;&nbsp;" accesskey="s" tabindex="7" class="button" /></td>
       </tr>
     </tbody>
   </table>
 </form>

 <div class="register">
 <a href="register.cgi">&gt;&gt; 登録/設定変更（無料）</a>
 </div>

 </div>

"""

REGISTER_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <link rel="SHORTCUT ICON" href="images/favicon.ico" />
    <link rel="stylesheet" href="styles/style.css" type="text/css" />
    <script type="text/javascript" src="javascript/common.js"></script>
    <title>本日の万葉集 / 登録/設定変更（無料）</title>
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
       <li><a class="selected" href="register.cgi">登録/設定変更<br />（無料）</a></li>
       <li><a class="calibrate" href="cancel.html">利用解除</a></li>
     </ul>
   </div>
 </div>

 <div id="content">

 %(message)s

 <h1>登録/設定変更（無料）</h1>

 <p>
 万葉集4,565首を最初から一首ずつ配信します。
 </p>

 <p>
 設定を変更した場合は、次の配信から反映されます。
 </p>

 <p>
 <a href="privacy.html">個人情報保護方針</a>にご同意の上、ご利用下さい。
 </p>

 <form method="post" action="register.cgi">
   <table summary="register" class="form" cellspacing="0">
     <tbody>
       <tr>
         <td class="label">メールアドレス</td>
         <td><input name="mail_address" type="text" value="%(mail_address)s" accesskey="m" size="30" tabindex="1" /><br />
             携帯電話のアドレスをおすすめします。<br />
携帯電話で拒否設定をされている方は、「tmkc.igo@gmail.com」からのメールは受信するよう設定をお願い致します。<br />
<br />
確認のため、再度ご入力ください。
<input name="mail_address2" type="text" value="" size="30" tabindex="2" />
         </td>
       </tr>
       <tr>
         <td class="label">文字の方向</td>
         <td><input type="radio" name="direction" value="vertical" accesskey="v" id="vertical" onclick="set_width( false );" onkeypress="set_width( false );" %(vertical)stabindex="3" /><label for="vertical">縦書き</label>
             <span class="space30"></span>
             <input type="radio" name="direction" value="horizontal" accesskey="h" id="horizontal" onclick="set_width( true );" onkeypress="set_width( true );" %(horizontal)s tabindex="4" /><label for="horizontal">横書き</label>
         </td>
       </tr>
       <tr>
         <td class="label">横幅（縦書きのみ）</td>
         <td><select name="column" tabindex="5">
             <option value="6">６文字</option>
             <option value="7" selected="selected">７文字</option>
             <option value="8">８文字</option>
             <option value="9">９文字</option>
             <option value="10">１０文字</option>
             <option value="11">１１文字</option>
             <option value="12">１２文字</option>
             </select>
         </td>
       </tr>
       <tr>
         <td class="label">縦幅（縦書きのみ）</td>
         <td><select name="row" tabindex="6">
             <option value="9">９文字</option>
             <option value="10">１０文字</option>
             <option value="11" selected="selected">１１文字</option>
             <option value="12">１２文字</option>
             <option value="13">１３文字</option>
             <option value="14">１４文字</option>
             <option value="15">１５文字</option>
             </select>
         </td>
       </tr>
       <tr>
         <td class="label">送る時期</td>
         <td><select name="day" tabindex="7">
             <option value="everyday">毎日</option>
             <option value="weekday">平日（月〜金）</option>
             <option value="holiday">土日</option>
             </select>

             <select name="hour" tabindex="8">
             <option value="0">０時</option>
             <option value="1">１時</option>
             <option value="2">２時</option>
             <option value="3">３時</option>
             <option value="4">４時</option>
             <option value="5">５時</option>
             <option value="6">６時</option>
             <option value="7">７時</option>
             <option value="8">８時</option>
             <option value="9">９時</option>
             <option value="10">１０時</option>
             <option value="11">１１時</option>
             <option value="12">１２時</option>
             <option value="13">１３時</option>
             <option value="14">１４時</option>
             <option value="15">１５時</option>
             <option value="16">１６時</option>
             <option value="17">１７時</option>
             <option value="18">１８時</option>
             <option value="19">１９時</option>
             <option value="20">２０時</option>
             <option value="21">２１時</option>
             <option value="22">２２時</option>
             <option value="23">２３時</option>
             </select>
         </td>
       </tr>
       <tr>
         <td class="label">利用規約</td>
         <td>保守、改善のため、一時的に利用できないときがあることを予めご了承下さい</td>
       </tr>
       <tr>
         <td><input name="submitted" type="hidden" value="submitted" /></td>
         <td><input type="submit" value="&nbsp;登録／設定変更（無料）&nbsp;" accesskey="s" tabindex="9" class="button" /></td>
       </tr>
     </tbody>
   </table>
 </form>

 </div>

"""

CANCEL_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <link rel="SHORTCUT ICON" href="images/favicon.ico" />
    <link rel="stylesheet" href="styles/style.css" type="text/css" />
    <title>本日の万葉集 / 利用解除完了</title>
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
       <li><a class="calibrate-selected" href="cancel.html">利用解除</a></li>
     </ul>
   </div>
 </div>

 <div id="content">

 %(message)s

 </div>

"""

CONTACT_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <link rel="SHORTCUT ICON" href="images/favicon.ico" />
    <link rel="stylesheet" href="styles/style.css" type="text/css" />
    <title>本日の万葉集 / お問い合わせ完了</title>
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

 %(message)s

 </div>

"""

SEARCH_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <link rel="SHORTCUT ICON" href="images/favicon.ico" />
    <link rel="stylesheet" href="styles/style.css" type="text/css" />
    <script type="text/javascript" src="javascript/common.js"></script>
    <title>本日の万葉集 / 万葉集検索</title>
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

 <h1>万葉集検索</h1>

 <div>
   <form action="search.cgi" method="post">
     <table summary="万葉集検索" class="search">
       <tr>
         <td>万葉集検索</td>
         <td><input type="text" name="keyword" value="%(keyword)s" accesskey="k" tabindex="1" /></td>
         <td><input name="submitted" type="hidden" value="submitted" />
             <input type="submit" value="&nbsp;&nbsp;検索&nbsp;&nbsp;" accesskey="s" tabindex="2" /></td>
       </tr>
       <tr>
         <td></td><td>（例） 山上憶良, 恋, 春, 額田王 など</td><td></td>
       </tr>
     </table>
   </form>
 </div>

 %(message)s

 %(table)s

 %(recommendation)s

 </div>
"""

SEARCHED_TABLE_TEMPLATE = """<table class="searched" cellspacing="0">
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

SEARCH2_TEMPLATE = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <link rel="SHORTCUT ICON" href="images/favicon.ico" />
    <link rel="stylesheet" href="styles/style.css" type="text/css" />
    <script type="text/javascript" src="javascript/common.js"></script>
    <title>本日の万葉集 / 万葉集検索</title>
</head>

<body>
<div id="page">

 <div id="header">
   <a id="logo" name="logo" href="index.html">
     本日の<br />万葉集
   </a>

   <div id="menu">
     <ul>
       <li><a class="calibrate" href="sample.cgi">サンプル</a></li>
       <li><a href="register.cgi">登録/設定変更<br />（無料）</a></li>
       <li><a class="calibrate" href="cancel.html">利用解除</a></li>
     </ul>
   </div>
 </div>

 <div id="content">

 <h1>万葉集検索</h1>

 <div>
   <form action="http://www.google.co.jp/search" method="get">
     <table summary="万葉集検索" class="search">
       <tr>
         <td>万葉集検索</td>
         <td>
	   <input type="text" name="q" value="%s" accesskey="k" tabindex="1" />
	   <input type="hidden" name="ie" value="utf-8" />
	   <input type="hidden" name="oe" value="utf-8" />
	   <input type="hidden" name="hl" value="ja" />
	   <input type="hidden" name="sitesearch" value="tmkc.pgq.jp" />
	 </td>
         <td><input name="submitted" type="hidden" value="submitted" />
             <input type="submit" value="&nbsp;&nbsp;検索&nbsp;&nbsp;" accesskey="s" tabindex="2" /></td>
       </tr>
       <tr>
         <td></td><td>（例） 山上憶良, 恋, 春, 額田王 など</td><td></td>
       </tr>
     </table>
   </form>
 </div>

"""

