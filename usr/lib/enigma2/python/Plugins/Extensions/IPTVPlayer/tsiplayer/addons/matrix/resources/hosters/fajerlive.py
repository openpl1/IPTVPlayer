﻿#-*- coding: utf-8 -*-

import json

from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import (
    VSlog, dialog)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler

UA = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36'

class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'fajerlive', 'fajerlive')

    def isDownloadable(self):
        return True

    def _getMediaLinkForGuest(self):
        VSlog(self._url)

        url = 'https://fajer.live/api/source/' + self._url.rsplit('/', 1)[1]

        postdata = 'r=&d=fajer.live'

        oRequest = cRequestHandler(url)
        oRequest.setRequestType(1)
        oRequest.addHeaderEntry('User-Agent', UA)
        oRequest.addHeaderEntry('Referer', self._url)
        oRequest.addParametersLine(postdata)

        sHtmlContent = json.loads(oRequest.request())
        if sHtmlContent:
            url = []
            qua = []
            for x in sHtmlContent['data']:
                url.append(x['file'])
                qua.append(x['label'])

            if (url):
                api_call = dialog().VSselectqual(qua, url)

        if api_call:
            return True, api_call + '|User-Agent=' + UA + '&Referer=' + self._url+ '&Origin=https://fajer.live' +'&verifypeer=false'

        return False, False