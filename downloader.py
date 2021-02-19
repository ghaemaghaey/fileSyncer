#all imports
from requests import get
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from os.path import exists
from re import findall
from wget import filename_from_url

#origin base
#should filePath have a / in last charekter
filePath = 'C:/Users/ghaem/Desktop/fuck/'
url = 'http://127.0.0.1/ghaemdata/video/atack%20on%20titan/'
req = get(url)
soup = BeautifulSoup(req.content,'html.parser')
#get links from url
links = findall('href=\"(S.*.mkv)',str(soup))
for link in links:
    fileName = filename_from_url(url+link)
    #check file is exist
    if exists(filePath+fileName):
        print('Dowloaded')
    #after check start download 
    else:
        urlretrieve(url+link,filePath + fileName)
        print(fileName,'   Downloaded now')