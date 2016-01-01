# coding: utf-8
__author__ = 'Ruben'
data = '''

<!DOCTYPE html>
<html dir="ltr" lang="fr">
<head>
    <meta charset="windows-1252"/>
    <meta name="msvalidate.01" content="A36C61EB614A11D8C591351E6A42139B" />
    <link rel="shortcut icon" href="/images/default.png"/>
    <link rel="alternate" type="application/rss+xml" title="T411 :: Torrents" href="/rss/" />
    <link rel="alternate" type="application/rss+xml" title="T411 :: Torrents Rapides" href="/rsshot/" />
    <link rel="search" type="application/opensearchdescription+xml" title="T411 :: Torrents Search" href="/opensearch.xml"/>
    <title>T411 - Torrent 411 - Tracker Torrent Fran&#231;ais - French Torrent Tracker - Tracker Torrent Fr</title>
    <meta name="keywords" content="torrent, torrents, torrent francais, french torrent, torrents french, tracker fr"/>
    <meta name="description" content="Torrent 411 - Les Pages Jaunes du Torrent Francais - French Torrent Tracker - Tracker Torrent Fr - L'Acad&#233;mie du Torrent Fran&#231;ais"/>
    <link rel="profile" href="http://gmpg.org/xfn/11"/>
    <link media="screen" rel="stylesheet" type="text/css" href="/themes/blue/css/jquery-ui.css"/>
<!--    <link media="screen" rel="stylesheet" type="text/css" href="/themes/blue/css/styles.css"/>-->
    <link media="screen" rel="stylesheet" type="text/css" href="/themes/blue/css/styles.min.css?v=10"/>

    <script type="text/javascript" src="/js/jquery/jquery-1.7.js"></script>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.16/jquery-ui.min.js"></script>

    <script type="text/javascript" src="/js/jquery/jquery.cookie.js"></script>
    <script type="text/javascript" src="/js/jquery/jquery.easing.js"></script>
    <script type="text/javascript" src="/js/jquery/jquery.lavalamp.js"></script>
    <script type="text/javascript" src="/js/jquery/jquery.tools.min.js"></script>
<!--    <script type="text/javascript" defer src="/js/swfobject.js"></script>-->
    <script type="text/javascript" src="/js/messages.js"></script>
    <!--<script type="text/javascript" src="/themes/blue/js/theme.js"></script>-->
    <script type="text/javascript" src="/themes/blue/js/theme.min.js?v=6"></script>

    <script type="text/javascript" src="/themes/blue/js/jbox.js"></script>
    <link media="screen" rel="stylesheet" type="text/css" href="/themes/blue/css/jbox.css">

            <!-- head -->

    <!--[if IE]>
    <script type="text/javascript" defer src="/js/html5forIE.js"></script>
<![endif]-->
<!--[if IE 7]>
    <link media="screen" rel="stylesheet" type="text/css" href="/themes/blue/css/styles-ie7.css" />
<![endif]-->
    <script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-5001083-1']);
      _gaq.push(['_trackPageview']);

      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();
    </script>
    <link rel="alternate" type="application/rss+xml" title="T411 :: Film/Vidéo :: @name divergente 2 " href="/torrents/rss/?search=%40name+divergente+2+&cat=210" /></head>
<body>
<div class="headerPlace">
  <div class="loginWrapper">
      <div class="loginBox">
    <form action="/users/login/" id="loginform" method="post">
        <input type="hidden" name="url" value="/torrents/search/?name=divergente+2&description=&file=&user=&cat=210&subcat=&search=%40name+divergente+2+&submit=Recherche"/>
        <label class="username" for="login">Pseudonyme</label>
        <input class="userInput" id="login" name="login"/>
        <label class="password" for="password">Mot de passe</label>
        <input class="passInput" type="password" id="password" name="password"/>
        <input type="submit" class="loginbtn" value="Connexion"/>
        <input type="checkbox" id="remeberMe" name="remember" value="1" class="rememberMe"  checked/>
        <label class="remMe" for="remeberMe">Rester connect&eacute;</label>
        <ul class="register">
            <li><a href="/users/signup/" title="Enregistrer un compte">Enregistrer un compte</a></li>
            <li><a href="/users/recover/" title="Mot de passe oubli&eacute;?">Mot de passe oubli&eacute;?</a></li>
        </ul>
    </form>
</div>
  </div>
  <div class="headWrapper">
    <div class="head">
      <div class="logo"><a href="/" title="Torrent411">Torrent411</a></div>
      <div class="toolbar">
        <div class="searchBar">
    <form id="bar-search" action="/torrents/search/" method="GET">
        <input x-webkit-speech speech style="width: 230px; margin-top: 8px;" class="searchInput" name="search"
               type="text" data-url="//api.t411.in/suggest?term="
               value=""/>

        <span class="searchBtn"></span>
        <span class="searchHistory" data-url="//api.t411.in/torrents/searches"></span>
    </form>
</div>
<style>

    #bar-search .searchHistory {
        color: white;
        display: inline;
        float: left;
        width: 20px;
        height: 20px;
        margin-top: 8px;
        background: url("/themes/blue/images/search-history.png") repeat scroll 0 0 transparent;
        border: 0 none;
        cursor: pointer;
        margin-top: 8px;
        position: relative;

    }

    #bar-search .searchBtn {
        float: left;
    }

    .searches {
        z-index: 10000;
        position: absolute;
        display: none;
        top: 26px;
        left: 254px;

    }

    .searches .dropdown-menu {
        position: absolute;
        top: 100%;
        left: 0;
        z-index: 1000;
        display: none;
        float: left;
        min-width: 160px;
        padding: 5px 0;
        margin: 2px 0 0;
        list-style: none;
        background-color: #ffffff;
        border: 1px solid #ccc;
        border: 1px solid rgba(0, 0, 0, 0.2);
        -webkit-border-radius: 6px;
        -moz-border-radius: 6px;
        border-radius: 6px;
        -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
        -moz-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
        box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
        -webkit-background-clip: padding-box;
        -moz-background-clip: padding;
        background-clip: padding-box;
    }

    .searches .dropdown-menu > li > a {
        display: block;
        padding: 3px 20px;
        clear: both;
        font-weight: normal;
        line-height: 20px;
        color: #333333;
        white-space: nowrap;
    }


</style>
<div class="dropdown clearfix searches">
    <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu"
        style="display: block; position: static; margin-bottom: 5px; *width: 180px;">
        <li>
            <a href="/my/search/">Mes Recherches</a>
        </li>
    </ul>
</div>
<script>

</script>                    <div class="loginBar">
                <a href="/users/signup/" title="Enregistrer un compte" class="reg">Enregistrer un compte</a>
                <span class="sep">|</span>
                <a href="/users/login/" title="Login" class="slide" >Connexion</a>
            </div>
                <div class="loginBarSide"></div>
      </div>
      <ul id="lavamenu">
    <li><a href="/" title="Accueil">Accueil</a></li>
    <li><a href="#" title="Torrents" onclick="javascript:return false;">Torrents</a>
        <ul>
            <li><a href="/requests/">Demander/Combler un torrent</a></li>
<!--            <li><a href="/torrents/presentation/">G&#233;n&#233;rateur de Pr&#233;sentations</a></li>-->
            <li><a href="/cloud/">Mots-cl&#233;s Populaires</a></li>
            <li><a href="/torrents/search/">Rechercher un Torrent</a></li>
<!--            <li><a href="/torrents/search/">Rechercher un Torrent</a></li>-->
            <li><a href="/top/today/">Torrents du Jour</a></li>
            <li><a href="/top/week/">Torrents de la Semaine</a></li>
            <li><a href="/top/month/">Torrents du Mois</a></li>
            <li><a href="/torrents/needseed/">Torrents non Seed&#233;s</a></li>
            <li><a href="/top/100/">Torrents Rapides (Top 100)</a></li>
            <li><a href="/torrents/upload-step-1/">Uploader un Torrent</a></li>
        </ul>
    </li>
    <li><a href="#" title="Communaut&#233;" onclick="javascript:return false;">Communaut&#233;</a>
        <ul>
            <li><a href="irc://irc.t411.in/t411">Chat IRC</a></li>
            <li><a href="irc://irc.t411.in:+9999/t411">Chat IRC SSL</a></li>
            <li><a href="http://wiki.t411.in">DokuWiki</a></li>
            <li><a href="/forum.php">Forum</a></li>
            <li><a href="/users/staff/">Le Staff</a></li>
            <li><a href="/users/online/">Membres en Ligne</a></li>
            <li><a href="/users/search/">Rechercher un Membre</a></li>
        </ul>
    </li>
    <li><a href="#" title="Support" onclick="javascript:return false;">Support</a>
        <ul>
            <li><a href="/tags/">Tester votre PREZ</a></li>
            <li><a href="/tos/">Conditions d'Utilisation</a></li>
            <li><a href="/contactstaff/">Contacter le Staff</a></li>
                        <li><a href="/formats/">Formats des Fichiers</a></li>
            <li><a href="/videoformats/">Formats Vid&#233;o</a></li>
            <li><a href="/rules/">R&#232;gles du Site</a></li>
            <li><a href="/faq/#332">R&#232;gles d'Upload</a></li>
            <li><a href=/ratio/>Calculer son Ratio</a></li>
        </ul>
    </li>
    <li><a href="/faq/" title="FAQ">FAQ</a></li>
    <li><a href="#" title="Produits" onclick="javascript:return false;">Produits</a>
        <ul>
            <li><a href="http://T411.ourtoolbar.com" target="_blank">Toolbar</a></li>
        </ul>
    </li>
    <li><a href="/rssinfo/" title="Flux RSS">Flux RSS</a>
        <ul>
            <li><a href="/rsshot/" class="rss textleft">Torrents Rapides</a></li>
                        <li><a href="/rss/?cat=395" class="rss textleft">Audio</a></li>
                        <li><a href="/rss/?cat=404" class="rss textleft">eBook</a></li>
                        <li><a href="/rss/?cat=340" class="rss textleft">Emulation</a></li>
                        <li><a href="/rss/?cat=624" class="rss textleft">Jeu vidéo</a></li>
                        <li><a href="/rss/?cat=392" class="rss textleft">GPS</a></li>
                        <li><a href="/rss/?cat=233" class="rss textleft">Application</a></li>
                        <li><a href="/rss/?cat=210" class="rss textleft">Film/Vidéo</a></li>
                        <li><a href="/rss/?cat=456" class="rss textleft">xXx</a></li>
                    </ul>
    </li>
    <li><a href="/bonus/" title="Faire un don">Faire un don</a></li>
</ul>
    </div>
  </div>
  </div>

<div class="wrapper">

<div class="contentWrapper">
    <div class="banner728">
        <script type="text/javascript">
        document.write(unescape('%3Cscript src="' + (('https:' == document.location.protocol) ? "https://secure.pubdirecte.com/script/banniere.php?id=18982&ref=9710&secure=1" : "http://www.pubdirecte.com/script/banniere.php?id=18982&ref=9710") + '" %3E%3C/script%3E'));
        </script>
        <script type='text/javascript' src='//onclickads.net/apu.php?zoneid=15029'></script>
    </div>
</div>  <div class="contentWrapper">

<div id="left">
    <div class="banner">
        <!-- BEGIN TAG - DO NOT MODIFY -->
        <script type="text/javascript">
            /*<![CDATA[*/
            toroadv_key = "8f8e6e725871aa8fd7cd314caf841f9c";
            toroadv_channel = "";
            toroadv_code_format = "ads";
            toroadv_ads_host = "//toroadvertisingmedia.com";
            toroadv_click = "";
            toroadv_custom_params = {m: encodeURIComponent(document.title)};
            toroadv_width = "160";
            toroadv_height = "600";

            document.write("<script type='text\/javascript' src='"+(location.protocol == 'https:' ? 'https:' : 'http:') + "//toroadvertisingmedia.com\/js/show_ads_toroadv.js?pubId=4311'><\/script>");
            /*]]>*/
        </script>
        <!-- END TAG -->
    </div>

</div>
    <div class="content"><style>
    form.plainform label{
        width: 90px;
        text-align: right;
    }

    form.plainform input {
        width: 277px !important;
    }

    form.plainform input.big {
        width: 529px !important;
    }

    form.plainform label.cat {
        width: 35px;
    }

    form.plainform input[type=submit] {
        display: block;
        float: none;
        width: 150px;
        margin: 10px auto 0;
    }
</style>

<div class="block">
    <h2><span>Rechercher un Torrent</span></h2>
    <form action="/torrents/search/" id="searchform" class="plainform">
        <div>
            <div>
                <label for="search-query">Nom</label>
                <input x-webkit-speech speech type="text" class="big" id="search-name" name="name" value="divergente 2"/>
            </div>

            <div>
                <label for="search-description">Description</label>
                <input type="text" class="big" id="search-description" name="description" value=""/>

            </div>

            <div>
                <label for="search-file-name">Fichier</label>
                <input type="text" class="big" id="search-file-name" name="file" value=""/>

            </div>


            <div>
                <label for="search-owner">Uploader</label>
                <input type="text" id="search-user" name="user" value=""/>
                <label class="cat" for="search-cat">dans</label>
<select name="cat" id="search-cat">
    <option value="">-- Tous --</option>
            <option value="395" >Audio</option>
            <option value="404" >eBook</option>
            <option value="340" >Emulation</option>
            <option value="624" >Jeu vidéo</option>
            <option value="392" >GPS</option>
            <option value="233" >Application</option>
            <option value="210" selected="selected">Film/Vidéo</option>
    </select>
            </div>

            <div class="terms-wrapper">
                                    <div class="terms">
        <fieldset class="terms-type-cats">
        <legend>Cat&eacute;gorie</legend>
        <select name="subcat" id="search-subcat">
            <option value="">-- Tous --</option>
                    <option value="455" >Animation</option>
                    <option value="637" >Animation Série</option>
                    <option value="633" >Concert</option>
                    <option value="634" >Documentaire</option>
                    <option value="639" >Emission TV</option>
                    <option value="631" >Film</option>
                    <option value="433" >Série TV</option>
                    <option value="635" >Spectacle</option>
                    <option value="636" >Sport</option>
                    <option value="402" >Vidéo-clips</option>
                </select>
    </fieldset>
        </div>                            </div>
            <!--            <a href="#" class="terms-switcher">advanced</a>-->
        </div>

            <div>
                <input type="hidden" name="search">
                <input type="submit" name="submit" value="Recherche" class="btn"/>
            </div>

    </form>
    <p class="notice" align="center"><a href="https://www.t411.in/faq/#300">Cliquez ici pour connaitre les options et pr&#233;ciser votre recherche</a></p>
</div>
<div class="block">
            <div class="block">

            <h2>
            <span>
                R&#233;sultats de Recherche
                            </span>
            </h2>


<style>
    .field-mtime {
        width: 110px;
    }
</style>
<table width="100%" class="results" cellpadding="0" cellspacing="0">
        <thead>
        <tr>
                        <th width="40px" class="header "><a href="/torrents/search/?name=divergente+2&description=&file=&user=&cat=210&subcat=&search=%40name+divergente+2+&submit=Recherche&order=category&type=desc">Type</a></th>
            <th class="header "><a href="/torrents/search/?name=divergente+2&description=&file=&user=&cat=210&subcat=&search=%40name+divergente+2+&submit=Recherche&order=name&type=desc">Nom</a></th>
            <th width="45px">NFO</th>
            <th width="45px" class="header "><a href="/torrents/search/?name=divergente+2&description=&file=&user=&cat=210&subcat=&search=%40name+divergente+2+&submit=Recherche&order=comments&type=desc">Commentaires</a></th>
            <th width="60px" class="header "><a href="/torrents/search/?name=divergente+2&description=&file=&user=&cat=210&subcat=&search=%40name+divergente+2+&submit=Recherche&order=added&type=desc">Âge</a></th>
            <th width="60px" class="header "><a href="/torrents/search/?name=divergente+2&description=&file=&user=&cat=210&subcat=&search=%40name+divergente+2+&submit=Recherche&order=size&type=desc">Taille</a></th>
            <th width="45px" class="header "><a href="/torrents/search/?name=divergente+2&description=&file=&user=&cat=210&subcat=&search=%40name+divergente+2+&submit=Recherche&order=times_completed&type=desc">Compl&eacute;t&eacute;</a></th>
            <th width="45px" class="header "><a href="/torrents/search/?name=divergente+2&description=&file=&user=&cat=210&subcat=&search=%40name+divergente+2+&submit=Recherche&order=seeders&type=desc">Seeders</a></th>
            <th width="45px" class="header "><a href="/torrents/search/?name=divergente+2&description=&file=&user=&cat=210&subcat=&search=%40name+divergente+2+&submit=Recherche&order=leechers&type=desc">Leechers</a></th>
                                </tr>

    </thead>
        <tbody>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/insurgent-2015-multi-1080p-hdlight-x264-ght-divergente-2" title="Insurgent 2015 MULTi 1080p HDLight x264.GHT (Divergente 2)">Insurgent 2015 MULTi 1080p HDLight x264.GHT (Diver...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-03 00:51:16 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/ApoloWindow" title="ApoloWindow" class="profile">ApoloWindow</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>375</strong> seeders et <strong>6</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5358656" class="ajax nfo"></a>
            </td>
            <td align="center">48</td>
            <td align="center">5 mois</td>
            <td align="center">3.11 GB</td>
            <td align="center">9480</td>
            <td align="center" class="up">375</td>
            <td align="center" class="down">6</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/insurgent-2015-multi-1080p-hdlight-x265-hevc-ght-divergente-2" title="Insurgent 2015 MULTi 1080p HDLight x265 HEVC.GHT (Divergente 2)">Insurgent 2015 MULTi 1080p HDLight x265 HEVC.GHT (...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-03 01:46:45 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/ApoloWindow" title="ApoloWindow" class="profile">ApoloWindow</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>170</strong> seeders et <strong>0</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5358664" class="ajax nfo"></a>
            </td>
            <td align="center">35</td>
            <td align="center">5 mois</td>
            <td align="center">2.23 GB</td>
            <td align="center">5318</td>
            <td align="center" class="up">170</td>
            <td align="center" class="down">0</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-2-2015-french-720p-mhd-ac3-x264-romkent" title=" Divergente.2.2015.FRENCH.720p.mHD.AC3.x264-ROMKENT"> Divergente.2.2015.FRENCH.720p.mHD.AC3.x264-ROMKEN...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-05 13:55:21 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/superbus49" title="superbus49" class="profile">superbus49</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>452</strong> seeders et <strong>0</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5359843" class="ajax nfo"></a>
            </td>
            <td align="center">48</td>
            <td align="center">4 mois</td>
            <td align="center">1.6 GB</td>
            <td align="center">11165</td>
            <td align="center" class="up">452</td>
            <td align="center" class="down">0</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-2-2015-truefrench-720p-mhd-ac3-x264-romkent" title="Divergente.2.2015.TRUEFRENCH.720p.mHD.AC3.x264-ROMKENT">Divergente.2.2015.TRUEFRENCH.720p.mHD.AC3.x264-ROM...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-09 21:52:58 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/superbus49" title="superbus49" class="profile">superbus49</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>267</strong> seeders et <strong>0</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5361620" class="ajax nfo"></a>
            </td>
            <td align="center">29</td>
            <td align="center">4 mois</td>
            <td align="center">2.02 GB</td>
            <td align="center">9940</td>
            <td align="center" class="up">267</td>
            <td align="center" class="down">0</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-2-3d-h-sbs-minibdrip-1080p-vfq-eng-x264-ac3-insurgent-2015" title="Divergente 2 3D H-SbS MiniBDRip 1080p VFQ+Eng x264 AC3 (Insurgent-2015)">Divergente 2 3D H-SbS MiniBDRip 1080p VFQ+Eng x264...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-03 22:02:34 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/babeloo" title="babeloo" class="profile">babeloo</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>40</strong> seeders et <strong>0</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5359115" class="ajax nfo"></a>
            </td>
            <td align="center">12</td>
            <td align="center">4 mois</td>
            <td align="center">2.19 GB</td>
            <td align="center">884</td>
            <td align="center" class="up">40</td>
            <td align="center" class="down">0</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-2-l-insurrection-multi-truefrench-1080p-bluray-remux" title="Divergente 2 : l’insurrection Multi Truefrench 1080p Bluray Remux ">Divergente 2 : l’insurrection Multi Truefrench 108...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-12-04 10:01:22 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd>Anonymous</dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>33</strong> seeders et <strong>5</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5419919" class="ajax nfo"></a>
            </td>
            <td align="center">1</td>
            <td align="center">3 semaines</td>
            <td align="center">20.99 GB</td>
            <td align="center">122</td>
            <td align="center" class="up">33</td>
            <td align="center" class="down">5</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-2-l-insurrection-2015-3d-multi-vff-top-bottom-1080p-bluray-x264-dts-ac3-5-1-h72-3d" title="Divergente 2 l insurrection 2015 3D Multi VFF.Top Bottom.1080p.BluRay.x264.DTS.AC3.5.1-H72-3D">Divergente 2 l insurrection 2015 3D Multi VFF.Top ...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-17 15:18:31 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/halliday72" title="halliday72" class="profile">halliday72</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>58</strong> seeders et <strong>6</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5364849" class="ajax nfo"></a>
            </td>
            <td align="center">16</td>
            <td align="center">4 mois</td>
            <td align="center">11.06 GB</td>
            <td align="center">1190</td>
            <td align="center" class="up">58</td>
            <td align="center" class="down">6</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-2-2015-truefrench-720p-x264-aac-pixel" title="Divergente 2 2015 Truefrench 720p x264 AAC PIXEL">Divergente 2 2015 Truefrench 720p x264 AAC PIXEL&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-09-11 22:54:10 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/s3bb1z" title="s3bb1z" class="profile">s3bb1z</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>508</strong> seeders et <strong>6</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5376144" class="ajax nfo"></a>
            </td>
            <td align="center">18</td>
            <td align="center">3 mois</td>
            <td align="center">1.47 GB</td>
            <td align="center">5937</td>
            <td align="center" class="up">508</td>
            <td align="center" class="down">6</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-2-l-insurrection-2015-blu-ray-fra-1080p-avc-dts-hd-ma-5-1-wihd" title="Divergente 2 : L'insurrection (2015) Blu-ray FRA 1080p AVC DTS HD MA 5.1-WiHD">Divergente 2 : L'insurrection (2015) Blu-ray FRA 1...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-10-07 07:38:24 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/Phoenix10498" title="Phoenix10498" class="profile">Phoenix10498</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>29</strong> seeders et <strong>2</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5388313" class="ajax nfo"></a>
            </td>
            <td align="center">7</td>
            <td align="center">2 mois</td>
            <td align="center">35.9 GB</td>
            <td align="center">293</td>
            <td align="center" class="up">29</td>
            <td align="center" class="down">2</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-2-2015-truefrench-1080p-hdlight-x264-svr" title="Divergente 2 2015 TRUEFRENCH 1080p HDlight x264-SVR">Divergente 2 2015 TRUEFRENCH 1080p HDlight x264-SV...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-07 13:30:19 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/savior1377" title="savior1377" class="profile">savior1377</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>2273</strong> seeders et <strong>29</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5360729" class="ajax nfo"></a>
            </td>
            <td align="center">158</td>
            <td align="center">4 mois</td>
            <td align="center">2.61 GB</td>
            <td align="center">40428</td>
            <td align="center" class="up">2273</td>
            <td align="center" class="down">29</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-2-2015-truefrench-1080p-bluray-x264-svr" title="Divergente 2 2015 TRUEFRENCH 1080p BluRay x264-SVR">Divergente 2 2015 TRUEFRENCH 1080p BluRay x264-SVR&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-07 14:12:26 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/savior1377" title="savior1377" class="profile">savior1377</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>94</strong> seeders et <strong>3</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5360741" class="ajax nfo"></a>
            </td>
            <td align="center">10</td>
            <td align="center">4 mois</td>
            <td align="center">7.49 GB</td>
            <td align="center">2298</td>
            <td align="center" class="up">94</td>
            <td align="center" class="down">3</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-2-2015-multi-vf2-1080p-hdlight-x264-svr" title="Divergente 2 (2015) MULTI VF2 [1080p] HDlight x264-SVR">Divergente 2 (2015) MULTI VF2 [1080p] HDlight x264...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-07 14:22:04 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/savior1377" title="savior1377" class="profile">savior1377</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>232</strong> seeders et <strong>1</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5360751" class="ajax nfo"></a>
            </td>
            <td align="center">11</td>
            <td align="center">4 mois</td>
            <td align="center">3.52 GB</td>
            <td align="center">4520</td>
            <td align="center" class="up">232</td>
            <td align="center" class="down">1</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-2-2015-multi-truefrench-1080p-bluray-x264-svr" title="Divergente 2 2015 MULTI TRUEFRENCH 1080p BluRay x264-SVR">Divergente 2 2015 MULTI TRUEFRENCH 1080p BluRay x2...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-07 14:49:47 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/savior1377" title="savior1377" class="profile">savior1377</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>115</strong> seeders et <strong>1</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5360765" class="ajax nfo"></a>
            </td>
            <td align="center">14</td>
            <td align="center">4 mois</td>
            <td align="center">8.02 GB</td>
            <td align="center">2676</td>
            <td align="center" class="up">115</td>
            <td align="center" class="down">1</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-2-l-insurrection-insurgent-2015-3d-top-bot-truefrench-1080p-bluray-x264-dts-hd-ma-5-1-vff-jkf-3d" title="Divergente 2 L Insurrection (Insurgent) 2015 3D TOP-BOT TrueFrench 1080p Bluray X264 DTS-HD MA 5.1 VFF-JKF-3D">Divergente 2 L Insurrection (Insurgent) 2015 3D TO...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-09-21 08:31:37 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/nanomagicien" title="nanomagicien" class="profile">nanomagicien</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>31</strong> seeders et <strong>1</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5380636" class="ajax nfo"></a>
            </td>
            <td align="center">10</td>
            <td align="center">3 mois</td>
            <td align="center">8.85 GB</td>
            <td align="center">343</td>
            <td align="center" class="up">31</td>
            <td align="center" class="down">1</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/insurgent-2015-truefrench-bdrip-xvid-avitech-divergente-2" title="Insurgent 2015 TRUEFRENCH BDRiP XViD-AViTECH (Divergente 2)">Insurgent 2015 TRUEFRENCH BDRiP XViD-AViTECH (Dive...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-07 14:06:25 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/savior1377" title="savior1377" class="profile">savior1377</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>317</strong> seeders et <strong>0</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5360739" class="ajax nfo"></a>
            </td>
            <td align="center">15</td>
            <td align="center">4 mois</td>
            <td align="center">1.37 GB</td>
            <td align="center">5869</td>
            <td align="center" class="up">317</td>
            <td align="center" class="down">0</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/insurgent-2015-truefrench-dvdrip-xvid-glups-divergente-2" title="Insurgent 2015 TRUEFRENCH DVDRip XViD-GLUPS (Divergente 2)">Insurgent 2015 TRUEFRENCH DVDRip XViD-GLUPS (Diver...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-07 14:46:02 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/savior1377" title="savior1377" class="profile">savior1377</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>219</strong> seeders et <strong>3</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5360762" class="ajax nfo"></a>
            </td>
            <td align="center">16</td>
            <td align="center">4 mois</td>
            <td align="center">1.37 GB</td>
            <td align="center">5042</td>
            <td align="center" class="up">219</td>
            <td align="center" class="down">3</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/insurgent-2015-truefrench-dvdrip-xvid-ac3-glups-divergente-2" title="Insurgent 2015 TRUEFRENCH DVDRip XviD AC3-GLUPS (Divergente 2)">Insurgent 2015 TRUEFRENCH DVDRip XviD AC3-GLUPS (D...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-07 17:27:35 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/savior1377" title="savior1377" class="profile">savior1377</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>61</strong> seeders et <strong>0</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5360831" class="ajax nfo"></a>
            </td>
            <td align="center">8</td>
            <td align="center">4 mois</td>
            <td align="center">2.05 GB</td>
            <td align="center">1279</td>
            <td align="center" class="up">61</td>
            <td align="center" class="down">0</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-2-2015-french-1080p-bluray-x264-svr" title="Divergente 2  (2015) FRENCH 1080p BluRay x264-SVR">Divergente 2  (2015) FRENCH 1080p BluRay x264-SVR&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-08-02 22:08:07 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/savior1377" title="savior1377" class="profile">savior1377</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>54</strong> seeders et <strong>0</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5358613" class="ajax nfo"></a>
            </td>
            <td align="center">24</td>
            <td align="center">5 mois</td>
            <td align="center">7.49 GB</td>
            <td align="center">2662</td>
            <td align="center" class="up">54</td>
            <td align="center" class="down">0</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/insurgent-2015-multi-truefrench-1080p-bluray-x264-ulshd-divergente-2" title="Insurgent.2015.MULTi.TRUEFRENCH.1080p.BluRay.x264-ULSHD  (Divergente 2)">Insurgent.2015.MULTi.TRUEFRENCH.1080p.BluRay.x264-...&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-10-08 22:04:59 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd>Anonymous</dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>100</strong> seeders et <strong>2</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5389148" class="ajax nfo"></a>
            </td>
            <td align="center">7</td>
            <td align="center">2 mois</td>
            <td align="center">9.83 GB</td>
            <td align="center">566</td>
            <td align="center" class="up">100</td>
            <td align="center" class="down">2</td>
                                </tr>
                <tr>
                        <td valign="center">
                                <a href="/torrents/search/?subcat=631">
                    <i class="categories-icons category-spline-video-movie"></i>
                </a>
                            </td>
            <td valign="center">
                <a href="//www.t411.in/torrents/divergente-edition-collector-les-2-films-multi-iso" title="DIVERGENTE EDITION COLLECTOR LES 2 FILMS MULTI ISO">DIVERGENTE EDITION COLLECTOR LES 2 FILMS MULTI ISO&nbsp;<span class="up">(A)</span></a>
                <a href="#" class="switcher alignright"></a>
                                    <!-- body -->
<a href="http://www.terraclicks.com/watch?key=4e972a15b3923742bf5c20ca0045270d" target="_blank"><img src="/themes/blue/images/down.png" alt="Download"></a>
                                                <dl>
                    <dt>Ajout&#233; le:</dt>
                    <dd>2015-09-29 21:34:33 (+00:00)</dd>
                    <dt>Ajout&#233; par:</dt>
                    <dd><a href="/users/profile/marcetlu59" title="marcetlu59" class="profile">marcetlu59</a></dd>
                    <dt>Status:</dt>
                    <dd><strong class="up">BON</strong> &mdash; Ce torrent est actif (<strong>23</strong> seeders et <strong>5</strong> leechers) et devrait &#281;tre t&#233;l&#233;charg&#233; rapidement</dd>
                </dl>
            </td>
            <td>
                <a href="/torrents/nfo/?id=5384792" class="ajax nfo"></a>
            </td>
            <td align="center">1</td>
            <td align="center">3 mois</td>
            <td align="center">13.33 GB</td>
            <td align="center">155</td>
            <td align="center" class="up">23</td>
            <td align="center" class="down">5</td>
                                </tr>
            </tbody>
        <tfoot>
        <tr>
            <td colspan="9" class="textcenter">
            <div class="pagebar">
</div>            </td>
        </tr>
    </tfoot>
    </table>                    </div>
        <script type="text/javascript">
            function clearField() {
                $('#bookmarkName').val('');
            }
        </script>
    </div>
<script type="text/javascript">
    $(function(){
        $('.terms-switcher').click(function(){
            $('.terms-wrapper').slideToggle();
            return false;
        });
        $('#searchform #search-cat').change(function(){
            var cat = $(this).val();
            $('.terms-wrapper').load('/torrents/terms/?cat='+cat);
        });
        $('#searchform').delegate('#search-subcat', 'change', function(){
            var cat = $(this).val();
            $('.terms-wrapper').load('/torrents/terms/?subcat='+cat);
        });

        $('form.plainform').submit(function(){
            var allowed = ['name','description','file','user'];
            var form = this;

            var query = '';

            $(allowed).each(function(key, value){
                if (form[value] && form[value].value) {
                    query = query + '@' + value + ' ' + form[value].value + ' ';
                }
            });

            form['search'].value = query;
        })
    });
</script>                </div><!-- content -->


<div id="right">
<!--
    <div class="banner">
        <script type="text/javascript">
            document.write(unescape('%3Cscript src="' + (('https:' == document.location.protocol) ? "https://secure.pubdirecte.com/script/banniere.php?id=36995&ref=9710&secure=1" : "http://www.pubdirecte.com/script/banniere.php?id=36995&ref=9710") + '" %3E%3C/script%3E'));
        </script>
   </div>
-->
<!-- Place the div element where you want to display ads -->
<div id="myec_7214559_1" class="myec" data-ref='eyJpZF9zaXRlIjoiMSIsInByb2dfb24iOiI1fDZ8OHwyM3wyNXw0OXw1OSIsImlkX3Bvc2l0aW9uIjoiIiwidHlwZV9zaXRlIjoiNiIsInRyYWNrZXIxIjoiIiwidHJhY2tlcjIiOiIiLCJjYXRfb24iOiIiLCJwZWdpIjoiMiIsInRhcmdldCI6ImJsYW5rIiwicG9wX3VuZGVyIjoiIiwibGciOiJmciIsIm5zZnciOiIwIiwiX3dpZHRoIjoiMTYwIiwiX2hlaWdodCI6IjYwMCIsIm0iOiIiLCJkIjoiMCIsInByb3RvIjoiaHR0cCIsImRvbWFpbl9lYyI6InBybS5ldXJvcGFjYXNoLmNvbSJ9'></div>

<!-- Place this script only once per page just before the closing body tag -->
<script type="text/javascript">
	if (typeof multitagec === "undefined" && document.getElementsByClassName("myec").length) {
		multitagec = true;
		var script = document.createElement("script");
		script.src = "http://prm.clicks4ads.com/js/ec_connectorDelivery.js";
		document.body.appendChild(script);
	}
</script>
</div>
    </div>

<div class="contentWrapper">
    <div class="banner728">

        <script type="text/javascript">
            document.write(unescape('%3Cscript src="' + (('https:' == document.location.protocol) ? "https://secure.pubdirecte.com/script/banniere.php?id=20761&ref=9710&secure=1" : "http://www.pubdirecte.com/script/banniere.php?id=20761&ref=9710") + '" %3E%3C/script%3E'));
        </script>

    </div>
    <div class="banner728">

        <script type="text/javascript">
            document.write(unescape('%3Cscript src="' + (('https:' == document.location.protocol) ? "https://secure.pubdirecte.com/script/pop.php?id=21819&ref=9710&secure=1" : "http://www.pubdirecte.com/script/pop.php?id=21819&ref=9710") + '" %3E%3C/script%3E'));
        </script>

    </div>
</div>
<script data-cfasync="false" type="text/javascript" src="http://www.adnetworkperformance.com/a/display.php?r=443609"></script>

<!--europacash-->
<!-- Place the div element where you want to display ads -->
<div id="myec_7214559_3" class="myec" data-tt="38" data-ref='eyJpZF9zaXRlIjoiMSIsInByb2dfb24iOiI1fDZ8OHwxN3wyM3wyNXw0OXw1N3w1OSIsInR5cGVfc2l0ZSI6IjYiLCJ0cmFja2VyMSI6IiIsInRyYWNrZXIyIjoiIiwiY2F0X29uIjoiIiwibnNmdyI6IjAiLCJwZWdpIjoiMiIsImxnIjoiZnIiLCJtIjoiIiwiZCI6IjAiLCJwcm90byI6Imh0dHAiLCJkb21haW5fZWMiOiJwcm0uZXVyb3BhY2FzaC5jb20iLCJjYXBwaW5nIjoiMSJ9'></div>

<!-- Place this script only once per page just before the closing body tag -->
<script type="text/javascript">
	if (typeof multitagec === "undefined" && document.getElementsByClassName("myec").length) {
		multitagec = true;
		var script = document.createElement("script");
		script.src = "http://prm.clicks4ads.com/js/ec_connectorDelivery.js";
		document.body.appendChild(script);
	}
</script>    <div class="spacer">&nbsp;</div>

    <div class="footer">
        <p>
        <a href="/" title="Torrent411">t411.in</a> (Version 2.3) - Aucun droit r&#233;serv&#233;!
        <br/>
        Page g&#233;n&#233;r&#233;e en 0.053959 secondes        </p>
        <div class="logos"></div>
    </div>
</div>
<!-- overlay window -->
<div id="info" class="overlay black">
    <div class="inner">Loading...</div>
</div>
</body>
</html>
<!-- start cache: 12:18:50 -->
<!-- resources: 1 349 936 bytes / 0.041496 sec -->
'''
import bs4
from ast import literal_eval

soup = bs4.BeautifulSoup(data)
links = soup.select('tr')
titles = []
for link in links:
    td = link.select("td")
    if len(td) > 1:
        titles.append(link.select("td")[1].a["title"])

links = soup.select("tr td a.nfo")
for a in links:
    print a["href"].replace("/torrents/nfo/?id=", "/users/login/?returnto=/t/")

# import requests
#
# url = "http://www.elitetorrent.net/categoria/1/estrenos/modo:listado/pag:1"
# browser = requests.Session()
# page = "1"
# import bs4
#
# response = browser.get( url + page)
# soup = bs4.BeautifulSoup(response.text)
# links = soup.select("a.nombre")
# for link in links:
#     print link.get("title", ""), link["href"]

# import re
#
# datos = re.search("var datos =(.*?);", data, re.DOTALL).group(1).replace("{", "").replace("}", "")
# params = {}
# for item in datos.split("\n"):
#     if item.strip() != "":
#         key, value = item.strip()[:-1].split(':')
#         params[key] = value.replace("'", "")
# #settings.debug(params)
# opciones = re.search("var options =(.*?);", data, re.DOTALL).group(1).replace("{", "").replace("}", "") + ": ''"
# params1 = {}
# for item in opciones.split("\n"):
#     if item.strip() != "":
#         key, value = item.strip()[:-1].split(':')
#         params1[key] = value.replace("'", "")
# #settings.debug(params1)
# urlPage = re.search('url: "(.*?)"', data).group(1)
