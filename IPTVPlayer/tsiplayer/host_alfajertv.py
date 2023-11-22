# -*- coding: utf-8 -*-

import re

from Plugins.Extensions.IPTVPlayer.components.iptvplayerinit import \
    TranslateTXT as _
from Plugins.Extensions.IPTVPlayer.libs import ph
from Plugins.Extensions.IPTVPlayer.libs.tstools import (TSCBaseHostClass,
                                                        tscolor, tshost)


def getinfo():
    info_ = {}
    name = 'FajerShow'
    hst = 'https://show.alfajertv.com'
    info_['old_host'] = hst
    hst_ = tshost(name)
    if hst_ != '':
        hst = hst_
    info_['host'] = hst
    info_['name'] = name
    info_['version'] = '1.1 24/07/2023'
    info_['dev'] = 'MOHAMED_OS'
    info_['cat_id'] = '21'
    info_['desc'] = 'أفلام, مسلسلات عربية و اجنبية'
    info_['icon'] = 'https://i.ibb.co/Vmc6jXz/alfajertv.png'
    info_['recherche_all'] = '1'
    return info_


class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self, {})
        self.MAIN_URL = getinfo()['host']
        self.HTTP_HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0', 'referer': self.MAIN_URL}

    def showmenu(self, cItem):
        TAB = [('رمـــضــان 2023', '/genre/ramadan2023/', '20', 0), ('أفــلام', '', '10', 0), ('مسـلسـلات', '', '11', 0), ('مسـرحـيـات', '/genre/plays/', '20', 0)]
        self.add_menu(cItem, '', '', '', '', '', '', TAB=TAB, search=False)
        self.addDir({'import': cItem['import'], 'category': 'search', 'title': _('Search'), 'search_item': True, 'page': 1, 'hst': 'tshost', 'icon': cItem['icon']})

    def showmenu1(self, cItem):
        self.add_menu(cItem, r'id=["\']menu-item-12093["\'](.*?)id=["\']menu-item-13336["\']', r'<a href=["\'](.*?)["\']>(.*?)</a>', '', '20', ord=[0, 1], ind_0=cItem['sub_mode'], LINK='/movies/')

    def showmenu2(self, cItem):
        self.add_menu(cItem, r'id=["\']menu-item-12097["\'](.*?)id=["\']menu-item-12098["\']', r'<a href=["\'](.*?)["\']>(.*?)</a>', '', '20', ord=[0, 1], ind_0=cItem['sub_mode'], LINK='/tvshows/')

    def getTag(self, url):
        if 'turkish-movies' in url or 'indian-series' in url or 'plays' in url or 'ramadan2023' in url:
            return True
        return False

    def showitms(self, cItem):
        getTag = self.getTag(cItem.get('url'))
        if getTag:
            URL = cItem.get('url')
        else:
            page = cItem.get('page', 1)
            URL = cItem.get('url')+'page/'+str(page)
        sts, data = self.getPage(URL)
        if sts:
            data = re.findall(r'class=["\']items["\']>(.*?)["\']sidebar scrolling["\']>', data, re.S)[0]
            if data:
                Liste_els = re.findall(r'src=["\'](.*?)["\'].*?alt=["\'](.*?)["\'].*?href=["\'](.*?)["\']', data, re.S)
                for (image, titre, url) in Liste_els:
                    info = self.std_title(ph.clean_html(titre), with_ep=True)
                    self.addDir({'import': cItem['import'], 'category': 'host2', 'title': info.get('title_display'), 'icon': image, 'desc': info.get('desc'), 'mode': '21', 'url': url, 'good_for_fav': True, 'EPG': True, 'hst': 'tshost'})
        if getTag is False:
            self.addDir({'import': cItem['import'], 'category': 'host2', 'title': tscolor('\c00????00')+'Next Page >>'+tscolor('\c00??????'), 'icon': cItem['icon'], 'desc': '', 'mode': '20', 'url': cItem['url'], 'page': page+1})

    def showelms(self, cItem):
        sts, data = self.getPage(cItem.get('url'))
        if sts:
            if 'tvshows' in cItem.get('url'):
                Liste_els = re.findall(r'["\']episodiotitle["\']>.*?href=["\'](.*?)["\']>(.*?)</a>', data, re.S)
                if Liste_els:
                    for (url, titre) in Liste_els:
                        self.addVideo({'import': cItem['import'], 'hst': 'tshost', 'url': url, 'title': self.std_extract(titre), 'desc': '', 'icon': cItem['icon'], 'good_for_fav': True, 'EPG': True, 'hst': 'tshost'})
            else:
                Liste_els = re.findall(r'["\']data["\']>.*?<h1>(.*?)</h1>', data, re.S)
                if Liste_els:
                    for titre in Liste_els:
                        self.addVideo({'import': cItem['import'], 'hst': 'tshost', 'url': cItem['url'], 'title': ph.clean_html(titre), 'desc': '', 'icon': cItem['icon'], 'good_for_fav': True, 'EPG': True, 'hst': 'tshost'})

    def get_links(self, cItem):
        urlTab = []
        sts, data = self.getPage(cItem['url'])
        if sts:
            URL = self.MAIN_URL + '/wp-admin/admin-ajax.php'
            aResult = re.findall(r'data-type=["\'](.*?)["\'].*?data-post=["\'](.*?)["\'].*?data-nume=["\'](.*?)["\']', data, re.S)
            if aResult:
                for (type_, post_, nume_) in aResult:
                    params = {'action': 'doo_player_ajax', 'post': post_, 'nume': nume_, 'type': type_}
                    sts, data = self.getPage(URL, self.HTTP_HEADER, params)
                    if sts:
                        siteUrl = re.findall(r'<iframe.*?src=["\'](.*?)["\'] frameborder', data, re.S)[0]
                        sTitel = re.findall(r"\//(.*?)\/", siteUrl, re.S)[0].replace('show.alfajertv.com', 'سيرفر فلسـطيـن')
                        urlTab.append({'name': sTitel, 'url': siteUrl, 'need_resolve': 1})
        return urlTab

    def SearchResult(self, str_ch, page, extra):
        URL = self.MAIN_URL+'/?s='+str_ch
        sts, data = self.getPage(URL)
        if sts:
            data = re.findall(r'class=["\']details["\']>(.*?)["\']sidebar scrolling["\']>', data, re.S)[0]
            if data:
                Liste_els = re.findall(r'src=["\'](.*?)["\'].*?alt=["\'](.*?)["\'].*?href=["\'](.*?)["\']', data, re.S)
                for (image, titre, url) in Liste_els:
                    info = self.std_title(ph.clean_html(titre), with_ep=True)
                    sTitel = info.get('title_display')
                    desc_ = info.get('desc')
                    self.addDir({'import': extra, 'category': 'host2', 'title': sTitel, 'icon': image, 'desc': desc_, 'mode': '21', 'url': url, 'good_for_fav': True, 'hst': 'tshost'})

    def getArticle(self, cItem):
        if 'episodes' in cItem.get('url'):
            Desc = [('Year', 'class=["\']date["\']>.+?([^,]\d+)</span>', '\n', ''), ('Story', 'itemprop=["\']description["\'].+?<p>(.+?)</', '\n', '')]
            desc = self.add_menu(cItem, '', 'id=["\']info["\'](.+?)<div class=["\']sbox["\']>', '', 'desc', Desc=Desc)
        else:
            Desc = [('Year', 'class=["\']date["\']>.+?([^,]\d+)</span>', '\n', ''), ('Generes', 'genre.+?tag["\']>(.+?)</', '\n', ''), ('Rate', 'data-rating=["\']([^["\']]+)["\']', '\n', ''),
                    ('Time', 'class=["\']runtime["\']>(.+?)</', '\n', ''), ('Story', 'itemprop=["\']description["\'].+?<p>(.+?)</', '\n', '')]
            desc = self.add_menu(cItem, '', 'class=["\']sheader["\']>(.+?)class=["\']sbox srelacionados["\']>', '', 'desc', Desc=Desc)
        if desc == '':
            desc = cItem.get('desc', '')
        return [{'title': cItem['title'], 'text': desc, 'images': [{'title': '', 'url': cItem.get('icon', '')}], 'other_info': {}}]
