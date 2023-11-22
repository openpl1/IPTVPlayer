# -*- coding: utf-8 -*-
# Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
# Yonn1981 https://github.com/Yonn1981/Repo


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
        iHoster.__init__(self, 'febb', 'Febbox')

    def setUrl(self, url):
        self._url = str(url).replace('+', '%2B').split('?sub.info=')[0]
        self._url0 = str(url)

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        api_call = self._url

        if ('sub.info' in self._url0):
            SubTitle = self._url0.split('sub.info=')[1]
            if '&t=' in SubTitle:
                SubTitle = SubTitle.split('&t=')[0]
            else:
                SubTitle = SubTitle
            oRequest0 = cRequestHandler(SubTitle)
            sHtmlContent0 = oRequest0.request().replace('\\', '')

            sPattern = '"file":"([^"]+)".+?"label":"(.+?)"'
            aResult = oParser.parse(sHtmlContent0, sPattern)
            if aResult[0]:
                url = []
                qua = []
                for i in aResult[1]:
                    url.append(str(i[0]))
                    qua.append(str(i[1]))
                SubTitle = dialog().VSselectsub(qua, url)
        else:
            SubTitle = ''

        api_call = self._url
        VSlog(api_call)

        if api_call:
            if ('http' in SubTitle):
                return True, api_call, SubTitle
            else:
                return True, api_call

        return False, False
