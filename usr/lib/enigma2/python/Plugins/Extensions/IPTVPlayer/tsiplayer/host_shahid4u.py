# -*- coding: utf-8 -*-

import re

from Plugins.Extensions.IPTVPlayer.components.iptvplayerinit import \
    TranslateTXT as _
from Plugins.Extensions.IPTVPlayer.libs import ph
from Plugins.Extensions.IPTVPlayer.libs.tstools import (TSCBaseHostClass,
                                                        gethostname, tscolor,
                                                        tshost)


def getinfo():
    info_={}
    name = 'Shahid4u'
    hst = 'https://shaaheed4u.cam'
    info_['old_host'] = hst
    hst_ = tshost(name)
    if hst_!='': hst = hst_
    info_['host']= hst
    info_['name']=name
    info_['version']='1.5 16/09/2023'
    info_['dev']='MOHAMED_OS'
    info_['cat_id']='21'
    info_['desc']='أفلام و مسلسلات عربية و اجنبية'
    info_['icon']='https://i.ibb.co/pb6W99R/shahidu.png'
    info_['recherche_all']='1'
    return info_


class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self,{})
        self.MAIN_URL = getinfo()['host']
        self.USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
        self.HEADER = {'User-Agent': self.USER_AGENT, 'Connection': 'keep-alive', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','X-Requested-With': 'XMLHttpRequest','Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3'}
        self.defaultParams = {'header':self.HEADER}
        self.cacheLinks = {}

    def showmenu(self,cItem):
        TAB = [(tscolor('\c00????00')+'الرئيـسيـة','','10','filter'),('أفـــــلام','','10','film'),('مــسـلـسـلات','','10','serie'),('عـروض مصـارعـة','/category/عروض-مصارعة/','20','wwe'),
            ('بـرامـج تلفـزيـونـيـة','/category/برامج-تلفزيونية/','20','tv')]
        self.add_menu(cItem,'','','','','',TAB=TAB,search=False)
        self.addDir({'import':cItem['import'],'category' : 'search','title': _('Search'), 'search_item':True,'page':1,'hst':'tshost','icon':cItem['icon']})

    def showmenu1(self,cItem):
        gnr = cItem['sub_mode']
        if gnr == 'film':
            self.Shahid4u_TAB = [
                {'category':'host2','title': 'أفــلام أجنـبيـة','url':self.MAIN_URL+'/category/افلام-اجنبي/', 'mode':'20'},
                {'category':'host2','title': 'أفــلام عــربـيــة','url':self.MAIN_URL+'/category/افلام-عربي/', 'mode':'20'},
                {'category':'host2','title': 'أفــلام هنــديـة','url':self.MAIN_URL+'/category/افلام-هندي/',  'mode':'20'},
                {'category':'host2','title': 'أفــلام آسـيـويـة','url':self.MAIN_URL+'/category/افلام-اسيوية/',  'mode':'20'},
                {'category':'host2','title': 'أفــلام تـركـيـة','url':self.MAIN_URL+'/category/افلام-تركية/',  'mode':'20'},
                {'category':'host2','title': 'أفــلام أنـمـي','url':self.MAIN_URL+'/category/افلام-انمي/', 'mode':'20'}]
        elif gnr == 'serie':
            self.Shahid4u_TAB = [
                {'category':'host2','title': 'مسـلـسـلات أجنـبيـة','url':self.MAIN_URL+'/category/مسلسلات-اجنبي/', 'mode':'20'},
                {'category':'host2','title': 'مسـلـسـلات عــربـيــة','url':self.MAIN_URL+'/category/مسلسلات-عربي/', 'mode':'20'},
                {'category':'host2','title': 'مسـلـسـلات هنــديـة','url':self.MAIN_URL+'/category/مسلسلات-هندية/',  'mode':'20'},
                {'category':'host2','title': 'مسـلـسـلات آسـيـويـة','url':self.MAIN_URL+'/category/مسلسلات-اسيوية/',  'mode':'20'},
                {'category':'host2','title': 'مسـلـسـلات تـركـيـة','url':self.MAIN_URL+'/category/مسلسلات-تركية/',  'mode':'20'},
                {'category':'host2','title': 'مسـلـسـلات أنـمـي','url':self.MAIN_URL+'/category/مسلسلات-انمي/', 'mode':'20'}]
        elif gnr == 'filter':
            self.Shahid4u_TAB = [
                {'category':'host2','title': 'الأحــدث','url':self.MAIN_URL+'/', 'mode':'20'},
                {'category':'host2','title': 'الأعــلى تـقـيـما','url':self.MAIN_URL+'/?order=rating', 'mode':'20'},
                {'category':'host2','title': 'الأكـثـر مـشـاهـدة','url':self.MAIN_URL+'/?order=views',  'mode':'20'},
                {'category':'host2','title': 'المــثـبت','url':self.MAIN_URL+'/?order=pin_index',  'mode':'20'},
                {'category':'host2','title': 'جـديـد الأفـلام','url':self.MAIN_URL+'/?order=last_films',  'mode':'20'},
                {'category':'host2','title': 'جـديد الحـلـقات','url':self.MAIN_URL+'/?order=last_eps', 'mode':'20'}]

        self.listsTab(self.Shahid4u_TAB, {'import':cItem.get('import',''),'icon':cItem.get('icon','')})

    def showitms(self,cItem):
        if "getposts" in cItem.get('url'):
            URL = cItem.get('url')
        else:
            page = cItem.get('page',1)
            URL = cItem.get('url').rstrip('/')+'?page='+str(page)
        sts, data = self.getPage(URL)
        check = re.findall(r'container my-3["\']>', data, re.S)
        if sts:
            if check:
                Sdata = re.findall(r'container my-3["\']>(.+?)class=["\']pagination["\']>', data, re.S)
                Liste_els = re.findall(r'href=["\']([^"\']+)["\'].+?url\((.+?)\).+?<h4 class=["\']title["\']>(.+?)</', Sdata[0], re.S)
            else :
                Liste_els = re.findall(r'href=["\']([^"\']+)["\'].+?url\((.+?)\).+?<h4 class=["\']title["\']>(.+?)</', data, re.S)
            for (url,image,titre) in Liste_els:
                info  = self.std_title(ph.clean_html(titre),with_ep=True)
                self.addDir({'import':cItem['import'],'category' : 'host2','title':info.get('title_display'),'icon':image,'desc':info.get('desc'),'mode':'21','url':url,'good_for_fav':True,'EPG':True,'hst':'tshost'})
            if "page" in URL:
                self.addDir({'import':cItem['import'],'category' : 'host2','title':tscolor('\c00????00')+'Next Page >>'+tscolor('\c00??????'),'icon':cItem['icon'],'desc':'','mode':'20','url':cItem['url'],'page':page+1})


    def showelms(self,cItem):
        URL = cItem.get('url')
        if 'episode' in URL:
            sts, data = self.getPage(URL)
            if sts:
                self.addVideo({'import':cItem['import'], 'hst':'tshost', 'url':cItem['url'], 'title':cItem['title'], 'desc':'','icon':cItem['icon'],'good_for_fav':True,'hst':'tshost'})
                Liste = re.findall(r'class=["\']fa-solid fa-list-ul.+?</i>(.+?)</', data, re.S)
                if Liste:
                    for titer_ in Liste:
                        if "الحلقات" in titer_.replace(' ', ''):
                            self.addMarker({'title':tscolor('\c0000??00')+titer_,'icon':cItem['icon'],'desc':''})
                            Sdata = re.findall(titer_+'(.+?)rounded my-4["\']>', data, re.S)
                            sUrl = re.findall(r'href=["\']([^"\']+)["\'].+?px-1["\']>(.+?)</h3>', Sdata[0], re.S)
                            for (url,titre) in sUrl:
                                self.addVideo({'import':cItem['import'], 'hst':'tshost', 'url':url, 'title':ph.clean_html(titre), 'desc':'','icon':cItem['icon'],'good_for_fav':True,'hst':'tshost'})
                        elif "المواسم" in titer_.replace(' ', ''):
                            self.addMarker({'title':tscolor('\c0000??00')+titer_,'icon':cItem['icon'],'desc':''})
                            Sdata = re.findall(titer_+'(.+?)my-4 text-white', data, re.S)
                            sUrl = re.findall(r'href=["\']([^"\']+)["\'].+?px-1["\']>(.+?)</h3>', Sdata[0], re.S)
                            for (url,titre) in sUrl:
                                info  = self.std_title(ph.clean_html(titre),with_ep=True)
                                self.addDir({'import':cItem['import'],'category' : 'host2','title':info.get('title_display'),'icon':cItem['icon'],'desc':'','mode':'21','url':url,'good_for_fav':True,'EPG':True,'hst':'tshost'})
        elif 'season' in URL:
            URL += '/episodes'
            sts, data = self.getPage(URL)
            if sts:
                sUrl = re.findall(r'href=["\']([^"\']+)["\'].+?url\((.+?)\).+?<h4 class=["\']title["\']>(.+?)</', data, re.S)
                for (url,image,titre) in sUrl:
                    info  = self.std_title(ph.clean_html(titre),with_ep=True)
                    self.addVideo({'import':cItem['import'], 'hst':'tshost', 'url':url, 'title':info.get('title_display'), 'desc':'','icon':image,'good_for_fav':True,'hst':'tshost'})
        elif "film" in URL or "post" in URL:
            self.addVideo({'import':cItem['import'], 'hst':'tshost', 'url':cItem['url'], 'title':cItem['title'], 'desc':'','icon':cItem['icon'],'good_for_fav':True,'hst':'tshost'})

    def get_links(self,cItem):
        urlTab = []
        URL = cItem.get("url").replace("film","watch").replace("episode","watch").replace("post","watch")
        sts, data = self.getPage(URL)
        if sts:
            sData = re.findall(r'["\']url["\']:["\']([^"\']+)["\'],', data, re.S)
            for Url_ in sData:
                url = Url_.replace("\\","")
                urlTab.append({'name':'|Watch Server| '+ gethostname(url,True), 'url':url, 'need_resolve':1})

            sts_, data_ = self.getPage(URL.replace("watch","download"))
            if sts_:
                url_dat_ = re.findall(r'href=["\']([^"\']+)["\'].+?class=["\']fa-solid fa-tv["\']>(.+?)</', data_, re.S)
                for (Url_,Qua) in url_dat_:
                    titer = '|Downl Server| '+ gethostname(Url_,True)+" "+ph.clean_html(Qua)+"P"
                    urlTab.append({'name':titer, 'url':Url_, 'need_resolve':1})
        self.cacheLinks[str(cItem['url'])] = urlTab
        return urlTab


    def SearchResult(self,str_ch,page,extra):
        URL=self.MAIN_URL+'/search?s='+str_ch+'&page='+str(page)
        sts, data = self.getPage(URL)
        if sts:
            Sdata = re.findall(r'container my-3["\']>(.+?)class=["\']pagination["\']>', data, re.S)
            Liste_els = re.findall(r'href=["\']([^"\']+)["\'].+?url\((.+?)\).+?<h4 class=["\']title["\']>(.+?)</', Sdata[0], re.S)
            for (url,image,titre) in Liste_els:
                info  = self.std_title(ph.clean_html(titre),with_ep=True)
                self.addDir({'import':extra,'category' : 'host2','title':info.get('title_display'),'icon':image,'desc':info.get('desc'),'mode':'21','url':url,'good_for_fav':True,'EPG':True,'hst':'tshost'})

    def getArticle(self,cItem):
        Desc = [('Quality','href=["\'].+?quality.+?["\']>(.+?)</','\n',''),('Year','href=["\'].+?release-year.+?>(.+?)</','\n',''),
                ('Generes','href=["\'].+?genre.+?>(.+?)</','\n',''),('Story','class=["\']description["\']>(.+?)</','\n','')]
        desc = self.add_menu(cItem,'','class=["\']info-side(.+?)<div style','','desc',Desc=Desc)
        if desc =='': desc = cItem.get('desc','')
        return [{'title':cItem['title'], 'text': desc, 'images':[{'title':'', 'url':cItem.get('icon','')}], 'other_info':{}}]

