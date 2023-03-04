import scrapy
from scrapy.utils.response import open_in_browser


class MashhadSpider(scrapy.Spider):
    name = "mashhad01"
    allowed_domains = ["divar.ir"]
    start_urls = ["https://divar.ir/s/mashhad/auto"]

    def parse(self, response):
        open_in_browser(response)
        for item in response.css('.kt-post-card--has-action'):
            item = {
                'title' : item.css('.kt-post-card__title::text').extract_first(),
                'price' : item.css('.kt-post-card__description+ .kt-post-card__description::text').extract_first(),
                'description': item.css('.kt-post-card__title+ .kt-post-card__description::text').extract_first(),
                'location': item.css('.kt-text-truncate::text').extract_first()
            }
            yield item
        
