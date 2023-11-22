# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import cRequestHandler

import re

from Plugins.Extensions.IPTVPlayer.p2p3.UrlLib import (urllib2_Request,
                                                       urllib_urlopen)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import (
    VSlog, dialog)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0'


class cHoster(iHoster):
    def __init__(self):
        iHoster.__init__(self, 'googledrive', 'GoogleDrive')

    def __getIdFromUrl(self, sUrl):
        oParser = cParser()

        sPattern = 'google.+?([a-zA-Z0-9-_]{20,40})'
        aResult = oParser.parse(sUrl, sPattern)
        if aResult[0]:
            return aResult[1][0]

        return ''

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        url = []
        qua = []
        api_call = ''

        # reformatage du lien
        sId = self.__getIdFromUrl(self._url)
        sUrl = 'https://drive.google.com/file/d/' + sId + '/view'

        req = urllib2_Request(sUrl)
        response = urllib_urlopen(req)
        sHtmlContent = response.read()

        Headers = response.headers
        response.close()

        # listage des cookies
        c = Headers['Set-Cookie']
        c2 = re.findall('(?:^|,) *([^;,]+?)=([^;,\/]+?);', c)
        if c2:
            cookies = ''
            for cook in c2:
                cookies = cookies + cook[0] + '=' + cook[1] + ';'

        sPattern = '\["fmt_stream_map","([^"]+)"]'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if not aResult[0]:
            if '"errorcode","150"]' in sHtmlContent:
                dialog().VSinfo("Nombre de lectures max dépassé")
            return False, False

        sListUrl = aResult[1][0]

        if sListUrl:
            aResult2 = oParser.parse(sHtmlContent, '([0-9]+)\/([0-9]+x[0-9]+)\/')

        # liste les qualitee
            r = oParser.parse(sListUrl, '([0-9]+)\|([^,]+)')
            for item in r[1]:
                url.append(item[1].decode('unicode-escape'))
                for i in aResult2[1]:
                    if item[0] == i[0]:
                        qua.append(i[1])

        # Affichage du tableau
        api_call = dialog().VSselectqual(qua, url)
        api_call = api_call + '|User-Agent=' + UA + '&Cookie=' + cookies

        if api_call:
            return True, api_call

        return False, False
