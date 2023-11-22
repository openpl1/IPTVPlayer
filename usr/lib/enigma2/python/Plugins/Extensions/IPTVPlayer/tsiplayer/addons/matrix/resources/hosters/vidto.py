import re
import time

from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import \
    VSlog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.packer import \
    cPacker
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'vidto', 'VidTo')

    def setUrl(self, url):
        self._url = url.replace('http://vidto.me/', '')
        self._url = self._url.replace('embed-', '')
        self._url= re.sub(r'\-.*\.html', '', self._url)
        self._url = 'http://vidto.me/' + str(self._url)

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()

        sPattern = '<input type="hidden" name="([^"]+)" value="([^"]+)"'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            time.sleep(7)
            oRequest = cRequestHandler(self._url)
            oRequest.setRequestType(cRequestHandler.REQUEST_TYPE_POST)
            for aEntry in aResult[1]:
                oRequest.addParameters(aEntry[0], aEntry[1])

            oRequest.addParameters('referer', self._url)
            sHtmlContent = oRequest.request()
            sHtmlContent = sHtmlContent.replace('file:""', '')

            sPattern = '(eval\(function\(p,a,c,k,e(?:.|\s)+?\))<\/script>'
            aResult = oParser.parse(sHtmlContent, sPattern)
            if aResult[0]:
                sHtmlContent = cPacker().unpack(aResult[1][0])
                sPattern =  ',file:"([^"]+)"}'
                aResult = oParser.parse(sHtmlContent, sPattern)
                if aResult[0]:
                    return True, aResult[1][0]
            else:
                sPattern = '{file:"([^"]+)",label:"(\d+p)"}'
                aResult = oParser.parse(sHtmlContent, sPattern)
                if aResult[0]:
                    url=[]
                    qua=[]
                for i in aResult[1]:
                    url.append(str(i[0]))
                    qua.append(str(i[1]))

                if len(url) == 1:
                    return True, url[0]

                elif len(url) > 1:
                    return True, url[0]

        return False, False
