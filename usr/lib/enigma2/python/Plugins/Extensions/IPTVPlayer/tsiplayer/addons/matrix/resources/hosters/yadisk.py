﻿#-*- coding: utf-8 -*-



from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import (
    VSlog, dialog)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'yadisk', 'yadisk')

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        api_call = False

        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()

        sPattern =  '"height":(.+?)},"url":"(.+?)"}'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if (aResult[0]):

            url=[]
            qua=[]
            api_call = False

            for aEntry in aResult[1]:
                url.append(aEntry[1])
                qua.append(aEntry[0])

            api_call = dialog().VSselectqual(qua, url)

            if api_call:
                return True, api_call

        return False, False
