import scrapy
import app.config as config
import random

class ProductSpider(scrapy.Spider):
    name = "Product"

    def __init__(self, *args, **kwargs):
        super(ProductSpider, self).__init__(*args, **kwargs)
        self.proxy_pool = config.PROXY_POOL

    def start_requests(self):
        start_urls = config.getLinks()
        for link in start_urls:
            # randomly pick a proxy to send your request through
            proxy = random.choice(self.proxy_pool)
            meta = {'proxy' : proxy }
            yield  scrapy.Request(url=link, callback=self.parse, meta=meta)

    def parse(self,response):
        products = response.css(config.CSS_SELECTORS['PRODUCT_WRAPPER'])
        for product in products:

            #commented dictionary entries are optional, you can decide if you want them
            yield {
                'id': product.css(config.CSS_SELECTORS['PRODUCT_ID']).extract_first(),
                'availability': 'in stock',
                'description': product.css(config.CSS_SELECTORS['DESCRIPTION']).extract_first(),
                'price': product.css(config.CSS_SELECTORS['PRICE']).extract_first(),
                'image_link': product.css(config.CSS_SELECTORS['IMAGE_URL']).xpath('@src').extract_first(),
                'link': product.css(config.CSS_SELECTORS['URL']).extract_first(),
                #'brand': product.css(config.CSS_SELECTORS['BRAND']).extract_first(),
                'mpn': product.css(config.CSS_SELECTORS['SKU']).extract_first()
            }

        next_page = response.css(config.CSS_SELECTORS['NEXT_PAGE_BUTTON']).extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)



