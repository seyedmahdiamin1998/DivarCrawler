# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DivarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MashhadItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    category = scrapy.Field()
    model = scrapy.Field()
    vehicleTransmission = scrapy.Field()
    productionDate = scrapy.Field()
    mileageFromOdometer = scrapy.Field()
    knownVehicleDamages = scrapy.Field()
    priceCurrency = scrapy.Field()
    price = scrapy.Field()
    color = scrapy.Field()
    brand = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
