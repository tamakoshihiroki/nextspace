#!/usr/local/bin/python
# -*- coding: utf-8; -*-

HEADER = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="ja" xml:lang="ja">
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <meta http-equiv="Content-Style-Type" content="text/css" />
    <meta http-equiv="Content-Script-Type" content="text/javascript" />
    <link rel="SHORTCUT ICON" href="images/favicon.ico" />
    <link rel="stylesheet" href="styles/style.css" type="text/css" />
    <title>本日の万葉集 / 万葉集全首（第十五巻）</title>
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

 <h1>万葉集全首（第十五巻）</h1>

 <h2>遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌</h2>
<p><a href="3578.html">武庫の浦の入江の洲鳥羽ぐくもる君を離れて恋に死ぬべし</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3579.html">大船に妹乗るものにあらませば羽ぐくみ持ちて行かましものを</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3580.html">君が行く海辺の宿に霧立たば我が立ち嘆く息と知りませ</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3581.html">秋さらば相見むものを何しかも霧に立つべく嘆きしまさむ</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3582.html">大船を荒海に出だしいます君障むことなく早帰りませ</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3583.html">ま幸くて妹が斎はば沖つ波千重に立つとも障りあらめやも</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3584.html">別れなばうら悲しけむ我が衣下にを着ませ直に逢ふまでに</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3585.html">我妹子が下にも着よと贈りたる衣の紐を我れ解かめやも</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3586.html">我がゆゑに思ひな痩せそ秋風の吹かむその月逢はむものゆゑ</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3587.html">栲衾新羅へいます君が目を今日か明日かと斎ひて待たむ</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3588.html">はろはろに思ほゆるかもしかれども異しき心を我が思はなくに</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3589.html">夕さればひぐらし来鳴く生駒山越えてぞ我が来る妹が目を欲り</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3590.html">妹に逢はずあらばすべなみ岩根踏む生駒の山を越えてぞ我が来る</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3591.html">妹とありし時はあれども別れては衣手寒きものにぞありける</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3592.html">海原に浮寝せむ夜は沖つ風いたくな吹きそ妹もあらなくに</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3593.html">大伴の御津に船乗り漕ぎ出てはいづれの島に廬りせむ我れ</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3594.html">潮待つとありける船を知らずして悔しく妹を別れ来にけり</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3595.html">朝開き漕ぎ出て来れば武庫の浦の潮干の潟に鶴が声すも</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3596.html">我妹子が形見に見むを印南都麻白波高み外にかも見む</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3597.html">わたつみの沖つ白波立ち来らし海人娘子ども島隠る見ゆ</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3598.html">ぬばたまの夜は明けぬらし玉の浦にあさりする鶴鳴き渡るなり</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3599.html">月読の光りを清み神島の礒廻の浦ゆ船出す我れは</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3600.html">離れ礒に立てるむろの木うたがたも久しき時を過ぎにけるかも</a></p>
<h2>（遣新羅使人等悲別贈答及海路慟情陳思并當所誦之古歌）</h2>
<p><a href="3601.html">しましくもひとりありうるものにあれや島のむろの木離れてあるらむ</a></p>
<h2>當所誦詠古歌</h2>
<p><a href="3602.html">あをによし奈良の都にたなびける天の白雲見れど飽かぬかも</a></p>
<h2>（當所誦詠古歌）</h2>
<p><a href="3603.html">青楊の枝伐り下ろしゆ種蒔きゆゆしき君に恋ひわたるかも</a></p>
<h2>（當所誦詠古歌）</h2>
<p><a href="3604.html">妹が袖別れて久になりぬれど一日も妹を忘れて思へや</a></p>
<h2>（當所誦詠古歌）</h2>
<p><a href="3605.html">わたつみの海に出でたる飾磨川絶えむ日にこそ我が恋やまめ</a></p>
<h2>（當所誦詠古歌）</h2>
<p><a href="3606.html">玉藻刈る処女を過ぎて夏草の野島が崎に廬りす我れは</a></p>
<h2>（當所誦詠古歌）柿本朝臣人麻呂歌曰  又曰</h2>
<p><a href="3606S.html">敏馬を過ぎて 船近づきぬ</a></p>
<h2>（當所誦詠古歌）</h2>
<p><a href="3607.html">白栲の藤江の浦に漁りする海人とや見らむ旅行く我れを</a></p>
<h2>（當所誦詠古歌）柿本朝臣人麻呂歌曰  又曰</h2>
<p><a href="3607S.html">荒栲の 鱸釣る海人とか見らむ </a></p>
<h2>（當所誦詠古歌）</h2>
<p><a href="3608.html">天離る鄙の長道を恋ひ来れば明石の門より家のあたり見ゆ</a></p>
<h2>（當所誦詠古歌）柿本朝臣人麻呂歌曰</h2>
<p><a href="3608S.html">大和島見ゆ </a></p>
<h2>（當所誦詠古歌）</h2>
<p><a href="3609.html">武庫の海の庭よくあらし漁りする海人の釣舟波の上ゆ見ゆ</a></p>
<h2>（當所誦詠古歌）柿本朝臣人麻呂歌曰  又曰</h2>
<p><a href="3609S.html">笥飯の海の 刈り薦の乱れて出づ見ゆ海人の釣船 </a></p>
<h2>（當所誦詠古歌）</h2>
<p><a href="3610.html">安胡の浦に舟乗りすらむ娘子らが赤裳の裾に潮満つらむか</a></p>
<h2>（當所誦詠古歌）柿本朝臣人麻呂歌曰  又曰</h2>
<p><a href="3610S.html">嗚呼見の浦 玉裳の裾に </a></p>
<h2>七夕歌一首</h2>
<p><a href="3611.html">大船に真楫しじ貫き海原を漕ぎ出て渡る月人壮士</a></p>
<h2>備後國水調郡長井浦舶泊之夜作歌三首</h2>
<p><a href="3612.html">あをによし奈良の都に行く人もがも草枕旅行く船の泊り告げむに [旋頭歌也]</a></p>
<h2>（備後國水調郡長井浦舶泊之夜作歌三首）</h2>
<p><a href="3613.html">海原を八十島隠り来ぬれども奈良の都は忘れかねつも</a></p>
<h2>（備後國水調郡長井浦舶泊之夜作歌三首）</h2>
<p><a href="3614.html">帰るさに妹に見せむにわたつみの沖つ白玉拾ひて行かな</a></p>
<h2>風速浦舶泊之夜作歌二首</h2>
<p><a href="3615.html">我がゆゑに妹嘆くらし風早の浦の沖辺に霧たなびけり</a></p>
<h2>（風速浦舶泊之夜作歌二首）</h2>
<p><a href="3616.html">沖つ風いたく吹きせば我妹子が嘆きの霧に飽かましものを</a></p>
<h2>安藝國長門嶋舶泊礒邊作歌五首</h2>
<p><a href="3617.html">石走る瀧もとどろに鳴く蝉の声をし聞けば都し思ほゆ</a></p>
<h2>（安藝國長門嶋舶泊礒邊作歌五首）</h2>
<p><a href="3618.html">山川の清き川瀬に遊べども奈良の都は忘れかねつも</a></p>
<h2>（安藝國長門嶋舶泊礒邊作歌五首）</h2>
<p><a href="3619.html">礒の間ゆたぎつ山川絶えずあらばまたも相見む秋かたまけて</a></p>
<h2>（安藝國長門嶋舶泊礒邊作歌五首）</h2>
<p><a href="3620.html">恋繁み慰めかねてひぐらしの鳴く島蔭に廬りするかも</a></p>
<h2>（安藝國長門嶋舶泊礒邊作歌五首）</h2>
<p><a href="3621.html">我が命を長門の島の小松原幾代を経てか神さびわたる</a></p>
<h2>従長門浦舶&lt;出&gt;之夜仰觀月光作歌三首</h2>
<p><a href="3622.html">月読みの光りを清み夕なぎに水手の声呼び浦廻漕ぐかも</a></p>
<h2>（従長門浦舶&lt;出&gt;之夜仰觀月光作歌三首）</h2>
<p><a href="3623.html">山の端に月傾けば漁りする海人の燈火沖になづさふ</a></p>
<h2>（従長門浦舶&lt;出&gt;之夜仰觀月光作歌三首）</h2>
<p><a href="3624.html">我れのみや夜船は漕ぐと思へれば沖辺の方に楫の音すなり</a></p>
<h2>古挽歌一首[并短歌]</h2>
<p><a href="3625.html">夕されば 葦辺に騒き 明け来れば 沖になづさふ 鴨すらも 妻とたぐひて 我が尾には 霜な降りそと 白栲の 羽さし交へて うち掃ひ さ寝とふものを 行く水の 帰らぬごとく 吹く風の 見えぬがごとく 跡もなき 世の人にして 別れにし 妹が着せてし なれ衣 袖片敷きて ひとりかも寝む </a></p>
<h2>（古挽歌一首[并短歌]）反歌一首</h2>
<p><a href="3626.html">鶴が鳴き葦辺をさして飛び渡るあなたづたづしひとりさ寝れば</a></p>
<h2>属物發思歌一首[并短歌]</h2>
<p><a href="3627.html">朝されば 妹が手にまく 鏡なす 御津の浜びに 大船に 真楫しじ貫き 韓国に 渡り行かむと 直向ふ 敏馬をさして 潮待ちて 水脈引き行けば 沖辺には 白波高み 浦廻より 漕ぎて渡れば 我妹子に 淡路の島は 夕されば 雲居隠りぬ さ夜更けて ゆくへを知らに 我が心 明石の浦に 船泊めて 浮寝をしつつ わたつみの 沖辺を見れば 漁りする 海人の娘子は 小舟乗り つららに浮けり 暁の 潮満ち来れば 葦辺には 鶴鳴き渡る 朝なぎに 船出をせむと 船人も 水手も声呼び にほ鳥の なづさひ行けば 家島は 雲居に見えぬ 我が思へる 心なぐやと 早く来て 見むと思ひて 大船を 漕ぎ我が行けば 沖つ波 高く立ち来ぬ 外のみに 見つつ過ぎ行き 玉の浦に 船を留めて 浜びより 浦礒を見つつ 泣く子なす 音のみし泣かゆ わたつみの 手巻の玉を 家づとに 妹に遣らむと 拾ひ取り 袖には入れて 帰し遣る 使なければ 持てれども 験をなみと また置きつるかも </a></p>
<h2>（属物發思歌一首[并短歌]）反歌二首</h2>
<p><a href="3628.html">玉の浦の沖つ白玉拾へれどまたぞ置きつる見る人をなみ</a></p>
<h2>（（属物發思歌一首[并短歌]）反歌二首）</h2>
<p><a href="3629.html">秋さらば我が船泊てむ忘れ貝寄せ来て置けれ沖つ白波</a></p>
<h2>周防國玖河郡麻里布浦行之時作歌八首</h2>
<p><a href="3630.html">真楫貫き船し行かずは見れど飽かぬ麻里布の浦に宿りせましを</a></p>
<h2>（周防國玖河郡麻里布浦行之時作歌八首）</h2>
<p><a href="3631.html">いつしかも見むと思ひし粟島を外にや恋ひむ行くよしをなみ</a></p>
<h2>（周防國玖河郡麻里布浦行之時作歌八首）</h2>
<p><a href="3632.html">大船にかし振り立てて浜清き麻里布の浦に宿りかせまし</a></p>
<h2>（周防國玖河郡麻里布浦行之時作歌八首）</h2>
<p><a href="3633.html">粟島の逢はじと思ふ妹にあれや安寐も寝ずて我が恋ひわたる</a></p>
<h2>（周防國玖河郡麻里布浦行之時作歌八首）</h2>
<p><a href="3634.html">筑紫道の可太の大島しましくも見ねば恋しき妹を置きて来ぬ</a></p>
<h2>（周防國玖河郡麻里布浦行之時作歌八首）</h2>
<p><a href="3635.html">妹が家路近くありせば見れど飽かぬ麻里布の浦を見せましものを</a></p>
<h2>（周防國玖河郡麻里布浦行之時作歌八首）</h2>
<p><a href="3636.html">家人は帰り早来と伊波比島斎ひ待つらむ旅行く我れを</a></p>
<h2>（周防國玖河郡麻里布浦行之時作歌八首）</h2>
<p><a href="3637.html">草枕旅行く人を伊波比島幾代経るまで斎ひ来にけむ</a></p>
<h2>過大嶋鳴門而經再宿之後追作歌二首</h2>
<p><a href="3638.html">これやこの名に負ふ鳴門のうづ潮に玉藻刈るとふ海人娘子ども</a></p>
<h2>（過大嶋鳴門而經再宿之後追作歌二首）</h2>
<p><a href="3639.html">波の上に浮き寝せし宵あど思へか心悲しく夢に見えつる</a></p>
<h2>熊毛浦舶泊之夜作歌四首</h2>
<p><a href="3640.html">都辺に行かむ船もが刈り薦の乱れて思ふ言告げやらむ</a></p>
<h2>（熊毛浦舶泊之夜作歌四首）</h2>
<p><a href="3641.html">暁の家恋しきに浦廻より楫の音するは海人娘子かも</a></p>
<h2>（熊毛浦舶泊之夜作歌四首）</h2>
<p><a href="3642.html">沖辺より潮満ち来らし可良の浦にあさりする鶴鳴きて騒きぬ</a></p>
<h2>（熊毛浦舶泊之夜作歌四首）</h2>
<p><a href="3643.html">沖辺より船人上る呼び寄せていざ告げ遣らむ旅の宿りを</a></p>
<h2>（熊毛浦舶泊之夜作歌四首）一云</h2>
<p><a href="3643S.html">旅の宿りをいざ告げ遣らな </a></p>
<h2>佐婆海中忽遭逆風漲浪漂流經宿而後幸得順風到著豊前國下毛郡分間浦  於是追怛艱難悽惆作八首</h2>
<p><a href="3644.html">大君の命畏み大船の行きのまにまに宿りするかも</a></p>
<h2>（佐婆海中忽遭逆風漲浪漂流經宿而後幸得順風到著豊前國下毛郡分間浦  於是追怛艱難悽惆作八首）</h2>
<p><a href="3645.html">我妹子は早も来ぬかと待つらむを沖にや住まむ家つかずして</a></p>
<h2>（佐婆海中忽遭逆風漲浪漂流經宿而後幸得順風到著豊前國下毛郡分間浦  於是追怛艱難悽惆作八首）</h2>
<p><a href="3646.html">浦廻より漕ぎ来し船を風早み沖つみ浦に宿りするかも</a></p>
<h2>（佐婆海中忽遭逆風漲浪漂流經宿而後幸得順風到著豊前國下毛郡分間浦  於是追怛艱難悽惆作八首）</h2>
<p><a href="3647.html">我妹子がいかに思へかぬばたまの一夜もおちず夢にし見ゆる</a></p>
<h2>（佐婆海中忽遭逆風漲浪漂流經宿而後幸得順風到著豊前國下毛郡分間浦  於是追怛艱難悽惆作八首）</h2>
<p><a href="3648.html">海原の沖辺に灯し漁る火は明かして灯せ大和島見む</a></p>
<h2>（佐婆海中忽遭逆風漲浪漂流經宿而後幸得順風到著豊前國下毛郡分間浦  於是追怛艱難悽惆作八首）</h2>
<p><a href="3649.html">鴨じもの浮寝をすれば蜷の腸か黒き髪に露ぞ置きにける</a></p>
<h2>（佐婆海中忽遭逆風漲浪漂流經宿而後幸得順風到著豊前國下毛郡分間浦  於是追怛艱難悽惆作八首）</h2>
<p><a href="3650.html">ひさかたの天照る月は見つれども我が思ふ妹に逢はぬころかも</a></p>
<h2>（佐婆海中忽遭逆風漲浪漂流經宿而後幸得順風到著豊前國下毛郡分間浦  於是追怛艱難悽惆作八首）</h2>
<p><a href="3651.html">ぬばたまの夜渡る月は早も出でぬかも海原の八十島の上ゆ妹があたり見む [旋頭歌也]</a></p>
<h2>至筑紫舘遥望本郷悽愴作歌四首</h2>
<p><a href="3652.html">志賀の海人の一日もおちず焼く塩のからき恋をも我れはするかも</a></p>
<h2>（至筑紫舘遥望本郷悽愴作歌四首）</h2>
<p><a href="3653.html">志賀の浦に漁りする海人家人の待ち恋ふらむに明かし釣る魚</a></p>
<h2>（至筑紫舘遥望本郷悽愴作歌四首）</h2>
<p><a href="3654.html">可之布江に鶴鳴き渡る志賀の浦に沖つ白波立ちし来らしも</a></p>
<h2>（至筑紫舘遥望本郷悽愴作歌四首）一云</h2>
<p><a href="3654S.html">満ちし来ぬらし </a></p>
<h2>（至筑紫舘遥望本郷悽愴作歌四首）</h2>
<p><a href="3655.html">今よりは秋づきぬらしあしひきの山松蔭にひぐらし鳴きぬ</a></p>
<h2>七夕仰觀天漢各陳所思作歌三首</h2>
<p><a href="3656.html">秋萩ににほへる我が裳濡れぬとも君が御船の綱し取りてば</a></p>
<h2>（七夕仰觀天漢各陳所思作歌三首）</h2>
<p><a href="3657.html">年にありて一夜妹に逢ふ彦星も我れにまさりて思ふらめやも</a></p>
<h2>（七夕仰觀天漢各陳所思作歌三首）</h2>
<p><a href="3658.html">夕月夜影立ち寄り合ひ天の川漕ぐ船人を見るが羨しさ</a></p>
<h2>海邊望月作九首</h2>
<p><a href="3659.html">秋風は日に異に吹きぬ我妹子はいつとか我れを斎ひ待つらむ</a></p>
<h2>（海邊望月作九首）</h2>
<p><a href="3660.html">神さぶる荒津の崎に寄する波間なくや妹に恋ひわたりなむ</a></p>
<h2>（海邊望月作九首）</h2>
<p><a href="3661.html">風の共寄せ来る波に漁りする海人娘子らが裳の裾濡れぬ</a></p>
<h2>（海邊望月作九首）一云</h2>
<p><a href="3661S.html">海人の娘子が裳の裾濡れぬ </a></p>
<h2>（海邊望月作九首）</h2>
<p><a href="3662.html">天の原振り放け見れば夜ぞ更けにけるよしゑやしひとり寝る夜は明けば明けぬとも</a></p>
<h2>（海邊望月作九首）</h2>
<p><a href="3663.html">わたつみの沖つ縄海苔来る時と妹が待つらむ月は経につつ</a></p>
<h2>（海邊望月作九首）</h2>
<p><a href="3664.html">志賀の浦に漁りする海人明け来れば浦廻漕ぐらし楫の音聞こゆ</a></p>
<h2>（海邊望月作九首）</h2>
<p><a href="3665.html">妹を思ひ寐の寝らえぬに暁の朝霧隠り雁がねぞ鳴く</a></p>
<h2>（海邊望月作九首）</h2>
<p><a href="3666.html">夕されば秋風寒し我妹子が解き洗ひ衣行きて早着む</a></p>
<h2>（海邊望月作九首）</h2>
<p><a href="3667.html">我が旅は久しくあらしこの我が着る妹が衣の垢つく見れば</a></p>
<h2>到筑前國志麻郡之韓亭舶泊經三日於時夜月之光皎々流照奄對此&lt;華&gt;旅情悽噎各陳心緒聊以裁歌六首</h2>
<p><a href="3668.html">大君の遠の朝廷と思へれど日長くしあれば恋ひにけるかも</a></p>
<h2>（到筑前國志麻郡之韓亭舶泊經三日於時夜月之光皎々流照奄對此&lt;華&gt;旅情悽噎各陳心緒聊以裁歌六首）</h2>
<p><a href="3669.html">旅にあれど夜は火灯し居る我れを闇にや妹が恋ひつつあるらむ</a></p>
<h2>（到筑前國志麻郡之韓亭舶泊經三日於時夜月之光皎々流照奄對此&lt;華&gt;旅情悽噎各陳心緒聊以裁歌六首）</h2>
<p><a href="3670.html">韓亭能許の浦波立たぬ日はあれども家に恋ひぬ日はなし</a></p>
<h2>（到筑前國志麻郡之韓亭舶泊經三日於時夜月之光皎々流照奄對此&lt;華&gt;旅情悽噎各陳心緒聊以裁歌六首）</h2>
<p><a href="3671.html">ぬばたまの夜渡る月にあらませば家なる妹に逢ひて来ましを</a></p>
<h2>（到筑前國志麻郡之韓亭舶泊經三日於時夜月之光皎々流照奄對此&lt;華&gt;旅情悽噎各陳心緒聊以裁歌六首）</h2>
<p><a href="3672.html">ひさかたの月は照りたり暇なく海人の漁りは灯し合へり見ゆ</a></p>
<h2>（到筑前國志麻郡之韓亭舶泊經三日於時夜月之光皎々流照奄對此&lt;華&gt;旅情悽噎各陳心緒聊以裁歌六首）</h2>
<p><a href="3673.html">風吹けば沖つ白波畏みと能許の亭にあまた夜ぞ寝る</a></p>
<h2>引津亭舶泊之作歌七首</h2>
<p><a href="3674.html">草枕旅を苦しみ恋ひ居れば可也の山辺にさを鹿鳴くも</a></p>
<h2>（引津亭舶泊之作歌七首）</h2>
<p><a href="3675.html">沖つ波高く立つ日にあへりきと都の人は聞きてけむかも</a></p>
<h2>（引津亭舶泊之作歌七首）</h2>
<p><a href="3676.html">天飛ぶや雁を使に得てしかも奈良の都に言告げ遣らむ</a></p>
<h2>（引津亭舶泊之作歌七首）</h2>
<p><a href="3677.html">秋の野をにほはす萩は咲けれども見る験なし旅にしあれば</a></p>
<h2>（引津亭舶泊之作歌七首）</h2>
<p><a href="3678.html">妹を思ひ寐の寝らえぬに秋の野にさを鹿鳴きつ妻思ひかねて</a></p>
<h2>（引津亭舶泊之作歌七首）</h2>
<p><a href="3679.html">大船に真楫しじ貫き時待つと我れは思へど月ぞ経にける</a></p>
<h2>（引津亭舶泊之作歌七首）</h2>
<p><a href="3680.html">夜を長み寐の寝らえぬにあしひきの山彦響めさを鹿鳴くも</a></p>
<h2>肥前國松浦郡狛嶋亭舶泊之夜遥望海浪各慟旅心作歌七首</h2>
<p><a href="3681.html">帰り来て見むと思ひし我が宿の秋萩すすき散りにけむかも</a></p>
<h2>（肥前國松浦郡狛嶋亭舶泊之夜遥望海浪各慟旅心作歌七首）</h2>
<p><a href="3682.html">天地の神を祈ひつつ我れ待たむ早来ませ君待たば苦しも</a></p>
<h2>（肥前國松浦郡狛嶋亭舶泊之夜遥望海浪各慟旅心作歌七首）</h2>
<p><a href="3683.html">君を思ひ我が恋ひまくはあらたまの立つ月ごとに避くる日もあらじ</a></p>
<h2>（肥前國松浦郡狛嶋亭舶泊之夜遥望海浪各慟旅心作歌七首）</h2>
<p><a href="3684.html">秋の夜を長みにかあらむなぞここば寐の寝らえぬもひとり寝ればか</a></p>
<h2>（肥前國松浦郡狛嶋亭舶泊之夜遥望海浪各慟旅心作歌七首）</h2>
<p><a href="3685.html">足日女御船泊てけむ松浦の海妹が待つべき月は経につつ</a></p>
<h2>（肥前國松浦郡狛嶋亭舶泊之夜遥望海浪各慟旅心作歌七首）</h2>
<p><a href="3686.html">旅なれば思ひ絶えてもありつれど家にある妹し思ひ悲しも</a></p>
<h2>（肥前國松浦郡狛嶋亭舶泊之夜遥望海浪各慟旅心作歌七首）</h2>
<p><a href="3687.html">あしひきの山飛び越ゆる鴈がねは都に行かば妹に逢ひて来ね</a></p>
<h2>到壹岐嶋雪連宅満忽遇鬼病死去之時作歌一首[并短歌]</h2>
<p><a href="3688.html">天皇の 遠の朝廷と 韓国に 渡る我が背は 家人の 斎ひ待たねか 正身かも 過ちしけむ 秋去らば 帰りまさむと たらちねの 母に申して 時も過ぎ 月も経ぬれば 今日か来む 明日かも来むと 家人は 待ち恋ふらむに 遠の国 いまだも着かず 大和をも 遠く離りて 岩が根の 荒き島根に 宿りする君 </a></p>
<h2>（到壹岐嶋雪連宅満忽遇鬼病死去之時作歌一首[并短歌]）反歌二首</h2>
<p><a href="3689.html">岩田野に宿りする君家人のいづらと我れを問はばいかに言はむ</a></p>
<h2>（（到壹岐嶋雪連宅満忽遇鬼病死去之時作歌一首[并短歌]）反歌二首）</h2>
<p><a href="3690.html">世間は常かくのみと別れぬる君にやもとな我が恋ひ行かむ</a></p>
<h2></h2>
<p><a href="3691.html">天地と ともにもがもと 思ひつつ ありけむものを はしけやし 家を離れて 波の上ゆ なづさひ来にて あらたまの 月日も来経ぬ 雁がねも 継ぎて来鳴けば たらちねの 母も妻らも 朝露に 裳の裾ひづち 夕霧に 衣手濡れて 幸くしも あるらむごとく 出で見つつ 待つらむものを 世間の 人の嘆きは 相思はぬ 君にあれやも 秋萩の 散らへる野辺の 初尾花 仮廬に葺きて 雲離れ 遠き国辺の 露霜の 寒き山辺に 宿りせるらむ </a></p>
<h2>反歌二首</h2>
<p><a href="3692.html">はしけやし妻も子どもも高々に待つらむ君や島隠れぬる</a></p>
<h2>（反歌二首）</h2>
<p><a href="3693.html">黄葉の散りなむ山に宿りぬる君を待つらむ人し悲しも</a></p>
<h2></h2>
<p><a href="3694.html">わたつみの 畏き道を 安けくも なく悩み来て 今だにも 喪なく行かむと 壱岐の海人の ほつての占部を 肩焼きて 行かむとするに 夢のごと 道の空路に 別れする君 </a></p>
<h2>反歌二首</h2>
<p><a href="3695.html">昔より言ひけることの韓国のからくもここに別れするかも</a></p>
<h2>（反歌二首）</h2>
<p><a href="3696.html">新羅へか家にか帰る壱岐の島行かむたどきも思ひかねつも</a></p>
<h2>到對馬嶋淺茅浦舶泊之時不得順風經停五箇日於是瞻望物華各陳慟心作歌三首</h2>
<p><a href="3697.html">百船の泊つる対馬の浅茅山しぐれの雨にもみたひにけり</a></p>
<h2>（到對馬嶋淺茅浦舶泊之時不得順風經停五箇日於是瞻望物華各陳慟心作歌三首）</h2>
<p><a href="3698.html">天離る鄙にも月は照れれども妹ぞ遠くは別れ来にける</a></p>
<h2>（到對馬嶋淺茅浦舶泊之時不得順風經停五箇日於是瞻望物華各陳慟心作歌三首）</h2>
<p><a href="3699.html">秋去れば置く露霜にあへずして都の山は色づきぬらむ</a></p>
<h2>竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首</h2>
<p><a href="3700.html">あしひきの山下光る黄葉の散りの乱ひは今日にもあるかも</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3701.html">竹敷の黄葉を見れば我妹子が待たむと言ひし時ぞ来にける</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3702.html">竹敷の浦廻の黄葉我れ行きて帰り来るまで散りこすなゆめ</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3703.html">竹敷の宇敝可多山は紅の八しほの色になりにけるかも</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3704.html">黄葉の散らふ山辺ゆ漕ぐ船のにほひにめでて出でて来にけり</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3705.html">竹敷の玉藻靡かし漕ぎ出なむ君がみ船をいつとか待たむ</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3706.html">玉敷ける清き渚を潮満てば飽かず我れ行く帰るさに見む</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3707.html">秋山の黄葉をかざし我が居れば浦潮満ち来いまだ飽かなくに</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3708.html">物思ふと人には見えじ下紐の下ゆ恋ふるに月ぞ経にける</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3709.html">家づとに貝を拾ふと沖辺より寄せ来る波に衣手濡れぬ</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3710.html">潮干なばまたも我れ来むいざ行かむ沖つ潮騒高く立ち来ぬ</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3711.html">我が袖は手本通りて濡れぬとも恋忘れ貝取らずは行かじ</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3712.html">ぬばたまの妹が干すべくあらなくに我が衣手を濡れていかにせむ</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3713.html">黄葉は今はうつろふ我妹子が待たむと言ひし時の経ゆけば</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3714.html">秋されば恋しみ妹を夢にだに久しく見むを明けにけるかも</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3715.html">ひとりのみ着寝る衣の紐解かば誰れかも結はむ家遠くして</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3716.html">天雲のたゆたひ来れば九月の黄葉の山もうつろひにけり</a></p>
<h2>（竹敷浦舶泊之時&lt;各&gt;陳心緒作歌十八首）</h2>
<p><a href="3717.html">旅にても喪なく早来と我妹子が結びし紐はなれにけるかも</a></p>
<h2>廻来筑紫海路入京到播磨國家嶋之時作歌五首</h2>
<p><a href="3718.html">家島は名にこそありけれ海原を我が恋ひ来つる妹もあらなくに</a></p>
<h2>（廻来筑紫海路入京到播磨國家嶋之時作歌五首）</h2>
<p><a href="3719.html">草枕旅に久しくあらめやと妹に言ひしを年の経ぬらく</a></p>
<h2>（廻来筑紫海路入京到播磨國家嶋之時作歌五首）</h2>
<p><a href="3720.html">我妹子を行きて早見む淡路島雲居に見えぬ家つくらしも</a></p>
<h2>（廻来筑紫海路入京到播磨國家嶋之時作歌五首）</h2>
<p><a href="3721.html">ぬばたまの夜明かしも船は漕ぎ行かな御津の浜松待ち恋ひぬらむ</a></p>
<h2>（廻来筑紫海路入京到播磨國家嶋之時作歌五首）</h2>
<p><a href="3722.html">大伴の御津の泊りに船泊てて龍田の山をいつか越え行かむ</a></p>
<h2>中臣朝臣宅守与狭野弟上娘子贈答歌</h2>
<p><a href="3723.html">あしひきの山道越えむとする君を心に持ちて安けくもなし</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3724.html">君が行く道の長手を繰り畳ね焼き滅ぼさむ天の火もがも</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3725.html">我が背子しけだし罷らば白栲の袖を振らさね見つつ偲はむ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3726.html">このころは恋ひつつもあらむ玉櫛笥明けてをちよりすべなかるべし</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3727.html">塵泥の数にもあらぬ我れゆゑに思ひわぶらむ妹がかなしさ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3728.html">あをによし奈良の大道は行きよけどこの山道は行き悪しかりけり</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3729.html">愛しと我が思ふ妹を思ひつつ行けばかもとな行き悪しかるらむ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3730.html">畏みと告らずありしをみ越道の手向けに立ちて妹が名告りつ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3731.html">思ふゑに逢ふものならばしましくも妹が目離れて我れ居らめやも</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3732.html">あかねさす昼は物思ひぬばたまの夜はすがらに音のみし泣かゆ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3733.html">我妹子が形見の衣なかりせば何物もてか命継がまし</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3734.html">遠き山関も越え来ぬ今さらに逢ふべきよしのなきが寂しさ [一云 さびしさ] </a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3735.html">思はずもまことあり得むやさ寝る夜の夢にも妹が見えざらなくに</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3736.html">遠くあれば一日一夜も思はずてあるらむものと思ほしめすな</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3737.html">人よりは妹ぞも悪しき恋もなくあらましものを思はしめつつ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3738.html">思ひつつ寝ればかもとなぬばたまの一夜もおちず夢にし見ゆる</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3739.html">かくばかり恋ひむとかねて知らませば妹をば見ずぞあるべくありける</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3740.html">天地の神なきものにあらばこそ我が思ふ妹に逢はず死にせめ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3741.html">命をし全くしあらばあり衣のありて後にも逢はざらめやも [一云 ありての後も] </a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3742.html">逢はむ日をその日と知らず常闇にいづれの日まで我れ恋ひ居らむ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3743.html">旅といへば言にぞやすきすくなくも妹に恋ひつつすべなけなくに</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3744.html">我妹子に恋ふるに我れはたまきはる短き命も惜しけくもなし</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3745.html">命あらば逢ふこともあらむ我がゆゑにはだな思ひそ命だに経ば</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3746.html">人の植うる田は植ゑまさず今さらに国別れして我れはいかにせむ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3747.html">我が宿の松の葉見つつ我れ待たむ早帰りませ恋ひ死なぬとに</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3748.html">他国は住み悪しとぞ言ふ速けく早帰りませ恋ひ死なぬとに</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3749.html">他国に君をいませていつまでか我が恋ひ居らむ時の知らなく</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3750.html">天地の底ひのうらに我がごとく君に恋ふらむ人はさねあらじ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3751.html">白栲の我が下衣失はず持てれ我が背子直に逢ふまでに</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3752.html">春の日のうら悲しきに後れ居て君に恋ひつつうつしけめやも</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3753.html">逢はむ日の形見にせよとたわや女の思ひ乱れて縫へる衣ぞ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3754.html">過所なしに関飛び越ゆる霍公鳥多我子尓毛止まず通はむ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3755.html">愛しと我が思ふ妹を山川を中にへなりて安けくもなし</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3756.html">向ひ居て一日もおちず見しかども厭はぬ妹を月わたるまで</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3757.html">我が身こそ関山越えてここにあらめ心は妹に寄りにしものを</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3758.html">さす竹の大宮人は今もかも人なぶりのみ好みたるらむ [一云 今さへや] </a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3759.html">たちかへり泣けども我れは験なみ思ひわぶれて寝る夜しぞ多き</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3760.html">さ寝る夜は多くあれども物思はず安く寝る夜はさねなきものを</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3761.html">世の中の常のことわりかくさまになり来にけらしすゑし種から</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3762.html">我妹子に逢坂山を越えて来て泣きつつ居れど逢ふよしもなし</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3763.html">旅と言へば言にぞやすきすべもなく苦しき旅も言にまさめやも</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3764.html">山川を中にへなりて遠くとも心を近く思ほせ我妹</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3765.html">まそ鏡懸けて偲へとまつり出す形見のものを人に示すな</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3766.html">愛しと思ひし思はば下紐に結ひつけ持ちてやまず偲はせ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3767.html">魂は朝夕にたまふれど我が胸痛し恋の繁きに</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3768.html">このころは君を思ふとすべもなき恋のみしつつ音のみしぞ泣く</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3769.html">ぬばたまの夜見し君を明くる朝逢はずまにして今ぞ悔しき</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3770.html">味真野に宿れる君が帰り来む時の迎へをいつとか待たむ</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3771.html">宮人の安寐も寝ずて今日今日と待つらむものを見えぬ君かも</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3772.html">帰りける人来れりと言ひしかばほとほと死にき君かと思ひて</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3773.html">君が共行かましものを同じこと後れて居れどよきこともなし</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3774.html">我が背子が帰り来まさむ時のため命残さむ忘れたまふな</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3775.html">あらたまの年の緒長く逢はざれど異しき心を我が思はなくに</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3776.html">今日もかも都なりせば見まく欲り西の御馬屋の外に立てらまし</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3777.html">昨日今日君に逢はずてするすべのたどきを知らに音のみしぞ泣く</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3778.html">白栲の我が衣手を取り持ちて斎へ我が背子直に逢ふまでに</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3779.html">我が宿の花橘はいたづらに散りか過ぐらむ見る人なしに</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3780.html">恋ひ死なば恋ひも死ねとや霍公鳥物思ふ時に来鳴き響むる</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3781.html">旅にして物思ふ時に霍公鳥もとなな鳴きそ我が恋まさる</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3782.html">雨隠り物思ふ時に霍公鳥我が住む里に来鳴き響もす</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3783.html">旅にして妹に恋ふれば霍公鳥我が住む里にこよ鳴き渡る</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3784.html">心なき鳥にぞありける霍公鳥物思ふ時に鳴くべきものか</a></p>
<h2>（中臣朝臣宅守与狭野弟上娘子贈答歌）</h2>
<p><a href="3785.html">霍公鳥間しまし置け汝が鳴けば我が思ふ心いたもすべなし</a></p>

"""
FOOTER = """ <div class="register">
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

from keyword import extract_keyword
import os

def get_keyword():
    'extract keyword'
    referrer = os.getenv( 'HTTP_REFERER', '' )
    keyword  = extract_keyword( referrer )
    return keyword.replace( '"', '' )

def render_html( keyword ):
    'render html'
    return HEADER % dict( keyword = keyword ) + FOOTER

def display_html( html ):
    'display html'
    print 'Content-Type: text/html\n'
    print html

def do_it():
    'do it'
    html = render_html( get_keyword() )
    display_html( html )

if '__main__' == __name__:
    do_it()
