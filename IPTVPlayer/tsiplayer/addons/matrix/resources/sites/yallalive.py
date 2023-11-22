﻿# -*- coding: utf-8 -*-
# zombi https://github.com/zombiB/zombi-addons/

import base64
import re

import requests
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import (
    isMatrix, siteManager)
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
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.packer import \
    cPacker
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.util import \
    Quote

SITE_IDENTIFIER = 'yallalive'
SITE_NAME = 'Yallalive'
SITE_DESC = 'arabic vod'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

SPORT_LIVE = (URL_MAIN, 'showMovies')

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60'

def load():
    oGui = cGui()
    oOutputParameterHandler = cOutputParameterHandler()

    oOutputParameterHandler.addParameter('siteUrl', SPORT_LIVE[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'بث مباشر', 'sport.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovies():
    oGui = cGui()
    oParser = cParser()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sStart = '<div id="today"'
    sEnd = '<div id="tommorw"'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)

    sPattern = '<div class="AF_Match.+?class="AF_TeamName.+?>(.+?)</div>.+?class="AF_EvTime">(.+?)</div>.+?<div class="AF_TeamName.+?>(.+?)</div>.+?href="([^"]+)".+?<div class="AF_MaskText">(.+?)</div>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        oOutputParameterHandler = cOutputParameterHandler()
        for aEntry in aResult[1]:

            sTitle =  aEntry[0] +' - '+ aEntry[2]
            sThumb = ""
            siteUrl =  aEntry[3]
            sDesc = aEntry[1]+ " KSA \n \n"+aEntry[4]

            oOutputParameterHandler.addParameter('siteUrl',siteUrl)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oGui.addMisc(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()

def showHosters():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    sHosterUrl = ''

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = "redirectUrl='(.+?)';"
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0]):
        sUrl = aResult[1][0]

    oRequestHandler = cRequestHandler(sUrl)
    hdr = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36','Origin' : 'yallalive.id','Referer' : 'https://yallalive.id/'}
    St=requests.Session()
    sHtmlContent = St.get(sUrl,headers=hdr).content.decode('utf-8')

    sPattern = 'href="(.+?)" target="search_iframe">(.+?)</a>'
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:
            sTitle = sMovieTitle+' '+aEntry[1]
            url = aEntry[0]
            if '.m3u8' in url:
                sHosterUrl = url.split('=')[1]
            if 'embed' in url:
                oRequestHandler = cRequestHandler(url)
                sHtmlContent2 = St.get(url).content

                sPattern =  'src="(.+?)" scrolling="no">'
                aResult = oParser.parse(sHtmlContent2,sPattern)
                if aResult[0]:
                    sHosterUrl = aResult[1][0]
            if '/dash/' in url:
                oRequestHandler = cRequestHandler(url)
                sHtmlContent4 = St.get(url).content
                regx = '''var s = '(.+?)';.+?url="(.+?)".+?s;'''
                var = re.findall(regx,sHtmlContent4,re.S)
                if var:
                    a = var[0][0]
                    a = a.replace('\\','')
                    b = var[0][1]
                    url = 'https://video-a-sjc.xx.fbcdn.net/hvideo-ash66'+a
                sHosterUrl = url+ '|Referer=' + URL_MAIN
                Referer = aEntry[0].split('live')[0]

            if 'amazonaws.com'  in url:
                sHosterUrl = url + '|User-Agent=' + "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36" + '&Referer='+Referer
            if 'vimeo' in url:
                sHosterUrl = sHosterUrl + "|Referer=" + sUrl

            if 'sharecast' in url:
                Referer =  "https://sharecast.ws/"
                sHosterUrl = Hoster_ShareCast(url, Referer)

            if ".php" or ".html" in url:
                oRequestHandler = cRequestHandler(url)
                oRequestHandler.addHeaderEntry('Referer', sUrl)
                data = oRequestHandler.request()
                sPattern = "source:\s*'(.+?)',"
                aResult = oParser.parse(data, sPattern)
                if aResult[0]:
                    for aEntry in aResult[1]:
                        sHosterUrl = aEntry
            else:
                sHosterUrl = getHosterIframe(url, sUrl)

            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                oHoster.setDisplayName(sTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    sPattern = "'link': u'(.+?)',"
    aResult = oParser.parse(sHtmlContent, sPattern)
    if aResult[0]:
        for aEntry in aResult[1]:

            url = aEntry
            if '.php?' in url:
                oRequestHandler = cRequestHandler(url)
                sHtmlContent2 = St.get(url).content

                sPattern =  'source: "(.+?)",'
                aResult = oParser.parse(sHtmlContent2,sPattern)
                if aResult[0]:
                    url = aResult[1][0]
            if 'embed' in url:
                oRequestHandler = cRequestHandler(url)
                sHtmlContent2 = St.get(url).content

                sPattern =  'src="(.+?)" scrolling="no">'
                aResult = oParser.parse(sHtmlContent2,sPattern)
                if aResult[0]:
                    url = aResult[1][0]
            if 'multi.html' in url:
                url2 = url.split('=')
                live = url2[1].replace("&ch","")
                ch = url2[2]
                oRequestHandler = cRequestHandler(url)
                sHtmlContent2 = St.get(url).content

                sPattern =  "var src = (.+?),"
                aResult = oParser.parse(sHtmlContent2,sPattern)
                if aResult[0]:
                    url2 = aResult[1][0].split('hls:')
                    url2 = url2[1].split('+')
                    url2 = url2[0].replace("'","")
                    url = url2+live+'/'+ch+'.m3u8'
            if '/dash/' in url:
                oRequestHandler = cRequestHandler(url)
                sHtmlContent4 = St.get(url).content
                regx = '''var s = '(.+?)';.+?url="(.+?)".+?s;'''
                var = re.findall(regx,sHtmlContent4,re.S)
                if var:
                    a = var[0][0]
                    a = a.replace('\\','')
                    b = var[0][1]
                    url = 'https://video-a-sjc.xx.fbcdn.net/hvideo-ash66'+a
            sHosterUrl = url+ '|User-Agent=' + "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36" + '&Referer=' + URL_MAIN
            sMovieTitle = 'link'
            if 'vimeo' in sHosterUrl:
                sHosterUrl = sHosterUrl + "|Referer=" + sUrl

            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if oHoster:
                oHoster.setDisplayName(sMovieTitle+' '+sTitle)
                oHoster.setFileName(sMovieTitle)
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()

def Hoster_ShareCast(url, referer):
    oRequestHandler = cRequestHandler(url)
    oRequestHandler.addHeaderEntry('User-Agent', UA)
    oRequestHandler.addHeaderEntry('Referer', referer)
    sHtmlContent = oRequestHandler.request()

    sPattern = "new Player\(.+?player\",\"([^\"]+)\",{'([^\']+)"
    aResult = re.findall(sPattern, sHtmlContent)

    if aResult:
        site = 'https://' + aResult[0][1]
        url = (site + '/hls/' + aResult[0][0]  + '/live.m3u8') + '|Referer=' + Quote(site)
        return url

    return False, False

def getHosterIframe(url, referer):
    oRequestHandler = cRequestHandler(url)
    oRequestHandler.addHeaderEntry('Referer', referer)
    sHtmlContent = str(oRequestHandler.request())
    if not sHtmlContent:
        return False

    referer = url
    if 'channel' in referer:
        referer = referer.split('channel')[0]

    sPattern = '(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        sstr = aResult[0]
        if not sstr.endswith(';'):
            sstr = sstr + ';'
        sHtmlContent = cPacker().unpack(sstr)

    sPattern = '.atob\("(.+?)"'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        code = aResult[0]
        try:
            if isMatrix():
                code = base64.b64decode(code).decode('ascii')
            else:
                code = base64.b64decode(code)
            return code + '|Referer=' + referer
        except Exception as e:
            pass

    sPattern = '<iframe.+?src=["\']([^"\']+)["\']'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        for url in aResult:
            if url.startswith("./"):
                url = url[1:]
            if not url.startswith("http"):
                if not url.startswith("//"):
                    url = '//'+referer.split('/')[2] + url
                url = "https:" + url
            url = getHosterIframe(url, referer)
            if url:
                return url

    sPattern = 'src=["\']([^"\']+)["\']'
    aResult = re.findall(sPattern, sHtmlContent)

    if aResult:
        url = aResult[0]
        if '.m3u8' in url:
            return url

    sPattern = '<iframe.+?src=["\']([^"\']+)["\']'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        return aResult[0] +'|Referer='+referer

    sPattern = 'source:\s*["\']([^"\']+)["\']'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        return aResult[0] + '|referer=' + referer

    sPattern = '[^/]source.+?["\'](https.+?)["\']'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        return aResult[0] + '|referer=' + referer

    sPattern = 'file: *["\'](https.+?\.m3u8)["\']'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        return aResult[0] + '|referer=' + referer

    sPattern = "onload=\"ThePlayerJS\('.+?','([^\']+)"
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        url = 'https://sharecast.ws/player/' + aResult[0]
        b, url = Hoster_ShareCast(url, referer)
        if b:
            return True, url

    sPattern = '[^/]source.+?["\'](https.+?)["\']'
    aResult = re.findall(sPattern, sHtmlContent)
    if aResult:
        return True, aResult[0] + '|referer=' + url


    return False
