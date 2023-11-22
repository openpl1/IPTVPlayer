# -*- coding: utf-8 -*-

import base64
import re

from Plugins.Extensions.IPTVPlayer.libs import ph
from Plugins.Extensions.IPTVPlayer.libs.tstools import (TSCBaseHostClass,
                                                        tscolor, tshost,
                                                        unifurl)


def getinfo():
    info_ = {}
    name = 'Tvfun'
    hst = 'https://www.tv-f.com'
    info_['old_host'] = hst
    hst_ = tshost(name)
    if hst_ != '':
        hst = hst_
    info_['host'] = hst
    info_['name'] = name
    info_['version'] = '1.0 16/11/2023'
    info_['dev'] = 'MOHAMED_OS'
    info_['cat_id'] = '21'
    info_['desc'] = 'مسلسلات عربية و اجنبية'
    info_['icon'] = 'https://i.ibb.co/jwRjn0w/tvfun.png'
    info_['recherche_all'] = '0'
    return info_


class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self, {})
        self.MAIN_URL = getinfo()['host']

    def showmenu(self, cItem):
        TAB = [('مــسـلـسـلات', '', '10', 'serie')]
        self.add_menu(cItem, '', '', '', '', '', '', TAB=TAB, search=False)

    def showmenu1(self, cItem):
        self.CimaLina_TAB = [
            {'category': 'host2', 'title': 'مسـلـسـلات تـركـيـة', 'url': self.MAIN_URL+'/cat/mosalsalat-torkia/',  'mode': '20'},
            {'category': 'host2', 'title': 'مسـلـسـلات هنــديـة', 'url': self.MAIN_URL+'/cat/mosalsalat-hindia/',  'mode': '20'},
            {'category': 'host2', 'title': 'مسـلـسـلات عــربــيـة', 'url': self.MAIN_URL+'/cat/mosalsalat-3arabia/',  'mode': '20'},
            {'category': 'host2', 'title': 'مسـلـسـلات مـغربـيـة', 'url': self.MAIN_URL+'/cat/mosalsalat-maghribia/',  'mode': '20'},
            {'category': 'host2', 'title': 'مسـلـسـلات لاتـنـيـة', 'url': self.MAIN_URL+'/cat/mosalsalat-latinia/', 'mode': '20'},
            {'category': 'host2', 'title': 'مسـلـسـلات كـوريــة', 'url': self.MAIN_URL+'/cat/mosalsalat-korea/',  'mode': '20'},
            {'category': 'host2', 'title': 'مسـلـسـلات مدبـلـجـة', 'url': self.MAIN_URL+'/ts/mosalsalat-modablaja/',  'mode': '20'},
            {'category': 'host2', 'title': 'مسـلـسـلات مـترجــمـة', 'url': self.MAIN_URL+'/ts/mosalsalat-motarjama/',  'mode': '20'},
            {'category': 'host2', 'title': 'زي ألـــوان', 'url': self.MAIN_URL+'/ts/zee-alwan/',  'mode': '20'}]
        self.listsTab(self.CimaLina_TAB, {'import': cItem.get('import', ''), 'icon': cItem.get('icon', '')})

    def showitms(self, cItem):
        page = cItem.get('page', 1)
        URL = "{}?pageNo={}".format(cItem.get('url'),str(page))
        sts, data = self.getPage(URL)
        if sts:
            Liste_els = re.findall(r'class="serie-thumb">.*?href="(.+?)".*?title="(.+?)"><img.+?src="(.+?)"', data, re.S)
            for (url, titre, image) in Liste_els:
                info = self.std_title(ph.clean_html(titre), with_ep=True)
                sTitel = info.get('title_display')
                self.addDir({'import': cItem['import'], 'category': 'host2', 'title': sTitel, 'icon': image, 'desc': '', 'mode': '21', 'url': self.MAIN_URL + url, 'good_for_fav': True, 'EPG': True, 'hst': 'tshost'})
        self.addDir({'import': cItem['import'], 'category': 'host2', 'title': tscolor('\c00????00')+'Next Page >>' + tscolor('\c00??????'), 'icon': cItem['icon'], 'desc': '', 'mode': '20', 'url': cItem['url'], 'page': page+1})

    def showelms(self, cItem):
        page = cItem.get('page',1)
        URL = "{}page,{}/".format(cItem.get('url'),str(page))
        sts, data = self.getPage(URL)
        if sts:
            Liste_els = re.findall(r'class="video-thumb">.*?href="(.+?)".*?title="(.+?)"><img', data, re.S)
            for (url, titre) in Liste_els:
                info = self.std_title(ph.clean_html(titre), with_ep=True)
                sTitel = info.get('title_display')
                self.addVideo({'import': cItem['import'], 'hst': 'tshost', 'url': self.MAIN_URL + url, 'title': sTitel, 'desc': '', 'icon': cItem['icon'], 'good_for_fav': True, 'EPG': True, 'hst': 'tshost'})
            if 'class="pagination"' in data:
                self.addMore({'import':cItem['import'],'category' : 'host2','title':tscolor('\c00????00')+'Add More'+tscolor('\c00??????'),'icon':cItem['icon'],'desc':'','mode':'21','url':cItem['url'],'page':page+1})

    def get_links(self, cItem):
        urlTab = []
        sts, data = self.getPage(cItem['url'])
        if sts:
            siteUrl = re.findall(r"PGlmcmFt(.+?)'.+?server color.+?>(.+?)</", data, re.S)
            for (url, titre) in siteUrl:
                urlTab.append({'name': titre, 'url': 'hst#tshost#' + url, 'need_resolve': 1})
        return urlTab

    def getVideos(self, videoUrl):
        from Plugins.Extensions.IPTVPlayer.tools.iptvtools import printDBG
        urlTab = []
        data = str(base64.b64decode(videoUrl))
        sUrl = re.findall(r'src=(.+?)".+?allowfullscreen', data, re.S)
        URL_ = unifurl(sUrl[0].replace('"', ''))
        urlTab.append((URL_, '1'))
        return urlTab

    def getArticle(self, cItem):
        Desc = [('Desc', 'class="maxw">.+?<p>(.*?)</p>', '\n', '')]
        desc = self.add_menu(cItem, '', '', '', 'desc', Desc=Desc)
        if desc == '':
            desc = cItem.get('desc', '')
        return [{'title': cItem['title'], 'text': desc, 'images': [{'title': '', 'url': cItem.get('icon', '')}], 'other_info': {}}]
