﻿# -*- coding: utf-8 -*-
#############################################################
# Yonn1981 https://github.com/Yonn1981/Repo
#############################################################


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

SITE_IDENTIFIER = 'karbala'
SITE_NAME = 'Karbala TV'
SITE_DESC = 'arabic vod'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

ISLAM_SHOWS = (URL_MAIN+'?partName=Lectures', 'showSeries')
ISLAM_QURAN = (URL_MAIN+'?partName=Quran', 'showSeries')
ISLAM_NASHEED = (URL_MAIN+'?partName=poems', 'showSeries')
ISLAM_GENRES = (URL_MAIN, 'showGenres')


def load():
    oGui = cGui()
    addons = addon()
    oOutputParameterHandler = cOutputParameterHandler()

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(70003)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', ISLAM_QURAN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'القرآن الكريم', 'quran.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', ISLAM_SHOWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'دروس و محاضرات', 'brmg.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', ISLAM_NASHEED[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'قصائد و أناشيد', 'nsheed.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', ISLAM_GENRES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showGenres', 'أقسام المكتبة المرئية', 'islm.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showGenres():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    liste = []

    liste.append(['ادعية و زيارات', URL_MAIN + '?partName=Pra_Vis'])
    liste.append(['برامج دينية', URL_MAIN + '?partName=religious'])
    liste.append(['برامج حسينية', URL_MAIN + '?partName=hussien'])
    liste.append(['برامج ثقافية', URL_MAIN + '?partName=educational'])
    liste.append(['أفلام و مسلسلات', URL_MAIN + '?partName=series'])
    liste.append(['الاسرة و الطفل', URL_MAIN + '?partName=family'])

    for sTitle, sUrl in liste:

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addDir(SITE_IDENTIFIER, 'showSeries', sTitle, 'islm.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSeries(sSearch=''):
    oGui = cGui()
    oParser = cParser()

    if sSearch:
        sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
        sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
        sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<div class="col-md-3 taa">.+?href="([^"]+)".+?style="background-image:.+?["\']([^"\']+)["\'].+?<h3 class=".+?">(.+?)</h3>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] is True:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            sTitle = aEntry[2]
            sYear = ''
            siteUrl = URL_MAIN+aEntry[0]
            sThumb = URL_MAIN.split('/video')[0] + aEntry[1]
            sDesc = ''

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oOutputParameterHandler.addParameter('sYear', sYear)
            oOutputParameterHandler.addParameter('sDesc', sDesc)

            oGui.addTV(SITE_IDENTIFIER, 'showEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

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

    sPattern = '<div class="col-md-3 taa">.+?href="([^"]+)" title="([^"]+)".+?background:url(.+?);'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0] is True:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            sTitle = aEntry[1]
            siteUrl = URL_MAIN.split('video')[0] + aEntry[0]
            sThumb = URL_MAIN.split('/video')[0] + aEntry[2].replace("(", "").replace(")", "")
            sDesc = ""

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oGui.addEpisode(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
    else:
        oGui.addText(SITE_IDENTIFIER, '[COLOR coral]'+'عذرا , لا يمكن تنفيذ هذا الطلب'+'[/COLOR]')
        sNextPage = __checkForNextPage(sHtmlContent)
        if sNextPage:
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showEpisodes', '[COLOR teal]Next >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    oParser = cParser()

    sPattern = '<b class="current".+?href="(.+?)"'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        return URL_MAIN + aResult[1][0]


def showLinks():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<source src="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            sHosterUrl = URL_MAIN.split('/video')[0] + aEntry

            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()
