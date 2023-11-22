# -*- coding: utf-8 -*-
# vStream https://github.com/Kodi-vStream/venom-xbmc-addons

from Plugins.Extensions.IPTVPlayer.libs.xbmc import xbmcvfs
from Plugins.Extensions.IPTVPlayer.tools.iptvtools import GetCacheSubDir

# -----------------------
#     Cookies gestion
# ------------------------


class GestionCookie():
    PathCache = GetCacheSubDir('Tsiplayer')[:-1]
    def MakeListwithCookies(self,c):
        t = {}
        c = c.split(';')
        for i in c:
            j = i.split('=',1)
            if len(j) > 1:
                t[j[0]] = j[1]

        return t


    def DeleteCookie(self, Domain):
        Name = '/'.join([self.PathCache, 'cookie_%s.txt']) % (Domain)
        xbmcvfs.delete(Name)

    def SaveCookie(self, Domain, data):
        Name = '/'.join([self.PathCache, 'cookie_%s.txt']) % (Domain)

        f = xbmcvfs.File(Name, 'w')
        f.write(data)
        f.close()

    def Readcookie(self, Domain):
        Name = '/'.join([self.PathCache, 'cookie_%s.txt']) % (Domain)

        try:
            f = xbmcvfs.File(Name)
            data = f.read()
            f.close()
        except:
            return ''

        return data

    def AddCookies(self):
        cookies = self.Readcookie(self.__sHosterIdentifier)
        return 'Cookie=' + cookies

    def MixCookie(self,ancien_cookies, new_cookies):
        t1 = self.MakeListwithCookies(ancien_cookies)
        t2 = self.MakeListwithCookies(new_cookies)
        #Les nouveaux doivent ecraser les anciens
        for i in t2:
            t1[i] = t2[i]

        cookies = ''
        for c in t1:
            cookies = cookies + c + '=' + t1[c] + ';'
        cookies = cookies[:-1]
        return cookies

# -------------------------------
#     Configuration gestion
# -------------------------------

class cConfig():

    def isDharma(self):
        return self.__bIsDharma

    def getSettingCache(self):
        return False

    def getAddonPath(self):
        return False

    def getRootArt(self):
        return False

    def getFileFav(self):
        return False

    def getFileDB(self):
        return False

    def getFileCache(self):
        return False


def WindowsBoxes(sTitle, sFileName, metaType, year=''):
    return False
