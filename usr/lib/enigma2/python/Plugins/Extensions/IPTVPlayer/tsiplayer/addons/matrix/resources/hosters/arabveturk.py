﻿#-*- coding: utf-8 -*-
# https://github.com/Kodi-vStream/venom-xbmc-addons
# https://aparat.cam/embed-xxxxx.html

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
        iHoster.__init__(self, 'arabveturk', 'arabveturk')

    def isDownloadable(self):
        return True

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)

        url = self._url
        VideoType = 2 # dl mp4 lien existant non utilisé ici
        VideoType = 1 # m3u8
        VSlog(self._url)

        list_q = []
        list_url = []

        if VideoType == 1:
            oRequestHandler = cRequestHandler(url)
            sHtmlContent = oRequestHandler.request()

            sPattern = 'file:"(http.+?m3u8)"'
            aResult = oParser.parse(sHtmlContent, sPattern)
            if aResult[0]:
                url2 = aResult[1][0]
                oRequestHandler = cRequestHandler(url2)
                sHtmlContent2 = oRequestHandler.request()

                # prend tous les formats  (peu créer problemes CODECS avc1)

                # limite les formats
                sPattern = 'PROGRAM-ID.+?RESOLUTION=(\w+).+?(https.+?m3u8)'
                aResult = oParser.parse(sHtmlContent2, sPattern)
                for aEntry in aResult[1]:
                    list_q.append(aEntry[0])
                    list_url.append(aEntry[1]) # parfois lien de meme qualité avec url diffrentes

            if list_url:
                api_call = dialog().VSselectqual(list_q,list_url)


            if api_call:
                return True, api_call

        return False,False