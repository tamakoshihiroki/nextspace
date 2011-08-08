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
    <title>本日の万葉集 / 万葉集全首（第二巻）</title>
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

 <h1>万葉集全首（第二巻）</h1>

 <h2>相聞 / 難波高津宮御宇天皇代  [大鷦鷯天皇  謚曰仁徳天皇] / 磐姫皇后思天皇御作歌四首</h2>
<p><a href="0085.html">君が行き日長くなりぬ山尋ね迎へか行かむ待ちにか待たむ</a></p>
<h2>（相聞 / 難波高津宮御宇天皇代  [大鷦鷯天皇  謚曰仁徳天皇] / 磐姫皇后思天皇御作歌四首）</h2>
<p><a href="0086.html">かくばかり恋ひつつあらずは高山の磐根しまきて死なましものを</a></p>
<h2>（相聞 / 難波高津宮御宇天皇代  [大鷦鷯天皇  謚曰仁徳天皇] / 磐姫皇后思天皇御作歌四首）</h2>
<p><a href="0087.html">ありつつも君をば待たむうち靡く我が黒髪に霜の置くまでに</a></p>
<h2>（相聞 / 難波高津宮御宇天皇代  [大鷦鷯天皇  謚曰仁徳天皇] / 磐姫皇后思天皇御作歌四首）</h2>
<p><a href="0088.html">秋の田の穂の上に霧らふ朝霞いつへの方に我が恋やまむ</a></p>
<h2>（相聞 / 難波高津宮御宇天皇代  [大鷦鷯天皇  謚曰仁徳天皇] / 磐姫皇后思天皇御作歌四首）或本歌曰</h2>
<p><a href="0089.html">居明かして君をば待たむぬばたまの我が黒髪に霜は降るとも</a></p>
<h2>古事記曰  軽太子奸軽太郎女  故其太子流於伊豫湯也  此時衣通王  不堪戀&lt;慕&gt;而追徃時歌曰</h2>
<p><a href="0090.html">君が行き日長くなりぬ山たづの迎へを行かむ待つには待たじ</a></p>
<h2>近江大津宮御宇天皇代  [天命開別天皇  謚曰天智天皇] / 天皇賜鏡王女御歌一首</h2>
<p><a href="0091.html">妹が家も継ぎて見ましを大和なる大島の嶺に家もあらましを [一云 妹があたり継ぎても見むに] [一云 家居らましを]</a></p>
<h2>鏡王女奉和御歌一首</h2>
<p><a href="0092.html">秋山の木の下隠り行く水の我れこそ益さめ御思ひよりは</a></p>
<h2>内大臣藤原卿娉鏡王女時鏡王女贈内大臣歌一首</h2>
<p><a href="0093.html">玉櫛笥覆ふを安み明けていなば君が名はあれど吾が名し惜しも</a></p>
<h2>内大臣藤原卿報贈鏡王女歌一首</h2>
<p><a href="0094.html">玉櫛笥みむろの山のさな葛さ寝ずはつひに有りかつましじ [玉くしげ三室戸山の]</a></p>
<h2>内大臣藤原卿娶釆女安見&lt;兒&gt;時作歌一首</h2>
<p><a href="0095.html">我れはもや安見児得たり皆人の得かてにすとふ安見児得たり</a></p>
<h2>久米禅師娉石川郎女時歌五首</h2>
<p><a href="0096.html">み薦刈る信濃の真弓我が引かば貴人さびていなと言はむかも [禅師]</a></p>
<h2>（久米禅師娉石川郎女時歌五首）</h2>
<p><a href="0097.html">み薦刈る信濃の真弓引かずして強ひさるわざを知ると言はなくに [郎女]</a></p>
<h2>（久米禅師娉石川郎女時歌五首）</h2>
<p><a href="0098.html">梓弓引かばまにまに寄らめども後の心を知りかてぬかも [郎女]</a></p>
<h2>（久米禅師娉石川郎女時歌五首）</h2>
<p><a href="0099.html">梓弓弦緒取りはけ引く人は後の心を知る人ぞ引く [禅師]</a></p>
<h2>（久米禅師娉石川郎女時歌五首）</h2>
<p><a href="0100.html">東人の荷前の箱の荷の緒にも妹は心に乗りにけるかも [禅師]</a></p>
<h2>大伴宿祢娉巨勢郎女時歌一首  [大伴宿祢諱曰安麻呂也難波朝右大臣大紫大伴長徳卿之第六子平城朝任大納言兼大将軍薨也]</h2>
<p><a href="0101.html">玉葛実ならぬ木にはちはやぶる神ぞつくといふならぬ木ごとに</a></p>
<h2>巨勢郎女報贈歌一首  [即近江朝大納言巨勢人卿之女也]</h2>
<p><a href="0102.html">玉葛花のみ咲きてならずあるは誰が恋にあらめ我れ恋ひ思ふを</a></p>
<h2>明日香清御原宮御宇天皇代  [天渟&lt;中&gt;原瀛真人天皇謚曰天武天皇] / 天皇賜藤原夫人御歌一首</h2>
<p><a href="0103.html">我が里に大雪降れり大原の古りにし里に降らまくは後</a></p>
<h2>藤原夫人奉和歌一首</h2>
<p><a href="0104.html">我が岡のおかみに言ひて降らしめし雪のくだけしそこに散りけむ</a></p>
<h2>藤原宮御宇天皇&lt;代&gt;  [天皇謚曰持統天皇元年丁亥十一年譲位軽太子尊号曰太上天皇也] / 大津皇子竊下於伊勢神宮上来時大伯皇女御作歌二首</h2>
<p><a href="0105.html">我が背子を大和へ遣るとさ夜更けて暁露に我れ立ち濡れし</a></p>
<h2>（大津皇子竊下於伊勢神宮上来時大伯皇女御作歌二首）</h2>
<p><a href="0106.html">ふたり行けど行き過ぎかたき秋山をいかにか君がひとり越ゆらむ</a></p>
<h2>大津皇子贈石川郎女御歌一首</h2>
<p><a href="0107.html">あしひきの山のしづくに妹待つと我れ立ち濡れぬ山のしづくに</a></p>
<h2>石川郎女奉和歌一首</h2>
<p><a href="0108.html">我を待つと君が濡れけむあしひきの山のしづくにならましものを</a></p>
<h2>大津皇子竊婚石川女郎時津守連通占露其事皇子御作歌一首  &lt;[未詳]&gt;</h2>
<p><a href="0109.html">大船の津守が占に告らむとはまさしに知りて我がふたり寝し</a></p>
<h2>日並皇子尊贈賜石川女郎御歌一首  [女郎字曰大名兒也]</h2>
<p><a href="0110.html">大名児を彼方野辺に刈る草の束の間も我れ忘れめや</a></p>
<h2>幸于吉野宮時弓削皇子贈与額田王歌一首</h2>
<p><a href="0111.html">いにしへに恋ふる鳥かも弓絃葉の御井の上より鳴き渡り行く</a></p>
<h2>額田王奉和歌一首  [従倭京進入]</h2>
<p><a href="0112.html">いにしへに恋ふらむ鳥は霍公鳥けだしや鳴きし我が念へるごと</a></p>
<h2>従吉野折取蘿生松柯遣時額田王奉入歌一首</h2>
<p><a href="0113.html">み吉野の玉松が枝ははしきかも君が御言を持ちて通はく</a></p>
<h2>但馬皇女在高市皇子宮時思穂積皇子御作歌一首</h2>
<p><a href="0114.html">秋の田の穂向きの寄れる片寄りに君に寄りなな言痛くありとも</a></p>
<h2>勅穂積皇子遣近江志賀山寺時但馬皇女御作歌一首</h2>
<p><a href="0115.html">後れ居て恋ひつつあらずは追ひ及かむ道の隈廻に標結へ我が背</a></p>
<h2>但馬皇女在高市皇子宮時竊接穂積皇子事既形而御作&lt;歌&gt;一首</h2>
<p><a href="0116.html">人言を繁み言痛みおのが世にいまだ渡らぬ朝川渡る</a></p>
<h2>舎人皇子御歌一首</h2>
<p><a href="0117.html">ますらをや片恋せむと嘆けども醜のますらをなほ恋ひにけり</a></p>
<h2>舎人娘子奉和歌一首</h2>
<p><a href="0118.html">嘆きつつますらをのこの恋ふれこそ我が髪結ひの漬ちてぬれけれ</a></p>
<h2>弓削皇子思紀皇女御歌四首</h2>
<p><a href="0119.html">吉野川行く瀬の早みしましくも淀むことなくありこせぬかも</a></p>
<h2>（弓削皇子思紀皇女御歌四首）</h2>
<p><a href="0120.html">我妹子に恋ひつつあらずは秋萩の咲きて散りぬる花にあらましを</a></p>
<h2>（弓削皇子思紀皇女御歌四首）</h2>
<p><a href="0121.html">夕さらば潮満ち来なむ住吉の浅香の浦に玉藻刈りてな</a></p>
<h2>（弓削皇子思紀皇女御歌四首）</h2>
<p><a href="0122.html">大船の泊つる泊りのたゆたひに物思ひ痩せぬ人の子故に</a></p>
<h2>三方沙弥娶園臣生羽之女未經幾時臥病作歌三首</h2>
<p><a href="0123.html">たけばぬれたかねば長き妹が髪このころ見ぬに掻き入れつらむか [三方沙弥]</a></p>
<h2>（三方沙弥娶園臣生羽之女未經幾時臥病作歌三首）</h2>
<p><a href="0124.html">人皆は今は長しとたけと言へど君が見し髪乱れたりとも [娘子]</a></p>
<h2>（三方沙弥娶園臣生羽之女未經幾時臥病作歌三首）</h2>
<p><a href="0125.html">橘の蔭踏む道の八衢に物をぞ思ふ妹に逢はずして [三方沙弥]</a></p>
<h2>石川女郎贈大伴宿祢田主歌一首  [即佐保大納言大伴卿&lt;之&gt;第二子  母曰巨勢朝臣也]</h2>
<p><a href="0126.html">風流士と我れは聞けるをやど貸さず我れを帰せりおその風流士</a></p>
<h2>大伴宿祢田主報贈&lt;歌&gt;一首</h2>
<p><a href="0127.html">風流士に我れはありけりやど貸さず帰しし我れぞ風流士にはある</a></p>
<h2>同石川女郎更贈大伴田主中郎歌一首</h2>
<p><a href="0128.html">我が聞きし耳によく似る葦の末の足ひく我が背つとめ給ぶべし</a></p>
<h2>大&lt;津&gt;皇子宮侍石川女郎贈大伴宿祢宿奈麻呂歌一首  [女郎字曰山田郎女也宿奈麻呂宿祢者大納言兼大将軍卿之第三子也]</h2>
<p><a href="0129.html">古りにし嫗にしてやかくばかり恋に沈まむ手童のごと [恋をだに忍びかねてむ手童のごと]</a></p>
<h2>長皇子与皇弟御歌一首</h2>
<p><a href="0130.html">丹生の川瀬は渡らずてゆくゆくと恋痛し我が背いで通ひ来ね</a></p>
<h2>柿本朝臣人麻呂従石見國別妻上来時歌二首[并短歌]</h2>
<p><a href="0131.html">石見の海 角の浦廻を 浦なしと 人こそ見らめ 潟なしと [一云 礒なしと] 人こそ見らめ よしゑやし 浦はなくとも よしゑやし 潟は [一云 礒は] なくとも 鯨魚取り 海辺を指して 柔田津の 荒礒の上に か青なる 玉藻沖つ藻 朝羽振る 風こそ寄せめ 夕羽振る 波こそ来寄れ 波のむた か寄りかく寄り 玉藻なす 寄り寝し妹を [一云 はしきよし 妹が手本を] 露霜の 置きてし来れば この道の 八十隈ごとに 万たび かへり見すれど いや遠に 里は離りぬ いや高に 山も越え来ぬ 夏草の 思ひ萎へて 偲ふらむ 妹が門見む 靡けこの山</a></p>
<h2>（柿本朝臣人麻呂従石見國別妻上来時歌二首[并短歌]）反歌二首</h2>
<p><a href="0132.html">石見のや高角山の木の間より我が振る袖を妹見つらむか</a></p>
<h2>（（柿本朝臣人麻呂従石見國別妻上来時歌二首[并短歌]）反歌二首）</h2>
<p><a href="0133.html">笹の葉はみ山もさやにさやげども我れは妹思ふ別れ来ぬれば</a></p>
<h2>（柿本朝臣人麻呂従石見國別妻上来時歌二首[并短歌]）或本反歌曰</h2>
<p><a href="0134.html">石見なる高角山の木の間ゆも我が袖振るを妹見けむかも</a></p>
<h2>（柿本朝臣人麻呂従石見國別妻上来時歌二首[并短歌]）</h2>
<p><a href="0135.html">つのさはふ 石見の海の 言さへく 唐の崎なる 海石にぞ 深海松生ふる 荒礒にぞ 玉藻は生ふる 玉藻なす 靡き寝し子を 深海松の 深めて思へど さ寝し夜は 幾だもあらず 延ふ蔦の 別れし来れば 肝向ふ 心を痛み 思ひつつ かへり見すれど 大船の 渡の山の 黄葉の 散りの乱ひに 妹が袖 さやにも見えず 妻ごもる 屋上の [一云 室上山] 山の 雲間より 渡らふ月の 惜しけども 隠らひ来れば 天伝ふ 入日さしぬれ 大夫と 思へる我れも 敷栲の 衣の袖は 通りて濡れぬ</a></p>
<h2>（柿本朝臣人麻呂従石見國別妻上来時歌二首[并短歌]）反歌二首</h2>
<p><a href="0136.html">青駒が足掻きを速み雲居にぞ妹があたりを過ぎて来にける [一云 あたりは隠り来にける]</a></p>
<h2>（（柿本朝臣人麻呂従石見國別妻上来時歌二首[并短歌]）反歌二首）</h2>
<p><a href="0137.html">秋山に落つる黄葉しましくはな散り乱ひそ妹があたり見む [一云 散りな乱ひそ]</a></p>
<h2>（柿本朝臣人麻呂従石見國別妻上来時歌二首[并短歌]）或本歌一首[并短歌]</h2>
<p><a href="0138.html">石見の海 津の浦をなみ 浦なしと 人こそ見らめ 潟なしと 人こそ見らめ よしゑやし 浦はなくとも よしゑやし 潟はなくとも 鯨魚取り 海辺を指して 柔田津の 荒礒の上に か青なる 玉藻沖つ藻 明け来れば 波こそ来寄れ 夕されば 風こそ来寄れ 波のむた か寄りかく寄り 玉藻なす 靡き我が寝し 敷栲の 妹が手本を 露霜の 置きてし来れば この道の 八十隈ごとに 万たび かへり見すれど いや遠に 里離り来ぬ いや高に 山も越え来ぬ はしきやし 我が妻の子が 夏草の 思ひ萎えて 嘆くらむ 角の里見む 靡けこの山</a></p>
<h2>（（柿本朝臣人麻呂従石見國別妻上来時歌二首[并短歌]）或本歌一首[并短歌]）反歌一首</h2>
<p><a href="0139.html">石見の海打歌の山の木の間より我が振る袖を妹見つらむか</a></p>
<h2>柿本朝臣人麻呂妻依羅娘子与人麻呂相別歌一首</h2>
<p><a href="0140.html">な思ひと君は言へども逢はむ時いつと知りてか我が恋ひずあらむ</a></p>
<h2>挽歌 / 後岡本宮御宇天皇代  [天豊財重日足姫天皇譲位後即後岡本宮] / 有間皇子自傷結松枝歌二首</h2>
<p><a href="0141.html">磐白の浜松が枝を引き結びま幸くあらばまた帰り見む</a></p>
<h2>（有間皇子自傷結松枝歌二首）</h2>
<p><a href="0142.html">家にあれば笥に盛る飯を草枕旅にしあれば椎の葉に盛る</a></p>
<h2>長忌寸意吉麻呂見結松哀咽歌二首</h2>
<p><a href="0143.html">磐代の岸の松が枝結びけむ人は帰りてまた見けむかも</a></p>
<h2>（長忌寸意吉麻呂見結松哀咽歌二首）</h2>
<p><a href="0144.html">磐代の野中に立てる結び松心も解けずいにしへ思ほゆ[未詳]</a></p>
<h2>山上臣憶良追和歌一首</h2>
<p><a href="0145.html">鳥翔成あり通ひつつ見らめども人こそ知らね松は知るらむ</a></p>
<h2>大寶元年辛丑幸于紀伊國時&lt;見&gt;結松歌一首  [柿本朝臣人麻呂歌集中出也]</h2>
<p><a href="0146.html">後見むと君が結べる磐代の小松がうれをまたも見むかも</a></p>
<h2>近江大津宮御宇天皇代  [天命開別天皇謚曰天智天皇] / 天皇聖躬不豫之時太后奉御歌一首</h2>
<p><a href="0147.html">天の原振り放け見れば大君の御寿は長く天足らしたり</a></p>
<h2>一書曰近江天皇聖躰不豫御病急時&lt;太&gt;后奉獻御歌一首</h2>
<p><a href="0148.html">青旗の木幡の上を通ふとは目には見れども直に逢はぬかも</a></p>
<h2>天皇崩後之時倭太后御作歌一首</h2>
<p><a href="0149.html">人はよし思ひやむとも玉葛影に見えつつ忘らえぬかも</a></p>
<h2>天皇崩時婦人作歌一首  [姓氏未詳]</h2>
<p><a href="0150.html">うつせみし 神に堪へねば 離れ居て 朝嘆く君 放り居て 我が恋ふる君 玉ならば 手に巻き持ちて 衣ならば 脱く時もなく 我が恋ふる 君ぞ昨夜の夜 夢に見えつる</a></p>
<h2>天皇大殯之時歌二首</h2>
<p><a href="0151.html">かからむとかねて知りせば大御船泊てし泊りに標結はましを [額田王]</a></p>
<h2>（天皇大殯之時歌二首）</h2>
<p><a href="0152.html">やすみしし我ご大君の大御船待ちか恋ふらむ志賀の唐崎 [舎人吉年]</a></p>
<h2>&lt;太&gt;后御歌一首</h2>
<p><a href="0153.html">鯨魚取り 近江の海を 沖放けて 漕ぎ来る船 辺付きて 漕ぎ来る船 沖つ櫂 いたくな撥ねそ 辺つ櫂 いたくな撥ねそ 若草の 夫の 思ふ鳥立つ</a></p>
<h2>石川夫人歌一首</h2>
<p><a href="0154.html">楽浪の大山守は誰がためか山に標結ふ君もあらなくに</a></p>
<h2>従山科御陵退散之時額田王作歌一首</h2>
<p><a href="0155.html">やすみしし 我ご大君の 畏きや 御陵仕ふる 山科の 鏡の山に 夜はも 夜のことごと 昼はも 日のことごと 哭のみを 泣きつつありてや ももしきの 大宮人は 行き別れなむ</a></p>
<h2>明日香清御原宮御宇天皇代  [天渟中原瀛真人天皇謚曰天武天皇] / 十市皇女薨時高市皇子尊御作歌三首</h2>
<p><a href="0156.html">みもろの神の神杉已具耳矣自得見監乍共寝ねぬ夜ぞ多き</a></p>
<h2>（十市皇女薨時高市皇子尊御作歌三首）</h2>
<p><a href="0157.html">三輪山の山辺真麻木綿短か木綿かくのみからに長くと思ひき</a></p>
<h2>（十市皇女薨時高市皇子尊御作歌三首）</h2>
<p><a href="0158.html">山吹の立ちよそひたる山清水汲みに行かめど道の知らなく</a></p>
<h2>天皇崩之時大后御作歌一首</h2>
<p><a href="0159.html">やすみしし 我が大君の 夕されば 見したまふらし 明け来れば 問ひたまふらし 神岳の 山の黄葉を 今日もかも 問ひたまはまし 明日もかも 見したまはまし その山を 振り放け見つつ 夕されば あやに悲しみ 明け来れば うらさび暮らし 荒栲の 衣の袖は 干る時もなし</a></p>
<h2>一書曰天皇崩之時太上天皇御製歌二首</h2>
<p><a href="0160.html">燃ゆる火も取りて包みて袋には入ると言はずやも智男雲</a></p>
<h2>（一書曰天皇崩之時太上天皇御製歌二首）</h2>
<p><a href="0161.html">北山にたなびく雲の青雲の星離り行き月を離れて</a></p>
<h2>天皇崩之後八年九月九日奉為御齋會之夜夢裏習賜御歌一首  [古歌集中出]</h2>
<p><a href="0162.html">明日香の 清御原の宮に 天の下 知らしめしし やすみしし 我が大君 高照らす 日の御子 いかさまに 思ほしめせか 神風の 伊勢の国は 沖つ藻も 靡みたる波に 潮気のみ 香れる国に 味凝り あやにともしき 高照らす 日の御子</a></p>
<h2>藤原宮御宇天皇代  [高天原廣野姫天皇&lt;天皇元年丁亥十一年譲位軽太子尊号曰太上天皇&gt;] / 大津皇子薨之後大来皇女従伊勢齋宮上京之時御作歌二首</h2>
<p><a href="0163.html">神風の伊勢の国にもあらましを何しか来けむ君もあらなくに</a></p>
<h2>（大津皇子薨之後大来皇女従伊勢齋宮上京之時御作歌二首）</h2>
<p><a href="0164.html">見まく欲り我がする君もあらなくに何しか来けむ馬疲るるに</a></p>
<h2>移葬大津皇子屍於葛城二上山之時大来皇女哀傷御作歌二首</h2>
<p><a href="0165.html">うつそみの人にある我れや明日よりは二上山を弟背と我が見む</a></p>
<h2>（移葬大津皇子屍於葛城二上山之時大来皇女哀傷御作歌二首）</h2>
<p><a href="0166.html">磯の上に生ふる馬酔木を手折らめど見すべき君が在りと言はなくに</a></p>
<h2>日並皇子尊殯宮之時柿本朝臣人麻呂作歌一首[并短歌]</h2>
<p><a href="0167.html">天地の 初めの時 ひさかたの 天の河原に 八百万 千万神の 神集ひ 集ひいまして 神分り 分りし時に 天照らす 日女の命 [一云 さしのぼる 日女の命] 天をば 知らしめすと 葦原の 瑞穂の国を 天地の 寄り合ひの極み 知らしめす 神の命と 天雲の 八重かき別きて [一云 天雲の八重雲別きて] 神下し いませまつりし 高照らす 日の御子は 飛ぶ鳥の 清御原の宮に 神ながら 太敷きまして すめろきの 敷きます国と 天の原 岩戸を開き 神上り 上りいましぬ [一云 神登り いましにしかば] 我が大君 皇子の命の 天の下 知らしめしせば 春花の 貴くあらむと 望月の 満しけむと 天の下 食す国 四方の人の 大船の 思ひ頼みて 天つ水 仰ぎて待つに いかさまに 思ほしめせか つれもなき 真弓の岡に 宮柱 太敷きいまし みあらかを 高知りまして 朝言に 御言問はさぬ 日月の 数多くなりぬれ そこ故に 皇子の宮人 ゆくへ知らずも [一云 さす竹の 皇子の宮人 ゆくへ知らにす]</a></p>
<h2>（日並皇子尊殯宮之時柿本朝臣人麻呂作歌一首[并短歌]）反歌二首</h2>
<p><a href="0168.html">ひさかたの天見るごとく仰ぎ見し皇子の御門の荒れまく惜しも</a></p>
<h2>（（日並皇子尊殯宮之時柿本朝臣人麻呂作歌一首[并短歌]）反歌二首）</h2>
<p><a href="0169.html">あかねさす日は照らせれどぬばたまの夜渡る月の隠らく惜しも</a></p>
<h2>（日並皇子尊殯宮之時柿本朝臣人麻呂作歌一首[并短歌]）或本歌一首</h2>
<p><a href="0170.html">嶋の宮まがりの池の放ち鳥人目に恋ひて池に潜かず</a></p>
<h2>皇子尊宮舎人等慟傷作歌廿三首</h2>
<p><a href="0171.html">高照らす我が日の御子の万代に国知らさまし嶋の宮はも</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0172.html">嶋の宮上の池なる放ち鳥荒びな行きそ君座さずとも</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0173.html">高照らす我が日の御子のいましせば島の御門は荒れずあらましを</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0174.html">外に見し真弓の岡も君座せば常つ御門と侍宿するかも</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0175.html">夢にだに見ずありしものをおほほしく宮出もするかさ桧の隈廻を</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0176.html">天地とともに終へむと思ひつつ仕へまつりし心違ひぬ</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0177.html">朝日照る佐田の岡辺に群れ居つつ我が泣く涙やむ時もなし</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0178.html">み立たしの島を見る時にはたづみ流るる涙止めぞかねつる</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0179.html">橘の嶋の宮には飽かぬかも佐田の岡辺に侍宿しに行く</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0180.html">み立たしの島をも家と棲む鳥も荒びな行きそ年かはるまで</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0181.html">み立たしの島の荒礒を今見れば生ひざりし草生ひにけるかも</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0182.html">鳥座立て飼ひし雁の子巣立ちなば真弓の岡に飛び帰り来ね</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0183.html">我が御門千代とことばに栄えむと思ひてありし我れし悲しも</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0184.html">東のたぎの御門に侍へど昨日も今日も召す言もなし</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0185.html">水伝ふ礒の浦廻の岩つつじ茂く咲く道をまたも見むかも</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0186.html">一日には千たび参りし東の大き御門を入りかてぬかも</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0187.html">つれもなき佐田の岡辺に帰り居ば島の御階に誰れか住まはむ</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0188.html">朝ぐもり日の入り行けばみ立たしの島に下り居て嘆きつるかも</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0189.html">朝日照る嶋の御門におほほしく人音もせねばまうら悲しも</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0190.html">真木柱太き心はありしかどこの我が心鎮めかねつも</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0191.html">けころもを時かたまけて出でましし宇陀の大野は思ほえむかも</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0192.html">朝日照る佐田の岡辺に泣く鳥の夜哭きかへらふこの年ころを</a></p>
<h2>（皇子尊宮舎人等慟傷作歌廿三首）</h2>
<p><a href="0193.html">畑子らが夜昼といはず行く道を我れはことごと宮道にぞする</a></p>
<h2>柿本朝臣人麻呂獻泊瀬部皇女忍坂部皇子歌一首[并短歌]</h2>
<p><a href="0194.html">飛ぶ鳥の 明日香の川の 上つ瀬に 生ふる玉藻は 下つ瀬に 流れ触らばふ 玉藻なす か寄りかく寄り 靡かひし 嬬の命の たたなづく 柔肌すらを 剣太刀 身に添へ寝ねば ぬばたまの 夜床も荒るらむ [一云 荒れなむ] そこ故に 慰めかねて けだしくも 逢ふやと思ひて [一云 君も逢ふやと] 玉垂の 越智の大野の 朝露に 玉藻はひづち 夕霧に 衣は濡れて 草枕 旅寝かもする 逢はぬ君故</a></p>
<h2>（柿本朝臣人麻呂獻泊瀬部皇女忍坂部皇子歌一首[并短歌]）反歌一首</h2>
<p><a href="0195.html">敷栲の袖交へし君玉垂の越智野過ぎ行くまたも逢はめやも [一云 越智野に過ぎぬ]</a></p>
<h2>明日香皇女木Ｐ殯宮之時柿本&lt;朝臣&gt;人麻呂作歌一首[并短歌]</h2>
<p><a href="0196.html">飛ぶ鳥の 明日香の川の 上つ瀬に 石橋渡し [一云 石なみ] 下つ瀬に 打橋渡す 石橋に [一云 石なみに] 生ひ靡ける 玉藻もぞ 絶ゆれば生ふる 打橋に 生ひををれる 川藻もぞ 枯るれば生ゆる なにしかも 我が大君の 立たせば 玉藻のもころ 臥やせば 川藻のごとく 靡かひし 宜しき君が 朝宮を 忘れたまふや 夕宮を 背きたまふや うつそみと 思ひし時に 春へは 花折りかざし 秋立てば 黄葉かざし 敷栲の 袖たづさはり 鏡なす 見れども飽かず 望月の いやめづらしみ 思ほしし 君と時々 出でまして 遊びたまひし 御食向ふ 城上の宮を 常宮と 定めたまひて あぢさはふ 目言も絶えぬ しかれかも [一云 そこをしも] あやに悲しみ ぬえ鳥の 片恋づま [一云 しつつ] 朝鳥の [一云 朝霧の] 通はす君が 夏草の 思ひ萎えて 夕星の か行きかく行き 大船の たゆたふ見れば 慰もる 心もあらず そこ故に 為むすべ知れや 音のみも 名のみも絶えず 天地の いや遠長く 偲ひ行かむ 御名に懸かせる 明日香川 万代までに はしきやし 我が大君の 形見かここを</a></p>
<h2>（明日香皇女木Ｐ殯宮之時柿本&lt;朝臣&gt;人麻呂作歌一首[并短歌]）短歌二首</h2>
<p><a href="0197.html">明日香川しがらみ渡し塞かませば流るる水ものどにかあらまし [一云 水の淀にかあらまし]</a></p>
<h2>（（明日香皇女木Ｐ殯宮之時柿本&lt;朝臣&gt;人麻呂作歌一首[并短歌]）短歌二首）</h2>
<p><a href="0198.html">明日香川明日だに [一云 さへ] 見むと思へやも [一云 思へかも] 我が大君の御名忘れせぬ [一云 御名忘らえぬ]</a></p>
<h2>高市皇子尊城上殯宮之時柿本朝臣人麻呂作歌一首[并短歌]</h2>
<p><a href="0199.html">かけまくも ゆゆしきかも [一云 ゆゆしけれども] 言はまくも あやに畏き 明日香の 真神の原に ひさかたの 天つ御門を 畏くも 定めたまひて 神さぶと 磐隠ります やすみしし 我が大君の きこしめす 背面の国の 真木立つ 不破山超えて 高麗剣 和射見が原の 仮宮に 天降りいまして 天の下 治めたまひ [一云 掃ひたまひて] 食す国を 定めたまふと 鶏が鳴く 東の国の 御いくさを 召したまひて ちはやぶる 人を和せと 奉ろはぬ 国を治めと [一云 掃へと] 皇子ながら 任したまへば 大御身に 大刀取り佩かし 大御手に 弓取り持たし 御軍士を 率ひたまひ 整ふる 鼓の音は 雷の 声と聞くまで 吹き鳴せる 小角の音も [一云 笛の音は] 敵見たる 虎か吼ゆると 諸人の おびゆるまでに [一云 聞き惑ふまで] ささげたる 幡の靡きは 冬こもり 春さり来れば 野ごとに つきてある火の [一云 冬こもり 春野焼く火の] 風の共 靡くがごとく 取り持てる 弓弭の騒き み雪降る 冬の林に [一云 木綿の林] つむじかも い巻き渡ると 思ふまで 聞きの畏く [一云 諸人の 見惑ふまでに] 引き放つ 矢の繁けく 大雪の 乱れて来れ [一云 霰なす そちより来れば] まつろはず 立ち向ひしも 露霜の 消なば消ぬべく 行く鳥の 争ふはしに [一云 朝霜の 消なば消とふに うつせみと 争ふはしに] 渡会の 斎きの宮ゆ 神風に い吹き惑はし 天雲を 日の目も見せず 常闇に 覆ひ賜ひて 定めてし 瑞穂の国を 神ながら 太敷きまして やすみしし 我が大君の 天の下 申したまへば 万代に しかしもあらむと [一云 かくしもあらむと] 木綿花の 栄ゆる時に 我が大君 皇子の御門を [一云 刺す竹の 皇子の御門を] 神宮に 装ひまつりて 使はしし 御門の人も 白栲の 麻衣着て 埴安の 御門の原に あかねさす 日のことごと 獣じもの い匍ひ伏しつつ ぬばたまの 夕になれば 大殿を 振り放け見つつ 鶉なす い匍ひ廻り 侍へど 侍ひえねば 春鳥の さまよひぬれば 嘆きも いまだ過ぎぬに 思ひも いまだ尽きねば 言さへく 百済の原ゆ 神葬り 葬りいまして あさもよし 城上の宮を 常宮と 高く奉りて 神ながら 鎮まりましぬ しかれども 我が大君の 万代と 思ほしめして 作らしし 香具山の宮 万代に 過ぎむと思へや 天のごと 振り放け見つつ 玉たすき 懸けて偲はむ 畏かれども</a></p>
<h2>（高市皇子尊城上殯宮之時柿本朝臣人麻呂作歌一首[并短歌]）短歌二首</h2>
<p><a href="0200.html">ひさかたの天知らしぬる君故に日月も知らず恋ひわたるかも</a></p>
<h2>（（高市皇子尊城上殯宮之時柿本朝臣人麻呂作歌一首[并短歌]）短歌二首）</h2>
<p><a href="0201.html">埴安の池の堤の隠り沼のゆくへを知らに舎人は惑ふ</a></p>
<h2>（高市皇子尊城上殯宮之時柿本朝臣人麻呂作歌一首[并短歌]）或書反歌一首</h2>
<p><a href="0202.html">哭沢の神社に三輪据ゑ祈れども我が大君は高日知らしぬ</a></p>
<h2>但馬皇女薨後穂積皇子冬日雪落遥望御墓悲傷流涕御作歌一首</h2>
<p><a href="0203.html">降る雪はあはにな降りそ吉隠の猪養の岡の塞なさまくに</a></p>
<h2>弓削皇子薨時置始東人&lt;作&gt;歌一首[并短歌]</h2>
<p><a href="0204.html">やすみしし 我が大君 高照らす 日の御子 ひさかたの 天つ宮に 神ながら 神といませば そこをしも あやに畏み 昼はも 日のことごと 夜はも 夜のことごと 伏し居嘆けど 飽き足らぬかも</a></p>
<h2>（弓削皇子薨時置始東人&lt;作&gt;歌一首[并短歌]）反歌一首</h2>
<p><a href="0205.html">大君は神にしませば天雲の五百重が下に隠りたまひぬ</a></p>
<h2>（弓削皇子薨時置始東人&lt;作&gt;歌一首[并短歌]）又短歌一首</h2>
<p><a href="0206.html">楽浪の志賀さざれ波しくしくに常にと君が思ほせりける</a></p>
<h2>柿本朝臣人麻呂妻死之後泣血哀慟作歌二首[并短歌]</h2>
<p><a href="0207.html">天飛ぶや 軽の道は 我妹子が 里にしあれば ねもころに 見まく欲しけど やまず行かば 人目を多み 数多く行かば 人知りぬべみ さね葛 後も逢はむと 大船の 思ひ頼みて 玉かぎる 岩垣淵の 隠りのみ 恋ひつつあるに 渡る日の 暮れぬるがごと 照る月の 雲隠るごと 沖つ藻の 靡きし妹は 黄葉の 過ぎて去にきと 玉梓の 使の言へば 梓弓 音に聞きて [一云 音のみ聞きて] 言はむすべ 為むすべ知らに 音のみを 聞きてありえねば 我が恋ふる 千重の一重も 慰もる 心もありやと 我妹子が やまず出で見し 軽の市に 我が立ち聞けば 玉たすき 畝傍の山に 鳴く鳥の 声も聞こえず 玉桙の 道行く人も ひとりだに 似てし行かねば すべをなみ 妹が名呼びて 袖ぞ振りつる [一云 名のみを聞きてありえねば]</a></p>
<h2>（柿本朝臣人麻呂妻死之後泣血哀慟作歌二首[并短歌]）短歌二首</h2>
<p><a href="0208.html">秋山の黄葉を茂み惑ひぬる妹を求めむ山道知らずも [一云 道知らずして]</a></p>
<h2>（（柿本朝臣人麻呂妻死之後泣血哀慟作歌二首[并短歌]）短歌二首）</h2>
<p><a href="0209.html">黄葉の散りゆくなへに玉梓の使を見れば逢ひし日思ほゆ</a></p>
<h2>（柿本朝臣人麻呂妻死之後泣血哀慟作歌二首[并短歌]）</h2>
<p><a href="0210.html">うつせみと 思ひし時に [一云 うつそみと 思ひし] 取り持ちて 我がふたり見し 走出の 堤に立てる 槻の木の こちごちの枝の 春の葉の 茂きがごとく 思へりし 妹にはあれど 頼めりし 子らにはあれど 世間を 背きしえねば かぎるひの 燃ゆる荒野に 白栲の 天領巾隠り 鳥じもの 朝立ちいまして 入日なす 隠りにしかば 我妹子が 形見に置ける みどり子の 乞ひ泣くごとに 取り与ふ 物しなければ 男じもの 脇ばさみ持ち 我妹子と ふたり我が寝し 枕付く 妻屋のうちに 昼はも うらさび暮らし 夜はも 息づき明かし 嘆けども 為むすべ知らに 恋ふれども 逢ふよしをなみ 大鳥の 羽がひの山に 我が恋ふる 妹はいますと 人の言へば 岩根さくみて なづみ来し よけくもぞなき うつせみと 思ひし妹が 玉かぎる ほのかにだにも 見えなく思へば</a></p>
<h2>（柿本朝臣人麻呂妻死之後泣血哀慟作歌二首[并短歌]）短歌二首</h2>
<p><a href="0211.html">去年見てし秋の月夜は照らせれど相見し妹はいや年離る</a></p>
<h2>（（柿本朝臣人麻呂妻死之後泣血哀慟作歌二首[并短歌]）短歌二首）</h2>
<p><a href="0212.html">衾道を引手の山に妹を置きて山道を行けば生けりともなし</a></p>
<h2>（柿本朝臣人麻呂妻死之後泣血哀慟作歌二首[并短歌]）或本歌曰</h2>
<p><a href="0213.html">うつそみと 思ひし時に たづさはり 我がふたり見し 出立の 百枝槻の木 こちごちに 枝させるごと 春の葉の 茂きがごとく 思へりし 妹にはあれど 頼めりし 妹にはあれど 世間を 背きしえねば かぎるひの 燃ゆる荒野に 白栲の 天領巾隠り 鳥じもの 朝立ちい行きて 入日なす 隠りにしかば 我妹子が 形見に置ける みどり子の 乞ひ泣くごとに 取り与ふ 物しなければ 男じもの 脇ばさみ持ち 我妹子と 二人我が寝し 枕付く 妻屋のうちに 昼は うらさび暮らし 夜は 息づき明かし 嘆けども 為むすべ知らに 恋ふれども 逢ふよしをなみ 大鳥の 羽がひの山に 汝が恋ふる 妹はいますと 人の言へば 岩根さくみて なづみ来し よけくもぞなき うつそみと 思ひし妹が 灰にてませば</a></p>
<h2>（柿本朝臣人麻呂妻死之後泣血哀慟作歌二首[并短歌]）短歌三首</h2>
<p><a href="0214.html">去年見てし秋の月夜は渡れども相見し妹はいや年離る</a></p>
<h2>（（柿本朝臣人麻呂妻死之後泣血哀慟作歌二首[并短歌]）短歌三首）</h2>
<p><a href="0215.html">衾道を引手の山に妹を置きて山道思ふに生けるともなし</a></p>
<h2>（（柿本朝臣人麻呂妻死之後泣血哀慟作歌二首[并短歌]）短歌三首）</h2>
<p><a href="0216.html">家に来て我が屋を見れば玉床の外に向きけり妹が木枕</a></p>
<h2>吉備津釆女死時柿本朝臣人麻呂作歌一首[并短歌]</h2>
<p><a href="0217.html">秋山の したへる妹 なよ竹の とをよる子らは いかさまに 思ひ居れか 栲縄の 長き命を 露こそば 朝に置きて 夕は 消ゆといへ 霧こそば 夕に立ちて 朝は 失すといへ 梓弓 音聞く我れも おほに見し こと悔しきを 敷栲の 手枕まきて 剣太刀 身に添へ寝けむ 若草の その嬬の子は 寂しみか 思ひて寝らむ 悔しみか 思ひ恋ふらむ 時ならず 過ぎにし子らが 朝露のごと 夕霧のごと</a></p>
<h2>（吉備津釆女死時柿本朝臣人麻呂作歌一首[并短歌]）短歌二首</h2>
<p><a href="0218.html">楽浪の志賀津の子らが [一云 志賀の津の子が] 罷り道の川瀬の道を見れば寂しも</a></p>
<h2>（（吉備津釆女死時柿本朝臣人麻呂作歌一首[并短歌]）短歌二首）</h2>
<p><a href="0219.html">そら数ふ大津の子が逢ひし日におほに見しかば今ぞ悔しき</a></p>
<h2>讃岐狭&lt;岑&gt;嶋視石中死人柿本朝臣人麻呂作歌一首[并短歌]</h2>
<p><a href="0220.html">玉藻よし 讃岐の国は 国からか 見れども飽かぬ 神からか ここだ貴き 天地 日月とともに 足り行かむ 神の御面と 継ぎ来る 那珂の港ゆ 船浮けて 我が漕ぎ来れば 時つ風 雲居に吹くに 沖見れば とゐ波立ち 辺見れば 白波騒く 鯨魚取り 海を畏み 行く船の 梶引き折りて をちこちの 島は多けど 名ぐはし 狭岑の島の 荒磯面に 廬りて見れば 波の音の 繁き浜辺を 敷栲の 枕になして 荒床に ころ臥す君が 家知らば 行きても告げむ 妻知らば 来も問はましを 玉桙の 道だに知らず おほほしく 待ちか恋ふらむ はしき妻らは</a></p>
<h2>（讃岐狭&lt;岑&gt;嶋視石中死人柿本朝臣人麻呂作歌一首[并短歌]）短歌二首</h2>
<p><a href="0221.html">妻もあらば摘みて食げまし沙弥の山野の上のうはぎ過ぎにけらずや</a></p>
<h2>（（讃岐狭&lt;岑&gt;嶋視石中死人柿本朝臣人麻呂作歌一首[并短歌]）短歌二首）</h2>
<p><a href="0222.html">沖つ波来寄る荒礒を敷栲の枕とまきて寝せる君かも</a></p>
<h2>柿本朝臣人麻呂在石見國臨死時自傷作歌一首</h2>
<p><a href="0223.html">鴨山の岩根しまける我れをかも知らにと妹が待ちつつあるらむ</a></p>
<h2>柿本朝臣人麻呂死時妻依羅娘子作歌二首</h2>
<p><a href="0224.html">今日今日と我が待つ君は石川の峽に [一云 谷に] 交りてありといはずやも</a></p>
<h2>（柿本朝臣人麻呂死時妻依羅娘子作歌二首）</h2>
<p><a href="0225.html">直の逢ひは逢ひかつましじ石川に雲立ち渡れ見つつ偲はむ</a></p>
<h2>丹比真人[名闕]擬柿本朝臣人麻呂之意報歌一首</h2>
<p><a href="0226.html">荒波に寄り来る玉を枕に置き我れここにありと誰れか告げなむ</a></p>
<h2>或本歌曰</h2>
<p><a href="0227.html">天離る鄙の荒野に君を置きて思ひつつあれば生けるともなし</a></p>
<h2>寧樂宮 / 和銅四年歳次辛亥河邊宮人姫嶋松原見嬢子屍悲嘆作歌二首</h2>
<p><a href="0228.html">妹が名は千代に流れむ姫島の小松がうれに蘿生すまでに</a></p>
<h2>（和銅四年歳次辛亥河邊宮人姫嶋松原見嬢子屍悲嘆作歌二首）</h2>
<p><a href="0229.html">難波潟潮干なありそね沈みにし妹が姿を見まく苦しも</a></p>
<h2>霊龜元年歳次乙卯秋九月志貴親王&lt;薨&gt;時作歌一首[并短歌]</h2>
<p><a href="0230.html">梓弓 手に取り持ちて ますらをの さつ矢手挟み 立ち向ふ 高円山に 春野焼く 野火と見るまで 燃ゆる火を 何かと問へば 玉鉾の 道来る人の 泣く涙 こさめに降れば 白栲の 衣ひづちて 立ち留まり 我れに語らく なにしかも もとなとぶらふ 聞けば 哭のみし泣かゆ 語れば 心ぞ痛き 天皇の 神の御子の いでましの 手火の光りぞ ここだ照りたる</a></p>
<h2>（霊龜元年歳次乙卯秋九月志貴親王&lt;薨&gt;時作歌一首[并短歌]）短歌二首</h2>
<p><a href="0231.html">高円の野辺の秋萩いたづらに咲きか散るらむ見る人なしに</a></p>
<h2>（（霊龜元年歳次乙卯秋九月志貴親王&lt;薨&gt;時作歌一首[并短歌]）短歌二首）</h2>
<p><a href="0232.html">御笠山野辺行く道はこきだくも繁く荒れたるか久にあらなくに</a></p>
<h2>（霊龜元年歳次乙卯秋九月志貴親王&lt;薨&gt;時作歌一首[并短歌]）或本歌曰</h2>
<p><a href="0233.html">高円の野辺の秋萩な散りそね君が形見に見つつ偲はむ</a></p>
<h2>（（霊龜元年歳次乙卯秋九月志貴親王&lt;薨&gt;時作歌一首[并短歌]）或本歌曰）</h2>
<p><a href="0234.html">御笠山野辺ゆ行く道こきだくも荒れにけるかも久にあらなくに</a></p>

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
