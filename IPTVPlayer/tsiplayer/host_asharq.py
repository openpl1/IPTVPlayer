# -*- coding: utf-8 -*-

import re

from Plugins.Extensions.IPTVPlayer.libs import ph
from Plugins.Extensions.IPTVPlayer.libs.tstools import (TSCBaseHostClass,
                                                        gethostname, tshost)


def getinfo():
    info_={}
    name = 'Asharq'
    hst = 'https://now.asharq.com'
    info_['old_host'] = hst
    hst_ = tshost(name)
    if hst_!='': hst = hst_
    info_['host']= hst
    info_['name']=name
    info_['version']='1.0 17/10/2023'
    info_['dev']='MOHAMED_OS'
    info_['cat_id']='27'
    info_['desc']='افلام وثائقية'
    info_['icon']='https://i.ibb.co/xsbdc1f/asharq.png'
    info_['recherche_all']='0'
    return info_


class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self,{})
        self.MAIN_URL   =  getinfo()['host']

    def showmenu(self,cItem):
        TAB = [('افـلام وثائقية','/doc/','20','doc'),('أفـلام الاكــتشاف','/discovery/','20','dis'),
                ('بـودكــاسـت','/الشرق-بودكاست/','20','pod'),('QuickTake','/الشرق-quicktake/','20','qui'),('اقـتصـاد','/اقتصاد-الشرق/','20','blo')]
        self.add_menu(cItem,'','','','','','',TAB=TAB,search=False)

    def showitms(self,cItem):
        sts, data = self.getPage(cItem.get('url'))
        if sts:
            Liste_els = re.findall(r'card card-genre-show.+?href="(.+?)".+?src="(.+?)".+?alt="(.+?)".+?card-description">(.+?)</', data, re.S)
            for (url,image,titre,desc)in Liste_els:
                info  = self.std_title(ph.clean_html(titre),with_ep=True)
                sTitel = info.get('title_display')
                desc_ = info.get('desc') + desc
                self.addDir({'import':cItem['import'],'category' : 'host2','title':sTitel,'icon':image,'desc':desc_,'mode':'21','url':self.MAIN_URL + url,'good_for_fav':True,'EPG':True,'hst':'tshost'})


    def showelms(self,cItem):
        sts, data = self.getPage(cItem['url'])
        if sts:
            if '<div class="cards-list">' in data:
                Liste_els = re.findall(r'card card-genre-episode.+?href="(.+?)".+?src="(.+?)".+?alt="(.+?)".+?card-shortdescription">(.+?)</',data, re.S)
                for (url,image,titre,desc)in Liste_els:
                    info  = self.std_title(ph.clean_html(titre),with_ep=True)
                    sTitel = info.get('title_display')
                    self.addVideo({'import':cItem['import'], 'hst':'tshost', 'url':self.MAIN_URL+url, 'title':sTitel, 'desc':desc,'icon':image,'good_for_fav':True,'EPG':True,'hst':'tshost'})
            else:
                self.addVideo({'import':cItem['import'], 'hst':'tshost', 'url':cItem['url'], 'title':cItem['title'], 'desc':cItem['desc'],'icon':cItem['icon'],'good_for_fav':True,'EPG':True,'hst':'tshost'})

    def get_links(self,cItem):
        urlTab = []
        sts, data = self.getPage(cItem['url'])
        if sts:
            siteUrl = re.findall(r',"Link":.+?},"(.+?)","(.+?)",', data, re.S)
            for (titre, url) in siteUrl:
                if "https" in titre:
                    titre = gethostname(titre,True)
                urlTab.append({'name':titre, 'url':url, 'need_resolve':0})
        return urlTab

    def getArticle(self,cItem):
        Desc = [('Desc','card-description">(.+?)</','\n',''),('Time','class="duration">(.*?)</','\n','')]
        desc = self.add_menu(cItem,'','','','desc',Desc=Desc)
        if desc =='': desc = cItem.get('desc','')
        return [{'title':cItem['title'], 'text': desc, 'images':[{'title':'', 'url':cItem.get('icon','')}], 'other_info':{}}]