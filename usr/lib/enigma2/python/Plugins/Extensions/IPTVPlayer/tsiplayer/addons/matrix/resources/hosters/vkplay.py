#-*- coding: utf-8 -*-
# https://github.com/Kodi-vStream/venom-xbmc-addons
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'vkplay', 'vkPlay')

    def _getMediaLinkForGuest(self):
        oParser = cParser()

        sLive = self._url.split('embed/')[1]
        api_url = "https://api.vkplay.live/v1/blog/"
        url = api_url+sLive+'/public_video_stream'

        api_call = False
        sReferer = ""
        if '|Referer=' in self._url:
            url = self._url.split('|Referer=')[0]
        else:
            url = self._url


        oRequest = cRequestHandler(url)
        sHtmlContent = oRequest.request()

        sPattern = '"url":"([^"]+)'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            for aEntry in aResult[1]:
                if 'm3u8' not in aEntry:
                    continue
                if 'hls' not in aEntry:
                    continue
                if 'http' not in aEntry:
                    continue
                url = aEntry

            api_call = url

            if api_call:
                return True, api_call

            return False, False
