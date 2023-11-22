#-*- coding: utf-8 -*-
#############################################################
# Yonn1981 https://github.com/Yonn1981/Repo
#############################################################


from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import \
    dialog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'

class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'moviztime', 'MovizTime', 'gold')

    def isDownloadable(self):
        return False

    def setUrl(self, url):
        self._url = str(url)


    def _getMediaLinkForGuest(self):
        oParser = cParser()
        url = self._url
        api_call = ''

        oRequest = cRequestHandler(url)
        oRequest.addHeaderEntry('user-agent',UA)
        sHtmlContent = oRequest.request()

        sPattern = 'source:"([^"]+)'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
                api_call = aResult[1][0]
                shost = api_call.split('/videowl')[0]
                url = []
                qua = []
                oRequest = cRequestHandler(api_call)
                oRequest.addHeaderEntry('User-Agent', UA)
                sHtmlContent = oRequest.request()

                sPattern = 'RESOLUTION=(\d+x\d+)(.+?.m3u8)'
                aResult = oParser.parse(sHtmlContent, sPattern)
                if aResult[0] is True:
                    for aEntry in aResult[1]:
                        url.append(aEntry[1])
                        qua.append(aEntry[0])

                    if url:
                        api_call = dialog().VSselectqual(qua, url)
                        api_call = shost+api_call+'?double_encode=1'

        if api_call:
            return True, api_call

        return False, False
