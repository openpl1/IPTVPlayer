# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# import re
import base64

from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import (
    VSlog, dialog)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.packer import \
    cPacker
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser


class cHoster(iHoster):
    def __init__(self):
        iHoster.__init__(self, 'ddlfr', 'ddlfr')

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        api_call = ''

        oRequest = cRequestHandler(self._url)
        oRequest.addHeaderEntry('Referer', self._url)
        sHtmlContent = oRequest.request()

        sPattern = 'JuicyCodes\.Run\("(.+?)"\);'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:

            media = aResult[1][0].replace('+', '')
            media = base64.b64decode(media)

            # cPacker decode
            media = cPacker().unpack(media)
            if media:

                sPattern = '{"file":"(.+?)","label":"(.+?)"'
                aResult = oParser.parse(media, sPattern)
                if aResult[0]:
                    url = []
                    qua = []
                # Remplissage des tableaux
                    for i in aResult[1]:
                        url.append(str(i[0] + '|Referer=' + self._url))
                        qua.append(str(i[1]))
                # Si une seule url
                    api_call = dialog().VSselectqual(qua, url)

        if api_call:
            return True, api_call

        return False, False
