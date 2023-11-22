#-*- coding: utf-8 -*-
#Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import (
    VSlog, dialog, isKrypton)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'vidlox', 'Vidlox')
        if not isKrypton():
            self._defaultDisplayName = '(Windows\Android Nécessite Kodi17)' + ' Vidlox'

    def setUrl(self, url):
        url = url.replace('embed-dlox.me/','embed-')
        self._url = str(url)

    def _getMediaLinkForGuest(self):
        VSlog(self._url)
        oParser = cParser()
        oRequest = cRequestHandler(self._url)
        oRequest.addHeaderEntry('Referer', "https://vidlox.me/8m8p7kane4r1.html")
        sHtmlContent = oRequest.request()

        #accelère le traitement
        sHtmlContent = oParser.abParse(sHtmlContent, 'var player', 'vvplay')

        sPattern = '([^"]+\.mp4)'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            #initialisation des tableaux
            url=[]
            qua=["HD", "SD"] #sd en 2eme pos generalement quand sd
            api_call = ''

            #Remplissage des tableaux
            for i in aResult[1]:
                url.append(str(i))

            #dialogue qualité
            api_call = dialog().VSselectqual(qua, url)

        if api_call:
            return True, api_call

        return False, False
