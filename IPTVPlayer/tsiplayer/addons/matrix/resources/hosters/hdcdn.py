﻿#-*- coding: utf-8 -*-


import unicodedata

from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import \
    VSlog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.packer import \
    cPacker
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'

class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'hdcdn', 'hdcdn')

    def setUrl(self, url):
        self._url = str(url)

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        sReferer = self._url
        url = self._url

        oRequest = cRequestHandler(url)
        sHtmlContent = oRequest.request()

        sPattern = '(eval\(function\(p,a,c,k,e(?:.|\s)+?\))<\/script>'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if (aResult[0] == True):
            data = aResult[1][0]
            data = unicodedata.normalize('NFD', data).encode('ascii', 'ignore').decode('unicode_escape')
            sHtmlContent = cPacker().unpack(data)

            sPattern = 'file:"(.+?)"'
            aResult = oParser.parse(sHtmlContent, sPattern)
            if aResult[0]:
                api_call = aResult[1][0]

        if (api_call):
            return True, api_call+'|AUTH=TLS&verifypeer=false'  + '&User-Agent=' + UA + '&Referer=' + sReferer

        return False, False
