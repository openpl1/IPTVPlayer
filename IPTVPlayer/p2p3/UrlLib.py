# macro to load functions from correct modules depending on the python version
# build to simplify loading modules in e2iplayer scripts
# just change:
#   from urlib import
# to:
#   from Plugins.Extensions.IPTVPlayer.p2p3.UrlLib import
#

from Plugins.Extensions.IPTVPlayer.p2p3.pVer import isPY2

if isPY2():
    from urllib import addinfourl as urllib_addinfourl
    from urllib import quote as urllib_quote
    from urllib import quote_plus as urllib_quote_plus
    from urllib import unquote as urllib_unquote
    from urllib import unquote_plus as urllib_unquote_plus
    from urllib import urlencode as urllib_urlencode
    from urllib import urlopen as urllib_urlopen
    from urllib import urlretrieve as urllib_urlretrieve

    from urllib2 import BaseHandler as urllib2_BaseHandler
    from urllib2 import HTTPBasicAuthHandler as urllib2_HTTPBasicAuthHandler
    from urllib2 import HTTPCookieProcessor as urllib2_HTTPCookieProcessor
    from urllib2 import HTTPError as urllib2_HTTPError
    from urllib2 import HTTPErrorProcessor as urllib2_HTTPErrorProcessor
    from urllib2 import HTTPHandler as urllib2_HTTPHandler
    from urllib2 import HTTPRedirectHandler as urllib2_HTTPRedirectHandler
    from urllib2 import HTTPSHandler as urllib2_HTTPSHandler
    from urllib2 import ProxyHandler as urllib2_ProxyHandler
    from urllib2 import Request as urllib2_Request
    from urllib2 import URLError as urllib2_URLError
    from urllib2 import build_opener as urllib2_build_opener
    from urllib2 import install_opener as urllib2_install_opener
    from urllib2 import urlopen as urllib2_urlopen
else:
    from urllib.error import HTTPError as urllib2_HTTPError
    from urllib.error import URLError as urllib2_URLError
    from urllib.parse import quote as urllib_quote
    from urllib.parse import quote_plus as urllib_quote_plus
    from urllib.parse import unquote as urllib_unquote
    from urllib.parse import unquote_plus as urllib_unquote_plus
    from urllib.parse import urlencode as urllib_urlencode
    from urllib.request import BaseHandler as urllib2_BaseHandler
    from urllib.request import \
        HTTPBasicAuthHandler as urllib2_HTTPBasicAuthHandler
    from urllib.request import \
        HTTPCookieProcessor as urllib2_HTTPCookieProcessor
    from urllib.request import HTTPErrorProcessor as urllib2_HTTPErrorProcessor
    from urllib.request import HTTPHandler as urllib2_HTTPHandler
    from urllib.request import \
        HTTPRedirectHandler as urllib2_HTTPRedirectHandler
    from urllib.request import HTTPSHandler as urllib2_HTTPSHandler
    from urllib.request import ProxyHandler as urllib2_ProxyHandler
    from urllib.request import Request as urllib2_Request
    from urllib.request import addinfourl as urllib_addinfourl
    from urllib.request import build_opener as urllib2_build_opener
    from urllib.request import install_opener as urllib2_install_opener
    from urllib.request import urlopen as urllib2_urlopen
    from urllib.request import urlopen as urllib_urlopen
    from urllib.request import urlretrieve as urllib_urlretrieve
