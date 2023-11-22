#-*- coding: utf-8 -*-
#Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
import re

from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import \
    VSlog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'kvid', 'Kvid')

    def _getMediaLinkForGuest(self):
        VSlog(self._url)
        api_call = False

        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()

        r2 = re.search('file: *"([^"]+)",', sHtmlContent)
        if (r2):
            api_call = r2.group(1)

        if api_call:
            return True, api_call

        return False, False
