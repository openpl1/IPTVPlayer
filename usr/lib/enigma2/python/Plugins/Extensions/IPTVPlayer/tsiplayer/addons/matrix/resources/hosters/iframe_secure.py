#-*- coding: utf-8 -*-
#Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
import re

from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import \
    VSlog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.gui.hoster import \
    cHosterGui
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.packer import \
    cPacker
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'iframe_secure', 'Iframe-Secure')

    def setUrl(self, url):
        self._url = url.replace('http://www.iframe-secure.com/embed/', '')
        self._url = self._url.replace('//iframe-secure.com/embed/', '')
        self._url = 'http://www.iframe-secure.com/embed/iframe.php?u=%s' % self._url

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        api_call = ''

        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()

        sPattern = "(\s*eval\s*\(\s*function(?:.|\s)+?)<\/script>"
        aResult = re.findall(sPattern, sHtmlContent)

        if (aResult):
            sUnpacked = cPacker().unpack(aResult[0])
            sHtmlContent = sUnpacked

            if (sHtmlContent):
                sPattern = "replace\(.*'(.+?)'"
                aResult = oParser.parse(sHtmlContent, sPattern)

                if aResult[0]:
                    sHosterUrl = aResult[1][0]

                    if not sHosterUrl.startswith('http'):
                        sHosterUrl = 'http:%s' % sHosterUrl

                    sHosterUrl = sHosterUrl.replace('\\', '')
                    oHoster = cHosterGui().checkHoster(sHosterUrl)
                    oHoster.setUrl(sHosterUrl)
                    api_call = oHoster.getMediaLink()

                    if api_call[0]:
                        return True, api_call[1]

        return False, False
