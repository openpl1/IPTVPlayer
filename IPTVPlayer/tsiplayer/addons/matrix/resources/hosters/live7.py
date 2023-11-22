#-*- coding: utf-8 -*-
# https://github.com/Kodi-vStream/venom-xbmc-addons
import re

from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'live7', 'Live7')

    def _getMediaLinkForGuest(self):
        api_call = False
        Referer = ""
        if '|Referer=' in self._url:
            url = self._url.split('|Referer=')[0]
            Referer = self._url.split('|Referer=')[1]
        else:
            url = self._url
            Referer =  "https://www.live7.pro/"

        oRequestHandler = cRequestHandler(url)
        oRequestHandler.addHeaderEntry('Referer', Referer)
        data3 = oRequestHandler.request()

        sPatternUrl = 'hlsUrl = "https:\/\/" \+ ea \+ "([^"]+)"'
        sPatternPK = 'var pk = "([^"]+)"'
        sPatternEA = 'ea = "([^"]+)";'
        aResultUrl = re.findall(sPatternUrl, data3)
        aResultEA = re.findall(sPatternEA, data3)
        aResultPK = re.findall(sPatternPK, data3)
        if aResultUrl and aResultPK and aResultEA:
            aResultPK = aResultPK[0][:53] + aResultPK[0][54:]
            url3 = aResultEA[0] + aResultUrl[0] + aResultPK
            api_call = 'https://' + url3

        if api_call:
            return True, api_call

        return False, False
