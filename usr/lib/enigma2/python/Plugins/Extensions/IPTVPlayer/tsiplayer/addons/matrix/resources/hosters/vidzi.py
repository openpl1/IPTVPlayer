#-*- coding: utf-8 -*-
#https://vidzi.tv/xxx.html
#Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
import re

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


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'vidzi', 'Vidzi')

    def setUrl(self, url):
        self._url = url.replace('http://vidzi.tv/', '')
        self._url = self._url.replace('https://vidzi.tv/', '')
        self._url = self._url.replace('embed-', '')
        self._url= re.sub(r'\-.*\.html', r'', self._url)
        self._url = self._url.replace('.html', '')
        self._url = 'https://vidzi.tv/' + str(self._url) + '.html'

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        api_call = ''

        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()

        #lien direct
        sPattern = ',{file: *"([^"]+)"}\]'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            api_call = aResult[1][0]

        #2 test Dean Edwards Packer
        else:
            sPattern = "<script type='text/javascript'>(\s*eval\s*\(\s*function(?:.|\s)+?)<\/script>"
            aResult = oParser.parse(sHtmlContent, sPattern)
            if aResult[0]:
                sUnpacked = cPacker().unpack(aResult[1][0])
                sPattern =  'file:"([^"]+\.mp4)'
                aResult = oParser.parse(sUnpacked, sPattern)
                if aResult[0]:
                    api_call = aResult[1][0]

        if api_call:
            return True, api_call

        return False, False
