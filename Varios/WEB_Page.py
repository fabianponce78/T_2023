'''
Created on Jun 16, 2022

@author: Fabian Ponce
'''
import urllib.request, urllib.error, urllib.parse

url = 'http://www.photoplanet.com.mx/find/findphoto.asp?cat=5&subcat=84&gpo=863&alb=1077&Key=235&iNB=47786&Cnf=OK'
url = 'http://www.photoplanet.com.mx/find/detalle.asp?PH=N3318582&iwl=0'

response = urllib.request.urlopen(url)
#webContent = response.read().decode('UTF-8')
webContent = response.read()

f = open('xxx.html', 'wb')
f.write(webContent)
f.close