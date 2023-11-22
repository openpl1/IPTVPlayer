﻿#coding: utf-8
#
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import \
    VSlog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'wishfast', 'Wishfast')

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)

        api_call = ''

        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()

        sPattern = 'sources: [{file:"(.+?)"}],'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            api_call = aResult[1][0]

        sPattern = 'file:"(.+?)"}'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            api_call = aResult[1][0]

        sPattern = ',{file:"(.+?)",label'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            api_call = aResult[1][0]

        if api_call:
            return True, api_call +'|User-Agent=' + UA  + '&Referer=' + self._url


        return False, False