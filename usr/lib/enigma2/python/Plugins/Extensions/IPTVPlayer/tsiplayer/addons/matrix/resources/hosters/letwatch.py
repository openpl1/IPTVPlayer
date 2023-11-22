#-*- coding: utf-8 -*-
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
        iHoster.__init__(self, 'letwatch', 'LetWatch')

    def __getUrlFromJavascriptCode(self, sHtmlContent):

        aResult = re.search('(eval\(function.*?)\s*</script>', sHtmlContent, re.DOTALL)
        if (aResult.group(1)):
            sJavascript = aResult.group(1)

            #sUnpacked = cJsUnpacker().unpackByString(sJavascript)
            sUnpacked = cPacker().unpack(sJavascript)

            return sUnpacked

        return False

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        api_call = False

        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()

        sUnpacked = self.__getUrlFromJavascriptCode(sHtmlContent)

        sPattern = 'sources:\[{file:"(.+?)"'
        aResult = oParser.parse(sUnpacked, sPattern)
        if aResult[0]:
            api_call = aResult[1][0]
            return True, api_call

        return False, False
