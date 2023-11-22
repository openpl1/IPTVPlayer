# -*- coding: utf-8 -*-
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
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.util import \
    Quote

SITE_IDENTIFIER = 'arabseed'
SITE_NAME = 'Arabseed'
SITE_DESC = 'arabic vod'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

MOVIE_CLASSIC = (URL_MAIN + '/category/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d9%83%d9%84%d8%a7%d8%b3%d9%8a%d9%83%d9%8a%d9%87/', 'showMovies')
MOVIE_EN = (URL_MAIN + '/category/foreign-movies/', 'showMovies')
MOVIE_AR = (URL_MAIN + '/category/arabic-movies-5/', 'showMovies')
MOVIE_DUBBED = (URL_MAIN + '/category/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d9%85%d8%af%d8%a8%d9%84%d8%ac%d8%a9/', 'showMovies')
MOVIE_HI = (URL_MAIN + '/category/indian-movies/', 'showMovies')
MOVIE_ASIAN = (URL_MAIN + '/category/asian-movies/', 'showMovies')
MOVIE_TURK = (URL_MAIN + '/category/turkish-movies/', 'showMovies')
KID_MOVIES = (URL_MAIN + '/category/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d8%a7%d9%86%d9%8a%d9%85%d9%8a%d8%b4%d9%86/', 'showMovies')
SERIE_TR = (URL_MAIN + '/category/turkish-series-1/', 'showSeries')
SERIE_DUBBED = (URL_MAIN + '/category/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d9%85%d8%af%d8%a8%d9%84%d8%ac%d8%a9/', 'showSeries')
SERIE_ASIA = (URL_MAIN + '/category/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d9%83%d9%88%d8%b1%d9%8a%d9%87/', 'showSeries')
SERIE_HEND = (URL_MAIN + '/category/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d9%87%d9%86%d8%af%d9%8a%d8%a9/', 'showSeries')
SERIE_EN = (URL_MAIN + '/category/foreign-series/', 'showSeries')
SERIE_AR = (URL_MAIN + '/category/arabic-series/', 'showSeries')
SPORT_WWE = (URL_MAIN + '/category/wwe-shows/', 'showMovies')

RAMADAN_SERIES = (URL_MAIN + '/category/ramadan-series-2023/', 'showSeries')
ANIM_NEWS = (URL_MAIN + '/category/cartoon-series/', 'showSeries')


REPLAYTV_NEWS = (URL_MAIN + '/category/%D8%A8%D8%B1%D8%A7%D9%85%D8%AC-%D8%AA%D9%84%D9%81%D8%B2%D9%8A%D9%88%D9%86%D9%8A%D8%A9', 'showMovies')
URL_SEARCH_MOVIES = (URL_MAIN + '/find/?find=', 'showMovies')
URL_SEARCH_SERIES = (URL_MAIN + '/find/?find=', 'showSeries')
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

    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + '/category/netfilx/%d8%a7%d9%81%d9%84%d8%a7%d9%85-netfilx/')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'افلام Netfilx', 'film.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أجنبية', 'agnab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام عربية', 'arab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_ASIAN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أسيوية', 'asia.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_TURK[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام تركية', 'turk.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_CLASSIC[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام كلاسيكية', 'class.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HI[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام هندية', 'hend.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', KID_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام كرتون', 'crtoon.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30121)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + '/category/netfilx/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-netfilz/')
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات Netfilx', 'mslsl.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أجنبية', 'agnab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات عربية', 'arab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_TR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات تركية', 'turk.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30350)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + '/category/%d9%85%d8%b5%d8%a7%d8%b1%d8%b9%d9%87/')
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مصارعة', 'wwe.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText is not False:
        sUrl = URL_MAIN + '/find/?find='+sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showSeriesSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText is not False:
        sUrl = URL_MAIN + '/find/?find='+sSearchText
        showSeries(sUrl)
        oGui.setEndOfDirectory()
        return


def showMovies(sSearch=''):
    oGui = cGui()
    oParser = cParser()
    oRequestHandler = cRequestHandler(URL_MAIN)
    sHtmlContent = oRequestHandler.request()
    URL_MAIN2 = main_function(sHtmlContent)

    if sSearch:
        sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

    sUrl = sUrl.replace(URL_MAIN, URL_MAIN2)
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    s = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0', 'Referer': Quote(sUrl)}
    r = s.post(sUrl, headers=headers)
    sHtmlContent = r.content.decode('utf8')

    if sSearch:
        s = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0', 'Referer': Quote(sUrl)}
        psearch = sUrl.split('?find=')[1]
        data = {'search': psearch, 'type': 'movies'}
        r = s.post(URL_MAIN2 + '/wp-content/themes/Elshaikh2021/Ajaxat/SearchingTwo.php', headers=headers, data=data)
        sHtmlContent = r.content.decode('utf8')

    sPattern = '</div><a href="(.+?)">.+?data-src="([^"]+)".+?alt="(.+?)">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            sTitle = aEntry[2].replace("مشاهدة", "").replace("مسلسل", "").replace("انمي", "").replace("مترجمة", "").replace("مترجم", "").replace("برنامج", "").replace("فيلم", "").replace("والأخيرة", "").replace("مدبلج للعربية", "مدبلج").replace("مدبلج", "[arabic]").replace("والاخيرة", "").replace(
                "كاملة", "").replace("حلقات كاملة", "").replace("اونلاين", "").replace("مباشرة", "").replace("انتاج ", "").replace("جودة عالية", "").replace("كامل", "").replace("HD", "").replace("السلسلة الوثائقية", "").replace("الفيلم الوثائقي", "").replace("اون لاين", "").replace("عرض", "").replace("الرو", "")
            siteUrl = aEntry[0]
            sThumb = aEntry[1]
            sDesc = ''
            sYear = ''
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear, '')
            sDisplayTitle = ('%s (%s)') % (sTitle, sYear)

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('URL_MAIN', URL_MAIN2)

            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sDisplayTitle, '', sThumb, sDesc, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()


def showPacks(sSearch=''):
    oGui = cGui()
    oParser = cParser()
    oRequestHandler = cRequestHandler(URL_MAIN)
    sHtmlContent = oRequestHandler.request()
    URL_MAIN2 = main_function(sHtmlContent)

    if sSearch:
        sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

    sUrl = sUrl.replace(URL_MAIN, URL_MAIN2)

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="BlockItem"><a href="([^<]+)">.+?src="([^"]+)".+?class.+?<div class="BlockTitle">([^<]+)</div>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] is True:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            siteUrl = aEntry[0]
            sTitle = aEntry[2].replace("مشاهدة", "").replace("برنامج", "").replace("مترجمة", "").replace("مترجم", "").replace("فيلم", "").replace("اون لاين", "").replace("WEB-DL", "").replace("BRRip", "").replace("720p", "").replace("HD-TC", "").replace("HDRip", "").replace("HD-CAM", "").replace("DVDRip", "").replace("BluRay", "").replace("1080p", "").replace(
                "WEBRip", "").replace("WEB-dl", "").replace("4K", "").replace("All", "").replace("BDRip", "").replace("HDCAM", "").replace("HDTC", "").replace("HDTV", "").replace("HD", "").replace("720", "").replace("HDCam", "").replace("Full HD", "").replace("1080", "").replace("HC", "").replace("Web-dl", "").replace("مدبلج للعربية", "مدبلج")

            sThumb = aEntry[1]
            sDesc = ''

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('URL_MAIN', URL_MAIN2)

            oGui.addMovie(SITE_IDENTIFIER, 'showPack', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage != False:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showPacks', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()


def showPack():
    oGui = cGui()
    oParser = cParser()
    oRequestHandler = cRequestHandler(URL_MAIN)
    sHtmlContent = oRequestHandler.request()
    URL_MAIN2 = main_function(sHtmlContent)
    sUrl = sUrl.replace(URL_MAIN, URL_MAIN2)

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="BlockItem"><a href="([^<]+)">.+?src="([^"]+)".+?class.+?<div class="BlockTitle">([^<]+)</div>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] is True:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            sTitle = aEntry[2].replace("</em>", "").replace("<em>", "").replace("</span>", "").replace("<span>", "").replace("مشاهدة", "").replace("برنامج", "").replace("مترجمة", "").replace("مترجم", "").replace("فيلم", "").replace("اون لاين", "").replace("WEB-DL", "").replace("BRRip", "").replace("720p", "").replace("HD-TC", "").replace("HDRip", "").replace("HD-CAM", "").replace("DVDRip", "").replace(
                "BluRay", "").replace("1080p", "").replace("WEBRip", "").replace("WEB-dl", "").replace("4K", "").replace("All", "").replace("BDRip", "").replace("HDCAM", "").replace("HDTC", "").replace("HDTV", "").replace("HD", "").replace("720", "").replace("HDCam", "").replace("Full HD", "").replace("1080", "").replace("HC", "").replace("Web-dl", "").replace("مدبلج للعربية", "مدبلج")
            siteUrl = aEntry[0]
            sThumb = aEntry[1]
            sDesc = ""
            sYear = ''
            m = re.search('([0-9]{4})', sTitle)
            if m:
                sYear = str(m.group(0))
                sTitle = sTitle.replace(sYear, '')
            sDisplayTitle = ('%s (%s)') % (sTitle, sYear)

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('URL_MAIN', URL_MAIN2)

            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSeries(sSearch=''):
    oGui = cGui()
    oParser = cParser()
    oRequestHandler = cRequestHandler(URL_MAIN)
    sHtmlContent = oRequestHandler.request()
    URL_MAIN2 = main_function(sHtmlContent)

    if sSearch:
        sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

    sUrl = sUrl.replace(URL_MAIN, URL_MAIN2)

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    s = requests.Session()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0', 'Referer': Quote(sUrl)}
    r = s.post(sUrl, headers=headers)
    sHtmlContent = r.content.decode('utf8')

    if sSearch:
        s = requests.Session()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0', 'Referer': Quote(sUrl)}
        psearch = sUrl.rsplit('?find=', 1)[1]
        data = {'search': psearch, 'type': 'series'}
        r = s.post(URL_MAIN + '/wp-content/themes/Elshaikh2021/Ajaxat/SearchingTwo.php', headers=headers, data=data)
        sHtmlContent = r.content.decode('utf8', errors='ignore')

        sPattern = '<div class="Movie.+?">.+?<a href="([^<]+)">.+?data-image="([^<]+)" alt="([^<]+)">'
    else:
        sPattern = '</div><a href="(.+?)">.+?data-src="([^"]+)".+?alt="(.+?)">'

    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            sTitle = aEntry[2].replace("مشاهدة", "").replace("مسلسل", "").replace("انمي", "").replace("مترجمة", "").replace("مترجم", "").replace("برنامج", "").replace("فيلم", "").replace("اون لاين", "").replace("WEB-DL", "").replace("BRRip", "").replace("720p", "").replace(
                "HD-TC", "").replace("HDRip", "").replace("HD-CAM", "").replace("DVDRip", "").replace("BluRay", "").replace("1080p", "").replace("WEBRip", "").replace("WEB-dl", "").replace("مترجم ", "").replace("مشاهدة وتحميل", "").replace("اون لاين", "").replace("مدبلج للعربية", "مدبلج")
            siteUrl = aEntry[0]
            sThumb = aEntry[1]
            sDesc = ''
            sTitle = sTitle.replace("الموسم العاشر", "S10").replace("الموسم الحادي عشر", "S11").replace("الموسم الثاني عشر", "S12").replace("الموسم الثالث عشر", "S13").replace("الموسم الرابع عشر", "S14").replace("الموسم الخامس عشر", "S15").replace("الموسم السادس عشر", "S16").replace("الموسم السابع عشر", "S17").replace("الموسم الثامن عشر", "S18").replace("الموسم التاسع عشر", "S19").replace("الموسم العشرون", "S20").replace("الموسم الحادي و العشرون", "S21").replace("الموسم الثاني و العشرون", "S22").replace("الموسم الثالث و العشرون", "S23").replace("الموسم الرابع والعشرون", "S24").replace("الموسم الخامس و العشرون", "S25").replace("الموسم السادس والعشرون", "S26").replace(
                "الموسم السابع والعشرون", "S27").replace("الموسم الثامن والعشرون", "S28").replace("الموسم التاسع والعشرون", "S29").replace("الموسم الثلاثون", "S30").replace("الموسم الحادي و الثلاثون", "S31").replace("الموسم الثاني والثلاثون", "S32").replace("الموسم الاول", "S1").replace("الموسم الثاني", "S2").replace("الموسم الثالث", "S3").replace("الموسم الثالث", "S3").replace("الموسم الرابع", "S4").replace("الموسم الخامس", "S5").replace("الموسم السادس", "S6").replace("الموسم السابع", "S7").replace("الموسم الثامن", "S8").replace("الموسم التاسع", "S9").replace("الموسم", "S").replace("موسم", "S").replace("S ", "S").split('الحلقة')[0]

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sDesc', sDesc)
            oOutputParameterHandler.addParameter('URL_MAIN', URL_MAIN2)

            oGui.addTV(SITE_IDENTIFIER, 'showSeasons', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()


def showSeasons():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    URL_MAIN = oInputParameterHandler.getValue('URL_MAIN')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = 'data-id="(.+?)" data-season="(.+?)"><i class="fa fa-folder"></i>الموسم <span>(.+?)</span></li>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] is True:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            sSeason = aEntry[2].replace("مترجم", "").replace("مترجمة", "").replace(" الحادي عشر", "11").replace(" الثاني عشر", "12").replace(" الثالث عشر", "13").replace(" الرابع عشر", "14").replace(" الخامس عشر", "15").replace(" السادس عشر", "16").replace(" السابع عشر", "17").replace(" الثامن عشر", "18").replace(" التاسع عشر", "19").replace(" العشرون", "20").replace(" الحادي و العشرون", "21").replace(" الثاني و العشرون", "22").replace(" الثالث و العشرون", "23").replace(" الرابع والعشرون", "24").replace(
                " الخامس و العشرون", "25").replace(" السادس والعشرون", "26").replace(" السابع والعشرون", "27").replace(" الثامن والعشرون", "28").replace(" التاسع والعشرون", "29").replace(" الثلاثون", "30").replace(" الحادي و الثلاثون", "31").replace(" الثاني والثلاثون", "32").replace(" الاول", "1").replace(" الثاني", "2").replace(" الثانى", "2").replace(" الثالث", "3").replace(" الرابع", "4").replace(" الخامس", "5").replace(" السادس", "6").replace(" السابع", "7").replace(" الثامن", "8").replace(" التاسع", "9").replace(" العاشر", "10")
            sSeason = sMovieTitle+" S"+sSeason
            pseason = aEntry[1]
            post = aEntry[0]
            s = requests.Session()
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}
            data = {'post_id': post, 'season': pseason}
            r = s.post(URL_MAIN + '/wp-content/themes/Elshaikh2021/Ajaxat/Single/Episodes.php', headers=headers, data=data)
            sHtmlContent = r.content.decode('utf8', errors='ignore')
            sPattern = 'href="([^<]+)">([^<]+)<em>([^<]+)</em>'
            aResult = oParser.parse(sHtmlContent, sPattern)
            if aResult[0] is True:
                oOutputParameterHandler = cOutputParameterHandler()
                for aEntry in aResult[1]:
                    siteUrl = aEntry[0]
                    sEp = "E"+aEntry[2]
                    sTitle = sSeason+sEp
                    sThumb = sThumb
                    sDesc = ''

                    oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)
                    oOutputParameterHandler.addParameter('URL_MAIN', URL_MAIN)

                    oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
    else:

        sStart = '<div class="ContainerEpisodesList"'
        sEnd = '<div style="clear: both;"></div>'
        sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)

        sPattern = 'href="([^<]+)">([^<]+)<em>([^<]+)</em>'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0] is True:
            oOutputParameterHandler = cOutputParameterHandler()
            for aEntry in aResult[1]:
                sEp = "E"+aEntry[2].replace(" ", "")
                if "مدبلج" in sMovieTitle:
                    sMovieTitle = sMovieTitle.replace("مدبلج", "")
                    sMovieTitle = "مدبلج"+sMovieTitle
                sTitle = sMovieTitle+' '+sEp
                siteUrl = aEntry[0]
                sThumb = sThumb
                sDesc = ''
                sHost = ''

                oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                oOutputParameterHandler.addParameter('sHost', sHost)
                oOutputParameterHandler.addParameter('sThumb', sThumb)
                oOutputParameterHandler.addParameter('URL_MAIN', URL_MAIN)

                oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showEps():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    URL_MAIN = oInputParameterHandler.getValue('URL_MAIN')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sStart = '<div class="ContainerEpisodesList"'
    sEnd = '<div style="clear: both;"></div>'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)

    sPattern = 'href="([^<]+)">([^<]+)<em>([^<]+)</em>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] is True:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            sEp = "E"+aEntry[2].replace(" ", "")
            if "مدبلج" in sMovieTitle:
                sMovieTitle = sMovieTitle.replace("مدبلج", "")
                sMovieTitle = "مدبلج"+sMovieTitle
            sTitle = sMovieTitle+' '+sEp
            siteUrl = aEntry[0]
            sThumb = sThumb
            sDesc = ''
            sHost = ''

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sHost', sHost)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('URL_MAIN', URL_MAIN)

            oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oParser = cParser()

    sPattern = '<a class="next page-numbers" href="(.+?)">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] is True:
        return URL_MAIN+aResult[1][0]
    return False


def showHosters():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    URL_MAIN = oInputParameterHandler.getValue('URL_MAIN')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<a href="([^<]+)" class="watchBTn">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        m3url = aResult[1][0].replace(' ', '')
        oRequestHandler = cRequestHandler(m3url)
        oRequestHandler.addHeaderEntry('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0')
        oRequestHandler.addHeaderEntry('referer', URL_MAIN+'/')
        sHtmlContent = oRequestHandler.request()

    sStart = '<div class="containerServers">'
    sEnd = '<div class="containerIframe">'
    sHtmlContent0 = oParser.abParse(sHtmlContent, sStart, sEnd)

    sPattern = '<h3>(.+?)</h3>(.+?)</i>'
    aResult = oParser.parse(sHtmlContent0, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            sQual = aEntry[0].replace("مشاهدة", "").replace(' ', '')
            sHtmlContent = aEntry[1]

            sHosterUrl = url_function(sHtmlContent)
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                sDisplayTitle = ('%s [COLOR coral](%sp)[/COLOR]') % (sMovieTitle, sQual)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sDisplayTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    sPattern = '<h3>(.+?)</h3>(.+?)</i>(.+?)</i>'
    aResult = oParser.parse(sHtmlContent0, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            sQual = aEntry[0].replace("مشاهدة", "").replace(' ', '')
            sHtmlContent = aEntry[2]

            sHosterUrl = url_function(sHtmlContent)
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                sDisplayTitle = ('%s [COLOR coral](%sp)[/COLOR]') % (sMovieTitle, sQual)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sDisplayTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    sPattern = '<h3>(.+?)</h3>(.+?)</i>(.+?)</i>(.+?)</i>'
    aResult = oParser.parse(sHtmlContent0, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            sQual = aEntry[0].replace("مشاهدة", "").replace(' ', '')
            sHtmlContent = aEntry[3]

            sHosterUrl = url_function(sHtmlContent)
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                sDisplayTitle = ('%s [COLOR coral](%sp)[/COLOR]') % (sMovieTitle, sQual)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sDisplayTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    sPattern = '<h3>(.+?)</h3>(.+?)</i>(.+?)</i>(.+?)</i>(.+?)</i>'
    aResult = oParser.parse(sHtmlContent0, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            sQual = aEntry[0].replace("مشاهدة", "").replace(' ', '')
            sHtmlContent = aEntry[4]

            sHosterUrl = url_function(sHtmlContent)
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                sDisplayTitle = ('%s [COLOR coral](%sp)[/COLOR]') % (sMovieTitle, sQual)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sDisplayTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    sPattern = '<h3>(.+?)</h3>(.+?)</i>(.+?)</i>(.+?)</i>(.+?)</i>(.+?)</i>'
    aResult = oParser.parse(sHtmlContent0, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            sQual = aEntry[0].replace("مشاهدة", "").replace(' ', '')
            sHtmlContent = aEntry[5]

            sHosterUrl = url_function(sHtmlContent)
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                sDisplayTitle = ('%s [COLOR coral](%sp)[/COLOR]') % (sMovieTitle, sQual)
                oHoster.setDisplayName(sDisplayTitle)
                oHoster.setFileName(sDisplayTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    else:
        sPattern = 'data-link="(.+?)" class'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            for aEntry in aResult[1]:

                url = aEntry
                if 'vtbe' in url:
                    url = url + '|Referer='+URL_MAIN
                sTitle = " "
                if url.startswith('//'):
                    url = 'http:' + url

                sHosterUrl = url
                oHoster = cHosterGui().checkHoster(sHosterUrl)
                if oHoster:
                    sDisplayTitle = sTitle
                    oHoster.setDisplayName(sDisplayTitle)
                    oHoster.setFileName(sDisplayTitle)
                    cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()


def url_function(sHtmlContent):
    oParser = cParser()

    sPattern = 'data-link="(.+?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            url = aEntry
            if 'vtbe' in url:
                url = url + '|Referer='+URL_MAIN
            sTitle = " "
            if url.startswith('//'):
                url = 'http:' + url
    return url


def main_function(sHtmlContent):
    oParser = cParser()

    sPattern = 'HomeURL = "(.+?)";'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0]):
        URL_MAIN = aResult[1][0]
    return URL_MAIN
