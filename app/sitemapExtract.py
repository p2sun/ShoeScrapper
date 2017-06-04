import config as conf
import requests
from xml.etree import cElementTree as ET
import os

#initialize the output file
curDIR = os.path.dirname(os.path.realpath(__file__))
outputfile_path = os.path.join(curDIR, 'sitemaplinks.txt')

# extract links from the sitemap
sitemap = requests.get(url=conf.SITEMAP)

root = ET.fromstring(sitemap.content)

with open(outputfile_path,'w') as outputfile:
    for child in root:
        loc = child[0].text.encode('ascii', 'ignore')
        changefreq = child[1].text.encode('ascii', 'ignore')
        if loc.__contains__('Results'):
            outputfile.write(str.format('{},{}\n',loc,changefreq))



