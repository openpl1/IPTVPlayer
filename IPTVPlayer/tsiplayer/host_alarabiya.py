# -*- coding: utf-8 -*-

import re

from Plugins.Extensions.IPTVPlayer.libs import ph
from Plugins.Extensions.IPTVPlayer.libs.tstools import (TSCBaseHostClass,
                                                        tscolor, tshost)


def getinfo():
    info_={}
    name = 'Alarabiya'
    hst = 'https://www.alarabiya.net'
    info_['old_host'] = hst
    hst_ = tshost(name)
    if hst_!='': hst = hst_
    info_['host']= hst
    info_['name']=name
    info_['version']='1.0 18/07/2023'
    info_['dev']='MOHAMED_OS'
    info_['cat_id']='27'
    info_['desc']='افلام وثائقية'
    info_['icon'] = 'https://i.ibb.co/smkDkR8/alarabiya.png'
    info_['recherche_all']='0'
    return info_


class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self,{})
        self.MAIN_URL   =  getinfo()['host']

    def showmenu(self,cItem):
        TAB = [('افلام وثائقية','/programs/documentaries/','20',0)]
        self.add_menu(cItem,'','','','','','',TAB=TAB,search=False)

    def showitms(self,cItem):
        page = cItem.get('page',1)
        URL = cItem.get('url')+'?pageNo='+str(page)
        sts, data = self.getPage(URL)
        if sts:
            data = re.findall(r'class="video-list(.*?)class="pagination', data, re.S)[0]
            if data:
                Liste_els = re.findall(r'<a class="list-item-link" href="(.+?)" title="(.+?)">.+?<img src="(.+?)" width=', data, re.S)
                for (url,titre,image)in Liste_els:
                    info  = self.std_title(ph.clean_html(titre),with_ep=True)
                    sTitel = info.get('title_display')
                    desc_ = info.get('desc')
                    self.addDir({'import':cItem['import'],'category' : 'host2','title':sTitel,'icon':image,'desc':desc_,'mode':'21','url':url,'good_for_fav':True,'EPG':True,'hst':'tshost'})
            self.addDir({'import':cItem['import'],'category' : 'host2','title':tscolor('\c00????00')+'Next Page >>'+tscolor('\c00??????'),'icon':cItem['icon'],'desc':'','mode':'20','url':cItem['url'],'page':page+1})


    def showelms(self,cItem):
        sTitle = cItem['title'].replace("|","").replace("الفيلم الوثائقي","").replace("وثائقي","")
        self.addVideo({'import':cItem['import'], 'hst':'tshost', 'url':self.MAIN_URL+cItem['url'], 'title':sTitle, 'desc':'','icon':cItem['icon'],'good_for_fav':True,'EPG':True,'hst':'tshost'})

    def get_links(self,cItem):
        urlTab = []
        sts, data = self.getPage(cItem['url'])
        if sts:
            siteUrl = re.findall(r',"contentUrl": "(.+?)"', data, re.S)
            if siteUrl[0]:
                urlTab.append({'name':'', 'url':siteUrl[0], 'need_resolve':0})
        return urlTab

    def getArticle(self,cItem):
        Desc = [('Year','class="caption">(.*?)</','\n',''),('Time','class="time">(.*?)</','\n','')]
        desc = self.add_menu(cItem,'','video-list ">(.+?)light-theme”>','','desc',Desc=Desc)
        if desc =='': desc = cItem.get('desc','')
        return [{'title':cItem['title'], 'text': desc, 'images':[{'title':'', 'url':cItem.get('icon','')}], 'other_info':{}}]