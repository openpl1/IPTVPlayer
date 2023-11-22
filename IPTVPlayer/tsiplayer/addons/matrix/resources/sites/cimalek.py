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

SITE_IDENTIFIER = 'cimalek'
SITE_NAME = 'Cimalek'
SITE_DESC = 'arabic vod'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

MOVIE_FAM = (URL_MAIN + '/category/aflam-online/aflam-family/', 'showMovies')
MOVIE_EN = (URL_MAIN + '/category/aflam-online/', 'showMovies')
MOVIE_ASIAN = (URL_MAIN + '/category/asian-aflam/', 'showMovies')
MOVIE_TURK = (URL_MAIN + '/category/hindi-movie/', 'showMovies')
MOVIE_HI = (URL_MAIN + '/category/indian-movies/', 'showMovies')
KID_MOVIES = (URL_MAIN + '/category/cartoon-movies/', 'showMovies')
SERIE_EN = (URL_MAIN + '/category/english-series/', 'showSeries')
ANIM_NEWS = (URL_MAIN + '/category/anime-series/', 'showSeries')
ANIM_MOVIES = (URL_MAIN + '/category/anime-movies/', 'showMovies')
SERIE_ASIA = (URL_MAIN + '/category/asian-series/', 'showSeries')

URL_SEARCH = (URL_MAIN + '/search/', 'showSeries')
URL_SEARCH_MOVIES = (URL_MAIN + '/search/', 'showMovies')
URL_SEARCH_SERIES = (URL_MAIN + '/search/', 'showSeries')
URL_SEARCH_ANIMS = (URL_MAIN + '/search/', 'showAnimes')
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

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أجنبية', 'agnab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_TURK[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام تركية', 'turk.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HI[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام هندية', 'hend.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', KID_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام كرتون', 'crtoon.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30121)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', SERIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أجنبية', 'agnab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_ASIA[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أسيوية', 'asia.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', ANIM_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات إنمي', 'anime.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSeriesSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '?s='+sSearchText
        showSeries(sUrl)
        oGui.setEndOfDirectory()
        return


def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '?s='+sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showMovies(sSearch=''):
    oGui = cGui()
    oParser = cParser()

    if sSearch:
        sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="title">(.+?)</div>.+?<a href="(.+?)">.+?data-src="(.+?)" alt'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            if "فيلم" not in aEntry[0]:
                continue

            sTitle = aEntry[0].replace("مشاهدة", "").replace("مشاهده", "").replace("مترجم", "").replace("فيلم", "").replace("اون لاين", "").replace("برنامج", "").replace("WEB-DL", "").replace("BRRip", "").replace("720p", "").replace("HD-TC", "").replace("HDRip", "").replace("HD-CAM", "").replace("DVDRip", "").replace("BluRay", "").replace(
                "1080p", "").replace("WEBRip", "").replace("WEB-dl", "").replace("4K", "").replace("All", "").replace("BDRip", "").replace("HDCAM", "").replace("HDTC", "").replace("HDTV", "").replace("HD", "").replace("720", "").replace("HDCam", "").replace("Full HD", "").replace("1080", "").replace("HC", "").replace("Web-dl", "").replace("انمي", "")
            siteUrl = aEntry[1]+"/watch/"
            sDesc = ''
            sThumb = aEntry[2]
            sYear = ''
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear, '')

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sDesc', sDesc)

            oGui.addMovie(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()


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

    sPattern = 'data-id=".+?">.+?<a href="(.+?)">.+?data-src="(.+?)" alt="(.+?)">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            if "فيلم" in aEntry[2]:
                continue

            siteUrl = aEntry[0]

            sTitle = aEntry[2].replace("مشاهدة", "").replace("مسلسل", "").replace("انمي", "").replace("مترجمة", "").replace("مترجم", "").replace("مشاهده", "").replace("برنامج", "").replace("مترجمة", "").replace("فيلم", "").replace("اون لاين", "").replace("WEB-DL", "").replace(
                "BRRip", "").replace("720p", "").replace("HD-TC", "").replace("HDRip", "").replace("HD-CAM", "").replace("DVDRip", "").replace("BluRay", "").replace("1080p", "").replace("WEBRip", "").replace("WEB-dl", "").replace("مترجم ", "").replace("مشاهدة وتحميل", "").replace("اون لاين", "")
            sThumb = aEntry[1]
            sDesc = ''
            sTitle = sTitle.split('موسم')[0].split('حلقة')[0]
            sYear = ''
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear, '')

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            oGui.addTV(SITE_IDENTIFIER, 'showEps', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
    if not sSearch:

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

        oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oParser = cParser()

    sPattern = "class='arrow_pag' href=(.+?)><i id='nextpagination"
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        return aResult[1][0].replace('"', "")

    return False


def showEps():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = "href='([^<]+)' title='(.+?)'><span class='serie'>"
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            sTitle = aEntry[1].replace("الحلقة ", "E").replace("الحلقة ", "E").replace("الموسم", "S").replace("مشاهدة", "").replace("مسلسل", "").replace("انمي", "").replace("مترجمة", "").replace("مترجم", "").replace("مشاهده", "").replace("برنامج", "").replace("مترجمة", "").replace("فيلم", "").replace("اون لاين", "").replace(
                "WEB-DL", "").replace("BRRip", "").replace("720p", "").replace("HD-TC", "").replace("HDRip", "").replace("HD-CAM", "").replace("DVDRip", "").replace("BluRay", "").replace("1080p", "").replace("WEBRip", "").replace("WEB-dl", "").replace("مترجم ", "").replace("مشاهدة وتحميل", "").replace("اون لاين", "")
            siteUrl = aEntry[0] + '/watch/'
            sThumb = sThumb
            sDesc = ""

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)

            oGui.addEpisode(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showLinks():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '"ver":"([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        ver = aResult[1][0]

    sPattern = 'data-post=["\']([^"\']+)["\']\s*data-nume=["\']([^"\']+)["\']><ul><li>(.+?)</li>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            sHost = aEntry[2]
            siteUrl = f'{URL_MAIN}wp-json/lalaplayer/v2/?p={aEntry[0]}&t=movie&n={aEntry[1]}&ver={ver}'
            sHost = aEntry[2]
            sTitle = ('%s [COLOR coral]%s[/COLOR]') % (sMovieTitle, sHost)

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sHost', sHost)

            oGui.addLink(SITE_IDENTIFIER, 'showHosters', sTitle, sThumb, '', oOutputParameterHandler)

    sPattern = 'href="([^<]+)" target="_blank" rel.+?<em>([^<]+)</em></div>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            sHosterUrl = aEntry[0]
            sHosterUrl = sHosterUrl
            sTitle = sMovieTitle+' ['+aEntry[1]+'] '
            if sHosterUrl.startswith('//'):
                sHosterUrl = 'http:' + sHosterUrl

            if 'mystream' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                oHoster.setDisplayName(sTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()


def showHosters():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    siteUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(siteUrl)
    sData = oRequestHandler.request()

    sPattern = '"embed_url":"(.+?)",'
    aResult = oParser.parse(sData, sPattern)
    if aResult:
        for aEntry in aResult[1]:
            url = aEntry.replace("\/", "/")
            if url.startswith('//'):
                url = 'http:' + url

            oRequestHandler = cRequestHandler(url)
            oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0')
            oRequestHandler.addHeaderEntry('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
            oRequestHandler.addHeaderEntry('X-Requested-With', 'XMLHttpRequest')
            oRequestHandler.addHeaderEntry('Referer', URL_MAIN)
            sData = oRequestHandler.request()

            sPattern = '"file":"(.+?)","label":'
            aResult = oParser.parse(sData, sPattern)
            if aResult[0]:
                for aEntry in aResult[1]:
                    url = aEntry.replace("\/", "/")
                    if url.startswith('//'):
                        url = 'http:' + url

                    sHosterUrl = url
                    if 'streamtape' in sHosterUrl:
                        sHosterUrl = sHosterUrl
                    if 'mystream' in sHosterUrl:
                        sHosterUrl = sHosterUrl
                    oHoster = cHosterGui().checkHoster(sHosterUrl)
                    if oHoster:
                        oHoster.setDisplayName(sMovieTitle)
                        oHoster.setFileName(sMovieTitle)
                        cHosterGui().showHoster(oGui, oHoster, sHosterUrl+"|verifypeer=false", sThumb)

    oGui.setEndOfDirectory()
