﻿
import unicodedata

from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.hosters.hoster import \
    iHoster
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.handler.requestHandler import \
    cRequestHandler
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.packer import \
    cPacker
from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.matrix.resources.lib.parser import \
    cParser


class cHoster(iHoster):

    def __init__(self):
        iHoster.__init__(self, 'fileupload', 'File-Upload')

    def isDownloadable(self):
        return True

    def _getMediaLinkForGuest(self):
        oParser = cParser()

        if 'embed' not in self._url:
            Vid = self._url.split("/")[3]
            self._url = self._url.replace(Vid,('embed-'+Vid+'-1920x1080.html'))

        api_call = ''

        oRequest = cRequestHandler(self._url)
        sHtmlContent = oRequest.request()


        sPattern = '(eval\(function\(p,a,c,k,e(?:.|\s)+?\))<\/script>'
        aResult = oParser.parse(sHtmlContent, sPattern)
        if aResult[0]:
            data = aResult[1][0]
            data = unicodedata.normalize('NFD', data).encode('ascii', 'ignore').decode('unicode_escape')
            sHtmlContent2 = cPacker().unpack(data)

            sPattern = 'file:"(.+?)"'
            aResult = oParser.parse(sHtmlContent2, sPattern)
            if aResult[0]:
                api_call = aResult[1][0]

        if api_call:
            return True, api_call + "|verifypeer=false"

        return False, False