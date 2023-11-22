#-*- coding: utf-8 -*-

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
        iHoster.__init__(self, 'anafasts', 'Anafasts')


    def isDownloadable(self):
        return True

    def _getMediaLinkForGuest(self):
        oParser = cParser()

        self._url = self._url.replace('embed-','')
        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()
        VSlog(self._url)

        list_q = []
        list_url = []
        api_call = False

        sPattern = 'file:"([^"]+)'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            url2 = aResult[1][0]
            oRequestHandler = cRequestHandler(url2)
            sHtmlContent2 = oRequestHandler.request()

            sPattern = 'PROGRAM-ID.+?RESOLUTION=(\w+).+?(https.+?m3u8)'
            aResult = oParser.parse(sHtmlContent2, sPattern)
            for aEntry in aResult[1]:
                list_q.append(aEntry[0].split('x')[1]+"p")
                list_url.append(aEntry[1])

            if list_url:
                api_call = dialog().VSselectqual(list_q,list_url)


            if api_call:
                return True, api_call

        return False, False

