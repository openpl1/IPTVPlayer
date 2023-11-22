# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# 2 hoster giga & 2gigalink
# from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import cRequestHandler

import ssl

from Plugins.Extensions.IPTVPlayer.p2p3.UrlLib import (urllib2_Request,
                                                       urllib_urlopen)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import \
    VSlog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'giga', 'Giga')

    def isDownloadable(self):
        return False

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        myContext = ssl._create_unverified_context()

        req = urllib2_Request(self._url)
        handle = urllib_urlopen(req, context=myContext)
        sHtmlContent = handle.read()
        handle.close()

        sPattern = "var mp4v = '(.+?)'"
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            return True, aResult[1][0]
        else:
            # streamgk
            sPattern = '<a id="downloadb" class="btn btn-default.+?href="([^"]+)"'
            aResult = oParser.parse(sHtmlContent, sPattern)
            if aResult[0]:
                return True, aResult[1][0]

        return False, False
