# -*- coding: utf-8 -*-
import re

from Plugins.Extensions.IPTVPlayer.libs import ph
from Plugins.Extensions.IPTVPlayer.libs.tstools import T, TSCBaseHostClass


def getinfo():
    info_={}
    info_['name']='Shahiid Anime'
    info_['version']='1.0 17/08/2019'
    info_['dev']='RGYSoft'
    info_['cat_id']='22'
    info_['desc']='أفلام و مسلسلات اجنبية'
    info_['icon']='https://i.ibb.co/nfCx7PD/Shahiid-Anime.png'
    info_['recherche_all']='0'
    info_['update']='New Host'
    return info_


class TSIPHost(TSCBaseHostClass):
    def __init__(self):
        TSCBaseHostClass.__init__(self,{'cookie':'shahiidanime.cookie'})
        self.USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'
        self.MAIN_URL = 'https://shahiid-anime.net'
        self.HEADER = {'User-Agent': self.USER_AGENT,'Accept':'*/*','X-Requested-With':'XMLHttpRequest', 'Connection': 'keep-alive', 'Accept-Encoding':'gzip', 'Pragma':'no-cache'}
        self.defaultParams = {'timeout':9,'header':self.HEADER, 'use_cookie': True, 'load_cookie': True, 'save_cookie': True, 'cookiefile': self.COOKIE_FILE}

    def showmenu0(self,cItem):
        hst='host2'
        img_=cItem['icon']
        Cat_TAB = [{'category':hst,'title': 'أفلام الأنمي'       , 'mode':'30','url':self.MAIN_URL+'/anime/'},
                    {'category':hst,'title': 'مسلسلات الأنمي'      , 'mode':'30','url':self.MAIN_URL+'/series/'},]
        self.listsTab(Cat_TAB, {'import':cItem['import'],'icon':img_})
        self.addDir({'import':cItem['import'],'category' :'host2','title':T('Search')  ,'icon':cItem['icon'],'mode':'51'})

    def SearchAll(self,str_ch,page=1,extra='',type_=''):
        return self.get_items({'page':page,'import':extra,'str_ch':str_ch})

    def SearchAnims(self,str_ch,page=1,extra=''):
        elms = self.SearchAll(str_ch,page,extra=extra,type_='')
        return elms

    def get_items(self,cItem={}):
        elms    = []
        extra   = cItem.get('import')
        str_ch  = cItem.get('str_ch')
        page    = cItem.get('page', 1)
        if page>1:
            url_=self.MAIN_URL + '/page/' + str(page) + '/?s='+str_ch
        else:
            url_=self.MAIN_URL + '/?s='+str_ch
        sts, data = self.getPage(url_)
        if sts:
            films_list = re.findall('class="one-poster.*?href="(.*?)".*?src="(.*?)".*?<h2>(.*?)</h2>', data, re.S)
            for (url,image,titre) in films_list:
                info  = self.std_title(ph.clean_html(titre),with_ep=True)
                elms.append({'import':extra,'good_for_fav':True,'EPG':True,'category' : 'host2','url': url,'title':info.get('title_display'),'desc':info.get('desc'),'icon':image,'hst':'tshost','mode':'31'})
            films_list = re.findall("class='current'>.*?class='inactive'>", data, re.S)
            if films_list:
                elms.append({'import':extra,'category' : 'host2','title':T('Next'),'url':'','desc':'Next','icon':'','hst':'tshost','mode':'51','page':page+1,'str_ch':str_ch,'type_':''})
        return elms


    def showitms(self,cItem):
        url1=cItem['url']
        if url1.endswith('-search'):

            post_data={cItem['par']:cItem['val'].replace('%25','%'),'submit':'بحث'}
            sts, data = self.getPage(url1,post_data = post_data)
        else:
            page=cItem.get('page',1)
            url1=url1+'page/'+str(page)+'/'
            sts, data = self.getPage(url1)
        if sts:
            films_list = re.findall('class="one-poster.*?href="(.*?)".*?src="(.*?)".*?<h2>(.*?)</h2>', data, re.S)
            for (url,image,titre) in films_list:
                info  = self.std_title(ph.clean_html(titre),with_ep=True)
                self.addDir({'import':cItem['import'],'good_for_fav':True,'EPG':True,'category' : 'host2','url': url,'title':info.get('title_display'),'desc':info.get('desc'),'icon':image,'hst':'tshost','mode':'31'})
            if not url1.endswith('-search'):
                self.addDir({'import':cItem['import'],'title':'Page '+str(page+1),'page':page+1,'category' : 'host2','url':cItem['url'],'icon':image,'mode':'30'} )

    def showelms(self,cItem):
        sts, data = self.getPage(cItem['url'])
        if sts:
            films_list = re.findall('window.location.{1,4}"(.*?)"', data, re.S)
            if films_list:
                sts, data = self.getPage(films_list[0])
            if sts:
                if 'class="movies-servers' in data:
                    self.addVideo({'import':cItem['import'],'good_for_fav':True,'category' : 'host2','url': cItem['url'],'title':cItem['title'],'desc':cItem['desc'],'icon':cItem['icon'],'hst':'tshost'} )
                else:
                    films_list = re.findall('class="navbar.*?href="(.*?)".*?>(.*?)<', data, re.S)
                    if films_list:
                        for (url,titre) in films_list:
                            self.addVideo({'import':cItem['import'],'good_for_fav':True,'category' : 'host2','url': url,'title':self.std_extract(titre),'desc':cItem['desc'],'icon':cItem['icon'],'hst':'tshost'} )
                    else:
                        films_list = re.findall('class="one-poster.*?href="(.*?)".*?src="(.*?)".*?<h2>(.*?)</h2>', data, re.S)
                        for (url,image,titre) in films_list:
                            info  = self.std_title(ph.clean_html(titre),with_ep=True)
                            self.addDir({'import':cItem['import'],'good_for_fav':True,'category' : 'host2','url': url,'title':info.get('title_display'),'desc':cItem['desc'],'icon':image,'hst':'tshost','mode':'31'} )


    def SearchResult(self,str_ch,page,extra):
        url_=self.MAIN_URL + '/?s='+str_ch
        sts, data = self.getPage(url_)
        if sts:
            films_list = re.findall('class="one-poster.*?href="(.*?)".*?src="(.*?)".*?<h2>(.*?)</h2>', data, re.S)
            for (url,image,titre) in films_list:
                info  = self.std_title(ph.clean_html(titre),with_ep=True)
                self.addDir({'import':extra,'good_for_fav':True,'EPG':True,'category' : 'host2','url': url,'title':info.get('title_display'),'desc':info.get('desc'),'icon':image,'hst':'tshost','mode':'31'})

    def get_links(self,cItem):
        urlTab = []
        URL=cItem['url']
        sts, data = self.getPage(URL,self.defaultParams)
        if sts:
            Tab_els = re.findall('btn-trailer">.*?href="(.*?)"', data, re.S)
            if Tab_els:
                urlTab.append({'name':'TRAILER', 'url':Tab_els[0], 'need_resolve':1})
            Tab_els = re.findall('class="movies-servers(.*?)</ul', data, re.S)
            if Tab_els:
                Tab_els = re.findall('<li.*?data-serv="(.*?)".*?data-frameserver=\'(.*?)\'.*?data-post="(.*?)".*?>(.*?)</li>', Tab_els[0], re.S)
                for (serv,frame,post,titre) in Tab_els:
                    url=''
                    titre=ph.clean_html(titre)
                    Tab_els = re.findall('src="(.*?)"', frame.replace('&#34;','"'), re.IGNORECASE)
                    if Tab_els:
                        url = Tab_els[0]
                        if url.startswith('//'): url='https:'+url
                        urlTab.append({'name':titre, 'url':url, 'need_resolve':1})
                    else:
                        url = 'https://shahiid-anime.net/wp-admin/admin-ajax.php?action=codecanal_ajax_request&post='+post+'&frameserver='+frame+'&serv='+serv
                        urlTab.append({'name':'|shahiid-anime| '+titre, 'url':'hst#tshost#'+url, 'need_resolve':1})
        return urlTab

    def getVideos(self,videoUrl):
        urlTab = []
        sts, data = self.getPage(videoUrl)
        if sts:
            Tab_els = re.findall('src="(.*?)"', data, re.IGNORECASE)
            if Tab_els:
                url=Tab_els[0]
                if url.startswith('//'): url='https:'+url
                urlTab.append((url,'1'))
        return urlTab





    def getArticle(self, cItem):
        otherInfo1 = {}
        desc= cItem.get('desc','')
        sts, data = self.getPage(cItem['url'])
        if sts:
            films_list = re.findall('window.location.{1,4}"(.*?)"', data, re.S)
            if films_list:
                sts, data = self.getPage(films_list[0])
            if sts:
                #printDBG('ddddaaaaaaaaaaaatttaaaaaaaaaa'+data)
                lst_dat0=re.findall('<h1>(.*?)class="a-shars">', data, re.S)
                if lst_dat0:
                    lst_dat2=re.findall('<i.class="fa(.*?):(.*?)</span>', lst_dat0[0], re.S)
                    for (x1,x2) in lst_dat2:
                        if 'IMDB' in x1: otherInfo1['rating'] = ph.clean_html(x2)
                        if 'الدولة'  in x1: otherInfo1['country'] = ph.clean_html(x2)
                        if 'التوقيت'  in x1: otherInfo1['duration'] = ph.clean_html(x2)
                        if 'السنة' in x1: otherInfo1['year'] = ph.clean_html(x2)
                        if 'الجودة'  in x1: otherInfo1['quality'] = ph.clean_html(x2)
                    lst_dat2=re.findall('class="head-s-(.*?)clearfix">(.*?)</div>', lst_dat0[0], re.S)
                    for (x1,x2) in lst_dat2:
                        if 'meta-ctas'  in x1: otherInfo1['genres'] = ph.clean_html(x2)
                        if 'story'  in x1: desc=ph.clean_html(x2)

        icon = cItem.get('icon')
        title = cItem['title']
        return [{'title':title, 'text': desc, 'images':[{'title':'', 'url':icon}], 'other_info':otherInfo1}]




    def start(self,cItem):
        mode=cItem.get('mode', None)
        if mode=='00':
            self.showmenu0(cItem)
        if mode=='20':
            self.showmenu1(cItem)
        if mode=='30':
            self.showitms(cItem)
        if mode=='31':
            self.showelms(cItem)
        elif mode=='51':
            self.searchResult(cItem)
            name= 'searchResult'
