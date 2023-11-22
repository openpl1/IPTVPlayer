#-*- coding: utf-8 -*-
#https://www.cloudy.ec/embed.php?id=etc...
#http://www.cloudy.ec/v/etc...
#
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import (
    VSlog, dialog)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'

class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'Cloudy', 'Cloudy')

    def isDownloadable(self):
        return True

    def __getIdFromUrl(self):
        oParser = cParser()

        sPattern = "id=([^<]+)"
        aResult = oParser.parse(self._url, sPattern)
        if aResult[0]:
            return aResult[1][0]
        return ''

    def setUrl(self, sUrl):
        oParser = cParser()

        self._url = str(sUrl)
        sPattern =  'id=([a-zA-Z0-9]+)'
        aResult = oParser.parse(self._url, sPattern)
        if aResult[0]:
            self._url = 'https://www.cloudy.ec/embed.php?id=' + aResult[1][0] + '&playerPage=1'
            self._url = self._url.replace('https','http')
        else:
            VSlog(self._url)

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()
        VSlog(self._url)

        sPattern =  '<source src="([^"]+)" type=\'(.+?)\'>'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            url = []
            qua = []
            for x in aResult[1]:
                url.append(x[0])
                qua.append(x[1])

                api_call = dialog().VSselectqual(qua,url)

        if api_call:
            return True, api_call + '|User-Agent=' + UA

        return False, False
