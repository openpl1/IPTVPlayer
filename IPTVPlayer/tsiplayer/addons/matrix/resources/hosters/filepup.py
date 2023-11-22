#-*- coding: utf-8 -*-
#Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import \
    VSlog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'filepup', 'FilePup')

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        oRequestHandler = cRequestHandler(self._url)
        sHtmlContent = oRequestHandler.request()

        sPattern = 'type: "video\/mp4", *src: "([^<>"{}]+?)"'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            return True, aResult[1][0]

        return False, False
