﻿# -*- coding: utf-8 -*-
# zombi https://github.com/zombiB/zombi-addons/


from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import \
    siteManager
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

SITE_IDENTIFIER = 'beinmatch'
SITE_NAME = 'Beinmatch'
SITE_DESC = 'arabic vod'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

SPORT_LIVE = (URL_MAIN, 'showMovies')


def load():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SPORT_LIVE[0])

    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'بث مباشر و أهداف و ملخصات', 'sport.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovies(sSearch=''):
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<link rel="canonical" href="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        mSite = aResult[1][0]

    sPattern = 'onclick="goToMatch\((.+?)\,["\']([^"\']+)["\']\);".+?<span class="matchTime">([^<]+)</span>'
    sPattern += '.+?<img class="imgTeam" src=["\']([^"\']+)["\'].+?class="textMatch">(.+?)</div>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            sTitle = aEntry[1].replace('_', ' ')
            sThumb = ''
            if aEntry[3]:
                sThumb = aEntry[3]
            siteUrl = mSite+"bein/live/"+aEntry[0]
            if siteUrl.startswith('//'):
                siteUrl = 'http:' + aEntry[0]
            sDesc = aEntry[2]
            if aEntry[4]:
                sDesc = aEntry[2] + "\n \nوقت المباراة: "+aEntry[4]

            oOutputParameterHandler.addParameter('siteUrl', siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            oGui.addMisc(SITE_IDENTIFIER, 'showLive', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showLive():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<link rel="canonical" href="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        mSite = aResult[1][0]

    sStart = '<div id="contentBody">'
    sEnd = '<div id="leftSide">'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)

    sPattern = 'source: "(.+?)",'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            url = aEntry
            sHosterUrl = url
            sMovieTitle = sMovieTitle
            if 'vimeo' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + mSite
            if 'akamaized' in sHosterUrl:
                sHosterUrl = sHosterUrl
            else:
                sHosterUrl = sHosterUrl + '|Referer=' + mSite
            if sHosterUrl.startswith('//'):
                sHosterUrl = 'http:' + sHosterUrl

            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    sPattern = '><iframe.+?src="([^"]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:

            url = aEntry
            if '.php' in url:
                oRequestHandler = cRequestHandler(url)
                sHtmlContent1 = oRequestHandler.request()
                sPattern = 'src="([^"]+)'
                aResult = oParser.parse(sHtmlContent1, sPattern)
                if aResult[0]:
                    url = aResult[1][0]

                    sHosterUrl = url
                    sMovieTitle = sMovieTitle
                    if 'vimeo' in sHosterUrl:
                        sHosterUrl = sHosterUrl + "|Referer=" + mSite

                    oHoster = cHosterGui().checkHoster(sHosterUrl)
                    if oHoster:
                        oHoster.setDisplayName(sMovieTitle)
                        oHoster.setFileName(sMovieTitle)
                        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
            if 'youtube' in url:
                url = url.split('?')[0]

            sHosterUrl = url
            sMovieTitle = sMovieTitle
            if 'vimeo' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + mSite

            if sHosterUrl.startswith('//'):
                sHosterUrl = 'http:' + sHosterUrl

            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                oHoster.setDisplayName(sMovieTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    sPattern = 'onclick="goToLink(.+?), (.+?),'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:

        for aEntry in aResult[1]:
            siteUrl = mSite+"bein/live/"+aEntry[0].replace("(", "")
            siteUrl = siteUrl+'/'+aEntry[1]
            oRequestHandler = cRequestHandler(siteUrl)
            sHtmlContent0 = oRequestHandler.request()

            sStart = '<div id="contentBody">'
            sEnd = '<div id="leftSide">'
            sHtmlContent0 = oParser.abParse(sHtmlContent0, sStart, sEnd)

            sPattern = '<iframe.+?src="([^"]+)'
            aResult = oParser.parse(sHtmlContent0, sPattern)
            if aResult[0]:
                for aEntry in aResult[1]:
                    url = aEntry
                    sHosterUrl = url
                    sDisplayTitle = sMovieTitle

                    if sHosterUrl.startswith('//'):
                        sHosterUrl = 'http:' + sHosterUrl
                    sHosterUrl = sHosterUrl + '|Referer=' + mSite
                    oHoster = cHosterGui().checkHoster(sHosterUrl)
                    if oHoster:
                        oHoster.setDisplayName(sDisplayTitle)
                        oHoster.setFileName(sMovieTitle)
                        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    sPattern = 'href="javascript:goToMatch(.+?), (.+?),.+?>(.+?)</a>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            sTitle = aEntry[2]
            siteUrl = mSite+"bein/live/"+aEntry[0].replace("(", "")
            siteUrl = siteUrl+'/'+aEntry[1]
            oRequestHandler = cRequestHandler(siteUrl)
            sHtmlContent2 = oRequestHandler.request()

            sPattern = '<iframe.+?src="([^"]+)'
            aResult = oParser.parse(sHtmlContent2, sPattern)
            if aResult[0]:
                for aEntry in aResult[1]:
                    url = aEntry
                    sHosterUrl = url
                    sDisplayTitle = sMovieTitle+' - '+sTitle

                    if sHosterUrl.startswith('//'):
                        sHosterUrl = 'http:' + sHosterUrl
                    sHosterUrl = sHosterUrl + '|Referer=' + mSite
                    oHoster = cHosterGui().checkHoster(sHosterUrl)
                    if oHoster:
                        oHoster.setDisplayName(sDisplayTitle)
                        oHoster.setFileName(sMovieTitle)
                        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

            sPattern = 'source: "(.+?)",'
            aResult = oParser.parse(sHtmlContent, sPattern)
            if aResult[0]:
                for aEntry in aResult[1]:

                    url = aEntry
                    sHosterUrl = url
                    sDisplayTitle = sMovieTitle+' - '+sTitle

                    if sHosterUrl.startswith('//'):
                        sHosterUrl = 'http:' + sHosterUrl
                    sHosterUrl = sHosterUrl + '|Referer=' + mSite
                    oHoster = cHosterGui().checkHoster(sHosterUrl)
                    if oHoster:
                        oHoster.setDisplayName(sDisplayTitle)
                        oHoster.setFileName(sMovieTitle)
                        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)
    else:
        sPattern = 'id="video-container".+?<video.+?src="([^"]+)'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            for aEntry in aResult[1]:

                sHosterUrl = aEntry
                if sHosterUrl.startswith('//'):
                    sHosterUrl = 'http:' + sHosterUrl

                oHoster = cHosterGui().checkHoster(sHosterUrl)
                if oHoster:
                    oHoster.setDisplayName('لم يتم بعد وضع بث لهذه المباراة')
                    oHoster.setFileName(sMovieTitle)
                    cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

        sPattern = 'itemprop="embedUrl" content="([^"]+)'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            for aEntry in aResult[1]:

                sHosterUrl = aEntry
                if sHosterUrl.startswith('//'):
                    sHosterUrl = 'http:' + sHosterUrl

                oHoster = cHosterGui().checkHoster(sHosterUrl)
                if oHoster:
                    oHoster.setDisplayName('شاهد الاهداف')
                    oHoster.setFileName(sMovieTitle)
                    cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()
