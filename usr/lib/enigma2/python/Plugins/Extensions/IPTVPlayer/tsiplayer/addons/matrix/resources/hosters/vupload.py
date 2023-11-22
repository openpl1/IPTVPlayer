# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
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

UA = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'


class cHoster(iHoster):
    def __init__(self):
        iHoster.__init__(self, 'vupload', 'Vupload')

    def setUrl(self, url):
        self._url = str(url)
        self._url = self._url.replace('emb.html?', 'embed-')

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        api_call = False

        oRequest = cRequestHandler(self._url)
        oRequest.addHeaderEntry('Referer', self._url)
        oRequest.addParameters('User-Agent', UA)
        sHtmlContent = oRequest.request()

        sPattern = 'src: "(.+?)",'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            api_call = aResult[1][0]

        else:
            sPattern = '(eval\(function\(p,a,c,k,e(?:.|\s)+?\))<\/script>'
            aResult = oParser.parse(sHtmlContent, sPattern)
            if aResult[0]:
                sHtmlContent2 = cPacker().unpack(aResult[1][0])

                sPattern = '{src:"([^"]+)",type:"video\/mp4",res:([^:,<>]+)'
                aResult = oParser.parse(sHtmlContent2, sPattern)
                if aResult[0]:
                # initialisation des tableaux
                    url = []
                    qua = []
                    for i in aResult[1]:
                        url.append(str(i[0]))
                        qua.append(str(i[1]))

                    api_call = dialog().VSselectqual(qua, url)

        if api_call:
            return True, api_call

        return False, False
