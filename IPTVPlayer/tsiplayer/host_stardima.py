# -*- coding: utf8 -*-
import base64
import re

from Plugins.Extensions.IPTVPlayer.libs.tstools import (T, TSCBaseHostClass,
                                                        tshost)
from Plugins.Extensions.IPTVPlayer.tools.iptvtools import printDBG


def getinfo():
    info_ = {}
    name = 'Stardima'
    hst = 'https://www.stardima.co'
    info_['old_host'] = hst
    hst_ = tshost(name)
    if hst_ != '':
        hst = hst_
    info_['host'] = hst
    info_['name'] = name
    info_['version'] = '2.1 03/11/2023'
    info_['dev'] = 'RGYSoft'
    info_['cat_id'] = '22'
    info_['desc'] = 'افلام و مسلسلات كرتون'
    info_['icon'] = 'https://i.ibb.co/c10TPqS/stardima.png'
    info_['recherche_all'] = '0'
    return info_


class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self, {'cookie': 'stardima.cookie'})
        self.MAIN_URL = getinfo()['host']

    def showmenu(self, cItem):
        TAB = [('افلام', '/watch/movies/', '20', 0), ('مسلسلات - مواسم', '/watch/seasons/', '20', 1), ('مسلسلات - حلقات', '/watch/episodes/', '20', 2)]  # ,('قنوات بث مباشر','','10',3)]
        self.add_menu(cItem, '', '', '', '', '', TAB=TAB, search=False)
        self.addDir({'import': cItem['import'], 'category': 'host2', 'title': T('Search'), 'icon': cItem['icon'], 'mode': '51'})

    def showitms(self, cItem):
        next = ['rel=["\']next["\'].*?href=["\'](.*?)["\']', '20']
        self.add_menu(cItem, '<header class=["\']archive_post["\']>(.*?)["\']pagination["\']',
                      '<article.*?class=["\']item.*?data-src=["\'](.*?)["\'].*?alt=["\'](.*?)["\'](.*?)href=["\'](.*?)["\'](.*?)</article>', '', '21', ord=[3, 1, 0, 2, 4], Next=next, u_titre=True, bypass=True)

    def showelms(self, cItem):
        printDBG('cItem='+str(cItem))
        if "seasons" in cItem['url']:
            URL = cItem.get('url', '')
            sts, data = self.getPage(URL)
            if sts:
                Liste_els = re.findall(r'class=["\']episodiotitle["\']>.*?href=["\'](.*?)["\']>(.*?)</a>', data, re.S)
                if Liste_els:
                    for (url, titre) in Liste_els:
                        self.addVideo({'import': cItem['import'], 'category': 'host2', 'title': titre, 'url': url, 'desc': cItem['desc'], 'icon': cItem['icon'], 'good_for_fav': True, 'hst': 'tshost'})
        else:
            self.add_menu(cItem, '<ul class=["\']episodios["\']>(.*?)</ul>', '<li.*?src=["\'](.*?)["\'].*?numerando["\']>(.*?)<.*?href=["\'](.*?)["\'](.*?)</li>', '', 'video', ord=[2, 1, 0, 3])

    def SearchAll(self, str_ch, page=1, extra='', type_=''):
        return self.get_items({'page': page, 'import': extra, 'str_ch': str_ch})

    def SearchAnims(self, str_ch, page=1, extra=''):
        elms = self.SearchAll(str_ch, page, extra=extra, type_='')
        return elms

    def get_items(self, cItem={}):
        elms = []
        extra = cItem.get('import')
        str_ch = cItem.get('str_ch')
        page = cItem.get('page', 1)

        url = self.MAIN_URL+'/watch/page/'+str(page)+'/?s='+str_ch
        sts, data = self.getPage(url)
        if sts:
            films_list = re.findall(r'<article.*?href=["\'](.*?)["\'].*?src=["\'](.*?)["\'].*?alt=["\'](.*?)["\'](.*?)</article>', data, re.S)
            for (url, image, titre, desc) in films_list:
                desc = self.extract_desc(desc, [('type', 'class=["\']episodes["\']>(.*?)</span>'), ('type', 'class=["\']movies["\']>(.*?)</span>'), ('year', 'class=["\']year["\']>(.*?)</span>'), ('plot', 'class=["\']contenido["\']>(.*?)</div>')])
                info = self.std_title(titre, with_type=True)
                desc = info.get('desc')
                titre = info.get('title_display')
                image = self.std_url(image)
                elms.append({'import': cItem['import'], 'category': 'host2', 'title': titre, 'url': url, 'desc': desc, 'icon': image, 'mode': '21', 'good_for_fav': True, 'EPG': True, 'hst': 'tshost', 'info': info})
            films_list = re.findall(r'id=["\']nextpagination["\']', data, re.S)
            if films_list:
                elms.append({'import': extra, 'category': 'host2', 'title': T('Next'), 'url': '', 'desc': 'Next', 'icon': '', 'hst': 'tshost', 'mode': '51', 'page': page+1, 'str_ch': str_ch, 'type_': ''})
        return elms

    def SearchResult(self, str_ch, page, extra):
        url = self.MAIN_URL+'/watch/page/'+str(page)+'/?s='+str_ch
        desc = [('Type', 'class=["\']episodes["\']>(.*?)</span>', '', ''), ('Type', 'class=["\']movies["\']>(.*?)</span>', '', ''), ('Year', 'class=["\']year["\']>(.*?)</span>', '', ''), ('Story', 'class=["\']contenido["\']>(.*?)</div>', '\n', '')]
        self.add_menu({'import': extra, 'url': url}, '', '<article.*?href=["\'](.*?)["\'].*?src=["\'](.*?)["\'].*?alt=["\'](.*?)["\'](.*?)</article>', '', '21', ord=[0, 2, 1, 3], Desc=desc, u_titre=True)

    def get_links(self, cItem):
        urlTab = []
        URL = cItem['url']
        sts, data = self.getPage(URL)
        if sts:
            Liste_els = re.findall('<li id=["\']player.*?class=["\'](.*?)["\'].*?data-type=["\'](.*?)["\'].*?data-post=["\'](.*?)["\'].*?data-nume=["\'](.*?)["\']', data, re.S)
            for (action, type_, post_, nume) in Liste_els:
                URL = 'hst#tshost#'+action+'|||'+type_+'|||'+post_+'|||'+nume
                titre = '|Watch Server| Server '+nume
                urlTab.append({'name': titre, 'url': URL, 'need_resolve': 1})
            Liste_els = re.findall('<input rel=["\']nofollow["\'] .*?.open\(["\'](.*?)["\'].*?value=["\'](.*?)["\']', data, re.S)
            for (url, titre) in Liste_els:
                titre = titre.replace('إضغط هنا لتحميل الجودة ✔', 'Download Server')
                titre = titre.replace('إضغط هنا تحميل جودة ✔', 'Download Server')
                if '|' in titre:
                    titre = '|'+titre.split('|')[-1].strip()+'| '+titre.split('|')[0].strip()+'p'
                url = url.replace('https://freestore.app/?download=', 'https://www.stardima.net/player/download.php?slug=')
                urlTab.append({'name': titre, 'url': url, 'need_resolve': 0, 'type': 'local'})
        return urlTab

    def getVideos(self, videoUrl):
        urlTab = []
        action, type_, post_, nume = videoUrl.split('|||')
        # url='https://www.stardima.co/wp-json/dooplayer/v2/'+post_+'/'+type_+'/'+nume

        url_post = 'https://stardima.vip/watch/wp-admin/admin-ajax.php'
        post_data = {'action': 'doo_player_ajax', 'post': post_, 'nume': nume, 'type': type_}

        sts, data = self.getPage(url_post, post_data=post_data)
        if sts:
            Liste_els = re.findall('["\']embed_url["\']:["\'](.*?)["\']', data, re.S | re.IGNORECASE)
            if Liste_els:
                URL_ = Liste_els[0].replace('\\', '')
                if '/embed2/?id=' in URL_:
                    URL_ = URL_.split('/embed2/?id=', 1)[1]
                URL_ = str(base64.b64decode(URL_))
                if '?id=' in URL_:
                    URL_ = URL_.split('?id=', 1)[1]
                print(URL_)
                urlTab.append((URL_, '1'))
        return urlTab

    def SearchResult1(self, str_ch, page, extra):
        url_ = 'https://www.stardima.co/page/'+str(page)+'/?s='+str_ch
        sts, data = self.getPage(url_)
        if sts:
            Liste_els = re.findall('class=["\']thumbnail["\']>.*?echo=["\'](.*?)["\'].*?<a href=["\'](.*?)["\'].*?title=["\'](.*?)["\']', data, re.S)
            for (image, url, titre) in Liste_els:
                self.addVideo({'import': extra, 'category': 'host2', 'title': titre, 'url': url, 'icon': image, 'hst': 'tshost', 'good_for_fav': True})
