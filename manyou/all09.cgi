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
    <title>本日の万葉集 / 万葉集全首（第九巻）</title>
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

 <h1>万葉集全首（第九巻）</h1>

 <h2>雜歌 / 泊瀬朝倉宮御宇大泊瀬幼武天&lt;皇&gt;御製歌一首</h2>
<p><a href="1664.html">夕されば小倉の山に伏す鹿の今夜は鳴かず寐ねにけらしも</a></p>
<h2>崗本宮御宇天皇幸紀伊國時歌二首</h2>
<p><a href="1665.html">妹がため我れ玉拾ふ沖辺なる玉寄せ持ち来沖つ白波</a></p>
<h2>（崗本宮御宇天皇幸紀伊國時歌二首）</h2>
<p><a href="1666.html">朝霧に濡れにし衣干さずしてひとりか君が山道越ゆらむ</a></p>
<h2>大寳元年辛丑冬十月太上天皇大行天皇幸紀伊國時歌十三首</h2>
<p><a href="1667.html">妹がため我れ玉求む沖辺なる白玉寄せ来沖つ白波</a></p>
<h2>（大寳元年辛丑冬十月太上天皇大行天皇幸紀伊國時歌十三首）</h2>
<p><a href="1668.html">白崎は幸くあり待て大船に真梶しじ貫きまたかへり見む</a></p>
<h2>（大寳元年辛丑冬十月太上天皇大行天皇幸紀伊國時歌十三首）</h2>
<p><a href="1669.html">南部の浦潮な満ちそね鹿島なる釣りする海人を見て帰り来む</a></p>
<h2>（大寳元年辛丑冬十月太上天皇大行天皇幸紀伊國時歌十三首）</h2>
<p><a href="1670.html">朝開き漕ぎ出て我れは由良の崎釣りする海人を見て帰り来む</a></p>
<h2>（大寳元年辛丑冬十月太上天皇大行天皇幸紀伊國時歌十三首）</h2>
<p><a href="1671.html">由良の崎潮干にけらし白神の礒の浦廻をあへて漕ぐなり</a></p>
<h2>（大寳元年辛丑冬十月太上天皇大行天皇幸紀伊國時歌十三首）</h2>
<p><a href="1672.html">黒牛潟潮干の浦を紅の玉裳裾引き行くは誰が妻</a></p>
<h2>（大寳元年辛丑冬十月太上天皇大行天皇幸紀伊國時歌十三首）</h2>
<p><a href="1673.html">風莫の浜の白波いたづらにここに寄せ来る見る人なしに [一云 ここに寄せ来も] </a></p>
<h2>（大寳元年辛丑冬十月太上天皇大行天皇幸紀伊國時歌十三首）</h2>
<p><a href="1674.html">我が背子が使来むかと出立のこの松原を今日か過ぎなむ</a></p>
<h2>（大寳元年辛丑冬十月太上天皇大行天皇幸紀伊國時歌十三首）</h2>
<p><a href="1675.html">藤白の御坂を越ゆと白栲の我が衣手は濡れにけるかも</a></p>
<h2>（大寳元年辛丑冬十月太上天皇大行天皇幸紀伊國時歌十三首）</h2>
<p><a href="1676.html">背の山に黄葉常敷く神岳の山の黄葉は今日か散るらむ</a></p>
<h2>（大寳元年辛丑冬十月太上天皇大行天皇幸紀伊國時歌十三首）</h2>
<p><a href="1677.html">大和には聞こえも行くか大我野の竹葉刈り敷き廬りせりとは</a></p>
<h2>（大寳元年辛丑冬十月太上天皇大行天皇幸紀伊國時歌十三首）</h2>
<p><a href="1678.html">紀の国の昔弓雄の鳴り矢もち鹿取り靡けし坂の上にぞある</a></p>
<h2>（大寳元年辛丑冬十月太上天皇大行天皇幸紀伊國時歌十三首）</h2>
<p><a href="1679.html">紀の国にやまず通はむ妻の杜妻寄しこせね妻といひながら [一云 妻賜はにも妻といひながら] </a></p>
<h2>後人歌二首</h2>
<p><a href="1680.html">あさもよし紀へ行く君が真土山越ゆらむ今日ぞ雨な降りそね</a></p>
<h2>（後人歌二首）</h2>
<p><a href="1681.html">後れ居て我が恋ひ居れば白雲のたなびく山を今日か越ゆらむ</a></p>
<h2>獻忍壁皇子歌一首  [詠仙人形]</h2>
<p><a href="1682.html">とこしへに夏冬行けや裘扇放たぬ山に住む人</a></p>
<h2>獻舎人皇子歌二首</h2>
<p><a href="1683.html">妹が手を取りて引き攀ぢふさ手折り我がかざすべく花咲けるかも</a></p>
<h2>（獻舎人皇子歌二首）</h2>
<p><a href="1684.html">春山は散り過ぎぬとも三輪山はいまだふふめり君待ちかてに</a></p>
<h2>泉河邊間人宿祢作歌二首</h2>
<p><a href="1685.html">川の瀬のたぎつを見れば玉藻かも散り乱れたる川の常かも</a></p>
<h2>（泉河邊間人宿祢作歌二首）</h2>
<p><a href="1686.html">彦星のかざしの玉の妻恋ひに乱れにけらしこの川の瀬に</a></p>
<h2>鷺坂作歌一首</h2>
<p><a href="1687.html">白鳥の鷺坂山の松蔭に宿りて行かな夜も更けゆくを</a></p>
<h2>名木河作歌二首</h2>
<p><a href="1688.html">あぶり干す人もあれやも濡れ衣を家には遣らな旅のしるしに</a></p>
<h2>（名木河作歌二首）</h2>
<p><a href="1689.html">あり衣辺につきて漕がさね杏人の浜を過ぐれば恋しくありなり</a></p>
<h2>高島作歌二首</h2>
<p><a href="1690.html">高島の阿渡川波は騒けども我れは家思ふ宿り悲しみ</a></p>
<h2>（高島作歌二首）</h2>
<p><a href="1691.html">旅なれば夜中をさして照る月の高島山に隠らく惜しも</a></p>
<h2>紀伊國作歌二首</h2>
<p><a href="1692.html">我が恋ふる妹は逢はさず玉の浦に衣片敷き独りかも寝む</a></p>
<h2>（紀伊國作歌二首）</h2>
<p><a href="1693.html">玉櫛笥明けまく惜しきあたら夜を衣手離れて独りかも寝む</a></p>
<h2>鷺坂作歌一首</h2>
<p><a href="1694.html">栲領巾の鷺坂山の白つつじ我れににほはに妹に示さむ</a></p>
<h2>泉河作歌一首</h2>
<p><a href="1695.html">妹が門入り泉川の常滑にみ雪残れりいまだ冬かも</a></p>
<h2>名木河作歌三首</h2>
<p><a href="1696.html">衣手の名木の川辺を春雨に我れ立ち濡ると家思ふらむか</a></p>
<h2>（名木河作歌三首）</h2>
<p><a href="1697.html">家人の使ひにあらし春雨の避くれど我れを濡らさく思へば</a></p>
<h2>（名木河作歌三首）</h2>
<p><a href="1698.html">あぶり干す人もあれやも家人の春雨すらを間使ひにする</a></p>
<h2>宇治河作歌二首</h2>
<p><a href="1699.html">巨椋の入江響むなり射目人の伏見が田居に雁渡るらし</a></p>
<h2>（宇治河作歌二首）</h2>
<p><a href="1700.html">秋風に山吹の瀬の鳴るなへに天雲翔る雁に逢へるかも</a></p>
<h2>獻弓削皇子歌三首</h2>
<p><a href="1701.html">さ夜中と夜は更けぬらし雁が音の聞こゆる空ゆ月渡る見ゆ</a></p>
<h2>（獻弓削皇子歌三首）</h2>
<p><a href="1702.html">妹があたり繁き雁が音夕霧に来鳴きて過ぎぬすべなきまでに</a></p>
<h2>（獻弓削皇子歌三首）</h2>
<p><a href="1703.html">雲隠り雁鳴く時は秋山の黄葉片待つ時は過ぐれど</a></p>
<h2>獻舎人皇子歌二首</h2>
<p><a href="1704.html">ふさ手折り多武の山霧繁みかも細川の瀬に波の騒ける</a></p>
<h2>（獻舎人皇子歌二首）</h2>
<p><a href="1705.html">冬こもり春へを恋ひて植ゑし木の実になる時を片待つ我れぞ</a></p>
<h2>舎人皇子御歌一首</h2>
<p><a href="1706.html">ぬばたまの夜霧は立ちぬ衣手の高屋の上にたなびくまでに</a></p>
<h2>鷺坂作歌一首</h2>
<p><a href="1707.html">山背の久世の鷺坂神代より春は張りつつ秋は散りけり</a></p>
<h2>泉河邊作歌一首</h2>
<p><a href="1708.html">春草を馬咋山ゆ越え来なる雁の使は宿り過ぐなり</a></p>
<h2>獻弓削皇子歌一首</h2>
<p><a href="1709.html">御食向ふ南淵山の巌には降りしはだれか消え残りたる</a></p>
<h2></h2>
<p><a href="1710.html">我妹子が赤裳ひづちて植ゑし田を刈りて収めむ倉無の浜</a></p>
<h2></h2>
<p><a href="1711.html">百伝ふ八十の島廻を漕ぎ来れど粟の小島は見れど飽かぬかも</a></p>
<h2>登筑波山詠月一首</h2>
<p><a href="1712.html">天の原雲なき宵にぬばたまの夜渡る月の入らまく惜しも</a></p>
<h2>幸芳野離宮時歌二首</h2>
<p><a href="1713.html">滝の上の三船の山ゆ秋津辺に来鳴き渡るは誰れ呼子鳥</a></p>
<h2>（幸芳野離宮時歌二首）</h2>
<p><a href="1714.html">落ちたぎち流るる水の岩に触れ淀める淀に月の影見ゆ</a></p>
<h2>槐本歌一首</h2>
<p><a href="1715.html">楽浪の比良山風の海吹けば釣りする海人の袖返る見ゆ</a></p>
<h2>山上歌一首</h2>
<p><a href="1716.html">白波の浜松の木の手向けくさ幾代までにか年は経ぬらむ</a></p>
<h2>春日歌一首</h2>
<p><a href="1717.html">三川の淵瀬もおちず小網さすに衣手濡れぬ干す子はなしに</a></p>
<h2>高市歌一首</h2>
<p><a href="1718.html">率ひて漕ぎ行く舟は高島の安曇の港に泊てにけむかも</a></p>
<h2>春日蔵歌一首</h2>
<p><a href="1719.html">照る月を雲な隠しそ島蔭に我が舟泊てむ泊り知らずも</a></p>
<h2>元仁歌三首</h2>
<p><a href="1720.html">馬並めてうち群れ越え来今日見つる吉野の川をいつかへり見む</a></p>
<h2>（元仁歌三首）</h2>
<p><a href="1721.html">苦しくも暮れゆく日かも吉野川清き川原を見れど飽かなくに</a></p>
<h2>（元仁歌三首）</h2>
<p><a href="1722.html">吉野川川波高み滝の浦を見ずかなりなむ恋しけまくに</a></p>
<h2>絹歌一首</h2>
<p><a href="1723.html">かわづ鳴く六田の川の川柳のねもころ見れど飽かぬ川かも</a></p>
<h2>嶋足歌一首</h2>
<p><a href="1724.html">見まく欲り来しくもしるく吉野川音のさやけさ見るにともしく</a></p>
<h2>麻呂歌一首</h2>
<p><a href="1725.html">いにしへの賢しき人の遊びけむ吉野の川原見れど飽かぬかも</a></p>
<h2>丹比真人歌一首</h2>
<p><a href="1726.html">難波潟潮干に出でて玉藻刈る海人娘子ども汝が名告らさね</a></p>
<h2>和歌一首</h2>
<p><a href="1727.html">あさりする人とを見ませ草枕旅行く人に我が名は告らじ</a></p>
<h2>石川卿歌一首</h2>
<p><a href="1728.html">慰めて今夜は寝なむ明日よりは恋ひかも行かむこゆ別れなば</a></p>
<h2>宇合卿歌三首</h2>
<p><a href="1729.html">暁の夢に見えつつ梶島の礒越す波のしきてし思ほゆ</a></p>
<h2>（宇合卿歌三首）</h2>
<p><a href="1730.html">山科の石田の小野のははそ原見つつか君が山道越ゆらむ</a></p>
<h2>（宇合卿歌三首）</h2>
<p><a href="1731.html">山科の石田の杜に幣置かばけだし我妹に直に逢はむかも</a></p>
<h2>碁師歌二首</h2>
<p><a href="1732.html">大葉山霞たなびきさ夜更けて我が舟泊てむ泊り知らずも</a></p>
<h2>（碁師歌二首）</h2>
<p><a href="1733.html">思ひつつ来れど来かねて三尾の崎真長の浦をまたかへり見つ</a></p>
<h2>小辨歌一首</h2>
<p><a href="1734.html">高島の安曇の港を漕ぎ過ぎて塩津菅浦今か漕ぐらむ</a></p>
<h2>伊保麻呂歌一首</h2>
<p><a href="1735.html">我が畳三重の川原の礒の裏にかくしもがもと鳴くかはづかも</a></p>
<h2>式部大倭芳野作歌一首</h2>
<p><a href="1736.html">山高み白木綿花に落ちたぎつ夏身の川門見れど飽かぬかも</a></p>
<h2>兵部川原歌一首</h2>
<p><a href="1737.html">大滝を過ぎて夏身に近づきて清き川瀬を見るがさやけさ</a></p>
<h2>詠上総末珠名娘子一首[并短歌]</h2>
<p><a href="1738.html">しなが鳥 安房に継ぎたる 梓弓 周淮の珠名は 胸別けの 広き我妹 腰細の すがる娘子の その顔の きらきらしきに 花のごと 笑みて立てれば 玉桙の 道行く人は おのが行く 道は行かずて 呼ばなくに 門に至りぬ さし並ぶ 隣の君は あらかじめ 己妻離れて 乞はなくに 鍵さへ奉る 人皆の かく惑へれば たちしなひ 寄りてぞ妹は たはれてありける </a></p>
<h2>（詠上総末珠名娘子一首[并短歌]）反歌</h2>
<p><a href="1739.html">金門にし人の来立てば夜中にも身はたな知らず出でてぞ逢ひける</a></p>
<h2>詠水江浦嶋子一首[并短歌]</h2>
<p><a href="1740.html">春の日の 霞める時に 住吉の 岸に出で居て 釣舟の とをらふ見れば いにしへの ことぞ思ほゆる 水江の 浦島の子が 鰹釣り 鯛釣りほこり 七日まで 家にも来ずて 海境を 過ぎて漕ぎ行くに 海神の 神の娘子に たまさかに い漕ぎ向ひ 相とぶらひ 言成りしかば かき結び 常世に至り 海神の 神の宮の 内のへの 妙なる殿に たづさはり ふたり入り居て 老いもせず 死にもせずして 長き世に ありけるものを 世間の 愚か人の 我妹子に 告りて語らく しましくは 家に帰りて 父母に 事も告らひ 明日のごと 我れは来なむと 言ひければ 妹が言へらく 常世辺に また帰り来て 今のごと 逢はむとならば この櫛笥 開くなゆめと そこらくに 堅めし言を 住吉に 帰り来りて 家見れど 家も見かねて 里見れど 里も見かねて あやしみと そこに思はく 家ゆ出でて 三年の間に 垣もなく 家失せめやと この箱を 開きて見てば もとのごと 家はあらむと 玉櫛笥 少し開くに 白雲の 箱より出でて 常世辺に たなびきぬれば 立ち走り 叫び袖振り こいまろび 足ずりしつつ たちまちに 心消失せぬ 若くありし 肌も皺みぬ 黒くありし 髪も白けぬ ゆなゆなは 息さへ絶えて 後つひに 命死にける 水江の 浦島の子が 家ところ見ゆ </a></p>
<h2>（詠水江浦嶋子一首[并短歌]）反歌</h2>
<p><a href="1741.html">常世辺に住むべきものを剣大刀汝が心からおそやこの君</a></p>
<h2>見河内大橋獨去娘子歌一首[并短歌]</h2>
<p><a href="1742.html">しな照る 片足羽川の さ丹塗りの 大橋の上ゆ 紅の 赤裳裾引き 山藍もち 摺れる衣着て ただ独り い渡らす子は 若草の 夫かあるらむ 橿の実の 独りか寝らむ 問はまくの 欲しき我妹が 家の知らなく </a></p>
<h2>（見河内大橋獨去娘子歌一首[并短歌]）反歌</h2>
<p><a href="1743.html">大橋の頭に家あらばま悲しく独り行く子に宿貸さましを</a></p>
<h2>見武蔵小埼沼鴨作歌一首</h2>
<p><a href="1744.html">埼玉の小埼の沼に鴨ぞ羽霧るおのが尾に降り置ける霜を掃ふとにあらし</a></p>
<h2>那賀郡曝井歌一首</h2>
<p><a href="1745.html">三栗の那賀に向へる曝井の絶えず通はむそこに妻もが</a></p>
<h2>手綱濱歌一首</h2>
<p><a href="1746.html">遠妻し多賀にありせば知らずとも手綱の浜の尋ね来なまし</a></p>
<h2>春三月諸卿大夫等下難波時歌二首[并短歌]</h2>
<p><a href="1747.html">白雲の 龍田の山の 瀧の上の 小椋の嶺に 咲きををる 桜の花は 山高み 風しやまねば 春雨の 継ぎてし降れば ほつ枝は 散り過ぎにけり 下枝に 残れる花は しましくは 散りな乱ひそ 草枕 旅行く君が 帰り来るまで </a></p>
<h2>（春三月諸卿大夫等下難波時歌二首[并短歌]）反歌</h2>
<p><a href="1748.html">我が行きは七日は過ぎじ龍田彦ゆめこの花を風にな散らし</a></p>
<h2>（春三月諸卿大夫等下難波時歌二首[并短歌]）</h2>
<p><a href="1749.html">白雲の 龍田の山を 夕暮れに うち越え行けば 瀧の上の 桜の花は 咲きたるは 散り過ぎにけり ふふめるは 咲き継ぎぬべし こちごちの 花の盛りに あらずとも 君がみ行きは 今にしあるべし </a></p>
<h2>（春三月諸卿大夫等下難波時歌二首[并短歌]）反歌</h2>
<p><a href="1750.html">暇あらばなづさひ渡り向つ峰の桜の花も折らましものを</a></p>
<h2>難波經宿明日還来之時歌一首[并短歌]</h2>
<p><a href="1751.html">島山を い行き廻れる 川沿ひの 岡辺の道ゆ 昨日こそ 我が越え来しか 一夜のみ 寝たりしからに 峰の上の 桜の花は 瀧の瀬ゆ 散らひて流る 君が見む その日までには 山おろしの 風な吹きそと うち越えて 名に負へる杜に 風祭せな </a></p>
<h2>（難波經宿明日還来之時歌一首[并短歌]）反歌</h2>
<p><a href="1752.html">い行き逢ひの坂のふもとに咲きををる桜の花を見せむ子もがも</a></p>
<h2>検税使大伴卿登筑波山時歌一首[并短歌]</h2>
<p><a href="1753.html">衣手 常陸の国の 二並ぶ 筑波の山を 見まく欲り 君来ませりと 暑けくに 汗かき嘆げ 木の根取り うそぶき登り 峰の上を 君に見すれば 男神も 許したまひ 女神も ちはひたまひて 時となく 雲居雨降る 筑波嶺を さやに照らして いふかりし 国のまほらを つばらかに 示したまへば 嬉しみと 紐の緒解きて 家のごと 解けてぞ遊ぶ うち靡く 春見ましゆは 夏草の 茂くはあれど 今日の楽しさ </a></p>
<h2>（検税使大伴卿登筑波山時歌一首[并短歌]）反歌</h2>
<p><a href="1754.html">今日の日にいかにかしかむ筑波嶺に昔の人の来けむその日も</a></p>
<h2>詠霍公鳥一首[并短歌]</h2>
<p><a href="1755.html">鴬の 卵の中に 霍公鳥 独り生れて 己が父に 似ては鳴かず 己が母に 似ては鳴かず 卯の花の 咲きたる野辺ゆ 飛び翔り 来鳴き響もし 橘の 花を居散らし ひねもすに 鳴けど聞きよし 賄はせむ 遠くな行きそ 我が宿の 花橘に 住みわたれ鳥 </a></p>
<h2>（詠霍公鳥一首[并短歌]）反歌</h2>
<p><a href="1756.html">かき霧らし雨の降る夜を霍公鳥鳴きて行くなりあはれその鳥</a></p>
<h2>登筑波山歌一首[并短歌]</h2>
<p><a href="1757.html">草枕 旅の憂へを 慰もる こともありやと 筑波嶺に 登りて見れば 尾花散る 師付の田居に 雁がねも 寒く来鳴きぬ 新治の 鳥羽の淡海も 秋風に 白波立ちぬ 筑波嶺の よけくを見れば 長き日に 思ひ積み来し 憂へはやみぬ </a></p>
<h2>（登筑波山歌一首[并短歌]）反歌</h2>
<p><a href="1758.html">筑波嶺の裾廻の田居に秋田刈る妹がり遣らむ黄葉手折らな</a></p>
<h2>登筑波嶺為の歌會日作歌一首[并短歌]</h2>
<p><a href="1759.html">鷲の住む 筑波の山の 裳羽服津の その津の上に 率ひて 娘子壮士の 行き集ひ かがふかがひに 人妻に 我も交らむ 我が妻に 人も言問へ この山を うしはく神の 昔より 禁めぬわざぞ 今日のみは めぐしもな見そ 事もとがむな [の歌は、東の俗語に賀我比と曰ふ]</a></p>
<h2>（登筑波嶺為の歌會日作歌一首[并短歌]）反歌</h2>
<p><a href="1760.html">男神に雲立ち上りしぐれ降り濡れ通るとも我れ帰らめや</a></p>
<h2>詠鳴&lt;鹿&gt;一首[并短歌]</h2>
<p><a href="1761.html">三諸の 神奈備山に たち向ふ 御垣の山に 秋萩の 妻をまかむと 朝月夜 明けまく惜しみ あしひきの 山彦響め 呼びたて鳴くも </a></p>
<h2>（詠鳴&lt;鹿&gt;一首[并短歌]）反歌</h2>
<p><a href="1762.html">明日の宵逢はざらめやもあしひきの山彦響め呼びたて鳴くも</a></p>
<h2>沙弥女王歌一首</h2>
<p><a href="1763.html">倉橋の山を高みか夜隠りに出で来る月の片待ちかたき</a></p>
<h2>七夕歌一首[并短歌]</h2>
<p><a href="1764.html">久方の 天の川に 上つ瀬に 玉橋渡し 下つ瀬に 舟浮け据ゑ 雨降りて 風吹かずとも 風吹きて 雨降らずとも 裳濡らさず やまず来ませと 玉橋渡す </a></p>
<h2>（七夕歌一首[并短歌]）反歌</h2>
<p><a href="1765.html">天の川霧立ちわたる今日今日と我が待つ君し舟出すらしも</a></p>
<h2>相聞 / 振田向宿祢退筑紫國時歌一首</h2>
<p><a href="1766.html">我妹子は釧にあらなむ左手の我が奥の手に巻きて去なましを</a></p>
<h2>抜氣大首任筑紫時娶豊前國娘子紐兒作歌三首</h2>
<p><a href="1767.html">豊国の香春は我家紐児にいつがり居れば香春は我家</a></p>
<h2>（抜氣大首任筑紫時娶豊前國娘子紐兒作歌三首）</h2>
<p><a href="1768.html">石上布留の早稲田の穂には出でず心のうちに恋ふるこのころ</a></p>
<h2>（抜氣大首任筑紫時娶豊前國娘子紐兒作歌三首）</h2>
<p><a href="1769.html">かくのみし恋ひしわたればたまきはる命も我れは惜しけくもなし</a></p>
<h2>大神大夫任長門守時集三輪河邊宴歌二首</h2>
<p><a href="1770.html">みもろの神の帯ばせる泊瀬川水脈し絶えずは我れ忘れめや</a></p>
<h2>（大神大夫任長門守時集三輪河邊宴歌二首）</h2>
<p><a href="1771.html">後れ居て我れはや恋ひむ春霞たなびく山を君が越え去なば</a></p>
<h2>大神大夫任筑紫國時阿倍大夫作歌一首</h2>
<p><a href="1772.html">後れ居て我れはや恋ひむ印南野の秋萩見つつ去なむ子故に</a></p>
<h2>獻弓削皇子歌一首</h2>
<p><a href="1773.html">神なびの神寄せ板にする杉の思ひも過ぎず恋の繁きに</a></p>
<h2>獻舎人皇子歌二首</h2>
<p><a href="1774.html">たらちねの母の命の言にあらば年の緒長く頼め過ぎむや</a></p>
<h2>（獻舎人皇子歌二首）</h2>
<p><a href="1775.html">泊瀬川夕渡り来て我妹子が家の金門に近づきにけり</a></p>
<h2>石川大夫遷任上京時播磨娘子贈歌二首</h2>
<p><a href="1776.html">絶等寸の山の峰の上の桜花咲かむ春へは君し偲はむ</a></p>
<h2>（石川大夫遷任上京時播磨娘子贈歌二首）</h2>
<p><a href="1777.html">君なくはなぞ身装はむ櫛笥なる黄楊の小櫛も取らむとも思はず</a></p>
<h2>藤井連遷任上京時娘子贈歌一首</h2>
<p><a href="1778.html">明日よりは我れは恋ひむな名欲山岩踏み平し君が越え去なば</a></p>
<h2>藤井連和歌一首</h2>
<p><a href="1779.html">命をしま幸くもがも名欲山岩踏み平しまたまたも来む</a></p>
<h2>鹿嶋郡苅野橋別大伴卿歌一首[并短歌]</h2>
<p><a href="1780.html">ことひ牛の 三宅の潟に さし向ふ 鹿島の崎に さ丹塗りの 小舟を設け 玉巻きの 小楫繁貫き 夕潮の 満ちのとどみに 御船子を 率ひたてて 呼びたてて 御船出でなば 浜も狭に 後れ並み居て こいまろび 恋ひかも居らむ 足すりし 音のみや泣かむ 海上の その津を指して 君が漕ぎ行かば </a></p>
<h2>（鹿嶋郡苅野橋別大伴卿歌一首[并短歌]）反歌</h2>
<p><a href="1781.html">海つ道のなぎなむ時も渡らなむかく立つ波に船出すべしや</a></p>
<h2>与妻歌一首</h2>
<p><a href="1782.html">雪こそば春日消ゆらめ心さへ消え失せたれや言も通はぬ</a></p>
<h2>妻和歌一首</h2>
<p><a href="1783.html">松返りしひてあれやは三栗の中上り来ぬ麻呂といふ奴</a></p>
<h2>贈入唐使歌一首</h2>
<p><a href="1784.html">海神のいづれの神を祈らばか行くさも来さも船の早けむ</a></p>
<h2>神龜五年戊辰秋八月歌一首[并短歌]</h2>
<p><a href="1785.html">人となる ことはかたきを わくらばに なれる我が身は 死にも生きも 君がまにまと 思ひつつ ありし間に うつせみの 世の人なれば 大君の 命畏み 天離る 鄙治めにと 朝鳥の 朝立ちしつつ 群鳥の 群立ち行かば 留まり居て 我れは恋ひむな 見ず久ならば </a></p>
<h2>（神龜五年戊辰秋八月歌一首[并短歌]）反歌</h2>
<p><a href="1786.html">み越道の雪降る山を越えむ日は留まれる我れを懸けて偲はせ</a></p>
<h2>天平元年己巳冬十二月歌一首[并短歌]</h2>
<p><a href="1787.html">うつせみの 世の人なれば 大君の 命畏み 敷島の 大和の国の 石上 布留の里に 紐解かず 丸寝をすれば 我が着たる 衣はなれぬ 見るごとに 恋はまされど 色に出でば 人知りぬべみ 冬の夜の 明かしもえぬを 寐も寝ずに 我れはぞ恋ふる 妹が直香に </a></p>
<h2>（天平元年己巳冬十二月歌一首[并短歌]）反歌</h2>
<p><a href="1788.html">布留山ゆ直に見わたす都にぞ寐も寝ず恋ふる遠くあらなくに</a></p>
<h2>（（天平元年己巳冬十二月歌一首[并短歌]）反歌）</h2>
<p><a href="1789.html">我妹子が結ひてし紐を解かめやも絶えば絶ゆとも直に逢ふまでに</a></p>
<h2>天平五年癸酉遣唐使舶發難波入海之時親母贈子歌一首[并短歌]</h2>
<p><a href="1790.html">秋萩を 妻どふ鹿こそ 独り子に 子持てりといへ 鹿子じもの 我が独り子の 草枕 旅にし行けば 竹玉を 繁に貫き垂れ 斎瓮に 木綿取り垂でて 斎ひつつ 我が思ふ我子 ま幸くありこそ </a></p>
<h2>（天平五年癸酉遣唐使舶發難波入海之時親母贈子歌一首[并短歌]）反歌</h2>
<p><a href="1791.html">旅人の宿りせむ野に霜降らば我が子羽ぐくめ天の鶴群</a></p>
<h2>思娘子作歌一首[并短歌]</h2>
<p><a href="1792.html">白玉の 人のその名を なかなかに 言を下延へ 逢はぬ日の 数多く過ぐれば 恋ふる日の 重なりゆけば 思ひ遣る たどきを知らに 肝向ふ 心砕けて 玉たすき 懸けぬ時なく 口やまず 我が恋ふる子を 玉釧 手に取り持ちて まそ鏡 直目に見ねば したひ山 下行く水の 上に出でず 我が思ふ心 安きそらかも </a></p>
<h2>（思娘子作歌一首[并短歌]）反歌</h2>
<p><a href="1793.html">垣ほなす人の横言繁みかも逢はぬ日数多く月の経ぬらむ</a></p>
<h2>（（思娘子作歌一首[并短歌]）反歌）</h2>
<p><a href="1794.html">たち変り月重なりて逢はねどもさね忘らえず面影にして</a></p>
<h2>挽歌 / 宇治若郎子宮所歌一首</h2>
<p><a href="1795.html">妹らがり今木の嶺に茂り立つ嬬松の木は古人見けむ</a></p>
<h2>紀伊國作歌四首</h2>
<p><a href="1796.html">黄葉の過ぎにし子らと携はり遊びし礒を見れば悲しも</a></p>
<h2>（紀伊國作歌四首）</h2>
<p><a href="1797.html">潮気立つ荒礒にはあれど行く水の過ぎにし妹が形見とぞ来し</a></p>
<h2>（紀伊國作歌四首）</h2>
<p><a href="1798.html">いにしへに妹と我が見しぬばたまの黒牛潟を見れば寂しも</a></p>
<h2>（紀伊國作歌四首）</h2>
<p><a href="1799.html">玉津島礒の浦廻の真砂にもにほひて行かな妹も触れけむ</a></p>
<h2>過足柄坂見死人作歌一首</h2>
<p><a href="1800.html">小垣内の 麻を引き干し 妹なねが 作り着せけむ 白栲の 紐をも解かず 一重結ふ 帯を三重結ひ 苦しきに 仕へ奉りて 今だにも 国に罷りて 父母も 妻をも見むと 思ひつつ 行きけむ君は 鶏が鳴く 東の国の 畏きや 神の御坂に 和妙の 衣寒らに ぬばたまの 髪は乱れて 国問へど 国をも告らず 家問へど 家をも言はず ますらをの 行きのまにまに ここに臥やせる </a></p>
<h2>過葦屋處女墓時作歌一首[并短歌]</h2>
<p><a href="1801.html">古への ますら壮士の 相競ひ 妻問ひしけむ 葦屋の 菟原娘子の 奥城を 我が立ち見れば 長き世の 語りにしつつ 後人の 偲ひにせむと 玉桙の 道の辺近く 岩構へ 造れる塚を 天雲の そくへの極み この道を 行く人ごとに 行き寄りて い立ち嘆かひ ある人は 哭にも泣きつつ 語り継ぎ 偲ひ継ぎくる 娘子らが 奥城処 我れさへに 見れば悲しも 古へ思へば </a></p>
<h2>（過葦屋處女墓時作歌一首[并短歌]）反歌</h2>
<p><a href="1802.html">古への信太壮士の妻問ひし菟原娘子の奥城ぞこれ</a></p>
<h2>（（過葦屋處女墓時作歌一首[并短歌]）反歌）</h2>
<p><a href="1803.html">語り継ぐからにもここだ恋しきを直目に見けむ古へ壮士</a></p>
<h2>哀弟死去作歌一首[并短歌]</h2>
<p><a href="1804.html">父母が 成しのまにまに 箸向ふ 弟の命は 朝露の 消やすき命 神の共 争ひかねて 葦原の 瑞穂の国に 家なみか また帰り来ぬ 遠つ国 黄泉の境に 延ふ蔦の おのが向き向き 天雲の 別れし行けば 闇夜なす 思ひ惑はひ 射ゆ鹿の 心を痛み 葦垣の 思ひ乱れて 春鳥の 哭のみ泣きつつ あぢさはふ 夜昼知らず かぎろひの 心燃えつつ 嘆く別れを </a></p>
<h2>（哀弟死去作歌一首[并短歌]）反歌</h2>
<p><a href="1805.html">別れてもまたも逢ふべく思ほえば心乱れて我れ恋ひめやも [一云 心尽して]</a></p>
<h2>（（哀弟死去作歌一首[并短歌]）反歌）</h2>
<p><a href="1806.html">あしひきの荒山中に送り置きて帰らふ見れば心苦しも</a></p>
<h2>詠勝鹿真間娘子歌一首[并短歌]</h2>
<p><a href="1807.html">鶏が鳴く 東の国に 古へに ありけることと 今までに 絶えず言ひける 勝鹿の 真間の手児名が 麻衣に 青衿着け ひたさ麻を 裳には織り着て 髪だにも 掻きは梳らず 沓をだに はかず行けども 錦綾の 中に包める 斎ひ子も 妹にしかめや 望月の 足れる面わに 花のごと 笑みて立てれば 夏虫の 火に入るがごと 港入りに 舟漕ぐごとく 行きかぐれ 人の言ふ時 いくばくも 生けらじものを 何すとか 身をたな知りて 波の音の 騒く港の 奥城に 妹が臥やせる 遠き代に ありけることを 昨日しも 見けむがごとも 思ほゆるかも</a></p>
<h2>（詠勝鹿真間娘子歌一首[并短歌]）反歌</h2>
<p><a href="1808.html">勝鹿の真間の井見れば立ち平し水汲ましけむ手児名し思ほゆ</a></p>
<h2>見菟原處女墓歌一首[并短歌]</h2>
<p><a href="1809.html">葦屋の 菟原娘子の 八年子の 片生ひの時ゆ 小放りに 髪たくまでに 並び居る 家にも見えず 虚木綿の 隠りて居れば 見てしかと いぶせむ時の 垣ほなす 人の問ふ時 茅渟壮士 菟原壮士の 伏屋焚き すすし競ひ 相よばひ しける時は 焼太刀の 手かみ押しねり 白真弓 靫取り負ひて 水に入り 火にも入らむと 立ち向ひ 競ひし時に 我妹子が 母に語らく しつたまき いやしき我が故 ますらをの 争ふ見れば 生けりとも 逢ふべくあれや ししくしろ 黄泉に待たむと 隠り沼の 下延へ置きて うち嘆き 妹が去ぬれば 茅渟壮士 その夜夢に見 とり続き 追ひ行きければ 後れたる 菟原壮士い 天仰ぎ 叫びおらび 地を踏み きかみたけびて もころ男に 負けてはあらじと 懸け佩きの 小太刀取り佩き ところづら 尋め行きければ 親族どち い行き集ひ 長き代に 標にせむと 遠き代に 語り継がむと 娘子墓 中に造り置き 壮士墓 このもかのもに 造り置ける 故縁聞きて 知らねども 新喪のごとも 哭泣きつるかも </a></p>
<h2>（見菟原處女墓歌一首[并短歌]）反歌</h2>
<p><a href="1810.html">芦屋の菟原娘子の奥城を行き来と見れば哭のみし泣かゆ</a></p>
<h2>（（見菟原處女墓歌一首[并短歌]）反歌）</h2>
<p><a href="1811.html">墓の上の木の枝靡けり聞きしごと茅渟壮士にし寄りにけらしも</a></p>

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