# -*- coding: utf-8 -*-
from Plugins.Extensions.IPTVPlayer.libs.tstools import (TSCBaseHostClass,
                                                        tscolor)


def getinfo():
    info_={}
    info_['name'] = ' >●★| Ramadan' + tscolor('\c0000????') + ' 2023 ' + tscolor('\c00??????') + '|★●<'
    info_['version']='4.0 22/03/2023'
    info_['dev']='RGYSoft'
    info_['cat_id']='21'
    info_['desc']='أفلام و مسلسلات رمضان 2023'
    info_['icon']='https://i.ibb.co/pQ8LgPr/Ramadan.png'
    return info_


class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self,{'cookie':'tsiplayer.cookie'})

    def showmenu00(self,cItem):
        self.addDir({'import':cItem['import'],'category' :'host2','title':'رمضان 2020' ,'icon':cItem['icon'],'mode':'20','sub_mode':0})
        self.addDir({'import':cItem['import'],'category' :'host2','title':'رمضان 2019' ,'icon':cItem['icon'],'mode':'20','sub_mode':1})

    def showmenu0(self,cItem):
        sub_mode=cItem.get('sub_mode', 0)
        if sub_mode==0:
            self.addDir({'category': 'host2', 'title': tscolor('\c0000????')+'Assabile'  , 'mode': '00', 'url': '', 'import': 'from Plugins.Extensions.IPTVPlayer.tsiplayer.host_assabile import ', 'icon':cItem['icon'], 'type': 'category', 'desc': 'Quran Audio Library'})
            self.addDir({'category': 'host2', 'title': tscolor('\c0000????')+'MP3Quran'  , 'mode': '00', 'url': '', 'import': 'from Plugins.Extensions.IPTVPlayer.tsiplayer.host_mp3quran import ', 'icon':cItem['icon'], 'type': 'category', 'desc': 'Quran Audio Library'})
            self.addDir({'category': 'host2', 'title': 'Cima4u', 'mode': '30', 'url': '/category/مسلسلات-7series/مسلسلات-رمضان-2023/', 'name': 'category', 'import': 'from Plugins.Extensions.IPTVPlayer.tsiplayer.host_cima4u import ', 'type': 'category', 'icon':cItem['icon']})
            self.addDir({'category': 'host2', 'title': 'Akwam' , 'mode': '30', 'url': '/series?section=0&category=87&rating=0&year=2023&language=0&formats=0&quality=0', 'import': 'from Plugins.Extensions.IPTVPlayer.tsiplayer.host_akwam import ', 'icon':cItem['icon'], 'type': 'category', 'desc': ''})
            self.addDir({'category': 'host2', 'title': 'Extra-3sk' , 'mode': '20', 'url': '/category/ramadan-2023', 'sub_mode': '0', 'import': 'from Plugins.Extensions.IPTVPlayer.tsiplayer.host_extra3sk import ', 'type': 'category', 'icon':cItem['icon']})
            self.addDir({'category': 'host2', 'title': 'CimaNow'   , 'mode': '20', 'url': '/category/رمضان-2023/', 'mode': '20', 'import': 'from Plugins.Extensions.IPTVPlayer.tsiplayer.host_cimanow import ', 'type': 'category', 'icon':cItem['icon']})
            self.addDir({'category': 'host2', 'title': 'Wecima'    , 'mode': '20', 'url': '/category/مسلسلات/مسلسلات-رمضان-2023-series-ramadan-2023/', 'import': 'from Plugins.Extensions.IPTVPlayer.tsiplayer.host_mycima import ', 'icon':cItem['icon'], 'type': 'category', 'desc': ''})


    def start(self,cItem):
        mode=cItem.get('mode', None)
        if mode=='00':
            self.showmenu0(cItem)
        if mode=='20':
            self.showmenu1(cItem)
        return True

