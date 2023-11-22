#-*- coding: utf-8 -*-
#Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
#############################################################
# Yonn1981 https://github.com/Yonn1981/Repo
#############################################################


from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import \
    dialog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.packer import \
    cPacker
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser

UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0'

class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'egybest', 'EgyBest', 'gold')

    def isDownloadable(self):
        return False

    def setUrl(self, url):
        self._url = str(url).replace("eeggyy","")

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        sReferer = ""
        url = self._url.split('|Referer=')[0]
        sReferer = self._url.split('|Referer=')[1]

        oRequest = cRequestHandler(url)
        oRequest.addHeaderEntry('user-agent',UA)
        oRequest.addHeaderEntry('Referer',sReferer)
        sHtmlContent = oRequest.request()

        sPattern = '(eval\(function\(p,a,c,k,e(?:.|\s)+?\))<\/script>'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            sHtmlContent = cPacker().unpack(aResult[1][0])

        sPattern = 'file:"(.+?)"'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            api_call = aResult[1][0]

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
                    api_call = api_call + dialog().VSselectqual(qua, url)

        url=[]
        qua=[]
        sPattern = 'file:\s*"([^"]+)".+?label:\s*"([^"]+)'
        aResult = oParser.parse(sHtmlContent,sPattern)
        if aResult[0] is True:
            for aEntry in aResult[1]:

                url.append(aEntry[0])
                qua.append(aEntry[1])
            if url:
                api_call = dialog().VSselectqual(qua,url)

        if api_call:
            return True, api_call.replace(' ','%20')

        return False, False
