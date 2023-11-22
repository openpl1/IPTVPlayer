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

UA = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'

class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'myvid', 'myvid')

    def setUrl(self, sUrl):
        self._url = str(sUrl)
        if 'embed' not in self._url:
            self._url = self._url.replace("https://myviid.com/", "https://myviid.com/embed-")

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)

        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()


        sPattern = 'file:"([^<]+)",label'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            api_call = aResult[1][0] +'|User-Agent=' + UA + '&Referer=' + self._url

        sPattern = "(eval\(function\(p,a,c,k,e(?:.|\s)+?\))<\/script>"
        aResult = oParser.parse(sHtmlContent,sPattern)
        if aResult[0]:
            sHtmlContent = cPacker().unpack(aResult[1][0])
            sPattern = 'file:"(.+?)",label:".+?"}'
            aResult = oParser.parse(sHtmlContent,sPattern)
            if aResult[0]:
                api_call = aResult[1][0]

        if api_call:
            return True, api_call

        return False, False