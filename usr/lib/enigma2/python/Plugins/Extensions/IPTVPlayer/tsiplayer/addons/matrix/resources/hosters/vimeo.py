#-*- coding: utf-8 -*-
# https://github.com/Kodi-vStream/venom-xbmc-addons
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import (
    VSlog, dialog)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'vimeo', 'Vimeo')

    def __getIdFromUrl(self, sUrl):
        oParser = cParser()

        sPattern = 'vimeo\.com\/(?:event\/)?([0-9]+)'
        aResult = oParser.parse(sUrl, sPattern)
        if aResult[0]:
            return aResult[1][0]

        return ''

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        api_call = False
        sReferer = ""
        url = self._url.split('|Referer=')[0]
        sReferer = self._url.split('|Referer=')[1]

        oRequest = cRequestHandler(url)
        oRequest.addHeaderEntry('Host', 'vimeo.com')
        oRequest.addHeaderEntry('Referer', sReferer)
        oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1')
        sHtmlContent = oRequest.request()

        sPattern = '"config":"(.+?)",'
        aResult = oParser.parse(sHtmlContent, sPattern)
        sId = ''

        if (aResult[0]):
            sId = aResult[1][0]
        web_url = sId

        oRequest = cRequestHandler(web_url)
        cook = oRequest.GetCookies()
        oRequest.addHeaderEntry('Referer', 'https://vimeo.com/')
        oRequest.addHeaderEntry('User-Agent', 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1')
        sHtmlContent = oRequest.request()

        sPattern = '"origin":"(.+?)","url":"(.+?)",'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            #initialisation des tableaux
            url=[]
            qua=[]

            #Remplissage des tableaux
            for i in aResult[1]:
                url.append(str(i[1]))
                qua.append(str(i[0]))

            #tableau
            api_call = dialog().VSselectqual(qua, url)

            if api_call:
                return True, api_call

            return False, False
