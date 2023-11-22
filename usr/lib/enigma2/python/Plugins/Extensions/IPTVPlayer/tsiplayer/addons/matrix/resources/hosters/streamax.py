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

UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'

class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'streamax', 'Streamax')

    def __getIdFromUrl(self, sUrl):
        oParser = cParser()

        sPattern = 'id=([a-zA-Z0-9]+)'
        aResult = oParser.parse(sUrl, sPattern)
        if aResult[0]:
            return aResult[1][0]
        return ''

    def _getMediaLinkForGuest(self):
        VSlog(self._url)
        oParser = cParser()

        urlId = self.__getIdFromUrl(self._url)

        sUrl = 'https://streamax.club/hls/' + urlId + '/' + urlId + '.playlist.m3u8'

        url = []
        qua = []

        oRequest = cRequestHandler(sUrl)
        oRequest.addHeaderEntry('User-Agent', UA)
        oRequest.addHeaderEntry('Referer','https://streamax.club/public/dist/index.html?id=' + urlId)
        sHtmlContent = oRequest.request()

        sPattern = 'RESOLUTION=(\d+x\d+)(.+?.m3u8)'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            for aEntry in aResult[1]:
                url.append('https://streamax.club' + aEntry[1])
                qua.append(aEntry[0])

            if (url):
                api_call = dialog().VSselectqual(qua, url)

        if api_call:
            return True, api_call

        return False, False
