﻿# -*- coding: utf-8 -*-
# zombi https://github.com/zombiB/zombi-addons/

import base64

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

SITE_IDENTIFIER = 'tvfun'
SITE_NAME = 'Tvfun'
SITE_DESC = 'arabic vod'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

RAMADAN_SERIES = (URL_MAIN + '/ts/mosalsalat-ramadan-2023/', 'showSeries')
SERIE_TR = (URL_MAIN + '/cat/mosalsalat-torkia/', 'showSeries')
SERIE_DUBBED = (URL_MAIN + '/ts/mosalsalat-modablaja/', 'showSeries')
SERIE_SUBED = (URL_MAIN + '/cat/mosalsalat-motarjama/', 'showSeries')
SERIE_HEND = (URL_MAIN + '/cat/mosalsalat-hindia/', 'showSeries')
SERIE_AR = (URL_MAIN + '/cat/mosalsalat-3arabia/', 'showSeries')

SERIE_KR = (URL_MAIN + '/cat/mosalsalat-korea/', 'showSeries')
SERIE_LATIN = (URL_MAIN + '/cat/mosalsalat-latinia/', 'showSeries')
REPLAYTV_NEWS = (URL_MAIN + '/cat/zee-alwan/', 'showSeries')

URL_SEARCH = (URL_MAIN + '/q/', 'showSeriesSearch')
FUNCTION_SEARCH = 'showSeriesSearch'


def load():
    oGui = cGui()
    addons = addon()
    oOutputParameterHandler = cOutputParameterHandler()

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30076)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', addons.VSlang(30079), 'search.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30121)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', RAMADAN_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات رمضان', 'rmdn.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات عربية', 'arab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_KR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أسيوية', 'asia.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_TR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات تركية', 'turk.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_HEND[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات هندية', 'hend.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_LATIN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات لاتنية', 'latin.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_DUBBED[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات مدبلجة', 'mdbljt.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + '/ts/mosalsalat-motarjama/')
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات مترجمة', 'mslsl.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + '/ts/zee-alwan/')
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'زي الوان', 'mslsl.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', 'https://m.tvfun.me/cat/mosalsalat-maghribia/')
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات مغربية', 'mslsl.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/q/' + sSearchText

        showSeriesSearch(sUrl)
        oGui.setEndOfDirectory()
        return


def showSeries(sSearch=''):
    oGui = cGui()
    oParser = cParser()

    if sSearch:
        sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="thumb"><div class="serie-thumb"><a href="(.+?)" title="(.+?)"><img.+?src="(.+?)" alt='
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:

            sTitle = aEntry[1].replace("مشاهدة وتحميل", "").replace("اون لاين", "").replace("مترجمة", "").replace("مترجم", "")
            siteUrl = aEntry[0]
            if siteUrl.startswith('//'):
                siteUrl = 'http:' + siteUrl
            if URL_MAIN not in siteUrl:
                siteUrl = URL_MAIN + siteUrl
            sThumb = aEntry[2]
            sDesc = ''
            sYear = ''

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sDesc', sDesc)

            oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    if not sSearch:
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()


def showSeriesSearch(sSearch=''):
    oGui = cGui()
    oParser = cParser()

    if sSearch:
        sUrl = sSearch+'/'
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="thumb"><div class="video-thumb"><a href="(.+?)" title="(.+?)"><img.+?src="(.+?)" alt'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:

            sTitle = aEntry[1].replace("الحلقة ", " E").replace("حلقة ", " E").replace("مشاهدة وتحميل", "").replace("اون لاين", "").replace("والاخيرة", "")
            siteUrl = aEntry[0]
            sThumb = aEntry[2]
            if siteUrl.startswith('//'):
                siteUrl = 'http:' + siteUrl
            if URL_MAIN not in siteUrl:
                siteUrl = URL_MAIN + siteUrl

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oParser = cParser()

    sPattern = '<ul class="pagination">(.+?)div id="footer">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        sHtmlContent3 = aResult[1][0]

        sPattern = '<a class=\"current\" href=\"([^<]+)\">([^<]+)</a>'
        CurrentPage = oParser.parse(sHtmlContent3, sPattern)

        if CurrentPage[0]:

            sPattern = '<li><a href="([^<]+)">([^<]+)</a></li>'
            aResult = oParser.parse(sHtmlContent3, sPattern)
            if aResult[0]:
                for aEntry in aResult[1]:

                    if int(aEntry[1]) - int(CurrentPage[1][0][1]) == 1:
                        return aEntry[0]
        else:
            sPattern = '<li><a href="([^<]+)">2</a></li>'
            aResult = oParser.parse(sHtmlContent3, sPattern)
            return aResult[1][0]

    return False


def showEpisodes():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="thumb"><div class="video-thumb"><a href="(.+?)" title="(.+?)"><img loading="lazy" src="(.+?)" alt'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:

            sTitle = aEntry[1].replace("الحلقة ", " E").replace("حلقة ", " E").replace("مدبلج للعربية", "مدبلج").replace("مشاهدة وتحميل", "").replace("اون لاين", "")
            siteUrl = aEntry[0]
            if siteUrl.startswith('//'):
                siteUrl = 'http:' + siteUrl
            if URL_MAIN not in siteUrl:
                siteUrl = URL_MAIN + siteUrl
            sThumb = sThumb

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, '', oOutputParameterHandler)

    sPattern = 'class="videocontainer"> <iframe src="([^<]+)" id="([^<]+)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:

            sTitle = "playlist"
            siteUrl = 'https:'+aEntry[0]
            if siteUrl.startswith('//'):
                siteUrl = 'http:' + siteUrl
            if URL_MAIN not in siteUrl:
                siteUrl = URL_MAIN + siteUrl
            sThumb = sThumb
            sDesc = ""

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    sPattern = '<ul class="pagination">(.+?)id="footer">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        sHtmlContent3 = aResult[1][0]

        sPattern = '<li><a href="([^<]+)">([^<]+)</a></li>'
        aResult = oParser.parse(sHtmlContent3, sPattern)
        if aResult[0]:
            for aEntry in aResult[1]:

                sTitle = aEntry[1]

                sTitle = "PAGE " + sTitle
                sTitle = '[COLOR red]'+sTitle+'[/COLOR]'
                siteUrl = aEntry[0]
                if URL_MAIN not in siteUrl:
                    siteUrl = URL_MAIN + siteUrl
                sThumb = ""
                sDesc = ""

                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', siteUrl)

                oGui.addDir(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showHosters():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = "PGlmcmFt(.+?)'"
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            m3url = "PGlmcmFt" + aEntry
            sHtmlContent2 = base64.b64decode(m3url)

            sPattern = 'src="(.+?)".+?allowfullscreen'
            aResult = oParser.parse(sHtmlContent2, sPattern)
            if aResult[0]:
                for aEntry in aResult[1]:

                    url = aEntry.replace("https://dai.ly/", "https://www.dailymotion.com/video/")
                    sTitle = " "
                    if url.startswith('//'):
                        url = 'http:' + url

                    sHosterUrl = url
                    oHoster = cHosterGui().checkHoster(sHosterUrl)
                    if oHoster:
                        sDisplayTitle = sMovieTitle+sTitle
                        oHoster.setDisplayName(sDisplayTitle)
                        oHoster.setFileName(sDisplayTitle)
                        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()
