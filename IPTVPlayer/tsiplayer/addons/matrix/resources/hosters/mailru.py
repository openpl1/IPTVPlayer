# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons


from Plugins.Extensions.IPTVPlayer.p2p3.UrlLib import (urllib2_Request,
                                                       urllib2_URLError,
                                                       urllib_urlopen)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.comaddon import (
    VSlog, dialog)
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'mailru', 'MailRu')

    def _getMediaLinkForGuest(self):
        oParser = cParser()
        VSlog(self._url)
        api_call = False

        UA = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'

        headers = {"User-Agent": UA}

        req1 = urllib2_Request(self._url, None, headers)
        resp1 = urllib_urlopen(req1)
        sHtmlContent = resp1.read()
        resp1.close()

        sPattern = '{"metadataUrl":"([^"]+)",'
        aResult = oParser.parse(sHtmlContent, sPattern)

        vurl = 'http://my.mail.ru/' + aResult[1][0]

        req = urllib2_Request(vurl, None, headers)

        try:
            response = urllib_urlopen(req)
        except urllib2_URLError as e:
            print(e.read())
            print(e.reason)

        data = response.read()
        head = response.headers
        response.close()

        # get cookie
        cookies = ''
        if 'Set-Cookie' in head:

            sPattern = '(?:^|,) *([^;,]+?)=([^;,\/]+?);'
            aResult = oParser.parse(str(head['Set-Cookie']), sPattern)
            if aResult[0]:
                for cook in aResult[1]:
                    cookies = cookies + cook[0] + '=' + cook[1] + ';'

        sPattern = '{"url":"([^"]+)",.+?"key":"(\d+p)"}'
        aResult = oParser.parse(data, sPattern)
        if aResult[0]:
            # initialisation des tableaux
            url = []
            qua = []
            # Remplissage des tableaux
            for i in aResult[1]:
                url.append(str(i[0]))
                qua.append(str(i[1]))

            # Affichage du tableau
            api_call = dialog().VSselectqual(qua, url)

        if api_call:
            return True, 'http:' + api_call + '|User-Agent=' + UA + '&Cookie=' + cookies

        return False, False
