# -*- coding: utf-8 -*-
#############################################################
# Yonn1981 https://github.com/Yonn1981/Repo
#############################################################

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

SITE_IDENTIFIER = 'bazplay'
SITE_NAME = 'BazPlay'
SITE_DESC = 'arabic vod'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)


SERIE_TR = (URL_MAIN + 'series', 'showSeries')
MOVIE_TURK = (URL_MAIN + 'movies', 'showMovies')

URL_SEARCH = (URL_MAIN + '/search/', 'showSeries')
URL_SEARCH_MOVIES = (URL_MAIN + '/search/', 'showMovies')
URL_SEARCH_SERIES = (URL_MAIN + '/search/', 'showSeries')
FUNCTION_SEARCH = 'showSeries'


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

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_TURK[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام تركية', 'turk.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30121)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', SERIE_TR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات تركية', 'turk.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + 'episodes/')
    oGui.addDir(SITE_IDENTIFIER, 'showSeries2', 'احدث الحلقات', 'turk.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + 'search/'+sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showSeriesSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + 'search/'+sSearchText
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

    sPattern = '<article class="post">.+?href="([^"]+)" title=.+?style="([^"]+)".+?<div class="title">(.+?)</div>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            if "فيلم" not in aEntry[2]:
                continue

            sTitle = aEntry[2].replace("مشاهدة", "").replace("مسلسل", "").replace("انمي", "").replace("مترجمة", "").replace("مترجم", "").replace("برنامج", "").replace("فيلم", "").replace("والأخيرة", "").replace("مدبلج للعربية", "مدبلج").replace("والاخيرة", "").replace(
                "كاملة", "").replace("حلقات كاملة", "").replace("اونلاين", "").replace("مباشرة", "").replace("انتاج ", "").replace("جودة عالية", "").replace("كامل", "").replace("HD", "").replace("السلسلة الوثائقية", "").replace("الفيلم الوثائقي", "").replace("اون لاين", "")
            siteUrl = aEntry[0]
            sThumb = re.sub(r'-\d*x\d*.', '.', aEntry[1]).replace('background-image:url(', '').replace(');', '')

            sYear = ''
            sDesc = ''

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            oGui.addMovie(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

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

    sPattern = '<div class="block-post">.+?<a href="([^<]+)" title=.+?.+?style="([^"]+)".+?<div class="title">(.+?)</div>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            if "فيلم" in aEntry[2]:
                continue

            sTitle = aEntry[2].replace("مشاهدة", "").replace("مترجمة", "").replace("مترجم", "").replace("فيلم", "").replace("اون لاين", "").replace("مشاهدة", "").replace("مسلسل", "").replace("انمي", "").replace("مترجمة", "").replace("مترجم", "").replace("فيلم", "").replace("والأخيرة", "").replace(
                "مدبلج للعربية", "مدبلج").replace("والاخيرة", "").replace("كاملة", "").replace("حلقات كاملة", "").replace("اونلاين", "").replace("مباشرة", "").replace("انتاج ", "").replace("جودة عالية", "").replace("كامل", "").replace("HD", "").replace("السلسلة الوثائقية", "").replace("الفيلم الوثائقي", "").replace("اون لاين", "")
            sTitle = sTitle.replace("الموسم العاشر", "S10").replace("الموسم الحادي عشر", "S11").replace("الموسم الثاني عشر", "S12").replace("الموسم الثالث عشر", "S13").replace("الموسم الرابع عشر", "S14").replace("الموسم الخامس عشر", "S15").replace("الموسم السادس عشر", "S16").replace("الموسم السابع عشر", "S17").replace("الموسم الثامن عشر", "S18").replace("الموسم التاسع عشر", "S19").replace("الموسم العشرون", "S20").replace("الموسم الحادي و العشرون", "S21").replace("الموسم الثاني و العشرون", "S22").replace("الموسم الثالث و العشرون", "S23").replace("الموسم الرابع والعشرون", "S24").replace("الموسم الخامس و العشرون", "S25").replace("الموسم السادس والعشرون", "S26").replace(
                "الموسم السابع والعشرون", "S27").replace("الموسم الثامن والعشرون", "S28").replace("الموسم التاسع والعشرون", "S29").replace("الموسم الثلاثون", "S30").replace("الموسم الحادي و الثلاثون", "S31").replace("الموسم الثاني والثلاثون", "S32").replace("الموسم الاول", "S1").replace("الموسم الثاني", "S2").replace("الموسم الثالث", "S3").replace("الموسم الثالث", "S3").replace("الموسم الرابع", "S4").replace("الموسم الخامس", "S5").replace("الموسم السادس", "S6").replace("الموسم السابع", "S7").replace("الموسم الثامن", "S8").replace("الموسم التاسع", "S9").replace("الموسم", "S").replace("موسم", "S").replace("S ", "S").split('الحلقة')[0]
            siteUrl = aEntry[0]
            sThumb = re.sub(r'-\d*x\d*.', '.', aEntry[1]).replace('background-image:url(', '').replace(');', '')
            sDesc = ""

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            oGui.addTV(SITE_IDENTIFIER, 'showSeasons', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    sPattern = '<div class="block-post">.+?<a href="([^<]+)" title="([^<]+)">.+?data-img="([^<]+)" title='
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            if "فيلم" in aEntry[2]:
                continue

            sTitle = aEntry[1].replace("مشاهدة", "").replace("مترجمة", "").replace("مترجم", "").replace("فيلم", "").replace("اون لاين", "").replace("مشاهدة", "").replace("مسلسل", "").replace("انمي", "").replace("مترجمة", "").replace("مترجم", "").replace("فيلم", "").replace("والأخيرة", "").replace(
                "مدبلج للعربية", "مدبلج").replace("والاخيرة", "").replace("كاملة", "").replace("حلقات كاملة", "").replace("اونلاين", "").replace("مباشرة", "").replace("انتاج ", "").replace("جودة عالية", "").replace("كامل", "").replace("HD", "").replace("السلسلة الوثائقية", "").replace("الفيلم الوثائقي", "").replace("اون لاين", "")
            sTitle = sTitle.replace("الموسم العاشر", "S10").replace("الموسم الحادي عشر", "S11").replace("الموسم الثاني عشر", "S12").replace("الموسم الثالث عشر", "S13").replace("الموسم الرابع عشر", "S14").replace("الموسم الخامس عشر", "S15").replace("الموسم السادس عشر", "S16").replace("الموسم السابع عشر", "S17").replace("الموسم الثامن عشر", "S18").replace("الموسم التاسع عشر", "S19").replace("الموسم العشرون", "S20").replace("الموسم الحادي و العشرون", "S21").replace("الموسم الثاني و العشرون", "S22").replace("الموسم الثالث و العشرون", "S23").replace("الموسم الرابع والعشرون", "S24").replace("الموسم الخامس و العشرون", "S25").replace("الموسم السادس والعشرون", "S26").replace(
                "الموسم السابع والعشرون", "S27").replace("الموسم الثامن والعشرون", "S28").replace("الموسم التاسع والعشرون", "S29").replace("الموسم الثلاثون", "S30").replace("الموسم الحادي و الثلاثون", "S31").replace("الموسم الثاني والثلاثون", "S32").replace("الموسم الاول", "S1").replace("الموسم الثاني", "S2").replace("الموسم الثالث", "S3").replace("الموسم الثالث", "S3").replace("الموسم الرابع", "S4").replace("الموسم الخامس", "S5").replace("الموسم السادس", "S6").replace("الموسم السابع", "S7").replace("الموسم الثامن", "S8").replace("الموسم التاسع", "S9").replace("الموسم", "S").replace("موسم", "S").replace("S ", "S").split('الحلقة')[0]
            siteUrl = aEntry[0]
            sThumb = aEntry[2].replace("(", "").replace(")", "")
            sDesc = ""

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            oGui.addTV(SITE_IDENTIFIER, 'showSeasons', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()


def showSeries2(sSearch=''):
    oGui = cGui()
    oParser = cParser()

    if sSearch:
        sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="block-post">.+?<a href="([^<]+)" title="([^<]+)">.+?data-img="([^<]+)" title='
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            if "فيلم" in aEntry[2]:
                continue

            sTitle = aEntry[1].replace("مشاهدة", "").replace("مترجمة", "").replace("مترجم", "").replace("فيلم", "").replace("اون لاين", "").replace("مشاهدة", "").replace("مسلسل", "").replace("انمي", "").replace("مترجمة", "").replace("مترجم", "").replace("فيلم", "").replace("والأخيرة", "").replace(
                "مدبلج للعربية", "مدبلج").replace("والاخيرة", "").replace("كاملة", "").replace("حلقات كاملة", "").replace("اونلاين", "").replace("مباشرة", "").replace("انتاج ", "").replace("جودة عالية", "").replace("كامل", "").replace("HD", "").replace("السلسلة الوثائقية", "").replace("الفيلم الوثائقي", "").replace("اون لاين", "")
            sTitle = sTitle.replace("الموسم العاشر", "S10").replace("الموسم الحادي عشر", "S11").replace("الموسم الثاني عشر", "S12").replace("الموسم الثالث عشر", "S13").replace("الموسم الرابع عشر", "S14").replace("الموسم الخامس عشر", "S15").replace("الموسم السادس عشر", "S16").replace("الموسم السابع عشر", "S17").replace("الموسم الثامن عشر", "S18").replace("الموسم التاسع عشر", "S19").replace("الموسم العشرون", "S20").replace("الموسم الحادي و العشرون", "S21").replace("الموسم الثاني و العشرون", "S22").replace("الموسم الثالث و العشرون", "S23").replace("الموسم الرابع والعشرون", "S24").replace("الموسم الخامس و العشرون", "S25").replace(
                "الموسم السادس والعشرون", "S26").replace("الموسم السابع والعشرون", "S27").replace("الموسم الثامن والعشرون", "S28").replace("الموسم التاسع والعشرون", "S29").replace("الموسم الثلاثون", "S30").replace("الموسم الحادي و الثلاثون", "S31").replace("الموسم الثاني والثلاثون", "S32").replace("الموسم الاول", "S1").replace("الموسم الثاني", "S2").replace("الموسم الثالث", "S3").replace("الموسم الثالث", "S3").replace("الموسم الرابع", "S4").replace("الموسم الخامس", "S5").replace("الموسم السادس", "S6").replace("الموسم السابع", "S7").replace("الموسم الثامن", "S8").replace("الموسم التاسع", "S9").replace("الموسم", "S").replace("موسم", "S").replace("S ", "S")
            siteUrl = aEntry[0]
            sThumb = aEntry[2].replace("(", "").replace(")", "")
            sDesc = ""

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            oGui.addTV(SITE_IDENTIFIER, 'showSeasons', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries2', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()


def showSeasons():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = 'data-season="(.+?)">(.+?)</li>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:
            siteUrl = URL_MAIN+'wp-content/themes/vo2023/temp/ajax/seasons.php?seriesID='+aEntry[0]
            sTitle = sMovieTitle + aEntry[1].replace("الموسم العاشر", "S10").replace("الموسم الحادي عشر", "S11").replace("الموسم الثاني عشر", "S12").replace("الموسم الثالث عشر", "S13").replace("الموسم الرابع عشر", "S14").replace("الموسم الخامس عشر", "S15").replace("الموسم السادس عشر", "S16").replace("الموسم السابع عشر", "S17").replace("الموسم الثامن عشر", "S18").replace("الموسم التاسع عشر", "S19").replace("الموسم العشرون", "S20").replace("الموسم الحادي و العشرون", "S21").replace("الموسم الثاني و العشرون", "S22").replace("الموسم الثالث و العشرون", "S23").replace("الموسم الرابع والعشرون", "S24").replace("الموسم الخامس و العشرون", "S25").replace("الموسم السادس والعشرون", "S26").replace(
                "الموسم السابع والعشرون", "S27").replace("الموسم الثامن والعشرون", "S28").replace("الموسم التاسع والعشرون", "S29").replace("الموسم الثلاثون", "S30").replace("الموسم الحادي و الثلاثون", "S31").replace("الموسم الثاني والثلاثون", "S32").replace("الموسم الأول", "S1").replace("الموسم الاول", "S1").replace("الموسم الثاني", "S2").replace("الموسم الثالث", "S3").replace("الموسم الثالث", "S3").replace("الموسم الرابع", "S4").replace("الموسم الخامس", "S5").replace("الموسم السادس", "S6").replace("الموسم السابع", "S7").replace("الموسم الثامن", "S8").replace("الموسم التاسع", "S9").replace("الموسم", "S").replace("موسم", "S").replace("S ", "S").split('الحلقة')[0]

            sThumb = sThumb
            sDesc = ''

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('siteUrl0', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oGui.addSeason(SITE_IDENTIFIER, 'showEps', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    else:
        sPattern = '<a class="epNum" href="([^"]+)" title="([^"]+)'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            oOutputParameterHandler = cOutputParameterHandler()
            for aEntry in aResult[1]:

                sTitle = sMovieTitle + aEntry[1].replace('الحلقة', 'E').replace("الموسم", "S")
                siteUrl = aEntry[0]
                sThumb = sThumb
                sDesc = ''

                oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                oOutputParameterHandler.addParameter('sThumb', sThumb)
                oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        sPattern = '<a class="epNum.+?" href="([^"]+)" title="([^"]+)'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            oOutputParameterHandler = cOutputParameterHandler()
            for aEntry in aResult[1]:

                sTitle = sMovieTitle + aEntry[1].replace('الحلقة', 'E').replace("الموسم", "S")
                siteUrl = aEntry[0]
                sThumb = sThumb
                sDesc = ''

                oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                oOutputParameterHandler.addParameter('sThumb', sThumb)
                oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oParser = cParser()

    sPattern = '<link rel="next" href="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:

        return aResult[1][0]
    else:
        sPattern = "<span class='current'>.+?<a href='([^']+)"
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            return aResult[1][0]

    return False


def showEps():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sUrl0 = oInputParameterHandler.getValue('siteUrl0')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    St = requests.Session()
    oRequestHandler = cRequestHandler(sUrl0)
    sHtmlContent = oRequestHandler.request()

    siteUrl = str(sUrl).split('?')[0]

    sCode = sUrl.split('seriesID=')[1]
    cook = oRequestHandler.GetCookies()
    hdr = {'x-requested-with': 'XMLHttpRequest', 'accept': '*/*', 'Authority': 'bazplay.cc', 'Cookie': cook}
    params = {'seriesID': sCode}

    sHtmlContent = St.get(siteUrl, headers=hdr, params=params)
    sHtmlContent = sHtmlContent.content

    sPattern = 'href="([^"]+)".+?<span>(.+?)</span>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            sTitle = sMovieTitle + ' E'+aEntry[1].replace("مشاهدة", "").replace("مسلسل", "").replace("انمي", "").replace("مترجمة", "").replace("مترجم",
                                                                                                                                               "").replace("الموسم", " S").replace("S ", "S").replace("الحلقة ", " E").replace("حلقة ", " E")
            siteUrl = aEntry[0]
            sThumb = sThumb
            sDesc = ''

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            oGui.addEpisode(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

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

    sPattern = '<form method="post" action="([^"]+)".+?name="watch" value="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            wcode = aEntry[1]
            sLink = aEntry[0]

        s = requests.Session()
        headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36 Edg/115.0.1901.188',
                   'origin': 'https://bazplay.cc',
                   'referer': URL_MAIN,
                   'sec-fetch-dest': 'document',
                   'sec-fetch-mode': 'navigate',
                   'sec-fetch-site': 'cross-site',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'}

        data = {'watch': wcode, 'submit': ''}
        r = s.post(sLink, headers=headers, data=data)
        sHtmlContent = r.content.decode('utf8')

        sPattern = 'data-src=["\']([^"\']+)["\']'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            for aEntry in (aResult[1]):
                url = aEntry
                sThumb = ''
                if url.startswith('//'):
                    url = 'http:' + url

                sHosterUrl = url

                oHoster = cHosterGui().checkHoster(sHosterUrl)
                if oHoster != False:
                    oHoster.setDisplayName(sMovieTitle)
                    oHoster.setFileName(sMovieTitle)
                    cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()
