﻿# -*- coding: utf-8 -*-
# zombi https://github.com/zombiB/zombi-addons/


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

SITE_IDENTIFIER = 'beinsports_net'
SITE_NAME = 'Beinsports'
SITE_DESC = 'sport vod'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

SPORT_FOOT = ('https://www.beinsports.com/ar-mena/%D9%81%D9%8A%D8%AF%D9%8A%D9%88', 'showMovies')
SPORT_SPORTS = ('https://www.beinsports.com/ar/%D9%83%D8%B1%D8%A9-%D8%A7%D9%84%D9%82%D8%AF%D9%85/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88', 'showMovies')
SPORT_GENRES = ('http://', 'showGenres')
SPORT_SPORTS = ('http://', 'load')

URL_SEARCH = ('http://www.beinsports.com/ar/search?q=', 'showMovies')
FUNCTION_SEARCH = 'showMovies'


def load():
    oGui = cGui()
    addons = addon()
    oOutputParameterHandler = cOutputParameterHandler()

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30076)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/')
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', addons.VSlang(30330), 'search.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30350)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', 'http://frenchstream.org/les-plus-vues')
    oGui.addDir(SITE_IDENTIFIER, 'showGenres', 'Sports', 'foot.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSearch():
    oGui = cGui()
    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = 'http://www.beinsports.com/ar/search?q='+sSearchText+'&ft=%22%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88%22'
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showGenres():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    liste = []
    liste.append(["كرة القدم ", "https://www.beinsports.com/ar/%D9%83%D8%B1%D8%A9-%D8%A7%D9%84%D9%82%D8%AF%D9%85/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"])
    liste.append(["الدوري الإنكليزي الممتاز", "https://www.beinsports.com/ar/%D8%A7%D9%84%D8%AF%D9%88%D8%B1%D9%8A-%D8%A7%D9%84%D8%A5%D9%86%D9%83%D9%84%D9%8A%D8%B2%D9%8A-%D8%A7%D9%84%D9%85%D9%85%D8%AA%D8%A7%D8%B2/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"])
    liste.append(["دوري أبطال أوروبا", "https://www.beinsports.com/ar/%D8%AF%D9%88%D8%B1%D9%8A-%D8%A3%D8%A8%D8%B7%D8%A7%D9%84-%D8%A3%D9%88%D8%B1%D9%88%D8%A8%D8%A7/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"])
    liste.append(["الدوري-الإسباني", "https://www.beinsports.com/ar/%D8%A7%D9%84%D8%AF%D9%88%D8%B1%D9%8A-%D8%A7%D9%84%D8%A5%D8%B3%D8%A8%D8%A7%D9%86%D9%8A/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"])
    liste.append(["الدوري الإيطالي", "https://www.beinsports.com/ar/%D8%A7%D9%84%D8%AF%D9%88%D8%B1%D9%8A-%D8%A7%D9%84%D8%A5%D9%8A%D8%B7%D8%A7%D9%84%D9%8A/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"])
    liste.append(["الدوري الفرنسي", "https://www.beinsports.com/ar/%D8%A7%D9%84%D8%AF%D9%88%D8%B1%D9%8A-%D8%A7%D9%84%D9%81%D8%B1%D9%86%D8%B3%D9%8A/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"])
    liste.append(["تنس", "https://www.beinsports.com/ar/%D8%AA%D9%86%D8%B3/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"])
    liste.append(["كرة السلة", "https://www.beinsports.com/ar/%D9%83%D8%B1%D8%A9-%D8%A7%D9%84%D8%B3%D9%84%D8%A9/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"])
    liste.append(["القناة الأولمبية", "https://www.beinsports.com/ar/tag/%D8%A7%D9%84%D9%82%D9%86%D8%A7%D8%A9-%D8%A7%D9%84%D8%A3%D9%88%D9%84%D9%85%D8%A8%D9%8A%D8%A9/"])
    liste.append(["رياضات ميكانيكية", "https://www.beinsports.com/ar/%D8%B1%D9%8A%D8%A7%D8%B6%D8%A7%D8%AA-%D9%85%D9%8A%D9%83%D8%A7%D9%86%D9%8A%D9%83%D9%8A%D8%A9/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"])
    liste.append(["BOXE", "https://www.beinsports.com/ar/%D8%A7%D9%84%D9%85%D9%84%D8%A7%D9%83%D9%85%D8%A9/%D8%A7%D9%84%D9%81%D9%8A%D8%AF%D9%8A%D9%88"])

    for sTitle, sUrl in liste:

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)

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
    sHtmlContent = oRequestHandler.request()
    sPattern = 'src="(.+?)" decoding=.+?>([^<]+)</div></div><div class=.+?>([^<]+)</span><span class=.+?>([^<]+)</span></div></div></a><a class="bng-carousel-padding" href="([^<]+)"><div class='

    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            sUrl = URL_MAIN+aEntry[4]
            sTitle = aEntry[3]
            sDesc = '[COLOR aqua]'+aEntry[1]+" //[/COLOR]"+'[COLOR yellow]'+aEntry[2]+'[/COLOR]'
            if not 'http' in sUrl:
                sUrl = str(URL_MAIN) + sUrl
            sThumb = aEntry[0]

            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', str(aEntry[0]))
            oGui.addMisc(SITE_IDENTIFIER, 'showHosters', sTitle, 'doc.png', sThumb, sDesc, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    if not sSearch:
        oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oParser = cParser()

    sPattern = '<link rel="next" href="([^<]+)">'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        aResult = aResult[1][0]
        return aResult

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
    sHtmlContent = sHtmlContent.replace('\\', '')

    sPattern = ',"url":"(.+?)","thumbnail":'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:

            url = aEntry
            if url.startswith('//'):
                url = 'http:' + url
            if 'autoplay' not in url:
                url = url+'?autoplay=0+'

            sHosterUrl = url
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()
