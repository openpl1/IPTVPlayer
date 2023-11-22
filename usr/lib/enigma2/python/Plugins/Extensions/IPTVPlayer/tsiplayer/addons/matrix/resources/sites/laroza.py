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

SITE_IDENTIFIER = 'laroza'
SITE_NAME = 'Laroza'
SITE_DESC = 'arabic vod'

UA = 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.48 Mobile Safari/537.36'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

MOVIE_AR = (URL_MAIN + 'category.php?cat=arabic-movies10', 'showMovies')
MOVIE_EN = (URL_MAIN + 'category.php?cat=all_movies', 'showMovies')
MOVIE_HI = (URL_MAIN + 'category.php?cat=indian-movies3', 'showMovies')
MOVIE_ASIAN = (URL_MAIN + 'category.php?cat=asian-movies', 'showMovies')
MOVIE_DUBBED = (URL_MAIN + 'category.php?cat=aflammdblgh', 'showMovies')
KID_MOVIES = (URL_MAIN + 'category.php?cat=anime-movies', 'showMovies')

RAMADAN_SERIES = (URL_MAIN + 'category.php?cat=ramadan-2023', 'showSeries')
SERIE_EN = (URL_MAIN + 'category.php?cat=english-series3', 'showSeries')
SERIE_AR = (URL_MAIN + 'category.php?cat=arabic-series22', 'showSeries')
SERIE_HEND = (URL_MAIN + 'category.php?cat=4indian-series', 'showSeries')
SERIE_TR = (URL_MAIN + 'category.php?cat=turkish-3isk-seriess21', 'showSeries')

REPLAYTV_PLAY = (URL_MAIN+'category.php?cat=masrh1', 'showMovies')
REPLAYTV_NEWS = (URL_MAIN + 'category.php?cat=tv-programs5', 'showSeries')

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

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أجنبية', 'agnab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام عربية', 'arab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_ASIAN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أسيوية', 'asia.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', KID_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام كرتون', 'anim.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_DUBBED[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام مدبلجة', 'mdblg.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HI[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام هندية', 'hend.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30121)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', SERIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات عربية', 'arab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_TR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات تركية', 'turk.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_HEND[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات هندية', 'hend.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', REPLAYTV_PLAY[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'مسرحيات', 'msrh.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30350)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', REPLAYTV_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'برامج تلفزيونية', 'brmg.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', RAMADAN_SERIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'رمضان', 'rmdn.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + 'category.php?cat=26ramadan-2022')
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
        sUrl = URL_MAIN + '/search.php?keywords=فيلم+'+sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showRamdan():
    oGui = cGui()
    List = []
    List.append(['Ramadan 2023', 'category.php?cat=ramadan-2023', 'showSeries'])
    List.append(['Ramadan 2022', 'category.php?cat=26ramadan-2022', 'showSeries'])
    List.append(['Ramadan 2021', 'category.php?cat=18ramadan-2021', 'showSeries'])
    List.append(['Ramadan 2020', 'category.php?cat=2ramadan-2020', 'showSeries'])

    for li in List:
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + li[1])
        oGui.addDir(SITE_IDENTIFIER, li[2], li[0], '/Ramadan.png', oOutputParameterHandler)
    oGui.setEndOfDirectory()


def showMovies(sSearch=''):
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

    sPattern = '<div class="thumbnail">.+?<i class="fa fa-clock-o">.+?<a href="(.+?)".+?title="(.+?)".+?<img src=.+?data-echo="(.+?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            if "مسلسل" in aEntry[1]:
                continue

            if "حلقة" in aEntry[1]:
                continue

            sTitle = aEntry[1].replace("مشاهدة", "").replace("مشاهده", "").replace("مترجم", "").replace("فيلم", "").replace("اونلاين", "").replace("اون لاين", "").replace("برنامج", "").replace("WEB-DL", "").replace("BRRip", "").replace("720p", "").replace("HD-TC", "").replace("HDRip", "").replace("HD-CAM", "").replace("DVDRip", "").replace("BluRay", "").replace(
                "1080p", "").replace("WEBRip", "").replace("WEB-dl", "").replace("4K", "").replace("All", "").replace("BDRip", "").replace("HDCAM", "").replace("HDTC", "").replace("HDTV", "").replace("HD", "").replace("720", "").replace("HDCam", "").replace("Full HD", "").replace("1080", "").replace("HC", "").replace("Web-dl", "").replace("انمي", "")

            Url = aEntry[0]
            siteUrl = aEntry[0].replace("watch.php", "play.php").replace("video.php", "play.php") + '|Referer=' + Url
            sDesc = ""
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

            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

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
    oRequestHandler.addHeaderEntry('User-Agent', UA)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="thumbnail">.+?<i class="fa fa-clock-o">.+?<a href="(.+?)".+?title="(.+?)".+?<img src=.+?data-echo="(.+?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    itemList = []
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            if "فيلم" in aEntry[1]:
                continue

            siteUrl = aEntry[0]
            if 'حلقة' not in aEntry[1]:
                siteUrl = aEntry[0].replace("watch.php", "play.php").replace("video.php", "play.php")

            sTitle = aEntry[1].replace("مشاهدة", "").replace("مسلسل", "").replace("انمي", "").replace("مترجمة", "").replace("مترجم", "").replace("مشاهده", "").replace("برنامج", "").replace("مترجمة", "").replace("فيلم", "").replace("اون لاين", "").replace("WEB-DL", "").replace(
                "BRRip", "").replace("720p", "").replace("HD-TC", "").replace("HDRip", "").replace("HD-CAM", "").replace("DVDRip", "").replace("BluRay", "").replace("1080p", "").replace("WEBRip", "").replace("WEB-dl", "").replace("مترجم ", "").replace("مشاهدة وتحميل", "").replace("اون لاين", "")
            sThumb = aEntry[2]
            sDesc = ''
            sTitle = sTitle.split('موسم')[0].split('الحلقة')[0]
            sYear = ''
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear, '')

            if sTitle not in itemList:
                itemList.append(sTitle)
                oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                oOutputParameterHandler.addParameter('sYear', sYear)
                oOutputParameterHandler.addParameter('sThumb', sThumb)

                if 'حلقة' not in aEntry[1]:
                    oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
                else:
                    oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    if not sSearch:
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
        oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oParser = cParser()

    sPattern = '<li class="active">\s*<a href="#".+?<li class.+?href="([^"]+)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:

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

    sPattern = '<div class="SeasonsEpisodes" style="display:none;" data-serie="(.+?)">(.+?)</div>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            sSeason = "S"+aEntry[0]
            sHtmlContent = aEntry[1]

            sPattern = 'href="(.+?)" title.+?<em>(.+?)</em><span>'
            aResult = oParser.parse(sHtmlContent, sPattern)
            if aResult[0]:
                oOutputParameterHandler = cOutputParameterHandler()
                for aEntry in aResult[1]:
                    siteUrl = URL_MAIN + aEntry[0]
                    siteUrl = siteUrl.replace("video.php", "play.php")
                    sTitle = sMovieTitle+' '+sSeason
                    sTitle = sTitle+" E"+aEntry[1]
                    sThumb = sThumb
                    sDesc = ""

                    oOutputParameterHandler.addParameter('siteUrl', siteUrl)
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

    oRequestHandler = cRequestHandler(sUrl.split("|Referer=")[0])
    oRequestHandler.addHeaderEntry('User-Agent', UA)
    oRequestHandler.addHeaderEntry('Referer', sUrl.split("|Referer=")[0])

    sHtmlContent = oRequestHandler.request()

    sPattern = 'data-embed-url=["\']([^"\']+)["\']'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            sHosterUrl = aEntry
            sTitle = ""
            if sHosterUrl.startswith('//'):
                sHosterUrl = 'http:' + sHosterUrl
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
    else:
        sPattern = '<iframe src=["\']([^"\']+)["\']'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            for aEntry in aResult[1]:

                sHosterUrl = aEntry
                sTitle = ""
                if sHosterUrl.startswith('//'):
                    sHosterUrl = 'http:' + sHosterUrl

                oHoster = cHosterGui().checkHoster(sHosterUrl)
                if oHoster:
                    oHoster.setDisplayName(sMovieTitle)
                    oHoster.setFileName(sMovieTitle)
                    cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()
