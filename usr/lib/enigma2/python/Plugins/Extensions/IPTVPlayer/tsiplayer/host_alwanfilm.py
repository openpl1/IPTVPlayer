# -*- coding: utf8 -*-
import re

from Plugins.Extensions.IPTVPlayer.components.e2ivkselector import \
    GetVirtualKeyboard
from Plugins.Extensions.IPTVPlayer.libs import ph
from Plugins.Extensions.IPTVPlayer.libs.tstools import (T, TSCBaseHostClass,
                                                        gethostname, tscolor,
                                                        tshost)


def getinfo():
    info_={}
    name = 'Alwan Film'
    hst = 'https://alwanfilm.com'
    info_['old_host'] = hst
    hst_ = tshost(name)
    if hst_!='': hst = hst_
    info_['host']= hst
    info_['name']=name
    info_['version']='2.2 29/10/2023'
    info_['dev']='RGYSoft'
    info_['cat_id']='21'
    info_['desc']='أفـــلامـــ'
    info_['icon']='https://i.ibb.co/QM7qRth/alwanfilm.png'
    info_['recherche_all']='0'
    return info_

class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self,{'cookie':'none.cookie'})
        self.MAIN_URL   =  getinfo()['host']
        self.USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'
        self.HEADER     = {'User-Agent': self.USER_AGENT,'x-requested-with':'XMLHttpRequest', 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
        self.defaultParams = {'header':self.HEADER, 'use_cookie': False}

    def showmenu(self,cItem):
        TAB = [('أفــلام كـلاسـيكـية','/movies/','20',0)]
        self.add_menu(cItem,'','','','','',TAB=TAB,search=False)
        self.addDir({'import':cItem['import'],'category' :'host2','title':T('Search')  ,'icon':cItem['icon'],'mode':'51'})

    def showitms(self,cItem):
        page = cItem.get('page',1)
        URL = cItem.get('url','')+'page/'+str(page)+'/'
        sts, data = self.getPage(URL)
        if sts:
            Liste_els = re.findall('<article.+?src="([^"]+)".+?aria-label.+?href="([^<]+)">(.+?)</span>', data, re.S)
            for (image,url,titre) in Liste_els:
                info  = self.std_title(ph.clean_html(titre.replace("Colorized","")),with_ep=True)
                Url = self.MAIN_URL + "/movies/" + url.replace("index.html","")
                Image = self.MAIN_URL + image.replace("../","/")
                self.addVideo({'import':cItem['import'],'category' : 'host2','title':info.get('title_display'),'icon':Image,'desc':info.get('desc'),'url':Url,'good_for_fav':True,'EPG':True,'hst':'tshost'})
            self.addDir({'import':cItem['import'],'category' : 'host2','title':tscolor('\c00????00')+'Next Page >>'+tscolor('\c00??????'),'icon':cItem['icon'],'desc':'','mode':'20','url':cItem['url'],'page':page+1})

    def SearchResult(self,str_ch,page,extra):
        url = self.MAIN_URL+'/?s='+str_ch
        desc = [('Date','year">(.*?)</span>','',''),('Rating','rating">(.*?)</span>','',''),('Story','contenido">(.*?)</div>','\n','')]
        self.add_menu({'import':extra,'url':url},'','item">.*?href="(.*?)".*?data-src="(.*?)".*?title">(.*?)</div>(.*?)</article>','','video',ord=[0,2,1,3],Desc=desc)

    def get_links(self,cItem):
        urlTab = []
        sts, data = self.getPage(cItem.get('url'))
        if sts:
            Liste_els = re.findall('dooplay_player_response.+?src="([^"]+)"', data, re.S)
            for Url_ in Liste_els:
                urlTab.append({'name':gethostname(Url_,True), 'url':Url_, 'need_resolve':1,'type':'local'})
        return urlTab

    def searchResult(self,cItem):
        str_ch  = cItem.get('str_ch','')
        if str_ch =='':
            ret = self.sessionEx.waitForFinishOpen(GetVirtualKeyboard(), title=('Search Text:'), text='')
            str_ch = ret[0]
        if not str_ch: return []
        page    = cItem.get('page',1)
        extra   = cItem.get('import','')
        elms = self.SearchAll(str_ch,page,extra,'')
        for elm in elms:
            if elm.get('type','') == 'video':
                self.addVideo(elm)
            else: self.addDir(elm)
        return elms

    def get_items(self,url_,extra,pat='',page=1,mode_='',str_ch=''):
        elms = []
        if (page > 1) and ('/?s=' not in url_): url__ = url_ + 'page/'+str(page)+'/'
        else: url__ = url_
        sts, data = self.getPage(url__)
        if sts:
            lst_data=re.findall(pat, data, re.S)
            if 'data-src=' not in pat:
                lst_data_ = []
                for (image,desc1,url,titre,desc2) in lst_data:
                    lst_data_.append((url,image,titre,desc1+desc2))
                lst_data = lst_data_
            for (url,image,titre,desc) in lst_data:
                titre = self.cleanHtmlStr(titre)
                titre = titre.replace('&#8220;','').replace('&#8221;','').replace('باﻷلوان','').strip().replace('Colorized','').strip()
                info  = self.extract_desc(desc,[('year','year">(.*?)</span>'),('year','</h3>(.*?)</span>'),('rating','rating">(.*?)(?:</span>|</div>)'),('plot','contenido">(.*?)</div>'),('quality','quality">(.*?)</div>')])
                lst_=re.findall('<div class="metadata">(.*?)</div>', desc, re.S)
                if lst_:
                    lst_=re.findall('<span.*?>(.*?)</span>', lst_[0], re.S)
                    for elm in lst_:
                        if (len(elm.strip()) == 4) and (elm.strip().startswith('19')):
                            info['year'] = elm.strip()
                info  = self.std_title(titre,desc=info)
                elm = {'import':extra,'category' : 'host2','sTitle':info['title'],'title':info['title_display'],'url':url,'desc':info['desc'],'icon':image,'good_for_fav':True,'EPG':True,'hst':'tshost','info':info,'type':'video'}
                elms.append(elm)
            lst_data=re.findall('class="pagination">.*?class="current">.*?class="inactive">', data, re.S)
            if lst_data:
                elms.append({'import':extra,'category' : 'host2','title':T('Next'),'url':url_,'desc':'Next','icon':'','hst':'tshost','mode':mode_,'page':page+1,'str_ch':str_ch})
        return elms

    def SearchAll(self,str_ch,page=1,extra='',type_=''):
        elms=[]
        pat = 'item">.*?href="(.*?)".*?data-src="(.*?)".*?title">(.*?)</div>(.*?)</article>'
        url_ = self.MAIN_URL + '/page/'+str(page)+'/?s='+str_ch
        return self.get_items(url_,extra,pat=pat,page=page,mode_='51',str_ch=str_ch)

    def SearchMovies(self,str_ch,page=1,extra=''):
        elms = self.SearchAll(str_ch,page,extra=extra)
        return elms

    def getArticle(self,cItem):
        Desc = [('Year','dateCreated">(.+?)</','\n',''),('Generes','href=".+?genre.+?rel="tag">(.+?)</','\n',''),('Country','class="country">(.+?)</','\n',''),('Duration','class="runtime">(.+?)</','\n','')]
        desc = self.add_menu(cItem,'','','','desc',Desc=Desc)
        if desc =='': desc = cItem.get('desc','')
        return [{'title':cItem['title'], 'text': desc, 'images':[{'title':'', 'url':cItem.get('icon','')}], 'other_info':{}}]