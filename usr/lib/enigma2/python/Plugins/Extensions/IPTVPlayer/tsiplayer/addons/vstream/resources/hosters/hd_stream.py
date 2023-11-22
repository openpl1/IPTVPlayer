# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# Venom
# Hoster pour les liens https://hd-stream.xyz/embed/
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.lib.comaddon import \
    dialog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.lib.packer import \
    cPacker
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.lib.parser import \
    cParser


class cHoster(iHoster):
    def __init__(self):
        iHoster.__init__(self, 'hd_stream', 'HDStream')

    def _getMediaLinkForGuest(self):
        api_call = False

        oRequestHandler = cRequestHandler(self._url)
        sHtmlContent = oRequestHandler.request()

        oParser = cParser()
        sPattern = '(\s*eval\s*\(\s*function(?:.|\s)+?{}\)\))'
        aResult = oParser.parse(sHtmlContent, sPattern)

        if aResult[0] is True:

            sHtmlContent = cPacker().unpack(aResult[1][0])
            sPattern = 'file":"([^"]+)".+?"label":"([^"]+)"'
            aResult = oParser.parse(sHtmlContent, sPattern)

            if aResult[0] is True:
                url = []
                qua = []

                for aEntry in aResult[1]:
                    url.append(aEntry[0])
                    qua.append(aEntry[1])

                api_call = dialog().VSselectqual(qua, url)

        if api_call:
            return True, api_call

        return False, False
