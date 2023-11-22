﻿# -*- coding: utf-8 -*-
# zombi https://github.com/zombiB/zombi-addons/
#############################################################
# Yonn1981 https://github.com/Yonn1981/Repo
#############################################################
# big thx to Rgysoft for this code
# From this url https://gitlab.com/Rgysoft/iptv-host-e2iplayer/-/blob/master/IPTVPlayer/tsiplayer/host_faselhd.py
#############################################################

import base64
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

SITE_IDENTIFIER = 'cimanow'
SITE_NAME = 'Cimanow'
SITE_DESC = 'arabic vod'

UA = 'ipad'

URL_MAIN = siteManager().getUrlMain(SITE_IDENTIFIER)

MOVIE_EN = (URL_MAIN + '/category/افلام-اجنبية/', 'showMovies')
MOVIE_AR = (URL_MAIN + '/category/%D8%A7%D9%81%D9%84%D8%A7%D9%85-%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9/', 'showMovies')

MOVIE_HI = (URL_MAIN + '/category/%d8%a7%d9%84%d8%a7%d9%81%d9%84%d8%a7%d9%85/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d9%87%d9%86%d8%af%d9%8a%d8%a9/', 'showMovies')

MOVIE_TURK = (URL_MAIN + '/category/%d8%a7%d9%84%d8%a7%d9%81%d9%84%d8%a7%d9%85/%d8%a7%d9%81%d9%84%d8%a7%d9%85-%d8%aa%d8%b1%d9%83%d9%8a%d8%a9/', 'showMovies')
KID_MOVIES = (URL_MAIN + '/category/افلام-انيميشن/', 'showMovies')
SERIE_TR = (URL_MAIN + '/category/%d8%a7%d9%84%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%aa%d8%b1%d9%83%d9%8a%d8%a9/', 'showSeries')

RAMADAN_SERIES = (URL_MAIN + '/category/رمضان-2023/', 'showSeries')
SERIE_EN = (URL_MAIN + '/category/%d8%a7%d9%84%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%a7%d8%ac%d9%86%d8%a8%d9%8a%d8%a9/', 'showSeries')
SERIE_AR = (URL_MAIN + '/category/%d8%a7%d9%84%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa/%d9%85%d8%b3%d9%84%d8%b3%d9%84%d8%a7%d8%aa-%d8%b9%d8%b1%d8%a8%d9%8a%d8%a9/', 'showSeries')
ANIM_NEWS = (URL_MAIN + '/category/مسلسلات-انيميشن/', 'showSeries')

DOC_NEWS = (URL_MAIN + '/?s=%D9%88%D8%AB%D8%A7%D8%A6%D9%82%D9%8A', 'showMovies')

REPLAYTV_NEWS = (URL_MAIN + '/category/%d8%a7%d9%84%d8%a8%d8%b1%d8%a7%d9%85%d8%ac-%d8%a7%d9%84%d8%aa%d9%84%d9%81%d8%b2%d9%8a%d9%88%d9%86%d9%8a%d8%a9/', 'showMovies')
URL_SEARCH = (URL_MAIN + '/?s=', 'showMovies')
URL_SEARCH_MOVIES = (URL_MAIN + '/?s=%D9%81%D9%8A%D9%84%D9%85+', 'showMovies')
URL_SEARCH_SERIES = (URL_MAIN + '/?s=%D9%85%D8%B3%D9%84%D8%B3%D9%84+', 'showSeries')
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

    oOutputParameterHandler.addParameter('siteUrl', DOC_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام وثائقية', 'doc.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام أجنبية', 'agnab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام عربية', 'arab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_TURK[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام تركية', 'turk.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', MOVIE_HI[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام هندية', 'hend.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', KID_MOVIES[0])
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'أفلام كرتون', 'crtoon.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30121)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + '/category/رمضان-2022/')
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'رمضان 2022', 'rmdn.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_EN[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات أجنبية', 'agnab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_AR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات عربية', 'arab.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', SERIE_TR[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات تركية', 'turk.png', oOutputParameterHandler)

    oOutputParameterHandler.addParameter('siteUrl', ANIM_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'مسلسلات إنمي', 'anime.png', oOutputParameterHandler)

    oGui.addText(SITE_IDENTIFIER, '[COLOR olive]-----●★| ' + addons.VSlang(30350)+' |★●-----[/COLOR]')

    oOutputParameterHandler.addParameter('siteUrl', REPLAYTV_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'برامج تلفزيونية', 'brmg.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/?s=%D9%81%D9%8A%D9%84%D9%85+'+sSearchText
        showMovies(sUrl)
        oGui.setEndOfDirectory()
        return


def showSeriesSearch():
    oGui = cGui()

    sSearchText = oGui.showKeyBoard()
    if sSearchText:
        sUrl = URL_MAIN + '/?s=%D9%85%D8%B3%D9%84%D8%B3%D9%84+'+sSearchText
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

    oRequest = cRequestHandler(sUrl)
    data = oRequest.request()

    if 'adilbo' in data:
        t_script = re.findall('<script.*?;.*?\'(.*?);', data, re.S)
        t_int = re.findall('/g.....(.*?)\)', data, re.S)
        if t_script and t_int:
            script = t_script[0].replace("'", '')
            script = script.replace("+", '')
            script = script.replace("\n", '')
            sc = script.split('.')
            page = ''
            for elm in sc:
                c_elm = base64.b64decode(elm+'==').decode()
                t_ch = re.findall('\d+', c_elm, re.S)
                if t_ch:
                    nb = int(t_ch[0])+int(t_int[0])
                    page = page + chr(nb)

            sPattern = '<article aria-label="post"><a href="([^<]+)">.+?<li aria-label="year">(.+?)</li>.+?<li aria-label="title">([^<]+)<em>.+?data-src="(.+?)" width'
            aResult = oParser.parse(page, sPattern)
            if aResult[0]:
                oOutputParameterHandler = cOutputParameterHandler()
                for aEntry in aResult[1]:

                    sTitle = aEntry[2].replace("مشاهدة", "").replace("مسلسل", "").replace("انمي", "").replace("مترجمة", "").replace("مترجم", "").replace("برنامج", "").replace("فيلم", "").replace("والأخيرة", "").replace("مدبلج للعربية", "مدبلج").replace("والاخيرة", "").replace(
                        "كاملة", "").replace("حلقات كاملة", "").replace("اونلاين", "").replace("مباشرة", "").replace("انتاج ", "").replace("جودة عالية", "").replace("كامل", "").replace("HD", "").replace("السلسلة الوثائقية", "").replace("الفيلم الوثائقي", "").replace("اون لاين", "")
                    siteUrl = aEntry[0] + '/watching/'
                    sThumb = aEntry[3]
                    if sThumb.startswith('//'):
                        sThumb = 'http:' + sThumb
                    sYear = aEntry[1]
                    sDesc = ''

                    oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)
                    oOutputParameterHandler.addParameter('sYear', sYear)
                    oOutputParameterHandler.addParameter('sDesc', sDesc)

                    oGui.addMovie(SITE_IDENTIFIER, 'showServer', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

            sStart = '</section>'
            sEnd = '</ul>'
            page = oParser.abParse(page, sStart, sEnd)

            sPattern = '<li><a href="(.+?)">(.+?)</a>'
            aResult = oParser.parse(page, sPattern)
            if aResult[0]:
                oOutputParameterHandler = cOutputParameterHandler()
                for aEntry in aResult[1]:

                    sTitle = aEntry[1]

                    sTitle = "PAGE " + sTitle
                    sTitle = '[COLOR red]'+sTitle+'[/COLOR]'
                    siteUrl = aEntry[0]
                    sThumb = ""

                    oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)

                    oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, '', oOutputParameterHandler)

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

    oRequest = cRequestHandler(sUrl)
    data = oRequest.request()

    if 'adilbo' in data:
        t_script = re.findall('<script.*?;.*?\'(.*?);', data, re.S)
        t_int = re.findall('/g.....(.*?)\)', data, re.S)
        if t_script and t_int:
            script = t_script[0].replace("'", '')
            script = script.replace("+", '')
            script = script.replace("\n", '')
            sc = script.split('.')
            page = ''
            for elm in sc:
                c_elm = base64.b64decode(elm+'==').decode()
                t_ch = re.findall('\d+', c_elm, re.S)
                if t_ch:
                    nb = int(t_ch[0])+int(t_int[0])
                    page = page + chr(nb)

            sPattern = '<article aria-label="post"><a href="([^<]+)">.+?<li aria-label="year">(.+?)</li>.+?<li aria-label="title">([^<]+)<em>.+?data-src="(.+?)" width'
            aResult = oParser.parse(page, sPattern)
            itemList = []
            if aResult[0]:
                oOutputParameterHandler = cOutputParameterHandler()
                for aEntry in aResult[1]:

                    if "فيلم" in aEntry[2]:
                        continue

                    sTitle = aEntry[2]
                    siteUrl = aEntry[0]
                    sThumb = aEntry[3]
                    if sThumb.startswith('//'):
                        sThumb = 'http:' + sThumb
                    sDesc = ''
                    sYear = aEntry[1]

                    if sTitle not in itemList:
                        itemList.append(sTitle)

                        oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                        oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                        oOutputParameterHandler.addParameter('sThumb', sThumb)
                        oOutputParameterHandler.addParameter('sYear', sYear)
                        oOutputParameterHandler.addParameter('sDesc', sDesc)

                        oGui.addTV(SITE_IDENTIFIER, 'showSeasons', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

            sStart = '</section>'
            sEnd = '</ul>'
            page = oParser.abParse(page, sStart, sEnd)

            sPattern = '<li><a href="(.+?)">(.+?)</a>'
            aResult = oParser.parse(page, sPattern)
            if aResult[0]:
                oOutputParameterHandler = cOutputParameterHandler()
                for aEntry in aResult[1]:

                    sTitle = aEntry[1]

                    sTitle = "PAGE " + sTitle
                    sTitle = '[COLOR red]'+sTitle+'[/COLOR]'
                    siteUrl = aEntry[0]
                    sThumb = ""

                    oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)

                    oGui.addDir(SITE_IDENTIFIER, 'showSeries', sTitle, '', oOutputParameterHandler)

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

    sStart = '<section aria-label="seasons">'
    sEnd = '<ul class="tabcontent" id="related">'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)

    oRequest = cRequestHandler(sUrl)
    data = oRequest.request()

    if 'adilbo' in data:
        t_script = re.findall('<script.*?;.*?\'(.*?);', data, re.S)
        t_int = re.findall('/g.....(.*?)\)', data, re.S)
        if t_script and t_int:
            script = t_script[0].replace("'", '')
            script = script.replace("+", '')
            script = script.replace("\n", '')
            sc = script.split('.')
            page = ''
            for elm in sc:
                c_elm = base64.b64decode(elm+'==').decode()
                t_ch = re.findall('\d+', c_elm, re.S)
                if t_ch:
                    nb = int(t_ch[0])+int(t_int[0])
                    page = page + chr(nb)

            sPattern = '<a href="([^<]+)">([^<]+)<em>'
            aResult = oParser.parse(page, sPattern)
            if aResult[0]:
                oOutputParameterHandler = cOutputParameterHandler()
                for aEntry in aResult[1]:

                    sTitle = sMovieTitle+aEntry[1].replace("الموسم", " S").replace("S ", "S")
                    siteUrl = aEntry[0]
                    sThumb = sThumb
                    sDesc = ""

                    oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)

                    oGui.addSeason(SITE_IDENTIFIER, 'showEps', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showEps():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sStart = '<section aria-label="seasons">'
    sEnd = '<ul class="tabcontent" id="related">'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)

    oRequest = cRequestHandler(sUrl)
    data = oRequest.request()

    if 'adilbo' in data:
        t_script = re.findall('<script.*?;.*?\'(.*?);', data, re.S)
        t_int = re.findall('/g.....(.*?)\)', data, re.S)
        if t_script and t_int:
            script = t_script[0].replace("'", '')
            script = script.replace("+", '')
            script = script.replace("\n", '')
            sc = script.split('.')
            page = ''
            for elm in sc:
                c_elm = base64.b64decode(elm+'==').decode()
                t_ch = re.findall('\d+', c_elm, re.S)
                if t_ch:
                    nb = int(t_ch[0])+int(t_int[0])
                    page = page + chr(nb)

            sPattern = '<li><a href="(.+?)"><img  src="(.+?)" alt="logo" />.+?<em>(.+?)</em>'
            aResult = oParser.parse(page, sPattern)
            if aResult[0]:
                oOutputParameterHandler = cOutputParameterHandler()
                for aEntry in aResult[1]:

                    sTitle = sMovieTitle+' E'+aEntry[2]
                    siteUrl = aEntry[0] + 'watching/'
                    sThumb = aEntry[1]
                    sDesc = ""

                    oOutputParameterHandler.addParameter('siteUrl', siteUrl)
                    oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
                    oOutputParameterHandler.addParameter('sThumb', sThumb)

                    oGui.addEpisode(SITE_IDENTIFIER, 'showServer', sTitle, '', sThumb, sDesc, oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showServer():
    oGui = cGui()
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    host = URL_MAIN.split('/')[2]

    oRequestHandler = cRequestHandler(sUrl)
    cook = oRequestHandler.GetCookies()
    hdr = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36',
           'Accept-Encoding': 'gzip', 'cookie': cook, 'host': host, 'referer': URL_MAIN}
    St = requests.Session()
    sHtmlContent = St.get(sUrl, headers=hdr)
    sHtmlContent = sHtmlContent.content.decode('utf8')

    oRequest = cRequestHandler(sUrl)
    data = oRequest.request()

    if 'adilbo' in data:
        t_script = re.findall('<script.*?;.*?\'(.*?);', data, re.S)
        t_int = re.findall('/g.....(.*?)\)', data, re.S)
        if t_script and t_int:
            script = t_script[0].replace("'", '')
            script = script.replace("+", '')
            script = script.replace("\n", '')
            sc = script.split('.')
            page = ''
            for elm in sc:
                c_elm = base64.b64decode(elm+'==').decode()
                t_ch = re.findall('\d+', c_elm, re.S)
                if t_ch:
                    nb = int(t_ch[0])+int(t_int[0])
                    page = page + chr(nb)

            sStart = '<li aria-label="quality">'
            sEnd = '<li aria-label="download">'
            page0 = oParser.abParse(page, sStart, sEnd)

            sPattern = sPattern = '<a href="(.+?)".+?class="fas fa-cloud-download-alt"></i>(.+?)<p'
            aResult = oParser.parse(page0, sPattern)
            if aResult[0]:
                for aEntry in aResult[1]:
                    url = aEntry[0]
                    sTitle = aEntry[1].replace('</i>', "")
                    sTitle = ('%s  [COLOR coral]%s[/COLOR]') % (sMovieTitle, sTitle)
                    url = url.replace("cimanow", "rrsrr")
                    sThumb = sThumb
                    if url.startswith('//'):
                        url = 'http:' + url

                    sHosterUrl = url
                    oHoster = cHosterGui().getHoster('lien_direct')
                    if oHoster:
                        oHoster.setDisplayName(sTitle)
                        oHoster.setFileName(sMovieTitle)
                    cHosterGui().showHoster(oGui, oHoster, sHosterUrl + "|Referer=" + URL_MAIN, sThumb)

            sPattern = '<iframe src="([^"]+)" scrolling'
            aResult = oParser.parse(page, sPattern)
            if aResult[0]:
                for aEntry in aResult[1]:
                    url = aEntry.replace("cimanow", "rrsrrs").replace("newcima", "rrsrrs")
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
                        oHoster.setDisplayName(sTitle)
                        oHoster.setFileName(sMovieTitle)
                    cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

            sPattern = '<a href="([^"]+)"><i class="fa fa-download">'
            aResult = oParser.parse(data, sPattern)
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
                        oHoster.setDisplayName(sTitle)
                        oHoster.setFileName(sMovieTitle)
                    cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    # Recuperation infos
            sId = ''
            sPattern = 'data-id="([^"]+)"'
            aResult = oParser.parse(page, sPattern)

            if aResult[0]:
                sId = aResult[1][0]

            sPattern = 'data-index="([^"]+)"'
            aResult = oParser.parse(page, sPattern)
            if aResult[0]:
                for aEntry in aResult[1]:

                    sTitle = 'server '
                    siteUrl = URL_MAIN + '/wp-content/themes/Cima%20Now%20New/core.php?action=switch&index='+aEntry+'&id='+sId
                    hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0', 'host': host, 'referer': URL_MAIN}
                    params = {'action': 'switch', 'index': aEntry, 'id': sId}
                    St = requests.Session()
                    sHtmlContent = St.get(siteUrl, headers=hdr, params=params)
                    oRequestHandler = cRequestHandler(siteUrl)
                    sData = oRequestHandler.request()

                    if 'adilbo' in sData:
                        t_script = re.findall('<script.*?;.*?\'(.*?);', sData, re.S)
                        t_int = re.findall('/g.....(.*?)\)', sData, re.S)
                        if t_script and t_int:
                            script = t_script[0].replace("'", '')
                            script = script.replace("+", '')
                            script = script.replace("\n", '')
                            sc = script.split('.')
                            spage = ''
                            for elm in sc:
                                c_elm = base64.b64decode(elm+'==').decode()
                                t_ch = re.findall('\d+', c_elm, re.S)
                                if t_ch:
                                    nb = int(t_ch[0])+int(t_int[0])
                                    spage = page + chr(nb)

                            sPattern = '<iframe src="(.+?)" scrolling'
                            aResult = oParser.parse(spage, sPattern)
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

    oGui.setEndOfDirectory()
