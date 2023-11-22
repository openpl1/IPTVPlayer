# -*- coding: utf-8 -*-
import base64
import re

from Plugins.Extensions.IPTVPlayer.libs.tstools import (T, TSCBaseHostClass,
                                                        tshost)


def getinfo():
    info_ = {}
    name = 'Arblionz'
    hst = 'https://arlionztv.sbs'
    info_['old_host'] = hst
    hst_ = tshost(name)
    if hst_ != '':
        hst = hst_
    info_['host'] = hst
    info_['name'] = name
    info_['version'] = '2.1 01/08/2023'
    info_['dev'] = 'RGYSoft'
    info_['cat_id'] = '21'
    info_['desc'] = 'أفلام و مسلسلات عربية و اجنبية'
    info_['icon'] = 'https://i.ibb.co/xMDSfCV/arblionz.png'
    info_['recherche_all'] = '1'
    return info_


class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self, {'cookie': 'arblionz1.cookie'})
        self.MAIN_URL = getinfo()['host']
        self.SiteName = getinfo()['name']

    def getPage1(self, baseUrl, addParams={}, post_data=None):
        baseUrl = self.std_url(baseUrl)
        if addParams == {}:
            addParams = dict(self.defaultParams)
        sts, data = self.cm.getPage(baseUrl, addParams, post_data)
        code = data.meta.get('status_code', '')
        if code == 302:
            new_url = data.meta.get('location', '')
            if not new_url.startswith('http'):
                new_url = self.MAIN_URL + new_url
            new_url = self.std_url(new_url)
            sts, data = self.cm.getPage(new_url, addParams, post_data)
        elif str(data).strip() == '':
            url0 = self.MAIN_URL+'/ajax'
            post_data0 = {'action': 'action_page_load'}
            addParams0 = dict(self.defaultParams)
            addParams0['header']['X-Requested-With'] = 'XMLHttpRequest'
            sts0, data0 = self.cm.getPage(url0, addParams0, post_data0)
            sts, data = self.cm.getPage(baseUrl, addParams, post_data)
        return sts, data

    def showmenu(self, cItem):
        TAB = [('افلام', '', '10', 0), ('مسلسلات', '', '10', 2), ('عروض مصارعة', '/category/other-shows/wrestling/', '20', 0),]
        self.add_menu(cItem, '', '', '', '', '', TAB=TAB, search=False)
        self.addDir({'import': cItem['import'], 'category': 'host2', 'title': T('Search'), 'icon': cItem['icon'], 'mode': '50'})

    def showmenu1(self, cItem):
        self.add_menu(cItem, '(?:ChildsCats">|enresCats">)(.*?)</ul', '<li.*?href="(.*?)".*?>(.*?)</li>', '', '20', Titre='اقسام فرعية', ord=[0, 1], ind_0=cItem['sub_mode'], LINK='/eg/')
        self.add_menu(cItem, '(?:ChildsCats">|enresCats">)(.*?)</ul', '<li.*?href="(.*?)".*?>(.*?)</li>', '', '20', Titre='حسب النوع', ord=[0, 1], ind_0=cItem['sub_mode']+1, LINK='/eg/')

    def showitms(self, cItem):
        elms = self.get_items(cItem)
        for elm in elms:
            if elm.get('type', '') == 'video':
                self.addVideo(elm)
            elif elm.get('type', '') == 'marker':
                self.addMarker(elm)
            else:
                self.addDir(elm)

    def get_items(self, cItem={}):
        elms = []
        extra = cItem.get('import')
        str_ch = cItem.get('str_ch')
        page = cItem.get('page', 1)
        url_ = cItem.get('url', '')
        type_ = cItem.get('type_', '')
        if url_ == '':
            with_type = True
            if type_ == '':
                url0 = self.MAIN_URL+'/search/'+str_ch+'/'
            else:
                url0 = self.MAIN_URL+'/search/'+str_ch+'+'+type_+'/'
        else:
            with_type = False
            url0 = url_
        if (page > 1):
            url0 = url0+'page/'+str(page)+'/'
        sts, data = self.getPage(url0)
        if sts:
            data_list = re.findall('Posts--Single--Box">.*?href="(.*?)".*?title="(.*?)".*?image="(.*?)"(.*?)</a>', data, re.S)
            for (url, titre, image, desc) in data_list:
                if 'Bein Sports' not in titre:
                    info = self.std_title(titre, with_type=with_type)
                    desc = info.get('desc')
                    titre = info.get('title_display')
                    image = self.std_url(image)
                    elms.append({'import': cItem['import'], 'category': 'host2', 'title': titre, 'url': url, 'desc': desc, 'icon': image, 'mode': '21', 'good_for_fav': True, 'EPG': True, 'hst': 'tshost', 'info': info})
            films_list = re.findall('>&raquo;</a>', data, re.S)
            if films_list:
                if '/search/' in url0:
                    mode = '51'
                else:
                    mode = '20'
                elms.append({'import': extra, 'category': 'host2', 'title': T('Next'), 'url': url_, 'desc': 'Next', 'icon': '', 'hst': 'tshost', 'mode': mode, 'page': page+1, 'str_ch': str_ch, 'section': type_})
        return elms

    def showelms(self, cItem):
        post_data = {'href': cItem['url']}
        sts, data = self.getPage(cItem['url'], post_data=post_data)
        if sts:
            data_list = re.findall('class="JsutNumber.*?href="(.*?)".*?>(.*?)</a>', data, re.S)
            if data_list:
                for (url, titre) in data_list:
                    titre = self.cleanHtmlStr(titre)
                    titre = self.std_episode(titre, cItem)
                    self.addVideo({'import': cItem['import'], 'good_for_fav': True, 'category': 'host2', 'url': url, 'desc': '', 'title': titre, 'icon': cItem['icon'], 'EPG': True, 'hst': 'tshost'})
            else:
                self.addVideo({'import': cItem['import'], 'good_for_fav': True, 'category': 'host2', 'url': cItem['url'], 'desc': cItem['desc'], 'title': cItem['title'], 'icon': cItem['icon'], 'EPG': True, 'hst': 'tshost'})

    def showsearch(self, cItem):
        self.addDir({'import': cItem['import'], 'category': 'host2', 'title': 'البحث في الموقع', 'icon': cItem['icon'], 'mode': '51', 'section': ''})
        self.addDir({'import': cItem['import'], 'category': 'host2', 'title': 'البحث عن فيلم', 'icon': cItem['icon'], 'mode': '51', 'section': 'فيلم'})
        self.addDir({'import': cItem['import'], 'category': 'host2', 'title': 'البحث عن مسلسل', 'icon': cItem['icon'], 'mode': '51', 'section': 'مسلسل'})

    def SearchAll0(self, str_ch, page=1, extra='', type_='', icon=''):
        elms = []
        if type_ != '':
            type_ = ' ' + type_
        url_ = self.MAIN_URL+'/search/'+str_ch+type_+'/page/'+str(page)+'/'
        sts, data = self.getPage(url_)
        if sts:
            data_list = re.findall('Posts--Single--Box">.*?href="(.*?)".*?title="(.*?)".*?image="(.*?)"(.*?)</a>', data, re.S)
            for (url, titre, image, desc) in data_list:
                info = self.std_title(titre)
                image = self.std_url(image)
                title = info.get('title_display')
                sTitle = info.get('title')
                elms.append({'import': extra, 'category': 'host2', 'url': url, 'title': title, 'sTitle': sTitle, 'desc': '', 'icon': image, 'hst': 'tshost', 'good_for_fav': True, 'mode': '21'})
        return elms

    def SearchAll(self, str_ch, page=1, extra='', type_=''):
        elms = []
        r1 = self.get_items({'page': page, 'import': extra, 'str_ch': str_ch, 'type_': type_})
        for elm in r1:
            elms.append(elm)
        return elms

    def SearchMovies(self, str_ch, page=1, extra=''):
        elms = self.SearchAll(str_ch, page, extra=extra, type_='فيلم')
        return elms

    def SearchSeries(self, str_ch, page=1, extra=''):
        elms = self.SearchAll(str_ch, page, extra=extra, type_='مسلسل')
        return elms

    def SearchResult(self, str_ch, page, extra):
        elms = []
        url = self.MAIN_URL+'/search/'+str_ch+'/page/'+str(page)+'/'
        desc = []
        mode = '21'
        data = self.add_menu({'import': extra, 'url': url}, '', 'Posts--Single--Box">.*?href="(.*?)".*?title="(.*?)".*?image="(.*?)"', '', mode, ord=[0, 1, 2], u_titre=True, EPG=True, bypass=True)
        return data[2]

    def SearchResult1(self, str_ch, page, extra):
        elms = []
        data = ['', '', []]
        data_ = base64.b64encode('{"posts_per_page":20,"s":"'+str_ch+'","tax_query":{"relation":"AND"},"post_type":["post"]}')
        url = self.MAIN_URL+'/AjaxCenter/MorePosts/args/'+data_+'/type/posts/offset/'+str((page-1)*20)+'/curPage/https%3A%2F%2Farlionz.com%2FAjaxCenter%2FSearching%2F'+str_ch+'%2F/'
        sts, data0 = self.getPage(url)
        if sts:
            mode = [('', '20', 'URL'), ('/watch/', 'video', 'URL')]
            data = self.add_menu({'import': extra, 'url': url}, '', 'data-selector=".*?href="(.*?)".*?title="(.*?)".*?src="(.*?)"', data0.replace('\\', ''), mode, ord=[0, 1, 2], u_titre=True, EPG=True)
        return data[2]

    def get_links(self, cItem):
        urlTab = []
        URL = cItem['url']
        sts, data = self.getPage(URL)
        if sts:
            Liste_els = re.findall('"watch".*?data-id="(.*?)"', data, re.S)
            if Liste_els:
                params = dict(self.defaultParams)
                params['header']['X-Requested-With'] = 'XMLHttpRequest'
                sts_, data_ = self.getPage(self.MAIN_URL+'/PostServersWatch/'+Liste_els[0], params, {})
                if sts_:
                    Liste_els = re.findall('data-i="([^"]+)".+?data-id="([^"]+)".*?<em>(.*?)</', data_, re.S)
                    for (i, id_, titre_) in Liste_els:
                        URL = 'hst#tshost#'+i+'|||'+id_
                        urlTab.append({'name': titre_, 'url': URL, 'need_resolve': 1})
        return urlTab

    def getVideos(self, videoUrl):
        urlTab = []
        i, id_ = videoUrl.split('|||')
        URL = self.MAIN_URL + '/Embedder/'+id_+'/'+i
        params = dict(self.defaultParams)
        params['header']['X-Requested-With'] = 'XMLHttpRequest'
        sts, data = self.getPage(URL, params, {})
        if sts:
            Liste_els = re.findall('<iframe.*?src=["\'](.*?)["\']', data, re.IGNORECASE)
            if Liste_els:
                URL = Liste_els[0]
                urlTab.append((URL, '1'))
        return urlTab

    def getArticle(self, cItem):
        Desc = [('Time', 'runtime">(.*?)</li>', '', ''), ('Genre', 'Geners">(.*?)</ul>', '', ''), ('Quality', 'الجودات.*?<ul>(.*?)</ul>', '', ''), ('Story', 'Story">(.*?)</p>', '\n', '')]
        desc = self.add_menu(cItem, '', '<singular--header>(.*?)</section', '', 'desc', Desc=Desc)
        if desc == '':
            desc = cItem.get('desc', '')
        return [{'title': cItem['title'], 'text': desc, 'images': [{'title': '', 'url': cItem.get('icon', '')}], 'other_info': {}}]
