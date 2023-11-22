# -*- coding: utf8 -*-
import re

from Plugins.Extensions.IPTVPlayer.libs.e2ijson import loads as json_loads
from Plugins.Extensions.IPTVPlayer.libs.tstools import (TSCBaseHostClass,
                                                        tscolor)
from Plugins.Extensions.IPTVPlayer.tools.iptvtools import printDBG


def getinfo():
    info_={}
    info_['name'] = 'MP3Quran'
    info_['version']='1.1 07/07/2020'
    info_['dev']='RGYSoft'
    info_['cat_id']='24'
    info_['desc']='Quran Audio Library'
    info_['icon']='https://i.ibb.co/CzNcfh4/MP3Quran.png'
    info_['recherche_all']='0'
    return info_

class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self,{'cookie':'mp3quran.cookie'})
        self.USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
        self.MAIN_URL = 'https://www.mp3quran.net'
        self.HEADER = {'User-Agent': self.USER_AGENT, 'Connection': 'keep-alive', 'Accept-Encoding':'gzip', 'Content-Type':'application/x-www-form-urlencoded','Referer':self.getMainUrl(), 'Origin':self.getMainUrl()}
        self.defaultParams = {'header':self.HEADER, 'use_cookie': True, 'load_cookie': True, 'save_cookie': True, 'cookiefile': self.COOKIE_FILE}


    def showmenu(self,cItem):
        self.addDir({'import':cItem['import'],'category' :'host2','title':'Reciters | '+'القراء'+' Ar','icon':cItem['icon'],'mode': '20','lng':'ar'})
        self.addDir({'import':cItem['import'],'category' :'host2','title':'Reciters | '+'القراء'+' En','icon':cItem['icon'],'mode': '20','lng':'eng'})
        self.addDir({'import':cItem['import'],'category' :'host2','title':'Radios','icon':cItem['icon'],'mode': '21'})
        self.addAudio({'import':cItem['import'],'title':'LIVE Radio','url':'http://live.mp3quran.net:8006/;','icon':cItem['icon'],'desc':tscolor('\c00??0000')+'LIVE','hst':'direct'})


    def showmenu1(self,cItem):
        lng = cItem['lng']
        rewaya_ = cItem.get('rewaya',-1)
        if rewaya_ ==-1:
            if lng != 'eng':
                tt = tscolor('\c00????00')+'>>> '+'اختر الرواية / نوع المصحف'+' <<<'
            else:
                tt = tscolor('\c00????00')+'>>> '+'Select Rewaya'+' <<<'
            self.addDir({'import':cItem['import'],'category' :'host2','title':tt,'icon':cItem['icon'],'mode': '50','lng':lng})

        Url = self.MAIN_URL + '/'+lng+'/ajax/reads/list'
        addParams = dict(self.defaultParams)
        addParams['header']['X-Requested-With'] = 'XMLHttpRequest'
        sts, data = self.getPage(Url,addParams)
        if sts:
            data = json_loads(data)
            reads = data.get('reads',[{}])
            reads = sorted(reads, key=lambda d: d['title'])
            for elm in reads:
                printDBG('elm='+str(elm))
                titre   = elm.get('title','')
                count   = elm.get('soar_count','')
                rewaya  = elm.get('rewaya_name','')
                reciter = elm.get('reciter_name','')
                if 'reciter title' in titre: titre = reciter
                url     = elm.get('url','')
                id_     = elm.get('id','')
                slug    = elm.get('slug','')
                desc = tscolor('\c00????00')+'Info: '+tscolor('\c00??????')+count+'\n'
                desc = desc + tscolor('\c00????00')+'Reciter: '+tscolor('\c00??????')+reciter+'\n'
                desc = desc + tscolor('\c00????00')+'Rewaya: '+tscolor('\c00??????')+rewaya+'\n'
                if ((rewaya_ == -1) or (rewaya_ == rewaya)):
                    self.addDir({'import':cItem['import'],'category' :'host2','title':titre,'desc':desc,'icon':cItem['icon'],'slug':slug,'mode': '40','lng':lng,'url':url})

    def showmenu4(self,cItem):
        lng = cItem['lng']
        Url = self.MAIN_URL + '/'+lng
        sts, data = self.getPage(Url)
        if sts:
            data_ = re.findall('<a class="dropdown.*?emit.*?,(.*?)\).*?>(.*?)</a>', data, re.S)
            for (riwaya,titre) in data_:
                if riwaya.strip() != '0':
                    titre = self.cleanHtmlStr(titre).strip()
                    self.addDir({'import':cItem['import'],'category' :'host2','title':titre,'icon':cItem['icon'],'mode': '20','lng':lng,'rewaya':titre})

    def showmenu2(self,cItem):
        url='https://www.atheer-radio.com/assets/data/home-ar.json'
        sts, data = self.getPage(url)
        if sts:
            data = json_loads(data)
            print(data)
            for elm in data['banners']+data['listenHistory']+data['mostListen']:
                id_=elm['id']
                name=elm['name']
                radio_url=elm['url']
                image='https://www.atheer-radio.com/'+elm.get('image','')
                self.addAudio({'import':cItem['import'],'title':name,'url':radio_url,'icon':image,'desc':tscolor('\c00??0000')+'LIVE','hst':'direct'})



    def showmenu3(self,cItem):
        url=cItem['url']
        sts, data = self.getPage(url)
        if sts:
            data = json_loads(data)
            for elm in data['radios']:
                name=elm['name']
                radio_url=elm['radio_url']
                self.addAudio({'import':cItem['import'],'title':name,'url':radio_url,'icon':cItem['icon'],'hst': 'direct'})




    def showitms(self,cItem):
        Url=cItem['url']
        page=cItem.get('page',1)
        url_=Url+'?page='+str(page)
        sts, data = self.getPage(url_)
        if sts:
            data_ = re.findall('class="thumbnail">.*?href="(.*?)".*?src="(.*?)".*?<h5>(.*?)</h5>', data, re.S)
            for (url,image,titre) in data_:
                url='https://videos.mp3quran.net'+url.replace('//','/')
                image='https://videos.mp3quran.net'+image
                self.addVideo({'import':cItem['import'],'category' :'host2','title':titre,'url':url,'icon':image,'hst': 'tshost'})
            self.addDir({'import':cItem['import'],'category' : 'host2','title':'Next','url':Url,'page':page+1,'mode':'30'})





    def showitms1(self,cItem):
        lng  = cItem['lng']
        slug = cItem['slug']
        url  = cItem['url']
        Url  = self.MAIN_URL + '/'+lng+'/'+slug
        sts, data = self.getPage(Url)
        if sts:
            printDBG('Data001='+data)
            _data = re.findall('sora-info">.*?sora-num">(.*?)<.*?sora-name">.*?>(.*?)</a>.*?href="(.*?)"', data, re.S)
            for (num,titre,url) in _data:
                titre = tscolor('\c00????00')+str(num)+tscolor('\c00??????')+' - ' + self.cleanHtmlStr(titre).strip()
                self.addAudio({'import':cItem['import'],'title':titre,'url':url,'icon':cItem['icon'],'desc':'Num: '+tscolor('\c00????00')+str(num),'hst':'direct'})


    def get_links(self,cItem):
        urlTab = []
        URL=cItem['url']
        sts, data = self.getPage(URL)
        if sts:
            _data = re.findall('video-grid">.*?src="(.*?)"', data, re.S)
            if _data:
                url='https://videos.mp3quran.net'+_data[0]
                url=url.replace('&#39;',"'")
                urlTab.append({'name':cItem['title'], 'url':url, 'need_resolve':0})
        return urlTab




    def start(self,cItem):
        mode=cItem.get('mode', None)
        if mode=='00':
            self.showmenu(cItem)
        if mode=='20':
            self.showmenu1(cItem)
        if mode=='21':
            self.showmenu2(cItem)
        if mode=='22':
            self.showmenu3(cItem)
        if mode=='30':
            self.showitms(cItem)
        if mode=='40':
            self.showitms1(cItem)
        if mode=='50':
            self.showmenu4(cItem)
        return True
