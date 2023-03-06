import scrapy
from ..items import MashhadItem
import re
import json

class MashhadSpider(scrapy.Spider):
    name = "mashhad"
    allowed_domains = ["divar.ir"]
    start_urls = ["https://divar.ir/s/mashhad/auto"]

    def parse(self, response):

        items = response.css('div[class="post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46"]')
        for item in items:
            url = str(item.css("a::attr(href)").extract_first())
            yield scrapy.Request(url = 'https://'+self.allowed_domains[0]+url , callback = self.parse_detail)

        scripts = response.css('script::text').extract()
        for script in scripts:
            results = re.search(r'("last_post_sort_date":)\d*', script)
            if results:
                last_post_sort_date = re.split(":",results.group())[-1]

                my_data = { "json_schema":{
                                        "category":{"value":"cars"}, 
                                        "cities":["3"]
                                        },
                            "last-post-date":int(last_post_sort_date)}

                yield scrapy.Request( url='https://api.divar.ir/v8/web-search/3/cars',
                                method='POST',
                                body=json.dumps(my_data),
                                headers={'Content-Type':'application/json'},
                                callback = self.parse_scroll_data)

    
    
    def parse_scroll_data(self, response):
        '''
        scroll the page and get detail url of new items  
        '''
        json_data = json.loads(response.text)
        
        items = json_data['web_widgets']['post_list']

        last_post_sort_date = json_data['last_post_date']


        for item in items:
            token = item['data']['action']['payload']['token']
            web_info = item['data']['action']['payload']['web_info']

            title = web_info['title']
            title = title.replace(' ','-')
            category_slug_persian = web_info['category_slug_persian']
            category_slug_persian = category_slug_persian.replace(' ','-')
            city_persian = web_info['city_persian']
            city_persian = city_persian.replace(' ','-')
            district_persian = web_info['district_persian']
            district_persian = district_persian.replace(' ','-')
            url = 'https://divar.ir/v/'+title+'_'+category_slug_persian+'_'+city_persian+'_'+district_persian+'_'+'دیوار'+'/'+ token
            
            yield scrapy.Request(url = url , callback = self.parse_detail)
        
        my_data = {"json_schema":{
                                  "category":{"value":"cars"},
                                  "cities":["3"]
                                  },
                   "last-post-date":int(last_post_sort_date)}

        yield scrapy.Request(url='https://api.divar.ir/v8/web-search/3/cars',
                             method='POST',
                             body=json.dumps(my_data),
                             headers={'Content-Type':'application/json'},
                             callback = self.parse_scroll_data)


    def parse_detail(self, response):
        '''
        scrap data from item's detail page
        '''
        # info = {}
        info = MashhadItem()
        data = json.loads(response.css('script[type="application/ld+json"]::text').extract_first())
        for i in range(len(data)):
            if 'description' in data[i]:

                info['name'] = data[0]['name'] if 'name' in data[0] else 'null'
                info['category'] = data[0]['category'] if 'category' in data[0] else 'null'
                info['model'] = data[0]['model'] if 'model' in data[0] else 'null'
                info['vehicleTransmission'] = data[0]['vehicleTransmission'] if 'vehicleTransmission' in data[0] else 'null'
                info['productionDate'] = data[0]['productionDate'] if 'productionDate' in data[0] else 'null'
                info['mileageFromOdometer'] = data[0]['mileageFromOdometer']['value'] if 'mileageFromOdometer' in data[0] else -1
                info['knownVehicleDamages'] = data[0]['knownVehicleDamages'] if 'knownVehicleDamages' in data[0] else 'null'
                info['priceCurrency'] = data[0]['offers']['priceCurrency'] if 'offers' in data[0] else 'null'
                info['price'] = data[0]['offers']['price'] if 'offers' in data[0] else 'null'
                info['color'] = data[0]['color'] if 'color' in data[0] else 'null'
                info['brand'] = data[0]['brand']['name'] if 'brand' in data[0] else 'null'
                info['description'] = data[0]['description'] if 'description' in data[0] else 'null'
                info['url'] = data[0]['url'] if 'url' in data[0] else 'null'
                break
        
        yield info

# scrapy crawl mashhad -o a.json

