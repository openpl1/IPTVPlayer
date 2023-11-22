# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons
# Ovni-crea
import json

from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import \
    VSlog
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.premiumHandler import \
    cPremiumHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler


class cHoster(iHoster):
    def __init__(self):
        iHoster.__init__(self, 'alldebrid', 'Alldebrid', 'violet')
        self.__sRealHost = ''

    def setRealHost(self, host):
        self.__sRealHost = "/" + host

    def setDisplayName(self, displayName):
        self._displayName = displayName + ' [COLOR violet]'+ self._defaultDisplayName + self.__sRealHost + '[/COLOR]'

    def _getMediaLinkForGuest(self):
        VSlog(self._url)
        token_Alldebrid = cPremiumHandler(self.getPluginIdentifier()).getToken()
        if token_Alldebrid:
            sUrl_Bypass = "https://api.alldebrid.com/v4/link/unlock?agent=service&version=1.0-&apikey=" + \
                token_Alldebrid + "&link=" + self._url
        else:
            return False, False

        oRequest = cRequestHandler(sUrl_Bypass)
        sHtmlContent = json.loads(oRequest.request())

        if 'error' in sHtmlContent:
            if sHtmlContent['error']['code'] == 'LINK_HOST_NOT_SUPPORTED':
                # si alldebrid ne prend pas en charge ce type de lien, on retourne le lien pour utiliser un autre hoster
                return False, self._url
            else:
                VSlog('Hoster Alldebrid - Error: ' + sHtmlContent["error"]['code'])
                return False, False

        api_call = HostURL = sHtmlContent["data"]["link"]
        try:
            mediaDisplay = HostURL.split('/')
            VSlog('Hoster Alldebrid - play : %s/ ... /%s' % ('/'.join(mediaDisplay[0:3]), mediaDisplay[-1]))
        except:
            VSlog('Hoster Alldebrid - play : ' + HostURL)

        if api_call:
            return True, api_call

        return False, False
