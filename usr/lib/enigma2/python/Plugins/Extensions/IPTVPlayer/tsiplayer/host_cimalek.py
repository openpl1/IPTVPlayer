# -*- coding: utf-8 -*-

import re

from Plugins.Extensions.IPTVPlayer.components.iptvplayerinit import \
    TranslateTXT as _
from Plugins.Extensions.IPTVPlayer.libs import ph
from Plugins.Extensions.IPTVPlayer.libs.tstools import (TSCBaseHostClass,
                                                        gethostname, tscolor,
                                                        tshost)


def getinfo():
    info_ = {}
    name = 'Cimalek'
    hst = 'https://cimalek.to'
    info_['old_host'] = hst
    hst_ = tshost(name)
    if hst_ != '':
        hst = hst_
    info_['host'] = hst
    info_['name'] = name
    info_['version'] = '1.2 29/10/2023'
    info_['dev'] = 'MOHAMED_OS'
    info_['cat_id'] = '21'
    info_['desc'] = 'أفلام, مسلسلات عربية و اجنبية'
    info_['icon'] = 'https://i.ibb.co/qR8xY8G/cimalek.png'
    info_['recherche_all'] = '1'
    return info_


class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self, {'cookie': 'cimalek.cookie'})
        self.MAIN_URL = getinfo()['host']
        self.USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0'
        self.HEADER = {'User-Agent': self.USER_AGENT, 'Connection': 'keep-alive', 'Accept-Encoding': 'gzip', 'Content-Type': 'application/json; charset=UTF-8', 'Referer': self.getMainUrl(), 'Origin': self.getMainUrl()}
        self.defaultParams = {'header': self.HEADER, 'with_metadata': True, 'use_cookie': True, 'load_cookie': True, 'save_cookie': True, 'cookiefile': self.COOKIE_FILE}

    def showmenu(self, cItem):
        TAB = [('أفــلام', '', '10', 0), ('مسـلسـلات', '', '11', 0), ('الـمـواسـم', '/seasons/', '20', 0), ('الحــلـقــات', '/episodes/', '20', 0), ('المـضـاف حـديـثا', '', '13', 0), ('الاكـثـر مـشـاهـدة', '/trending/', '20', 0)]
        self.add_menu(cItem, '', '', '', '', '', TAB=TAB, search=False)
        self.addDir({'import': cItem['import'], 'category': 'search', 'title': _('Search'), 'search_item': True, 'page': 1, 'hst': 'tshost', 'icon': cItem['icon']})

    def showmenu1(self, cItem):
        self.add_menu(cItem, '<i class="fa fa-film(.*?)class="fa fa-desktop">', '<li.*?href="(.*?)".*?>(.*?)</li>', '', '20', ord=[0, 1], ind_0=cItem['sub_mode'], LINK='/movies/')

    def showmenu2(self, cItem):
        self.add_menu(cItem, 'class="fa fa-desktop(.*?)200163', '<li.*?href="(.*?)".*?>(.*?)</li>', '', '20', ord=[0, 1], ind_0=cItem['sub_mode'], LINK='/series/')

    def showmenu3(self, cItem):
        self.add_menu(cItem, 'class="cat-trending">(.*?)</div>', '<a href="(.*?)".*?<span>(.*?)</span>', '', '20', ord=[0, 1], ind_0=cItem['sub_mode'], LINK='/recent/')

    def showitms(self, cItem):
        page = cItem.get('page', 1)
        URL = cItem.get('url', '')+'page/'+str(page)
        sts, data = self.getPage(URL)
        if sts:
            data = re.findall('"film_list-wrap">(.*?)class="fcmpbox">|class="pagination">', data, re.S)
            if data:
                Liste_els = re.findall('<a href="(.*?)">.*?data-src="(.*?)".*?title">(.*?)class="item">', data[0], re.S)
                for (url, image, titre) in Liste_els:
                    info = self.std_title(ph.clean_html(titre), with_ep=True)
                    self.addDir({'import': cItem['import'], 'category': 'host2', 'title': info.get('title_display'), 'icon': image, 'desc': info.get('desc'), 'mode': '21', 'url': url, 'good_for_fav': True, 'EPG': True, 'hst': 'tshost'})
        self.addDir({'import': cItem['import'], 'category': 'host2', 'title': tscolor('\c00????00')+'Next Page >>'+tscolor('\c00??????'), 'icon': cItem['icon'], 'desc': '', 'mode': '20', 'url': cItem['url'], 'page': page+1})

    def showelms(self, cItem):
        URL = cItem.get('url')
        sts, data = self.getPage(URL)
        if sts:
            if 'series' in URL or 'seasons' in URL:
                Liste_els = re.findall("class='episodesList.*?href='(.*?)'.*?class='serie'>(.*?)</", data, re.S)
                if Liste_els:
                    for (url, titre) in Liste_els:
                        Stitel = ph.clean_html(titre).replace("(", "").replace(")", "")
                        self.addVideo({'import': cItem['import'], 'hst': 'tshost', 'url': url, 'title': Stitel, 'desc': '', 'icon': cItem['icon'], 'good_for_fav': True, 'EPG': True, 'hst': 'tshost'})
            else:
                Liste_els = re.findall(r'dynamic-name">(.*?)</h2>', data, re.S)
                if Liste_els:
                    for titre in Liste_els:
                        self.addVideo({'import': cItem['import'], 'hst': 'tshost', 'url': cItem['url'], 'title': ph.clean_html(titre), 'desc': '', 'icon': cItem['icon'], 'good_for_fav': True, 'EPG': True, 'hst': 'tshost'})

    def get_links(self, cItem):
        urlTab = []
        SitUrl = cItem.get('url')
        URL = self.MAIN_URL+'/wp-json/lalaplayer/v2/'
        if not SitUrl.endswith("watch/"):
            SitUrl = cItem.get('url') + "watch/"
        sts, data = self.getPage(SitUrl)
        if sts:
            WData = re.findall(r'class="player-servers">(.*?)class="module_single_sda">', data, re.S)
            if WData:
                url_ = re.findall(r"data-type='([^']+)'\sdata-post='([^']+)'\sdata-nume='([^']+)'", WData[0], re.S)
                if url_:
                    for (type_, post_, nume_) in url_:
                        sts, GetUrl = self.getPage(URL+'?p='+post_+'&t='+type_+'&n='+nume_, addParams=self.defaultParams)
                        if sts:
                            sitLink = re.findall(r'embed_url":"([^"]+)"', GetUrl.replace("\\", ""), re.S)
                            sts, url_data = self.getPage(sitLink[0], addParams=self.defaultParams)
                            if sts:
                                find_url = re.findall(r'"file":"(.+?)","label":', url_data, re.S)
                                if find_url and find_url[0].startswith(('https', "http")):
                                    Url = find_url[0].replace("\\", "")
                                    urlTab.append({'name': gethostname(Url, True), 'url': Url, 'need_resolve': 0, 'type': "local"})
        return urlTab

    def SearchResult(self, str_ch, page, extra):
        URL = self.MAIN_URL+'/search/'+str_ch+'/page/'+str(page)
        sts, data = self.getPage(URL)
        if sts:
            data = re.findall(r'"film_list-wrap">(.*?)class="fcmpbox">', data, re.S)
            if data:
                Liste_els = re.findall(r'<a href="(.*?)">.*?data-src="(.*?)".*?alt="(.*?)">', data[0], re.S)
                for (url, image, titre) in Liste_els:
                    info = self.std_title(titre, with_ep=True)
                    self.addDir({'import': extra, 'category': 'host2', 'title': info.get('title_display'), 'icon': image, 'desc': info.get('desc'), 'mode': '21', 'url': url, 'good_for_fav': True, 'hst': 'tshost'})

    def getArticle(self, cItem):
        URL = cItem.get('url')
        if 'series' in URL or 'seasons' in URL or 'episodes' in URL:
            Desc = [('Rate', 'class="item rating">(.+?)</', '\n', ''), ('Quality', 'class="item quality">(.*?)<a', '\n', ''), ('Year', 'class="tick-item">(.+?)</', '\n', ''),
                    ('Generes', 'type=series">(.+?)</', '\n', ''), ('Story', 'class="text">(.+?)</', '\n', '')]
        else:
            Desc = [('Rate', 'class="item rating">(.+?)</', '\n', ''), ('Quality', '"item quality">.+?tick-quality">(.+?)</', '\n', ''), ('Year', 'item year">.+?tick-quality">(.+?)</', '\n', ''),
                    ('Generes', 'type=movies">(.+?)</', '\n', ''), ('Story', 'film-description w-hide">.+?class="text">(.+?)</', '\n', '')]
        desc = self.add_menu(cItem, '', 'id="ani_detail">(.+?)class="module_single_sda">', '', 'desc', Desc=Desc)
        if desc == '':
            desc = cItem.get('desc', '')
        return [{'title': cItem['title'], 'text': desc, 'images': [{'title': '', 'url': cItem.get('icon', '')}], 'other_info': {}}]
