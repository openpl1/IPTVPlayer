# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
#

import json

import requests
from Plugins.Extensions.IPTVPlayer.p2p3.pVer import isPY2
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.lib.comaddon import \
    dialog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.lib.parser import \
    cParser
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.vstream.resources.lib.util import \
    cUtil


class cHoster(iHoster):
    def __init__(self):
        iHoster.__init__(self, 'ok_ru', 'Ok.ru')

    def getHostAndIdFromUrl(self, sUrl):
        sPattern = 'https*:\/\/.*?((?:(?:ok)|(?:odnoklassniki))\.ru)\/.+?\/([0-9]+)'
        oParser = cParser()
        aResult = oParser.parse(sUrl, sPattern)
        if aResult[0] is True:
            return aResult[1][0]
        return ''

    def _getMediaLinkForGuest(self):
        v = self.getHostAndIdFromUrl(self._url)
        sId = v[1]
        sHost = v[0]
        web_url = 'http://' + sHost + '/videoembed/' + sId

        St=requests.Session()
        oParser = cParser()

        sHtmlContent = oParser.abParse(sHtmlContent, 'data-options=', '" data-player-container', 14)
        sHtmlContent = cUtil().removeHtmlTags(sHtmlContent)
        sHtmlContent = cUtil().unescape(sHtmlContent)

        page = json.loads(sHtmlContent)
        page = json.loads(page['flashvars']['metadata'])
        if page:
            url = []
            qua = []
            numLien = 1
            for x in page['videos']:
                url.append(x['url'])
                qua.append('Lien %d' % numLien)
                numLien += 1
            # Si au moins 1 url
            if url:
                # dialogue qualité
                api_call = dialog().VSselectqual(qua, url)

        if api_call:
            if not isPY2():
                api_call = api_call.replace('&ct=0', '&ct=6')
            return True, api_call

        return False, False
