﻿# -*- coding: utf-8 -*-
# zombi https://github.com/zombiB/zombi-addons/

import re

import requests
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

SITE_IDENTIFIER = 'egyclub'
SITE_NAME = 'Egyclub'
SITE_DESC = 'arabic vod'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)
MOVIE_EN = (URL_MAIN + 'category/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d8%a7%d8%ac%d9%86%d8%a8%d9%8a', 'showMovies')
MOVIE_HI = (URL_MAIN + 'category/%D8%A7%D9%81%D9%84%D8%A7%D9%85-%D9%87%D9%86%D8%AF%D9%8A', 'showMovies')

MOVIE_TURK = (URL_MAIN + 'category/%D8%A7%D9%81%D9%84%D8%A7%D9%85-%D8%AA%D8%B1%D9%83%D9%8A', 'showMovies')
KID_MOVIES = (URL_MAIN + 'category/%D8%A7%D9%81%D9%84%D8%A7%D9%85-%D8%A7%D9%86%D9%8A%D9%85%D9%8A%D8%B4%D9%86', 'showMovies')

MOVIE_CLASSIC = (URL_MAIN + 'category/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d9%83%d9%84%d8%a7%d8%b3%d9%8a%d9%83%d9%8a%d8%a9-%d8%b9%d8%a7%d9%84%d9%85%d9%8a%d8%a9', 'showMovies')
SERIE_EN = (URL_MAIN + 'allseries/', 'showSeries')
DOC_NEWS = (URL_MAIN + 'category/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d9%88%d8%ab%d8%a7%d8%a6%d9%82%d9%8a%d8%a9', 'showMovies')


URL_SEARCH = (URL_MAIN + '?s=', 'showMovies')
URL_SEARCH_MOVIES = (URL_MAIN + '?s=', 'showMovies')
URL_SEARCH_SERIES = (URL_MAIN + '?s=%D9%85%D8%B3%D9%84%D8%B3%D9%84+', 'showSeries')
FUNCTION_SEARCH = 'showMovies'


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

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HI[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام هندية', 'hend.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_TURK[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام تركية', 'turk.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_CLASSIC[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام كلاسيكية', 'class.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30121)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', SERIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أجنبية', 'agnab.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '?s='+sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showSeriesSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '?s=%D9%85%D8%B3%D9%84%D8%B3%D9%84+'+sSearchText
        showSeries(sUrl)
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

    sPattern = '<div class="film_block"><a href="(.+?)" title="(.+?)">.+?data-image="(.+?)" title'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            if "فيلم" not in aEntry[1]:
                continue

            sTitle = aEntry[1].replace("مشاهدة", "").replace("اونلاين", "").replace("مشاهده", "").replace("مترجمة", "").replace("مسلسل", "").replace("انمي", "").replace("مترجم", "").replace("كاملة", "").replace("جودة عالية", "").replace("كامل", "").replace("فيلم", "").replace("اون لاين", "").replace("WEB-DL", "").replace("BRRip", "").replace("720p", "").replace("HD-TC", "").replace("HDRip", "").replace(
                "HD-CAM", "").replace("DVDRip", "").replace("BluRay", "").replace("1080p", "").replace("WEBRip", "").replace("WEB-dl", "").replace("4K", "").replace("All", "").replace("BDRip", "").replace("HDCAM", "").replace("HDTC", "").replace("HDTV", "").replace("HD", "").replace("720", "").replace("HDCam", "").replace("Full HD", "").replace("1080", "").replace("HC", "").replace("Web-dl", "").replace("أون لاين", "")
            siteUrl = aEntry[0]
            sThumb = aEntry[2]
            sDesc = ''
            sYear = ''
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear, '')

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            oGui.addMovie(SITE_IDENTIFIER, 'showServers', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    if not sSearch:
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
        oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oParser = cParser()

    sPattern = 'class="next page-numbers" href="(.+?)">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        return URL_MAIN+aResult[1][0]
    return False


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
    sPattern = '<div class="film_block"><a href="(.+?)" title="(.+?)">.+?data-image="(.+?)" title'
    aResult = oParser.parse(sHtmlContent, sPattern)

    itemList = []
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            if "فيلم" in aEntry[1]:
                continue

            sTitle = aEntry[1].replace("مشاهدة", "").replace("اونلاين", "").replace("مترجمة", "").replace("مسلسل", "").replace("انمي", "").replace("مترجم", "").replace("كامل", "").replace("فيلم", "").replace("اون لاين", "").replace("WEB-DL", "").replace("BRRip", "").replace("720p", "").replace("HD-TC", "").replace("HDRip", "").replace("HD-CAM", "").replace("DVDRip", "").replace(
                "BluRay", "").replace("1080p", "").replace("WEBRip", "").replace("WEB-dl", "").replace("4K", "").replace("All", "").replace("BDRip", "").replace("HDCAM", "").replace("HDTC", "").replace("HDTV", "").replace("HD", "").replace("720", "").replace("HDCam", "").replace("Full HD", "").replace("1080", "").replace("HC", "").replace("Web-dl", "").replace("كامل", "").replace("والاخيرة", "")
            siteUrl = aEntry[0]
            sThumb = aEntry[2]
            sDesc = ''
            sYear = ''
            sDisplayTitle = sTitle.replace("الموسم العاشر", "S10").replace("الموسم الحادي عشر", "S11").replace("الموسم الثاني عشر", "S12").replace("الموسم الثالث عشر", "S13").replace("الموسم الرابع عشر", "S14").replace("الموسم الخامس عشر", "S15").replace("الموسم السادس عشر", "S16").replace("الموسم السابع عشر", "S17").replace("الموسم الثامن عشر", "S18").replace("الموسم التاسع عشر", "S19").replace("الموسم العشرون", "S20").replace("الموسم الحادي و العشرون", "S21").replace("الموسم الثاني و العشرون", "S22").replace("الموسم الثالث و العشرون", "S23").replace("الموسم الرابع والعشرون", "S24").replace("الموسم الخامس و العشرون", "S25").replace(
                "الموسم السادس والعشرون", "S26").replace("الموسم السابع والعشرون", "S27").replace("الموسم الثامن والعشرون", "S28").replace("الموسم التاسع والعشرون", "S29").replace("الموسم الثلاثون", "S30").replace("الموسم الحادي و الثلاثون", "S31").replace("الموسم الثاني والثلاثون", "S32").replace("الموسم الاول", "S1").replace("الموسم الثاني", "S2").replace("الموسم الثانى", "S2").replace("الموسم الثالث", "S3").replace("الموسم الرابع", "S4").replace("الموسم الخامس", "S5").replace("الموسم السادس", "S6").replace("الموسم السابع", "S7").replace("الموسم الثامن", "S8").replace("الموسم التاسع", "S9").replace("الموسم", "S").replace("S ", "S").replace("موسم", "S").replace("S ", "S")
            sDisplayTitle = sDisplayTitle.split("الحلقة")[0]
            sDisplayTitle = sDisplayTitle.split("حلقة")[0]

            if sDisplayTitle not in itemList:
                itemList.append(sDisplayTitle)
                oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                oOutputParameterHandler.addParameter('sMovieTitle', sDisplayTitle)
                oOutputParameterHandler.addParameter('sThumb', sThumb)
                oOutputParameterHandler.addParameter('sYear', sYear)
                # if sSearch:
                # oGui.addEpisode(SITE_IDENTIFIER, 'showServers', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)
                # if not sSearch:
                oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)

    if not sSearch:
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)
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

    sPattern = '<div class="film_block"><a href="(.+?)" title="(.+?)"><div'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            sTitle = aEntry[1].replace("الجزء", "الموسم").replace("مترجمة", "").replace("اونلاين", "").replace("مشاهدة", "").replace("مسلسل", "").replace("انمي", "").replace("انمى", "").replace("مترجم", "").replace("فيلم", "").replace("اون لاين", "").replace("WEB-DL", "").replace("BRRip", "").replace("720p", "").replace("HD-TC", "").replace("HDRip", "").replace(
                "HD-CAM", "").replace("DVDRip", "").replace("BluRay", "").replace("1080p", "").replace("WEBRip", "").replace("WEB-dl", "").replace("كامل", "").replace("مشاهدة وتحميل", "").replace("اون لاين", "").replace("جميع حلقات", "").replace("والأخيرة", "").replace("والاخيرة", "").replace("الأخيرة", "").replace("الاخيرة", "").replace("والاخيرة", "")

            siteUrl = aEntry[0]
            sThumb = sThumb
            sDesc = ''
            sYear = ''
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear, '')
            sDisplayTitle = sTitle.replace("الموسم العاشر", "S10").replace("الموسم الحادي عشر", "S11").replace("الموسم الثاني عشر", "S12").replace("الموسم الثالث عشر", "S13").replace("الموسم الرابع عشر", "S14").replace("الموسم الخامس عشر", "S15").replace("الموسم السادس عشر", "S16").replace("الموسم السابع عشر", "S17").replace("الموسم الثامن عشر", "S18").replace("الموسم التاسع عشر", "S19").replace("الموسم العشرون", "S20").replace("الموسم الحادي و العشرون", "S21").replace("الموسم الثاني و العشرون", "S22").replace("الموسم الثالث و العشرون", "S23").replace("الموسم الرابع والعشرون", "S24").replace("الموسم الخامس و العشرون", "S25").replace("الموسم السادس والعشرون", "S26").replace(
                "الموسم السابع والعشرون", "S27").replace("الموسم الثامن والعشرون", "S28").replace("الموسم التاسع والعشرون", "S29").replace("الموسم الثلاثون", "S30").replace("الموسم الحادي و الثلاثون", "S31").replace("الموسم الثاني والثلاثون", "S32").replace("الموسم الاول", "S1").replace(" الثانى", "2").replace("الموسم الثاني", "S2").replace("الموسم الثالث", "S3").replace("الموسم الثالث", "S3").replace("الموسم الرابع", "S4").replace("الموسم الخامس", "S5").replace("الموسم السادس", "S6").replace("الموسم السابع", "S7").replace("الموسم الثامن", "S8").replace("الموسم التاسع", "S9").replace("الحلقة ", " E").replace("حلقة ", " E").replace("الموسم", "S").replace("S ", "S")

            oOutputParameterHandler.addParameter('siteUrl', aEntry[0])
            oOutputParameterHandler.addParameter('sMovieTitle', sDisplayTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)

            oGui.addEpisode(SITE_IDENTIFIER, 'showServers', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showEpisodes', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showServers():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<li data-i="(.+?)" data-id="(.+?)" class'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            sTitle = 'server '
            siteUrl = URL_MAIN + '/wp-content/themes/Elshaikh/Inc/Ajax/Single/Server.php'
            hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0', 'referer': URL_MAIN + ''}
            params = {'id': aEntry[1], 'i': aEntry[0]}
            St = requests.Session()
            sHtmlContent2 = St.post(siteUrl, headers=hdr, data=params)
            sHtmlContent2 = sHtmlContent2.content

            sPattern = 'src="([^<]+)" scrolling'
            aResult = oParser.parse(sHtmlContent2, sPattern)
            if aResult[0]:
                for aEntry in aResult[1]:
                    url = aEntry
                    sTitle = sMovieTitle
                    if url.startswith('//'):
                        url = 'http:' + url

                    sHosterUrl = url
                    if 'userload' in sHosterUrl:
                        sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
                    if 'mystream' in sHosterUrl:
                        sHosterUrl = sHosterUrl + "|Referer=" + URL_MAIN
                    oHoster = cHosterGui().checkHoster(sHosterUrl)
                    if oHoster:
                        oHoster.setDisplayName(sMovieTitle)
                        oHoster.setFileName(sMovieTitle)
                        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    sPattern = 'href="([^<]+)" rel="nofollow" class="download'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:

            url = aEntry
            sTitle = ""
            sThumb = sThumb
            if url.startswith('//'):
                url = 'http:' + url

            sHosterUrl = url
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
