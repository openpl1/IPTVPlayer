# -*- coding: utf-8 -*-

import re

import requests
from Plugins.Extensions.IPTVPlayer.components.iptvplayerinit import \
    TranslateTXT as _
from Plugins.Extensions.IPTVPlayer.libs import ph
from Plugins.Extensions.IPTVPlayer.libs.tstools import (TSCBaseHostClass,
                                                        tscolor, tshost)


def getinfo():
    info_={}
    name = 'TopCinema'
    hst = 'https://web3.topcinema.top'
    info_['old_host'] = hst
    hst_ = tshost(name)
    if hst_!='': hst = hst_
    info_['host']= hst
    info_['name']=name
    info_['version']='1.2 03/11/2023'
    info_['dev']='MOHAMED_OS'
    info_['cat_id']='21'
    info_['desc']='أفلام, مسلسلات أسيوية و اجنبية'
    info_['icon']='https://i.ibb.co/MG0J6YQ/topcinema.png'
    info_['recherche_all']='1'
    return info_


class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self,{})
        self.MAIN_URL = getinfo()['host']
        self.USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36 Edg/115.0.1901.203'
        self.HEADER = {'User-Agent': self.USER_AGENT, 'Sec-Fetch-Mode':'cors','X-Requested-With':'XMLHttpRequest','Sec-Fetch-Dest':'empty','Sec-Fetch-Site':'same-origin','Referer':self.getMainUrl(), 'Origin':self.getMainUrl()}
        # self.cacheLinks = {}

    def showmenu(self,cItem):
        TAB = [(tscolor('\c00????00')+'المـضـاف حـديـثا','/recent/','20','recent'),('أفــلام','','10','film'),('مسـلسـلات','','10','series'),('الأعــلى تـقـيـما','','10','top')]
        self.add_menu(cItem,'','','','','',TAB=TAB,search=False)
        self.addDir({'import':cItem['import'],'category' : 'search','title': _('Search'), 'search_item':True,'page':1,'hst':'tshost','icon':cItem['icon']})

    def showmenu1(self,cItem):
        gnr = cItem['sub_mode']
        if gnr == 'film':
            self.TopCinema_TAB = [
                    {'category':'host2','title': 'أفــلام أجنـبيـة','url':self.MAIN_URL+'/category/افلام-اجنبي/', 'mode':'20'},
                    {'category':'host2','title': 'أفــلام أنمــي','url':self.MAIN_URL+'/category/افلام-انمي/',  'mode':'20'},
                    {'category':'host2','title': 'أفــلام آسـيـويـة','url':self.MAIN_URL+'/category/افلام-اسيوي/',  'mode':'20'},
                    {'category':'host2','title': 'أفــلام نتـفليـكس','url':self.MAIN_URL+'/netflix-movies/',  'mode':'20'},
                    {'category':'host2','title': 'سـلاسـل الافــلام','url':self.MAIN_URL+'/movies-collections/', 'mode':'20'}]
        elif gnr == 'series':
            self.TopCinema_TAB = [
                    {'category':'host2','title': 'مسـلسـلات أجنـبيـة','url':self.MAIN_URL+'/category/مسلسلات-اجنبي/', 'mode':'20'},
                    {'category':'host2','title': 'مسـلسـلات أنمــي','url':self.MAIN_URL+'/category/مسلسلات-انمي/',  'mode':'20'},
                    {'category':'host2','title': 'مسـلسـلات آسـيـويـة','url':self.MAIN_URL+'/category/مسلسلات-اسيوية/',  'mode':'20'}]
        elif gnr == 'top':
            self.TopCinema_TAB = [
                    {'category':'host2','title': 'أفــلام','url':self.MAIN_URL+'/top-rating-imdb/', 'mode':'20'},
                    {'category':'host2','title': 'مسـلسـلات','url':self.MAIN_URL+'/top-rating-imdb-series/', 'mode':'20'},]
        self.listsTab(self.TopCinema_TAB, {'import':cItem.get('import',''),'icon':cItem.get('icon','')})

    def showitms(self,cItem):
        if "movies-collections" in cItem.get('url'):
            URL = cItem.get('url')
        else:
            page = cItem.get('page',1)
            URL = cItem.get('url','')+'page/'+str(page)
        sts, data = self.getPage(URL)
        if sts:
            data = re.findall('class=["\']Posts--List SixInRow["\']>(.*?)<div style', data, re.S)
            if data:
                Liste_els = re.findall('<a href=["\'](.*?)["\'].*?data-src=["\'](.*?)["\'].*?alt=["\'](.*?)["\']>', data[0], re.S)
                for (url,image,titre) in Liste_els:
                    info  = self.std_title(ph.clean_html(titre),with_ep=True)
                    self.addDir({'import':cItem['import'],'category' : 'host2','title':info.get('title_display'),'icon':image,'desc':info.get('desc'),'mode':'21','url':url,'good_for_fav':True,'EPG':True,'hst':'tshost'})
        if 'page' in URL:
            self.addDir({'import':cItem['import'],'category' : 'host2','title':tscolor('\c00????00')+'Next Page >>'+tscolor('\c00??????'),'icon':cItem['icon'],'desc':'','mode':'20','url':cItem['url'],'page':page+1})


    def showelms(self,cItem):
        URL = cItem.get('url')

        if "series" in cItem.get('url'):
            url_ = URL+"list/"
        else:
            url_ = URL
        sts, data = self.getPage(url_)
        if sts:
            if 'list' in url_:
                Liste_els = re.findall('class=["\']Small--Box Season["\']>.*?<a href=["\'](.*?)["\'].*?class=["\']epnum["\']>(.*?)</div>', data, re.S)
                if Liste_els:
                    for (url,titre) in Liste_els:
                        info  = self.std_title(ph.clean_html(titre),with_ep=True)
                        self.addDir({'import':cItem['import'],'category' : 'host2','url':url,'title':info.get('title_display'),'icon':cItem['icon'],'desc':info.get('desc'),'mode':'19','good_for_fav':True,'EPG':True,'hst':'tshost'})
            else:
                self.addVideo({'import':cItem['import'], 'hst':'tshost', 'url':cItem['url'], 'title':cItem['title'], 'desc':'','icon':cItem['icon'],'good_for_fav':True,'EPG':True,'hst':'tshost'})

    def showfilter(self,cItem):
        URL = cItem.get('url')+"list/"
        sts, data = self.getPage(URL)
        if sts:
            Liste_els = re.findall('<a href=["\'](.*?)["\'].*?title=["\'](.*?)["\']', data, re.S)
            for (url,titre) in Liste_els:
                self.addVideo({'import':cItem['import'], 'hst':'tshost', 'url':url, 'title':self.std_extract(titre), 'desc':'','icon':cItem['icon'],'good_for_fav':True,'EPG':True,'hst':'tshost'})

    def get_links(self,cItem):
        urlTab = []
        URL = cItem.get("url")+"watch/"
        SiteUrl = self.MAIN_URL+'/wp-content/themes/movies2023/Ajaxat/Single/Server.php'
        sts, data = self.getPage(URL)
        sData = re.findall(r'data-id="(.+?)" data-server="([^"]+)".+?<span>(.+?)</span>', data, re.S)
        if sts:
            for (Serv,Sid,sHost) in sData:
                data = {'id':Serv,'i':Sid}
                s = requests.Session()
                GetUrl = s.post(SiteUrl,data=data,headers=self.HEADER)
                Liste_els = re.findall('<iframe src="([^"]+)', GetUrl.text, re.S)
                for Url_ in Liste_els:
                    urlTab.append({'name':'|Watch Server| '+ sHost, 'url':Url_, 'need_resolve':1})

        #     sts_, data_ = self.getPage(URL.replace("watch","download"))
        #     if sts_:
        #         url_dat_ = re.findall(r'rel="nofollow" href="([^"]+)".*?class="text">.*?span>(.*?)</', data_, re.S)
        #         for (url,titre) in url_dat_:
        #             urlTab.append({'name':'|Downl Server| '+ titre, 'url':url, 'need_resolve':1})
        # self.cacheLinks[str(cItem['url'])] = urlTab
        return urlTab

    def SearchResult(self,str_ch,page,extra):
        URL=self.MAIN_URL+'/page/'+str(page)+'/?s='+str_ch+'&type=all'
        sts, data = self.getPage(URL)
        if sts:
            data = re.findall('class=["\']Posts--List SixInRow["\']>(.*?)class=["\']paginate["\']>', data, re.S)
            if data:
                Liste_els = re.findall('<a href=["\'](.*?)["\']>.*?data-src=["\'](.*?)["\'].*?alt=["\'](.*?)["\']>', data[0], re.S)
                for (url,image,titre) in Liste_els:
                    info  = self.std_title(titre,with_ep=True)
                    self.addDir({'import':extra,'category' : 'host2','title':info.get('title_display'),'icon':image,'desc':info.get('desc'),'mode':'21','url':url,'good_for_fav':True,'hst':'tshost'})

    def getArticle(self,cItem):
        Desc = [('Rate',' class="imdbRating">.*?i>(.+?)</','\n',''),('Quality','Quality.*?">(.+?)</','\n',''),('Year','release-year.*?">(.+?)</','\n',''),
                ('Generes','genre.*?">(.+?)</','\n',''),('Story','class="story".*?p>(.+?)</','\n','')]
        desc = self.add_menu(cItem,'','class="infoAndWatch">(.+?)class="BTNSDownWatch">','','desc',Desc=Desc)
        if desc =='': desc = cItem.get('desc','')
        return [{'title':cItem['title'], 'text': desc, 'images':[{'title':'', 'url':cItem.get('icon','')}], 'other_info':{}}]