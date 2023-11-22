# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons

from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import \
    VSlog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'directmoviedl', 'DirectMovieDl')

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        api_call = False

        if 'movie.directmoviedl' in self._url:
            oRequest = cRequestHandler(self._url)
            sHtmlContent = oRequest.request()

            sPattern = '="([^"]+)" type="video/mp4'
            aResult = oParser.parse(sHtmlContent, sPattern)
            api_call = aResult[1][0]
        else:
            oRequest = cRequestHandler(self._url)
            sHtmlContent = oRequest.request()

            sPattern = 'src="(http.+?)"'
            aResult = oParser.parse(sHtmlContent, sPattern)
            if aResult[0]:
                for aEntry in aResult[1]:
                    sHoster = aEntry
                    oRequest = cRequestHandler(sHoster)
                    sHtmlContent1 = oRequest.request()
                    sPattern1 = '="([^"]+)" type="video/mp4'
                    aResult1 = oParser.parse(sHtmlContent1, sPattern1)
                    api_call = aResult1[1][0]

        if api_call:
            return True, api_call

        return False, False
