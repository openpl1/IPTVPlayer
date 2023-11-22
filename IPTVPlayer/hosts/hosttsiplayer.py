# -*- coding: utf-8 -*-

import inspect
import os
import re
import sys

from Components.config import (ConfigSelection, ConfigText, ConfigYesNo,
                               config, getConfigListEntry)
from Plugins.Extensions.IPTVPlayer.components.ihost import (CBaseHostClass,
                                                            CHostBase)
from Plugins.Extensions.IPTVPlayer.components.iptvplayerinit import \
    TranslateTXT as _
from Plugins.Extensions.IPTVPlayer.libs.tstools import URLResolver, tscolor
from Plugins.Extensions.IPTVPlayer.libs.urlparser import urlparser
from Plugins.Extensions.IPTVPlayer.libs.urlparserhelper import \
    getDirectM3U8Playlist
from Plugins.Extensions.IPTVPlayer.tools.iptvtools import printDBG
from Plugins.Extensions.IPTVPlayer.tools.iptvtypes import strwithmeta

###################################################
config.plugins.iptvplayer.ts_hosts_online  = ConfigSelection(default = "", choices = [("", "Local"), ("vHKniFBR", "Saad"), ("gX993iaj", "ab0_0d"), ("2JfmFdzk", "Fagmixy"), ("J6j2Qgfe", "Test List")])
config.plugins.iptvplayer.ts_dsn           = ConfigYesNo(default = True)
config.plugins.iptvplayer.vs_meta_view     = ConfigYesNo(default = False)
config.plugins.iptvplayer.tsi_resolver     = ConfigSelection(default = "tsiplayer", choices = [("tsiplayer", "TSIPlayer"),("e2iplayer", "E2Iplayer")])
config.plugins.iptvplayer.xtream_active    = ConfigSelection(default = "Yes", choices = [("Yes", _("Yes")), ("", _("No"))])
config.plugins.iptvplayer.ts_xtream_user   = ConfigText(default = '', fixed_size = False)
config.plugins.iptvplayer.ts_xtream_pass   = ConfigText(default = '', fixed_size = False)
config.plugins.iptvplayer.ts_xtream_host   = ConfigText(default = '', fixed_size = False)
config.plugins.iptvplayer.ts_xtream_ua     = ConfigText(default = '', fixed_size = False)
config.plugins.iptvplayer.use_colors    = ConfigSelection(default = "", choices = [("", _("Auto")), ("yes", _("Yes")), ("no", _("No"))])

def GetConfigList():
    optionList = []
    optionList.append( getConfigListEntry(_("Get Hosts From:"), config.plugins.iptvplayer.ts_hosts_online) )
    optionList.append( getConfigListEntry(_("Decrypt Server Name:"), config.plugins.iptvplayer.ts_dsn) )
    optionList.append( getConfigListEntry(_("TSIplayer Resolver:"), config.plugins.iptvplayer.tsi_resolver) )
    optionList.append( getConfigListEntry(_("Display Xtream:"), config.plugins.iptvplayer.xtream_active) )
    if config.plugins.iptvplayer.xtream_active.value =='Yes':
        optionList.append( getConfigListEntry(_("    Xtream User:"), config.plugins.iptvplayer.ts_xtream_user) )
        optionList.append( getConfigListEntry(_("    Xtream Pass:"), config.plugins.iptvplayer.ts_xtream_pass) )
        optionList.append( getConfigListEntry(_("    Xtream Host:"), config.plugins.iptvplayer.ts_xtream_host) )
        optionList.append( getConfigListEntry(_("    Xtream User Agent:"), config.plugins.iptvplayer.ts_xtream_ua) )
    optionList.append( getConfigListEntry(_("Use colors:"), config.plugins.iptvplayer.use_colors) )
    return optionList


def gettytul():
    return 'TS IPlayer'

class TSIPlayer(CBaseHostClass):
    def __init__(self,item={}):
        self.MAIN_URL = ''
        self.startitem_=item
        CBaseHostClass.__init__(self, {'cookie':'TSIPlayer.cookie1'})
        self.USER_AGENT = self.cm.getDefaultHeader()['User-Agent']
        self.HEADER = {'User-Agent': self.USER_AGENT, 'Accept': 'text/html', 'Accept-Encoding':'gzip, deflate', 'Referer':'', 'Origin':''}
        self.defaultParams = {'header':self.HEADER, 'use_cookie': True, 'load_cookie': True, 'save_cookie': True, 'cookiefile': self.COOKIE_FILE}
        self.DEFAULT_ICON_URL = 'https://i.ibb.co/12Wsvq9/tsiplayer.png'
        self.import_str	=''
        self.ts_up = urlparser()


###################################################
# MAIN CATEGORY
###################################################
    def MainCat(self):
        try:
            hosts_path = '/tmp/tsiplayer_hosts.txt'
            if os.path.exists(hosts_path):
                os.remove(hosts_path)
            url_ = config.plugins.iptvplayer.ts_hosts_online.value
            if url_ !='':
                URL = 'https://pastebin.com/raw/'+url_
                sts, data = self.cm.getPage(URL)
                with open(hosts_path, 'w') as file:
                    file.write(data)
        except:
            pass
        self.tsiplayer_host({'cat_id':'901','ordre':0})
        self.addDir({'name':'cat','category' : 'MoviesSeriesAr','title':'Arabic Section','desc':'Arabic section','icon':'https://i.ibb.co/1vkwnDC/Arabic-section.png'} )

        if os.path.exists('/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/tsiplayer/addons/matrix/'):
            desc=tscolor('\c00????00')+'Une version '+tscolor('\c0000????')+'"Non Officielle"'+ '\\n'
            desc=desc + tscolor('\c00????00')+'Info:'+tscolor('\c00??????')+' '+'matrix est un addon KODI de streaming videos'+'\\n'
            desc=desc+tscolor('\c00????00')+'Version:'+tscolor('\c00??????')+' '+'19/02/2023'+'\\n'
            desc=desc+tscolor('\c00????00')+'Source:'+tscolor('\c00??????')+' '+'https://github.com/zombiB/zombi-addons/ | https://github.com/Yonn1981'+'\\n'
            desc=desc+tscolor('\c00????00')+'Developpeur:'+tscolor('\c00??????')+' '+'ZombiTn | '+ tscolor('\c00????00')+'Adaptation pour Tsiplayer: '+tscolor('\c00??????')+'fagmixy'+'\\n'
            elm = {'category': 'host2', 'import': 'from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.host_matrix import ', 'icon': 'https://i.ibb.co/p0ncdhN/matrix.png',
                   'mode': '03', 'title': 'Arabic Section ('+tscolor('\c0000????')+'Matrix'+tscolor('\c00??????')+')', 'desc': desc}
            self.addDir(elm )

        if os.path.exists('/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/tsiplayer/addons/vstream/'):
            desc=tscolor('\c00????00')+'Une version '+tscolor('\c0000????')+'"Non Officielle"'+ '\\n'
            desc=desc + tscolor('\c00????00')+'Info:'+tscolor('\c00??????')+' '+'vStream est un addon KODI de streaming videos'+'\\n'
            desc=desc+tscolor('\c00????00')+'Version:'+tscolor('\c00??????')+' '+'19/02/2023'+'\\n'
            desc=desc+tscolor('\c00????00')+'Source:'+tscolor('\c00??????')+' '+'https://github.com/Kodi-vStream/venom-xbmc-addons/'+'\\n'
            desc=desc+tscolor('\c00????00')+'Developpeur:'+tscolor('\c00??????')+' '+'vStream Team | '+ tscolor('\c00????00')+'Adaptation pour Tsiplayer: '+tscolor('\c00??????')+'RGYSoft'+'\\n'
            elm = {'category': 'host2', 'import': 'from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.host_vstream import ', 'icon': 'https://i.ibb.co/cDz1XLH/vstream.png', 'mode': '03', 'title': 'French Section ('+tscolor('\c0000????')+'VSTREAM'+tscolor('\c00??????')+')','desc':desc}
            self.addDir(elm )
        if os.path.exists('/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/tsiplayer/addons/kod/'):
            desc=tscolor('\c00????00')+'Une version '+tscolor('\c0000????')+'"Non Officielle"'+ '\\n'
            desc=desc + tscolor('\c00????00')+'Info:'+tscolor('\c00??????')+' '+'Kodi on Demand est un addon KODI de streaming videos'+'\\n'
            desc=desc+tscolor('\c00????00')+'Version:'+tscolor('\c00??????')+' '+'05/06/2021'+'\\n'
            desc=desc+tscolor('\c00????00')+'Source:'+tscolor('\c00??????')+' '+'https://github.com/Kodi-vStream/venom-xbmc-addons/'+'\\n'
            desc=desc+tscolor('\c00????00')+'Developpeur:'+tscolor('\c00??????')+' '+'vStream Team | '+ tscolor('\c00????00')+'Adaptation pour Tsiplayer: '+tscolor('\c00??????')+'RGYSoft'+'\\n'
            elm = {'category': 'host2', 'import': 'from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.host_kod import ', 'icon': 'https://i.ibb.co/cDz1XLH/vstream.png', 'mode': '03', 'title': 'Italien Section (KOD)','desc':desc}
            self.addDir(elm )


        self.addDir({'name':'cat','category' : 'Addons','title':'Addons','desc':'','icon':'https://i.ibb.co/gMVZfVq/addons.png'} )
        self.addDir({'name':'cat','category' : 'Trash','title':'Trash','desc':'','icon':'https://i.ibb.co/TgmYKTb/Trash.png'} )
        self.tsiplayer_host({'cat_id':'901','ordre':1})


    def FilmCatEn(self):
        self.addMarker({'category' :'marker','title':tscolor('\c00????00')+' -----●★| Movies & Series |★●-----','desc':'Movies, Series & Anime'})
        self.tsiplayer_host({'cat_id':'11'})
        self.tsiplayer_host({'cat_id':'12'})
        self.tsiplayer_host({'cat_id':'41'})
        self.tsiplayer_host({'cat_id':'904','gnr':'en'})

    def TrashCat(self):
        self.addMarker({'category' :'marker','title':tscolor('\c00????00')+' -----●★| Not Supported Hosts |★●-----','desc':'Not supported Hosts'})
        self.tsiplayer_host({'cat_id':'99'})
        self.addMarker({'category' :'marker','title':tscolor('\c00????00')+' -----●★| Not Working Hosts |★●-----','desc':'Not Working Hosts'})
        self.tsiplayer_host({'cat_id':'98'})




    def FilmCatAr(self):
        self.addMarker({'category' :'marker','title':tscolor('\c00????00')+' -----●★| LIVE & Replay |★●-----','desc':'Live & Replay'})
        self.tsiplayer_host({'cat_id':'10'})
        self.tsiplayer_host({'cat_id':'25'})
        self.tsiplayer_host({'cat_id':'26'})
        self.addMarker({'category' :'marker','title':tscolor('\c00????00')+' -----●★| Movies & Series |★●-----','desc':'Movies move us like nothing else can, whether they’re scary, funny, dramatic, romantic or anywhere in-between.\nSo many titles, so much to experience.'.title()})
        self.tsiplayer_host({'cat_id':'904','gnr':'ar'})
        self.tsiplayer_host({'cat_id':'11'})
        self.tsiplayer_host({'cat_id':'12'})
        self.tsiplayer_host({'cat_id':'21'})
        self.addMarker({'category' :'marker','title':tscolor('\c00????00')+' -----●★| Anime & Cartoons |★●-----','desc':'Action-packed adventures, comedies, inspirational stories\nthese anime movies and TV shows have a style and spirit unlike anything else'.title()})
        self.tsiplayer_host({'cat_id':'22'})
        self.tsiplayer_host({'cat_id':'23'})
        self.addMarker({'category' :'marker','title':tscolor('\c00????00')+' -----●★| Islamic |★●-----','desc':'The beauty of ‘The Quran’ is that you cannot change its message,\nbut its message can change you.'.title()})
        self.tsiplayer_host({'cat_id':'24'})
        self.addMarker({'category' :'marker','title':tscolor('\c00????00')+' -----●★| Documentary |★●-----','desc':'Documentary'})
        self.tsiplayer_host({'cat_id':'27'})

    def SportLiveReplay(self):
        self.tsiplayer_host({'cat_id':'10'})
        desc=''
        desc=desc + tscolor('\c00????00')+'Info:'+tscolor('\c00??????')+' '+'Youtube'+'\\n'
        desc=desc+tscolor('\c00????00')+'Version:'+tscolor('\c00??????')+' '+'1.1 24/06/2021'+'\\n'
        desc=desc+tscolor('\c00????00')+'Developpeur:'+tscolor('\c00??????')+' '+'E2IPlayer | '+ tscolor('\c00????00')+'Adaptation pour Tsiplayer: '+tscolor('\c00??????')+'RGYSoft'+'\\n'
        elm = {'category': 'host2', 'import': 'from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.host_youtube import ', 'icon': 'https://i.ibb.co/cgRTW3r/youtube.png', 'mode': '00', 'title': 'Youtube','desc':desc}
        self.addDir(elm )
        self.addMarker({'category' :'marker','title':tscolor('\c00????00')+' -----●★| Sport Replay |★●-----','desc':'Replay Sport'})
        self.tsiplayer_host({'cat_id':'25'})
        self.addMarker({'category' :'marker','title':tscolor('\c00????00')+' -----●★| Sport Live |★●-----','desc':'Replay Sport'})
        self.tsiplayer_host({'cat_id':'26'})

    def AddonsCat(self):
        self.tsiplayer_host({'cat_id':'902'})

    def DevCat(self):
        self.addDir({'name':'cat','category' : 'Addons','title':'Addons','desc':'','icon':'https://i.ibb.co/gMVZfVq/addons.png'} )
        self.addMarker({'category' :'marker','title':tscolor('\c00????00')+' -----●★| Tools |★●-----','desc':'Cartoons & Anime en VF et VOSTFR'})
        self.tsiplayer_host({'cat_id':'900'})


    def PrintExTs(self,e):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        inf_ = str(fname)+' ('+ str(exc_tb.tb_lineno)+')\n'+str(type(e).__name__)+' ('+str(e)+')\n'
        frm = inspect.trace()[-1]
        mod = inspect.getmodule(frm[0])
        (filename, line_number,function_name, lines, index) = inspect.getframeinfo(frm[0])
        filename = filename.replace('/usr/lib/enigma2/python/Plugins/Extensions/','>> ')
        inf_ = inf_+'FileName: '+str(filename)+' ('+str(line_number)+')\n'
        inf_ = inf_+'Function: '+str(function_name)+'\n'
        try:
            inf_ = inf_+'Line: '+str(lines[index]).strip()
        except:
            pass
        self.addMarker({'title':tscolor('\c00????00')+'----> Erreur <----','icon':'','desc':inf_})

###################################################
# HOST tsiplayer
###################################################
    def tsiplayer_get_host(self,cItem,type_):
        printDBG('-----> check type_'+type_)
        ordre = -1
        if type_ == 'private' :
            folder='/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/tsiplayer_local/'
            import_ = 'from Plugins.Extensions.IPTVPlayer.tsiplayer_local.'
            color_ = tscolor('\c0000????')
        elif type_ == 'public' :
            folder='/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/tsiplayer/'
            import_ = 'from Plugins.Extensions.IPTVPlayer.tsiplayer.'
            color_ = tscolor('\c00??????')
        elif type_ == 'addons' :
            folder='/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/tsiplayer/addons/'
            import_ = 'from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.'
            ordre = cItem.get('ordre',-1)
            color_ = tscolor('\c00??????')
        elif type_ == 'system' :
            folder='/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/tsiplayer/modules/'
            import_ = 'from Plugins.Extensions.IPTVPlayer.tsiplayer.modules.'
            ordre = cItem.get('ordre',-1)
            color_ = tscolor('\c00??????')

        gnr_=cItem.get('gnr','')
        cat_id=cItem.get('cat_id','')
        devmod=cItem.get('devmod','')

        lst=[]
        printDBG('-----> check Folder'+folder)
        if os.path.exists(folder):
            lst=os.listdir(folder)
            lst.sort()
            for (file_) in lst:
                printDBG('-----> check Host'+file_)
                if (file_.endswith('.py'))and((file_.startswith('host_')) or ((file_.startswith('hide_')))):
                    path_=folder+'/'+file_
                    import_str=import_+file_.replace('.py',' import ')
                    printDBG('-----> check Host1'+file_)
                    if 'vstream1' in file_:
                        try:
                            printDBG('-----> check Host2'+file_)
                            exec (import_str+'getinfo')
                            info=getinfo()
                            printDBG('-----> check info'+str(info))
                        except Exception as e:
                            info={}
                            info['warning']=' >>>>>>> Problem in this host <<<<<<<'
                            info['desc']=str(e)
                            info['name']=file_
                            info['icon']=''
                            info['version']=''
                            info['cat_id']='98'
                            info['dev']=''
                    else:
                        try:
                            printDBG('------------->IMPORT:'+import_str+'getinfo'+'<--------------------')
                            prg = import_str+'getinfo'
                            exec (prg, globals())
                            info=getinfo()
                        except Exception as e:
                            info={}
                            info['warning']=' >>>>>>> Problem in this host <<<<<<<'
                            info['desc']=str(e)
                            info['name']=file_
                            info['icon']=''
                            info['version']=''
                            info['cat_id']='98'
                            info['dev']=''
                    desc=''
                    icon_ = info['icon']
                    param_ = 'oui'
                    name_ = info['name']
                    if (info.get('filtre', '')!=''):
                        try:
                            cmd_='param_ = config.plugins.iptvplayer.'+info.get('filtre', '')+'.value'
                            exec(cmd_)
                        except:
                            param_ = ''
                    if param_!='':
                        if cat_id==info['cat_id']:
                            if cat_id=='n10':
                                desc=desc+tscolor('\c00????00')+' -----> !!!!!!!!! Not Working (Dev Mod) !!!!!!!!! <-----\\n'
                            if info.get('warning', '')!='':
                                desc=desc+tscolor('\c00????00')+' '+info.get('warning', '')+'\\n'
                            desc=desc+tscolor('\c00????00')+' Info: '+tscolor('\c00??????')+info['desc']+'\\n '+tscolor('\c00????00')+'Version: '+tscolor('\c00??????')+info['version']+'\\n '+tscolor('\c00????00')+'Developpeur: '+tscolor('\c00??????')+info['dev']+'\\n'
                            if info.get('update', '')!='':
                                desc=desc+tscolor('\c00????00')+' Last Update: '+tscolor('\c00??????')+info.get('update', '')+'\\n'
                            if info.get('old_host','')!='':
                                if info.get('old_host','') != info.get('host',''):
                                    desc=desc+tscolor('\c00????00')+' Host: '+tscolor('\c00??????')+info.get('old_host', '')+tscolor('\c00????00')+' >>> '+tscolor('\c0000????')+info.get('host', '')+'\\n'
                                else:
                                    desc=desc+tscolor('\c00????00')+' Host: '+tscolor('\c00??????')+info.get('host', '')+'\\n'
                            elif info.get('host','')!='':
                                desc=desc+tscolor('\c00????00')+' Host: '+tscolor('\c00??????')+info.get('host', '')+'\\n'
                            show = True
                            if ordre >-1:
                                show = False
                            if show:
                                self.addDir({'category' : 'host2','title':color_+name_,'desc':desc,'icon':icon_,'mode':'00','import':import_str,'gnr':gnr_})

    def tsiplayer_get_addons_host(self,cItem):
        folder='/usr/lib/enigma2/python/Plugins/Extensions/IPTVPlayer/tsiplayer/addons/'
        import_ = 'from Plugins.Extensions.IPTVPlayer.tsiplayer.addons.'
        color_ = tscolor('\c00????99')

        cat_id=cItem.get('cat_id','')

        lst=[]
        if os.path.exists(folder):
            lst=os.listdir(folder)
            lst.sort()
            for (file_) in lst:
                if (file_.endswith('.py'))and((file_.startswith('host_')) or ((file_.startswith('hide_')))):
                    path_=folder+'/'+file_
                    import_str=import_+file_.replace('.py',' import ')
                    sys.argv=''
                    try:
                        exec (import_str+'getinfo')
                        info = getinfo()
                    except Exception as e:
                        info={}
                        info['warning']=' >>>>>>> Problem in this host <<<<<<<'
                        info['desc']=str(e)
                        info['name']=file_
                        info['version']=''
                        info['dev']=''
                    try:
                        exec (import_str+'getHosts')
                        hsts=getHosts()
                    except Exception as e:
                        hsts=[]
                    for (cat_id_,elm_) in hsts:
                        if cat_id==cat_id_:
                            elm_['title']=color_+elm_['title']
                            self.addDir(elm_)


    def tsiplayer_host(self,cItem):
        self.tsiplayer_get_host(cItem,'private')
        self.tsiplayer_get_host(cItem,'public')
        self.tsiplayer_get_host(cItem,'addons')
        self.tsiplayer_get_host(cItem,'system')
        self.tsiplayer_get_addons_host(cItem)

    def host2_host(self,cItem):
        printDBG('cItem00='+str(cItem))
        mode_=cItem.get('mode','00')
        import_str = cItem.get('import',self.import_str)
        if self.import_str!=import_str:
            '''file_=import_str.replace('from Plugins.Extensions.IPTVPlayer.tsiplayer.','').replace(' import ','')
            try:
                _url='http://86.105.212.206/tsiplayer/stat.php?host='+file_+'&cat=Main_'
                self.cm.getPage(_url)
            except:
                printDBG('erreur')'''
            exec (import_str+'TSIPHost',globals())
            self.import_str=import_str
            self.host_ = TSIPHost()
        self.host_.currList=[]
        self.host_.start(cItem)
        self.currList=self.host_.currList

###################################################
# Main
###################################################

    def handleService(self, index, refresh = 0, searchPattern = '', searchType = ''):
        CBaseHostClass.handleService(self, index, refresh, searchPattern, searchType)
        if self.startitem_!={}:
            self.currItem=self.startitem_
            self.startitem_={}
        name     = self.currItem.get("name", '')
        category = self.currItem.get("category", '')
        printDBG( "handleService: || name[%s], category[%s] " % (name, category) )
        self.currList = []
        self.cacheLinks = {}
        if name == None:
            self.MainCat()
        elif category == 'search':
            self.listSearchResult(self.currItem,searchPattern, searchType)
        elif category == '_next_page':
            self.listSearchResult(self.currItem,'', '')
        elif category == 'MoviesSeriesAr':
            self.FilmCatAr()
        elif category == 'MoviesSeriesEn':
            self.FilmCatEn()
        elif category == 'SportLiveReplay':
            self.SportLiveReplay()
        elif category == 'Live':
            self.IptvCat()
        elif category == 'Devmod':
            self.DevCat()
        elif category == 'Trash':
            self.TrashCat()
        elif category == 'Addons':
            self.AddonsCat()
        else:
            try:
                try:
                    xx = len(sys.argv)
                except:
                    sys.argv = ''
                exec('self.'+category+'_host(self.currItem)')
            except Exception as e:
                self.PrintExTs(e)
                printDBG('erreeuuu')

        CBaseHostClass.endHandleService(self, index, refresh)



    def listSearchResult(self, cItem, searchPattern, searchType):
        hst=cItem['hst']
        cat=cItem['category']
        page=cItem.get('page',1)
        if cat=='_next_page':
            str_ch = cItem['searchPattern']
        else:
            str_ch = searchPattern
        if hst=='tshost':
            img = cItem['icon']
            self.host_.currList=[]
            self.host_.SearchResult(str_ch,page,extra=cItem['import'])
            self.currList=self.host_.currList
            if (type(page) != str) and (page>0):
                self.addDir({'import':cItem['import'],'category':'_next_page','title': tscolor('\c0000??00')+'Page Suivante','icon':img, 'search_item':False,'page':page+1,'searchPattern':str_ch,'hst':hst})
        else:
            exec('self.'+hst+'_search(str_ch,page)')
            if page>0:
                self.addDir({'category':'_next_page','title': tscolor('\c0000??00')+'Page Suivante', 'search_item':False,'page':page+1,'searchPattern':str_ch,'hst':hst})

    def getVideoLinks(self, videoUrl):
        printDBG("getVideoLinks [%s]" % videoUrl)
        urlTab = []
        if videoUrl.startswith('hst'):
            _data = re.findall('hst#(.*?)#(.*?)#', videoUrl+'#', re.S)
            hst=_data[0][0]
            videoUrl=_data[0][1]
        else:
            hst='none'
        if hst=='none':
            urlTab = self.TSgetVideoLinkExt(videoUrl)
        elif hst=='host':
            import_str,videoUrl=videoUrl.split('||')
            exec (import_str+'getVideos')
            urlTab1=getVideos(videoUrl)
            for (url_,type_) in urlTab1:
                if 	type_=='1':
                    urlTab = self.TSgetVideoLinkExt(url_)
                else:
                    urlTab.append({'name':'Direct', 'url':url_})
        elif hst=='tshost':
            urlTab1=self.host_.getVideos(videoUrl)
            urlTab=[]
            for (url_,type_) in urlTab1:
                if 	type_=='1':
                    printDBG('type=1')
                    urlTab = self.TSgetVideoLinkExt(url_)
                elif type_=='3':
                    urlTab = getDirectM3U8Playlist(url_, False, checkContent=True, sortWithMaxBitrate=999999999)
                elif type_=='0':
                    urlTab.append({'name':'Direct', 'url':url_})
                elif type_=='4':
                    meta =''
                    try:
                        meta = url_.meta
                    except:
                        pass
                    if meta != '':
                        urlTab.append({'name':url_.split('|')[0], 'url':strwithmeta(url_.split('|')[1],meta)})
                    else:
                        urlTab.append({'name':url_.split('|')[0], 'url':url_.split('|')[1]})
                elif type_=='5':
                    name = url_.split('|')[0]
                    URL  = url_.split('|')[1]
                    urltabout = self.TSgetVideoLinkExt(URL)
                    if urltabout !=[]:
                        for elm in urltabout:
                            elm['name']=name+' ['+elm['name']+']'
                            urlTab.append(elm)
                elif type_=='6':
                    vtt,lng,URL = url_.split('|',2)
                    subTrack = [{'title':lng, 'url':vtt, 'lang':lng, 'format':'vtt'}]
                    URL=strwithmeta(URL,{'external_sub_tracks':subTrack})
                    urlTab = getDirectM3U8Playlist(URL, False, checkContent=True, sortWithMaxBitrate=999999999)
                    print
                elif '7||||' in type_:
                    add_url = type_.split('||||')[1]
                    urlTab = getDirectM3U8Playlist(url_, False, checkContent=True, sortWithMaxBitrate=999999999)
                    urlTab1 = []
                    printDBG('urlTab ================ '+str(urlTab))
                    for elm in urlTab:
                        elm1 = dict(elm)
                        meta_ = elm1['url'].meta
                        printDBG('meta_ ================ '+str(meta_))
                        elm1['url'] = strwithmeta(add_url + elm1['url'],meta_)

                        urlTab1.append(elm1)
                    printDBG('urlTab ================ '+str(urlTab))
                    printDBG('urlTab ================ '+str(urlTab1))
                    return urlTab1
                else:
                    urlTab.append({'name':'Direct', 'url':url_})
        else:
            exec('urlTab = self.'+hst+'_videos(videoUrl)')
        return urlTab

    def getLinksForVideo(self, cItem):
        printDBG("TVProart.getLinksForVideo [%s]" % cItem)
        name=cItem['title']
        hst=cItem['hst']

        urlTab = []
        if hst=='direct':
            urlTab.append({'name':name, 'url':cItem['url'], 'need_resolve':0})
        elif hst=='none':
            urlTab.append({'name':name, 'url':cItem['url'], 'need_resolve':1})
        elif hst=='tshost':
            import_str = cItem.get('import',self.import_str)
            printDBG("self.import_str = "+str(self.import_str))
            printDBG("import_str = "+str(import_str))
            if self.import_str!=import_str:
                exec (import_str+'TSIPHost',globals())
                self.import_str=import_str
                self.host_ = TSIPHost()
            urlTab0=self.host_.get_links(cItem)
            urlTab=[]
            for elm in urlTab0:
                name_ = elm.get('name','XXXX')
                type_ = elm.get('type','XXXX')
                color =''
                name_ = name_.replace('\c0060??60','').replace('\c0090??20','').replace('\c00??3030','').replace('\C0060??60','').replace('\C0090??20','').replace('\C00??3030','')
                if config.plugins.iptvplayer.tsi_resolver.value=='tsiplayer':
                    printDBG('name_==='+name_)
                    if type_=='local':
                        color = tscolor('\c0060??60')
                    elif urlparser().checkHostSupportbyname(name_):
                        color = tscolor('\c0090??20')
                    elif urlparser().checkHostNotSupportbyname(name_):
                        color = tscolor('\c00??3030')
                    elif urlparser().checkHostSupportbyname_e2iplayer(name_):
                        color = tscolor('\c00????60')
                else:
                    if type_=='local':
                        color = tscolor('\c0060??60')
                    else: color = tscolor('\c00????60')

                if '|' in name_:
                    name_=name_.replace(name_.split('|')[-1],color+name_.split('|')[-1].lower().replace('www.','').title())
                else:
                    name_=color+name_.lower().replace('www.','').title()
                elm ['name']= name_
                urlTab.append(elm)

        else:
            exec('urlTab = self.'+hst+'_links(cItem[\'url\'])')
        return urlTab

    def getArticleContent(self, cItem):
        printDBG("getArticleContent [%s]" % cItem)
        retTab = []
        hst=cItem['hst']
        if hst=='direct':
            data=cItem.get('category', '')
            if data=='host2':
                retTab=self.host_.getArticle(cItem)
        elif hst=='tshost':
            retTab=self.host_.getArticle(cItem)
        elif hst=='xtream_vod':
            data=cItem.get('category', '')
            if data=='host2':
                retTab=self.host_.getArticle(cItem)
        else:
            exec ('retTab=self.'+hst+'_getArticleContent(cItem)')
        return retTab



    def TSgetVideoLinkExt(self,videoUrl):
        urlTab=[]
        try:
            urlTab = URLResolver(videoUrl).getLinks()
        except:
            urlTab=[]
        return urlTab


class IPTVHost(CHostBase):

    def __init__(self,item={}):
        CHostBase.__init__(self, TSIPlayer(item=item), False, [])

    def withArticleContent(self, cItem):
        if cItem.get('EPG', False): return True
        else: return False

