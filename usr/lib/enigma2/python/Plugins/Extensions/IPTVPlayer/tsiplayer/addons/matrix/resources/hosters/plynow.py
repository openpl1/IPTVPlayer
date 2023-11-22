# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# http://uqload.com/embed-xxx.html

import re

from Plugins.Extensions.IPTVPlayer.p2p3.UrlLib import urllib_unquote
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser

UA = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'


class cHoster(iHoster):
    def __init__(self):
        iHoster.__init__(self, 'plynow', 'Plynow')

    def _getMediaLinkForGuest(self):
        oParser = cParser()

        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()

        # On récupere l'array
        sPattern = '<script>\s*\(function\(\).+?=(.+?)var player'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if (aResult):
            for aEntry in aResult[1]:
                uHv4sb = aEntry

        # On récupere chaque element de l'array et ont le mets dans un tuple que Python gere
        b = re.findall('"(.+?)"', str(uHv4sb))
        x = []

        for a in b:
            # Unquote decode les elements qui sont en unicode.
            x.append(urllib_unquote(a.replace('\\x', '%')))

        # On inverse le resultat et l'assemble en un string.
        result = ''.join(x)[::-1]
        sHosterUrl = re.findall('src="([^"]+)', result)
        sHosterUrl = str(sHosterUrl).replace('[', '').replace(']', '').replace("'", '')
        api_call = sHosterUrl

        if api_call:
            return True, api_call

        return False, False
