# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# Meme code que thevideo
# https://vidup.me/embed-xxx-703x405.html
# https://vidup.me/embed/xxx-703x405.html
# https://vidup.me/xxx-703x405.html
# https://vidup.io/embed/xxx
# https://vidup.io/xxx

import json
import ssl

from Plugins.Extensions.IPTVPlayer.p2p3.UrlLib import (urllib2_Request,
                                                       urllib_urlopen)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.lib.comaddon import \
    dialog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.lib.parser import \
    cParser

UA = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"


class cHoster(iHoster):
    def __init__(self):
        iHoster.__init__(self, 'vidup', 'VidUp')

    def __getIdFromUrl(self, sUrl):
        sPattern = 'https*:\/\/vidup.+?\/(?:embed-)?(?:embed/)?([0-9a-zA-Z]+)'
        oParser = cParser()
        aResult = oParser.parse(sUrl, sPattern)
        if aResult[0] is True:
            return aResult[1][0]

        return ''

    def _getMediaLinkForGuest(self):
        api_call = False

        request_headers = {"User-Agent": UA}
        req = urllib2_Request(self._url, headers=request_headers)
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        response = urllib_urlopen(req, context=gcontext)
        self._url = response.geturl()

        response.close()

        Json_url = "https://vidup.io/api/serve/video/" + self.__getIdFromUrl(self._url)

        req = urllib2_Request(Json_url, headers=request_headers)
        gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        response = urllib_urlopen(req, data={}, context=gcontext)
        sHtmlContent = response.read()
        aResult = json.loads(sHtmlContent)

        response.close()

        if aResult:
            url = []
            qua = []

            for i in aResult['qualities']:
                url.append(aResult['qualities'][i])
                qua.append(str(i))

            api_call = dialog().VSselectqual(qua, url)

        if api_call:
            return True, api_call

        return False, False
