# -*- coding: utf8 -*-
import re

from Plugins.Extensions.IPTVPlayer.components.e2ivkselector import \
    GetVirtualKeyboard
from Plugins.Extensions.IPTVPlayer.libs.tstools import (T, TSCBaseHostClass,
                                                        gethostname, tshost)
from Plugins.Extensions.IPTVPlayer.p2p3.UrlLib import urllib_quote
from Plugins.Extensions.IPTVPlayer.tools.iptvtools import printDBG
from Plugins.Extensions.IPTVPlayer.tools.iptvtypes import strwithmeta


def getinfo():
    info_ = {}
    name = 'CimaNow'
    hst = 'https://cimanow.cc'
    info_['old_host'] = hst
    hst_ = tshost(name)
    if hst_ != '':
        hst = hst_
    info_['host'] = hst
    info_['name'] = name
    info_['version'] = '2.1 18/07/2022'
    info_['dev'] = 'RGYSoft'
    info_['cat_id'] = '21'
    info_['desc'] = 'افلام و مسلسلات'
    info_['icon'] = 'https://i.ibb.co/VL1PLZ9/cimanow.png'
    info_['recherche_all'] = '0'
    return info_


class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self, {'cookie': 'cimanow.cookie'})
        self.MAIN_URL = getinfo()['host']

    def showmenu(self, cItem):
        TAB = [('الاحدث', '', '15', 0), ('رمضان', '', '13', 0), ('أفــلام', '', '10', 0), ('مسلسلات', '', '11', 0), ('برامج', '', '14', 0)]
        self.add_menu(cItem, '', '', '', '', '', TAB=TAB, search=False)
        self.addDir({'import': cItem['import'], 'category': 'host2', 'title': T('Search'), 'icon': cItem['icon'], 'mode': '50'})

    def showmenu1(self, cItem):
        self.CimaNow_TAB = [
            {'category': 'host2', 'title': 'أفــلام أجنـبيـة', 'url': self.MAIN_URL+'/category/افلام-اجنبية/', 'mode': '20'},
            {'category': 'host2', 'title': 'أفــلام عربــيـة', 'url': self.MAIN_URL+'/category/افلام-عربية/',  'mode': '20'},
            {'category': 'host2', 'title': 'أفــلام تـركـيـة', 'url': self.MAIN_URL+'/category/افلام-تركية/',  'mode': '20'},
            {'category': 'host2', 'title': 'أفــلام هنــديـة', 'url': self.MAIN_URL+'/category/افلام-هندية/',  'mode': '20'},
            {'category': 'host2', 'title': 'أفــلام أنـيميشـن', 'url': self.MAIN_URL+'/category/افلام-انيميشن/', 'mode': '20'},
        ]
        self.listsTab(self.CimaNow_TAB, {'import': cItem.get('import', ''), 'icon': cItem.get('icon', '')})

    def showmenu2(self, cItem):
        self.CimaNow_TAB = [
            {'category': 'host2', 'title': 'مسـلسـلاتـ أجنـبيـة', 'url': self.MAIN_URL+'/category/مسلسلات-اجنبية/', 'mode': '20'},
            {'category': 'host2', 'title': 'مسـلسـلاتـ عربــيـة', 'url': self.MAIN_URL+'/category/مسلسلات-عربية/',  'mode': '20'},
            {'category': 'host2', 'title': 'مسـلسـلاتـ تـركـيـة', 'url': self.MAIN_URL+'/category/مسلسلات-تركية/',  'mode': '20'},
            {'category': 'host2', 'title': 'مسـلسـلاتـ أنـيميشـن', 'url': self.MAIN_URL+'/category/مسلسلات-انيميشن/', 'mode': '20'},
        ]
        self.listsTab(self.CimaNow_TAB, {'import': cItem.get('import', ''), 'icon': cItem.get('icon', '')})

    def showmenu3(self, cItem):
        self.CimaNow_TAB = [
            {'category': 'host2', 'title': '2023 رمـضـــان', 'url': self.MAIN_URL+'/category/رمضان-2023/',  'mode': '20'},
            {'category': 'host2', 'title': '2022 رمـضـــان', 'url': self.MAIN_URL+'/category/رمضان-2022/',  'mode': '20'},
            {'category': 'host2', 'title': '2021 رمـضـــان', 'url': self.MAIN_URL+'/category/رمضان-2021/',  'mode': '20'},
            {'category': 'host2', 'title': '2020 رمـضـــان', 'url': self.MAIN_URL+'/category/رمضان-2020/',  'mode': '20'},
            {'category': 'host2', 'title': '2019 رمـضـــان', 'url': self.MAIN_URL+'/category/رمضان-2019/',  'mode': '20'},
        ]
        self.listsTab(self.CimaNow_TAB, {'import': cItem.get('import', ''), 'icon': cItem.get('icon', '')})

    def showmenu4(self, cItem):
        self.CimaNow_TAB = [
            {'category': 'host2', 'title': 'بـــرامــــج', 'url': self.MAIN_URL+'/category/برامج-التلفزيونية/',  'mode': '20'},
            {'category': 'host2', 'title': 'مسـرحــيــات', 'url': self.MAIN_URL+'/category/مسرحيات/',  'mode': '20'},
            {'category': 'host2', 'title': 'حــفــــــلات', 'url': self.MAIN_URL+'/category/حفلات/',  'mode': '20'},
        ]
        self.listsTab(self.CimaNow_TAB, {'import': cItem.get('import', ''), 'icon': cItem.get('icon', '')})

    def showmenu5(self, cItem):
        self.addDir({'import': cItem['import'], 'category': 'host2', 'url': self.MAIN_URL+'/الاحدث/', 'title': 'الأحــ', 'desc': '', 'icon': cItem['icon'], 'mode': '20'})

    def showmenu0(self, cItem):
        del_ = ['قريبا', 'أختر وجهتك المفضلة', 'الاكثر مشاهدة', 'الاكثر اعجا', 'احدث الحفلات']
        self.add_menu(cItem, '', '<section>.*?<span>(.*?)<.*?href="(.*?)"', '', '20', ord=[1, 0], del_=del_)

    def showsearch(self, cItem):
        self.addDir({'import': cItem['import'], 'category': 'host2', 'title': 'البحث عن فيلم', 'icon': cItem['icon'], 'mode': '51', 'section': 'فيلم'})
        self.addDir({'import': cItem['import'], 'category': 'host2', 'title': 'البحث عن مسلسل', 'icon': cItem['icon'], 'mode': '51', 'section': 'مسلسل'})
        self.addDir({'import': cItem['import'], 'category': 'host2', 'title': 'البحث في الموقع', 'icon': cItem['icon'], 'mode': '51', 'section': ''})

    def getTag(self, url):
        if 'الافلام-' in url:
            tag = 'MOVIE'
        elif 'مسلسلات-انيميشن' in url:
            tag = 'ANIM'
        elif 'مسلسلات' in url:
            tag = 'TVSHOW'
        else:
            tag = 'MOVIE'
        return tag

    def showitms(self, cItem):
        URL = cItem['url']
        if not URL.startswith('http'):
            URL = self.MAIN_URL + URL
        titre = cItem['title']
        page = cItem.get('page', 1)
        print('titre='+titre)
        pat = '<a .*?href="(.*?)"(.*?)title">(.*?)(<em>.*?)</li>.*?-src="(.*?)"'
        tag = self.getTag(URL)
        if page == 1:
            URL0 = URL
        else:
            URL0 = URL + '/page/'+str(page)+'/'
        if 'افلام قصيرة' in titre:
            URL = self.MAIN_URL+'/category/%D8%A7%D9%84%D8%A7%D9%81%D9%84%D8%A7%D9%85/'
            sts, data = self.getPage(URL)
            if sts:
                data_list0 = re.findall('<section>.*?<div class="owl-body">(.*?)</div>', data, re.S)
                if data_list0:
                    data = data_list0[-2]
        elif 'افلام وثائقية' in titre:
            URL = self.MAIN_URL+'/category/%D8%A7%D9%84%D8%A7%D9%81%D9%84%D8%A7%D9%85/'
            sts, data = self.getPage(URL)
            if sts:
                data_list0 = re.findall('<section>.*?<div class="owl-body">(.*?)</div>', data, re.S)
                if data_list0:
                    data = data_list0[-1]
        else:
            sts, data = self.getPage(URL0)
            pat = '<article aria-label="post".*?href="(.*?)"(.*?)title">(.*?)(<em>.*?)</li>.*?-src="(.*?)"'
        if sts:
            data = self.getData(data)
            data_list = re.findall(pat, data, re.S)
            for (url, desc1, titre, desc2, image) in data_list:
                year = ''
                desc = ''
                data_desc = desc1 + desc2
                titre = titre.replace('&#8217;', "'").replace('&#8216;', "'").replace('&#8230;', "...")
                inf_list = re.findall('Ribbon">(.*?)</li>', data_desc, re.S)
                if inf_list:
                    desc = desc + 'Info: '+inf_list[0]+'\n'
                inf_list = re.findall('year">(.*?)</li>', data_desc, re.S)
                if inf_list:
                    desc = desc + 'Year: '+inf_list[0]+'\n'
                    year = inf_list[0].strip()
                inf_list = re.findall('<em>(.*?)</em>', data_desc, re.S)
                if inf_list:
                    desc = desc + 'Genre: '+inf_list[0]+'\n'
                inf_list = re.findall('aria-label="ribbon">(.*?)<', data_desc, re.S)
                TAG = ''
                for elm in inf_list:
                    if TAG == '':
                        TAG = elm
                    else:
                        TAG = TAG + '|'+elm
                if TAG != '':
                    desc = desc + 'TAG: '+TAG+'\n'
                if '1080' in TAG:
                    qual = '1080p'
                elif '720' in TAG:
                    qual = '720p'
                else:
                    qual = ''
                image = self.std_url(image)
                if ('/selary/' in url):
                    self.addDir({'import': cItem['import'], 'category': 'host2', 'url': url, 'title': titre.strip(), 'year': year, 'qual': qual,
                                'desc': desc, 'icon': image, 'hst': 'tshost', 'good_for_fav': True, 'mode': '21', 'tag': tag, 'selary': '1'})
                else:
                    self.addDir({'import': cItem['import'], 'category': 'host2', 'url': url, 'title': titre.strip(), 'year': year, 'qual': qual,
                                'desc': desc, 'icon': image, 'hst': 'tshost', 'good_for_fav': True, 'mode': '21', 'tag': tag, 'selary': '0'})
            self.addDir({'import': cItem['import'], 'category': 'host2', 'url': URL, 'page': page+1, 'title': T('Next'),
                        'desc': cItem.get('desc', ''), 'icon': cItem['icon'], 'mode': '20', 'hst': 'tshost', 'good_for_fav': True})

    def showelms(self, cItem):
        saison = cItem.get('saison')
        URL = cItem['url']
        page = cItem.get('page', 1)
        title = cItem.get('name', cItem['title']).strip()
        tag = cItem['tag']
        img = cItem['icon']
        sts, data = self.getPage(URL)
        if sts:
            data = self.getData(data)
            if cItem.get('selary', '0') == '0':
                Liste_els = re.findall('iframe.src="(https://www.youtube.*?)"', data, re.S)
                if Liste_els:
                    self.addVideo({'category': 'host2', 'good_for_fav': True, 'title': cItem['title']+' - Trailer', 'url': Liste_els[0],
                                  'desc': cItem.get('desc', ''), 'import': cItem['import'], 'icon': cItem['icon'], 'hst': 'none'})
                self.addVideo({'category': 'host2', 'good_for_fav': True, 'title': cItem['title'], 'url': cItem['url'],
                              'desc': cItem.get('desc', ''), 'import': cItem['import'], 'icon': cItem['icon'], 'hst': 'tshost'})
            else:
                if not saison:
                    tag = 'TVSHOW'
                    printDBG('title='+title)
                    Liste_els = re.findall('label="seasons">(.*?)</section>', data, re.S)
                    if Liste_els:
                        Liste_els = re.findall('<li.*?href="(.*?)".*?>(.*?)<', Liste_els[0], re.S)
                        for (url, saison) in Liste_els:
                            saison = saison.replace('الموسم', '').strip()
                            printDBG('S'+saison+' '+title)
                            self.addDir({'import': cItem['import'], 'category': 'host2', 'url': url, 'title': title+' S'+saison, 'desc': cItem['desc'],
                                        'icon': img, 'mode': '21', 'hst': 'tshost', 'good_for_fav': True, 'tag': tag, 'saison': saison, 'selary': '1'})
                else:
                    tag = 'EPISODE'
                    Liste_els = re.findall('<ul class.{,30}?id="eps">(.*?)</ul>', data, re.S)
                    if Liste_els:
                        Liste_els = re.findall('<li.*?href="(.*?)".*?(?:alt="logo"|</h3>).*?src="(.*?)".*?alt="(.*?)".*?<em>(.*?)</em>', Liste_els[0], re.S)
                        for (url, image, titre, ep) in Liste_els:
                            image = self.std_url(image)
                            self.addVideo({'import': cItem['import'], 'category': 'host2', 'url': url, 'title': title + 'E'+ep,
                                          'desc': cItem['desc'], 'icon': image, 'hst': 'tshost', 'good_for_fav': True, 'tag': tag})

    def get_links(self, cItem):
        urlTab = []
        url = cItem['url']+'watching/'
        referer = url
        sts, data = self.getPage(url)
        if sts:
            data = self.getData(data)
            Liste_els = re.findall('<li .*?data-index="(.*?)".*?data-id="(.*?)".*?>(.*?)</li>', data, re.S)
            for (url0, id_, titre) in Liste_els:
                local_ = ''
                if 'cn server' in titre.lower():
                    titre = 'fembed'
                elif 'vidbob' in titre.lower():
                    titre = 'jawcloud'
                elif 'Cima Now' in titre:
                    local_ = 'local'
                titre = self.cleanHtmlStr(titre).strip()
                urltab_ = self.getVideos_direct(url0+'|'+id_)
                urlTab = urlTab + urltab_
            Liste_els = re.findall('id="download">(.*?)</ul>', data, re.S)
            for elm in Liste_els:
                Tag = '|Down|'
                L_els = re.findall('href="(.*?)".*?</i>(.*?)</a>', elm, re.S)
                for (url0, titre) in L_els:
                    local_ = 'non'
                    resolve = 1
                    if url0.endswith('.mp4'):
                        local_ = 'local'
                        url0 = strwithmeta(url0, {'Referer': url})
                        resolve = 0
                    urlTab.append({'name': Tag+self.cleanHtmlStr(titre), 'url': url0, 'need_resolve': resolve, 'type': local_})
        return urlTab

    def getVideos_direct(self, videoUrl):
        urlTab = []
        tabs = self.getVideos(videoUrl)
        for (url, type_) in tabs:
            if type_ == '1':
                resolve = 1
                label = gethostname(url)
            elif type_ == '4':
                label, url = url.split('|', 1)
                resolve = 0
            urlTab.append({'name': '|Watch|'+label, 'url': url, 'need_resolve': resolve})
        return urlTab

    def getVideos(self, videoUrl):
        urlTab = []
        code, id_ = videoUrl.split('|', 1)
        if id_ == 'DOWN':
            sts, data = self.getPage(code, self.defaultParams)
            Liste_els = re.findall('id="downloadbtn".*?href="(.*?)"', data, re.S | re.IGNORECASE)
            if Liste_els:
                url_ = Liste_els[0]
                if url_.endswith('mp4'):
                    host = url_.split('.net/', 1)[0]+'.net'
                    URL_ = strwithmeta('MP4|'+url_, {'Referer': host})
                    urlTab.append((URL_, '4'))
                else:
                    urlTab.append((url_, '1'))
        else:
            url = self.MAIN_URL+'/wp-content/themes/Cima%20Now%20New/core.php?action=switch&index='+code+'&id='+id_
            addParams = dict(self.defaultParams)
            header = dict(addParams['header'])
            header['Referer'] = self.MAIN_URL
            addParams.update({'header': header})
            sts, data = self.getPage(url, addParams)
            if sts:
                Liste_els_3 = re.findall('src="(.+?)"', data, re.S | re.IGNORECASE)
                if Liste_els_3:
                    URL = Liste_els_3[0]
                    if URL.startswith('//'):
                        URL = 'http:'+URL
                    if 'cimanow.net' not in URL:
                        urlTab.append((URL, '1'))
                    else:
                        host = 'https://' + URL.split('/')[2]
                        sts, data = self.getPage(URL, addParams)
                        if sts:
                            Liste_els = re.findall('source.*?src="(.*?)".*?size="(.*?)"', data, re.S | re.IGNORECASE)
                            for elm in Liste_els:
                                url_ = elm[0]
                                if not (url_.startswith('http')):
                                    url_ = host + urllib_quote(url_)
                                URL_ = strwithmeta(elm[1]+'|'+url_, {'Referer': host})
                                urlTab.append((URL_, '4'))
        return urlTab

    def searchResult(self, cItem):
        str_ch = cItem.get('str_ch', '')
        if str_ch == '':
            ret = self.sessionEx.waitForFinishOpen(GetVirtualKeyboard(), title=('Search Text:'), text='')
            str_ch = ret[0]
        if not str_ch:
            return []
        page = cItem.get('page', 1)
        section = cItem.get('section', '')
        extra = cItem.get('import', '')
        elms = self.SearchAll(str_ch, page, extra, section)
        for elm in elms:
            self.addDir(elm)
        return elms

    def SearchAll(self, str_ch, page=1, extra='', type_='', icon=''):
        elms = []
        if type_ != '':
            URL = self.MAIN_URL+'/page/'+str(page)+'/?s='+str_ch+'+'+type_
        else:
            URL = self.MAIN_URL+'/page/'+str(page)+'/?s='+str_ch
        sts, data = self.getPage(URL)
        if sts:
            data = self.getData(data)
            data_list0 = re.findall('<article .*?href="(.*?)"(.*?)title">(.*?)(<em>.*?)</li>.*?data-src="(.*?)"', data, re.S)
            if data_list0:
                for (url, desc1, titre, desc2, image) in data_list0:
                    year = ''
                    desc = ''
                    data_desc = desc1 + desc2
                    titre = titre.replace('&#8217;', "'").replace('&#8216;', "'")
                    inf_list = re.findall('Ribbon">(.*?)</li>', data_desc, re.S)
                    if inf_list:
                        desc = desc + 'Info: '+inf_list[0]+'\n'
                    inf_list = re.findall('year">(.*?)</li>', data_desc, re.S)
                    if inf_list:
                        desc = desc + 'Year: '+inf_list[0]+'\n'
                        year = inf_list[0].strip()
                    episode = ''
                    inf_list = re.findall('label="episode">(.*?)</li>', data_desc, re.S)
                    if inf_list:
                        episode = self.cleanHtmlStr(inf_list[0]).replace('الحلقة', 'E')
                    inf_list = re.findall('الموسم(.*?)</li>', data_desc, re.S)
                    if inf_list:
                        saison = 'S'+self.cleanHtmlStr(inf_list[-1])
                        episode = saison + episode
                    if episode != '':
                        desc = desc + 'Episode: '+episode+'\n'
                    inf_list = re.findall('<em>(.*?)</em>', data_desc, re.S)
                    if inf_list:
                        desc = desc + 'Genre: '+inf_list[-1]+'\n'
                    inf_list = re.findall('aria-label="ribbon">(.*?)<', data_desc, re.S)
                    TAG = ''
                    for elm in inf_list:
                        if TAG == '':
                            TAG = elm
                        else:
                            TAG = TAG + '|'+elm
                    if TAG != '':
                        desc = desc + 'TAG: '+TAG+'\n'
                    if '1080' in TAG:
                        qual = '1080p'
                    elif '720' in TAG:
                        qual = '720p'
                    else:
                        qual = ''
                    image = self.std_url(image)
                    titre = titre.strip()
                    if ('/فيلم-' in url) or ('/%d9%81%d9%8a%d9%84%d9%85-' in url):
                        tag = 'MOVIE'
                        elms.append({'import': extra, 'category': 'host2', 'url': url, 'title': titre, 'year': year, 'qual': qual, 'desc': desc,
                                    'icon': image, 'mode': '21', 'hst': 'tshost', 'good_for_fav': True, 'tag': tag, 'selary': '0'})
                    else:
                        tag = 'TVSHOW'
                        name = titre
                        titre = titre + ' ' + episode
                        elms.append({'import': extra, 'category': 'host2', 'url': url, 'title': titre.strip(), 'year': year, 'qual': qual, 'desc': desc,
                                    'icon': image, 'hst': 'tshost', 'good_for_fav': True, 'mode': '21', 'tag': tag, 'selary': '1', 'name': name})
                if re.findall('<li class="active">.*?</li>.{0,5}<li><a href="(.*?)"', data, re.S):
                    elms.append({'import': extra, 'category': 'host2', 'title': T('Next'), 'mode': '51', 'section': type_, 'page': page+1, 'str_ch': str_ch})
        return (elms)

    def SearchMovies(self, str_ch, page=1, extra=''):
        elms = self.SearchAll(str_ch, page, extra=extra, type_='فيلم')
        return elms

    def SearchSeries(self, str_ch, page=1, extra=''):
        elms = self.SearchAll(str_ch, page, extra=extra, type_='مسلسل')
        return elms

    def SearchResult(self, str_ch, page, extra):
        URL = self.MAIN_URL+'/page/'+str(page)+'/?s='+str_ch
        sts, data = self.getPage(URL)
        if sts:
            self.getData(data)
            data_list0 = re.findall('<article .*?href="(.*?)"(.*?)title">(.*?)(<em>.*?)</li>.*?data-src="(.*?)"', data, re.S)
            if data_list0:
                for (url, desc1, titre, desc2, image) in data_list0:
                    year = ''
                    desc = ''
                    data_desc = desc1 + desc2
                    titre = titre.replace('&#8217;', "'").replace('&#8216;', "'")
                    inf_list = re.findall('Ribbon">(.*?)</li>', data_desc, re.S)
                    if inf_list:
                        desc = desc + 'Info: '+inf_list[0]+'\n'
                    inf_list = re.findall('year">(.*?)</li>', data_desc, re.S)
                    if inf_list:
                        desc = desc + 'Year: '+inf_list[0]+'\n'
                        year = inf_list[0].strip()
                    inf_list = re.findall('<em>(.*?)</em>', data_desc, re.S)
                    if inf_list:
                        desc = desc + 'Genre: '+inf_list[0]+'\n'
                    inf_list = re.findall('aria-label="ribbon">(.*?)<', data_desc, re.S)
                    TAG = ''
                    for elm in inf_list:
                        if TAG == '':
                            TAG = elm
                        else:
                            TAG = TAG + '|'+elm
                    if TAG != '':
                        desc = desc + 'TAG: '+TAG+'\n'
                    if '1080' in TAG:
                        qual = '1080p'
                    elif '720' in TAG:
                        qual = '720p'
                    else:
                        qual = ''
                    printDBG("titttttr"+url)
                    if ('/فيلم-' in url) or ('/%d9%81%d9%8a%d9%84%d9%85-' in url):
                        tag = 'MOVIE'
                        self.addVideo({'import': extra, 'category': 'host2', 'url': url, 'title': titre, 'year': year,
                                      'qual': qual, 'desc': desc, 'icon': image, 'hst': 'tshost', 'good_for_fav': True, 'tag': tag})
                    else:
                        tag = 'TVSHOW'
                        self.addDir({'import': extra, 'category': 'host2', 'url': url, 'title': titre, 'year': year, 'qual': qual,
                                    'desc': desc, 'icon': image, 'hst': 'tshost', 'good_for_fav': True, 'mode': '21', 'tag': tag})

    def getArticle(self, cItem):
        Desc = [('Quality', 'fa-play"></i>الجودة.*?<a>(.*?)</a>', '', ''), ('Time', 'fa-clock">.*?<a>(.*?)</a>', '', ''),
                ('Story', 'fa-info-circle">(.*?)</li>', '\n', '')]
        desc = self.add_menu(cItem, '', '', '', 'desc', Desc=Desc)
        if desc == '':
            desc = cItem.get('desc', '')
        return [{'title': cItem['title'], 'text': desc, 'images': [{'title': '', 'url': cItem.get('icon', '')}], 'other_info': {}}]
