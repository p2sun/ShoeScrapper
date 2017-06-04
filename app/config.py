import os
import logging
from scrapy.utils.log import configure_logging


""" SITEMAP is the URL to the sitemap of the site you want to crawl
    You should insert the link to the XML Sitemap within the string below
"""
SITEMAP = "INSERT THE SITEMAP LINK"

# This is your Project Root directory location
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

#configuring the logging system for scrapy
configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)

""" PROXY_POOL is a the list of proxies you want to use
    to submit all your HTTP requests for your crawls through.
    They should be string value following the format of
    either:
        http://some_proxy_server:port
        OR
        http://username:password@some_proxy_server:port
"""
PROXY_POOL = []

""" CSS_SELECTORS is a Dictionary of all the CSS selectors for the elements

    PRODUCT_WRAPPER  is the css selector for the HTML element that wraps the whole product listing
    PRODUCT_ID       is the css selector for the HTML element that contains the unique product ID
    TITLE            is the css selector for the HTML element that contains name of the product
    DESCRIPTION      is the css selector for the HTML element that contains the description of the product
    IMAGE_URL        is the css selector for the HTML element that contains the url of the product image
    SKU              is the css selector for the HTML element that contains the SKU of the product
    BRAND            is the css selector for the HTML element that contains the brand of the product
    URL              is the css selector for the HTML element that contains the link to the product's page
    NEXT_PAGE_BUTTON is the css selector for the HTML element that is the button/link to the next page

"""
CSS_SELECTORS = {
    'PRODUCT_WRAPPER':"",
    'PRODUCT_ID':"",
    'TITLE':"",
    'DESCRIPTION':"",
    'IMAGE_URL':"",
    'PRICE':"",
    'SKU':"",
    'BRAND':"",
    'URL':"",
    'NEXT_PAGE_BUTTON': "",
}

"""
    FEED_EXPORT_CONFIG is a dictionary that specifies where you want to send the feed
    You must specify the URI and format of the feed,
    if you decide to have a CSV output, uncomment the last entry and put the list of column names
    in the list
"""
FEED_EXPORT_CONFIG = {
    'FEED_URI':"", #FTP or s3 URI to where you want the feed to be exported to after
    'FEED_FORMAT':"", #csv, json or XML
    #'FEED_EXPORT_FIELDS' = [], #only if you decide to use CSV, specify the column titles
    #
}

def getLinks():
    """ Extract the URL Links of all the Scraped links from the sitemap
    :return: list of URL strings
    """
    curDIR = os.path.dirname(os.path.realpath(__file__))
    inputfile_path = os.path.join(curDIR, 'sitemaplinks.txt')
    links=[]
    with open(inputfile_path,'r') as outputfile:
        for line in outputfile:
            links.append(line.split(',')[0])
    return links
