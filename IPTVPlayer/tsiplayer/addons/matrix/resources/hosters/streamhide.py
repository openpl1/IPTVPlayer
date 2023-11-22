# coding: utf-8
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons

from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.packer import \
    cPacker
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser

UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'


class cHoster(iHoster):
    def __init__(self):
        iHoster.__init__(self, 'streamhide', 'StreamHide')

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        eURL = self._url
        if ('/d' in eURL):
            eURL = eURL.replace('/d','/e').split('_')[0]
        else:
            eURL = eURL
        oRequest = cRequestHandler(eURL)
        sHtmlContent = oRequest.request()

        sPattern = '(eval\(function\(p,a,c,k,e(?:.|\s)+?\))<\/script>'
        aResult = oParser.parse(sHtmlContent,sPattern)
        if aResult[0] is True:
            sHtmlContent = cPacker().unpack(aResult[1][0])

        sPattern = '{file:"([^"]+)"}]'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0] is True:
            api_call = aResult[1][0]

            return True, api_call

        return False, False