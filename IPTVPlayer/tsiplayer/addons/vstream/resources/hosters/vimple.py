# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# http://player.vimple.ru/iframe/XXXXXXXXXXXXXXXXXXXXX

from Plugins.Extensions.IPTVPlayer.p2p3.UrlLib import (urllib2_Request,
                                                       urllib_urlopen)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.lib.parser import \
    cParser


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'vimple', 'Vimple')

    def _getMediaLinkForGuest(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
        req = urllib2_Request(self._url, None, headers)
        response = urllib_urlopen(req)
        sHtmlContent = response.read()
        head = response.headers
        response.close()

        oParser = cParser()

        cookies = ''
        if 'Set-Cookie' in head:
            sPattern = '(?:^|,) *([^;,]+?)=([^;,\/]+?);'
            aResult = oParser.parse(str(head['Set-Cookie']), sPattern)
            if aResult[0] is True:
                for cook in aResult[1]:
                    cookies = cookies + cook[0] + '=' + cook[1] + ';'
        # Get link
        sPattern = '"video":\[{"default":true,"url":"([^"]+?)"}]'
        aResult = oParser.parse(sHtmlContent, sPattern)

        if aResult[0] is True:
            url = aResult[1][0]
            url = url.replace('\/', '/')

            api_call = url + '|Cookie=' + cookies

            return True, api_call

        return False, False
