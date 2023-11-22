# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
#
import re

from Plugins.Extensions.IPTVPlayer.p2p3.UrlLib import (urllib2_Request,
                                                       urllib2_URLError,
                                                       urllib_urlopen)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.util import \
    urlEncode


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'playreplay', 'PlayReplay')

    def __getIdFromUrl(self, sUrl):
        sPattern = 'http:..playreplay.net\/framevideo\/(.+?)\?'
        aResult = re.findall(sPattern, sUrl)
        if (aResult):
            return aResult[0]

        return ''

    def _getMediaLinkForGuest(self):
        vUrl = False
        sId = self.__getIdFromUrl(self._url)

        query_args = {'r': '["tVL0gjqo5",["preview/flv_image",{"uid":"' + sId + '"}],' + \
            '["preview/flv_link",{"uid":"' + sId + '"}]]'}

        data = urlEncode(query_args)
        headers = {'User-Agent': 'Mozilla 5.10'}
        url = 'http://api.letitbit.net'
        request = urllib2_Request(url, data, headers)

        try:
            reponse = urllib_urlopen(request)
        except urllib2_URLError as e:
            print(e.read())
            print(e.reason)

        html = reponse.read()

        sHtmlContent = html.replace('\\', '')

        link = re.findall('"link":"(.+?)"', sHtmlContent)
        if link:
            vUrl = link[0]

        if (vUrl):
            api_call = vUrl
            return True, api_call

        return False, False
