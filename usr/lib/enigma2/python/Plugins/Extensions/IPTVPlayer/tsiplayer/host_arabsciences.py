# -*- coding: utf-8 -*-

import re

from Plugins.Extensions.IPTVPlayer.components.iptvplayerinit import \
    TranslateTXT as _
from Plugins.Extensions.IPTVPlayer.libs import ph
from Plugins.Extensions.IPTVPlayer.libs.tstools import (TSCBaseHostClass,
                                                        gethostname, tscolor,
                                                        tshost, unifurl)


def getinfo():
    info_={}
    name = 'ArabSciences'
    hst = 'https://arabsciences.com'
    info_['old_host'] = hst
    hst_ = tshost(name)
    if hst_!='': hst = hst_
    info_['host']= hst
    info_['name']=name
    info_['version']='1.0 16/09/2023'
    info_['dev']='MOHAMED_OS'
    info_['cat_id']='27'
    info_['desc']='افلام وثائقية'
    info_['icon']='https://i.ibb.co/cDdx7JD/arabsciences.png'
    info_['recherche_all']='1'
    return info_


class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self,{})
        self.MAIN_URL = getinfo()['host']
        self.cacheLinks = {}

    def showmenu(self,cItem):
        TAB = [('الصـنفـ الاول','','10','part1'),('الصـنـفـ الثـانـي','','10','part2'),('الصـنفـ الـثالـث','','10','part3')]
        self.add_menu(cItem,'','','','','',TAB=TAB,search=False)
        self.addDir({'import':cItem['import'],'category' : 'search','title': _('Search'), 'search_item':True,'page':1,'hst':'tshost','icon':cItem['icon']})

    def showmenu1(self,cItem):
        gnr = cItem['sub_mode']
        if gnr == 'part1':
            self.ArabSciences_TAB = [
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/cultures/', 'title':'ثقافات', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/countries/', 'title':'البلدان', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/islam/', 'title':'الإسلام', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/nature/', 'title':'الطبيعة', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/politics/', 'title':'سياسة', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/engineering/', 'title':'هندسة', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/catastrophe/', 'title':'كوارث', 'desc':'', 'icon':cItem['icon'], 'mode':'20'}]
        elif gnr == 'part2':
            self.ArabSciences_TAB = [
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/tv-channels/natgeoad/', 'title':'ناشونال جيوغرافيك ابو ظبي', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/tv-channels/dw-arabic/', 'title':'DW (عربية)', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/tv-channels/jazeeradoc-tv-channels/', 'title':'الجزيرة الوثائقية', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/tv-channels/alarabyatv/', 'title':'قناة العربية', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/tv-channels/bbc-arabic/', 'title':'BBC Arabic', 'desc':'', 'icon':cItem['icon'], 'mode':'20'}]
        elif gnr == 'part3':
            self.ArabSciences_TAB = [
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/animals-categories/', 'title':'الحيوانات و الحياة البريّة', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/history/', 'title':'تاريخ', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/space/', 'title':'الفضاء', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/technology/', 'title':'علوم وتكنولوجيا', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/mystery/', 'title':'غموض و ألغاز', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/adventure/', 'title':'مغامرات', 'desc':'', 'icon':cItem['icon'], 'mode':'20'},
                    {'category' :'host2', 'url':self.MAIN_URL+'/category/weapons-fight/', 'title':'أسلحة و فنون قتال', 'desc':'', 'icon':cItem['icon'], 'mode':'20'}]
        self.listsTab(self.ArabSciences_TAB, {'import':cItem.get('import',''),'icon':cItem.get('icon','')})

    def showitms(self,cItem):
        page = cItem.get('page',1)
        URL = cItem.get('url','')+'page/'+str(page)
        sts, data = self.getPage(URL)
        if sts:
            Liste_els = re.findall('<a aria-label="([^"]+)".+?href="([^"]+)".+?data-breeze="([^"]+)".+?class="post-excerpt">([^<]+)</', data, re.S)
            for (titre,url,image,desc) in Liste_els:
                info  = self.std_title(ph.clean_html(titre),with_ep=True)
                Desc = tscolor('\c00????00') + "\nDesc: "+tscolor('\c00??????') + ph.clean_html(desc)
                self.addDir({'import':cItem['import'],'category' : 'host2','title':info.get('title_display'),'icon':image,'desc':info.get('desc')+Desc,'mode':'21','url':url,'good_for_fav':True,'EPG':True,'hst':'tshost'})
            self.addDir({'import':cItem['import'],'category' : 'host2','title':tscolor('\c00????00')+'Next Page >>'+tscolor('\c00??????'),'icon':cItem['icon'],'desc':'','mode':'20','url':cItem['url'],'page':page+1})


    def showelms(self,cItem):
            self.addVideo({'import':cItem['import'], 'hst':'tshost', 'url':cItem['url'], 'title':cItem['title'], 'desc':'','icon':cItem['icon'],'good_for_fav':True,'EPG':True,'hst':'tshost'})

    def get_links(self,cItem):
        urlTab = []
        sts, data = self.getPage(cItem.get("url"))
        if sts:
            sData = re.findall(r'<iframe.+?src="([^"]+)"', data, re.S)
            for Url_ in sData:
                urlTab.append({'name':'|Watch Server| '+ gethostname(unifurl(Url_),True), 'url':unifurl(Url_), 'need_resolve':1})
        return urlTab

    def SearchResult(self,str_ch,page,extra):
        URL=self.MAIN_URL+'/search/'+str_ch+'/page/'+str(page)
        sts, data = self.getPage(URL)
        if sts:
            Liste_els = re.findall('<a aria-label="([^"]+)".+?href="([^"]+)".+?src="([^"]+)".+?class="post-excerpt">([^<]+)</', data, re.S)
            for (titre,url,image,desc) in Liste_els:
                info  = self.std_title(ph.clean_html(titre),with_ep=True)
                Desc = tscolor('\c00????00') + "Desc: "+tscolor('\c00??????') + ph.clean_html(desc)
                self.addDir({'import':extra,'category' : 'host2','title':info.get('title_display'),'icon':image,'desc':Desc,'mode':'21','url':url,'good_for_fav':True,'EPG':True,'hst':'tshost'})

    def getArticle(self,cItem):
        Desc = [('Year','date meta-item tie-icon">(.+?)</','\n',''),('Story','sharethis-inline-share-buttons.+?p>(.+?)<p><span','\n','')]
        desc = self.add_menu(cItem,'','','','desc',Desc=Desc)
        if desc =='': desc = cItem.get('desc','')
        return [{'title':cItem['title'], 'text': desc, 'images':[{'title':'', 'url':cItem.get('icon','')}], 'other_info':{}}]