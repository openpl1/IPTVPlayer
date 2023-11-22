#coding: utf-8
#
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import \
    dialog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'rumble', 'Rumble')

    def setUrl(self, sUrl):
        self._url = str(sUrl)

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()

        sPattern = '},"(.+?)":{"url":"(.+?)",'
        aResult = oParser.parse(sHtmlContent, sPattern)
        api_call = False
        if aResult[0]:

            #initialisation des tableaux
            url=[]
            qua=[]

            #Replissage des tableaux
            for i in aResult[1]:
                url.append(str(i[1]))
                qua.append(str(i[0]))
            api_call = dialog().VSselectqual(qua, url)

            if api_call:
                return True, api_call
        else:
            sPattern = 'RESOLUTION=(\d+x\d{0,3}).+?(https.+?m3u8)'
            aResult = oParser.parse(sHtmlContent, sPattern)

            api_call = False

            if aResult[0]:
            #initialisation des tableaux
                url=[]
                qua=[]

            #Replissage des tableaux
                for i in aResult[1]:
                    url.append(str(i[1]))
                    qua.append(str(i[0]))
                api_call = dialog().VSselectqual(qua, url)

                if api_call:
                    return True, api_call

        return False, False
