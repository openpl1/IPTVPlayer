﻿# -*- coding: utf-8 -*-
#############################################################
# Yonn1981 https://github.com/Yonn1981/Repo
#############################################################

import re

from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import (
    addon, siteManager)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.gui.gui import \
    cGui
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.gui.hoster import \
    cHosterGui
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.inputParameterHandler import \
    cInputParameterHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.outputParameterHandler import \
    cOutputParameterHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser

SITE_IDENTIFIER = 'yalladrama'
SITE_NAME = 'YallaDrama'
SITE_DESC = 'arabic vod'

UA = 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.48 Mobile Safari/537.36'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

MOVIE_EN = (URL_MAIN + '/category.php?cat=foreign-moives', 'showMovies')
RAMADAN_SERIES = (URL_MAIN + '/category.php?cat=ramadan-2023', 'showSeries')
MOVIE_AR = (URL_MAIN + '/category.php?cat=arabic-moives', 'showMovies')
MOVIE_TURK = (URL_MAIN + '/category102.php?cat=turkish-movies2023', 'showMovies')
MOVIE_HI = (URL_MAIN + '/category.php?cat=indian-moives', 'showMovies')
SERIE_AR = (URL_MAIN + '/category.php?cat=arabic-series1', 'showSeries')
SERIE_EN = (URL_MAIN + '/category.php?cat=foreign-series', 'showSeries')
SERIE_TR = (URL_MAIN + '/category.php?cat=turkish-series1', 'showSeries')
SERIE_TR_AR = (URL_MAIN + '/category.php?cat=turkish-series-modblj1', 'showSeries')
SERIE_ASIA = (URL_MAIN + '/category.php?cat=asian-series', 'showSeries')
SERIE_HEND = (URL_MAIN + '/category.php?cat=indian-series1', 'showSeries')
SERIE_DUBBED = (URL_MAIN + '/category.php?cat=modblj-series1', 'showSeries')

ANIM_NEWS = (URL_MAIN + '/category.php?cat=moslslat-animeanime-series', 'showSeries')
REPLAYTV_PLAY = (URL_MAIN + '/category.php?cat=masrahiaat', 'showSeries')

URL_SEARCH = (URL_MAIN + '/search.php?keywords=', 'showSeries')
URL_SEARCH_MOVIES = (URL_MAIN + '/search.php?keywords=', 'showMovies')
URL_SEARCH_SERIES = (URL_MAIN + '/search.php?keywords=', 'showSeries')
FUNCTION_SEARCH = 'showSearch'

def load():
    oGui = cGui()
    addons = addon()
    oOutputParameterHandler = cOutputParameterHandler()

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30076)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', addons.VSlang(30078), 'search.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSeriesSearch', addons.VSlang(30079), 'search.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30120)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', RAMADAN_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'رمضان', 'rmdn.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أجنبية', 'agnab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HI[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام هندية', 'hend.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_TURK[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام تركية', 'turk.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام عربية', 'arab.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30121)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', SERIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات عربية', 'arab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أجنبية', 'agnab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_ASIA[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أسيوية', 'asia.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_TR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات تركية', 'turk.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_TR_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات تركية مدبلجة', 'turk.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_HEND[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات هندية', 'hend.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_DUBBED[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات مدبلجة', 'mdbljt.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', ANIM_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات إنمي', 'anime.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30350)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', REPLAYTV_PLAY[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسرحيات', 'msrh.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + '/category.php?cat=3ramdan-2022')
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'رمضان 2022', 'rmdn.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showSeriesSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/search.php?keywords='+sSearchText
        showSeries(sUrl)
        oGui.setEndOfDirectory()
        return

def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/search.php?keywords='+sSearchText+'&video-id='
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return

def showMovies(sSearch = ''):
    oGui = cGui()
    oParser = cParser()

    if sSearch:
        sUrl = sSearch+'&video-id='
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addHeaderEntry('User-Agent', UA)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="thumbnail">.+?<a href="(.+?)".+?title="(.+?)".+?data-echo="(.+?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            if " لم يتم العثور على ما يطابق بحثك"  in sHtmlContent:
                continue

            if "مسلسل"  in aEntry[1]:
                continue

            if "حلقة"  in aEntry[1]:
                continue

            sTitle = aEntry[1].replace("مشاهدة","").replace("كامل","").replace("مشاهده","").replace("مترجم","").replace("فيلم","").replace("اونلاين","").replace("اون لاين","").replace("برنامج","").replace("WEB-DL","").replace("BRRip","").replace("720p","").replace("HD-TC","").replace("HDRip","").replace("HD-CAM","").replace("DVDRip","").replace("BluRay","").replace("1080p","").replace("WEBRip","").replace("WEB-dl","").replace("4K","").replace("All","").replace("BDRip","").replace("HDCAM","").replace("HDTC","").replace("HDTV","").replace("HD","").replace("720","").replace("HDCam","").replace("Full HD","").replace("1080","").replace("HC","").replace("Web-dl","").replace("انمي","")

            siteUrl = aEntry[0].replace("watch.php","view.php")
            sDesc = ""
            sThumb = aEntry[2]
            sYear = ''
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear,'')


            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sDesc', sDesc)

            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()

def showSeries(sSearch = ''):
    oGui = cGui()
    oParser = cParser()

    if sSearch:
        sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')



    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addHeaderEntry('User-Agent', UA)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="thumbnail">.+?<a href="(.+?)".+?title="(.+?)".+?data-echo="(.+?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    itemList = []
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            if 'فيلم' in aEntry[1]:
                continue

            siteUrl = aEntry[0]

            sTitle = aEntry[1].replace("كامل HD","").replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("مترجم","").replace("مشاهده","").replace("برنامج","").replace("مترجمة","").replace("فيلم","").replace("اون لاين","").replace("WEB-DL","").replace("BRRip","").replace("720p","").replace("HD-TC","").replace("HDRip","").replace("HD-CAM","").replace("DVDRip","").replace("BluRay","").replace("1080p","").replace("WEBRip","").replace("WEB-dl","").replace("مترجم ","").replace("مشاهدة وتحميل","").replace("اون لاين","")
            sThumb = aEntry[2]
            sDesc = ''
            sName = sTitle.split('الحلقة')[0].split('الموسم ')[0].split('موسم ')[0]
            sTitle = sName.replace("مترجم","").replace("مترجمة","").replace(" الحادي عشر","11").replace(" الثاني عشر","12").replace(" الثالث عشر","13").replace(" الرابع عشر","14").replace(" الخامس عشر","15").replace(" السادس عشر","16").replace(" السابع عشر","17").replace(" الثامن عشر","18").replace(" التاسع عشر","19").replace(" العشرون","20").replace(" الحادي و العشرون","21").replace(" الثاني و العشرون","22").replace(" الثالث و العشرون","23").replace(" الرابع والعشرون","24").replace(" الخامس و العشرون","25").replace(" السادس والعشرون","26").replace(" السابع والعشرون","27").replace(" الثامن والعشرون","28").replace(" التاسع والعشرون","29").replace(" الثلاثون","30").replace(" الحادي و الثلاثون","31").replace(" الثاني والثلاثون","32").replace(" الاول","1").replace(" الثاني","2").replace(" الثانى","2").replace(" الثالث","3").replace(" الرابع","4").replace(" الخامس","5").replace(" السادس","6").replace(" السابع","7").replace(" الثامن","8").replace(" التاسع","9").replace(" العاشر","10")

            sYear = ''
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear,'')

            if sTitle not in itemList:
                itemList.append(sTitle)
                oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                oOutputParameterHandler.addParameter('sYear', sYear)
                oOutputParameterHandler.addParameter('sThumb', sThumb)

                oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    if not sSearch:
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()

def __checkForNextPage(sHtmlContent):
    oParser = cParser()

    sPattern = '<li class="active"><a href="#".+?<li class><a href="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] :

        return URL_MAIN+aResult[1][0]

    return False

def showEpisodes():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addHeaderEntry('User-Agent', UA)
    sHtmlContent = oRequestHandler.request()

    sStart = '<div class="SeasonsEpisodesMain">'
    sEnd = '<div id="content-main" class="container-fluid">'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)

    sPattern = '<div.+?id="([^"]+)".+?class="tabcontent">(.+?)</ul></div>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] :
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            sSeason = "S"+aEntry[0].replace("Season","")
            sHtmlContent = aEntry[1]

            sPattern = 'title=["\']([^"\']+)["\'] href=["\']([^"\']+)["\']><li>(.+?)</li>'
            aResult = oParser.parse(sHtmlContent, sPattern)
            if aResult[0] :
                oOutputParameterHandler = cOutputParameterHandler()
                for aEntry in aResult[1]:

                    siteUrl = URL_MAIN +aEntry[1]
                    siteUrl = siteUrl.replace("watch.php","view.php")
                    Ss = sSeason+' '
                    Eps = aEntry[2].replace("الحلقة ","")
                    Eps = re.findall(r'\d+', Eps)[0]
                    sTitle = sMovieTitle+Ss+" E"+Eps
                    sThumb = sThumb
                    sDesc = ""

                    oOutputParameterHandler.addParameter('siteUrl',siteUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)
                    oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, '', oOutputParameterHandler)


    oGui.setEndOfDirectory()

def showHosters():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')


    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addHeaderEntry('User-Agent', UA)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<a href="(.+?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        URL_MAIN = aResult[1][0]


    sPattern = 'data-code="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] :
        for aEntry in aResult[1]:
            sHosterUrl = aEntry
            sTitle =  ""
            if sHosterUrl.startswith('//'):
                sHosterUrl = 'http:' + sHosterUrl
            if 'userload' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'mystream' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()