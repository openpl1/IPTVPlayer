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
        iHoster.__init__(self, 'fajer', 'fajer')

    def isDownloadable(self):
        return True

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)

        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()

        sPattern = '#EXT-X-STREAM-INF:BANDWIDTH=(.+?),RESOLUTION=.+?/drive//hls/(.+?).m3u8'
        aResult = oParser.parse(sHtmlContent, sPattern)
        api_call = False
        if aResult[0]:

            #initialisation des tableaux
            url=[]
            qua=[]

            #Replissage des tableaux
            for i in aResult[1]:
                url.append("https://fajer.video/drive/hls/"+str(i[1])+".m3u8")
                qua.append(str(i[0]).replace("1500000","720p").replace("3000000","1080p").replace("500000","360p").replace("750000","480p"))

            api_call = dialog().VSselectqual(qua, url)

            if api_call:
                return True, api_call

        return False, False

