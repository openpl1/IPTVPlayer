﻿# -*- coding: utf-8 -*-
# zombi https://github.com/zombiB/zombi-addons/

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

SITE_IDENTIFIER = 'asiaarabs'
SITE_NAME = 'Asia4arabs'
SITE_DESC = 'arabic vod'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

MOVIE_ASIAN = (URL_MAIN + '/search/label/%D8%A3%D9%81%D9%84%D8%A7%D9%85', 'showMovies')
SERIE_ASIA = (URL_MAIN + '/search/label/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA', 'showSeries')


URL_SEARCH = (URL_MAIN + '/search?q=', 'showMovies')
URL_SEARCH_SERIES = (URL_MAIN + '/search?q=', 'showSeries')
URL_SEARCH_MOVIES = (URL_MAIN + '/search?q=', 'showMovies')
FUNCTION_SEARCH = 'showMovies'

def load():
    oGui = cGui()
    addons = addon()
    oOutputParameterHandler = cOutputParameterHandler()

    oGui.addText(SITE_IDENTIFIER,'[COLOR olive]-----●★| '+ addons.VSlang(30076)+' |★●-----[/COLOR]')

    oGui.addDir(SITE_IDENTIFIER, 'showSearch', addons.VSlang(30078), 'search.png', oOutputParameterHandler)


    oGui.addDir(SITE_IDENTIFIER, 'showSearchSeries', addons.VSlang(30079), 'search.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER,'[COLOR olive]-----●★| '+ addons.VSlang(30120)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_ASIAN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام', 'film.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER,'[COLOR olive]-----●★| '+ addons.VSlang(30121)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', SERIE_ASIA[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات', 'mslsl.png', oOutputParameterHandler)


    oGui.setEndOfDirectory()

def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/search?q='+sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return

def showSearchSeries():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/search?q='+sSearchText
        showSeries(sUrl)
        oGui.setEndOfDirectory()
        return

def showMovies(sSearch = ''):
    oGui = cGui()
    oParser = cParser()

    if sSearch:
        sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = "<a class='Img-Holder thumb' href='([^<]+)' title='([^<]+)'>.+?rel='tag'>(.+?)</span>.+?class='post-thumb' data-src='([^<]+)' height"
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            if "مترجم" not in aEntry[1]:
                continue
            if "مسلسل" in aEntry[1]:
                continue

            sTitle = aEntry[1].replace("مترجمة","").replace("مشاهدة","").replace("مسلسل","").replace("انمي","").replace("انمى","").replace("مترجم","").replace("فيلم","").replace("اون لاين","").replace("WEB-DL","").replace("BRRip","").replace("720p","").replace("HD-TC","").replace("HDRip","").replace("HD-CAM","").replace("DVDRip","").replace("BluRay","").replace("1080p","").replace("WEBRip","").replace("WEB-dl","").replace("كامل","").replace("مشاهدة وتحميل","").replace("اون لاين","").replace("جميع حلقات","").replace("والأخيرة","").replace("والاخيرة","").replace("الأخيرة","").replace("الاخيرة","").replace("والاخيرة","")
            siteUrl = aEntry[0]
            sThumb = aEntry[3]
            sDesc = aEntry[2]
            sYear = ''
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear,'')


            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)

            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    sPattern = "href='([^<]+)' id='.+?' title='(.+?)'>"
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            if "youtube" in aEntry[1]:
                continue

            sTitle = aEntry[1]

            sTitle =  "PAGE " + sTitle
            sTitle =   '[COLOR red]'+sTitle+'[/COLOR]'
            siteUrl = aEntry[0]


            oOutputParameterHandler.addParameter('siteUrl',siteUrl)

            oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, '', oOutputParameterHandler)

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
    sHtmlContent = oRequestHandler.request()

    sPattern = "<a class='Img-Holder thumb' href='([^<]+)' title='([^<]+)'>.+?rel='tag'>(.+?)</span>.+?class='post-thumb' data-src='([^<]+)' height"
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            if "مترجم" not in aEntry[1]:
                continue
            if "فيلم" in aEntry[1]:
                continue

            sTitle = aEntry[1].replace("مشاهدة","").replace("مترجم","").replace("المسلسل الباكستاني","").replace("مسلسل باكستاني","").replace("مسلسل","").replace("انمي","").replace("مترجمة","").replace("مدبلج للعربية","مدبلج").replace("فيلم","").replace("والأخيرة","").replace("والاخيرة","").replace("اون لاين","").replace("WEB-DL","").replace("BRRip","").replace("720p","").replace("HD-TC","").replace("HDRip","").replace("HD-CAM","").replace("DVDRip","").replace("BluRay","").replace("1080p","").replace("WEBRip","").replace("WEB-dl","").replace("4K","").replace("All","").replace("BDRip","").replace("HDCAM","").replace("HDTC","").replace("HDTV","").replace("HD","").replace("720","").replace("HDCam","").replace("Full HD","").replace("1080","").replace("HC","").replace("Web-dl","").replace("الموسم الحادي عشر","S11").replace("الموسم الثاني عشر","S12").replace("الموسم الثالث عشر","S13").replace("الموسم الرابع عشر","S14").replace("الموسم الخامس عشر","S15").replace("الموسم السادس عشر","S16").replace("الموسم السابع عشر","S17").replace("الموسم الثامن عشر","S18").replace("الموسم التاسع عشر","S19").replace("الموسم العشرون","S20").replace("الموسم الحادي و العشرون","S21").replace("الموسم الثاني و العشرون","S22").replace("الموسم الثالث و العشرون","S23").replace("الموسم الرابع والعشرون","S24").replace("الموسم الخامس و العشرون","S25").replace("الموسم السادس والعشرون","S26").replace("الموسم السابع والعشرون","S27").replace("الموسم الثامن والعشرون","S28").replace("الموسم التاسع والعشرون","S29").replace("الموسم الثلاثون","S30").replace("الموسم الحادي و الثلاثون","S31").replace("الموسم الثاني والثلاثون","S32").replace("الموسم الاول","S1").replace("الموسم الثاني","S2").replace("الموسم الثالث","S3").replace("الموسم الثالث","S3").replace("الموسم الرابع","S4").replace("الموسم الخامس","S5").replace("الموسم السادس","S6").replace("الموسم السابع","S7").replace("الموسم الثامن","S8").replace("الموسم التاسع","S9").replace("الموسم العاشر","S10").replace("الموسم","S").replace("S ","S").replace("موسم","S").replace("S ","S")
            siteUrl = aEntry[0]
            sThumb = aEntry[3]
            sDesc = aEntry[2]


            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    sPattern = "href='([^<]+)' id='.+?' title='(.+?)'>"
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            if "youtube" in aEntry[1]:
                continue

            sTitle = aEntry[1]

            sTitle =  "PAGE " + sTitle
            sTitle =   '[COLOR red]'+sTitle+'[/COLOR]'
            siteUrl = aEntry[0]


            oOutputParameterHandler.addParameter('siteUrl',siteUrl)

            oGui.addDir(SITE_IDENTIFIER, 'showSeries', sTitle, '', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()


def showEpisodes():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern =  '<a href="(https://asia4arabs-fs.+?)"'
    aResult = oParser.parse(sHtmlContent,sPattern)
    if aResult[0]:
        m3url =  aResult[1][0]
        oRequest = cRequestHandler(m3url)
        sHtmlContent = oRequest.request()
    sPattern =  '<a href="(https://www.asia4arabs.co.+?)" target'
    aResult = oParser.parse(sHtmlContent,sPattern)
    if aResult[0]:
        m3url =  aResult[1][0]
        oRequest = cRequestHandler(m3url)
        sHtmlContent = oRequest.request()

    sPattern = 'iframes([^<]+)=.+?width="100%" height="400" src="(.+?)" frameborder='
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:

            url = aEntry[1]
            sTitle = "E"+aEntry[0].replace(" ","").replace("]","").replace("[","").replace(" = {};","").replace(" iframes","").replace("iframes","").replace("={};","")
            if url.startswith('//'):
                url = 'http:' + url

            sHosterUrl = url
            if "youtube" in sHosterUrl:
                continue
            if 'userload' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'mystream' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                sTitle = sTitle+sMovieTitle
                oHoster.setDisplayName(sTitle)
                oHoster.setFileName(sTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    sPattern = '<a href="([^<]+)" target="_blank">(.+?)</a>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:

            url = aEntry[0]
            sTitle = aEntry[1].replace("الحلقة "," E")
            if url.startswith('//'):
                url = 'http:' + url

            sHosterUrl = url
            if "youtube" in sHosterUrl:
                continue
            if 'userload' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'mystream' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                sTitle = sTitle+sMovieTitle
                oHoster.setDisplayName(sTitle)
                oHoster.setFileName(sTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    sPattern = '<td><a href=["\']([^"\']+)["\']\s*target="iframe_a">(.+?)</a>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:

            url = aEntry[0]
            sTitle = aEntry[1].replace("Episode "," E").replace("Episod "," E")
            if url.startswith('//'):
                url = 'http:' + url

            sHosterUrl = url
            if "youtube" in sHosterUrl:
                continue
            if "google" in sHosterUrl:
                continue
            if "LINK0" in sHosterUrl:
                continue
            if 'userload' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'moshahda' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'mystream' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                sTitle = sTitle+sMovieTitle
                oHoster.setDisplayName(sTitle)
                oHoster.setFileName(sTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    sPattern = '>الحلقة([^<]+)</span></span></h4><iframe allowfullscreen.+?src="(.+?)" width'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            url = aEntry[1]
            sTitle = "E"+aEntry[0].replace(" ","").replace("]","").replace("[","").replace(" = {};","").replace(" iframes","").replace("iframes","").replace("={};","")
            if url.startswith('//'):
                url = 'http:' + url

            sHosterUrl = url
            if "youtube" in sHosterUrl:
                continue
            if 'userload' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'mystream' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                sTitle = sTitle+sMovieTitle
                oHoster.setDisplayName(sTitle)
                oHoster.setFileName(sTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)


    oGui.setEndOfDirectory()

def __checkForNextPage(sHtmlContent):
    oParser = cParser()

    sPattern = "href='([^<]+)' id='.+?' title='NextUrl'>"
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        return aResult[1][0]

    return False

def showHosters():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<iframe.+?src="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:

            url = str(aEntry)
            sTitle = " "
            if url.startswith('//'):
                url = 'http:' + url

            sHosterUrl = url
            if "youtube" in sHosterUrl:
                sTitle = "-trailer"

            if "blogger" in sHosterUrl:
                continue
            if ".jpg" in sHosterUrl:
                continue
            if ".jpeg" in sHosterUrl:
                continue
            if 'userload' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'mystream' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                sDisplayTitle = sMovieTitle+sTitle
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)


    sPattern = '<a href="([^<]+)" target="'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:

            url = str(aEntry)
            sTitle = " "
            if url.startswith('//'):
                url = 'http:' + url

            sHosterUrl = url
            if "youtube" in sHosterUrl:
                sTitle = "-trailer"

            if "blogger" in sHosterUrl:
                continue
            if ".jpg" in sHosterUrl:
                continue
            if ".jpeg" in sHosterUrl:
                continue
            if 'userload' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            if 'mystream' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                sDisplayTitle = sMovieTitle+sTitle
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()